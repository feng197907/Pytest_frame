import os
import yaml
import getpathinfo


class ReadYaml():
    def __init__(self, filename):
        path = getpathinfo.get_path()  # 获取本地路径
        self.filepath = os.path.join(path, 'data') + "/" + filename  # 拼接定位到data文件夹

    def get_yaml_data(self):
        with open(self.filepath, 'r', encoding='utf-8')as f:
            # 调用load方法加载文件流
            return yaml.load(f, yaml.FullLoader)


if __name__ == '__main__':
    data = ReadYaml("add_account_page.yml").get_yaml_data()
    username = data["test_add_account_data2"][0]
    print(username)
