# NFL_Daily_Fantasy_Model
**Model yielded $7,243.99 in FanDuel winnings on $1,132.35 of entry fees in 2024, a profit of more than 600%.**<br>

Models predict fantasy points for defense, quarterbacks, and flex positions (running backs, wide receivers, tight ends) on FanDuel and DraftKings. Interactive interface in **Streamlit** with Python **PuLP** library used for lineup optimization based on constraints such as salary cap and position requirements.

## Model Performance
### RMSE testing scores
**DEFENSE**
- Ridge Regression: 6.0157
- Gradient Boost: 6.0251
- XGBoost: 6.0249

**QUARTERBACK**<br>
**FanDuel**
- Random Forest: 6.7946
- Gradient Boost: 6.8371
- XGBoost: 6.826

**DraftKings**
- Random Forest: 7.4053
- Gradient Boost: 7.4412
- XGBoost: 7.4497

**FLEX**<br>
**FanDuel**
- Random Forest: 5.6812
- Gradient Boost: 5.6761
- XGBoost: 5.664

**DraftKings**
- Random Forest: 6.7096
- Gradient Boost: 6.6893
- XGBoost: 6.6718

## Live Model Performance
|             |   2024 Week 3 |   2024 Week 6 |   2024 Week 7 |   2024 Week 8 |   2024 Week 9 |   2024 Week 10 |   2024 Week 11 |   2024 Week 12 |   2024 Week 13 |   2024 Week 14 |   2024 Week 15 |   2024 Week 16 |
|:------------|--------------:|--------------:|--------------:|--------------:|--------------:|---------------:|---------------:|---------------:|---------------:|---------------:|---------------:|---------------:|
| FD_Ridge_D  |       5.43932 |       4.94016 |       6.61802 |       4.06598 |       4.64662 |        6.44919 |        3.61561 |        5.59608 |        6.22801 |        5.23671 |      nan       |        5.65359 |
| FD_GB_D     |       5.44245 |       5.05887 |       6.70447 |       3.84469 |       4.70134 |        6.38519 |        3.57019 |        5.47552 |        6.25093 |        5.11978 |      nan       |        5.592   |
| FD_XGB_D    |       5.43394 |       5.06082 |       6.69844 |       3.85492 |       4.70386 |        6.38193 |        3.57198 |        5.4673  |        6.21474 |        5.1344  |      nan       |        5.5959  |
| DK_Ridge_D  |       5.56043 |       5.16421 |       4.78816 |       4.49276 |       5.10845 |        5.63909 |        4.67104 |        6.66211 |        5.35193 |        5.2294  |      nan       |        4.2857  |
| DK_GB_D     |       5.45913 |       5.29611 |       4.98213 |       4.46313 |       5.18824 |        5.63218 |        4.76139 |        6.61258 |        5.3558  |        5.19947 |      nan       |        4.29474 |
| DK_XGB_D    |       5.44491 |       5.29582 |       4.97537 |       4.45454 |       5.18407 |        5.62915 |        4.75701 |        6.60776 |        5.33642 |        5.20605 |      nan       |        4.29759 |
| FD_RF_QB    |       6.40443 |       6.30695 |       7.86644 |       6.50852 |       6.35382 |        6.79816 |        7.36005 |        5.92756 |        7.99098 |        7.07818 |        9.06439 |        6.37344 |
| FD_GB_QB    |       6.32921 |       6.10332 |       7.6214  |       6.55822 |       6.43341 |        6.88316 |        7.87574 |        6.02957 |        8.03109 |        7.3476  |        9.09876 |        5.95915 |
| FD_XGB_QB   |       6.27523 |       6.02756 |       7.61861 |       6.64382 |       6.44374 |        6.81333 |        7.93199 |        5.99056 |        8.00869 |        7.27432 |        9.0055  |        6.10395 |
| DK_RF_QB    |       6.88722 |       6.81272 |       8.20518 |       6.92674 |       6.41128 |        6.87663 |        7.87289 |        6.69998 |        8.10473 |        8.34176 |        9.49526 |        7.31198 |
| DK_GB_QB    |       7.02554 |       6.64756 |       8.2515  |       7.13517 |       6.24201 |        6.84189 |        8.58469 |        6.71606 |        8.29385 |        8.36864 |        9.59325 |        7.27916 |
| DK_XGB_QB   |       6.90776 |       6.60635 |       8.02421 |       7.08391 |       6.29617 |        6.95214 |        8.44917 |        6.61017 |        8.13808 |        8.33405 |        9.61584 |        7.00124 |
| FD_RF_FLEX  |       6.34076 |       5.5043  |       5.22942 |       5.59216 |       5.55466 |        4.71361 |        6.15497 |        5.78946 |        4.89853 |        6.37815 |        6.02606 |        6.00608 |
| FD_GB_FLEX  |       6.29923 |       5.50443 |       5.19345 |       5.61978 |       5.63362 |        4.71557 |        6.09969 |        5.83225 |        4.93693 |        6.34837 |        6.02633 |        6.07552 |
| FD_XGB_FLEX |       6.32592 |       5.49527 |       5.21154 |       5.60112 |       5.60693 |        4.73311 |        6.14163 |        5.83782 |        4.96537 |        6.32518 |        5.96614 |        6.05691 |
| DK_RF_FLEX  |       7.6902  |       6.54713 |       6.15942 |       6.20409 |       6.41163 |        5.30416 |        7.14524 |        6.42429 |        5.69073 |        7.4166  |        6.94747 |        7.00166 |
| DK_GB_FLEX  |       7.67743 |       6.41776 |       6.12574 |       6.21264 |       6.47226 |        5.2633  |        7.10676 |        6.42721 |        5.7362  |        7.3269  |        6.90688 |        7.21808 |
| DK_XGB_FLEX |       7.64608 |       6.43443 |       6.10767 |       6.21163 |       6.46891 |        5.27845 |        7.15403 |        6.47833 |        5.75851 |        7.315   |        6.88846 |        7.19515 |


