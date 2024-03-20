import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_facebook_with_profile(profile_path, chrome_driver_path):
    # Chrome options ko setup karein
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=" + profile_path)

    # Chrome WebDriver ka istemal karein
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    # Facebook open karein
    driver.get("https://facebook.com")

    # 8 minutes ke liye wait karein
    time.sleep(8 * 60)

    # WebDriver ko band karein
    driver.quit()

if __name__ == "__main__":
    # Terminal se profile path input lein
    profile_path = "C:/Users/user/AppData/Local/Google/Chrome/User Data/Profile 19"
    chrome_driver_path = input("Enter your Chrome WebDriver path: ")

    # Facebook open karein
    open_facebook_with_profile(profile_path, chrome_driver_path)

