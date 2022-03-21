# Каждый следующий элемент ряда Фиббоначи получается при сложении двух предыдущих. Начиная с 1 и 2
# Первые 10 эелементов будут 1 2 3 5 8 13 21 34 55 89
# Найти сумму всехъ четных элементов ряда Фибоначчи, которые не превышают четыре миллиона

# def Fibonacci():
#     ante = 0
#     post = 1
#     amount = 0
#
#     for _ in range(10):
#         if ante % 2 == 0:
#             amount += ante
#         ante, post = post, ante + post
#     return amount
#
# print(Fibonacci())



class Fibonacci:

    def __init__(self, number):
        self.counter, self.ante, self.post, self.number = 0, 0, 1, number

    def __iter__(self):
        self.counter, self.ante, self.post = 0, 0, 1
        return self


    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration()
            self.ante, self.post = self.post, self.ante + self.post
            return self.ante


fib = Fibonacci(number = 10000)

print(88 in fib)