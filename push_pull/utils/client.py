import json

import zmq


def create_connection():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    return socket


def send_message(socket, message):
    message_bytes = json.dumps(message).encode('utf-8')
    print(f"Sending {message}")
    socket.send(message_bytes)
    return
