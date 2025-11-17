file_commands = 'commands.0.txt'
file_proteins = 'sequences.0.txt'

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
        if protein in (proteins[i])[2]:
            answer_search = (proteins[i])[1]+ '   ' + (proteins[i])[0]
            return answer_search
            
    if answer_search == '':
        return 'NOT FOUND'

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
        if letters[i]==max_num:
            answer_letter=i
            break
    return answer_letter,max_num

def diff(protein1, protein2):
    proteins = read_protein_data (file_proteins)
    f_protein1=''
    f_protein2=''
    for i in range(len(proteins)):
            if (proteins[i])[0]==protein1:
                f_protein1 = (proteins[i])[2]
    if f_protein1=='':
        return 'MISSING'

    for i in range(len(proteins)):
            if (proteins[i])[0]==protein2:
                f_protein2 = (proteins[i])[2]
    if f_protein2=='':
        return 'MISSING'

    if len(f_protein1)>len(f_protein2):
        max_protein = f_protein1
        min_protein = f_protein2
    else:
        max_protein=f_protein2
        min_protein = f_protein1

    answer_diff = (len(max_protein)-len(min_protein))

    for i in range(len(min_protein)):
        if min_protein[i] != max_protein[i]:
            answer_diff = answer_diff + 1

    return answer_diff

file = open('genedata0.txt','w')
file.write('Matveuk Antonina\n')
file.write('Genetic Searching\n')
file.write('--------------------------------------------------------------------------\n')
commands = read_commands_data(file_commands)
count = 1
for i in range(len(commands)):
    if (commands[i])[0] == 'search':
        file.write('00'+str(count)+'   ')
        file.write((commands[i])[0]+'   '+ decode((commands[i])[1])+'\n')
        file.write('organism'+'                     '+'protein\n')
        file.write(search((commands[i])[1])+'\n')
        file.write('--------------------------------------------------------------------------\n')
        count = count+1


    if (commands[i])[0] == 'mode':
        file.write('00'+str(count)+'   ')
        file.write((commands[i])[0]+'   '+ decode((commands[i])[1])+'\n')
        file.write('amino-acid occurs:\n')
        file.write(str((mode((commands[i])[1]))[0])+'       '+str((mode((commands[i])[1]))[1])+'\n')
        file.write('--------------------------------------------------------------------------\n')
        count = count+1



    if (commands[i])[0] == 'diff':
        file.write('00'+str(count)+'   ')
        file.write((commands[i])[0]+'   '+ (commands[i])[1]+'   '+ (commands[i])[2]+'\n')
        file.write('amino-acids difference: \n')
        file.write(str(diff((commands[i])[1],(commands[i])[2]))+'\n')
        file.write('--------------------------------------------------------------------------\n')
        count = count+1









