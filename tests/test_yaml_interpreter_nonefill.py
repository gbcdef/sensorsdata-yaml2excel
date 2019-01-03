import unittest

from yaml_interpreter import YAMLInterpretor


class LoadYamlTest(unittest.TestCase):

    def setUp(self):
        self.si = YAMLInterpretor()

    def test_load_yaml_to_2d_list(self):
        yaml = '''
        a:
          x: 1
          y: 2
        '''
        res = self.si.load(yaml)
        self.assertEqual([
            ['a', 'x', 1],
            [None, 'y', 2]
        ], res)

    def test_load_yaml_with_null(self):
        yaml = '''
        a: 
          x: 1
          y: 
            - null: 注释
            - null
        '''
        res = self.si.load(yaml)

        self.assertEqual([
            ['a', 'x', 1],
            [None, 'y', None, '注释'],
            [None, None, None, None]
        ], res)

    def test_load_yaml_file(self):
        filepath = 'mock_data/01.yaml'
        res = self.si.load_file(filepath)
        self.assertEqual([
            ['a', 'x', 1],
            [None, 'y', 2]
        ], res)

    def test_load_wrong_file(self):
        res = self.si.load_file('abc.asdf')
        self.assertIsNone(res)
