import sqlite3
import datetime
import time
conn = sqlite3.connect('db.sqlite3') #連結指定的資料庫

def disp_data():
	cursor = conn.execute('select * from club_list;')
	for row in cursor:
		print("Name : {}, id : {}\n".format(row[1],row[0],row[2]))

def insert_data(table_name,input_arr):
	for post in input_arr:
		print(post,"\n\n")
		if 'message' in post.keys():
			conn.execute("insert into fb_fetch (  textid, content ) values('{}','{}');".format( post['id'], post['message']) )
			conn.commit()


def setsal_insert_data( fanpage_id, table_name, input_arr ):
	i = 2;
	for post in input_arr:
		#print(post,"\n\n")
		if 'message' in post.keys():
			conn.execute("insert into fb_fetch_article (  uid, textid, content, created_at ) values( '{}', '{}', '{}', '{}');".format( fanpage_id, post['id'], post['message'], datetime.datetime.now()) )
			conn.commit()
		i = i+1
