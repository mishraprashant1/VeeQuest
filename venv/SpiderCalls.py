import VeeQuestCrawler.VeeQuestCrawler.spiders.blogscrawler as crawler1
import VeeQuestCrawler.VeeQuestCrawler.spiders.featurecrawler as crawler2
import VeeQuestCrawler.VeeQuestCrawler.spiders.flipkartcrawler as crawler
from scrapy.crawler import CrawlerProcess

def callSpiders():
    phone=input("Enter the phone name:")

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    })
    process.crawl(crawler1.QuotesSpider,phoneName=phone)
    process.crawl(crawler2.QuotesSpider,phoneName=phone)
    process.crawl(crawler.FlipkartSpider,phoneName=phone)
    process.start()
callSpiders()
