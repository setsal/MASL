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

function : count_num_of_cid( table_name , cid )
return   : integer, the number of cid's article count.

'''
# =============================



# =========  CODE  ============

def cid_to_cname(table_name, cid):
	cursor = conn.execute(
		'select name from {} WHERE cid="{}";'.format(table_name, cid))
	return cursor.fetchone()[0]

# test it !
#print(cid_to_cname("fb_fetch_club", 120909948018734))


def count_num_of_row(table_name):
	cursor = conn.execute(
		'select count() from {} ;'.format(table_name))
	return cursor.fetchone()[0]

# test it !
# print(tecount_num_of_rowst("fb_fetch_club"))

def count_num_of_cid(table_name, cid):
	cursor = conn.execute(
		'select count("cid") from {} WHERE cid="{}";'.format(table_name, cid))
	return cursor.fetchone()[0]

# test it !
# print(120909948018734," 's article number is: ", count_num_of_cid("fb_fetch_article", 120909948018734))

# Just backup.
def disp_content():
	cursor = conn.execute('select * from fb_fetch_article;')
	for row in cursor:
		print("Content : {}\n".format(row[3]))
