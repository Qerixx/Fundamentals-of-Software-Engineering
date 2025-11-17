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
  
def search(protein):
    answer_search=''
    protein=decode(protein)
    proteins = read_protein_data (file_proteins)
    for i in range(len(proteins)):
        if (proteins[i])[2].find(protein):
            answer_search = (proteins[i])[1]+ '   ' +(proteins[i])[2]
    if answer_search == '':
        return 'NOT FOUND'
    else:
        return answer_search

def mode(protein):
    proteins = read_protein_data (file_proteins)
    f_protein=''
    for i in range(len(proteins)):
            if (proteins[i])[0]==protein:
                f_protein = (proteins[i])[2]
    if f_protein=='':
        return 'MISSING'

    letters=dict()
    for i in f_protein:
        letters[i]=letters.get(i,0)+1

    answer_letter = max(letters,key=letters.get)
    max_num= letters[answer_letter]
    for i in sorted(letters):
        print(i)
        if letters[i]==max_num:
            answer_letter=i
            break
    return answer_letter,max_num




