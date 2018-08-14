# -*- coding: utf-8 -*-
# Author: setsal Lan

#from gensim.models import word2vec
#from gensim import models
import logging
import sqlite3
import jieba
import gensim
from gensim import corpora
from gensim.similarities import Similarity
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
        #print(type(content))
        item_str = jieba.lcut(''.join(content))
        seg_list.append(item_str)

    # Create dictionary
    dictionary = corpora.Dictionary(seg_list)

    # Remove stop words
    stop_ids = [dictionary.token2id[stopword] for stopword in stopword_set
        if stopword in dictionary.token2id]
    dictionary.filter_tokens(stop_ids)
    dictionary.compactify()

    # Create dict & list dict word & id
    dictionary.save("output/0814.dict")
    logging.info("Create dict success.")
    """
    for word,index in dictionary.token2id.items():
        print(word +" id:"+ str(index))
    """

    # Serialize it
    corpus = [dictionary.doc2bow(text) for text in seg_list]
    corpora.MmCorpus.serialize("output/0814.mm", corpus)
    logging.info("Create data flow success.")

    """
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
