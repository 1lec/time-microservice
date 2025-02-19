import zmq
from datetime import date, datetime


def calculate_time_difference(datetime_string):
    """Receives a datetime as a string in the format YYYY-MM-DD HH:MM:SS. Returns two values: a string of the difference in time
    between the received datetime and the current datetime, and the status of the time difference: remaining or overdue."""
    # Create datetime objects to prepare comparison
    received_datetime = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()

    # Determine whether the received datetime lies in the past or future, and generate a timedelta object
    if received_datetime > current_datetime:
        status = "remaining"
        time_difference = received_datetime - current_datetime
    else:
        status = "overdue"
        time_difference = current_datetime - received_datetime

    display_string = generate_display_string(time_difference)
    return (display_string, status)
    
def generate_display_string(time_difference):
    """Receives a timedelta object and returns a human-readable version of the time difference in the form of a string."""
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
            time_difference, status = calculate_time_difference(request.decode())
            socket.send_multipart([time_difference.encode(), status.encode()])


if __name__ == "__main__":
    main()
