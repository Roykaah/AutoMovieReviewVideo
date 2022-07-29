import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys


def get_letterboxd_data():
    driver = webdriver.Firefox(
        executable_path='C:\Drivers_firef\geckodriver.exe')

    driver.get('https://letterboxd.com/roykaah/films/diary/')
    element = driver.find_elements_by_class_name('diary-entry-row')

    infos = element[0].text.splitlines()
    name = infos[3][:-5]
    year = infos[3][-4:]
    rating = infos[4]
    rating = rating.count('½') + rating.count('★') * 2

    primeiro_filme = element[0].find_elements_by_class_name('td-film-details')
    details = primeiro_filme[0].find_elements_by_class_name('react-component')
    ultimo_filme_logado = details[0].get_attribute('data-film-link')
    driver.get("https://letterboxd.com" + ultimo_filme_logado)
    crew = driver.find_element_by_id('tab-crew')
    director = crew.find_element_by_xpath('div[1]/p/a').get_attribute(
        "textContent")
    return {
        'title': name,
        'year': year,
        'my_rating': rating,
        "director": director,
    }
