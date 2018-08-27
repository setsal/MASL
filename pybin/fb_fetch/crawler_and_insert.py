import sqlite3
import datetime
import time
import sys
import io
from gettweepy import *

conn = sqlite3.connect('../../db.sqlite3')  # 連結指定的資料庫
cur = conn.cursor()

def disp_data():
	cursor = conn.execute('select * from club_list;')
	for row in cursor:
		print("Name : {}, id : {}\n".format(row[1],row[0]))

def disp_content():
	cursor = conn.execute('select * from fb_fetch_article;')
	for row in cursor:
		print("Content : {}\n".format(row[3]))

def insert_data(table_name,input_arr):
	for post in input_arr:
		print(post,"\n\n")
		if 'message' in post.keys():
			conn.execute("insert into fb_fetch (  textid, content ) values('{}','{}');".format( post['id'], post['message']) )
			conn.commit()

def setsal_insert_data( fanpage_id, table_name, input_arr ):
	for post in input_arr:
		#print(post,"\n\n")
		if 'message' in post.keys():
			conn.execute("insert into fb_fetch_article (  uid, textid, content, created_at ) values( '{}', '{}', '{}', '{}');".format( fanpage_id, post['id'], post['message'], datetime.datetime.now()) )
			conn.commit()
def tweet_insert( table_name ):
	#conn.execute('SELECT count(*) FROM {}'.format( table_name ))
	print(getUserId())
	input_arr = from_public_to_dict(getUserId(), getPT())
	for post in input_arr:
		conn.execute("insert into fb_fetch_article (  cid, textid, content, created_at ) values( '{}', '{}', '{}', '{}');".format(
			post['cid'], post['text_id'], post['content'], post['created_at']))
		conn.commit()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
#disp_content()
tweet_insert("fb_fetch_article")
