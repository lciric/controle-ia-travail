# Rapport de rédaction — préenregistrement « R2 seul », brouillon 1 (v1)

- Rédacteur : sous-agent (Claude, Opus 5.5), **auteur de l'analyse principale de R1-R2 et de son code** (donc non neuf à leur égard) ; commandé par conv-audit le 2026-11-02 vers 01:40 UTC ; écrit entre 01:41 et ≈ 02:00 UTC.
- Préparé seulement : rien de scellé, rien de lancé ; ne sert que si Lazar choisit l'option (c) du nœud R-1103. Aucune donnée de R1 ni de R2 ; aucun `git fetch` ; aucune branche `calcul/…` ; aucun commit ; aucune empreinte compagnon ; aucun fichier existant modifié.

## Ce que j'ai écrit (fichiers neufs)

- `brouillons/preuves-mentors-v1/analyse-r2-seul-v1/preenregistrement-analyse-r2-seul-v1-brouillon1.md`.
- Code, modules neufs (`_v3`) dans `src/controle_ia/analyse_principale_r1_r2/` :
  - `constantes_v3.py` : bras, comparaisons, contrôle, motifs, commande du rejeu, clés de graines, entropie ;
  - `entrees_v3.py` : fiche `fiche-reception-r2-seul-v1` et preuve de l'arrêt de R1 (`verifier_arret_r1`) ;
  - `lecture_v3.py` : gardes, `calculer_r2` (réutilise `lecture_v1._lecture_ensemble` et `calcul_v1`), `issue_r2`, rendu, commande.
- Essais : `tests/test_analyse_r2_seul_v1.py` (10).
- Fréquence sous le nul : `frequence-nul-analyse-r2-seul-v1.py` et sa sortie.

## Ce que j'ai fixé

- Écarts au fournisseur, déclarés :
  - E1 : lire R2 malgré « rien n'est lu », sur le mot de Lazar ;
  - E2 : éligible = notée (fidélité impossible sans R1) ;
  - E3 : famille J3s − G et J3s − T, Bonferroni sur deux, 97,5 % ; secondaires J8s − G et J8s − T ;
  - E4 : contrôles au seuil de J3s ;
  - E5 : plancher, diagnostics, contexte exact et P-R1, P-R3, P-R4 tombent avec W ;
  - E6 : « trop beau » et « nettement inférieur » adaptés au juge.
- Hypothèses H-S1 (le juge contre G) et H-S2 (le juge contre T), propres à ce texte. Prédictions a priori : S-1 > 0 faible, confiance 0,55 ; S-2 < 0, confiance 0,70 ; elles sont ouvertes dans les deux sens et chaque classe a sa lecture.
- Lecture « J3s − G supérieure, mention contraire » : réserve de spécificité, sans lecture « sépare le saboteur ». C'est mon choix, le fournisseur ne prévoyant rien pour le juge.
- Graines dérivées de l'empreinte de ce texte (règle de conv-audit, Q9 de la principale). Clés « plis » et « tirages », sans plancher.
- Preuve de l'arrêt vérifiée par le code :
  - `arret.json` scellé et rattaché au manifeste d'un rejeu, avec la commande, les textes et l'identité cités ;
  - le verdict donne le motif déclaré ;
  - aucune sortie de rejeu pour ce run.

## Ce que je n'ai pas pu fixer (nœuds ou points à confirmer)

- Le texte entier est un nœud : il n'existe que sur le mot de Lazar.
- La contre-lecture et le lecteur de concordance doivent être neufs à l'égard de **deux** textes de ce rédacteur (la principale et celui-ci).
- `FETCH_HEAD` attendu `d19ffd56…`, selon le n° 247. Ce n'est vérifiable qu'à la récupération ; un autre commit doit être consigné.
- Le nombre d'anomalies du juge 8B n'est pas donné par le n° 247 : il sera lu par le code (`anomalie`).

## Essais et mesures

- 10 essais réussis pour le mode R2 seul. Avec les essais v1 (20) et v2 (4) de l'analyse principale : 34 réussis en 28 s (`nice -n 10`).
- Fréquence sous le nul global (200 répliques) :
  - au moins une classe non nulle parmi J3s − G et J3s − T : 4/200 = 0,020 (Wilson [0,008 ; 0,050]) ;
  - taux réalisés moyens à 1 % : de 0,0104 à 0,0134.
- Durée de la lecture réelle : moins d'une minute (aucune activation, cinq régressions de T).
