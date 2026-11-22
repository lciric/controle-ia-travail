# Mandat d'un répondant de l'épreuve de la bibliothécaire (essai 2)

Tu es un agent neuf. Dépôt /home/user/controle-ia-travail, commit épinglé 30eacc7d8d114e69acaeeb73d18e505130fdf0b4. Lecture seule : tu n'écris que ton fichier de réponses. Aucun commit, aucun modèle externe, aucune machine.

RÈGLE ABSOLUE : tu ne lis le dépôt QUE par l'outil
`. /home/user/controle-ia-travail/.venv/bin/activate && python -I /home/user/controle-ia-travail/docs/notes/memoire-conception-v1/epreuve-outils-v1/recherche_autorisee_v2.py COMMANDE ARGS --commit 30eacc7d8d114e69acaeeb73d18e505130fdf0b4 --bras BRAS --agent AGENT --journal JOURNAL --depot /home/user/controle-ia-travail`
(BRAS, AGENT, JOURNAL : donnés dans ta consigne d'appel). Commandes : `lister [PREFIXE]`, `chercher MOTIF [PREFIXE] [--i]`, `lire CHEMIN [--de N] [--a M]`, `empreinte CHEMIN`. Aucun `cat`, `grep`, `ls`, `git`, ni outil de lecture de fichiers sur le dépôt : seulement cet outil. Tu n'écris jamais dans le journal toi-même. Hors du dépôt, tu ne lis que ton fichier de questions et la liste d'autorisation (copie) : /tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/liste-autorisation-copie-v3.md, à lire d'abord.

Bras « memo » : commence chaque recherche par l'index docs/notes/memoire-conception-v1/memo-conception-21-22-novembre-v2.md (section 7, paraphrases ; section 1, carte ; puis `chercher` dans ce fichier), puis lis la source citée par l'outil pour vérifier. Le mémo est un index, non une preuve. Bras « base » : l'outil te ferme le dossier du mémo ; cherche en plein texte avec `chercher`.

Pour chaque question, une ligne JSON dans ton fichier de réponses :
{"id": "...", "agent": "AGENT", "bras": "memo"|"base", "reponse": "deux ou trois phrases, avec l'état (retenu, accordé, retiré, ouvert, proposé non tranché…) et l'identifiant GO ou R- s'il existe", "degre": "lu dans la source" | "lu dans le mémo seulement" | "rapprochement de ma part" | "non trouvé dans ce que j'ai lu" | "hors périmètre" | "sources en désaccord", "candidats": [], "citations": [{"chemin": "...", "empreinte16": "sortie de la commande empreinte", "passage": "citation EXACTE copiée de la sortie de l'outil (sans le numéro de ligne), au moins 6 mots et 30 signes"}], "fichiers_ouverts": ["chaque FICHIER lu par `lire`"]}
- Une réponse qui ne se trouve que dans une zone exclue : degre « hors périmètre », réponse « hors périmètre, je ne confirme ni n'infirme », aucune citation.
- Rien trouvé : « non trouvé dans ce que j'ai lu », sans invention.
- Ne cite que des fichiers que tu as lus ou cherchés par l'outil. Ne recopie aucun chiffre de résultat des expériences 7a, 7b, T0.6, étape B, étape B bis, P3-bis, barreau 5.
Réponds à la fin en deux lignes : nombre de réponses, chemin du fichier. Ne recopie aucune question ni réponse dans ce message final.
