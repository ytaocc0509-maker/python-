# list1 = [1, 2, 3, 4]
# tuple_a = (1, 2, 3, 4)
# print(list1[1])
# print(tuple_a[2])
# list2 = tuple()
# print(type(list2))

# while元组的遍历

# tuple_color = ("white", "red", "blue", "yellow", "black")
#
# count = 0
# while count < len(tuple_color) :
#     print(tuple_color[count])
#     count += 1

# for元组的遍历
# tuple_color = ("white", "red", "blue", "yellow", "black")
#
# for ele in tuple_color:
#     print(ele)

# tuple_a = (1, 2, 3, [1, 2, 3, ])
#
# print(type(tuple_a[3]))

# tuple_a = (1, 2, 3, [1, 2, 3])
#
# tuple_a[4][1] = [1, 2]

# list_a = [1,2,(1,2)]
# list_a[2] = 3
# print(list_a)

# tuple_a = (1,)
# print(type(tuple_a))

# 定义一个元组,('大话西游’，'周星驰',80，['周星驰'，'小甜甜’]),信息为(片名,导演,票价,演员列表)
# 1)查询票价对应索引
# 2)遍历所有的演员
# 3)删除'小甜甜'增加 演员'牛魔王'、"猪八戒”

# tuple_a = ("大话西游", "周星驰", 80, ["周星驰", "小甜甜"],)
# print("票价的索引值：", tuple_a.index(80))
#
# for actor in tuple_a[3]:
#     print("演员：", actor)
#
# del tuple_a[3][1]
# tuple_a[3].append("牛魔王")
# tuple_a[3].append("猪八戒")
#
# print(tuple_a[3])

# 定义一个字符串，str names="tom jack mary nono smith hsp
# 统计一共有多少个人名
# 如果有"hsp"则替换成"老韩"
# 如果人名是英文，则把首字母改成大写

# str_names = "tom jack mary nono smith hsp"
# str_names_list = str_names.split(" ")
# print(f"一共有{len(str_names_list)}人名")
#
# str_names_new = str_names.replace("hsp", "老韩")
# print(str_names_new)
#
# str_names_upper = ""
# for ele in str_names_list:
#     if ele.isalpha():
#         str_names_upper += ele.capitalize() + " "
#
# print(str_names_upper)

# str ="1234"
# srt_slice=str[-1:-5:1]
# print(srt_slice)

# 定义列表 fist_name = ["Jack","Lisa","Hsp","Pau!","smith","Kobe"]
# 取出前三个名字取出后三个名字，
# 并且保证原来顺序
# fist_name = ["Jack", "Lisa", "Hsp", "Pau!", "smith", "Kobe"]
# fist_name_slice_a = fist_name[0:3:1]
# print(fist_name_slice_a)
#
# fist_name_slice_b = fist_name[-1:-4:-1]
# fist_name_slice_b.reverse()
# print(fist_name_slice_b)


# set_a = {1,2,3,4,5,6,0,9,"123","321","aaa"}
# print(type(set_a))
# for set_value in set_a:
#     print(set_value)

# 用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)
# s_history = {'小明'"张三”,'李四’"王五”,'Lily',"Bob"}
# s_politic ={'小明’"小花”，'小红’"二狗"}
# s_english = {'小明’,'Lily',"Bob","Davil","李四"}

# 求选课学生总共有多少人
# 求只选了第一个学科的学生数量和学生名字
# 求只选了一门学科的学生数量和学生名字
# 求选了三门学科的学生数量和学生名字

s_history = {"小明", "张三", "李四", "王五", "Lily", "Bob"}
s_politic = {"小明", "小花", "小红", "二狗"}
s_english = {"小明", "Lily", 'Bob', 'Davil', '李四'}

s_total_sum = s_history | s_politic | s_english
print(f"学生总人数为：{len(s_total_sum)}")

s_history_only = s_history - s_politic - s_english
print(f"只选了第一门学科的学生为：{s_history_only}只选了第一个学科的人数是{len(s_history_only)}")

s_politic_only = s_politic - s_history - s_english
s_english_only = s_english - s_politic - s_history

s_subject_one = s_english_only | s_politic_only | s_history_only

print(f"只选了一门学科的学生为：{s_subject_one}只选了一个学科的人数是{len(s_subject_one)}")

print(f"选了三门学科的学生为：{s_history & s_politic & s_english}")
