import pandas as pd

cleaned_nba_college_data = pd.read_csv("data/NBAPlayerCollegeStats.csv")
raw_nba_college_data = pd.read_csv("data/NBAPlayerCollegeStats.csv")

#Removes the previous college years, keeps the latest year
cleaned_nba_college_data = cleaned_nba_college_data.drop_duplicates(subset=['player'], keep='last')

#Removes the wrong Donovan Mitchell in the sheet
names_to_remove = ['Donovan Mitchell', 'Kyle Anderson', 'Gary Harris', 'Isaiah Jackson', 'Cameron Johnson', 'Jalen Johnson', 'Tre Jones', 'AJ Lawson', ' Isaiah Stevens', 'Brandon Williams', 'Grant Williams', ' Jaylin Williams']
rows_to_add = [726, 26, 361, 429, 471, 485, 515, 527, 596, 1004, 1136, 1141, 1155]

for player in names_to_remove:
    cleaned_nba_college_data = cleaned_nba_college_data[cleaned_nba_college_data['player'] != player]

df_list = []
for row in rows_to_add:
    df1 = raw_nba_college_data.iloc[[row]]
    df_list.append(df1)

cleaned_new_players = pd.concat(df_list, ignore_index=True)
cleaned_nba_college_data = pd.concat([cleaned_nba_college_data, cleaned_new_players], ignore_index=True)


cleaned_nba_college_data.to_csv("data/CleanedNBACollegeStats.csv", index=False)
