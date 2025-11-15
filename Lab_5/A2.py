import re

s = str(input('Enter sentense: '))
sen = re.split(r'(?<=[.?!])\s+', s)
print(sen)
for sentences in sen:
    print(sentences)
print(f'Amount of sentences: {len(sen)}')
