import pandas as pd
#week 4
df = pd.read_csv("athlete_events.csv")

# Count missing values in each column
print(df.isnull().sum())

# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)