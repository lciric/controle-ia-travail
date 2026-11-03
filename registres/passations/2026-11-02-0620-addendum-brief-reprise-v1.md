# Addendum au brief de reprise — ce matin, piste A (organisme d'idéation, Kirchner) — 2 novembre 2026, 06:17 UTC (heure relevée par `date -u`)

Complète `registres/passations/2026-11-02-0605-brief-reprise-conv-audit-nouvelle-instance.md` (qui prime pour tout le reste). **Mot de Lazar, 07:15 Paris : « go »** sur les quatre manques du § 6.1 du brief : ils passent dans les choses à faire **ce matin** par l'instance neuve (registre R-1115). Ce « go » porte sur les tâches ; chaque lancement payant cite encore un devis et une ligne de `registres/go.md` (règle gelée) : présente les devis **en un seul bloc** dans ton premier message à Lazar, puis avance sur son mot.

## Les quatre tâches, dans l'ordre (échéance de la candidature : 11:59 UTC ; un résultat ne se cite que sur verdict « confirmé » d'un lecteur neuf)

### A1 — Résistance à un proposeur modèle de langage qui optimise contre le juge (courbe de Goodhart)
- Un sous-agent de l'ancienne session écrivait le brouillon 1 (prompt § 6.7 du brief). **S'il est dans `main` du dépôt public** (commit « Attaque de Goodhart : brouillon 1 », fichiers `orchestrator/prereg/preenregistrement-attaque-goodhart-v1-brouillon1.md`, `pole/attaque_goodhart_v1.py`, `demonstrations/attaque_goodhart_v1.py`, `essais/test_attaque_goodhart_v1.py`, `orchestrator/prereg/rapport-redaction-attaque-goodhart-v1.md`), reprends à la contre-lecture ; sinon relance le prompt tel quel.
- Puis : contre-lecture neuve (liste de fichiers explicite) → brouillon 2 par voie B → devis (appels, USD, durée) → GO de Lazar → scellement, commit du texte **avant** la course → course chez session-depot (clés) sur demande par le canal, GO cité → sortie scellée avant lecture → lecteur neuf (R13) → rangée du README public (empreinte dans `MANIFEST.md`) → phrase pour Kirchner si « confirmé ».
- Ordre de grandeur du coût : quelques USD (le second tour réel du 1er novembre : 62 appels, 1,47 USD) ; le devis exact vient du sous-agent.

### A2 — La boucle fermée pour de vrai (tests de mort dans le vrai bac à sable, sélection lue par la génération suivante)
- Code d'abord (processeur, gratuit) : fermer la flèche ouverte (README § 2, étape 9 ; `pole/course2_v57.py`, `pole/etage_entre_generations_v57.py`, `pole/tests_de_mort_v5.py`) : la génération suivante **lit** la sélection scellée ; le lanceur `demonstrations/ideation_v8.py` et le tour `ideation_v2.py` appellent l'étage v5 (plus le v56) ; essais de bout en bout et banc de mutations sur l'étage neuf (chaque mutant tué pour la raison attendue) ; version nouvelle (`_v58` ou suivant), jamais d'écrasement.
- Bac à sable : installer `bwrap` (bubblewrap) sur la machine qui jouera (ou sur l'instance de session-depot) ; jouer **à blanc** l'étage v5 dans le vrai bac à sable avec des cartes scriptées (sans réseau) ; consigner le journal.
- Préenregistrement **d'un tour fermé sur un monde à loi plantée** (vérité connue hors du système) : proposeurs réels (Kimi et Argon), gardien, juge (nul v8), tests de mort exécutés pour de vrai, vérificateur d'une autre famille, sélection ; prédictions : la loi vraie plantée survit, les fausses sont éliminées, taux d'« inconclusif » ≤ seuil ; audit de symétrie ; liste d'arrêt ; contre-lecture ; devis ; GO ; course ; R13.
- Ensuite seulement : le même tour sur une **vraie question** (celle du 1er novembre) — c'est A3.

### A3 — Au moins une hypothèse réelle promue, puis vérifiée par exécution sur des données tenues à l'écart
- C'est l'issue, non garantie, du tour fermé de A2 joué sur la vraie question : une hypothèse promue par le juge **et** survivante d'un test de mort exécuté sur des données tenues à l'écart est un résultat ; **zéro promotion est aussi un résultat et se rapporte tel quel** (aucun run visant un signe, R3). Préenregistre les deux issues, et la façon de dire chacune au mentor.
- Données tenues à l'écart : réservées **avant** la course, par empreinte, dans le préenregistrement ; jamais vues par les proposeurs ni par le juge.

### A4 — Proposeur de référence : taux de fausses découvertes de toute la chaîne
- Deux bras de référence dans le **même** préenregistrement que A2 (pas de texte séparé) : un proposeur **aléatoire** scripté (processeur, gratuit) et un proposeur **qui recopie ou mélange des lois déjà promues** (celui que le nul v8 a appris à refuser), passés par toute la chaîne (gardien, juge, tests de mort, vérificateur). Mesure : part de cartes promues puis survivantes sous chaque bras, avec intervalle de Wilson ; c'est le **taux de fausses découvertes de la chaîne**, à mettre en face du bras réel.
- Lecture écrite d'avance : si le bras aléatoire promeut autant que le bras réel, la chaîne ne discrimine pas (ce serait une réserve majeure pour A3).

## Enchaînement du matin (heures UTC, indicatives)
07:30 routine, n° 344, bloc de décisions et de devis à Lazar (N1, N-A, N2, GO relance R1 + extension GO-13, GO A1, GO A2-A4) · 07:45 A1 contre-lecture ; A2 code en parallèle (sous-agent distinct) · 09:00 A1 scellée, course si GO · 09:30 préenregistrement A2-A4 brouillon 1 · 10:30 A1 R13 · 11:30 dernière mise à jour des réponses aux mentors (v15 si un fichier change) · 11:59 échéance · après : A2-A4 course et verdicts, puis A3 sur la vraie question.

## Rappels
Aucun résultat cité sans verdict « confirmé » ; aucun lancement payant sans GO cité ; sous-agents neufs pour contre-lecture et verdict ; piste B (programme de contrôle) continue en parallèle selon le brief § 7 (relance de R1 sur mot de Lazar ; préenregistrement « lecture par épisode » § 7.8, gratuit, à lancer dès la reprise).
