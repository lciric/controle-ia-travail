# Relecture du différentiel entre la commande v4 et la commande v5 de la tranche B-α de « Neuron Lens », code compris — v1

**Verdict : feu possible.** Aucun point bloquant. Deux remarques à porter par consigne du feu (points 9 et 12), le reste conforme.

Lecteur neuf (ni auteur du code, ni des commandes, ni des relectures), le 2026-11-15 vers 12:05 UTC. Objet : copie détachée de la
branche `prep/neuron-lens-v1` au commit `6d336a6a` ; décisions lues : R-2887, R-2892, R-2900, R-2901. Rien n'a été loué ; aucun appel
au loueur ; aucune valeur de clé lue ni écrite ; aucun code du dépôt voisin exécuté ; aucun commit, aucune poussée.

## A. Pièces et empreintes (compagnons recalculés : 23 sur 23 conformes)
Commande v5 `423b74b4…` ; commande v4 `f54d5ec3…` ; journal de la relance `48f55ea8…` ; estimation de mémoire `423d7955…` ; lanceur v3
`44bba9c0…` ; ses essais `0b1fb66f…` ; amorce v5 `085c9d07…` ; dépôt réduit v6 `97c41abf…` ; `essai_environnement_b0_v2.py`
`1e7ed65b…` ; essai à blanc v8 `723674fa…` ; son journal `ece58ca4…` ; texte gelé v6 `34b88243…` ; devis v2 `61c394f5…` ; garde v4
`6a98d816…` ; suivi v6 `2ecaaeed…` ; minuterie v4 `45113683…` ; exigences `ef184e58…` ; et les pièces précédentes (lanceur v2
`a9f0324c…`, amorce v4 `290309c6…`, dépôt réduit v5 `4d26589d…`, essais à blanc v6 et v7, `essai_environnement_b0_v1.py`). Les
empreintes transmises par la mère sont toutes exactes.

## B. Différentiels exacts (point 1 de la demande)
1. **Lanceur v2 → v3** : en-tête ; constante `CTX_BATCH = 16` (l. 65) ; son propre nom dans la liste des modules (l. 73) ; l'appel de
   `_measure` reçoit `--ctx-batch 16` (l. 673-674). Rien d'autre : étapes, ordre, échéances, pires cas, environnement des enfants,
   partie 2, audits : identiques. Conforme au déclaré.
