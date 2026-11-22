# Notes du développeur neuf des deux passes — étape 1 : le code de la première passe accordé à l'addendum de concentration scellé — v2

Pièce de travail (classe C) qui accompagne un code de classe B. Développeur neuf des deux passes, sous-agent de la session des
lentilles (`session_01QPDgKhLLz1oJQwPBeB5aFs`), modèle servi Fable 5.2, branche `claude/brave-galileo-jhp684`, 2026-11-20 (UTC).
Suit `notes-developpement-v1.md` (premier développeur), qui reste valable pour tout ce que cette étape ne change pas.

- Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-deux-passes-lentilles-v1.md`,
  `0a9517ea4e1d7460b411a0914996503eb3c6a9a680b4d3c88ae9d4f1f67bbdfc` (vérifié avant toute lecture ; commit `dbd65821`).
- Texte v1 scellé : `prereg/lecture-sondes-bbis-par-lentilles-v1.md`, `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`
  (absent de cette branche : lu sur la branche principale par `git show origin/main:…`, empreinte recalculée, égale).
- Addendum scellé : `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
  `7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970` (compagnon vérifié).
- **Étape 1 seulement.** L'étape 2 (seconde passe) n'est pas entamée.

## 1. Ce qui est rendu

| pièce | chemin |
|---|---|
| code neuf (trois modules) | `src/controle_ia/lentilles_sondes_bbis/entrees_v3.py` (clé de l'addendum, EC-4) ; `statistiques_v3.py` (garde d'égalité au vingtième rang, EC-6 ; précision de la comparaison, C5 ; formules de EC-1 et EC-2 reprises de `statistiques_v2` par appel) ; `lanceur_v4.py` (`lanceur_v3` plus l'addendum) |
| code inchangé, employé | `__init__`, `constantes_v1`, `entrees_v2`, `montage_v1`, `lecture_v1`, `nuls_v1`, `statistiques_v1`, `statistiques_v2`, `audits_v1`, `phrases_v1` : aucun octet changé (R12) |
| essais neufs | `tests/test_lentilles_sondes_bbis_addendum_concentration_v2.py` ; `tests/test_lentilles_sondes_bbis_garde_egalite_v1.py` |
| essais repris, visant le code neuf | `tests/lentilles_sondes_bbis_jouets_v4.py` ; `tests/test_lentilles_sondes_bbis_{entrees,montage,procedure}_v4.py`, `…_nuls_statistiques_v3.py`, `…_gardes_non_vues_v3.py`, `…_corrections_contre_lecture_v3.py` |
| table des essais | `table-essais-v2.md` (ce dossier) |
| note de conformité, point par point | `conformite-code-a-l-addendum-concentration-scelle-v1.md` (ce dossier) |
| sortie des essais du paquet | `sortie-essais-v4.txt` (ce dossier) : `1125 passed in 519.98s` |
| empreintes du code et des essais | `empreintes-code-v4.txt` (ce dossier) |
| outils | `outils/fabrique-lanceur-v4-v1.py` (remplacements exacts de `lanceur_v3` à `lanceur_v4`) ; `outils/essai-des-essais-v3.py` et `outils/sortie-essai-des-essais-v3.txt` ; `outils/banc-taille-reelle-v3.py` et `outils/sortie-banc-taille-reelle-v3.txt` |

Le lanceur (`python -m controle_ia.lentilles_sondes_bbis.lanceur_v4`) garde ses quatre sous-commandes (`montage`, `recuperer`,
`calcul`, `phrases`). Il n'inscrit aucune ligne de registre et ne pousse rien. **Pour qu'il parte, il faut**, au registre propre :
`SCELLEMENT-`, `GO-` et `CODE-LENTILLES-BBIS`, `ABSENCE-VERDICT-LENTILLES-BBIS`, et la ligne
`ADDENDUM-CONCENTRATION-LENTILLES-BBIS` (une seule, placée avant `CODE-LENTILLES-BBIS`) ; et, dans la fiche citée par
`CODE-LENTILLES-BBIS`, les empreintes des **treize** modules de `lanceur_v4.MODULES` sous `fichiers`, et le champ
`addendum_concentration` : `{"chemin": "prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md", "sha256":
"7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970"}`.

## 2. Ce qui change, en mots

- **Clé de l'addendum (EC-4)** : rien ne part (montage, récupération, calcul) sans la ligne de l'addendum, seule, placée avant
  `CODE-LENTILLES-BBIS` et `ENTREES-LENTILLES-BBIS`, de l'empreinte que portent la fiche du code et le code. Le rapport du montage,
  les tables et le manifeste citent l'addendum à côté du texte.
- **Statistique des directions nulles (EC-1, EC-2)** : celle de `statistiques_v2`, inchangée ; la comparaison C(u_j) ≥ C(v) est
  faite explicitement en simple précision (C5).
- **Garde d'égalité au vingtième rang (EC-6, option 3)** : direction lue : arrêt nommé, avant toute écriture de table ; direction
  nulle : marquée, p_bas et p_haut, la valeur p écrite est p_haut, arrêt nommé si un libellé diffère entre les deux bornes ;
  témoin : compté ; au montage, compte des paires de jetons gardés de même ligne de sortie.
- **Tables** : champs neufs `addendum`, `egalites_au_vingtieme_rang`, et, par lecture et par nul, `p_part_bas`, `p_part_haut`,
  `directions_nulles_marquees`, `familles/<nom>/p_bas`, `p_haut` ; `garde_egalite` par lecture ; `conventions` complétées. Les
  phrases gelées ne changent pas d'un mot.
- **Remarque reprise de la vérification de la version 2 du code** : le rapport du montage est exigé au départ du calcul.

## 3. Ce que j'ai lu (déclaration)

- `CLAUDE.md` ; mon mandat et celui du premier développeur, en entier ; le mot de Lazar sur la garde d'égalité
  (`docs/notes/neuron-lens-v1/mot-lazar-garde-egalite-vingtieme-rang-2026-11-19-v1.md`, vérifié).
- Le texte v1 scellé, en entier ; l'addendum scellé, en entier.
- **Le texte v2 scellé** (`prereg/lecture-sondes-bbis-par-lentilles-v2.md`, `a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`,
  lu sur la branche principale, empreinte recalculée, égale) : **pas en entier à cette étape** — la liste de ses titres de sections
  (par recherche) et les lignes 2428 à 2520 de sa section « Code neuf » (ce que la seconde passe réemploie et ajoute), pour choisir
  des noms qui ne gênent pas l'étape 2 (`montage_v2`, `audits_v2`, `phrases_v2` et le module neuf des statistiques de la seconde
  passe lui sont laissés). **Écart au mandat, déclaré** : le mandat demande de lire les trois textes en entier ; le texte v2 ne
  commande rien de l'étape 1, et je le lirai en entier au départ de l'étape 2, avant d'écrire une ligne de la seconde passe.
