import requests
import warnings
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-tu', '--twitch_username', default='zycromerz')
parser.add_argument('-pc', '--proxy_count', default=10, type=int)
parser.add_argument('-tl', '--total_loop', default=1, type=int)


args = parser.parse_args()

warnings.filterwarnings("ignore", category=DeprecationWarning)

def check_for_updates():
    # try:
    #     r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/version.txt")
    #     remote_version = r.content.decode('utf-8').strip()
    #     local_version = open('version.txt', 'r').read().strip()
    #     if remote_version != local_version:
    #         print("A new version is available. Please download the latest version from GitHub.")
    #         time.sleep(3)
    #         return False
    #     return True
    # except:
    #     return True
    return True


def main():
    if not check_for_updates():
        return
def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")

def set_stream_quality(driver, quality):
    if quality == "yes":
        element_xpath = "//div[@data-a-target='player-overlay-click-handler']"

        element = driver.find_element(By.XPATH, element_xpath)

        actions = ActionChains(driver)

        actions.move_to_element(element).perform()

        settings_button = driver.find_element(By.XPATH, "//button[@aria-label='Settings']")
        settings_button.click()

        wait = WebDriverWait(driver, 10)
        quality_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Quality']")))
        quality_option.click()

        time.sleep(15)

        quality_levels = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'video-quality-option')]")))

        target_quality = "160p"
        for level in quality_levels:
            if target_quality in level.text:
                level.click()
                break

def main():
    if not check_for_updates():
        return
    print_announcement()
    

    # os.system(f"title Kichi779 - Twitch Viewer Bot @kichi#0779 ")

    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/AFV9m8UXuT    
                             Github  github.com/kichi779    """)))
    announcement = print_announcement()
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")
    print("")
    

    # proxy_servers = {
    #     1: "https://www.blockaway.net",
    #     2: "https://www.croxyproxy.com",
    #     3: "https://www.croxyproxy.rocks",
    #     4: "https://www.croxy.network",
    #     5: "https://www.croxy.org",
    #     6: "https://www.youtubeunblocked.live",
    #     7: "https://www.croxyproxy.net",
    # }

    # # Selecting proxy server
    # print(Colors.green,"Proxy Server 1 Is Recommended")
    # print(Colorate.Vertical(Colors.green_to_blue,"Please select a proxy server(1,2,3..):"))
    # for i in range(1, 7):
    #     print(Colorate.Vertical(Colors.red_to_blue,f"Proxy Server {i}"))
    # proxy_choice = int(input("> "))
    # proxy_url = proxy_servers.get(proxy_choice)

    proxy_servers = [
        "https://www.blockaway.net",
        "https://www.blockaway.net",
        "https://www.blockaway.net",
        "https://www.croxyproxy.com",
        "https://www.croxyproxy.rocks",
        "https://www.croxy.network",
        "https://www.croxy.org",
        "https://www.youtubeunblocked.live",
        "https://www.croxyproxy.net",
        'https://proxysite.pro',
        'https://proxysite.site',
        'https://proxyium.com',
    ]
    def selectRandom(proxy_servers):
        return random.choice(proxy_servers)

    proxy_url = selectRandom(proxy_servers)

    twitch_username = args.twitch_username
    proxy_count = args.proxy_count
    os.system("cls")
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/AFV9m8UXuT    
                             Github  github.com/kichi779    """)))
    print('')
    print('')
    print(Colors.red, Center.XCenter("Viewers Send. Please don't hurry. If the viewers does not arrive, turn it off and on and do the same operations"))


    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    try:
        with open('chrome-path.txt', 'r') as file:
            lines = file.read().rstrip()
            if lines:
                chrome_path = lines
    except:
        pass

    if 'exe' not in chrome_path:
        driver_path = 'chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)

    for i in range(proxy_count):
        random_proxy_url = selectRandom(proxy_servers)  # Select a random proxy server for this tab
        driver.execute_script("window.open('" + random_proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(random_proxy_url)
        time.sleep(10)

        if 'proxysite.site' in random_proxy_url or 'proxyium.com' in random_proxy_url:
            text_box = driver.find_element(By.NAME, 'url')
        else:
            text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    for i in range(4):
        time.sleep(30)
        try:
            set_stream_quality(driver, "yes")
        except:
            pass

    if args.total_loop > 1:
        LoopNumber = 1
        while LoopNumber < args.total_loop:
            print('loop a')
            time.sleep(60)
            LoopNumber = LoopNumber + 1
    else:
        LoopNumber='1'
        while LoopNumber == '1':
            print('loop b')
            time.sleep(60)
            try:
                with open('loop.txt', 'r') as file:
                    LoopNumber = file.read().rstrip()
            except:
                pass
    driver.quit()


if __name__ == '__main__':
    main()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
