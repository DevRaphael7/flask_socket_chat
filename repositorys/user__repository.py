from models.usuario import Usuario
from services.json_files import JsonFileSystem


class UserRepository:
    
    def __init__(self):
        self.jsonService = JsonFileSystem()
        
    def getLastId(self):
        return int(self.jsonService.listDirectoryAndFile('db/')[-1]) + 1
        
    
    def save(self, usuario: Usuario):
        self.jsonService.createFolder('db/' + str(usuario.id))
        self.jsonService.createAndSaveFile('db/' + str(usuario.id) + '/user.json', usuario.__dict__)
    
    def getUser(self, usuario: Usuario):
        try:
            usuario = self.jsonService.getDataInFile('db/' + str(usuario.id) + '/user.json')
            return usuario
        except:
            return None
    
    def getAllUser(self):
        usuarios = {}
        try:
            loop = True
            count = 1
            while(loop):
                usuario = self.jsonService.getDataInFile('db/' + str(count) + '/user.json')
                usuarios[count] = usuario
                count += 1
        except:
            print('Recuperou todos os usuários...')
        
        return usuarios
            
        