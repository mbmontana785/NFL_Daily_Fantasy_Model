# NFL_Daily_Fantasy_Model
Machine learning models that predict fantasy points for defense, quarterbacks, and flex positions (running backs, wide receivers, tight ends) on FanDuel and DraftKings. Interactive interface in **Streamlit** with Python **PuLP** library used for lineup optimization based on constraints such as salary cap and position requirements.

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
|             |   2024 Week 3 |   2024 Week 6 |
|:------------|--------------:|--------------:|
| FD_Ridge_D  |       5.43932 |       4.94016 |
| FD_GB_D     |       5.44245 |       5.05887 |
| FD_XGB_D    |       5.43394 |       5.06082 |
| DK_Ridge_D  |       5.56043 |       5.16421 |
| DK_GB_D     |       5.45913 |       5.29611 |
| DK_XGB_D    |       5.44491 |       5.29582 |
| FD_RF_QB    |       6.40443 |       6.30695 |
| FD_GB_QB    |       6.32921 |       6.10332 |
| FD_XGB_QB   |       6.27523 |       6.02756 |
| DK_RF_QB    |       6.88722 |       6.81272 |
| DK_GB_QB    |       7.02554 |       6.64756 |
| DK_XGB_QB   |       6.90776 |       6.60635 |
| FD_RF_FLEX  |       6.34076 |       5.5043  |
| FD_GB_FLEX  |       6.29923 |       5.50443 |
| FD_XGB_FLEX |       6.32592 |       5.49527 |
| DK_RF_FLEX  |       7.6902  |       6.54713 |
| DK_GB_FLEX  |       7.67743 |       6.41776 |
| DK_XGB_FLEX |       7.64608 |       6.43443 |

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
