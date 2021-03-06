#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#
import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

messages = []

while True:

    #  Wait for next request from client
    message = socket.recv()
    #print("Received request: %s" % message)
    print(message)
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do.-
    time.sleep(1)

    messages.append(message)


    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    socket.send(b"World")

