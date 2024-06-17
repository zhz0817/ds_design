from typing import Any


class Student:

    def __init__(self, name, sno, cname, grade):
        self.name = name
        self.sno = sno
        self.cname = cname
        self.grade = grade


def select(stu_list, name) -> Any | None:
    for stu in stu_list:
        if stu.name == name:
            return stu
    return None


def delete(stu_list, name) -> bool:
    index = 0
    for stu in stu_list:
        if stu.name == name:
            break
        index += 1
    if index == len(stu_list):
        return False
    del stu_list[index]
    return True


def update(stu_list, name, attribute, value):
    for stu in stu_list:
        if stu.name == name:
            setattr(stu, attribute, value)
            return True
    return False


if __name__ == '__main__':
    student_list = []
    stu1 = Student(name="张三", sno="100", cname="数据结构", grade=100)
    student_list.append(stu1)
    update(student_list, "张三", "grade", 99)
