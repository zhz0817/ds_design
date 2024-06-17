class Parking:
    def __init__(self, n):
        self.n = n
        self.stack = []
        self.queue = []

    def park(self, number, time):
        if len(self.stack) == self.n:
            self.queue.append([number, time])
            print("便道")
        else:
            self.stack.append([number, time])
            print("停车场")

    def un_park(self, number, time):
        index = -1
        for i in range(len(self.stack)):
            if self.stack[i][0] == number:
                index = i
                break
        if index == -1:
            for i in range(len(self.queue)):
                if self.queue[i] == number:
                    index = i
            self.queue.pop(index)
            print("车"+str(number)+"已经开走，收费为0")
        else:
            info = self.stack[index]
            self.stack.pop(index)
            if len(self.queue) > 0:
                front = self.queue[0]
                self.queue.pop(0)
                self.stack.append(front)
            cost = (time - info[1]) * 5
            print("车"+str(number)+"已经开走，收费为"+str(cost))

if __name__ == '__main__':
    p = Parking(10)
    s = [['A', 1, 5], ['D', 1, 20]]
    for i in range(len(s)):
        info = s[i]
        if info[0] == 'A':
            p.park(info[1], info[2])
        else:
            p.un_park(info[1], info[2])
