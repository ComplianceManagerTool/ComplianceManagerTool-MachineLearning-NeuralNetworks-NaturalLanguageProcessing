import pdftotext
import numpy
from sklearn.feature_extraction.text import CountVectorizer

# Load your PDF
with open("/home/akansha/Documents/295B/Glossary of banking terms _ American Banker.pdf", "rb") as f1:
    businessGlossaryPdf = pdftotext.PDF(f1)
with open("/home/akansha/Documents/295B/ISO_IEC_27001.pdf", "rb") as f2:
    regulatoryDocPdf = pdftotext.PDF(f2)
# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(businessGlossaryPdf))
print(len(regulatoryDocPdf))

# Iterate over all the pages
#for page in pdf:
#    print(page)

# Read some individual pages
#print(pdf[0])
#print(pdf[1])

# Read all the text into one string
businessGlossaryString = "\n\n".join(businessGlossaryPdf) 
regulatoryDocString = "\n\n".join(regulatoryDocPdf)
#print(regulatoryDocString) 
#print(businessGlossaryString);
text1 = [businessGlossaryString]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text1)
# summarize
print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform(text1)
# summarize enocoded vector
print(vector.shape)
print(type(vector))
#print(vector.toarray())
arr1 = vector.toarray()
#################################
# enclode another document
text2 = [regulatoryDocString]
vector = vectorizer.transform(text2)
arr2 = vector.toarray()
#print(arr)
print("======================================================")
#nump.arange(100).reshape(25,4).tolist()
a = numpy.array(arr1)
b = numpy.array(arr2)
numpy.set_printoptions(threshold=numpy.nan)
print(a)
print("======================================================")
print(b)
#numpy.reshape(a,1357).tolist()
