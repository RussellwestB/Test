import tensorflow as tf
import os

list = os.listdir("./")
print(list)
old_name = input('请输入要复制的文件名：\n')

old_name_file  = open(old_name,"r")
#new_name_file = open('test.text',"w")
position = old_name.rfind('.')
new_file_name =  old_name[:position] + '[复件]' + old_name[position:]
new_name_file = open(new_file_name,"w")
context = old_name_file.read()
new_name_file.write(context)

old_name_file.close()
new_name_file.close()
