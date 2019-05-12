from TextToSpeech import TSpeech
from SpeechRecogChinese import StoText
import DigiAssistant_Server as Agent
import DigiAssist_BookRoom as RoomBook
from datetime import timedelta
import datetime
import time
import getpass
import json
#import SocketClient as sClient
#import socket
import requests

tts = TSpeech()
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('35.229.208.102',12345))

class WeChatBot:
    #i=1
    def welcomeSpeech(self):
        name=getpass.getuser()
        if len(name)==0:
            name="Mr.X"
        print(name)

        tts.say ("你好！ 请问有什么可以帮到您呢？")
        #tts.say ("Hello! What can I do for you?")

    def chatAndAct(self):
        strRequest = self.getClientRequestText()
        while (strRequest != "over"):
            print("start while:")
            #Send text to server to get intent
            #strResponse = sClient.sendRequest(strRequest)
            #strResponse = self.sendRequest(strRequest)
            strResponse = self.sendRequest_Api(strRequest)

            self.ActForRequest(strResponse)
            
            #strRequest = self.getClientRequestText_TempOver() #need to remove this line and uncomment next
            strRequest = self.getClientRequestText()
    
    def sendRequest_Api(self, stringText):
        r = requests.get('http://35.229.208.102:5000/'+stringText)
        print("Receive data:{0}".format(r.text))
        return r.text

    def sendRequest(self,stringText):
        s.send(stringText.encode())
        rcvdData = s.recv(8888).decode()
        print ("Receive data:{0}".format(rcvdData))
        return rcvdData

    def getClientRequestText(self):
        objText=StoText()
        stringText=objText.ListenandReturnText()
        print ("Listen and return text:")
        print (stringText)

        #if (self.i==3):
        #    stringText="over"
        #    #s.close()
        #else:
        #    if (self.i==2):
        #        stringText="2 years"
        #    else:
        #        stringText="I can speak English"
        #self.i=self.i+1
        #print(stringText)
        return stringText

    def getClientRequestText_TempOver(self):
        #objText=StoText()
        #stringText=objText.ListenandReturnText()
        stringText="over"
        print(stringText)
        return stringText
    
    #This part is to be used in GCP server
    def translateRequest(self,stringText):
        #Response from Agent
        queryResponse = Agent.detect_intent_texts('df-eva-agent',1,stringText,'en')
        #eep-hackathon12-bpid-301119
        print('queryResponse:')
        print(queryResponse)
        return queryResponse
    
    def ActForRequest(self,queryResponse):
        intentName = json.loads(queryResponse)['queryResult']['intent']['displayName']

        print("intentName:")
        print(intentName)
        
        stringResponse=json.loads(queryResponse)['queryResult']['fulfillmentText']
        print("stringResponse:")
        print(stringResponse)
        tts.say(stringResponse, 'en')
        return stringResponse
        
if __name__ == "__main__":
    wcb=WeChatBot()
    wcb.welcomeSpeech()
    wcb.chatAndAct()