#_*_ coding:utf-8 _*_
import web
import datetime
from web import form
from models import getUserByUserName
# from setting import urls

urls=(
      '/', 'MainPage',
      '/Login', 'Login',
      '/(.*)', 'Page404'
      )
app = web.application(urls,globals())
render = web.template.render('templates',base='base')
session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'login':0,})
class MainPage():
    def GET(self):
        info = {}
        print 'MainPage'
        ip = web.ctx  
#         print ip
        curTime = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        info["ip"] = ip.ip
        info["curTime"] = curTime
        return render.MainPage(info)
class Page404:
    def GET(self,name):
        print "404"
        errorStr = name,"页面没找到，请处理"
        return render.Page404(name)
class Login:
    print "Login--"
    loginForm=form.Form(form.Textbox('username',description=u'用户名'),
                        form.Password("password",description=u"密码"),
                        form.Button(u"马上登陆", type="submit", description="submit"),)
    def GET(self):
        if logged(session):
            return 'you are logged'
        else:
            return render.LoginPage(self.loginForm)
    def POST(self):
        postdata=web.input()
        username=web.net.websafe(postdata.username)
        password=web.net.websafe(postdata.password)
        rslist=getUserByUserName(username)
        if username=="":
            return render.Login(self.loginForm,"账号或密码不能为空！")
        if len(rslist)==0:
            errorInfo = "对不起，%s不存在----"%(username)
            return render.login(self.LoginForm,errorInfo)
        else:
            if password==rslist[0].pwd:                
                session.login=1
                #session.login222=1
#                 return  '登陆成功,欢迎你:'+username+':'+str(session.login)
                return '登录成功，欢迎你*****',username,':',str(session.login)
            else:
                return render.Login(self.loginForm,'用户名及密码不匹配')
#
def logged(session):
    return False
#     if session.login == 1:
#         return True
#     else:
#         return False
if __name__ == '__main__':
    app.run()