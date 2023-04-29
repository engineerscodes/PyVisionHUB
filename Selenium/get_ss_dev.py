import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from datetime import date


class Webscraper:
    __driver: WebDriver
    __title: str

    def __init__(self, chrome_driver_path="C:\\Users\\NAVEEN\Documents\\chromedriver.exe",user_data="C:\\Users\\NAVEEN\\AppData\\Local\\Google\\Chrome\\User Data"):
        self.__chrome_options = webdriver.ChromeOptions()
        self.__chrome_options.add_argument('--headless')
        self.__chrome_options.add_argument('--disable-gpu')
        self.__chrome_options.add_argument('debuggerAddress=127.0.0.1:9222')
        self.__chrome_options.add_argument(f'--user-data-dir={user_data}')
        self.__driver = webdriver.Chrome(chrome_driver_path, chrome_options=self.__chrome_options)

    def load_page(self, url: str = "https://github.com/engineerscodes", loading_time: int = 30):
        print("Reaching to Endpoint ........................")
        self.__driver.get(url)
        self.__title = self.__driver.title
        print(f"Waiting to Load Page for {loading_time} seconds -> {self.__title}")
        time.sleep(loading_time)

    def get_title(self) -> str:
        return self.__title

    def screenshot(self, filename: str, des_folder: str = os.path.dirname(__file__), custom_width: int = 1600):
        s = lambda x: self.__driver.execute_script('return document.body.parentNode.scroll' + x)
        self.__driver.set_window_size(custom_width, s('Height'))
        today = date.today().strftime("%d_%m_%Y")
        self.__driver.find_element(By.TAG_NAME, 'body').screenshot(f"{des_folder}\\{filename}_{today}.png")
        print(f'File Saved -> check path {des_folder}\\{filename}_{today}.png')

    def close(self):
        self.__driver.close()
        print("closing program")
