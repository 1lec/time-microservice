import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")
socket.send_string("date")

response = socket.recv()
print(response.decode())
