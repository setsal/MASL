#-*- coding: utf-8 -*-
# Author: setsal Lan
import sys
import numpy
import os
import sqlite3
import datetime
import time
import logging
import io

conn = sqlite3.connect('../../db.sqlite3') #連結指定的資料庫

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# insert to sql
def insert_data( title, contents ):
    conn.execute("insert into fb_fetch_article ( cid, textid, content, created_at ) values( ?, ?, ?, ? )", ( "unknown", title, contents, datetime.datetime.now()) )
    conn.commit()

# Read file
def readfile(filename):
    fp = open( filename, "r", encoding="utf-8" )
    lines = fp.readlines()
    fp.close()

    cnt = 0
    # generate array list

    title = ''
    for i in range( len(lines) ):
        content = ''
        if i%5 == 2:
            title = lines[i][3:]
        if i%5 == 4:
            cnt = cnt + 1
            news = lines[i].lstrip()
            if not news:
                continue
            start = news.find('報導') + 3
            content = news[start:]

            # add to sql
            logging.info("嘗試新增第 %d 篇新聞" % cnt )
            #print(title)
            #print(content)
            insert_data( title, content )



# Main func
def main():

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("No argument")
        logging.info("Usage: $python news_tranfer.py [filename]")
        logging.info("Btw, *.txt also work.")
        sys.exit()

    for filename in sys.argv[1:]:
        readfile(filename)


if __name__ == '__main__':
    main()
