import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # log leve = 3 means it receives server message
chrome_options.headless = False  # if we turn this to True then the opening window of the following page is not be seen
Path = "D:\[Programming]\[Python Code]\[J.A.R.V.I.S.]\chromedriver.exe"

driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = r"https://www.youtube.com/"
driver.get(website)

from speak import say
say("sir, youtube is opened, can you please tell me what kind of content you want to search?")
time.sleep(8)

def search(text):
    searchText = str(text)
    form_area = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
    driver.find_element(By.XPATH, value=form_area).send_keys(searchText)
    driver.find_element(By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button').click()