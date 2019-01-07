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
globalerelationship=''
matrix = [[]]#gihan output tabale contentships
matrix2=[[]]#gihan output relationships
relationship1=[]
output1= []
temprelation =''
finalcount=0



def clear():

    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput1.txt", 'r+')
    f.truncate(0)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\gihanfianaloutput.txt",'r+')
    f.truncate(0)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput2.txt", 'r+')
    f.truncate(0)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships.txt", 'r+')
    f.truncate(0)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships2.txt", 'r+')
    f.truncate(0)
    f.truncate(0)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt",'r+')
    f.truncate(0)
    f = open( "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\outputgihan.txt",'r+')
    f.truncate(0)
    f= open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping_relationship.txt",'r+')
    f.truncate(0)
    f = open( "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\gihanfianaloutput.txt",'r+')
    f.truncate(0)



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

                  #  elif (tags == patten7):
                  #      print("Match7")
                   #     filter_Entites(text)
                    #    filter_Relationship(text)

                    else:
                      #check_Attrybuts(line)

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
        global globalerelationship


        lines = token

        sentences = nltk.sent_tokenize(lines)  # tokenize sentences

        nouns = []  # empty to array to hold all nouns

        for sentence in sentences:

            for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
                if (pos == 'VBP' or pos == 'VBZ' or pos == 'VB'):
                    nouns.append(word)
                    relationship = word
                    print('**Relationships------------------>'+word)
                    globalerelationship=word
                    readrelationshipfile()########################


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
                print('Entites**------------------------>' + word)

    printrelationships(lines)



def filter_attri(token):


    #global
    count=0
    global entites_relationships

    lines = token
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


                store_antites(word)

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
    mappingoutput(str(entites_relationships))
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





def Erinputfilecreator(xx):

    primarykey=xx
    key='ww'
    flag='t'


    try:


                file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt",''"a+")
                file1 = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\outputgihan.txt",''"a+")
                defoultkey = '-'
                tablename=''
                count =0
                c = 0#notkeycount
                for x in entites_relationships:

                    count = count + 1

                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!entites_relationships!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

                    print(entites_relationships)

                    if (count == 1):

                        file.write("\n"+"t[" + str(x)+"-"+"\n")
                        file1.write("\n" + "t[" + str(x) + "-" + "\n")
                        count = count + 1
                        tablename=str(x)
                        key=str(x)

                    elif (count != 0 and x == "ID"):
                        print("~~~~~~~~~~~~~~key~~~~~~~~~~~~~~~~~~~~~"+primarykey)
                        flag = 't'
                        file.write("*"+x + "," + "\n")
                        file1.write('[PK]'+x+ "," + "\n")
                        count = count + 1
                        defoultkey= "no"

                    elif(count != 0 and x == "id" and flag=='f'):
                        flag = 't'
                        file.write("*" + x + "\n")
                        file1.write('[PK]'+x+','+ "\n")
                        count = count + 1
                        defoultkey = "no"

                    elif (count != 0 and x == "CODE"and flag=='f'):
                        flag = 't'
                        file.write("*" + x + "," + "\n")
                        file1.write('[PK]'+x+"," + "\n")
                        count = count + 1
                        defoultkey = "no"

                    elif (count != 0 and x == "code" or x == "Code" and flag=='f'):
                        flag = 't'
                        file.write("*" + x + "," + "\n")
                        file1.write('[PK]'+x +"," + "\n")
                        count = count + 1
                        defoultkey = "no"

                    elif (count != 0 and (x == "number" or x == "NUMBER" or x == 'Number')and flag=='f'):
                        flag = 't'
                        file.write("*" + x + "," + "\n")
                        file1.write('[PK]'+x+"," + "\n")
                        count = count + 1
                        defoultkey = "no"


                    elif (count != 0  and defoultkey == "no"):
                        count = count + 1
                        file.write(x + "," +"\n")
                        file1.write(x + "," + "\n")

                    elif (count != 0 and defoultkey == "-"):


                        if(c == 0 and  flag=='f'):
                            c=c+1
                            file.write('*'+tablename+"ID"+ "," + "\n")
                            #file1.write('[PK]'+tablename + "ID"+"," + "\n")
                        if(c != 0):
                            file.write(x + "," + "\n")
                            file1.write(x + "," + "\n")


                file.write("]")
                file1.write("]")
                file.write("\n")
                file1.write("\n")
                file.close()



    except IOError:
        print('An error occured trying to read the file.')



def printrelationships(lines):

    print("printrelationships(lines)")
    relationshipword=(lines)



    try:
        file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships.txt",''"a+")


        file.write(relationshipword)




    except IOError:
        print('An error occured trying to read the file.')


