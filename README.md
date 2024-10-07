# NFL_Daily_Fantasy_Model
Machine learning models that predict fantasy points for quarterbacks, running backs, wide receivers, tight ends and defenses on FanDuel and DraftKings.

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
