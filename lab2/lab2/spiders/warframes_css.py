import scrapy
from lab2.items import Lab2Item


class WarframesCssSpider(scrapy.Spider):
    name = "warframe_css"
    allowed_domains = ["warframe.com"]
    start_urls = ["https://www.warframe.com/uk/game/warframes"]

    def parse(self, response):
        items = response.css('div.row').css('.wf')
        
        for item in items:
            # Знаходимо назву
            name = item.css('div.innerWfTitle::text').get()
            # url
            url = item.css('div.innerWfTitle::attr(href)').get()
            yield Lab2Item(
                name=name,
                url=url,
            )
