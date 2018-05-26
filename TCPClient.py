import socket
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
'''Enter your ip in place of socket.gethostbyname(socket.gethostname()) and change the port accoedingly'''
ip = socket.gethostbyname(socket.gethostname())
print(ip)
port = 1234
address = (ip,port)
client.connect(address)




request = "Hello"

client.send(request.encode())
result = client.recv(1024)
print(result)