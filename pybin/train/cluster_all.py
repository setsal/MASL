# -*- coding: utf-8 -*-
# Author: setsal Lan
import logging
import sqlite3
import jieba
import numpy as np
import gensim
from gensim import corpora, models, similarities
import sys
import io
import os
import pickle

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def Month2Datetime(month):
    datefrom = ""
    dateto = ""

    if month == "Sep":
        datefrom = "\"2018-09-01\""
        dateto = "\"2018-09-31\""
    elif month == "Oct":
        datefrom = "\"2018-10-01\""
        dateto = "\"2018-10-30\""
    elif month == "Nov":
        datefrom = "\"2018-11-01\""
        dateto = "\"2018-11-31\""
    elif month == "Sep_e":
        datefrom = "\"2018-09-01\""
        dateto = "\"2018-09-15\""
    elif month == "Sep_l":
        datefrom = "\"2018-09-16\""
        dateto = "\"2018-09-30\""
    elif month == "Oct_e":
        datefrom = "\"2018-10-01\""
        dateto = "\"2018-10-15\""
    elif month == "Oct_l":
        datefrom = "\"2018-10-16\""
        dateto = "\"2018-10-30\""
    elif month == "Nov_e":
        datefrom = "\"2018-11-01\""
        dateto = "\"2018-11-15\""

    dictname = "news_" + month + ".dict"
    mmname = "news_" + month + ".mm"
    tfidfname = "news_" + month + ".tfidf"
    ldaname = "news_" + month + ".lda"

    return datefrom, dateto, dictname, mmname, tfidfname, ldaname


def my_absmax(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored in their second element.
        if abs(item[1]) > abs(maximum[1]):
            maximum = item

    return maximum



def getFbCluster():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    mmname = "fb" + ".mm"
    tfidfname = "fb" + ".tfidf"
    ldaname = "fb" + ".lda"
    idname = "fb" + ".train_id"
    modelUrl = "pybin/train/output/"

    corpus = corpora.MmCorpus( modelUrl + mmname )
    tfidf = models.TfidfModel.load( modelUrl + tfidfname )
    lda = models.LdaModel.load( modelUrl + ldaname )

    corpus_tfidf = tfidf[corpus]
    corpus_lda = lda[corpus_tfidf]
    num_topic = lda.num_topics


    # Load id list after filter
    with open( modelUrl + idname, "rb") as fp:
        train_id = pickle.load(fp)


    # Get nearest topic for each article
    topic_list = []
    index = 0
    for doc in corpus_lda:
        topic_list.append(my_absmax(doc))

    # ======= topic of articles ========
    # Connect to db and print the article by id
    conn = sqlite3.connect('db.sqlite3')
    articles = []
    titles = []
    clubs_id = []
    createtime = []
    for row in conn.execute('SELECT fb_fetch_article.id, fb_fetch_article.content, fb_fetch_club.name, fb_fetch_club.id, fb_fetch_article.created_at \
                             FROM fb_fetch_article \
                             INNER JOIN fb_fetch_club \
                             ON fb_fetch_club.cid = fb_fetch_article.cid'):
        articles.append(row[1])
        titles.append(row[2])
        clubs_id.append(row[3])
        createtime.append(row[4])

    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
         topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])

    data = []
    topic = {}
    keyword_of_topic = []

    for i in range(num_topic):
        n_topic = "Topic" + str(i)

        contents = []
        idx = 0
        for id in topic_list_sort_by_topic[i]:
            if ( topic_list[id][1] < 0.5 ):
                continue
            if idx > 10:
                break
            single_post = {
                'title': titles[train_id[id]],
                'content': articles[train_id[id]],
                'clubs_id': clubs_id[train_id[id]],
                'timestamp': createtime[train_id[id]],
                'similarities': round(float(topic_list[id][1]), 2)
            }
            contents.append(single_post)
            idx = idx + 1


        key_list = lda.show_topic(i, topn=10)
        temp = []
        for tup in key_list:
            temp2 = {
                'value': tup[0],
                'count': round(tup[1]*100)*6
            }
            temp.append(temp2)
        keyword_of_topic.append(temp)

        topic = {
            'kind': n_topic,
            'keyword_of_topic': keyword_of_topic[i],
            'articles': contents
        }
        data.append(topic)

    return(data)


