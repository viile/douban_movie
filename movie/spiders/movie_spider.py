import scrapy

class MovieSpider(scrapy.Spider):
	name = "movie"
	allowed_domains = ["douban.com"]
	start_urls = [
		"https://movie.douban.com/subject/1292052/"
	]

	def parse(self, response):
		#for i in response.selector.xpath('//div[@id="info"]/span/text()')
		#	print i.extract()
		pass
