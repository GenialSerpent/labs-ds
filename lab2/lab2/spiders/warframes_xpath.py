import scrapy
from lab2.items import Lab2Item


class WarframesXpathSpider(scrapy.Spider):
    name = "warframe_css"
    allowed_domains = ["warframe.com"]
    start_urls = ["https://www.warframe.com/uk/game/warframes"]

    def parse(self, response):
        items = response.xpath('//div[contains(@class, "row")]'
            ).xpath('.//*[contains(@class,"wf")]')

        for item in items:
            name = item.xpath('.//div[contains(@class,"innerWfTitle")]/text()').get()
            url = item.xpath('.//div[contains(@class,"innerWfTitle")]/@href').get()

            yield Lab2Item(
                name=name,
                url=url,
            )
