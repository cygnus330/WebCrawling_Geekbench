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
    #options.add_argument('headless')

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0.5)
    driver.set_window_size(1920, 1080)
    driver.get(f'https://browser.geekbench.com/search?page={CPUpage}&q={CPUname}&utf8=%E2%9C%93')
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #bench_list = soup.select('#wrap > div > div > div > div > div.col-9')

    Score_data = []

    for i in range(1, 26):
        OS = soup.select(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div:nth-child(3) > span.list-col-text')#.text.strip()
        ST = soup.select(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div:nth-child(4) > span.list-col-text-score')#.text.strip()
        MT = soup.select(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div:nth-child(5) > span.list-col-text-score')#.text.strip()
        mylist = [OS, ST, MT]
        print(mylist)
        Score_data.append(mylist)

    return Score_data