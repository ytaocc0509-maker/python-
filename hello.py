# coding:utf-8
'''
print("姓名\t\t年龄\t\t籍贯\t\t地址\njohn\t12\t\t河北\t\t北京")
print("姓名\t\t年龄\t\t籍贯\t\t地址\njohn\t12\t\t河北\t\t北京")
print("姓名\t\t年龄\t\t籍贯\t\t地址\njohn\t12\t\t河北\t\t北京")
'''
import sys


# rint("求-100.67的绝对值",abs(-100.67))

# print("姓名\t    年龄\t    籍贯\t    地址\n老于\t    12\t    河北\t    北京")

# print("123456 \r  7890")


# n1 = 2
# n2 = 2 ** 3
# print(n1,sys.getsizeof(n1),"类型",type(n1))
# print(n2,sys.getsizeof(n2),"类型",type(n1))

# from decimal import Decimal
#
# n1 = 8.1
# n2 = 3
#
# b = Decimal("8.1") / Decimal("3")
#
# print(b)
# if 1.1:
#     print("123")


# print(r"\n \t \\ 1 2 3")
#
# n1 = "书本1"
# n2 = "书本2"
# n3 = n1 + n2
# print(n3)

# name = "tom"
# age = 26
# score = 100
# gender = "男"
# hobby = "篮球"
#
# print("姓名\t年龄\t分数\t性别\t爱好" + "\n" + name + "\t" + str(age) + "\t" + str(score) + "\t" + gender + "\t" + hobby)
#
# print((str(97 // 7) + "个星期" + "零" + str(+97 % 7) + "天"))

# hua_du = 234.5
#
# she_du = 5 / 9 * (hua_du - 100)
# print("华氏温度 %.1f 对应摄氏温度 %.2f " % (hua_du, she_du))
# print(f"华氏温度 {hua_du} 对应摄氏温度 {she_du} ")

# name = input("请输入名字：")
# age = input("请输入年龄：")
#
# print(f"姓名 {name}   年龄{age}",type(name),type(age))

# num1 = 0x123
#
# print(hex(0o110))
# print(bin(123))
# print(oct(123))

# a = 1 >> 2
# b = -1 >> 2
# c = 1 << 3
# d = -1 << 3
# print(d)

# print((~2))#-3
# print(2&3)#2
# print(2|3)#3
# print(~-5)#4
# print(13&7)#
# print((5|4))
# print((-3^3))

# a = "123*#"
#
# b = sys.intern(a)
# print(id(a),id(b))

# age = input("请输入年龄:")
# if int(age) > 18:
#     print("你的年龄大于18，要对自己的行为负责！")
# else:
#     print("你还是个孩子啊！")

# x1 = 20
# x2 = 23
# if x1 + x2 >= 50:
#     print("666")


# x1 = 11.2
# x2 = 11.3
#
# if x1 > 10.0 and x2 < 20.0:
#     print(x1 + x2)


# year = int(input("请输入一个年份："))
# if year % 400 == 0 or (year % 4 == 0 and not (year % 100 == 0)):
#     print(f"{year}闰年")
# else:
#     print(f"{year}不是闰年")

# x1 = 10
# x2 = 11
# if x1 > 10:
#     print("good")
# elif x2 > 10:
#     print("ok")
# else:
#     print("no")


# score = int(input("小头儿子的成绩是："))
# if score == 100:
#     print("奖励你一台bmw")
# elif 80 < score <= 99:
#     print("奖励你一台iphone13")
# elif 60 < score <= 80:
#     print("奖励一个ipad")
# else:
#     print("啥也没有")

# score = float(input("你的成绩是:"))
#
#
# if score > 8.0:
#     gender = input("你的性别是（男/女）：")
#     if gender == "男":
#         print("进入男子决赛")
#     elif gender == "女":
#         print("进入女子决赛")
# else:
#     print("淘汰")
# month = int(input("请输入月份："))
# age = int(input("请输入年龄："))
#
# if 4 <= month <= 10:
#     if 18 <= age <= 60:
#         print("门票60元")
#     elif age < 18:
#         print("门票半价")
#     else:
#         print(("门票20"))
# else:
#     if 18 <= age <= 60:
#         print("40")
#     else:
#         print("20")
# for letter in 'Python':     # 第一个实例
#    print("当前字母: %s" % letter)

#

# i = 0
# while i < 10:
#     print("12345",i,id(i))
#     i += 1


# for i in range(1,101):
#     if i%3==0:
#         print(i)

# i = 1
# while i <= 100:
#     i += 1
#     if i % 3 == 0:
#         print(i)

# for i in range(40, 201):
#     if i % 2 == 0:
#         print(i)


# i = 40
# while i <= 400:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# name = input("请输入名字")
#
# while name !="exit":
#     name = input("请输入名字")
# while
# num = 1
# count = 0
# num_total = 0
# while num <= 100:
#     if num % 9 == 0:
#         print(num)
#         count += 1
#         num_total += num
#     num += 1
# else:
#     print(count, num_total)

# num = int(input("请输入一个整数："))
# x = 0
# while num > 0:
#     print(x, "+", num, "=", num + x)
#     x += 1
#     num -= 1
# else:
#     print(num + x, "+", num, "=", num + x)

# a = 10
# for i in range(a):
#
#     for k in range(a - i):
#         print(" ", end="")
#
#     for j in range(i):
#         if j == 0 or j == i - 1 or i==a:
#             print("⭐", end="")
#         else:
#             print("  ", end="")
#     i += 1
#     print("")

# sum = 0.0;
# for i in range(1, 6):
#     score = float(input("请输入学生成绩："))
#     sum += score
# print(f"平均分：{sum / 5}")

# import random
#
# n = 0
# while n != 97:
#     n = random.randint(1, 100)
#     print(n)
#     if n == 97:
#         break


# for i in range(1, 4):
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#
#     if name == "张无忌" and password == "888":
#         print("登陆成功")
#         break
#     else:
#         print(f"登陆失败，还剩余{3 - i}次机会")

# money = 100000
# count = 0
# while True:
#     if money > 50000:
#         money -= money * 0.05
#     elif money < 1000:
#         break
#     else:
#         money -= 1000
#     count += 1
#
# print(count,money)


# def cat_cry():
#     print("小猫喵喵喵")
#
# cat_cry()

def cal01(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum

a= cal01(1,1000)