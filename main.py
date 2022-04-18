import scrapy
from scrapy import item
from scrapy.loader import ItemLoader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

s = Service(ChromeDriverManager().install())

options = ChromeOptions()
options.headless = False

driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.linkedin.com/login/de?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.set_window_size(1920, 1080)

xpath_login = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
xpath_password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
xpath_login_btn = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

xpath_login.clear()
xpath_login.send_keys("artur.pfeifer30@gmail.com")
xpath_password.clear()
xpath_password.send_keys("314159abc")
xpath_login_btn.click()

# driver.get("https://www.linkedin.com/company/meta/people/")
#
# xpath_allPeople = '//span[@class="link-without-visited-state t-bold t-black--light"]'
#
# href_link = WebDriverWait(driver,500).until(EC.presence_of_element_located((By.XPATH,xpath_allPeople))).click()
#
# #driver.find_element(by=By.XPATH,value=xpath_allPeople).click()
#
# xpath_linkToUser = '//a[@class="app-aware-link"]'
# href_link = driver.find_elements(by=By.XPATH, value=xpath_linkToUser)
# print('TEST')
# print(href_link)
# xpath_link = '//*[contains(@class,"ember-view link-without-visited-state")]'
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

try:
    time.sleep(1)

   #  # href_link = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,xpath_link)))
   #  xpath_linkToUser = '//a[@class="app-aware-link"]'
   #
   #  ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
   #
   #  href_link = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
   #      .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath_linkToUser)))
   #
   # # href_link = driver.find_elements(by=By.XPATH, value=xpath_linkToUser)
   #  print('TEST')
   #  print(href_link)

    links = []

finally:
    for x in (n + 1 for n in range(10)):
        time.sleep(3)

        driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B28985631%2C8935798%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page="+str(x))


        #driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%2210667%22%2C%2276987811%22%2C%22289891%22%2C%222763277%22%2C%222289109%22%2C%2227046884%22%2C%2223769%22%2C%2227104390%22%2C%2216159097%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page="+str(x))
        #for link_el in href_link:
        xpath_linkToUser = '//a[@class="app-aware-link"]'
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        time.sleep(3)

        href_elements = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
    .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath_linkToUser)))

        for link_el in href_elements:
            href = link_el.get_attribute("href")
            print(href)
            links.append(href)

        # val = href_element.get_attribute("href")
        #
        # #href = link_el.get_attribute("href")
        # print(val)
        # links.append(href_element)
        # yield scrapy.Request(href)
    driver.quit()










#showMoreBtnXpath = '//*[@class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button"]'
#
# for x in range(100):
#     time.sleep(2)
#
#     try:
#         driver.find_element(by=By.XPATH, value=showMoreBtnXpath).click()
#     except:
#         action = ActionChains(driver)
#
#         action.send_keys(Keys.PAGE_DOWN)
#
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#
# # weitere elemente anzeigen btn
# # artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button
# try:
#     time.sleep(500)
#
#     # href_link = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,xpath_link)))
#     xpath_link = '//a[@class="ember-view link-without-visited-state"]'
#     href_link = driver.find_elements(by=By.XPATH, value=xpath_link)
#     print('TEST')
#     print(href_link)
#
#     links = []
#
# finally:
#     for link_el in href_link:
#         href = link_el.get_attribute("href")
#         print('TESTESTESTESTTESTETSTETSTESTST START')
#         print(href)
#         links.append(href)
#         # yield scrapy.Request(href)
#     driver.quit()
