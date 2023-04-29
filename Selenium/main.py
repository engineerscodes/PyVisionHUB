from get_ss_dev import Webscraper

driver = Webscraper(chrome_driver_path="C:\\Users\\NAVEEN\Documents\\chromedriver.exe",user_data="C:\\Users\\NAVEEN\\AppData\\Local\\Google\\Chrome\\User Data")
driver.load_page("https://twitter.com/home", 60)
driver.screenshot(filename="Tbl",des_folder="C:\\Users\\NAVEEN\\Pictures\\Saved Pictures",custom_width=1600)
driver.close()

