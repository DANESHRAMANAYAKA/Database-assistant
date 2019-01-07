import speech_recognition as sr

r = sr.Recognizer()
ss = ''
with sr.Microphone() as source:
    print ('Say Your Scenario.....!')
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)
    ss=audio


try:

    print (r.recognize_google(audio))
    file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput.txt", "w")
    file.write(r.recognize_google(audio))
    file.close()

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


'''
try:
    print (r.recognize_google(audio))
    file = open("voiceinput.txt", "w")
    file.write(r.recognize_google(audio))
    file.close()

except Exception as e:
    print (e)
    
    '''

