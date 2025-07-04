# Interactive Analysis of Tips Datase
* * *

## Description

This project presents an interactive dashboard for visual analysis of the tips dataset using Python, Plotly, and Dash. The dataset contains transactional data from a restaurant, including total bill, tip, group size, gender, smoking status, day, and time (Lunch/Dinner).


### The dashboard features three key interactive visualizations:-
#### 1.  Bar Graph (Tip vs. Size):
Displays the average tip amount based on the group size (number of people). 
With description of tip on each bin size

#### 2.  Scatter Plot (Tip vs. Total Bill):
Shows the relationship between the total bill and the tip amount. This plot helps to identify how tip values changes bills and how the trend changes based on the selected filters (gender, smoker, day).

#### 3. Pie Chart (Time Contribution by Day):
Visualizes the distribution of Lunch vs. Dinner for each day, showing how much each time contributes to the total visits. This helps understand the busiest periods of the week and customer preferences.
* * *


## Key Features:
- Fully interactive and filterable dashboard using Dash
- Dynamic visualizations created with Plotly
- Real-time updates based on user inputs
- Insightful UI to understand customer behavior
* * *


## Insights Gained:
1. Larger groups tend to give higher tips, but the per-person tip can vary.
2. Dinner time and weekends show higher tip amounts.
3. Tipping behavior varies slightly by gender and smoker status.
4. Most visits and higher tips are observed during dinner on weekends.
* * * 


## Technologies Used:
- Python – Data processing and logic
- Plotly – Interactive graphs and charts
- Dash – Web dashboard development
* * *

## Requirements :-
1. `Python = 3.12.3`
2. `Plotly = 6.2.0`
3. `Dash = 3.1.1`
* * *


## How To Run In Your Machine :-
_Save Python file and give it to a name_

_tips dataset file and give name it to `tip.csv`_

***Open Your Terminal/cmd and type***
``` python
python name_of_your_file.py
```
