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
    driver.get(f'https://browser.geekbench.com/search?page={CPUpage}&q={CPUname}&utf8=%E2%9C%93')
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #bench_list = soup.select('#wrap > div > div > div > div > div.col-9')

    Score_data = []
    for i in range(1, 26):
        Nm = soup.select_one(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div.col-12.col-lg-4 > span.list-col-model').text.strip()
        OS = soup.select_one(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div:nth-child(3) > span.list-col-text').text.strip()
        ST = soup.select_one(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div:nth-child(4) > span.list-col-text-score').text.strip()
        MT = soup.select_one(f'#wrap > div > div > div > div > div.col-9 > div.row > div:nth-child({i}) > div > div > div:nth-child(5) > span.list-col-text-score').text.strip()
        if(OS == 'Windows'):
            if(Nm.find(CPUname) != -1):
                #print(Nm, OS, ST, MT)
                mylist = [int(ST), int(MT)]
                Score_data.append(mylist)

    driver.quit()

    return Score_data

def crawlbenchlen(CPUname, CPUpage):
    options = Options()
    options.add_argument('headless')

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0.5)
    driver.set_window_size(1920, 1080)
    driver.get(f'https://browser.geekbench.com/search?page={CPUpage}&q={CPUname}&utf8=%E2%9C%93')
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    a = soup.select_one(f'#wrap > div > div > div > div > div.col-3 > ul > li.list-group-item.d-flex.justify-content-between.align-items-center.current > span').text.strip()

    if(a.find('K') != -1):
        a = a[:-1]
        return int(float(a)*1000)
    else:
        return int(a)