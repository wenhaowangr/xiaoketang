
import pymysql

def query(sql):
    #以下为固定写法，相当于navicat
    #连接数据库
    db=pymysql.connect(host="192.144.148.91",user="ljtest",password="Lj123456+",db="ljtestdb")
    #获取查询窗口，游标
    cur=db.cursor()
    #执行sql语句
    cur.execute(sql)
    #获取返回的结果
    res=cur.fetchall()
    db.close()
    return res


if __name__=="__main__":
    # a = query("select * from t_user where username = 'liuyun'")
    # a = query("select * from t_user where username = '{}'".format("liuyun"))     #外双内单，外单内双
    #print(a)

    u=input("请输入账号")
    p=input("请输入密码")
    sql= "select * from t_pymysql_account where username='{}' and password='{}'".format(u,p)
    r=query(sql)
    print(r)

    if len(r)!=0:
        print("登录成功")
    else:
        print("登录失败")


'''
#python的小tips
a=(1)
print(type(a))      #数字
a=(1,)
print(type(a))      #元组
'''


