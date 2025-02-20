# Requesting data from the time microservice
To send a request to the microservice, the client must utilize the python module ZeroMQ. Below is an example of how to establish connection to the microservice:  
  
```
import zmq  
context = zmq.Context()  
socket = context.socket(zmq.REQ)  
socket.connect("tcp://localhost:5559")
```

Once connection is established, the client can send one of two requests to the microservice.

**Request Type 1 - Request the current date**  
Note: The string sent for this request must exactly match "date". 
```
socket.send_string("date")  
```  

**Request Type 2 - Request the difference in time between the current datetime and a provided datetime**  
Note: The format of the datetime string sent for this request must exactly match "YYYY-MM-DD HH:MM:SS".  
```
provided_datetime = "2025-07-04 00:00:00"  
socket.send_string(provided_datetime)
```

# Receiving data from the time microservice
The method for receiving data from the microservice depends on the type of request sent by the client.

