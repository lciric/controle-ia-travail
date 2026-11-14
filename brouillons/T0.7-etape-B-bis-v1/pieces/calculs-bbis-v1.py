"""Calculs de planification de l'étape B bis de T0.7, v1 : aires minimales détectables, écarts minimaux détectables et
devis. Planification seulement, jamais une sélection (aucune donnée de 7a, de 7b, de T0.7 ni de P3-bis n'est lue).

Sources des constantes (toutes internes au programme, aucun chiffre de l'état de l'art, R7) :
- demi-largeurs de l'intervalle apparié de D à 97,5 % sur 60 tâches, rejeu de la règle (a) sur P3 : 0,047901 (tromperie),
  0,048676 (enjeux) ; T0.7 scellé (`prereg/T0.7-sondes-v0-v1.md`, `d7d180ec…`), section « Puissance », point 1 (ii) ;
- formule de T0.7 (même point 1 (iii)) : aire minimale à 80 % = Q + (z_niveau + z_0,8) * s, s = (w / z_0,9875) * sqrt(60 / n),
  quantile du plancher Q tenu pour fixe (optimiste : T0.7 écrit une perte simulée de 0,16 à 0,35 par sonde, point 4 (ii)) ;
- écart type nul de l'aire, formule du texte de validité (`prereg/validite-adaptateur-v1.md`, `7e78909d…`, « Métrique »,
  « Effectifs ») : sigma(n1, n0) = 1,188 * sqrt((n1 + n0 + 1) / (12 n1 n0)) ;
- débits et prix : T0.6 scellé (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`, « Devis ») : 0,45 s par passe d'épisode
  (108,4 s pour 240 épisodes de P3), prix A100 SXM4 80 Go attendu 1,0889 à 1,30 USD de l'heure, pire 1,40 ; H200 NVL 4,70 ;
  stockage au plus 0,08 USD de l'heure ; téléchargement au plus 0,05 USD par Go.
Lancement : `python3 -I -B calculs-bbis-v1.py` (bibliothèque standard seulement).
"""
from math import sqrt
from statistics import NormalDist

N = NormalDist()
Z08 = N.inv_cdf(0.80)
Z_W = N.inv_cdf(0.9875)          # w est une demi-largeur à 97,5 % bilatéral


def z_bilateral(niveau: float) -> float:
    return N.inv_cdf(1.0 - (1.0 - niveau) / 2.0)


def s_formule(w: float, n_taches: int) -> float:
    return (w / Z_W) * sqrt(60.0 / n_taches)


def aire_minimale(Q: float, w: float, niveau: float, n_taches: int = 64) -> float:
    return Q + (z_bilateral(niveau) + Z08) * s_formule(w, n_taches)


def sigma_nul(n1: int, n0: int) -> float:
    return 1.188 * sqrt((n1 + n0 + 1) / (12.0 * n1 * n0))


def ligne(*valeurs) -> str:
    return " | ".join(str(v) for v in valeurs)


print("# Sortie de calculs-bbis-v1.py (planification, jamais une sélection)")
print()
print("## 1. Contrôle : la formule de T0.7 redonne ses valeurs (64 tâches, 98,75 %)")
for nom, Q, w in (("tromperie", 0.5717, 0.047901), ("enjeux", 0.5356, 0.048676)):
    print(ligne(nom, f"Q={Q}", f"w={w}", f"aire minimale={aire_minimale(Q, w, 0.9875):.4f}"))
print("attendu par T0.7 scellé : 0,6408 (tromperie) et 0,6058 (enjeux)")
print()
print("## 2. Aire minimale détectable à 80 %, règle (a), 64 tâches, aire moyenne des deux plis")
print("niveaux : 99 % (Bonferroni sur les cinq cellules d'un bras), 95 % (réserves et descriptifs)")
for niveau in (0.99, 0.95):
    for w in (0.047901, 0.048676):
        s = s_formule(w, 64)
        marge = (z_bilateral(niveau) + Z08) * s
        valeurs = ", ".join(f"Q={Q:.2f}: {Q + marge:.4f}" for Q in (0.50, 0.53, 0.55, 0.60, 0.65, 0.70, 0.80, 0.90))
        print(ligne(f"niveau={niveau}", f"w={w}", f"s={s:.6f}", f"marge={marge:.4f}", valeurs))
print()
print("## 3. Écart minimal détectable d'une différence appariée d'aires (sonde moins adversaire ; TE moins ART)")
print("écart type de la différence pris à c fois s (c = 1 : corrélation semblable à celle de D sur P3)")
for niveau in (0.99, 0.95):
    s = s_formule(0.048676, 64)
    print(ligne(f"niveau={niveau}", ", ".join(f"c={c}: {(z_bilateral(niveau) + Z08) * c * s:.4f}" for c in (0.5, 0.75, 1.0, 1.25, 1.5))))
