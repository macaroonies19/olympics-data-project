import pandas as pd
#week 4
df = pd.read_csv("athlete_events.csv")

# Count missing values in each column
print(df.isnull().sum())

# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

# Count missing values in each column
print(df.isnull().sum())

print("")
print("")
print("")


# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

print("")
print("")
print("")

# Fill missing medals with 'None'
df_cleaned.loc[:, 'Medal'] = df_cleaned['Medal'].fillna('None')

# Fill missing ages with average age
avg_age = df_cleaned['Age'].mean()
df_cleaned.loc[:, 'Age'] = df_cleaned['Age'].fillna(avg_age)

print(df_cleaned.head())

# Calculate and display mean and median for Age, Height, and Weight
for column in ['Age', 'Height', 'Weight']:
    mean_value = df_cleaned[column].mean()
    median_value = df_cleaned[column].median()
    print(f"{column} - Mean: {mean_value:.2f}, Median: {median_value:.2f}")

# Unique values in 'Sex' and 'Medal'
print(df_cleaned['Sex'].unique())
print(df_cleaned['Medal'].unique())

# Check again for missing values
print(df_cleaned.isnull().sum())

# Get stats after cleaning
print(df_cleaned.describe())