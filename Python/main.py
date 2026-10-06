# ==========================================
# IPL DATA ANALYSIS Project
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)

# Load IPL datasets
matches = pd.read_csv("Dataset/IPL_Cleaned_Matches.csv")
deliveries = pd.read_csv("Dataset/IPL_Cleaned_Deliveries.csv")

print("IPL DATA LOADED SUCCESSFULLY")
print("-" * 40)

print("Matches shape:", matches.shape)
print("Deliveries shape:", deliveries.shape)

print("\nFirst 5 matches:")
print(matches.head())

print("\nFirst 5 deliveries:")
print(deliveries.head())

# ==========================================
# PART 2: DATA EXPLORATION & CLEANING
# ==========================================

print("\n" + "=" * 50)
print("DATA EXPLORATION & CLEANING")
print("=" * 50)

# 1. Check data types
print("\n--- Data Types ---")
print(matches.dtypes)

# 2. Basic statistical information
print("\n--- Statistical Summary ---")
print(matches.describe(include="all"))

# 3. Check missing values
print("\n--- Missing Values in Matches ---")
print(matches.isnull().sum())

print("\n--- Missing Values in Deliveries ---")
print(deliveries.isnull().sum())

# 4. Check duplicate records
print("\n--- Duplicate Records ---")
print("Duplicate matches:", matches.duplicated().sum())
print("Duplicate deliveries:", deliveries.duplicated().sum())

# 5. Unique values in important columns
print("\n--- Unique Seasons ---")
print(matches["season"].unique())

print("\n--- Teams ---")
teams = sorted(
    set(matches["team1"].dropna()) |
    set(matches["team2"].dropna())
)
print(teams)

print("\n--- Toss Decisions ---")
print(matches["toss_decision"].value_counts())

print("\n--- Match Results ---")
print(matches["result"].value_counts())

# 6. Dataset information
print("\n--- Matches Information ---")
matches.info()

print("\n--- Deliveries Information ---")
deliveries.info()

# ==========================================
# DATA CLEANING
# ==========================================

print("\n" + "=" * 50)
print("DATA CLEANING")
print("=" * 50)

# 1. Convert date column to proper date format
matches["date"] = pd.to_datetime(matches["date"], errors="coerce")

# 2. Remove duplicate records
matches = matches.drop_duplicates()
deliveries = deliveries.drop_duplicates()

# 3. Fill missing values in important categorical columns
matches["city"] = matches["city"].fillna("Unknown")
matches["player_of_match"] = matches["player_of_match"].fillna("Unknown")
matches["winner"] = matches["winner"].fillna("Unknown")

# 4. Fill missing numeric values
matches["result_margin"] = matches["result_margin"].fillna(0)
matches["target_runs"] = matches["target_runs"].fillna(0)
matches["target_overs"] = matches["target_overs"].fillna(0)

# 5. Clean delivery data
deliveries["extras_type"] = deliveries["extras_type"].fillna("None")
deliveries["player_dismissed"] = deliveries["player_dismissed"].fillna("None")
deliveries["dismissal_kind"] = deliveries["dismissal_kind"].fillna("None")
deliveries["fielder"] = deliveries["fielder"].fillna("None")

# 6. Standardize team names
team_name_mapping = {
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Kings XI Punjab": "Punjab Kings",
    "Delhi Daredevils": "Delhi Capitals",
    "Rising Pune Supergiants": "Rising Pune Supergiant"
}

team_columns = ["team1", "team2", "toss_winner", "winner"]

for column in team_columns:
    matches[column] = matches[column].replace(team_name_mapping)

deliveries["batting_team"] = deliveries["batting_team"].replace(
    team_name_mapping
)

deliveries["bowling_team"] = deliveries["bowling_team"].replace(
    team_name_mapping
)

# 7. Check cleaned data
print("\n--- Cleaned Matches Shape ---")
print(matches.shape)

print("\n--- Cleaned Deliveries Shape ---")
print(deliveries.shape)

print("\n--- Remaining Missing Values in Matches ---")
print(matches.isnull().sum())

print("\n--- Remaining Missing Values in Deliveries ---")
print(deliveries.isnull().sum())

print("\n--- Duplicate Records After Cleaning ---")
print("Matches:", matches.duplicated().sum())
print("Deliveries:", deliveries.duplicated().sum())

print("\n--- Date Data Type ---")
print(matches["date"].dtype)

print("\nDATA CLEANING COMPLETED!")

# ==========================================
# PART 3: IPL DATA ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("IPL DATA ANALYSIS")
print("=" * 50)

# 1. Total number of matches
total_matches = matches["id"].nunique()

print("\n1. Total Number of Matches:")
print(total_matches)


