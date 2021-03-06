import scrapy
import geturls as urls


class QuotesSpider(scrapy.Spider):
    global phone
    phone=""
    name = "FeaturesCrawler"
    def __init__(self, phoneName=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        print(phoneName,"--------------------------------------------------")
        phone=phoneName

    def start_requests(self):
        urllist=urls.geturllist(phone,"gsmarena")
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\ScrapedPages\\gsmarenaFeatures\\Page-%s.txt' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
