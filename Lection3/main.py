from math import sqrt


def polnyi_kvadrat(a, b, c):
    D = b ** 2 - 4 * a * c
    if (D > 0):
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
    elif (D < 0):
        x1, x2 = None, None
    else:
        x1 = -b / (2 * a)
        x2 = x1
    return x1, x2


# def factorial(num):
#     fact = 1
#     for n in range(num,1,-1):
#         fact*=n
#     return fact

# def factorial(num):
#     if (num == 0):
#         return 1
#     else:
#         return num * factorial(num - 1)

def foo():
    pass

if __name__ == '__main__':
    # print(polnyi_kvadrat(2, 4, 8))
    # print(polnyi_kvadrat(8, 4, -2))
    # print(polnyi_kvadrat(4, 4, 1))
    # print(factorial(10))
    print(type(foo()))