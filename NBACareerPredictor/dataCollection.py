import pandas as pd
import time

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players

active_players = players.get_active_players()

nba_college_stats = pd.read_csv("data/college_seasons.csv")

df_list = []

for player in active_players:
    full_name = player['full_name']
    try:
        df = nba_college_stats[nba_college_stats["player"] == full_name]
        df_list.append(df)
    except Exception as e:
        print(f"Error finding college stats for {full_name}, {e}")
    time.sleep(0.6)

final_df = pd.concat(df_list, ignore_index=True)
final_df.to_csv("data/NBAPlayerCollegeStats.csv", index=False)


