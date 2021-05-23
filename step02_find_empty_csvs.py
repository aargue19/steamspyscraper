import pandas as pd
import numpy as np
import os
import datetime
from os import listdir
from os import getcwd

# THIS DATA COMES FROM "https://steamdb.info/tags/"
# I SAVED THE RAW SOURCE AS "steamdb_tag_codes_raw.txt"
# I used "step0_get_tag_codes.py" to make "tag_names_codes_counts.csv" which is a list of ALL CODES+totals FOR ALL TAGS


#GET A LIST OF ALL THE CSV FILES WITH TAGS OVER TIME DATA DOWNLOADED FROM STEAMSPY AND CLEAN UP

rootdir = getcwd()

filepath = rootdir + os.sep + "csvs" + os.sep

list_of_gamez = []
list_of_file_names = []

with os.scandir(filepath) as dir_entries:
    for entry in dir_entries:
        info = entry.stat()
        list_of_file_names.append(entry)
        list_of_gamez.append(entry.name.replace("_",":").replace(".csv",""))

for i in range(1,len(list_of_gamez)):

    try:
        #print(f"trying {list_of_gamez[i]}")

        data = pd.read_csv(list_of_file_names[i])

        column_name_list = data.columns.tolist()

        # print(column_name_list)
        # print(len(column_name_list))

        # if len(column_name_list) < 2 :
        #     print(f"{list_of_gamez[i]}: {len(column_name_list)}") 
    except Exception as e:
        print(list_of_gamez[i])

        ##ADD CODE HERE TO MOVE THESE FILES TO EMPTY_CSV DIRECTORY