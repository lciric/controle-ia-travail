# Extrait — sortie des calculs du brouillon 5 de G1

- **Fabriqué par programme** : `docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py`, fiche `docs/notes/g1-extraits-tiers-v1/fiches/fiche-calculs-g1-brouillon5-sortie-v1.json` (numéros de lignes et bornes seulement) ; tiers d'extraction (session_013QMayjcfUDMKLzsbuNwNHm). Classe C.
- **Source** : `brouillons/preuves-mentors-v1/g1-prereg-v1/calculs-g1-brouillon5-v1-sortie.txt` (lue sur `refs/remotes/origin/canal/conv-audit-n04`), empreinte `d53e7e5a81058217df12ed3ea3c1066ae4260f3a0945cd8e4a85ec04258d00fe`, 122 lignes.
- **Objet** : demande 1 du rédacteur successeur : paragraphes 1 à 3 et 5 à 9.
- **Lignes reprises** : 1–31, 65–118 ; recopiées à l'octet. Les lignes et passages non repris le sont pour l'objet de la demande ou par prudence ; le motif n'est pas donné ligne par ligne.
- **Statut** : à transmettre seulement si le rapport d'un vérificateur neuf le déclare propre.

---

<!-- lignes 1 à 31 de la source -->
# Sortie de calculs-g1-brouillon5-v1.py
Python 3.13.18 ; numpy 2.5.3 ; scipy 1.18.1
Aucune graine : tous les calculs sont déterministes (formules fermées).

## 1. Seuil par action à 1 % : fausses alarmes par épisode, actions indépendantes (brouillon 3, Métrique)

T =  10 actions : 1 - 0,99^T = 0,0956
T = 100 actions : 1 - 0,99^T = 0,6340

## 2. Seuil conforme sur K épisodes honnêtes entiers (rang ceil((K+1)(1-a)) ; taux réel ~ Bêta(K+1-r, r))

a = 0,01 : plus petit K pour un seuil fini = 99
a = 0,05 : plus petit K pour un seuil fini = 19

a = 0,01 ; P(taux réel de fausses alarmes > 0,02 | calibrage) :
  K =     99 : rang     99 ; P(> 0,02) = 0,1353
  K =    299 : rang    297 ; P(> 0,02) = 0,0611
  K =    499 : rang    495 ; P(> 0,02) = 0,0285
  K =    999 : rang    990 ; P(> 0,02) = 0,0047
  K =   4000 : rang   3961 ; P(> 0,02) = 0,0000
  K =  40000 : rang  39601 ; P(> 0,02) = 0,0000
  K =  64000 : rang  63361 ; P(> 0,02) = 0,0000

## 3. Borne haute unilatérale à 95 % de Clopper-Pearson pour un taux observé de 1 %

  n =    300,    3 alarmes : borne haute = 0,0256
  n =    700,    7 alarmes : borne haute = 0,0187
  n =   4000,   40 alarmes : borne haute = 0,0130
  n =   6400,   64 alarmes : borne haute = 0,0123
  n =  40000,  400 alarmes : borne haute = 0,0109

[lignes 32 à 64 non reprises]
<!-- lignes 65 à 118 de la source -->
## 5. Intersection-union : puissance conjointe si les fiches étaient indépendantes (illustration prudente)

  puissance par fiche 0,9 : 1 fiche(s) -> 0,900 ; 2 fiche(s) -> 0,810 ; 3 fiche(s) -> 0,729 ; 4 fiche(s) -> 0,656 ; 6 fiche(s) -> 0,531
  puissance par fiche 0,8 : 1 fiche(s) -> 0,800 ; 2 fiche(s) -> 0,640 ; 3 fiche(s) -> 0,512 ; 4 fiche(s) -> 0,410 ; 6 fiche(s) -> 0,262
Les fiches partagent les jumeaux honnêtes et les comparateurs : elles sont corrélées positivement, la puissance
conjointe réelle est au-dessus du produit (borne basse sous dépendance positive, non démontrée ici).

## 6. Holm sur e-valeurs converties en p = min(1, 1/e) : seuils d'e-valeur par rang, a = 0,05

  famille de 4 : rang 1 : p <= 0,0125 (e >= 80) ; rang 2 : p <= 0,0167 (e >= 60) ; rang 3 : p <= 0,0250 (e >= 40) ; rang 4 : p <= 0,0500 (e >= 20)
  famille de 3 : rang 1 : p <= 0,0167 (e >= 60) ; rang 2 : p <= 0,0250 (e >= 40) ; rang 3 : p <= 0,0500 (e >= 20)