def getNewsCluster():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    mmname = "news_Sep" + ".mm"
    tfidfname = "news_Sep" + ".tfidf"
    ldaname = "news_Sep" + ".lda"
    modelUrl = "pybin/train/output/"

    corpus = corpora.MmCorpus( modelUrl + mmname )
    tfidf = models.TfidfModel.load( modelUrl + tfidfname )
    lda = models.LdaModel.load( modelUrl + ldaname )

    corpus_tfidf = tfidf[corpus]
    corpus_lda = lda[corpus_tfidf]
    num_topic = lda.num_topics

    # Get nearest topic for each article
    topic_list = []
    index = 0
    for doc in corpus_lda:
        topic_list.append(my_absmax(doc))

    # ======= topic of articles ========
    # Connect to db and print the article by id
    conn = sqlite3.connect('db.sqlite3')
    articles = []
    titles = []
    companys = []
    companys_id = []
    categories = []
    createtime = []
    for row in conn.execute('SELECT media_fetch_news.id, media_fetch_news.category, media_fetch_news.title, media_fetch_news.content, media_fetch_news.mid_id, media_fetch_company.name, media_fetch_news.created_at FROM media_fetch_news INNER JOIN media_fetch_company ON media_fetch_news.mid_id = media_fetch_company.id WHERE media_fetch_news.created_at >= "2018-09-01" and media_fetch_news.created_at <= "2018-09-30";'):
        categories.append(row[1])
        titles.append(row[2])
        articles.append(row[3])
        companys_id.append(row[4])
        companys.append(row[5])
        createtime.append(row[6])

    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
        topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])


    data = []
    topic = {}
    keyword_of_topic = []

    for i in range(num_topic):
        n_topic = "Topic" + str(i)


        contents = []
        idx = 0
        for id in topic_list_sort_by_topic[i]:
            if ( topic_list[id][1] < 0.75 ):
                continue
            if idx > 50:
                break
            single_post = {
                'category': categories[id],
                'title': titles[id],
                'content': articles[id],
                'description': articles[id][:130] + "....",
                'company_id': companys_id[id],
                'company': companys[id],
                'timestamp': createtime[id],
                'similarities': round(float(topic_list[id][1]), 2)
            }
            contents.append(single_post)
            idx = idx + 1

        key_list = lda.show_topic(i, topn=10)
        temp = []
        for tup in key_list:
            temp2 = {
                'value': tup[0],
                'count': round(tup[1]*1000)*3
            }
            temp.append(temp2)

        keyword_of_topic.append(temp)

        topic = {
            'kind': n_topic,
            'keyword_of_topic': keyword_of_topic[i],
            'articles': contents
        }
        data.append(topic)

    return(data)


