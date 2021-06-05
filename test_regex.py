import pandas as pd

df = pd.read_csv("step2_result.csv")

print(df.columns)

#print(len(list(set(df['app_id'].tolist()))))

# import re
# # string = '<td data-order="100,000">100,000&nbsp;..&nbsp;200,000</font></td><td class="tplaytime" data-order="0">00:00 (00:00)</td><td data-order="Visual Concepts, Yuke">Visual Concepts, Yuke</td><td data-order="2K">2K</td></tr>'


# string='0.08"><a 688180="" <view-source:https:="" app="" href="/app/688180" steamspy.com="">&gt;<img class="img-ss-list" src="https://steamcdn-a.akamaihd.net/steam/apps/688180/capsule_184x69.jpg &lt;view-source:https://steamcdn-a.akamaihd.net/steam/apps/688180/capsule_184x69.jpg&gt;"/> 80.08</a></'

# if "src" not in string:
#     print("not")

