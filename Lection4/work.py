import random


def func(x):
    if x >= 0:
        return x ** 2
    return x


"""
Задание: Заполнить список рандомными целыми числами, потом каждое положительное число возвести в квадрат
"""

if __name__ == '__main__':
    # Первый вариант (в функциональном стиле)
    a = list()
    for i in range(20):
        a.append(random.randint(-50, 50))
    print(a)
    a = list(map(func, a))
    print(a)

    print()
    # Второй вариант (в процедурном стиле)
    a = list()
    for i in range(20):
        a.append(random.randint(-50, 50))
    print(a)
    for i in range(len(a)):
        if a[i] >= 0:
            a[i] **= 2
            # a[i] = a[i] ** 2 Аналогичная запись
    print(a)

