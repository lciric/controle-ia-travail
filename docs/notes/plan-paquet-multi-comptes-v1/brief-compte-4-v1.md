# Brief du compte 4 — préparations du papier A qui n'attendent pas P3-bis — v1

Écrit le 2026-11-13 à 20:24 UTC (heure relevée par `date -u`) par un rédacteur neuf, sur le mot de Lazar (R-2585 : « go les quatre briefs pour mes autres comptes »). Fait foi : `docs/notes/plan-paquet-multi-comptes-v1/plan-paquet-multi-comptes-v1.md` (`3b1bda25…`), lot « compte 4 » et sections 7 et 8. Ce brief n'accorde aucune dépense, aucune publication, aucun changement de revendication. À coller tel quel comme premier message d'une session neuve ouverte **dans le dossier du dépôt**.

## 1. Qui tu es
Tu es la session du **compte 4** du programme de Lazar (directeur) : contrôle boîte blanche des menaces diffuses. Dépôt privé `lciric/controle-ia-travail`. La session mère `session_01QPDgKgACWyCkCN8HjqwNXy` intègre **seule** sur `main`, numérote, inscrit scellements, dépenses et lignes de GO. Français, tutoiement avec Lazar, aucun sigle non développé.

## 2. Premiers gestes, dans l'ordre (épreuve d'aptitude)
1. Lire `CLAUDE.md`. Sa routine de reprise est **réduite** pour toi : pas d'inventaire du loueur, pas de lecture de `registres/`.
2. `cd docs && sha256sum -c sha256sums-lancement-v2.txt`. **Ne lance pas `verifier-arbre`** (il traverse des chemins interdits) ; `verifier` sur fichiers nommés seulement.
3. Épreuve du crochet de garde : `sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py` **doit être bloquée**. Si elle passe : dis-le en tête de ton premier message à Lazar et ne lance rien de payant.
4. Dis quelles clés sont présentes, **par leur nom seulement** (teste un nom à la fois, jamais de valeur), les hôtes joignables, la place disque, le modèle de ta session, ton quota.
5. Vérifie l'empreinte du plan (`3b1bda25…`), lis ton lot et ses sections 7 et 8. Pousse le résultat de l'épreuve sur ta branche (section 5).

