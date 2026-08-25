# Projet 1 — Analyseur de santé financière d'une entreprise

## En une phrase
Un programme Python qui lit les comptes d'une entreprise et calcule tout seul ses grands **ratios financiers**, avec la **décomposition de DuPont** du ROE, puis sort une fiche Excel + un graphique.

## Ce qu'il fait, concrètement
1. Prend les postes comptables d'une entreprise (chiffre d'affaires, résultat net, actif, capitaux propres…).
2. Calcule les ratios de **liquidité**, d'**endettement**, d'**autonomie financière** et de **rentabilité** (marge nette, ROA, ROE).
3. Décompose le **ROE = marge nette × rotation de l'actif × levier financier** (méthode DuPont) — pour comprendre *d'où vient* la rentabilité.
4. Exporte une **fiche Excel** propre + un **graphique** des ratios.

## Comment le lancer
```bash
py analyse_financiere.py                 # données d'exemple (marche toujours)
py analyse_financiere.py --ticker MC.PA  # LVMH, vraies données (Yahoo Finance)
```
Sorties : `fiche_analyse.xlsx` et `ratios.png`.

## Ce que ça démontre (compétences)
- **Analyse financière** : maîtrise des ratios et de leur lecture.
- **Python** : pandas, matplotlib, openpyxl, gestion d'une source de données externe.
- **Rigueur** : la décomposition DuPont se réconcilie exactement avec le ROE calculé.

## Ce que tu peux dire en entretien (simple)
> « J'ai codé un outil qui automatise l'analyse financière d'une société : il calcule les ratios de liquidité, d'endettement et de rentabilité, et décompose le ROE façon DuPont pour voir si la rentabilité vient de la marge, de la rotation de l'actif ou de l'effet de levier. Il peut tourner sur les vraies données d'une entreprise cotée. »

## Puce de CV
- *Développé un outil Python d'analyse financière automatisée : extraction des états financiers, calcul des ratios (liquidité, endettement, rentabilité) et décomposition DuPont du ROE, avec export Excel et visualisation.*
