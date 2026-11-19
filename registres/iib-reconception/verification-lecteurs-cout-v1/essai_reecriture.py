"""Aller-retour de la réécriture, au niveau du texte (sans jetons) : suite du jumeau -> lire_suite (valeur H, texte du
nombre) -> champ COST réécrit « COST: <texte du nombre> » (toute la valeur remplacée, comme reecrire_valeur_cout) ->
cout_action. Égalité attendue : relu == H. Montre aussi ce que le jumeau voit aux pas suivants."""
from controle_ia.t06.cout import NOMBRE, cout_action, cout_lisible, lire_cout


def lire_suite(texte):  # copie de iib/oracle_v1.py, lignes 83-88, au commit 836c7ccc
    v = lire_cout(texte)["cout"]
    if not cout_lisible(v):
        return None, None
    return float(v), NOMBRE.search(texte).group(0)


SUITES = [" 2,500 GPU-hours", " 2.5k GPU-hours", " 2.5 k GPU-hours", " 2 500 GPU-hours", " 2 500 GPU-hours",
          " 3 K GPU-hours", " 120h", " 2.5kh", " $1,200 (about 400 GPU-hours)", " 4 GPUs for 100 hours",
          " 8 x 50 = 400 GPU-hours", " 200-400 GPU-hours", " **1,000** GPU-hours", " 2.500 GPU-hours", " 1,5 GPU-hours",
          " 0 extra, 200 GPU-hours", " ~1e3 GPU-hours"]
GABARIT = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS: c\nCOST: {v}\nPREDICTION: q\n"

if __name__ == "__main__":
    print(f"{'suite du jumeau':34s} {'H':>8s} {'texte réécrit':>14s} {'relu':>8s}  égal")
    for s in SUITES:
        h, n = lire_suite(s)
        if h is None:
            print(f"{s!r:34s} {'illisible':>8s}")
            continue
        relu = cout_action(GABARIT.format(v=n.strip()))["cout"]
        print(f"{s!r:34s} {h:8g} {n.strip()!r:>14s} {relu:8g}  {'oui' if relu == h else 'NON'}")
