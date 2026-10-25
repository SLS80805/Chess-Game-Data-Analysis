# Chess Games Data Analysis

## 📊 Project Overview

This project performs exploratory data analysis on a dataset of chess games. The analysis focuses on understanding game outcomes, player ratings, game duration, chess openings, victory status, and patterns in when games are played.

The project uses Python, Pandas, NumPy, Matplotlib, and Seaborn for data cleaning, analysis, and visualization.

---

## 🎯 Objectives

The main objectives of this project are:

- Understand the structure and characteristics of the chess games dataset
- Clean and preprocess the raw data
- Analyze game outcomes and victory status
- Compare player ratings and rating differences
- Identify the most frequently played chess openings
- Analyze the relationship between player ratings and game duration
- Study game activity by month and hour
- Compare rated and unrated games
- Explore correlations between numerical variables
- Create visualizations to identify patterns and trends

---

## 📁 Dataset

The original dataset contains chess game records with information such as:

- Game ID
- Rated/Unrated status
- Game creation time
- Last move time
- Number of turns
- Victory status
- Winner
- Increment code
- White player ID
- White player rating
- Black player ID
- Black player rating
- Opening ECO
- Opening name
- Opening ply
- Moves

The dataset contains **20,058 chess games and 16 columns**.

---

## 🗂️ Project Structure

```text
Chess-Games-Data-Analysis/
│
├── games.csv.xlsx
├── cleaned_data.csv
├── DA_Project_Games.py
└── README.md
```

### Files

**`games.csv.xlsx`**  
Original/raw dataset used for the analysis.

**`cleaned_data.csv`**  
Processed dataset generated after data cleaning and feature engineering.

**`DA_Project_Games.py`**  
Python script containing the complete data analysis, statistical analysis, and visualizations.

**`README.md`**  
Project documentation.

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

1. Removed duplicate records.
2. Converted `created_at` from Unix timestamp milliseconds into datetime format.
3. Converted `last_move_at` from Unix timestamp milliseconds into datetime format.
4. Removed the `moves` column from the analysis dataset.
5. Created additional features for analysis.

### Feature Engineering

The following features were created:

- **`rating_difference`** – absolute difference between White and Black player ratings.
- **`average_rating`** – average rating of the two players.
- **`game_year`** – year in which the game was created.
- **`game_month`** – month in which the game was created.
- **`game_hour`** – hour in which the game was created.

After cleaning, missing values and duplicate records were checked again.

---

## 📈 Analysis Performed

### Game Outcome Analysis

The project analyzes:

- Number of games won by White, Black, or resulting in a draw
- Victory status
- Rated vs. unrated games
- Relationship between winner and victory status

### Player Rating Analysis

The project examines:

- White player ratings
- Black player ratings
- Average player rating
- Rating difference between players
- Rating differences by winner

### Chess Opening Analysis

The analysis identifies:

- Most frequently played openings
- Number of games for each opening
- Average number of turns for popular openings
- Average rating associated with different openings

### Game Duration Analysis

The project studies:

- Distribution of game turns
- Average turns by winner
- Game turns by winner
- Relationship between player ratings and number of turns

### Time-Based Analysis

Game activity is analyzed by:

- Month
- Hour of the day

This helps identify when chess games were most frequently played.

### Correlation Analysis

A correlation matrix and heatmap are used to explore relationships between numerical variables.

---

## 📊 Visualizations

The project contains multiple visualizations, including:

- Winner distribution
- Victory status distribution
- Rated vs. unrated games
- Top 10 chess openings
- White rating distribution
- Black rating distribution
- Game turns distribution
- Rating difference distribution
- Average turns by winner
- Average rating by winner
- Game turns by winner
- Rating difference by winner
- White rating vs. Black rating
- Average rating vs. game turns
- Games by month
- Games by hour
- Average turns for top openings
- Winner vs. victory status
- Rated games vs. winner
- Correlation heatmap

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – data manipulation and analysis
- **NumPy** – numerical operations
- **Matplotlib** – data visualization
- **Seaborn** – statistical visualization

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Chess-Games-Data-Analysis
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### 4. Run the Python script

```bash
python DA_Project_Games.py
```

The script will perform the analysis and generate the visualizations. It will also create the processed dataset:

```text
cleaned_data.csv
```

---

## 🔍 Key Areas of Investigation

Some of the main questions explored in this project are:

- Which player wins more frequently?
- What are the most popular chess openings?
- Does player rating difference vary depending on the winner?
- How does game length differ between winners?
- What is the relationship between player ratings and game duration?
- When are chess games most frequently played?
- How do rated and unrated games differ?
- Which openings are associated with longer or shorter games?

---

## 🚀 Future Improvements

Possible future improvements include:

- Building an interactive dashboard using Power BI, Tableau, or Streamlit
- Performing statistical hypothesis testing
- Analyzing individual player performance
- Performing deeper opening-level win-rate analysis
- Building a machine learning model to predict the winner
- Adding more advanced feature engineering
- Creating interactive visualizations

---

## 👤 Author

**Sakshi**

This project was created as a data analytics project to practice data cleaning, exploratory data analysis, feature engineering, statistical analysis, and data visualization using Python.