def readrelationshipfile():


    #2darraycounting
    global globalerelationship
    global matrix2
    global relationship1
    wordcount=0
    relationwords = []
    entity1=''
    entity2=''
    thisrelationship=''

    print("working readrelationshipfile()")

    with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships.txt",'r') as f:
        for line in f:


            for word in line.split():
                wordcount = wordcount + 1

                relationwords.append(word)
                print('entity----------->'+str(word))

    entity1=relationwords[0]
    thisrelationship= relationwords[2]
    entity2=relationwords[-1]
    kadanality1=''
    kadanality2=''
    k1=''
    k2=''
    #gihanoutput
    k11=''
    k22=''


    print('entity1---------------------->'+entity1)
    print('relationship----------------->'+globalerelationship)
    print ('entity2--------------------->'+entity2)

    kadanality1=nltk.tag.pos_tag([entity1])
    kadanality2=nltk.tag.pos_tag([entity2])

    '''
                       ['NNS', 'VBP', 'IN', 'NN']
                       ['NNS', 'VBZ', 'DT', 'NN']
                       ['NNS', 'VBP', 'IN', 'NN']
                       ['NNP', 'NN', 'IN', 'NN']
                       ['NN', 'VBZ', 'DT', 'NN']
                       ['NNP', 'VBP', 'NNS']
                       ['NN', 'VB', 'DT', 'NN']
                       '''
    if(kadanality1[0][1]=='NNP' or kadanality1[0][1]=='NN'):
        k1='1'
        k11='@n'
    if (kadanality1[0][1] == 'NNS' or kadanality1[0][1] == 'NNPS'):
        k1 ='*'
        k11='@m'
    if (kadanality2[0][1] == 'NNP' or kadanality2[0][1] == 'NN'):
        k2 ='1'
        k22= '@n'
    if (kadanality2[0][1] == 'NNS' or kadanality2[0][1] == 'NNPS'):
        k2 ='*'
        k22=='@m'

    file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships2.txt", ''"a+")

    relationship2=''

    file.write("\n")
    file.write("r" + "[" + entity1 + " " + globalerelationship + " " + entity2 + "-" + k1 + " " + "to" + " " + k2 + " " + "]")
    file.write("\n")
    relationship1=[]
    file2 = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping_relationship.txt",''"a+")

    relationship1='.'+entity1+';'+k11+';'+k22+';'+'R_'+globalerelationship+';'+'.'+entity2+';'
    file2.write(str(relationship1))
    file2.write('\n')
    relationship2 ='.'+entity2+';'+k22+';'+k11+'R_'+';'+globalerelationship+';'+'.'+entity1+';'
    file2.write(str(relationship2))
    file2.write('\n')

    file2.close()

    print('relationship1========='+str(relationship1))

    #.Bank;@m;@n;R_has;.Branch;


    print(relationwords[0])
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships.txt",'r+')
    f.truncate(0)










def combinetxt():
    global storeantites
    global fullarray
    global gtext

    file = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt",''"a+")

    with open( "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\relationships2.txt","r") as ins:



        i = 0
        for line in ins:
            i = i + 1
            text = line
            gtext = text
            file.write(line)
            file.write("\n")


def mappingoutput(msg):

    global matrix
    global matrix2
    global relationship1

    global globalerelationship

    print("working mappingoutput(msg)"+msg)
    matrix.append(str(msg))
    print(str(matrix))
    #print(str(matrix2))

    print('print(matrix2[0][0])--------------------->')
    #print(relationship1)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping_relationship.txt",'r+')
    #f.write(str(matrix))


def token():
    global matrix
    global matrix2

    string=str(matrix)










def readoutput1():

    global output1

    filterdwerb=''
    count=0
    l=''
    output1=[]

    passkey=''


    f1 = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\outputgihan.txt",'r+')


    flag='f'
    flag2='f'
    count=0
    tempval=''
    tempva2=''

    for words1 in f1.read().split('\n'):
        count=0
        count=count+1

        l=filterdwerb=words1
        l = filterdwerb.strip('-')
        #l=filterdwerb
        # .strip('t[')
        l = l.replace('-', '')
        l=l.replace('t[', '')

        output1.append(l)

    #print("1234666")
    print(output1)


def mapgihan():

    global temprelation



    output1
    sentance_count = 0
    keyword=''

    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping_relationship.txt",'r+')
    f1 = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\outputgihan.txt",'r+')

    for words in f.read().split('\n'):
        sentance_count = sentance_count + 1
        print('  sentance_count=0' + str(sentance_count))

        print(str(words) + '789')
        temprelation=str(words)
        wcount = 0
        for word in words.split(';'):
            if (wcount == 0):
                wcount = wcount + 1
                keyword = str(word)
                keyword = keyword.replace('.', '')

                print(keyword)

                if (keyword != ""):
                    print('keyword-------->' + keyword)
                    print("")

                    filteroutput1(str(keyword))
                    keyword = ''


def filteroutput1(keyword):


    flag1='f'
    flag2='f'
    count=0
    key=keyword
    global output1
    count1 =0
    count2 =0
    temp=[]
    ifcount=0
    string=''


    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\gihanfianaloutput.txt",'r+')
  

    #print("eliment2"+output1[7])
    for element in output1:

        print (str(count)+"----->"+element)
        count=count+1

        if(key == element):
            flag1='t'
            count1=count
            print('find key---->'+str(element))
            flag1 = 't'

        if(element == ']' and flag1=='t' and ifcount==0):
            ifcount=ifcount+1
            print('find key]---->' + str(element))
            count2=count




    temp=output1[count1:count2]
    #str(temp).replace(",", ";")
    string =''.join(temp)

    print('final--------------------->'+string)
    f.write("\n")
    f.write(string)
    f.write("\n")
    combinegihanwithoutput1(string)

def combinegihanwithoutput1(string):

    global output1
    global temprelation
    global finalcount
    localtep=''
    finaloutcome=''

    localtep= str(string).replace(",", ";")
    #localtep = str(string).replace("]", "")

    print('def combinegihanwithoutput--->'+str(temprelation)+localtep)
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\finalmap.txt",'r+')
    f.write("\n")
    finaloutcome=(str(temprelation)+localtep)
    f.write(finaloutcome)
    print(finaloutcome)

    f.write("\n")








##########################################################################################################################################################################################




clear()
removeblankfile()
check_Entity_And_Relatios()
analizer()
combinetxt()
readoutput1()


mapgihan()







