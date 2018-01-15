import scrapy

class DailyStarSpider(scrapy.Spider):
	name = "dailystar"

	def start_requests(self):
		urls = [
			'http://www.thedailystar.net/newspaper',
			]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

#	def parse(self, response):
#		for news in response.css('div.three-33'):
##				headings = inner_news.extract()
#				links = "http://www.thedailystar.net"+link.extract()
#			print(dict(headings=headings))
#			print(dict(links=links))
	def parse(self, response):
		for news in response.css('div.three-33'):
			#database = {}
			yield{
			'newz' : news.css('a::text').extract_first(),
			'links': "http://www.thedailystar.net" + str(news.css('a.thumb::attr(href)').extract_first()),
			#database[newz]=link
			}