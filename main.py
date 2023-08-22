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

class AdsAutomater:
    def __init__(self) -> None:
        self.driver = self.gen_driver()
        # self.email, self.password = self.read_creds()

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

    def read_creds(self):
        with open ("creds.txt", "r") as myfile:
            creds = myfile.read().splitlines()
        return creds

    def prosecutor(self):
        # self.driver.get("https://muhammadmobeen.com")
        self.driver.get("https://huggingface.co/chat/")
        print("Please Enter Your Prompt: ",end="")
        # ask_text = input()
        ask_text = """
        You are a story teller.
        Please generate a short story based on a simple narrative, the story should not be more than 200 words.

        CONTEXT: two bulls fighiting each other
        STORY:
        """
        # ask_text = """hello"""
        print()
        self.send_keys_manager(
            "Entered Text", 
            '//*[@id="app"]/div[1]/div/div[2]/form/div/div/textarea',
            ask_text
            )
        self.click_manager(
            "Enter Text BTN",
            '//*[@id="app"]/div[1]/div/div[2]/form/div/button'
        )
        text_response = self.get_text_manager(
            "Get Text",
            '//*[@id="app"]/div[1]/nav[3]/div[2]/a[1]/div',
            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[1]/div'
        )
        print("\n\nText Response:-\n",text_response)
        # self.login_manager()
        # os.system("pause")
        # self.initial_page_navigator()
        # self.campaign_settings_navigator()

    def wait_manager(self, identifier, t, mode=By.XPATH):
        i = 1
        while True:
            try:
                # WebDriverWait(self.driver, t).until(EC.visibility_of_element_located((By.CLASS_NAME, identifier)))
                element = self.driver.find_element(mode, identifier)
                if element:
                    print("[{}]Wait Manager [Success]: Element Detected no need to wait for {} seconds".format(i,t))
                    break
                else:
                    print("[{}]Wait Manager [Active]: Element not Detected! Waiting for {} seconds".format(i,t))
                    time.sleep(t)
                # WebDriverWait(self.driver, t).until(EC.presence_of_element_located((By.CSS_SELECTOR, identifier)))
            except Exception as e:
                print("[{}]Wait Manager [Error]: {}\nNow waiting for {} seconds!".format(i,str(e).split('\n')[0],t))
                time.sleep(t)
            i+=1

    def click_manager(self, name, identifier, mode=By.XPATH):
        t = 3
        i=1
        while True:
            try:
                self.driver.find_element(mode, identifier).click()
                print("[{}]Click Manager [Success]: {} clicked successfully!".format(i,name))
                break
            except Exception as e:
                print("[{}]Click Manager [Error]:{}\n[{}]Click Manager [Active]: Activating Wait Manager".format(i,str(e).split('\n')[0],i))
                # time.sleep(t)
                self.wait_manager(identifier, t, mode)
            i+=1

    def get_text_manager(self, name, tag_identifier, text_identifier, mode=By.XPATH):
        t = 3
        i=1
        while True:
            try:
                generated_text = self.driver.find_element(mode, text_identifier).text
                chat_tag = self.driver.find_element(mode, tag_identifier).text
                if chat_tag.find("Untitled") == -1:
                    print("[{}]Get Text Manager [Success]: {} content generated successfully!".format(i,name))
                    break
                else:
                    print("[{}]Get Text Manager [Waiting]: {} waiting for contenet generation".format(i,name))
            except Exception as e:
                print("[{}]Get Text Manager [Error]:{}\n[{}]Get Text Manager [Active]: Activating Wait Manager".format(i,str(e).split('\n')[0],i))
                # time.sleep(t)
                self.wait_manager(text_identifier, t, mode)
            i+=1
        return generated_text

    def send_keys_manager(self, name, identifier, keys, mode=By.XPATH):
        t = 3
        i=1
        while True:
            try:
                for part in keys.split('\n'):
                    self.driver.find_element(mode, identifier).send_keys(part)
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                print("[{}]Send Keys Manager [Success]: {} keys sent successfully!".format(i,name))
                break
            except Exception as e:
                print("[{}]Send Keys Manager [Error]:{}\n[{}]Send Keys Manager [Active]: Activating Wait Manager".format(i,str(e).split('\n')[0],i))
                self.wait_manager(identifier, t, mode)
            i+=1

    def login_manager(self):
        username_XPATH = '//*[@id="identifierId"]'
        username_next_btn_XPATH = '//*[@id="identifierNext"]/div/button'
        password_XPATH = '//*[@id="password"]/div[1]/div/div[1]/input'
        password_next_btn_XPATH = '//*[@id="passwordNext"]/div/button'

        # username
        self.send_keys_manager('username', username_XPATH, self.email)
        self.click_manager("Username Next Button", username_next_btn_XPATH)

        # password
        self.send_keys_manager('password', password_XPATH, self.password)
        self.click_manager("Password Next Button", password_next_btn_XPATH)




if __name__ == '__main__':
    agent = AdsAutomater()
    agent.prosecutor()
    os.system("pause")
    