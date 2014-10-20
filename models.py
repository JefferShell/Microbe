#_*_ coding:utf-8 _*_
import os

import web


debug = 'SERVER_SOFTWARE' not in os.environ
web.config.debug = debug
# 数据库配置
if debug:
    # 本地
    MYSQL_DBN = 'mysql'
    MYSQL_DB = 'test'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
else:
    # SAE
    MYSQL_DBN = 'mysql'
    MYSQL_DB = 'test'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = "3306"
db1=web.database(dbn=MYSQL_DBN, 
    db=MYSQL_DB, 
    user=MYSQL_USER,
    host=MYSQL_HOST,
    pw=MYSQL_PASS,
    port=MYSQL_PORT)
db2=web.database(dbn='mysql', 
    db='test', 
    user='root',
    host='127.0.0.1',
    pw='root',
    port=3306,)
#根据用户名查询用户信息
def getUserByUserName(username):
    rs=db2.select('user',where='userName="'+username+'"')
    rslist=[]
    for r in rs:
        rslist.append(r)
    return rslist    