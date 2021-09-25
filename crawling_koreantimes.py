from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
path = '/home/ec2-user/environment/selenium/chromedriver'

driver = webdriver.Chrome(executable_path=path,options=options)
driver.implicitly_wait(8)

text = ''

driver.get('http://www.koreatimes.co.kr/www/sublist_743.html')

# news_list = driver.find_elements_by_class_name('list_article_area')
news_element = driver.find_element_by_class_name('list_article_area')

news_title_en = news_element.find_element_by_css_selector('div.list_article_headline.HD > a').text
news_title_kr = news_element.find_element_by_css_selector('div.list_articleHDK.HD_kor > a').text
title = news_title_en + '\n' + news_title_kr

news_element.click()

news_text = driver.find_element_by_id('startts').text

newline = news_text.find('\n')
text += title + news_text[newline + 1:]
print(text)


# text += news_title + '\n'

# print(news_body.text)


driver.quit()
