# Provenance du code — AUTODISC (lecture contre O4) — v1

- **Lecteur** : modèle I (session du compte organisme). Relevé fait le Wed Nov 18 03:32:41 UTC 2026 (date -u, même commande que l'écriture de ce fichier).
- **Pièce** : Agarwal et al., AutoDiscovery (arXiv 2507.00310 v3, NeurIPS 2025) ; note de lecture : `docs/notes/lecture-o4-suite-v1/lecture-piste-nouvelle-autodisc-o4-v1.md`.
- **Origine** : clone en lecture seule fourni par la session mère, sous le bloc-notes de la session (`code-o4/autodiscovery`) ; dépôt distant `origin` = https://github.com/allenai/autodiscovery (git remote get-url origin). Je n'ai fait aucun clonage ni téléchargement ; l'heure du clonage n'est pas relevée par moi (fichiers de travail datés 03:05 sur disque, ls -la).
- **Commit** : 66aa2d513cafdb23bf38313ebef522ade93f8cd9 (git rev-parse HEAD), date du commit 2026-08-13 09:42:43 -0700 ; dépôt superficiel (is-shallow-repository = true), un seul commit visible ; historique non lu.
- **Fichiers suivis** : 23 (git ls-files).
- **Licence** : aucun fichier de licence suivi au commit (fichiers suivis dont le nom contient *licen* : 0) ; `pyproject.toml` lu en entier, sans champ de licence ; `README.md` lu en entier, sans mention de licence ; `NOTICES.txt` est un recueil d'avis de licences de paquets tiers (tête lue), pas la licence du dépôt. Conséquence : aucun droit de réutilisation présumé ; le code n'est pas versé dans le dépôt du programme, seuls des extraits courts sont cités dans la note (fichier d'extraits rejoué).
- **Aucun programme du clone n'a été lancé, rien n'a été installé.**

## Fichiers et lecture (sha256 recalculés au relevé)

| fichier | sha256 | lecture |
|---|---|---|
| `.gitignore` | `9b4a1e2bff19c6e1201d6b78ffdb177e317bb1b7b8fe1b91f93762924d844ed9` | lu en entier (20 lignes) |
| `NOTICES.txt` | `79d84bc3777be1b9e729093b13dc01bc89e8e74605a77f812c1b86662d6bbd56` | tête (40 lignes) et recherche de mots (8727 lignes) |
| `README.md` | `11fafcfdb9503746a8318dfd7971e352fa92682d33eb1c50e2a1b1000daeb1ce` | lu en entier (118 lignes) |
| `artifacts/autodiscovery_logo.png` | `e94e2cf9fcb095b9c0235722532a92aa3f6e2c6424df3b315a20cea5bac231cb` | non lu (image) |
| `artifacts/autods_logo.png` | `395576db028e5bccf26b89312622eec132f2b8f6776bdd90d3698d16ce2fb556` | non lu (image) |
| `environment.yml` | `967a476ccab3d8c8b416fccf5f16b9ad1977a46c32da143ebb78617ce2761ef4` | lu en entier (15 lignes) |
| `pyproject.toml` | `b7b6f00bc1c06ca6f3b5981bff094fc6d579f60c68c7e53ea940e8bdcdb59c2d` | lu en entier (42 lignes) |
| `src/__init__.py` | `678fd0827da3b7b4c57bce1d724d8155866c4d30abbbbdda5cff63699f322f89` | lu en entier (3 lignes) |
| `src/agents.py` | `2d067ecec821fdededb644a9c461f81303cf38330407a873091204afc8249770` | lu en entier (294 lignes) |
| `src/args.py` | `0b37a7fcc505993bd7576481ab7c3a656bb6c4b0440933c1ea3dd4bdbe896479` | lu en entier (80 lignes) |
| `src/beliefs.py` | `9b8e0f41b616cd41fe0aed6b0f223eee43ee4bc90cf096c82f286354c741cffc` | lu en entier (1273 lignes) |
| `src/dataset.py` | `65cb0c4ac5d349f87e299a1c6e615e77913359b0d6a166541ae908b8650fa91e` | lu en entier (182 lignes) |
| `src/deduplication.py` | `cb10931913a293e2b515891d34b957c2927b00a8dda90fa6c70ea942ff88d77c` | lu en entier (276 lignes) |
| `src/log_utils.py` | `afdcce06a55d1f0934611bb41968cb4e03df16478cc64cd21a9662c99e98b046` | lu en entier (273 lignes) |
| `src/logger.py` | `4980e47bcd18415280c1c2cde110a435bda115a90cb2d2d8dd513c63f8a68502` | lu en entier (89 lignes) |
| `src/mcts.py` | `7a128b7b1f04841f195cf9d6526b05135aeb550cfbe718f0710bfe3c0cc92e10` | lu en entier (439 lignes) |
| `src/mcts_utils.py` | `8bd01c6e5064db5866066ac78b9fbf1dbd6495361e5c66649271cb177758b931` | lu en entier (347 lignes) |
| `src/mcts_viz.html` | `c4b6b908fd54f82a12fe112167184a531ed32e43285174d2e6ba6958234d50f4` | recherche de termes seulement (466 lignes) |
| `src/nodes_to_csv.py` | `e72a6db5a6b27fba300afd360bf40b46321f5b932eeeedda0d613843da5578c8` | lu en entier (79 lignes) |
| `src/run.py` | `aff9fd80c0be2bdbaefce6dd3bcba24c3ba7f59e46def7592a6aa993fb135f4e` | lu en entier (520 lignes) |
| `src/structured_outputs.py` | `2f5158f8c6a55d8225d0e6d45ca24aa256826a43114bc0db167d3270ab86d9f1` | lu en entier (189 lignes) |
| `src/transitions.py` | `761c8383eba1fe9bf37289dbfa72f3ee50c45ccef74c49d817743a7a10b57bb3` | lu en entier (66 lignes) |
| `src/utils.py` | `6f9091bba53132ce1203d99eb274edb0f05460ae50d03356576e9f2c29ba0673` | lu en entier (125 lignes) |
