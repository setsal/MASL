
import sys
import sqlite3
conn = sqlite3.connect('../../db.sqlite3')  # 連結指定的資料庫

# it is only for create a table of Fan Page (column: name, id)
def create_database(table_name):
	#sql = 'create table if not exists ' + table_name + ' (id integer)'
	#conn.execute(sql)
	conn.execute("CREATE TABLE if not exists `{}` (\
		'name'	TEXT NOT NULL,\
		'id'	TEXT NOT NULL PRIMARY KEY \
	);".format(table_name))
	conn.commit()


def insert_data(table_name, fpName, fpId):
	conn.execute("insert into {} values('{}','{}');".format(table_name, fpName, fpId))
	conn.commit()

def printFileName(filename):
    print(filename)
def getFanpageInfofromTxt(filename):
    f = open(filename, 'r', encoding='utf8')
    fpName = f.readline()[:-1]  # Fanpage Name
    fpId = f.readline()[:-1]   # Fanpage Id
    f.close()
    return fpName, fpId

# Usage : myscript.py /my/folder/of/stuff/*.txt
# Example : python3 create.py *.txt
def main():
    table_name = "fb_club"

    # if u first use it ,uncomment this
    create_database(table_name)
    argc = len(sys.argv)
    if argc < 3:
        print("Usage : myscript.py /my/folder/of/stuff/*.txt")
        sys.exit()
    args = sys.argv[1:]
    for filename in args:
        printFileName(filename)
        fpName, fpId = getFanpageInfofromTxt(filename)
        insert_data(table_name, fpName, fpId)

if __name__ == '__main__':
  main()
