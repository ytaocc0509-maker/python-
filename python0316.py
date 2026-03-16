# try:
#     num1 = 10
#     num2 = 0
#     res = num1 / num2
# except Exception as e:
#     print(f"捕获到异常{e}")# 捕获到异常division by zero
#
# print("程序继续运行...")

# 如果用户输入的不是一个整数，就提示他反复输入，直到输入一个整数为止

# while True:
#     try:
#         num = int(input("请输入一个整数："))
#         break
#     except Exception as e:
#         print("输入错误")

# 当我们接收Person年龄时，要求范围在18-120之间，否则抛出一个自定义异常，
# 并给出提示信息(循环提示,直到输入了正确的年龄)

class AgeError(Exception):
    pass


while True:
    try:
        age = int(input("请输入你的年龄："))
        if not (18 <= age <= 120):
            raise AgeError("年龄要18-120")
        break
    except ValueError as e:
        print("你输入的不是整数")

    except AgeError as e:
        print(e)

print(age)
