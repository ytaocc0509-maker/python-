"""
提供房屋的各种操作
"""

from my_tools import *


def main_menu():
    print()
    print("房屋出租系统菜单")
    print("\t\t\t1 新增房源")
    print("\t\t\t2 查找房物")
    print("\t\t\t3 删除房屋信息")
    print("\t\t\t4 修改房屋信息")
    print("\t\t\t5 房屋列表")
    print("\t\t\t6 退出")


# 全局变量houses,存放所有的房屋信息

houses = [{"id": 1, "name": "tim", "phone": "234", "address": "广东", "rent": "800", "state": "未出租"}]


# 显示房屋列表
def list_houses():
    print("房屋列表".center(60, "="))

    # 打印表头信息
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（已出租/未出租）")

    # 遍历houses列表
    for house in houses:
        for value in house.values():
            print(value, end="\t\t")

        print()
    print("房屋列表显示完毕")


# 全局变量id_counter 记录当前房屋的id
id_counter = 1


# 添加房屋信息
def add_house():
    print("添加房屋".center(32, "="))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = input("租金：")
    state = input("状态：")
    # 由系统分配添加的id
    global id_counter
    id_counter += 1
    # 构建房屋信息对应的字典，加入到全局的房屋列表
    house = {"id": id_counter, "name": name, "phone": phone, "address": address, "rent": rent, "state": state}
    houses.append(house)
    print("添加房屋成功".center(32, "="))


# 完成退出系统，并y/n确认
def exit_sys():
    choice = read_confirm_select()

    if choice == 'y':
        return True
    else:
        return False


# 根据id查找房屋
def find_by_id(find_id):
    for house in houses:
        if house["id"] == find_id:
            return house

    return None


# 根据id查找房屋，返回对应房屋信息
def find_house():
    print("查找房屋信息".center(32, "="))
    house_id = int(input("请输入查找的房屋id："))
    # 调用函数范围对用的房屋
    house = find_by_id(house_id)
    if house:
        # 打印表头信息
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（已出租/未出租）")
        for value in house.values():
            print(value, end="\t\t")

    else:
        print(f"房屋id{house_id}不存在：")


# 修改房屋信息
def update_house_info():
    print("修改房屋信息".center(32, "="))
    house_id = int(input("请选择修改房屋的编号（-1表示退出）："))
    if house_id == -1:
        print("放弃修改房屋信息".center(32, "="))
        return

    house = find_by_id(house_id)
    if not house:
        print("修改房屋编号不存在".center(32, "="))
        return

    house["name"] = read_str(f"姓名{house['name']}：", house["name"])
    house['phone'] = read_str(f"姓名{house['phone']}：", house["phone"])
    house['address'] = read_str(f"姓名{house['address']}：", house["address"])
    house['rent'] = read_str(f"姓名{house['rent']}：", house["rent"])
    house['state'] = read_str(f"姓名{house['state']}：", house["state"])
    print("修改房屋信息成功".center(32, "="))


def del_house():
    # 删除房屋信息
    print("删除房屋信息：".center(32, "="))
    del_id = int(input("请输入删除房屋编号(-1退出)："))

    if del_id == -1:
        print("放弃删除房屋".center(32, "="))
        return
    # 确认删除
    choice = read_confirm_select()

    if choice == 'y':
        house = find_by_id(del_id)
        if house:
            houses.remove(house)
            print("删除房屋信息：".center(32, "="))
        else:
            print("房屋不存在，删除失败：".center(32, "="))

    else:
        print("放弃删除房屋信息：".center(32, "="))
