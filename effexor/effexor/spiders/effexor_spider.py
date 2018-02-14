# Import required packages 
from scrapy import Spider, Request
from effexor.effexor_item import EffexorItem


#Set up spider class
class effexor_spider(Spider):
	name = "effexor_spider"
	allowed_urls = ["https://www.webmd.com/"]
	start_urls = ["https://www.webmd.com/drugs/2/index"]
# just have to do one parse layer. first parse func cycles through reviews in groups of 5
	def parse(self, response):
		link = "https://www.webmd.com/drugs/drugreview-4896-Effexor+XR+oral.aspx?drugid=4896&drugname=Effexor+XR+oral&pageIndex={}&sortby=3&conditionFilter=-1" 
		links = [link.format(n) for n in range(689)] # change range to 689 for full run

		for url in links:
			yield Request(url, callback = self.parse_detail)

	def parse_detail(self, response):

		for x, y in zip(range(4,9), range(1,6)): #5 reviews per page. 
			
			review = '//*[@id="ratings_fmt"]/div[{}]'.format(x) #setting up tags for each of the 5

			reviewer = review + '//p[@class="reviewerInfo"]/text()'#pulling out relevant data from each review
			condition = review + '//div[1]/div[1]/text()'
			date = review + '//div[1]/div[2]/text()'
			effective = review + '//*[@id="ctnStars"]/div[1]/p[2]/span/text()'
			ease = review + '//*[@id="ctnStars"]/div[2]/p[2]/span/text()'
			satisfaction = review + '//*[@id="ctnStars"]/div[3]/p[2]/span/text()'
			comment = review + '//*[@id="comTrunc{}"]/text()'.format(y)

			item = EffexorItem()

			item['reviewer'] = response.xpath(reviewer).extract_first()
			item['condition'] = response.xpath(condition).extract_first()
			item['date'] = response.xpath(date).extract_first()
			item['effective'] = response.xpath(effective).extract_first()
			item['ease'] = response.xpath(ease).extract_first()
			item['satisfaction'] = response.xpath(satisfaction).extract_first()
			item['comment'] = response.xpath(comment).extract_first()

			yield item



		

		


	