import pandas as pd
import numpy as np

df = pd.read_csv("step5_result.csv",index_col=False)

# print(df.columns[1:40])

# print(len(df))
# genrez1 = df['genre_1'].tolist()
# genrez1 = list(set(genrez1))
# print(genrez1)

df = df.loc[(df.genre_1 != 'Animation & Modeling')
            & (df.genre_1 != 'Audio Production') 
            & (df.genre_1 != 'Video Production')
            & (df.genre_1 != 'Education')
            & (df.genre_1 != 'Free to Play') , :]

# print(len(df))
# genrez1 = df['genre_1'].tolist()
# genrez1 = list(set(genrez1))
# print(genrez1)
# print(df.columns[37:463])

df = df.replace(np.nan,0)
df = df.replace(999999,0)

df = df.loc[df.genre_1 == 'Action']

slice_and_dice = df.iloc[:,37:463]               #THIS NEEDS TO BE CHANGED BECAUSE YOU ADDED 5 EXTRA GENRE COLUMNS IN STEP 4

# print(slice_and_dice.columns)

slice_and_dice[slice_and_dice != 0] = 1

# print(slice_and_dice.iloc[0,:].tolist())

# print(len(slice_and_dice))

what_does_it_mean = slice_and_dice.mean(axis=0)

# print(what_does_it_mean[37:463].tolist())


# CALCULATE COSINE SIMILARITY BETWEEN A GAME AND THE VECTOR OF AVERAGES FOR EACH TAG COLUMN FOR ACTION GAMES
from numpy import dot
from numpy.linalg import norm

game_1_tag_vec = df.iloc[0,37:463].tolist()     #THIS NEEDS TO BE CHANGED BECAUSE YOU ADDED 5 EXTRA GENRE COLUMNS IN STEP 4

game_2_tag_vec = df.iloc[1,37:463].tolist()     #THIS NEEDS TO BE CHANGED BECAUSE YOU ADDED 5 EXTRA GENRE COLUMNS IN STEP 4

cos_sim_game_1 = dot(game_1_tag_vec, what_does_it_mean)/(norm(game_1_tag_vec)*norm(what_does_it_mean))
cos_sim_game_2 = dot(game_2_tag_vec, what_does_it_mean)/(norm(game_2_tag_vec)*norm(what_does_it_mean))

print(cos_sim_game_1)
print(cos_sim_game_2)


