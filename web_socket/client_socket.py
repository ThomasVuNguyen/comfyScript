# This is a client socket to run on windows or mac machines for testing purposes

from simple_websocket import Client, ConnectionClosed

def main():
    ws = Client.connect('ws://tung.local:5000/echo')
    try:
        while True:
            data = input('> ')
            ws.send(data)
            data = ws.receive()
            print(f'< {data}')
    except (KeyboardInterrupt, EOFError, ConnectionClosed):
        ws.close()

if __name__ == '__main__':
    main()