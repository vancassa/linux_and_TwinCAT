import socket

s = socket.socket()

host = '192.168.52.1'
port = 30000

s.connect((host, port))
print(s.recv(1024))

data = input("Send command: ")
s.send(bytes(data, 'utf8'))
while (data != 'close'):
	print(s.recv(1024))
	data = input("Send command: ")
	s.send(bytes(data, 'utf8'))