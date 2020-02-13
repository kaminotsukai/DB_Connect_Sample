# encoding: utf8
import shutil
import glob
import os
import json
import pymysql.cursors
import re
import unicodedata
import sys
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

conn = pymysql.connect(host="DB_HOST",
                    user="DB_USERNAME",
                    password="DB_PASSWORD",
                    db="DB_DATABASE",
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)



def insert_db():
    try:
        with conn.cursor() as cursor:
            sql = ''
            cursor.execute(sql)
            conn.commit()
            
    except Exceptopn as e:
        print(e)
        conn.close()

    finally:
        conn.close()


if __name__ == '__main__':
    insert_db()