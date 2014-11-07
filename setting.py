#_*_ coding:utf-8 _*_
import os

#地址跳转页面
urls=(
      '/', 'mainPage',
      '/login', 'login',
      '/logout', 'logout',
      '/addArticle/.*?','addArticle',
      '/articlDetail','articlDetail'
#       '/.*?', 'Page404'
      )
#全局变量
def getGlobals(web):
    t_globals={
           "global_data":web.datestr,
           "cookie":web.cookies,
           }
    return t_globals
