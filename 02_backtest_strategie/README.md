# Projet 2 — Backtest d'une stratégie de marché avec mesures de risque

## En une phrase
Un programme Python qui teste une **stratégie de suivi de tendance** sur des données de marché et mesure sa performance et son **risque** (Sharpe, volatilité, drawdown), face à une détention passive « buy & hold ».

## Ce qu'il fait, concrètement
1. Prend une série de prix (indice ou action).
2. Applique une stratégie de **croisement de moyennes mobiles** : investi quand la moyenne courte passe au-dessus de la moyenne longue, en liquidité sinon.
3. Calcule les mesures standard en gestion : **rendement annualisé**, **volatilité annualisée**, **ratio de Sharpe**, **drawdown maximal**.
4. Compare la stratégie au « buy & hold » et trace la **courbe de performance**.

> ⚠️ Point honnête à comprendre : sur les données d'exemple (hausse → krach → reprise), la stratégie **ne bat pas** forcément le marché en rendement, mais elle **réduit fortement le drawdown** (elle sort pendant le krach). C'est exactement le rôle d'une stratégie de tendance : protéger le capital. Savoir dire ça montre que tu comprends la mesure du risque.

## Comment le lancer
```bash
py backtest.py                                  # série synthétique (marche toujours)
py backtest.py --ticker ^GSPC --courte 50 --longue 200   # S&P 500, vraies données
```
Sortie : `performance.png`.

## Ce que ça démontre (compétences)
- **Marchés financiers** + **mesure du risque** (Sharpe, volatilité, drawdown) — vocabulaire middle office / gestion.
- **Quantitatif** : manipulation de séries temporelles, rendements, annualisation (ton socle proba/stats CPGE).
- **Honnêteté analytique** : pas de « triche » sur l'information (signal décalé d'un jour), lecture nuancée des résultats.

## (simple)
> « J'ai backtesté une stratégie de tendance (croisement de moyennes mobiles) et je l'ai évaluée avec les mesures de risque classiques : Sharpe, volatilité, drawdown maximal. Sur un scénario de krach simulé, la stratégie a réduit le drawdown de moitié par rapport à une détention passive — ce qui illustre son intérêt : protéger le capital plus que battre le marché. »

## Puce de CV
- *Conçu en Python un backtester de stratégie de marché (croisement de moyennes mobiles) avec calcul des mesures de risque (ratio de Sharpe, volatilité, drawdown maximal) et comparaison à une détention passive.*
