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
import pickle
from jiebaFunc import init_stopword, getArticle, getSegment, getArticleByTime


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    logging.basicConfig(
        format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("No argument")
        logging.info("Usage: $python train_ff.py [activity]")
        logging.info("FF31~32 CWT48 49 PF26~28, etc.")
        sys.exit()


    datefrom = ""
    dateto = ""

    if sys.argv[1] == "FF31":
        datefrom = "\"2017-12-01\""
        dateto = "\"2018-04-14\""
    elif sys.argv[1] == "FF32":
        datefrom = "\"2018-04-15\""
        dateto = "\"2018-11-11\""

    elif sys.argv[1] == "CWT49":
        datefrom = "\"2018-04-01\""
        dateto = "\"2018-08-20\""
    elif sys.argv[1] == "CWT48":
        datefrom = "\"2017-12-15\""
        dateto = "\"2018-03-31\""


    elif sys.argv[1] == "PF26":
        datefrom = "\"2016-11-15\""
        dateto = "\"2017-04-29\""
    elif sys.argv[1] == "PF27":
        datefrom = "\"2017-04-30\""
        dateto = "\"2018-10-30\""
    elif sys.argv[1] == "PF28":
        datefrom = "\"2017-10-31\""
        dateto = "\"2018-05-28\""
    

    init_stopword()
    article_lists = getArticleByTime("fb_fetch_article", datefrom, dateto)
    #article_lists = getArticle("fb_fetch_article")
    seg_list = getSegment(article_lists)

    #print(seg_list)
    #'FGO','fgo','少女前線','白貓','寫真','cosplay','東方','演唱會','百合','艦娘','血小板','碧藍','偶像','音樂'

    train_list = []
    train_id = []
    idx = 0
    for doc in seg_list:
        for word in doc:
            if word in ['PF','FF','FGO', 'fgo', 'Fate', '少女前線', '白貓', '寫真', 'cosplay', 'cos', '東方', '演唱會', '百合', '艦娘', '血小板', '碧藍', '音樂', '工作細胞']:
                train_list.append(doc)
                train_id.append(idx)
                break
        idx += 1

    #print("-----????---\n",train_list)
    #print(train_id)

    filt_list = [[y for y in x if y in ['PF', 'FF', 'FGO', 'fgo', 'Fate', '少女前線', '白貓', '寫真', 'cosplay',
                                        'cos', '東方', '演唱會', '百合', '艦娘', '血小板', '碧藍', '音樂', '工作細胞']] for x in train_list]
    #print("-----????---\n",filt_list)

    with open("output/fb_train_id", "wb") as fp:
       pickle.dump(train_id, fp)

    n = 20

    # 移除只出現n次的字詞
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in filt_list:
        for token in text:
            frequency[token] += 1

    """
    sorted_frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for word in sorted_frequency:
        if word[1] >= 30:
            print(word[0]+":"+str(word[1]))
    """

    texts = [[token for token in text if frequency[token] >= n]
             for text in filt_list]

    # Create dictionary
    dictionary = corpora.Dictionary(texts)
    dictionary.compactify()
    dictionary.save("output/fb_"+sys.argv[1]+".dict")
    logging.info("Create dict success.")

    # Serialize it
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize("output/fb_"+sys.argv[1]+".mm", corpus)
    logging.info("Create data flow success.")

    tfidf = models.TfidfModel(corpus)
    tfidf.save("output/fb_"+sys.argv[1]+".tfidf")
    corpus_tfidf = tfidf[corpus]
    logging.info("Create TF-IDF model success.")

    num_topic = 9

    # Transfer to LSI model
    lda = models.LdaModel(corpus, id2word=dictionary,
                          num_topics=num_topic, iterations=100, passes=20)
    lda.save("output/fb_"+sys.argv[1]+".lda")
    logging.info("Create LDA model success.")

    for i in range(lda.num_topics):
        print(lda.print_topic(i))
        print('\n')

    """
    keyword_of_topic = []
    for i in range(lda.num_topics):
        key_list = lda.show_topic(i, topn=10)
        temp = []
        for tup in key_list:
            temp.append(tup[0])
        keyword_of_topic.append(temp)
    
    print(keyword_of_topic)
    """


if __name__ == "__main__":
	main()
