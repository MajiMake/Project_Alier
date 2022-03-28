import time


def devider(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def counter():
    n = 1
    while devider(n) is False:
        n += 1
    print(n)


started_at = time.time()
counter()
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
minuts = round(elapsed / 60, 4)
hours = round(minuts / 60, 4)
if elapsed >= 60:
    if minuts >= 60:
        print(f'Функция работала{hours} часов')
    else:
        print(f'Функция работала{minuts} минут')
else:
    print(f'Функция работала{elapsed} секунд')