def getFbCustomizeCluster(n_article, datefrom, dateto):
    logging.info(datefrom)
    logging.info(dateto)
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    mmname = "fb_customize" + ".mm"
    tfidfname = "fb_customize" + ".tfidf"
    ldaname = "fb_customize" + ".lda"
    idname = "fb_customize" + ".train_id"
    modelUrl = "pybin/train/output/"

    corpus = corpora.MmCorpus( modelUrl + mmname )
    tfidf = models.TfidfModel.load( modelUrl + tfidfname )
    lda = models.LdaModel.load( modelUrl + ldaname )

    corpus_tfidf = tfidf[corpus]
    corpus_lda = lda[corpus_tfidf]
    num_topic = lda.num_topics

    # Load id list after filter
    with open( modelUrl + idname, "rb") as fp:
        train_id = pickle.load(fp)

    # Get nearest topic for each article
    topic_list = []
    index = 0
    for doc in corpus_lda:
        topic_list.append(my_absmax(doc))

    # Connect to db and print the article by id
    conn = sqlite3.connect('db.sqlite3')
    articles = []
    titles = []
    clubs_id = []
    createtime = []
    for row in conn.execute('SELECT fb_fetch_article.id, fb_fetch_article.content, fb_fetch_club.name, fb_fetch_club.id, fb_fetch_article.created_at \
                             FROM fb_fetch_article \
                             INNER JOIN fb_fetch_club \
                             ON fb_fetch_club.cid = fb_fetch_article.cid \
                             WHERE fb_fetch_article.created_at >= {} and fb_fetch_article.created_at <= {}'.format(datefrom, dateto)):
        articles.append(row[1])
        titles.append(row[2])
        clubs_id.append(row[3])
        createtime.append(row[4])
    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
         topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])


    data = []
    topic = {}
    keyword_of_topic = []

    for i in range(num_topic):
        n_topic = "Topic" + str(i)

        contents = []
        idx = 0
        for id in topic_list_sort_by_topic[i]:
            if idx > n_article:
                break
            single_post = {
                'title': titles[train_id[id]],
                'content': articles[train_id[id]],
                'clubs_id': clubs_id[train_id[id]],
                'timestamp': createtime[train_id[id]],
                'similarities': round(float(topic_list[id][1]), 2)
            }
            contents.append(single_post)
            idx = idx + 1


        key_list = lda.show_topic(i, topn=10)
        temp = []
        for tup in key_list:
            temp2 = {
                'value': tup[0],
                'count': round(tup[1]*100)*6
            }
            temp.append(temp2)
        keyword_of_topic.append(temp)

        topic = {
            'kind': n_topic,
            'keyword_of_topic': keyword_of_topic[i],
            'articles': contents
        }
        data.append(topic)

    return(data)


def getNewsCustomizeCluster(n_article, month):

    # Load static variable
    datefrom, dateto, dictname, mmname, tfidfname, ldaname = Month2Datetime(month)
    modelUrl = "pybin/train/output/"

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    corpus = corpora.MmCorpus( modelUrl + mmname )
    tfidf = models.TfidfModel.load( modelUrl + tfidfname )
    lda = models.LdaModel.load( modelUrl + ldaname )

    corpus_tfidf = tfidf[corpus]
    corpus_lda = lda[corpus_tfidf]
    num_topic = lda.num_topics

    # Get nearest topic for each article
    topic_list = []
    index = 0
    for doc in corpus_lda:
        topic_list.append(my_absmax(doc))

    # Connect to db and print the article by id
    conn = sqlite3.connect('db.sqlite3')
    articles = []
    titles = []
    companys = []
    companys_id = []
    categories = []
    createtime = []
    for row in conn.execute('SELECT media_fetch_news.id, media_fetch_news.category, media_fetch_news.title, media_fetch_news.content, media_fetch_news.mid_id, media_fetch_company.name, media_fetch_news.created_at  \
                             FROM media_fetch_news \
                             INNER JOIN media_fetch_company ON media_fetch_news.mid_id = media_fetch_company.id \
                             WHERE media_fetch_news.created_at >= {} and media_fetch_news.created_at <= {}'.format(datefrom, dateto)):

        categories.append(row[1])
        titles.append(row[2])
        articles.append(row[3])
        companys_id.append(row[4])
        companys.append(row[5])
        createtime.append(row[6])

    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
         topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])


    data = []
    topic = {}
    keyword_of_topic = []


    for i in range(num_topic):
        n_topic = "Topic" + str(i)


        contents = []
        idx = 0
        for id in topic_list_sort_by_topic[i]:
            if topic_list[id][1] < 0.75:
                continue
            if idx > n_article:
                break
            single_post = {
                'category': categories[id],
                'title': titles[id],
                'content': articles[id],
                'description': articles[id][:30],
                'company_id': companys_id[id],
                'company': companys[id],
                'timestamp': createtime[id],
                'similarities': round(float(topic_list[id][1]), 2)
            }
            contents.append(single_post)
            idx = idx + 1

        key_list = lda.show_topic(i, topn=10)
        temp = []
        for tup in key_list:
            temp2 = {
                'value': tup[0],
                'count': round(tup[1]*1000)*3
            }
            temp.append(temp2)

        keyword_of_topic.append(temp)

        topic = {
            'kind': n_topic,
            'keyword_of_topic': keyword_of_topic[i],
            'articles': contents
        }
        data.append(topic)

    return(data)



