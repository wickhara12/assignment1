from model.converter import *
from Command_Help import *
#from model.Database import *
#from model.printPrettyWithDB import *
from model.printPrettywithoutDB import *
from model.Pickle import Pickle
from model.pickle_save import *

class Menu:
    @staticmethod
    def start_menu():
        print("press zero to get file from pickle")
        print("press one to convert file into framework")
        print("press two to save data into a database "
              "or press three to read from a database")
        print("press four to get the command help line")
        print("press five for graphs with DB "
              "or press six for graphs with DB")

        user_input = input("please enter your input")
        if user_input == '0':
           # SavingToPickleFile.get_file()
            Pickle.savingPickle()
            return Menu.start_menu()
        if user_input == "1":
            Converter.start()
            return Menu.start_menu()
     #   if user_input == "2":
     #       create_table()
      #      data_entry()
      #      return start_menu()
       # if user_input == "3":
        #    read_from_db()
         #   return start_menu()
        if user_input == "4":
            quitter = CommandHelp()
            quitter.cmdloop()

    #    if user_input == "5":
    #        graph_data()
    #        cursor.close()
     #       connection.close()
          #  return start_menu()
        if user_input == "6":
            PrintPretty.graphs()
            return Menu.start_menu()
        else:
            print("goodbye")


if __name__ == '__main__':

    Menu.start_menu()
