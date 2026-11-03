# Contre-lecture de la fiche de lancement de la course Ibrahim Q1 (brouillon 1) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 11:55 UTC (`date -u`).
Aucun appel payant, aucun réseau, aucune clé, aucun fichier existant modifié. Seul fichier écrit : ce rapport (non scellé, non
commité). J'ai aussi extrait par `git show`, dans le bloc-notes, les huit sources de conv-audit, pour les comparer.

Objet : `docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/fiche-lancement-course-ibrahim-q1-v1-brouillon1.md`,
sha256 `985f22e70012d342aefea40c296cfccbfa87b0d7578b03beee4ac6df39f441e1` (compagnon `.sha256` vérifié : OK). Arbre
`wt-ibrahim`, branche `outils/course-ibrahim-q1-v1`, commit `a4b02faa`. Sauf mention, les numéros de ligne renvoient à la fiche.

## Verdict

**Scellable après corrections.** Aucun constat bloquant. Deux constats majeurs : CLI-01 (marge d'appels) et CLI-02 (source
Gu-Krenn). Chacun se corrige dans le kit à coût nul en dépense, ou par une déclaration dans la fiche. Quatre constats
mineurs.

Les défauts relevés sur Kirchner ne reviennent pas :
- la liste d'arrêt contient C13, l'arrêt sans fiche et les codes du lanceur ;
- le mot de Lazar est direct et cité à la lettre (conforme à R-1135) ;
- le numéro de GO est décrit et n'est plus un remplissage ;
- les chiffres de la § 7 portent leurs empreintes, vérifiées ;
- l'exclusivité d'Argon dit comment elle se vérifie.

Exception : la règle de la source Gu-Krenn est mieux écrite, mais deux codages s'en écartent encore (CLI-02). Si une pièce du
kit change, il faut un nom neuf (R12), de nouvelles empreintes dans les trois configurations, une nouvelle table et une
nouvelle répétition.

## Vérifié conforme

- **Sources de conv-audit** (`origin/canal/conv-audit-n04`) : chacune est à l'empreinte de son compagnon et identique à
  l'octet (`cmp`) à la copie du kit. Ce sont la spécification `0874d561…`, la question `5e905798…`, les pièces `4e3851e3…`,
  `9e424a02…` et `d6fa8011…`, le protocole `fbbbb520…` et le n° 417 `fecc2d0b…`.
- **Mot de Lazar** : « go trois tours et course Ibrahim ; pas de plafond », direct, reçu entre 11:28:51 et 11:30 UTC
  (`registres/decisions.md`, R-1135). Il porte le GO et le « pas de plafond ».
- **Pièces gelées** :
  - Les 47 lignes de la table (l. 124-170) sont toutes OK par `sha256sum -c`.
  - `table_pieces_gelees_ibrahim_v1.py --verifier` donne « conforme : 47 pièces gelées, toutes à leur empreinte, aucune
    manquante ».
  - La table couvre les trois configurations, les cinq consignes, la question, les trois pièces, le protocole, les deux
    spécifications, le n° 417, la liste fermée, la source et les deux lanceurs.
  - Tous les compagnons du kit sont OK, et les empreintes de l'orchestrateur sont conformes sur disque.
  - Les deux empreintes citées en § 7 (mutations `d666c9c6…`, répétition `9221a60d…`) sont exactes.
- **Marqueurs** : le seul `<<…>>` est à la l. 10.
- **Consigne du proposeur** :
  - `construire_consigne_proposeur_ibrahim_v1.py --verifier` donne « conforme ».
  - Contrôle indépendant : on y trouve à l'octet, dans cet ordre, la section « La question… », la section « Règles
    d'intégrité », la pièce Ibrahim, la pièce sycophancie et nos résultats (positions 467 < 1 035 < 1 910 < 14 142 < 18 369).
  - « Ce qu'on attend de chaque espèce » et « Lecture prévue » sont absentes, comme le veut la spécification § 1.
  - Le livrable porte les trois demandes de la question : ce qu'on entraîne ou mesure, le résultat attendu chiffré et signé,
    la chose qui rendrait le résultat trompeur avec son contrôle.
  - Taille : 25 598 octets (24 825 caractères), loin des bornes de corps (4 Mo) et des fenêtres.
  - Les trois écarts sont déclarés (§ 8.1-8.2) : trois pièces sur le n° 417, ordre Ibrahim, puis sycophancie, puis nos
    résultats ; règles d'intégrité gardées.
- **Juge** :
  - La question et la phrase sur la direction visée sont reprises à l'octet.
  - K1 à K3 viennent de la question ; K4 et K5 viennent des deux critères du protocole qu'un juge sans moisson peut lire.
    L'écart est déclaré (§ 8.3). Aucun item ne pousse vers une réponse.
