import codecs
import nltk

rule_1p2dir12 = ['activating', 'activates', 'activate', 'cofactors', 'cofactor', 'counteract',
                'counteracts', 'counteracting', 'decreased with', 'decrease with', 'decreases with',
                'down-regulate', 'down-regulates', 'down-regulating', 'downregulate', 'downregulates',
                'downregulating', 'by downregulating', 'by the downregulation of', 'by down-regulating',
                'by the down-regulation of', 'up-regulate', 'up-regulates', 'up-regulating', 'upregulate',
                'upregulates', 'upregulating', 'by upregulating', 'by the upregulation of', 'by up-regulating',
                'by the up-regulation of', 'regulate', 'regulates', 'regulating', 'by regulating',
                'by the regulation of', 'enhance', 'enhances', 'enhancing', 'enchanced', 'by enhancing',
                'increase', 'increases', 'induces', 'induce', 'induced', 'inducing', 'inhibiting', 'inhibits',
                'inhibit', 'inhibitor of', 'mediating', 'mediators of', 'mediator of', 'mediates', 'mediate',
                'modulates', 'modulate', 'modulating', 'protects', 'protect', 'protecting', 'suppress', 'suppresses',
                'suppressed', 'suppressing', 'triggers', 'trigger', 'mimic', 'mimics', 'mimicing', 'mimiced',
                'promote', 'promotes', 'promoted', 'promoting', 'target', 'targets', 'targteted', 'targteting',
                'regulator', 'mediator', 'repressor', 'inhibitor', 'activator', 'modulator']
rule_1p2dir21 = ['activated by', 'cofactors', 'cofactor', 'down-regulated by', 'down-regulation by',
                'downregulated by', 'downregulation by', 'up-regulated by', 'up-regulation by',
                'upregulated by', 'upregulation by', 'regulated by', 'regulation by', 'enchanced', 'induced', 'inhibited by',
                'is a substrate for', 'mediated by', 'mediation by', 'modulated by', 'modulation by', 'taret of',
                'targets of', 'target for', 'targets for', 'transactivation through', 'responce to', 'in responce to', 'mimiced',
                'promoted', 'targteted']
rule_1p2dirnm = ['attach', 'attaches', 'attachment ', 'attached', 'bind', 'bind to', 'binds',
                'binds to', 'interacts with', 'interact with', 'interacting with', 'interacted with',
                'associated with', 'associate', 'associates', 'associating']
rule_p12dir21 = ['activation of ', 'down-regulation of', 'downregulation of', 'up-regulation of', 'upregulation of',
                'regulation of', 'inhibition of ', 'mediation of', 'modulation of', 'reduction in']
rule_p12dirnm = ['attachment ', 'binding of', 'interaction of', 'interactions of', 'interactions was', 'interaction',
                'interactions', 'relationship between']
##rule_12pdir12 = ['cofactors', 'cofactor']
##rule_12pdir21 = ['cofactors', 'cofactor']
rule_12pdirnm = ['interaction', 'interactions']

dirtory = input('Enter working directory: ') + "\\"

fileR = codecs.open(dirtory + 'proteins CRF NER.txt', 'r', encoding = 'utf-8')
lines = fileR.readlines()
lines = lines[1:]

