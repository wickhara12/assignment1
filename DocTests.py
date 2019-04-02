
#doctests for assignment one

# checking if the the model.converter does work

"""

>>> from model.converter import *
>>> Converter.start()
>>> file_content = file_reader('data.pickle')

# checking if the model.fileHandler is working

>>> from model.file_handler import *
>>> Exception = ''
>>> FileExistsError = ''
>>> FileNotFoundError = ''

# checking if the main menu is working correctly
>>> from mainMenu import Menu


# checking if pickle files are working
>>> from model.Pickle import *

# checking if class_maker is working
>>> from model.class_maker import *
>>> ClassMaker.method_maker.methods = ''
>>> ClassMaker.attribute_maker.attributes = ''

# checking if the command line is correct
>>> from Command_Help import  *
>>> quitter = CommandHelp()
>>> quitter.cmdloop()
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)

