import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from datetime import date


class Webscraper:
    __driver: WebDriver
    __title: str
    __download_path: str

    def __init__(self, chrome_driver_path="C:\\Users\\NAVEEN\Documents\\chromedriver.exe",
                 user_data="C:\\Users\\NAVEEN\\AppData\\Local\\Google\\Chrome\\User Data",
                 download_path: str = os.path.dirname(__file__)):
        self.__download_path = download_path
        self.__chrome_options = webdriver.ChromeOptions()
        self.__chrome_options.add_argument('--headless')
        # prefs = {"download.default_directory": self.__download_path}
        # self.__chrome_options.add_experimental_option("prefs", prefs)
        self.__chrome_options.add_argument('--disable-gpu')
        self.__chrome_options.add_argument('debuggerAddress=127.0.0.1:9222')
        self.__chrome_options.add_argument(f'--user-data-dir={user_data}')
        self.__chrome_options.add_argument(f'--download.default_directory={self.__download_path}')
        self.__chrome_options.add_argument(
            "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'")
        self.__driver = webdriver.Chrome(chrome_driver_path, chrome_options=self.__chrome_options)
        self.__driver.execute_cdp_cmd('Page.setDownloadBehavior',
                                      {'behavior': 'allow', 'downloadPath': download_path})

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
        time.sleep(10)  # wait till file is downloaded
        self.__file_handler()

    def close(self):
        self.__driver.close()
        print("closing program")

    def __file_handler(self):
        today = date.today().strftime("%d_%m_%Y")
        extension = ".png"  # Filter by file Type
        os.chdir(self.__download_path)
        files = glob.glob("*" + extension)
        files.sort(key=os.path.getmtime, reverse=True)
        most_recent_file = os.path.join(self.__download_path, files[0])
        file_name, file_ext = os.path.splitext(most_recent_file)
        new_rename_path = f"{file_name}_{today}{file_ext}"
        os.rename(most_recent_file, new_rename_path)
        print(f"Most recently downloaded file: {most_recent_file} has been renamed to -> {new_rename_path}")
