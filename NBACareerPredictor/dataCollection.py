import pandas as pd
import time

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players

players = players.get_active_players()



