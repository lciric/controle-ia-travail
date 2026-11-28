"""Les extraits de la v3 et de la v4 cités par le rapport VV4-fidelite : présents mot pour mot (espaces normalisés), et
première ligne du fichier où l'extrait commence. Usage : python3 -I -B extraits_v4.py"""
import hashlib
import re
import sys
from pathlib import Path

D = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
F = {"v4": (D / "synthese-comment-detecter-v4.md", "fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a"),
     "v3": (D / "synthese-comment-detecter-v3.md", "ec4239e9da0a6b8282ce0b685695fcb71b2777038fd18618b096797502ae6890")}

X = [
    ("v4", 303, "T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce type"),
    ("v4", 212, "toutes, seule comparaison publiée (« using fewer layers consistently yields worse performance ») [CC p. 8], sur une autre tâche"),
    ("v4", 284, "la proposition P-015 en estime la réécriture en mode « coût »"),
    ("v4", 350, "T0.6 réécrit en mode « coût » peut dépasser 10 USD par lancement (brouillon actuel : 1 536 + 640 épisodes ; P-015) : nœud de dépense possible"),
    ("v4", 65, "[DYL] range Llama-3.3-70B, souvent pris pour les organismes, sous Qwen 3.5 2B Reasoning (p. 5)"),
    ("v3", 55, "P3 n'avait aucune de ces conditions."),
    ("v4", 72, "2. Deux types de contraste sont à séparer."),
    ("v4", 84, "Le 0,5 de [BX] vient d'un organisme affiné, sans consigne ni raisonnement"),
    ("v4", 61, "entre consignes, la même sonde sépare presque parfaitement [AP p. 18]"),
    ("v4", 210, "entre consignes, séparation presque parfaite (« Our recall at 1% is greater than 99% on all four evaluation datasets », [AP p. 18])"),
    ("v4", 283, "entre consignes, séparation presque parfaite [AP p. 18] ;"),
    ("v4", 301, "et T1 n'y vaut qu'avec T4"),
    ("v4", 240, "lu « l'agrégation explique-t-elle le nul ? », (N-026, conditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse."),
    ("v4", 282, "base : N-026 permet ce bras dans un préenregistrement, mais il n'est pas dans le périmètre du GO de N-028 (localisation au champ et oracle, `registres/go.md` l. 32) : extension de N-028, comme E2 et la manipulation (nœud)."),
    ("v4", 326, "- **E2 et manipulation du nombre sur les actions de P3** : extension de N-028"),
    ("v4", 345, "E1, puis E3 (et E2 ou la manipulation du nombre si tu étends N-028)"),
    ("v4", 20, "Phrases et chiffres ajoutés : repris de ces deux rapports, qui les ont relus à la page et à la ligne ; aucun chiffre neuf."),
    ("v4", 34, "relus vers 12:00 UTC (lignes citées inchangées depuis 11:45 ; N-029 et GO-2026-10-20-08 ajoutés entre-temps)"),
    ("v4", 77, "réponses honnêtes déjà plus hautes que presque tout Alpaca, p. 9"),
    ("v4", 79, "Qwen3-8B 0,74 en exactitude équilibrée [DYL p. 5 ; table 9, p. 28] ; sur ce même modèle, rappel à 1 % de faux positifs"),
    ("v4", 23, "Le fond change en sections 1, 3, 4 et 5 : contrastes séparés par type (P3-P3 contre T1), prédiction de E2, pouvoirs des rangs 2, 3, 4, 6 et 9, confiances, nœuds."),
    ("v4", 290, "(2) Puis **E1 (P3b), lu comme diagnostic de l'instrument**"),
    ("v4", 334, "confiance ≈ 50 % (v3 : 60 %)"),
    ("v4", 80, "Analogues de **T1** (consigne égale ; l'étiquette vient du choix du modèle) : 0,81 et 0,63 sur ce même modèle"),
    ("v4", 208, "**faible à moyen** (v1 : fort ; v3 : moyen)"),
    ("v4", 212, "faible à moyen (v1 : moyen ; v3 : moyen)"),
    ("v4", 209, "[AU] : 0,653, dix derniers jetons, agrégation non dite"),
    ("v4", 85, "[AU] : 0,653 sur Phi-4, sonde lue sur les 10"),
    ("v4", 349, "Au-delà de 10 USD par lancement ou du crédit : nœud."),
    ("v4", 299, "**Confiance** (jugement du correcteur ; revue depuis la v1, VV2-sens-09 et VV3-sens-09)."),
    ("v4", 286, "sur T0.6 : témoin et mention à jouer (le brouillon actuel de T0.6, l. 74-81, n'a pas de mention : T3 n'y serait pas calculable)"),
    ("v4", 283, "brouillon de T0.6 l. 75, ou son équivalent dans T0.6 réécrit"),
    ("v4", 284, "compte à recharge automatique (R-283)"),
]


def main():
    txt = {}
    for k, (p, h) in F.items():
        s = hashlib.sha256(p.read_bytes()).hexdigest()
        print(f"{k} {s} {'égale' if s == h else 'ÉCART'}")
        if s != h:
            sys.exit("ARRÊT")
        txt[k] = p.read_text(encoding="utf-8")
    n = 0
    for k, ligne, e in X:
        t = txt[k]
        # recherche avec espaces normalisés, en gardant la correspondance des positions
        motif = r"\s+".join(re.escape(m) for m in e.split())
        m = re.search(motif, t)
        if not m:
            print(f"[ABSENT] {k} l. {ligne} : {e[:90]!r}")
            n += 1
            continue
        l0 = t.count("\n", 0, m.start()) + 1
        etat = "OK" if l0 == ligne else f"LIGNE {l0}"
        n += etat != "OK"
        print(f"[{etat}] {k} l. {ligne} : {e[:90]!r}")
    print(f"{len(X)} extraits, {n} écart(s)")


if __name__ == "__main__":
    main()
