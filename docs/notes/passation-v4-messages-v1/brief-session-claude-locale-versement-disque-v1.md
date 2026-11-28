# Brief — session Claude locale sur le poste de Lazar : retrouver sur le disque et verser ce qui manque (v1)

Tu es une session Claude Code lancée par Lazar sur son ordinateur, où se trouvent les clones locaux du dépôt et les dossiers de travail de la session mère précédente (Gemini, devbox Antigravity). Ta tâche est bornée : **inventorier et verser**, rien d'autre. Lis d'abord `CLAUDE.md` du dépôt (règles R1 à R14, garde P8). Pour la routine de reprise, fais seulement les vérifications d'empreintes ; ne relance aucun calcul, aucune machine.

## Où chercher
1. **Clones locaux** de `lciric/controle-ia-travail`, dont `/home/antigravity/lciric/controle-ia-travail`, les worktrees sous `/home/antigravity/worktrees/`, et tout clone sous `C:\Users\lciri\`. Dans chacun :
   - `git status` ;
   - `git stash list` ;
   - `git log --branches --not --remotes --oneline` (commits jamais poussés) ;
   - fichiers non suivis, y compris ignorés (`git status --ignored`).
2. **Dossiers de travail de Gemini** : `/home/antigravity/.gemini/jetski/brain/**/scratch/` et voisins. On y cherche brouillons, scripts, sorties, versions de `registres/go.md` (« Tour 1 »), `registres/decisions.md` et `registres/etat.md` non poussées.
3. **Fichiers précis à retrouver** (par nom, puis par empreinte SHA-256) :
   - `gemini-code-1795778660659.md`, `kit-r2-lot1-slim.txt`, `kit-r2-lot2-slim.txt` (pièces remises au contre-lecteur R2) ;
   - tout fichier d'empreinte `59a2a571c687da0e1a6c84cd3e2bc5f9cb3a8e016bbcc4bb3f52d6f0b61020ac` (version de la contre-épreuve des volets 11 à 13 citée par Gemini ; la version versée est `8547ee1c…`) ;
   - toute pièce des « Volets 1 à 13 » autre que `registres/contre-lectures/contre-lecture-r2-etages-1-2-20261128-v1.md` et `contre-epreuve-r2-volets-11-13-20261128-v1.md` ;
   - toute banque de tâches de code Python exécutables avec tests (critère de révision du constat C-1).
4. **Fichiers du modèle** `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, dans le cache Hugging Face : donne seulement l'empreinte SHA-256 de `tokenizer.json`, `tokenizer_config.json`, `config.json` et `generation_config.json`. Ce sont des fichiers de configuration publics, pas des poids ; n'ouvre aucun fichier de poids.

## Garde P8 (absolue)
- N'ouvre jamais : un `*.npz`, un `*.npy`, un `*.safetensors`, des poids, scores, planchers ou verdicts de sondes, une consigne privée (`consignes-privees-*.json`, `brouillons/ii-b-saboteur-budget-*/`, `prereg/P3-consignes-v1.md` et ses brouillons, `src/controle_ia/iib/`).
- Pour ces fichiers : nom, taille et empreinte seulement, dans l'inventaire ; ne les verse pas.
- Dans le doute, n'ouvre pas : signale.

## Comment verser
- Branche neuve `versement/disque-local-20261128-v1`, créée depuis `origin/main`. Jamais `main`, jamais de poussée forcée, jamais le dépôt `lciric/controle-ia` (copie publique).
- Arborescence : `docs/notes/versement-disque-local-20261128-v1/<origine>/…`. L'origine est par exemple `devbox-depot`, `jetski-scratch` ou `windows`. Garde les chemins d'origine dans l'inventaire.
- Un commit jamais poussé d'un clone local se pousse tel quel sur une branche `versement/commits-locaux-<nom-de-branche>-v1`. Sinon, verse ses fichiers sous le dossier ci-dessus.
- Chaque fichier versé reçoit son compagnon `.sha256`, au format du dépôt : « empreinte, deux espaces, nom nu ».
- Aucun fichier de plus de 95 Mo, aucun fichier de jeton ou de clé : ni `.env`, ni identifiants, ni trousseau `gh`.
- Écris `docs/notes/versement-disque-local-20261128-v1/LISEZMOI-inventaire-v1.md` avec :
  - tout ce que tu as trouvé : chemin d'origine, taille, empreinte, versé ou non, et pourquoi ;
  - les commits locaux non poussés ;
  - les empreintes des fichiers du modèle ;
  - ce que tu n'as pas trouvé.

## Rendu
Pousse, puis donne à Lazar :
- le nom de la branche et le SHA du dernier commit ;
- le décompte des fichiers versés et non versés ;
- la liste de ce qui reste introuvable.

Lazar transmettra à la session mère Claude Code (session_01QPDgKfh86KrPUDxcz8M1GQ), qui vérifiera les empreintes et intégrera.
