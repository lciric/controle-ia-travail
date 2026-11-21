VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI JOKER. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS UN CHEMIN COMPLET DE TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du rédacteur — course de l'organisme d'idéation sur le seuil à 1 % de fausses alertes et l'emploi du papier « dopamine » pour les moniteurs : question, ordre de course, devis, préenregistrement court — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21. Elle répond à la demande de la mère, vers 06:35Z, qui porte un mot de Lazar : « lance le collisonneur et l'organisme d'ideation dessus ».

Le sujet, tel que la mère le donne :
- la question du seuil à 1 % de fausses alertes, à régler avec quelques centaines d'épisodes honnêtes seulement ;
- l'emploi du papier « dopamine » (arXiv 2602.00986 v2) pour construire des moniteurs ou pour le contrôle : protocoles, routage, audit, budget d'examen humain.

Le collisionneur tourne déjà, chez la mère, sur les mêmes pièces. **Rien ne se lance sans le mot de la mère et une ligne de GO. Aucune dépense, aucun appel.**

## Qui

Tu es un rédacteur neuf (modèle F). Tu n'as écrit aucune pièce de la course « nouvelles attaques », du papier « dopamine » ni du collisionneur. Tu signes « rédacteur de la conception de la course seuil et moniteurs, modèle F ».

## Règles de fond, à tenir dans chaque pièce

- **N-058** : la composition des proposeurs se juge sur l'oracle du monde planté et sur le coût, **jamais sur le verdict du juge**. Les juges sont joués pour information.
- **Kimi est absent** : aucun rôle ne lui revient, et aucun relais qui passe par lui.
- **Aucune clé n'est nommée** dans les sorties : les rôles se disent par relais ou par clé désignée, comme dans le complément de valeurs v3.
- **N-064, N-067** : la revendication O2 de l'organisme d'idéation est resserrée, et les citations sont obligatoires. Ne revendique rien que ces nœuds n'accordent pas.
- **N-065** : l'organisme est un atelier d'idées du programme.
- **Leçon de la course « nouvelles attaques »**, à ne pas reproduire : son texte scellé exigeait un « véhicule neuf » que personne n'avait écrit, et la course s'est trouvée sans programme le jour du départ. **Ta conception nomme dès maintenant le programme qui la fera tourner.** Si un orchestrateur ou un lanceur existant convient, tu le nommes, avec son chemin et son empreinte sur `main`. Sinon, tu dis clairement qu'un véhicule est à écrire, ce qu'il doit faire, et tu le comptes au devis et au calendrier.
- Faits neutres : la question ne prend parti ni pour ni contre le papier « dopamine ». Elle demande des idées, chacune avec son oracle de vérification possible.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Sur `origin/main`, par `git show` redirigé :
- **Les deux pièces neutres de la mère**, scellées. Elles sont versées sur `main` « au prochain versement » ; si elles n'y sont pas encore, **arrête-toi et dis-le** :
  - `docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/faits-seuil-et-moniteurs-v1.md` (`c8c7fb32…`) ;
  - `docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/question-seuil-et-moniteurs-v1.md` (`a5fbe898…`).
- **Les modèles de forme**, que la course « nouvelles attaques » a menés jusqu'au scellement :
  - la question v5 et sa partie servie (`prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v5.md`, `partie-servie-question-v5-v1.md`) ;
  - l'ordre de course v3 et son erratum (`docs/notes/ideation-nouvelles-attaques-v1/conception-v3/`) ;
  - le préenregistrement court v9 et l'additif 1 v5 ;
  - le devis v11 et ses calculs ;
  - le complément de valeurs v3 et son additif.
  Prends la forme ; ne reprends pas le contenu.
- `CLAUDE.md` ; les nœuds N-044, N-045, N-049, N-058, N-064, N-065, N-067 sous `docs/decisions/`.
- `registres/go.md` et `registres/decisions.md`, pour les soldes et les clés, par leur désignation seulement. Nomme ta copie de lecture du registre `lecture-registre-origin-main.md` et celle des GO `lecture-go-origin-main.md` : elles sont exclues du versement.
- Les coûts réels des courses passées (course v9 : 72,50 USD) et les devis passés.

## Ce que tu écris (dossier ci-dessous)

1. **`question-course-seuil-et-moniteurs-v1.md`** : la question au format de l'organisme, sur le modèle de la question v5 et de sa partie servie. Elle porte :
   - le périmètre ;
   - les cases ou axes ;
   - les champs fermés d'une fiche ;
   - ce qu'est une idée recevable, avec son oracle de vérification possible ;
   - ce qui est hors champ ;
   - la synthèse d'antériorité à servir, tirée des faits neutres de la mère, avec citations.
2. **`ordre-course-seuil-et-moniteurs-v1.md`**. Il fixe :
   - le nombre de générations et d'espèces ;
   - les rôles et les relais, sans Kimi ;
   - le portier, les juges pour information et l'oracle (N-058) ;
   - les tâches fraîches (N-049) ;
   - l'héritage et le coût dans le signal (N-044, N-045) ;
   - la lecture par la mère ;
   - **le véhicule** (règle ci-dessus).
3. **`devis-course-seuil-et-moniteurs-v1.md`**, avec un programme de calcul versionné (`calcul_devis_course_seuil_et_moniteurs_v1.py`, arithmétique seule, entrées sourcées) et sa sortie, jouée deux fois et comparée à l'octet. Il donne :
   - les cas bas, haut et pire ;
   - le plafond par relais ;
   - le plafond total ;
   - la ligne de GO à demander ;
   - la répartition proposée sur les clés désignées, avec les soldes connus au registre.
4. **`preenregistrement-court-course-seuil-et-moniteurs-v1.md`**, si la règle R1 l'exige. Dis pourquoi dans le rapport : la course « nouvelles attaques » en a eu un, et la question est de savoir si une course d'idéation est une « expérience décisive ». Si tu l'écris : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères gelés, liste d'arrêt, sur le gabarit `prereg/gabarit-preregistrement-v1.md`.
5. **`rapport-redacteur-conception-seuil-et-moniteurs-v1.md`**. Il contient :
   - les sources et leurs empreintes ;
   - tes choix ;
   - ce que la lettre ne fixe pas, en remarque ;
   - les décisions qui reviennent à Lazar ou à la mère, au format : décision en une phrase ; enjeu ; deux ou trois options ; recommandation et confiance ; défaut sous 48 heures.
6. Une table d'empreintes du dossier.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-conception-seuil-moniteurs/`. Chaque fichier a son compagnon (`env -C DOSSIER sha256sum F`, redirigé par `>` vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement de l'organisme, de l'orchestrateur ni du collisionneur. Aucun appel à un fournisseur de modèles, aucune clé lue ni nommée, aucune dépense. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucune publication d'artefact. Aucun identifiant de modèle dans tes sorties. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
