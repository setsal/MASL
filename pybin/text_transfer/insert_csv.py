import logging
import sys
import io
import csv
import sqlite3
import datetime

conn = sqlite3.connect('../../db.sqlite3')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# Main func
def main():

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    with open('news.csv', 'r', encoding='utf8') as f:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(f)
        to_db = [(i['serialNo'], i['deptName'], i['stitle']) for i in dr]  

    to_db.pop(0)
    
    for row in to_db:
        conn.execute("insert into fb_fetch_article ( cid, textid, content, created_at ) values( ?, ?, ?, ? )", ( row[0], row[1], row[2], datetime.datetime.now()) )
        conn.commit()
    
    
if __name__ == '__main__':
    main()