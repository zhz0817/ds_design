class HashMap:

    def __init__(self):
        self.capacity = 16  # 容量
        self.nums = [-1] * self.capacity
        self.key = 11
        self.load_factor = 0.75  # 负载因子
        self.length = 0

    def display(self):
        for n in self.nums:
            if n != -1:
                print(n)

    def find(self, value):
        index = value % self.key
        while index < self.capacity:
            if self.nums[index] == value:
                return index
            index += 1
        return -1

    def insert(self, value) -> bool:
        if self.length == self.capacity:
            return False
        index = value % self.key
        while True:
            if self.nums[index] == -1:
                self.nums[index] = value
                self.length += 1
                return True
            index += 1
            if index >= self.capacity:
                index -= self.capacity

    def remove(self, value) -> bool:
        if self.length == 0:
            return False
        index = value % self.key
        while True:
            if self.nums[index] == value:
                self.nums[index] = -1
                self.length -= 1
                return True
            index += 1
            if index >= self.capacity:
                index -= self.capacity


if __name__ == '__main__':
    hashmap = HashMap()
