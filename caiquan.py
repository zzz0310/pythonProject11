# #
# book1 = {'id':'1','name':'水浒传','position':'c区12层'}
# book2 = {'id':'2','name':'三国志','position':'b区1层'}
# book3 = {'id':'3','name':'西游记','position':'a区2层'}
# book_lis =[]
# book_lis.append(book1)
# print(book_lis)
# book_lis.append(book2)
# print(book_lis)
# book_lis.append(book3)
# print(book_lis)
# #
#
# book ={'id':'','name':'','position':''}
# book_list=[]
# id = input('id=')
# name =input('name=')
# position =input('position=')
# book['id']=id
# book['name']= name
# book['position']=position
#
# book_list.append(book)
# print(book_list)

book_list = []
while True:
    book = {'id': '', 'name': '', 'position': ''}
    book['id'] = input('请输入添加书籍编号：')
    book['name'] = input('请输入添加书籍名称：')
    book['position'] = input('请输入添加书籍位置：')
    for i in book_list:
        a = i['id']
        print(a)
    # if book['id'] not in a:
    #     book_list.append(book)
    # else:
    #     print('id重复,请重新输入')
    print('书籍编号：{},书籍名称{},书籍位置{}'.format(book['id'], book['name'], book['position']))
    print(book_list)