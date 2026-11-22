# Rapport des essais R5 — lot B1 du pilote « oracles plantés » — v1

- Nature : rapport de travail (classe C), par l'exécutant du mandat `mandat-code-lot-b1-v1.md` (`407ef6f1…`), Opus 5.5 neuf, le 2026-11-22. Processeur seul, 0 USD, aucun appel de modèle, aucune machine louée.
- Commande : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_oracles_plantes_v1_*.py` (seulement ces fichiers ; la suite complète du dépôt n'a pas été lancée). Python 3.13.18, numpy 2.4.6.
- **Résultat : 122 essais passés, 0 échoué** (grammaire 34, évaluation 20, tests de mort et lignée 45, banque et rejeu 23), en 43 secondes environ.
- Paramètres : tous provisoires (`parametres_provisoires_v1.json`) ; racines d'essai seulement (20261122 dans les essais) ; aucune banque réelle produite.

## Gardes et tests, cas sains et artefacts

| garde ou test | cas sain (essai) | artefact (essai) |
|---|---|---|
| T1 forme | 7 énoncés conformes, réanalysés à la même forme normale (`test_t1_sain_et_aller_retour`) ; confiance décimale lue exactement | 13 hors grammaire (caractère non ASCII, variable libre, NAT hors du préfixe de tête, existentiel non borné déguisé, fonction inconnue, arité, nom réservé, variable déjà liée, comparaisons enchaînées, pas de comparaison, vide, virgule manquante), 9 hors schéma (clé en trop, champ vide, flottant, booléen, confiance hors [0, 1], énoncé non textuel, NaN, non-JSON, liste) ; vocabulaire d'un autre monde ; profondeur excessive. Tous « informe », aucun ne tue |
| T2 contre-exemple | vérité non tuée ; borne : vrai jusqu'à N non tué à N | faux tué avec instance ≤ N (issue typée) ; tué en N + 1 à la borne 3N ; contradiction avec les définitions ; indéfini en n = 0 tué ; hors capacité « non décidée », jamais une mort |
| T3 vacuité | hypothèses satisfiables ; « sans objet » sans hypothèse | hypothèses insatisfiables jusqu'à N (aussi par la batterie) ; domaine d'intervalle vide ; hypothèses en chaîne contradictoires |
| T4 trivialité | deux vérités non triviales | instance littérale d'une définition ; définition renommée et réordonnée ; initiale retournée ; identité close ; quatre instances d'axiomes par substitution (F1, F2) |
| T5 redite | deux puis trois vérités distinctes non redites | renommage ; permutation du préfixe et des membres ; double négation et contraposée ; réordonnancement de conjonctions à quantificateurs ; équivalence propositionnelle (distributivité) ; même profil de vérité (« ≤ 50 » contre « < 51 ») |
| T6 vérification (garde G-C) | vrai contre-exemple accepté ; contre-exemple dans ]N .. 3N] accepté ; intervalle dépendant accepté | faux contre-exemple refusé (« réfutation fausse », ne tue pas) ; hors domaine refusé (n = −1, n = 3N + 1, n = 10⁹, partie hors de PARTIES, s hors de [0 .. t]) ; six instances informes (variable manquante ou en trop, texte, flottant, booléen, liste) ; verdict « vrai » sans réfutation ; sortie de S hors schéma |
| Lignée (D-M5) | registre rejouable, dernière empreinte identique au rechargement | reformulation d'une morte héritée morte ; mort par T6 héritée par une reformulation ; résurrection refusée ; ligne supprimée, modifiée ou réordonnée : chaîne refusée |
| Plantation | banque de 12 mondes, 312 plantés, 8/4/4/5/5 par monde ; pièges certifiés dans ]N .. 3N], faux tôt ≤ N ; seuil de piège réalisable et certifié | fausse vérité refusée ; vérité triviale refusée comme vérité ; piège tué sous N refusé ; piège sans contre-exemple dans ]N .. 3N] refusé (vrai au-delà, ou faux seulement après 3N) ; gabarit non réalisable : arrêt ; doublon de vérité refusé par T5 ; doublon de faux tôt : arrêt ; seuil sur une constante ou une expression indéfinie : aucun candidat |
| Clés | définition servie et clé distinctes, scellées, sans aucun octet de clé dans les 12 définitions servies ; clé intacte chargée | énoncé planté glissé dans la définition servie : arrêt (fuite) ; clé altérée d'un octet : refusée au chargement |
| P8 et A1 | rejeu conforme : faux tôt 48/48 tués, vérités 0/96, pièges 0/48 tués sous N, témoins conformes, 96/96 instances de clé vérifiées par T6, code 0 | fausse vérité injectée dans une clé : A1 ; faux tôt rendu vivant : A1 ; piège remplacé par un faux tôt : A1 ; rejeu en ligne de commande avec une clé altérée en mémoire : code 3 ; dossier de sortie non vide : refusé, code 1 |
| Flottant dans un chemin de vérité | valeurs exactes acceptées | littéral flottant, variable flottante, booléen, paramètre de monde flottant, constante flottante : refusés (`GardeArret`) |
| Calcul exact | variation totale par types égale à l'énumération brute (t ≤ 3) ; queue binomiale exacte ; programmation linéaire exacte égale à Fréchet et à une grille exacte | recoupement de Fréchet faussé : arrêt à la construction du monde |
| Normaliseur | dépliage de la récurrence et de la suite affine : clos à vrai et vrai jusqu'à 3N ; même issue de T2 avant et après normalisation sur 72 énoncés de la base aléatoire | dépliage refusé sur une variable d'intervalle qui descend sous zéro |
| Graines (R9) | enfants égaux à `SeedSequence(racine).spawn(10)` ; tirages reproductibles | chemin hors de l'arbre, chemin vide, racine négative, booléenne ou flottante : refusés |
| Déterminisme | deux rejeux de même racine : mêmes empreintes de tous les fichiers (manifeste à part, il porte l'heure) et même table d'empreintes au manifeste | racines différentes : banques différentes |
| Sous-banque S/N | 150 énoncés, 75/38/37, 6 ou 7 vrais et 3 ou 4 faux tôt par monde, identifiants uniques, ni étiquette ni gabarit servis, reproductible | quota impossible : arrêt |
| Base « grammaire aléatoire » | 24 énoncés par monde, tous conformes à T1, reproductibles | — (un énoncé tiré non réanalysable lèverait `GardeArret`) |

## Rejeu sans appel sur deux racines d'essai

`python -m controle_ia.oracles_plantes_v1.rejeu --racine R --sortie <dossier du bloc-notes>`, environ 10 secondes chacun :

| racine | mondes | plantés | faux tôt tués | vérités tuées | pièges tués sous N | témoins triviaux tués | témoins grossiers tués | instances de clé vérifiées (T6) | redites parmi les analysables | A1 | code |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 12 | 312 | 48/48 | 0/96 | 0/48 | 0/60 | 60/60 | 96/96 | 0 | tenue | 0 |
| 20261122 | 12 | 312 | 48/48 | 0/96 | 0/48 | 0/60 | 60/60 | 96/96 | 0 | tenue | 0 |

Base « grammaire aléatoire » (288 énoncés) : racine 11 : 0 informe, 198 morts, 90 vivants dont 18 vrais-bornés non triviaux ; racine 20261122 : 0, 193, 95, 21. Les 20 redites relevées parmi les témoins triviaux sont attendues (tous les témoins clos à « vrai » ont la même forme normale).

## Balayage de robustesse de la plantation (hors essais)

Construction de la banque et rejeu de la batterie sur 42 racines d'essai (0 à 39, 11, 20261122), code final : **0 arrêt, 0 écart** (A1 tenue partout, aucune redite parmi les analysables plantés) ; un candidat de repli (rang > 0, inscrit à la clé) a servi dans 17 racines (gabarits : période modulaire et sa période unité, signe de Cassini, croissance sans QU, rang d'apparition, et seuils de F1 et F2 dont le premier tirage de n₀ était redit ou non réalisable). Deux versions antérieures du code avaient des refus : seuils placés au même n₀ (redites par profil), et période modulaire à un seul module ; toutes deux corrigées (note de choix, lignes 29 et 34).

## Réserves

- Les essais portent sur des paramètres provisoires et des racines d'essai ; ils ne valent pas étalonnage de la banque réelle.
- L'étage « profil de vérité » de T5 peut déclarer redites deux affirmations distinctes dont les statuts coïncident sur le domaine fini (note de choix, ligne 29) ; la plantation refuse un tel candidat, un proposeur en serait pénalisé.
- La forme de la sortie du bras S (T6) et la forme de « ce qui le tuerait » ne sont fixées nulle part : choix provisoires (note de choix, lignes 15 et 31).
