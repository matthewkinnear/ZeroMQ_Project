import json

import zmq


def create_connection():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    return socket


def subscribe(socket, topic=""):
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)


def send_message(socket, message):
    message_bytes = json.dumps(message).encode('utf-8')
    print(f"Sending {message}")
    socket.send(message_bytes)
    return


def main():
    socket = create_connection()
    subscribe(socket, "")

    while True:
        message = socket.recv()
        print(f"Received {message}")


if __name__ == "__main__":
    main()
