# 确认用户输入的是(Y/N)，不区分大小写如果用户输入的不是Y/N 就反复输入
def read_confirm_select():
    print("请输入你的选择（Y/N）,请确认选择:", end="")
    while True:
        key = input()
        if key.lower() == 'y' or key.lower() == "n":
            break
        else:
            print("选择错误，重新输入：", end="")
    return key.lower()


# 读取用户输入，输入为空则范围default_val

def read_str(tip, default_val):
    str = input(tip)
    if len(str) > 0:
        return str
    else:
        return default_val
