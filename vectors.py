class Vector_calc:
    def __init__(self, *args, **kwargs):
        self.b2 = args[4]
        self.a2 = args[1]
        self.a1 = args[0]
        self.b1 = args[3]
        self.a3 = args[2]
        self.b3 = args[5]
        self_sum = kwargs

    if self.a3 is None:
        def vector_calc(self):
            if self.sum == '+':
                first_sum = self.a1 + self.b1
                second_sum = self.a2 + self.b2
                return '({},{})'.format(first_sum, second_sum)  # добавить вторую функцию для 3х векторов
            elif self.sum == '-':
                first_sum = self.a1 - self.b1
                second_sum = self.a2 - self.b2
                return '({},{})'.format(first_sum, second_sum)
            elif self.sum == '*':
                first_sum = self.a1 * self.b1
                second_sum = self.a2 * self.b2
                return '({},{})'.format(first_sum, second_sum)
            elif self.sum == '/':
                first_sum = self.a1 // self.b1
                second_sum = self.a2 // self.b2
                return '({},{})'.format(first_sum, second_sum)
    else:
        def vector_calc_v3(self):
            if self.sum == '+':
                first_sum = self.a1 + self.b1
                second_sum = self.a2 + self.b2
                third_sum = self.a3 + self.b3
                return '({},{},{})'.format(first_sum, second_sum, third_sum)  # добавить вторую функцию для 3х векторов
            elif self.sum == '-':
                first_sum = self.a1 - self.b1
                second_sum = self.a2 - self.b2
                third_sum = self.a3 - self.b3
                return '({},{},{})'.format(first_sum, second_sum, third_sum)
            elif self.sum == '*':
                first_sum = self.a1 * self.b1
                second_sum = self.a2 * self.b2
                third_sum = self.a3 * self.b3
                return '({},{},{})'.format(first_sum, second_sum, third_sum)
            elif self.sum == '/':
                first_sum = self.a1 // self.b1
                second_sum = self.a2 // self.b2
                third_sum = self.a3 // self.b3
                return '({},{},{})'.format(first_sum, second_sum, third_sum)
