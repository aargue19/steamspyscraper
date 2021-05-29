import pandas as pd
import requests
import json












# response = requests.get(f'https://steamspy.com/api.php?request=appdetails&appid=573120').text

# response_info = json.loads(response)

# owners_string = response_info['owners']

# owners_vals = owners_string.split(" .. ")

# clean_owners_vals = []

# for string in owners_vals:
#     new_string = string.replace(",", "")
#     clean_owners_vals.append(new_string)

# print(clean_owners_vals)

# final_df = pd.read_csv("test4444.csv")

# genres_df = pd.read_csv("test6666.csv")

# # merge with previous file

# mgd_df = pd.merge(final_df, genres_df, on="app_id")

# mgd_df.to_csv("final_df.csv", index=False)