# 显示菜单
import time


def main_menu():
    print("1\t查\t看\t当\t前\t登\t录\t用\t户")
    print("2\t查\t看\t登\t录\t日\t志")
    print("3\t退\t出\t系\t统")


list_user_name = ["smith", "tom", "tim"]

list_log = []


# 记录登录日志
def save_log(info):
    with open("d:/a/log.txt", "a", encoding="utf-8") as f:
        f.write(info)


# 读取日志
def read_log():
    with open("d:/a/log.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line)


# 登录验证和记录
def login(name, passwrod):
    try:
        if list_user_name.index(name) or passwrod == "888":
            print("登录成功")
            info = f"登录用户:{name},登录成功 登录时间:{time.strftime('%m-%d %H:%M:%S', time.localtime())}\n"
            # list_log.append(info)
            save_log(info)
            return 1
    except Exception as e:
        info = f"登录用户:{name},登录失败 登录时间:{time.strftime('%m-%d %H:%M:%S', time.localtime())}\n"
        # list_log.append(info)
        save_log(info)
        return None
