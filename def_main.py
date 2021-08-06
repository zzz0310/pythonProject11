#登录12
def login():
    from ruamel import yaml
    username_input = input('请输入用户名：')
    password_input = input('请输入密码：')
    user_ku = []
    username_ku= []
    with open('user.yaml','r',encoding='utf-8') as f:
        user_ku = yaml.load(f.read(),Loader=yaml.Loader)
        for i in user_ku:
            username_ku.append(i['username'])
            if username_input in username_ku:
                password_ku = user_ku[username_ku.index(username_input)]['password']
                if password_ku == password_input:
                    return {'code':1}#登录成功
        else:
            return {'code':2}#登录失败


#注册
def registered():
    from ruamel import yaml
    username_input = input('请输入用户名：')
    password_input = input('请输入密码：')
    user_ku = []
    username_ku = []
    if len(username_input) != 0 and len(password_input) != 0:
        with open('user.yaml', 'r', encoding='utf-8') as f:
            user_ku = yaml.load(f.read(), Loader=yaml.Loader)
        for i in user_ku:
            username_ku.append(i['username'])
        if username_input not in username_ku:
            lis = [{'username':'{}'.format(username_input),'password':'{}'.format(password_input)}]
            with open("user.yaml","a",encoding="utf-8") as f:
                yaml.dump(lis,f,Dumper=yaml.RoundTripDumper)
            return {'code':1}#成功注册
        else:
            return {'code':2}#注册失败
    else:
        return {'code':3}     #请输入有效值

#添加书籍
def book_add():
    from ruamel import yaml
    book_id_input = input('请输入书的id号:')
    book_name_input = input('请输入书名:')
    book_position_input = input('请输入书的位置:')
    with open('book_list.yaml', 'r', encoding='utf-8') as f:
        book_list_ku = yaml.load(f.read(), Loader=yaml.Loader)
    book_id_ku = []
    book_position_ku = []
    book_name_ku = []
    for i in book_list_ku:
        book_id_ku.append(i['id'])
        book_position_ku.append(i['position'])
        book_name_ku.append(i['name'])
    if len(book_id_input) == 0 or len(book_name_input) == 0 or len(book_position_input) == 0:
        return {'code': 2}#添加书籍失败，书籍内容不能为空
    elif book_id_input not in book_id_ku and book_position_input not in book_position_ku:
        book_list_input = [{'id':'{}'.format(book_id_input),'name':'{}'.format(book_name_input),'position':'{}'.format(book_position_input)}]
        with open("book_list.yaml","a",encoding="utf-8") as f:
            yaml.dump(book_list_input,f,Dumper=yaml.RoundTripDumper)
            return {'code':1}#添加书籍成功
    else:
        return {'code':3}#添加失败，id或位置错误

#删除书籍
def book_del():
    from ruamel import yaml
    with open('book_list.yaml', 'r', encoding='utf-8') as f:
        book_list_ku = yaml.load(f.read(), Loader=yaml.Loader)
    book_name_del = input('请输入你需要删除的书籍名：')
    book_name_ku = []
    for i in book_list_ku:
        book_name_ku.append(i['name'])
    if book_name_del not in book_name_ku:
        print('没有找到你要')
#查找图书
def book_search():
    from ruamel import yaml
    with open('book_list.yaml', 'r', encoding='utf-8') as f:
        book_list_ku = yaml.load(f.read(), Loader=yaml.Loader)
    book_name_seach =input('请输入你要搜索的书名：')
    print(book_list_ku)
    book_name_ku = []
    for i in book_list_ku:
        book_name_ku.append(i['name'])
    if book_name_seach not in book_name_ku:
        # print('对不起，暂未收藏这本书')
        return {'code':2}
    elif book_name_seach in book_name_ku:
        # num = indexs(book_name_ku,book_name_seach)
        # print('搜索到的书籍如下：')
        # for num1 in num:
        #     print('书籍id：{}，书名：{}，位置：{}'.format(book_list_ku[num1]['id'],book_list_ku[num1]['name'],book_list_ku[num1]['position']))
        return {'code':1}









#书籍管理系统
def tushuxitong():
    print('-----欢迎进入图书系统-----\n[1] 添加图书\n[2] 删除图书\n[3] 查询图书\n[4] 退出系统\n-----------------------')
    num = input('请输入你的选项：')
    if num == '1':
        while True:
            add = book_add()
            if add['code'] == 1:
                print('添加书籍成功')
                break
            elif add['code'] == 2:
                print('添加书籍失败，书籍内容不能为空\n1.重新输入\n2.返回')
                num = input('你的选择:')
                if num == '2':
                    break
            else:
                print('添加失败，id或位置错误\n1.重新输入\n2.返回')
                num1 = input('你的选择')
                if num1 == '2':
                    break
    # elif num == '2':
    #     book_del()
    elif num == '3':
        seach = book_search()
        if seach['code'] == 1:
            print('搜索到的书籍如下：')
            for num1 in num:
                print('书籍id：{}，书名：{}，位置：{}'.format(book_list_ku[num1]['id'],book_list_ku[num1]['name'],book_list_ku[num1]['position']))


tushuxitong()




def main():
    while True:
        print('-----欢迎进入图书系统-----\n1.登录\n2.注册\n3.退出\n-----------------------')
        num = input('请输入你需要操作的选项：')
        if num == '1':
            while True:
                log = login()
                if log['code'] == 1:
                    print('登录成功，进入主菜单')
                    while True:
                        tushuxitong()

                elif log['code'] == 2:
                    print('账号或密码错误：1.请重新输入账号\n2.退出登录')
                    num1 = input('你的选择：')
                    if num1 == '2':
                        break

        elif num == '2':
            while True:
                reg = registered()
                if reg['code'] == 1:
                    print('注册成功')
                    break
                elif reg['code'] == 2:
                    print('注册失败，用户名重复:1.重新注册\n2.退出注册')
                    num2 = input('你的选择：')
                    if num2 == '2':
                        break
                else:
                    print('请输入有效字符')
        elif num == '3':
            print('退出成功')
            break
        else:

            print('请输入有效字符')


