# -*- coding: utf-8 -*-
# Author: setsal Lan

import logging
import jieba
import gensim
from gensim import corpora, models, similarities
from gensim.similarities import Similarity
import sys
import io
import os
from jiebaFunc import init_stopword, getArticle, getSegment, getTestData, getSingleSegment

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

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

    # test_data = ''
    # with open('input/test.txt', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         words = jieba.cut(line)
    #         test_data += ' '.join(words)
    #
    # print(test_data.split())

    test_data = []
    init_stopword()
    test_data = getTestData('input/test.txt')
    test_data_seg = getSingleSegment(test_data)

    vec_bow = dictionary.doc2bow(test_data_seg)
    vec_lsi = lsi[vec_bow]

    print("\nAriticle:\n%s" % test_data )


    # Create index
    index = similarities.MatrixSimilarity(lsi[corpus])
    index.save("output/0814.index")

    # Similarity
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])


    print("result:")
    print(sims[:5])

    # Print results
    articles = getArticle()
    for idx in sims[:3]:
        print("\nSimilar Ariticle：\n",  articles[idx[0]])
        print("\nSimilarity：",  idx[1])


if __name__ == "__main__":
	main()
