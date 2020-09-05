
#官方包
import time
import math
import random

# time
# datetime（time升级版）
#time.sleep(2)
print("延迟2s打印")

# math
a = math.cos(0)
b = math.sqrt(100)
print("cos(0)={},根号100={}".format(a,b))

# randm
c = random.randint(0,10)
print("产生0-10的随机数'{}'".format(c))

# unitest(后面详细讲)

#第三方包——pip安装
#查看版本号————pip -V
#查看已安装的包————pip list
#安装第三方包————pip install 第三方包名
#卸载第三方包————pip uninstall 第三方包名


from tools.dbtools import query
from o3method import *

if __name__=="__main__":
    print("计算2-8={}".format(minus(2,8)))




'''
#异常处理：没报错，执行try，报错了，执行except
#try里写要测试的代码，except里写出错之后怎么办
#开发中用的多，测试中用得少
res=[0,1,2,3]
try:
    print(res[0])
    print("最先运行")
except Exception as e:
    print(e)
    print("报错了就执行：代码出错啦")
else:
    print("没报错就执行：好像没错？？！")
finally:
    print("出不出错都绕不过的finally")
'''