## 7. Devis de la campagne de G1 (T1.2) : épisodes, heures de carte A100 80 Go, dollars

Hypothèses : K_s = 10 (R-504), K_h = 10 (R-733 N2), 3 modes (coût, contrôles, tenu à l'écart),
témoin et mention 12 par tâche, disques, téléchargements et extraction des tâches non comptés.

### variante minimale : 288 tâches x 152 épisodes = 43 776 épisodes (n_h plancher 288 (R-716, R-719) ; famille (ii) seule ; calibrage 10 fois)
      bas : 42,10 s + 1 x 58,2 s = 100,3 s par épisode ; 1 220 h ; 1 317 USD
  central : 48,35 s + 2 x 58,2 s = 164,8 s par épisode ; 2 003 h ; 2 297 USD
     haut : 54,60 s + 4 x 58,2 s = 287,4 s par épisode ; 3 495 h ; 4 240 USD
  tension : 54,60 s + 8 x 58,2 s = 520,2 s ; 6 326 h ; 9 046 USD (prix 1,43)

### variante par défaut : 400 tâches x 232 épisodes = 92 800 épisodes (400 unités sans mesure au pilote (R-556 (2)) ; (ii) et (i-a) ; calibrage 15 fois)
      bas : 42,10 s + 1 x 58,2 s = 100,3 s par épisode ; 2 586 h ; 2 792 USD
  central : 48,35 s + 2 x 58,2 s = 164,8 s par épisode ; 4 247 h ; 4 870 USD
     haut : 54,60 s + 4 x 58,2 s = 287,4 s par épisode ; 7 409 h ; 8 989 USD
  tension : 54,60 s + 8 x 58,2 s = 520,2 s ; 13 410 h ; 19 176 USD (prix 1,43)

### variante plafond de la table : 544 tâches x 242 épisodes = 131 648 épisodes (n_h maximal de la table v9 au seuil 160 (rho chapeau 0,17) ; 16 fois)
      bas : 42,10 s + 1 x 58,2 s = 100,3 s par épisode ; 3 668 h ; 3 961 USD
  central : 48,35 s + 2 x 58,2 s = 164,8 s par épisode ; 6 025 h ; 6 908 USD
     haut : 54,60 s + 4 x 58,2 s = 287,4 s par épisode ; 10 510 h ; 12 752 USD
  tension : 54,60 s + 8 x 58,2 s = 520,2 s ; 19 023 h ; 27 203 USD (prix 1,43)

Plafond proposé (variante par défaut, estimation centrale x 1,3, marge du brief § 14) : 6 331 USD ; alerte à 80 % : 5 064 USD
Durée murale de la variante par défaut, estimation centrale : 4 247 h de carte ; sur 20 cartes en parallèle : 8,8 jours ; sur 40 : 4,4 jours
Part du calibrage honnête dans la variante par défaut : 0,647
Prix central retenu : 1,1467 USD de l'heure ; génération centrale 48,35 s

## 8. Règle des graines (R9) : racine tirée de l'empreinte du texte scellé — démonstration sur une empreinte connue

empreinte d'exemple (brouillon 3, jamais utilisée pour G1) : e488d0658c7ab6fd964eb269d3b5e675b7c93a0873f666482bf8c71551b609c4
entropie = int(empreinte, 16) = 103369058978783545414536266751319004429566687541780039550350674988902020155844
clé de dérivation (1, 2, 17, 3) -> trois premiers entiers 32 bits : [412114354, 3683019775, 3981643205]
rejoué : [412114354, 3683019775, 3981643205] (identique attendu)
contrôle : sha256 de la chaîne de la clé = e86043b01f5c21b2…

## 9. Réglages des statistiques séquentielles (bases.sequentiel) proposés pour G1, T = 10, tau = 0,01

rho* du processus e unilatéral de mélange normal, n0 = 10, alpha = 0,01 (règle de la note v3, § 2, simulation_t03.calibrage.rho_optimal) : 1,0126 (frontière 10,604)
k de Page = 0,5 et fenêtre de balayage w = 5 : valeurs de T0.3 (simulation_t03/blocs.py, l. 97 et 230 ; « glissante_5 » de la grille v2)
empreinte du module lu : a2be6f6b127032aced5d75acd9cdf7c18c17e28df89978bd7102cf692c560def

[lignes 119 à 122 non reprises]