- Du registre propre de ces textes (`registres/lecture-sondes-bbis-par-lentilles-v1.md`, branche principale, permis en entier) :
  ses cinq lignes. **Constat** : il porte la ligne de l'addendum (2026-11-19T16:35:35Z, `7c738708…`) ; il ne porte, à ma lecture,
  ni `GO-LENTILLES-BBIS` ni `CODE-LENTILLES-BBIS` : le code refusera de partir tant qu'elles manquent (texte, « Liste d'arrêt »).
- Le dossier `developpement/` : note de conformité de la version 3, passation, notes v1, les trois notes de traitement de la
  contre-lecture, renvois des chiffres ; de `table-essais-v1.md`, les quarante premières lignes ; de `empreintes-code-v3.txt`, les
  huit premières ; des outils, `essai-des-essais-v2.py`, `banc-taille-reelle-v2.py` et sa sortie.
- Le paquet `src/controle_ia/lentilles_sondes_bbis/` : `__init__`, `constantes_v1`, `statistiques_v1`, `statistiques_v2`,
  `audits_v1`, `entrees_v2`, `lanceur_v3`, `lecture_v1`, `phrases_v1`, `nuls_v1` en entier ; `montage_v1` : la liste de ses
  fonctions et `charger_tenseur` ; les différences de `lanceur_v2` à `lanceur_v3` et de `entrees_v1` à `entrees_v2`. Les essais :
  `jouets_v3` en entier, `addendum_concentration_v1` en entier, et les passages des autres que j'ai dû accorder.
- Des pièces de l'addendum (`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`) : `bornes_calibration_statistique_corrigee_v2.py`
  (`0f31484b…`, lignes 1 à 70) et les trente premières lignes de sa sortie (`39a410e4…`).
- **Vu par des listes de noms seulement** : les noms des fichiers de `prereg/` qui portent « lentilles » (branche principale), du
  dossier des pièces, du dossier `mandats/`, du dossier `developpement/` et de ses outils.
