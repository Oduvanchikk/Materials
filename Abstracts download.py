from Bio import Entrez
import codecs
import time
Entrez.email = input("Enter mail (Entrez requirement): ")
request = input("Enter a query to the PubMed database: ")
retmax = int(input("Enter the number of texts to be downloaded: "))
dirtory = input("Enter the directory where you want to save the files: ")
handle = Entrez.esearch(db="pubmed", term=request, retmax = retmax) ##retmax = "300"
record = Entrez.read(handle)
ids = record["IdList"]
texts = []
pmids = []
count = 0
for id in ids:
    count = count +1
    handle = Entrez.efetch(db='pubmed',
                               retmode='xml',
                               id=id)
    results = Entrez.read(handle)
    papers = results
    try:
        title = papers['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle']
        abstract = papers['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
        texts.append(title + '\n' + ' '.join(abstract))
        pmids.append(id)
    except:
          pass
    print (str(count) + " loaded out of " + str(len(ids)))

i=0
while i<len(texts):
    f = codecs.open(dirtory + '''\\''' + str(pmids[i]) + '.txt' , 'a', encoding = 'utf-8')
    f.write (texts[i])
    f.close()
    i=i+1