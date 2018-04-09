#2018-04-09 13:20
from sys import argv

#参数的使用
number = 7
print ("Hello World! \n计算题：",end='')
print ("计算结果 25+42/7=",25+42/float(number))

#格式化输出
my_height = 74 
print ("我的身高: %d" %(my_height))

filename = argv
print ("当前文件位置：",filename)

#读取当前文件内容并显示出来
print ("下面显示本文件的内容：")
txt = open(argv[0], encoding='UTF-8')
print (txt.read())
