# Règle de mot de la carte de l'alarme (`fcbf4a2dd1a57`) — seuils fixés avant tout calcul — v1

Pièce de travail du rédacteur de l'additif 4 de la ligne 3. Écrite le 2026-11-20 vers 10:05Z, **avant** d'écrire et de lancer le calcul exact des lois du banc (`calcul_puissance_mot_alarme_ligne_3_v1.py`). Son empreinte compagnon est prise avant ce calcul : elle prouve que les seuils ne viennent ni d'une mesure de l'étage 1 (non lue), ni du calcul exact (pas encore fait). Aucun seuil ne changera après le calcul ; si le calcul montre un défaut de la règle, il sera dit, non corrigé en silence.

Bras : B = la sentinelle sur ancres ; D = le test sur le taux brut à coût apparié (m cartes de production de plus). Mélange planté, par cellule m, 2 000 suites : 1 000 sans changement, 500 « à effet », 500 « sans effet » (additif 1, règle D).

Comptes entiers, par cellule m :
- N0 = suites sans changement ; NE = suites « à effet ».
- F = suites sans changement où B sonne au moins une fois.
- EB, ED = suites « à effet » détectées par B, par D (alarme à la génération du changement ou après).
- n10 = suites « à effet » détectées par B et non par D ; n01 = l'inverse. EB − ED = n10 − n01.
- S = somme, sur les suites « à effet » détectées par B, du délai (génération de la première alarme à partir du changement, moins génération du changement).
- A = suites, parmi les 2 000, où B sonne au moins une fois (avant ou après le changement, changement ou non).

Clauses :
1. **Fausse alarme.** Atteinte si 100 F > 8 N0 (plus de 80 sur 1 000 : la borne 0,08 du texte, stricte, comme l'additif 1). Tenue sinon.
2. **Détection contre le bras apparié.** Dans cet ordre : « sans prise » si 100 ED ≥ 98 NE (plafond : rien à gagner), ou si 100 EB ≤ 2 NE et 100 ED ≤ 2 NE (plancher : changement invisible aux deux) ; sinon tenue si 100 (EB − ED) ≥ 5 NE (marge 0,05 de la ligne) et si le test du signe exact unilatéral sur les suites discordantes rend au plus 0,025 (40 × somme, pour k de n10 à n10 + n01, de C(n10 + n01, k) ≤ 2^(n10 + n01)) ; sinon atteinte si EB ≤ ED (lettre de la clause de réfutation du texte) ; sinon indécise.
3. **Délai.** Indéfinie si EB = 0. Tenue si S ≤ EB (délai moyen d'une génération au plus : une chance sur deux au moins de voir, à chaque regard, un changement présent). Atteinte si 6 S ≥ 17 EB (délai moyen de 17/6 générations ou plus : celui d'une alarme dont l'instant ne doit rien au changement). Indécise sinon.
4. **Part des alarmes à effet**, lecture (b) de l'additif 1 (EB / A). Indéfinie si A = 0. Tenue si 2 EB > A (une suite en alarme sur deux, au moins, porte un changement à effet détecté). Atteinte si 4 EB ≤ A (pas mieux que la part des suites « à effet » dans le mélange planté, un quart). Indécise sinon. La lecture (a) est rapportée, sans seuil.

Mot de la cellule m, dans cet ordre, après la garde du mélange planté (1 000 ; 500 ; 500 ; 1 000, sinon faute du banc, aucun mot) :
- « réfuté sur le banc » si la clause 1 est atteinte ;
- sinon « sans prise » si la clause 2 est « sans prise » ;
- sinon « réfuté sur le banc » si l'une des clauses 2, 3 ou 4 est atteinte ;
- sinon « tient sur le banc » si les clauses 1, 2, 3 et 4 sont tenues ;
- sinon « sans prise ».

Mot de la carte : lu sur m = 20 et m = 40 (le seul appui de taille du texte : « à partir de 20 ancres par génération »). « réfuté sur le banc » si l'une des deux cellules l'est ; sinon « tient sur le banc » si les deux tiennent ; sinon « sans prise ». La cellule m = 10 reçoit son mot de cellule, rapporté, hors du mot de la carte.

Racines neuves : essais 2026112041 ; chronométrage 2026112042 ; passage décisif 2026112043.

Rédacteur neuf, modèle F.
