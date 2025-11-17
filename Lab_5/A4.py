import string;
import re;

def read_protein_data (filename):

  proteins=[]
  file = open(filename, 'r',encoding='utf-8')

  for line in file:
     parts=line.strip().split('\t')
     protein_data= (
         parts[0].strip(),
         parts[1].strip(),
         parts[2].strip()
         )
     proteins.append(protein_data)
  return proteins

def decode(word):
    final_word=''
    for i in range(len(word)):
        if word[i].isdigit():
            final_word = final_word + word[i+1]*(int(word[i])-1)
        else:
            final_word=final_word+word[i]
    return final_word


