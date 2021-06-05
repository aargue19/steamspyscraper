import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


gamez_df = pd.read_csv("steamspy_2017_games_clean.csv")                  #THIS IS FOR 2017 GAMES WITH CHINESE NAME GAMES STILL TO BE REMOVED USING CODE BELOW
# THIS REMOVES ANY CHINESE GAMES
# gamez_df = gamez_df.loc[~gamez_df.app_name.str.contains("<U+"),:]
# gamez_df.to_csv("steamspy_2017_game_ids_clean_no_ch.csv")

# "steamspy_2018_games_clean.csv" is a list of all 2018 games listed on Steamspy
# I extracted the data from the page source at "https://steamspy.com/year/2018"
# gamez_df = pd.read_csv("steamspy_2018_games_clean_no_ch.csv")         #THIS IS FOR 2018 GAMES WITH CHINESE NAME GAMES ALREADY REMOVED


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
# time.sleep(60)  # Time to enter credentials

start_num = 0

# HERE YOU CAN CHOOSE WHAT RANGE OF GAMES YOU WANT TO SCRAPE DATA FOR
gamez = gamez_df.loc[start_num:start_num+1, "app_id"].tolist()


for current_app_id in gamez:

    first_game_url = f"https://steamspy.com/app/{int(current_app_id)}#tab-tagstime"
    driver.get(first_game_url)


###############################################################################################################
# GET ADDITIONAL DATA FROM PAGE 

    # GET DIV
    # /html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]
    info_div = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]")

    href_elems = info_div.find_elements_by_xpath("//a[@href]")

    # for elem in href_elems:
    #     print(elem)
    #     print(elem.get_attribute("href"))

    current_href_list = []
    for elem in href_elems:
        current_href_list.append(elem.get_attribute("href"))

    all_devs_list=[]

    only_devs_list=[]
    for href in current_href_list:
        if "/dev/" in str(href):
            only_devs_list.append(re.findall(r'(?<=dev\/)(.*)', str(href))[0])

    #FOR SOME REASON THERE ARE THE SAME N DEVS AT THE START SO GOTTA GET RID OF THEM
    only_devs_list = only_devs_list[-2:]

    all_devs_list.append(only_devs_list)

    #LANGUAGES

    all_langs_list = []
    only_lang_list=[]
    for href in current_href_list:
        if "/language/" in str(href):
            only_lang_list.append(re.findall(r'(?<=language\/)(.*)', str(href))[0])

    #print(only_lang_list)

    final_lang_list = ['','','','','','','','','','','','','','','','','','','',''] # 20 LANGUAGES SHOULD BE ENOUGH
    
    #FOR SOME REASON THERE ARE THE SAME 18 LANGUAGES AT THE START SO GOTTA GET RID OF THEM
    count = 0
    for i in range(18,len(only_lang_list)):
        if only_lang_list[i] is not None:
            final_lang_list[count] = only_lang_list[i]
            count+=1

    all_langs_list.append(final_lang_list)
    #print(final_lang_list)

    #TAGS
    #MAKE A LIST OF ALL THE TEXT ASSOCIATED WITH LINKS TO MATCH UP THE COUNTS (WRITTEN AS TEXT) WITH THE TAG LABELS (AS LINKS) 

    only_tags_list=[]
    all_tags_list = []


    for href in current_href_list:
        if "/tag/" in str(href):
            only_tags_list.append(re.findall(r'(?<=tag\/)(.*)', str(href)))

    final_tags_list = ['','','','','','','','','','','','','','','','','','','',''] # 20 TAGS MAX


    #FOR SOME REASON THERE ARE THE SAME 23 tags AT THE START SO GOTTA GET RID OF THEM
    count = 0
    for i in range(23,len(only_tags_list)):
        if only_tags_list[i] is not None:
            final_tags_list[count] = only_tags_list[i][0]
            count+=1

    all_tags_list.append(final_tags_list)

    # print(only_tags_list)
    # print(final_tags_list)

    # GET COUNTS FOR TAGS

    all_tags_and_counts = []
    tag_counts_list = []
    p_text = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]")

    tag_counts_list = re.findall(r'(?<=\()\d*(?=\))', p_text.text)

    tags_and_counts = [['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0],
                        ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0]]

    counter = 0
    for i in range(len(final_tags_list)):
        if len(final_tags_list[i]) > 0:
            tags_and_counts[counter] = [final_tags_list[i], int(str(tag_counts_list[i]))]
            counter+=1

    all_tags_and_counts.append(tags_and_counts)

    # print(tags_and_counts)

    #GET SCORES
    old_userscore_list = []
    old_userscore =  re.findall(r'(?<=Old userscore:)(.*)(?=Metascore)', p_text.text)
    if len(old_userscore) > 0:
        old_userscore_list.append(old_userscore)
    else:
        old_userscore_list.append([''])

    metascore_list = []
    metascore =  re.findall(r'(?<=Metascore:)(.*)', p_text.text)
    if len(metascore) > 0:
        metascore_list.append(metascore)
    else:
        metascore_list.append([''])

    #GET GENRES
    genres_list = []
    genres =  re.findall(r'(?<=Category:)(.*)', p_text.text)
    genres_list.append(genres)

    # GET FOLLOWERS
    followers_list = []
    followers =  re.findall(r'(?<=Followers: )(.*)', p_text.text)
    followers_list.append(followers)

    # GET PLAYTIME
    playtime_list=[]
    playtime = re.findall(r'(?<=Playtime total: )(.*)', p_text.text)
    playtime_list.append(playtime)

    # GET YOUTUBE STATS
    yt_list=[]
    yt_stats = re.findall(r'(?<=YouTube stats: )(.*)', p_text.text)
    yt_list.append(yt_stats)

    # GET CCU STATS
    ccu_list = []
    ccu_stats = re.findall(r'(?<=Peak concurrent players yesterday: )(.*)', p_text.text)
    ccu_list.append(ccu_stats)


