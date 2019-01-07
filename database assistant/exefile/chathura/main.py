import re
from __builtin__ import list
import pytesseract
from PIL import Image
import cv2

im = Image.open("eng.jpg")

#gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(im, lang='eng').replace('\n', ' ').replace('  ', ' ')

split = text.split(".")


f = open('ER.txt','r+')
f.truncate(0)

def processTable(line):
    if 'table has these attribute' in line.lower():

        data = re.split('table has these attribute', line, flags=re.IGNORECASE)



        data[1] = data[1].replace(
            data[1][-data[1].index(' '):data[1].lower().index(' as primary key')],
            '*' + data[1][-data[1].index(' '):data[1].lower().index(' as primary key')].strip()).replace(
            ' as primary key', '')


        data[1] = data[1].replace('\n', ' ').replace(' as foreign key', '*')
        export = 't[' + data[0].replace(" ", "")+ "-" + data[1] + ']'

        intoFile(export)

        print (data[0])

        print(data[1])

        print (export)

        #print ("identify entity and relationship")





    elif 'relation' in line.lower():


        export = 'r[' + line[0:line.lower().index(' table has')].split(' ')[
            len(line[0:line.lower().index(' table has')].split(' ')) - 1] + ' has ' + \
                 line[line.lower().index('relation with ') + len('relation with '):len(line)].split(' ')[
                     0] + '- ' + line[line.lower().index('table has ') + len('table has '):line.lower().index(
            ' relation with')].replace('one', '1').replace('many', '*') + ' ] '
        intoFile(export)

       # print ("identify relationship")



def countObject(self):

        blurred = cv2.pyrMeanShiftFiltering(img, 71, 111)
        gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
        ret, threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        _, contours1, _ = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

        print ("number of shape detected {0} ".format(len(contours1)))
        cv2.drawContours(img, contours1, 2, (0, 0, 255), 6)
        return contours1





def drawcontours(self):
        img = cv2.imread("shapes.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, contours2, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours2:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            img = cv2.drawContours(img, [box],0 ,(0, 255, 0), 3)
            cv2.imshow('imagetest', img)





def intoFile(export):
    with open("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\ER.txt", "a") as myfile:
        myfile.write(export + "\n")

    print("nkfnjknhkdnfgkjndfgnd")



for x in split:
    processTable(x)


name = raw_input("PLZ Enter ?")
type(name)
