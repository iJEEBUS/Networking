import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
# send data
client.sendto(message.encode(), (target_host, target_port))

# receive data
response = client.recv(4096)

#print data
print(response)