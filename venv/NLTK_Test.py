from nltk import *
from nltk.corpus import stopwords
import Ratings as rate
import WordList as wordlist
import DatabaseConnection as db
import getreview as amazon
import GetBlogs as blogs
import json
import GetRatings as getrating
import time
import SpiderCalls

def preProcess(document):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(document)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    global sentence
    sentences=""
    for w in word_tokens:
        if w not in stop_words:
            sentences=sentences+" "+w
    sentences=sent_tokenize(sentences)
    sentences=[word_tokenize(sent) for sent in sentences]
    sentences=[pos_tag(sent) for sent in sentences]
    return sentences

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=" ")
    else:
        for child in t:
            if type(child)==tree.Tree:
                global noun
                noun=""
                for words in child:
                    if words[1]=="NN":
                        temp=wordlist.getNoun(words[0])
                        if temp!="":
                            noun=temp
                        elif noun=="":
                            noun="misc"
                    elif words[1]=="JJ":
                        if noun in ratings:
                            temp=ratings[noun]
                            temp.append(words[0])
                            ratings[noun]=temp
                        else:
                            ratings[noun]=([words[0]])

"""phoneName=input("Name of the Phone : ")
def getPhoneName():
    return phoneName"""
SpiderCalls.callSpiders()
data_=[]
review=amazon.ReadAsin()
listrev=[]
sentence=""
for i in range(0,len(review[0]["reviews"])):
    sentence=sentence+review[0]["reviews"][i]["review_text"]
sentence=sentence+blogs.getBlogs()
data_=preProcess(sentence)
grammar = "Relation:{<NN.*><.*>*<JJ>}"
#grammar = "Relation:{<JJ.*><.*>*<NN.*>}"
ratings={}
cp=RegexpParser(grammar)
for i in range(0,len(data_)):
    result=cp.parse(data_[i])
    traverse(result)
rates=rate.rateReviews(ratings)
print(rates)
featureList=["processor","ram","camera","battery","screen_quality","launch_months","misc"]
global stars
stars=0
values=[]
cursor=db.mydb.cursor()
values.append(cursor.rowcount+1)
values.append("Realme U1")
for words in featureList:
    try:
        temp=rates[words]
        positive=temp[0]
        negative=temp[1]
        pos=((positive)/(positive+negative))*2.5
        neg=((negative)/(positive+negative))*2.5
        stars=pos+(2.5-neg)
        values.append(stars)
    except KeyError:
        values.append(0)
print(values)

#
#FLIPKART RATINGS CODE HERE
#
time.sleep(5)
fliprating = getrating.getRatings()
print(fliprating)

"""query="insert into ratings values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values=tuple(values)
cursor.execute(query,values)
db.mydb.commit()"""
