import requests
from bs4 import BeautifulSoup, SoupStrainer
# import scrapy
import tempfile
from selenium import webdriver
from io import BytesIO
from PIL import Image
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import time
import os
from selenium_stealth import stealth

URL = "https://www.tiktok.com/@dayo_dayo34/photo/7394169229882215686"
URL2 = "https://www.tiktok.com/@pred.encounters/video/7377548736496454945"
URL3 = "https://www.tiktok.com/@leo_naard/photo/7392829857794641157"
# page = requests.get(URL2)
# # print(page.content)

# soup = BeautifulSoup(page.content, "html.parser")
# only_div_tags = SoupStrainer("div")
# result = soup.find("video")
# print(result)

def download_file(url, local_filename):
    response = requests.get(url)
    response.raise_for_status()


    with open(local_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk: 
                file.write(chunk)
    return local_filename

def createSlideshow(audio, image_files, output_file, duration_per_image, temp_dir):
    try:
        audio_temp_path = os.path.join(temp_dir, "audio.mp3")
        audio_content = download_file(audio, audio_temp_path)
        audio = AudioFileClip(audio_content)
        print('me audio worked')

        clips = []

        for index, image_file in enumerate(image_files):
            filename = os.path.join(temp_dir, f'image_{index}.jpeg')
            image_content = download_file(image_file, filename)
            # image = Image.open(image_content)
            clip = ImageClip(image_content).set_duration(duration_per_image)
            clips.append(clip)


        video = concatenate_videoclips(clips, method="compose")

        audio = audio.audio_loop(duration=video.duration)

        video = video.set_audio(audio)

        print(audio, 'audio')
        print(clips, 'clips')
        print(video)

        video.write_videofile(output_file, codec="libx264", fps=24, audio_codec="libvorbis")

    except Exception as e:
        print(e)

    finally:
        os.remove("audio.mp3")
        for index in range(len(image_files)):
            os.remove(f'image_{index}.jpeg')


def download(url):
    with tempfile.TemporaryDirectory() as temp_dir:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')

        # options.add_argument("start-maximized")

# options.add_argument("--headless")

        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options)
        # stealth(driver,
        #     languages=["en-US", "en"],
        #     vendor="Google Inc.",
        #     platform="Win32",
        #     webgl_vendor="Intel Inc.",
        #     renderer="Intel Iris OpenGL Engine",
        #     fix_hairline=True,
        # )

        driver.get(url)

        # time.sleep(10)

        imageLinks = []
        audio = None

        # found = Falseß
        # while(found == False):

        try: 
            # print(audioElement)
            # swipers = driver.find_element(By.CLASS_NAME, 'swiper-wrapper')
            swipers = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'swiper-wrapper'))
            )
            print('found swiper wrapper')
            images = swipers.find_elements(By.TAG_NAME, 'img')
            # print(images)
            audioElement = driver.find_element(By.TAG_NAME, "audio").get_attribute('src')
            # print('found images in swiper wrapper')
            # print(swipers.get_attribute('outerHTML'))
            for image in images:
                image_link = image.get_attribute('src')
                # print(image_link)
                # print('printing each image link')
                if image_link not in imageLinks:
                    # if 'p77' not in image_link:
                    imageLinks.append(image_link)
            print(len(imageLinks))
            print(imageLinks)
            print(audioElement)

            createSlideshow(audioElement, imageLinks, f'slideshow_{hash(url)}.mp4', 2.5, temp_dir)
            # found = True
            # swiper = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'swiper-wrapper')))
            # print(swiper.__getattribute__('outerHTML'))
            # print(swiper.get_attribute('outerHTML'))
        except Exception as e:
            # print(e)
            # print("something went wrong", e)
            # found = False
            # print('retrying now....')
            return
            # driver.quit()

            # return
        
        # driver.quit()

download(URL3)
# print(None)

# options = webdriver.ChromeOptions()
#         # options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)

# driver.get(URL3)