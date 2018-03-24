def deco(func):
    print("Hello {0}".format(func.__name__))
    return func


@deco
def my_func(a, b, c):
    print("Call my_func")


class MyClass:
    def __init__(self, a=0, b=10):  # Конструктор
        self.a = a  # self.a - атрибут класса MyClass, a - аргумент метода
        self.b = b
        self.pub = 0
        self._prot = 10
        self.__priv = 100

    def getA(self):  # Геттер
        return self.a

    def setA(self, a):  # Сеттер
        self.a = a

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b


if __name__ == '__main__':
    my_func(1, 2, 3)
    obj = MyClass()
    print(obj._prot)
    print(obj.pub)
    print(obj.__priv)
    print(obj._MyClass__priv)
