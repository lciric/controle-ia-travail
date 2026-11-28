# Consigne du correcteur neuf de la chaîne v4 de P4-instrument — v1

Session 16, 2026-10-21 vers 00:45 UTC (à lancer après le retour de la chaîne v3). Programme de contrôle de l'IA de Lazar ;
dépôt de travail `/home/user/controle-ia-travail` (lecture seule pour toi). Tu es un correcteur neuf : tu n'as écrit ni la
chaîne v1, v2 ou v3, ni le module, ni aucune relecture, vérification ou traitement.

Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument` (lien vers le
bloc-notes restauré ; garde-le tel quel dans tout ce que tu écris : les scripts le nomment).

## Ce que tu fais

1. Copie `…/chaine-v3/` vers `…/chaine-v4/` (la v3 reste intacte, R12). Mêmes noms de scripts.
2. Lis en entier `…/chaine-v3/RAPPORT-CORRECTION-v1.md` et `…/chaine-v3/NOTES-CHAINE-v3.md` (désaccords, réserves,
   résultats des bancs), puis applique **toutes les décisions** de `…/traitement-verification-fidelite-chaine-v2-P4-v1.md`
   (scellé `dde35f6f…` ; lis-le en entier), chacune avec son cas sain et ses artefacts dans les bancs. Les corrections
   détaillées sont dans le rapport qu'il traite : `…/verification-chaine-v2-fidelite/verification-chaine-v2-fidelite-v1.md`
   (section « Constats »). Les décisions déjà portées par la v3 (VC2-fidelite-04, -05) se vérifient, et se complètent
   seulement si la v3 ne les a pas faites en entier.
3. Remplace `RAPPORTS_NOMS` (et `RAPPORTS_CONNUS` des outils d'essai) par la liste de **27 noms**, dans l'ordre exact de
   la section « Liste `RAPPORTS_NOMS` de la chaîne v4 » du traitement ; adapte les bancs qui la lisent.
4. Paires du texte : écris `…/chaine-v4/paires-candidat2-chaine-v4-v1.json` à partir de
   `…/chaine-v3/paires-candidat2-chaine-v3-v1.json`, avec les phrases des décisions (VC2-fidelite-01 règle des rapports
   postérieurs, -03, -09, -10, -11, -12 si la phrase change) et toute autre phrase dont la correction change la vérité.
   Écris `…/ecrire_candidat2_v2.py` (copie de la v1, seule la paire CL3-10 change : « ; le texte prime. » retiré).
   Essaie l'assemblage avec les paires du module v3
   (`…/verification-module-v3/travail/paires-texte-module-v3-corrigees-vm3-v2.json`) et les tiennes, comme le fait la v3 :
   `problemes` = [], aucune collision.
5. Le tokeniseur est restauré : `…/tokeniseur/tokenizer.json` (`79e3e522…`, sceau à côté). Fais pointer le banc des
   contrôles dessus.
6. Rejoue **tous les bancs** et la **répétition jouet** (avec le sixième passage de VC2-fidelite-07 et l'artefact
   « textes absents » de VC2-fidelite-08), avec le **module v3** (`…/module-v3/`), sur un C d'essai neuf fabriqué comme le
   fait la v3 (dossier de travail `…/chaine-v4-travail/`). Puis `verifications_p4_v1.py preuves` et
   `verifications_p4_v1.py repetition` : code 0. Chaque journal versé est la sortie brute du banc, redirigée dans un
   fichier neuf. Vérifie qu'aucune fausse alerte ne sort sur `registres/go.md` et `registres/decisions.md` lus à la tête
   de `main` (`git show origin/main:…` en lecture seule).
7. Écris `…/chaine-v4/RAPPORT-CORRECTION-v1.md` (verdict ; ce qui est fait, décision par décision ; résultats des bancs ;
   réserves ; désaccords ; table des empreintes de tous les fichiers de `…/chaine-v4/`) et `…/chaine-v4/NOTES-CHAINE-v4.md` ;
   un sceau compagnon `.sha256` (format `sha256sum`, nom relatif) pour chaque fichier de `…/chaine-v4/` et pour
   `ecrire_candidat2_v2.py`.

## Règles impératives

- Écris seulement sous `…/chaine-v4/`, `…/chaine-v4-travail/` et le seul fichier `…/ecrire_candidat2_v2.py` (et son
  sceau). Ne touche ni `…/chaine-v3/`, ni `…/chaine-v2/`, ni `…/module-v3/`, ni `…/tokeniseur/`, ni aucun rapport, ni le
  dépôt de travail.
- Dépôt de travail : commandes git de lecture seulement, `GIT_OPTIONAL_LOCKS=0` ; pour un C d'essai, clone le dépôt local
  dans ton dossier de travail ; jamais de poussée, jamais vers `lciric/controle-ia`.
- Aucun outil de location réel (faux outils dans le PATH des bancs) ; aucune instance ; aucune dépense.
- Ne lis jamais `prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `donnees/`, ni
  `episodes-defaut.json`, ni `chemin-defaut.json`, pas même pour une empreinte. Aucune recherche récursive dans le dépôt
  de travail ni dans le système de fichiers.
- `python3 -B`, `PYTHONDONTWRITEBYTECODE=1` ; aucun `__pycache__` sous `…/chaine-v4/`. Interpréteur du module :
  `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python`.
- Les bancs ne laissent ni tube nommé ni lien hors de `…/chaine-v4-travail/`.
- Aucune clé ni aucun jeton affiché (jetons factices dans les bancs) ; aucun sous-agent.
- Si une décision du traitement te paraît fausse ou dangereuse, ne l'applique pas en silence : écris-le dans le rapport
  (section « Désaccords »), applique le reste.

## Ce que tu rends

En réponse finale : le chemin du rapport, son empreinte, le verdict (« chaîne v4 conforme sur C d'essai », ou ce qui
manque), les compteurs des bancs, l'empreinte des paires, l'empreinte de `ecrire_candidat2_v2.py`, et la liste de tes
désaccords éventuels.
