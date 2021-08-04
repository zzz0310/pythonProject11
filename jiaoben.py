'''99乘法表'''
# for x in range(1,10):
# #x=[1,2,3,4,5,6,7,8,9]
#     for y in range(1,x+1):
# #当x=1时，y=[1]
# 当x=2时，y=[1,2]
#         print("%s*%s=%s" % (y,x,x*y),end=" ")
#
#     print()

'''yaml文件的读写'''
from ruamel import yaml
#读出test.yaml的数据
with open('test.yaml', 'r', encoding='utf-8') as f:
	print(yaml.load(f.read(),Loader=yaml.Loader))

# def yaml_load(file):
# 	from ruamel import yaml
# 	with open(file, 'r', encoding='utf-8') as f:
# 		print(yaml.load(f.read(), Loader=yaml.Loader))

# yaml_load(user.yaml)

#追加数据写进test.yaml，覆盖把a改为w
# list=[4,5,6,]
# with open("test.yaml","a",encoding="utf-8") as f:
#     yaml.dump(list,f,Dumper=yaml.RoundTripDumper)

'''将字符串转换列表'''
# image ='1.jsp,2.jsp,3.jsp,4.jsp'
# image_list = image.strip(',').split(',')
# print(image_list)

'''多个同元素取下标'''
#例子
# a = ["aa","bb","aa","cc","aa","dd","bb","aa","cc"]
# b = a.count("aa")
# c = -1
# for i in range(b):
#     c = a.index("aa",c+1,len(a))
#     print("aa",c)
#函数
# def indexs(lis,value):
# 	num = lis.count(value)
# 	num1 = -1
# 	result = []
# 	for i in range(num):
# 		num1 = lis.index(value,num1+1,len(lis))
# 		result.append(num1)
# 	return result



#
'''直接取值后放入列表'''
#list_0 = [x for x in range(5)]
# print(list_0)

'''函数：a，b，c是必须参数，d=1为默认参数，当只传三个参数时，d默认=1，*arge和**arge是不定长参数，可以不传，
也可以传多个参数，*arge接收必须参数接收完之外的位置参数，以元祖的形式保存，**kwarge接收必须参数接收之外的关键字参数，以
字典的形式保存
'''
# def add_num(a,b,c,d=1,*args,**kwargs):
#     print('a的值',a)
#     print('b的值',b)
#     print('c的值',c)
#     print('d的值',d)
#     print(args)
#     print(kwargs)
#     return a+b+c
# add_num(1,2,3,4,5,6,gg=11,hh=22)

'''拆包'''
# def func():
#     return 11,22,33
# res = func()
# print(res)
# a,b,c = func()
# print(a)
# print(b)
# print(c)

# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# #利用*对元祖拆包：只能在函数调用的时候去使用
# func(*(1,2,3))
# tu =(1,2,3)
# func(*tu)
# #利用**对字典拆包
# func(**{'a':11,'b':22,'c':33})
# dic = {'a':11,'b':22,'c':33}
# func(**dic)






