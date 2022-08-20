from flask import request, Flask, json, jsonify
from models.conversation import Conversation
from models.response import Response
from repositorys.conversation__repository import ConversationRepository
from services.json_files import JsonFileSystem

app = Flask(__name__)
fileSystem = JsonFileSystem()
response = Response()
repository = ConversationRepository()

@app.route("/conversation", methods=["POST"])
def saveConversation():
    data = request.get_json()
    conversation = Conversation(data["message"], data["numero"])
    repository.save(conversation)
    response.setSucessResponse("Conversa gravada com sucesso!")
    return response.__dict__

@app.route('/conversation', methods=["GET"])
def getConversation():
    numero = request.args.get("numero")
    try:
        data = repository.getConversations(numero)
        response.setSucessResponse("Conversas recuperadas com sucesso", data)
    except:
        response.setErrorResponse("Esse número é inválido ou não existe")
    
    return response.__dict__