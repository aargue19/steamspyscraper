import requests
import json
import pandas as pd
import time
import datetime
import numpy as np

query_games_df = pd.read_csv('step3_earliest_tags.csv')

all_app_ids = query_games_df['app_id'].tolist()

list_of_app_ids_to_check = all_app_ids

# create blank dataframe and reorder columns

all_df = pd.DataFrame(columns = ['app_id','pos_rev_num','neg_rev_num','usr_score','avg_pt_forever',
                                             'avg_pt_2weeks','initial_price','current_price','ccu',
                                             'lang_1','lang_2','lang_3','lang_4','lang_5',
                                             'lang_6','lang_7','lang_8','lang_9','lang_10',
                                             'genre_1','genre_2','genre_3','genre_4','genre_5'])

# logf = open("failed_games.txt", "w")

for i in range(len(list_of_app_ids_to_check)):

    print(f"checking #{i}: {list_of_app_ids_to_check[i]}")
    try:
        

        response = requests.get(f'https://steamspy.com/api.php?request=appdetails&appid={list_of_app_ids_to_check[i]}').text

        response_info = json.loads(response)

        app_id = response_info['appid']

        pos_rev_num = response_info['positive']
        neg_rev_num = response_info['negative']
        usr_score = response_info['userscore']

        avg_pt_forever = response_info['average_forever']
        avg_pt_2weeks = response_info['average_2weeks']
        initial_price = response_info['initialprice']
        current_price = response_info['price']
        ccu = response_info['ccu']

        # split the string into two
        owners_string = response_info['owners']

        owners_vals = owners_string.split(" .. ")

        clean_owners_vals = []

        for string in owners_vals:
            new_string = string.replace(",", "")
            clean_owners_vals.append(new_string)

        if len(clean_owners_vals) > 0:
            owners_min = int(clean_owners_vals[0])
            owners_max = int(clean_owners_vals[1])
        if len(clean_owners_vals) == 0:
            owners_min = 999999
            owners_max = 999999 

        genre_list = response_info['genre'].split(", ")

        if len(genre_list) < 11:
            number_of_nas_to_append = 10 - len(genre_list)

            for j in range(number_of_nas_to_append):
                genre_list.append("NA")    
        
        else:
            # logf.write(f"{app_id}\n")
            print(f"more than 10 game #{app_id}")

        lang_list = response_info['languages'].split(", ")

        if len(lang_list) < 11:
            number_of_nas_to_append = 10 - len(lang_list)

            for j in range(number_of_nas_to_append):
                lang_list.append("NA")  

        row_to_add = {'app_id':[app_id],
                    'pos_rev_num':[pos_rev_num],
                    'neg_rev_num':[neg_rev_num],
                    'usr_score':[usr_score],
                    'avg_pt_forever':[avg_pt_forever],
                    'avg_pt_2weeks':[avg_pt_2weeks],
                    'initial_price':[initial_price],
                    'current_price':[current_price],
                    'ccu':[ccu],

                    'lang_1':[lang_list[0]],
                    'lang_2':[lang_list[1]],
                    'lang_3':[lang_list[2]],
                    'lang_4':[lang_list[3]],
                    'lang_5':[lang_list[4]],
                    'lang_6':[lang_list[5]],
                    'lang_7':[lang_list[6]],
                    'lang_8':[lang_list[7]],
                    'lang_9':[lang_list[8]],
                    'lang_10':[lang_list[9]],

                    'genre_1':[genre_list[0]],
                    'genre_2':[genre_list[1]],
                    'genre_3':[genre_list[2]],
                    'genre_4':[genre_list[3]],
                    'genre_5':[genre_list[4]],
                    'genre_6':[genre_list[5]],
                    'genre_7':[genre_list[6]],
                    'genre_8':[genre_list[7]],
                    'genre_9':[genre_list[8]],
                    'genre_10':[genre_list[9]]}

        df = pd.DataFrame(row_to_add, columns = ['app_id','pos_rev_num','neg_rev_num','usr_score','avg_pt_forever',
                                                'avg_pt_2weeks','initial_price','current_price','ccu',
                                                'lang_1','lang_2','lang_3','lang_4','lang_5',
                                                'lang_6','lang_7','lang_8','lang_9','lang_10',
                                                'genre_1','genre_2','genre_3','genre_4','genre_5',
                                                'genre_6','genre_7','genre_8','genre_9','genre_10'])   

        all_df = pd.concat([all_df,df])

        #print(all_df)

        time.sleep(10)

    except Exception as e:
        print(f"Game #{i} failed -- ID# {list_of_app_ids_to_check[i]} failed")
        #print(e)
#########################################
# CHECK HERE TO SEE WHICH OF THE 476 GAMES FAILED

all_df.to_csv('step4_steam_api_data.csv', index=False)

###################################################################
# WHEN YOU HAVE THE DATA FOR ALL 476 GAMES THEN merge with previous file

all_df = pd.read_csv('step4_steam_api_data.csv', index_col=False)

step3_df = pd.read_csv('step3_earliest_tags.csv', index_col=False)

step_4_df = pd.merge(step3_df, all_df, on="app_id")


# REORDER COLUMNS

# for i in range(len(step_4_df.columns)):
#     print(i)
#     print(step_4_df.columns[i])

cols = step_4_df.columns.tolist()

myorder = [0,1,2,3,4,5,6,7,8,9,10,11,12]
myorder = myorder + list(np.arange(444,467,1)) + list(np.arange(13,444,1))
mylist = [cols[i] for i in myorder]


step_4_df = step_4_df[mylist]

step_4_df.to_csv("step4_result_earliest_tags.csv", index=False)

