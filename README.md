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

**Request Type 1 - Request the current date**  
Using the recv() method, the client receives the current date as a byte string, which can be converted to a string using the decode() method.
```
response = socket.recv().decode()
```

**Request Type 2 - Request the difference in time between the current datetime and a provided datetime**  
Using the recv_multipart() method, the client receives a list containing two byte strings: the time difference and the remaining/overdue status. Each of these byte strings can be converted to strings using the decode() method.
```
response = socket.recv_multipart()
time_difference = response[0].decode()
status = response[1].decode()
```