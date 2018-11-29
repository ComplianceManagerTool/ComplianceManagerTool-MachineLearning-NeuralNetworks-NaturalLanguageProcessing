import re
import pdftotext
import numpy as np


with open("/home/akansha/Documents/295B/ComplianceManagerTool-MachineLearning-NeuralNetworks-NaturalLanguageProcessing/app/" + "file2.pdf", "rb") as f1:
        regulatoryDocText = pdftotext.PDF(f1)
regulatoryDocString = "\n\n".join(regulatoryDocText).lower()

para = re.split('\n{2,}',regulatoryDocString)
texts = []
for p in range(len(para)):
    #print("-------------------------------")
    para[p] = re.sub('line\s*[0-9]*\s*', '',para[p])
    texts.append(para[p])
    #print("-------------------------------")


  



