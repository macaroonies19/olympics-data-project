# ***Week 2***

# Activity 1: Describe the Dataset
## 1. How many columns are in the dataset?
- There are 15 Coloumns in the dataset.
## 2. Name 3 of them and explain what they represent.
- Name: Represents the persons name.
- Sport: Represents what sport the person is playing in the event.
- Medal: Represents the medal they got for their sport, NaN = no medal.
## 3. What do the first 5 rows show?
- The first 5 rows is the head of the dataset.

# Activity 2
### What are the top 5 sports?
- Athletics, gymnastics, swimming, shooting, and cycling.
### How many male vs female athletes?
- There are 196,594 male and 74,522 female athletes.

# Activity 3: Quick Stats with describe()
### What’s the average age?
- 25.5 or 26 rounded up.
### What’s the oldest and youngest athlete?
- The oldest athlete is 97 and the youngest athlete is 10.
### Are there any columns with missing or strange values?
- Some values are missing and replaced with "NA".

# Extension: Explore Country Codes
### Research what three of the lesser-known codes stand for, e.g. URS, GDR, FRG.
- URS stands for the Soviet Union.
- GDR stands for the German Democratic Republic.
- FRG stands for the Federal Republic of Germany.

# Reflection
### What’s one thing you learned about the Olympics dataset?
- I learnt that even if your as young as a 10 year old, or as old as a 97 year old, anyone can compete in the Olympics if they have the skills for it.
### What did you find challenging in setting up or running Pandas?
- I had trouble setting up Pandas due to the connection problems, but I managed to download it later at home with a Python 3 command line the teacher helped me with.
### What’s something you'd like to analyse next?
- I think analysing the stock market would be interesting and useful.

# ***Week 3***

# Task 1: Filtering Basics
## Reflect:
### 1. What do these filters do?
- Show the first 5 rows of female athletes and athletes older than 35.
### 2. How many rows were returned? Use len().
- 5 rows were returned for each filter.

# Task 2: Combine Filters
## Create a new filter
### 1. Write a filter for athletes from Australia in Swimming
- aussie_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
  print(aussie_swimmers.head()) 
  print("Total rows:", len(aus_swimmers)) # Atheltes from Australia in swimming

# Task 3: Sorting Data
## Apply the skill
### 1. Sort by Height then Weight and display top 10.
- #Sort by height

  sorted_by_height = df.sort_values(by='Height', ascending=False)

  print(sorted_by_height[['Name', 'Height', 'Sport']].head())

- #Sort by weight

  sorted_by_weight = df.sort_values(by='Weight', ascending=False)

  print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Task 4: Grouping Data
## Apply the skill
  females_per_sport = df[df['Sex'] == 'F']['Sport'].value_counts()
  print(females_per_sport.head(1))
  ### 1. Which sport had the most female participants?
-  had the most female participants.

# Task 5: Aggregating with groupby()
## Challenge: Create a new group that shows average weight by Sex and Sport:
- avg_weight = df.groupby(['Sport', 'Sex'])['Weight'].mean().sort_values(ascending=False)
  print(avg_weight.head())
# Task 6: Exporting a Subset
## Try exporting:
### All athletes under 18
- #Filter under 18s and save to new CSV
  under18s = df[df['Age'] < 18]
  under18s.to_csv('under18_athletes.csv', index=False)
### All athletes who won a gold medal
- #Filter gold medalists and save to new CSV
  goldmedal = df[df['Medal'] == 'Gold']
  goldmedal.to_csv('goldmedals_athletes.csv', index=False)

# 📚 Reflection Journal
### 1. What was the easiest filtering task and why?
- Filtering for gold medals because I only had to only change a few things from the draft given.
### 2. What was the most difficult grouping or sorting task?
- Probably the australian swimmers one as I was on for it a while and needed help for it.
### 3. What trends surprised you in the Olympic data?
- That there are athletes that are only 15 years old.
### 4. What kinds of real-world questions could this kind of analysis help answer?
- What countries win the most gold medals, which sports are more dominated by males or females, ect.

# Task 1: Check for Missing Data
### Which 3 columns have the most missing values?
- Medal with 231333 missing values, Weight with 62875 missing values, and Height with 60171 missing values.
### Why might this happen in real-world Olympic data?
- Because with the large amount of data, mistakes may be made or data can be lost easily.

# Task 2: Drop Rows with Critical Missing Data
## Challenge:
### How many rows did you remove?
- 206868 in total.
### What are the pros and cons of dropping data?
- To make the charts cleaner.

# Task 3: Fill Missing Values (e.g. 'Medal')
## Add:
### .median() as well as .mean() and compare the results:
- The median and mean for age is only a 1.06 age difference, and an even lower difference between the means and medians of height and weight.

# Task 4: Detect Inconsistent Data
## Extra spaces or capitalisation issues
- Didn't see any.
## Typos or strange values
- Didn't see any.

# Task 5 Validate and Describe Cleaned Data
## Reflection:
### Did cleaning improve the dataset?
- It clumped up lows, averages, and highs, making it look kind of weird, but easier to collect data.
### What questions could now be answered more confidently?
- Statistical questions and questions about averages, lows, and highs.