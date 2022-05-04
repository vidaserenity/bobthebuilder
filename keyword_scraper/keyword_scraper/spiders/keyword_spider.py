import scrapy

class keyword_spider(scrapy.Spider):
    name = "keyword_scraper"

    start_urls = ["https://www.theladders.com/career-advice/1000-industry-specific-keywords-that-will-make-your-resume-unstoppable-according-to-experts"]

    def parse(self,response):
        career = []
        article = response.css('article.article-content').get()
        # for x in article.css():
        #     pass

        for headings in article.css('h3'):
            career += headings.css('::text').get()
            # grabs all the text under headings
            # appends them to list named career
            # we'd probably have to clean it afterwards
            # list comprehension form
            # career = [headings.css('::text') for headings in article.css('h3')]
        
        yield career   
