# Projets Finance — Yvan Akogbeto

Trois projets finance 
Chacun tourne en une commande et produit un résultat concret (graphique / classeur Excel).

| # | Projet | Compétences | Cible CV |
|---|--------|-------------|----------|
| 1 | [Analyse financière](01_analyse_financiere/) | Ratios, DuPont, Python | Analyse financière |
| 2 | [Backtest & risque](02_backtest_strategie/) | Marchés, Sharpe/drawdown, quant | Marchés / middle office |
| 3 | [Trésorerie & écarts](03_tresorerie_ecarts/) | Excel/VBA, contrôle de gestion | Trésorerie / contrôle de gestion |

## Prérequis
- Python 3.12 installé.
- Librairies : `py -m pip install pandas numpy matplotlib openpyxl yfinance`

## Lancer les 3
```bash
py 01_analyse_financiere/analyse_financiere.py
py 02_backtest_strategie/backtest.py
py 03_tresorerie_ecarts/generer_tableau_tresorerie.py
```

Chaque dossier a son propre `README.md` avec l'explication simple, ce que le projet

> Les jeux de données d'exemple garantissent que tout tourne pour une démo ; les
> options `--ticker` branchent les vraies données de marché.