- **Aiguilleur** :
  - « concret » est restreint à la recette opérationnelle contre une évaluation réelle ; planter pour éprouver une mesure
    relève de `niveau_methode`.
  - « En cas de doute, concret » est gardé et déclaré.
  - Pour cette question (persona, sycophancie), le risque de débordement de Kimi est faible.
  - Lecteur et metteur sont conformes, avec les champs du kit.
- **Garde lexicale** : passée par `pole/fiches_v54.trouver` (« prefixe ») sur les cinq consignes, la liste, le vocabulaire
  du substitut, la question et les trois pièces : rien n'est trouvé.
  - Phrases essayées qui passent : « juge GPT-4o », « points de contrôle fusionnés », « Gemma-2-9B », « Mistral-7B »,
    « Tülu 3 ».
  - **Retirer « fusion » est juste.** « fusionnés » (pièce Ibrahim § 3) désigne les points de contrôle d'Open Character
    Training, c'est-à-dire le matériel même de la plupart des premières expériences. En mode préfixe, toutes les fiches qui
    les citent seraient exclues.
  - **Retirer « argon » est juste**, pour la même raison que pour Kirchner (nos résultats § 3).
  - Le prix est déclaré : une fusion qui se dirait « fusion » passerait, et la marque « exploratoire » reste attrapée.
  - « étude exploratoire » serait exclue, risque déjà accepté.
- **Dépense** :
  - S17 = 198 ≥ 1,2 × 164,46 = 197,35 (calcul), le plus petit entier au-dessus.
  - Plafonds de session, chacun au-dessus du pire cas d'un appel de son rôle : proposeur 3,5 > 3,2834 ; aiguilleur 0,4 > 0,3385 ;
    juge 0,9 > 0,8481 ; lecteur 0,9 > 0,8478 ; fusion 3,5 > 3,2862.
  - Relais à cinq espèces : Kimi 2 ≥ 0,81 ; Argon 3 ≥ 1,73 ; Astra 101,8 ≥ 84,83 ; Claude 91,2 ≥ 77,09.
  - Relais à quatre espèces : Claude 112,5 ≥ 68,95 ; Astra 83,5 ≥ 69,57. Sans Kimi : 132,8 ≥ 60,82 ; 65,2 ≥ 54,31.
  - La somme fait 198 dans chaque variante.
  - Étape « proposition » : 8,73 au plafond, contre 8,72 au devis et 8,67 avec la formule des commandes (caractères / 3).
  - Les étapes protégées reçoivent au lancement le plus grand de leur plafond de relais et du reste de S17
    (`pole/budget_v56.py`, en-tête, point 4). Des fiches en plus ne coupent donc pas le budget aux prix réels.

## Constats

### CLI-01 — majeur — la marge d'appels couvre au plus 13 fiches de trop au total, et le correctif n'a pas été rejoué sur le cas qui l'a motivé

- **Où** : l. 76-77 (§ 3.8), l. 115-116 (§ 7). Relais des configurations : Claude `max_appels` 203 pour 148 au plan ; Astra
  139 pour 100. Le calcul est dans `calcul_devis_course_ibrahim_v1.py` l. 192.
- **Le calcul** : une fiche de plus, si elle reçoit son passeport, coûte 4 appels Claude (aiguilleur, juge, deux lecteurs) et
  3 appels Astra (juge, deux lecteurs). Les fusions restent fixes (8). Le nombre de fiches en trop tolérées est donc :
  - Claude : (203 − 148) / 4 = 13,75 ;
  - Astra : (139 − 100) / 3 = 13 (calcul).
- **Ce que ça couvre** :
  - Si chaque proposeur rend 8 fiches au lieu de 6 (cinq espèces : 10 de trop), on arrive à Claude 188 et Astra 130 : ça passe.
  - Une seule espèce peut rendre jusqu'à 19 fiches seule.
  - Si chacun en rend 9 (15 de trop), Claude 208 > 203 et Astra 145 > 139 : relais en 429, puis trois échecs consécutifs ou
    C13, et l'arrêt tombe à l'étape des étiquettes, **sans aucune fiche**.
- **Rien d'autre ne borne** le nombre de fiches lues (`fiches_v53.fiches_du_texte` rend la liste entière). La répétition
  corrigée a été rejouée avec 6 fiches seulement (l. 116 ; `resultat-repetition-ibrahim-v1.txt`, essai 1). Le cas à 8 fiches,
  qui a motivé le correctif, n'a pas été rejoué avec la marge neuve (R5).
- **Correction** :
  - Option sans risque de dépense : porter `max_appels` à deux fois le plan plus 5, soit Claude 301 et Astra 205. C'est une
    garde de comptage ; les plafonds en dollars restent ceux du devis et continuent de borner. Il faut alors des configurations
    sous un nom neuf, la table et la répétition, et rejouer la répétition avec un faux amont à 8 fiches. Coût nul, quelques
    minutes.
  - À défaut, écrire au § 3.8 la borne exacte (« au plus 13 fiches de trop, toutes espèces ; au-delà, arrêt sans fiche ») et
    au § 7 que le cas à 8 fiches n'est pas rejoué.

