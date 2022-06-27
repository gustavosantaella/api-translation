import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chromium_path = "./driver/chromedriver"
service = Service(chromium_path)

browser = webdriver.Chrome(service=service)
browser.get('https://translate.google.cn/?hl=es&sl=es&tl=en&op=translate')
element = browser.find_element(by='xpath', value='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
element.send_keys("hola amigo")
time.sleep(2)
print('two seconds')
resultElement = browser.find_element(by='xpath', value='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[7]/div/div[1]/span[1]')
print(resultElement.text)

browser.close()
