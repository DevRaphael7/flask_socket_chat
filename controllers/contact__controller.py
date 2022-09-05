from flask import request, Flask, jsonify
from models.response import Response
from repositorys.contact__repository import ContactRepository

app = Flask(__name__)

@app.route("/contact/<number_user>", methods=["GET"])
def getAllContactByNumber(number_user: int):
    repository = ContactRepository(number_user)
    response = Response()
    if repository.getContactsByNumero():
        response.setSucessResponse('Contatos obtidos com sucesso!', repository.getContactsByNumero())
        print(repository.getContactsByNumero())
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
