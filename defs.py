'''列表中多个同一元素去下标'''
def indexs(lis,value):
	num = lis.count(value)
	num1 = -1
	result = []
	for i in range(num):
		num1 = lis.index(value,num1+1,len(lis))
		result.append(num1)
	return result
#返回的是个列表