import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os


class TranslateService:

    @staticmethod
    def translate(from_language, to,  value_to_translate):
        try:
            
            url = os.environ.get('ENDPOINT')
            url = url.replace('{from}', from_language)
            url = url.replace('{to}', to)
            url = url.replace('{text}', value_to_translate)
        
            service = Service(executable_path='/usr/local/bin/chromedriver')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            browser = webdriver.Chrome(service=service, options=chrome_options)

            browser.get(url)
            time.sleep(2)
            result_element = None
            try:
                result_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1] ')))
                result_text = result_element.text
            except Exception as e:
                print(e)
                raise Exception(f"Try again, error: {str(e)}")
            browser.quit()
            print(url)
            return {
                "status":200,
                "from": from_language,
                "to": to,
                "text": value_to_translate,
                "result": result_text
            }
        except Exception as e:
            return {
                "status":400,
                "error": str(e)
            }

