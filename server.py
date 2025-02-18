import zmq


while True:
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5559")
    request = socket.recv()

    print(request.decode())
