# python interpreter session, since you only have to do it once
import nltk
#nltk.download()
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import RegexpParser
from nltk.corpus import brown
import sys
import re
from nltk.corpus import brown

gsentences = ""
string = ""
segment = ""
sentences_tokenized = []
nouns = ""
verbs = ""
result3 = ""
###############################################
Entites = []
relationship = []
Attrybuts = []
storeantites = []
fullarray = {}
entites_relationships = []
entites_relations = []
gtext = ''
gtags = ''
grelationship = ''



def readfile():
        print(" readfile()")
        global gsentences
        f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\exefiles\\spech2txt\\dist\\Script\\sample.txt","r")
        gsentences = f.readlines()
        f.close()
        print('---1Speachfileread---')
        print(gsentences)


def segment():

        global gsentences
        for i in gsentences:
                ch = i

        print("----------text-string-------------------")
        print(ch)

        print('----------segment-----------------------')
        print(sent_tokenize(ch))


        segfileright()
######################################################################Mapinput###################################################################################
def removeblankfile():

    try:
        with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput.txt","r") as fileobj:
            for line in fileobj:
                print(line)

                for ch in line:
                    if ch != ".":
                        file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput1.txt", "a+")
                        file.write(ch)

                    if ch == ".":
                        file.write('\n')

        file.close()


    except Exception as e:
        print (e)







    try:
        with open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput1.txt') as infile, open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput2.txt','w') as outfile:
            for line in infile:
                if not line.strip(): continue  # skip the empty line
                outfile.write(line)  # non-empty line. Write it to output


        file.close()


    except Exception as e:
        print (e)

    #with open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput1.txt') as infile, open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput2.txt', 'w') as outfile:
     #     if not line.strip(): continue  # skip the empty line
       #     outfile.write(line)  # non-empty line. Write it to output




def segfileright():


        try:
              with open("'D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput.txt'","r") as fileobj:
                    for line in fileobj:
                        print(line)

                        for ch in line:
                                if ch != ".":

                                    file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput1.txt", "a+")
                                    file.write(ch)

                                if ch == ".":
                                       file.write('\n')

              file.close()


        except Exception as e:
            print (e)


def tokenize():

        global sentences_tokenized
        try:
              with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\ScriptsegmentOutput.txt", "a+") as fileobj:

                    for line in fileobj:
                           for ch in line:
                                 if ch == '\n':

                                      #  file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\tokenize.txt", "a+")
                                      #  file.write(ch)
                                       print(line)
                                       for s in gsentences:
                                               sentences_tokenized.append(word_tokenize(line))
                                               print('---tokenize---')
                                               print(sentences_tokenized)

                                 if ch == "." or ch == "!":
                                         print("")

              file.close()

        except Exception as e:
            print (e)

def postag():
        print(" postag())")

        global result3

        print("----------Resultofpostaging------------")
        file = open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\ScriptsegmentOutput.txt','r')
        text = file.read() # read the contents of the text file into a variable
        result1 = nltk.sent_tokenize(text)
        result2 = [nltk.word_tokenize(sent) for sent in result1]
        result3 = [nltk.pos_tag(sent) for sent in result2]


        print(result3)


def filterpattens():

        global result3

        file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\postokenize.txt", "a+")
        file.write(str(result3))

        file.close()




def filternouns():

        print("-------------------nouns-----------------")
        file = open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\ScriptsegmentOutput.txt','r')

        lines = file.read()  # read all lines

        sentences = nltk.sent_tokenize(lines)  # tokenize sentences

        nouns = []  # empty to array to hold all nouns

        for sentence in sentences:


             for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
                 if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                     nouns.append(word)

                     print(word)

def filterverbs():

        print("-------------------VERBS-----------------")
        file = open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\ScriptsegmentOutput.txt','r')

        lines = file.read() #read all lines

        sentences = nltk.sent_tokenize(lines) #tokenize sentences

        nouns = [] #empty to array to hold all nouns

        for sentence in sentences:
             for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
                 if (pos == 'VBP' or pos == 'VBZ'):
                     nouns.append(word)

                     print(word)

