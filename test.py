from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


URL = "https://www.tiktok.com/@dayo_dayo34/photo/7394169229882215686"

def download_tiktok_video(url):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    try:
        driver.get(url)

        video_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "swiper-wrapper"))
        )

        video_url = video_element.get_attribute('outerHTML')

        print(video_url)
    finally:
        driver.quit()

download_tiktok_video(URL)