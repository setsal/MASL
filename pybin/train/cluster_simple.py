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
sys.path.append('../fb_fetch')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def my_absmax(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored in their second element.
        if abs(item[1]) > abs(maximum[1]):
            maximum = item

    return maximum



def getCluster():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if ( os.path.exists("pybin/train/output/0814.dict") ):
        dictionary = corpora.Dictionary.load("pybin/train/output/0814.dict")
        corpus = corpora.MmCorpus("pybin/train/output/0814.mm")
        logging.info("Load model success")
    else:
        logging.info("Please run the train2.py to create models")

    # Load tf-idf model
    tfidf = models.TfidfModel.load("pybin/train/output/1011.tfidf")
    corpus_tfidf = tfidf[corpus]


    num_topic = 7

    # Load to LDA model
    lda = models.LdaModel.load("pybin/train/output/1011.lda")
    corpus_lda = lda[corpus_tfidf]

    # Get nearest topic for each article
    topic_list = []
    index = 0
    for doc in corpus_lda:
        topic_list.append(my_absmax(doc))

    # ======= topic of articles ========
    # Connect to db and print the article by id
    conn = sqlite3.connect('db.sqlite3')
    articles = []
    for row in conn.execute('SELECT id, content FROM fb_fetch_article'):
        articles.append(row[1])

    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
        topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])


    data = []
    topic = {}


    for i in range(num_topic):
        n_topic = "Topic" + str(i)


        contents = []
        idx = 0
        for id in topic_list_sort_by_topic[i]:
            if idx > 20:
                break
            single_post = {
                'title': 'unknown',
                'content': articles[id][:30]
            }
            contents.append(single_post)
            idx = idx + 1

        topic = {
            'kind': n_topic,
            'articles': contents
        }
        data.append(topic)

    return(data)



# if __name__ == "__main__":
# 	main()
