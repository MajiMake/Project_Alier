# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def polyndrom(n_1, n_2):
    c_1 = n_1 * n_2
    list = str(c_1)
    polyndrom = list[::-1]
    if list == polyndrom:
        return True
    else:
        return False


def counter(c_2=0):
    for number in range(100, 1000):
        for number_2 in range(100, 1000):
            if polyndrom(number, number_2) is True:
                c_1 = number * number_2

                if c_1 > c_2:
                    c_2 = c_1
                    print(c_2)


