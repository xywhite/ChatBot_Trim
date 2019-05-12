import speech_recognition as sr  

class StoText:

    def ListenandReturnText(self):

        sText=""
        r = sr.Recognizer()
        r.energy_threshold =1200
        print("Test:SpeechRecogChinese")   

        with sr.Microphone() as source:
            print("Speak:")                                                                                   
            audio = r.listen(source, timeout=8, phrase_time_limit=20)   
            print("Speak End.") 
        try:
            sText=r.recognize_google(audio, language="zh-CN") #language="zh-CN",show_all=True
            print("Recognize voice as: " + sText)

        except sr.UnknownValueError:
            sText="-1,---"
            
        except sr.RequestError as e:
            sText="-1"
            print("Could not request results; {0}".format(e))

        return sText

