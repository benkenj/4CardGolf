from flask import Flask, render_template
from flask_socketio import SocketIO, send,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return render_template('index.html', token="Hello world! ")

@app.route('/join')
def index():
    return render_template('join.html')

# @socketio.on('message')
# def handleMessage(msg):
#     #print(request)
#     print('Message: ' + msg)
#     send(msg, broadcast=True)

# @socketio.on('joinroom')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     print(username + ' has entered the room.')
#     send(username + ' has entered the room.', room=room)
@socketio.on('message')
def handleMessage(data):
    
    #print(request)
    for key, value in data.items():
        print('Message: ' + key + " / " + value)
    #send(msg, broadcast=True)
    emit('message', data, broadcast=True)

@socketio.on('message')
def handleMessage(data):
    
    #print(request)
    for key, value in data.items():
        print('Message: ' + key + " / " + value)
    #send(msg, broadcast=True)
    emit('message', data, broadcast=True)





if __name__ == "__main__":
    print("Startingpy")
    socketio.run(app)
