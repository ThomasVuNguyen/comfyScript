#Receive and log message only

from flask import Flask, request
from simple_websocket import Server, ConnectionClosed

app = Flask(__name__)

@app.route('/echo', websocket=True)
def echo():
    ws = Server.accept(request.environ)
    try:
        while True:
            data = ws.receive()
            ws.send(data)
            print(data)
    except ConnectionClosed:
        pass
    return ''