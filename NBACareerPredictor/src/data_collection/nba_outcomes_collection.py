import pandas as pd
import time

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players

college = pd.read_csv("data/FinalNBACollegeStats.csv")
college2 = pd.read_csv("data/FinalNBACollegeStats2.csv")
intl = pd.read_csv("data/FinalNBAInternationalStats.csv")

all_names = pd.concat([college["Name"], college2["Name"], intl["Name"]]).drop_duplicates().to_list()

def find_player_id(name):
    matches = players.find_players_by_full_name(name)
    if len(matches) == 0:
        return None
    return matches[0]["id"]

def get_nba_career_data(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]
    totals = df[df["LEAGUE_ID"] == "00"]

    #Career Totals
    career_mp = totals["MIN"].sum()
    career_ws = totals["WS"].sum()
    career_vorp = totals["VORP"].sum()

    #Awards
    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    info_df = info.get_data_frames()[0]
    all_star = info_df["ALL_STAR_APPEARANCES"].iloc[0]
    all_nba = info_df["ALL_NBA_SELECTIONS"].iloc[0]

    return career_mp, career_ws, career_vorp, all_star, all_nba

def classify_player(mp, ws, vorp, all_star, all_nba):
    if ws >= 80 or vorp >= 40 or all_nba >= 3:
        return "superstar"

    if all_star >= 1 or 40 <= ws < 80 or 15 <= vorp < 40:
        return "all_star"
    
    if mp >= 12000 or 15 <= ws < 40 or 5 <= vorp < 15:
        return "starter"
    
    return "rotational"

rows = []
for name in all_names:
    pid = find_player_id(name)
    if pid is None:
        continue
    mp, ws, vorp, all_star, all_nba = get_nba_career_data(pid)
    label = classify_player(mp, ws, vorp, all_star, all_nba)

    rows.append({
        "Name": name,
        "Career_MP": mp,
        "Career_WS": ws,
        "Career_VORP": vorp,
        "All_Star_Selections": all_star,
        "All_NBA_Selections": all_nba,
        "OutcomeClass": label
    })

nba_outcomes = pd.DataFrame(rows)
nba_outcomes.to_csv("NBAOutcomes.csv", index=False)

