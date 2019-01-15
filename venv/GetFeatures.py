import re
import os as op
import VeeQuestCrawler.VeeQuestCrawler.spiders.featurecrawler as crawler
import DatabaseConnection as db
from scrapy.crawler import CrawlerProcess
import ramandsdprocessing as getramandsd
"""process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(crawler.QuotesSpider)
process.start()"""
file=open("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\ScrapedPages\\gsmarenaFeatures\\Page-www.gsmarena.com.txt","r")
features={}
global rear,front
for words in file:
    regex=re.search('data-spec="[a-zA-Z0-9]*">[a-zA-Z0-9 (),:~&.\/-]*',words)
    regex1=re.search('<td class="ttl"\><a href="glossary.php3\?term=camera"\>[a-zA-Z]*<\/a></td>',words)
    if regex1:
        temp=regex1.group(0)
        if("Single" in temp or "Dual" in temp or "Triple" in temp or "Quad" in temp):
            rear=temp[52:]
    regex1=re.search('<td class="ttl"\><a href="glossary.php3\?term=secondary-camera"\>[a-zA-Z]*<\/a></td>',words)
    if regex1:
        temp=regex1.group(0)
        if("Single" in temp or "Dual" in temp or "Triple" in temp or "Quad" in temp):
            front=temp[62:]
    if regex:
        temp=regex.group(0)
        temp=temp[11:]
        temp=temp.split("\">")
        print (temp)
        features[temp[0]]=temp[1]
values=[]
cursor=db.mydb.cursor()
phoneid=cursor.rowcount+1
values.append(phoneid)
values.append(features["modelname"])
temp=features["year"]
year=temp[0:4]
values.append(int(year))
month=temp[6:]
switcher = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
            "August":8,"September":9,"October":10,"November":11,"December":12}
values.append(switcher[month])
values.append(int(features["weight"][0:3]))
values.append(float(features["displaysize"][0:4]))
values.append(features["displayresolution"][20:25])
ostype=features["os"].split(" ")
values.append(ostype[0])
values.append(ostype[1])
values.append(features["chipset"])
values.append(features["cpu"])
values.append(features["gpu"])
rmp=features["cam1modules"].split(" ")
rmp=int(rmp[0])
values.append(rmp)
if "Single" in rear:
    values.append(1)
elif "Dual" in rear:
    values.append(2)
elif "Triple" in rear:
    values.append(3)
elif "Quad" in rear:
    values.append(4)
else:
    values.append(0)
fmp=features["cam2modules"].split(" ")
fmp=int(fmp[0])
values.append(fmp)
if "Single" in front:
    values.append(1)
elif "Dual" in front:
    values.append(2)
elif "Triple" in front:
    values.append(3)
elif "Quad" in front:
    values.append(4)
else:
    values.append(0)
if "Fingerprint" in features["sensors"]:
    values.append(True)
else:
    values.append(False)
if "gyro" in features["sensors"]:
    values.append(True)
else:
    values.append(False)
bat=features["batdescription1"].split(" ")
for word in bat:
    try:
        values.append(int(word))
    except ValueError:
        continue
try:
    pr=features["price"].split(" ")
    for word in pr:
        try:
            values.append(int(word)*80-2000)
        except ValueError:
            print()
except KeyError:
    values.append(0)
query="insert into phonefeatures values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values=tuple(values)
print (query)
cursor.execute(query,values)
db.mydb.commit()
variants=features["internalmemory"]
querystmt="SELECT phoneID FROM `phonefeatures` WHERE ModelName=\""+features["modelname"]+"\""
cursor.execute(querystmt)
phid = cursor.fetchone()
variants=getramandsd.getRamAndSD(phid[0],variants)
for info in variants:
    query="insert into phonevariants values(%s,%s,%s)"
    values=tuple(info)
    cursor=db.mydb.cursor(buffered=True)
    cursor.execute(query,values)
db.mydb.commit()
