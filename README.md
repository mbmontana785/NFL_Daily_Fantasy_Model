# NFL_Daily_Fantasy_Model
Machine learning models that predict fantasy points for defense, quarterbacks, and flex positions (running backs, wide receivers, tight ends) on FanDuel and DraftKings. Interactive interface in **Streamlit** with Python **PuLP** library used for lineup generation.

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
|             |   2024 Week 3 |
|:------------|--------------:|
| FD_Ridge_D  |       5.43932 |
| FD_GB_D     |       5.44245 |
| FD_XGB_D    |       5.43394 |
| DK_Ridge_D  |       5.56043 |
| DK_GB_D     |       5.45913 |
| DK_XGB_D    |       5.44491 |
| FD_RF_QB    |       6.40443 |
| FD_GB_QB    |       6.32921 |
| FD_XGB_QB   |       6.27523 |
| DK_RF_QB    |       6.88722 |
| DK_GB_QB    |       7.02554 |
| DK_XGB_QB   |       6.90776 |
| FD_RF_FLEX  |       6.34076 |
| FD_GB_FLEX  |       6.29923 |
| FD_XGB_FLEX |       6.32592 |
| DK_RF_FLEX  |       7.6902  |
| DK_GB_FLEX  |       7.67743 |
| DK_XGB_FLEX |       7.64608 |

## Jupyter Notebook Workflow

### Live_Notebook1 (1)
Process player lists downloaded from FanDuel and DraftKings. Player lists stored in **SQLite.** Name matching with **rapidfuzz** library.

### Live_Notebook1a
Calculate previous week's points for fantasy defenses
- Use **R Studio** to download weekly data and play-by-play data from [nflfastr](https://www.nflfastr.com/articles/beginners_guide.html)

### Live_Notebook1b
- Gather odds from [The Odds API](https://the-odds-api.com/)
- Create binary outdoors variables depending on stadium
- Scrape RotoGrinders using **Beautiful Soup** for predicted wind speeds

### Live_Notebook2
Process dataset to be used for defense model

### Live_Notebook3
Process dataset to be used for quarterback model

### Live_Notebook5
Process dataset to be used for FLEX model (RB, WR, TE)

### Live_Notebook7
- Takes user input to adjust QB_role variable (1 or 2) if there's a starting QB change.
- Adjusts quarterback dataset if there are starting QB changes.
- Adjusts FLEX dataset if there's a starting QB change. FLEX dataset contains QB strength variables that relate to starting QB

## Live_Notebook8
Adjust FLEX dataset for injuries. Adjusting certain variables to reflect increased roles for injury replacements.

## Live_Notebook9
EDA. Check summary statistics for irregularities. Assess missing data and decide to fill values or drop rows.

## Live_Notebook10
Predictions
**Defense** Ridge Regression, Gradient Boost, XG Boost
**Quarterback** Random Forest, Gradient Boost, XG Boost
**FLEX** Random Forest, Gradient Boost, XG Boost
Feature scalers and models stored in pickle files

## Live_Notebook11
Generate lineups using PuLP
