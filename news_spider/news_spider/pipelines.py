
from itemadapter import ItemAdapter
import sqlite3
import psycopg2
import requests
class NewsSpiderPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=psycopg2.connect(
        host="localhost",
        database="news_data",
        user="postgres",
        password="1234")
        print("connect sucess")
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS read""")
        self.curr.execute("""DROP TABLE IF EXISTS politics""")
        self.curr.execute("""DROP TABLE IF EXISTS sports""")
        self.curr.execute("""DROP TABLE IF EXISTS entertainment""")
        self.curr.execute("""DROP TABLE IF EXISTS business""")
        self.curr.execute("""create table business(head text,news text,img text)""")
        self.curr.execute("""create table entertainment(head text,news text,img text)""")
        self.curr.execute("""create table sports(head text,news text,img text)""")
        self.curr.execute("""create table read(head text,news text,img text)""")
        self.curr.execute("""create table politics(head text,news text,img text)""")

    def process_item(self, item, spider):
        x=item['url']
        tname=x[x.rfind('/')+1:]
        self.store_db(item,tname)
        return item
    def store_db(self,item,tname):
       
        self.curr.execute(
                """insert into """ + tname+ """(head,news,img) values (%s, %s, %s)""",
                    (item['head'], item['news'],item['img']))

        self.conn.commit()
        print("data commit")
        # self.curr.close()
        # self.conn.close()
    

