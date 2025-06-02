print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts())

print(df.describe())

print(df['NOC'].nunique())
print(df['NOC'].unique())
