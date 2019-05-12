from gtts import gTTS
import pyglet

tts = gTTS('Hello EEP team, how are you? Testing my voice')
tts.save('test.mp3')
song = pyglet.media.load(r'C:\VINAYAKA\PROJECT\DigiAssist\test.mp3')
song.play()

def exiter(dt):
                pyglet.app.exit()
               


pyglet.clock.schedule_once(exiter, song.duration)
pyglet.app.run()



