#-*- coding: utf-8 -*-
# Author: setsal Lan
import sys
import numpy
import os
import sqlite3
import datetime
import time
conn = sqlite3.connect('../../db.sqlite3') #連結指定的資料庫


# insert to sql
def insert_data( fanpage_id, text_id, contents ):
    for content in contents:
        data = ''.join(content)
        conn.execute("insert into fb_fetch_article ( cid, textid, content, created_at ) values( '{}', '{}', '{}', '{}');".format( fanpage_id, text_id, data, datetime.datetime.now() ))
        conn.commit()


# Read file
def readfile(filename):
    fp = open( filename, "r", encoding="utf-8" )
    lines = fp.readlines()
    fp.close()

    fanpage_name = lines[0]
    fanpage_id = lines[1]

    content = [[]for i in range(10) ]
    idx = 0

    # generate array list
    for i in range( len(lines) ):
        if ( i == 0 or i == 1 ):
            continue

        if( lines[i] == '\n' ):
            idx+=1

        content[idx].append(lines[i])

    # add to sql
    insert_data( fanpage_id, 0, content )


# Main func
def main():
    if len(sys.argv) < 2:
        print("Info: No argument")
        print("Usage: $python tranfer.py [filename1] [filename2] [filename3]")
        sys.exit()

    for filename in sys.argv[1:]:
        readfile(filename)



main()
