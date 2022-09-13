from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def crawlpage(CPUname, CPUpage):
    options = Options()
    options.add_argument('headless')

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0.5)
    driver.set_window_size(1920, 1080)
    driver.get('https://browser.geekbench.com/search?page={CPUpage}&q={CPUname}&utf8=%E2%9C%93')
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    bench_list = soup.select('div.row')

    Score_data = []

    for v in bench_list:
        if v.find('div', class_='col-12 list-col'):
            if (v.select_one('div:nth-child(3) > span.list-col-text').text.strip() == "Windows"):
                stscore = v.select_one('div:nth-child(4) > span.list-col-text-score').text.strip()
                mtscore = v.select_one('div:nth-child(5) > span.list-col-text-score').text.strip()
            #mylist = [stscore, mtscore]
            print(stscore, mtscore)
            #Score_data.append(mylist)

    #return Score_data