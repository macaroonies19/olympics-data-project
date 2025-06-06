import pandas as pd
#week 3
df = pd.read_csv("athlete_events.csv")

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(len(female_athletes.head()))

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(len(older_athletes[['Name', 'Age', 'Sport']].head()))

# Filter for athletes from Australia in swimming
aussie_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(aussie_swimmers.head())
