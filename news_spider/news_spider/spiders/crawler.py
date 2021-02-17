import scrapy  
from ..items import NewsSpiderItem
from selenium import webdriver
import time
from scrapy import Selector
class Nspider(scrapy.Spider): 
   name = "news" 
#    allowed_domains = ["dmoz.org"] 
   
   start_urls = [ 
    "https://inshorts.com/en/read",
    "https://inshorts.com/en/read/politics",
    "https://inshorts.com/en/read/sports",
    "https://inshorts.com/en/read/entertainment",
    "https://inshorts.com/en/read/business",

       ]  
   
   def parse(self, response): 
      options = webdriver.ChromeOptions()
      options.add_argument("headless")
      desired_capabilities = options.to_capabilities()
      driver = webdriver.Chrome('C:/Users/HP/chromedriver',desired_capabilities=desired_capabilities)
      # driver = webdriver.Chrome('C:/Users/HP/chromedriver')
      driver.get(response.url)
      time.sleep(4)
      button = driver.find_element_by_xpath('//*[@id="load-more-btn"]')
      button.click()
      time.sleep(5)
      
      new_selector = Selector(text=driver.page_source)
      x=new_selector.css(".news-card")
      items=NewsSpiderItem()
      url=response.url
      items['url']=url
      for i in x:
         head=i.css(".news-right-box .clickable span::text").extract()
         news=i.css(".news-card-content div::text").extract()
         img=i.css(".news-card-image::attr(style)")[0].extract()[23:-2]
         items['head']=head[0]
         items['news']=news[0]
         items['img']=img
         
         yield items         
            # 'news':i
      
         
