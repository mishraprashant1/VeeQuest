import os as op
import VeeQuestCrawler.VeeQuestCrawler.spiders.blogscrawler as crawler
from scrapy.crawler import CrawlerProcess
import os as os

def getBlogs():
    """process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(crawler.QuotesSpider)
    process.start()"""
    files=os.listdir("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\blogs")
    sentence=""
    for file in files:
        f=open("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\blogs\\"+file,"r")
        try:
            for words in f:
                if type(words)==str:
                    sentence=sentence+words
        except UnicodeDecodeError:
            print("Unicode decode error")
    return sentence
