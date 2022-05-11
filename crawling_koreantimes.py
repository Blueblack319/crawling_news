from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
# driver.implicitly_wait(8)

category_list = ["743", "761"]


def extract_news_urls(src):
    urls = []
    driver.get(src)
    # time.sleep(10)
    news_list = driver.find_elements(By.CLASS_NAME, "list_article_area")
    for news_element in news_list:
        url = news_element.find_element_by_css_selector(
            "div.list_article_headline.HD > a"
        ).get_attribute("href")
        urls.append(url)
    # driver.close()
    return urls


def extract_by_content(urls):
    content = ""
    split_news = (
        "\n" + "---------------------------End----------------------------" + "\n"
    )

    for idx, url in enumerate(urls):
        driver.get(url)
        driver.implicitly_wait(5)
        # news_title_en = driver.find_element_by_css_selector('div.list_article_headline.HD > a').text
        # news_title_kr = driver.find_element_by_css_selector('div.list_articleHDK.HD_kor > a').text
        # title = news_title_en + '\n' + news_title_kr

        # driver.click()
        # time.sleep(3)

        title_en = driver.find_element_by_css_selector("div.view_headline.HD").text
        title_kr = driver.find_element_by_css_selector("div.view_headlineK.HD_kor").text
        title = title_en + "\n" + title_kr

        news_text = driver.find_element_by_id("startts").text

        first_enter = news_text.find("\n")
        text = title + news_text[first_enter:]

        content += text + split_news

    return content


def get_koreantimes(start, end, category):
    contents = ""
    for page in range(start, end + 1):
        URL = f"http://www.koreatimes.co.kr/www/sublist_{category}_{page}.html"
        urls = extract_news_urls(URL)
        contents += extract_by_content(urls)
    driver.quit()
    return contents
