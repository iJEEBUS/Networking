import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# add the option to reuse the socket later
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client.bind((target_host, target_port))

message = "This is an initial test for the UDP client."
# send data
client.sendto(message.encode(), (target_host,target_port))

# receive data
response, address = client.recvfrom(4096)

#print data
print(response, address)