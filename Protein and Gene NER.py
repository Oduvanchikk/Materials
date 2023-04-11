import nltk
import sklearn_crfsuite
from sklearn_crfsuite import metrics
import glob
import codecs
import joblib
dirtory = input("Enter working directory: ") + '\\'
folder = input("Enter the name of the folder where abstract texts are stored: ") + "\\"
labels = ['S', 'O', 'B', 'I', 'E']
fileNS= open (dirtory + 'Non-specific (proteins).txt', 'r')
linesNS=fileNS.readlines()
non_specifics=[]
for elem in linesNS:
    non_specifics.append(elem[:-1])
file_SW = open (dirtory + 'English-Stopwords.txt', 'r')
linesSW=file_SW.readlines()
SW=[]
for word in linesSW:
    SW.append(word[:-1])
symbols = ['.', ',', '/', '<', '>', '"', '!', '?', '(', ')', '+', '-', ':', ';', '±', '[', ']', '{', '}', '%', '=', '&', "'"]
files_pred=glob.glob(dirtory + folder + '*.txt')
X_test=[]
pmids=[]
pmids_sent = []
sents = []
sents_token = []
l=0
while l<len(files_pred):
    start = files_pred[l].find(folder)
    pmids.append(files_pred[l][start+len(folder)+1:-4])
    try:
        file=codecs.open(files_pred[l], 'r', encoding='utf-8')
        lines=file.readlines()
    except:
        file=open(files_pred[l])
        lines=file.readlines()
    all_text = ' '.join(lines)
    all_text = all_text.replace('<sup>', '')
    all_text = all_text.replace('</sup>', '')
    all_text = all_text.replace('<sub>', '')
    all_text = all_text.replace('</sub>', '')
    all_text = all_text.replace('<i>', '')
    all_text = all_text.replace('</i>', '')
    sentences = nltk.sent_tokenize(all_text)
    print (str(l) + " from " + str (len (files_pred)))
    i=0
    while i<len(sentences):
        fromDB=nltk.wordpunct_tokenize(sentences[i])
        wordsFile=[]
        m=0
        while m<len(fromDB):
            word_true=fromDB[m]
            if word_true.lower() in non_specifics:
                NS_param=1
            else:
                NS_param=0
            if word_true.lower() in SW:
                SW_param=1
            else:
                SW_param=0
            for elem in word_true:
                if elem in symbols:
                    sym_param=1
                    break
                else:
                    sym_param=0
            for elem in word_true:
                if elem.isdigit():
                    digit_param=1
                    break
                else:
                    digit_param=0
            pos = nltk.pos_tag([word_true])[0][1]
            features = {
            'word':word_true.encode('utf-8').decode('ascii', errors = 'ignore'),
            'word.lower()': (word_true.lower()).encode('utf-8').decode('ascii', errors = 'ignore'),
            'word.isupper()': word_true.isupper(),
            'word.istitle()': word_true.istitle(),
            'word.isdigit()': word_true.isdigit(),
            'word.havedigits()':digit_param,
            'word.isNonSpecific': NS_param,
            'word.isStopWord': SW_param,
            'word.isSymbol': sym_param,
            'word[-3:]': word_true.encode('utf-8').decode('ascii', errors = 'ignore')[len(word_true)-3:len(word_true)],
            'word[-2:]': word_true.encode('utf-8').decode('ascii', errors = 'ignore')[len(word_true)-2:len(word_true)],
            'word.FirstSymbol': word_true[0].encode('utf-8').decode('ascii', errors = 'ignore'),
            'word.CharNumber': len(word_true),
            'postag': pos,
            'postag[:2]': pos[:2]
                }
            if m>0:
                word_true=fromDB[m-1]
                if word_true.lower() in non_specifics:
                    NS_param=1
                else:
                    NS_param=0
                if word_true.lower() in SW:
                    SW_param=1
                else:
                    SW_param=0
                for elem in word_true:
                    if elem in symbols:
                        sym_param=1
                        break
                    else:
                        sym_param=0
                for elem in word_true:
                    if elem.isdigit():
                        digit_param=1
                        break
                    else:
                        digit_param=0
                pos = nltk.pos_tag([word_true])[0][1]
                features.update({
                '-1:word':word_true.encode('utf-8').decode('ascii', errors = 'ignore'),
                '-1:word.lower()': (word_true.lower()).encode('utf-8').decode('ascii', errors = 'ignore'),
                '-1:word.isupper()': word_true.isupper(),
                '-1:word.istitle()': word_true.istitle(),
                '-1:word.isdigit()': word_true.isdigit(),
                '-1:word.havedigits()':digit_param,
                '-1:word.isNonSpecific': NS_param,
                '-1:word.isStopWord': SW_param,
                '-1:word.isSymbol': sym_param,
                '-1:word[-3:]': word_true.encode('utf-8').decode('ascii', errors = 'ignore')[len(word_true)-3:len(word_true)],
                '-1:word[-2:]': word_true.encode('utf-8').decode('ascii', errors = 'ignore')[len(word_true)-2:len(word_true)],
                '-1:word.FirstSymbol': word_true[0].encode('utf-8').decode('ascii', errors = 'ignore'),
                '-1:word.CharNumber': len(word_true),
                '-1:postag': pos,
                '-1:postag[:2]': pos[:2]
                })
            if m<len (fromDB)-1:
                word_true=fromDB[m+1]
                if word_true.lower() in non_specifics:
                    NS_param=1
                else:
                    NS_param=0
                if word_true.lower() in SW:
                    SW_param=1
                else:
                    SW_param=0
                for elem in word_true:
                    if elem in symbols:
                        sym_param=1
                        break
                    else:
                        sym_param=0
                for elem in word_true:
                    if elem.isdigit():
                        digit_param=1
                        break
                    else:
                        digit_param=0
                pos = nltk.pos_tag([word_true])[0][1]
                features.update({
                '+1:word':word_true.encode('utf-8').decode('ascii', errors = 'ignore'),
                '+1:word.lower()': (word_true.lower()).encode('utf-8').decode('ascii', errors = 'ignore'),
                '+1:word.isupper()': word_true.isupper(),
                '+1:word.istitle()': word_true.istitle(),
                '+1:word.isdigit()': word_true.isdigit(),
                '+1:word.havedigits()':digit_param,
                '+1:word.isNonSpecific': NS_param,
                '+1:word.isStopWord': SW_param,
                '+1:word.isSymbol': sym_param,
                '+1:word[-3:]': word_true.encode('utf-8').decode('ascii', errors = 'ignore')[len(word_true)-3:len(word_true)],
                '+1:word[-2:]': word_true.encode('utf-8').decode('ascii', errors = 'ignore')[len(word_true)-2:len(word_true)],
                '+1:word.FirstSymbol': word_true[0].encode('utf-8').decode('ascii', errors = 'ignore'),
                '+1:word.CharNumber': len(word_true),
                '+1:postag': pos,
                '+1:postag[:2]': pos[:2]
                })
            wordsFile.append(features)
            m=m+1
        X_test.append(wordsFile)
        pmids_sent.append(files_pred[l][start+len(folder)+1:-4])
        sents.append(sentences[i])
        sents_token.append(' '.join(fromDB))
        i=i+1
    l=l+1
crf = joblib.load(dirtory+"pred_proteins.pkl")
y_pred = crf.predict(X_test)

fileW = codecs.open(dirtory+'proteins CRF NER.txt', 'a', encoding='utf-8')
fileW.write('PMID\tSentence\tTokenized_sentence\tProtein_and_gene_NEs\n')
i=0
while i<len(pmids_sent):
    if ('S' not in y_pred[i]) and ('B' not in y_pred[i]):
        pass
    else:
        entities = []
        j=0
        while j<len(y_pred[i]):
            if y_pred[i][j] == 'S':
                entities.append(X_test[i][j]['word'])
            if y_pred[i][j]=='B':
                ent = [X_test[i][j]['word']]
            if y_pred[i][j]=='I':
                ent = ent + [X_test[i][j]['word']]
            if y_pred[i][j]=='E':
                ent = ent + [X_test[i][j]['word']]
                entities.append(' '.join(ent))
            j=j+1
        fileW.write(pmids_sent[i] + '\t' + sents[i] + '\t' + sents_token[i] + '\t' + '\t'.join(entities) + '\n')
    i=i+1
fileW.close()
