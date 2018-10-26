#-*- coding: utf-8 -*-
# Author: setsal Lan
import sys
import os
import sqlite3
import logging
conn = sqlite3.connect('../../../db.sqlite3') #連結指定的資料庫

# Main func
def main():
    conn.execute("DELETE FROM media_fetch_news");
    conn.execute("DELETE FROM media_fetch_company");
    conn.execute("delete from sqlite_sequence where name = 'media_fetch_news'");
    conn.execute("delete from sqlite_sequence where name = 'media_fetch_company'");
    conn.commit()

if __name__ == '__main__':
    main()
