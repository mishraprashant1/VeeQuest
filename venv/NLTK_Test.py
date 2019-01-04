from nltk import *
from nltk.corpus import stopwords
import Ratings as rate
import WordList as wordlist
import DatabaseConnection as db
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
    #print("After sentence Tokenization : ", sentences)
    sentences=[word_tokenize(sent) for sent in sentences]
    #print("After word Tokenization : ", sentences)
    sentences=[pos_tag(sent) for sent in sentences]
    #print("After POS Tagging : ",sentences)
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
                    #print(words)
s1="The phone seems premium while holding. The camera quality is also fabulous. Excellent RAM management is a cherry on the cake. "
s2="User-Interface is also quite simple and easy to understand with ColourOS built-in. But the battery is poor and not up to the mark!"
s3="camera-quality is bad. battery is poor. processor is also awesome and weak"
sentence=s1+s2+s3
data_=preProcess(sentence)
grammar = "Relation:{<NN.*><.*>*<JJ>}"
ratings={}
cp=RegexpParser(grammar)
for i in range(0,len(data_)):
    result=cp.parse(data_[i])
    #print(result)
    traverse(result)
rates=rate.rateReviews(ratings)
print(rates)
featureList=["processor","ram","camera","battery","screen_quality","launch_months","misc"]
global stars
stars=0
cursor=db.mydb.cursor()
values=[]
values.append(cursor.rowcount+1)
values.append("Realme U1")
for words in featureList:
    try:
        temp=rates[words]
        positive=temp[0]
        negative=temp[1]
        pos=(positive/(positive+negative))*2.5
        neg=(negative/(positive+negative))*2.5
        stars=pos+(2.5-neg)
        values.append(stars)
    except KeyError:
        values.append(0)
print(values)
"""query="insert into ratings values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values=tuple(values)
cursor.execute(query,values)
db.mydb.commit()"""
