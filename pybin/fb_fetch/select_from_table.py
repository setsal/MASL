import sqlite3
import sys
import io

conn = sqlite3.connect('../../db.sqlite3')  # 連結指定的資料庫
cur = conn.cursor()

# ========= WARNING ===========
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# ========= WARNING ===========

# ========= Interface =========
'''
import select_from_table

function : cid_to_name( table_name , cid )
return   : string, Just a char_arr.

function : count_num_of_row( table_name )
return   : integer, the number of row.

'''
# =============================



# =========  CODE  ============

def cid_to_cname(table_name, cid):
	cursor = conn.execute('select name from {} WHERE cid="{}";'.format(table_name, cid))
	return cursor.fetchone()[0]

# test it !
#print(cid_to_cname("fb_fetch_club", 120909948018734))


def count_num_of_row(table_name):
	cursor = conn.execute(
		'select count() from {} ;'.format(table_name))
	return cursor.fetchone()[0]

# test it !
# print(tecount_num_of_rowst("fb_fetch_club"))

# Just backup.
def disp_content():
	cursor = conn.execute('select * from fb_fetch_article;')
	for row in cursor:
		print("Content : {}\n".format(row[3]))