# 2. Matches played in each season
matches_by_season = matches.groupby("season")["id"].nunique()

print("\n2. Matches Played in Each Season:")
print(matches_by_season)


# 3. Matches won by each team
wins_by_team = matches["winner"].value_counts()

print("\n3. Matches Won by Each Team:")
print(wins_by_team)


# 4. Team with highest number of wins
highest_wins_team = wins_by_team.idxmax()
highest_wins = wins_by_team.max()

print("\n4. Team with Highest Number of Wins:")
print(highest_wins_team, "-", highest_wins, "wins")


# 5. Team with lowest number of wins
lowest_wins_team = wins_by_team.idxmin()
lowest_wins = wins_by_team.min()

print("\n5. Team with Lowest Number of Wins:")
print(lowest_wins_team, "-", lowest_wins, "wins")


# 6. Most successful Player of the Match
player_of_match = matches["player_of_match"].value_counts()

print("\n6. Most Successful Player of the Match:")
print(player_of_match.head(10))


# 7. Most frequently used venue
venue_count = matches["venue"].value_counts()

print("\n7. Most Frequently Used Venue:")
print(venue_count.head(10))


# 8. Toss decisions
toss_decisions = matches["toss_decision"].value_counts()

print("\n8. Toss Decisions:")
print(toss_decisions)


# 9. Percentage of matches won after winning toss
valid_toss_matches = matches[
    matches["toss_match_winner"].isin(["Yes", "No"])
]

toss_win_percentage = (
    (valid_toss_matches["toss_match_winner"] == "Yes").mean() * 100
)

print("\n9. Percentage of Matches Won After Winning Toss:")
print(round(toss_win_percentage, 2), "%")


# 10. Highest winning margin by runs
highest_run_margin = matches[
    matches["result"] == "runs"
].sort_values(
    "result_margin", ascending=False
).head(1)

print("\n10. Highest Winning Margin by Runs:")
print(highest_run_margin[["winner", "result_margin"]])


# 11. Highest winning margin by wickets
highest_wicket_margin = matches[
    matches["result"] == "wickets"
].sort_values(
    "result_margin", ascending=False
).head(1)

print("\n11. Highest Winning Margin by Wickets:")
print(highest_wicket_margin[["winner", "result_margin"]])


# 12. Highest individual run scorer
top_run_scorer = deliveries.groupby(
    "batter"
)["batsman_runs"].sum().sort_values(
    ascending=False
)

print("\n12. Highest Individual Run Scorer:")
print(top_run_scorer.head(10))


# 13. Highest number of wickets
top_wicket_taker = deliveries[
    deliveries["is_wicket"] == 1
].groupby(
    "bowler"
)["is_wicket"].sum().sort_values(
    ascending=False
)

print("\n13. Highest Number of Wickets:")
print(top_wicket_taker.head(10))


# 14. Top 10 batsmen
top_10_batsmen = top_run_scorer.head(10)

print("\n14. Top 10 Batsmen:")
print(top_10_batsmen)


# 15. Top 10 bowlers
top_10_bowlers = top_wicket_taker.head(10)

print("\n15. Top 10 Bowlers:")
print(top_10_bowlers)


# 16. Season-wise total runs
delivery_season = deliveries["match_id"].map(
    matches.set_index("id")["season"]
)

season_runs = deliveries.assign(
    season=delivery_season
).groupby(
    "season"
)["total_runs"].sum()

print("\n16. Season-wise Total Runs:")
print(season_runs)


# 17. Season-wise total wickets
season_wickets = deliveries.assign(
    season=delivery_season
).groupby(
    "season"
)["is_wicket"].sum()

print("\n17. Season-wise Total Wickets:")
print(season_wickets)


# 18. Average runs per match
runs_per_match = deliveries.groupby(
    "match_id"
)["total_runs"].sum()

average_runs = runs_per_match.mean()

print("\n18. Average Runs per Match:")
print(round(average_runs, 2))


# 19. Team-wise average runs
team_average_runs = deliveries.groupby(
    "batting_team"
)["total_runs"].mean().sort_values(
    ascending=False
)

print("\n19. Team-wise Average Runs:")
print(team_average_runs)


print("\n" + "=" * 50)
print("PART 3 ANALYSIS COMPLETED")
print("=" * 50)


# ==========================================
# PART 4: DATA VISUALIZATION
# CHARTS 1–5
# ==========================================

print("\n" + "=" * 50)
print("DATA VISUALIZATION - CHARTS 1 TO 5")
print("=" * 50)


# ------------------------------------------
# 1. Matches Played by Season
# ------------------------------------------

plt.figure(figsize=(10, 5))

