# def add(a):
#     print(f"a的值：{a}地址：{id(a)}")
#     a += 1
#     print(f"a的值：{a}地址：{id(a)}")
#
#
# a = 2
# print(f"a的值：{a}地址：{id(a)}")
# add(a)
# print(f"a的值：{a}地址：{id(a)}")


# def test(n):
#     if n > 2:
#         test(n - 1)
#     print("n", n)
#
#
# test(4)


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n - 1) * n
#
#
# print(factorial(4))

# 请使用递归的方式求出斐波那契数1,1,2,3,5,8,13...给你一个整数n，求出它的值是多 (n-2)+(n-1)+1

def fibonacci_sequence(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1)


print((fibonacci_sequence(10)))
