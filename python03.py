# 猴子吃桃子问题:有一堆桃子，猴子第一天吃了其中的一半，并再多吃了一个!
# 以后每天猴子都吃其中的一半，然后再多吃一个。当
# 到第10天时，想再吃时(即还没吃)发现只有1个桃于了
# 。问题:最初共多少个桃于

# 第九天桃子 - 第九天桃子/2 -1 = 第十天桃子
# 第九天桃子  = (第十天桃子+1)2
# 第八天桃子  = （第九天桃子+1）2

# def eat_peach(day):
#     if day == 10:
#         return 1
#     else:
#         return (eat_peach(day + 1) + 1) * 2
#
#
# print("第一天桃子数量为：", (eat_peach(1)))

# 求函数值，
# 題 f(1)= 3; f(n)= 2 *f(n-1)+ 1;這使用递归的黒想编程，求出 f(n)的值

# f(0) = 1 ,f(1) = 3,  f(2) = 7, f(3) = 15, f(4) = 31
#

# def get_value(num):
#     if num == 1:
#         return 3
#     else:
#         return (get_value(num - 1) * 2) + 1
#
#
# print(get_value(10))


# 汉诺塔
# def han_num_ta(num, a, b, c):
#     if num == 1:
#         print("第1个盘子从：", a, "->", c)
#     else:
#         han_num_ta(num - 1, a, c, b)
#         print(f"第{num}个盘子从 ：{a} -> {c}")
#         han_num_ta(num - 1, b, a, c)
#
#
# han_num_ta(2, "A", "B", "C")

# 列表

# 再举一个案例,要求生成一个列表,内容为[1,4,9,16,25,36,49,64,81,100],文件list_create.py
# lst1 = [ele * ele for ele in range(1, 11)]
# print(lst1)


def input_list(n):
    list1 = list()

    for i in range(1, n + 1):
        list1.append(int(input("请输入成绩：")))
    return list1


print(input_list(5))
