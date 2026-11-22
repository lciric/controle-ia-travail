# Extrait — sortie des calculs du devis du brouillon 7 de G1, paragraphes 1 à 3

- **Fabriqué par programme** : `docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py`, fiche `docs/notes/g1-extraits-tiers-v1/fiches/fiche-calculs-g1-brouillon7-sortie-v1.json` (numéros de lignes et bornes seulement) ; tiers d'extraction (session_013QMayjcfUDMKLzsbuNwNHm). Classe C.
- **Source** : `docs/notes/g1-brouillon7-fable-v1/calculs/calculs-g1-brouillon7-v1-sortie.txt` (lue sur `origin/prep/g1-brouillon7-fable-v1`), empreinte `ed8677f61d4cbfd03c0e7988cf35a1f076337f993af0327eb00b045d57b13357`, 84 lignes.
- **Objet** : demande 7 du rédacteur successeur : arithmétique du devis et du bruit de seuil.
- **Lignes reprises** : 1–35 ; recopiées à l'octet, sauf 1 passage(s) remplacé(s) par « [passage non repris] » (ligne(s) 11). Les lignes et passages non repris le sont pour l'objet de la demande ou par prudence ; le motif n'est pas donné ligne par ligne.
- **Statut** : à transmettre seulement si le rapport d'un vérificateur neuf le déclare propre.

---

<!-- lignes 1 à 35 de la source -->
# Sortie de calculs-g1-brouillon7-v1.py
Python 3.13.18 ; bibliothèque standard seule (math)
Aucune graine : tous les calculs sont déterministes.

## 1. Contrôle : la variante par défaut du brouillon 6 est retrouvée (même modèle de coût que [calc § 7] du brouillon 5)

Épisodes par tâche (brouillon 6) : 10 jumeaux + 3 modes x 10 x 2 familles + 12 témoin bénin et mention + 150 de calibrage honnête = 232
Variante par défaut : 400 tâches x 232 = 92 800 épisodes ; central 4 247 h, 4 870 USD (attendu d'après le brouillon 6 : 92 800 épisodes, 4 247 h, 4 870 USD)
Contrôle : conforme.

## 2. Épisodes du témoin apparié selon l'énoncé retenu ([passage non repris]brouillon de décision N-074, non pris)

Épisodes d'évaluation du témoin par tâche, communs à tous les énoncés : 3 modes x 10 (organisme sans consigne) + 3 modes x 3 (organisme à consigne) = 39
Par cellule de la porte (un mode, organisme sans consigne) : 400 x 10 = 4 000 épisodes d'évaluation du témoin (le brouillon de N-074 en demande au moins 300)

| variante | épisodes par tâche | épisodes | heures de carte (bas / central / haut) | USD (bas / central / haut) | central x 1,3 | rapport au plafond accordé (6 331 USD) |
|---|---|---|---|---|---|---|
| sans témoin apparié (brouillon 6, rappel) | 232 | 92 800 | 2 586 / 4 247 / 7 409 | 2 792 / 4 870 / 8 989 | 6 331 | 1,00 |
| garde de spécificité, ou garde avec contraste rapporté à 5 % (énoncés B et C2) | 271 | 108 400 | 3 020 / 4 961 / 8 654 | 3 262 / 5 688 / 10 500 | 7 395 | 1,17 |
| contraste, calibrage du témoin au minimum du brouillon de N-074 : 300 épisodes par cellule, 6 cellules (énoncés A et C1) | 275,5 | 110 200 | 3 070 / 5 043 / 8 798 | 3 316 / 5 783 / 10 674 | 7 518 | 1,19 |
| contraste, calibrage du témoin à l'échelle du calibrage honnête, cellules de la porte seules : 2 témoins x 150 par tâche (énoncés A et C1) | 571 | 228 400 | 6 363 / 10 452 / 18 234 | 6 873 / 11 985 / 22 123 | 15 581 | 2,46 |
| contraste, calibrage du témoin à l'échelle du calibrage honnête, les trois modes de l'organisme sans consigne : 3 témoins x 150 par tâche (énoncés A et C1) | 721 | 288 400 | 8 035 / 13 198 / 23 024 | 8 678 / 15 134 / 27 935 | 19 674 | 3,11 |

Non comptés, en plus de ceux du brouillon 6 : une distillation de plus par témoin d'adaptateur et sa remise à l'intensité du saboteur ; la conception du témoin du mode tenu à l'écart par son concepteur.

## 3. Bruit d'un seuil conforme à 1 % : écart-type du taux réel de fausses alarmes selon le nombre d'épisodes de calibrage (épisodes indépendants ; taux réel ~ Bêta(K + 1 - r, r), r = ceil((K + 1) x 0,99))

  K =    300 : rang    298 ; taux réel moyen 0,997 % ; écart-type 0,572 point
  K =   1200 : rang   1189 ; taux réel moyen 0,999 % ; écart-type 0,287 point
  K =   4000 : rang   3961 ; taux réel moyen 1,000 % ; écart-type 0,157 point
  K =  12000 : rang  11881 ; taux réel moyen 1,000 % ; écart-type 0,091 point
  K =  18000 : rang  17821 ; taux réel moyen 1,000 % ; écart-type 0,074 point
  K =  60000 : rang  59401 ; taux réel moyen 1,000 % ; écart-type 0,041 point
Repères de l'étude de la formulation (d04da790…, texte) : 0,57 point à 300 épisodes ; 0,09 à 12 000 ; 0,07 à 18 000.
Calibrage d'épreuve du brouillon 6 : 150 épisodes honnêtes par tâche x 400 tâches = 60 000 épisodes (groupés par tâche : l'information réelle est moindre que celle d'épisodes indépendants ; le contrôle par moitiés jumelles le mesure).
[lignes 36 à 84 non reprises]
