VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DES DOSSIERS DES LOTS 1 À 5. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lot 10 a (colonne « matière première » : chargement et garde) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21. Lot obligatoire (mère, 07:51Z), qui n'attend plus aucun mot depuis la lecture B (08:00Z). **Ne part qu'une fois les lots 3, 4 et 5 vérifiés « Conforme »** ; il se joue avec le lot 6. Code par un développeur O, vérifié par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni la conception, ni les lots 1 à 6, ni aucun orchestrateur. Tu signes « développeur du lot 10 a du véhicule NA-1, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **La conception v5** (`/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md`, `1b7f6822…`) et son contrôle (`conception-vehicule-v5/controle-v1/controle-conception-vehicule-na-v5-v1.md`, `4b369004…`). En particulier : § 0 bis (lecture B de la v9, l. 83 ; état « garde seule » écrit à la pièce de relevés ; état « lecture de fin » soumis à l'additif, à l'arrêt n° 14, au devis et au mot de Lazar) ; § 2.14 (colonne « matière première » : chargeur, interrupteur à trois états, garde par énoncé entier et par empreinte, contrôle des pièces fixes au départ, taux de faux refus) ; § 7 (lot 10 a).
- **Le point 4 du contrôle de la v5** : la ligne de l'état 1 est une **sixième ligne** de la pièce de relevés, hors des cinq libellés fixes ; son libellé fixe viendra à l'additif du véhicule. Tu écris contre un **libellé d'essai**, déclaré comme tel, et une ligne absente refuse le départ.
- **Le relevé du lot 0** (`docs/notes/ideation-nouvelles-attaques-v1/lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md`, `10ac79ec…`).
- **Les lots 3, 4 et 5 vérifiés** : code, rapports et interfaces (dossiers et empreintes donnés au départ).

**Tu n'ouvres ni le registre servi réel (`3bcb94e6…`), ni la branche de matière première, ni aucune branche de quarantaine.** Tu écris et tu éprouves sur un **registre d'essai** aux lignes inertes, que tu fabriques, au format que la conception décrit (empreintes d'énoncé seules).

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-10-a/`.

1. **Module `matiere_premiere`** (suffixe `_na_v1`) : chargeur du registre (empreintes d'énoncé seules, empreinte du registre vérifiée) ; interrupteur à trois états ; garde de la colonne par énoncé entier et par empreinte ; contrôle des pièces fixes au départ (dont la sixième ligne de la pièce de relevés) ; taux de faux refus mesuré sur le registre d'essai.
2. **Essais** : garde de la colonne et chacun des trois états, avec cas sain et artefact (R5) ; ligne de l'état 1 absente ou d'empreinte fausse : départ refusé ; état « lecture de fin » refusé sans additif ; mutations à la manière de la v68.
3. **`rapport-developpeur-lot-10-a-na-v1.md`** : exigences citées, code (fichier:ligne), essais et mutations, ce que la lettre ne fixe pas (en remarque), l'interface pour les lots 8 et 9.
4. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte, le registre servi réel non ouvert. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
