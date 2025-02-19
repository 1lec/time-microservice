import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5559")

    print("             Welcome to Small Test Program for the Time Microservice!")
    print("This program will demonstrate how to request and receive data from the Time Microservice.\n")
    print("Instructions:")
    print("""To request the current date, enter 'date' (without quotes), or enter a datetime in YYYY-MM-DD HH:MM:SS format to
request the difference between the two datetimes, and whether said difference is time 'remaining' or time 'overdue'.\n""")

    while True:
        request = input("Enter request: ")
        if request == 'date':
            socket.send_string(request)
            response = socket.recv()
            print(response.decode())
        else:
            socket.send_string(request)
            response = socket.recv_multipart()
            print(response[0].decode(), response[1].decode())


if __name__ == "__main__":
    main()
