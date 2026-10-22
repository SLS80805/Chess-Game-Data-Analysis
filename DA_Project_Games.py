import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load Data
df = pd.read_excel("games.csv.xlsx")
print(df.head())
print(df.tail())
# Data Understanding
print("\nShape:", df.shape)
print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn Names:")
print(df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
print("\nUnique Values:")
print(df.nunique())
# Data Cleaning
df = df.drop_duplicates()
df["created_at"] = pd.to_datetime(
    df["created_at"], unit="ms"
)
df["last_move_at"] = pd.to_datetime(
    df["last_move_at"], unit="ms"
)
df = df.drop(columns=["moves"])
# Feature Creation
df["rating_difference"] = abs(
    df["white_rating"] - df["black_rating"]
)
df["average_rating"] = (
    df["white_rating"] + df["black_rating"]
) / 2
df["game_year"] = df["created_at"].dt.year
df["game_month"] = df["created_at"].dt.month
df["game_hour"] = df["created_at"].dt.hour
# Final Cleaning Check
print("\nAfter Cleaning")
print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Categorical Analysis
print("\nWinner Count:")
print(df["winner"].value_counts())
print("\nVictory Status:")
print(df["victory_status"].value_counts())
print("\nRated Games:")
print(df["rated"].value_counts())
print("\nTop Openings:")
print(df["opening_name"].value_counts().head(10))
print("\nTop Victory Reasons:")
print(df["victory_status"].value_counts())

# Numerical Analysis
print("\nWhite Rating:")
print(df["white_rating"].describe())
print("\nBlack Rating:")
print(df["black_rating"].describe())
print("\nGame Turns:")
print(df["turns"].describe())
print("\nRating Difference:")
print(df["rating_difference"].describe())
print("\nAverage Rating:")
print(df["average_rating"].mean())
print("\nAverage Turns:")
print(df["turns"].mean())

# Group Analysis
print("\nAverage Turns by Winner:")
print( df.groupby("winner")["turns"].mean()
)
print("\nAverage Rating by Winner:")
print(df.groupby("winner")["average_rating"].mean())
print("\nAverage Rating Difference by Winner:")
print( df.groupby("winner")["rating_difference"].mean())
print("\nGames by Opening:")
print(df.groupby("opening_name")["id"]
    .count()
    .sort_values(ascending=False)
    .head(10))

# Opening Analysis
opening_analysis = df.groupby("opening_name").agg(
    games=("id", "count"),
    average_turns=("turns", "mean"),
    average_rating=("average_rating", "mean"))
opening_analysis = opening_analysis.sort_values(
    "games", ascending=False)
print("\nOpening Analysis:")
print(opening_analysis.head(10))

# Winner and Victory Analysis
winner_status = pd.crosstab(
    df["winner"],
    df["victory_status"])
print("\nWinner vs Victory Status:")
print(winner_status)

# Rated and Winner Analysis
rated_winner = pd.crosstab(
    df["rated"],
    df["winner"])
print("\nRated vs Winner:")
print(rated_winner)

# Monthly Analysis
monthly_games = df.groupby("game_month").size()
print("\nGames by Month:")
print(monthly_games)

# Hourly Analysis
hourly_games = df.groupby("game_hour").size()
print("\nGames by Hour:")
print(hourly_games)

# Correlation
numeric_df = df.select_dtypes(include=np.number)
print("\nCorrelation:")
print(numeric_df.corr())

# Visualizations
sns.set_style("whitegrid")
# 1 Winner Distribution
plt.figure(figsize=(7,5))
sns.countplot(data=df,x="winner")
plt.title("Games by Winner")
plt.xlabel("Winner")
plt.ylabel("Number of Games")
plt.show()
# 2 Victory Status
plt.figure(figsize=(8,5))
sns.countplot(data=df,x="victory_status")
plt.title("Victory Status Distribution")
plt.xlabel("Victory Status")
plt.ylabel("Number of Games")
plt.xticks(rotation=20)
plt.show()
# 3 Rated vs Unrated
plt.figure(figsize=(7,5))
sns.countplot(data=df,x="rated")
plt.title("Rated vs Unrated Games")
plt.xlabel("Rated")
plt.ylabel("Number of Games")
plt.show()
# 4 Top 10 Openings
plt.figure(figsize=(10,6))
top_openings = (
    df["opening_name"]
    .value_counts()
    .head(10)
    .sort_values())
top_openings.plot(kind="barh")
plt.title("Top 10 Most Played Openings")
plt.xlabel("Number of Games")
plt.ylabel("Opening")
plt.show()
# 5 White Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["white_rating"],bins=30,kde=True)
plt.title("White Player Rating Distribution")
plt.xlabel("White Rating")
plt.ylabel("Frequency")
plt.show()
# 6 Black Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["black_rating"],bins=30,kde=True)
plt.title("Black Player Rating Distribution")
plt.xlabel("Black Rating")
plt.ylabel("Frequency")
plt.show()
# 7 Game Turns Distribution
plt.figure(figsize=(8,5))
sns.histplot( df["turns"],bins=30, kde=True)
plt.title("Game Turns Distribution")
plt.xlabel("Number of Turns")
plt.ylabel("Frequency")
plt.show()
# 8 Rating Difference
plt.figure(figsize=(8,5))
sns.histplot( df["rating_difference"],bins=30,kde=True)
plt.title("Rating Difference Distribution")
plt.xlabel("Rating Difference")
plt.ylabel("Frequency")
plt.show()
# 9 Average Turns by Winner
plt.figure(figsize=(7,5))
sns.barplot(data=df,x="winner",y="turns",estimator="mean")
plt.title("Average Game Turns by Winner")
plt.xlabel("Winner")
plt.ylabel("Average Turns")
plt.show()
# 10 Average Rating by Winner
plt.figure(figsize=(7,5))
sns.barplot(data=df,x="winner",y="average_rating",estimator="mean")
plt.title("Average Player Rating by Winner")
plt.xlabel("Winner")
plt.ylabel("Average Rating")
plt.show()
# 11 Turns by Winner
plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="winner", y="turns")
plt.title("Game Turns by Winner")
plt.xlabel("Winner")
plt.ylabel("Turns")
plt.show()
# 12 Rating Difference by Winner
plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="winner", y="rating_difference")
plt.title("Rating Difference by Winner")
plt.xlabel("Winner")
plt.ylabel("Rating Difference")
plt.show()
# 13 White Rating vs Black Rating
sample = df.sample(
    min(3000, len(df)),
    random_state=42)
