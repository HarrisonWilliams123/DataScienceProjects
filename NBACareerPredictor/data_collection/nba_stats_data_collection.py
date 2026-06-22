import pandas as pd
import time

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, BoxScoreAdvancedV3
from nba_api.stats.static import players

active_players = players.get_active_players()

df_list = []

for player in active_players:
    full_name = player['full_name']
