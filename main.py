import pyjokes as PJ
import pyttsx3
import random
import winsound

laugh = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3", "6.mp3"]
joke_maker = PJ.get_joke()
voice = random.choice(laugh)


def laughter():
    winsound.PlaySound('1.mp3', winsound.SND_ASYNC)


def joke():
    print(joke_maker)
    engine = pyttsx3.init()
    engine.say(joke_maker)
    laughter()
    engine.runAndWait()
    engine.stop()


joke()
