import pandas as pd
import time

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players

active_players = players.get_active_players()

#nba_college_stats = pd.read_csv("data/college_seasons.csv")

df_list = []

active_df = pd.read_csv("data/ActiveNBAPlayerNames.csv")
active_df = active_df[active_df['0'] != "Full Name"]
active_df.to_csv("data/CleanedActiveNBAPlayerNames.csv", index=False)

#Loop that gets all active nba players names and creates a dataframe with their college stats
#for player in active_players:
    #full_name = player['full_name']
    #df = pd.DataFrame({"Full Name", full_name})
    #df_list.append(df)
    #try:
        #df = nba_college_stats[nba_college_stats["player"] == full_name]
        #df_list.append(df)
    #except Exception as e:
        #print(f"Error finding college stats for {full_name}, {e}")
    #time.sleep(0.6)

#final_df = pd.concat(df_list, ignore_index=True)
#final_df.to_csv("data/ActiveNBAPlayerNames.csv", index=False)


