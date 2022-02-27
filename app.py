from gevent import monkey; monkey.patch_all()
from flask import Flask, render_template, redirect, request
from flask_socketio import SocketIO
from threading import Thread
import socket

from static.py.handler import getCords, openLocal, handl
from static.py.utilsDB import createGroup, createButton, getAll, removeGroup, \
    removeButton

from engineio.async_drivers import gevent
import os, sys


port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = f"{(s.getsockname()[0])}:{port}"
s.close()


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

# app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = False
# gevent, threading
# socketio = SocketIO(app, async_mode='threading', ping_timeout=30, logger=True)
socketio = SocketIO(app, async_mode='gevent', ping_timeout=30, logger=False)
thread = Thread()


class RandomThread(Thread):
    def __init__(self):
        self.event = False
        super(RandomThread, self).__init__(daemon=True)

    def randomNumberGenerator(self):
        while not self.event:
            socketio.emit(
                'newnumber',
                {'number': getCords()},
                namespace='/cords'
            )
            socketio.sleep(.2)

    def run(self):
        self.randomNumberGenerator()


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', host=host)


@app.route('/')
def index():
    return render_template('index.html', groups=getAll())


@app.route('/addButton/<int:id>/<int:step>/<int:type>')
def addButton(id, step, type=0):
    control = [0, 0, 0, 0, 0, 0, 0]
    control[step] = 1
    return render_template('addButton.html', id=id, type=type, control=control)


@app.route('/addGroup')
def addGroup():
    return render_template('addGroup.html')


@socketio.on('handler')
def handler(id):
    handl(id)


@socketio.on('removeBtn')
def removeBtn(id):
    removeButton(id)


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
def connect():
    print("connect")


@socketio.on('disconnect')
def disconnect():
    print("disconnect")


@socketio.on_error_default
def error_handler(e):
    socketio.emit('error', {'data': str(e)})


@socketio.on('connect', namespace='/cords')
def test_connect():
    global thread
    if not thread.isAlive():
        thread = RandomThread()
        thread.start()
    else:
        pass


@socketio.on('disconnect', namespace='/cords')
def test_disconnect():
    global thread
    thread.event = True


if __name__ == '__main__':
    openLocal(port)
    socketio.run(app, host='0.0.0.0', port=port,
                 debug=False, use_reloader=False, log_output=False)
