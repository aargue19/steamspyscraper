import pandas as pd
import numpy as np
 
df = pd.read_csv("step5_result.csv")

gamez = df['app_id'].tolist()

print(len(df.columns))

gamez = list(set(gamez))



# col_list = []

# #for i in range(0,len(df.columns)):
# for i in range(len(gamez)):
#     col_list.append([i,df.columns[i]])

# print(len(col_list))

# new_col_list = []

# for entry in col_list:
#     new_col_list.append(entry.replace("tag_",""))

# new_col_list = list(set(new_col_list))

# new_col_list = list(map(int, new_col_list))

# print(len(new_col_list))
# print(new_col_list)

# tc = pd.read_csv('tag_codes.csv', index_col=False)
# codez  = tc['code'].tolist()

# print(len(codez))
# print(codez)

# for code in new_col_list:
#     if code not in codez:
#         print(code)

###########################################################################################
# list(np.arange(13,444,1))

# for i in range(13,20):
#     print(i)

##################################################################################

# pd.set_option('display.max_rows', 440)

# df = pd.read_csv("test2222.csv", index_col=False)

# which_game = 8

# # print(len(df.iloc[0, 15:445].tolist()))
# # print(df.iloc[0, 15:445].tolist())

# # print(len(df.iloc[0, 446:876].tolist()))
# # print(df.iloc[0, 446:876].tolist())

# df1 = pd.DataFrame({"t1" : df.iloc[which_game, 15:445].tolist(), "t2" : df.iloc[which_game, 446:876].tolist()})

# df1 = df1.loc[~df1.t1.isnull()]

# df1['diff'] = np.where((df1.t1 != 999999) & (df1.t2 != 999999), (df1.t2 - df1.t1) / df1.t1, 999999)



# print(df1)


################################################################################################

# df.iloc[0, 446:876]


# df_all = pd.concat([df1, df2], ignore_index=True, sort=False)

# df_all = df_all[df_all.columns[~df_all.isnull().all()]]



# def jaccard_similarity(list1, list2):
#     s1 = set(list1)
#     s2 = set(list2)
#     return float(len(s1.intersection(s2)) / len(s1.union(s2)))
# list1 = ['dog', 'cat', 'wolf', 'rat']
# list2 = ['dog', 'cat', 'rat','a','XXXXXX','bb','ccccXXX','onemore']
# print(jaccard_similarity(list1, list2))

# list1 = ['dog', 'cat', 'wolf', 'rat'] 
#list2 = ['dog', 'cat', 'wolf', 'rat'] # 1.0
#list2 = ['dog', 'cat', 'wolf']  #0.75
#list2 = ['dog', 'cat', 'rat','a'] #0.6
# list2 = ['dog', 'cat', 'rat','a','XXXXXX','bb','ccccXXX'] #0.375


#list2 = ['dog', 'cat', 'rat','a','XXXXXX','bb','ccccXXX','onemore']

# def jaccard_similarity(list1, list2):
#     intersection = len(list(set(list1).intersection(list2)))
#     union = (len(list1) + len(list2)) - intersection
#     return float(intersection) / union

# print(jaccard_similarity(list1, list2))

















################################################################################## 
#EXCLUDE GAMES WHERE THE TAGS DATA CAME AFTER THE RELEASE DATE

# df = pd.read_csv("step2_result.csv")

# # convert the 'Date' column to datetime format
# df['release_date']= pd.to_datetime(df['release_date'])
# df['tag_date']= pd.to_datetime(df['tag_date'])

# #print(df.loc[:,['app_name','release_date','tag_date']].dtypes)

# list_of_ids = df['app_id'].tolist()
# list_of_ids = set(list_of_ids)
# list_of_ids = list(list_of_ids)

# #CREATE A COLUMN TO INDICATE IF A ROW IS THE EARLIEST TAGS FOR EACH GAME

# # df['tag_year'] = pd.DatetimeIndex(df['tag_date']).year

# df['one_year_after'] = np.where(pd.DatetimeIndex(df['release_date']).year == 1 + pd.DatetimeIndex(df['tag_date']).year, "yes", "no")

# df.to_csv("test2222.csv")





# current_idx = tags_before_release_df['tag_date'].loc[tags_before_release_df['app_id'] == games_with_producer_tags[0]].idxmin()

# 

#CREATE A COLUMN TO INDICATE IF A ROW IS THE FIRST TAGS AFTER THE ONE YEAR MARK FOR EACH GAME