Tu es un lecteur neuf (règle R2 du programme) : tu n'as écrit ni le texte du complément de validation du rejeu à graine, ni notre brouillon 2 de ce texte, ni sa contre-lecture, ni l'addendum v2 scellé. Travaille en français, sans sigle non développé. Toute heure que tu écris vient de `date -u`. Lis d'abord `/home/claude/controle-ia-travail/CLAUDE.md` (règles R1 à R14).

## Contexte
Le rejeu à graine (R1) a résolu 7 épisodes sur 7, mais sa validation n'a rejoué que 54 épisodes sur 147, coupée par un budget d'étape de 2 400 s. Le **complément de validation** rejoue les 147 avec `combinaisons_max` 272, `duree_max_episode_s` 14 400 et `duree_max_s` 259 200 (gardes seulement), même code `c2a8b6e1`, sous le GO-2026-11-02-30 (40 USD). Nous (conv-audit) avons écrit un brouillon 2 ; l'autre lignée (session-depot) l'a fusionné dans son texte, l'a fait contre-lire (« scellable après corrections », bloquant B1 sur la garde de dépense), puis l'a corrigé. Avant le scellement, il faut **notre concordance** : le texte corrigé dit-il ce que notre brouillon 2 disait, et chaque différence est-elle déclarée et acceptable ?

## Pièces (dépôt privé `/home/claude/controle-ia-travail`, déjà récupérées : n'utilise que `git show`, `git diff`, `git ls-tree`)
- Texte corrigé : `git show origin/prep/r1-complement-v1:prereg/R1-addendum-relance-v2-complement-validation-v1.md` (tête `c5293408`, sha256 attendu `b5afc8b6e67622c04bebfee1315bb3e4602fe3e8c848d39344f8073d799e65ae`) ; texte fusionné d'avant : `git show 2764e6cc:prereg/R1-addendum-relance-v2-complement-validation-v1.md` (`3b7955f1…`) ; tableau et diff des corrections : `docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/corrections-apres-contre-lecture-v1.md` et `.patch` sur `origin/prep/r1-complement-v1`.
- Contre-lecture : `git show origin/prep/r1-complement-v1:docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/contre-lecture-complement-validation-v1.md` (`2ef1f192…`).
- Configuration de la branche : `prereg/R1-graine-config-complement-v2.json` (attendu `1b6f943c…`, canonique `70b0b771…`) ; la nôtre : `brouillons/preuves-mentors-v1/complement-validation-rejeu-v1/R1-graine-config-complement-v2.json`.
- Notre brouillon 2 : `brouillons/preuves-mentors-v1/complement-validation-rejeu-v1/R1-addendum-relance-v2-complement-validation-v1-brouillon2.md` (`41d5350e…`) et `notes-redaction-v2.md`.
- Addendum v2 scellé (parent) : `git show c2a8b6e1:prereg/R1-addendum-relance-v2.md`.
- Verdict du rejeu à graine : `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md` (`64fab1a5…`).
- Ligne GO-2026-11-02-30 de `registres/go.md` ; addendum 1 de la passation de session-depot : `git show origin/main:registres/passations/2026-11-02-2006-addendum-1.md` ; son message n° 295 : `/home/claude/lectures/session-depot_2026-11-02_n295.md` (§ 2).

## Points à traiter
1. Chacune des 17 différences listées à « Fusion » : déclarée, et compatible avec l'intention de notre brouillon 2 ? Y en a-t-il de non listées ?
2. Les gardes de dépense corrigées (deux tâches indépendantes ; destruction par identifiant à `T0 + H`, `H` = (39,5 USD − imputé − disque) / prix de l'offre − 15 min ; alerte à 30 USD) : cohérentes avec GO-30 (40 USD), avec la règle « le plafond du texte scellé égale le montant du GO » si elle s'applique ici, et avec la règle R10 (arrêt par identifiant) ? Ce qu'une destruction pendant la validation fait à la lecture est-il écrit d'avance (aucune lecture partielle opportuniste) ?
3. Les gardes R5 (cas sain et artefact) pour chaque garde nouvelle ; la prédiction P-C7 (durée, descriptive) ; le cas « Haut ».
4. Le nœud que session-depot pose à Lazar (exposition résiduelle ≈ 258 à 305 USD si les deux tâches échouent) : décris-le sans le trancher ; dis seulement si le texte l'écrit honnêtement.

## Interdits
Aucun `git fetch`, `checkout`, `stash` ni rien qui change l'arbre ou l'index ; n'ouvre aucun fichier sous `diag/` (la branche en contient : ne les lis pas), `runs/` ni `donnees/`, aucune branche `calcul/…` ; aucun commit, aucun `.sha256`, aucun fichier existant modifié ; aucun appel de réseau ni de modèle ; `nice -n 10` (machine à deux cœurs avec une course décisive : reste sobre).

## Rendu
Un seul fichier neuf : `brouillons/preuves-mentors-v1/complement-validation-rejeu-v1/concordance-complement-validation-v1.md`, première ligne en gras = verdict (« concordant », « concordant si … (C-1 à C-n) », ou « écart de fond : nœud de Lazar … »), puis « En bref » (une ligne par point), puis le détail (fichier, ligne, empreinte vérifiée pour chaque affirmation). Ta réponse finale : verdict, changements demandés une ligne chacun, sha256 du fichier.
