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




def clear():
    f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput1.txt", 'r+')
    f.truncate(0)


def readeroutput():
    print("Read_outputFile")
    global gsentences
    #f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt","r")

    entity=''
    relationship=''
    entity1=''
    entity2=''
    cadanality=''
    cadanaliti1=''
    cadanaliti2 = ''
    temp2=''
    key1=''
    key2=''
    flagtable='t'
    temp4=[]




    with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt", "r") as myfile:
        for line in myfile:
            print line
            if(line[:2] == 'r['):

                temprelay=""
                print("catch"+">>>>"+line[:2])

                temp=''
                temp =line[2:-2]
                print(temp)
                entity, cadanality  = temp.split('-')
                cadanaliti1 =cadanality[0]
                cadanaliti12 =cadanality[5]
                print("relationship>>"+entity)
                print("cadanalities>>"+cadanality)
                print("cadanalities1>>" + cadanaliti1)
                print("cadanalities2>>" + cadanaliti12)

                entity1, relationship, entity2 =entity.split(' ')
                key1=entity1
                key2=entity2

                print("entity1>>"+entity1)
                print("relationship>>"+relationship)
                print("entity1>>"+entity2)


                if(cadanaliti1 == "*" and cadanaliti12=="*"):
                    cadanaliti1 ="@n"
                    cadanaliti12="@m"

                if (cadanaliti1 == "1" and cadanaliti2 == "*"):
                    cadanaliti1 = "@1"
                    cadanaliti12 = "@m"


                if(cadanaliti1 == "*" and cadanaliti12=="1"):
                    cadanaliti1 = "@m"
                    cadanaliti12 = "@1"
                if (cadanaliti1 == "1" and cadanaliti12 == "1"):
                    cadanaliti1 = "@1"
                    cadanaliti12 = "@1"

                temp4 = []
                #relationships---------------------------------------------------------------------------------------------------------------------------------------------------
                with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt","r") as myfile1:
                    for line1 in myfile1:
                        cloum=''

                        if (line1[:2] == 't['):
                            flagtable='t'
                            print "identify_tabale>>>" + line1[2:-2]
                            tablename=line1[2:-2]


                        if(line1 [:1] == ']'):
                                flagtable = 'f'
                                #if(flagtable !='t' and tablename==key1):

                        if(flagtable!= 'f' and tablename ==entity1) :
                            print ">>>>filterVAL>>>>"+entity1
                            cloum=line1
                            print("cloum????"+cloum)
                            temp4.append(cloum)
                            print(temp4)
                            temp4 = [s.rstrip() for s in temp4]

                print(temp4.pop(0))

                print(temp4)

                pk=temp4[0]
                pk=pk[1:]
                pk="[PK]"+pk
                print pk
                print temp4
                del temp4[0]
                print(temp4)
                temp4.insert(0, pk)
                print(temp4)
                val=''.join(temp4)

                print(val)
                ss=str(temp4)[1:-1]

                #ss=ss[2:]
                #ss.pop(0)
                #print ss[0:]

                print cadanaliti1.replace("*", "@m")

                if (cadanaliti1=="1"):
                    cadanaliti1="@1"
                if (cadanaliti2 == "*"):
                    cadanaliti2 = "@m"

                val = val.rstrip(',')
                cadanaliti2=(cadanaliti12.replace("*","@m"))

                #.Bank;@1;@1;R_has;.Branch;[PK]bankid;bankname;[MV]tp;email
                str1="."+entity1+";"+cadanaliti1.replace("*","@m")+";"+cadanaliti12.replace("*","@m")+";R_"+relationship+";"+"."+entity2+";"+val
                print(str1)

                str2 = "."+entity2+";"+cadanaliti2.replace("*","@m")+ ";" + cadanaliti1.replace("*","@m") + ";" + entity1 + ";R_" + relationship;
                #bind(entity2)
                writewalues(str1)
    bind()



