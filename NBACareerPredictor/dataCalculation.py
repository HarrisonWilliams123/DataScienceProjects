import pandas as pd
import numpy as np


#Python script to calculate PER, 3PAr, PProd, TRB%, OWS, DWS, WS, WS/40


df = pd.read_csv("data/TestNBACollegeStats.csv")

def safe_div(a, b):
    return np.where(b == 0, 0, a / b)

#3PAr Calculation
df['3PAr'] = np.round(safe_div(df['3PA'], df['FGA']), 3)

#PProd (Points Produced)
FGProd = 2 * (df['FG'] - df['3P']) + 3 * df['3P']
ASTProd = 0.5 * df['AST']
FTProd = df['FT']

df['PProd'] = np.round(FGProd + ASTProd + FTProd, 0)


#TRB% Calculation
df["TRB%"] = np.round((
    df["ORB%"] * df["ORB"] + df["DRB%"] * df["DRB"]
) / (df["ORB"] + df["DRB"]), 1)

#PER Calculation
df["factor"] = (2/3) - (0.5 * ((safe_div(df["AST"], df["FG"])) / (2 * safe_div(df["FG"], df["FT"])) ))



uPER = (
    df["3P"]
    + (2/3) * df["AST"]
    + (2 - df["factor"] * safe_div(df["AST"], df["FG"])) * df["FG"]
    + df["FT"] * 0.5 * (1 + safe_div(1 - safe_div(df["AST"], df["FG"]), 2))
    - safe_div(df["FGA"] - df["FG"], 1)
    - safe_div(df["FTA"] - df["FT"], 1)
    + df["TRB"]
    + df["STL"]
    + df["BLK"]
    - df["TOV"]
)

df["uPER"] = safe_div(uPER, df["MP"])

#Normalize PER to league pace (college standard)
LEAGUE_PACE= 70.0
df["PER"] = np.round(df["uPER"] * LEAGUE_PACE, 1)


#OWS, DWS, WS, WS/40
df["TeamMinutes"] = 5 * df["G"] * 40

#Win Shares Formula
df["OWS"] = np.round(safe_div(df["MP"], df["TeamMinutes"]) * (df["ORTG"] / 100) * df["G"], 1)
df["DWS"] = np.round(safe_div(df["MP"], df["TeamMinutes"]) * ((100 - df["DRTG"]) / 100) * df["G"], 1)

df["WS"] = df["OWS"] + df["DWS"]
df["WS/40"] = np.round(40 * safe_div(df["WS"], df["MP"]), 3)

df.to_csv("data/NBA_College_Advanced_Stats.csv")
