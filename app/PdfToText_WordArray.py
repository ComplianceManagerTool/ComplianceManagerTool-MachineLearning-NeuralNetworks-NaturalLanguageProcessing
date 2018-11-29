import pdftotext
import numpy
from sklearn.feature_extraction.text import CountVectorizer

vocab1 = {}

def createWordArray(file1,file2):
    # Load your PDF
    with open(file1, "rb") as f1:
        businessGlossaryPdf = pdftotext.PDF(f1)
    with open(file2, "rb") as f2:
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
    # A list of common english words which should not affect predictions
    stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone',
             'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount',
             'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around',
             'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before',
             'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both',
             'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de',
             'describe', 'detail', 'did', 'do', 'does', 'doing', 'don', 'done', 'down', 'due', 'during', 'each', 'eg',
             'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone',
             'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for',
             'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had',
             'has', 'hasnt', 'have', 'having', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed',
             'interest', 'into', 'is', 'it', 'its', 'itself', 'just', 'keep', 'last', 'latter', 'latterly', 'least', 'less',
             'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly',
             'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine',
             'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',
             'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
             'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed', 'seeming',
             'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 
             'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system',
             't', 'take', 'ten', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there',
             'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third', 'this',
             'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward',
             'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we',
             'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby',
             'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom',
             'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself',
             'yourselves']
    for i in range(len(arr01)):
            if(arr01[i]!=0 and arr02[i]!=0):
               MatchedDict = {}
               if (vocab1[i].isalpha()) and (vocab1[i] not in stopwords):
                   MatchedDict['Matchedword'] = vocab1[i]
                   MatchedDict['count in business glossary'] = arr01[i]
                   MatchedDict['count in regulatory doc'] = arr02[i]
               else:
                   continue
               result.append(MatchedDict)   
    return result   

#list1,list2 = createWordArray("file1.pdf", "file2.pdf")
#print(getMatchedWords(list1,list2))