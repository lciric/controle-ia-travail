# Couche 1 bis — lecture exploratoire P3 (ii) sur la banque T0.5 complète (sans `e2`), en simulation d'agents — v1

Lignée conv-audit (instance du 27 octobre 2026 ; session servie par Opus 5.5), écrit à partir de 20:32 UTC (heure lue sur
`date -u` : 20:31:32). **Exploratoire (R-546), zéro dépense** : agents simulés, juge et banque réels. Code : v7 version 17
(`orchestrateur-pole-v7/`, constructeur `exemples/construire_banque_t05_v3.py`, lecture `demonstrations/demo_couche1bis_v7.py`).
Lecture fixée avant les courses dans le script (L1, L2, L3) ; les deux bras du second jeu ont été ajoutés après le
premier jeu (dit ici).

## Verdict

1. **Validité tenue (L1)** : aucun témoin faux promu, sur 4 courses (témoins par permutation dans la tâche, par bruit, et
   plantés sur le bruit).
2. **Le juge a des dents au régime de cette banque, à condition de lire toute l'épreuve d'un coup (L2)** : des effets
   plantés sur les traits réels sont promus jusqu'à la force 0,5 avec 96 épisodes d'épreuve par fiche (4 sur 4), mais
   seulement à la force 2 avec 32 épisodes par fiche (2 sur 2 à la force 2, 0 sur 1 à la force 1) — la découpe en trois
   tranches (une par génération, exigée depuis la v11 pour l'héritage) divise la puissance par trois sur une banque de
   cette taille.
3. **Rien sur les 13 moniteurs réels (L3)** : aucune loi des quatre traits du texte (longueur, actions valides, dispersion
   des jetons par action, bruit) ne prédit les notes des juges au-delà de la marginale : le chercheur mécanique ne trouve
   rien qui passe sa pénalité sur 48 épisodes de développement ; ses 12 meilleures lois sans filtre sont toutes éliminées
   sur 96 épisodes d'épreuve (log W maximal 0,53, contre log 20 = 3,0) ; la confirmation croisée n'établit **aucun**
   témoin vrai réel. Lu dans les deux sens (R4) : le pôle voit des structures plantées de force ≥ 0,5 à 96 épisodes ;
   l'absence sur les moniteurs réels dit qu'il n'y a pas, dans ces quatre traits et sous ces formes, de relation de cette
   force ; elle ne dit rien d'autres traits, d'autres formes, ni d'effets plus faibles.

## Données

- Pilote T0.5 (`diag/20261012-105125-t05-pilote-reel`, 60 tâches, 120 épisodes notés `e0`/`e1`) + banque complète de la
  couche 1 bis (b) (`donnees/t05-banque-complete-v1`, commit `93d5d5c8`, run `20261027-153857-t05-pilote-reel`, 36 tâches,
  72 épisodes notés ; `e2` pas encore noté). Empreintes des sources dans chaque banque (`sources`). Aucune tâche commune.
- Banque v3 : 192 épisodes, 96 tâches ; parties **par tâche** : calibrage 24 tâches (48 épisodes), développement 24 (48),
  épreuve 48 (96) ; 13 moniteurs réels (8B : 7 rubriques ; 3B : 6) ; 4 moniteurs **plantés** sur les traits réels
  (loi à seuil non linéaire : `si z_j > 0` softmax en `+a·z_i`, sinon en `−a·z_i` ; le prédicteur connu, linéaire, ne la
  capture pas ; la loi n'est pas écrite dans la banque, seulement dans les témoins).
- Témoins : vrais établis par confirmation croisée (ajustés sur 12 tâches de développement, confirmés sur les 12 autres
  à log 20) : **0** (ni réels ni plantés : 24 + 24 épisodes ne suffisent pas) ; vrais plantés : 4 ; faux : 8 par
  permutation dans la tâche (meilleures candidates sans filtre), 17 sur le bruit, 4 plantés sur le bruit.

## Courses

| jeu | banque (forces plantées) | générations × épisodes d'épreuve par fiche | population | nul | L1 faux promus | L2 vrais plantés promus | L3 réelles promues |
|---|---|---|---|---|---|---|---|
| 1 | 2, 1, 2, 1 | 3 × 32 (tranches) | 6 lois aléatoires au gabarit + proposeur mécanique | informé | 0 / 3 | 2 / 3 servis (forces 2, 2 ; force 1 éliminée) | 0 (course arrêtée après la génération 0 : le proposeur n'a rien proposé) |
| 1 | idem | idem | idem | aveugle | 0 / 3 | idem | 0 |
| 2 | 2, 1,5, 1, 0,5 | 1 × 96 | 12 meilleures lois du mécanique sur le développement, **sans** filtre de pénalité | informé | 0 / 4 | **4 / 4** (log W max 6,4 à 44,9) | 0 (log W max des 12 : 0,53) |
| 2 | idem | idem | idem | aveugle | 0 / 4 | 4 / 4 | 0 |

Lectures scellées : `lecture-couche1bis-v3-course-{informe,aveugle}.json` (jeu 1), `lecture-couche1bis-v3b-course1-{informe,aveugle}.json`
(jeu 2) ; banques et témoins à côté. **Audit de propreté (R4)** : les deux bras « informé » et « aveugle » donnent des
richesses identiques à 10⁻³ près pour les 20 fiches du jeu 2 ; vérifié : la bibliothèque diffère (4 membres avec le
prédicteur connu, 3 sans), mais le prédicteur connu (ajusté sur 48 épisodes de calibrage) n'est jamais le meilleur membre
sur l'épreuve — il fait moins bien que la marginale ajustée, ce qui va dans le sens de L3 (pas de relation trait → note).

## Ce que cela change

- **Pour la porte de la couche 1** (« le pôle retrouve seul le connu », N-029) : sur cette banque, il n'y a pas de connu
  à retrouver dans les quatre traits du texte (aucun témoin établissable, aucune loi qui batte la marginale). La porte ne
  peut être jugée que sur des **témoins plantés** (tenue : jusqu'à la force 0,5 à 96 épisodes) ou sur des traits plus
  riches (traits du texte de N-029 : à verser dans la banque).
- **Pour la conception** : sur une banque de cette taille, une seule génération lisant toute l'épreuve vaut mieux que
  trois tranches (puissance ×3 en log W) ; l'héritage ne rattrape rien quand le proposeur ne repropose pas la même loi.
  La règle d'arrêt « plus aucune fiche ne survit » a coupé le jeu 1 après la génération 0 parce que le proposeur
  mécanique, filtré par la pénalité de Schwarz à 48 épisodes, n'a rien proposé : à 48 épisodes, la pénalité (environ
  0,5 · p · log 48, soit 12 à 35 nats selon la forme) écrase tout effet réaliste ; laisser le juge décider (population
  sans filtre, jeu 2) est le bon réglage pour une petite banque.
- **`e2`** (60 + 36 épisodes de plus quand le module complémentaire aura tourné) : 288 épisodes, 144 en épreuve ; à
  refaire alors, avec les mêmes témoins plantés (forces 2, 1,5, 1, 0,5, 0,25).

## Limites

Agents simulés (le proposeur réel n'est pas mesuré ici) ; quatre traits seulement ; formes du gabarit (softmax, par
sous-population, si/sinon à 0, sur un ou deux traits) ; lois plantées écrites par moi (non linéaires, de forme que le
gabarit connaît) ; une seule graine ; exploratoire, rien de décisif.
