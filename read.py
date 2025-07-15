import pandas as pd

df_premier24 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

df_premier24.rename(columns = {'FTHG':'home_goals' , 'FTAG':'away_goals'}, inplace = True)

print(df_premier24)
