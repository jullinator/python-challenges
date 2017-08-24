import string
import re
f = open('l3_data.txt','r')
data = f.read()


#regex

res = "".join(re.findall("[^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+", data))
print(res)

#sloppy
upper = string.ascii_uppercase
lower = string.ascii_lowercase

def sloppy ():

    for i in range(len(data)-9):
        truth = True
        temp = ""
        for j in range(9):
            c = data[i + j]
            if j in [0,4,8]:
                if not c in lower:
                    truth = False
            else:
                if not c in upper:
                    truth = False

            temp+= c

        if truth:
            print(temp)
            pass