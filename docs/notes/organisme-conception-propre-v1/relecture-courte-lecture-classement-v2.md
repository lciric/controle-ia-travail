# Relecture courte — outil du lecteur et programme de classement, v2 — course « conception propre »

Même contre-lecteur que la v1 (modèle B, autre que l'auteur), sous-agent de la session mère ; 14 novembre 2026, de 00:37 à
00:43 UTC (heures relevées par `date -u`). Lu : le dossier `lecture-classement-v2/` (outil `a58fb8b9…`, classement
`2cb65f33…`, essais `f91318a9…`, banc `aa2393f0…`, rapport `fefa2bd5…` ; toutes les empreintes égalent leurs
compagnons), le différentiel entier v1 → v2 des deux programmes, la ligne R-2630, et, pour les formats, le code du lanceur
(`ecrire_scelle`, manifeste de fin). **Aucun fichier de `runs/course-ideation-conception-propre-v1/` ouvert, aucune fiche
lue, aucun modèle, aucune clé, rien sous `src/` ni `tests/`.** Essais joués sous une racine factice, dans un dossier
temporaire hors du dépôt, retiré.

## Verdict : « utilisable », sous une condition d'emploi (C1)

M1, M2 et M3 sont tenus ; κ est exact ; la variante est inerte sans décision ; je ne trouve aucun changement non dit qui
touche la règle. Une réserve ancienne, que ma première lecture n'avait pas relevée, reste ouverte (r1) : d'où C1.

## Ce qui est vérifié

- **M1 tenu.** `e`, `+`, `.`, `de`, `levier:juge`, un passage de 19 caractères hors espaces : refusés ; 20 : accepté ;
  des lettres espacées ne trompent pas le compte. Occupation C7 : refusée avec `C7`, `2026`, le nom de la conception, la
  cellule de la source, le mécanisme de C2, ou un passage de fiche court ; acceptée avec 60 caractères du mécanisme de C7,
  avec ou sans marques de gras. Les douze lignes du catalogue ont bien quatre colonnes (la cellule 2 est le mécanisme).
  Passages courts et passages de plus de 200 caractères comptés au JSON et au résumé.
- **M2 tenu.** Sur ma sonde de la v1 (36 fiches factices, lot 1 de la lecture 2 illisible) : « E2 : lecture illisible ou
  incomplète (L2 lot 1 : reponse_illisible) ; 15 fiche(s) réelle(s) et 4 témoin(s) touchés ; aucune idée désignée », cité
  aussi au résumé. Même issue pour un JSON coupé au milieu et pour une seule entrée manquante. Cas sain : deux désignées,
  comme en v1.
- **M3 tenu.** Refusés : liste à la forme de la quarantaine, autre nom de fichier, fichier hors du dossier de run, run
  atteint par un lien symbolique, pile sans fiche réelle admissible (avant tout envoi). Un chemin avec `..` est ramené au
  chemin réel et accepté seulement s'il est le bon. Formats confrontés au code du lanceur : nom du run, `code`,
  `pour_l_attestation.fiches_validees_sha256`, forme du compagnon : égaux. Le classement revérifie la provenance. Il lit
  donc, en plus de la copie des fiches, `manifeste-lanceur-fin.json` du run (bilan du lanceur : aucune note du juge) :
  écart à la lettre de C5, dit au rapport, sans objet pour le § 4.8.
- **κ en fractions exactes.** Table 2 × 2 (2, 0, 3, 5) sur 10 fiches : κ = 2/5 ; le calcul flottant de la v1 rendait
  0,3999999999999999 (L4 manquait à tort : défaut réel, confirmé) ; la v2 rend 0,4 et « tient ». Accord brut de 4/5 exact à
  marge constante : tient. Seuil de E5 en fraction.
- **Variante inerte.** Sans `--decision`, ou avec une décision mal formée : refus avant toute lecture des envois. Par
  défaut (`L5`), `designer_detachee` n'est pas appelée (un seul appel dans le code, sous la branche de la variante) ;
  `variante_detachee` vaut `null`, aucun autre champ de la sortie n'en porte la trace. Avec décision : même paire que la
  règle dans le cas sain ; aucune désignation sous lecture incomplète.
- **Rien d'autre n'a changé sans être dit**, à ces détails près, sans effet sur la règle : `kappa_accord` refuse des listes
  vides ; `lecture-verifiee` garde le texte des passages rendus (`passage_rendu`) ; le compte « au-delà de 200 » ne
  couvre que R1 à R7, pas les deux passages de N.

## Essais et mutations

- Essais de l'auteur rejoués à 00:37 UTC : **80 passés**.
- Mes six sondes de la v1, adaptées à la racine factice, plus κ exact, provenance (7 formes), anomalies (4 formes),
  variante (5 formes) : résultats ci-dessus.
- Mutations, 00:39 à 00:43 UTC : mes **22 de la v1 rejouées sur le code v2 : 22 tuées** (les 9 survivantes de la v1
  comprises) ; **16 neuves sur les corrections : 15 tuées, 1 survivante** — le dossier `copies` non exigé dans le chemin
  (sans conséquence : le nom du fichier, la profondeur du chemin et l'empreinte du manifeste de fin gardent). Total : 37
  sur 38.

## Réserves

- **r1 (moyenne, ancienne) — une entrée à laquelle il manque une clé de critère n'est pas une anomalie.** Sonde : un lot
  dont toutes les entrées sont rendues sans `N` ni `R7` → aucune anomalie, aucun compte, lecture « complète ». R manquant
  compte 0 (contre la fiche) ; **N manquant compte `aucune`** (pour la nouveauté) : si l'autre lecture dit `aucune`, la
  fiche est « neuve » sur une seule opinion. La trace existe (valeur brute nulle, motifs « valeur hors {0, 1} » et « valeur
  de N illisible » dans `lecture-verifiee`), mais rien ne la porte au verdict.
  **C1 (condition d'emploi)** : avant de lire le verdict, la mère compte dans les deux `lecture-verifiee-L*-v2.json` les
  critères à valeur brute nulle hors anomalie bloquante ; s'il y en a sur une fiche réelle ou sur un témoin, la lecture est
  dite incomplète et rien n'est désigné. Mieux : une version qui en fait une cinquième anomalie bloquante.
- **r2** — `--decision` n'est vérifiée que dans sa forme (`R-` ou `N-` et des chiffres) : c'est la mère qui garantit
  que la ligne existe au registre et précède le lancement du classement.
- **r3** — restent telles que dites : aveugle par la forme du fond non mesuré (m1 de la v1) ; seuil de 20 caractères et
  cellule du mécanisme seule, plus sévères (taux de « non prouvé » du lecteur inconnu, L1 peut manquer si le lecteur cite
  le nom) ; programmes sans vérification de leur propre empreinte ; nœud A1 à Lazar.
