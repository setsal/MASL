#-*- coding: utf-8 -*-
# Author: setsal Lan
import sys
import numpy
import os
import sqlite3
import datetime
import time
import logging
conn = sqlite3.connect('../../db.sqlite3') #連結指定的資料庫



def create_club( fanpage_id, fanpage_name ):
    conn.execute("insert into fb_fetch_club ( cid, name, created_at ) values( ?, ?, ? )", ( fanpage_id, fanpage_name, datetime.datetime.now()) )
    conn.commit()


# insert to sql
def insert_data( fanpage_id, text_id, contents ):
    for i in range(text_id):
        data = ''.join(contents[i])

        # Remove too less article
        if ( len(data) <= 10 ):
            continue;

        tid = "{:05d}".format(i)
        conn.execute("insert into fb_fetch_article ( cid, textid, content, created_at ) values( ?, ?, ?, ? )", ( fanpage_id, tid, data, datetime.datetime.now()) )
        conn.commit()


# Read file
def readfile(filename):
    fp = open( filename, "r", encoding="utf-8" )
    lines = fp.readlines()
    fp.close()

    fanpage_name = lines[0].strip("\n")
    fanpage_id = lines[1].strip("\n")

    content = [[]for i in range(10) ]
    idx = 0

    # generate array list
    for i in range( len(lines) ):
        if ( i == 0 or i == 1 ):
            continue

        if( lines[i] == '\n' ):
            idx+=1

        if ( idx > 9 ):
            logging.error("Error in %s textfile" % fanpage_name )
            logging.error("The text file is out of range, check if it is valid")
            sys.exit()

        content[idx].append(lines[i])

    # add to sql
    logging.info("嘗試新增 %s 粉專內容" % fanpage_name )

    #Create club index
    create_club( fanpage_id, fanpage_name )
    insert_data( fanpage_id, idx, content )



# Main func
def main():

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("No argument")
        logging.info("Usage: $python tranfer.py [filename1] [filename2] [filename3]")
        logging.info("Btw, *.txt also work.")
        sys.exit()

    for filename in sys.argv[1:]:
        readfile(filename)


if __name__ == '__main__':
    main()
