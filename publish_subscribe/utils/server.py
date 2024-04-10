import time
import zmq

from utils.random_user import get_random_user
from utils.mogrify import mogrify

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    message = mogrify("user", get_random_user())

    time.sleep(1)

    socket.send_string(message)
