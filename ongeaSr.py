"""using Speech Recognition module in python"""
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Though shall now speak: ")
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print("Thine lips have parted and uttered: {}".format(text))
	except:
		print("Sorry, i didn't get that :-)")