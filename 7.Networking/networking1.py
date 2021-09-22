import socket
s=socket.socket()
print("Socket Successfully created.....")

#port >1024

port =65432
s.bind(('',port))
print("Socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")

while True:
    c,addr=s.accept()
    print("Got connection from",addr)

    s.send("connection",encode())
    s.close()