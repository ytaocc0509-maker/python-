# # 1)定义员工类Employee，包含私有属性(姓名和月工资)，以及计算年工资get_annual的方法
# # 2)普通员工(Worker)和经理(Manager)继承员工类，经理类多了奖金bonus属性和管理manage方法，普通员工类多了work方法，普通员工和经理类要求根据需要重写get_annual方法
# # 3)编写函数show emp annual(e:Employee)，实现获取任何员工对象的年工资
# # 4)编写函数working(e:Employee),如果是普通员工，则调用work方法，如果是经理，则调用manage方法
#
# class Employee:
#     __name = None
#     __monthly_salary = None
#
#     def __init__(self, name, monthly_salary):
#         self.__name = name
#         self.__monthly_salary = monthly_salary
#
#     def get_annual(self):
#         return self.__monthly_salary * 12
#
#
# class Worker(Employee):
#
#     def work(self):
#         return "work"
#
#
# class Manager(Employee):
#     bonus = None
#
#     def __init__(self, name, monthly_salary, bonus):
#         super().__init__(name, monthly_salary)
#         self.bonus = bonus
#
#     def manager(self):
#         return "manager"
#
#     def get_annual(self):
#         return super().get_annual() + self.bonus
#
#
# def show_emp_annual(employee: Employee):
#     return employee.get_annual()
#
#
# def working(employee: Employee):
#     if isinstance(employee, Manager):
#         print(employee.manager())
#     elif isinstance(employee, Worker):
#         print(employee.work())
#
#
# p1 = Worker("tom", 5000)
# print(show_emp_annual(p1))
# working(p1)
#
# p2 = Manager("jack", 8000, 10000)
# print(show_emp_annual(p2))
# working(p2)
import time


# 1)编写一个Employee类，做成抽象基类,包含如下三个属性:name，id，salary,提供必要的构造器和抽象方法:work()
# # 2)对于Manager类来说，他既是员工，还具有奖金(bonus)的属,请使用继承的思想，设计CommonEmployee类和Manager类，要求实现work()，提示"经理/普通员工 名字 工作中..”
# from abc import ABC, abstractmethod
#
#
# class Employee(ABC):
#     name = None
#     id = None
#     salary = None
#
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary
#
#     @abstractmethod
#     def work(self):
#         return f"{self.name},{self.id},{self.salary}"
#
#
# class Manager(Employee):
#     bonus = None
#
#     def __init__(self, name, id, salary, bonus):
#         super().__init__(name, id, salary)
#         self.bonus = bonus
#
#     def work(self):
#         return f"{super().work()},{self.bonus}"
#
#
# p1 = Manager("tom","manager","10000","2000")
# print(p1.work())


# start = time.time()
# for i in range(1, 90001):
#     print(i)
# end = time.time()
#
# print(end - start)

# class A:
#     age = None
#
#     def __init__(self, age):
#         self.age = age
#
#
#
#
#
# p1 = A(19)
# p2 = A(14)
# p3 = A(20)
# print(p1.age)
# my_list = [p1, p2, p3]
#
#
# def sss(ele):
#     return ele.age
#
# my_list.sort(key=sss, reverse=False)
#
# for p in my_list:
#     print(p.age)
