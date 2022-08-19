from flask import request, Flask, json, jsonify
from models.conversation import Conversation
from models.response import Response
from services.json_files import JsonFileSystem

app = Flask(__name__)
fileSystem = JsonFileSystem()
response = Response()

@app.route("/conversation", methods=["POST"])
def saveConversation():
    data = request.get_json()
    conversation = Conversation(data["message"], data["numero"])
    fileSystem.createFolder("db/" + conversation.getNumero())
    fileSystem.createAndSaveFile("db/" + conversation.getNumero() + "/conversations.json", conversation.__dict__)
    response.setSucessResponse("Conversa gravada com sucesso!")
    return response.__dict__

@app.route('/conversation', methods=["GET"])
def getConversation():
    data = request.get_json()
    conversation = Conversation(data["message"], data["numero"])
    
    pass