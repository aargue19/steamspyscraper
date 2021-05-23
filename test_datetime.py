##################################################################################
# TESTING REORDERING COLUMNS IN 6MO DF
# import pandas as pd
# import numpy as np

# full_df2 = pd.read_csv("test_tags_after_6_mo.csv")

# # # REORDER THE COLUMNS OF THE 6MO DF SO ALL TAG CODES ARE AT THE END
# # # THIS IS SO RENAMING THEM IS EASIER

# cols = full_df2.columns.tolist()

# print(len(cols)) # 0:445

# test_list = []

# myorder = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,439,445,438]
# myorder = myorder + list(np.arange(14,438,1)) + [441,442,443,444,440]

# for cnum in myorder:
#     test_list.append(cols[cnum])

# print(test_list)
# print(len(test_list))
# # mylist = [cols[i] for i in myorder]
# # full_df2 = full_df2[mylist]








###################################################################################
# CODE TO GET THE 6MO TAGS

# import numpy as np
# import pandas as pd

# # GAMES WITH NO TAGS AFTER 6 MONTHS:
# # GOOD GIRL (1 MO)


# df1 = pd.read_csv("step3_earliest_tags.csv")
# df2 = pd.read_csv("step2_result.csv")

# df2 = df2.loc[df2.app_id.isin(df1.app_id) ]

# # convert the 'Date' column to datetime format
# df2['release_date']= pd.to_datetime(df2['release_date'])
# df2['tag_date']= pd.to_datetime(df2['tag_date'])

# #CREATE A COLUMN TO INDICATE HOW MANY MONTHS BETWEEN RELEASE AND EACH TAG DATE

# df2['nb_months'] = ((df2.tag_date - df2.release_date)/np.timedelta64(1, 'M'))
# df2['nb_months'] = df2['nb_months'].astype(int)

# full_df = pd.DataFrame(columns=df2.columns)

# ids_to_check = list(set(df2['app_id'].tolist()))

# ## SOME GAMES DONT HAVE TAGS AT 6 MONTHS SO REMOVE THEM FROM THE DF
# #875230, 

# ids_to_check.remove(875230)

# print(ids_to_check)

# counter = 0

# for current_id in ids_to_check:

#     print(counter)
#     print(current_id)

#     counter += 1

#     current_idx = df2['tag_date'].loc[(df2['app_id'] == current_id) & (df2['nb_months'] == 6)].idxmin()

#     temp_df = df2.loc[df2.index == current_idx,:]

#     full_df = pd.concat([full_df, temp_df], ignore_index=True, sort=False)

# full_df.to_csv("test_tags_after_6_mo.csv")

# cols = full_df.columns.tolist()

# print(cols)

# myorder = [0,1,2,3,4,5,6,7,8,9,10,11,12,443,438]
# myorder = myorder + list(np.arange(13,437,1))
# mylist = [cols[i] for i in myorder]
# full_df = full_df[mylist]






###################################################################################


#use just the first game in the list to set up the dataframe
# current_idx = df2['tag_date'].loc[df2.app_id == 882750 & df2['nb_months'] == 2].idxmin()

# temp_df = df2.loc[df2.index == current_idx,:]

# print(temp_df)

# test_df = pd.read_csv("step3_earliest_tags.csv")

# #print(test_df['release_date'].head)

# test_df['release_date'] = pd.to_datetime(test_df['release_date'])

# # print(test_df.loc[0,'release_date'].year)

# test_year = int(test_df.loc[0,'release_date'].year)
# test_mth = int(test_df.loc[0,'release_date'].month)

# print(test_year)
# print(test_mth)


# print(test_df.iloc[0,4].year > test_df.iloc[0,4].year)