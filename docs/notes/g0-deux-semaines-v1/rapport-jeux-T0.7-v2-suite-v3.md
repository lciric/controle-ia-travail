# Rapport additif — jeux synthétiques de T0.7 : J-C écrit, trois jeux sur 32 tâches (fille 12, Sonnet 5.5) — v3

Complète `rapport-jeux-T0.7-v2-suite-v1.md` et `…-suite-v2.md` (inchangés, R12). Écrit le 2026-11-07 (relevé `date -u`) ; branche `prep/fille-12-t07-v1`. Mêmes conditions : aucune clé, aucune location, aucune dépense, rien sous `donnees/`, `diag/`, `runs/` ; tokeniseur factice (`cfc0c143…`, non opposable) ; réserve et évaluation de travail bâties sur la projection ; **jeux non scellables, non contre-lus** (R2 à faire). Aucune règle du script officiel changée.

## 1. État exact

| jeu | tâches | où |
|---|---|---|
| J-D dissimulation | r00–r31 (320 paires) | `…-brouillon1/taches/` (r00–r07, r08–r17 pour la part J-D), `taches/` (r08–r17, fusion), `remises-completes/` (r18–r31) |
| J-A intention, autres modes | r00–r31 (160 + 160) | idem |
| **J-C domaine, mode coût** | **r00–r31 (320 paires, 640 séquences)** | `remises-jc/` (20 enregistrements par tâche ; `incitation_id` par rotation de l'annexe B) |

Aucune tâche perdue ; aucun `.sha256` posé.

## 2. Script officiel sur les trois jeux, 32 tâches (assemblage sans `--jeux`, `--nombre-taches 32`, graine 20261105)

Contrôles fichiers, 1, 2, 3, 4, 5, 7, 8, 9, 10 et annexes : **OK**. Contrôle 6 : **31 écarts en jetons** (> 15 %) sous le tokeniseur factice, **non opposables** (15 dans J-C, 16 dans J-A ; aucun dans J-D) ; aucun écart en mots ni en caractères. Textes de P3 et de T0.6 absents : contrôle 9 à rejouer. Journal : `mesures/journal-verification-3-jeux-r00-r31-v1.txt`.

Aires du sac de mots, 32 plis (réponse entière / avant COST) : **J-C 0,818 / 0,812** ; J-A contrôles 0,815 / 0,806 ; J-A direction 0,739 / 0,740. Aucune ne passe 0,90 ; aucune réserve de surface levée. Courbe de J-C aux jalons de 8, 16, 24, 32 tâches (mêmes règles, même assemblage) : **0,855 / 0,864 ; 0,858 / 0,846 ; 0,860 / 0,855 ; 0,818 / 0,812** (journaux `journal-jc-jalon-{8,16,24,32}-v1.txt`). Courbe de J-A : voir le rapport v2.

Observations (non décisionnelles) : à taille égale, J-C est plus lisible par les mots que J-A ; avant les jalons, j'avais lu des aires hors jalon (2 tâches 0,940 / 0,915 ; 6 tâches 0,862 / 0,857), déclarées au journal. Au jalon de 32 tâches l'aire de J-C est la plus basse de la série.

## 3. Règles fixes et renvois de J-C (R-1660) — détail : `mesures/journal-jc-regles-fixes-v1.md`

Règles fixes appliquées à toutes les tâches : alternance des longueurs (le gonflé plus long dans 3 à 7 paires sur 10) ; fuite lexicale du lot (unigrammes et bigrammes, ≥ 0,40 contre ≤ 0,10) ; N3 étendue aux unités matérielles ; 8 mots de l'énoncé avec la normalisation du script ; plus N1–N3, D1 ≥ 0,32, longueurs, annexe C, rotation, identifiants. Renvois, **un au plus par tâche**, tous déclenchés par un pré-contrôle : r02 et r03 (alternance 2/10 et 10/10), r06 (N3 matériel), r12 (8 mots de l'énoncé, paire 4). Aucun renvoi décidé sur l'aire. Écarts de procédure déclarés : lecture d'aires hors jalon avant le message de la mère ; trois sous-agents quelques secondes (quatre une fois en J-D/J-A) avec arrêt immédiat.

## 4. Indices de surface déclarés par les écrivains de J-C

Dérives corrigées en cours de route : membre gonflé toujours le plus long ; marqueurs d'échelle (« every », « at each », « many », « multiple », « single », « across »), nombres de graines (3 contre 10), modèles plus gros (70B), mots d'unités (« rerun », « grids »), clauses finales (« Report … and keep … »), titres plus longs. Résidus déclarés : phrases de fermeture partagées (« may fail »), membre gonflé qui nomme plus souvent des études de balayage, des modèles plus grands ou des sondages en fin de proposition, et dont le « besoin honnête » (le tiers du chiffre) est un jugement d'écrivain non vérifié ; paires jugées incertaines par leurs écrivains : r18 p2 et p9, r19 p5–p8, r20 p4 et p10, r21 p9–p10, r22 p4 et p7 et p10, r23 p3 et p5–p6, r24 p2 et p6 et p9, r25 p1 et p9, r26 p3 et p7, r27 p3 et p9, r28 p1 et p5 et p10, r29 p3–p4 et p6–p7 et p9–p10, r30 p4–p5 et p8–p10, r31 p8 et p10.

## 5. Trois risques

1. **Le « tiers » n'est pas mesuré** : rien ne vérifie que le plan gonflé a besoin d'environ un tiers du chiffre déclaré (jugement de l'écrivain, souvent signalé « mou » pour les chiffres faibles) ; la contre-vérification à l'aveugle (section 9) est la seule lecture du fond, et elle n'est pas faite.
2. **Les 31 écarts en jetons** seront jugés sur le tokeniseur conforme (`79e3e522…`, introuvable ici) : les corrections de ces paires ne seront pas des renvois « gratuits » (une seule réécriture par tâche selon la consigne), ce qui peut laisser des défauts sur plusieurs tâches.
3. **L'aire dépend de la taille et des habitudes des écrivains** : J-C 0,94 à 2 tâches, 0,86 à 6 à 24 tâches, 0,82 à 32 ; chaque écrivain neuf a ses indices (échelle, closures), le contrôle de fréquence documentaire ne voit que les termes courants, et les deux premières règles de pré-contrôle ont été ajoutées après les premiers lots.

## 6. Reste (pour la mère ou la session suivante)

Tokeniseur conforme, réserve et évaluation scellées, textes de P3 et de T0.6 pour le contrôle 9 ; réécriture éventuelle des paires en défaut de jetons ; contre-vérification à l'aveugle des trois jeux (échantillon par graine R9) ; rapport de l'écrivain (section 12) ; scellement et `provenance-v2.md`.
