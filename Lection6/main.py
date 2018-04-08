# Модули и пакеты. Пространства имен (namespaces)
# Подключение модуля
# import module_name

# Подключение модуля из пакета
# import package_name.module_name
# ИЛИ
# from package_name import module_name

# В чем разница?: при обращении к элементам в модуле прописывается разный путь
# Пример: 1-ый случай: obj = package_name.module_name.SomeClass()
#         2-ой случай: obj = module_name.SomeClass()
#

# Для сокращения имен импорта используется конструкция as
# import some_long_module_name_isn_it_mmm as m
# obj = m.SomeClass()
# from some_long_package_name_yea_yeaaaaaaaah_uuuuuuuuuuh import ohhhh_maiiiiii as oh
# obj = oh.SomeClass()

# Популярные модули
# time, requests, sys, os, argparse, postgresql, math, json, random

# Область видимости переменных
# global - глобальные переменные. Доступны из всех мест в программе
# local - локальные переменные. Доступны в том месте, где её определили (в функции, в цикле, в if-else), и во вложенных конструкциях
#  Перестает существовать, когда заканчивается её блок (for, if, func) (область жизни переменной)


# Глобальные переменные - это плохо, откажитесь от сатанинских глобальных переменных,
#       передавайте переменные в функции, спасите себя

a = 3


def foo(a):
    print(a)  # Здесь используется локальна переменная
    print(locals())  # locals() - возвращает словарь локальных перменных
    print(globals())  # globals() - возвращает словарь глобальных переменных


class MyClass:
    def __init__(self):  # Конструктор класса - он собирает из переменных объект и возвращает ссылку на этот объект
        self.a = 100  # Какие-то действия

    def __del__(self):  # Деструктор класса - он очищает память от внутренних
        # объектов класса. Вызывается в момент удаления объекта или в: del some_obj
        pass


# Есть два ключевых слова:
# global и nonlocal
# global var_name: ищет переменную var_name в глобальной области видимости и делает её доступной в текущей области
# nonlocal var_name: ищет переменную var_name в области видимости выше и делает её доступной в текущей области

# Абстрактный класс и абстрактный методы
from abc import ABCMeta, abstractmethod


class SomeAbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def abstract_method(self):
        pass


# Если в классе есть хотя бы один абстрактный метод, то этот класс является абстрактным
# Абстрактные классы - это классы, которые
# Абстрактные методы задают - интерфейс класса.
# Интерфейс класса - методы, которые доступны в классе

# В Java есть отдельная единица, которая называется interface


class SubClass(MyClass):
    def __init__(self):
        super().__init__()  # Или так super(MyClass, self).__init__()
        # Эта конструкция вызывает конструктор супер-класса
        # Для того, чтобы у подкласса в констркуторе появились атрибуты супер класса (т.к. подкласс наследует атрибуты)

    @staticmethod  # статические методы вызываются через имя класса: SubClass.some_static_method()
    def some_static_method():
        # Статические методы не имеют в аргументах self
        # Статические методы должны работать только со статическими переменными (в целях безопасности)
        pass

    #   "Перегрузка" операторов
    def __add__(self, other):  # obj+7
        self.a += other

    def __sub__(self, other):  # obj-7
        self.a -= other

    def __mul__(self, other):  # obj*87
        self.a *= other

    def __truediv__(self, other):  # obj/87
        self.a /= other

    def __pow__(self, power, modulo=None):  # obj**3
        self.a **= power

    # Имеются аналоги с приставками i и r
    # __iadd__ obj+=45
    # __radd__ 45+obj
    # приставки доступны для других простых математических операций


if __name__ == '__main__':
    global a
    print(locals())
    print(globals())
    foo(100500)
    from twisted.internet.endpoints import TCP4ClientEndpoint

    print(
        TCP4ClientEndpoint.__mro__)  # __mro__ - возвращает список супер-классов (классов, от которых наследуется класс)
