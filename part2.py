import nltk
from nltk import RegexpParser
from nltk.tree import Tree

def is_actionable(tagged_sent):

        if tagged_sent[-1][0] == "?":
            return False
        
        #Sentence starts with verb or modal
        if tagged_sent[0][1] == "VB":# or tagged_sent[0][1] == "MD":
            return True

        #sentence with first chuck as verb phrase
        else:
            chunk = extract_verbphrase(tagged_sent)
            if type(chunk[0]) is Tree and chunk[0].label() == "VB-Phrase":
                return True

        #sentence containing plaese keyword
        pleasekey = len([w for w in tagged_sent if w[0].lower() == "please"]) > 0
        if pleasekey: # and (tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD"):
            return True

        return False

#verb phrase chunk possibilities
def extract_verbphrase(tagged_sent):
    chunkgram = r"""VB-Phrase: {<UH><,>*<VB>}
                    VB-Phrase: {<UH><,><VBP>}
                    VB-Phrase: {<PRP><VB>}
                    VB-Phrase: {<NN.?>+<,>*<VB>}
                    VB-Phrase: {<DT><,>*<VB>}
                    VB-Phrase: {<RB><VB>}
                    Q-Tag: {<,><MD><RB>*<PRP><.>*}"""
    vbchunkparser = RegexpParser(chunkgram)
    return vbchunkparser.parse(tagged_sent)


#positive sentence count
i =0
#negative sentence count
j =0

filenameTrue = open("C:/Users/Nikhil/Desktop/actionItemDetection/finaloutputTrue.txt","w")
filenameFalse = open("C:/Users/Nikhil/Desktop/actionItemDetection/finaloutputFalse.txt","w")
with open("C:/Users/Nikhil/Desktop/actionItemDetection/emailDataFilter.txt") as f:
    for line in f:
        if(i> 50000 and j>50000):
            break;
        tokens = nltk.word_tokenize(line)
        taggedtokens =  nltk.pos_tag(tokens)
        value = is_actionable(taggedtokens)
        if(value):
            if(i>50000):
                continue
            filenameTrue.write(line)
            print(i)
            i+=1
        else:
            if(j>50000):
                continue
            filenameFalse.write(line)  
            print(j)
            j+=1
print(i,j)
filenameTrue.close()
filenameFalse.close()