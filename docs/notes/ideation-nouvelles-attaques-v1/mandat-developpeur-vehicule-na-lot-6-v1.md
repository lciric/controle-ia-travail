VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DES DOSSIERS DES LOTS 1 À 5. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lot 6 (classe de génération, surcharge de `juger`, simulation, configuration) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21. La conception v5 est vérifiée « Conforme » (contrôle `4b369004…` : « le lot 6 peut partir à son tour »). **Ne part qu'une fois les lots 3, 4 et 5 vérifiés « Conforme »**, dont il dépend en code ; il se joue avec le lot 10 a. Il est sur le chemin critique (7,5 heures à la v5). Code par un développeur O, vérifié par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni la conception, ni les lots 1 à 5, ni aucun orchestrateur. Tu signes « développeur du lot 6 du véhicule NA-1, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **La conception v5** (`/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md`, `1b7f6822…`) et son contrôle (`conception-vehicule-v5/controle-v1/controle-conception-vehicule-na-v5-v1.md`, `4b369004…`), qui priment sur la v4. En particulier : § 0 bis ; § 2.5 (juges joués pour information, et la surcharge de `juger` : passeport du portier neuf, identifiant réencodé fait des mêmes octets que le jeton du noyau, `self.appel`, verdicts au coffre, arrêt d'A2 quand la version servie d'un juge change) ; § 2.9 (génération et course du régime) ; § 2.12 (moteur simulé) ; § 2.13 (gardes héritées, une par une, par rôle ; **A3 et A14 désactivées par écrit, vérifiées au départ ; le délai d'A3 actif ; garde de remplacement de onze refus écrits d'un même proposeur par génération ; A17 en arrêt nommé**) ; § 5.1 ; § 6 (arrêts n° 5, n° 6, n° 7, n° 10, n° 14) ; § 7 (lot 6).
- **La remarque du contrôle de la v5, point 1, à lire telle quelle** : un rôle arrêté le reste jusqu'à la fin de la génération ; un proposeur arrêté en cours de génération n'atteint donc jamais onze refus ; ses cases sont comptées « non jouées », et la course continue. Tu codes cette lettre, sans la lire autrement.
- **La v9 scellée** et ses compléments, sur `origin/main` (`prereg/ideation-nouvelles-attaques-v1/`) : trois générations, six étapes neutralisées, régime, mémoire déclarée, seuils et délais des gardes héritées.
- **Le relevé du lot 0** (`docs/notes/ideation-nouvelles-attaques-v1/lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md`, `10ac79ec…`) : Q3 (étapes), Q4 (cases et mémoire), Q9 (relais sur trois générations), Q11 (appels en suite), Q12 (gardes héritées).
- **Les lots 3, 4 et 5 vérifiés** : code, rapports et **interfaces figées** (le mélange `AppelGardeNA` du lot 4 ; le passeport du portier du lot 5). Dossiers et empreintes donnés au départ.
- **La base** : la v68 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/`, `GenerationV68`) et l'orchestrateur en lecture seule (`/home/user/lciric/ideation-organism`, `a41b7b50…` ; `noyau_v56.py`, l. 194, 198, 199 pour `juger`).

**Les valeurs de l'additif du véhicule** (bornes, seuils des gardes héritées, délais) ne sont pas à toi : tu écris contre un brouillon d'essai, déclaré comme tel, lu dans la configuration.

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-6/`.

1. **Module `course`** (suffixe `_na_v1`) : classe de génération (le mélange du lot 4 devant `GenerationV68`) ; proposition neuve ; six étapes neutralisées ; `fournisseurs_requis` ; copie de la configuration par génération ; gardes héritées et refus écrits avec ce qu'ils rendent par rôle ; A3 et A14 désactivées par écrit et vérifiées au départ ; garde de remplacement ; A17 ; **étape « aiguillage » surchargée** ; **surcharge de `juger`** (classe neuve) ; mémoire déclarée.
2. **Lanceur de l'orchestrateur**, **module `simulation`** (moteur simulé, faux fournisseur) et **configuration de course** d'essai.
3. **Les formats que lit le lot 7** (sorties de génération, attestations, comptes) : figés dans ton rapport, sur le § 5, pour que le lot 7 parte sans t'attendre.
4. **Essais** : arrêts n° 5, n° 6, n° 7, n° 10, n° 14, A17 et la garde de remplacement, chacun avec cas sain et artefact (R5) ; régime ; gardes héritées une par une ; mémoire ; identifiants dans les requêtes des juges (réencodés, aucune suite de huit chiffres hexadécimaux) ; A2 sur changement de version servie ; trois générations en moteur simulé ; mutations à la manière de la v68.
5. **`rapport-developpeur-lot-6-na-v1.md`** : exigences citées, code (fichier:ligne), essais et mutations, ce que la lettre ne fixe pas (en remarque), les interfaces pour les lots 7, 8 et 10 a.
6. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
