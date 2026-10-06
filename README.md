# IPL Data Analysis

## Project Overview

This project analyzes Indian Premier League (IPL) match and ball-by-ball
data using Python and Power BI. The objective is to identify important
trends in team performance, player performance, toss impact, season-wise
statistics, and other IPL insights.

## Project Details

-   **Project:** IPL Data Analysis
-   **Program:** Data Analytics Master Program -- Batch 2
-   **Student:** Sairam Nallapati
-   **Project Type:** Major Project-I

## Dataset

The project uses cleaned IPL datasets containing:

-   Match-level information
-   Ball-by-ball delivery information
-   Season-wise summary information

The analysis covers **1,095 matches**, **260,920 delivery records**, and
**17 seasons**.

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn
-   Jupyter Notebook
-   Power BI
-   DAX

## Python Analysis

The Python analysis includes:

1.  Matches played by season
2.  Matches won by team
3.  Top run scorers
4.  Top wicket takers
5.  Player of the Match awards
6.  Toss decision analysis
7.  Matches won after winning the toss
8.  Season-wise total runs
9.  Season-wise total wickets
10. Runs distribution
11. Team performance comparison
12. Venue-wise match count
13. Runs vs wickets analysis
14. Correlation heatmap

## Power BI Dashboard

The Power BI dashboard provides interactive analysis of IPL data
through:

-   KPI cards
-   Team performance visuals
-   Player performance visuals
-   Season-wise analysis
-   Toss analysis
-   Match result analysis
-   Batting and bowling statistics
-   Season slicer for interactive filtering

## Key KPIs

-   **Total Matches:** 1,095
-   **Total Runs:** Approximately 348K
-   **Total Wickets:** Approximately 13K
-   **Total Seasons:** 17
-   **Total Batsmen:** 673

## DAX Measures

The dashboard uses DAX measures including:

``` dax
Total Matches = DISTINCTCOUNT(IPL_Cleaned_Matches[id])

Total Runs = SUM(IPL_Cleaned_Deliveries[total_runs])

Total Wickets =
CALCULATE(
    COUNTROWS(IPL_Cleaned_Deliveries),
    IPL_Cleaned_Deliveries[is_wicket] = 1
)

Total Seasons = DISTINCTCOUNT(IPL_Cleaned_Matches[season])
```

## Data Model

The Power BI model connects the match and delivery datasets using:

-   `IPL_Cleaned_Matches[id]`
-   `IPL_Cleaned_Deliveries[match_id]`

The relationship is one-to-many from matches to deliveries.

## Key Insight

The toss analysis shows that teams winning the toss won **554 out of
1,090 completed matches**, which is approximately **50.83%**. This
indicates that winning the toss alone does not guarantee a match
victory.

## Project Structure

``` text
StudentName_IPL_Data_Analysis
│
├── Dataset
│   └── IPL_Cleaned.csv
│
├── Python
│   └── IPL_Data_Analysis.ipynb
│
├── PowerBI
│   └── IPL_Analytics_Dashboard.pbix
│
├── Report
│   └── IPL_Project_Report.pdf
│
└── README.md
```

## Conclusion

This project demonstrates the use of data analytics techniques to
explore IPL cricket data. Python was used for data analysis and
visualization, while Power BI was used to build an interactive dashboard
and present meaningful insights.

## Author

**Yasaswini Adimulam**
