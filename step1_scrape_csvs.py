###################################################################################################
# STEP 1: DOWNLOAD TAGS OVER TIME CSVS FOR ALL GAMES IN 2018
###################################################################################################
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# "steamspy_2018_games_clean.csv" is a list of all 2018 games listed on Steamspy
# I extracted the data from the page source at "https://steamspy.com/year/2018"
# gamez_df = pd.read_csv("steamspy_2018_games_clean.csv")
# # THIS REMOVES ANY CHINESE GAMES
# gamez_df = gamez_df.loc[~gamez_df.app_name.str.contains("<U+"),:]
# gamez_df.to_csv("steamspy_2018_games_clean_no_ch.csv")

gamez_df = pd.read_csv("steamspy_2018_games_clean_no_ch.csv")

# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument("user-data-dir=C://Users/gaoan/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=chrome_options)

# UNCOMMENT THIS IF YOU GET LOGGED OUT (if credentials need to be renewed)
# driver.get('https://steamspy.com/login')
# time.sleep(220)  # Time to enter credentials

# Start the stopwatch
start = time.time()

#Already done
#0-140
#140-200
#201-275
#275-426
#426-577
#577-800
#801-895
#894-919
#919-1045
#1045-1194

# Running now....
#1195-

start_num = 1195

# HERE YOU CAN CHOOSE WHAT RANGE OF GAMES YOU WANT TO SCRAPE DATA FOR
gamez = gamez_df.loc[start_num:start_num+200, "app_id"].tolist()

# OPEN A LOGFILE TO TRACK ANY GAMES THAT DIDN'T GET SCRAPED
logf = open("failed_games.txt", "w")

counter = start_num

# ITERATE THROUGH THE LIST AND GET DOWNLOAD THE CSV TO THE DOWNLOADS FOLDER
for current_app_id in gamez:

    print(f"trying game #{counter}")
    counter+=1
    try:
        first_game_url = f"https://steamspy.com/app/{current_app_id}#tab-tagstime"
        driver.get(first_game_url)
        time.sleep(12)

        driver.find_element(By.XPATH, '//*[@id="amch-tagstime"]/div/div[2]/ul/li/a').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="amch-tagstime"]/div/div[2]/ul/li/ul/li[2]/a/span').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="amch-tagstime"]/div/div[2]/ul/li/ul/li[2]/ul/li[1]/a').click()
        
        print(f"game #{current_app_id} was successful")
        # THIS MAY BE NECESSARY IF THE SAVE FILE DIALOG BOX COMES UP
        # time.sleep(10)
        # import keyboard
        # keyboard.press_and_release('enter')
        
        time.sleep(1)
    
    except Exception as e:
        print(f"game #{current_app_id} failed")
        logf.write(f"{current_app_id}\n")

driver.quit()

# LOG HOW LONG IT TOOK
print('It took {0:0.1f} seconds'.format(time.time() - start))





# DO SOMETHING HERE TO CHECK WHAT THE LAST SUCCESSFULLY SCRAPED GAME WAS
# YOU NEED THE ID OF THE GAME WHERE YOU WANT TO START AGAIN FROM
# YOU ALSO NEED A LIST OF ANY GAMES THAT WERE UNSUCCESSFUL












###################################################################################################
# UNUSED CODE

# import time
# import keyboard
# from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_argument("user-data-dir=chrome-data")

# #chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

# start_url = "https://steamspy.com/login"
# driver.get(start_url)
# time.sleep(100)

# first_game_url = "https://steamspy.com/app/590380"
# driver.get(first_game_url)

# driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/ul/li[12]/a/span').click()
# time.sleep(10)
# driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[11]/div[2]/div/div[2]/ul/li/ul/li[2]/ul/li[1]/a/span').click()
# time.sleep(5)
# keyboard.press_and_release('enter')
# driver.quit()

#username
# //*[@id="login_form"]/div[1]/input
#pass
# //*[@id="login_form"]/div[2]/input
#captcha
# //*[@id="recaptcha-anchor"]
#print(driver.page_source.encode("utf-8"))
#login button
# /html/body/div[3]/div[2]/div/div[2]/div/div/div/div[1]/form/button
# username = driver.find_element(By.XPATH, '//*[@id="login_form"]/div[1]/input')
# password = driver.find_element(By.XPATH, '//*[@id="login_form"]/div[2]/input')
# captcha = driver.find_element(By.XPATH, '//span[@id="recaptcha-anchor"]')
# login_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[1]/form/button')
# username.send_keys("nsysu")
# time.sleep(5)
# password.send_keys("6d12380383ec")
# time.sleep(5)
# driver.find_element_by_name("captcha").click()
# time.sleep(5)
# driver.find_element_by_name("login_button").click()
# time.sleep(10)

