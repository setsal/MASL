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
import json

conn = sqlite3.connect('../../../db.sqlite3') #連結指定的資料庫
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# insert company to sql
def insert_company( name ):
    cursor = conn.execute('select id from media_fetch_company where name = ?', ( name,) )
    value = cursor.fetchone()

    if not value:
        # Create new company
        cursor = conn.execute("insert into media_fetch_company ( name, created_at ) values( ?, ? )", ( name, datetime.datetime.now()) )
        conn.commit()
        mid = cursor.lastrowid
    else:
        mid = value[0]

    return(mid)


# insert news to sql
def insert_news( category, title, content, url, datetime, mid  ):
    conn.execute("insert into media_fetch_news ( category, title, content, url, mid_id, created_at ) values( ?, ?, ?, ?, ?, ? )", ( category, title, content, url, mid, datetime ) )
    conn.commit()


# Read file
def readfile(filename):
    with open( filename, "r", encoding="utf-8" ) as f:
        data = json.load(f)

    mid = insert_company(data[1]['website'])

    for i in range( 1 ):
        category = data[i]['category'].strip()
        title = data[i]['title'].strip()
        content = data[i]['content'].strip()
        url = data[i]['url'].strip()
        datetime = data[i]['date'].strip()


        if not title or not content or len(content)<20:
            continue
        logging.info("Try to add %d mid company %d news", mid, i )
        insert_news( category, title, content, url, datetime, mid )



# Main func
def main():

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("No argument, support validate json")
        logging.info("Usage: $python news_tranfer.py [filename]")
        logging.info("Btw, *.json also work.")
        sys.exit()

    for filename in sys.argv[1:]:
        readfile(filename)


if __name__ == '__main__':
    main()
