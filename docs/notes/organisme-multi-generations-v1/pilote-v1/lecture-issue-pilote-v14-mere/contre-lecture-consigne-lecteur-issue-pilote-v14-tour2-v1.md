# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — tour 2 — v1

Contre-lecteur neuf (R2), modèle C ; auteur de la pièce : modèle A. Début 2026-11-16T13:43:31Z ; fin 2026-11-16T13:50Z (`date -u`).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v2.md`, empreinte
`0e12acbd6ea72bf2318c809d13be20382b6e6864041ce0e20a56365425c8e30b` (égale à son compagnon). Version précédente : `…-v1.md`,
`5189c44202e8f9aa8ed65506222f9317e6596cf1c0839b0c89a9af43ad60d539` (recalculée, égale). Rapport du tour 1 : empreinte recalculée
`14725e82ff9e8d6a7dc0f11457dcb6131c45a69d69d2085965c3fad430e2c8ea`, égale.

## Verdict : corrections

Deux corrections majeures, sept mineures. Les corrections du tour 1 sont appliquées fidèlement ; ce qui reste tient à deux points que
la pièce déclare elle-même « ouverts » et à des précisions que la relecture des passages touchés fait apparaître. Aucune conception en
cause : « a_refaire » n'est pas justifié.

## Ce qui a été lu, ce qui ne l'a pas été

Lus : la consigne v2 en entier ; son différentiel avec la v1 (`diff`) ; le rapport du tour 1 ; le texte scellé (empreinte recalculée
`8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, égale), en entier ; la procédure v14 (commit `2d35cafa`),
sections 5 à 11 ; le programme de dépense (commit `dbe3d24e`, empreinte recalculée `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`,
égale) ; le programme de la mesure (`676d5f37…`, égal) pour les noms de champs ; le registre des inscriptions ; la ligne R-2981. Pour
les **noms de champs**, j'ai lu les pièces de l'essai à blanc v70 du dépôt (`code-v70/essai-a-blanc-v70/A/`, proposeurs factices : sortie de
mesure, pièce de liaison, relevé, manifeste, lecture) : ce ne sont pas des pièces de l'issue réelle ; les noms qu'elles portent sont ceux
du même code, mais je n'ai pas pu les confirmer sur les pièces réelles. De `retour/` : **noms et tailles seulement**. Aucune pièce de
`retour/` ni de la branche de sortie ouverte ; aucun `pytest` ; aucune clé.

## A. Les corrections du tour 1 sont-elles appliquées fidèlement ?

`diff` v1 → v2 : le différentiel ne contient que les changements ci-dessous, tous vus.

