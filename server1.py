import socket


Address = "localhost"

port = 5051

s = socket.socket()

s.bind((Address,port))

s.listen(5)
print("Server1 listening for echo service")
while True:
    c,addr = s.accept()
    print("Main server connected for echo service ",addr)
    data = c.recv(1024)
    c.send(data)