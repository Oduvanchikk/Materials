import codecs
import glob
import nltk

dirtory = input("Enter working diretory: ") + "\\"
folder = input("Enter the name of folder where texts for the recognition are stored: ")

def collect(fr):
    count = 1
    info = []
    files = glob.glob(dirtory + folder + "\\*.txt")
    for file in files:
        print(count, '/', len(files))
        count = count+1
        mid_info = []
        start = file.find(fr)
        pmid = file[start+len(fr)+1:-4]
        f = codecs.open(file, 'r', encoding = 'utf-8')
        lines = f.readlines()
        f.close()
        sentences = nltk.sent_tokenize(' '.join(lines[:-1]))
        for sent in sentences:
            i=0
            while i<len(entities):
                j=0
                while j<len(entities[i]):
                    flag = 1
                    for s in entities[i][j]:
                        if s.isupper():
                            pass
                        else:
                            flag = 0
                            break
                    if flag == 0:
                        if entities[i][j] in sent.lower():
                            mid_info.append([pmid, sent, doids[i], entities[i][j]])
                    else:
                        if entities[i][j] in sent:
                            mid_info.append([pmid, sent, doids[i], entities[i][j]])
                    j=j+1
                i=i+1
        info.append(mid_info)
    return info


file = codecs.open(dirtory + 'DOID_filtered_ext.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
lines = lines[1:]
file.close()
doids = []
entities = []
for line in lines:
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    mid = line.split('\t')
    doids.append(mid[0])
    mid_ent = []
    if mid[1]!='':
        flag = 1
        for s in mid[1]:
            if s.isupper():
                pass
            else:
                flag = 0
                break
        if flag==0:
            mid_ent.append(mid[1].lower())
        else:
            mid_ent.append(mid[1])
    syn = mid[2].split('; ')
    for elem in syn:
        if elem!='':
            flag = 1
            for s in elem:
                if s.isupper():
                    pass
                else:
                    flag = 0
                    break
            if flag==0:
                mid_ent.append(elem.lower())
            else:
                mid_ent.append(elem)
    entities.append(mid_ent)

info_hh = collect(folder)
filew = codecs.open(dirtory + 'neoplastic-diseases-NER.txt', 'a', encoding = 'utf-8')
i=0
for elem in info_hh:
    for e in elem:
        filew.write('\t'.join(e) + '\n')
filew.close()



