from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chromium_path = "./driver/chromedriver"
service = Service(chromium_path)

login = "https://rahulshettyacademy.com/loginpagePractise/"
secretPassword = "learning"

browser = webdriver.Chrome(service=service)
browser.implicitly_wait(4)

browser.get(login)
browser.find_element(by='xpath', value='/html/body/a').click()
tabsOpened = browser.window_handles
browser.switch_to.window(tabsOpened[1])

element = browser.find_element(by='xpath', value='//*[@id="interview-material-container"]/div/div[2]/p[2]/strong/a')
username = element.text[7:25] + 'sd'

browser.close()

browser.switch_to.window(tabsOpened[0])
input_username = browser.find_element(by='id', value='username')
password = browser.find_element(by='id', value="password")
browser.find_element(by='id', value="terms").click()
input_username.send_keys(username)
password.send_keys(secretPassword)
selectElement = browser.find_element(by='xpath', value='//*[@id="login-form"]/div[5]/select')
select = Select(selectElement)
select.select_by_visible_text('Teacher')
browser.find_element(by='id', value="signInBtn").click()
try:
    wait = WebDriverWait(browser, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    print(browser.find_element(By.CSS_SELECTOR, ".alert-danger").text)
except:
    print('login')


browser.close()