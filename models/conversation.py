class Conversation:
    
    def __init__(self, message: str, numero: int, numero_friend: int):
        self.message = message
        self.numero = numero
        self.numero_friend = numero_friend
    
    def getNumero(self):
        return self.numero
    
    def getNumeroFriend(self):
        return self.numero_friend