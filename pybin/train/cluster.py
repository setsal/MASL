import logging
import sqlite3
import jieba
import numpy as np
import gensim
from gensim import corpora, models, similarities
import sys
import io
import os
sys.path.append('../fb_fetch')
from select_from_table import cid_to_cname
from jiebaFunc import getArticleByCid, getSingleKeywords, init_stopword

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def my_absmax(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored in their second element.
        if abs(item[1]) > abs(maximum[1]):
            maximum = item

    return maximum[0]

def my_absmax_for_test(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored in their second element.
        if abs(item[1]) > abs(maximum[1]):
            maximum = item

    return maximum


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if ( os.path.exists("output/0814.dict") ):
        dictionary = corpora.Dictionary.load("output/0814.dict")
        corpus = corpora.MmCorpus("output/0814.mm")
        logging.info("Load model success")
    else:
        logging.info("Please run the train2.py to create models")

    # Load tf-idf model
    tfidf = models.TfidfModel.load("output/1011.tfidf")
    corpus_tfidf = tfidf[corpus]

    # Load to LDA model
    lda = models.LdaModel.load("output/1011.lda")
    corpus_lda = lda[corpus_tfidf]

    # Get nearest topic for each article
    topic_list = []
    topic_list_test = []
    index = 0
    for doc in corpus_lda:
        #print(str(index) + ':' + str(my_absmax(doc)))
        #index = index + 1
        #print(doc)
        topic_list.append(my_absmax(doc))
        topic_list_test.append(my_absmax_for_test(doc))
    #print('==================================')

    """
    # ======= topic of clubs =======
    # Connect to db and print the article by id
    conn = sqlite3.connect('../../db.sqlite3')

    cid_list = []
    for row in conn.execute('select min(cast(id as INT)), max(cast(id as INT)), cid from fb_fetch_article GROUP BY cid'):
        cid_list.append(row)

    topic_cid = [[None for col in range(0)] for row in range(num_topic)]
    for row in cid_list:
        start = int(row[0]) - 1
        end = int(row[1])
        #print(str(start) + ',' + str(end))
        #print(row[2] + ':' + str(topic_list[start:end]))
        num = max(topic_list[start:end], key=topic_list[start:end].count)
        #print(cid_to_cname('fb_fetch_club', row[2]) + ':' + 'Topic' + str(num + 1))
        #print('\n')
        topic_cid[num].append(row[2])

    for n in range(num_topic):
        print('Topic' + str(n) + ':')
        for cid in topic_cid[n]:
            print(cid_to_cname('fb_fetch_club', cid))
        print('\n')

    
    for i in range(0, lda.num_topics):
        print(lda.print_topic(i))

    # ==============================
    """
    
    # ======= topic of articles ========
    # Connect to db and print the article by id
    conn = sqlite3.connect('../../db.sqlite3')
    articles = []
    for row in conn.execute('SELECT id, content FROM fb_fetch_article'):
        articles.append(row[1])

    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(lda.num_topics):
        topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list_test) if y[0] == i])
    #print(topic_list_sort_by_topic)
    
    
    for i in range(lda.num_topics):
        print("*********************************************************************")
        print("Topic" + str(i) + ":")
        count = 0 
        for id in topic_list_sort_by_topic[i]:
            print(articles[id])
            count += 1
            if count > 20:
                break
        print("\n\n")
    

    for i in range(lda.num_topics):
        print(lda.print_topic(i))
        print("\n")
    
    # =================================
    
    

if __name__ == "__main__":
	main()
