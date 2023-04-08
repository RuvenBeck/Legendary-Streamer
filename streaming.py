import random
import time 
import selenium
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from seleniumwire import webdriver
import pickle

#Combo line wird ausgegeben und anschließend in Password und Email unterteilt. Dies wird dann in die Eingabe später übergeben
with open('C:/Coding/Python/Music-Streaming/combo.txt', 'r') as combopick:
    
    zeile = combopick.readline()
    
random_line = random.choice(zeile)

print(random_line)


with open('C:\Coding\Python\Music-Streaming\combos.txt', 'r') as d:
     
    zeile = d.readline()
    wortliste = zeile.split(":")
    if len(wortliste) > 1:
        password = wortliste[1].strip()
        print(password)
    else: 
        print("Ich konnte kein Password erkennen")

username = f 
password = d

driver = uc.Chrome()

driver.get('https://accounts.spotify.com/de/login?continue=https%3A%2F%2Fopen.spotify.com%2F__noul__%3Fl2l%3D1%26nd%3D1&_locale=de-DE')
driver.maximize_window()
time.sleep(1000)
driver.find_element(By.ID, 'login-username').send_keys(username)
time.sleep(2)
driver.find_element(By.ID, 'login-password').send_keys(password)
driver.find_element(By.ID,'login-button').click()
time.sleep(10)
#skip = time.sleep(random.randint(33, 100))


#cookies = driver.get_cookies()
#pickle.dump(cookies, open("cookies.pkl", "wb"))