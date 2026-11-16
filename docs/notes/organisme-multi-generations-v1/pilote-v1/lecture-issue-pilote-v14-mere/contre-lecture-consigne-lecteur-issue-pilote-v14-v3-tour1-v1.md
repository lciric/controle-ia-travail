# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14), v3 — tour 1 — v1

Contre-lecteur neuf (R2), modèle C ; auteur de la pièce : modèle A. Début 2026-11-16T14:24Z ; fin 2026-11-16T14:32Z (`date -u`).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v3.md`, empreinte
`f06f46b31944f88b62ea2de08b8b95d06ce92fd906b52e2856c10479942034c8` (égale à son compagnon). Version précédente : v2,
`0e12acbd6ea72bf2318c809d13be20382b6e6864041ce0e20a56365425c8e30b` (recalculée, égale). Rapport du tour 2 de la v2 : recalculé
`8c020f418de840403f666c501bdf05e07e1e57cef0b0735421bef89675fe5293`, égal.

## Verdict : corrections

Aucune majeure ; trois corrections mineures, toutes de précision. Les corrections du tour précédent sont appliquées fidèlement. La
conception tient : « a_refaire » n'est pas justifié.

## Lu / non lu

Lus : la v3 en entier ; `diff` v2 → v3 ; le rapport du tour 2 ; le texte scellé du pilote (branche `prep/pilote-mr2-compte-organisme-v1`,
empreinte recalculée `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, égale), en entier pour « Prédiction chiffrée »,
« Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Audit de symétrie (R4) », « Liste d'arrêt » et le bloc gelé ;
la procédure v14 (commit `2d35cafa`), sections 5, 8, 9, 11 ; le programme de dépense (commit `dbe3d24e`, empreinte recalculée
`9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, égale) ; le registre des inscriptions ; la ligne R-2981. Pour les
noms de champs : les pièces de la répétition locale versées au commit `lot/compte-organisme-v1` (hors issue réelle). De `retour/` :
**noms et tailles seulement** (`find … -printf '%s %P\n'`) ; aucune pièce de `retour/` ni de la branche de sortie ouverte ; aucun
`pytest` ; aucune clé ; seul appel réseau : deux `git fetch` avec refspec.

## A. Les corrections du tour 2 sont-elles appliquées ?

`diff` v2 → v3 : tout le différentiel est lu. Oui, fidèlement :

| correction | état dans la v3 |
|---|---|
| M1 (a) phrase | présente, mot pour mot |
| M1 (b) graine | présente, avec trois précisions déclarées (un seul générateur ; indices à partir de 0 ; aucun tirage si k ≤ 3) ; elles ne contredisent pas le texte scellé, qui ne dit que « graine dérivée de l'empreinte de `CARTES.json` » ; pas un écart |
| M1 (c) deux « points ouverts » | levés, avec l'adaptation « rédacteur des corrections (modèle A) » déclarée |
| M1 (d) puce du tour 2 | présente ; empreinte du rapport exacte (`8c020f41…`) |
| M2 ordre de lecture de la sortie de mesure | présente, mot pour mot |
| m1 à m7 | présentes (m3 : « `arret` vide, `null` » et « `appels_complets_illisibles` à 0 » adaptés au type du champ, déclaré ; vérifié sur le relevé de la répétition : `partiel` faux, `arret` null, `appels_complets_illisibles` 0) |
| F1 à F5 | non appliquées, comme permis |

Ajouts hors couples : la ligne 3 (version) et la sous-section « Tour 2 », avouées ; références exactes.

## B. Vérifications (1) à (8)

**(1)** Les points 0 à 7 appliquent « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Audit de symétrie (R4) » et
« Liste d'arrêt », dans l'ordre du plan (empreintes, mesure, issue, coûts, exclusions, rapport ; arrêts en tête, audit en fin). Empreintes
citées toutes exactes : texte `8aa33014…`, programme de la mesure `676d5f37…` (texte scellé, « Métrique »), programme de dépense
`9866e611…`, rapport du tour 2. Contrôles cités : `fichier_mondes_sha256` et empreintes de mondes dans le manifeste
(`controles.mondes`), `programme_sha256` et `cartes_sha256` de la pièce de liaison, `hors_corps.script_sha256` et
`hors_corps.modules_importes` de la sortie de mesure (S-c), `corps.mondes_sha256` triée : tous présents et exacts. Une réserve de
retranchement : le point 6 (voir m1).

**(2)** Tous les noms de pièces cités existent dans `retour/` : à la racine `etat.txt` (468), `lancements.jsonl` (158), les sept
`code-*.txt` (2 chacun), `journal-09-reel.txt` (399), `journal-10-mesurer.txt` (686), `engagement-mondes.json` (497),
`secret-sha256.txt` (79), `phrase-sha256.txt` (87) ; sous `rapatrie-reel/` : lecture, sortie de mesure, pièce de liaison, manifeste,
relevé, `CARTES.json`, liste de rapatriement, les quatre `journal-relais-*.jsonl`, leurs compagnons là où il y en a ;
`remis-au-sous-agent/sortie-lire-non-ouverte.txt` (204). Dossiers `monde-1` à `monde-4` : 4 proposeurs chacun, 16 `reponse-brute.json`, 16
`temoin-isolement.json`, 16 `corps-relais.json`, chacun avec son compagnon ; aucun `CARTES-partiel.json` ; `journal-09-reel-2` absent
(mention conditionnelle correcte). Rien d'interdit n'est remis : mondes, secret et phrase en clair, `prive/` et branche d'entrée sont
exclus ; les réponses brutes ne sont remises que lues pour empreintes, présence et audit, jamais recopiées (R-2731, qui vise `main`).
Aucune pièce nécessaire ne manque : le programme de dépense ne lit ni la configuration ni les prix (voir (6)).

**(3)** Lecture de l'issue au champ `regle` de `lecture-pilote-v70.json`, première ligne de la table qui s'applique ; distinction P-2 /
P-2 avec réserve par `regle.noeuds_avant_banc` (vérifiée sur la répétition) ; nœuds et « ce qui suit » mot pour mot. Conforme.

**(4)** Le point 0 précède l'ouverture de la lecture et de la sortie de `lire` ; la sortie de mesure n'est ouverte avant que pour
`hors_corps` et `corps.mondes_sha256` ; tout écart d'empreinte arrête avant toute issue lue (point 1) ; un contrôle impossible aux points
0 à 2 est un arrêt écrit « non fait » (R5), au point 7 seulement « non fait » sans arrêt ; conditions mécaniques. Une imprécision
(m2).

**(5)** Rendu conforme : verdict scellé, français, sans identifiant de modèle ni identifiant servi (R-2731), sur une branche désignée par la
mère, fichier neuf au nom donné par elle (R12), rien d'autre d'écrit ; contenu demandé complet ; interdits explicités.

**(6)** **Voie 1 : la dépense est remise calculée par le programme du compte organisme**, le lecteur recoupant lui-même par lecture les
sommes du relevé et des journaux. La consigne la fixe, nomme le programme et son empreinte exacte, et dit ce qu'il lit : seulement
`releve-pilote-v70.json` et `journal-relais-*.jsonl` (confirmé sur le code : ni lecture, ni sortie de mesure, ni pièce de liaison, ni
configuration, ni prix). Arguments `--machine` et `--autre` donnés par la mère, rapportés sans vérification possible ; code de sortie 3 et
part de la machine (3 USD, comprise dans 21,72) bien dits et exacts (`MACHINE = 3.0`, code 3 si une part, π1 ou π2 est dépassée). Conforme à
R-2981. Voir m2 pour deux champs du programme que le point 0 devrait nommer.

**(7)** Symétrie R4 telle que le texte la gèle : déclencheurs x = 0 et x ≥ 3 repris ; l'audit commente, ne change pas l'issue ; champ
`corps.audit_R4` absent si P-0 ; graine complète (voir m3 pour la version de `numpy`). Les cartes de `CARTES.json` sont une liste plate
(`monde`, `proposeur`), compatible avec « toutes celles que `CARTES.json` lui attribue, dans l'ordre où il les liste ». Réserve, non
exigée : voir « Remarques ».

**(8)** Aucun identifiant de modèle dans la consigne ; seuls les noms de fichiers `journal-relais-fable52.jsonl` et `…-opus55.jsonl`
(clés de proposeurs du texte scellé, qui dit n'avoir aucun identifiant de modèle hors du bloc gelé et nommer les proposeurs par leur clé) ;
voir points pour la mère. Empreintes citées vérifiées.

## Corrections exigées (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans la v3, vérifié par comptage)

### Mineures

**m1 (point 6 : liste de taux présentée comme exhaustive alors que le texte dit « les taux d'erreur ci-dessus »).** Le texte gèle toute la
section (aussi 0,075 ; 0,10 ; les taux à 12 et 14 appels à 0,075 ; la ligne « entre 0,03 et 0,05, le pilote ne décide rien de fiable ») ; la
parenthèse de la consigne n'en cite qu'une partie et se lit comme complète.
ancien : `les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu » : course refusée`
→ nouveau : `tous les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu », dont : course refusée`

**m2 (point 0 : « aucune part atteinte » et « aucun appel au-dessus de son pire cas » sans les champs qui les portent ; le programme juge
`≤` la part, le texte dit « atteignant sa part → arrêt »).**
ancien : `aucun appel au-dessus de son pire cas, aucune part atteinte. Tout`
→ nouveau : `aucun appel au-dessus de son pire cas (`journal_au_dessus_du_pire_cas` à 0 pour chaque proposeur) et aucune part atteinte (le coût du relevé et celui des journaux de chaque proposeur strictement inférieurs à sa part, même si `sous_la_part` est vrai ; la machine, de même, strictement sous 3 USD). Tout`

**m3 (point 7 : tirage non reproductible d'une version de `numpy` à l'autre).** Le flux de `Generator.choice` sans remise n'est pas garanti stable
entre versions ; le bloc gelé du texte fixe d'ailleurs une version précise de `numpy` pour la machine. Le lecteur doit écrire ce qu'il
a employé, pour que la mère puisse rejouer.
ancien : `sans `numpy` (version 1.25 au moins), le tirage est écrit « non fait », avec sa cause),`
→ nouveau : `sans `numpy` (version 1.25 au moins), le tirage est écrit « non fait », avec sa cause ; la version de `numpy` employée et, pour chaque appel, les indices tirés sont écrits au rapport, pour que la mère puisse rejouer le tirage),`

## Remarques facultatives (aucune n'est exigée)

- F1 : au point 7, dire où le lecteur trouve de quoi vérifier « les épisodes servis contiennent les traits » et « les témoins disent le
  gabarit servi » : le manifeste porte seulement des empreintes (`controles.textes_servis.N.sha256`, `episodes_sha256`, `controles.gabarit_sha256`),
  et les textes servis sont dans `prive/`, jamais rapatriés. Si `corps-relais.json` ne porte pas le texte servi, ce contrôle sera « non
  fait » (c'est prévu par la consigne) ; la mère peut le dire d'avance.
- F2 : le champ `couts` de `lecture-pilote-v70.json` (coût par appel) pourrait être rapporté à côté de la sortie du programme de dépense.
- F3 : le texte « tour 1 » de la section « Contre-lecture » dit que les corrections du tour 1 ont été appliquées par un rédacteur du
  modèle C, alors que celles du tour 2 le sont par le modèle A ; à rectifier si inexact (sans effet sur le lecteur).

## Points pour la mère

1. Aucun écart au texte scellé, aucune dépense, aucun mot du directeur nécessaire ; la graine du tirage est une précision, non un écart.
2. **Noms de fichiers `fable52` et `opus55`** : clés de proposeurs du texte scellé, jamais des identifiants servis ; mais le lecteur les
   verra et pourrait les recopier dans son verdict (R-2731 vise les identifiants servis) : à toi de dire si c'est toléré.
3. **Remise au lecteur** : donner aussi, dans la consigne de lancement, la version de `numpy` disponible (au moins 1.25) ; sans `numpy`,
   le tirage est « non fait ». Ne pas ouvrir toi-même la sortie de mesure avant la fin des points 0 et 1.
4. La sortie du programme de dépense doit être produite par toi (arguments `--machine` : prix, heures de création et de destruction
   — destruction à 13:01:11Z selon R-2981 — et `--autre` pour l'épreuve des clés) et scellée avant remise ; le code de sortie 3 est à
   donner au lecteur.
5. Rectifier si besoin la mention « modèle C » de la puce « Application » du tour 1 (F3).

## Incidents de ma main

Aucun. Un fichier de travail dans le bloc-notes de session (copies du texte scellé, de la procédure et du programme de dépense, lectures
seules) ; deux `git fetch` avec refspec (`prep/pilote-mr2-compte-organisme-v1`, `lot/compte-organisme-v1`) ; aucune pièce de `retour/`
ni de la branche de sortie ouverte (noms et tailles) ; aucune clé ; aucun calcul lourd. Une commande mal formée de ma main (échec sans
effet) lors de la lecture des pièces de la répétition locale, sans écriture.
