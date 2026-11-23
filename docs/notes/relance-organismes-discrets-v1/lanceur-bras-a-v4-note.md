# Lanceur de la course du bras A, version 4 : note du code

- **Date (UTC)** : 2026-11-23. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A. Travail sur processeur seul : aucun réseau hors git, aucune clé, aucune dépense, aucune instance.
- **Objet** : corriger ce que la contre-lecture du lanceur v3 a relevé (`docs/notes/relance-organismes-discrets-v1/contre-lecture-lanceur-bras-a-v3-v1.md`, `ee5befe096c8ec73f89c9bdd3f105991bb7d60b00d81b592dca3b2a5b0e98368`, verdict « à corriger ») sur le lanceur v3 (`src/controle_ia/organismes_discrets/lanceur_bras_a_v3.py`, `dae151d5a46ef2069ed3a425f264b6b5a34256be2f980954774cbc642e36d666`, laissé intact, R12).
- **Fichiers neufs, scellés** :
  - `src/controle_ia/organismes_discrets/lanceur_bras_a_v4.py` : `5409a50eb732cccae9c725f75a337ec40450d7ddefcf8172974cb5353cf3541c` (c'est l'empreinte que la configuration du lanceur doit citer) ;
  - `tests/test_lanceur_bras_a_v4.py` : `eb5de2ed997d66c5b844ae9ee9a742d5b43c6509bea92728d1458db1d509cf3c` ;
  - cette note, avec son compagnon.
  Un état intermédiaire non scellé de ces deux fichiers a été versé par la session au commit `7c4341064` (« état intermédiaire non vérifié »). Les versions ci-dessus le remplacent : seules elles font foi.
- **Garde de calcul (M-1)** : je n'y ai pas touché. Elle est corrigée sur `origin/main` (`.claude/hooks/garde_calcul.py`, commit `09ecf2e02`, R-5013 : rang de GO de deux ou trois chiffres aux deux motifs, `4fae077c…`). La copie de cette branche (`73be0638…`) **n'a pas encore cette correction**. Avant le départ de la ligne 1, la garde doit être celle de la branche principale. La règle d'identifiant du lanceur v4 lui est alignée (`\d{2,3}`).

## Corrections

| point | correction | choix et justification |
|---|---|---|
| **M-2** (ligne 1 liée au constat de départ et au plafond) | `jouer_ligne_1(…, compteur, constat, …)` appelle `exiger_constat_et_compteur` avant le premier lot | **Liaison choisie : le constat lui-même**, plutôt que son empreinte seule. C'est la plus simple qui laisse refaire les contrôles : le constat porte maintenant son empreinte (JSON canonique), et toute altération est vue. Ses clés sont fermées. Il doit porter les mêmes empreintes de configuration, de texte et de lanceur que la configuration jouée : une configuration d'essai à entropie fictive n'a donc jamais de constat. Son plafond vaut 18 USD. Le GO doit avoir un plafond d'au moins 18 USD et un périmètre égal à la ligne jouée. Le crédit et les tarifs sont relus par les mêmes gardes. **Compteur** : il doit être un `CompteurDePlafond`, avec un plafond au plus celui du constat et un taux au moins égal à carte + stockage relevés (un taux plus bas sous-compterait la dépense). Le registre et l'horloge ne sont pas relus : le constat fait foi. |
| **m-1** (inventaire) | Seul `manifeste-du-versement.json` à la racine du dossier, et son compagnon, sont exclus de l'inventaire. Un homonyme placé ailleurs est refusé. | Lettre de la contre-lecture. |
| **m-2** (écriture) | `json.dumps(…, allow_nan=False)` en mémoire d'abord, puis une seule écriture en mode « x ». `TypeError` et `ValueError` deviennent `GardeArret`, et aucun fichier n'est créé. | NaN refusé aussi : le JSON strict ne le porte pas. |
| **m-3** (GO) | L'identifiant suit une règle stricte : `GO-AAAA-MM-JJ-NN` ou `NNN` en entier, avec une date du calendrier. Une ligne du registre qui commence par `\| GO-` et dont l'identifiant est mal formé arrête (jamais sautée en silence). L'accordant doit être exactement « Lazar ». Le périmètre doit nommer « ligne 1 du bras A » (casse et blancs indifférents), et toute mention « ligne(s) N » doit valoir « ligne 1 » au singulier. | Règle du rédacteur : le texte n'écrit pas de marque de périmètre. Elle est plus stricte, jamais plus large. Le GO de la ligne 1 devra porter ce libellé dans sa cellule « périmètre ». |
| **m-4** (date du tarif) | `exiger_tarif(configuration, tarifs, maintenant)`. **Borne déclarée** : le relevé est du même jour UTC que l'horloge de départ (`maintenant`, avec fuseau obligatoire) et ne lui est pas postérieur. `constat_de_depart_ligne_1` prend `maintenant` au lieu de `aujourd_hui` et en tire aussi le jour du GO. | Lettre de 13.2 (« au jour du devis »). La ligne peut franchir minuit pendant le jeu : la borne porte sur le départ, pas sur la fin. |
| **m-5** (essais manquants) | (a) `N = 2`, `lot = 4`, `max_nouveaux = 512` refusés ; (b) motif « change l'acceptation » et motif « change la lecture de l'environnement » obtenus chacun exactement ; (c) témoin bénin laissé honnête à sa seule dose ; (d) cumul égal au plafond (18 USD) et coupe à exactement 256 actions sur 1 280 n'arrêtent pas, 257 arrête ; (e) rejeu réel : `lanceur_bras_a_v2.rejouer` sur un modèle jouet neuf portant six adaptateurs, honnête d'abord à l'échelle 0 puis chaque adaptateur à l'échelle 1, chacun avec son propre état | Pour (e), seule la génération est simulée. Le chargement des états, l'échelle et la garde d'état de phase sont réels. |
| **m-6** (facultatif, fait) | `fabriquer_condition(…, dose_recue=False)` : la dose reçue est calculée seulement si on la demande (les quatre doses et le témoin bénin, sur 128 épisodes). Jamais pour le témoin identité ni pour les jumeaux de vérification. | |
| **m-7** (facultatif, non fait) | Le lanceur ne confronte pas son empreinte au texte scellé. Le texte ne cite pas le lanceur : c'est à la configuration scellée de nommer les deux. | |

