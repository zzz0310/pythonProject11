import pprint
import yaml

# #读yaml
# with open('conf.yml', 'r', encoding='utf-8') as fs:
#     data = yaml.safe_load(fs)  #解析yaml文件内容并生成python对象
#     pprint.pprint(data)        #打印

#写yaml
data_w={'psw': {'new': 'abcdefg', 'old': 'abcdefgwj'}}
with open('conf.yml','w') as fs:     #写入模式
    data2=yaml.safe_dump(data_w,fs)  #将python对象转化为yaml流

# #重新再读取yaml文件
# with open('conf.yml','r') as fs:
#     # 也是解析yaml文档，但是有一个Loader参数，默认为空。Loader=yaml.FullLoader解决告警问题
#     data3=yaml.load(fs,Loader=yaml.FullLoader)
#     pprint.pprint(data3)
