# Contre-lecture (brouillon 4, lecteur C) de l'addendum de relance de l'idée 1.2 — tour 3, v1

- **Pièce relue** : `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon4.md`
  (`632a897944c1c36e8c7b3e2b078e1a4e1ed8bd0489379f10391c191404ed4f55`, égale à son compagnon ; 724 lignes). Brouillon 3 :
  `2590228454cd6a7f507fd9fef7ee77e914fee34af30d66acb04e2b745b1b61a6` (égal à son compagnon).
- **Lecteur** : modèle C, neuf pour ce tour ; n'ai écrit ni la pièce ni les brouillons ni [T] ni [AE] ni le code. Rédacteur : modèle A.
- **Date** : 2026-11-16, vers 13:50Z à 13:50:09Z (`date -u`).
- **Verdict : « scellable »** — 0 majeure, 0 mineure exigée. Remarques facultatives seulement (§ 3).

## 1. Corrections du tour 2 (rapport `…-b2-tour2-v1.md`, `7f837739…8c4db`, empreinte recalculée égale)

`diff` brouillon 3 → brouillon 4 : cinq hunks.
- **m-1** : « quatre minutes plus tard » → « quatre minutes après la seconde de ces deux sorties » : identique au « nouveau » du rapport.
- **m-2** : puce « durée » de 4.10 : texte identique au « nouveau » du rapport, caractère pour caractère (cinq processus = deux de l'idée 1.2
  + trois du jeu de l'idée 1.1, étape 0 v5 finie ; quatre pendant l'étape 0 v5 seule ; sept si le jeu de l'idée 1.1 partait avant sa fin).
  Arithmétique relue : 2+3 = 5 ; 2+2 = 4 ; 2+2+3 = 7 ; 3 × 1,25 = 3,75 et 5,5 × 1,25 ≈ 6,9 : justes.
- Reste du différentiel : en-tête (version, empreinte du brouillon 3, tête `99275f89` — commit existant, ancêtre de `main` —, heure 13:44:20Z),
  ligne « Statut et lieu » (brouillon 4), entrées « Contre-lecture 3 » et « Traitement » de la section « Contre-lecture », et liste de la
  décision (v) mise à jour (renvoi à m-2). **Rien d'autre.** Facultatifs du rapport non appliqués, déclarés comme tels.
- Compagnons du brouillon 3, du brouillon 4 et du programme d'application `…-brouillon4.py` : `sha256sum` égal ; programme relu (empreintes
  vérifiées avant, refus d'écraser, unicité des « ancien », zéro ligne au format du lanceur).

## 2. Vérifications refaites

- (2)-(3), (5)-(7) : passages non touchés par le différentiel, déjà jugés conformes aux tours 1 et 2 ; relus au passage des lignes 225-270 :
  rien de dérangé. Les autres mentions de « cinq » (l. 386, 404) sont cohérentes avec m-2.
- (4) : `grep -cE '^[0-9a-f]{64}  \S+\s*$'` = 0 sur la pièce ; `--addendum`, commande, PID, commit, borne de 24 h, contrôle des versions
  inchangés et présents.
- (8) : recherche d'identifiants de modèle : vide ; section « Contre-lecture » remplie (rapport du tour 2, son empreinte, traitement point par
  point, condition sur le journal de la mère conservée) ; empreintes citées exactes.
- Les décisions (i) à (vi) de la mère sont toujours écrites dans la pièce ; (v) est désormais plus précise.

## 3. Remarques facultatives (aucune exigée)

- La condition de m5 du brouillon 2 (journal de la mère, 02:30Z à 04:40Z, à confirmer avant la recopie sous `prereg/`) reste à lever par la mère.
- f-1 à f-5, disque « ≈ 39 Go » (`df` rend aujourd'hui une capacité bien supérieure), mise en page de lignes longues du § 5 : cosmétique.
- La tête `main` a avancé depuis 99275f89 (`df131fbd`) : sans effet, la pièce date sa lecture.

## 4. Incidents et gestes de ma main

Aucun incident. Commandes légères : `diff`, `sha256sum`, `grep`, `sed`, `git rev-parse`/`cat-file`/`merge-base`, `uptime`. Aucun fichier du run
invalide ouvert ; rien écrit dans la copie ni sous `diag/`, `runs/`, `donnees/` ; aucun appel réseau, aucune clé ; aucun processus arrêté ;
pièce non modifiée ; pas de commit.
