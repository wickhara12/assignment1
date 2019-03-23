import unittest
from model.file_handler import *


# tests relating to opening a file

class PickleAndFileHandlerTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.x = file_reader('data.pickle')

    def tearDown(self):
        print('error')

# checking that the file that is pass through to file handler is correct
    def test1(self):
        self.assertTrue(self.x == file_reader('data.pickle'))
# a false check if you put a text file instead of the pickle file

    def test2(self):
        self.assertFalse(self.x == file_reader('test.txt'))
# having no file check

    def test3(self):
        self.assertFalse(self.x == '')
# pickle files can load and view pickle files

    def test4(self):
        self.y = 'data.pickle'
        self.assertTrue(self.y == 'data.pickle')

    def test5(self):
        self.y = 'data.pickle'
        self.assertFalse(self.y == '')

# these tests is what happens when it reading file, these tests are from class-maker and the converter
class MainTests(unittest.TestCase):

    def setUp(self):
        # be executed before each test
        self.x = 'plantUML.txt'

    def test_01(self):
        self.assertTrue(self.x == 'plantUML.txt', "the value of x should be this file")

    def test_02(self):
        self.x = 'toy'
        self.assertTrue(self.x == 'toy')

    def test_03(self):
        self.assertFalse(self.x == 'diagram.txt', "this should be plantUML.txt")

    def test_04(self):
        self.assertEqual(self.x, 'plantUML.txt')

    def test_05(self):
        self.x = 'toy'
        self.assertFalse(self.x == 'teddyBear')

    def test_06(self):
        self.x = 'ToyBox'
        self.assertTrue(self.x == 'ToyBox')

    def test_07(self):
        self.x = 'ToyBox'
        self.assertFalse(self.x == 'box')

    def test_08(self):
        self.x = 'Toy'
        self.x2 = 'name'
        self.assertTrue(self.x == 'Toy', self.x2 == 'name')

    def test_09(self):
        self.x = 'ToyBox'
        self.x2 = 'name'
        self.assertTrue(self.x == 'ToyBox', self.x2 == 'name')

    def test_10(self):
        self.x = 'Toy'
        self.x2 = 'name'
        self.assertFalse(self.x == 'Toybox', self.x2 == 'name')

    def test_11(self):
        self.x = 'ToyBox'
        self.x2 = 'name'
        self.assertFalse(self.x == 'Toy', self.x2 == 'name')

    def test_12(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.assertEqual(self.data2, 'color')

    def test_13(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.assertEqual(self.data2, 'none')

    def test_14(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.assertNotEqual(self.data2, 'color')

    def test_15(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.assertNotEqual(self.data, 'color')

    def test_16(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.assertNotEqual(self.data2, 'name')

    def test_17(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.assertNotEqual(self.data, 'color')

    def test_18(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.attributes = 'createAttribute()'

        self.assertNotEqual(self.attributes, 'color')

    def test_19(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.attributes = 'createAttribute()'

        self.assertEqual(self.attributes, 'createAttribute()')

    def test_20(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.attributes = 'createAttribute()'
        self.assertEqual(self.attributes, 'createAttribute()')

    def test_21(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.assertEqual(self.methods, 'createMethods()')

    def test_22(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.assertTrue(self.methods == 'createMethods()')

    def test_23(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.assertNotEqual(self.methods, 'createMethod()')

    def test_24(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.assertEqual(self.methods, 'createMethods()')

    def test_25(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.assertFalse(self.methods == 'create()')

    def test_26(self):
        self.x = 'ToyBox'
        self.data = 'name'
        self.data2 = 'none'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.relationship = ''
        self.assertEqual(self.methods, 'createMethods()')
    def test_27(self):
        self.x = 'Toy'
        self.data = 'name'
        self.data2 = 'color'
        self.attributes = 'createAttribute()'
        self.methods = 'createMethods()'
        self.relationship = '<|--'
        self.assertTrue(self.relationship == '<|--')

if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
