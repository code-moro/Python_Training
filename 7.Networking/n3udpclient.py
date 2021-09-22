import socket
msgfromclient = "Hello UDP Server"

bytesTosend=str.encode(msgfromclient)
serverAddressPort = ('127.0.0.1',20001)

buffersize=1024
UDPCLIENTSOCKET = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPCLIENTSOCKET.sendto(bytesTosend,serverAddressPort)

msgfromserver = UDPCLIENTSOCKET.recvfrom(buffersize)
msg="message from server{}".format(msgfromserver[0])

print(msg)