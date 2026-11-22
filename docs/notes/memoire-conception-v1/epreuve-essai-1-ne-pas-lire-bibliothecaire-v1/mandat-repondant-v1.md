# Mandat d'un répondant de l'épreuve de la bibliothécaire (essai 1)

Tu es un agent neuf. Dépôt /home/user/controle-ia-travail, état épinglé : commit cf3a1aa5d05195f234f3ee64d0819cbdf92299ff (l'arbre de travail est à cet état pour tout ce que tu as le droit de lire). Lecture seule : tu n'écris que ton fichier de réponses. Aucun commit, aucun modèle externe, aucune machine.

1. Lis d'abord en entier docs/notes/memoire-conception-v1/liste-autorisation-bibliothecaire-v2.md : c'est ton périmètre strict. N'ouvre rien d'autre. En plus : n'ouvre JAMAIS docs/notes/memoire-conception-v1/epreuve-banque-ne-pas-lire-bibliothecaire-v1/, ni aucun autre fichier de lot que le tien, ni rien sous /tmp sauf ton fichier de questions et ton fichier de réponses.
2. BRAS : indiqué dans ta consigne d'appel.
   - Bras « memo » : commence chaque recherche par l'index docs/notes/memoire-conception-v1/memo-conception-21-22-novembre-v2.md (section 7, index des paraphrases ; section 1, carte ; puis grep), puis ouvre la source citée pour vérifier. Ne réponds jamais du mémo seul : le mémo est un index, non une preuve.
   - Bras « base » : n'ouvre RIEN sous docs/notes/memoire-conception-v1/ (ni le mémo, ni rien d'autre de ce dossier). Cherche en plein texte (grep) dans le reste du périmètre.
3. Pour chaque question de ton lot (fichier indiqué dans ta consigne d'appel), réponds en une ligne JSON (fichier JSONL) :
   {"id": "...", "bras": "memo"|"base", "reponse": "deux ou trois phrases : la réponse, avec l'état (retenu, accordé, retiré, ouvert, proposé non tranché…) et l'identifiant GO ou R- s'il existe", "degre": "lu dans la source" | "lu dans le mémo seulement" | "rapprochement de ma part" | "non trouvé dans ce que j'ai lu" | "hors périmètre" | "sources en désaccord", "candidats": ["si la question est une paraphrase ambiguë : deux ou trois candidats et ce qui les distingue, sinon liste vide"], "citations": [{"chemin": "chemin relatif au dépôt", "empreinte16": "16 premiers signes de `git show cf3a1aa5d05195f234f3ee64d0819cbdf92299ff:CHEMIN | sha256sum`", "passage": "citation EXACTE, mot pour mot, d'au moins 6 mots et 30 signes, copiée du fichier (ne la reformule pas)"}], "fichiers_ouverts": ["TOUS les chemins relatifs que tu as ouverts ou lus pour cette question, grep compris quand tu as lu des lignes d'un fichier"]}
   - Si la réponse ne peut se trouver que dans une zone exclue par la liste : degre « hors périmètre », réponse « hors périmètre, je ne confirme ni n'infirme », aucune citation, et n'ouvre rien d'exclu.
   - Si tu ne trouves rien : « non trouvé dans ce que j'ai lu », aucune invention.
   - Ne recopie aucun chiffre de résultat des expériences 7a, 7b, T0.6, étape B, étape B bis, P3-bis, ni du barreau 5.
4. Vérifie chaque passage par grep avant de l'écrire, et chaque empreinte par la commande ci-dessus.
Réponds à la fin en deux lignes : nombre de réponses écrites, chemin du fichier. Ne recopie aucune question ni réponse dans ce message final.
