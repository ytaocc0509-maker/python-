# class cat:
#     age = 2
#     name = None
#     color = "yellow"
#
#
# cat1 = cat()
#
# print(cat1.color)
import pickletools


# class Person:
#     age = None
#     name = None


# p1 = Person()
# p1.age = 10
# p1.name = "xiaoming"
# p2 = p1
# p2.age = 12
# p1.age = 13
#
#
# print(p1.age)
# print(p2.age)
# print(f"p1.name地址:{id(p1.name)}p2.name地址:{id(p2.name)}" )

# class Person:
#     name = None
#     age = None
#
#     def hi(self):
#         print("hi,python")
#
#     def cal01(self):
#         sum = 0
#         for i in (0, 1001):
#             sum += i
#
#         print(sum)
#
#     def cal02(self, n):
#         sum = 0
#         for i in (0, n + 1):
#             sum += i
#
#         print(sum)
#
#     def get_sum(self, n1, n2):
#         return n1 + n2
#
#
# p1 = Person()
# p1.hi()
# p1.cal01()
# p1.cal02(10)
# print(p1.get_sum(5,5))


# def hi():
#     print("hi")
#
#
# class Person:
#     age = None
#
#
# p1 = Person
# p2 = Person
# p1.m1 = hi
# p1.m1()
#
# p2.m1()#报错

# 。定义Person类
# 1)里面有name、age属性
# 2)并提供compare_to比较方法，用于判断是否和另一个人相等
# 3)名字和年龄都一样，就返回True,否则返回False

class Person:
    name = None
    age = None

    def compare_to(self, other):
        return self.name == other.name and self.age == other.age


p1 = Person()
p2 = Person()

p1.name = "jack"
p1.age = 12

p2.name = "tom"
p2.age = 12

print(p1.compare_to(p2))
