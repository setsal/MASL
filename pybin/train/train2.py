# -*- coding: utf-8 -*-
# Author: setsal Lan

#from gensim.models import word2vec
#from gensim import models
import logging
import jieba
import gensim
from gensim import corpora
import sys
import io
from jiebaFunc import init_stopword, getArticle, getSegment


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    init_stopword()
    article_lists = getArticle()
    seg_list = getSegment(article_lists)

    #print(seg_list)


    # Create dictionary
    #dictionary = corpora.Dictionary(seg_list)


    # Remove stop words
    # stop_ids = [dictionary.token2id[stopword] for stopword in stopword_set
    #             if stopword in dictionary.token2id]
    # dictionary.filter_tokens(stop_ids)
    #dictionary.compactify()

    # Create dict & list dict word & id
    #dictionary.save("output/0814.dict")
    #logging.info("Create dict success.")

    """
    for word,index in dictionary.token2id.items():
        print(word +" id:"+ str(index))
    """

    n = 30

    # 移除只出現n次的字詞
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in seg_list:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > n]
             for text in seg_list]

    # Create dictionary
    dictionary = corpora.Dictionary(texts)
    dictionary.compactify()
    dictionary.save("output/0814.dict")
    logging.info("Create dict success.")

    print(dictionary.token2id)


    # Serialize it
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize("output/0814.mm", corpus)
    logging.info("Create data flow success.")



if __name__ == "__main__":
	main()
