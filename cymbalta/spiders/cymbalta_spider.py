# Import required packages 
from scrapy import Spider, Request
from cymbalta.cymbalta_items import CymbaltaItem


#Set up spider class
class cymbalta_spider(Spider):
	name = "cymbalta_spider"
	allowed_urls = ["https://www.webmd.com/"]
	start_urls = ["https://www.webmd.com/drugs/2/index"]
# just have to do one parse layer. first parse func cycles through reviews in groups of 5
	def parse(self, response):
		link = "https://www.webmd.com/drugs/drugreview-91491-Cymbalta+oral.aspx?drugid=91491&drugname=Cymbalta+oral&pageIndex={}&sortby=3&conditionFilter=-1" 
		links = [link.format(n) for n in range(10)] # change range to 917 for full run

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

			item = CymbaltaItem()

			item['reviewer'] = response.xpath(reviewer).extract_first()
			item['condition'] = response.xpath(condition).extract_first()
			item['date'] = response.xpath(date).extract_first()
			item['effective'] = response.xpath(effective).extract_first()
			item['ease'] = response.xpath(ease).extract_first()
			item['satisfaction'] = response.xpath(satisfaction).extract_first()
			item['comment'] = response.xpath(comment).extract_first()

			yield item



		

		


		

		#dates = response.xpath('//div[@class = "date"]/text()').extract() # saves a list of dates 
		#reviewers = response.xpath('//p[@class = "reviewerInfo"]/text()').extract() # saves a list of reviewrs
		#conditions = conditions = response.xpath('//div[@class = "conditionInfo"]/text()').extract() # saves a list of conditions
		#except for comment, which has it's own tag condition
		#com_tag = '//p[@id = "comFull{}"]/text()' 
		#comments = [response.xpath(com_tag.format(n)).extract() for n in range(1,6)] # gives a list of comments 
		#ratings = response.xpath('//span[@class = "current-rating"]/text()').extract() # gives all ratings listed on the site
		#effects = [ratings[n] for n in range(0, len(ratings),3)] # saves a list of ratings for effectiveness 
		#eases = [ratings[n] for n in range(1, len(ratings),3)] # saves a list of ratings for ease of use
		#satisfactions = [ratings[n] for n in range(2, len(ratings),3)] # saves a list of ratings for satisfaction

		#item = CymbaltaItem()

#setting loop to append to items  
		#for i in range(5):

			#item['date'] = dates
			#item['reviewer'] = reviewers[i]
			#item['condition'] = conditions[i]
			#item['effective'] = effects[i]
			#item['ease'] = eases[i]
			#item['satisfaction'] = satisfactions[i]
			#item['comment'] = comments[i]

			#print(item)
			#yield item





	




#url = 'https://www.webmd.com/drugs/drugreview-91491-Cymbalta+oral.aspx?drugid=91491&drugname=Cymbalta+oral&pageIndex=0&sortby=3&conditionFilter=-1'


