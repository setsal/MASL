# -*- coding: utf-8 -*-
# Author: setsal Lan

import logging
import jieba
import gensim
from gensim import corpora, models
import sys
import io
import operator
import pickle
from .jiebaFunc import init_stopword, getArticleByTime, getSegment


def Exhibition2Datetime(exhibition):
    datefrom = ""
    dateto = ""

    if exhibition == "FF31":
        datefrom = "\"2017-12-01\""
        dateto = "\"2018-04-14\""
    elif exhibition == "FF32":
        datefrom = "\"2018-04-15\""
        dateto = "\"2018-11-11\""

    elif exhibition == "CWT49":
        datefrom = "\"2018-04-01\""
        dateto = "\"2018-08-20\""
    elif exhibition == "CWT48":
        datefrom = "\"2017-12-15\""
        dateto = "\"2018-03-31\""


    elif exhibition == "PF26":
        datefrom = "\"2016-11-15\""
        dateto = "\"2017-04-29\""
    elif exhibition == "PF27":
        datefrom = "\"2017-04-30\""
        dateto = "\"2018-10-30\""
    elif exhibition == "PF28":
        datefrom = "\"2017-10-31\""
        dateto = "\"2018-05-28\""


    return datefrom, dateto


def train(keywords, num_topic, exhibition):
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)
    init_stopword()

    datefrom, dateto = Exhibition2Datetime(exhibition)

    article_lists = getArticleByTime("fb_fetch_article", datefrom, dateto)
    seg_list = getSegment(article_lists)


    train_list = []
    train_id = []
    idx = 0
    for doc in seg_list:
        for word in doc:
            if word in keywords:
                train_list.append(doc)
                train_id.append(idx)
                break
        idx += 1

    filt_list = [[y for y in x if y in keywords] for x in train_list]

    with open("pybin/train/output/fb_customize.train_id", "wb") as fp:
       pickle.dump(train_id, fp)

    n = 20

    # 移除只出現n次的字詞
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in filt_list:
        for token in text:
            frequency[token] += 1


    texts = [[token for token in text if frequency[token] >= n]
             for text in filt_list]

    # Create dictionary
    dictionary = corpora.Dictionary(texts)
    dictionary.compactify()
    dictionary.save("pybin/train/output/fb_customize.dict")
    logging.info("Create dict success.")

    # Serialize it
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize("pybin/train/output/fb_customize.mm", corpus)
    logging.info("Create data flow success.")


    tfidf = models.TfidfModel(corpus)
    tfidf.save("pybin/train/output/fb_customize.tfidf")
    corpus_tfidf = tfidf[corpus]
    logging.info("Create TF-IDF model success.")

    # Transfer to LSI model
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topic, iterations=100, passes=20)
    lda.save("pybin/train/output/fb_customize.lda")
    logging.info("Create LDA model success.")


    for i in range(lda.num_topics):
        print(lda.print_topic(i))
        print('\n')

    return datefrom, dateto
