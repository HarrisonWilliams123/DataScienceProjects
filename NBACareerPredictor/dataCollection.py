from nba_api.stats.endpoints import playercareerbycollege, commonplayerinfo, playercareerstats
from nba_api.stats.static import players
import pandas as pd
import time

active_players = players.get_active_players()
#Method to find their full names

df_list = []

for player in active_players:
    player_id = player['id']
    #full_name = player['full_name']

    try:
        player_data = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        df1 = player_data.get_data_frames()[0]
        #df2 = player_data.get_data_frames()[1]

        #school = df1['SCHOOL']
        #basic = df2[['PLAYER_ID', 'PLAYER_NAME']]

        #result_df = pd.concat([basic.reset_index(drop=True), school.reset_index(drop=True)], axis=1)

        df_list.append(df1)
    except Exception as e:
        print(f"Failed to retrieve data for ID {player_id}: {e}")
    time.sleep(0.6)

final_df = pd.concat(df_list, ignore_index=True)

final_df.to_csv("data/NBAPlayerSchools.csv")


