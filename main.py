# coding: utf-8

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
import pandas


class SensorsInterpretor:
    def __init__(self):
        pass

    def load_yaml(self, string):
        yaml = YAML()
        data = yaml.load(string)
        return self.parse_node(data)

    def load_file(self, filepath):
        try:
            f = open(filepath, 'r', encoding='utf8')
        except:
            print('file path is wrong')
            return None
        else:
            res = self.load_yaml(f.read())
            f.close()
            return res

    def parse_node(self, data):
        # 每次递归返回的结果
        result = []

        for key in data:
            skip_flag = False
            if isinstance(data, CommentedMap):
                value = data[key]
            else:
                value = key
                skip_flag = True

            # 判断是否是最后一级不可分解
            if isinstance(value, CommentedMap) or isinstance(value, list):
                # 收到下一级递归返回的list
                li_child_result = self.parse_node(value)

                # 为每一项增加本级递归的key
                for list_item in li_child_result:
                    if not skip_flag:
                        list_item.insert(0, key)

                    # 将添加本级key后的新list添加到result末尾
                    result.append(list_item)

            # 不可分解时，通过循环返回最底层的二维数组
            else:
                result.append([key, value])

        # 将结果向上一级递归返回
        return result
