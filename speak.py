# following module is for say function be getting a voice from chrome by using chrome driver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # log leve = 3 means it receives server message
chrome_options.headless = False  # if we turn this to True then the opening window of the following page is not be seen
Path = "D:\[Programming]\[Python Code]\[J.A.R.V.I.S.]\chromedriver.exe"

driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')


def say(text):
    textLength = len(str(text))
    if textLength == 0:
        pass
    data = str(text)
    form_area = '/html/body/div[3]/div[2]/form/textarea'
    driver.find_element(By.XPATH, value=form_area).send_keys(data)
    driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/form/input[1]').click()
    driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/form/textarea').clear()

    if textLength >= 30:
        time.sleep(4)
    elif textLength >= 40:
        time.sleep(6)
    elif textLength >= 55:
        time.sleep(8)
    elif textLength >= 70:
        time.sleep(10)
    elif textLength >= 100:
        time.sleep(12)
    elif textLength >= 120:
        time.sleep(14)
    else:
        time.sleep(2)


# import pyttsx3
# def say(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # rate is used to slow down the speech
#     engine.say(text)
#     engine.runAndWait()
