class Dog(object):

    __instance = None

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # return上一次创建的对象的引用
            return cls.__instance

    def __init__(self, name):
        self.name = name


a = Dog("旺财")
print(id(a))
print(a.name)
b = Dog("哮天犬")
print(id(b))
print(b.name)