fileW = codecs.open(dirtory + 'protein-protein RE.txt', 'a', encoding = 'utf-8')
errors = []
count = 0
for line in lines:
    count = count+1
    print(count, '/', len(lines))
    try:
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        mid = line.split('\t')
        pmid = mid[0]
        sent = mid[1]
        sent_tokenize = mid[2]
        entities = []
        for elem in mid[3:]:
            entities.append(elem)
        if len(entities)<2:
            pass
        else:
            for elem in rule_1p2dir12:
                phrase = ' '.join(nltk.word_tokenize(elem))
                if phrase.lower() in sent_tokenize.lower():
                    splitted_sent = (sent_tokenize.lower()).split(phrase.lower())
                    part1 = splitted_sent[0]
                    part2 = splitted_sent[1]
                    entities1 = []
                    entities2 = []
                    for ent in entities:
                        if ent.lower() in part1:
                            entities1.append(ent)
                        if ent.lower() in part2:
                            entities2.append(ent)
                    if (entities1!=[]) and (entities2!=[]):
                        for ent1 in entities1:
                            for ent2 in entities2:
                                fileW.write(pmid + '\t' + sent + '\t' + ent1 + '\t' + ent2 + '\t' + '12' + '\t' + elem + '\n')
            for elem in rule_1p2dir21:
                phrase = ' '.join(nltk.word_tokenize(elem))
                if phrase.lower() in sent_tokenize.lower():
                    splitted_sent = (sent_tokenize.lower()).split(phrase.lower())
                    part1 = splitted_sent[0]
                    part2 = splitted_sent[1]
                    entities1 = []
                    entities2 = []
                    for ent in entities:
                        if ent.lower() in part1:
                            entities1.append(ent)
                        if ent.lower() in part2:
                            entities2.append(ent)
                    if (entities1!=[]) and (entities2!=[]):
                        for ent2 in entities2:
                            for ent1 in entities1:
                                fileW.write(pmid + '\t' + sent + '\t' + ent2 + '\t' + ent1 + '\t' + '21' + '\t' + elem + '\n')
            for elem in rule_1p2dirnm:
                phrase = ' '.join(nltk.word_tokenize(elem))
                if phrase.lower() in sent_tokenize.lower():
                    splitted_sent = (sent_tokenize.lower()).split(phrase.lower())
                    part1 = splitted_sent[0]
                    part2 = splitted_sent[1]
                    entities1 = []
                    entities2 = []
                    for ent in entities:
                        if ent.lower() in part1:
                            entities1.append(ent)
                        if ent.lower() in part2:
                            entities2.append(ent)
                    if (entities1!=[]) and (entities2!=[]):
                        for ent1 in entities1:
                            for ent2 in entities2:
                                fileW.write(pmid + '\t' + sent + '\t' + ent1 + '\t' + ent2 + '\t' + 'nm' + '\t' + elem + '\n')
            for elem in rule_p12dir21:
                phrase = ' '.join(nltk.word_tokenize(elem))
                if phrase.lower() in sent_tokenize.lower():
                    splitted_sent = (sent_tokenize.lower()).split(phrase.lower())
                    part1 = splitted_sent[0]
                    part2 = splitted_sent[1]
                    entities1 = []
                    entities2 = []
                    for ent in entities:
                        if ent.lower() in part2:
                            entities2.append(ent)
                    if (entities2!=[]) and (len(entities2)>1):
                        for ent2 in entities2[:-1]:
                            fileW.write(pmid + '\t' + sent + '\t' + ent2 + '\t' + entities[-1] + '\t' + '21' + '\t' + elem + '\n')
            for elem in rule_p12dirnm:
                phrase = ' '.join(nltk.word_tokenize(elem))
                if phrase.lower() in sent_tokenize.lower():
                    splitted_sent = (sent_tokenize.lower()).split(phrase.lower())
                    part1 = splitted_sent[0]
                    part2 = splitted_sent[1]
                    entities1 = []
                    entities2 = []
                    for ent in entities:
                        if ent.lower() in part2:
                            entities2.append(ent)
                    if (entities2!=[]) and (len(entities2)>1):
                        i=0
                        while i<len(entities2):
                            j=i+1
                            while j<len(entities2):
                                fileW.write(pmid + '\t' + sent + '\t' + entities2[i] + '\t' + entities2[j] + '\t' + 'nm' + '\t' + elem + '\n')
                                j=j+1
                            i=i+1
            for elem in rule_12pdirnm:
                phrase = ' '.join(nltk.word_tokenize(elem))
                if phrase.lower() in sent_tokenize.lower():
                    splitted_sent = (sent_tokenize.lower()).split(phrase.lower())
                    part1 = splitted_sent[0]
                    part2 = splitted_sent[1]
                    entities1 = []
                    for ent in entities:
                        if ent.lower() in part1:
                            entities1.append(ent)
                    if (entities1!=[]) and (len(entities1)>1):
                        fileW.write(pmid + '\t' + sent + '\t' + entities1[-2] + '\t' + entities1[-1] + '\t' + 'nm' + '\t' + elem + '\n')
    except:
        errors.append(line)
fileW.close()
print(len(errors), errors)