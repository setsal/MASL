#-*- coding: utf-8 -*-
# Author: setsal Lan
import sys
import os
import sqlite3
import logging
conn = sqlite3.connect('../../db.sqlite3') #連結指定的資料庫

# Main func
def main():
    conn.execute("DELETE FROM fb_fetch_article");
    conn.execute("DELETE FROM fb_fetch_club");
    conn.execute("delete from sqlite_sequence where name = 'fb_fetch_club'");
    conn.execute("delete from sqlite_sequence where name = 'fb_fetch_article'");
    conn.commit()

if __name__ == '__main__':
    main()
