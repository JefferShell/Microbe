#_*_ coding:utf-8 _*_
import os
import datetime
import web
# 数据库配置
MYSQL_DBN = 'mysql'
MYSQL_DB = 'test'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306

db=web.database(dbn=MYSQL_DBN, 
    db=MYSQL_DB, 
    user=MYSQL_USER,
    host=MYSQL_HOST,
    pw=MYSQL_PASS,
    port=MYSQL_PORT)
#获取所有文章
def getAllArticle():
    articles = db.select('entries',order = "id DESC")
    return articles
#获取一篇文章
def getArticleById():
    try:
        db.select('entries',where="id=$id",vars=locals())[0]
    except:
        print "获取文章%s失败"%(id)
#新建文章
def createArticle(title,content):
    try:
        db.insert(
                  'entries',
                  title=title,
                  content=content,
                  posted_on=datetime.datetime.utcnow()
                  )
    except:
        print "文章插入失败!",title,content
#删除文章
def deleteArticle(id):
    try:
        db.delete('entries',where = 'id=$id',vars = locals())
    except:
        print "删除%s失败"%(id)
#修改文章 
def updateArticle(id,title,content):
    try:
        db.update(
                  'entries',
                  where='id=%id',
                  vars=locals(),
                  title=title,
                  content=content
                  )
    except:
        print "修改%s文章失败"%(id)
        
    