# -*- coding: utf-8 -*-
# Author: setsal Lan

#from gensim.models import word2vec
#from gensim import models
import logging
import sqlite3
import jieba
conn = sqlite3.connect('../../db.sqlite3')

def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('../jieba_dict/dict.txt.big.txt')

    # load stopwords set
    stopword_set = set()
    with open('../jieba_dict/stop_words.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))

    output = open('output/fb_article_seg.txt', 'w', encoding='utf-8')

    for row in conn.execute('SELECT id, content FROM fb_fetch_article'):
        content = row[1].strip('\n').split()
        for line in content:
            seg_list = jieba.cut(line)
            output.write(' '.join(seg_list) )
        output.write("\n")

    output.close()

if __name__ == "__main__":
	main()
