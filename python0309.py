# 冒泡排序
# list_bubble = [24, 69, 80, 57, 13]
#
# print("排序前：".center(32, "_"))
# print(f"list_bubble: {list_bubble}")
import random

# list_bubble.sort()

# 递归
# num = len(list_bubble) - 1
#
#
# def bubble_sort(list, num):
#     if num >= 0:
#         for j in range(0, num):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#
#         else:
#             num -= 1
#             return bubble_sort(list, num)
#     else:
#         return list
#
#
# bubble_sort(list_bubble, num)

# def bubble_sort(list):
#     for i in range(0, len(list) - 1):
#
#         for j in range(0, len(list) - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#
# bubble_sort(list_bubble)
# print("排序后：".center(32, "_"))
# print(f"list_bubble: {list_bubble}")

# # 顺序查找
# names_list = ["白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王","金毛狮王"]
# find_name = "金毛狮王"
#
# list_b = list()
# def search_str(list_a, find_val):
#     for i in range(0, len(list_a)):
#
#         if list_a[i] == find_val:
#             list_b.append(i)
#
#     else:
#         print(list_b)
#
#
# search_str(names_list, find_name)


# 二分查找

# list_a = [1, 8, 10, 89, 1000, 1234]
#
#
# def binart_search(list_ab, find_val):
#     find_index = -1
#     index_left, index_right = 0, len(list_ab) - 1
#
#     while index_left <= index_right:
#         mid = (index_left + index_right) // 2
#
#         if list_ab[mid] > find_val:
#             index_right = mid - 1
#         elif list_ab[mid] < find_val:
#             index_left = mid + 1
#         else:
#             find_index = mid
#             break
#
#     return find_index
#
#
# num = binart_search(list_a, 1234)
# print(num)

# # 随机生成10个整数(1-100的范围)保存到列表，使用冒泡排序，对其进行从大到小排序
# list_num = list()
# for _ in range(0, 100):
#     list_num.append(random.randint(1, 100))
#
# print(list_num)
#
#
# def bubble_sort(my_list):
#     for i in range(0, len(my_list) - 1):
#         for j in range(0, len(my_list) - 1 - i):
#             if list_num[j] > list_num[j + 1]:
#                 list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
#
#
# bubble_sort(list_num)
# print(list_num)
#
# # 在第1题的基础上，使用二分查找，查找是否有8这个数,如果有，则返回对应的下标,如果没有，返回-1
#
# list_val = list()
#
#
# def binart_search(my_list, find_val):
#     find_index = -1
#
#     index_left, index_right = 0, len(my_list) - 1
#     while index_left <= index_right:
#         mid_index = (index_left + index_right) // 2
#         if my_list[mid_index] < find_val:
#             index_right = mid_index - 1
#         elif my_list[mid_index] > find_val:
#             index_left = mid_index + 1
#         else:
#             find_index = mid_index
#             break
#     return find_index

sum_a = 0
# debug for 循环过程
# for i in range(0, 10):
#     sum += i
#     print(f"i ={i}")
#     print(f"sum={sum_a}")
#
# print("end...")
