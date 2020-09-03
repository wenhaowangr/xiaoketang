'''
def minus(s1=0,s2=0):
    res=s1-s2
    return res
res1=minus(7,9)
res2=minus()
print(res1,res2)

#把注册改成一个method
def register(username,password):
    b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"},]
    succ_register=True

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

uname=input("请输入账号")
pword=input("请输入密码")
registerres=register(uname,pword)
'''


n=[0,0]*5
print(n)