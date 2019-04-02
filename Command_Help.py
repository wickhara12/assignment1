"""this is Rebecca's code for tasks 2 & 3"""
from cmd import Cmd
import mainMenu
from testing.UnitTesting import *
from testing.DocTests import *


class CommandHelp(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_name(self, the_name):
        if the_name:
            self.my_name = the_name
        print(self.my_name)

    # commands

    def do_mainmenu(self, the_name):
        """the main will run the program """
        if the_name:
            pass
        else:
            mainMenu.Menu.start_menu()

    def do_unittests(self, the_name):
        """unit testing examines if the information or data is correct in your program '
              'it is different from DocTests, so some people can be confused. however, both tests programs'
              ' ran the same way by going to run on the menu bar and clicking on run'"""
        if the_name:
            pass
        else:
            unittest.main()

    def do_doctests(self, the_name):
        """ ('there are tests that examines the file "plantUML.txt" and checks if the class information is correct '
              'it is different from unitTests, so some people can be confused. however, both tests programs'
              ' ran the same way by going to run on the menu bar and clicking on run... ') """
        if the_name:
            doctest

    def help_pickle(self):
        print('pickle opens the file when it was last save')

    def help_converter(self):
        print('opens a file and shows the file location of the file '
              'and evaluates and checks for classes, attributes and methods '
              'and also has file handling/exceptions')

    def help_database(self):
        print('the database will save and read data that is hard coded, '
              'the data is based on the PlantUML.txr file and also includes date of class creation '
              'the select statement is showing all of the data that is in the database.')

    def help_printPrettyWithoutDB(self):
        print('this is hard coded, and when u run the program, it will display a bar chart of how many information'
              'is in each class')

    def help_printPrettyWithDB(self):
        print('this is a part of the database file which allows data to be display in a graph ')





    # quit

    def do_quit(self, line):
        print("Quitting ......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

    do_q = do_quit


if __name__ == "__main__":
    quitter = CommandHelp()
    quitter.cmdloop()