#def bind(keybind):
def bind():


    print("!!!!!!!!!!!!!!!!!!!!!!!!!BIND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!BIND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!BIND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Read_outputFile")
    global gsentences
    # f = open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt","r")

    entity = ''
    relationship = ''
    entity1 = ''
    entity2 = ''
    cadanality = ''
    cadanaliti1 = ''
    cadanaliti2 = ''
    temp2 = ''
    key1 = ''
    key2 = ''
    flagtable = 't'
    temp4 = []

    with open( "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt","r") as myfile:
        for line in myfile:
            print line
            if (line[:2] == 'r['):

                temprelay = ""
               # print("catch" + ">>>>" + line[:2])

                temp = ''
                temp = line[2:-2]
                #print(temp)
                entity, cadanality = temp.split('-')
                cadanaliti1 = cadanality[0]
                cadanaliti12 = cadanality[5]
                #print("relationship>>" + entity)
                #print("cadanalities>>" + cadanality)
                #print("cadanalities1>>" + cadanaliti1)
                #print("cadanalities2>>" + cadanaliti12)

                entity1, relationship, entity2 = entity.split(' ')
                key1 = entity1
                key2 = entity2

                #print("entity1>>" + entity1)
                #print("relationship>>" + relationship)
                #print("entity1>>" + entity2)

                if (cadanaliti1 == "*" and cadanaliti12 == "*"):
                    cadanaliti1 = "@n"
                    cadanaliti12 = "@m"

                if (cadanaliti1 == "1" and cadanaliti2 == "*"):
                    cadanaliti1 = "@1"
                    cadanaliti12 = "@m"

                if (cadanaliti1 == "*" and cadanaliti12 == "1"):
                    cadanaliti1 = "@m"
                    cadanaliti12 = "@1"
                if (cadanaliti1 == "1" and cadanaliti12 == "1"):
                    cadanaliti1 = "@1"
                    cadanaliti12 = "@1"

                temp4 = []
                # relationships---------------------------------------------------------------------------------------------------------------------------------------------------
                with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\output1.txt","r") as myfile1:
                    for line1 in myfile1:
                        cloum = ''

                        if (line1[:2] == 't['):
                            flagtable = 't'
                            print "identify_tabale>>>" + line1[2:-2]
                            tablename = line1[2:-2]

                        if (line1[:1] == ']'):
                            flagtable = 'f'
                            # if(flagtable !='t' and tablename==entity2):

                        if (flagtable != 'f' and tablename == entity2):
                            print ">>>>filterVAL>>>>" + entity1
                            cloum = line1
                            print("cloum????" + cloum)
                            temp4.append(cloum)
                            print(temp4)
                            temp4 = [s.rstrip() for s in temp4]

                print(temp4.pop(0))

                print(temp4)

                pk = temp4[0]
                pk = pk[1:]
                pk = "[PK]" + pk
                print pk
                print temp4
                del temp4[0]
                print(temp4)
                temp4.insert(0, pk)
                print(temp4)
                val = ''.join(temp4)

                print(val)
                ss = str(temp4)[1:-1]

                # ss=ss[2:]
                # ss.pop(0)
                # print ss[0:]

                print cadanaliti1.replace("*", "@m")

                if (cadanaliti1 == "1"):
                    cadanaliti1 = "@1"
                if (cadanaliti2 == "*"):
                    cadanaliti2 = "@m"


                #.Bank;@1;@1;R_has;.Branch;[PK]bankid;bankname;[MV]tp;email

                cadanaliti2 = (cadanaliti12.replace("*", "@m"))
                str1 = "." + entity1 + ";" + cadanaliti1.replace("*", "@m") + ";" + cadanaliti12.replace("*","@m") + ";" + entity2 + ";R_" + relationship + ";" + val

                val = val.rstrip(',')

                str2 = "." + entity2 + ";" + cadanaliti2.replace("*", "@m") + ";" + cadanaliti1.replace("*","@m")+"R_" +relationship + ";"+"." + entity1 +";"+ val
                print(str2)
                writewalues(str2)




def writewalues(val):
    with open('D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping.txt', 'a+') as the_file:
        the_file.write(val.replace(",",";"))
        the_file.write('\n')


def removeduplicaates():

    input_file = "input.txt"
    with open(input_file, "rb") as fp:
        lines = fp.readlines()
        new_lines = []
        for line in lines:
            # - Strip white spaces
            line = line.strip()
            if line not in new_lines:
                new_lines.append(line)

    output_file = "output.txt"
    with open(output_file, "wb") as fp:
        fp.write("\n".join(new_lines))








clear()
readeroutput()
#bind()





