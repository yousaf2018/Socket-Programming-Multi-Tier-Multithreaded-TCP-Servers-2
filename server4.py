from re import U
import socket
import json
import mysql.connector
import secrets

Address = "localhost"

port = 5054

utf8 = "utf-8"
s = socket.socket()

s.bind((Address,port))

s.listen(5)
print("Server4 listening for Authentication")
while True:
    c,addr = s.accept()
    print("Main server connected with server 4 for authentication service ",addr)
    data = c.recv(1024)
    data = data.decode(utf8)
    data = json.loads(data)
    id1 = int(data[0])
    password1 = data[1]
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="a simple identity service"
    )

    mycursor = mydb.cursor()

    sql = """SELECT * FROM users WHERE id = %s and password = %s"""
    mycursor.execute(sql,(id1,password1,))
    myresult = mycursor.fetchall()
    if len(myresult) == 1:
        token = secrets.token_hex(20)
        c.send(token.encode(utf8))
    else:
        c.send("0".encode(utf8))