- **Non refait** : la vérification des noms des clés et des champs au commit de la dernière ligne `CODE-BBIS` (faite par le premier
  développeur, `notes-developpement-v1.md`, § 2) : `entrees_v2`, qui les porte, n'est pas changé ; je n'ai ouvert ni
  `registres/t07-etape-b-bis-v1.md` ni le code de `src/controle_ia/t07bbis/`.
- **Jamais ouvert** : aucun fichier sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `donnees/*` ni `calcul/*` ;
  aucun fichier de scores, aucune table, aucune lecture, aucun verdict de l'apprentissage des sondes sur la tâche ; aucune sortie de
  la lecture par la lentille publique ; aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; aucun autre
  registre. **Aucune exposition involontaire à déclarer.**
- **Aucun téléchargement** de Llama, d'une lentille, d'un fichier d'ajustement ni d'un corpus ; aucune clé lue ni testée (les essais
  emploient une fausse clé, dans un environnement passé en argument) ; aucune machine, aucune dépense. Deux `git fetch origin main`
  en lecture (pour les textes v1 et v2 et le registre propre).

## 4. Environnement des essais

Environnement Python du bloc-notes de la session (hors du dépôt), installé depuis le registre public de paquets, coût nul :
torch 2.14.1+cpu (index de PyTorch pour processeur), transformers 5.18.0, tokenizers 0.23.2, safetensors 0.8.0,
huggingface_hub 1.33.0, scipy 1.17.1 ; numpy 2.5.3 et pytest 9.1.1 du conteneur ; Python 3.13. Quatre fils, 15 Go de mémoire.

## 5. Essais

- **Essais du paquet** (`python -m pytest -q -p no:cacheprovider tests/test_lentilles_sondes_bbis_*.py`, avec `PYTHONPATH=src`) :
  **1 125 essais, tous verts** (`1125 passed in 519.98s`), dont 371 de plus qu'avant cette étape (`sortie-essais-v4.txt`). Avant mon premier changement, les mêmes fichiers rendaient `754 passed` (sept minutes) : les
  essais des versions 1 à 3 restent verts.
- **Essai des essais** (`outils/essai-des-essais-v3.py`) : **quarante-quatre altérations du code neuf, une à une, quarante-quatre vues** (`outils/sortie-essai-des-essais-v3.txt`). Une première
  passe, avant le rendu, avait montré quatre altérations non vues (quantile sans soi-même dans les bornes de départage ; valeur p
  écrite pour la part ; les deux comptes de la garde dans le lanceur) : trois essais ont été ajoutés ou renforcés
  (`sain_direction_nulle_marquee_bornes_a_un_cran_pour_la_part`, sixième cas de l'énumération,
  `couche_direction_nulle_marquee_et_temoin_a_egalite_comptes_ecrits_sans_arret`).
- Après cette sortie, un seul fichier d'essais a changé : `test_lentilles_sondes_bbis_addendum_concentration_v2.py` (l'essai
  `bornes_recalculees_par_le_programme_de_l_addendum` joue désormais le programme de l'addendum sur une copie hors du dépôt, pour ne
  rien écrire à côté de la pièce scellée) ; rejoué seul : `45 passed`. Le code n'a pas changé depuis la sortie.
- **Constat sur les essais existants, non corrigé (R12)** : l'essai des versions 1 à 3 qui charge la copie versée de `readout.py`
  laisse un dossier `__pycache__` à côté d'elle, sous `docs/sources/` (ignoré par git, mais compté par `verifier-arbre`) ; je l'ai
  retiré après mes essais. Jouer les essais avec `PYTHONDONTWRITEBYTECODE=1` l'évite.
