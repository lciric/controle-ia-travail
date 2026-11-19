# Journal du rédacteur du brouillon 6 de relance du préenregistrement du papier C — v2 (suite)

Suite de `journal-redacteur-v1.md` (`9328432d…`, intact). Même rédacteur (Claude Fable 5.2), même mandat. Heures UTC
relevées par `date -u`, le 2026-11-19. Aucun écrit hors de `bloc-notes/redacteur/`. Dépôt intact (`git status` vide).
Aucun refus de permission. Aucune dépense, aucun appel à un modèle, aucun autre agent, aucune suite d'essais.
Aucune pièce existante écrasée (R12) : les programmes de construction refusent d'écrire sur une sortie présente.

## Déroulé
- 11:43 — message de la session de conduite : 17 remarques de la contre-lecture complète. Rapport lu en entier,
  empreinte recalculée conforme (`9a7121bc52890f6e761227ac916f72078b41086bbce7d29bf6ef44a33dc186a0`).
- 11:44 à 11:46 — N-026 lue (section 1, `85bd4023…`) ; N-023, ligne 11, relue pour les figures ; programmes de
  simulation du contre-lecteur lus (en-tête et sortie de U3, scénarios de U1).
- 11:46 à 11:55 — rejeu de la grille en arrière-plan (voir ci-dessous) ; pendant ce temps, 35 remplacements de la
  version c1 écrits, liste des décisions v2, table de traitement.
- 11:55 à 11:58 — version c1 construite (aucun échec d'ancre), validateur, note v2, ce journal.

## Rejeu de la grille (CL-09)
- Programmes : copies des fichiers de `bloc-notes/contre-lecteur/outils/rejeu/` (eux-mêmes ceux de l'archive, seul le
  chemin de la configuration y est changé par le contre-lecteur ; seules les longueurs de la configuration brouillon 3
  de l'archive y sont lues) : `commun_b5_v1.py`, `commun_cb6_v1.py`, `t1_loi_nette_rejeu_v1.py`,
  `t2_rang_temoins_partages_v1.py`, `u1_rang_vrai_reechantillonnage_v1.py`, `u3_lecture_rho_sur_r_v1.py` ; empreintes :
  `travail/rejeu-grille-c1/sha256sums-programmes-v1.txt`. Aucune ligne de ces programmes n'est modifiée par moi.
- Lanceur : `travail/rejeu-grille-c1/lancer_grille_v1.sh`. 24 cases : scénarios N0 à N5 × k = 3, 5 × 45, 60 tâches ;
  1 000 essais × 1 000 tirages ; graine 20261021 (dérivée par `numpy.random.SeedSequence` dans le programme). Quatre
  processus à la fois, environ 9 minutes. Sorties : `travail/rejeu-grille-c1/sorties/`, manifeste
  `sha256sums-sorties-v1.txt`. Fichiers `.err` tous vides.
- Contrôle : ma sortie de la case N5, k = 5, 60 tâches est identique, hors ligne d'en-tête (durée), à celle du
  contre-lecteur.
- Lecture : aux trois lectures jointes, au plus 0,043 (C-P3a) et 0,054 (C-P3b), pour un seuil de clause de 0,064 à
  1 000 essais ; aux deux premières lectures seules, jusqu'à 0,149 et 0,150 (scénario du mélange à g = 0,20).
- Limites : données simulées seulement ; C-P3c non simulée ; g = 0,20 seulement sous le mélange ; un rejeu par le
  rédacteur ne tient pas lieu du rapport neutre que la clause exige (verrou 10).

## Pièces neuves
- `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c1.md`
- `table-traitement-contre-lecture-brouillon6-relance-v1.md`
- `decisions-du-directeur-exigees-v2.md`
- `note-differences-brouillon5-brouillon6-relance-v2.md`
- `problemes-brouillon6-relance-c1-v1.txt`
- `travail/changements_c1_v1.py`, `travail/construire_brouillon6_relance_c1_v1.py` et son journal,
  `travail/ecrire_note_v2.py`, `travail/rejeu-grille-c1/`.

## Doutes de cette suite
1. CL-03 : j'ai tranché la confirmation niveau par niveau comme une question de méthode. Si la session mère y voit une
   lecture de l'énoncé, elle se range sous D-2 ou D-15.
2. CL-02 : la lecture complète de la sonde porte l'effet de longueur de l'agrégation dans le sens favorable ; exiger e
   et e_c durcit la ligne sans la rendre neutre. Je l'ai écrit au texte.
3. CL-04 : tolérance du témoin de l'instrument (1 % de l'écart saboteur moins honnête, sur 99 % des contenus) choisie
   sans mesure ; harnais non lu (verrou 9).
4. CL-10 : la transposition du banc est de ma conception ; avec 30 à 60 négatifs, un « taux de faux positifs de 1 % »
   se réduit au maximum des négatifs. Banc et licence non vérifiés.
5. D-9 : je garde le défaut « trois lectures » alors que la lettre de la décision appliquée retire déjà le verdict de
   deux statistiques. La session mère peut préférer en faire un nœud.
6. Le texte fait maintenant sept cases « À REMPLIR » et environ 168 000 octets.
7. Le rapport dit « 7 mineures » en tête de section et en liste six (CL-12 à CL-17) ; j'ai traité les dix-sept
   remarques numérotées.
