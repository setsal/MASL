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
from jiebaFunc import init_stopword, getArticle, getSegment


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    init_stopword()
    article_lists = getArticle("media_fetch_news")
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

    # Create dictionary
    dictionary = corpora.Dictionary(texts)
    dictionary.compactify()
    dictionary.save("output/news.dict")
    logging.info("Create dict success.")


    # Serialize it
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize("output/news.mm", corpus)
    logging.info("Create data flow success.")

    
    tfidf = models.TfidfModel(corpus)
    tfidf.save("output/news.tfidf")
    corpus_tfidf = tfidf[corpus]
    logging.info("Create TF-IDF model success.")

    num_topic = 6

    # Transfer to LSI model
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topic, iterations=100, passes=20)
    lda.save("output/news.lda")
    logging.info("Create LDA model success.")

    for i in range(lda.num_topics):
        print(lda.print_topic(i))
        print('\n')
    

if __name__ == "__main__":
	main()
