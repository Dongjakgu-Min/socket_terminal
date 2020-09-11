from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.secret_key = 'super secret key'
socket_io = SocketIO(app)


@app.route('/')
def main():
    return render_template("index.html")


@socket_io.on('message', namespace='/req')
def handle_message(message):
    print('request message : ' + message)
    send(message, broadcast=True, namespace='/req')


@socket_io.on('message', namespace='/resp')
def send_message(message):
    print('response message : ' + message)
    send(message, broadcast=True, namespace='/resp')


if __name__ == '__main__':
    socket_io.run(app)
