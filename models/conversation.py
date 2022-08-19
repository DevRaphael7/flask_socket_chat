class Conversation:
    
    def __init__(self, message: str, numero: int):
        self.message = message
        self.numero = numero
    
    def getNumero(self):
        return self.numero