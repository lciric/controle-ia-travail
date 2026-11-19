# Notice — préparation des lectures des deux moniteurs à modèle de langue, sous identifiants opaques — v1

**En bref.**
- Un paquet frère, `bras_a_v2_habilite_preparation`, prépare ce que l'étape de production lit : un fichier scellé de demandes à trois champs (identifiant opaque, message, graine), dans l'ordre trié des identifiants. L'étape de production ne voit ni condition, ni tâche, ni épisode, ni pas.
- 8 essais passent ; chacune des 20 gardes, retirée seule, fait échouer un essai.
- Pièce de classe B, à contre-lire avec la version 7 du module des autres moniteurs.

Qui : développeur habilité côté moniteurs, le 19 novembre 2026. Aucun résultat lu, aucun poids chargé, aucune dépense, jamais la suite d'essais complète. Aucun outil refusé.

| rôle | chemin | empreinte |
|---|---|---|
| paquet | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/__init__.py` | `7cd9e03c131da522534ba5a97ab979294a375de3aa4c1d553089c2e67aa80321` |
| module | `…/bras_a_v2_habilite_preparation/preparation_des_lectures_v1.py` | `72d2216747c102bc5dca12227bb6e6648c20a121b72edcaefa51c817ad037dae` |
| essais | `tests/test_bras_a_v2_habilite_preparation_des_lectures_v1.py` | `6b1acc0785013f6a2fc92101c432584d47b899fc20711070823bcdd7c8285405` |

Commit `2ee2a8cf`. Essais ciblés : `PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_preparation_des_lectures_v1.py` ; dernière ligne : `8 passed`.

## Ce que fait le module

- `preparer` reçoit les actions des cinq conditions, l'énoncé de chaque tâche, la table des identifiants opaques (identifiant → clé d'action), l'entropie de la configuration du bras et le nom du moniteur. Il construit le message avec la fonction du module des deux moniteurs (`moniteurs_langue_v2.py`, `2400c138…`), tire la graine de chaque lecture par la clé de ce module, et rend les demandes sous identifiants opaques, triées, plus un bilan par condition.
- Pour le juge, seules les positions de son sous-échantillon sont préparées.
- `ecrire_les_demandes` écrit et scelle `demandes-{moniteur}.jsonl` ; le bilan par condition s'écrit **à part** (`ecrire_le_bilan`), hors du dossier que lit la production.
- `lire_les_demandes` rend à l'étape de production les demandes au format que lit `lire_avec_raisonnement`, la consigne étant chargée par son empreinte.

## Pourquoi un paquet frère

Les essais des versions antérieures du module des autres moniteurs portent une garde statique sur les importations du paquet `bras_a_v2_habilite` ; un module de plus qui importe ses voisins les ferait échouer. Le paquet frère laisse ces essais intacts.

## Avec la version 7 du module des autres moniteurs

`preparer` prend la table comme un dictionnaire : avec la version 7, on lui passe le champ `table` de ce que rend `tirer_la_table_opaque`. Celui qui prépare tient donc la table ; il la scelle à part et ne passe à la production que les demandes et l'engagement (l'empreinte du fichier de la table). Les essais de ce paquet tirent leur table avec la version 6, qui reste en place.

## Ce qui reste

- Le lanceur qui enchaîne préparation, production, ouvertures et lecture commune n'est pas écrit (après scellement du texte).
- **Limite de l'opacité, à dire au texte et au contre-lecteur.** Une demande porte le message, donc le texte de l'action, et la graine de sa lecture, qui vient de l'entropie du bras et de la position de l'action. Qui tient les épisodes du rejeu retrouve, par le texte, l'action d'une demande et donc sa condition, sans la table ; qui tient seulement l'entropie du bras retrouve par la graine la position (tâche, épisode, pas), pas la condition : la clé de graine ne porte pas la condition. L'opacité vaut donc pour l'étape de production telle qu'elle est écrite (elle ne reçoit ni condition, ni épisodes, ni entropie, ni table) et pour les fichiers qu'elle rend (identifiant, score et trois champs à listes fermées) ; elle ne vaut pas contre une session qui tiendrait aussi les épisodes. L'entropie propre de la table ferme une voie (refaire la table), pas celle-là.
