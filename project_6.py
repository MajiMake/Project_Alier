class Project6:
    def __init__(self, stop):
        self.count = 0
        self.amount = 0
        self.stop = stop

    def square_sum(self):
        self.count = 0
        self.amount = 0
        for i in range(1, self.stop + 1):
            self.count = i ** 2
            self.amount += self.count
        return self.amount

    def square_of_sum(self):
        self.count = 0
        self.amount = 0
        for number in range(1, self.stop + 1):
            self.count += number

        self.amount = self.count ** 2
        return self.amount

    def act(self):
        print(self.square_of_sum() - self.square_sum())


proto10 = Project6(10)
proto100 = Project6(100)
proto100.act()