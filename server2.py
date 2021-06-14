import socket


Address = "localhost"

port = 5052

s = socket.socket()

s.bind((Address,port))

s.listen(5)
#function for checking palindrome
def isPalindrome(data):
    
    reverse = ''.join(reversed(data))

    if (data == reverse):
        return True
    return False
print("Server2 listening for palindrome service")
while True:
    c,addr = s.accept()
    print("Main server connected for palindrome service ",addr)
    data = c.recv(1024)
    data = data.decode("utf-8")

    
    check = isPalindrome(data)
    
    if (check==True):
        c.send("Yes".encode("utf-8"))
    else:
        c.send("No".encode("utf-8"))
