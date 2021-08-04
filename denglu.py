info = {'username':'admin','password':'admin'}
book_list=[]
book = {}
num = 0
while num == 0:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == info['username'] and password == info['password']:
        num = 1
        print('-----欢迎进入图书系统-----\n[1] 添加图书\n[2] 删除图书\n[3] 查询图书\n[4] 退出系统\n------------------')
        while True:
            i = input('请输入你操作的选项：')
            if i == '1':
                lis = []
                # 字典放在循环里，每次循环都被重新定义，放外面全局变量会产生对同一个对象赋值
                book = {'id': '', 'name': '', 'position': ''}
                book['id'] = input('请输入添加书籍编号：')
                book['name'] = input('请输入添加书籍名称：')
                book['position'] = input('请输入添加书籍位置：')
                #判断输入是否为空，为空提示
                if len(book['id']) !=0 and len(book['name']) !=0 and len(book['position']) !=0:
                    #id重复验证
                    for i in book_list:
                        lis.append(i['id'])
                    lis = lis
                    if book['id'] not in lis:
                        book_list.append(book)
                        print('书籍：<<{}>>书籍已添加，返回主菜单'.format(book['name']))
                    else:
                        print('id重复，请重新输入')
                else:
                    print('输入有误，请重新输入')
                for book in book_list:
                    print('编号:{},书名:<<{}>>,位置:{}.'.format(book['id'], book['name'], book['position']))
            elif i == '2':
                del_name = input('请输入需要删除的书籍名称：')
                #列出图书列表中所有图书（全部信息id，name，posttion）
                for book in book_list:
                    if del_name == book['name']:
                        #此处的book是字典
                        book_list.remove(book)
                        print('<<{}>>图书已删除，返回主菜单'.format(del_name))
                    else:
                        print('没有找到您要删除的图书，返回主菜单')
            #查询书籍
            elif i == '3':
                if len(book_list) == 0:
                        print('暂时没有书籍')
                else:
                    step = input('1:查询现有所有图书\n2:查询指定图书\n请输入您要执行的步骤：')
                    #查询所有书籍（后续书籍较多时需要分区显示）
                    if step == '1':
                        for book in book_list:
                            print('编号:{},书名:<<{}>>,位置:{}.'.format(book['id'],book['name'],book['position']))
                    #按书名查询指定所有同名书籍
                    elif step == '2':
                        book_name = input('请输入您要查询的书籍名：')
                        lis = []
                        for book in book_list:
                            lis.append(book['name'])
                        #查询出列表中同名书籍的下标
                        if book_name in lis:
                            a = lis.count(book_name)
                            b = -1
                            for i in range(a):
                                b = lis.index(book_name,b+1,len(lis))
                                print('书籍编号：{}，名称：{}，位置：{}'.format(book_list[b]['id'],book_list[b]['name'],book_list[b]['position']))

            elif i == '4':
                print('谢谢使用，即将退出系统')
                break
    else:
        print('用户名或密码错误')
