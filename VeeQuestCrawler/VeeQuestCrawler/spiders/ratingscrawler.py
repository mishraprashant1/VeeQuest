import scrapy
import geturls as urls

global phone
class QuotesSpider(scrapy.Spider):
    phone=""
    name = "FeaturesCrawler"
    def __init__(self, phoneName=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        print(phoneName,"--------------------------------------------------")
        phone=phoneName
    def start_requests(self):
        urllist=urls.geturllist(phone,"flipkart")
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\ScrapedPages\\FlipkartRatings\\Page-www.flipkart.com.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
