import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

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

df = df.replace(999999,np.nan)
df = df.replace(np.nan,0)

############################################################################################################################################################
############################################################################################################################################################
# CALCULATE A MEASURE OF CONFUSION 

# FIND OUT HOW MANY NEW TAGS WERE ADDED TO A GAME ON TOP OF PRODUCERS' TAGS AT T=0
columns = [2] + list(np.arange(37,462))

t0_df = df.iloc[:,columns]

# print(t6_df.columns[:40])
# print(t6_df.columns[420:])

t0_df = t0_df.mask(t0_df >=1, 1)

tag_counts_t0 = t0_df.apply(lambda x: x.sum(), axis='columns')

# FIND OUT HOW MANY NEW TAGS WERE ADDED TO A GAME ON TOP OF PRODUCERS' TAGS AT T=6

columns = [2] + list(np.arange(464,889))

t6_df = df.iloc[:,columns]

t6_df = t6_df.mask(t6_df >=1, 1)

tag_counts_t6 = t6_df.apply(lambda x: x.sum(), axis='columns')

tag_counts_df = pd.DataFrame({'app_id': df.app_id, 't0_tag_count': tag_counts_t0, 't6_tag_count': tag_counts_t6})

tag_counts_df['tags_added'] = tag_counts_df.t6_tag_count - tag_counts_df.t0_tag_count

print(tag_counts_df.head)

tag_counts_df.to_csv("test2222.csv")