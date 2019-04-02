"""Task 14 was done by LeRoi and task 7 was created by Rebecca"""
import pickle
import os
from tkinter import *
from tkinter import filedialog


class SavingToPickleFile(object):

    @staticmethod
    def get_file():
        root = Tk()
        try:
            name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("All files", "*.*")))
            with open(name_of_file) as file:
                file_data = file.read()
                root.destroy()
                print("\nfile loaded...\n")
                print(file_data)
        except FileNotFoundError:
            root.destroy()
            print("Error, no file inserted")


@staticmethod
def choose_directory():
    root = Tk()
    try:
        dir_name = filedialog.askdirectory()
        root.destroy()
        return dir_name
    except FileNotFoundError:
        root.destroy()

#SavingToPickleFile.get_file()


