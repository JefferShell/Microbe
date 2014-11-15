#_*_ coding:utf-8 _*_
import web
import datetime
import sys

sys.path.append('./service')
from web import form
from setting import urls,  getGlobals
from ArticleService import *
from UserService import *
web.config.debug=False
app = web.application(urls,globals()) 
#设置静态文件的目录
web.template.Template.globals['static'] = '/static'
render = web.template.render('templates',globals=getGlobals(web))
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'id': 0})  
tempInfo = {}
class mainPage():
    def GET(self):
#         print session.id
#         print 'MainPage'
        articles = getAllArticle()
        return render.MainPage(articles,session.id)
# class Page404:
#     def GET(self,name):
#         print "404"
#         errorStr = name,"页面没找到，请处理"
#         return render.Page404(name)
class login:
    def GET(self):
        if str(session.id) != "0":
            articles = getAllArticle()
            return render.MainPage(articles,session.id)
        else:
            return render.LoginPage("")
    def POST(self):
        postdata=web.input()
        username=web.net.websafe(postdata.username)
        password=web.net.websafe(postdata.password)
        user=getPwdByName(username)
        if username=="":
            return render.LoginPage(u"账号密码不能为空！")
        if len(user)==0:
            errorInfo = u"对不起,%s没有找到!"%(username)
            return render.LoginPage(errorInfo)
        else:
            if password==user["pwd"]:  
#                 print session.id             
#                 print user,"userId"             
                session.id=int(user["userId"])
                raise web.seeother("/")
            else:
                return render.LoginPage(u"密码错误！！！")
class logout():
    def GET(self):
        session.kill()
        raise web.seeother("/")
class addArticle():
    def GET(self,id=''):
        print id
        user=getUserById(session.id)
        return render.AddArticle(user);
    def POST(self):
        data = web.input()
        title = web.net.websafe(data.title);
        content = web.net.websafe(data.content);
        if title=="" or content=="":
            raise web.seeother("/addArticle/"+id)
        else:
            createArticle(title,content,session.id)
        raise web.seeother("/")
class modifyArticle():
#     print "22111"
    def GET(self,id=''):
        if session.id !=0 and id!="":
            article = getArticleById(id)
            return render.ModifyArticle(article)
        else:
            raise web.seeother("/")
    def POST(self,name):
        print "name=",name
        data = web.input()
        title = web.net.websafe(data.title);
        content = web.net.websafe(data.content);
        id = web.net.websafe(data.id)
        if title=="" or content=="":
            raise web.seeother("/modifyArticle/"+id)
        else:
            updateArticle(id,title,content)
        raise web.seeother("/")
class deleteArticle():
    def GET(self,id):
        print id
        if session.id !=0 and id!="":
            deleteArticleById(id)
            raise web.seeother("/")
        else:
            raise web.seeother("/")
        
class articleDetail():
    def GET(self,blogId):
        print "blogId=",blogId
        if blogId=="" :
            raise web.seeother("/")
        if blogId:
            article = getArticleById(blogId)
            article.contents = article.content.split("\n")
            print article.contents
            if not str(article).strip():
                raise web.seeother("/")
            else:
                return render.DetailArticl(article)
        return render.DetailArticl(article)
class personal():
    def GET(self,userId=""):
        if userId!="":
            user = getUserById(userId)
        return render.Personal(user)
if __name__ == '__main__':
    app.run()