plt.figure(figsize=(8,6))
sns.scatterplot(data=sample,x="white_rating",y="black_rating",hue="winner")
plt.title("White Rating vs Black Rating")
plt.xlabel("White Rating")
plt.ylabel("Black Rating")
plt.show()
# 14 Rating vs Turns
plt.figure(figsize=(8,6))
sns.scatterplot( data=sample, x="average_rating", y="turns", hue="winner")
plt.title("Average Rating vs Game Turns")
plt.xlabel("Average Rating")
plt.ylabel("Game Turns")
plt.show()
# 15 Games by Month
plt.figure(figsize=(8,5))
monthly_games.plot( kind="line",marker="o")
plt.title("Games by Month")
plt.xlabel("Month")
plt.ylabel("Number of Games")
plt.xticks(range(1,13))
plt.show()
# 16 Games by Hour
plt.figure(figsize=(9,5))
hourly_games.plot(kind="line",marker="o")
plt.title("Games by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Games")
plt.show()
# 17 Top Openings by Average Turns
top10 = (
    df["opening_name"]
    .value_counts()
    .head(10)
    .index)
opening_turns = (
    df[df["opening_name"].isin(top10)]
    .groupby("opening_name")["turns"]
    .mean().sort_values())
plt.figure(figsize=(10,6))
opening_turns.plot(kind="barh")
plt.title("Average Turns of Top Openings")
plt.xlabel("Average Turns")
plt.ylabel("Opening")
plt.show()
# 18 Winner vs Victory Status
plt.figure(figsize=(8,5))
sns.countplot(data=df,x="winner", hue="victory_status")
plt.title("Winner vs Victory Status")
plt.xlabel("Winner")
plt.ylabel("Number of Games")
plt.show()
# 19 Rated vs Winner
plt.figure(figsize=(8,5))
sns.countplot(data=df,x="rated",hue="winner")
plt.title("Rated Games by Winner")
plt.xlabel("Rated")
plt.ylabel("Number of Games")
plt.show()
# 20 Correlation Heatmap
plt.figure(figsize=(11,8))
sns.heatmap(numeric_df.corr(),annot=True,fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
# Save Clean Data
df.to_csv("cleaned_data.csv",index=False)
print("\nCleaned dataset saved successfully!")