import socket

#Client asks for user input
host = input('Enter a host: ')
port = int(input('Enter a port: '))

#Client displays a message for the user
print(f'Checking {host} on port {port}...')

#Varible "client" is assigned to socket module with given functions and parameters
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Client variable sends data to host for host to respond
client.connect((host, port))

#To send data with user input for "host" variable, variable "somedata" is assigned to formatted string containing "host" variable and then encoded into bytes
somedata = (f'GET / HTTP/1.1\r\nHost: {host}\r\n\r\n')
client.send(somedata.encode(encoding='UTF-8'))

#Client recieves data from host and prints a human-readable result
result = client.recv(4096)
print(result.decode())

#Client closes connection
client.close()
