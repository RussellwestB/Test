#encoding = utf-8
import  hello as hellott

class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获开启, 已经捕获到了异常，信息如下：")
            else:
                # 重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理
                raise

try:
    open("xxx.txt")
    print("---1--------")
except (NameError,FileNotFoundError):
    print("该文件不存在,名称错误")
    

a = Test(True)
a.calc(11, 0)
print("------------------------------华丽的分割线----------------")