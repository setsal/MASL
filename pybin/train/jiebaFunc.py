# -*- coding: utf-8 -*-
# Author: setsal Lan

import jieba.analyse
import sqlite3
import re

stopword_path = "../jieba_dict/stop_words.txt"
jieba_dict_path = "../jieba_dict/dict.txt.big.txt"
jieba.analyse.set_stop_words("../jieba_dict/stop_words.txt")
stopWords = []

# initial stopword
def init_stopword():
    with open( stopword_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            stopWords.append(line)


# Get sql data
def getArticle(table_name):
    data = []
    conn = sqlite3.connect('../../db.sqlite3')
    r = u'[0-9ぁ-ゟ゠-ヿ’!＆"#$%&\'()*+,-.・▪．･˙｀／/:：´;<=＝>≧≦＞?↓➡@⚠🙏😂❤♥♡💕🌸▲😭※＊◎🔸🐢🦔🎉✨📢💦🎀🎊🤣😊∀▽⭐🌟☆✮▶■—－─～＿●•ωД๑，。ﾟ｡?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    for row in conn.execute('SELECT id, content FROM {}'.format(table_name)):
        temp = ''.join(row[1].strip('\n').split())
        temp = re.sub(r, '', temp)
        data.append(temp)
    return data

# Get sql data by cid
def getArticleByCid(cid):
    data = []
    conn = sqlite3.connect('../../db.sqlite3')
    for row in conn.execute('SELECT id, content FROM fb_fetch_article WHERE cid="{}";'.format(cid)):
        data.append(''.join(row[1].strip('\n').split()))
    return data


# Get the segments from jieba
def getSegment(data):
    jieba.set_dictionary(jieba_dict_path)
    seg_list = []
    for line in data:
        segments = jieba.lcut(line)
        remain_segments = list(filter(lambda a: a not in stopWords, segments))
        seg_list.append(remain_segments)
    return seg_list


def getSingleSegment(data):
    jieba.set_dictionary(jieba_dict_path)
    seg_list = []
    for line in data:
        segments = jieba.cut(line)
        remain_segments = list(filter(lambda a: a not in stopWords, segments))
        seg_list.extend(remain_segments)
    return seg_list


def getTestData(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(''.join(line.strip('\n').split()))
    f.close()
    return data


# Get single article keywords
def getSingleKeywords(data, n):
    keywords = []
    article = ' '.join(data)
    words = jieba.analyse.extract_tags( article, n )
    remain_words = list(filter(lambda a: a not in stopWords, words))
    keywords.extend(remain_words)
    #keywords.extend(words)
    return keywords
