VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DU DOSSIER DES LOTS 1 ET 2. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lot 3 (requête et journal) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21, sur le mot de la mère (08:04Z : « les lots 3 à 5 peuvent suivre de la même façon dès que leurs mandats sont prêts »). **Ne part qu'une fois les lots 1 et 2 vérifiés « Conforme »**, dont il dépend en code. Code par un développeur O, vérifié par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni la conception, ni les lots 1 et 2, ni aucun orchestrateur. Tu signes « développeur du lot 3 du véhicule NA-1, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **La conception v4** (`/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v4/conception-vehicule-course-nouvelles-attaques-v4.md`) et, quand elle est versée, **la v5 courte** du même dossier parent (`conception-vehicule-v5/`), qui prime ; leur contrôle. En particulier : § 0 bis (décisions de la mère, dont D2 : rien n'est ajouté à l'enveloppe ; dernier octet des pièces servies gardé, empreinte sur la pièce entière), § 2.2 (assemblage, partie servie, ligne de case), § 2.7 (journal), § 2.13 (refus écrits, par rôle), § 5.3 (l'enveloppe), § 5.4 (contrat de sortie), § 6 (épreuves), § 7 (lot 3).
- **La v9 scellée** et ses compléments, sur `origin/main` : la partie servie (`prereg/ideation-nouvelles-attaques-v1/partie-servie-question-v5-v1.md`), la requête assemblée et sa journalisation, l'arrêt n° 8 (taille), la garde de motifs avant l'envoi (n° 16).
- **Les lots 1 et 2 vérifiés** : leur code, leur rapport et leur interface (dossiers et empreintes que la session te donnera au départ).
- **Le relevé du lot 0** (`docs/notes/ideation-nouvelles-attaques-v1/lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md`, `10ac79ec…`), Q1 (textes ajoutés par les adaptateurs) pour ce que la requête ne doit pas porter.

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-3/`.

1. **Modules `requete` et `journal`** (suffixe `_na_v1`) : partie servie remplie par la ligne de case du lot 1 ; enveloppe **sans ajout** (D2) ; composition par rôle ; forme de la fiche servie au portier et aux juges, déclarée ; journal **d'ajout seul** (taille et empreinte SHA-256 de chaque requête assemblée, génération, rôle) ; lignes « non envoyé » et « non lancé » ; refus écrits par rôle (ce qu'ils rendent : § 2.13 de la conception).
2. **Essais** : partie servie à l'octet ; requête journalisée et rejouée égale ; arrêt n° 8 (mesure de la taille) avec cas sain et artefact ; aucune ligne ajoutée à l'enveloppe ; le dernier octet de chaque pièce servie gardé et l'empreinte calculée sur la pièce entière ; le journal refuse une réécriture ; mutations à la manière de la v68.
3. **`rapport-developpeur-lot-3-na-v1.md`** : exigences citées, code (fichier:ligne), essais et mutations, ce que la lettre ne fixe pas (en remarque), l'interface pour les lots 4 et 5.
4. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
