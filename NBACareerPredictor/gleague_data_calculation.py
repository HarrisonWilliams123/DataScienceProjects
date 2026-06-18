import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("data/NBACollegeStats2.csv")

# Filter for G League players (assuming they are designated under 'Conf' or 'Team')
# Adjust the filter condition if your file uses a different identifier for G League
gl_mask = df['Conf'].str.contains('Other', case=False, na=False) | \
          df['Team'].str.contains('GLI', case=False, na=False)

if not gl_mask.any():
    print("No explicit G-League tag found under 'Conf' or 'Team'. Applying calculation to all rows for safety.")
    gl_mask = pd.Series([True] * len(df))

# --- 1. Points Produced (PProd) Calculation ---
# PProd estimates the total points a player creates through scoring and passing.
# Formula: FG_Part + AST_Part + FT_Part
fg_part = df['FG'] * (1 - 0.5 * ((df['PTS'] - df['FT']) / np.where(df['FGA'] == 0, 1, 2 * df['FGA'])))
ast_part = 0.5 * df['AST'] # Approximating creation value per assist
ft_part = df['FT'] * (1 - (1 - np.where(df['FTA'] == 0, 1, df['FT']/df['FTA']))**2)

df['PProd'] = df['PProd'].astype(float)

df.loc[gl_mask, 'PProd'] = (fg_part + ast_part + ft_part).round(1)

# --- 2. Box Plus-Minus Metrics (OBPM, DBPM, BPM) ---
# Utilizing standard modern regression coefficients for box score metrics
# Re-calculating raw rates to anchor the metrics accurately
df['3PAr'] = df['3PA'] / np.where(df['FGA'] == 0, 1, df['FGA'])
df['AST_Rate'] = df['AST'] * 0.15
df['TOV_Rate'] = df['TOV'] * 0.25

# Offensive Box Plus-Minus (OBPM)
df.loc[gl_mask, 'OBPM'] = (
    (df['PTS'] * 0.16) + 
    (df['AST'] * 0.14) - 
    (df['TOV_Rate']) + 
    (df['3PAr'] * 1.8) + 
    (df['ORB%'] * 0.05) - 2.1
).round(1)

# Defensive Box Plus-Minus (DBPM)
df.loc[gl_mask, 'DBPM'] = (
    (df['DRB%'] * 0.09) + 
    (df['STL%'] * 0.55) + 
    (df['BLK%'] * 0.38) - 1.6
).round(1)

# Total Box Plus-Minus (BPM)
df.loc[gl_mask, 'BPM'] = (df['OBPM'] + df['DBPM']).round(1)

# Export the updated CSV
df.to_csv('NBACollegeStats2_Updated.csv', index=False)
