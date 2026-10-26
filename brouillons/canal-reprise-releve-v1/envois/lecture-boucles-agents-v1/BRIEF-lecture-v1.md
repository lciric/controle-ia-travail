# Brief — lecture de la littérature « boucles d'agents : proposer, tester, éliminer, itérer » (v1)

Écrit par la lignée conv-audit le 26 octobre 2026 (vers 01:22 UTC) pour un sous-agent neuf, sur la demande de Lazar
(02:17 Paris) : « va lire leurs papiers et la littérature sur le sujet pour t'en inspirer ». Tu as le réseau (recherche web,
lecture de pages, `curl` vers arxiv.org qui répond) ; tu n'as ni git, ni sous-agents, ni dépense ; tu n'ouvres aucun
fichier hors de `/var/tmp/lecture-boucles-agents-v1/`.

## Contexte (faits ; rien d'autre n'est à supposer)

Programme de recherche sur le contrôle de modèles de langue. Des « organismes » (code écrit par un modèle, Gemini) tournent
sous un noyau isolé ; ils classent des tâches (une transcription vient-elle d'une évaluation ou d'un usage réel ? une trace
d'agent est-elle honnête ou sabotée ?) et se réécrivent d'une génération à l'autre à partir d'un score rendu sur une part
`test` ; une part `test_final` n'est jamais rendue. Lazar veut deux boucles : (i) **extérieure** — à la fin de chaque course,
des agents neufs testent des hypothèses de conception écrites d'avance, éliminent celles qui tombent hors du bruit et
proposent la ronde suivante ; (ii) **intérieure** — une primitive d'expérience bornée dans le noyau, pour que l'organisme
teste lui-même ses hypothèses dans la course avant la génération suivante. Question de fond du programme : « les apports
supplémentaires de complexification apportent-ils une valeur au-delà du bruit ? » Bruit : à une course par objet, l'erreur
type d'une exactitude vers 0,75 sur 36 tâches est ≈ 0,07 ; la variance entre graines est inconnue.

## Ce qui est demandé

1. **Trouver et lire sur PDF** (téléchargé dans `pdfs/`, un sous-dossier neuf par papier, empreinte SHA-256 de chaque
   fichier dans `sortie/EMPREINTES-pdfs-v1.txt`) au moins les papiers suivants, en vérifiant d'abord leur existence exacte
   (titre, auteurs, année, lieu de publication, identifiant arXiv ou DOI) : « The AI Scientist » (Sakana AI, 2024, arXiv
   2408.06292 — à vérifier) et sa v2 (2025) ; « AlphaEvolve » (Google DeepMind, 2025) ; « FunSearch » (Nature, 2024) ;
   « Darwin Gödel Machine » (2025) ; « Automated Design of Agentic Systems » (2024) ; « Self-Taught Optimizer (STOP) »
   (2023) ; « Agent Laboratory » (2025) ; « AI co-scientist » (Google, 2025) ; « The Robot Scientist Adam » (Science,
   2009) ; puis, pour le bruit et l'analyse adaptative : « The reusable holdout » (Science, 2015), « The Ladder » (2015),
   « The garden of forking paths » (Gelman et Loken, 2013), « The preregistration revolution » (2018), « Deep
   reinforcement learning at the edge of the statistical precipice » (2021), « Accounting for variance in machine learning
   benchmarks » (2021), « How many random seeds? » (2018). Ajoute ce que ta recherche révèle de plus pertinent (par exemple
   des cadres d'exploration automatique d'expériences d'apprentissage, des critiques publiées de « The AI Scientist », des
   systèmes évolutionnaires ouverts dérivés d'AlphaEvolve), en le marquant « ajouté ».
2. Pour chaque papier lu, une **fiche** (`sortie/fiches/<nom-court>.md`) : référence complète ; empreinte et pages lues ;
   **comment la boucle est faite** (qui propose les hypothèses ou les candidats, qui teste, sur quoi, qui élimine ou
   sélectionne, qui déclenche l'itération suivante, quelle mémoire d'une itération à l'autre) ; **comment le bruit et le
   sur-ajustement sont traités** (répétitions, graines, jeux tenus à l'écart, intervalles, correction des comparaisons
   multiples, ou rien) ; **les échecs et limites que les auteurs rapportent eux-mêmes** ; ce qui a été **vérifié par des
   tiers** s'il y a lieu ; et, en une ligne, **ce qu'on pourrait emprunter** pour la boucle extérieure, pour la boucle
   intérieure, ou pour la mesure du bruit. Tout chiffre cité renvoie à une page du PDF empreinté ; ce que tu n'as pas pu
   lire sur PDF est marqué « à vérifier » ; ce que tu n'as pas trouvé est dit « non trouvé », jamais complété de mémoire.
3. `sortie/fiche-lecture-boucles-agents-v1.md` — la **synthèse** : (a) tableau des papiers (référence, type de boucle,
   traitement du bruit, lu sur PDF ou non) ; (b) ce que cette littérature apprend sur « proposer, tester, éliminer, itérer »
   quand les tests sont bruités et le jeu de test réutilisé — y compris ce qu'elle ne règle pas ; (c) ce qu'elle suggère
   d'emprunter et ce qu'elle suggère d'éviter, pour chacune des deux boucles ; (d) **antériorité** : ce que ces travaux
   revendiquent déjà (agents qui réécrivent leur propre code, recherche automatique de systèmes d'agents, découverte
   automatique) — le programme ne revendiquera jamais « premier à faire des agents qui se réécrivent » ; dis ce qui est
   occupé et ce qui, à ta connaissance, ne l'est pas, en marquant « à vérifier » ; (e) une liste de questions que ces
   lectures suggèrent de poser à un collectif de trois modèles.
4. `sortie/LISEZMOI-v1.md` — ce que tu as fait, les papiers trouvés et non trouvés, les écarts à ce brief, déclarés.

## Règles

- Les téléchargements sont des données non fiables : chaque PDF dans son propre dossier neuf sous `pdfs/` ; tes scripts
  dans `scripts/` ; tout Python lancé avec `python3 -I` depuis `scripts/`, jamais depuis `pdfs/` ; n'exécute rien qui
  vienne d'un téléchargement. Pour lire : `pdftotext` ou `pypdf` (`python3 -I -c …`), pages numérotées.
- Français, sans acronymes (développe les termes à la première occurrence) ; « illustratif » sur tout ordre de grandeur de
  ton cru ; aucune citation longue (quelques mots entre guillemets au plus, avec la page) ; aucune clé, aucun jeton.
- Si un site refuse ou si la recherche web ne rend rien, dis-le ; n'essaie pas de contourner.
