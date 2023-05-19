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
        url = url.replace('{text}', value_to_translate)
     
        service = Service(executable_path='/usr/local/bin/chromedriver')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(service=service, options=chrome_options)

        browser.get(url)
        # element = browser.find_element(by='xpath',
        #                                value='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
        # element.send_keys(value_to_translate)
        time.sleep(2)
        result_element = browser.find_element(by='xpath',
                                              value='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]')

        print(url)
        return {
            "from": from_language,
            "to": to,
            "text": value_to_translate,
            "result": result_element.text
        }