print()
print("## 4. Écart type nul de l'aire et repères")
for n1, n0 in ((640, 640), (320, 320), (100, 300), (50, 200), (30, 100)):
    sg = sigma_nul(n1, n0)
    print(ligne(f"n1={n1}", f"n0={n0}", f"sigma={sg:.6f}",
                f"quantile 0,95 sous le nul={0.5 + N.inv_cdf(0.95) * sg:.4f}",
                f"réserve 95 % (borne basse > 0,5) détectable={0.5 + (z_bilateral(0.95) + Z08) * sg:.4f}",
                f"aire minimale 95 % (formule du texte de validité, plancher 0,5 + 1,645 sigma)={0.5 + (N.inv_cdf(0.95) + 1.10 * (z_bilateral(0.95) + Z08)) * sg:.4f}"))
q_temoin = 0.5 + N.inv_cdf(0.95) * sigma_nul(640, 640)
print(ligne("témoin de sélectivité (100 réétiquetages)", f"quantile 0,95 attendu sous le nul={q_temoin:.4f}",
            f"aire minimale à 99 %={aire_minimale(q_temoin, 0.048676, 0.99):.4f}"))
print()
print("## 5. Devis (heures de carte A100 SXM4 80 Go ; USD)")
passes = {"O : états d'origine, 9 conditions x 64": 576, "J_d : textes de S_d sous le modèle nu, 4 x 64": 256,
          "J_IA : textes de IA sans consigne, modèle nu": 64, "A_d : textes de H sous l'adaptateur saboteur, 4 x 64": 256,
          "A_T : textes de H sous T100": 64}
total_passes = sum(passes.values())
for k, v in passes.items():
    print(ligne(k, v))
print(ligne("passes au total", total_passes, f"heures de passe à 0,45 s : {total_passes * 0.45 / 3600:.3f}"))
cellules = 5
configs = 2 * 3 * 3                       # familles x couches x régularisations
par_cellule = 2 * 4 * configs + 2         # deux plis externes x quatre plis internes x grille, plus deux sondes finales
sondes_tache = cellules * par_cellule
sondes_lecteur = cellules * par_cellule
temoins = 100 * 2 * cellules
entrainements = sondes_tache + sondes_lecteur + temoins
print(ligne("entraînements", f"sondes de la tâche {sondes_tache}", f"lecteur honnête {sondes_lecteur}",
            f"témoins de sélectivité {temoins}", f"total {entrainements}"))
for sec in (2.0, 3.0, 4.0):
    print(ligne(f"à {sec} s par entraînement", f"{entrainements * sec / 3600:.2f} h"))
postes = [("mise en place (image, modèle, dépôt, données de 7b)", 1.0, 1.0),
          ("essais ciblés sur l'instance, égalité carte-processeur", 0.5, 0.5),
          ("contrôles d'identité des adaptateurs", 0.05, 0.05),
          ("relecture forcée et écriture des activations (3 couches, demi-précision)", 0.35, 0.55),
          ("garde d'équivalence sur la série O", 0.05, 0.05),
          ("entraînement, 2 à 4 s par apprentissage supposés (chargement compris, 0,2 h)", 1.6, 2.9),
          ("planchers et notation de toutes les séries", 0.2, 0.4),
          ("écriture des scores fermés, sceaux, poussée", 0.2, 0.2)]
bas = sum(p[1] for p in postes)
haut = sum(p[2] for p in postes)
for nom, a, b in postes:
    print(ligne(nom, a, b))
print(ligne("total de marche attendu (h)", f"{bas:.2f}", f"{haut:.2f}"))
calc_bas, calc_haut = bas * 1.0889, haut * 1.30
disque = 0.08 * (haut + 1.0)
telech = 40 * 0.05
print(ligne("calcul attendu (USD)", f"{calc_bas:.2f}", f"{calc_haut:.2f}", f"valeur centrale {((bas + haut) / 2) * 1.16:.2f}"))
print(ligne("disque au plus (USD)", f"{disque:.2f}", "téléchargement au plus (USD)", f"{telech:.2f}"))
print(ligne("attendu total (USD)", f"{calc_bas + 0.3 + 1.0:.2f}", f"{calc_haut + disque + telech:.2f}"))
p1_h = 2 * haut
p1 = p1_h * 1.40 + 0.08 * (p1_h + 1.0) + telech
p2 = p1 + p1_h * 1.40 + telech
p3 = p1_h * 4.70 + 0.08 * (p1_h + 1.0) + 2 * telech
print(ligne("P1 : hôte deux fois plus lent, 1,40 USD/h", f"{p1_h:.1f} h", f"{p1:.2f} USD"))
print(ligne("P2 : P1 plus une relance complète au même débit", f"{2 * p1_h:.1f} h", f"{p2:.2f} USD"))
print(ligne("P3 : H200 NVL à 4,70 USD/h aux heures de P1 (mot de Lazar seulement)", f"{p1_h:.1f} h", f"{p3:.2f} USD"))
