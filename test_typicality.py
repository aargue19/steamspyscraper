import pandas as pd
import numpy as np

######################################################################################
# SET UP DATA

df = pd.DataFrame({'restaurant': ['A','A','B','E','C','C','D'], 
              'genre1': ['french','french','italian','italian','french','french','texmex'],
              'genre2' : ['','','','','spanish','spanish',''],
              'mushroom' : [1,1,0,0,1,0,0],
              'sandwich' : [1,0,1,0,0,0,0],
              'quiche':   [0,1,0,0,1,0,0],
              'pizza' :    [0,0,1,0,0,0,0],
              'mozzarella' : [0,0,0,1,0,0,0],
              'paella' :     [0,0,0,0,0,1,0],
              'chili' :      [0,0,0,0,0,0,1]})

df['two_genres'] = 0
df['two_genres'].loc[df.genre2 != ''] = 'yes'

# print(df)
# print("\n")

######################################################################################
# PRODUCE CATEGORY-WORD OCCURANCE TABLE

############################# OLD WAY FOR ONLY 2 GENRES
genre1_names = df.genre1.tolist()
genre1_names = list(filter(None,list(set(genre1_names))))
# print(genre1_names)

genre2_names = df.genre2.tolist()
genre2_names = list(filter(None,list(set(genre2_names))))
# print(genre2_names)

new_temp_df = []

for i in range(len(genre1_names)):

    temp_df = df.loc[(df.genre1==genre1_names[i])]
    pure_temp_df = temp_df.loc[temp_df.genre2=='']
    hybrid_temp_df = temp_df.loc[temp_df.genre2!='']
    hybrid_temp_df = hybrid_temp_df.replace(1,0.5)
    new_temp_df.append(pd.concat([pure_temp_df, hybrid_temp_df]))

for i in range(len(genre2_names)):

    temp_df = df.loc[(df.genre2==genre2_names[i])]
    pure_temp_df = temp_df.loc[temp_df.genre1=='']
    hybrid_temp_df = temp_df.loc[temp_df.genre1!='']
    hybrid_temp_df = hybrid_temp_df.replace(1,0.5)
    new_temp_df.append(pd.concat([pure_temp_df, hybrid_temp_df]))

occ_df = pd.DataFrame(np.zeros((len(genre1_names)+len(genre2_names),8)), 
                        columns = ["genre",
                                    "mushroom", 
                                    "sandwich",
                                    "quiche",
                                    "pizza",
                                    "mozzarella",
                                    "paella",
                                    "chili"])

count = 0

for gen_name in genre1_names:

    tag_totals = new_temp_df[count].iloc[:,3:10].loc[new_temp_df[count].genre1 == gen_name].sum(axis=0).tolist()
    # print(action_tag_totals)

    occ_df.loc[count,["genre",
                    "mushroom", 
                    "sandwich",
                    "quiche",
                    "pizza",
                    "mozzarella",
                    "paella",
                    "chili"]] = [gen_name] + tag_totals
    count+=1

for gen_name in genre2_names:

    tag_totals = new_temp_df[count].iloc[:,3:10].loc[new_temp_df[count].genre2 == gen_name].sum(axis=0).tolist()
    # print(action_tag_totals)

    occ_df.loc[count,["genre",
                    "mushroom", 
                    "sandwich",
                    "quiche",
                    "pizza",
                    "mozzarella",
                    "paella",
                    "chili"]] = [gen_name] + tag_totals
    count+=1

occ_df = occ_df.sort_values("genre")

print(occ_df)
print("\n")

######################################################################################
# CALCULATE JACCARD SIMILARITY INDEX FOR ALL WORD-CATEGORY PAIRS

js_df = occ_df

vals = []
for i in range(0,4):
    for j in range(1,8):
        value = occ_df.iloc[i,j]
        col_sum = sum(occ_df.iloc[:,j].tolist())
        row_sum = sum(occ_df.iloc[i,1:8].tolist())
        # js_df.iloc[i,j] = occ_df.iloc[i,j] / (sum(occ_df.iloc[:,j].tolist()) + sum(occ_df.iloc[i,1:8].tolist()) - occ_df.iloc[i,j])
        vals.append(occ_df.iloc[i,j] / (sum(occ_df.iloc[:,j].tolist()) + sum(occ_df.iloc[i,1:8].tolist()) - occ_df.iloc[i,j]))

count=0
for i in range(0,4):
    for j in range(1,8):
        js_df.iloc[i,j] = vals[count]
        count+=1

print(js_df)
print("\n")

######################################################################################
# CALCULATE WEIGHTED TYPICALITY SCORE FOR EACH RESTAURANT-CATEGORY PAIR

