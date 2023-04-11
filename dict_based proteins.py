import codecs
import nltk
import glob

dirtory = input('Enter working directory: ') + "\\"
folder = input('Enter the name of folder where texts for the recognition are stored: ')

def collect(fr, f_ent):
    file = codecs.open(dirtory+f_ent, 'r', encoding = 'utf-8')
    lines = file.readlines()
    file.close()
    e_info = []
    ents = []
    for line in lines:
        line = line.replace('\r', '')
        line = line.replace('\n', '')
        mid = line.split('\t')
        e_info.append([mid[0], mid[1]])
        all = (mid[2].lower()).split('; ') + (mid[3].lower()).split('; ') + (mid[4].lower()).split('; ')
        a = []
        for e in all:
            if e not in ['', ' ']:
                a.append(e)
        ents.append(a)
    files = glob.glob(dirtory+folder+"\\*.txt")
    info = []
    count = 1
    for file in files:
        print(count, '/', len(files))
        count+=1
        mid_info = []
        f = codecs.open(file, 'r', encoding = 'utf-8')
        start = file.find(folder)
        pmid = file[start+len(folder)+1:-4]
        lines = f.readlines()
        sentences = nltk.sent_tokenize(' '.join(lines[:-1]))
        for sent in sentences:
            i=0
            while i<len(ents):
                j=0
                while j<len(ents[i]):
                    if ents[i][j] in sent.lower():
                        mid_info.append([pmid, sent, ents[i][j], e_info[i][0], e_info[i][1]])
                    j=j+1
                i=i+1
        info.append(mid_info)
    return info
excep = ['Hedgehog', 'Hh', 'Wingless', 'Vertebrate Hedgehog', 'chicken snail', 'Sonic Hedgehog', 'Transcriptional co', 'NH2', 'para', 'halo', 'beta', 'anti', 'Cov', 'SARS', 'alpha', 'Gli', 'zinc finger']
i=0
while i<len(excep):
    excep[i] = excep[i].lower()
    i=i+1
hh_info = collect(folder, 'HH proteins info.txt')
filew = codecs.open(dirtory+'HH_proteins_dict_NER.txt', 'a', encoding = 'utf-8')
for elem in hh_info:
    for e in elem:
        if e[2] not in excep:
            filew.write('\t'.join(e) + '\n')
filew.close()
