# 业务层：提供对房屋操作的方法

from house import *


class HouseService:
    # 定义属性Houses列表，存放房屋信息（对象）
    houses = []
    # 定义id
    id_counter = 1

    # 根据find_id ,返回对用的house对象,不存在返回None
    def find_by_id(self, find_id):
        for house in self.houses:
            if find_id == house.id:
                return house

    # 根据接受的id删除房屋信息
    def del_by_id(self, del_id):
        house = self.find_by_id(del_id)
        if house is None:
            return False
        self.houses.remove(house)
        return True

    # 接收到的new_house 添加到houses
    def add(self, new_house):
        self.id_counter += 1
        new_house.id = self.id_counter
        self.houses.append(new_house)

    def __init__(self):
        house = House(1, "tim", "118", "北京", 800, "未出组")
        self.houses.append(house)

    def get_houses(self):
        return self.houses
