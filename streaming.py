import random
import time 
import selenium
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from seleniumwire import webdriver
import threading
from selenium import webdriver
import queue
from pyfiglet import Figlet
from colorama import Fore, Back, Style


custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Legendary Streamer'))
print(rf"""{Fore.RED}                                                      v1
                                                    by RuvenBeck   
{Style.RESET_ALL}
""")

lock = threading.Lock()


with open('C:/Coding/Python/Music-Streaming/proxies.txt', 'r') as f:
    proxies = f.read().splitlines()
chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % proxies[0])
chrome_options.add_argument('--disable-webrtc')
chrome_options.add_argument('--start-maximized')

with open('C:/Coding/Python/Music-Streaming/Playlist.txt', 'r') as p:
    playlist_urls = p.readlines()


def worker(q, chrome_options,):

    while True:
        line = q.get()
        if line is None:
            break
        parts = line.split(":", 1)
        email = parts[0]
        password = parts[1].strip()
        print("Email:", email, "Password:", password)
        # Hier können weitere Aktionen mit der E-Mail und dem Passwort durchgeführt werden

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://accounts.spotify.com/de/login?continue=https%3A%2F%2Fopen.spotify.com%2F__noul__%3Fl2l%3D1%26nd%3D1&_locale=de-DE')

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'login-username'))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-password'))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'login-button'))).click()

        time.sleep(5)

        #PopUps entfernen
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div/div[2]/button[2]'))).click()

        except:
            pass

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()

        except:
            pass

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div/div[2]/button[2]'))).click()

        except: 
            pass

        #Die Playlist versuchen an zu wählen
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'AINMAUImkAYJd4ertQxy'))).click()

        #Die Playlist manuel suchen
        except:    
            playlist_url = random.choice(playlist_urls)        
            driver.get(playlist_url)

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button-sc-qlcn5g-0 jqMzOG'))).click()
        except:
            pass

        #Loop und Shuffle an machen
        loopactive = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR')))
        shuffleactive = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'KVKoQ3u4JpKTvSSFtd6J')))

        if loopactive.get_attribute("aria-checked") == "true":
            print("Loop was set")
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()

        if loopactive.get_attribute("aria-checked") == "mixed":
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()
            time.sleep(0.5)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()
            print("Permanent loop to loop.")

        else:
            pass

        if shuffleactive.get_attribute("aria-checked") == "true":
            print("Shuffle already active")
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'KVKoQ3u4JpKTvSSFtd6J'))).click()

        count = 0

        while True:
            count += 1


            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mnipjT4SLDMgwiDCEnRC'))).click()


            print(f"The song was {count} time streamed!")

            if count == 1000:
                driver.quit()
                break

            start_time = time.time()

            time.sleep(35 + 35 *random.random())

            end_time = time.time()
            duration = end_time - start_time

            print(f"The song was played {duration} seconds.")
        q.task_done()


q = queue.Queue()

# Zeilen aus der Textdatei in die Queue einfügen
with open('combo.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        q.put(line)


with open('combo.txt') as f:
    anzahl_zeilen = sum(1 for line in f)

anzahl_threads = anzahl_zeilen

# Threads erstellen
threads = []
for i in range(15):
    t = threading.Thread(target=worker, args=(q, chrome_options))
    threads.append(t)
    t.start()
    time.sleep(8)

# Warten, bis alle Zeilen abgearbeitet sind
q.join()

# Alle Threads beenden
for i in range(15):
    q.put(None)
for t in threads:
    t.join()

