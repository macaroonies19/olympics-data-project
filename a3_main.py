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
print(aussie_swimmers.head()) # First 5 rows of atheltes from Australia in swimming

# Sort by height
sorted_by_height = df.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count females per sport
females_by_sport = df[df['Sport'].notnull()].groupby('Sex')['Sport'].count()
print(females_by_sport.sort_values(ascending=False).head())