import pandas as pd
data = {'이름': ['Kim', 'park', 'Lee', 'Ho'],
        '국어': [90, 58, 88, 100],
        '영어': [100, 60, 80, 70],
        '수학': [55, 65, 76, 88] }
#1
df = pd.DataFrame(data)
#2
print(df ,end="\n\n")
#3
sr_name = df['이름']
print(sr_name, end="\n\n")
#4
park_data = df.loc[1]
park_data = df.loc[df['이름'] == 'Park']
print(park_data, end="\n\n")
#5
df.loc[df['이름'] == 'Ho', '수학'] = 90
print (df, end="\n\n")
#6
df.loc[3] = ['Oh', 100 , 70, 80]
print(df, end="\n\n")
#7
df = df.drop([2], axis=0)
print(df, end="\n\n")