for x in list(set(df.restaurant.tolist())):
    
    typ_vec = []
    for y in js_df.genre.tolist():

        tot_count = 0
        products = []
        for z in df.columns.tolist()[3:10]:

            temp_df = df.loc[df.restaurant == x]
            count = sum(temp_df[str(z)].tolist())
            weight = js_df.loc[js_df.genre == y, [f'{z}']].iloc[0].tolist()[0]
            # print(f"count: {count}")
            # print(f"weight: {weight}")
            if count > 0:
                tot_count += count

            if df.two_genres.loc[df.restaurant == x].tolist()[0] == 0:
                products.append(count*weight)
            else:
                products.append(count/2*weight)   

        # print(f"{x}, {y} = {products}")
        # print(f"total count = {tot_count}")

        denominator = tot_count
        if denominator != 0:
            typicality = sum(products) / denominator
        else:
            typicality = sum(products)

        #print(f"{x}, {y} = {typicality}")
        typ_vec.append(typicality)
    
    tot_typ = sum(typ_vec)
    print(f"{x} = {tot_typ}")





#############################################################
# UNUSED CODE

# row_count = 0 
# for resto in list(set(df.restaurant.tolist())):
#     print(f"restaurant: {resto}")
    
#     col_count=1
#     resto_temp_df = df.loc[df.restaurant == resto]

#     typ=[]
#     for tag in df.columns.tolist()[3:10]:
#         print(f"food: {tag} \n")
        
#         mush_count = sum(resto_temp_df[str(tag)].tolist())
#         print(f"mush count: {mush_count}")

#         print(f"weight row#: {row_count}")
#         print(f"weight col#: {col_count}")

#         mush_weight = js_df.iloc[row_count,col_count]
#         print(f"mush_weight: {mush_weight}")

#         weighted_mush = mush_count * mush_weight
#         print(f"weighted_mush: {weighted_mush}")

#         typ.append(weighted_mush)
        
#         col_count+=1

#     row_count+=1

#     typ = typ[1:len(typ)]
#     print(f"summing: {typ}")
#     typ_total = sum(typ)
    
#     print(f"typicality: {typ_total} \n")

# print(mush_count)
# print(mush_weight)



# typ = (weighted_mush + weighted_sand + weighted_quiche + weighted_pizza + weighted_paella + weighted_chili) / 4


# #########################################

# sand_count = sum(a_french_typ_df.sandwich.tolist())
# sand_weight = js_df.iloc[0,2]
# weighted_sand = sand_count * sand_weight
# # print(sand_count)
# # print(sand_weight)

# quiche_count = sum(a_french_typ_df.quiche.tolist())
# quiche_weight = js_df.iloc[0,3]
# weighted_quiche = quiche_count * quiche_weight
# # print(quiche_count)
# # print(quiche_weight)

# pizza_count = sum(a_french_typ_df.pizza.tolist())
# pizza_weight = js_df.iloc[0,4]
# weighted_pizza = pizza_count * pizza_weight
# # print(pizza_count)
# # print(pizza_weight)

# mozzarella_count = sum(a_french_typ_df.mozzarella.tolist())
# mozzarella_weight = js_df.iloc[0,5]
# mozzarella_pizza = mozzarella_count * mozzarella_weight

# paella_count = sum(a_french_typ_df.paella.tolist())
# paella_weight = js_df.iloc[0,6]
# weighted_paella = paella_count * paella_weight

# chili_count = sum(a_french_typ_df.chili.tolist())
# chili_weight = js_df.iloc[0,7]
# weighted_chili = chili_count * chili_weight

# typ = (weighted_mush + weighted_sand + weighted_quiche + weighted_pizza + weighted_paella + weighted_chili) / 4

# print(typ)

#you got 0.31 -- now you need to do this for every restaurant-genre combination iteratively

















# print(weighted_sand)




# c_french_typ_df = df.loc[df.restaurant == 'C']
# mush_count = sum(a_french_typ_df.mushroom.tolist())
# mush_weight = js_df.iloc[0,1]
# weighted_mush = mush_count * mush_weight





# count = 0
# for gen in occ_df['genre'].tolist():

#     genre_tag_occ = occ_df.loc[occ_df.genre == gen].iloc[:,1]
#     print(f"french_mushroom_occ: {genre_tag_occ}")
#     tag_total = sum(occ_df['mushroom'])
#     print(f"mushroom total: {tag_total}")
#     genre_total = sum(occ_df.loc[occ_df.genre == gen].iloc[0,1:8].tolist())
#     print(f"french total: {genre_total}")
#     numerator = genre_tag_occ 
#     denominator = tag_total + genre_total - genre_tag_occ
#     sim_val = numerator/denominator
#     print(f"similarity: {sim_val}")

#     js_df.loc[0, count] = sim_val
#     count+=1

# print(js_df)

