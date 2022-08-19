from flask import request, Flask, json, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def method_name():
    return jsonify({
        "message": "Hello World!"
    })

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback="Teste")

if __name__ == "__main__":
    socketio.run(app, debug=True)