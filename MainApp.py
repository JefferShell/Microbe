#_*_ coding:utf-8 _*_
import web
import datetime
import sys
sys.path.append('./service')
from web import form
from setting import urls,  getGlobals
from ArticleService import *
web.config.debug=False
app = web.application(urls,globals()) 
#设置静态文件的目录
web.template.Template.globals['static'] = '/static'
render = web.template.render('templates',globals=getGlobals(web))
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'id': 0,'status': 0})  
tempInfo = {}
class MainPage():
    def GET(self):
        print session.id
        print session.status
        ord=1
        print 'MainPage'
        articles = getAllArticle()
        return render.MainPage(articles,session.status,ord)
class Page404:
    def GET(self,name):
        print "404"
        errorStr = name,"页面没找到，请处理"
        return render.Page404(name)
class Login:
    loginForm=form.Form(form.Textbox('username',description=u'用户名'),
                        form.Password("password",description=u"密码"),
                        form.Button(u"马上登陆", type="submit", description="submit"),)
    def GET(self):
        if logged():
            return 'you are logged'
        else:
            return render.LoginPage(self.loginForm)
    def POST(self):
        postdata=web.input()
        username=web.net.websafe(postdata.username)
        password=web.net.websafe(postdata.password)
#         rslist=getUserByUserName(username)
        rslist=['123546']
        if username=="":
            return render.LoginPage(self.loginForm,u"账号密码不能为空！")
        if len(rslist)==0:
            errorInfo = u"对不起,%s没有找到!"%(username)
            return render.LoginPage(self.loginForm,errorInfo)
        else:
            if password==rslist[0].pwd:                
                session.count=1
                #session.login222=1
#                 return  '登陆成功,欢迎你:'+username+':'+str(session.login)
#                 return render.MainPage(tempInfo)
                raise web.seeother("/",tempInfo)
            else:
                return render.LoginPage(self.loginForm,u"密码错误！！！")
class Logout():
    def GET(self):
        session.kill()
        raise web.seeother("/", tempInfo)
#
def logged():
    if session.count == 1:
        return True
    else:
        return False
if __name__ == '__main__':
    app.run()