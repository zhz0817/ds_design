from datetime import date
from typing import List


class Worker:
    def __init__(self, name, gender, birthday, workday, education, business, address, phone):
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.workday = workday
        self.education = education
        self.business = business
        self.address = address
        self.phone = phone

    def __eq__(self, __value):
        if isinstance(__value, Worker):
            return (self.name == __value.name and self.gender == __value.gender and self.birthday == __value.birthday
                    and self.workday == __value.workday and self.education == __value.education
                    and self.business == __value.business and self.address == __value.address
                    and self.phone == __value.phone)
        return False

    def __hash__(self):
        return hash((str(self.name), str(self.gender), str(self.birthday), str(self.workday), str(self.education),
                     str(self.business), str(self.address), str(self.phone)))

    def __str__(self):
        return super().__str__()


def add(worker: Worker, dict1: dict):
    dict1[worker] = 1


def delete(worker: Worker, dict1: dict):
    del dict1[worker]


def find_by_attribute(list1: List[Worker], attribute, value):
    for i in range(len(list1)):
        if getattr(list1[i], attribute) == value:
            return list1[i]
    return None


def update_by_attribute(list1: List[Worker], attribute, value1, value2) -> bool:
    for i in range(len(list1)):
        if getattr(list1[i], attribute) == value1:
            setattr(list1[i], attribute, value2)
            return True
    return False


def order_by_attribute(list1: List[Worker], attribute, order):
    sorted_list = sorted(list1, key=lambda x: getattr(x, attribute),reverse=order)
    if order == "desc":
        sorted_list.reverse()


if __name__ == '__main__':
    dict1 = {}
    worker1 = Worker(name="张三", gender="male", birthday=date(2004, 6, 16),
                     workday=date(2024, 6, 16), education="本科", business="科员", address="沈阳大街",
                     phone="123456")
    worker2 = Worker(name="张三", gender="male", birthday=date(2005, 6, 16),
                     workday=date(2024, 6, 16), education="本科", business="科员", address="沈阳大街",
                     phone="123457")
    add(worker1, dict1)
    add(worker2, dict1)
    list1 = list(dict1.keys())
    order_by_attribute(list1, attribute="phone", order=True)
    # update_by_attribute(list1, "name", "张三", "李四")
    # ans = find_by_attribute(list1, "name", "李四")
    # print(ans.phone)
