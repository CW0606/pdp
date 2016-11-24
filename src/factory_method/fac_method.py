# coding:utf-8
"""
    工厂方法示例
"""
import json
from xml.etree import ElementTree as etree


class JSONConnector:
    """
    Json 数据解析链接器
    """

    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property  # 将方法转化为属性
    def parsed_data(self):
        return self.data


class XMLConnector:
    """
    XML 数据解析链接器
    """

    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    @property
    def parsed_data(self):
        return self.tree


def connect_factory(file_path):
    """
    获得一个链接器
    :param file_path:
    :return:
    """
    if file_path.endswith('json'):
        connector = JSONConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(file_path))
    return connector


def connect_to(file_path):
    factory = None
    try:
        factory = connect_factory(file_path)
    except ValueError as ve:
        print(ve)
    return factory


if __name__ == '__main__':
    pass
