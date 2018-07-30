#-*- coding: utf-8 -*-
# Author: setsal Lan
import sqlite3
import datetime
import time
conn = sqlite3.connect('db.sqlite3') #連結指定的資料庫


def insert_data( fanpage_id, text_id, content ):
    print( len(content) )
