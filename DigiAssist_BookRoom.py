import requests

#Static URL
URL="http://35.242.145.13/book/"
API_KEY="47cb9bb88f2546518b38f44a4be72b40"

def bookRoom(location, startDate, endDate, startTime, endTime, bookedBy, meetingName, guests):
                parameter={'startDate': startDate,
                                'endDate' : endDate,
                                  'startTime':startTime,
                                 'endTime': endTime,
                                 'bookBy': bookedBy,
                                 'bookName': meetingName,
                                 'capacity':str(int(guests))}
                stringParams=location
                response = requests.get(url=URL+stringParams, params=parameter)
                resultMessage = response.json()
                print(resultMessage)
                return resultMessage

def cancelRoom(bookedBy):                                         
                stringParams=bookedBy
                response = requests.get(url=URL+"cancel/"+bookedBy)
                resultMessage = response.json()
                print(resultMessage)
                return resultMessage

def getNewsFeed(key, fromDate):
                newsURL="https://newsapi.org/v2/everything?q="+key+"&from="+fromDate+"&sortBy=popularity"+"&apikey="+API_KEY
                response= requests.get(newsURL)
                resultMsg= response.json()
                print(resultMsg)
                return resultMsg
                
                
                
                


