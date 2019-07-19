class Dog(object):
    def __init__(self): #初始化
        print("-----init方法----")

    def __del__(self):
        print("-----del方法-----")

    def __str__(self):
        print("------str方法----")

    def __new__(cls): #创建对象
        print("----new方法------")
        return object.__new__(cls)


xtq = Dog() #相当于要做三件事，调用new方法创建对象，然后找了一个变量来接收__new__的返回值（表示创建对象的引用），调用__init__(创建对象的引用)