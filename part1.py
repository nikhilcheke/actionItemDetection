import pandas as pd
import re
from nltk.tokenize import sent_tokenize
"""
filename = "C:/Users/Nikhil/Desktop/actionItemDetection/enron-email-dataset/emails.csv"
messagefile = open("C:/Users/Nikhil/Desktop/actionItemDetection/emailData.txt","w")

#taken message data only
maildata = pd.read_csv(filename, usecols = ["message"])
data = list(maildata["message"])

#filter mail details to take out mail content only
#Split mail content into sentences using nltk sentence tokenizer
total = 0
for row in range(len(data)) :
    messagedata = str(data[row])
    messagedata = re.split("X-FileName:"+r".*"+"\n",messagedata)
    msgSentences = sent_tokenize(messagedata[1])
    for i in msgSentences:
        #print(i.replace('\n','')+"\n")
        i = i.replace('\n','')+"\n"
        messagefile.write(i)
        total = total + 1
        print(total)
        
messagefile.close()
"""
filterfile = open("C:/Users/Nikhil/Desktop/actionItemDetection/emailDataFilter.txt","w")
totalSentCount = 0
filterSentCount = 0
with open("C:/Users/Nikhil/Desktop/actionItemDetection/emailData.txt") as f:
    for line in f:
        totalSentCount = totalSentCount + 1
        if "www" in line:
            continue
        if "~~~" in  line:
            continue
        if len(line.split()) > 25:
            continue
        if "\t" in line:
            continue
        if "--" in line:
            continue
        if len(line.split()) < 3:
            continue
        if "http:" in line:
            continue
        if "[IMAGE]" in line:
            continue
        if ">>" in line:
            continue
        if "**" in line:
            continue
        if "=" in line:
            continue
       
        
        """
        if "www" or  "~~~" or "\t" or "--" or "http:" or "[IMAGE]" or ">>" or "**" or "=" in line:
            continue
        if len(line.split()) > 25 or len(line.split()) < 3:
            continue"""
       
        filterSentCount = filterSentCount + 1
        filterfile.write(line)
        print(totalSentCount,filterSentCount)
       
filterfile.close()
print(totalSentCount,filterSentCount)

