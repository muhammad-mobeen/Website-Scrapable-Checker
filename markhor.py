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
            chrome_options.add_argument('--headless=new')
            # chrome_options.add_argument('--proxy-server=http://'+PROXY)
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

    def markhors(self):
        self.driver.get("https://markhorverse.com/about")
        card_xpath = '//*[@id="root"]/div/div[4]/div[2]/div/div'
        cards = self.driver.find_elements(By.XPATH, card_xpath)
        print("Cards Found:", len(cards))

        for card in cards:
            name = card.find_element(By.TAG_NAME, "h1").text
            role = card.find_element(By.TAG_NAME, "p").text
            print("Name:",name)
            print("Role:",role)
            print("--------------------------------------------")


if __name__ == '__main__':
    agent = WebScrapper()
    # agent.prosecutor()
    agent.markhors()
    os.system("pause")
    