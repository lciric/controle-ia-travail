# P3-bis, écart 3 — relance à l'aveugle après la fin anormale par épuisement du crédit, garde du crédit d'origine rétablie : rapport du développeur-rédacteur, v1

- Écrit le 2026-11-13 vers 08:20 UTC (heure relevée par `date -u`) par un **développeur-rédacteur neuf** (Claude Opus 5.5),
  qui n'a écrit ni la chaîne de P3-bis, ni les écarts 1 et 2, ni leurs addendums.
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-p3bis-ecart3-v1.md`
  (`09311f1c4aed6db0fa01c6b2737e07c57c5f3b924f3559cc3abbd0fb387a75ba`, recalculée, égale à son compagnon).
- Décision : R-2492 (mot de Lazar, option (b) des nœuds R-2490 et R-2491).
- Branche `prep/p3bis-ecart3-v1`, tirée de `444645bbde329e05a5738e9a40a8ad48c8c28eb4` (tête de `prep/p3bis-ecart2-v1`),
  dans un arbre de travail neuf du bac à sable. Ajouts seulement, aucun fichier existant modifié (R12), **aucune
  poussée**.
- **Aucune dépense.** Aucun appel à l'interface de Vast ni à aucun modèle, aucune instance touchée, aucune clé lue.
- Rien n'a été lu de T0.7 ; ni la branche `calcul/p3bis-reel-v1`, ni aucun résultat de P3-bis n'ont été ouverts ;
  aucun chemin interdit n'a été listé ni ouvert ; aucun outil n'a haché l'arbre entier. L'arbre de travail neuf extrait,
  comme tout arbre de ce commit, des dossiers interdits ; ils n'ont été ni listés ni ouverts.

## Verdict

Les deux pièces de code demandées sont faites et éprouvées : l'**enchaîneur v6**, qui appelle le lanceur d'origine scellé
(garde du crédit d'origine rétablie, écart 1 retiré), et son **banc R5**, **tous les cas conformes**, dont le témoin de
l'écart 1 (création à 7,05 USD) et les trois artefacts demandés (crédit sous le minimum, lanceur d'origine modifié,
tentative N = 2 sans la branche v1). Les bancs existants du lanceur d'origine et de l'écart 2 rejouent égaux à leurs
journaux. Le brouillon 1 de l'**addendum 3** est écrit et scellé (versé dans le commit qui suit celui du code). Reste : la contre-lecture (R2), le scellement de
l'addendum, la recharge par Lazar et le sort de l'instance 60417353 (préalables 2 et 3 de l'addendum).

## Fichiers neufs

Tous sont sous `docs/procedures/P3-bis-temoin-positif-v1/` et chacun est scellé par son compagnon `.sha256`.

| Fichier | sha256 | Rôle |
|---|---|---|
| `enchaineur_p3bis_v6.sh` | `1b49b701253b89fd42cad589097f700697dd38de0a178b1fadda168dbd7f521f` | enchaîneur détaché v6 (appelle le lanceur d'origine scellé) |
| `essais_ecart3_p3bis_v1.sh` | `56659e9d498ade34b9d00578433f2eb0f00bea1184de25fd9aebb1e878d6bf81` | banc des essais R5 de l'écart 3 |
| `essais-ecart3-p3bis-v1.log` | `06e2aeca127f4c886d3fd891e141623097a84eebc21fddc7823d269981d8436a` | journal du passage final (2026-11-13T08:03:54Z → 08:09:55Z) |
| `sorties-essais-ecart3-v1/` (7 fichiers) | voir leurs compagnons | sorties choisies du passage final : journal de v6 et `lancement.txt` du cas sain (E6-01) ; console du lanceur à 7,05 USD (E6-04) ; `lancement.txt` du témoin v5 (E6-04T) ; refus de v6, lanceur modifié (E6-11) ; refus du lanceur, épingle contournée (E6-12) ; refus du lanceur, N = 2 sans branche v1 (E6-14) |
| `rapport-developpeur-p3bis-ecart3-v1.md` | son compagnon | ce rapport |

Hors du dossier, dans le commit suivant : `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-3-relance-credit-v1-brouillon1.md`
(brouillon 1 de l'addendum 3, scellé par son compagnon).

Aucun fichier existant n'est modifié. Les originaux restent au dossier, égaux à S (cas R-03) ; v5, le lanceur d'écart 1 et
les pièces d'écart 2 sont inchangés (cas R-04).

## Enchaîneur v6

- v6 = v5 (`34131eaf…`, gardé tel quel) dont le **seul changement de logique est le lanceur appelé** :
  `lancer_p3bis_v2.sh`, le lanceur d'origine scellé (`029bdb5c…`, égal à sa copie versée à S), épinglé
  (`E_LANCEUR`, l. 35) et vérifié avant tout appel (l. 47-49).
- Hors commentaires, **trois lignes** diffèrent de v5 (cas V-01, diff cité au journal) : l'épingle du lanceur, le nom
  dans l'usage, l'étiquette du journal « enchaîneur p3bis v6 ». L'en-tête et deux commentaires sont réécrits.
- Les arguments passés au lanceur (S, `DOSSIER_NEUF/traces`, `EN_MARCHE`, N) sont ceux de v5 : l'usage du lanceur
  d'origine est le même que celui du lanceur d'écart 1, qui en était la copie.
- Le lanceur d'origine se contrôle lui-même (bloc 2 : `$0` comparé à sa copie versée à S). Appelé par
  `bash "$H/lancer_p3bis_v2.sh"`, `$0` est bien le fichier du dossier. L'épingle de v6 et ce contrôle forment deux gardes
  indépendantes (cas E6-11 et E6-12).
- Contrôle à cinq minutes, surveillance et module d'écart 2 : mêmes épingles que v5 (cas V-03), mêmes appels.
- v6 ne vérifie pas sa propre empreinte (comme v5) : la session la vérifie avant le lancement.

## Essais R5

**Le banc.** `essais_ecart3_p3bis_v1.sh RACINE_NEUVE PYTHON_AVEC_PYTEST`, joué avec l'interpréteur du `.venv` du dépôt
(Python 3.13.18, pytest 9.1.1), un seul processus. Faux outil de location (aucun service appelé), horloge simulée
(faux `date` et `sleep`), dépôt synthétique et dépôt nu local, registre des GO temporaire (en-tête et ligne
GO-2026-11-10-02 de `main`, plus une ligne de calcul fabriquée, GO-2026-11-08-13, comme le banc du lanceur d'origine),
contrôles avant dépense en bouchon. Le distant factice porte, comme le vrai au 13 novembre, une branche
`calcul/p3bis-reel-v1` égale à S.

**Copies jouées** (lignes changées comptées par le banc) : lanceur d'origine et lanceur d'écart 1 : 3 lignes (`DEPOT`,
`DEPOT_URL`, `INTERVALLE_OFFRE_S`) ; enchaîneur v6 et enchaîneur v5 : 1 ligne, l'épingle du lanceur devenue celle de sa
copie jouée. Les autres scripts sont des copies exactes.

| Section | Cas | Contenu |
|---|---|---|
| V forme | V-01 à V-03 | trois lignes hors commentaires changées contre v5 ; épingle du lanceur égale au lanceur d'origine du dossier et à S ; épingles d'écart 2 égales à v5 et aux pièces |
| E sain | E6-01 (b à e), E6-03, E6-07 | N = 2, crédit 50 : lanceur d'origine appelé, ligne officielle du crédit, aucune ligne d'écart 1, création sur `calcul/p3bis-reel-v2` étiquette `p3bis-v2`, contrôle d'écart 2 à + 181 à 185 s conforme, surveillance jusqu'à FIN, dépense antérieure passée ; seuil au centime 20,00 ; avec une instance nommée à 1,342 USD/h, 33,42 |
| E artefacts du crédit | E6-02, E6-04, E6-05, E6-05c, E6-06, E6-09, E6-10 | 19,99 ; **7,05 (crédit de la création de 60432755)** ; 0 ; −0,93 ; 33,41 avec l'instance nommée ; outil en échec avec réponse lisible ; réponse illisible : aucune création, ni contrôle ni surveillance |
| E témoin | E6-04T | **l'enchaîneur v5 et le lanceur d'écart 1 créent à 7,05 USD** (le défaut de l'écart 1 reproduit) |
| E liste fermée | E6-08 | instance d'autrui arrêtée sur le compte (cas de 60417353) : refus |
| E lanceur | E6-11, E6-12, E6-13 | lanceur d'origine modifié : refus de v6 avant tout appel ; épingle de v6 contournée : refus du lanceur lui-même (« exécuté ≠ copie versée au commit S ») ; lanceur absent : refus |
| E branches | E6-14, E6-15, E6-16 | **N = 2 sans la branche v1 au distant : refus** ; branche v2 déjà présente : refus ; N = 1 avec la branche v1 présente : refus |
| E aval | E6-17, E6-18 | échec d'amorce : contrôle en code 1, surveillance qui suit et arrête ; pièce d'écart 2 modifiée : refus |
| E arguments | E6-19 à E6-22 | dépense antérieure illisible ; dossier existant ; usage ; cinq créations factices en tout, toutes sur v2 |
| R rejeux | R-01 à R-04 | banc du lanceur d'origine (58 cas, verdicts égaux au canonique de S) ; banc de l'écart 2 (132 cas, verdicts égaux au journal versé) ; quinze scripts d'origine égaux à S ; v5, lanceur d'écart 1 et pièces d'écart 2 inchangés |

**Ce que les rejeux comparent.** R-01 : lignes du journal hors lignes citées « | » (deux lignes citées diffèrent : les
commits factices des cas L17 et L18). R-02 : la liste « nom du cas, verdict » des 132 cas, et la dernière ligne ; les
descriptions portent des heures et des chemins.

**Passages.** Deux passages complets, l'un de 07:57:48Z à 08:03:46Z (non versé), l'autre, final et versé, de 08:03:54Z
à 08:09:55Z : **71 cas, 0 non conforme**, dernière ligne « ESSAIS DE L'ÉCART 3 DE P3-BIS : CONFORMES ». Une fois
normalisés les heures, les commits factices et le nom de la racine, les deux journaux ne diffèrent que par deux lignes
citées : l'empreinte de la copie jouée du lanceur, qui porte le chemin de la racine (cas E6-11 et E6-13). Aucune sortie
versée n'affiche de jeton factice (vérifié par recherche).

## Lignes du texte scellé touchées

Texte `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`), détail et citations dans l'addendum 3 :
- l. 1844 (critères, ligne 1 : relance seulement si aucun épisode joué) — **Q1, règle R1** ;
- l. 2468-2471 (devis, « Relances ») — Q2 ;
- l. 1936-1937, 1947 et 2150-2152 (garde du crédit) — Q3, **retour à la lecture d'origine** ;
- l. 2285 (écart 8, recharge automatique) — Q4 ;
- l. 2289-2291 (écart 11, tentative et branche) — Q5 ;
- l. 1962-1963 (dépense cumulée, toutes tentatives) — Q6 ;
- l. 2174-2175 (lanceur d'origine cité par empreinte) — Q7 ;
- lus sans changement : l. 1410-1411 (lignes `PROGRES`), l. 1941-1942 (borne de création), l. 1949-1954 (relance après une
  instance arrêtée), l. 2465 et 2467 (attendu et pire cas d'une tentative).

Addendums : A1 l. 46-58, 164-185 (règle retirée, réserve gardée) ; A2 l. 296-297, 302-304, 311-318, 351-359, 361-385,
453-461, 514-522, 526-546, 552-554 (lus sous l'écart 3).

## Montant de recharge conseillé à Lazar

Règle de la consigne : au minimum de la garde plus le coût attendu de la course. Calcul :
- garde : M = 20 + 10 × P USD (texte l. 1936-1937), P = somme des prix de l'heure des instances nommées en marche ;
- coût attendu, haut de la fourchette du devis : K = 7,5 USD (l. 2465) ;
- dette du compte : D = 0,93 USD (solde −0,93 à 07:30Z, R-2491) ;
- **sans autre instance en marche** : 20 + 7,5 + 0,93 = **28,43 USD** ;
- **avec 60417353 relancée et nommée** (1,342 USD/h, R-2491) : 20 + 13,42 + 7,5 + 0,93 = **41,85 USD** ;
- variante prudente (pire cas d'une tentative, K = 22,2 USD, l. 2467), avec 60417353 : **56,55 USD**.

**Conseil : au moins 42 USD** (couvre le cas avec 60417353 en marche ; ≈ 13,4 USD de marge sans elle), relu au crédit
présent juste avant le lancement, car d'autres instances consomment le crédit entre-temps.

## Points ouverts

1. **Instance 60417353** (témoin Bailey, autre session, arrêtée faute de crédit) : tant qu'elle reste arrêtée sur le
   compte, la liste fermée refuse toute création (cas E6-08). Relance et nom en `EN_MARCHE` avec son GO, ou destruction
   par sa session ou par Lazar : à trancher hors de cet écart.
2. **Dépense antérieure** : calcul indicatif ≈ 6,07 USD (addendum, préalable 4), à refaire par la session ; la facture de
   60432755, si elle est lisible, remplace le majorant de 2,00 USD et le stockage estimé.
3. **Condition (ii)** : la tête de `calcul/p3bis-reel-v1` est à relire égale à S juste avant le lancement, par
   `git ls-remote` seulement (préalable 5) ; le développeur ne l'a pas fait (branche interdite à son mandat).
4. **Empreinte de v6** (`1b49b701…`) : à vérifier par la session avant le lancement.
5. **Refspec** : le lanceur d'origine fait `git fetch` sans refspec sur le clone de `/home/user/controle-ia-travail`
   (l. 88 et 92), comme le lanceur d'écart 1 ; restreindre le refspec par défaut de ce clone à `main` et
   `prep/p3bis-ecart3-v1`, comme R-2463 (préalable 8).
6. **Borne du banc** : le banc lit la date réelle pour la borne de création du 18 novembre ; joué après cette date, ses
   cas de création rendraient le code 3 (comme les bancs des écarts 1 et 2).
7. **Cause « probable »** : la condition (i) repose sur le constat de R-2491 (solde, consommation, heure) ; le loueur n'a
   rendu aucune raison d'arrêt (R-2490). À juger par le contre-lecteur.
