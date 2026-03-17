from login_log_operation import *


def main():
    while True:
        name = input("请输入用户名:")
        password = input("请输入密\t码:")
        if login(name, password):
            break
        print("用户名或密码错误")

    # 调用main_menu函数显示主菜单
    while True:
        print("=======请选择操作========：")
        main_menu()
        key = input("请输入你的选择：")
        if key in ["1", "2", "3"]:
            if key == "1":
                print(name)
            elif key == "2":
                read_log()
                pass
            elif key == "3":
                print("退出...")
                break


# 测试
if __name__ == "__main__":
    main()
    print("你退出了程序")
