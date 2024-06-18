import copy
from typing import List


class Student:

    def __init__(self, sno, sname):
        self.sno = sno
        self.sname = sname
        self.dno = None


class Dormitory:

    def __init__(self, n, dno):
        self.n = n  # 宿舍最大人数
        self.dno = dno
        self.std_list = []

    def add(self, student: Student):
        if len(self.std_list) < self.n:
            student.dno = self.dno
            self.std_list.append(student)
            return True
        return False


def sort_by_name(std_list: List[Student]):
    s = copy.deepcopy(std_list)
    for i in range(len(s))[::-1]:
        for j in range(0, i):
            if s[j].sname > s[j + 1].sname:
                s[j + 1], s[j] = s[j], s[j + 1]
    return s


def sort_by_sno(std_list: List[Student]):
    pass


def sort_by_dno(std_list: List[Student]):
    pass


def select_by_dno(std_list: List[Student], dno):
    pass


def select_by_sno(std_list: List[Student], sno):
    pass


def select_by_name(std_list: List[Student], name):
    left = 0
    right = len(std_list)-1
    while left <= right:
        mid = left + (right-left)//2
        if std_list[mid].sname == name:
            return std_list[mid]
        elif std_list[mid].sname < name:
            left = mid+1
        else:
            right = mid-1
    return None


def write_to_file(path, info):
    with open(path, 'w') as f:
        for item in info:
            f.write(item + "\n")


if __name__ == '__main__':
    std = Student(sno="123", sname="张三")
    dormitory = Dormitory(4, 1)
    dormitory.add(std)
    print(std.dno)
    dormitory_list = [dormitory]
    std_list = []
    for i in range(len(dormitory_list)):
        for j in range(len(dormitory_list[i].std_list)):
            std_list.append(dormitory_list[i].std_list[j])
    list1 = sort_by_name(std_list)
    select_by_name(list1, "张三")
