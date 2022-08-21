from flask import request, Flask, jsonify
from models.response import Response

from models.usuario import Usuario
from repositorys.user__repository import UserRepository

app = Flask(__name__)

@app.route("/user", methods=["POST"])
def saveUser():
    data = request.get_json()
    usuarioRepository = UserRepository()
    usuario = Usuario(data["nome"], usuarioRepository.getLastId(), data["avatar"])
    usuarioRepository.save(usuario)
    response = Response()
    response.setSucessResponse("Usuário criado com sucesso!")
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