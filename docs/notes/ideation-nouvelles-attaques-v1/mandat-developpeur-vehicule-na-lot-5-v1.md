VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DES DOSSIERS DES LOTS 1 À 3. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lot 5 (lecteur et contrat des fiches, portier neuf, identifiants, registres) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21, sur le mot de la mère (08:04Z : « les lots 3 à 5 peuvent suivre de la même façon dès que leurs mandats sont prêts »). **Ne part qu'une fois le lot 3 vérifié « Conforme »** (il dépend en code des lots 1 et 3) ; il se joue avec le lot 4. Il est sur le chemin critique. Code par un développeur O, vérifié par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni la conception, ni les lots 1 à 4, ni aucun orchestrateur. Tu signes « développeur du lot 5 du véhicule NA-1, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **La conception v5** (`/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md`, `1b7f6822…`) et son contrôle (`conception-vehicule-v5/controle-v1/`, `4b369004…`), qui priment sur la v4. En particulier : § 0 bis ; § 2.4 (portier et ses classes : `lecteur_fiches`, `contrat_fiche`, `portier`) ; § 2.6 (registre des tentatives, registre servi) ; § 5.1 ; § 5.2 (identifiant neutre, encodage dans les deux sens) ; § 5.4 (contrat de sortie d'une fiche) ; § 6 (arrêts n° 4, n° 5, n° 8, n° 9, n° 19) ; § 7 (lot 5).
- **La v9 scellée** et ses compléments, sur `origin/main` (`prereg/ideation-nouvelles-attaques-v1/`) : contrat de fiche, bornes en octets, classes d'appel, champ `case`, « autre, à nommer ».
- **Le relevé du lot 0** (`docs/notes/ideation-nouvelles-attaques-v1/lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md`, `10ac79ec…`) : Q4 (cases et mémoire), Q6 (lecteur et validateur de fiches).
- **Les lots 1 et 3 vérifiés** : code, rapports et interfaces (dossiers et empreintes donnés au départ) ; l'encodage des identifiants du lot 1 est repris, non réécrit.
- **La base** : la v68 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/`) et l'orchestrateur en lecture seule (`/home/user/lciric/ideation-organism`, `a41b7b50…`).

**Les consignes du portier et des juges (D3) et les bornes en octets** ne sont pas à toi : tu écris contre un **brouillon d'essai** factice, au format que la conception permet, que tu déclares comme tel.

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-5/`.

1. **Modules** (suffixe `_na_v1`) : `lecteur_fiches` (syntaxes déclarées, grammaire par étiquettes ancrées sans ordre exigé) ; `contrat_fiche` (validateur neuf, sans caviardage) ; **`portier`, code neuf** (lecture des seules étiquettes de D3, ses deux sortes d'appel, ses passeports, son journal) ; `identifiants` (encodage dans les deux sens, repris du lot 1) ; `registre` ; `verifier_registre_servi` (sur un registre d'essai aux lignes inertes ; **le registre servi réel n'est pas ouvert**).
2. **Essais** : arrêts n° 4, n° 5, n° 8, n° 9, n° 19, chacun avec cas sain et artefact (R5) ; classes d'appel ; champ `case` ; « autre, à nommer » ; hors contrat de longueur ; lignes de compte à zéro ; passeport exigé ; mutations à la manière de la v68.
3. **`rapport-developpeur-lot-5-na-v1.md`** : exigences citées, code (fichier:ligne), essais et mutations, ce que la lettre ne fixe pas (en remarque), l'interface pour les lots 6, 7 et 10 a (passeport du portier, que la surcharge de `juger` du lot 6 exige).
4. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte, le registre servi réel non ouvert. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
