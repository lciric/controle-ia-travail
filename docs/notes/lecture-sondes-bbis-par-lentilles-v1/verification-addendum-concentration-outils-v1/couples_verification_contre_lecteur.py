"""Contre-lecteur Opus 5.5 : couples de la vérification de l'addendum corrigé (924d0298…). Vérifie que chaque texte « avant » paraît
une seule fois dans la version, applique tous les couples à une copie, et écrit la section « Couples exacts » du rapport.
Usage : python -B couples_verification_contre_lecteur.py VERSION COPIE_APPLIQUEE SECTION_MD"""
import sys

COUPLES = [
    ("G1", "obligatoire", "EC-6 (ii) : bornes exactes au lieu de la borne haute qui compte toute direction marquée ; valeur p écrite et attendu "
     "des familles définis quand une direction est marquée (sinon le tri choisit encore en silence)",
     """> égalité au vingtième rang n'arrête pas à elle seule ; la direction nulle est **marquée**. Pour chaque statistique S qui dépend des
> vingt premiers jetons (part au-dessus du nul ; compte de chaque famille), le code rend, à côté de p, deux bornes :
> p_bas = (1 + #{j non marquée : S(u_j) ≥ S(v)}) / (M + 1) et p_haut = p_bas + (nombre de directions marquées) / (M + 1). Le libellé""",
     """> égalité au vingtième rang n'arrête pas à elle seule ; la direction nulle est **marquée**. Pour une direction marquée u_j et une
> statistique S qui dépend des vingt premiers jetons (part au-dessus du nul ; compte de chaque famille), S_min(u_j) et S_max(u_j)
> sont la plus petite et la plus grande valeur de S quand les places des vingt premiers que laissent les jetons de score strictement
> plus grand que le vingtième sont données, de toutes les façons possibles, aux jetons de score égal au vingtième. Le code rend, pour
> chaque S, deux bornes, sur les directions du même nul et de la même lentille :
> p_bas = (1 + #{j non marquée : S(u_j) ≥ S(v)} + #{j marquée : S_min(u_j) ≥ S(v)}) / (M + 1) et
> p_haut = (1 + #{j non marquée : S(u_j) ≥ S(v)} + #{j marquée : S_max(u_j) ≥ S(v)}) / (M + 1) : la plus petite et la plus grande
> valeur p que donnerait un départage. Quand une direction est marquée, la valeur p écrite dans les tables et les phrases est p_haut
> (sens conservateur), p_bas écrit à côté, et l'attendu sous le nul d'une famille est la moyenne sur les seules directions non
> marquées. Le libellé"""),
    ("G2", "obligatoire", "EC-5 de la garde, essais : les essais des directions nulles suivent G1",
     """- **direction nulle, cas sain** : une direction nulle à égalité au vingtième rang, libellé égal aux deux bornes : pas d'arrêt, une
  direction marquée écrite, p_haut − p_bas = 1/(M + 1) ;
- **direction nulle, artefact** : jouet à M = 99 où, pour une famille, p_bas = 0,01 sous les deux nuls et p_haut = 0,02 sous l'un
  d'eux (une direction marquée ; libellé « sur-représentée » à une borne seulement) : arrêt, message (ii) ;""",
     """- **direction nulle, cas sain** : une direction nulle à égalité au vingtième rang, avec S_min < S(v) ≤ S_max, libellé égal aux deux
  bornes : pas d'arrêt, une direction marquée écrite, p_haut − p_bas = 1/(M + 1) ; une direction marquée avec S_max < S(v) :
  p_bas = p_haut, pas d'arrêt ; S_min et S_max égaux au plus petit et au plus grand S d'une énumération de tous les départages, sur
  un jouet à trois jetons de même score au vingtième rang ; valeur p écrite égale à p_haut ; attendu calculé sans la direction
  marquée ;
- **direction nulle, artefact** : jouet à M = 99 où, pour une famille, p_bas = 0,01 sous les deux nuls et p_haut = 0,02 sous l'un
  d'eux (une direction marquée avec S_min < S(v) ≤ S_max ; libellé « sur-représentée » à une borne seulement) : arrêt, message (ii) ;
  le même jouet où la direction marquée a S_max < S(v) : pas d'arrêt ;"""),
    ("G3", "obligatoire", "EC-6 (i) : les listes de dix des pôles sont des listes montrées de la direction lue ; sans garde, le tri y choisit en silence",
     """> (i) **Direction lue** (chaque vecteur, chaque signe, chaque lentille, lentille des logits comprise ; chaque liste qui entre dans
> une table ou une comparaison : vingt premiers par score, vingt premiers par z sous le nul isotrope, listes du témoin de couche) :""",
     """> (i) **Direction lue** (chaque vecteur, chaque signe, chaque lentille, lentille des logits comprise ; chaque liste qui entre dans
> une table ou une comparaison : vingt premiers par score, vingt premiers par z sous le nul isotrope, listes du témoin de couche ;
> et les deux listes de dix des pôles, les dix pôles par cosinus et les dix premiers jetons de la lecture de chaque pôle, où
> l'égalité se lit entre la dixième et la onzième valeur) :"""),
    ("G4", "obligatoire", "EC-6 (iii), dernière phrase, accordée à G3",
     """> nul). La concentration, les pôles et les bornes de calibration ne sont pas concernés : aucun n'emploie les vingt premiers jetons.""",
     """> nul). La concentration, la concentration des pôles (cosinus maximal, rang parmi les maxima nuls) et les bornes de calibration ne
> sont pas concernées : aucune n'emploie une liste de premiers ; les listes de dix des pôles le sont, par (i)."""),
    ("G5", "obligatoire", "essai de G3",
     """  de la liste par z : arrêt ;""",
     """  de la liste par z : arrêt ; deux colonnes égales d'une matrice `W_down` jouet, au dixième et au onzième cosinus : arrêt ;"""),
    ("G6", "obligatoire", "EC-6, chiffres d'appui : valeur du modèle calculée sans comptage d'événements rares, et étendue selon l'échelle",
     """rang est de **7,0 × 10⁻⁶ par direction** (28 sur 4 000 000 ; ± 1,3 × 10⁻⁶) pour des scores centrés ; 3,2 × 10⁻⁵ si la moyenne des
scores vaut dix écarts types, 2,8 × 10⁻⁴ si elle en vaut cent (l'arrondi pèse plus quand les scores sont grands devant leur
dispersion). Soit, pour des scores centrés : rare pour une direction lue ; 0,014 direction marquée attendue par jeu de 2 000
directions nulles ; mais **1,4 égalité attendue sur les ≈ 195 000 lectures du calcul** (texte, plan, point 6), c'est-à-dire au moins
une avec une probabilité d'environ 0,74 (1 − e^(−1,36)), et davantage si les scores ne sont pas centrés (6 et 54 égalités attendues
aux deux autres lignes).""",
     """rang est de **9,0 × 10⁻⁶ par liste** pour des scores centrés réduits (valeur du modèle calculée par la contre-lecture sans compter
d'événements rares ; le comptage de l'auteur, 28 sur 4 000 000, soit 7,0 × 10⁻⁶ ± 1,3 × 10⁻⁶, en est une fluctuation basse), de
8,3 × 10⁻⁶ à 1,5 × 10⁻⁵ selon l'échelle des scores ; 3,6 × 10⁻⁵ si la moyenne des scores vaut dix écarts types, 2,9 × 10⁻⁴ si elle
en vaut cent (l'arrondi pèse plus quand les scores sont grands devant leur dispersion). Soit, pour des scores centrés : rare pour une
direction lue ; 0,018 direction marquée attendue par jeu de 2 000 directions nulles ; mais **1,6 à 2,9 égalités attendues sur les
≈ 195 000 lectures du calcul** (texte, plan, point 6), c'est-à-dire au moins une avec une probabilité de 0,80 à 0,95, et davantage si
les scores ne sont pas centrés (7 et 56 égalités attendues aux deux autres lignes)."""),
    ("G7", "obligatoire", "§ 9, point 7, option 1 : chiffre par liste et non par direction ; ce que l'option laisse passer",
     """     Avantage : la plus simple ; arrêt rare (≈ 7 × 10⁻⁶ par direction lue dans le modèle simple de EC-6). Inconvénient : une égalité
     sur une direction nulle reste tranchée en silence par le tri, et peut déplacer une valeur p de 1/2 001.""",
     """     Avantage : la plus simple ; arrêt rare (≈ 10⁻⁵ par liste dans le modèle simple de EC-6, soit de l'ordre de 0,5 à 1 % pour les
     quelque neuf cents listes des directions lues). Inconvénient : une égalité sur une direction nulle reste tranchée en silence par
     le tri, et peut déplacer une valeur p de 1/2 001, donc, rarement, un libellé, sans que rien ne l'écrive."""),
    ("G8", "obligatoire", "§ 9, point 7, option 2 : chiffre",
     """     ≈ 195 000 lectures, au moins une égalité est attendue avec une probabilité de l'ordre de 0,7 ou plus dans le même modèle ; la""",
     """     ≈ 195 000 lectures, au moins une égalité est attendue avec une probabilité de 0,8 à 0,95 dans le même modèle ; la"""),
    ("H1", "facultatif", "§ 9, point 7 : deux variantes que Lazar peut vouloir voir",
     """   - **Recommandation** : option 3 ; confiance moyenne à bonne (environ 0,75).""",
     """   - **Variantes, pour mémoire** : (a) adopter dès maintenant la règle de départage de la version 2 (score décroissant, puis
     identifiant croissant) : jamais d'arrêt, valeurs p valides (même règle pour v et les nuls) ; mais c'est un second écart au texte
     scellé, et, à score égal, la règle préfère toujours les petits identifiants ; (b) au lieu d'arrêter le calcul, rendre « non
     calculable » le seul libellé en cause (ou la seule direction lue à égalité), comme le texte le fait pour une calibration hors de
     ses bornes : la lecture continue et l'égalité est écrite ; mais un libellé manque sans mot de Lazar.
   - **Recommandation** : option 3 ; confiance moyenne à bonne (environ 0,75)."""),
    ("H2", "facultatif", "EC-6 : rendre connu d'avance le cas des lignes de sortie identiques, qui fait des égalités pour toute direction",
     """> | égalité au vingtième rang d'une direction nulle, décisive pour un libellé | arrêt ; nœud |.""",
     """> | égalité au vingtième rang d'une direction nulle, décisive pour un libellé | arrêt ; nœud |. Au montage, le code compte les paires de
> jetons gardés dont les lignes de `lm_head.weight` sont égales octet pour octet, et l'écrit, sans arrêt."""),
]


def main():
    version, copie, section = sys.argv[1:4]
    t = open(version, encoding="utf-8").read()
    lignes = ["## Couples exacts", "",
              "Texte « avant » copié de la version corrigée (`924d0298…`), retours à la ligne compris ; chacun y paraît une seule fois, et "
              "tous s'appliquent ensemble (vérifié par programme).", ""]
    for nom, nature, raison, avant, apres in COUPLES:
        n = t.count(avant)
        print(f"{nom} : avant présent {n} fois")
        assert n == 1, nom
        t = t.replace(avant, apres)
        lignes += [f"**{nom}** ({nature} : {raison}).", "", "Avant :", "", "```", avant, "```", "", "Après :", "", "```", apres, "```", ""]
    open(copie, "w", encoding="utf-8").write(t)
    open(section, "w", encoding="utf-8").write("\n".join(lignes))
    print("tous appliqués")


main()
