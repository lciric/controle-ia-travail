VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B` ET `-m pip show numpy` NOMMÉS CI-DESSOUS

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. LE CODE DE RETOUR SE LIT DANS LE RETOUR DE L'OUTIL, JAMAIS PAR `; echo`. **TU N'OUVRES NI N'AFFICHES LE FICHIER DE RÉSULTAT.**

# Mandat de l'exécutant — ligne 3, mesure « portée à 200 » : chronométrage puis mesure, une fois chacun — v1

Pièce de travail (classe C), écrite par la session du compte organisme le 2026-11-20, à la demande de la mère qui l'exécute dans sa session, sur `main` (voie (c)). Sous GO-2026-11-20-26 (accord de calcul de l'étage 2 à 200 témoins ; cette mesure-ci est sur processeur, **sans aucune dépense**), l'additif 3 v3 scellé (`ADDITIF-3-ORGANISME-V9-LIGNE-3`, R-4183) et l'additif 5 v2 scellé (`ADDITIF-5-ORGANISME-V9-LIGNE-3`, R-4220), qui fait foi pour tout ce qui suit.

## Qui

Un exécutant neuf : tu n'as écrit ni le texte de la ligne 3, ni ses additifs, ni le code, ni le verdict de l'étage 1, et tu n'as lu aucune mesure de l'étage 1. Tu lances, tu vérifies les empreintes, tu rends. Tu signes « exécutant neuf ».

## Règle d'aveugle

Tu n'ouvres aucune mesure de l'étage 1 (rien sous `…/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`), et **tu n'ouvres pas le fichier de résultat de cette mesure** : tu en prends l'empreinte par `sha256sum` sur le fichier, sans l'ouvrir. La mère contrôle le seul manifeste avant toute lecture (additif 3, § 6, point 3).

## Ce qui fait foi

L'additif 5 scellé : `/home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md`, empreinte de son compagnon (HEX) `581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c`. Lis-le en entier : § 2 (table des quatorze fichiers et leurs empreintes ; commit `cce6f2341eb74b5730f4a9aaf77266b139a3e20b`), § 3 (racines), § 4 (commandes, dossiers, variables), § 5 (interpréteur).

## Ce que tu fais, dans cet ordre, une fois chacun, jamais relancé

1. `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py` ; code de retour.
2. Vérifications, chacune par une commande simple :
   - `sha256sum -c` du compagnon de l'additif 5 (dans son dossier) : OK, et l'empreinte égale à HEX ;
   - `git -C /home/user/controle-ia-travail rev-parse HEAD` : la tête contient `cce6f234…` (`git -C /home/user/controle-ia-travail merge-base --is-ancestor cce6f2341eb74b5730f4a9aaf77266b139a3e20b HEAD`, code 0) ;
   - pour chacun des quatorze fichiers de la table, `env -C DOSSIER_DU_CODE sha256sum -c F.sha256` : OK, et l'empreinte égale à la table ;
   - `git -C DOSSIER_DU_CODE status --porcelain .` : vide ;
   - `command -v python3` et `python3 --version` (attendu `/usr/local/bin/python3`, 3.13.18) ; `python3 -m pip show numpy` (attendu 2.5.3) ;
   - `test -e` sur `DOSSIER`, sur `DOSSIER_NEUF` et sur leur parent `…/execution-portee-200-v1` : absents ;
   - `printenv BANC_LIGNE_3_CHEMIN` et `printenv CHRONOMETRAGE_LIGNE_3_CHEMIN` : vides.
   Un seul écart : tu t'arrêtes, tu ne lances rien, tu rends l'écart.
3. **Chronométrage**, commande du § 4 de l'additif 5, à la lettre, chemins absolus et HEX ci-dessus, avec `DOSSIER` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/chronometrage`. Code de retour ; empreinte du manifeste et `sha256sum -c` de son compagnon. Il n'imprime que des durées : tu les recopies.
4. **Mesure**, commande du § 4 de l'additif 5, à la lettre, avec `DOSSIER_NEUF` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/mesure`. Lance-la en tâche de fond (elle peut durer) et attends sa fin par l'outil de tâches, sans commande d'arrêt ni recherche de processus. Code de retour ; empreintes du résultat et du manifeste par `sha256sum` sur les fichiers, sans les ouvrir ; `sha256sum -c` de leurs compagnons.
5. **Un refus** d'un programme : tu t'arrêtes, rien n'est relancé, tu rends le motif tel qu'écrit. **Une interruption** avant que le résultat soit écrit (additif 3, § 6, point 1) : rien n'a été rendu ni lu ; tu le dis, sans relancer : la mère décide d'une relance à l'identique dans un dossier neuf. **Un résultat écrit n'est jamais rejoué.**

## Ce que tu rends

`compte-rendu-execution-portee-200-v1.md`, dans `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/` **seulement après la mesure** (le dossier n'existe pas avant ; tu ne le crées pas toi-même : ce sont les programmes qui créent `chronometrage/` et `mesure/`) : heure (`date -u`) de chaque geste, commandes exactes, codes de retour, sorties d'écran du chronométrage, empreintes des trois sorties, résultats des vérifications du point 2, tout écart. **Aucune valeur de puissance, aucun compte de répliques** : tu n'as rien lu du résultat. Son compagnon `.sha256`. Aucun commit : la mère verse.

## Interdits

Voir en tête et la règle d'aveugle. Aucune autre racine, aucun autre argument que ceux de l'additif 5. Aucune écriture dans le dossier du code. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