# PREPARE ROWS FOR DF
all_rows=[]

for i in range(len(gamez[0:1])):
    current_row = [int(i), 
                    old_userscore_list[i][0], 
                    metascore_list[i][0],
                    genres_list[i][0],
                    followers_list[i][0], 
                    playtime_list[i][0],
                    yt_list[i][0], 
                    ccu_list[i][0], 

                    all_devs_list[i][0],
                    all_devs_list[i][1],

                    all_langs_list[i][0],
                    all_langs_list[i][1],
                    all_langs_list[i][2],
                    all_langs_list[i][3],
                    all_langs_list[i][4],
                    all_langs_list[i][5],
                    all_langs_list[i][6],
                    all_langs_list[i][7],
                    all_langs_list[i][8],
                    all_langs_list[i][9],
                    all_langs_list[i][10],
                    all_langs_list[i][11],
                    all_langs_list[i][12],
                    all_langs_list[i][13],
                    all_langs_list[i][14],
                    all_langs_list[i][15],
                    all_langs_list[i][16],
                    all_langs_list[i][17],
                    all_langs_list[i][18],
                    all_langs_list[i][19],

                    all_tags_and_counts[i][0][0], all_tags_and_counts[i][0][1],
                    all_tags_and_counts[i][1][0], all_tags_and_counts[i][1][1],
                    all_tags_and_counts[i][2][0], all_tags_and_counts[i][2][1],
                    all_tags_and_counts[i][3][0], all_tags_and_counts[i][3][1],
                    all_tags_and_counts[i][4][0], all_tags_and_counts[i][4][1],
                    all_tags_and_counts[i][5][0], all_tags_and_counts[i][5][1],
                    all_tags_and_counts[i][6][0], all_tags_and_counts[i][6][1],
                    all_tags_and_counts[i][7][0], all_tags_and_counts[i][7][1],
                    all_tags_and_counts[i][8][0], all_tags_and_counts[i][8][1],
                    all_tags_and_counts[i][9][0], all_tags_and_counts[i][9][1],
                    all_tags_and_counts[i][10][0], all_tags_and_counts[i][10][1],
                    all_tags_and_counts[i][11][0], all_tags_and_counts[i][11][1],
                    all_tags_and_counts[i][12][0], all_tags_and_counts[i][12][1],
                    all_tags_and_counts[i][13][0], all_tags_and_counts[i][13][1],
                    all_tags_and_counts[i][14][0], all_tags_and_counts[i][14][1],
                    all_tags_and_counts[i][15][0], all_tags_and_counts[i][15][1],
                    all_tags_and_counts[i][16][0], all_tags_and_counts[i][16][1],
                    all_tags_and_counts[i][17][0], all_tags_and_counts[i][17][1],
                    all_tags_and_counts[i][18][0], all_tags_and_counts[i][18][1],
                    all_tags_and_counts[i][19][0], all_tags_and_counts[i][19][1]]

    all_rows.append(current_row)

df = pd.DataFrame(all_rows, columns = ['app_id_scrap', 
                                       'old_usrscore_scrap', 
                                       'metascore_scrap',
                                       'genres_scrap',
                                       'followers_scrap',
                                       'playtime_scrap',
                                       'youtube_scrap',
                                       'ccu_scrap',
                                       'developer_scrap',
                                       'publisher_scrap',

                                       'lang_1_scrap',
                                       'lang_2_scrap',
                                       'lang_3_scrap',
                                       'lang_4_scrap',
                                       'lang_5_scrap',
                                       'lang_6_scrap',
                                       'lang_7_scrap',
                                       'lang_8_scrap',
                                       'lang_9_scrap',
                                       'lang_10_scrap',
                                       'lang_11_scrap',
                                       'lang_12_scrap',
                                       'lang_13_scrap',
                                       'lang_14_scrap',
                                       'lang_15_scrap',
                                       'lang_16_scrap',
                                       'lang_17_scrap',
                                       'lang_18_scrap',
                                       'lang_19_scrap',
                                       'lang_20_scrap',

                                       'tag_1_scrap', 'tag_1_count',
                                       'tag_2_scrap', 'tag_2_count',
                                       'tag_3_scrap', 'tag_3_count',
                                       'tag_4_scrap', 'tag_4_count',
                                       'tag_5_scrap', 'tag_5_count',
                                       'tag_6_scrap', 'tag_6_count',
                                       'tag_7_scrap', 'tag_7_count',
                                       'tag_8_scrap', 'tag_8_count',
                                       'tag_9_scrap', 'tag_9_count',
                                       'tag_10_scrap', 'tag_10_count',
                                       'tag_11_scrap', 'tag_11_count',
                                       'tag_12_scrap', 'tag_12_count',
                                       'tag_13_scrap', 'tag_13_count',
                                       'tag_14_scrap', 'tag_14_count',
                                       'tag_15_scrap', 'tag_15_count',
                                       'tag_16_scrap', 'tag_16_count',
                                       'tag_17_scrap', 'tag_17_count',
                                       'tag_18_scrap', 'tag_18_count',
                                       'tag_19_scrap', 'tag_19_count',
                                       'tag_20_scrap', 'tag_20_count'])

df.to_csv("test222222.csv", index=False)
################################################################################################


    