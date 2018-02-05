# Import required packages 
from scrapy import spider 
from cymbalta import cymbalta.items


#Set up spider class
class cymbalta_spider(spider):
	name = "cymbalta_spider"
	allowed_urls = ["https://www.webmd.com/"]
	start_urls = ["https://www.webmd.com/drugs/drugreview-91491-Cymbalta+oral.aspx?drugid=91491&drugname=Cymbalta+oral&pageIndex=0&sortby=3&conditionFilter=-1"]
# just have to do one parse layer. first parse func cycles through reviews in groups of 5
def parse(self, response):
	link = "https://www.webmd.com/drugs/drugreview-91491-Cymbalta+oral.aspx?drugid=91491&drugname=Cymbalta+oral&pageIndex={}&sortby=3&conditionFilter=-1" 
	links = [link.format(n) for n in range(10)] # change to 917 for full run

	for url in links:
		response(url, callback = self.parse_detail)

def parse_detail(self, response):
	#for each cat, scrapes 5 inputs at a time for the current page

	dates = response.xpath('//div[@class = "date"]/text()').extract() # saves a list of dates 
	reviewers = response.xpath('//p[@class = "reviewerInfo"]/text()').extract() # saves a list of reviewrs
	conditions = conditions = response.xpath('//div[@class = "conditionInfo"]/text()').extract() # saves a list of conditions
	#except for comment, which has it's own tag condition
	com_tag = '//p[@id = "comFull{}"]/text()' 
	comments = [response.xpath(com_tag.format(n)).extract() for n in range(1,6)] # gives a list of comments 
	ratings = response.xpath('//span[@class = "current-rating"]/text()').extract() # gives all ratings listed on the site
	effects = [stars[n] for n in range(0, len(stars),3)] # saves a list of ratings for effectiveness 
	eases = [stars[n] for n in range(1, len(stars),3)] # saves a list of ratings for ease of use
	satisfactions = [stars[n] for n in range(2, len(stars),3)] # saves a list of ratings for satisfaction

	




#url = 'https://www.webmd.com/drugs/drugreview-91491-Cymbalta+oral.aspx?drugid=91491&drugname=Cymbalta+oral&pageIndex=0&sortby=3&conditionFilter=-1'


