import speech_recognition as sr

r = sr.Recognizer()
ss = ''
with sr.Microphone() as source:
    print ('Say Your Scenario.....!')
    audio = r.listen(source)
    ss=audio
try:
    print (r.recognize_google(audio))
    file = open("voiceinput.txt", "w")
    file.write(r.recognize_google(audio))
    file.close()

except Exception as e:
    print (e)
