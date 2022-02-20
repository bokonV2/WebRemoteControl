from gevent import monkey; monkey.patch_all()
from flask import Flask, render_template, redirect, request
from flask_socketio import SocketIO
from threading import Thread
import pyautogui

from utilsDB import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = False
# gevent, threading
socketio = SocketIO(app, async_mode='gevent', ping_timeout=30)
thread = Thread()


class RandomThread(Thread):
    def __init__(self):
        self.event = False
        super(RandomThread, self).__init__(daemon=True)

    def randomNumberGenerator(self):
        while not self.event:
            socketio.emit(
                'newnumber',
                {'number': pyautogui.position()},
                namespace='/cords'
            )
            socketio.sleep(.2)

    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    return render_template('index.html', groups=getAll())


@app.route('/addButton/<int:id>/<int:step>/<int:type>')
def addButton(id, step, type=0):
    control = [0, 0, 0, 0, 0]
    control[step] = 1
    return render_template('addButton.html', id=id, type=type, control=control)


@app.route('/addGroup')
def addGroup():
    return render_template('addGroup.html')


@socketio.on('handler')
def handler(id):
    print(id)


@socketio.on('removeGroup')
def addGroupDB(id):
    removeGroup(id)


@socketio.on('addGroup')
def addGroupDB(name):
    createGroup(name)


@socketio.on('addButtonOnGr')
def addButtonDB(data):
    createButton(**data)


@socketio.on('stop')
def stop(data):
    socketio.stop()


@socketio.on('connect')
def connect(environ):
    print(environ)
    print(request.sid)
    print("connect")


@socketio.on('disconnect')
def disconnect():
    print("disconnect")


@socketio.on('connect', namespace='/cords')
def test_connect():
    global thread
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()
    else:
        print("Thread life")


@socketio.on('disconnect', namespace='/cords')
def test_disconnect():
    global thread
    print("Stop Thread")
    thread.event = True


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    socketio.run(app, host='0.0.0.0', port=5000,
                 debug=False, use_reloader=False)
