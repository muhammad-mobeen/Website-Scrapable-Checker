import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #..............
from selenium.webdriver.support import expected_conditions as EC    #................
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
import random, string  # Remove in production


# url = https://ads.google.com/aw/campaigns/new

class WebScrapper:
    def __init__(self) -> None:
        self.driver = self.gen_driver()

    def gen_driver(self):
        try:
            chrome_options = uc.ChromeOptions()
            # chrome_options.headless = True
            # chrome_options.add_argument('--headless=new')
            driver = uc.Chrome(options=chrome_options)
            return driver
        except Exception as e:
            print("Error in Driver: ",e)

    def prosecutor(self):
        self.driver.get("https://www.daraz.pk/")
        os.system("pause")
        product_title_xpath = '//*[@id="hp-flash-sale"]/div[2]/div[2]/a[1]/div[2]/div[1]'
        title = self.driver.find_element(By.XPATH, product_title_xpath).text

        print("Product Title:",title)
        productpricepath = '//*[@id="hp-flash-sale"]/div[2]/div[2]/a[1]/div[2]/div[2]/span[2]'
        price = self.driver.find_element(By.XPATH, productpricepath).text
        print("Price is: ", price)


if __name__ == '__main__':
    agent = WebScrapper()
    # agent.prosecutor()
    agent.markhors()
    os.system("pause")
    