# Requesting data from the time microservice
To send a request to the microservice, the client must utilize the python module ZeroMQ. Below is an example of how to establish connection to the microservice:  
  
import zmq  
context = zmq.Context()  
socket = context.socket(zmq.REQ)  
socket.connect("tcp://localhost:5559")

Once connection is established, the client can send one of two requests to the microservice. Below are examples of both:  
1. To request the current date:  
socket.send_string("date")
2. To request the difference in time between the current datetime and a provided datetime:  
provided_datetime = "2025-07-04 00:00:00"  
socket.send_string(provided_datetime)

For the first type of request, the string must exactly match "date". For the second type of request, the string must exactly match the datetime format "YYYY-MM-DD HH:MM:SS".


# Receiving data from the time microservice