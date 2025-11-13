sentence = str(input('Enter a sentence: '))


while '(' in sentence and ')' in sentence:
    left=sentence.find('(')
    right=sentence.find(')',left)
    sentence=sentence.replace(sentence[left:right+1],'')


print(sentence)