def filterrelationship():

        print("-------------------Relationships-----------------")
        file = open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\ScriptsegmentOutput.txt','r')

        lines = file.read() #read all lines

        sentences = nltk.sent_tokenize(lines) #tokenize sentences

        nouns = [] #empty to array to hold all nouns

        for sentence in sentences:


             for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
                 if (pos == 'VBP'):
                     nouns.append(word)

                     print(word)


def filterEntity():

        print("-------------------Entity-----------------")
        file = open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\dist\\ScriptsegmentOutput.txt','r')

        lines = file.read() #read all lines

        sentences = nltk.sent_tokenize(lines) #tokenize sentences

        nouns = [] # empty to array to hold all nouns

        for sentence in sentences:


             for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
                 if (pos == 'NNP'):
                     nouns.append(word)

                     print(word)


def check_Entity_And_Relatios():

        global storeantites
        global fullarray
        global  gtext

        global grelationship

        print(" check_Entity_And_Relatios")


        with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput2.txt","r") as ins:

                patten1 = ['NN', 'VB', 'IN', 'NN']
                patten2 = ['NN', 'VBZ', 'DT', 'NN']

                patten3 = ['NN', 'VB', 'IN', 'NN']
                patten4 = ['NN', 'NN', 'IN', 'NN']
                patten5 = ['NN', 'VBZ', 'DT', 'NN']
                patten6 = ['NN', 'VB', 'NN']
                patten7 = ['NN', 'VBZ', 'DT', 'NN']

                i=0
                for line in ins:
                    i=i+1
                    text=line
                    text=text.translate(None, '.')
                    print(i)
                    print('xxx'+text)
                    txt = nltk.word_tokenize(text)
                    #txt kiyanne token karapu wachana tica
                    tagged = nltk.pos_tag(txt)
                    tags = [e[1] for e in tagged]

                    tags = [s.strip('S') for s in tags]
                    tags = [s.strip('P') for s in tags]
                    tags = [s.strip('Z') for s in tags]

                    gtext=text

                    print(tags)
                    gtags = tags

                    if(tags == patten1):
                        print("Match1")
                        filter_Entites(text)
                        filter_Relationship(text)

                    elif(tags == patten2):
                        print("Match2")
                        filter_Entites(text)
                        filter_Relationship(text)

                    elif(tags == patten3):
                        print("Match3")
                        filter_Entites(text)
                        filter_Relationship(text)

                    elif (tags == patten4):
                        print("Match4")
                        filter_Entites(text)
                        filter_Relationship(text)


                    elif(tags == patten5):
                        print("Match5")
                        filter_Entites(text)
                        filter_Relationship(text)

                    elif (tags == patten6):
                        print("Match6")
                        filter_Entites(text)
                        filter_Relationship(text)
                        grelationship=text

                  #  elif (tags == patten7):
                  #      print("Match7")
                   #     filter_Entites(text)
                    #    filter_Relationship(text)

                    else:
                      #check_Attrybuts(line)
                        #grelationship = line
                        del storeantites[:]
                        filter_attri(line)
                        print ("Notmatch")


                    #relationship tag_pttens
                    '''
                    ['NNS', 'VBP', 'IN', 'NN']
                    ['NNS', 'VBZ', 'DT', 'NN']
                    ['NNS', 'VBP', 'IN', 'NN']
                    ['NNP', 'NN', 'IN', 'NN']
                    ['NN', 'VBZ', 'DT', 'NN']
                    ['NNP', 'VBP', 'NNS']
                    ['NN', 'VB', 'DT', 'NN']
                    '''


def check_Attrybuts(line):


          print(line)


def analizer():

     global Attrybuts
     global Entites

     #print("analizer")
     #print (Attrybuts)
     #print (Entites)



