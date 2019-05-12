import socket
#from ChatBot import WeChatBot
import DigiAssistant_Server as Agent

#wcb = WeChatBot()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from:")
print (addr)
i=1
while True:
    rcvdData = c.recv(1024).decode()
    print ("Receive data:{0}".format(rcvdData))
    sendData = Agent.detect_intent_texts('df-eva-agent',1,rcvdData,'en')#wcb.translateRequest(rcvdData)
    c.send(sendData.encode())
    print ("Send data:{0}".format(sendData.encode().decode()))

    i=i+1
    #if(sendData == "Bye" or sendData == "bye" or sendData == "over"):
    if(i == 3):
        break
c.close()
