import pandas as pd
import numpy as np

######################################################################################
# SET UP DATA

df = pd.read_csv("step5_result.csv",index_col=False)
df = df.replace(999999,np.nan)
df = df.replace(np.nan,0)

# df = df.loc[(df.genre_1 != 'Animation & Modeling')
#             & (df.genre_1 != 'Audio Production') 
#             & (df.genre_1 != 'Video Production')
#             & (df.genre_1 != 'Education')
#             & (df.genre_1 != 'Free to Play') , :]

columns = [2,31,32,33,34,35] + list(np.arange(37,462)) # EXCLUDE "TAG_OTHER" (COLUMN 463)
t0_tags_df = df.iloc[:,columns]

#REPLACE ANY VALUES ABOVE 0 WITH 1
tag_columns_list = t0_tags_df.iloc[:,6:462].columns.tolist()
tag_columns_list_length = len(tag_columns_list)


for colname in tag_columns_list: 
    t0_tags_df.loc[t0_tags_df[f'{colname}'] > 0, f'{colname}'] = 1

# CREATE A NEW COLUMN FOR THE NUMBER OF GENRES FOR EACH GAME
t0_tags_df['num_of_genres'] = 5 - (t0_tags_df.iloc[:,2:6]==0).sum(axis=1)

# DIVIDE ALL THE VALUES BY THE NUMBER OF GENRES
# t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1] = t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1] / t0_tags_df['num_of_genres']
t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1]  = t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].div(t0_tags_df.num_of_genres, axis=0)

#CHECK
# t0_tags_df.to_csv("~/Desktop/test1.csv")

######################################################################################
# PRODUCE CATEGORY-WORD OCCURANCE TABLE

#MAKE A LIST OF ALL GENRES THAT APPEAR IN THE 5 GENRE COLUMNS
g1 = list(filter(None,list(set(t0_tags_df.genre_1.tolist()))))
g2 = list(filter(None,list(set(t0_tags_df.genre_2.tolist()))))
g3 = list(filter(None,list(set(t0_tags_df.genre_3.tolist()))))
g4 = list(filter(None,list(set(t0_tags_df.genre_4.tolist()))))
g5 = list(filter(None,list(set(t0_tags_df.genre_5.tolist()))))

# genre_names_list = list(set(g1 + g2 + g3 + g4 + g5))
genre_names_list = ['Indie',
'Action',
'Casual',
'Adventure',
'Video Production',                 # THIS IS TEMPORARY SO IT MATCHES THE EXCEL FILE FOR CHECKING
'Simulation',
'Strategy',
'Audio Production',
'Sports',
'Free to Play',
'RPG',
'Animation & Modeling',
'Education',
'Racing',
'Utilities',
'Design & Illustration',
'Software Training',
'Massively Multiplayer',
'Web Publishing']

genre_names_list_length = len(genre_names_list)

occ_columns = ['genre'] + tag_columns_list

occ_df = pd.DataFrame(np.zeros((len(genre_names_list),tag_columns_list_length+1)), 
                        columns = [occ_columns])

occ_df.genre = genre_names_list

tag_totals = t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].loc[t0_tags_df.genre_1 == "Indie"].sum(axis=0).tolist()
print(tag_totals[0])

# tag_totals = []

# count=0
# for current_tag in genre_names_list:
#     tag_totals.append(t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].loc[t0_tags_df.genre_1 == current_tag].sum(axis=0).tolist())

#     tag_totals.append(t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].loc[t0_tags_df.genre_2 == current_tag].sum(axis=0).tolist())

#     tag_totals.append(t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].loc[t0_tags_df.genre_3 == current_tag].sum(axis=0).tolist())

#     tag_totals.append(t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].loc[t0_tags_df.genre_4 == current_tag].sum(axis=0).tolist())

#     tag_totals.append(t0_tags_df.iloc[:,6:len(t0_tags_df.columns)-1].loc[t0_tags_df.genre_5 == current_tag].sum(axis=0).tolist())

#     tag_totals_sum = [sum(i) for i in zip(*tag_totals)]

#     occ_df.loc[count,['genre'] + tag_columns_list] = [current_tag] + tag_totals_sum
    
#     count+=1

# #CHECK
# occ_df.to_csv("~/Desktop/test1.csv")