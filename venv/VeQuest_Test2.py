"""from numpy import *
reviews=random.randint(low=1,high=10,size=(6,10))
print(reviews)
mean_val=zeros(shape=(6,1))
for i in range(reviews.shape[0]):
    idx=[0,1,2,3,4,5,6,7,8,9]
    mean_val[i]=mean(reviews[i,idx])
    reviews[i,idx]=reviews[i,idx]-mean_val[i]
print(reviews)
print(mean_val)
f=open("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\positive-words.txt","r")
wordslist=[];
for word in f:
    wordslist.append(word[0:int(len(word)-1)])
temp=input("Get word")
if temp in wordslist:
    print("In the set")
else:
    print("Not in the set")
def tempfunction(text):
    print (text)
tempfunction("Somethign printed")
te={"rating":1,"is":2,"given":3}
for wrods in te:
    print(te[wrods])"""
"""import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="VeQuest")
query="insert into TemporaryTable values(%s,%s)"
values=(10,20)
cursor=mydb.cursor()
cursor.execute(query,values)
mydb.commit()"""
import json
file=open("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\ScrapedPages\\FlipkartRatings\\Page.json", "r")
data=json.load(file)
print(data["Display"])