# genre_tag_occ = occ_df.iloc[0,1]
# print(f"french_mushroom_occ: {genre_tag_occ}")
# tag_total = sum(occ_df.mushroom.tolist())
# print(f"mushroom total: {tag_total}")
# genre_total = sum(occ_df.iloc[0,1:8].tolist())
# print(f"french total: {genre_total}")
# numerator = genre_tag_occ 
# denominator = tag_total + genre_total - genre_tag_occ
# print(f"similarity: {numerator/denominator}")
#js_df.iloc[i,1] = sim_val


# all_vals=[]
# for j in range(1,8):

#     sim_vals = []
#     for i in range(len(occ_df)):
        
#         genre_tag_occ = occ_df.iloc[i,j]
#         # print(genre_tag_occ)
#         tag_total = sum(occ_df.mushroom.tolist())
#         # print(tag_total)
#         genre_total = sum(occ_df.iloc[i,1:8].tolist())
#         # print(genre_total)
#         numerator = genre_tag_occ 
#         denominator = tag_total + genre_total - genre_tag_occ
#         sim_vals.append(numerator/denominator)
#         #js_df.iloc[i,1] = sim_val

#     all_vals.append(sim_vals)

# print(all_vals)


# for j in range(1,8):
#     js_df.iloc[:,j] = all_vals[j]

# print(js_df)



# for i in range(len(js_df)):

#     french_mushroom_occ = js_df.iloc[i,1]
#     mushroom_total = sum(js_df.mushroom.tolist())
#     french_total = sum(js_df.iloc[i,1:8].tolist())
#     sim_val = french_mushroom_occ / (mushroom_total + french_total - french_mushroom_occ)
#     js_df.iloc[i,1] = sim_val

# print(js_df)







##########################
# UNUSED CODE




# french_df = df.loc[df.genre1=='french']
# pure_french_df = french_df.loc[french_df.genre2=='']
# hybrid_french_df = french_df.loc[french_df.genre2!='']
# hybrid_french_df = hybrid_french_df.replace(1,0.5)
# new_french_df = pd.concat([pure_french_df, hybrid_french_df])
# # print(new_french_df.sum(axis=0))

# italian_df = df.loc[df.genre1=='italian']
# pure_italian_df = italian_df.loc[italian_df.genre2=='']
# hybrid_italian_df = italian_df.loc[italian_df.genre2!='']
# hybrid_italian_df = hybrid_italian_df.replace(1,0.5)
# new_italian_df = pd.concat([pure_italian_df, hybrid_italian_df])
# print(new_italian_df.sum(axis=0))

# print(new_french_df.sum(axis=0).tolist()[3:10])
# print(new_italian_df.sum(axis=0).tolist()[3:10])

# combo_df = pd.DataFrame({"french":new_french_df.sum(axis=0).tolist()[3:10], 
#                          "italian": new_italian_df.sum(axis=0).tolist()[3:10]})

# print(combo_df.transpose())





# col_names = df.iloc[:,3:10].columns.tolist()
# # print(col_names)

# df.loc[(df.two_genres == 1),] = 0.25

# print(df)

# tag_counts_for_french = df.iloc[:,3:10].loc[(df.genre1 == "french") | (df.genre2 == "french")].sum(axis=0)
# tag_counts_for_italian = df.iloc[:,3:10].loc[(df.genre1 == "italian") | (df.genre2 == "italian")].sum(axis=0)
# tag_counts_for_texmex = df.iloc[:,3:10].loc[(df.genre1 == "texmex") | (df.genre2 == "texmex")].sum(axis=0)
# tag_counts_for_spanish = df.iloc[:,3:10].loc[(df.genre1 == "spanish") | (df.genre2 == "spanish")].sum(axis=0)


# new_df = pd.DataFrame({"french": tag_counts_for_french, 
#                        "italian": tag_counts_for_italian,
#                        "texmex": tag_counts_for_texmex,
#                        "spanish": tag_counts_for_spanish})

# print(new_df.transpose())

# genre_names = df.genre1.tolist() + df.genre2.tolist()
# genre_names = list(set(genre_names))
# # print(genre_names)

# occ_df = pd.DataFrame(np.zeros((4,8)), columns = ["genre",
#                                             "tag1", 
#                                             "tag2",
#                                             "tag3",
#                                             "tag4",
#                                             "tag5",
#                                             "tag6",
#                                             "tag7"])
# # print(occ_df)

# for i in range(len(genre_names)):

#     action_tag_totals = df.iloc[:,3:10].loc[df.genre1 == genre_names[i]].sum(axis=0).tolist()
#     # print(action_tag_totals)

#     occ_df.loc[i,["genre",
#                     "tag1", 
#                     "tag2",
#                     "tag3",
#                     "tag4",
#                     "tag5",
#                     "tag6",
#                     "tag7"]] = [genre_names[i]] + action_tag_totals


# print(occ_df)