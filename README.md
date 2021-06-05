1. Get all possible names and codes of Steam tags
- downloaded source from "steamdb.info/tags/" and saved it as "steamdb_tag_codes_raw.txt"
- used "step0_get_tag_codes.py" to create a dataframe of tag codes, names and counts for all ~425 tags
- saved as two column csv file called "tag_codes.csv" with the following columns:
	['tag_code', 'tag_name', 'tag_count']

2. Get list of all games released in 2017
- logged into steamspy.com (this is important b/c some access to data is limited to members)
- downloaded source from "steamspy.com/year/2017" and saved it as 'steamspy_year_2017_games_raw.txt'
- used "step0_get_game_ids_2017.py" to create a dataset of all ~6000 games 
- saved as "steamspy_2017_games_clean.csv" with the following columns:
	['app_num', 'app_name', 'app_id','release_date','price','price_decimal','user_score_meta_score', 'owners','playtime_median','developer','developer2', 'publisher', 'publisher2']

3. Make a list of games that were in early access
- downloaded source from "steamdb.info/tag/493/?all" (the tag associated with early access)
- used regex to clean it up (ctrl+shift+p >> "select all occurances" also useful)
- saved as "ex_early_access_games.csv" with the following columns:
	['#', 'Game', 'Release date', 'Price', 'Score rank(Userscore / Metascore)' , 'Owners', 'Players', 'Playtime (Median)', 'Developer(s)', 'Publisher(s)']

4. Scrape csv files with tags over time data and other data
- logged into steamspy.com (this is important b/c tags over time data is limited to members)
- used "step1_scrape_csvs_info.py" to scrape data from steamspy.com
- script uses headless browser to access the page for every game listed in "steamspy_2017_games_clean.csv" 
- csvs are downloaded individually to "C:/Users/gaoan/Downloads" folder then moved manually into "~/empty_csvs"
- other game info from each page is saved to "steamspy_scraped_data_2017.csv" to be merged later (see #10 below)

5. Remove empty csvs with no tags over time data
- for some games the csvs downloaded from steamspy.com are empty
- used "step02_find_empty_csvs.py" to move the empty csvs to the directory "~/empty_csvs"

6. Merge remaining csvs
- all remaining csvs are put into the directory "~/csvs"
- used "step2_merge_csvs.py" to merge game and tags information for all remaining csvs
- the script uses "tag_names_codes_counts.csv" to create ~425 columns (one for each possible tag)
- data is saved as "step2_result.csv" with the following columns:
	[app_num,app_name,app_id,release_date,price,price_decimal,user_score_meta_score,owners,playtime_median,developer,developer2,publisher,publisher2,
	tag_492, ...., tag_348922, tag_date, tag_other, tag_999999, tag_1694, tag_5144, tag_134316]
- the following tags were removed because they tags don't actually exist or don't contain data:
	['tag_999999', 't6_tag_999999', 'tag_5144', 't6_tag_5144', 'tag_1694', 't6_tag_1694', 'tag_134316', 't6_tag_134316']

7. Create a dataframe of only the earliest record of tags for each game
- used "step3_keep_earliest_6mo_tags.py" to create a dataframe of tag counts at only 2 time points
- games where the earliest record of tags comes after the game's release date are dropped		#### THIS CONDITION MAY BE TOO STRICT AS IT DROPS ABOUT 50% OF GAMES
- the earliest records for each of remaning are saved to a dataset called "step3_earliest_tags.csv"
- the first record of tags after a given time period (currently 6 months) are saved to "step3_tags_after_6_mo.csv"

8. Merge additional data from the steamspy.com api with the dataframe of earliest tags records
- used "step4_merge_api_info.py" to query steamspy api for additional info on each game in "step3_earliest_tags.csv"
- data is saved to "step4_result_earliest_tags.csv" with the folowing columns:
	['app_id','pos_rev_num','neg_rev_num','usr_score','avg_pt_forever','avg_pt_2weeks','initial_price','current_price','ccu',
         'lang_1','lang_2','lang_3','lang_4','lang_5','lang_6','lang_7','lang_8','lang_9','lang_10',
         'genre_1','genre_2','genre_3','genre_4','genre_5','genre_6','genre_7','genre_8','genre_9','genre_10']  

9. Merge the two dataframes at the two time points into one dataframe
- used "step5_merge_t1_t2_tags.py" to merge "step4_result_earliest_tags.csv" and "step3_tags_after_6_mo.csv"
- merged dataframe is saved as "step5_result.csv" with the following 890 columns:
	[app_num_x,app_name_x,app_id,release_date_x,price_x,price_decimal_x,user_score_meta_score_x,owners_x,playtime_median_x,developer_x,developer2_x,publisher_x,publisher2_x,
	pos_rev_num,neg_rev_num,usr_score,avg_pt_forever,avg_pt_2weeks,initial_price,current_price,ccu,
	lang_1,lang_2,lang_3,lang_4,lang_5,lang_6,lang_7,lang_8,lang_9,lang_10,
	genre_1,genre_2,genre_3,genre_4,genre_5,genre_6,genre_7,genre_8,genre_9,genre_10,
	tag_date,tag_492, .... ,tag_348922,tag_other,t6_tag_date,t6_tag_492, .... ,t6_tag_348922,t6_tag_other]

10. Merge the data scraped from the individual game pages on steamspy while downloading csvs
- used "step6_merge_scraped_data.py" to merge "step5_result.csv" with "steamspy_scraped_data_2017.csv"
- merged on the "app_id" column and saved the dataframe as "step6_result.csv" with 967 columns  












##########################
OLD

1. Get all codes for steam tags
- looked at source of "https://steamdb.info/tags/" and used regex to get codes for each tag from links on page
- used regex to clean in vscode using ctrl+f and ctrl+shift+p >> "select all occurances"
- saved as two column csv file called "tag_codes.csv"

2. Get list of all games released in 2018
- use links to games in Steamspy 2018 list at "https://steamspy.com/year/2018"
- use regex to clean in vscode and ctrl+shift+p >> "select all occurances" (this is bad - you should write a python script)
- saved as "steamspy_2018_games_clean.csv"

3. Figure out which games from 2018 were early access
- use all games listed by Steamdb as being tagged with "Early Access" from "https://steamdb.info/tag/493/?all"
- saved source from page and use regex to clean in vscode and ctrl+shift+p >> "select all occurances"

4. Using either Steamspy tags over time or Wayback Machine get the original tags for each game
- first try to automate the process of downloading the tags data for the first 10 games
- combine the data from the individual csvs with the steamspy_2018_games_clean.csv
- remove chinese games and games that are "ex early access" (https://steamspy.com/genre/Ex+Early+Access)

5. Make a subset of the data for all games with tags before the release date
- first just make a subset of all appropriate games 
- make a df of only the earliest tags entry for each game
- check if any of the games i have so far say "previously in early access" on steamspy (yes 71 games) 

6. Make a dataset of all the same games but get the current tags and counts by querying the API
- see "get_current_tags.py"
