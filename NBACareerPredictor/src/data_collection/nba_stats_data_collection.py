import pandas as pd
import time

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, boxscoreadvancedv3
from nba_api.stats.static import players

active_players = players.get_active_players()

df_list = []

for player in active_players:

    full_name = player['full_name']
    id = player['id']

    career = playercareerstats.PlayerCareerStats(player_id=id)
    career_totals_df = career.get_data_frames()[0]

    #box_stats = boxscoreadvancedv3.BoxScoreAdvancedV3()
    #box_stats_df = box_stats.get_data_frames()[0]

    name_df = pd.DataFrame({"Name": [full_name]})

    career_totals_df = career_totals_df.reset_index(drop=True)
    #box_stats_df = box_stats_df.reset_index(drop=True)

    combined = pd.concat([name_df, career_totals_df], axis=1)

    df_list.append(combined)
    time.sleep(0.6)

final_df = pd.concat(df_list, ignore_index=True)
final_df.to_csv("data/TestNBAStats.csv", index=False)

