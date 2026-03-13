# # 编写Computer类，包含CPU、内存、硬盘等属性
# # 1)get_details方法用于返回Computer的详细信息
# # 2)编写PC子类，继承Computer类，添加特有属性【品牌brand】
# # 3)编写NotePad子类，继承Computer类，添加特有属性【color】
# # 完成测试，创建PC和NotePad对象，分别给对象中特有的属性赋值，以及从Computer类继承的属性赋值，并使用方法打印输出信息
#
# class Computer:
#     cpu = None
#     memory = None
#     hard_disk = None
#
#     def __init__(self, cpu, memory, hard_disk):
#         self.cpu = cpu
#         self.memory = memory
#         self.hard_disk = hard_disk
#
#     def get_details(self):
#         return f"cpu:{self.cpu}\t memery: {self.memory}\t hard_disk:{self.hard_disk}"
#
#
# class PC(Computer):
#     brand = None
#
#     def __init__(self, cpu, memory, hard_disk, brand):
#         # 通过super().xx 方式可以去调用父类的构造器，对父类的属性完成初始化
#         super().__init__(cpu, memory, hard_disk)
#         self.brand = brand
#
#     def print_info(self):
#
#         print(f"品牌：{self.brand}\t{super().get_details()}")
#
#
# class NotePad(Computer):
#     color = None
#
#
# p1 = PC("inter", 32, 1000, "华为")
#
# p1.print_info()
#
#
# 1)编写一个Person类，包括属性(name、age),构造方法、say方法(返回Person自我介绍的字符串)
# 绍的信息)
# 2)编写一个Student类，继承Person类，增加属性(id、score)，以及构造方法，重写say方法(返回Student自我介
# 3)分别创建Person和Student对象，调用say方法输出自我介绍，体会重写的作用

# class Person:
#     name = None
#     age = None
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         return f"我是{self.name},{self.age}岁"
#
#
# class Student(Person):
#     id = None
#     score = None
#
#     def __init__(self, name, age, id, score):
#         super().__init__(name, age)
#         self.id = id
#         self.score = score
#
#     def say(self):
#         return f"{super().say()},{self.id},{self.score}"
#
#
# p1 = Person("tom", 18)
# print(p1.say())
#
# p2 = Student("jack", 20, "boy", 99)
# print(p2.say())

# from typing import Union
#
# a: dict[Union[float, str], int] = {22.2: 123, "2131": 333}
