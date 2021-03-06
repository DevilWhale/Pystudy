# print("hello world!")


# print("哈哈",22,2.33)
# print("哈哈"+"嘻嘻")    #字符串的拼接
# print("哈哈"*10)        

# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取的内容:",a+b)



# 元组,下表,从0开始
# a = (1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",False,True)  在这里修改属于定义
# print(a[5])           (下标也可以是负数)
# 切片(批量取值)
# print(a[0:4]) #左闭右开


# print(a.index("哈哈")) (就近原则)
# print(a.count("哈哈"))

# 二维元组
# b = (a,"哈哈","嘻嘻")   ("3个值")
# print(b[0][3])  打印a元组里的4





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
3.
"""

# a = {
#     "name":"瓜皮",
#     "age":12,
#     0:"哈哈"
# }


# #取值
# print(a["key"])

# # 新增
# a["key"] = "value"
# print(a)

# # 修改
# a["key"] = "value"
# print(a)

# b = a.get("key")
# print(b)
# b = a.pop("key")
# print(a)
# print(b)

# a.update(key=value)   key可以不打""
# print(a)

# print("---------get方法取值和直接取值的却别---------")

# # 正常情况下
# print(a.get("key"))           输出结果:key
# print(a["key])                输出结果:key

# # 不正常情况下
# print(a.get("key1"))          输出结果:None
# print(a["key"])               输出结果:报错




