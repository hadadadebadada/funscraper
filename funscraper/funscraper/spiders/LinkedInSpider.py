import scrapy
from scrapy import item
from scrapy.loader import ItemLoader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from funscraper.items import SimpleItem


class LinkedInSpider(scrapy.Spider):
    name = 'linkedin'
    start_urls = ['https://www.linkedin.com/company/lufthansa-systems/']

    def start_requests(self):
        s = Service(ChromeDriverManager().install())

        options = ChromeOptions()
        options.headless = False

        driver = webdriver.Chrome(service=s, options=options)

        driver.get("https://www.linkedin.com/login/de?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

        xpath_login = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
        xpath_password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        xpath_login_btn = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

        xpath_login.clear()
        xpath_login.send_keys("artur_pfeifer2@gmx.de")
        xpath_password.clear()
        xpath_password.send_keys("314159abc")
        xpath_login_btn.click()

        driver.get("https://www.linkedin.com/company/meta/people/")
        xpath_link = '//a[@class="ember-view link-without-visited-state"]'
        href_link = driver.find_elements(by=By.XPATH, value=xpath_link)
        links = []

        for link_el in href_link:
            href = link_el.get_attribute("href")
            print('TESTESTESTESTTESTETSTETSTESTST START')
            print(href)
            links.append(href)
            #yield scrapy.Request(href)
        driver.quit()

    def parse(self, response, **kwargs):
        item = SimpleItem()
       # item['title'] = response.css('h1::text').get()
        item['title'] = response.xpath('//h1[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]//text()').extract()
        yield item

    # def parse(self, response):
    #
    #     item['title'] = response.xpath('//*[@id="ember58"]').extract()
    #    # item['link'] = link.xpath('@href').extract()
    #     yield item
