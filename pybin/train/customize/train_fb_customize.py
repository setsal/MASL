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
from .jiebaFunc import init_stopword, getArticle, getSegment


def train(keywords, num_topic):
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)
    init_stopword()
    article_lists = getArticle("fb_fetch_article")
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

    return
