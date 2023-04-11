import codecs
import urllib.request
import os
import pathlib
import urllib.request as ull
dirtory = input("Enter working directory: ") + '\\'
file = codecs.open(dirtory + 'HH proteins info.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
hh = []
for line in lines:
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    line = line.lower()
    mid = line.split('\t')
    prot = (mid[2].split('; '))
    dom = mid[3].split('; ')
    gene = mid[4].split('; ')
    all = prot + dom + gene
    hh.append(all)

file = codecs.open(dirotry + 'protein-protein RE.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
file = codecs.open(dirtory + 'protein-protein RE UniProt.txt', 'a', encoding='utf-8')
count = 1
print(len(lines))
for line in lines:
    print(str(count) + ' out of ' + str(len(lines)))
    count = count+1
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    feat = line.split('\t')
    for elem in hh:
        if feat[2].lower() in elem:
            proteins = [elem[0], feat[3]]
            break
        if feat[3].lower() in elem:
            proteins = [feat[2], elem[0]]
            break
    file.write(feat[0] + '\t' + feat[1] + '\t')
    for p in proteins:
        ts = p.replace(" ", "+")
        ts = ts.replace('/', '+')
        ts = ts.replace('-', '+')
        ts = ts.replace('++', '+')
        try:
            ull.urlretrieve('https://rest.uniprot.org/uniprotkb/search?query=' + ts + '+AND+reviewed:true+AND+(organism_id:9606)&fields=accession,id,protein_name,organism_name,gene_names,go&format=tsv',
                            dirtory + ts + ".tsv")
            f = codecs.open(dirtory+ts+'.tsv', 'r', encoding = 'utf-8')
            l = f.readlines()
            mid = l[1].split('\t')
            f.close()
            end = mid[2].find("(")
            mid[5] = mid[5].replace('\n','')
            file.write(p + '\t' +  mid[0] + '\t' + mid[1] + '\t' + mid[2][:end] + '\t' + mid[4] + '\t' + mid[5] + '\t')
            os.remove(dirtory+ts + '.tsv')
        except:
            file.write(p + '\t' + '\t'.join(['-']*5) + '\t')
            print ("IOError", ts)
    file.write(feat[4] + '\n')
file.close()