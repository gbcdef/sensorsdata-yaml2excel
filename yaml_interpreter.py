# coding: utf-8

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


class YAMLInterpretor:
    """
    将YAML文件转为2维列表

    eg.
        a:
          x: 1
          y: 2

    将被转为：
        [[a, x, 1],
        [None, y, 2]]

    当指定
    """
    def __init__(self, fill_with_none=True):
        self.fill_with_none = fill_with_none

    def load(self, string):
        yaml = YAML()
        data = yaml.load(string)
        return self.parse_node(data, self.fill_with_none)

    def load_file(self, filepath):
        try:
            f = open(filepath, 'r', encoding='utf8')
        except:
            print('file path is wrong')
            return None
        else:
            res = self.load(f.read())
            f.close()
            return res

    def parse_node(self, data, fill_with_none=True):
        # 每次递归返回的结果
        result = []

        for key in data:

            # 根据是否为最后一级决定value的取值
            skip_flag = False
            if isinstance(data, CommentedMap):
                value = data[key]
            else:
                value = key
                skip_flag = True

            # 判断是否可以继续递归
            if isinstance(value, CommentedMap) or isinstance(value, list):
                # 收到下一级递归返回的2Dlist
                li_child_2dlist = self.parse_node(value)

                # 为每一个列表的第1个增加本级的key，其余增加None
                for list_item in li_child_2dlist:
                    if fill_with_none and not skip_flag:
                        list_item.insert(0, key if list_item == li_child_2dlist[0] else None)
                    elif not skip_flag:
                        list_item.insert(0, key)

                    # 将添加本级key后的新list添加到result末尾
                    result.append(list_item)

            # 最后一级不可分解时，通过循环返回二维数组
            else:
                result.append([key, value])

        # 将结果向上一级递归返回
        return result
