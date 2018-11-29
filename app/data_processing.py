import re
import pdftotext
import numpy as np

def split_para(file):
    with open(file, "rb") as f1:
          regulatoryDocText = pdftotext.PDF(f1)
    regulatoryDocString = "\n\n".join(regulatoryDocText).lower()
    para = re.split('\n{2,}',regulatoryDocString)
    texts = []
    for p in range(len(para)):
        para[p] = re.sub('line\s*[0-9]*\s*', '',para[p])
        texts.append(para[p])
    return texts
        


  



