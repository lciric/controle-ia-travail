# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14), v4 — tour 2 de la v3 — v1

Contre-lecteur neuf (R2), modèle C ; auteur de la pièce : modèle A. Rapport écrit le 2026-11-16T14:36Z (`date -u`).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v4.md`, empreinte
`de826db5953ec86123ffca204c5b0c488098043298d5b15bc39563025781f8e4` (égale à son compagnon). Version précédente : v3,
`f06f46b31944f88b62ea2de08b8b95d06ce92fd906b52e2856c10479942034c8` (recalculée, égale). Rapport du tour 1 de la v3 : recalculé
`27269e9275f2fb094c5e4b4f88e182974d96a1bb49f3485426af94797253af4c`, égal.

## Verdict : corrections

Aucune majeure ; une seule correction mineure (provenance de l'application, section « Contre-lecture »). Les trois corrections du tour
précédent sont appliquées fidèlement, le différentiel ne contient rien d'autre que ce qui est déclaré. Si la session mère confirme que
le rédacteur de la v4 était bien du modèle C, la correction tombe et la pièce est scellable telle quelle.

## A. Corrections du tour précédent (`diff` v3 → v4, lu en entier)

Le différentiel comporte : titre (v3 → v4) ; ligne 3 (version, heure `14:33:58Z`, antérieure à ce rapport ; v3, v2, v1 citées avec leurs
préfixes exacts) ; trois lignes de corrections ; une sous-section ajoutée « Tour 1 de la v3 ». Rien d'autre.
- m1 (point 6, « tous les taux d'erreur … dont : ») : mot pour mot.
- m2 (point 0, `journal_au_dessus_du_pire_cas` à 0 ; parts strictement inférieures ; machine strictement sous 3 USD) : mot pour mot. Champ
  `journal_au_dessus_du_pire_cas`, comparaison `<=` de `sous_la_part` et `MACHINE = 3.0` relus sur `depense_pilote_v14_v1.py`
  (commit `dbe3d24e`, empreinte recalculée `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, égale) : exact.
- m3 (point 7, version de `numpy` et indices tirés écrits au rapport) : mot pour mot.
- Programme d'application `appliquer-…-v4.py` : empreinte égale à son compagnon (`0da3c518…`) ; vérifie les empreintes de la v3 et du
  rapport, l'unicité de chaque « ancien », refuse d'écraser. Empreinte citée du rapport du tour 1 exacte.
- F1 à F3 non appliquées, comme permis.

## B. Vérifications (1) à (8) rejouées sur les passages touchés

(1) Les contrôles d'empreinte du point 0 restent conformes au texte scellé ; m2 y ajoute des conditions plus strictes que la lettre
(« atteignant sa part → arrêt » du texte scellé = strictement inférieur : cohérent). (2) Noms de pièces : `find … -printf '%s %P\n'` sur
`retour/` ; présents : `etat.txt`, `lancements.jsonl`, `engagement-mondes.json`, `secret-sha256.txt`, `phrase-sha256.txt`, `code-11-rapatrier.txt`,
`code-08-blanc.txt`, `rapatrie-reel/` (manifeste, relevé, `CARTES.json`, lecture, mesure, sortie de mesure, liste de rapatriement, quatre
journaux de relais, `monde-1` à `monde-4`) ; je n'ai rien ouvert. Les nouveaux passages ne nomment aucune pièce nouvelle. (3) Inchangé.
(4) Le point 0 précède toujours la lecture de l'issue ; écart = arrêt avant issue ; « non fait » jamais silencieux (R5). (5) Inchangé.
(6) Voie 1 inchangée (dépense remise calculée par le programme du compte organisme, qui ne lit que `releve-pilote-v70.json` et
`journal-relais-*.jsonl` ; code 3 si une part, π1 ou π2 est dépassée). (7) m3 rend le tirage rejouable ; aucun ajout au texte scellé.
(8) Aucun identifiant de modèle (lettres A, B, C seulement) ; empreintes citées toutes vérifiées.

## Correction exigée (chaque « ancien » figure une seule fois dans la v4, vérifié par comptage)

### Mineure

**m1 (sous-section « Tour 1 de la v3 », puce « Application » : modèle du rédacteur).** La puce dit que les corrections du tour 1 de la v3 ont
été appliquées par « un rédacteur neuf (modèle C) ». Or le programme `appliquer-…-v4.py` reprend ce texte tel quel du gabarit de la v1 → v2
(où « modèle C » était exact), alors que les corrections de la v3 → v4 sont écrites par le modèle A (comme celles du tour 2 de la v2, puce
« modèle A » du même fichier). Une provenance fausse dans une pièce scellée est à éviter, surtout quand elle vise l'indépendance du rédacteur.
ancien : `par un rédacteur neuf (modèle C), qui n'a écrit ni la consigne`
→ nouveau : `par un rédacteur neuf (modèle A), qui n'a écrit ni la consigne`
Remarque : « n'a écrit ni la consigne » reste faux au sens strict si le rédacteur est le modèle A qui l'a écrite ; le plus fidèle est donc, si
la mère confirme A : `par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme` à la place du
segment `par un rédacteur neuf (modèle C), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme` (même ligne, une seule
occurrence), comme la v3 l'a fait pour le tour 2. Si la mère confirme que le rédacteur était C et neuf, aucune correction.

## Remarques facultatives

- F1 à F3 du rapport précédent restent applicables (pas exigées).

## Points pour la mère

1. Dire qui a réellement appliqué la v3 → v4 (modèle A ou C) ; sinon la puce est invérifiable de mon côté.
2. Aucun écart au texte scellé, aucune dépense, aucun mot du directeur nécessaire.
3. Inchangés du tour précédent : tolérance des clés de proposeurs `fable52`/`opus55` dans les noms de fichiers ; donner au lecteur la version
   de `numpy` (au moins 1.25) ; produire et sceller la sortie du programme de dépense (`--machine`, `--autre`) avant remise, code 3 dit.

## Incidents de ma main

Aucun. Un fichier de travail dans le bloc-notes de session (copie du programme de dépense, lecture seule) ; un `git fetch` avec refspec ;
aucune pièce de `retour/` ni de la branche de sortie ouverte (noms et tailles) ; aucune clé ; aucun calcul lourd.
