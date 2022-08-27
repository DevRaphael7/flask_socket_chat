from flask import request, Flask, jsonify
from flask_socketio import SocketIO
from controllers.user__controller import app
from flask_cors import CORS, cross_origin

socketio = SocketIO(app, cors_allowed_origins =
    ["*"]
)
CORS(app)

@socketio.on('conversa')
def conversationSocket(message_request):
    data = message_request
    socketio.emit('conv', { "message": data["message"], "numero": data["numero"]})
    
if __name__ == "__main__":
    socketio.run(app, debug=True)