matches_by_season.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Matches Played by Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------
# 2. Matches Won by Team
# ------------------------------------------

plt.figure(figsize=(10, 6))

wins_by_team.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Matches Won by Team")
plt.xlabel("Number of Wins")
plt.ylabel("Team")
plt.tight_layout()
plt.show()


# ------------------------------------------
# 3. Top 10 Run Scorers
# ------------------------------------------

plt.figure(figsize=(10, 6))

top_10_batsmen.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
plt.tight_layout()
plt.show()


# ------------------------------------------
# 4. Top 10 Wicket Takers
# ------------------------------------------

plt.figure(figsize=(10, 6))

top_10_bowlers.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Top 10 IPL Wicket Takers")
plt.xlabel("Total Wickets")
plt.ylabel("Bowler")
plt.tight_layout()
plt.show()


# ------------------------------------------
# 5. Player of the Match Awards
# ------------------------------------------

plt.figure(figsize=(10, 6))

player_of_match.head(10).sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Top 10 Player of the Match Awards")
plt.xlabel("Number of Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


print("\nCharts 1 to 5 completed successfully!")


# ==========================================
# CHARTS 6–9
# ==========================================

# ------------------------------------------
# 6. Season-wise Total Runs
# ------------------------------------------

plt.figure(figsize=(10, 5))

season_runs.plot(
    kind="line",
    marker="o"
)

plt.title("Season-wise Total Runs")
plt.xlabel("Season")
plt.ylabel("Total Runs")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ------------------------------------------
# 7. Season-wise Total Wickets
# ------------------------------------------

plt.figure(figsize=(10, 5))

season_wickets.plot(
    kind="line",
    marker="o"
)

plt.title("Season-wise Total Wickets")
plt.xlabel("Season")
plt.ylabel("Total Wickets")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ------------------------------------------
# 8. Toss Decision Distribution
# ------------------------------------------

plt.figure(figsize=(7, 5))

toss_decisions.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Toss Decision Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()


# ------------------------------------------
# 9. Top 10 Most Used Venues
# ------------------------------------------

plt.figure(figsize=(10, 6))

venue_count.head(10).sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Top 10 Most Frequently Used IPL Venues")
plt.xlabel("Number of Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()


print("\nCharts 6 to 9 completed successfully!")

# ==========================================
# CHARTS 10–14
# ==========================================

# ------------------------------------------
# 10. Team-wise Average Runs
# ------------------------------------------

team_avg_runs = deliveries.groupby(
    "batting_team"
)["total_runs"].mean().sort_values(ascending=True)

plt.figure(figsize=(10, 6))

team_avg_runs.plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Team-wise Average Runs per Delivery")
plt.xlabel("Average Runs")
plt.ylabel("Team")
plt.tight_layout()
plt.show()


# ------------------------------------------
# 11. Highest Winning Margin by Runs
# ------------------------------------------

run_margin_data = matches[
    matches["result"] == "runs"
].sort_values(
    "result_margin",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    run_margin_data["winner"],
    run_margin_data["result_margin"],
    edgecolor="black"
)

plt.title("Top 10 Highest Winning Margins by Runs")
plt.xlabel("Winning Margin (Runs)")
plt.ylabel("Team")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# ------------------------------------------
# 12. Highest Winning Margin by Wickets
# ------------------------------------------

wicket_margin_data = matches[
    matches["result"] == "wickets"
].sort_values(
    "result_margin",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    wicket_margin_data["winner"],
    wicket_margin_data["result_margin"],
    edgecolor="black"
)

plt.title("Top 10 Highest Winning Margins by Wickets")
plt.xlabel("Winning Margin (Wickets)")
plt.ylabel("Team")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# ------------------------------------------
# 13. Toss Winner vs Match Winner
# ------------------------------------------

toss_match = pd.crosstab(
    matches["toss_match_winner"],
    matches["result"]
)

plt.figure(figsize=(8, 5))

toss_match.plot(
    kind="bar",
    ax=plt.gca(),
    edgecolor="black"
)

plt.title("Toss Winner vs Match Result")
plt.xlabel("Did Toss Winner Win the Match?")
plt.ylabel("Number of Matches")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------
# 14. Top 10 Batsmen - Runs Distribution
# ------------------------------------------

top_batsmen_data = top_10_batsmen.sort_values(
    ascending=False
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_batsmen_data.values,
    y=top_batsmen_data.index
)

plt.title("Top 10 Batsmen by Total Runs")
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
plt.tight_layout()
plt.show()


print("\n" + "=" * 50)
print("ALL 14 VISUALIZATIONS COMPLETED SUCCESSFULLY!")
print("=" * 50)

# ------------------------------------------