# Consigne du correcteur neuf de la chaîne v3 de P4-instrument — v1

Session 16, 2026-10-20 vers 23:28 UTC. Programme de contrôle de l'IA de Lazar ; dépôt de travail
`/home/user/controle-ia-travail` (lecture seule pour toi). Tu es un correcteur neuf : tu n'as écrit ni la chaîne v1 ou v2,
ni le module, ni aucune relecture ou vérification.

Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument` (ce chemin est un
lien vers le bloc-notes restauré ; garde-le tel quel dans tout ce que tu écris : les scripts le nomment).

## Ce que tu fais

1. Copie `…/chaine-v2/` vers `…/chaine-v3/` (la v2 reste intacte, R12 : on n'écrase jamais). Mêmes noms de scripts.
2. Applique **toutes les décisions** de `…/traitement-verifications-chaine-v2-P4-v1.md` (scellé `10664a97…` ; lis-le en
   entier), avec, pour chacune, son cas sain et ses artefacts dans les bancs. Les corrections détaillées sont dans les deux
   rapports qu'il traite : `…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md` et
   `…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md` (lis leurs sections « Constats » et « Texte à
   ajouter » ; la correction éprouvée de VC2-depense-01 est la fonction `proposees` de
   `…/verification-chaine-v2-depense/bancs/banc_voisines_v2.py`).
3. Remplace `RAPPORTS_NOMS` du module commun `verifications_p4_v1.py` par la liste finale de 26 noms, dans l'ordre exact
   de la section « Liste RAPPORTS_NOMS » du traitement ; adapte les bancs qui la lisent.
4. Paires du texte : écris `…/chaine-v3/paires-candidat2-chaine-v3-v1.json` à partir de
   `…/chaine-v2/paires-candidat2-chaine-v2-v1.json` : paires 2 et 9 remplacées mot pour mot (rapport « dépense »,
   « Texte à ajouter » 1 et 2) ; phrases de VC2-donnees-04 et -09 (rapport « données », « Texte à ajouter ») ; phrase de
   VC2-depense-05 si tu ajoutes la ligne à `lancement.txt` ; toute autre phrase dont la correction change la vérité.
   Essaie l'assemblage : `…/ecrire_candidat2_v1.py` avec les paires du module v3
   (`…/verification-module-v3/travail/paires-texte-module-v3-corrigees-vm3-v2.json`) et les tiennes, comme dans
   `…/chaine-v2-travail/essai-candidat2/` : `problemes` = [], aucune collision.
5. Rejoue **les sept bancs** et la **répétition jouet**, cette fois avec le **module v3** (`…/module-v3/`), sur un C
   d'essai neuf fabriqué comme dans `…/chaine-v2-travail/fabriquer_c_essai_v2.sh` (dossier de travail
   `…/chaine-v3-travail/`). Puis `verifications_p4_v1.py preuves` (journaux des bancs) et `verifications_p4_v1.py
   repetition` : code 0. Chaque journal versé est la sortie brute du banc, redirigée dans un fichier neuf.
6. Écris `…/chaine-v3/RAPPORT-CORRECTION-v1.md` (verdict ; ce qui est fait, décision par décision ; résultats des bancs ;
   réserves ; table des empreintes de tous les fichiers de `…/chaine-v3/`) et `…/chaine-v3/NOTES-CHAINE-v3.md` ;
   un sceau compagnon `.sha256` (format `sha256sum`, nom relatif) pour chaque fichier de `…/chaine-v3/`.

## Règles impératives

- Écris seulement sous `…/chaine-v3/` et `…/chaine-v3-travail/`. Ne touche ni `…/chaine-v2/`, ni `…/module-v3/`, ni aucun
  rapport, ni le dépôt de travail. Une autre vérification (« fidélité ») lit `…/chaine-v2/` en ce moment : n'y écris rien.
- Dépôt de travail : commandes git de lecture seulement, `GIT_OPTIONAL_LOCKS=0` ; pour un C d'essai, clone le dépôt local
  dans ton dossier de travail ; jamais de poussée, jamais vers `lciric/controle-ia`.
- Aucun outil de location réel (faux outils dans le PATH des bancs) ; aucune instance ; aucune dépense.
- Ne lis jamais `prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `donnees/`, ni
  `episodes-defaut.json`, ni `chemin-defaut.json`. Aucune recherche récursive dans le dépôt de travail.
- `python3 -B`, `PYTHONDONTWRITEBYTECODE=1` ; aucun `__pycache__` sous `…/chaine-v3/`. Interpréteur du module :
  `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python`.
- Aucune clé ni aucun jeton affiché (jetons factices dans les bancs) ; aucun sous-agent.
- Si une décision du traitement te paraît fausse ou dangereuse, ne l'applique pas en silence : écris-le dans le rapport
  (section « Désaccords »), applique le reste.

## Ce que tu rends

En réponse finale : le chemin du rapport, son empreinte, le verdict (« chaîne v3 conforme sur C d'essai », ou ce qui
manque), les compteurs des bancs, l'empreinte des paires, et la liste de tes désaccords éventuels.
