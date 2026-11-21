VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DES DOSSIERS DES LOTS 1 À 3. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lot 4 (surcharge d'`appel`, adaptateur Claude neuf) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21, sur le mot de la mère (08:04Z : « les lots 3 à 5 peuvent suivre de la même façon dès que leurs mandats sont prêts »). **Ne part qu'une fois le lot 3 vérifié « Conforme »**, dont il dépend en code ; il se joue avec le lot 5. Code par un développeur O, vérifié par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni la conception, ni les lots 1 à 3, ni aucun orchestrateur. Tu signes « développeur du lot 4 du véhicule NA-1, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **La conception v5** (`/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md`, `1b7f6822…`) et son contrôle (`conception-vehicule-v5/controle-v1/`, `4b369004…`), qui priment sur la v4. En particulier : § 0 bis ; § 2.3 (surcharge d'`appel` : routage, part de la clé, garde de motifs, journal, égalité, refus avant le noyau ; adaptateur Claude neuf) ; § 2.13 (gardes héritées et refus écrits, par rôle ; A3 et A14 désactivées par écrit) ; § 5.1 (ligne `appel_garde`) ; § 6 (arrêts n° 1, n° 12, n° 13, n° 16 au point d'envoi) ; § 7 (lot 4).
- **La v9 scellée** et ses compléments, sur `origin/main` (`prereg/ideation-nouvelles-attaques-v1/`) : parts par clé, plafonds, D11, envoi refusé sans coût, `hors_course`, conservation des réponses brutes.
- **Le relevé du lot 0** (`docs/notes/ideation-nouvelles-attaques-v1/lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md`, `10ac79ec…`) : Q1 (textes ajoutés par les adaptateurs), Q2 (noms des adaptateurs et routage), Q5 (statuts), Q7 (faux fournisseur), Q8 (coûts par rôle), Q10 (réponses brutes), Q13 (coût d'un envoi refusé).
- **Les lots 1 à 3 vérifiés** : code, rapports et interfaces (dossiers et empreintes donnés au départ).
- **La base** : la v68 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/`) et l'orchestrateur en lecture seule (`/home/user/lciric/ideation-organism`, `a41b7b50…`).

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-4/`.

1. **Mélange `AppelGardeNA`** (suffixe `_na_v1`) : routage par rôle ; part de la clé et cumul compté ; garde de motifs du lot 2 au point d'envoi ; journal du lot 3 ; égalité entre ce qui est journalisé et ce qui part ; refus avant le noyau (« non envoyé », sans coût) ; « refus écrit » ; lecture des statuts et de l'état du relais ; `hors_course`. **L'interface avec le lot 6** (ce que le mélange attend de la classe de génération : numéro, table scellée, parts, pires par rôle, journal, fonction qui rend l'identifiant de la case d'une session) est écrite dans ton rapport, et figée.
2. **Adaptateur Claude neuf**, sans texte système, avec la conservation des réponses brutes ; tables des lignes à part.
3. **Relevé au faux fournisseur** de ce que l'outil envoie sans texte système (§ 2.3, § 7) : **écrit et éprouvé contre le faux fournisseur seul, sur `127.0.0.1`**. Le jeu derrière le vrai relais n'est pas à toi : il demande un mot de la mère, et se fait avant l'écriture de l'additif. Tu rends le programme de relevé prêt à jouer et sa sortie contre le faux fournisseur.
4. **Essais** : arrêts n° 1, n° 12 (D11), n° 13, n° 16 au point d'envoi, chacun avec cas sain et artefact (R5) ; envoi refusé sans coût ; `hors_course` ; réponses brutes conservées ; aucun texte système envoyé ; journal égal à l'octet à l'envoi ; mutations à la manière de la v68.
5. **`rapport-developpeur-lot-4-na-v1.md`** : exigences citées, code (fichier:ligne), essais et mutations, ce que la lettre ne fixe pas (en remarque), l'interface pour le lot 6.
6. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, **aucun relais lancé**. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
