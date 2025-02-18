import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5559")

    print("Enter 1 to receive the current date, or enter 2 to enter a date and calculate the difference.")

    while True:
        first_choice = input("Enter 1 or 2: ")
        if first_choice == '1':
            socket.send_string("date")
        if first_choice == '2':
            second_choice = input("Enter a date in YYYY-MM-DD format: ")
            socket.send_string(second_choice)

        response = socket.recv()
        print(response.decode())


if __name__ == "__main__":
    main()
