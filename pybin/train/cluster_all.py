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
        datefrom = "\"2018-01-01\""
        dateto = "\"2018-01-31\""
    elif month == "Sep_e":
        datefrom = "\"2018-09-01\""
        dateto = "\"2018-09-31\""
    elif month == "Oct":
        datefrom = "\"2018-10-01\""
        dateto = "\"2018-10-31\""
    elif month == "Nov":
        datefrom = "\"2018-11-01\""
        dateto = "\"2018-11-31\""
    elif month == "Nov_e":
        datefrom = "\"2018-11-01\""
        dateto = "\"2018-11-15\""

    return datefrom, dateto


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

    if ( os.path.exists("pybin/train/output/fb.dict") ):
        dictionary = corpora.Dictionary.load("pybin/train/output/fb.dict")
        corpus = corpora.MmCorpus("pybin/train/output/fb.mm")
        logging.info("Load model success")
    else:
        logging.info("Please run the train2.py to create models")

    # Load tf-idf model
    tfidf = models.TfidfModel.load("pybin/train/output/fb.tfidf")
    corpus_tfidf = tfidf[corpus]


    num_topic = 9

    # Load to LDA model
    lda = models.LdaModel.load("pybin/train/output/fb.lda")
    corpus_lda = lda[corpus]

    num_topic = lda.num_topics

    # Load id list after filter
    with open("pybin/train/output/train_id", "rb") as fp:
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
    for row in conn.execute('SELECT fb_fetch_article.id, fb_fetch_article.content, fb_fetch_club.name, fb_fetch_club.id FROM fb_fetch_article INNER JOIN fb_fetch_club ON fb_fetch_club.cid = fb_fetch_article.cid'):
        articles.append(row[1])
        titles.append(row[2])
        clubs_id.append(row[3])

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
            if idx > 20:
                break
            single_post = {
                'title': titles[train_id[id]],
                'content': articles[train_id[id]],
                'clubs_id': clubs_id[train_id[id]]
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

    if ( os.path.exists("pybin/train/output/news_sep.dict") ):
        dictionary = corpora.Dictionary.load("pybin/train/output/news_sep.dict")
        corpus = corpora.MmCorpus("pybin/train/output/news_sep.mm")
        logging.info("Load model success")
    else:
        logging.info("Please run the train2.py to create models")

    # Load tf-idf model
    tfidf = models.TfidfModel.load("pybin/train/output/news_sep.tfidf")
    corpus_tfidf = tfidf[corpus]

    num_topic = 6

    # Load to LDA model
    lda = models.LdaModel.load("pybin/train/output/news_sep.lda")
    corpus_lda = lda[corpus]

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
    for row in conn.execute('SELECT media_fetch_news.id, media_fetch_news.category, media_fetch_news.title, media_fetch_news.content, media_fetch_news.mid_id, media_fetch_company.name FROM media_fetch_news INNER JOIN media_fetch_company ON media_fetch_news.mid_id = media_fetch_company.id WHERE media_fetch_news.created_at >= "2018-09-01" and media_fetch_news.created_at <= "2018-09-30";'):
        categories.append(row[1])
        titles.append(row[2])
        articles.append(row[3])
        companys_id.append(row[4])
        companys.append(row[5])

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
            if idx > 50:
                break
            single_post = {
                'category': categories[id],
                'title': titles[id],
                'content': articles[id],
                'company_id': companys_id[id],
                'company': companys[id]
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


def getFbCustomizeCluster(n_article):

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)
    if ( os.path.exists("pybin/train/output/fb.dict") ):
        dictionary = corpora.Dictionary.load("pybin/train/output/fb.dict")
        corpus = corpora.MmCorpus("pybin/train/output/fb.mm")
        logging.info("Load model success")
    else:
        logging.info("Please run the train2.py to create models")

    # Load tf-idf model
    tfidf = models.TfidfModel.load("pybin/train/output/fb.tfidf")
    corpus_tfidf = tfidf[corpus]


    num_topic = 6

    # Load to LDA model
    lda = models.LdaModel.load("pybin/train/output/fb.lda")
    corpus_lda = lda[corpus_tfidf]

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
    for row in conn.execute('SELECT fb_fetch_article.id, fb_fetch_article.content, fb_fetch_club.name, fb_fetch_club.id FROM fb_fetch_article INNER JOIN fb_fetch_club ON fb_fetch_club.cid = fb_fetch_article.cid'):
        articles.append(row[1])
        titles.append(row[2])
        clubs_id.append(row[3])

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
                'title': titles[id],
                'content': articles[id],
                'clubs_id': clubs_id[id]
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
    datefrom, dateto = Month2Datetime(month)
    # return month, datetime, dateto
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    dictionary = corpora.Dictionary.load("pybin/train/output/news_" + month+ ".dict")
    corpus = corpora.MmCorpus("pybin/train/output/news_" + month+ ".mm")

    # Load tf-idf model
    tfidf = models.TfidfModel.load("pybin/train/output/news_" + month+ ".tfidf")
    corpus_tfidf = tfidf[corpus]


    # Load to LDA model
    lda = models.LdaModel.load("pybin/train/output/news_" + month+ ".lda")
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
    logging.info('% % ', datefrom, dateto)
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
            # if topic_list[id][1] < 0.85:
            #     idx = idx + 1
            #     continue
            if idx > n_article:
                break
            single_post = {
                'category': categories[id],
                'title': titles[id],
                'content': articles[id],
                'company_id': companys_id[id],
                'company': companys[id],
                'timestamp': createtime[id]
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


#if __name__ == "__main__":
    #cluster = getCluster()
    #print(cluster)
