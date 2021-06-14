import socket


Address = "localhost"

port = 5053

s = socket.socket()

s.bind((Address,port))

s.listen(5)
print("Server3 listening for string length checking service")
while True:
    c,addr = s.accept()
    print("Main server connected for stirng length checking service ",addr)
    data = c.recv(1024)
    data = data.decode("utf-8")
    data = str(len(data))
    c.send(data.encode("utf-8"))