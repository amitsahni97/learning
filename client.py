import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message=input()

host=socket.gethostname()

port=12345

s.connect((host, port))

s.send(message.encode())
print("\nSending data:",message)

data=s.recv(1000).decode()
print("Echo",data)

print("Asking for reverse message")
s.send("asks reverse message".encode())

reverse_data=s.recv(1000).decode()
print("data received",reverse_data)

if(reverse_data=="cquit"):
    print("closing client")


s.close()

