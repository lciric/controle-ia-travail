import json, sys, math
racine = sys.argv[1]
d = racine + "/diag/20261017-193648-t05-notations-reel/"
def k(n):  # positions de zone générée nécessaires pour que le q99 de l'action voie le décalage (T0.4 v3, l. 172)
    return n - math.floor(0.99 * (n - 1))
for juge in ("8B", "3B"):
    ns = json.load(open(d + f"notations-{juge}-decisives.json", encoding="utf-8"))["resultat"]["notations"]
    lots = [ns[i:i+8] for i in range(0, len(ns), 8)]
    cadre = [l for l in lots if len(l) == 8 and any(x["tronquee"] for x in l)]
    def courte(x):
        lc, g = x["jetons_contexte"], x["jetons_reponse"]
        n = lc + g  # positions capturées (contexte + jetons générés relus)
        decalees = g - 1  # comparaisons décalées dans la zone générée (première position générée exclue)
        return decalees < k(n)
    tot = sum(courte(x) for x in ns)
    par_lot = [sum(courte(x) for x in l) for l in cadre]
    print(f"{juge}: réponses dont la zone générée est sous ~1 % des positions : {tot} sur {len(ns)} ;"
          f" lots du cadre avec au moins une telle rangée : {sum(1 for c in par_lot if c)} sur {len(cadre)} ; par lot : {par_lot}")
    rep = sorted(x["jetons_reponse"] for x in ns)
    print(f"   5 plus courtes réponses (jetons) : {rep[:5]}")
