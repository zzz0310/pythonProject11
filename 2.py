import yaml
def read_yaml():
    with open("config.yaml", encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        print(data)
        print(data["logger"]["name"])
read_yaml()