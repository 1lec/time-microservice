import zmq
from datetime import date, datetime

while True:
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5559")
    request = socket.recv()

    if request.decode() == "date":
        today = date.today()
        today_str = today.strftime("%Y-%m-%d")
        socket.send_string(today_str)
    else:
        received_datetime = datetime.strptime(request.decode(), "%Y-%m-%d")
        current_datetime = datetime.now()
        difference = received_datetime - current_datetime
        socket.send_string("It works!")
