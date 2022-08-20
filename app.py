from flask import request, Flask, jsonify
from flask_socketio import SocketIO
from controllers.conversation__controller import app
from models.conversation import Conversation

from repositorys.conversation__repository import ConversationRepository
from repositorys.message__repository import MessageRepository

socketio = SocketIO(app, cors_allowed_origins =
    ["http://localhost:8100"]
)

@socketio.on('conversa')
def conversationSocket(message_request):
    data = message_request
    socketio.emit('conv', { "message": data["message"], "numero": data["numero"]})
    
if __name__ == "__main__":
    socketio.run(app, debug=True)