| correction | état dans la v2 |
|---|---|
| C1 (nouveau point 0, arrêts) | présente, mot pour mot ; voir m1 (contradiction interne héritée du couple) |
| C2 (P-2 contre P-2 avec réserve) | présente, mot pour mot ; confirmée sur le code de la mesure (`regle.issue` = `P-2` dans les deux cas, réserve = `regle.noeuds_avant_banc` non vide) |
| C3 (pièces manquantes) | présente ; la remarque « à adapter par A… » du rapport est omise (correct : elle ne s'adressait pas au lecteur) |
| C4 (audit de symétrie) | présente, mot pour mot ; la graine reste « point ouvert » (M1) |
| C5 (deux couples, dépense) | présents, mot pour mot ; empreinte du programme exacte (`9866e611…`), parts exactes |
| C6, C8, C10, C11, C13 | présentes, mot pour mot |
| C7 (compagnons, secret, phrase) | présente, mot pour mot ; la parenthèse « A dit si… » reste (M1) |
| C12 (taux d'erreur) | présente **avec une correction de chiffres**, justifiée : le couple du tour 1 disait « mêmes taux à 12 et 14 appels répondus » ; le texte scellé donne 0,22 et 0,21 (refus à 0,02), 0,29 et 0,27 (acceptation à 0,051). Chiffres vérifiés contre la section « Prédiction chiffrée et signe attendu » : 0,20 ; 0,26 ; 0,22 ; 0,21 ; 0,29 ; 0,27, tous exacts. C'était une erreur de mon tour 1, bien rattrapée |
| R1 à R4 (facultatives) | non appliquées, comme permis ; R1 reprise en m7 parce qu'elle prive le lecteur d'une interdiction |

**Ajouts hors des couples du tour 1** (le différentiel n'est donc pas limité aux corrections) : (i) la ligne 3, « Version 2, … » ;
(ii) la section « Contre-lecture » en fin de pièce (une trentaine de lignes). Ils sont avoués par la pièce, ne remettent rien d'interdit et leurs
références sont exactes (empreintes de la v1 et du rapport du tour 1 : vérifiées). Mais la section est **adressée à la mère et à l'auteur**
et contient deux « points ouverts à lever par l'auteur avant la remise » : une pièce à « remettre telle quelle » ne peut pas les porter (M1).
Elle affirme aussi que l'application a été faite par « un rédacteur neuf (modèle C) », alors que la commande de ce tour dit que les
corrections sont écrites par le modèle A : à trancher par la mère (voir points pour la mère).

## B. Vérifications (1) à (8)

**(1) Sections gelées et empreintes citées.** Les points 0 à 7 appliquent « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture
gelés », « Audit de symétrie (R4) » et « Liste d'arrêt », et rien d'autre ; l'ordre du « Plan d'analyse » est tenu (empreintes, mesure, issue,
coûts, exclusions, rapport), le point 0 (arrêts) précède ; l'audit est le point 7. Empreintes : texte `8aa33014…` exact ; programme
`676d5f37…` exact ; `programme_sha256`, `cartes_sha256`, `fichier_mondes_sha256` existent bien dans la pièce de liaison et le manifeste
(essai v70) ; `hors_corps.script_sha256`, `hors_corps.modules_importes` existent dans la sortie de mesure ; `mondes_sha256` y est triée (le code
écrit `sorted(...)`) : la remarque « comparer comme ensemble » est exacte. Les champs `mondes_sha256`, `regle`, `audit_R4` de la sortie de
mesure sont dans `corps.` (m3). Les contrôles de la « Liste d'arrêt » repris au point 0 sont ceux du texte (code non nul, une ligne de
registre des lancements, `aucun_monde`, relevé et manifeste non partiels, réponse brute et témoin des 16 appels, aucun coût au-dessus du
pire cas, aucune part atteinte) ; la liste du texte comporte aussi des arrêts que le lecteur ne peut juger que par les codes (empreinte
d'une pièce servie, C-16 et C-17, réflexion de l'un des proposeurs, relevé de sonde invalide) : le point 0 les couvre par « tous à 0 » et
l'état `fini` ; c'est suffisant. Rien n'est ajouté au texte scellé, sauf la précision de la graine (M1, voir plus bas).

**(2) Pièces remises, noms existants (noms et tailles seulement).** Tous les noms cités existent dans `retour/` : à la racine
`etat.txt` (468 octets), `lancements.jsonl` (158), `code-06-generer.txt`, `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`,
`code-10-mesurer.txt`, `code-10-lire.txt`, `code-11-rapatrier.txt` (2 octets chacun), `journal-09-reel.txt`, `journal-10-mesurer.txt`,
`engagement-mondes.json`, `secret-sha256.txt` (79), `phrase-sha256.txt` (87) ; sous `rapatrie-reel/` : `lecture-pilote-v70.json`,
`sortie-mesure-pilote-v70.json`, `mesure-pilote-v70.json`, `manifeste-pilote-v70.json`, `releve-pilote-v70.json`, `CARTES.json`,
`liste-rapatriement-pilote-v70.json`, les quatre `journal-relais-*.jsonl` (sans compagnon), leurs compagnons `.sha256` (sauf pour les
journaux, `etat.txt`, `lancements.jsonl` et `remis-au-sous-agent/`, comme la pièce le dit) ; `remis-au-sous-agent/sortie-lire-non-ouverte.txt`
(204). Les quatre dossiers `monde-N/` ont chacun quatre sous-dossiers de proposeur de six fichiers (corps du relais, réponse brute, témoin
d'isolement et leurs compagnons) : 16 appels, 96 fichiers, aucun `CARTES-partiel.json`. `journal-09-reel-2` n'existe pas (mention
conditionnelle correcte). Rien d'interdit n'est nommé : ni mondes, ni secret, ni phrase en clair (seules les empreintes), ni `prive/`. La
**configuration du pilote** n'est pas nécessaire (voir (6)). Deux défauts : la pièce dit « avec les seules pièces nommées » mais remet « la
copie de la branche » dont la liste n'est que « en particulier » (m2) ; le lecteur reçoit aussi `rapatrie-reel/liste-rapatriement…` qui porte
des noms de pièces laissées sur la machine (sans valeur) : sans objet.

**(3) Lecture de l'issue.** Le champ est bien `regle` de `lecture-pilote-v70.json` (essai v70 : champs `issue`, `regle.issue`,
`regle.noeuds_avant_banc`, `couts`, `a_dire_au_rapport`) ; la table est celle du texte, première ligne qui s'applique ; nœuds et « ce qui suit »
mot pour mot demandés ; la distinction P-2 / P-2 avec réserve est maintenant écrite et exacte (C2). Le lecteur peut aussi lire P-1 par la
borne basse non arrondie de `principale` (remarque facultative R3 du tour 1, toujours valable, non exigée).

**(4) Arrêts.** Le point 0 existe et précède la lecture de l'issue ; les contrôles sont mécaniques. Deux défauts : une contradiction
interne (m1) et une exposition de l'issue avant la fin des points 0 et 1 par l'ouverture de la sortie de mesure, qui porte `corps.regle`
(M2). Aucun repli silencieux : le texte « jamais sauté en silence (R5) » est présent.

**(5) Rendu.** Conforme : verdict scellé, en français, sans identifiant de modèle ni identifiant servi, sur une branche de travail
désignée par la mère, fichier neuf au nom donné par elle (R12), rien d'autre d'écrit. Le contenu demandé est complet (issue, ligne, comptes,
empreintes, écarts, dépense, contrôles d'arrêt, audit R4, phrases, nœuds). « les trois phrases du point 6 » est périmé : il y en a
quatre (m6). « (brief, section 6) » renvoie à un document que le lecteur ne reçoit pas (m7).

**(6) Dépense : quelle voie.** **Voie 1 : la dépense lui est remise calculée par le programme du compte organisme**, le lecteur recoupant
lui-même, par lecture, les sommes du relevé et des journaux. Le point 4 des pièces fixe bien cette voie, nomme le programme et son
empreinte exacte, dit ce qu'il lit (seulement `releve-pilote-v70.json` et `journal-relais-*.jsonl` : confirmé sur le code, qui ne lit pas
la configuration ni les prix et n'ouvre ni la lecture, ni la sortie de mesure, ni la pièce de liaison) et d'où viennent les arguments (la
mère). Conforme à R-2981 (« dépense par son programme »). Deux précisions : le code de sortie 3 du programme n'est pas dans sa sortie JSON,
et la part de la machine (3 USD, comprise dans la ligne de 21,72 USD) n'est pas citée (m4). Observation, non exigée : la lecture contient
elle-même un champ `couts` (par appel : coût de la commande, coût du relais, écart) ; le lecteur le verra au point 3 ; la pièce ne dit pas s'il
le recoupe : le plus simple est de le lui faire rapporter à côté de la sortie du programme de dépense.

**(7) Symétrie R4.** Les déclencheurs chiffrés du texte (x = 0, x ≥ 3) et leur contenu sont repris ; l'audit commente, ne change pas
l'issue. Précisions : le champ est `corps.audit_R4` ; il est **absent** quand l'issue est P-0 (la sortie rend la règle avant de le calculer :
code lu) (m5). La **graine** n'est pas définie par le texte (« dérivée de l'empreinte de `CARTES.json` ») : la formule de la pièce est une
proposition du tour 1, présentée comme ouverte ; elle laisse aussi libre l'ordre des appels, l'ordre des cartes et le générateur, donc
le tirage n'est pas reproductible (M1). Les pièces servies : le manifeste porte `controles.episodes_servis` (traits, issues vues, …) et
`gabarit_sha256`, la lecture porte le gabarit servi dans `a_dire_au_rapport`, le relevé porte `gabarit_sha256` et `episodes_sha256` par appel : le
lecteur peut donc faire une partie des vérifications de l'audit sans pièce supplémentaire ; la pièce pourrait le dire (facultatif).

**(8) Identifiants de modèle, empreintes.** Aucun identifiant de modèle ni de version servie dans la pièce. Elle cite en revanche les
**quatre noms de proposeurs du texte scellé** (point 2 des pièces) ; ce sont des noms du texte, pas des identifiants servis, mais deux
d'entre eux ressemblent à des noms de modèle : voir points pour la mère. Empreintes citées exactes (texte, programme de la mesure,
programme de dépense, v1, rapport du tour 1). Ce rapport n'emploie que les lettres A, B, C.

## Corrections exigées (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans la v2, vérifié par comptage)

### Majeures

**M1 (deux points « ouverts » à lever avant la remise ; graine non reproductible ; parenthèse adressée à l'auteur).**
(a) ancien : `égaux aux empreintes du secret, de la phrase, de `H` et de `S1` à `S4` du registre (A dit si `phrase-sha256.txt` est de même nature que l'empreinte inscrite) ;`
→ nouveau : `égaux aux empreintes du secret, de la phrase (empreinte du fichier de la phrase, retour à la ligne final compris : procédure v14, section 5, point 5), de `H` et de `S1` à `S4` du registre (la valeur hexadécimale est celle que porte le fichier, après son nom de champ éventuel) ;`
(vérifié : la machine pousse `phrase-sha256.txt` après avoir contrôlé que l'empreinte du fichier déchiffré égale celle du feu, et le registre
inscrit « l'empreinte du fichier de la phrase (retour à la ligne final compris) » imprimée par ce feu ; même nature.)
(b) ancien : `l'entier des 16 premiers octets, gros-boutiste, de sha256 de `CARTES.json` ; tirage sans remise, toutes les cartes si l'appel en a au plus 3),`
→ nouveau : `l'entier g des 16 premiers octets, lus gros-boutiste, de l'empreinte sha256 (32 octets) du fichier `CARTES.json` tel que remis ; générateur `numpy.random.default_rng(numpy.random.SeedSequence(g))` ; appels pris par monde croissant puis par nom de proposeur dans l'ordre alphabétique ; pour un appel de k cartes (toutes celles que `CARTES.json` lui attribue, refusées comprises, dans l'ordre où il les liste), tirage `rng.choice(k, size=3, replace=False)` ; toutes les cartes si k ≤ 3),`
(Proposition : A la confirme ou la remplace par une définition aussi complète ; ce qui compte est qu'elle soit complète et écrite (R9). Si
le lecteur n'a pas `numpy`, le tirage est « non fait », dit au rapport.)
(c) Section « Contre-lecture » : les deux puces ne doivent plus dire « point ouvert ».
ancien (trois lignes, retrait de 4 espaces) : `**Point ouvert, à lever par l'auteur avant la remise** : la formule de la graine
    est une proposition du contre-lecteur ; le texte scellé dit seulement « graine dérivée de l'empreinte de `CARTES.json` » ; l'auteur la
    confirme ou la remplace (R9).`
→ nouveau : `**Levé au tour 2** : la formule de la graine, proposée au tour 1, est confirmée et complétée par l'auteur (modèle A) : ordre des appels, ordre des cartes, générateur (voir le point 7) ; le texte scellé dit seulement « graine dérivée de l'empreinte de `CARTES.json` ».`
ancien (deux lignes) : `**Point ouvert, à lever par l'auteur avant la remise** : la
    parenthèse sur la nature de `phrase-sha256.txt` s'adresse à l'auteur, non au lecteur ; le rédacteur ne peut la trancher sans ouvrir
    la pièce.`
→ nouveau : `**Levé au tour 2** : la parenthèse sur la nature de `phrase-sha256.txt` s'adressait à l'auteur, non au lecteur ; elle est retirée.`
et ancien : `l'auteur le confirme et retire la parenthèse.` → nouveau : `le contre-lecteur du tour 2 l'a vérifié et l'auteur a retiré la parenthèse.`
(d) À la fin de la section, une puce pour le tour 2 (au choix de A, mais utile à la traçabilité) : rapport
`contre-lecture-consigne-lecteur-issue-pilote-v14-tour2-v1.md`, empreinte à reporter après son scellement, verdict « corrections ».

**M2 (l'issue est exposée avant la fin des points 0 et 1 : la sortie de mesure porte `corps.regle`).** Le texte gèle « tout arrêt après le premier appel :
aucune issue n'est lue, pas même P-0 » ; or le point 1 exige d'ouvrir `sortie-mesure-pilote-v70.json` (`hors_corps`, `corps.mondes_sha256`), qui contient aussi `corps.regle`,
`corps.principale` et `corps.audit_R4`. La consigne ne protège que `lecture-pilote-v70.json` et `sortie-lire-non-ouverte.txt`.
ancien : `(ces deux pièces s'ouvrent en dernier, après les points 0 et 1).`
→ nouveau : `(ces deux pièces s'ouvrent en dernier, après les points 0 et 1 ; avant cela, `sortie-mesure-pilote-v70.json` ne s'ouvre que pour `hors_corps` et `corps.mondes_sha256`, jamais pour `corps.regle`, `corps.principale` ni `corps.audit_R4`, ni le relevé ni le manifeste pour autre chose que leurs champs de contrôle ; une issue aperçue avant la fin des points 0 et 1 est écrite au rapport).`

### Mineures

**m1 (contradiction dans le point 0 : « contrôle impossible : arrêt » et « non fait »).** Les deux phrases du point 0 prescrivent deux conduites pour le même cas.
ancien : `écart ou tout contrôle impossible : arrêt, rapport,`
→ nouveau : `écart (empreinte, code, état, compte, part) : arrêt, rapport,`
et ancien : `ne peut faire est écrit « non fait » avec sa cause, jamais sauté en silence (R5).`
→ nouveau : `ne peut faire (pièce absente ou illisible) est aussi un arrêt aux points 0 à 2, écrit « non fait » avec sa cause, jamais sauté en silence (R5) ; au point 7 seul, il est écrit « non fait » sans arrêt.`

**m2 (« seules pièces nommées » contre « la copie de la branche »).**
ancien : `final (`etape=fini` dans `etat.txt`) ; en particulier :`
→ nouveau : `final (`etape=fini` dans `etat.txt`) ; la mère ne remet aucune pièce de la copie qui n'est pas nommée ci-dessous ; elle remet :`

**m3 (noms de champs exacts ; chemins `corps.`).** (noms relevés sur l'essai à blanc v70 et le code ; à confirmer par A sur les pièces réelles sans les ouvrir si possible)
ancien : `fichiers exclus au balayage : aucun nécessaire`
→ nouveau : `le champ `exclus_balayage=` ne nomme aucune pièce remise ici`
et ancien : `relevé et manifeste complets (non partiels)`
→ nouveau : `relevé et manifeste complets (`partiel` faux et `arret` nul dans chacun ; `appels_complets_illisibles` nul dans le relevé)`
et ancien : `il lit `audit_R4` de la sortie de la mesure.`
→ nouveau : `il lit `corps.audit_R4` de la sortie de la mesure.`
et ancien : `(la liste `mondes_sha256` de la sortie de mesure est triée`
→ nouveau : `(la liste `corps.mondes_sha256` de la sortie de mesure est triée`

**m4 (dépense : code 3 hors sortie ; part de la machine).**
ancien : `un code 3 du programme ou une part dépassée est déjà un arrêt du point 0)`
→ nouveau : `une part dépassée est déjà un arrêt du point 0 ; le code de sortie 3 du programme n'est pas dans sa sortie JSON : la mère le donne, sinon il se déduit de `sous_la_part` (chaque proposeur et `machine`), `pi1_sous_la_ligne` et `pi2_sous_la_ligne`, qui doivent tous être vrais ; la machine contre 3 USD, comprise dans les 21,72 USD de π2)`

**m5 (`audit_R4` absent si P-0).**
ancien : `« non déclenché » : aucun audit.`
→ nouveau : `« non déclenché », ou champ absent (issue P-0 : la sortie s'arrête avant de le calculer) : aucun audit.`

**m6 (« trois phrases » périmé depuis C12).**
ancien : `les trois phrases du point 6`
→ nouveau : `les phrases du point 6`

**m7 (interdits : « brief, section 6 » n'est pas remis au lecteur).**
ancien : `(brief, section 6)`
→ nouveau : `(hors des pièces nommées ci-dessus : ni `prive/`, ni les mondes, ni la branche d'entrée `calcul/pilote-mr2-v74-entree-v14`, ni aucune clé ni variable d'environnement)`

## Remarques facultatives (aucune n'est exigée)

- F1 : au point 6, le parenthésé ne cite qu'une partie des taux d'erreur du texte (il n'y a ni 0,075 ni 0,10) ; dire « tous, dont : » avant
  « course refusée à tort… » éviterait qu'on le lise comme exhaustif (« les taux d'erreur ci-dessus » dit le texte).
- F2 : dire au point 4 si le lecteur recoupe le champ `couts` de la lecture avec la sortie du programme de dépense (voir (6)).
- F3 : dire au point 7 où se trouvent les pièces servies utiles à l'audit (`controles.episodes_servis` et `gabarit_sha256` du manifeste ;
  `a_dire_au_rapport` de la lecture) ; sans cela, le contrôle « épisodes servis » risque d'être écrit « non fait » à tort.
- F4 : le lecteur peut aussi comparer à leurs compagnons `releve_sha256` et `sortie_mesure_sha256` de la lecture, et `manifeste_sha256` et
  `sortie_sha256` de la pièce de liaison : contrôles mécaniques de liaison, non gelés par le texte ; si A les ajoute, le dire comme tels.
- F5 : la section « Contre-lecture » pourrait ne pas faire partie de la pièce remise au lecteur (elle est destinée à la mère) ; la mère peut
  en remettre une copie sans cette section, ce qui rend M1 (c) sans objet pour la pièce remise mais pas pour la traçabilité.

## Points pour la mère

1. **Provenance de l'application des corrections** : la v2 dit que les corrections ont été appliquées par « un rédacteur neuf (modèle C) »
   avec un programme ; la commande de ce tour disait que les corrections sont écrites par le modèle A. À rectifier dans la section, ou à
   expliquer : la contre-lecture neuve (R2) ne dépend pas de qui a écrit, mais la section décrit ce qui s'est passé.
2. **Choix de la graine de l'audit** : M1 (b) fixe une formule complète ; le texte scellé ne la définit pas. C'est une précision, pas un
   écart, mais elle doit être écrite avant le lancement du lecteur, et l'auteur (modèle A) la confirme (R9).
3. **Ordre de lecture des pièces** (M2) : à relayer aussi dans la consigne de lancement du lecteur (la mère ne doit pas ouvrir non plus la
   sortie de mesure).
4. **Noms de proposeurs** : la pièce cite les quatre noms de proposeurs du texte scellé, dont deux évoquent des noms de modèle. Ce ne
   sont pas des identifiants servis (R-2731 vise ceux-ci), mais le lecteur les recopiera sans doute dans son verdict ; à toi de dire si c'est toléré.
5. **Lecteur** : il lui faut Python avec `numpy` pour le tirage de M1 (b), en lecture seule ; sinon l'audit est « non fait » pour le tirage.
6. Aucune dépense, aucun écart au texte scellé, aucun mot du directeur nécessaire pour ces corrections.

## Incidents de ma main

Aucun. Fichiers de travail dans le bloc-notes de session (copies du texte scellé, de la procédure, des programmes), lectures seules ;
`git fetch` avec refspec de deux branches (`prep/…`, `lot/compte-organisme-v1`) ; aucune pièce de `retour/` ni de la branche de sortie
ouverte (noms et tailles seulement) ; les pièces de l'essai à blanc v70 lues sont dans le dépôt, hors de l'issue réelle ; aucune clé ; aucun
calcul lourd.
