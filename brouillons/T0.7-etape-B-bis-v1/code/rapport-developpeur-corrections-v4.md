# Rapport du développeur sur les corrections du code de l'étape B bis de T0.7 (modèle A), v4 — instance 60670453 (R-2795)

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu sous `diag/`, `runs/`,
`donnees/` ; aucune machine, aucun appel réseau, aucune dépense ; aucun vrai outil `vastai` appelé (faux outil seulement).

- **Auteur** : « modèle A ». **Date (UTC, `date -u`)** : 2026-11-14, de 22:54 à 23:05.
- **Objet** : la seule correction demandée par la mère avant la contre-lecture de la répétition, recommandée au § 6 de
  `rapport-developpeur-repetition-carte-v1.md` (`a053aa8f…`) : ajouter **60670453** (instance d'une autre session, apparue le
  14 novembre, R-2795) à la liste de la course, avec son essai, et faire lire la même liste par le mode répétition.
- **Commit du code** : `bbc2e1c86314560988eaadc5b739b0e34a3c58c0` (branche `prep/t07bbis-code-v1`, jamais poussée) ; cette note et la
  sortie des essais : commit suivant. Les notes antérieures ne sont pas réécrites (R12).

## Fait

| fichier | fait | empreinte |
|---|---|---|
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | `INSTANCES_D_AUTRES_SESSIONS` : six identifiants, 60670453 ajoutée (58936096, 58936099, 58936100, 60480302, 60599797, 60670453) ; commentaire : liste unique, lue aussi par la répétition. Aucune autre ligne. | `642f9004ab8f51cff2308bee336145971e84c171b65b2a41fdba754794f0d1da` |
| `scripts/repetition_carte_bbis_v1.py` | ne porte plus sa propre copie de la liste : `from controle_ia.t07bbis.registre_bbis_v1 import INSTANCES_D_AUTRES_SESSIONS` (lue telle quelle). Aucune autre ligne. | `229310db482f60695690925928de1e1f4a39000205bfc8155056f37d3ec28ce2` |
| `scripts/amorce_bbis_v1.sh` | `MIN_ESSAIS` 86 → **87** (interprétation 25 : un essai de plus sur l'arbre de l'instance) et son commentaire. Aucune autre ligne. | `cdebee4befd5378b1be01d9032be757a996b29ca9d98331a912fb85a3eefd6ee` |
| `tests/test_t07bbis_chaine_instance_v1.py` | essai neuf `test_instance_60670453_refusee_comme_cible_admise_comme_temoin` : six identifiants distincts dans la liste ; **refusée comme cible** par `lancer_bbis_v1.sh detruire` (aucune commande imprimée), `exiger_identifiant_a_detruire` et `exiger_absence` ; **admise comme témoin** : destruction d'une autre instance jouée contre le faux `vastai`, puis `verifier-destruction 123456 60670453` → « DESTRUCTION PROUVEE … témoin 60670453 présent » ; artefact : 60670453 absente de la liste → « témoin 60670453 absent », code 2. | `f5ab794a5b65049e78058299ed36cf1aa5cb6f43f2c02b1900193d6f3b00e6e2` |
| `tests/test_repetition_bbis_v1.py` | essai neuf `test_la_repetition_lit_la_liste_de_la_course` : la liste de la répétition **est** l'objet de la course (`is`) ; aucune affectation de la liste dans le script ; 60670453 refusée comme cible et admise comme témoin par les gardes de la répétition. | `4cc1eab9c4deb81dc3ecd8984750e32a01f680c4abe96d7725f8b617f8e6cc12` |

Aucun autre fichier ne change (`lancer_bbis_v1.sh`, `lancer_repetition_bbis_v1.sh` et `amorce_repetition_bbis_v1.sh` compris ; la
liste en commentaire de `lancer_repetition_bbis_v1.sh` portait déjà les six identifiants).

## Décomptes

- Arbre complet : **119 passés** (109 de la course + 10 de la répétition), 4 min 29 s.
- Arbre de l'instance simulé au commit `bbc2e1c8` (même procédure, motifs inchangés) : **87 passés, 22 sautés** (les mêmes 22
  sautés) ; `MIN_ESSAIS = 87`.
- Liste des 90 fichiers de la fiche (`fichiers-fiche-code-bbis-v1.txt`, `8e3d0799…`) recalculée à ce commit : inchangée.
- Sortie : `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v4.txt`, `bf556cde2077e0add69fe8691c798a99f047428ebf9f16ad48a3c842f0cfcbd5`.

## Mises à jour des commandes

- Note v2, § 3, geste 0 (et sa mise à jour de la v3) : le code éprouvé est maintenant celui de `bbc2e1c8` ; comparer avec
  `git diff --quiet bbc2e1c86314560988eaadc5b739b0e34a3c58c0 HEAD -- $(cat "$L")` ; essais attendus sur l'arbre complet :
  **109 passés** pour `tests/test_t07bbis_*.py` (119 avec `tests/test_repetition_bbis_v1.py`).
- Répétition (`rapport-developpeur-repetition-carte-v1.md`) : l'empreinte du script change (`229310db…`, passée à l'instance par
  `SCRIPT_SHA256`, calculée par `commande` au commit) ; essais de l'arbre de l'instance attendus : « 87 passed, 22 skipped » et
  minimum 87 (lu au commit par l'amorce de répétition). Le reste des gestes est inchangé.

Aucun refus de la garde d'isolement dans ce tour.
