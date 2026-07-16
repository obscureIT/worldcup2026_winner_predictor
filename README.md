# ⚽ 2026 World Cup Final Predictor

**Spain vs Argentina — July 19, 2026, MetLife Stadium**

A data science project that predicts the winner of the 2026 FIFA World Cup final by combining three independent approaches — Elo ratings, Poisson Monte Carlo simulation, and machine learning — trained on **every men's international match ever played (49,000+ matches, 1872–2026)**.

## 🏆 The verdict

| Lens | Spain | Argentina |
|---|---|---|
| Elo expectancy | 53.9% | 46.1% |
| Poisson Monte Carlo (200k sims) | 43.7% | 56.3% |
| Gradient boosting (ML) | 52.6% | 47.4% |
| **Ensemble** | **50.1%** | **49.9%** |

A statistical dead heat between the world's #1 and #2 Elo-rated teams — with the models disagreeing in interesting ways: Spain's tournament defence (1 goal conceded in 7 games) drives the Elo and ML lenses, while Argentina's attacking output and superior penalty-shootout record (65% career win rate vs Spain's 50%) tilt the goal-level simulation their way.

## 📓 Notebooks

| Notebook | What it does |
|---|---|
| [`01_data_exploration.ipynb`](notebooks/01_data_exploration.ipynb) | EDA: finalists' all-time records, head-to-head, road to the final, form analysis |
| [`02_elo_and_ml_models.ipynb`](notebooks/02_elo_and_ml_models.ipynb) | Elo ratings from 150 years of matches; leakage-free feature engineering; logistic regression & gradient boosting with time-based validation |
| [`03_final_prediction.ipynb`](notebooks/03_final_prediction.ipynb) | Poisson attack/defence model, 200,000-match Monte Carlo simulation (incl. extra time & shootouts), ensemble verdict |

## 🔍 Highlights

- **No data leakage**: every feature uses only pre-match information; train/test split is chronological (train 1994–2023, test 2024–2026)
- **Honest evaluation**: models are benchmarked against naive baselines on accuracy *and* log loss, with calibration curves — 60.7% accuracy / 0.86 log loss on 3-class outcomes, in line with published football-prediction benchmarks
- **Domain-aware simulation**: extra time modeled at 1/3 scoring rate, penalty shootouts weighted by each team's historical shootout record
- **Stated limitations**: no player-level data, Poisson strengths not opponent-adjusted — with concrete next steps (Dixon-Coles, odds benchmarking)

## 🚀 Reproduce

```bash
git clone https://github.com/<your-username>/worldcup-2026-predictor.git
cd worldcup-2026-predictor
pip install -r requirements.txt
jupyter lab
```

Run the notebooks in order (01 → 02 → 03). Notebook 02 saves the trained model and ratings that notebook 03 consumes.

## 📊 Data

[International football results 1872–present](https://github.com/martj42/international_results) by Mart Jürisoo (CC0 / public domain), including `results.csv` (all matches) and `shootouts.csv` (every international penalty shootout since 1967). A snapshot as of July 16, 2026 — after the semi-finals, before the final — is included in `data/`.

## 🛠️ Stack

Python · pandas · NumPy · scikit-learn · SciPy · Matplotlib · Jupyter
