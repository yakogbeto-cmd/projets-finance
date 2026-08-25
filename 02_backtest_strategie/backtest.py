"""
Backtest d'une strategie de croisement de moyennes mobiles
===========================================================
Teste une strategie simple sur un indice/action et la compare a une detention
passive ("buy & hold"). Calcule les mesures de risque et de performance
standard en gestion : rendement annualise, volatilite, ratio de Sharpe,
drawdown maximal.

Strategie : on est investi (position = 1) quand la moyenne mobile courte passe
au-dessus de la moyenne mobile longue ; sinon on reste en liquidite (position = 0).
C'est une strategie de suivi de tendance (momentum) classique et facile a expliquer.

Deux modes :
  - Sans argument        -> serie de prix synthetique reproductible (marche toujours)
  - --ticker ^FCHI / AAPL -> vraies donnees via Yahoo Finance (yfinance)

Auteur : Yvan Akogbeto
Usage  : py backtest.py
         py backtest.py --ticker ^GSPC --courte 50 --longue 200
"""

import argparse
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

JOURS_BOURSE = 252  # jours de cotation par an (annualisation)


# ---------------------------------------------------------------------------
# 1. Donnees
# ---------------------------------------------------------------------------
def prix_synthetiques(graine=7):
    """Genere une serie de prix reproductible en 3 regimes : hausse -> krach -> reprise.
    Ce profil illustre l'interet d'une strategie de tendance : sortir pendant le krach."""
    rng = np.random.default_rng(graine)
    segments = [
        (700, 0.0007, 0.010),   # marche haussier
        (250, -0.0020, 0.021),  # krach / marche baissier
        (550, 0.0007, 0.011),   # reprise
    ]
    rendements = np.concatenate([rng.normal(mu, sig, k) for k, mu, sig in segments])
    prix = 100 * np.exp(np.cumsum(rendements))
    dates = pd.bdate_range("2019-01-01", periods=len(prix))
    return pd.Series(prix, index=dates, name="Cloture")


def prix_yahoo(ticker):
    import yfinance as yf
    df = yf.download(ticker, period="6y", interval="1d", progress=False, auto_adjust=True)
    if df is None or df.empty:
        raise RuntimeError("Aucune donnee pour ce ticker.")
    serie = df["Close"]
    if isinstance(serie, pd.DataFrame):
        serie = serie.iloc[:, 0]
    return serie.dropna().rename("Cloture")


# ---------------------------------------------------------------------------
# 2. Strategie et mesures
# ---------------------------------------------------------------------------
def backtester(prix, courte=50, longue=200):
    """Applique la strategie et renvoie un DataFrame avec positions et rendements."""
    df = pd.DataFrame({"prix": prix})
    df["mm_courte"] = df["prix"].rolling(courte).mean()
    df["mm_longue"] = df["prix"].rolling(longue).mean()
    # Signal : investi si MM courte > MM longue. On decale d'un jour (on n'agit
    # qu'au lendemain du signal : pas de "triche" sur l'information).
    df["position"] = (df["mm_courte"] > df["mm_longue"]).astype(int).shift(1).fillna(0)
    df["rdt_marche"] = df["prix"].pct_change().fillna(0)
    df["rdt_strategie"] = df["position"] * df["rdt_marche"]
    df["capital_strategie"] = (1 + df["rdt_strategie"]).cumprod()
    df["capital_buyhold"] = (1 + df["rdt_marche"]).cumprod()
    return df


def mesures(rendements):
    """Rendement annualise, volatilite, Sharpe, drawdown max a partir des rendements quotidiens."""
    rendements = rendements.dropna()
    capital = (1 + rendements).cumprod()
    n = len(rendements)
    rdt_total = capital.iloc[-1] - 1
    rdt_annualise = (1 + rdt_total) ** (JOURS_BOURSE / n) - 1
    vol_annualisee = rendements.std() * np.sqrt(JOURS_BOURSE)
    sharpe = (rendements.mean() * JOURS_BOURSE) / vol_annualisee if vol_annualisee else 0.0
    drawdown_max = ((capital - capital.cummax()) / capital.cummax()).min()
    return {
        "Rendement total": rdt_total * 100,
        "Rendement annualise": rdt_annualise * 100,
        "Volatilite annualisee": vol_annualisee * 100,
        "Ratio de Sharpe": sharpe,
        "Drawdown maximal": drawdown_max * 100,
    }


# ---------------------------------------------------------------------------
# 3. Sorties
# ---------------------------------------------------------------------------
def afficher(libelle, m_strat, m_bh):
    print("=" * 66)
    print(f"  BACKTEST — {libelle}")
    print("=" * 66)
    print(f"  {'Indicateur':<26}{'Strategie':>16}{'Buy & Hold':>18}")
    print("-" * 66)
    for cle in m_strat:
        unite = "" if "Sharpe" in cle else " %"
        print(f"  {cle:<26}{m_strat[cle]:>14.2f}{unite}{m_bh[cle]:>16.2f}{unite}")
    print("=" * 66)


def graphique(df, libelle, chemin="performance.png"):
    plt.figure(figsize=(9, 5))
    plt.plot(df.index, df["capital_strategie"], label="Strategie (MM)", color="#274060", lw=1.6)
    plt.plot(df.index, df["capital_buyhold"], label="Buy & Hold", color="#B0B7C3", lw=1.4)
    plt.title(f"Performance cumulee — {libelle}")
    plt.ylabel("Capital (base 1)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(chemin, dpi=130)
    plt.close()
    return chemin


def main():
    p = argparse.ArgumentParser(description="Backtest croisement de moyennes mobiles.")
    p.add_argument("--ticker", help="Ticker Yahoo (ex: ^FCHI, ^GSPC, AAPL). Sinon serie synthetique.")
    p.add_argument("--courte", type=int, default=50, help="Fenetre moyenne mobile courte (defaut 50).")
    p.add_argument("--longue", type=int, default=200, help="Fenetre moyenne mobile longue (defaut 200).")
    args = p.parse_args()

    if args.ticker:
        try:
            prix = prix_yahoo(args.ticker)
            libelle = args.ticker
        except Exception as e:
            print(f"[!] Echec donnees live ({e}). Bascule sur la serie synthetique.", file=sys.stderr)
            prix, libelle = prix_synthetiques(), "Serie synthetique"
    else:
        prix, libelle = prix_synthetiques(), "Serie synthetique"

    df = backtester(prix, args.courte, args.longue)
    m_strat = mesures(df["rdt_strategie"])
    m_bh = mesures(df["rdt_marche"])
    afficher(libelle, m_strat, m_bh)
    img = graphique(df, libelle)
    print(f"\n[OK] Graphique de performance : {img}")


if __name__ == "__main__":
    main()
