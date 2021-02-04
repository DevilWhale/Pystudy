# print("hello world!")


# print("哈哈",22,2.33)
# print("哈哈"+"嘻嘻")    #字符产的拼接
# print("哈哈"*10)        

# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取的内容:",a+b)

"""
练习:通过代码获取两段内容,并且计算他们长度的和
"""

# a = float(len(input("请输入:")))
# b = float(len(input("请输入:")))
# print("两段内容的长度和为:",a+b)


# 元组
# a = (1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",False,True)
# # 切片
# print(a[0:4]) #左闭右开

#数组(元组不可修改数组可以)
# a = [1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",False,True]
# a.append("append")
# print(a)

# a.insert(4,"insert")
# print(a)

# b = a.pop(0)
# c = a.pop(0)     #剪切
# print(c+b)
# print(a)
# print(b)

"""
下标不要超出范围 = 越界
所有的方法都是小括号结尾,比如,print(),insert()
元组,数组,字典的取值,都是用中括号,比如,a[0]
元组,数组,字典的定义,分别是(),[],{}
"""

"""
字典的特点
1.字典中没有顺序
2.字典的接口必须是键值对的结构:   key:value
"""

# a = {
#     "name":"瓜皮",
#     "age":12,
#     "age":122
# }

# #取值
# print(a["name"])
# # 新增
# a["height"] = "183cm"
# print(a)
# # 修改
# a["name"] = "李四"
# print(a)

# b = a.get("name")
# print(b)
# b = a.pop("name")
# print(a)
# print(b)

# a.update(name=11111)
# print(a)

# print("----------------------------")

# # 正常情况下
# print(a.get("name"))
# print(a["name"])

# # 不正常情况下
# print(a.get("name11"))
# print(a["name11"])

"""
练习:
获取用户的个人信息,并且存储到字典中
个人信息包括,name,age,sex
"""

name = input("请输入您的姓名:")
age = input("请输入您的年龄:")
sex = input("请输入您的性别:")

userinfo = {}

userinfo["name"] = name
userinfo["age"] = age
userinfo["sex"] = sex
print(userinfo)





