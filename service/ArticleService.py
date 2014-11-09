#_*_ coding:utf-8 _*_


import datetime

import web


######==========================文章的操作=============================
db = web.database(dbn = 'mysql', db = 'blog', user = 'root', 
                  pw = 'root',port =3306,host='127.0.0.1')
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
                  userId=userId
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
if __name__ == '__main__':
    print getAllArticle()[0]