## Jupyter Notebook Workflow

### Live_Notebook_a
Process player lists downloaded from FanDuel and DraftKings. Player lists stored in **SQLite.** Name matching with **rapidfuzz** library.

### Live_Notebook_b
- Use **R Studio** to download weekly data and play-by-play data from [nflfastr](https://www.nflfastr.com/articles/beginners_guide.html). This is used to generate variables for the models.
- Calculate previous week's points for fantasy defenses

### Live_Notebook_c
- Gather odds for upcoming games from [The Odds API](https://the-odds-api.com/)
- Create binary outdoors variables depending on stadium
- Scrape RotoGrinders using **Beautiful Soup** for predicted wind speeds
- **Future Work**: Enable filling games without odds with means

### Live_Notebook_d
Process dataset to be used for defense model

### Live_Notebook_e
- Process dataset to be used for quarterback model
- Create QB_role variables (1 or 2) to denote starting and backup QBs

### Live_Notebook_f
Process dataset to be used for FLEX model (RB, WR, TE)

### Live_Notebook_g
- Takes user input to adjust FLEX dataset for injuries.
- Adjusts target or carry variables to reflect increased roles for injury replacements.

### Live_Notebook_h
- EDA. Check summary statistics for irregularities. 
- Assess missing data and decide to fill values or drop rows.

### Live_Notebook_i
#### Predictions
**Defense** Ridge Regression, Gradient Boost, XG Boost
**Quarterback** Random Forest, Gradient Boost, XG Boost
**FLEX** Random Forest, Gradient Boost, XG Boost
Feature scalers and models stored in **pickle** files

### Live_Notebook_j
- Generate lineups using **PuLP**
- With Streamlit deployment, this notebook is really only a backup. The PuLP operation occurs in the **app.py** file.

### Live_Notebook_k
Model Evaluation
