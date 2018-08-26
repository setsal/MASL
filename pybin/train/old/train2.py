# -*- coding: utf-8 -*-
# Author: setsal Lan

#from gensim.models import word2vec
#from gensim import models
import logging
import sqlite3
import jieba
import gensim
from gensim import corpora
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
conn = sqlite3.connect('../../db.sqlite3')
seg_list = []

def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('../jieba_dict/dict.txt.big.txt')

    # Load stopword
    stopword_set = set()
    with open('../jieba_dict/stop_words.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip())


    # Load Data
    for row in conn.execute('SELECT id, content FROM fb_fetch_article'):
        content = row[1].strip('\n').split()
        print(''.join(content))
        #item_str = jieba.lcut(''.join(content))
        #print(item_str)
        #seg_list.append(item_str)


    #
    # # Create dictionary
    # dictionary = corpora.Dictionary(seg_list)
    #
    #
    # # Remove stop words
    # stop_ids = [dictionary.token2id[stopword] for stopword in stopword_set
    #             if stopword in dictionary.token2id]
    # dictionary.filter_tokens(stop_ids)
    # dictionary.compactify()
    #
    # # Create dict & list dict word & id
    # dictionary.save("output/0814.dict")
    # logging.info("Create dict success.")
    #
    # """
    # for word,index in dictionary.token2id.items():
    #     print(word +" id:"+ str(index))
    # """
    #
    # # 移除只出現一次的字詞
    # from collections import defaultdict
    # frequency = defaultdict(int)
    # for text in seg_list:
    #     for token in text:
    #         frequency[token] += 1
    #
    # texts = [[token for token in text if frequency[token] > 1]
    #          for text in seg_list]
    #
    #
    # # Serialize it
    # corpus = [dictionary.doc2bow(text) for text in texts]
    # corpora.MmCorpus.serialize("output/0814.mm", corpus)
    # logging.info("Create data flow success.")



if __name__ == "__main__":
	main()
