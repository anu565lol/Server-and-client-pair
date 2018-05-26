import socket
name = socket.gethostname()
print(name)
client = socket.socket()
client.connect(('192.168.137.1',1234))
