from flask import Flask, render_template
#from flask_socketio import SocketIO, send

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', token="Hello world! ")


if __name__ == "__main__":
    print("Startingpy")
    app.run(debug=True)
