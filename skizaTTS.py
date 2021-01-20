import pyttsx3, time
eng = pyttsx3.init()
eng.setProperty('rate', 130)
eng.setProperty('volume', 1.1)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
time.sleep(3)
eng.say('Hello,')
eng.runAndWait()
eng.say('I am HOST, Host stands for Heart Of Stark. I was created by Oliver who goes by the pseudoname Gamine. I am running on Sphinx, from a Deepin Linux node, the new coolest linux distro')
eng.runAndWait()
eng.setProperty('voice', en_voice_id)
#eng.say('Sorry, i didnt catch that. Please repeat')
eng.say("I look up to ULTRON, why not Jarvis you'd ask, well ... JARVIS is a sissy. Its just another rather Very Intelligent system while Ultron is super dark and powerful.")
eng.say('the time is 9:39pm ')
eng.runAndWait()