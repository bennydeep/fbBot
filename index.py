import xml.etree.ElementTree as ET
from pathlib import Path
from time import sleep

import json
import os
import pyautogui
import pyperclip
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

sleep(3)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def idezet():
    r = requests.get(
        'https://api.citatum.hu/idezet.php?f=apitest&j=957811486d3132fe353d18e116cb17c6&kat=%C9let&rendez=veletlen')
    root = ET.fromstring(r.content)
    idezet = root[0][0].text + " - " + root[0][1].text
    return (idezet)


def idezetSP():
    r = requests.get(
        'https://api.citatum.hu/idezet.php?f=apitest&j=957811486d3132fe353d18e116cb17c6&szerzo=szabo+peter&rendez=veletlen')
    root = ET.fromstring(r.content)
    idezet = root[0][0].text + " - A Mester Maga"
    return (idezet)

def idezetteszt(kat):
    r = requests.get(
        'https://api.citatum.hu/idezet.php?f=apitest&j=957811486d3132fe353d18e116cb17c6&kat={}&rendez=veletlen'
            .format(kat))
    root = ET.fromstring(r.content)
    idezet = "'" + root[0][0].text + "'" + " - " + root[0][1].text + " (Sent by PyCharm)"
    return (idezet)


class FbBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get(os.environ['whotospam'])

        sleep(2)
        self.driver.maximize_window()
        wait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Az összes elfogadása']"))).click()
        sleep(1)

        self.driver.find_element_by_xpath("//input[@name=\"email\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@name="login"]') \
            .click()
        sleep(5)



my_bot = FbBot(username=os.environ['fbusername'], pw=os.environ['fbpw'])

pyperclip.copy(idezetteszt('Motiv%E1ci%F3'))
sleep(0.25)
pyautogui.hotkey("ctrl", "v")
sleep(0.25)
pyautogui.press("enter")
sleep(0.25)

