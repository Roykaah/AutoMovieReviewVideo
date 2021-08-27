from selenium import webdriver
from bs4 import BeautifulSoup
from conf import IMAGES_DIR
import requests
import urllib.request
import time
import sys
import os


def download_images(query, num):
    site = 'https://www.google.com/search?tbm=isch&q=' + query
    driver = webdriver.Firefox(
        executable_path='C:\Drivers_firef\geckodriver.exe')
    driver.get(site)

    i = 0
    while i < 3:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        try:
            driver.find_element_by_xpath(
                "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input"
            ).click()
        except Exception as e:
            pass
        time.sleep(5)
        i += 1
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    img_tags = soup.find_all("img", class_="rg_i")

    count = 0
    for i in img_tags:
        images_path = os.path.join(IMAGES_DIR, f'{count}.jpg')
        try:
            urllib.request.urlretrieve(i['src'], images_path)
            count += 1
        except Exception as e:
            pass
        if count >= num:
            break
