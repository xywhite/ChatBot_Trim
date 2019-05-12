from gtts import gTTS
#import pyglet
import os

class TSpeech:
    def say(self, messageText, lang='zh-cn'):
        if messageText=='':
            messageText='No message to play'

        tts = gTTS(text=messageText, lang=lang)
        print("Test:before save mp3")
        tts.save("Message.mp3")
        print("Test:after save mp3")
        os.system("mpg123 Message.mp3") #mpg321
        print("Test:broacast mp3")
        #song = pyglet.media.load("Message.mp3")
        #song.play()

        #def exiter(dt):
        #    pyglet.app.exit()

        #pyglet.clock.schedule_once(exiter, song.duration)
        #pyglet.app.run()

        return 1






