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

  print(aussie_swimmers.head()) # First 5 rows of atheltes from Australia in swimming

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
  ### 1. Which sport had the most female participants?
  - * had the most female participants.