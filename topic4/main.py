class Account:
    def __init__(self):
        self.dict1 = {}

    def add(self, name, money) -> bool:
        if name in self.dict1:
            return False
        self.dict1[name] = money
        return True

    def remove(self, name) -> bool:
        if name not in self.dict1:
            return False
        del self.dict1[name]
        return True

    def store(self, name, money) -> bool:
        if name not in self.dict1:
            return False
        self.dict1[name] += money
        return True

    def spend(self, name, money) -> bool:
        if name not in self.dict1:
            return False
        value = self.dict1[name]
        if value < money:
            return False
        self.dict1[name] = value - money
        return True


if __name__ == '__main__':
    account = Account()
