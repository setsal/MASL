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

    num_topic = 3

    # Transfer to LSI model
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic)
    corpus_lsi = lsi[corpus_tfidf]

    # Get nearest topic for each article
    topic_list = []
    for doc in corpus_lsi:
        #print(my_absmax(doc))
        topic_list.append(my_absmax(doc))
    
    # Sort by topic
    topic_list_sort_by_topic = []
    for i in range(num_topic):
        topic_list_sort_by_topic.append([x for x, y in enumerate(topic_list) if y[0] == i])
    #print(topic_list_sort_by_topic)

    # Connect to db and print the article by id
    conn = sqlite3.connect('../../db.sqlite3')
    articles = []
    for row in conn.execute('SELECT id, content FROM fb_fetch_article'):
        articles.append(row[1])
    
    for i in range(num_topic)):
        print("*********************************************************************")
        print("Topic" + str(i + 1) + ":")
        for id in topic_list_sort_by_topic[i]:
            print(articles[id])
    

if __name__ == "__main__":
	main()
