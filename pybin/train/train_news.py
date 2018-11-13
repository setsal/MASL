# -*- coding: utf-8 -*-
# Author: setsal Lan

#from gensim.models import word2vec
#from gensim import models
import logging
import jieba
import gensim
from gensim import corpora, models
import sys
import io
import operator
from jiebaFunc import init_stopword, getArticle, getSegment, getArticleByTime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("No argument")
        logging.info("Usage: $python train_news.py [month]")
        logging.info("Jan for January, Feb for February, etc.")
        sys.exit()

    datefrom = ""
    dateto = ""
    
    if sys.argv[1] == "Jan":
        datefrom = "\"2018-01-01\""
        dateto = "\"2018-01-31\""
    elif sys.argv[1] == "Feb":
        datefrom = "\"2018-02-01\""
        dateto = "\"2018-02-31\""
    elif sys.argv[1] == "Mar":
        datefrom = "\"2018-03-01\""
        dateto = "\"2018-03-31\""
    elif sys.argv[1] == "Apr":
        datefrom = "\"2018-04-01\""
        dateto = "\"2018-04-31\""
    elif sys.argv[1] == "May":
        datefrom = "\"2018-05-01\""
        dateto = "\"2018-05-31\""
    elif sys.argv[1] == "Jun":
        datefrom = "\"2018-06-01\""
        dateto = "\"2018-06-31\""
    elif sys.argv[1] == "Jul":
        datefrom = "\"2018-07-01\""
        dateto = "\"2018-07-31\""
    elif sys.argv[1] == "Aug":
        datefrom = "\"2018-08-01\""
        dateto = "\"2018-08-31\""
    elif sys.argv[1] == "Sep":
        datefrom = "\"2018-09-01\""
        dateto = "\"2018-09-31\""
    elif sys.argv[1] == "Oct":
        datefrom = "\"2018-10-01\""
        dateto = "\"2018-10-31\""
    elif sys.argv[1] == "Nov":
        datefrom = "\"2018-11-01\""
        dateto = "\"2018-11-31\""
    elif sys.argv[1] == "Dec":
        datefrom = "\"2018-12-01\""
        dateto = "\"2018-12-31\""


    init_stopword()
    article_lists = getArticleByTime("media_fetch_news", datefrom, dateto)
    if not article_lists:
        logging.error("No news data in the month, please choose another")
        sys.exit()
    
    seg_list = getSegment(article_lists)

    minn = 30
    maxn = 200

    # 移除只出現n次的字詞
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in seg_list:
        for token in text:
            frequency[token] += 1

    """
    sorted_frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

    for word in sorted_frequency:
        if word[1] > 30 and word[1] < 200:
            print(word[0]+":"+str(word[1]))
    """

    texts = [[token for token in text if frequency[token] > minn and frequency[token] < maxn]
             for text in seg_list]

    dictname = "news_" + sys.argv[1] + ".dict"
    mmname = "news_" + sys.argv[1] + ".mm"
    tfidfname = "news_" + sys.argv[1] + ".tfidf"
    ldaname = "news_" + sys.argv[1] + ".lda" 

    # Create dictionary
    dictionary = corpora.Dictionary(texts)
    dictionary.compactify()
    dictionary.save("output/" + dictname)
    logging.info("Create dict success.")


    # Serialize it
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize("output/" + mmname, corpus)
    logging.info("Create data flow success.")

    
    tfidf = models.TfidfModel(corpus)
    tfidf.save("output/" + tfidfname)
    corpus_tfidf = tfidf[corpus]
    logging.info("Create TF-IDF model success.")

    num_topic = 6

    # Transfer to LSI model
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topic, iterations=100, passes=20)
    lda.save("output/" + ldaname)
    logging.info("Create LDA model success.")

    for i in range(lda.num_topics):
        print(lda.print_topic(i))
        print('\n')
    

if __name__ == "__main__":
	main()
