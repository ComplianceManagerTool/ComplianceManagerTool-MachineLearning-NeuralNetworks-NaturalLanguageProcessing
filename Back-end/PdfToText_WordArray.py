import pdftotext
import numpy
from sklearn.feature_extraction.text import CountVectorizer

vocab1 = {}

def createWordArray(file1,file2):
    # Load your PDF
    with open("/home/akansha/Documents/295B/" + file1, "rb") as f1:
        businessGlossaryPdf = pdftotext.PDF(f1)
    with open("/home/akansha/Documents/295B/" + file2, "rb") as f2:
        regulatoryDocPdf = pdftotext.PDF(f2)
    # Read all the text into one string
    businessGlossaryString = "".join(businessGlossaryPdf).lower() 
    regulatoryDocString = "\n\n".join(regulatoryDocPdf).lower()
    text1 = [businessGlossaryString]
    # create the transform
    vectorizer = CountVectorizer()
    # tokenize and build vocab
    vectorizer.fit(text1)
    # summarize
    #print(vectorizer.vocabulary_)
    vocab = vectorizer.vocabulary_
    # encode document
    vector = vectorizer.transform(text1)
    # summarize enocoded vector

    arr1 = vector.toarray()
    businessGlossaryList = numpy.array(arr1)
    # enclode another document
    text2 = [regulatoryDocString]
    vector = vectorizer.transform(text2)
    arr2 = vector.toarray()
    regulatoryDocList = numpy.array(arr2)
    numpy.set_printoptions(threshold=numpy.nan)
    for name,count in vocab.items():
        vocab1[count] = name

    businessGlossaryNewList = []
    regulatoryDocNewList = []
    for item in businessGlossaryList:
        for i in item:
            businessGlossaryNewList.append(i)

    for item in regulatoryDocList:
        for i in item:
            regulatoryDocNewList.append(i)
    
    return businessGlossaryNewList,regulatoryDocNewList
    

def word_count(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count



def getMatchedWords(arr01,arr02):
    result = []
    for i in range(len(arr01)):
            if(arr01[i]!=0 and arr02[i]!=0):
               MatchedDict = {}
               MatchedDict['Matchedword'] = vocab1[i]
               MatchedDict['count in business glossary'] = arr01[i]
               MatchedDict['count in regulatory doc'] = arr02[i]
               result.append(MatchedDict)   
    return result   

#list1,list2 = createWordArray("Glossary of banking terms _ American Banker1-merged.pdf", "California-Consumer-Privacy-Act1.pdf")
#print(getMatchedWords(list1,list2))