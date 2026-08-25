# Projet 3 — Tableau de bord de trésorerie & analyse d'écarts

## En une phrase
Un générateur (Python) qui produit un **classeur Excel professionnel** de suivi de **trésorerie** et d'**analyse d'écarts budget/réalisé**, avec de **vraies formules** qui se recalculent, des graphiques, et une **macro VBA** en bonus.

## Ce qu'il fait, concrètement
Le classeur `tableau_bord_tresorerie.xlsx` contient 3 feuilles :
1. **Trésorerie** : prévision sur 12 mois (solde initial → encaissements − décaissements → flux net → solde final). Le solde final d'un mois devient le solde initial du suivant, **par formule**.
2. **Budget_Realise** : analyse d'**écarts** par poste (écart en €, en %, et un **statut Favorable/Défavorable** calculé automatiquement — une charge sous le budget = favorable, un produit au-dessus = favorable).
3. **Dashboard** : graphiques (évolution du solde, budget vs réalisé).

Comme ce sont de **vraies formules Excel**, si tu changes un encaissement ou un budget, tout se recalcule — c'est un vrai outil, pas une capture figée.

## Comment le lancer
```bash
py generer_tableau_tresorerie.py     # produit tableau_bord_tresorerie.xlsx
```
Bonus VBA : ouvrir Excel → `Alt+F11` → importer `macro_ecarts.bas` → lancer `ColorierEcarts` (colore les statuts en vert/rouge).

## Ce que ça démontre (compétences)
- **Trésorerie / cash management** et **contrôle de gestion** (tes cibles exactes).
- **Excel avancé** (formules chaînées, mise en forme) + **VBA** (macro d'automatisation).
- **Python** appliqué à la génération de reporting (openpyxl).

## Ce que tu peux dire en entretien (simple)
> « J'ai construit un outil qui génère un tableau de bord de trésorerie et une analyse d'écarts budget/réalisé sous Excel, avec des formules vivantes et une macro VBA qui met en couleur les écarts favorables et défavorables. Ça correspond directement à ce que fait un contrôleur de gestion ou un trésorier au quotidien. »

## Puce de CV
- *Automatisé la production d'un tableau de bord de trésorerie et d'une analyse d'écarts budget/réalisé sous Excel (formules dynamiques, macro VBA, graphiques), généré par un script Python.*
