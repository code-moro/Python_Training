import socket
localIP='127.0.0.1'
localport=20001

bufferSize=1024

msgFromServer="Hello UDP client"
bytesToSend=str.encode(msgFromServer)

UDPSERVERSOCKET=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPSERVERSOCKET.bind((localIP,localport))

print("UDP server up and listening...")

while True:
    bytesAddressPair=UDPSERVERSOCKET.recvfrom(bufferSize)
    message=bytesAddressPair[0]
    address=bytesAddressPair[1]
    clientmsg="Message from client{}".format(message)
    ClientIP="Cilent IP address{}".format(address)
    print(clientmsg)
    print(ClientIP)

    UDPSERVERSOCKET.sendto(bytesToSend,address)