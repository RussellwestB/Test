class Game(object):

    #类属性
    num = 0

    #实例对象
    def __init__(self):
        #实例属性
        self.name = "老王"

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100

    #静态方法
    @staticmethod
    def print_menu():
        print("---------------------------")
        print("   穿越火线v11.1")
        print(" 1.开始游戏")
        print(" 2.结束游戏")
        print("---------------------------")


game = Game()
game.add_num()  #可以通过类名调用类方法
#Game.add_num() #还可以通过这个类创建出来的对象 去调用这个类方法
print(Game.num)

#Game.print_menu() #类调用静态方法
game.print_menu() #实例对象调用静态方法