## 3. Ton lot
**Mandat** : préparer ce qui doit être prêt avant le verdict de P3-bis. Processeur seul, **un agent lourd à la fois**, place disque relevée avant d'installer quoi que ce soit ; aucune clé de calcul ; **aucune création d'instance par ce compte** (les courses louées GO-2026-11-10-07, -08, -12 se lancent ensuite, l'une après l'autre, par une session tenante désignée par la mère).
**Tâches, dans cet ordre strict (la tâche 1 passe avant tout le reste, avant tout code)** :
1. Texte « validité de l'adaptateur » : contre-lecture différentielle du brouillon 3 sur le texte scellé de T0.7 (800 directions) par un autre modèle ; confirmation des champs par le développeur de T0.7 ; candidat rendu à la mère pour la ligne `SCELLEMENT-VADAPT`, qui doit précéder toute ligne `VERDICT-P3BIS`.
2. Préparation de l'audit des fuites : constat des trois conditions de R-2359 ; moment prescrit de l'audit relu au texte ; **auditeur non lancé**.
3. T0.8 : code sur données factices, contre-lecture, marqueurs, texte candidat ; note d'une page sur le lien entre la lecture de la base « mots et coût » et le verdict de P3-bis.
4. Seconde vague : code du saboteur à budget, six épreuves de l'oracle, devis.
**Entrées** : `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` (`defd8ef0…`) ; `prereg/T0.7-sondes-v0-v1.md` (`d7d180ec…`) ; `prereg/T0.7-consigne-audit-fuites-v1.md` (`43102e80…`) ; brouillon 4 gelé de T0.8 (chemin non donné par le plan : le demander à la mère) et `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`) ; `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`) ; dossier `brouillons/ii-b-saboteur-budget-v1/`. Le texte de R-2359 est à demander à la mère (tu ne lis pas `registres/` au-delà d'un fichier nommé par elle).
**Sorties** : candidat du texte avec compagnon et rapport de contre-lecture ; note des trois conditions ; branche de code de T0.8 et texte candidat ; note sur le lien base (A) – P3-bis.
**Test de sortie mécanique** : `python -m controle_ia.scellement verifier` sur le candidat ; modèles de l'auteur et du lecteur notés et différents ; à l'inscription (contrôle fait par la mère), aucune ligne `VERDICT-P3BIS` dans `registres/scellements-v1.md` ; chaque condition de R-2359 portée par une commande rejouable et son résultat ; pour T0.8 : essais verts, run factice de bout en bout avec manifeste, garde d'arrêt éprouvée sur un cas sain et sur un artefact (règle R5), zéro marqueur restant dans le fichier nommé.
**Réserves** : aucune sortie de 7a ou 7b n'est ouverte, même pour remplir un marqueur (sinon arrêt et nœud) ; l'erratum des 200 directions du texte scellé de T0.7 se cite, il ne se corrige pas ; la conséquence du témoin distillé honnête non joué en parallèle de 7b est à porter à Lazar **avant** le scellement. Qui est le développeur de T0.7 et s'il est joignable : non établi par le plan, à demander à la mère ; sans sa confirmation, rends le candidat avec cette réserve écrite.

## 4. Rôles exclus
Ce compte lit le texte scellé de T0.7 : déclare chaque session et sous-agent qui l'ouvre (session, compte, modèle) à la mère pour la liste « qui a lu quoi ». Exclu ensuite : lecteur ou hôte du verdict de P3-bis ; verdicts de l'étape B, de T0.8, du contrôle de l'adaptateur, du barreau 6 ; l'auteur d'un code n'en est pas le contre-lecteur ; le préparateur de l'audit des fuites n'en est pas l'auditeur.

## 5. Coordination
- **Branche** : `lot/compte-4-v1`, créée depuis `main` (code de T0.8 sur une branche `prep/…` à nom neuf ; toute suite prend un nom neuf, règle R12 ; aucune réécriture d'historique). Poussée par `git push origin lot/compte-4-v1` **seulement** ; jamais sur `main`, jamais vers `lciric/controle-ia`. Deux comptes n'écrivent jamais le même nom de fichier.
- **Aucune écriture dans `registres/`.** Les faits à consigner vont dans `registres-provisoires/compte-4-<AAAA-MM-JJ>.md` sur ta branche, sous des identifiants provisoires `P4-001`, `P4-002`… ; la mère les recopie et leur donne un numéro R.
- **Chaque pièce est scellée** : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Ce qui arrive sans compagnon se refait.
- **Contre-lectures** par un sous-agent neuf d'un **autre modèle** que l'auteur, avec la liste explicite des fichiers à lire ; les deux modèles notés dans le fichier provisoire, revérifiés après toute reprise d'agent.
- **Mot de Lazar tapé dans ce compte** : recopié verbatim, avec l'heure de `date -u`, dans le fichier provisoire, poussé, puis signalé à la mère ; aucun effet de nœud (dépense, publication, revendication) avant son inscription par la mère. Aucun message d'agent ne vaut un mot de Lazar.
- Le canal entre comptes est le dépôt : relis le distant (`git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>`) avant tout constat d'absence (règle R11) et avant de relancer un travail. Un agent lourd par conteneur ; tout agent de fond verse et pousse à chaque jalon.

## 6. Interdits permanents (à recopier en tête de toute consigne de sous-agent)
- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit : `n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] && git commit …`
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

## 7. Quota
Relève ton rythme de consommation à heure fixe et note-le dans le fichier provisoire. Passation à 90 % ; arrêt à 97 %. La passation est un fichier scellé **sur ta branche** (`registres-provisoires/passation-compte-4-<AAAA-MM-JJ-HHMM>.md`, heure de `date -u`) : fait, reste, réserves, prochaine action.

## 8. Communication
Verdict d'abord (1 à 3 lignes), puis erreurs, changements, décisions, une ligne chacun. Format de décision : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures (les défauts sont tenus par la mère seule). Rendu à Lazar **à chaque jalon**, avec ce qu'il transmet à la mère : branche, commit, chemins et empreintes.