2. **Essais v2 → v3** : en-tête, module importé, un essai neuf à deux graines (l. 501-526) : 50 + 2 = 52. Conforme.
3. **Amorce v4 → v5** : commentaire d'en-tête, nom du lanceur (l. 14 et l. 86), fichier d'essais du lanceur (l. 55). Rien d'autre
   (balayage des deux secrets, codes d'arrêt, poussées, état final : identiques). Conforme.
4. **Dépôt réduit v5 → v6** : en-tête, usage, et les trois noms de fichiers (lanceur v3, essais v3, amorce v5 ; l. 34, 38, 52).
   Conforme. Liste reconstruite par moi : `0293f4e1…`, 347 fichiers, sur le commit `09425238` (commit réduit `b09e29cd…`, paquet
   `7640465d…`, identiques au journal versé) **et** sur le commit de tête `6d336a6a` (même liste ; commit réduit `d588d8c6…`).
5. **Essai à blanc v6 → v8** (v7 lue aussi) : en-tête ; dépôt réduit v6 par défaut (l. 30) ; fichier d'essais v3 (l. 76) ; titre
   (l. 109) ; contrôle d'environnement v2 avec le lanceur v2 comme artefact (l. 194, 199) ; compte des appels de `measure` ancré sur
   la ligne entière (l. 200 ; le défaut de la v7, qui comptait aussi les lignes d'artefact, est bien fermé). `essai_environnement_b0`
   v1 → v2 : fonction `controler_measure` (l. 72-97), défauts des arguments, deux appels (l. 151 et 169). Conforme.
6. **Commande v4 → v5** : en-tête du différentiel (l. 1-18) ; pièces v3, v5, v6 ; branches `course/neuron-lens-b-alpha-reduit-v6` et
   `calcul/neuron-lens-b-alpha-v3` ; fichiers de suivi en `-b-alpha-v3` ; mention du lot à l'étape 12 (l. 155) ; « 143 » essais
   (l. 151) ; préambule (l. 56) et étape 10 (l. 130) en préavis sans attente (point 9 de la lecture R-2892) ; fondement de l'étape 15
   (l. 192) ; section de l'essai à blanc (l. 199-208) ; dépense déjà faite (l. 236-237) ; table des empreintes. Tout est déclaré,
   **sauf un point de forme** : la table des empreintes perd onze lignes de pièces inchangées (les modules `grandeurs`, `addendum
   partie 2`, `balayage`, `verdicts`, `controles_b0`, les trois fichiers de correctifs, la vérification courte, le journal de la
   première course, la relecture du différentiel de la v2). Sans effet : le code reste tenu par la liste `0293f4e1…` du dépôt réduit
   et les documents par la v4 citée avec son empreinte. À dire à la prochaine version.

## C. Le lot de `measure` (point 2 de la demande)
7. **Passé à chaque appel de `measure`, et à rien d'autre.** `_measure` (l. 672-675 du lanceur v3) est le seul endroit qui lance
   `measure` ; il a deux appelants : l'étape `measure` (graine 0, l. 701) et l'audit « trop beau » (graine 1, l. 780). `score` (l. 685
   et l. 833, audit « tout négatif ») ne reçoit pas le lot ; `CTX_BATCH` n'apparaît qu'aux l. 65 et 673. Aucun autre paramètre de
   mesure n'est passé (`--per-layer`, `--contexts`, `--ctx-len`, `--top-contexts`, `--cond-batch` absents ; vérifié par l'essai neuf
   et par le contrôle par programme de l'essai à blanc, lanceur v2 pris en défaut aux deux graines).
8. **Le lot n'est pas un défaut publié fixé.** Texte gelé v6, l. 182-184 : « `checks/causal_lens.py measure` avec ses défauts publiés
   (lignes 374 à 377 de la copie) : 32 neurones par couche, deux pôles, 16 contextes de 64 jetons […] 8 premiers documents du pôle,
   fenêtre de 8 ». Copie empreintée du code voisin (`befb7018…`, identique au fichier de la copie de lecture du voisin, arbre
   `b22006e9…`) : l. 374 à 377 = `--per-layer`, `--contexts`, `--ctx-len`, `--top-contexts` ; `--cond-batch` est l. 378 et
   `--ctx-batch` l. 379. La lecture de R-2901 tient à la lettre.
   **Le lot ne change que le nombre de lignes par passe.** Code lu sans l'exécuter (l. 216-247) : les tâches sont découpées par
   tranches du lot (l. 216), dans le même ordre ; chaque tâche occupe deux lignes, propre et ablatée, côte à côte dans la même passe
   (l. 221-224), et la différence se prend entre ces deux lignes ; le complément est à droite sous masque d'attention, dans un modèle
   causal : une ligne ne dépend d'aucune autre ; les sommes par pôle s'accumulent dans le même ordre (l. 241-243). Seules changent la
   forme du lot et la longueur de complément de chaque passe : effet au bruit numérique du bf16 près, comme déclaré. Le fichier de
   résultats ne consigne pas le lot (`meta`, l. 127) ; la trace est la ligne de commande en tête du journal de `measure`, qui est
   poussé : suffisant.
9. **Remarque (consigne proposée)** : la lecture « écart de lot, non écart au texte gelé » est celle de la mère (R-2901) ; je la
   confirme à la lettre. Elle doit rester visible à la lecture des résultats : que l'écart de lot soit reporté dans l'addendum ou le
   rapport de la course, avec la ligne de commande journalisée, pour les deux graines.

## D. Estimation de mémoire (point 3 de la demande)
10. **Calcul refait.** Journal de l'échec (`diag/20261115-102017-neuron-lens-b-alpha/journaux/measure.log`, l. 84) : 896 Mio demandés,
    21,07 Gio alloués, 1,93 Gio réservés non alloués, 100,75 Mio libres sur 23,57 Gio ; pilotage des 32 couches fait (l. 35, 519 s) ;
    aucune ligne d'ablation : échec à la première passe de la première couche. 896 Mio = 128 lignes × 256 jetons × 14 336 × 2 octets :
    exact (documents coupés à 256 jetons, `06_activations.py` l. 88 de la copie de lecture). Poids en bf16 : 8,03 milliards de
    paramètres × 2 octets = 14,96 Gio : exact. Hors de la bibliothèque : 0,46 Gio : exact.
    **Deux biais de la note, de même sens (optimiste)** : (a) elle prend les 21,07 Gio alloués *au moment de l'échec* pour la pointe
    à 64 ; or les 896 Mio refusés s'y ajoutaient (pointe ≥ 21,95 Gio, et sans doute plus : l'appel, l. 235, ne désactive pas le cache
    des clés et valeurs, qui croît de couche en couche — 0,125 Gio par couche à 32 768 jetons, 4 Gio en fin de passe) ; (b) elle met
    à l'échelle une part qui ne dépend pas du lot : le reste du pilotage encore tenu pendant l'ablation (dernier bloc de
    probabilités, 768 × 128 256 en 32 bits, et derniers états : ≈ 0,5 Gio).
    **Mon recalcul**, par deux voies : règle calée corrigée (pointe à 64 ≥ 14,96 + 0,5 + 6,5) : à 16, part variable ≈ 2,1 Gio,
    alloué ≈ **17,1 Gio** ; décompte par jeton (cache 131 072 octets, trois tenseurs de la couche à portes 86 016, états ≈ 32 768,
    attention ≤ 16 384, soit ≈ 0,25 Mio par jeton) : 8 192 jetons → 2,0 Gio, plus 0,5 de reste : alloué ≈ **17,5 Gio**. Ce décompte
    retrouve les deux faits observés : pilotage à 17 408 jetons ≈ 19,6 Gio (passé), ablation à 64 ≈ 23,6 Gio (au-dessus des
    23,11 Gio utilisables : échec).
    **Marge recalculée : ≈ 3,7 à 4,1 Gio en lecture prudente** (les 1,93 Gio réservés tenus pour perdus), **≈ 5,6 à 6,0 Gio** s'ils
    sont rendus. La note annonce ≈ 16,5 Gio alloués et ≈ 4,7 Gio de marge : optimiste d'environ 0,6 à 1,0 Gio, **conclusion
    inchangée**.
11. **Argument indépendant du calage, le plus solide** : la passe de pilotage (272 lignes × 64 jetons = 17 408 jetons, l. 184) est
    passée en vrai sur cette carte, avec le même reste ; la passe d'ablation à 16 porte au plus 32 lignes × 256 jetons = 8 192
    jetons, moins de la moitié. Les seuls termes propres à l'ablation sont la copie du crochet (l. 230, 0,22 Gio, qui ne s'ajoute pas
    à la pointe des trois tenseurs) et l'attention sur 256 positions (≤ 0,25 Gio si elle est matérialisée). L'ablation à 16 demande
    donc moins que ce qui est déjà passé. **Autres parties** : `measure` n'a que deux lots sur la carte (`--cond-batch`, pilotage,
    passé ; `--ctx-batch`, ablation) ; l'audit « trop beau » est le même appel dans un processus neuf, mêmes pointes ; `score`, les
    grandeurs par pôle et l'audit « tout négatif » tournent sur le processeur (mémoire vive ≈ 10 Go contre 64) ; la fumée et la passe
    sont passées en vrai. **Rien d'autre ne peut saturer la carte.** Durée : le nombre total de jetons de l'ablation ne change pas
    (quatre fois plus de passes, quatre fois plus petites) ; ordre de grandeur 10 à 20 minutes, sous l'attendu d'une heure et sous
    l'échéance de 5 h (l. 675) ; la note ne le dit pas (mineur).

