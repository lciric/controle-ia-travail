# Rapport du développeur — moteur v9-v8q (option --cle-gemini), voie abonnement v7, script de vague v3 (v1)

- 24 novembre 2026, vers 22:20Z. Développeur : Claude Opus 5.5, session des collisionneurs (`session_016QhUrsc1rhjmmiLEmqPygF`). Classe B : contre-lecture par un autre modèle (un Opus neuf), puis vérification des corrections par le même. **Rien n'est lancé avec ces pièces** (consigne de la mère, R-5322).
- Motif : le 24 à 21:48Z, la clé que le moteur v8m lit sous un nom fixe (`GEMINI_API_KEY`) a rendu HTTP 402 « prepayment credits are depleted ». Remplacer cette variable dans l'environnement au lancement a été refusé par le classifieur de la session (`pannes-abonnement-v1/refus-de-credit-google-2026-11-24-v1.md`, `6807a3e9…`). La mère demande une option du moteur pour nommer la clé de Google, sur le modèle de `--cle-openai`.

## Pièces
| pièce | empreinte | base |
|---|---|---|
| `collisionneur_v9_v8q.py` | `047489b8…` | copie du `collisionneur_v9_v8m.py` (`420394f9…`, intact) |
| `test_collisionneur_v9_v8q.py` | `f7f8b951…` | neuf |
| `abonnement-v1/voie_abonnement_v7.py` | `fd1c37b7…` | copie de la v6 (intacte) |
| `reprise-v8d-v1/vague_abonnement_v3.sh` | `51c27240…` | copie de la v2 (intacte) |

## Changements du moteur (v8m → v8q), et seulement ceux-là
1. En-tête « v9-v8q » ; `VERSION = "collisionneur-v9-v8q"`.
2. Constantes `PREFIXE_CLE_GEMINI = "GEMINI_API_KEY"` et `NOMS_CLE_GEMINI_REFUSES = ("GEMINI_API_KEY_3",)` (clé épuisée, mot de la mère).
3. `fixer_composition(..., nom_cle_gemini=None)` : défaut `NOMS_CLES["gemini"]`. Le nom passe par le même contrôle de forme que les autres (`MOTIF_NOM_VARIABLE`). Il doit commencer par `GEMINI_API_KEY`, sinon arrêt nommé, code 1. Un nom refusé arrête aussi, code 1. Le nom est donné en `m["nom_cle"]` aux seules espèces dont le fournisseur est Gemini (Argon, Carbon, Neon).
4. Les trois lectures de la clé de Google sont l'envoi en flux (`appeler_gemini`), l'envoi par lot (`appeler_gemini_lot`) et le comptage (`compter_gemini`). Elles lisaient `os.environ.get("GEMINI_API_KEY")` ; elles lisent désormais `os.environ.get(m.get("nom_cle") or NOMS_CLES["gemini"])`. Le message d'absence nomme la variable, jamais sa valeur.
5. Option `--cle-gemini` (étages I, II et III), défaut `GEMINI_API_KEY`, passée à `fixer_composition`.
6. `declarer_cle_gemini(dossier)`, appelée après `declarer_options`. Elle affiche le nom de la variable, jamais sa valeur. Elle l'écrit au journal (`{"nom_cle_gemini": NOM, "quand", "script"}`) au premier lancement qui emploie un nom autre que le défaut, puis à chaque changement de nom. Elle ne fait rien si le run n'a aucune espèce de Google. Le nom de clé n'est **pas** scellé dans `especes.json`, comme `--cle-openai` : il peut changer d'une vague à l'autre, et ce changement est journalisé. `essais_journal`, `depense` et `verifier` ne lisent que les entrées qui portent leurs clés propres ; la nouvelle entrée ne les touche pas.
- `verifier_cles` lit déjà `m["nom_cle"]` : une variable nommée absente arrête avant tout envoi, code 1.
- Reprise d'un run commencé sous v8m : l'empreinte du script change. Le moteur exige donc `--reprise`, consigné au journal (« changement_script »), comme pour toute reprise par un autre script.

## Voie v7 et script de vague v3
- Voie v7 : la table `MOTEURS` admet `v8q` par son chemin et son empreinte (`047489b8…`) ; la commande `v8q` s'ajoute aux commandes. Rien d'autre ne change. `--cle-gemini` passe au moteur avec les autres arguments du programme.
- Script v3 : il appelle la voie v7 au lieu de la v6 ; rien d'autre ne change. Usage prévu, non lancé :
  `bash …/vague_abonnement_v3.sh v8q DOSSIER QUESTION GO EFFORT PLAFOND --especes… --cle-gemini GEMINI_API_KEY_2 --reprise`

## Essais (sans réseau ; transport intercepté, valeurs factices)
- `PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/test_collisionneur_v9_v8q.py` : **14 sur 14 passés**. Ils couvrent :
  - le défaut, inchangé ;
  - le nom donné aux seules espèces de Google ;
  - le refus d'un autre préfixe, d'une clé épuisée et d'un nom mal formé ;
  - la lecture de la variable nommée par l'envoi en flux, avec et sans option, et par le comptage ;
  - l'absence de la variable nommée, en flux comme par lot : rien ne part et aucune valeur n'est affichée ;
  - le journal du nom, avec un passage au premier lancement, une répétition, un retour au défaut et un run sans Google ;
  - la ligne de commande, avec une clé épuisée et une clé absente : code 1, aucun journal ;
  - un devis identique octet pour octet à celui de la v8m ;
  - l'absence de toute lecture à nom fixe.
- **Mutations** (copies du moteur, une garde retirée) : quatre sur quatre tuées. Il s'agit du refus de la clé épuisée, du contrôle du préfixe, de l'envoi en flux à clé fixe et du journal muet.
- La voie v7 sur la v8q et la voie v6 sur la v8m rendent un devis identique, octet pour octet, sur la question v4 des idées intéressantes. À travers la voie v7, `--cle-gemini GEMINI_API_KEY_3` est refusée, code 1, et rien n'est écrit.

## Limites déclarées
- `GEMINI_API_KEY_3` est inscrite dans le code comme refusée : c'est une consigne d'exploitation, que la mère pourra retirer par une version neuve.
- L'option ne vérifie pas le crédit de la clé nommée : un 402 reste possible, et le moteur le rend comme avant (échec sans coût).
- Choisir une autre clé reste une décision de Lazar ou de la mère, au lancement : `GEMINI_API_KEY_FREE`, par exemple, n'est accordée que pour Carbon et Neon (R-5294).
