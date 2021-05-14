import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import alert_is_present
from ObjectPage import ObjectPage

class WebInterface(object):
    def __init__(self):
        self.implicitly_timeout = 15
        self.page_load_timeout = 15
        self.chromedriver_path = os.path.join("driver", "chromedriver.exe")

    def start_browser(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--safebrowsing-disable-download-protection")
        options.add_argument("safebrowsing-disable-extension-blacklist")

        self.driver = webdriver.Chrome(options=options, executable_path=self.chromedriver_path)
        self.driver.get(url)

    def get_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        try:
            self.driver.close()
            self.driver.quit()
        except:
            traceback.print_exc()
            raise Exception(traceback._context_message)

    def wait_for_seconds(self, timer=1):
        time.sleep(timer)
        return timer

    def is_page_ready(self):
        result = self.driver.execute_script("return document.readyState;")
        if result.lower() == "complete":
            return True
        return False

    def wait_for_ready(self):
        print("Wait for loading complete...")
        timer = 0
        while not self.is_page_ready():
            if timer > self.page_load_timeout:
                break
            timer += self.wait_for_seconds()
        self.wait_for_seconds(self.implicitly_timeout)

    def click_on_xpath(self, locator):
        element = WebDriverWait(self.driver, self.implicitly_timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def check_on_notify(self, locator):
        try:
            WebDriverWait(self.driver, self.implicitly_timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
            return True
        except:
            return False

    def click_on_notify(self, locator):
        if self.check_on_notify(locator):
            self.click_on_xpath(locator)
        else:
            pass

    def send_key_on_element(self, locator, key):
        WebDriverWait(self.driver, self.implicitly_timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        self.driver.find_element_by_xpath(locator).clear()
        self.driver.find_element_by_xpath(locator).send_keys(key)

    def click_on_product(self, name_product):
        locator = "//span[contains(text(), '" + name_product + "')]"
        element = WebDriverWait(self.driver, self.implicitly_timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def submit_on_element(self, locator):
        self.driver.find_elements_by_xpath(locator).submit()

    def find_element_on_xpath(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def check_element_exist(self, locator):
        try:
            self.driver.find_element_by_xpath(locator)
            return True
        except:
            return False