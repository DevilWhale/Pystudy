"""
    练习:通过代码获取两段内容,并且计算他们长度的和


    a = float(len(input("请输入:")))
    b = float(len(input("请输入:")))
    print("两段内容的长度和为:",a+b)
"""


"""
练习:
    获取用户的个人信息,并且存储到字典中
    个人信息包括,name,age,sex
"""

#   name = input("请输入您的姓名:")
#     age = input("请输入您的年龄:")
#     sex = input("请输入您的性别:")

#     userinfo = {}
#     userinfo["name"] = name
#     userinfo["age"] = age
#     userinfo["sex"] = sex
#     print(userinfo)


"""
练习:
现在有7个学生的成绩,需要录入系统
分别为张三,李四,王五,浪晋,流云,希希,亚索
名字和成绩需要对应上
而且大于60和小于60的需要分开存放.

"""
# studentlist = ["张三","李四","王五","浪晋","流云","希希","亚索"]
# Hscore = {}
# Lscore = {}

# for i in studentlist:
#     cj = int(input("请输入"+i+"的成绩"))
#     if cj >=60 :
#         Hscore[i] = cj
#     else:
#         Lscore[i] = cj   


# print(Hscore)  
# print(Lscore)








"""
练习:
打印99乘法表
"""

# for i in range(1,10):
#     for j in range(1,i+1):

#         print(i,"X",j,"=",i*j,end="     ")
#     print()






"""
练习:
通过print打印,模拟一个红绿灯的功能,注意:红灯10次,绿灯15次,黄灯3次
"""

# for  i in range(1,16):                   简化:light = {"红灯":15,"绿灯":10,"黄灯":5}                                                   
#     print("红灯还有2秒",i)                        for i in light:                                                   
#     print("红灯还有1秒")                             for j in range(light[i]):
#         print("绿灯还有2秒",j)                         print(i,"还有",light[i]-j,"秒")                             
#         print("绿灯还有1秒")
# for k in range(1,6):
#             print("黄灯还有2秒",k)
#             print("黄灯还有1秒")







"""
练习:
使用代码,实现一个注册的功能
用户输入账号和密码.要求账号长度是5-8位,密码6-12位,并且账号开头必须小写
储存到字典中,{username:password}
"""

# username = input("请输入账号:")
# password = input("请输入密码:")
# if len(username)>=5 and len(username) <=8:
#     if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#         if len(password)>=6 and len(password)<=12:

#             print("注册成功",username,password)
#         else:
#             print("密码长度不规范,请输入6-12位的额账号")
#     else:
#         print("账号首字母必须小写")

# else:
#     print("账号长度不规范,请输入5-8位的额账号")





"""
练习:
"""


"""
练习:
"""

"""
练习:
"""


"""
练习:
"""