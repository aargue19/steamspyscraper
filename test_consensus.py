import pandas as pd
import numpy as np
from scipy import spatial

df = pd.read_csv("step5_result.csv",index_col=False)
#df = df.replace(999999,np.nan)
df = df.replace(np.nan,0)

df = df.loc[(df.genre_1 != 'Animation & Modeling')
            & (df.genre_1 != 'Audio Production') 
            & (df.genre_1 != 'Video Production')
            & (df.genre_1 != 'Education')
            & (df.genre_1 != 'Free to Play') , :]

columns = [2,31] + list(np.arange(37,462)) #ADD ONE MORE COLUMN TO THE END (463) IF YOU WANT THE "TAG_OTHER"

t0_tags_df = df.iloc[:,columns]

# Change all null cells to 0 and all positive cells to 1
#t0_tags_df.iloc[:,2:len(t0_tags_df.columns)] = t0_tags_df.mask(t0_tags_df.iloc[:,2:len(t0_tags_df.columns)]>=1, 1)
#print(t0_tags_df.iloc[0:6,0:6])

# COUNT HOW MANY 999999s THERE ARE FOR EACH GAME
t0_tags_df['tags_added'] = (t0_tags_df.iloc[:,2:len(t0_tags_df.columns)]==999999).sum(axis=1)

# COUNT HOW MANY TAGS WERE APPLIED BY PRODUCER ORIGINALLY
t0_tags_df['num_orig_tags'] = (t0_tags_df.iloc[:,2:len(t0_tags_df.columns)].replace(999999,0)>0).sum(axis=1)

#CALCULATE THE NUMBER OF ADDED TAGS AS A PERCENTAGE OF ORIGINAL TAGS
t0_tags_df['tags_added_rel'] = t0_tags_df['tags_added'] / t0_tags_df['num_orig_tags']

print(t0_tags_df[['app_id', 'tags_added', 'num_orig_tags','tags_added_rel']])

plot = t0_tags_df.tags_added_rel.plot.hist(bins=100)
fig = plot.get_figure()
fig.savefig("histplot222222.png")