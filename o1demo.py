
#字符串操作
print("hello",end="   ")
print("world")
print("这里是王文灏",213163344,"东南大学")    #print的内容可以用，相连
print("嘻嘻"+"哈哈")        #字符串相加是拼接的效果
print("嘻嘻"*2)             #字符串×数字表次数

print(10//3)                #取整
print("2的3次方=",2**3)     #幂
print(1>3 or 1==1)

name="maggie"
print(name)

#输出两数和
a=input("请输入a")
b=input("请输入b")
print("a+b=",a+b)

#强制类型转换
print("a的数据类型为",type(a))   #input的数据默认为str类型
a=float(a) 
b=float(b)                      #强制数据类型转换
print("a的数据类型为",type(a))   #强制转换成float类型
print("a+b=",a+b)



#计算输入字数是单数还是双数
#len_a = len(input("请输入字符串："))
#if len_a%2 == 0:
#   print("输入字符串长度为双")
#if len_a%2 == 1:
#   print("输入字符串长度为单")


#元组
b=("maggie","john")
a=(1,2,3,"haha","xixi",True,False,b)    #二维元组
print(a)
#a[-1]代表元组最后一个元素
#a[0]和a[-8]是一样的，都对应到第一个数据
print("haha的下标是：",a.index("haha"))
print("元组a中有 ",a.count(1)," 个1")
#取二维元组中数据
print(a[-1][-1])
#元组的“切片”取数据,左闭右开
print(a[0:3])


#数组list
b=("maggie","john")
a=[1,2,3,"haha","xixi",True,False,b]    #元组里装数组
print("数组a为：",a)
#元组数组操作方式一模一样，元组元素不可修改，数组可以修改
name=input("请输入你的名字")

a.append(name)          #数组尾部追加数据
print("append应用——数组a为：",a)

a.remove(a[-1])         #删除数据
print("remove应用——数组a为：",a)

a.insert(1,name)        #指定位置插入数据
print("insert应用——数组a为：",a)

xx=a.pop(a.index("wwh"))   #把数组a中haha这个元素弹出，赋给xx
print(xx)
print("pop应用——数组a为：",a)

c=["liwei","dongyue"]
a.extend(c)
print("extend应用——数组a为：",a)
#效果等同于a+c

d=[1,2,3,5,4]
d.reverse()
print("reverse应用——数组d为：",d)
d.sort()
print("sort应用——数组d为：",d)
d.sort(reverse=True)
print("倒序sort应用——数组d为：",d)


#字典key-value
#没有下标的概念，即无顺序，取值靠key
a={"name":"maggie","age":22,"tel":"18651626207"}
#字典的两种取值方法
print(a["name"])        #a["name1"]报错
print(a.get("name"))    #a.get("name1")返回NULL
#新增
a["address"]="shanghai" #当key不存在时，新增；存在时，修改
print(a)
#更新——key是一个变量
a.update(name="wwh")    #当key不存在时，新增
print(a)
#弹出
xx=a.pop("tel")
print(xx)
print(a)
#通用删除方法，数组写下标，字典写key
del a["address"]
print(a)

print(list(a.keys()))
print(list(a.values()))