####################################################################################################################################################################################

def filter_Relationship(token):


        global Entites
        global relationship


        lines = token

        sentences = nltk.sent_tokenize(lines)  # tokenize sentences

        nouns = []  # empty to array to hold all nouns

        for sentence in sentences:

            for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
                if (pos == 'VBP' or pos == 'VBZ' or pos == 'VB'):
                    nouns.append(word)
                    relationship = word
                    print('**Relationships------------------>'+word)
                    print("call printrelationships(lines)")
                    printrelationships(lines)




def filter_Entites(token):

    global entites_relations

    lines = token

    sentences = nltk.sent_tokenize(lines)  # tokenize sentences


    nouns = []  # empty to array to hold all nouns


    for sentence in sentences:

        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):


                if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                    entites_relations.append(word)
                    relationship = word
                    print('Entites*0------------------------>' + word)







#identfy and write entiies and atrybute
def filter_attri(token):


    #global
    count=0
    global entites_relationships
    global grelationship
    lines = token
    grelationship=token
    sentences = nltk.sent_tokenize(lines)  # tokenize sentences

    nouns = []  # empty to array to hold all nouns
    Attrybuts =[]
    for sentence in sentences:

        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):

            if(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                nouns.append(word)

                if (count == 0):
                    count = count + 1

                    print('Entites22------------------------>' + word)
                    entites_relationships.append(word)
                    print(count)

                elif(count <= 1 ):
                    print('Attribiutes22------------------------>' + word)
                    entites_relationships.append(word)

                #print('Attribiutes------------------------>' + word)
                store_antites(word)
                #return (attry)
    print("entite list"+str(entites_relationships))
    Erinputfilecreator(str(entites_relationships))


    write_entites_and_attrybute()
    del entites_relationships[:]

    #print(nouns)


def store_antites(word):
    #store entites

    global storeantites
    storeantites.append(word)


def write_entites_and_attrybute():

    global entites_relationships
    msg="sssssss"+str(entites_relationships)
    print(msg)
    file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\entites_and_attrybute.txt", "a+")
    file.write(str( entites_relationships))
    file.write("\n")
    file.close()



def relationship_among_entites():

    global entites_relations
    print("s")

    file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\entites_and_attrybute.txt", ''"a+")
    file.write(str(entites_relationships))
    file.write("\n")
    file.close()

def erinterface():


    #print (str(entites_relationships[0]))
    #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    ststus=''
    count = 0
    ststus = 'keyfound'
    for x in entites_relationships:
            count= count+1
            if (x == "ID" or x == "Id" or x =="Id" ):

                    ststus='keyfound'
                    print('statusssssssssssssssssssssssssss-'+ststus)

                    Erinputfilecreator(x)


            elif ((x == "code" or x == "Code" or x=="CODE") and ststus !='keyfound' and count == 2):
                    count = count + 1
                    Erinputfilecreator(x)
                    ststus = 'keyfound'
                    print('statusssssssssssssssssssssssssss2222222222222222222222222222-' + ststus)

            elif ((x == "number" or x == "NUMBER" or x == 'Number')and ststus !='keyfound' and count == 3):
                    count = count + 1
                    Erinputfilecreator(x)
                    ststus = 'keyfound'
                    print('statusssssssssssssssssssssssssss333333333333333333333333333333-' + ststus)
            else:
                  #Erinputfilecreator(x)
                    print("")




            #if(ststus == 'keyfound' ):
             #   Erinputfilecreator(x)

            #if (ststus == 'Notkeyfound'):
             #   print("")
              #  Erinputfilecreator2(sentence)







def Erinputfilecreator(xx):

    primarykey=xx
    key='ww'


    try:


                file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt",''"a+")

                defoultkey = '-'
                tablename=''
                count =0
                c = 0#notkeycount
                for x in entites_relationships:

                    count = count + 1
