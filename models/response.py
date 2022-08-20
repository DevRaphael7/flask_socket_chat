class Response:
    
    def __init__(self):
        self.message: str = None
        self.code: int = None
        self.data: dict = None
    
    def setSucessResponse(self, message: str, data: dict = None):
        self.message = message
        self.code = 200
        self.data = data
    
    def setErrorResponse(self, message: str):
        self.message = message
        self.code = 400
        self.data = None