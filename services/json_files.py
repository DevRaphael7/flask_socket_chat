import json
import os

class JsonFileSystem:
    def __init__(self):
        pass
    
    def createFolder(self, path: str):
        try:
            os.makedirs(path)
        except:
            pass
    
    def createAndSaveFile(self, path: str, data: dict):
        with open(path, "w") as outfile:
            json.dump(data, outfile)