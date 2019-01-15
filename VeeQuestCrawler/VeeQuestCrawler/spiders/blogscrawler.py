import scrapy
import geturls as urls
from inscriptis import get_text
global phone

class QuotesSpider(scrapy.Spider):
    phone=""
    name = "FeaturesCrawler"
    def __init__(self, phoneName=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        print(phoneName,"--------------------------------------------------")
        phone=phoneName

    def start_requests(self):
        urllist = urls.geturllist(phone, "")
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\blogs\\Page-%s.txt' % page
        resp = response.css("body").extract()
        output = get_text(resp[0])
        with open(filename, 'wb') as f:
            f.write(output.encode())
