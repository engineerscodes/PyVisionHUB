from get_ss_dev import Webscraper

driver = Webscraper(chrome_driver_path="C:\\Users\\NAVEEN\Documents\\chromedriver.exe",
                    user_data="C:\\Users\\NAVEEN\\AppData\\Local\\Google\\Chrome\\User Data",
                    download_path="C:\\Users\\NAVEEN\\Pictures\\Saved Pictures")
driver.load_page("https://github.com/engineerscodes/Khonshu", 20)

driver.screenshot(filename="Tbl",custom_width=1600)
#driver.close()
