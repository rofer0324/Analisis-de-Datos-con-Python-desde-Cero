import scrapy
from scrapy.crawler import CrawlerProcess

class EventsSpider(scrapy.Spider):
    name = 'eventspider'
    start_urls = ['https://www.python.org/events/python-events/',]
    eventos = []
    
    def parse(self, response):
        events = response.xpath('//ul[contains(@class, "list-recent-events menu")]/li')
        
        for event in events:
            detalles = {}
            detalles["name"] = event.xpath('h3[@class="event-title"]/a/text()').get()
            detalles["Location"] = event.xpath('p/span[@class="event-location"]/text()').get()
            detalles["time"] = event.xpath('p/time/text()').get()
            self.eventos.append(detalles)

if __name__ == "__main__":
    process = CrawlerProcess({'LOG_LEVEL': "ERROR"})
    process.crawl(EventsSpider)
    spider = next(iter(process.crawlers)).spider
    process.start()
    
    for event in spider.eventos:
        print(event)
    
    