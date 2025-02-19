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
    total_seconds = int(time_difference.total_seconds())
    years = total_seconds // 31536000
    total_seconds = total_seconds % 31536000
    weeks = total_seconds // 604800
    total_seconds = total_seconds % 604800
    days = total_seconds // 86400
    total_seconds = total_seconds % 86400
    hours = total_seconds // 3600
    total_seconds = total_seconds % 3600
    minutes = total_seconds // 60
    total_seconds = total_seconds % 60

    if years > 1:
        return f"{years} years"
    if years == 1:
        return "1 year"
    if weeks > 1:
        return f"{weeks} weeks"
    if weeks == 1:
        return "1 week"
    if days > 1:
        return f"{days} days"
    if days == 1:
        return f"1 day, {hours} hour(s)"
    if hours > 1:
        return f"{hours} hours, {minutes} minute(s)"
    if hours == 1:
        return f"1 hour, {minutes} minute(s)"
    return "Less than 1 hour"


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