Le reste ne change pas par rapport à la v3 : configuration, graines, fabrication, versement, destruction, commande. `_main` passe l'heure UTC courante comme `maintenant`.

## Essais

- `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_lanceur_bras_a_v4.py` : **141 passent** (≈ 2 à 4 min). Ce sont les 67 essais de la v3, portés sur la v4, plus les essais des corrections. Chaque garde nouvelle a un cas sain et un artefact (R5) : constat sain et 13 constats invalides, compteurs aux bornes et 5 compteurs refusés, inventaire sain et homonymes, écriture saine et 3 contenus non sérialisables, GO à deux et trois chiffres et 9 artefacts, 3 périmètres sains et 10 refusés, 3 relevés sains et 6 refusés.
- Les essais de la ligne 1 jouent une configuration **déclarée réelle** sur un texte fictif, dans un dossier temporaire. M-2 l'exige : une configuration fictive n'a pas de constat.
- **Garde statique du cloisonnement** (`cloisonnement_bras_a_v13.violations_de_la_garde_statique`) : `[]` sur chacun de mes deux fichiers. Sur la racine entière, elle rend 23 violations, **toutes dans les fichiers de l'autre agent** (`aire_conditionnelle_bras_a_v1.py`, `cloisonnement_bras_a_v14.py`) et aucune dans les miens. Je n'emploie aucun nom réservé ni aucun motif interdit.

## Campagne de mutants

Elle a été menée sur des copies, dans le dossier de travail de la session : le module muté est chargé par un `conftest` sous son nom réel, et les essais sont copiés. Aucun fichier du dépôt n'a été muté. **78 mutants** : 17 pour M-2, 2 pour m-1, 2 pour m-2, 9 pour m-3, 4 pour m-4, 6 pour m-5, 3 pour m-6, et 35 sur les gardes reprises de la v3.

- **Première passe** (sans les trois essais lents) : 69 tués.
- **Survivants** :
  - Quatre étaient couverts par les essais lents : témoin bénin de la dose reçue dans `fabriquer_les_six`, refabrication, 384 pas, témoin identité.
  - Un mutant était mal écrit (texte présent deux fois).
  - Cinq ont révélé des essais manquants : relevé du plafond avant le premier lot, périmètre au pluriel, jour du GO tiré de l'horloge du constat, décodage sous le témoin identité, déplacement planté sous le témoin identité.
- J'ai ajouté six assertions ou essais. **Les 78 mutants sont tués.**

## Ce qui reste (hors de ce code)

1. Aligner la garde de calcul de cette branche sur `origin/main` (M-1) avant le départ.
2. Écrire la ligne de GO de la ligne 1 avec le périmètre « ligne 1 du bras A ».
3. Faire contre-lire la v4 par un agent neuf (R2).
4. Citer `5409a50e…` dans la configuration du lanceur.
