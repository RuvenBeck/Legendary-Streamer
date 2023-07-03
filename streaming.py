import random
import time 
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import threading
from selenium import webdriver
import queue
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import json


custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Legendary Streamer'))
print(rf"""{Fore.RED}                                                      v1
                                                    by RuvenBeck   
{Style.RESET_ALL}
""")

gesamte_streams_lock = threading.Lock()


with open('proxies.txt', 'r') as f:
    proxies = f.read().splitlines()

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--disable-webrtc')
chrome_options.add_argument('--start-maximized')

with open('Playlist.txt', 'r') as p:
    playlist_urls = p.readlines()
    random.shuffle(playlist_urls)


# Lese die Konfigurationsdatei
with open('config.json', 'r') as f:
    config = json.load(f)

# Überprüfe, ob song_titles aktiviert oder deaktiviert ist
if config["song_titles"] == True:
    use_song_titles = True
else:
    use_song_titles = False


gesamte_streams = 0


def worker(q, chrome_options,):

    while True:
        global gesamte_streams
        line = q.get()
        if line is None:
            break
        parts = line.split(":", 1)
        email = parts[0]
        password = parts[1].strip()
        random_proxy = random.choice(proxies)
        chrome_options.add_argument('--proxy-server=%s' % random_proxy)
        print("Email:", email, "Password:", password, "Proxy:", random_proxy)
        # Hier können weitere Aktionen mit der E-Mail und dem Passwort durchgeführt werden

        chrome_driver_path = "chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
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
            playlist_url = random.choice(playlist_urls)        
            driver.get(playlist_url)

        #Die Playlist manuel suchen
        except:    
            playlist_url = random.choice(playlist_urls)        
            driver.get(playlist_url)

        #Playlist abspielen
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.ZQftYELq0aOsg6tPbVbV.WIPpgUp9J37Dwd0ZJnv0 > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button > span'))).click()
        except:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.ZQftYELq0aOsg6tPbVbV.WIPpgUp9J37Dwd0ZJnv0 > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button > span'))).click()

        time.sleep(2)

        #Playlist abspielen website bug fix
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.ZQftYELq0aOsg6tPbVbV.WIPpgUp9J37Dwd0ZJnv0 > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button > span'))).click()
        except:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.ZQftYELq0aOsg6tPbVbV.WIPpgUp9J37Dwd0ZJnv0 > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button > span'))).click()


        #Loop und Shuffle an machen
        loopactive = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR')))
        shuffleactive = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'KVKoQ3u4JpKTvSSFtd6J')))

        if loopactive.get_attribute("aria-checked") == "true":
            print("Loop Bereits aktiviert")
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()

        if loopactive.get_attribute("aria-checked") == "mixed":
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()
            time.sleep(0.5)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()
            print("Dauerhafter-Loop auf Loop gestellt.")

        else:
            pass

        if shuffleactive.get_attribute("aria-checked") == "true":
            print("Shuffle bereits aktiviert")
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'KVKoQ3u4JpKTvSSFtd6J'))).click()


        #Check ob die ausgewählten sachen auch wirklich true sind:
        if loopactive.get_attribute("aria-checked") == "false":
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Vz6yjzttS0YlLcwrkoUR'))).click()
        else:
            pass

        if shuffleactive.get_attribute("aria-checked") == "false":
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'KVKoQ3u4JpKTvSSFtd6J'))).click()
        else:  
            pass

        stream_counts = {}
        song_titles = []


        while True:
        

            gesamte_streams += 1

            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mnipjT4SLDMgwiDCEnRC'))).click()


            print(f"Die Songs wurden {Fore.GREEN}{gesamte_streams}{Fore.RESET} mal gestreamt!")
            print(f"")
            print(f"---------------------------------------------------------------------------")
            print(f"")

            title_of_current_song = driver.find_element(By.CSS_SELECTOR, '#main > div > div.ZQftYELq0aOsg6tPbVbV.WIPpgUp9J37Dwd0ZJnv0 > div.Root__now-playing-bar > footer > div > div.OgkbKIVYE_mrNpYESylB > div > div.j96cpCtZAIdqxcDrYHPI.ZcNcu7WZgOAz_Mkcoff3 > div.Q_174taY6n64ZGC3GsKj > div > div > div > div').text

            if use_song_titles:
                song_title = driver.find_element(By.CSS_SELECTOR, '#main > div > div.ZQftYELq0aOsg6tPbVbV.WIPpgUp9J37Dwd0ZJnv0 > div.Root__now-playing-bar > footer > div > div.OgkbKIVYE_mrNpYESylB > div > div.j96cpCtZAIdqxcDrYHPI.ZcNcu7WZgOAz_Mkcoff3 > div.Q_174taY6n64ZGC3GsKj > div > div > div > div').text

                # Aktualisiere die Anzahl der Streams pro Song
                if song_title not in song_titles:
                    song_titles.append(song_title)
                    stream_counts[song_title] = 1
                    print(f"Der Song '{Fore.LIGHTYELLOW_EX}{song_title}{Fore.RESET}' wurde {stream_counts[song_title]} mal gestreamt!")
                else:
                    stream_counts[song_title] += 1
            else:
                song_title = None

               
            if gesamte_streams == 15000:
                driver.quit()
                break
            else:
                if stream_counts == 15000:
                    driver.quit()
                    break


            start_time = time.time()

            time.sleep(35 + 35 *random.random())

            end_time = time.time()
            duration = end_time - start_time
            rounded_duration = round(duration, 2)

            print(f"{Fore.RED}{title_of_current_song}{Fore.RESET} wurde {Fore.RED}{rounded_duration}{Fore.RESET} Sekunden gespielt.")
        
        q.task_done()



q = queue.Queue()

# Zeilen aus der Textdatei in die Queue einfügen
with open('combo.txt', 'r') as file:
    lines = file.readlines()
    random.shuffle(lines)
    for line in lines:
        q.put(line)


with open('combo.txt') as f:
    anzahl_zeilen = sum(1 for line in f)

anzahl_threads = anzahl_zeilen



#Printing of all the inputs
print(f"{Fore.LIGHTYELLOW_EX}{len(proxies)}{Fore.RESET} Proxies are loaded")
print(f"{Fore.LIGHTYELLOW_EX}{len(playlist_urls)}{Fore.RESET} Playlists are loaded")
print(f"{Fore.LIGHTYELLOW_EX}{len(lines)}{Fore.RESET} Combos are loaded")



# Threads erstellen
threads = []
for i in range(anzahl_threads):
    t = threading.Thread(target=worker, args=(q, chrome_options))
    threads.append(t)
    t.start()
    time.sleep(15)

# Warten, bis alle Zeilen abgearbeitet sind
q.join()

# Alle Threads beenden
for i in range(anzahl_threads):
    q.put(None)
for t in threads:
    t.join()
