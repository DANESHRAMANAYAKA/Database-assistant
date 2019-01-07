import speech_recognition as sr

r = sr.Recognizer()
ss = ''
with sr.Microphone() as source:
    print ('Say Your Scenario.....!')
    audio = r.listen(source)
    ss=audio
try:
    print (r.recognize_google(audio))
    file = open("sample.txt", "w")
    file.write("ssssssssss")
    file.close()
    print("finish")

except Exception as e:
    print (e)
