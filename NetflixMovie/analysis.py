import pandas as pd
import os

movie_data = pd.read_csv("mymoviedb.csv", engine="python", on_bad_lines="skip")

print(movie_data)