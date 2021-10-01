import socket

def reverse(x):
  return x[::-1]

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()

port=12345

s.bind((host, port))

s.listen(5)


count=0
while True:
    count=count+1
    print("\nWaiting for connection.....",count)
    c, addr=s.accept()

    print("\nConnection established")
    print("recieved request from", addr)

    data=c.recv(1000)
    print("\nReceived")

    print("Response Sent")
    c.send(data)

    data1=c.recv(1000)
    rev=reverse(data)
    c.send(rev)

    if data=="squit":
        print("\nClosing server window")
        break

s.close()






