import sys


class UserInfo:

    def __init__(self, name, number):
        self.name = name
        self.number = number


class AddressBook:

    def __init__(self):
        self.users = []

    def add(self, node: UserInfo):
        self.users.append(node)

    def select_by_name(self, name):
        for i in range(len(self.users)):
            if self.users[i].name == name:
                return self.users[i]
        return None

    def remove_by_name(self, name) -> bool:
        index = -1
        for i in range(len(self.users)):
            if self.users[i].name == name:
                index = i
                break
        if index == -1:
            return False
        del self.users[index]
        return True

    def display(self):
        for i in range(len(self.users)):
            print(self.users[i].name + "--" + self.users[i].number)


def exit():
    sys.exit()


if __name__ == '__main__':
    address = UserInfo(name="张三", number="12324")
    exit()
    print(1)