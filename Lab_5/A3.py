import re
import string

text = str(input())
words = text.split()

i=0

for word in words:
    if len(word)<3:
        del words[i]
    i=i+1

final = ''

for word in words:
    final = final + word[0]

print(final)

