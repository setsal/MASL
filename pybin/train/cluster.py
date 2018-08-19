import logging
import sqlite3
import jieba
import gensim
from gensim import corpora, models, similarities
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def my_absmax(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored
        # in their second element.
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
        logging.info("Please run the train2.py to create dict & data flow")

    # Create tf-idf model
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    # Transfer to LSI model
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=5)
    corpus_lsi = lsi[corpus_tfidf]

    for doc in corpus_lsi:
        print(my_absmax(doc))

if __name__ == "__main__":
	main()
