# #abc.txt 文件，并写入10句"hello,123”到文件在d盘的a目录下创建
# f = open("d://a//abc.txt", "w", encoding="utf-8")
#
# i = 1
# while i <= 10:
#     f.write("hello,123\n")
#     i += 1
#
# f.close()
#
# #将abc.txt 内容覆盖成新的内容10句“hi，123”
#
# i = 1
# while i <= 10:
#     f.write("hi,123\n")
#     i += 1
#
# f.close()
#
#
# #在abc.txt 原有内容基础上追加10句'你好!python'，mod? 指定为"a“追加模式
# f = open("d://a//abc.txt", "a", encoding="utf-8")
# i = 1
# while i <= 10:
#     f.write("hi,python\n")
#     i += 1
#
# f.close()
# import os
#
# # 判断在d盘的a目录下是否有 abc.txt 文件，如果有则删除
# # 如果没有，则提示“文件不存在，无法删除"
#
# if os.path.exists("d://a//abc.txt"):
#     os.remove("d://a//abc.txt")
# else:
#     print("不存在")

# # 创建一级目录 d://aaa
#
# import os
#
# if not (os.path.isdir("d://aaa")):
#     os.mkdir("d://aaa")
# else:
#     print("d://aaa目录已存在")
#
# # 创建多级目录 d://bbb//ccc
#
# if not (os.path.isdir("d://bbb//ccc")):
#     os.makedirs("d://bbb//ccc")
# else:
#     print("d://bbb//ccc目录已存在")
# # 删除多级目录使用removedirs,要求目录为空
# if os.path.isdir("d://bbb//ccc"):
#     os.removedirs("d://bbb//ccc")
# else:
#     print("d://bbb//ccc目录不存在")

# 获取文件相关信息(大小、创建时间、访问时间、修改时间等)
# import os
# import time
#
# f_start = os.stat("d:/Python_Code/Hello/hello.py")
# print(f"文件大小{f_start.st_size}")
# print(f"最近访问时间{time.ctime(f_start.st_atime)}")
# print(f"最近修改时间{time.ctime(f_start.st_mtime)}")
# print(f"文件创建时间{time.ctime(f_start.st_ctime)}")

# 说明:将一张图片/一首歌 拷贝到另外一个目录下,要求使用read()和write()原生方法完成

# f = open("d:/a/黑神话.png", "rb")
# content = f.read()
#
# d = open("d:/b/黑神话1.png", "wb")
# d.write(content)
# f.close()
# d.close()
# print("ok")
#
# # 我们再使用with子句的方式完成文件拷贝(读取一行数据，就写入)
#
# with open("d:/a/黑神话.png", "rb") as f:
#     with open("d:/b/黑神话3.png", "wb") as d:
#         for data in f:
#             d.write(data)
# import os
#
# list_a = os.listdir("d:/a")
# path = "d:/a"
# for ele in list_a:
#     if os.path.isdir(path + '/' + ele):
#         print(f"目录{path + '/' + ele}")
#     else:
#         print(f"文件{path + '/' + ele}")