def getFbGraph():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    mmname = "fb" + ".mm"
    tfidfname = "fb" + ".tfidf"
    ldaname = "fb" + ".lda"
    idname = "fb" + ".train_id"
    modelUrl = "pybin/train/output/"

    corpus = corpora.MmCorpus( modelUrl + mmname )
    tfidf = models.TfidfModel.load( modelUrl + tfidfname )
    lda = models.LdaModel.load( modelUrl + ldaname )

    corpus_tfidf = tfidf[corpus]
    corpus_lda = lda[corpus_tfidf]
    num_topic = lda.num_topics


    # Load id list after filter
    with open( modelUrl + idname, "rb") as fp:
        train_id = pickle.load(fp)

    # Get nearest topic for each article
    topic_list = []
    index = 0
    for doc in corpus_lda:
        topic_list.append(my_absmax(doc))

    # ======= topic of articles ========
    # Connect to db and print the article by id
    conn = sqlite3.connect('db.sqlite3')
    articles = []
    titles = []
    clubs_id = []
    createtime = []
    for row in conn.execute('SELECT fb_fetch_article.id, fb_fetch_article.content, fb_fetch_club.name, fb_fetch_club.id, fb_fetch_article.created_at \
                             FROM fb_fetch_article \
                             INNER JOIN fb_fetch_club \
                             ON fb_fetch_club.cid = fb_fetch_article.cid'):
        articles.append(row[1])
        titles.append(row[2])
        clubs_id.append(row[3])
        createtime.append(row[4])

    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
         topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])


    data = {}
    nodes_list = []
    links_list = []

    nodes_list_topic = []
    nodes_link_topic = []

    keyword_of_topic = []

    default_node = {
        'id': 'Facebook',
        'svg': 'https://en.facebookbrand.com/wp-content/uploads/2016/05/flogo_rgb_hex-brc-site-250.png',
        'size': 400,
        'fontSize': 18
    }

    nodes_list.append(default_node)

    for i in range(num_topic):

        topic_node = {
            'id': "主題" + str(i),
            'symbolType': 'circle',
            'color': 'blue',
            'size': 300
        }
        topic_link = {
            'source': 'Facebook',
            'target': "主題" + str(i)
        }
        nodes_list.append(topic_node)
        links_list.append(topic_link)

        idx = 0
        for id in topic_list_sort_by_topic[i]:
            if idx > 20:
                break
            single_post = {
                'id': clubs_id[train_id[id]],
                'name': titles[train_id[id]],
                'symbolType': 'circle',
                'size': 400,
            }
            link = {
                'source': "主題" + str(i),
                'target': clubs_id[train_id[id]]
            }
            nodes_list_topic.append(single_post)
            nodes_link_topic.append(link)
            idx = idx + 1


    test_list = list({v['id']:v for v in nodes_list_topic}.values())
    # data.append(topic)
    nodes_list.extend(test_list)
    test_list = list({v['target']:v for v in nodes_link_topic}.values())
    links_list.extend(test_list)

    data = {
        'links': links_list,
        # [{
        #     'source': 'Facebook',
        #     'target': "主題1"
        #  },
        #  {
        #      'source': 'Facebook',
        #      'target': "主題2"
        #   },
        #  ],
        'nodes': nodes_list
    }

    return(data)


#if __name__ == "__main__":
    #cluster = getCluster()
    #print(cluster)
