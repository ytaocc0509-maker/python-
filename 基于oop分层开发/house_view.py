# 界面层：显示界面,接受用户的输入，调用业务层的方法

from house_service import *
from utility import *

class HouseView:
    house_operation: HouseService = HouseService()

    # 根据输入的id修改房屋信息
    def update_house_info(self):
        print("修改房屋信息".center(32, "="))
        house_id = int(input("请选择修改房屋的编号（-1表示退出）："))
        if house_id == -1:
            print("放弃修改房屋信息".center(32, "="))
            return

        house = self.house_operation.find_by_id(house_id)
        if not house:
            print("修改房屋编号不存在".center(32, "="))
            return

        house.name = Utility.read_str(f"姓名{house.name}：", house.name)
        house.phone = Utility.read_str(f"姓名{house.phone}：", house.phone)
        house.address = Utility.read_str(f"姓名{house.address}：", house.address)
        house.rent = Utility.read_str(f"姓名{house.rent}：", house.rent)
        house.state = Utility.read_str(f"姓名{house.state}：", house.state)
        print("修改房屋信息成功".center(32, "="))

    # 根据输入的id查询返回房屋信息
    def find_house_info(self):
        print("查找房屋信息".center(32, "="))
        house_id = int(input("请输入查找的房屋id："))
        # 调用函数范围对用的房屋
        house = self.house_operation.find_by_id(house_id)
        if house:
            # 打印表头信息
            print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（已出租/未出租）")
            # for value in house.values():
            #     print(value, end="\t\t")
            print(house)

        else:
            print(f"房屋id{house_id}不存在：")

    # 退出系统
    def exit_sys(self):
        key = Utility.read_confirm_select()
        if key == "y":
            return True
        else:
            return False

    # 删除房屋信息，接受用户的的输入
    def del_house(self):
        # 删除房屋信息
        print("删除房屋信息：".center(32, "="))
        del_id = int(input("请输入删除房屋编号(-1退出)："))

        if del_id == -1:
            print("放弃删除房屋".center(32, "="))
            return
        # 确认删除
        choice = Utility.read_confirm_select()

        if choice == 'y':
            # 调用service层的删除方法
            if self.house_operation.del_by_id(del_id):
                print("删除房屋信息：".center(32, "="))
            else:
                print("房屋不存在，删除失败：".center(32, "="))

        else:
            print("放弃删除房屋信息：".center(32, "="))

    # 接受用户的输入，添加方法无心
    def add_house(self):
        print("添加房屋".center(32, "="))
        name = input("姓名：")
        phone = input("电话：")
        address = input("地址：")
        rent = input("租金：")
        state = input("状态：")

        # 构建房屋信息对象
        new_house = House(0, name, phone, address, rent, state)
        #
        self.house_operation.add(new_house)
        print("添加房屋成功".center(32, "="))

    def list_houses(self):
        print("房屋列表".center(60, "="))

        # 打印表头信息
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（已出租/未出租）")

        houses = self.house_operation.get_houses()

        for house in houses:
            print(house)

        print()
        print("房屋列表显示完毕")

    def main_menu(self):

        while True:
            print()
            print("房屋出租系统菜单")
            print("\t\t\t1 新增房源")
            print("\t\t\t2 查找房物")
            print("\t\t\t3 删除房屋信息")
            print("\t\t\t4 修改房屋信息")
            print("\t\t\t5 房屋列表")
            print("\t\t\t6 退出")
            key = input("请输入你的选择（1-6）：")
            if key in ["1", "2", "3", "4", "5", "6"]:
                if key == "1":
                    HouseView().add_house()
                elif key == "2":
                    self.find_house_info()
                elif key == "3":
                    self.del_house()
                elif key == "4":
                    self.update_house_info()
                elif key == "5":
                    HouseView().list_houses()
                elif key == "6":

                    if self.exit_sys():
                        break
