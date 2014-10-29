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
######==========================文章的操作=============================
#获取所有文章
def getAllArticle():
    articles = db.select('entries',order = "id DESC")
    return articles
#获取一篇文章
def getArticleById(id):
    try:
        article = db.select('entries',where="id=$id",vars=locals())[0]
    except:
        print "获取文章%s失败"%(id)
    return article
#新建文章
def createArticle(title,content,userId):
    try:
        db.insert(
                  'entries',
                  title=title,
                  content=content,
                  posted_on=datetime.datetime.utcnow(),
                  belongId=userId
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
                  where='id=$id',
                  vars=locals(),
                  title=title,
                  content=content
                  )
    except:
        print "修改%s文章失败"%(id)
 ######==========================用户的操作============================= 
 #根据用户名获取密码
def getPwdByName(userName):
    user = db.select('user',where='username=$userName',order="id DESC",vars=locals())
    reslist = []
    for u in user:
        reslist.append(u)
    return reslist
#增加用户
def addUser(userName,pwd):
    try:
        db.insert('user',
                  username=userName,
                  pwd=pwd)
    except:
        print "添加用户失败!"
#根据id修改账号密码
def updateuser(id,username='',pwd=''):
    if(username!='' and pwd !=''):
        db.update('entries',where="id=$id",vars=locals(),pwd=pwd,username=username) 
def deleteUserById(id):
    db.delete('entries',where="id=$id",vars=locals())      
if __name__=='__main__':
    addUser("zhangtao","123456")
 
 
 
       
    