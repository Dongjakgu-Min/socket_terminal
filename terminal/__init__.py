import socketio
import time
from subprocess import Popen, PIPE

sio = socketio.Client()

fw = open('fw', 'wb')
fr = open('fw', 'r+t')
proc = Popen('bash', stdin=PIPE, stdout=fw, stderr=fw)


@sio.event(namespace='/req')
def connect():
    print('connection established')


@sio.event(namespace='/req')
def message(data):
    proc.stdin.write(bytes(data.encode('utf-8')))
    proc.stdin.flush()
    time.sleep(1)

    stdout = fr.read()
    fr.truncate(0)
    for line in stdout.split('\n'):
        sio.emit('message', line, namespace='/resp')


sio.connect('http://localhost:5000', namespaces=['/req', '/resp'])
sio.wait()
