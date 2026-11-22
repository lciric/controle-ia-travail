# Rapport des essais R5 — lot B1 du pilote « oracles plantés » — v2

- Nature : rapport de travail (classe C), version 2, pour le paquet `oracles_plantes_v2` (corrections de la contre-lecture `contre-lecture-code-lot-b1-v1.md`, `305bb4a3…` ; réponse : `reponse-contre-lecture-lot-b1-v1.md`). Le rapport v1 (`4ea57f3c…`) reste tel quel pour la v1. Par l'exécutant du mandat `mandat-code-lot-b1-v1.md` (`407ef6f1…`), Opus 5.5, le 2026-11-22. Processeur seul, 0 USD, aucun appel de modèle, aucune machine louée.
- Commande : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_oracles_plantes_v2_*.py` (seulement ces fichiers ; la suite complète du dépôt n'a pas été lancée). Python 3.13.18, numpy 2.4.6.
- **Résultat : 147 essais passés, 0 échoué** (grammaire 34, évaluation 20, tests de mort et lignée 45, banque et rejeu 23, contre-lecture 25), en 56 secondes environ.
- Essais de la contre-lecture rejoués sur la v1 (`OP_PAQUET=oracles_plantes_v1 … tests/test_oracles_plantes_v2_contre_lecture.py`) : **19 échoués, 6 passés** (les 5 cas sains, et l'essai de la remarque 8, qui portait sur l'essai et non sur le code). Les 122 essais repris de la v1 passent tous sur la v2.
- Paramètres : tous provisoires (`parametres_provisoires_v2.json`) ; racines d'essai seulement (20261122 dans les essais) ; aucune banque réelle produite.

## Gardes et tests, cas sains et artefacts

| garde ou test | cas sain (essai) | artefact (essai) |
|---|---|---|
| T1 forme | (v2) parenthèse de tête conforme ; 7 énoncés conformes, réanalysés à la même forme normale (`test_t1_sain_et_aller_retour`) ; confiance décimale lue exactement | 13 hors grammaire (caractère non ASCII, variable libre, NAT hors du préfixe de tête, existentiel non borné déguisé, fonction inconnue, arité, nom réservé, variable déjà liée, comparaisons enchaînées, pas de comparaison, vide, virgule manquante), 9 hors schéma (clé en trop, champ vide, flottant, booléen, confiance hors [0, 1], énoncé non textuel, NaN, non-JSON, liste) ; vocabulaire d'un autre monde ; profondeur excessive ; (v2) NAT entre parenthèses, membre d'un « et », d'un « ou », d'une implication : « informe » sans arrêt de la batterie. Tous « informe », aucun ne tue |
| T2 contre-exemple | vérité non tuée ; borne : vrai jusqu'à N non tué à N | faux tué avec instance ≤ N (issue typée) ; tué en N + 1 à la borne 3N ; (v2) contradiction avec les définitions atteinte et typée (`u(1000) - u(1000) = 1`, remarque 8 ; l'essai repris de la v1 meurt, lui, par contre-exemple) ; indéfini en n = 0 tué ; hors capacité « non décidée », jamais une mort |
| T3 vacuité | hypothèses satisfiables ; « sans objet » sans hypothèse | hypothèses insatisfiables jusqu'à N (aussi par la batterie) ; domaine d'intervalle vide ; hypothèses en chaîne contradictoires |
| T4 trivialité | deux vérités non triviales | instance littérale d'une définition ; définition renommée et réordonnée ; initiale retournée ; identité close ; quatre instances d'axiomes par substitution (F1, F2) |
| T5 redite | deux puis trois vérités distinctes non redites | renommage ; permutation du préfixe et des membres ; double négation et contraposée ; réordonnancement de conjonctions à quantificateurs ; équivalence propositionnelle (distributivité) ; même profil de vérité (« ≤ 50 » contre « < 51 ») ; (v2) deux vérités distinctes dont le profil ne diffère que par des « hors capacité » : non redites |
| T6 vérification (garde G-C) | (v2) réfutation fausse : rien d'inscrit au registre ; vrai contre-exemple accepté ; contre-exemple dans ]N .. 3N] accepté ; intervalle dépendant accepté | faux contre-exemple refusé (« réfutation fausse », ne tue pas) ; hors domaine refusé (n = −1, n = 3N + 1, n = 10⁹, partie hors de PARTIES, s hors de [0 .. t]) ; six instances informes (variable manquante ou en trop, texte, flottant, booléen, liste) ; verdict « vrai » sans réfutation ; sortie de S hors schéma ; (v2) contre-exemple vérifié : mort inscrite d'office (`appliquer_t6`) et héritée |
| Lignée (D-M5) | registre rejouable, dernière empreinte identique au rechargement ; (v2) Cassini vivante après la mort de sa variante indéfinie ; « u(n) > 0 » vivante après la mort de « u(n) + 0 · w(n − 1) > 0 » ; triviale close à vrai vivante après la mort de « w(n − 1) · 0 = 0 » ; vérité non héritée d'un piège mort | reformulation d'une morte héritée morte ; mort par T6 héritée par une reformulation ; résurrection refusée ; ligne supprimée, modifiée ou réordonnée : chaîne refusée ; (v2) troncature et dernière ligne modifiée : refusées ; reformulation entière d'un piège tué par T6 (« u(k) <= c − 1 ») : morte par héritage |
| Plantation | banque de 12 mondes, 312 plantés, 8/4/4/5/5 par monde ; pièges certifiés dans ]N .. 3N], faux tôt ≤ N ; seuil de piège réalisable et certifié | fausse vérité refusée ; vérité triviale refusée comme vérité ; piège tué sous N refusé ; piège sans contre-exemple dans ]N .. 3N] refusé (vrai au-delà, ou faux seulement après 3N) ; gabarit non réalisable : arrêt ; doublon de vérité refusé par T5 ; doublon de faux tôt : arrêt ; seuil sur une constante ou une expression indéfinie : aucun candidat |
| Clés | définition servie et clé distinctes, scellées, sans aucun octet de clé dans les 12 définitions servies ; clé intacte chargée | énoncé planté glissé dans la définition servie : arrêt (fuite) ; (v2) instance glissée, indentée, dans un objet servi : arrêt ; clé altérée d'un octet : refusée au chargement |
| P8 et A1 | rejeu conforme : faux tôt 48/48 tués, vérités 0/96, pièges 0/48 tués sous N, témoins conformes, 96/96 instances de clé vérifiées par T6, code 0 | fausse vérité injectée dans une clé : A1 ; faux tôt rendu vivant : A1 ; piège remplacé par un faux tôt : A1 ; (v2) témoin trivial à la place d'une vérité : A1 ; piège non décidé sous N, à instance de clé vérifiée : A1 ; rejeu en ligne de commande avec une clé altérée en mémoire : code 3 ; dossier de sortie non vide : refusé, code 1 |
| Flottant dans un chemin de vérité | valeurs exactes acceptées ; (v2) fichier de paramètres sans décimal accepté | littéral flottant, variable flottante, booléen, paramètre de monde flottant, constante flottante : refusés (`GardeArret`) ; (v2) marges flottantes et AV flottant refusés à la construction, décimal JSON refusé à la lecture des paramètres |
| Calcul exact | variation totale par types égale à l'énumération brute (t ≤ 3) ; queue binomiale exacte ; programmation linéaire exacte égale à Fréchet et à une grille exacte | recoupement de Fréchet faussé : arrêt à la construction du monde |
| Normaliseur | dépliage de la récurrence et de la suite affine : clos à vrai et vrai jusqu'à 3N ; même issue de T2 avant et après normalisation sur 72 énoncés de la base aléatoire | dépliage refusé sur une variable d'intervalle qui descend sous zéro |
| Graines (R9) | enfants égaux à `SeedSequence(racine).spawn(10)` ; tirages reproductibles | chemin hors de l'arbre, chemin vide, racine négative, booléenne ou flottante : refusés |
| Déterminisme | deux rejeux de même racine : mêmes empreintes de tous les fichiers (manifeste à part, il porte l'heure) et même table d'empreintes au manifeste | racines différentes : banques différentes |
| Sous-banque S/N | 150 énoncés, 75/38/37, 6 ou 7 vrais et 3 ou 4 faux tôt par monde, identifiants uniques, ni étiquette ni gabarit servis, reproductible | quota impossible : arrêt |
| Base « grammaire aléatoire » | 24 énoncés par monde, tous conformes à T1, reproductibles | — (un énoncé tiré non réanalysable lèverait `GardeArret`) |

## Rejeu sans appel sur deux racines d'essai

`python -m controle_ia.oracles_plantes_v2.rejeu --racine R --sortie <dossier du bloc-notes>`, environ 10 secondes chacun :

| racine | mondes | plantés | faux tôt tués | vérités tuées | pièges tués sous N | témoins triviaux tués | témoins grossiers tués | instances de clé vérifiées (T6) | redites parmi les analysables | A1 | code |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 12 | 312 | 48/48 | 0/96 | 0/48 | 0/60 | 60/60 | 96/96 | 0 | tenue | 0 |
| 20261122 | 12 | 312 | 48/48 | 0/96 | 0/48 | 0/60 | 60/60 | 96/96 | 0 | tenue | 0 |

Base « grammaire aléatoire » (288 énoncés) : racine 11 : 0 informe, 198 morts, 90 vivants dont 18 vrais-bornés non triviaux ; racine 20261122 : 0, 193, 95, 21. Les 20 redites relevées parmi les témoins triviaux sont attendues : tous les témoins clos à « vrai » sont équivalents (en v2 leurs empreintes diffèrent par leurs sous-termes partiels, l'étage 2 de T5 les rapproche). Comptes identiques à ceux de la v1.

## Balayage de robustesse de la plantation (hors essais)

Construction de la banque et rejeu de la batterie sur 42 racines d'essai (0 à 39, 11, 20261122), code v2 : **0 arrêt, 0 écart** (A1 tenue partout, y compris ses deux contrôles neufs ; aucune redite parmi les analysables plantés) ; un candidat de repli (rang > 0, inscrit à la clé) a servi dans 17 racines, les mêmes qu'avec le code final de la v1.

## Réserves

- Les essais portent sur des paramètres provisoires et des racines d'essai ; ils ne valent pas étalonnage de la banque réelle.
- L'étage « profil de vérité » de T5 peut déclarer redites deux affirmations distinctes dont les statuts coïncident sur le domaine fini (note de choix v2, ligne 29) ; la plantation refuse un tel candidat, un proposeur en serait pénalisé. Le même étage sert à l'héritage par équivalence (ligne 32) et lit la vérité jusqu'à 3N.
- Pièges reconnaissables à leur forme (remarque 7) et écarts au préenregistrement (enfant [9], borne du profil ; remarque 12) : renvoyés au concepteur (note de choix v2, lignes 46 et 47).
- La tête de chaîne du registre protège de l'accident, pas d'une réécriture des deux fichiers.
- La forme de la sortie du bras S (T6) et la forme de « ce qui le tuerait » ne sont fixées nulle part : choix provisoires (note de choix v2, lignes 15 et 31).
