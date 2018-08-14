# -*- coding: utf-8 -*-
# Author: setsal Lan

import logging
import sqlite3
import jieba
import gensim
from gensim import corpora, models, similarities
from gensim.similarities import Similarity
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('../jieba_dict/dict.txt.big.txt')

    # Load stopword
    stopword_set = set()
    with open('../jieba_dict/stop_words.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip())


    if ( os.path.exists("output/0814.dict") ):
        dictionary = corpora.Dictionary.load("output/0814.dict")
        corpus = corpora.MmCorpus("output/0814.mm")
        logging.info("Load model success")
    else:
        logging.info("Please run the train2.py to create dict & data flow")


    # Create tf-idf model
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    # Transfer to LSI model
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=40)
    corpus_lsi = lsi[corpus_tfidf] # LSI潛在語義索引
    lsi.save('output/0814.lsi')
    corpora.MmCorpus.serialize('output/0814_lsi.mm', corpus_lsi)

    """
    print("LSI topics:")
    results = lsi.print_topics(5)
    for result in results:
        print(result)
    """


    with open('input/test.txt', 'r', encoding='utf-8') as input:
        test_data_1 = input.read()
    vec_bow = dictionary.doc2bow(test_data_1.split())
    vec_lsi = lsi[vec_bow]
    #print(vec_lsi)

    print("\n輸入字串 or 文章:\n%s" % test_data_1 )


    # Create index
    index = similarities.MatrixSimilarity(lsi[corpus])
    index.save("output/0814.index")

    # Similarity
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])


    print("result:")
    print(sims[:5])

    # Print results
    conn = sqlite3.connect('../../db.sqlite3')


    articles = []
    for row in conn.execute('SELECT id, content FROM fb_fetch_article'):
        articles.append(row[1])


    for idx in sims[:3]:
        print("\n相似文章：",  articles[idx[0]])
        print("相似度：",  idx[1])


    """ old version
    similarity = Similarity('-Similarity-index', corpus, num_features=5000)

    with open('input/test.txt', 'r', encoding='utf-8') as input:
        test_data_1 = input.read()

    test_cut_raw_1 = jieba.lcut(test_data_1)
    test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
    similarity.num_best = 5
    print(similarity[test_corpus_1])
    """

if __name__ == "__main__":
	main()
