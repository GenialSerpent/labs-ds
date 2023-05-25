import scrapy
from bs4 import BeautifulSoup
from lab2.items import Lab2Item


class LaptopsSpider(scrapy.Spider):
    name = "warframe_css"
    allowed_domains = ["warframe.com"]
    start_urls = ["https://www.warframe.com/uk/game/warframes"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        items = soup.find(name="div", class_="row").find_all(class_="wf") + soup.find(name="div", class_="row").find_all(class_="primewf")
        
        for item in items:
            name = item.find(name="div", class_="innerWfTitle").find(string=True, recursive=False).strip()
            url = item.find(name="div", class_="innerWfTitle").get("href")

            yield Lab2Item(
                name=name,
                url=f"https://hotline.ua{url}",
            )
