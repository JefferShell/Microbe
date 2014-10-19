#_*_ coding:utf-8 _*_
import web
import datetime
# from setting import urls

urls=(
      '/', 'MainPage',
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
        print ip
        curTime = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        info["ip"] = ip.ip
        info["curTime"] = curTime
        return render.MainPage(info)
class Page404:
    def GET(self,name):
        print "404"
        errorStr = name,"页面没找到，请处理"
        return render.Page404(name)
#
if __name__ == '__main__':
    app.run()