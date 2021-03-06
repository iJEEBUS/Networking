import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# add the option to reuse the socket later
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# connect the client
client.bind((target_host, target_port))

message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
# send data
client.sendto(message.encode(), (target_host,target_port))

# receive data
response, address = client.recvfrom(4096)

#print data
print(response)