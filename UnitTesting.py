import unittest
from model.converter import *
import model.class_maker

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

# checking if the converter can converted file into diagram
# does each class diagram begins with 'class'

    def test4(self):
        self.class_Maker = 'class'
        self.assertTrue(self.class_Maker == 'class')

# what happens if you don't show 'class' before name

    def test5(self):
        self.class_Maker = 'class'
        self.assertFalse(self.class_Maker == '')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