### CLI-02 — majeur — source Gu-Krenn : un rapprochement du rédacteur et un lien omis qui fabrique une fausse nouveauté

- **Où** : `pieces/source-gu-krenn-ibrahim-v1.json`, œuvres `chaleur-2507.21919` et `r8-post-entrainement` ; fiche l. 56-62
  (§ 3.4).
- **Rapprochement** : `chaleur-2507.21919` porte « optimisation directe des préférences ». La pièce (§ 1.1) dit seulement que
  « le rôle de l'optimisation par préférences n'est que supposé (les évaluateurs humains récompenseraient implicitement la
  chaleur…) ». Elle parle de l'optimisation par préférences en général, pas de la méthode « optimisation directe des
  préférences », qu'elle ne nomme que chez Open Character Training (§ 2) et dans R8.
  - Le choix est déclaré (l. 61-62), mais il contredit la règle déclarée elle-même (« aucun rapprochement du rédacteur »).
  - Effet : « entraînement à la chaleur », « phrase émotionnelle », « fausse croyance de l'utilisateur » et les autres
    concepts de cette œuvre sont comptés reliés à l'optimisation directe des préférences.
- **Lien omis** : `r8-post-entrainement` ne porte pas « loi d'attraction », alors que la pièce sycophancie (§ 2) dit que R8 est
  « la loi mesurée à chaque étape publique du post-entraînement ».
  - Effet : « loi d'attraction » × « apprentissage par renforcement », × « récompense vérifiable » et × « étapes publiques du
    post-entraînement » sortent « jamais reliées », vérifié.
  - Le bras pousserait donc comme neuve la mesure que Lazar a déjà préenregistrée (R8).
- **Moindre** : `loi-attraction-r3-r6` et `loi-r6-nos-resultats` sont deux œuvres pour le même travail (R6). C'est sans effet
  sur les liens, mais la règle dit « une œuvre par source ».
- **Correction recommandée** (source v2, nom neuf, puis empreintes, table, répétition) :
  - retirer « optimisation directe des préférences » de `chaleur-2507.21919` ;
  - ajouter « loi d'attraction » à `r8-post-entrainement` ;
  - fondre les deux œuvres R6.
- **À défaut** : déclarer nommément les deux premiers points au § 3.4 et au § 8.4.

### CLI-03 — mineur — le protocole « mentors du soir » ne nomme pas la course parmi ses entrées

- **Où** : l. 105-108 (§ 6). Le protocole (`fbbbb520…`, § 1) ne prend en entrée que les cellules du tour du collisionneur et
  les fiches du matin. La spécification de la course (§ 3) ne nomme aucun protocole.
- **Correction** : l'inscrire comme écart n° 7 au § 8 (« lecture de la course au protocole des mentors du soir, par
  extension ; à confirmer par conv-audit »), et dire comment ses fiches se joignent à celles du tour (dédoublonnage, étape A).

### CLI-04 — mineur — une règle propre au collisionneur est servie aux proposeurs

- **Où** : `pieces/consigne-proposeur-ibrahim-v1.md`, section « Règles d'intégrité » servie à l'octet. On y lit « Au plus
  1 200 mots par cellule de conception ».
- **Effet** : la course n'a pas de « cellule ». Un proposeur peut lire la règle comme une borne pour ses six fiches à la fois,
  et les raccourcir.
- **Correction** : le déclarer au § 8.2, sans retoucher la consigne (fidélité à l'octet).

### CLI-05 — mineur — juge : deux items qu'il ne peut pas lire seul

- **Où** : `pieces/consigne-juge-ibrahim-v1.md` l. 15-19.
- **Le constat** :
  - K5 demande « ce que les travaux de la mentore ont déjà fait » et « n'invente aucun identifiant ». Le juge ne voit pas les
    pièces : il ne peut ni le vérifier, ni savoir si 2507.21919, 2511.01689 ou 2605.21778 sont donnés par une pièce.
  - K1 exige une étape d'apprentissage par renforcement. Il défavorise les fiches des axes `mesure_et_juge` et
    `resultat_trompeur` qui n'en ont pas.
- **Effet** : faible, puisque les sorties des juges sont rapportées à part.
- **Correction** : une phrase au § 3.2.

### CLI-06 — mineur — cosmétique

- **Le constat** : la docstring de `repetition/faux_mandataire_tls_ibrahim_v1.py` (l. 12) dit encore « 8 fiches par proposeur ».
  Le code lit `simulation.fiches_par_appel` (6) dans la configuration. Rien ne change à l'exécution.
- **Correction** : à corriger dans une version suivante.
