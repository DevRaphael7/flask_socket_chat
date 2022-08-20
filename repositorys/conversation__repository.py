from models.conversation import Conversation
from services.json_files import JsonFileSystem


class ConversationRepository:
    
    def __init__(self):
        self.service = JsonFileSystem()

    def getConversations(self, conversation: Conversation):
        return self.service.getDataInFile("db/" + conversation.getNumero() + "/" + conversation.getNumeroFriend() + "/conversation.json")
    
    def save(self, conversation: Conversation, id_c: int):
        self.service.createFolder("db/" + conversation.getNumero())
        self.service.createFolder("db/" + conversation.getNumero() + "/" + conversation.getNumeroFriend())
        
        conversas = self.getConversations(conversation)
        
        if conversas:
            pass
        else:
            self.service.createAndSaveFile("db/" + conversation.getNumero() + "/" + conversation.getNumeroFriend(), {
                "id": id_c,
                "numero_friend": conversation.getNumeroFriend()
            })