## E. Essais rejoués (point 4 de la demande)
Montage, déclaré : la copie détachée n'a pas été touchée ; clone partagé et partiel (`scripts`, `src`, `tests`, notes et sources de
« Neuron Lens », `prereg`) dans le dossier de travail de la session, au commit `6d336a6a` ; interpréteur de travail du lecteur
précédent (paquets du programme plus `pyarrow` 26.0.1) ; copie de lecture du dépôt voisin (déjà présente dans le dossier de travail,
arbre `b22006e9…` vérifié) reliée le temps des essais au chemin par défaut `/home/user/stdlogits/neuron-lens`, lien et dossier
retirés ensuite (vérifié). Incident dit : un premier clone complet a rempli le disque de la session ; je l'ai retiré (c'était le
mien) et remplacé par le clone partiel ; rien d'autre n'a été effacé.
- **52 essais du lanceur v3** : avec l'environnement du programme tel quel, **50 passés, 1 en échec, 1 sauté** (l'échec est
  `test_partie2_bout_en_bout`, « version absente : pyarrow », paquet épinglé pour la machine et absent de la session ; le sauté est
  l'essai sur copie réelle, copie de lecture absente du chemin par défaut) — même tableau que pour le lecteur de la v4. Avec
  l'interpréteur de travail et la copie reliée : **52 passés, 0 échec, 0 sauté**.
