#_*_ coding:utf-8 _*_
import web
import os

#地址跳转页面
urls=(
      '/', 'MainPage',
      '/.*?', 'Page404'
      )