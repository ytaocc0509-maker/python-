# 工具类，将工具方法写到这

class Utility:
    @staticmethod
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
    @staticmethod
    def read_str(tip, default_val):
        str = input(tip)
        if len(str) > 0:
            return str
        else:
            return default_val

