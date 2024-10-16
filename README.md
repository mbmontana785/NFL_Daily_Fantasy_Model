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
2024 Week 3
FD_Ridge_D	5.439323
FD_GB_D	5.442453
FD_XGB_D	5.433941
DK_Ridge_D	5.560427
DK_GB_D	5.459133
DK_XGB_D	5.444914
FD_RF_QB	6.404433
FD_GB_QB	6.329214
FD_XGB_QB	6.275229
DK_RF_QB	6.887222
DK_GB_QB	7.025536
DK_XGB_QB	6.907759
FD_RF_FLEX	6.340756
FD_GB_FLEX	6.299230
FD_XGB_FLEX	6.325915
DK_RF_FLEX	7.690199
DK_GB_FLEX	7.677433
DK_XGB_FLEX	7.646078


## Live_Notebook1 (1)
Process player lists downloaded from FanDuel and DraftKings

## Live_Notebook1a
Calculate previous week's points for fantasy defenses
- Use **R Studio** to download weekly data and play-by-play data from [nflfastr](https://www.nflfastr.com/articles/beginners_guide.html)

## Live_Notebook1b
- Gather odds from The Odds API
- Create binary outdoors variables depending on stadium
- Scrape RotoGrinders for predicted wind speeds

## Live_Notebook2
Process dataset to be used for defense model

## Live_Notebook3
Process dataset to be used for quarterback model

## Live_Notebook5
Process dataset to be used for FLEX model (RB, WR, TE)

## Live_Notebook7
Adjust quarterback dataset, and FLEX dataset, if there's a starting QB change. FLEX dataset contains QB strength variables that relate to starting QB

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
