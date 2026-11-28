# Brief — session Claude locale sur le poste de Lazar (LAPTOP-P0ELSG8M) : retrouver sur le disque et verser ce qui manque (v2)

Remplace la v1 (gardée intacte, R12). Ajoute les chemins exacts donnés par la mère précédente Gemini (`docs/notes/passation-v4-messages-v1/reponse-gemini-mere-precedente-v1.md`) et le canal d'échange avec la session mère dans le nuage.

Tu es une session Claude Code lancée par Lazar sur son ordinateur Windows. Ta tâche est bornée : **inventorier et verser**, rien d'autre.
- Lis d'abord `CLAUDE.md` du dépôt `lciric/controle-ia-travail` (règles R1 à R14, garde P8).
- De la routine de reprise, ne fais que les vérifications d'empreintes. Aucun calcul, aucune machine louée, **aucune suppression** : « récupérer ce qui est récupérable » d'abord. Les fichiers que Gemini dit « à supprimer » sont versés ou inventoriés ; c'est Lazar qui décide de les effacer.

## Canal d'échange avec la session mère (dans le nuage, sans accès à ton disque)
- Elle lit ta branche `versement/disque-local-20261128-v1` et le fichier `docs/notes/versement-disque-local-20261128-v1/ECHANGE-avec-la-mere-v1.md`. Écris-y tes questions ; ajoute des lignes, n'en réécris aucune. Puis pousse.
- Elle répond dans `docs/notes/passation-v4-messages-v1/ECHANGE-avec-la-session-locale-v1.md`, sur la branche `claude/happy-davinci-j4xp7t` : `git fetch origin claude/happy-davinci-j4xp7t` puis `git show origin/claude/happy-davinci-j4xp7t:<chemin>`.
- Si tu peux te relier par Remote Control, la session mère s'appelle `controle-ia-travail-a9`.

## Où chercher (chemins donnés par Gemini, à vérifier)
1. **Deux clones Windows** : `C:\Users\lciri\controle-ia-travail` et `C:\Users\lciri\OneDrive\Documents\controle-ia-travail`. Ce dernier est le dépôt principal piloté par l'interface en ligne de commande d'Antigravity ; il porte une branche locale `passation/claude-mere-v4-20261128`. Dans chacun :
   - `git worktree list --porcelain` (huit arbres de travail étaient actifs le 28 au matin) ;
   - `git status --ignored` ;
   - `git stash list` ;
   - `git log --branches --not --remotes --oneline` (commits jamais poussés).
2. **Arbres de travail d'Antigravity** : `C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\`, dont `lecture-dr` (branche du commit `42cdfcf29`) et `wt-b8-puissance` (branche du commit `5817bb0a5`). Dans chacun, `git status`, puis inventaire des fichiers non suivis.
3. **`C:\Users\lciri\Downloads\`** :
   - `gemini-code-1795778660659.md`, `kit-r2-lot1-slim.txt`, `kit-r2-lot2-slim.txt` : les pièces d'entrée de la contre-lecture R2, **à verser en priorité** ;
   - `contre-lecture-r2-etages-1-2-v1.md`, `test_oracles_r5_cloture_etages_1_2.py`, `contre-epreuve-r2-volets-11-13-v1.md`, `test_contre_epreuve_v4_r5.py`, `verif-p8-hors-depot.txt` : donne leur empreinte brute et leur empreinte sans retours chariot (`tr -d '\r' < fichier | sha256sum`), à comparer aux versions du dépôt ;
   - `ancrages-depot-v4.md` : à verser. C'est la source de l'empreinte `59a2a571…` ; cherche aussi qui l'a produite ;
   - tout export `.md` ou `.py` daté du 27 ou du 28 novembre, par exemple `verifier_cloture_v3_3.py`.
4. **Fichiers temporaires du 28** (inventaire et versement, pas de suppression) : `C:\Users\lciri\controle-ia-travail\scripts\_go_2026_11_28_v4.md`, `scripts\_etape1_worker_v4.py`, `scripts\etape1_forensique_et_go_v4.sh`, `C:\Users\lciri\etape1_passation_v4.log`.
5. **Scripts cités par Gemini**, dans les deux clones : `reparer_tout_b8_et_prep_dr.py`, `verifier_cloture_v3_3.py`, et le script qui a produit `kit-r2-lot*-slim.txt`.
6. **Recherches par empreinte** : tout fichier d'empreinte `59a2a571c687da0e1a6c84cd3e2bc5f9cb3a8e016bbcc4bb3f52d6f0b61020ac`, avec ou sans retours chariot.
7. **Fichiers du modèle** `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, dans le cache Hugging Face : l'empreinte seule de `tokenizer.json`, `tokenizer_config.json`, `config.json` et `generation_config.json`. N'ouvre aucun fichier de poids.
8. **Banque de tâches** : toute banque de tâches de code Python exécutables avec tests (critère de révision du constat C-1).

## Garde P8 (absolue)
- N'ouvre jamais : un `*.npz`, un `*.npy`, un `*.safetensors`, des poids, scores, planchers ou verdicts de sondes, une consigne privée (`consignes-privees-*.json`, `brouillons/ii-b-saboteur-budget-*/`, `prereg/P3-consignes-v1.md` et ses brouillons, `src/controle_ia/iib/`).
- Pour ces fichiers : nom, taille et empreinte seulement, dans l'inventaire ; ne les verse pas.
- Dans le doute, n'ouvre pas : signale.

## Comment verser
- Branche neuve `versement/disque-local-20261128-v1`, créée depuis `origin/main`. Jamais `main`, jamais de poussée forcée, jamais le dépôt `lciric/controle-ia` (copie publique).
- Fichiers sous `docs/notes/versement-disque-local-20261128-v1/<origine>/`. L'origine vaut `downloads`, `clone-onedrive`, `clone-users`, `antigravity-scratch` ou `huggingface` ; garde le chemin d'origine dans l'inventaire.
- Chaque fichier versé reçoit son compagnon `.sha256`, au format du dépôt : « empreinte, deux espaces, nom nu ».
- Un commit jamais poussé se pousse tel quel sur `versement/commits-locaux-<nom-de-branche>-v1`.
- Aucun fichier de plus de 95 Mo, aucun jeton ni clé : ni `.env`, ni identifiants, ni trousseau `gh`.
- Écris `docs/notes/versement-disque-local-20261128-v1/LISEZMOI-inventaire-v1.md` avec :
  - chaque élément trouvé : chemin d'origine, taille, empreinte brute et sans retours chariot pour les textes, versé ou non et pourquoi ;
  - les commits locaux non poussés ;
  - les arbres de travail ;
  - ce qui reste introuvable.

## Rendu
Pousse, puis écris dans le fichier d'échange :
- la branche et le SHA du dernier commit ;
- le décompte des fichiers versés et non versés ;
- la liste de ce qui reste introuvable.

Dis la même chose à Lazar.
