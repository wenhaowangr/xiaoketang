#if语句
#整数判断 == < <= > >= != 
'''
age=22
if age>18:
    print("成年人，别早睡了")
else:
    print("未成年，可以早睡")

#字符串判断in 、 not in
str1="一二三四五，上山打老虎"
str2="四五"
if str2 not in str1:
    print("逮到了！")
else:
    print("两字符串无重叠")

#多条件
age=int(input("请输入年龄"))
gender=input("请输入性别")
if gender=="男":
    gender=False
else:
    gender=True
if age<18 and gender==True:
    print("满足基本要求")
else:
    print("落选")


a = 30
if a > 18:                          # a > 18
    print("成年人")
elif a > 16:                        # a > 16 and a < 18
    print("青年小伙伴")
elif a > 14:                        # a > 14 and a < 16
    print("少年小伙伴")
elif a > 6:                         # = a >6 and a < 14
    print("xxxx小伙伴")
else:                               # = a <=6
    print("这是啥，编不出来了")

#format
#"。。。{}".format(任意格式的数据)  将任意格式数据拼接到字符串
print("python{},{}{}".format("好难啊","是真的难",23333))


#while
grade=[80,92,88,26,71,66,99,54]
i=0
while i<len(grade):
    if grade[i]<60:
        print("发现了一个壮士，啊哈哈哈，成绩是{}".format(grade[i]),end=" ")    
    i+=1

i=0
while i<60:
    if i<35:
        print("red")
    elif i<55:
        print("green")
    elif i<60:
        print("yellow")
    i+=1


#for遍历所有元素的值，可以遍历数组、元组
grade=[80,92,88,26,71,66,99,54]
passgrade=[]
failgrade=[]
for i in grade:
    if i>59:
        passgrade.append(i)
    if i<60:
        failgrade.append(i)
print(passgrade)
print(failgrade)


#遍历字典
grade={"wwh":90,"bzj":94,"aaa":47,"bbb":59}
passgrade={}
failgrade={}

for i,j in grade.items():
    if j>59:
        passgrade[i]=j
    if j<60:
        failgrade[i]=j
print(passgrade)
print(failgrade)

#也可以写成下面这种格式
for i in grade.keys():
    if grade[i]>59:
        passgrade[i]=grade[i]
    if grade[i]<60:
        failgrade[i]=grade[i]
print(passgrade)
print(failgrade)       


#遍历字符串
a = "小王加油鸭"
for i in a:
    print(i)


a=["王文灏","bzj","小乔","林阳","浪老师","流云老师","xixi","mama","baba"]
for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])
'''

b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"},]
succ_register=True
uname=input("请输入账号")
pword=input("请输入密码")
new={"username":uname,"passwprd":pword}
for a in b:
    if uname==a["username"]:
        print("注册失败，账号已存在")
        succ_register=False
        break
if succ_register==True:
    b.append(new)
    print("注册成功")
    print(b)
