VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DU DOSSIER DES LOTS 1 ET 2 (NI `git ls-tree`, NI `git show` D'UN DOSSIER). TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du vérificateur — véhicule NA-1, lots 1 et 2 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21. Code écrit par un développeur O ; tu le vérifies (modèle S). **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.**

## Qui

Un vérificateur neuf (modèle S), qui n'a écrit ni la conception, ni le mandat, ni le code. Tu signes « vérificateur des lots 1 et 2 du véhicule NA-1, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **Le mandat du développeur** : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lots-1-et-2-v1.md`.
- **La conception v5** (`…/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md`, `1b7f6822…`) et son contrôle (`…/conception-vehicule-v5/controle-v1/`, `4b369004…`) : § 0 bis, § 2.1, § 2.3 (garde de motifs), § 5.2 (identifiant neutre, règle d'encodage en cinq points), § 6.1, § 6.2, § 7 (lots 1 et 2).
- **La v9 scellée** et ses compléments (`prereg/ideation-nouvelles-attaques-v1/` sur `origin/main`) : R9, clés gelées, clés n° 30 et n° 40, arrêts n° 10 et n° 16, ligne de case.
- **Le livrable** : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/lots-1-et-2-vehicule-na-v1/` (table `310cc708…`, rapport `960845db…`, manifeste `ea106f1d…`, programme d'application `ba6341c5…`, paquet sous `paquet/orchestrator/`).
- L'orchestrateur en lecture seule : `/home/user/lciric/ideation-organism` (`a41b7b50…`), jamais modifié.

## Ce que tu fais

1. Vérifie la table d'empreintes du livrable.
2. Fais une copie neuve de `orchestrator/` (sans `.git`) dans ton dossier ; applique le paquet par son programme d'application ; rejoue les essais (le rapport annonce 83 passés) et les mutations (42, toutes tuées ; une mutation inerte survit). Les comptes sont-ils égaux ?
3. Pour chaque exigence du mandat et des paragraphes cités de la conception : est-elle faite, et où (fichier:ligne) ? L'essai qui l'éprouve échoue-t-il si on retire la garde ? Points d'attention : tirage rejoué égal à l'octet ; clés n° 30 et n° 40 au même geste ; encodage dans les deux sens, alphabet, base 60 à longueur fixe (18 et 14 lettres), refus hors alphabet, aucune suite de huit chiffres hexadécimaux ; arrêt n° 16 par famille (cas sain, artefact) ; aucun octet changé après la garde, l'empreinte journalisée étant celle de ce que la garde a lu ; la ligne « envoi » écrite avant l'envoi, la ligne « non envoyé » sans recopier le texte trouvé.
4. Les douze points « que la lettre ne fixe pas » du rapport : en est-il un que le code tranche à tort, ou qui contredit la conception ? Dis lesquels doivent aller à l'additif du véhicule.
5. L'interface rendue pour les lots 3, 5 et 6 : est-elle complète et cohérente avec le § 5.1 de la conception ?
6. Aucun identifiant de modèle, aucune clé, aucune recette dans le livrable.

Écris `verification-lots-1-et-2-na-v1.md`, avec son compagnon, dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-vehicule-na-lots-1-2/`. Verdict « Conforme » (le lot 3 peut partir) ou « À corriger », avec chaque correction dite précisément. Tu ne corriges pas le code toi-même.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte (et pas de `git fetch` sans nom de branche). Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
