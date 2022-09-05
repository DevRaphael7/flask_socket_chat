import json
import os

class JsonFileSystem:
    def __init__(self):
        pass
    
    def createFolder(self, path: str):
        try:
            os.makedirs(path)
            return True
        except:
            return False
    
    def createAndSaveFile(self, path: str, data: dict):
        with open(path, "w") as outfile:
            json.dump(data, outfile)
            
    def getDataInFile(self, path: str):
        with open(path, "r") as readfile:
            return json.load(readfile)
    
    def listDirectoryAndFile(self, path: str):
        listDiretory = os.listdir(path)
        return listDiretory