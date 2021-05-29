import pandas as pd
import numpy as np

######################################################################################
# SET UP DATA

# df = pd.read_csv("step5_result.csv",index_col=False)
# df = df.replace(999999,np.nan)
# df = df.replace(np.nan,0)

# df = df.loc[(df.genre_1 != 'Animation & Modeling')
#             & (df.genre_1 != 'Audio Production') 
#             & (df.genre_1 != 'Video Production')
#             & (df.genre_1 != 'Education')
#             & (df.genre_1 != 'Free to Play') , :]

# columns = [2,31] + list(np.arange(37,463))
# t0_tags_df = df.iloc[:,columns]
# t0_tags_df = t0_tags_df.loc[t0_tags_df.genre_1=="Action"]
# how_many_action_games = len(t0_tags_df)
# # print(f"{how_many_action_games} action games")
# t0_tags_df = t0_tags_df.iloc[:,2:len(t0_tags_df.columns)-1]  
# # print(t0_tags_df.iloc[1:10,0:6])
# t0_tags_df = t0_tags_df.mask(t0_tags_df >=1, 1)

# # CREATE A NEW COLUMN FOR THE NUMBER OF GENRES FOR EACH GAME
# df.num_of_genres = np.count_nonzero(df.iloc[:,31:36], axis=1)

# g1 = list(filter(None,list(set(df.genre_1.tolist()))))
# g2 = list(filter(None,list(set(df.genre_2.tolist()))))
# g3 = list(filter(None,list(set(df.genre_3.tolist()))))
# g4 = list(filter(None,list(set(df.genre_4.tolist()))))
# g5 = list(filter(None,list(set(df.genre_5.tolist()))))

# genre_names_list = list(set(g1 + g2 + g3 + g4 + g5))
# # print(genre_names_list)

# new_temp_df = []

# for i in range(len(genre_names_list)):

#     temp_df = df.loc[(df.genre_1==genre_names_list[i])]
#     pure_temp_df = temp_df.loc[temp_df.num_of_genres == 1]
#     hybrid_temp_df = temp_df.loc[temp_df.num_of_genres > 1]
#     hybrid_temp_df = hybrid_temp_df.replace(1,1/temp_df.num_of_genres)
#     new_temp_df.append(pd.concat([pure_temp_df, hybrid_temp_df]))

# for i in range(len(genre_names_list)):

#     temp_df = df.loc[(df.genre_2==genre_names_list[i])]
#     pure_temp_df = temp_df.loc[temp_df.num_of_genres == 1]
#     hybrid_temp_df = temp_df.loc[temp_df.num_of_genres > 1]
#     hybrid_temp_df = hybrid_temp_df.replace(1,1/temp_df.num_of_genres)
#     new_temp_df.append(pd.concat([pure_temp_df, hybrid_temp_df]))