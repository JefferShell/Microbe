#_*_ coding:utf-8 _*_
import datetime

import web


######==========================用户的操作============================= 
db = web.database(dbn = 'mysql', db = 'blog', user = 'root', 
                  pw = 'root' ,port = 3306 ,host='127.0.0.1')  
 #根据用户名获取密码
def getPwdByName(userName):
    user = ''
    try:
        user = db.select('user',where='username=$userName',vars=locals())[0]
    except:
        print "get %s fail"%(userName)
    return user
#根据id获取user
def getUserById(userId):
    user = ''
    try:
        user = db.select('user',where='userId=$userId',vars=locals())[0]
    except:
        print "get %s fail"%(userId)
    return user
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
    try:
        if(username!='' and pwd !=''):
            db.update('entries',where="id=$id",vars=locals(),pwd=pwd,username=username)[0]
        else:
            print "账号或密码不能为空" 
    except:
        print "修改失败"
#根据id删除
def deleteUserById(id):
    try:
        db.delete('entries',where="id=$id",vars=locals())  
    except:
        print "删除%s失败"%(id)
    
if __name__ == '__main__':
    print getUserById("1")