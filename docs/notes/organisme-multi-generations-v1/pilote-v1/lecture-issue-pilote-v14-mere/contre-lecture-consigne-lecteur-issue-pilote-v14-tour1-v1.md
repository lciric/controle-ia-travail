# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — tour 1 — v1

Contre-lecteur neuf (R2), modèle C ; auteur de la pièce : modèle A. Début 2026-11-16T13:20:24Z ; fin 2026-11-16T13:25Z (`date -u`).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v1.md`, empreinte `5189c44202e8f9aa8ed65506222f9317e6596cf1c0839b0c89a9af43ad60d539`
(égale à son compagnon et à celle du commit `dbe3d24e`).

## Verdict : corrections

Cinq corrections majeures, sept mineures. La consigne suit bien l'ordre du « Plan d'analyse » et ne contredit aucune section gelée, mais
elle omet la « Liste d'arrêt » (hors les empreintes), laisse le lecteur confondre « P-2 » et « P-2 avec réserve », ne remet pas des pièces
que ses propres points 4 et 7 exigent, ne gèle pas l'audit de symétrie tel que le texte l'écrit, et ne fixe pas la voie de la dépense.
Aucune conception en cause : « a_refaire » n'est pas justifié.

## Ce qui a été lu, ce qui ne l'a pas été

Lus : la consigne ; le texte scellé (empreinte recalculée `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, égale) ;
procédure v14 (commit `2d35cafa`, sections 0, 8, 9, 10, 11) ; programme de dépense (commit `dbe3d24e`, empreinte recalculée
`9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, égale à son compagnon) ; registre des inscriptions ; ligne R-2981 ;
programme de la mesure `mesure_pilote_v4.py` (empreinte `676d5f37…`, égale), lu pour les noms de champs. De `retour/` : **noms et tailles
seulement** (`find … -printf '%s %P\n'`). Aucune pièce de `retour/` ni de la branche de sortie ouverte ; aucun `pytest`.

## Vérifications (1) à (8)

**(1) Sections gelées, ordre, empreintes.** Les points 1 à 6 suivent l'ordre du « Plan d'analyse » (empreintes, mesure, issue, coûts, exclusions,
rapport) ; le point 7 reprend l'audit de symétrie. Empreintes citées : texte `8aa33014…` exact ; programme `676d5f37…` exact (c'est celui du
bloc gelé et du fichier du dépôt) ; le bloc gelé liste bien les douze modules importés et `mesure_pilote_v4.py` (`modules_importes` est au
champ `hors_corps` de la sortie, d'après le code lu). Contrôles dont je ne peux confirmer le nom de champ : `fichier_mondes_sha256` (existe :
`controles.mondes.fichier_mondes_sha256` du manifeste, d'après la contre-lecture du code v69), `programme_sha256` et `cartes_sha256` de la pièce
de liaison `mesure-pilote-v70.json` (`programme_sha256` : nommé par la procédure section 8 ; `cartes_sha256` : **absent du texte scellé et de
la procédure**, donc contrôle de liaison ajouté par la consigne ; mécanique, inoffensif, mais A doit en confirmer le nom sur le code du lanceur
v74). La sortie de la mesure donne `mondes_sha256` **triée** (code lu) : la comparaison à `S1` à `S4` est un ensemble, pas un ordre
(correction C6). La sortie porte aussi `hors_corps.script_sha256` : non contrôlé par la consigne (C6). Écarts au gel : la « Liste d'arrêt » est
déclarée appliquée (point 1 de la consigne) mais aucun de ses contrôles n'est écrit hors empreintes (C1) ; l'audit de symétrie est réduit à une
phrase générique (C4).

**(2) Pièces remises (noms existants dans `retour/`).** Existent : `rapatrie-reel/{lecture-pilote-v70.json, sortie-mesure-pilote-v70.json,
mesure-pilote-v70.json, manifeste-pilote-v70.json, releve-pilote-v70.json, CARTES.json}` et leurs `.sha256` ;
`remis-au-sous-agent/sortie-lire-non-ouverte.txt` (204 octets, sans compagnon) ; `journal-10-mesurer.txt`, `code-10-mesurer.txt`,
`code-10-lire.txt`, `journal-09-reel.txt` (à la **racine** de la copie, la consigne ne le dit pas), `engagement-mondes.json`, `etat.txt` ;
`journal-09-reel-2` n'existe pas (la mention « ou … -reel-2 » est correcte, conditionnelle). Manquent dans la consigne alors que le texte ou les
points 4 et 7 les exigent : `rapatrie-reel/journal-relais-{fable52,opus55,argon,astra}.jsonl` (le point 4 dit « journaux des relais » mais ne
nomme que des journaux d'étape) ; `rapatrie-reel/liste-rapatriement-pilote-v70.json` ; `lancements.jsonl` ; les `code-06` à `code-11` ;
`secret-sha256.txt` et `phrase-sha256.txt` (le registre en donne les empreintes ; la consigne les annonce au point 3 sans les faire contrôler) ;
les dossiers `monde-N/PROPOSEUR/` (réponses brutes, corps des relais, témoins d'isolement : le point 1 du « Plan d'analyse » les compte parmi
les empreintes à vérifier, la liste d'arrêt exige leur présence, l'audit les lit) ; `rapatrie-blanc/` existe et n'est pas mentionné (risque de
confusion avec `rapatrie-reel/`, dont le `CARTES.json` est différent : 106 034 contre 147 747 octets). **Prix de la configuration** : la
configuration v12 n'est pas dans `retour/` ni sur la branche versée ; sous la voie 1 (point 6) elle n'est pas nécessaire (voir C5). Rien de ce
que le texte interdit n'est remis : `prive/` (secret, phrase, mondes) n'est pas dans la liste de `retour/` ; les réponses brutes sont dans
`rapatrie-reel/monde-N/…` et sont permises par le texte (procédure section 9), la consigne interdit déjà de les recopier.

**(3) Lecture de l'issue.** Le champ est bien `regle` et la table est celle du texte, ordre de première ligne correct, nœuds et « ce qui suit »
mot pour mot demandés. **Défaut** : dans le code de la mesure, `regle.issue` vaut `P-2` aussi bien pour « P-2 avec réserve » que pour « P-2 » ;
la réserve est portée par `regle.noeuds_avant_banc` non vide. La consigne ne le dit pas : un lecteur qui lit seulement `regle.issue` ne
verrait pas la réserve, donc le nœud de Lazar avant le banc (C2).

**(4) Arrêts.** Seul l'écart d'empreinte arrête. Manquent : `etat.txt` `etape=fini`, codes 0 de `code-06` à `code-11`, aucun arrêt (A) /
code 3 / « noeud, machine gardee » / « sortie inattendue », une seule ligne de `lancements.jsonl`, relevé et manifeste non partiels (pas de
`CARTES-partiel.json`), `"aucun_monde": true`, aucun coût au-dessus du pire cas, aucune part atteinte, réponses brutes et témoins présents
pour les 16 appels, et la règle « tout arrêt après le premier appel : aucune issue lue, pas même P-0 » (C1). La consigne n'interdit pas
d'ouvrir `lecture-pilote-v70.json` avant les contrôles. Elle ne dit pas ce qu'il faut faire d'un code de mesure non nul, d'une exception ou
d'un refus nommé (texte : « Erreur du programme de la mesure ») (C13) ; ni qu'aucun contrôle impossible ne doit être sauté en silence (R5) (C1).

**(5) Rendu.** Verdict scellé, en français, sans identifiant de modèle ni identifiant servi, sur une branche de travail désignée par la mère :
conforme. À préciser : fichier neuf au nom donné par la mère (R12) et rien d'autre d'écrit ; le contenu du verdict doit inclure la dépense, l'audit
R4, les contrôles d'arrêt et les trois phrases du point 6 (C10). « n'ouvre aucun chemin interdit (brief, section 6) » renvoie à un brief qui n'est
pas remis au lecteur (remarque facultative R1). « Le lecteur ne lance rien » est trop large si le lecteur doit sommer des coûts : le dire (C11).

**(6) Dépense : quelle voie fixer.** **Voie 1 : la dépense lui est remise calculée** par le programme du compte organisme (accord avec R-2981 :
« dépense par son programme »). Raisons : le programme ne lit que `releve-pilote-v70.json` (`depense_usd`, `appels[]` : `proposeur`, `appele`,
`etat`, `cout_usd`) et `journal-relais-<proposeur>.jsonl` (`cout_usd`, `au_dessus_du_pire_cas`), ne lit **pas** la configuration ni les prix
(les coûts sont déjà ceux de la commande, aux prix de la configuration), et ne touche jamais à l'issue : il garde l'aveugle du compte
organisme. Ce que le programme reçoit **de la mère** et que le lecteur ne peut pas vérifier : prix horaire de la machine, heures de création et
de destruction (destruction : 13:01:11Z selon R-2981), éventuels `--autre` (épreuve des clés 0,001164 USD, machines des tentatives précédentes).
Il fixe π1 = max(relevé, journal) de `fable52` + `opus55`, π2 = `argon` + `astra` + machine + autres, contre 20 et 21,72 USD, et sort avec le code
3 si une part ou une ligne est dépassée ; il écrit sa sortie en mode exclusif (`x`). La consigne doit donc : nommer la sortie JSON remise
(non nommée aujourd'hui), citer l'empreinte du programme, dire d'où viennent les arguments, faire recouper à la lecture directe les quatre sommes
du relevé et des journaux, et corriger « (même dossier) » : le programme est dans
`…/lecture-depense-pilote-v14-compte-organisme/`, qui n'est **pas** le dossier de la consigne dans cette copie (C5). Un rejeu par le lecteur
n'ajouterait que la machine et les « autres », qu'il ne peut vérifier ; il est facultatif.

**(7) Symétrie R4.** Le texte gèle des déclencheurs chiffrés (`audit_R4` de la sortie : « x = 0 » et « x ≥ 3 ») et un contenu d'audit précis ;
la consigne les remplace par « trop propre dans un sens ou dans l'autre » (C4). Manques : lire `audit_R4` ; lister les contrôles (cartes
refusées, au-delà de six, non évaluables ; trois cartes par appel tirées au hasard avec une graine dérivée de l'empreinte de `CARTES.json`, que le
texte ne définit pas : il faut la fixer, R9 ; pour x ≥ 3 : cartes qui portent, absence de description de la famille ou d'une condition dans les
pièces servies, isolement) ; dire que l'audit commente sans changer l'issue ; dire qui le fait (le lecteur, neuf, remplit la condition du texte).
Les pièces servies gelées (épisodes, gabarit) ne sont pas dans `retour/` : le contrôle « les épisodes servis contiennent les traits » ne peut
se faire que si la mère les remet ; sinon il est écrit « non fait » (voir points pour la mère).

**(8) Identifiants de modèle, empreintes.** Aucun identifiant de modèle dans la consigne (recherche des motifs de modèles : aucun résultat) ;
empreintes citées exactes (texte, programme). Rapport de ce contre-lecteur : lettres A, B, C seulement.

## Corrections exigées (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois, vérifié par `grep -cF`)

Majeures.

**C1 (arrêts, point 4 de la vérification).**
ancien : `## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)`
→ nouveau :
```
## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)

0. **Arrêts (« Liste d'arrêt »), avant toute ouverture de `lecture-pilote-v70.json` et de `remis-au-sous-agent/sortie-lire-non-ouverte.txt`**
   (ces deux pièces s'ouvrent en dernier, après les points 0 et 1). Il lit à la racine de la copie : `etat.txt` (`etape=fini`, aucun
   `arret (A)`, `noeud, machine gardee` ni `sortie inattendue` ; fichiers exclus au balayage : aucun nécessaire) ; `code-06-generer.txt`,
   `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-10-mesurer.txt`, `code-10-lire.txt`, `code-11-rapatrier.txt` : tous
   à 0 (un code 3 vaut arrêt) ; `lancements.jsonl` : une seule ligne ; `rapatrie-reel/liste-rapatriement-pilote-v70.json` : `"aucun_monde": true`
   et pas de `CARTES-partiel.json` ; relevé et manifeste complets (non partiels) ; les 16 appels ont une réponse brute et un témoin
   d'isolement scellés ; dans la dépense remise (point 4 des pièces) : aucun appel au-dessus de son pire cas, aucune part atteinte. Tout
   écart ou tout contrôle impossible : arrêt, rapport, **aucune issue lue, pas même P-0** (texte scellé, « Liste d'arrêt ») ; un contrôle qu'il
   ne peut faire est écrit « non fait » avec sa cause, jamais sauté en silence (R5).
```

**C2 (issue : P-2 contre P-2 avec réserve).**
ancien : `lue au champ `regle` de `lecture-pilote-v70.json` ;`
→ nouveau : `lue au champ `regle` de `lecture-pilote-v70.json` (`regle.issue` vaut `P-0`, `P-1` ou `P-2` ; « P-2 avec réserve » est `P-2` dont `regle.noeuds_avant_banc` n'est pas vide, chaque nœud nommé ; « P-2 » sans réserve a cette liste vide) ;`

**C3 (pièces manquantes).**
ancien : `` `engagement-mondes.json`. ``
→ nouveau : `` `engagement-mondes.json`, `etat.txt`, `lancements.jsonl`, `code-06-generer.txt`, `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-11-rapatrier.txt`, `secret-sha256.txt`, `phrase-sha256.txt`, `rapatrie-reel/liste-rapatriement-pilote-v70.json`, `rapatrie-reel/journal-relais-fable52.jsonl`, `…-opus55.jsonl`, `…-argon.jsonl`, `…-astra.jsonl` (point 4 du plan), et les dossiers `rapatrie-reel/monde-N/PROPOSEUR/` (réponses brutes, corps des relais, témoins d'isolement : lus pour leurs empreintes, leur présence et l'audit du point 7, jamais recopiés). Les journaux, les `code-*.txt` et `etat.txt` sont à la racine de la copie. `rapatrie-blanc/` (essai à blanc, proposeurs factices) ne sert pas à l'issue et n'est jamais confondu avec `rapatrie-reel/`. `` (À adapter par A si un de ces noms change ; tous existent aujourd'hui dans `retour/`.)

**C4 (audit de symétrie R4 tel que le texte le gèle).**
ancien : `7. **Audit de symétrie (R4)** : un résultat trop propre, dans un sens ou dans l'autre, reçoit le même audit et une réserve.`
→ nouveau :
```
7. **Audit de symétrie (R4)**, tel que le texte le gèle : il lit `audit_R4` de la sortie de la mesure. « déclenché : x = 0 » : il relit toutes
   les cartes refusées au gardien, au-delà de six ou non évaluables, et 3 cartes par appel tirées au hasard (graine : `SeedSequence` de
   l'entier des 16 premiers octets, gros-boutiste, de sha256 de `CARTES.json` ; tirage sans remise, toutes les cartes si l'appel en a au plus 3),
   vérifie que les épisodes servis contiennent les traits et que les témoins disent le gabarit servi. « déclenché : x ≥ 3 » : il relit les cartes
   qui portent, vérifie qu'aucune pièce servie ne décrit la famille ou une condition et l'isolement (témoins), relit aussi les cartes refusées et
   non évaluables. « non déclenché » : aucun audit. L'audit ne change pas l'issue, il la commente (réserve écrite) ; un contrôle qui exige une
   pièce non remise est écrit « non fait ».
```
(La formule de la graine est ma proposition : le texte dit seulement « dérivée de l'empreinte de `CARTES.json` » ; A la confirme ou la remplace, R9.)

**C5 (dépense : voie 1, programme, arguments).**
ancien : `4. **La dépense** calculée par `depense_pilote_v14_v1.py` (même dossier), pour le point 4 du plan.`
→ nouveau : `4. **La dépense**, calculée par le compte organisme avec `depense_pilote_v14_v1.py` (empreinte `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, dossier `…/lecture-depense-pilote-v14-compte-organisme/` de la branche `lot/compte-organisme-v1`, copié par la mère avec la copie de sortie) : le programme ne lit que `releve-pilote-v70.json` et `journal-relais-*.jsonl`. Le lecteur reçoit sa **sortie JSON scellée** (nom donné par la mère) et les arguments `--machine` (prix horaire, heures de création et de destruction) et `--autre` tels que la mère les a donnés ; il les rapporte sans pouvoir les vérifier. Il vérifie l'empreinte du programme et recoupe lui-même, par lecture, les sommes du relevé et des journaux. Les prix de la configuration ne sont pas remis (le programme ne les lit pas) ; il ne recalcule aucun coût.`
et, au point 4 du plan,
ancien : `(relevé, journaux des relais, prix de la configuration)`
→ nouveau : `(`depense_usd` et coûts des appels du relevé, somme des `cout_usd` des journaux des relais, parts de 12, 8, 9,36 et 9,36 USD ; π1 contre 20 USD, π2 contre 21,72 USD ; un code 3 du programme ou une part dépassée est déjà un arrêt du point 0)`

Mineures.

**C6** (comparaison des mondes et du programme).
ancien : `` `programme_sha256` de `mesure-pilote-v70.json` égal à ``
→ nouveau : `` `programme_sha256` de `mesure-pilote-v70.json` et `hors_corps.script_sha256` de la sortie de mesure égaux à ``
et ancien : `` égales à `S1` à `S4` ``
→ nouveau : `` égales à `S1` à `S4` (la liste `mondes_sha256` de la sortie de mesure est triée : comparer comme ensemble) ``

**C7** (compagnons, texte, secret et phrase).
ancien : `1. **Empreintes** : chaque pièce égale à son compagnon ;`
→ nouveau : `1. **Empreintes** : chaque pièce qui a un compagnon égale à son compagnon (les journaux, `etat.txt`, `lancements.jsonl` et `remis-au-sous-agent/` n'en ont pas) ; le texte scellé lu égal à `8aa33014…` ; `secret-sha256.txt`, `phrase-sha256.txt` et `engagement-mondes.json` égaux aux empreintes du secret, de la phrase, de `H` et de `S1` à `S4` du registre (A dit si `phrase-sha256.txt` est de même nature que l'empreinte inscrite) ;`

**C8** (champ des modules).
ancien : `liste `modules_importes` de la sortie comparée`
→ nouveau : `liste `hors_corps.modules_importes` de la sortie de mesure comparée`

**C10** (rendu).
ancien : `sur une branche de travail désignée par la mère : issue`
→ nouveau : `sur une branche de travail désignée par la mère, dans un fichier neuf au nom donné par elle (R12), rien d'autre n'étant écrit : issue`
et ancien : `écarts, nœuds de Lazar appelés.`
→ nouveau : `écarts, dépense rapprochée, contrôles d'arrêt, audit R4 (déclenché ou non, fait ou non fait), les trois phrases du point 6, nœuds de Lazar appelés.`

**C11** (périmètre de « ne lance rien »).
ancien : `Le lecteur ne lance rien, ne dépense rien,`
→ nouveau : `Le lecteur ne lance ni la mesure, ni le pilote, ni aucun programme qui écrit hors de son fichier de verdict (il lit et additionne les pièces remises), ne dépense rien,`

**C12** (taux d'erreur du point 6, chiffrés).
ancien : `les taux d'erreur du texte.`
→ nouveau : `les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu » : course refusée à tort 0,20 si p vaut 0,02 ; permise à tort 0,26 si p vaut 0,051 ; mêmes taux à 12 et 14 appels répondus) et, si l'issue est P-2, la phrase « Une issue P-2 favorable ne dit pas que les proposeurs « ne voient pas » les conditionnelles ».`

**C13** (mesure en échec).
ancien : `faite une seule fois sur la machine (code 0 attendu) ; il ne la refait pas.`
→ nouveau : `faite une seule fois sur la machine (code 0 attendu : `code-10-mesurer.txt`, `journal-10-mesurer.txt`) ; il ne la refait pas ; code non nul, exception ou refus nommé : arrêt (« Liste d'arrêt », erreur du programme de la mesure), aucune issue lue.`

(C9 supprimée à la rédaction, intégrée à C3.)

## Remarques facultatives (aucune n'est exigée)

- R1 : « (brief, section 6) » renvoie à un document que le lecteur ne reçoit pas ; le nommer ou le remplacer par la liste des interdits du texte.
- R2 : A confirme sur le code du lanceur les noms de champs `programme_sha256` et `cartes_sha256` de `mesure-pilote-v70.json` (non lisible par moi).
- R3 : P-1 se lit aussi sur `principale.borne_basse_non_arrondie` contre `p_max` = 0,051 (code lu) ; utile au lecteur pour « les comptes mènent bien à cette ligne ».
- R4 : si la réponse brute d'un appel porte un champ de réflexion pour `fable52` ou `opus55`, ce n'est pas un arrêt (règle « comprise ») ; seul `argon` « sans réflexion » est concerné par l'arrêt du texte ; ne pas l'étendre.

## Incidents de ma main

Aucun. Fichiers de travail dans le bloc-notes de session (copies du texte scellé, de la procédure et du programme de dépense, lectures seules).
Un `git fetch` avec refspec de `lot/compte-organisme-v1` (en plus de la branche `prep/…`), nécessaire pour lire le commit `2d35cafa` et `dbe3d24e` ;
aucune pièce de `retour/` ni de `calcul/pilote-mr2-v74-sortie-v14` ouverte ; aucune clé ; aucun calcul lourd.
