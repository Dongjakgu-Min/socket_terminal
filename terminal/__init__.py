import socketio
from subprocess import Popen, PIPE

sio = socketio.Client()

fw = open('fw', 'wb')
fr = open('fw', 'r+t')
proc = Popen('bash', stdin=PIPE, stdout=fw, stderr=fw)


@sio.event(namespace='/test')
def connect():
    print('connection established')


@sio.event(namespace='/test')
def message(data):
    proc.stdin.write(bytes(data.encode('utf-8')))
    proc.stdin.flush()
    print(fr.read())
    sio.emit('message', fr.read())


sio.connect('http://localhost:5000', namespaces=['/test'])
sio.wait()
