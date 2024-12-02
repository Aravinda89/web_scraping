# Install selenium
# !pip install selenium# Import the libraries.

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time# Install the chrome web driver from selenium.

# !apt-get update
# !apt install chromium-chromedriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('webdriver//chromedriver',chrome_options=chrome_options)# Create url variable containing the webpage for a Google image search.

url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")# Launch the browser and open the given url in the webdriver.
# url = ("https://www.google.com/search?q={s}&tbm=isch")

driver.get(url.format(s='car'))# Scroll down the body of the web page and load the images.
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)# Find the images.

# imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'YQ4gaf')]")# Access and store the scr list of image url's.
# imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'sFlh5c FyHeAf')]")# Access and store the scr list of image url's.

# imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'YQ4gaf')]")# Access and store the scr list of image url's.
# imgResults = driver.find_elements(By.XPATH,"//img[contains(@id,'dimg_N9hNZ6KoNIub4-EP94O6iAI')]")# Access and store the scr list of image url's.
imgResults = driver.find_elements(By.XPATH,"//img[contains(@class, 'sFlh5c FyHeAf iPVvYb')]")

src = []
for img in imgResults:
    src.append(img.get_attribute('src'))# Retrieve and download the images.

for i in range(10):
    urllib.request.urlretrieve(str(src[i]),"sample_data/dogs{}.jpg".format(i))