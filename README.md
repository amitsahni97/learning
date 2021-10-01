1. Implement a continuous echo messaging client & server using TCP Sockets

• Client will read input from console and send to server

• Server will reverse/toggle the string send by client and echo back 6

• If client detects input as “cquit” client will perform active close, server should detect

client closure and exit.

• If received data from client to server is “squit”, server will perform active close, client

should detect server closing client conn and exit.