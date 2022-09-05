from flask import request, Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
from models.response import Response
from models.usuario import Usuario

from repositorys.contact__repository import ContactRepository
from repositorys.user__repository import UserRepository

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

@app.route("/contact/<number_user>", methods=["GET"])
def getAllContactByNumber(number_user: int):
    repository = ContactRepository(number_user)
    response = Response()
    if repository.getContactsByNumero():
        response.setSucessResponse('Contatos obtidos com sucesso!', repository.getContactsByNumero())
        return response.__dict__
    else:
        response.setSucessResponse('Sem contatos para esse número')
        return response.__dict__
    
@app.route("/contact", methods=["POST"])
def saveContact():
    data = request.get_json()
    repository = ContactRepository(data["numero"])
    response = Response()
    try:
        repository.saveContact(data["numero_friend"])
        response.setSucessResponse("Contato salvo com sucesso!")
        return response.__dict__
    except Exception:
        print(Exception)
        response.setErrorResponse('Ocorreu um erro ao salvar contato!')
        return response.__dict__

@app.route("/user", methods=["POST"])
def saveUser():
    data = request.get_json()
    usuarioRepository = UserRepository()
    usuario = Usuario(data["nome"], usuarioRepository.getLastId(), data["avatar"])
    usuarioRepository.save(usuario)
    response = Response()
    response.setSucessResponse("Usuário criado com sucesso!", { "id": usuario.id })
    return response.__dict__

@app.route("/user/<id_user>", methods=["GET"])
def getUser(id_user: int):
    usuarioRepository = UserRepository()
    checkUserFound = usuarioRepository.getUser(Usuario(None, id_user, None))
    response = Response()
    if checkUserFound:
        response.setSucessResponse("Usuário encontrado com sucesso!", checkUserFound)
        return response.__dict__
    else:
        response.setErrorResponse("Usuário não encontrado!")
        return response.__dict__

@app.route("/users", methods=['GET'])
def getAllUsers():
    usuarioRepository = UserRepository()
    usuarios = usuarioRepository.getAllUser()
    response = Response()
    response.setSucessResponse('Usuários encontrados', usuarios)
    return response.__dict__

@socketio.on('conversa')
def conversationSocket(message_request):
    data = message_request
    print(message_request)
    socketio.emit('conv', { 
        "message": data["message"], 
        "numero": data["numero"],
        "numeroDestin": data["numeroDestin"]
    })
    
if __name__ == "__main__":
    socketio.run(app, debug=True)