'''
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
    # print(a)

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

'''
    #python的小tips
    a=(1)
    print(type(a))      #数字
    a=(1,)
    print(type(a))      #元组
'''


# # 作业：使用python查询商品表t_goods表里面的商品名为 iPhone的价格，
#  并且判断价格如果价格大于5488，则显示买不起，否则显示买买买。
# 作业的数据库信息：

# 118.24.105.78
# root
# 1qaz!QAZ123***123
# # 数据库：ljtestdb
import pymysql
def query(sql):
    db=pymysql.connect(host="118.24.105.78",user="root",password="1qaz!QAZ123***123",db="ljtestdb")
    cur=db.cursor()
    cur.execute(sql)
    res=cur.fetchall()
    db.close()
    return res

if __name__=="__main__":
    sql = "select * from t_goods where goods='iPhone12'"
    a=query(sql)
    print(a)
    if a[0][2]>5488:
        print("买不起")
    else:
        print("买买买")
    
