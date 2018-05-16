# try:
#     pass  # Код, который возбуждает исключение
# except:
#     pass  # Код, который выполнится при отлове исключения
# else:
#     pass  # Код, который выполнится, если исключения не было
# finally:
#     pass  # Код, который выполнится в любом случае
#
# # except ExceptionName:
# # except ExceptionName as err:
# #   print(err.__name__)
# from typing import Any
#
#
# class MyException(BaseException):
#
#     def __init__(self, *args: object, **kwargs: object) -> None:
#         super().__init__(*args, **kwargs)
#
#     def with_traceback(self, tb: Any) -> BaseException:
#         return super().with_traceback(tb)
#
#
# if __name__ == '__main__':
#     input_num = int(input("Введите число: "))
#     input_num_delitel = int(input("Введите делитель: "))
#     try:
#         print("{0}/{1} = {2}".format(input_num, input_num_delitel, input_num / input_num_delitel))
#         raise MyException("Я злой")
#     except MyException as err:
#         print(err.__str__())
#     except ZeroDivisionError as err:
#         print(err.__str__())
#         print("Лох - это судьба!!! =(")


# def foo(a):
#     print(a)


if __name__ == '__main__':
    # pFunc = foo
    # pFunc(3)
    # b = print
    # print(print(print(print(print(1)))))
    # b(b(b(b(b(1)))))
    pFunc = lambda x, y: x ** y
    print(pFunc(3, 3))
    res = list(map(lambda x: x ** 2, [1, 2, 3]))
    for x, y, z in zip([1, 2, 3], [10, 20, 30], [100, 200, 300]):
        print(x, y, z)

    a = [-1, 2, -3, 4]
    a = list(filter(lambda x: x > 0, a))
    print(a)
    a = [-199,-1, 2, -3, -4, -100]
    print(a)
    a.sort(key=lambda a: abs(a))
    print(a)
    # for _ in range(100):
    #     print()
