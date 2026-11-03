Tu es un relecteur neuf : tu n'as écrit ni les deux pages publiques, ni les verdicts qu'elles résument, ni la candidature. Français pour ton rapport. Heures par `date -u`. Lis `/home/claude/controle-ia-travail/CLAUDE.md`.

## Objet
Deux pages publiques nouvelles, non committées, dans `/home/claude/ideation-organism/resultats/` : `controle-p3-premier-test/` (README et `pieces/`) et `controle-simulation-defenses/` (README et `pieces/`), écrites d'après le rapport `/home/claude/scratch/pages-publiques/rapport-pages-publiques-v1.md`. Modèle de forme : `resultats/controle-r1-blanche-noire/README.md`.

## Ce que tu vérifies
1. **Exactitude** : chaque chiffre, intervalle, date, empreinte et phrase de résultat de chaque page contre la source scellée du dépôt privé `/home/claude/controle-ia-travail` (P3 : `docs/verdicts/verdict-P3-premier-test-i-a-v2.md`, `diag/20261020-075740-p3-lecture/lecture-p3.json`, `prereg/P3-premier-test-i-a-v1.md` et addenda ; T0.3 : `diag/20261004-080257-t03/bloc-P8.json`, `lecture.md` du même run, `docs/notes/resultats-T0.3-v1.md`, préenregistrement T0.3). Rien d'ajouté au verdict, réserves toutes portées, « What this does not show » complet.
2. **Publication** : aucun chemin `donnees/`, aucun chemin de bloc-notes `/tmp/…`, aucun identifiant de tâche ou d'item (identifiants arXiv des 60 tâches compris), aucune clé, aucun nom de machine, aucune décision verbatim du directeur (section 7 du README public), rien des bras tenus à l'écart. Vérifie chaque fichier de `pieces/` ligne par ligne (`grep` sur `donnees/`, `/tmp/`, `arxiv`, `sk-`, `ghp_`, `AKIA`, `@`, `/home/`).
3. **Compagnons** : chaque `.sha256` de `pieces/` égal à l'empreinte du fichier et à celle de l'original privé.
4. **Deux lignes proposées pour le README principal** (rapport, section 4) : exactes ? Et la ligne 130 du README principal date la simulation du 1er novembre : dis quelle correction datée il faut, sans la faire.
5. Les deux phrases anglaises proposées pour la candidature (rapport, fin) : exactes contre les pages ?

## Rendu
Fichier neuf `/home/claude/scratch/pages-publiques/relecture-pages-publiques-v1.md` : verdict en trois lignes (publiable tel quel / après corrections listées / non publiable), puis les constats une ligne chacun avec fichier et ligne. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien lu sous `donnees/`, aucun appel réseau ni modèle, `nice -n 10` ; n'ouvre pas `resultats/banc-tricheurs-v9-validation-v1/`. Réponse finale : verdict et constats.
