import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os


class TranslateService:

    @staticmethod
    def translate(from_language, to,  value_to_translate):

        url = os.environ.get('ENDPOINT')
        url = url.replace('{from}', from_language)
        url = url.replace('{to}', to)

        chromium_path = "./driver/chromedriver"
        service = Service(chromium_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(service=service, options=chrome_options)

        browser.get(url)
        element = browser.find_element(by='xpath',
                                       value='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
        element.send_keys(value_to_translate)
        time.sleep(2)
        result_element = browser.find_element(by='xpath',
                                              value='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[7]/div/div[1]/span[1]')

        return {
            "from_language": from_language,
            "to": to,
            "original_text": value_to_translate,
            "value_translated": result_element.text
        }

