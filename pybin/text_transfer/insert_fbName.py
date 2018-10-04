#-*- coding: utf-8 -*-
# Author: setsal Lan
import sys
import os
import logging
import requests
import sqlite3
import datetime
import io
import json
from dotenv import find_dotenv,load_dotenv
conn = sqlite3.connect('../../db.sqlite3') #連結指定的資料庫
load_dotenv(find_dotenv())
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def create_club( fanpage_id, fanpage_name ):
    conn.execute("insert into fb_fetch_club ( cid, name, created_at ) values( ?, ?, ? )", ( fanpage_id, fanpage_name, datetime.datetime.now()) )
    conn.commit()


# Read file
def readfile(filename):
    fp = open( filename, "r", encoding="utf-8" )
    lines = fp.readlines()
    fp.close()

    for i in range( len(lines) ):
        fanpage_id = getNameID( lines[i] )
        fanpage_name = getFbName( fanpage_id )
        logging.info("嘗試新增 %s 粉專" % fanpage_name )
        create_club( fanpage_id, fanpage_name )


# Get Fanpage Link ID via findmyfbid.com
def getNameID(clublink):
    API_url = 'https://findmyfbid.com/'
    clublink = clublink.strip('\n')
    data = {
        'url': clublink
    }
    r = requests.post( API_url, data = data )
    data = r.json()

    return data['id']



# Get Fanpage Name via Graph API
def getFbName(id):
    token = os.getenv("FB_TOKEN")
    API_url = ('https://graph.facebook.com/v3.1/{}?fields=id,name&access_token={}'.format(id, token))
    parameter = ['name']
    r = requests.get( API_url )
    data = r.json()
    return data['name']


# Main func
def main():

    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)
    if len(sys.argv) < 2:
        logging.error("No argument")
        logging.info("Usage: $python fb_id.py [filename] [fb_token]")
        sys.exit()


    readfile(sys.argv[1])


if __name__ == '__main__':
    main()
