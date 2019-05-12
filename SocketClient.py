import socket

def sendRequest(stringText):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('35.229.208.102',12345))
    str = stringText
    #s.sendall('Here I am')
    s.send(str.encode())
    rcvdData = s.recv(8888).decode()
    print ("Receive data:{0}".format(rcvdData))
    s.close()
    return rcvdData

#sendRequest('Here I am')