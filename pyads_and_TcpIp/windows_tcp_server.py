import socket
import pyads

s = socket.socket()

host = '192.168.52.1'
port = 30000


pyads.open_port()
pyads.get_local_address()
adr = pyads.AmsAddr('10.123.66.28.1.1', 851)

s.bind((host, port))

s.listen(1)

conn, addr = s.accept()

print('Connection address:', addr)
conn.send(b'connected')
data = conn.recv(1024)
while (data != b'close' and data != b''):
    print("received data:", data)
    if data == b'read':
    	var = pyads.read_by_name(adr, 'MAIN.test', pyads.PLCTYPE_BOOL)
    	print(var)
    	conn.send(bytes(str(var), 'utf8'))
    elif data == b'write 1':
    	pyads.write_by_name(adr, 'MAIN.test', True, pyads.PLCTYPE_BOOL)
    	conn.send(data) #echo
    elif data == b'write 0':
    	pyads.write_by_name(adr, 'MAIN.test', False, pyads.PLCTYPE_BOOL)
    	conn.send(data) #echo
    else:
    	conn.send(data) #echo
    data = conn.recv(1024)

conn.close()
