#-*- coding: utf-8 -*-
# Author: setsal Lan

import requests
import json
import sys
import os
import io
import sqlite3
import logging
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
### Our FB access token ###
bot_token = os.getenv('FB_TOKEN')

conn = sqlite3.connect('../../db.sqlite3')  # 連結指定的資料庫
cur = conn.cursor()


def set_parameter(fanpage_id):
	tmp_url = ('https://graph.facebook.com/v3.2/{}/picture?redirect=0&type=large&access_token={}'.format(fanpage_id, bot_token))
	return tmp_url



def main():

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    cursor = conn.execute('select * from fb_fetch_club;')

    for row in cursor:
        if( row[0] < 224 ):
            continue;
        url = set_parameter(row[1])
        logging.info("Try to fetch id:%d fanpage pic url" % row[0])
        r = requests.get( set_parameter(row[1]) )
        data = r.json()
        print(data['data']['url'])



if __name__ == '__main__':
    main()
