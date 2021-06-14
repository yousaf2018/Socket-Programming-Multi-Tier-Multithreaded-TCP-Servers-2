import socket
import time 
import json
address = "localhost"
utf8 = "utf-8"
port = 5050

c = socket.socket()

c.connect((address,port))
time.sleep(1)
#Getting the choice from client what client to do
print("Enter 1 for login")
print("Enter 2 for using echo service")
print("Enter 3 for checking palindrome")
print("Enter 4 for checking length of string")
print("Enter 5 for logout")
#After input from client call the main server to provide the services the client wanted
check = input()
#Function will send client data for authentication 
def request_main_server_for_authentication():
    c.send("1".encode(utf8))
    login_details = []
    id = input("Please enter your id---->")
    password = input("Please enter your password---->")
    login_details.append(id)
    login_details.append(password)
    login_details = json.dumps(login_details)
    c.send(login_details.encode(utf8))
    data = c.recv(1024)
    data = data.decode(utf8)
    print(data)
    if data == "0":
        print("You are not authurized")
    else:
        print("You are authurized with token---->",data)
        
#Function which will get info for service1 from main server
def request_main_server_for_service1():
    c.send("2".encode(utf8))
    token = str(input("Enter token number for service1---->"))
    c.send(token.encode(utf8))
    data = c.recv(1024)
    data = data.decode(utf8)
    data = json.loads(data)
    if data == "0":
        print("You are allowed to use service with invalid token")
    else:
        address = data[0]
        port = data[1]
        print("Here is information for server 1-->",address,port)
        c1 = socket.socket()
        c1.connect((address,port))
        print("Connected with server1 for echo service")
        data = input("Enter word for echo service--->")
        c1.send(data.encode(utf8))
        data = c1.recv(1024)
        print(data.decode(utf8))
        

#Function which will request for service2 from main server
def request_main_server_for_service2():
    c.send("3".encode(utf8))
    token = str(input("Enter token number for service2---->"))
    c.send(token.encode(utf8))
    data = c.recv(1024)
    data = data.decode(utf8)
    data = json.loads(data)
    if data == "0":
        print("You are allowed to use service with invalid token")
    else:
        address = data[0]
        port = data[1]
        print("Here is information for server 2-->",address,port)
        c1 = socket.socket()
        c1.connect((address,port))
        print("Connected with server2 for palindrome service")
        data = input("Enter your string for palindrome---->")
        c1.send(data.encode(utf8))      
        data = c1.recv(1024)
        data = data.decode(utf8)
        print(data)
#Function which will request for service3 from main server
def request_main_server_for_service3():
    c.send("4".encode(utf8))
    token = str(input("Enter token number for service3---->"))
    c.send(token.encode(utf8))
    data = c.recv(1024)
    data = data.decode(utf8)
    data = json.loads(data)
    if data == "0":
        print("You are allowed to use service with invalid token")
    else:
        address = data[0]
        port = data[1]
        print("Here is information for server 3-->",address,port)
        c1 = socket.socket()
        c1.connect((address,port))
        print("Connected with server3 for length checking service")
        data = input("Enter word for length checking--->")
        c1.send(data.encode(utf8))
        data = c1.recv(1024)
        print(data.decode(utf8))
#Function will logout user 
def Logout_user():
    c.send("5".encode(utf8))
    token = str(input("Enter token number for Logout---->"))
    c.send(token.encode(utf8))
    data = c.recv(1024)
    data = data.decode(utf8)
    if data == "1":
        print("Successfully logout Sir")
    else:
        print("Not able to logout due to invalid token")      
#Condition will check if user want to login
if check == "1":
    request_main_server_for_authentication()
#If check == 2 than call main server to provide service1
elif check == "2":
    request_main_server_for_service1()
#If check == 3 than call main server to provide service2
elif check == "3":
    request_main_server_for_service2()
    
#If check == 4 than call main server to provide service3
elif check == "4":
    request_main_server_for_service3()
#If check == 5 than call main server to logout user
elif check == "5":
    Logout_user()