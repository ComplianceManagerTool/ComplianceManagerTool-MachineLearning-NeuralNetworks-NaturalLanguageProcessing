from flask import Flask, request,render_template
from flask_restful import Resource, Api
from flask import jsonify
import PdfToText_WordArray as p1

app = Flask(__name__)

#@app.route('/')
#def home():
#    return render_template('home.html')


@app.route('/')
def getMatchedArray():
    matchedWords = []
    list1,list2 = p1.createWordArray("Glossary of banking terms _ American Banker1-merged.pdf", "California-Consumer-Privacy-Act1.pdf")
    matchedWords = p1.getMatchedWords(list1,list2)
    return str(matchedWords)

if __name__ == '__main__':
    app.run()