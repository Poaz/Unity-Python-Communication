#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import cv2
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:

    #  Wait for next request from client
    message = socket.recv()
    #print("Received request: %s" % message)

    print(message)

    demsg = message.decode("utf-16", "ignore")
    print(demsg)
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do.-
    time.sleep(1)

    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    socket.send(b"World")

    #img = cv2.imread('messi5.jpg', 0)
    #cv2.imshow('image', img)
    #cv2.waitKey(0)


