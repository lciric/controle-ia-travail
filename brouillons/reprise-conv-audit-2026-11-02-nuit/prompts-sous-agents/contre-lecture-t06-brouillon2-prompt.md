Tu es un contre-lecteur neuf (règle R2). Tu n'as écrit ni ce brouillon, ni le brouillon 1, ni P3. Rapport en français, sans sigle non développé ; toute heure vient de `date -u`. Dépôt : `/home/claude/controle-ia-travail` (lecture seule).

## Objet
Contre-lire le **préenregistrement de T0.6, organismes v0, brouillon 2** : `brouillons/T0.6-organismes-v0-v1-brouillon2.md` (vérifie son compagnon par `sha256sum -c`), et dire s'il est **scellable** (règle R1 : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt), avec les couples « ancien → nouveau » à appliquer.

## Fichiers à lire (tous dans le dépôt)
- Le brouillon 2 et ses pièces : `brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/puissance_t06_v2.py` et `puissance-t06-v2.txt` ; le brouillon 1 `brouillons/T0.6-organismes-v0-v1-brouillon1.md` et la conception `brouillons/T0.6-organismes-v0-conception-brouillon1.md` ; `brouillons/T0.7-sondes-v0-v1-brouillon4.md`.
- Décisions : `docs/decisions/proposition-P-009-T0.6-organismes-v1.md`, `proposition-P-011-T0.7-sondes-v1.md`, `proposition-P-015-T0.6-T0.8-mode-cout-v1.md`, `decision-N-007-N-008-v1.md`, `decision-N-029-v1.md` ; `docs/brief-claude-code-programme-complet-v2.md` l. 160-201 ; la ligne GO-2026-11-02-28 de `registres/go.md` ; la ligne R-1276 de `registres/decisions.md` (l. 1240).
- Code : `src/controle_ia/organismes/lora.py` et `distillation.py` ; `src/controle_ia/sondes/familles.py` et `evaluation.py` ; `src/controle_ia/harnais/episode.py` ; `prereg/P3-premier-test-i-a-v1.md` et `prereg/P3-consignes-v1.md`.
- Le préenregistrement de P3-bis en brouillon 2 (`brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon2.md`) et le rapport de reprise `brouillons/P3-bis-temoin-positif-v1/rapport-preparation-p3-bis-t06-v1.md`.

## Points à viser
L'obstacle des tâches (section 0) et DT-1 (les deux plans, leurs puissances : refais le compte des tâches, 64 d'évaluation, P3 en a pris 60, 32 de réserve) ; l'aire moyenne des plis et l'appariement des planchers ; la sonde fixée d'avance et la coïncidence déclarée ; le contrôle d'identité à dose 0 ; la lecture « diffus » renvoyée à T0.8 ; l'ordre de lecture et le témoin positif (DT-4) ; la puissance au plan (a) ; la cohérence des décisions DT-1 à DT-6 avec le texte (écrit sous leurs défauts) ; chaque chiffre renvoie-t-il à un chemin et une empreinte (R6, R7) ; gardes éprouvables sur un cas sain et un artefact (R5) ; symétrie (R4) ; aucun couperet de temps (R-1276).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch`, `checkout`, `stash` ; aucun appel de réseau ni de modèle ; `nice -n 10 python3 -I -B` pour tout calcul (tu peux rejouer `puissance_t06_v2.py` et comparer sa sortie). Tes fichiers sous `/home/claude/scratch/contre-lecture-t06/`.

## Rendu
Un rapport `/home/claude/scratch/contre-lecture-t06/contre-lecture-t06-brouillon2-v1.md` : verdict (scellable / scellable après couples / non scellable) ; bloquants, importants, mineurs, numérotés ; couples « ancien → nouveau » (texte exact, chaque « ancien » unique dans le brouillon) dans `couples-contre-lecture-t06-brouillon2-v1.json` ; ce que tu as rejoué et ses empreintes. Réponse finale : verdict, nombre de points par catégorie, chemins et sha256 du rapport et des couples.
