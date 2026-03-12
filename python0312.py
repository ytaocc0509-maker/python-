# class Person:
#     name = None
#     age = None
#
#
#
# def f1(person):
#     print(f"person的地址：{id(person)}")
#     person.name = "james"
#     person.age += 1
#
#
# p1 = Person()
#
# p1.name = "tom"
# p1.age = 12
#
#
#
#
#
import random


# 在初始化对象时，会自动执行__init__方法
# class Person:
#     # 构造方法/构造器
#     def __init__(self):
#         print("__init__执行了")
#
#
# p1 = Person()
# p2 = Person()

# class Person:
#     name = None
#     age = None
#
#     # 构造方法/构造器
#     def __init__(self, name, age):
#         print("__init__执行了", {name}, {age})
#         self.name = name
#         self.age = age
#
#     def test(self):
#         print(self.age)
#
# p1 = Person("tom", 12)
# print(p1.test())


# class Person:
#     def __init__(self, name, age):
#         print(f"__init_- 执行了...得到了{name} {age}")
#         self.name = name
#         self.age = age
#
#
# p1 = Person("tim", 30)
# print(f"p1的 name={p1.name} age={p1.age}")


# 编写类A01，定义方法max，
# 实现求某个float 列表list =[1.1,2.9,-1.9,67.9]的最大值，并返回

# list_a = [1.1, 99.3, 2.9, -1.9, 67.9, 5.2]
#
#
# def max_num(my_list):
#     for i in range(0, len(my_list)):
#         for j in range(0, len(my_list) - 1 - i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#     return list_a[len(my_list) - 1]
#
#
# print(f"列表最大指时：{max_num(list_a)}")


# 2、编写类Book，定义方法update_price，实现更改某本书的价格，
# 具体:如果价格>150,则更改为150，如果价格>100,更改为

# class Book:
#     price = 98
#
#     def update_price(self, price):
#         if price > 150:
#             self.price = 150
#         elif price > 100:
#             self.price = 100
#
#
# p1 = Book()
# p1.update_price(99)
# print(p1.price)

# 定义一个圆类 Circle，定义属性:半径，提供显示圆周长功能的方法，提供显示圆面积的方法
# import math
#
#
# class Circle:
#     r = None
#
#     # 计算周长
#     def get_perimeter(self, r):
#         return 2 * r * math.pi
#
#     # 计算面积
#     def get_area(self, r):
#         return math.pi * r * r
#
#
# p1 = Circle()
#
# print(f"圆周长是：{p1.get_perimeter(3)}")
# print(f"圆面积是：{p1.get_area(3)}")

# 编程创建一个Cal计算类，在其中定义2个成员变量表示两个操作数，
# 定义四个方法实现求和、差、乘、商(要求除数为0的话，要提示)并创建对象，分别测试

# class Cal:
#     num1 = None
#     num2 = None
#
#     # 求和
#     def get_sum(self):
#         return self.num1 + self.num2
#
#     # 求差
#     def get_dif(self):
#         return self.num1 - self.num2
#
#     # 求乘
#     def get_mul(self):
#         return self.num1 * self.num2
#
#     # 求商
#     def get_quotient(self):
#         if self.num2 == 0:
#             print("除数为0的话")
#         else:
#
#             return self.num1 / self.num2
#
#
# p1 = Cal()
# p1.num1 = 5
# p1.num2 = 3
# print(f"和：{p1.get_sum()}")
# print(f"差：{p1.get_dif()}")
# print(f"乘：{p1.get_mul()}")
# print(f"商：{p1.get_quotient()}")

# 定义Music类，
# 里面有音乐名name、
# 音乐时长times属性，并有播放play功能,和返回本身属性信息的方法

# class Music:
#     name = None
#     times = None
#
#     def __init__(self, name, times):
#         self.name = name
#         self.times = times
#
#     def play(self):
#         return self.name, self.times
#
#
# p1 = Music("歌曲1", "100s")
# print(p1.play())


# 1)有个人 Tom 设计他的成员变量, 成员方法,可以进行电脑猜拳,电脑每次都会随机生成 0,1,2
# 2)0 表示 石头 1 表示剪刀 2 表示 布
# 3)并要可以显示 Tom的输赢次数(清单)

# class Tom:
#     num = None
#
#     def __init__(self, num):
#         self.num = num
#
#     def rock_paper_scissors(self):
#         range_num = random.randint(0, 2)
#         if range_num == 0:
#             self.ai_0()
#         elif range_num == 1:
#             self.ai_1()
#         else:
#             self.ai_2()
#
#     def ai_0(self):
#         if self.num == 0:
#             print("平局")
#         elif self.num == 1:
#             print("输了")
#         else:
#             print("赢了")
#
#     def ai_1(self):
#         if self.num == 0:
#             print("输了")
#         elif self.num == 1:
#             print("平局")
#         else:
#             print("赢了")
#
#     def ai_2(self):
#         if self.num == 0:
#             print("赢了")
#         elif self.num == 1:
#             print("输了")
#         else:
#             print("平局")
#
#
# p1 = Tom(random.randint(0, 2))
# print(p1.rock_paper_scissors())

class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共方法，对私有属性进行访问
    # def set_job(self,job):
    #     self.__job = job

    def get_job(self):
        return self.__job

    def __hi(self):
        print("hi")

    def get_hi(self):
        self.__hi()



p1 = Clerk("tom", "python", 2000)
print(p1.name)  # 可直接访问
print(p1.get_job())
p1.get_hi()