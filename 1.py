import string
original = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
 bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
 lmu ynnjw ml rfc spj. """

table = string.maketrans(
    
)

def trans(character="a"):
    res = character                         #if no match, return argument( ,(). )
    letters = string.ascii_lowercase
    for i in range(len(letters)):
        l = letters[i]
        if l == character:
            j = i+2
            if j >= len(letters):
                j -= len(letters)
            res = letters[j]
    return res

answer = ""
for char in original:
    answer += trans(char)
print (answer)