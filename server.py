import zmq
from datetime import date, datetime


def calculate_time_difference(date_string):
    """Receives a date as a string in the format YYYY-MM-DD and returns a string containing the difference
    in time between the received date and the current datetime."""
    # received_datetime = datetime.strptime(date_string, "%Y-%m-%d")
    received_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    time_difference = received_datetime - current_datetime
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = time_difference.seconds // 60

    if days >= 730:  # If time remaining is 2 or more years
        return f"{days // 365} years"
    elif days >= 365:
        return "1 year"
    elif days >= 14:
        return f"{days // 7} weeks"
    elif days >= 7:
        return "1 week"
    elif days > 1:
        return f"{days} days, {hours} hour(s)"
    elif days > 0:
        return f"1 day, {hours} hour(s)"
    elif hours > 1:
        return f"{hours} hours"
    elif hours > 0:
        return "1 hour"
    elif minutes > 1:
        return f"{minutes} minutes"
    elif minutes > 0:
        return "1 minute"
    else:
        return f"{time_difference.seconds} seconds"


def main():
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
            time_difference = calculate_time_difference(request.decode())
            socket.send_string(time_difference)


if __name__ == "__main__":
    main()
