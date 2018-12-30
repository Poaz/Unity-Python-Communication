#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

from datetime import datetime


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

messages = []
t1 = start_time = datetime.now()
while True:

    #  Wait for next request from client
    message = socket.recv()
    #print("Received request: %s" % message)

    #  Do some 'work'.
    #  Try reducing sleep time to 0.01 to see how blazingly fast it communicates
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do, maybe a machine learning task?
    #time.sleep(1)

    messages.append(message)


    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    socket.send(b"World")

    if len(messages) == 10000:
        time_elapsed = datetime.now() - start_time
        #print('Packets per sec: ' + str(len(messages) / current_t - t1))
        print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
        messages = []
