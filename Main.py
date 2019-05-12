from TextToSpeech import TSpeech
from SpeechRecogChinese import StoText
import DigiAssistant_Server as Agent
import DigiAssist_BookRoom as RoomBook
from datetime import timedelta
import datetime
import time
import getpass
import json

def checkAllValuesPresent(parameters):
        val=json.loads(json.dumps(parameters))
        print(val)
        if val[0]['parameters']['time.original']!="" and val[0]['parameters']['date.original']!="" and  val[0]['parameters']['guests.original']!="" and val[0]['parameters']['duration.original']!=""  and val[0]['parameters']['location.original']!="":
            return True
        else:
            return False

def getStartDate(parameters):
        val=json.loads(json.dumps(parameters))        
        if  val[0]['parameters']['date']!="" :
            dateVal=val[0]['parameters']['date']
            dateVal = dateVal[0:10]
            return dateVal

def getEndDate(parameters):
        val=json.loads(json.dumps(parameters))       
        if  val[0]['parameters']['date']!="" :
            dateVal=val[0]['parameters']['date']
            dateVal = dateVal[0:10]
            return dateVal

def getStartTime(parameters):
        val=json.loads(json.dumps(parameters))        
        if  val[0]['parameters']['time']!="" :
            dateVal=val[0]['parameters']['time']
            dateVal = dateVal[11:16]
            return dateVal

def getEndTime(parameters):
        val=json.loads(json.dumps(parameters))
        endTime=datetime.datetime.strptime(val[0]['parameters']['time'][0:16],"%Y-%m-%dT%H:%M")
        if  val[0]['parameters']['duration']['amount']!="" :
            dateVal=val[0]['parameters']['duration']['amount']
            endTime = endTime + timedelta(minutes=dateVal)   
            return endTime.strftime("%H:%M")

def getLocation(parameters):
        val=json.loads(json.dumps(parameters))        
        if  val[0]['parameters']['location.original']!="" :
            dateVal=val[0]['parameters']['location.original']            
            return dateVal

def getGuests(parameters):
        val=json.loads(json.dumps(parameters))        
        if  val[0]['parameters']['guests']!="" :
            dateVal=val[0]['parameters']['guests']           
            return dateVal


tts = TSpeech()
objText=StoText()
name=getpass.getuser()

if len(name)==0:
    name="Mr.X"
print(name)


#tts.say ("你好！ 先生, 请问有什么可以帮到您呢？")
#stringText=objText.ListenandReturnText()
#print(stringText)
stringText="I can speak English"

while (stringText != "over"):
    print("start while:") 
    #Response from Agent
    queryResponse = Agent.detect_intent_texts('df-eva-agent',1,stringText,'en')
    print('queryResponse:')
    print(queryResponse)
    #eep-hackathon12-bpid-301119
    intentName = json.loads(queryResponse)['queryResult']['intent']['displayName']

    print("intentName:")
    print(intentName)
    
    if intentName=='room-cancel':
        result=RoomBook.cancelRoom(getpass.getuser())
        tts.say(result['description'])
        break

    if intentName=='news-feed':
        result=RoomBook.getNewsFeed('HSBC',  datetime.datetime.now().strftime('%Y-%m-%d'))
        #result=RoomBook.getNewsFeed('HSBC',  '2018-11-23')

        if result['totalResults']>0:
            tts.say(result['articles'][0]['title'])
        else:
            tts.say('No  news Today')
        break
    
    print ("actionText:")
    actionText = json.loads(queryResponse)['queryResult']['action']
    print (actionText)
    
    #Check if we have received all required data for booking a room
    if actionText!='input.unknown' and checkAllValuesPresent(json.loads(queryResponse)['queryResult']['outputContexts'])==True:

        userName= getpass.getuser()
        startDate = getStartDate(json.loads(queryResponse)['queryResult']['outputContexts'])
        endDate=getEndDate(json.loads(queryResponse)['queryResult']['outputContexts'])
        startTime = getStartTime(json.loads(queryResponse)['queryResult']['outputContexts'])
        endTime = getEndTime(json.loads(queryResponse)['queryResult']['outputContexts'])
        meetingName = userName + " - Meeting"
        location = getLocation(json.loads(queryResponse)['queryResult']['outputContexts'])
        guests= getGuests(json.loads(queryResponse)['queryResult']['outputContexts'])
        
        if guests==-1:
            guests=4
            
        result = RoomBook.bookRoom(location, startDate, endDate, startTime, endTime, userName, meetingName, guests)
        
        #If all values are available then call function to book a room
        tts.say(result['description'])
        break
     
    #Else
    stringResponse=json.loads(queryResponse)['queryResult']['fulfillmentText']
    tts.say(stringResponse)
    stringText=objText.ListenandReturnText()
    #print(stringText)


