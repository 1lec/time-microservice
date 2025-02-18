import zmq
from datetime import date

while True:
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5559")
    request = socket.recv()

    if request.decode() == "date":
        today = date.today()
        today_str = today.strftime("%Y-%m-%d")
        socket.send_string(today_str)
