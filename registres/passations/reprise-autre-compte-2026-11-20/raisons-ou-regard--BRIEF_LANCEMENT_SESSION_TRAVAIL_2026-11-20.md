# Brief de lancement — la session qui succède à la session de travail « Raisons ou regard ? » (20 novembre 2026)

Tu reprends la session de travail de l'expérience 1 de « Raisons ou regard ? », dans `lciric/raisons-ou-regard-travail`, branche `claude/stoic-mayer-51otyy`. Lazar décide ; la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) coordonne.

## À lire d'abord, dans cet ordre

1. `claude/PASSATION_SESSION_TRAVAIL_2026-11-20.md` : l'état exact, et ce qui reste.
2. `claude/papier_2026-11-14/experience_1/NOTE_EXPERIENCE_1_v1.md` : la section 9, la section 8, et les ajouts datés à partir du 19 novembre à 10 h 43. Le dernier ajout date du 20 novembre, 08 h 20.
3. `DECISIONS.md`, de la ligne de la décision 250 à la décision 257.
4. Les docstrings de `experiences/analyses/exp1_juges_fin.py`, `exp1_verdict_fin.py` et `exp1_lecture_fin.py`.
5. Le journal `claude/POINT_AUTONOMIE_2026-11-14.md`, ses dernières entrées.

## Règles de cloisonnement (non négociables)

- **Aucun texte généré, de scénario, de version ou de juge** dans git, ni affiché dans la conversation. Seulement des clés, des comptes, des empreintes et des verdicts. Les textes vont au dépôt privé `Sirmium/rr-resultats` ou restent hors de git (`exp1_commun.garde_hors_git`).
- **Les réponses de Lazar** restent hors de git.
- **Les clés** ne sont jamais écrites, affichées, ni posées sur une machine louée. Pour les juges, seulement la clé de Rigaud, depuis le conteneur : `RR_ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD" RR_ANTHROPIC_WORKSPACE_ID=`.
- **Le scellé ne se réécrit jamais.**
  - Toute décision va dans un ajout daté de la note, et le `.sha256` est refait.
  - La partie scellée (les 51 125 premiers octets) garde l'empreinte `e406fdd6…`.
  - Chaque décision est une ligne de `DECISIONS.md`, avec les mots de Lazar.
- **Le code neuf** passe par trois relecteurs indépendants, l'un après l'autre (décision 230), avant toute dépense ou toute lecture d'épisodes. Un petit changement demande un relecteur. Régime sobre jusqu'au 22 novembre : un sous-agent à la fois.
- **Autonomie (décision 246)** : tu fais ce qui découle des décisions prises ; toute décision nouvelle de fond va à Lazar.
- **Toute dépense** est annoncée au journal, avec le solde ou le crédit lu.
- **Machines** : tu ne touches à aucune machine d'une autre session (58936096, 58936099, 58936100, 60988826, 61170458, 61552174).
- **Le python** : celui de l'environnement virtuel, avec `huggingface_hub`, `anthropic`, `transformers` et `tokenizers`, et `RR_RESULTS_REPO=Sirmium/rr-resultats`. S'il manque, recrée-le : `pip install huggingface_hub==1.33.0 transformers==5.18.0 tokenizers==0.23.2 anthropic requests pyyaml jinja2`.

## Accords en cours (GO)

- **Décision 257** : les juges de la fin.
  - Le juge d'origine et le témoin sont **envoyés** ; il reste à les relever et à les lire.
  - **Le juge d'action est accordé, mais il attend le solde.** Le module refuse de l'envoyer si le reste estimé tombe sous 15 $. Il faut un solde relu (plus bas, une fois les deux lots facturés) ou une recharge, dit par Lazar.
- Rien d'autre n'est accordé : aucune location, aucune autre dépense.

## Prochaine action exacte

1. **Refaire les fichiers d'entrée hors de git**, si le conteneur est neuf :
   - les épisodes, depuis le dépôt privé : `runs/regard_msm-20261120-052259-debb/out/episodes.jsonl`, sous `experiences/resultats/regard_msm-20261120-052259-debb/runs/regard_msm-20261120-052259-debb/out/` (empreinte `e011ae2c…`) ;
   - les invites : `data/exp1_2026-11-20/invites_exp1_fin.jsonl` (`a3469095…`), dans un dossier hors de git ;
   - puis `exp1_juges_fin.py preparer <episodes> <invites> <dossier_neuf_hors_git>`. Les empreintes des lots doivent égaler celles du registre (`lots_juges_fin/*.json`, `requetes_sha256`).
2. **Relever** les deux lots (`D` est le dossier des requêtes) :
   ```
   RR_ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD" RR_ANTHROPIC_WORKSPACE_ID= python3 -I -B experiences/analyses/exp1_juges_fin.py relever D origine
   RR_ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD" RR_ANTHROPIC_WORKSPACE_ID= python3 -I -B experiences/analyses/exp1_juges_fin.py relever D temoin
   ```
   Commite le registre après chaque relève.
3. **Lire** les deux lots :
   - `exp1_juges_fin.py lire D origine <decisions_origine.jsonl>`, puis `lire D temoin <decisions_temoin.jsonl>`. Les décisions sont sans texte : commite-les sous `claude/papier_2026-11-14/experience_1/juges_fin/`, avec le registre.
   - Puis `exp1_juges_fin.py temoin D <decisions_temoin> <decisions_origine> <temoin.json>`.
4. **Lecture complète** : `exp1_lecture_fin.py --juge <decisions_origine> --temoin <temoin.json>`. Sortie : `lecture_fin/lecture_exp1_fin.json`. Commite-la.
5. **Rapport** à Lazar et à la mère :
   - la règle, puis le juge (section 8 : l'écart sur G, le contrôle des jumelles), puis l'accord du témoin ;
   - les réserves de la passation, section 3 ;
   - les questions ouvertes de la passation, section 2, point 6.
