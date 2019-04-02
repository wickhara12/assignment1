import pickle
from model.pickle_save import *

class Pickle:
    @staticmethod
    def savingPickle():
        with open("data.pickle", "wb") as f:
            pickle.dump(SavingToPickleFile, f)

        with open("data.pickle", "rb") as f:
            data = pickle.load(f)
        print(data)
        print(SavingToPickleFile.get_file())


#Pickle.savingPickle()
