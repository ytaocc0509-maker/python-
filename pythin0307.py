# books = ["书本A", "书本B", "书本C"]
# authors = ["作者A", "作者B", "作者C"]
#
# dict_Book = {A: B for A, B in zip(books, authors)}
#
# print(dict_Book)

# en_list = ["red", "black", "white", "yellow"]
# cn_list = ["红色", "黑色", "白色", "黄色"]
#
# dict_color = {cn: en for cn, en in zip(cn_list, en_list)}
#
# print(dict_color)

# 个公司有多个员工,请使用合适的数据类型保存员工的信息(比如员工号、年龄、名字、入职时间、薪水等)，
# 要求员工号是入职时分配的，唯一不重复

# clerk = {"0001": {"age": 20, "name": "贾宝玉", "entry_time": "2011-11-11", "sal": 12000},
#          "0002": {"age": 21, "name": "薛宝钗", "entry_time": "2015-12-12", "sal": 10000},
#          "0010": {"age": 18, "name": "林黛玉", "entry_time": "2018-10-10", "sal": 20000}}
# # print(clerk["0001"]["name"])
#
# clerk['0003'] = {"age": 20, "name": "张三", "entry_time": "2017-12-12", "sal": 30000}
# del clerk["0001"]
#
#
# clerk["0009"]["sal"] = 50000
# print(clerk)

# for i in keys:
#     clerk[i]['sal'] += clerk[i]['sal'] * 0.2
#     print(clerk[i]["sal"])
# keys = clerk.keys()
# for key in keys:
#     print(
#         f"员工号：{key}年龄：{clerk[key]['age']} 姓名：{clerk[key]['name']} 入职时间：{clerk[key]['entry_time']} 工资：{clerk[key]['sal']}")



