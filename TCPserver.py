import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip= socket.gethostbyname(socket.gethostname())
port = 1234
address = (ip,port)
server.bind(address)
server.listen(5)
print("[*] Listenting to ", address)

print("So far so good")
client,addr = server.accept()

print("Got connected to ",addr[0], ":", addr[1])

while True:
	data = client.recv(1024)
	print("[*]Recived ",data, " From the client" )
	print("Processing")
	if(data==b"Hello"):
		client.send("Hi".encode())
		print("Processing Done\n [*] Reply Sent")
	elif(data==b"Disconnect"):
		client.send("Bye!".encode())
		client.close()
		break
	else:
		client.send("Invalid data".encode())
		print("Processing Done\n [*] Reply Sent")
        
        
        
'''    print("Here")
    print("[*]Accepted connection from: %s:%d" % (addr[0],addr[1]))
    print("[*]Connecetion established from : %s:%d" % (addr[0],addr[1]))
    print("still here")
    client_handler = threading.Thread(target = handle_client, args = (client,))
    client_handler.start()'''