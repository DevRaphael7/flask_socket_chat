from models.usuario import Usuario
from services.json_files import JsonFileSystem

class ContactRepository:

    def __init__(self, numero: int):
        self.numero = numero;
        self.service = JsonFileSystem()

    def getContactsByNumero(self):
        try:
            return self.service.getDataInFile('db/' + str(self.numero) + '/contacts/listContacts.json')
        except Exception:
            print('Erro ao obter lista de contatos')
    
    def saveContact(self, numero__friend: int):
        self.service.createFolder('db/' + str(self.numero) + '/contacts')
        contact = self.getListContact()

        if contact:
            contact[str(numero__friend)] = self.getContactByNumeroFriend(numero__friend)
        
            self.service.createAndSaveFile('db/' + str(self.numero) + '/contacts/listContacts.json', contact)
        else:
            self.service.createAndSaveFile('db/' + str(self.numero) + '/contacts/listContacts.json', { 
                numero__friend: self.getContactByNumeroFriend(numero__friend)
            })
        
    def getListContact(self):
        try:
            return self.service.getDataInFile('db/' + str(self.numero) + '/contacts/listContacts.json')
        except Exception:
            return {}

    def getContactByNumeroFriend(self, numero__friend: int):
        return self.service.getDataInFile('db/' + str(numero__friend) + '/user.json')