- **Non lancés** : la suite complète du dépôt (plus de deux heures ici ; mandat) ; aucun fichier d'essais voisin n'est touché par
  ce code (aucun essai hors de `tests/test_lentilles_sondes_bbis_*.py` n'importe ce paquet). `verifier-arbre` : joué en fin
  d'étape (§ 8).

## 6. Banc sans données, à la taille réelle (matrices aléatoires ; aucune sonde, aucun poids, aucune lentille réelle)

`outils/sortie-banc-taille-reelle-v3.txt` (89 498 jetons, largeur 4 096, 14 336 neurones, M = 2 000, 4 fils) :
- une couche, deux vecteurs, deux lentilles : **87,0 s**, pointe **5,97 Go** (version 3 du premier développeur, même banc : 76,3 s
  et 5,97 Go) ; le compte des lignes de sortie égales du montage : 1,7 s, sans copie de la matrice ;
- calibration du banc : inchangée (49 et 47 pour [23, 85] ; 26 et 22 pour [6, 39]) ;
- garde d'égalité, **sur ces matrices aléatoires** : une direction nulle marquée (nul isotrope, lentille publique) sur 12 000
  directions nulles lues, aucun témoin à égalité sur 2 800, aucune direction lue à égalité (le calcul va à son terme). Ce n'est pas
  une mesure sur la lentille réelle, et ce n'est pas un résultat du programme ; cela montre seulement que l'étage (ii) sert.

## 7. Réserves (ce que les jouets ne prouvent pas)

- Celles de `notes-developpement-v1.md`, § 4, inchangées : réseau réel, tokeniseur lu du cache, paquets du voisin, mémoire.
- **Fréquence réelle des égalités** : inconnue (addendum, EC-6). Si une égalité tombe au vingtième rang d'une direction lue, le
  calcul s'arrête par construction (nœud) ; les jouets ne disent rien de cette fréquence.
- **Le message de l'arrêt (i)** porte deux identifiants de jeton et un score d'une direction lue, et sort par la ligne de commande :
  voir la note de conformité, § 4 (à porter à la session des lentilles, pour l'opérateur).
- Le champ `addendum_concentration` de la fiche du code est un nom que j'ai choisi (l'addendum ne le nomme pas) : la session
  principale doit l'écrire tel quel dans la fiche, sinon rien ne part.

## 8. Scellement et empreintes

Chaque pièce de ce dossier est scellée (`python -m controle_ia.scellement sceller`). Les empreintes des fichiers de code et d'essais
sont dans `empreintes-code-v4.txt`, scellé ; comme aux versions 1 à 3, aucun compagnon `.sha256` n'est posé à côté des fichiers de
code : la fiche `CODE-LENTILLES-BBIS`, que la session principale écrit, les portera. `python -m controle_ia.scellement verifier-arbre .` :
joué après le scellement des pièces de ce dossier ; son résultat est dans le message de rendu.

## 9. Fichiers à donner au contre-lecteur (classe B ; autre modèle : Opus 5.5, neuf)

- Les textes : `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`, branche principale), sections « Métrique », « Seuil »,
  « Plan d'analyse », « Liste d'arrêt », « Lignes de registre », « Code neuf » ; l'addendum scellé (`7c738708…`), en entier ; le mot
  de Lazar sur la garde (`docs/notes/neuron-lens-v1/mot-lazar-garde-egalite-vingtieme-rang-2026-11-19-v1.md`).
- Le code neuf : `src/controle_ia/lentilles_sondes_bbis/entrees_v3.py`, `statistiques_v3.py`, `lanceur_v4.py` ; et, pour ce qu'ils
  appellent : `statistiques_v2.py`, `statistiques_v1.py`, `entrees_v2.py`, `audits_v1.py`, `constantes_v1.py`, `lanceur_v3.py` (pour
  la différence avec `lanceur_v4`, que rend `outils/fabrique-lanceur-v4-v1.py`).
- Les essais : `tests/test_lentilles_sondes_bbis_addendum_concentration_v2.py`, `tests/test_lentilles_sondes_bbis_garde_egalite_v1.py`,
  `tests/lentilles_sondes_bbis_jouets_v4.py`, et les six fichiers repris (`…_entrees_v4.py`, `…_montage_v4.py`, `…_procedure_v4.py`,
  `…_nuls_statistiques_v3.py`, `…_gardes_non_vues_v3.py`, `…_corrections_contre_lecture_v3.py`).
- Les notes de ce dossier : `conformite-code-a-l-addendum-concentration-scelle-v1.md`, `table-essais-v2.md`, cette note,
  `sortie-essais-v4.txt`, `empreintes-code-v4.txt`, `outils/essai-des-essais-v3.py` et sa sortie, `outils/banc-taille-reelle-v3.py`
  et sa sortie.
- À vérifier d'abord : les quatre précisions de lecture de la note de conformité, § 3 ; `bornes_de_departage` contre une
  énumération indépendante ; la place de chaque appel de la garde dans `lanceur_v4` (toute liste d'une direction lue qui entre
  dans une table ou une comparaison) ; que `exiger_addendum` refuse chacun des cas de la « Liste d'arrêt » ; que rien d'autre ne
  change de `lanceur_v3` à `lanceur_v4`.
