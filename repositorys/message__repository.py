from services.json_files import JsonFileSystem

class MessageRepository:
    
    def __init__(self):
        self.id: int = None
        self.service = JsonFileSystem()
    
    def getIdInLastidJson(self):
        return self.service.getDataInFile('db/lastId.json')["id"]
    
    def verifyExistFolderWithById(self, id: int):
        if not self.service.createFolder('db/conversations/' + id):
            return True
        else:
            return False
        
    def createNewConversation(self):
        if self.verifyExistFolderWithById(self, self.getIdInLastidJson() + 1):
            count = self.getIdInLastidJson() + 1
            while True:
                count += 1
                if not self.service.createFolder('db/conversations/' + count):
                    continue
                else:
                    self.id = count
                    break
        else:
            self.service.createFolder('db/conversations/' + self.getIdInLastidJson() + 1)
        
    def save(self, message: str, id: int , numero: int):
        checkLastSave: list = self.service.getDataInFile('db/conversations/' + id + '/conversation.json')
        if checkLastSave:
            checkLastSave.append({ "message": message, "id": id, "numero": numero })
            self.service.createAndSaveFile('db/conversations/' + id + '/conversation.json', checkLastSave)
        else:
            checkLastSave = []
            checkLastSave.append({ "message": message, "id": id, "numero": numero })
            self.service.createAndSaveFile('db/conversations/' + id + '/conversation.json', checkLastSave)