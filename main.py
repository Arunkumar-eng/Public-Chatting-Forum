from flask import Flask, render_template
from flask_socketio import SocketIO
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/session',methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    # socketio.run(app)
    app.run(host = '192.168.1.40', port=8081)

# if __name__ == '__main__':
#     http_server = WSGIServer(('172.16.4.150', 8081), app, handler_class=WebSocketHandler)
#     http_server.serve_forever()