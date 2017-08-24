import string
from l2_mess import mess

res = ""
for char in mess:
    if char in string.ascii_lowercase:
        res+=char
print(res)

d = {}
for char in mess:
    d[char] = d.get(char, 0) +1
print(d)