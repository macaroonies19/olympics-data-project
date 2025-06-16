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
print("Total rows:", len(aussie_swimmers)) # Atheltes from Australia in swimming

# Sort by height
sorted_by_height = df.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count sport with most female participants
females_per_sport = df[df['Sex'] == 'F']['Sport'].value_counts()
print(females_per_sport.head(1))

# Average height per sport
avg_height = df.groupby('Sport')['Height'].mean().sort_values(ascending=False)
print(avg_height.head())

# Median age by year
median_age_by_year = df.groupby('Year')['Age'].median()
print(median_age_by_year.tail())

# Average weight by sex and sport
avg_weight = df.groupby(['Sport', 'Sex'])['Weight'].mean().sort_values(ascending=False)
print(avg_weight.head())

# Filter gymnasts and save to new CSV
gymnasts = df[df['Sport'] == 'Gymnastics']
gymnasts.to_csv('gymnastics_athletes.csv', index=False)