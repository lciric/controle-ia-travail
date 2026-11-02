Tu es un lecteur neuf (règle R2 du programme) : tu n'as écrit ni l'addendum v3 de relance de R1, ni ses brouillons, ni sa contre-lecture, ni nos deux analyses scellées, ni leurs contre-lectures, ni les concordances antérieures. Travaille en français, sans sigle non développé. Toute heure que tu écris vient de `date -u`. Lis d'abord `/home/claude/controle-ia-travail/CLAUDE.md` (règles R1 à R14).

## Ce qu'on te demande
Une **concordance** : l'addendum v3 de relance de R1 (brouillon 2, écrit par l'autre lignée, « session-depot ») produit-il exactement ce que nos deux analyses scellées et notre procédure de réception lisent, et ne change-t-il rien que nous n'ayons accepté ? Même méthode que les concordances antérieures (à lire comme modèles) :
`brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md` et `…/concordance-finale-addendum-r1-v2-scelle-v1.md`.

## Pièces (dépôt privé `/home/claude/controle-ia-travail`, tout est déjà récupéré localement : n'utilise que `git show`, `git diff`, `git ls-tree`)
- Addendum v3, **brouillon 2** : `git show origin/prep/r1-relance-v3:prereg/R1-addendum-relance-v3.md` (tête `49d29c8e`, sha256 attendu `86c68b0ec323cfdce1a6a21d1fcee14ed8d0647f485906eb031e7ee6ac32746d`) ; brouillon 1 : `git show 145da951:prereg/R1-addendum-relance-v3.md` (`382ba627…`) ; tableau et diff des corrections : `docs/notes/runs-r1-r2-r4-v1/relance-v3/corrections-apres-contre-lecture-v1.md` et `.patch` sur la même branche.
- Contre-lecture neuve du brouillon 1 : `git show origin/prep/r1-relance-v3:docs/notes/runs-r1-r2-r4-v1/relance-v3/contre-lecture-addendum-relance-v3-v1.md` (`c19fdbc7…`).
- Configuration v5 `prereg/R1-rejeu-config-v5.json` (attendu `acad6253…`, canonique `1cfb7fba…`) et table `prereg/R1-table-tokenisation-v3.json` (attendue `ead8a668…`), scripts `scripts/r1_relance_instance_v3.sh`, `scripts/amorce_instance_r1_relance_v3.sh`, essais `tests/test_bornes_relance_v3.py`, pré-vol `docs/notes/runs-r1-r2-r4-v1/relance-v3/prevol-relance-v3-sortie.txt` : tous sur `origin/prep/r1-relance-v3`.
- Addendum v2 scellé (parent) : `git show c2a8b6e1:prereg/R1-addendum-relance-v2.md`.
- Nos analyses scellées : principale `git show 83ce7a91:prereg/analyse-principale-r1-r2-v1.md` (`8e267952…`) ; secondaire `git show 7a238666:prereg/analyse-blanche-noire-v3.md` (`1f6a6da2…`). Si un commit de leur code cité par les concordances antérieures n'est pas présent localement, ne le récupère pas : dis-le et travaille sur les textes.
- Notre procédure de réception : `brouillons/preuves-mentors-v1/reception-r1-relance-v1/procedure-reception-lecture-r1-relance-v1.md` (et le script `ecrire_fiches_reception_v1.py`, ses essais) ; verdict du rejeu à graine (table v3) : `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md`.
- Le message n° 295 de session-depot qui te transmet le texte : `/home/claude/lectures/session-depot_2026-11-02_n295.md` (§ 1).

## Points à traiter en plus de la concordance d'ensemble
1. Le paragraphe « où atterrissent les renvois de l'addendum v2 » (lignes 152 à 170 du brouillon 2) : chaque renvoi atterrit-il bien ?
2. Une part de G10 (brouillon 1 de la v2, l. 118 : essai au nom hérité `test_relance_regle_b_non_resolus_fidele_faux_et_seuil`, dans `CIBLES`) est déclarée non couverte, nom et docstring inchangés : est-ce suffisant, ou faut-il renommer (commit de code neuf) ? Recommande, avec ta raison.
3. La réserve E16 (`tokenisation.addendum` vaut encore `prereg/R1-addendum-relance-v2.md`) : tient-elle, et que doit vérifier notre fiche de réception ?
4. Le nœud N-A et toute ligne gelée de nos analyses que la relance pourrait contredire (voir la première concordance).

## Interdits
Aucun `git fetch`, `checkout`, `stash` ni rien qui change l'arbre ou l'index ; n'ouvre aucun fichier sous `diag/`, `runs/` ni `donnees/`, aucune branche `calcul/…` ; aucun commit, aucun `.sha256`, aucun fichier existant modifié ; aucun appel de réseau ni de modèle ; `nice -n 10` pour tout calcul (la machine a deux cœurs et une course décisive y tourne : reste sobre, n'exécute pas de suites d'essais lourdes).

## Rendu
Un seul fichier neuf : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v3-brouillon2-v1.md`, dont la première ligne en gras est le verdict (« concordant », « concordant si … (C-1 à C-n) », ou « écart de fond : nœud de Lazar … »), puis « En bref » (une ligne par point), puis le détail avec, pour chaque affirmation, le fichier, la ligne et l'empreinte vérifiée. Ta réponse finale : le verdict, les changements demandés une ligne chacun, le sha256 du fichier.
