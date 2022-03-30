def square_sum(c = 0):
    for n in range(1,11):
        q = c + n**2
    print(q)

def square_of_sum(c = 0):
    for n in range(1,11):
        c += n

    q = c**2
    print(q)


square_sum()
square_of_sum()