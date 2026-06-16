import pandas as pd

cleaned_nba_college_data = pd.read_csv("data/NBAPlayerCollegeStats.csv")
raw_nba_college_data = pd.read_csv("data/NBAPlayerCollegeStats.csv")

#Removes the previous college years, keeps the latest year
cleaned_nba_college_data = cleaned_nba_college_data.drop_duplicates(subset=['player'], keep='last')

#Removes the wrong nba players in the databases
names_to_remove = ['Donovan Mitchell', 'Kyle Anderson', 'Gary Harris', 'Isaiah Jackson', 'Cameron Johnson', 'Jalen Johnson', 'Isaac Jones', 'Tre Jones', 'AJ Lawson', ' Isaiah Stevens', 'Brandon Williams', 'Grant Williams', ' Jaylin Williams']
rows_to_add = [726, 26, 361, 429, 471, 485, 515, 527, 596, 1004, 1136, 1141, 1155]

#Removes the wrong nba player data 
for player in names_to_remove:
    cleaned_nba_college_data = cleaned_nba_college_data[cleaned_nba_college_data['player'] != player]

#Adds the correct nba player data
df_list = []
for row in rows_to_add:
    df1 = raw_nba_college_data.iloc[[row]]
    df_list.append(df1)

cleaned_new_players = pd.concat(df_list, ignore_index=True)
cleaned_nba_college_data = pd.concat([cleaned_nba_college_data, cleaned_new_players], ignore_index=True)

#Moves around the columns to match the nba prospects data
cleaned_nba_college_data = cleaned_nba_college_data[['player', 'team', 'conf', 'exp', 'pos', 'g', 'mpg', 'fgm', 'fga', 'fg_pct', 'three_m', 'three_a', 'three_pct', 'two_m', 'two_a', 'two_pct', 'efg', 'ftm', 'fta', 'ft_pct', 'oreb', 'dreb', 'rpg', 'apg', 'spg', 'bpg', 'tov', 'pfr', 'ppg', 'ortg', 'drtg', 'ts', 'ftr', 'oreb_rate', 'dreb_rate', 'ast', 'stl', 'blk', 'to', 'usg', 'obpm', 'dbpm', 'bpm']]
cleaned_nba_college_data = cleaned_nba_college_data.rename(columns={"player" : "Name","team": "Team", "conf": "Conf", "pos": "Pos", "exp": "Class", "g": "G", "mpg":"MP", "fgm":"FG", "fga":"FGA", "fg_pct":"FG%",  "three_m":"3P", "three_a":"3PA", "three_pct":"3P%", "two_m":"2P", "two_a":"2PA", "two_pct":"2P%", "efg":"eFG%", "ftm": "FT", "fta":"FTA", "ft_pct":"FT%", "oreb":"ORB", "dreb":"DRB", "rpg":"TRB", "apg":"AST", "spg":"STL", "bpg":"BLK", "tov":"TOV", "pfr":"PF", "ppg":"PTS", "ortg":"ORTG", "drtg":"DRTG", "ts":"TS%", "ftr":"FTr", "oreb_rate":"ORB%", "dreb_rate":"DRB%", "ast":"AST%", "stl":"STL%", "blk":"BLK%", "to":"TOV%", "usg":"USG%", "obpm":"OBPM", "dbpm":"DBPM", "bpm": "BPM"})

cleaned_nba_college_data.to_csv("data/ComparedNBACollegeStats.csv", index=False)
