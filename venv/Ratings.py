def getWordlist(path):
    f=open(path,"r")
    wordslist=[]
    for word in f:
        wordslist.append(word[0:int(len(word)-1)])
    return wordslist
positveWordList_path="C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\positive-words.txt"
negativeWordList_path="C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\negative-words.txt"
positveWordList=getWordlist(positveWordList_path)
negativeWordList=getWordlist(negativeWordList_path)
def rateReviews(dictionary):
    for nouns in dictionary:
        neg=0
        pos=0
        templist=dictionary[nouns]
        for adj in templist:
            if adj in positveWordList:
                pos+=1
            elif adj in negativeWordList:
                neg+=1
            else:
                print ("Adjective Not Found : ",adj)
        dictionary[nouns]=([pos,neg])
    return dictionary

