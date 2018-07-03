# -*- coding: utf-8 -*-
import jieba
import sqlite3
import datetime
import time
#import str



conn = sqlite3.connect('db.sqlite3') #連結指定的資料庫
jieba.set_dictionary("./pybin/nlp/dict.txt.big.txt")

def setsal_insert_data():
    seg_list = jieba.cut("這是一份自然語言處理展示用的程式")
    sep_content = (", ".join(seg_list).encode('utf-8'))
    #sep_content = join(seg_list).encode('utf-8')
	#conn.execute("insert into fb_fetch_article ( uid, textid, content, created_at ) values ( '1', '1', '{}', '{}');".format( sep_content, datetime.datetime.now()))
    conn.execute("insert into fb_fetch_article ( uid, textid, content, created_at ) values( '1', '1', '{}', '{}');".format( sep_content, datetime.datetime.now() ))
    conn.commit()


setsal_insert_data()