- **Essai à blanc v8**, commit source `09425238` : **conforme, 0 écart, code 0**, en 3 min 7 s. Nominal : 13 appels du lanceur,
  **143 essais réels passés, 1 désélectionné**, 13 résultats poussés, état final ; relance sans appel ; reprise (`passe b3 measure
  score grandeurs verdicts`, essais non refaits) ; échec 20 ; 14 formes refusées sur 14, 0 dans le dépôt distant ; gardes 10, 10, 17,
  13, 16, 14, 12, 12 ; environnement de B0 conforme ; **appels de `measure` : 2 sur 2 avec `--ctx-batch 16`** (graine 0, et
  `--seed 1`), lanceur v2 pris en défaut (2 écarts) ; témoins 14 sur 14 ; 0 processus restant. Sortie comparée ligne à ligne au
  journal versé : identique, hors durées, numéro du groupe tué et nombre d'objets lus au balayage (610 contre 605, sans portée).

## F. Argent, clés, destruction, absence, préavis, branches (point 5 de la demande)
12. **Argent : rien de dégradé, marge au plafond réduite, à dire.** Prix lu ≤ 0,73 dollar l'heure (l. 70, étape 8), minuterie et garde
    v4 inchangées, plafond 12, arrêt dur à 10,80. La garde et la minuterie comptent la seule instance neuve (frais fixes à zéro,
    l. 113 et 126, comme en v4) ; avec ≈ 0,85 déjà dépensé sur la ligne (l. 236-237) et ≈ 0,1 de trafic, le pire cas à l'arrêt dur
    fait ≈ 11,75 dollars : sous le plafond de 12, mais avec ≈ 0,25 de marge (≈ 1,1 à la v4). Consigne proposée : la mère le sait
    et le dit au feu ; je ne recommande pas de changer les arguments (des frais fixes de 0,85 raccourciraient la minuterie à 13,6 h,
    sous le pire cas complet de 14,7 h).
13. **Clés** : par leur nom seulement, partout ; balayage des deux secrets inchangé dans l'amorce ; contrôle par programme que les
    appels de `measure` n'en portent aucune et sont hors ligne. Aucune valeur dans les pièces neuves ni dans les journaux versés.
14. **Destruction et absence** : étape 15 inchangée hors son fondement (l. 192-194) : destruction manuelle avec sa confirmation
    automatique `-y` et l'entrée fermée, preuve d'absence avec témoin par le suivi v6, automates arrêtés par leur identifiant de
    processus. Table de destruction (étape 13) inchangée. Un nouvel échec de l'ablation par mémoire tombe dans la ligne « arrêt code
    2x » : destruction immédiate après l'étape 14, rapport, aucune relance sans mot de la mère (l. 11-12) : cohérent.
15. **Préavis sans attente** : étapes 7, 10 et 15 et préambule alignés (l. 56, 87, 107, 130, 192) ; plus aucune mention d'un signal à
    attendre ; les refus d'une permission, du crochet ou du classifieur restent « ni rejoués, ni reformulés, ni contournés » (l. 87-88).
    La création n'est citée ici que par son étape (étape 7), inchangée hors les noms de branche et d'amorce.
16. **Branches neuves absentes à distance** (lecture seule du dépôt de travail, 12:00 UTC) : `course/neuron-lens-b-alpha-reduit-v6` et
    `calcul/neuron-lens-b-alpha-v3` absentes ; témoins présents (`…-reduit-v4`, `…-reduit-v5`, `calcul/…-v1`, `calcul/…-v2`) ;
    `prep/neuron-lens-v1` à `6d336a6a`. La branche réduite sera créée à l'étape 5 ; l'étape 5 exige la branche des résultats vide.

## G. Mineurs
17. Le défaut de branche codé dans l'amorce (`calcul/neuron-lens-b-alpha-v1`, l. 47) reste ; sans effet, la commande passe
    `BRANCHE_RESULTATS` (déclaré, l. 16-17).
18. La note de mémoire écrit « aucune autre partie n'a de lot sur la carte » : exact pour `measure` et les audits ; la passe
    d'activations en a un (`--batch-docs 32`), déjà passé en vrai, ce que la note dit plus haut.
19. Réserve de la note (linéarité, même schéma de réservation) : tenue pour juste ; l'estimation n'est pas une mesure. Le premier
    journal d'ablation (« ablate L0 ») dira en moins d'une minute si la passe tient.

## H. Ce que je n'ai pas fait
Aucune mesure de mémoire (pas de carte) ; aucun code du dépôt voisin exécuté (les correctifs sont appliqués par `preparer`, les
essais de B0 remplacés par un enregistreur) ; pas de vrai clone par le réseau, pas de vraie installation ; `donnees/` et
`docs/verdicts/` non ouverts ; aucun résultat de mesure lu.
