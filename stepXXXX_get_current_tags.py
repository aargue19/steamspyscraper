#query the steamspy api for the 108 games in test2222.csv and get the current tags at present
import requests
import json
import pandas as pd
import time
import datetime
import numpy as np

query_games_df = pd.read_csv('step3_result.csv')

#list_of_app_ids_to_check = query_games_df['app_id'].tolist()
all_app_ids = query_games_df['app_id'].tolist()
#list_of_app_ids_to_check = all_app_ids[0:2]
#list_of_app_ids_to_check = [706560]

list_of_app_ids_to_check = all_app_ids

# create blank dataframe and reorder columns
all_df = pd.DataFrame(columns = query_games_df.columns)

count = 0

for current_app_id in list_of_app_ids_to_check:

    count +=1

    print(f"checking #{count}: {current_app_id}")

    time.sleep(10)

    response = requests.get(f'https://steamspy.com/api.php?request=appdetails&appid={current_app_id}').text

    response_info = json.loads(response)

    tags_info = []

    for tag in response_info['tags']:
        tags_info.append([tag, response_info['tags'][tag]])

    df = pd.DataFrame(tags_info, columns = ['tag_name','tag_count'])

    #the tag data from the api is labeled using the names so match it with tag ids from tag_codes.csv

    tag_codes_df = pd.read_csv('tag_names_codes_counts.csv')

    df['app_name'] =  response_info['name']
    df['app_id'] = current_app_id
    df['new_tag_code'] = 999999

    for i in range(len(df)):
        try:
            name_to_code = str(df.tag_name[i])
            code_to_use = tag_codes_df.code.loc[tag_codes_df.tag == name_to_code].item()
            # print(name_to_code)
            # print(code_to_use)
            df.new_tag_code.iloc[i] = code_to_use
        except Exception as e:
            print(e)
    #print(df)

    #CREATE A DATAFRAME WITH THE GAME DETAILS AND ALL 445 TAG COLUMNS AS BLANK

    temp_present_tags_df = pd.DataFrame(columns=query_games_df.columns)

    # append the data from test2222.csv to the first 15 columns and leave the rest blank

    to_append = query_games_df.loc[query_games_df.app_id == current_app_id].values.tolist()

    #print(f"to append is :")
    #print(to_append)

    a_series = pd.Series(to_append[0], index = temp_present_tags_df.columns)

    temp_present_tags_df = temp_present_tags_df.append(a_series, ignore_index=True)

    temp_present_tags_df.iloc[0,14:444] = ""

    #put the current tags data in the same format as the original tags data
    today = datetime.date.today()
    d1 = today.strftime("%m/%d/%Y")
    temp_present_tags_df.tag_date = pd.to_datetime(d1)
    temp_present_tags_df.tag_before_release = 0

    #iterate through the tag_#### columns and add the counts from the current game if they exist

    tags_in_current_game = df['new_tag_code'].tolist()

    #print(tags_in_current_game)

    for i in range(len(tags_in_current_game)):

        for j in range(len(temp_present_tags_df.columns)):
            
            tag_to_check = f'tag_{tags_in_current_game[i]}'

            if temp_present_tags_df.columns[j] == tag_to_check:
                #print(f"{tag_to_check} is the {j}th column")

                temp_present_tags_df.iloc[0,j] = df.tag_count.loc[df.new_tag_code == tags_in_current_game[i]]

    all_df = all_df.append(temp_present_tags_df)

    all_df.to_csv('step4_result.csv')

















#combine the data for original tags and the present day tags


# temp_present_tags_df.index
# temp_present_tags_df.app_num
# temp_present_tags_df.app_name
# temp_present_tags_df.app_id
# temp_present_tags_df.release_date
# temp_present_tags_df.price
# temp_present_tags_df.price_decimal
# temp_present_tags_df.user_score_meta_score
# temp_present_tags_df.owners
# temp_present_tags_df.playtime_median
# temp_present_tags_df.developer
# temp_present_tags_df.developer2
# temp_present_tags_df.publisher
# temp_present_tags_df.publisher2
