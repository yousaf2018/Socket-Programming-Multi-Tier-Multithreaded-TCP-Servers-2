import json
from os import utime
import socket
from threading import Thread
import time

#create a class that extends/inherits from Thread class
class MyThread(Thread):
    #create a constructor for our class,
    # aurguments for our thread
    utf8 = "utf-8"
    Authurized_users = []
    def __init__(self, client):
        #class the parent constructor that will make sure
        # a separate thread is created, when called
        Thread.__init__(self)
        #save the counter parameter, so that we can use
        #it later
        self.client=client
        #override the run function of the Thread class

    
    def run(self):
        #Receiving data from client what client wants 
        data = self.client.recv(1024)
        data = data.decode(self.utf8)
        #function will call server 4 for authentication of user
        def request_for_authentications(client):
            data = client.recv(1024)
            address = "localhost"
            port = 5054

            c = socket.socket()

            c.connect((address,port))
            print("Connected with server4 for authentication service")
            c.send(data)
            data = c.recv(1024)
            data = data.decode(self.utf8)
            if data == "0":
                client.send("0".encode(self.utf8))
            else:
                self.Authurized_users.append(data)
                client.send(data.encode(self.utf8))  
        #fucntion will verify token and will send service1 info to client
        def request_for_echo_service(client):
            data = client.recv(1024)
            data = data.decode(self.utf8)
            print(data)
            count = self.Authurized_users.count(data)
            if count > 0:
                service1_details = []
                address = "localhost"
                port = 5051
                service1_details.append(address)
                service1_details.append(port)
                service1_details = json.dumps(service1_details)
                client.send(service1_details.encode(self.utf8))
            else:
                client.send("0".encode(self.utf8))

        #fucntion will call service2 from server2
        def request_for_palindrome_service(client):
            data = client.recv(1024)
            data = data.decode(self.utf8)
            print(data)
            count = self.Authurized_users.count(data)
            if count > 0:
                service2_details = []
                address = "localhost"
                port = 5052
                service2_details.append(address)
                service2_details.append(port)
                service2_details = json.dumps(service2_details)
                client.send(service2_details.encode(self.utf8))
            else:
                client.send("0".encode(self.utf8))
            
              

        #fucntion will call service3 from server3
        def request_for_checking_length_service(client):
            data = client.recv(1024)
            data = data.decode(self.utf8)
            print(data)
            count = self.Authurized_users.count(data)
            if count > 0:
                service1_details = []
                address = "localhost"
                port = 5053
                service1_details.append(address)
                service1_details.append(port)
                service1_details = json.dumps(service1_details)
                client.send(service1_details.encode(self.utf8))
            else:
                client.send("0".encode(self.utf8)) 
        #function will logout the user
        def Logout_user(client):
            data = client.recv(1024)
            data = data.decode(self.utf8)
            count = self.Authurized_users.count(data)
            if count > 0:
                self.Authurized_users.remove(data)
                client.send("1".encode(self.utf8))
            else:
                client.send("0".encode(self.utf8)) 
        #If data == 1 tha call server 4 for authentications
        if data == "1":
            request_for_authentications(self.client)
        #if data == 2 than call server 1 for services
        elif data == "2":
            request_for_echo_service(self.client)
            
        #if data == 3 than call server 2 for services
        elif data == "3":
            request_for_palindrome_service(self.client)
    
        #if data == 4 than call server 3 for services
        elif data == "4":
            request_for_checking_length_service(self.client)
        #if data == 5 than logout 
        elif data == "5":
            Logout_user(self.client)


def main():
    Address = "localhost"

    port = 5050

    s = socket.socket()

    s.bind((Address,port))

    s.listen(5)
    print("Main server listening for client")
    while True:
        c,addr = s.accept()
        #Create object for our thread class
        thread=MyThread(c)
        #thread.run()
        #if you start the thread using run() function, it
        #will be executed on the main thread as normal
        #function. Never use the run() function your self
        #rather call the start(), it will create a separate
        # thread, and there it will call the run function
        thread.start()
if __name__=='__main__':
    main()