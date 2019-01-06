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
internal="64 GB, 4/6 GB RAM or 32 GB, 4 GB RAM"
internal=internal.split(" or ")
variants=[]
for words in internal:
    temp=words.split(", ")
    try:
        internalsd=temp[0]
        ram=temp[1]
    except IndexError:
        continue
    internalsd=internalsd.split(" ")
    internalsd=internalsd[0]
    ram=ram.split(" ")
    ram=ram[0]
    internalsd=internalsd.split("/")
    ram=ram.split("/")
    temp1=[]
    if len(internalsd)==len(ram):
        for i in range(0,len(ram)):
            temp1.append(internalsd[i])
            temp1.append(ram[i])
        variants.append(temp1)
    else:
        if len(ram)==1:
            for j in range(0,len(internalsd)):
                temp2=[]
                temp2.append(internalsd[j])
                temp2.append(ram[0])
                variants.append(temp2)
        if len(internalsd)==1:
            for j in range(0,len(ram)):
                temp2=[]
                temp2.append(internalsd[0])
                temp2.append(ram[j])
                variants.append(temp2)
print(variants)
