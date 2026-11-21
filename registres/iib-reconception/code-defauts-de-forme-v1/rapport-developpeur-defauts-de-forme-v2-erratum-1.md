# Erratum 1 au rapport du développeur en version 2 — lanceur de session du saboteur à budget

Date : 2026-11-19. Pièce d'instrument (classe B). Complète `rapport-developpeur-defauts-de-forme-v2.md` (`534c84b1…3c7b`, intact) après la vérification `verification-corrections-code-lanceur-v2-cl1.md` (`3ece4ffe…14d1`, empreinte vérifiée) : « autorisable », quatre mineurs neufs. Rien poussé, aucun appel au loueur, aucun refus d'outil.

- Commit : `11cdc0a9`, par-dessus `806bce0f`, branche locale `prep/iib-code-v5`.
- Fichiers touchés :
  - `scripts/lancer_iib_v2.sh` : `dba3e09769e97e7304600924c4d6c43077412e25347edb76dee193c627947c96`
  - `tests/test_iib_lanceur_forme_v2.py` : `4f223f74a0232322aa00049b6f02718fec09d6846905a23ec6f57ef6388adf1f` (156 essais, 136 avant)
  - `src/controle_ia/iib/location_v1.py` : inchangé, `6446a304357338ab5a3a4a92de9eb8c0225db86eeec91541ab95dd25b6b92db3`

## Ce qui change, point par point

| Point | Correction | Essais (sain, artefact) |
|---|---|---|
| 1. États d'arrêt | La variable `IIB_DESTRUCTION_ETATS_ARRET` est retirée ; la liste `exited stopped` est fermée, écrite dans le code. La variable posée dans l'environnement est un refus (code 2). Une instance qui tourne n'est jamais détruite par cette sous-commande. Un état d'arrêt d'un autre nom est refusé en clair, avec la phrase « le code changera en version nouvelle ». | `test_erratum_n1_…` (sans variable, variable retirée, variable interne) ; cas `etat_d_arret_d_un_autre_nom`, `etats_elargis_par_variable` |
| 2. Étiquette exacte | L'étiquette de l'inventaire doit être égale à celle consignée à la création (60 caractères au plus), et non plus commencer par elle. | `test_erratum_n2_…` (attaque du contre-lecteur, hors de la liste des intouchables) ; cas `etiquette_au_meme_debut`, `etiquette_plus_courte` |
| 2. Liste des intouchables | Liste vide ou absente : refus, sauf `IIB_AUCUNE_INTOUCHABLE=oui`, dit sur la sortie et dans `destruction.txt`. L'attestation avec une liste non vide est refusée comme contradictoire. | cas `liste_absente`, `liste_vide`, `attestation_autre_mot`, `attestation_contredite` ; `test_erratum_intouchables_absentes_avec_attestation_…` (sain) |
| 3. Essais de création | Tous les refus de `creation` sont maintenant au-dessus de l'écriture de `essai_creation` : un refus ne consomme plus un des trois essais. | `test_erratum_n3_…` : deux refus sans ligne d'essai, puis la création saine porte l'essai 1 |
| 4. Module de lecture | Le lanceur vérifie l'empreinte de `location_v1.py` avant tout emploi. Empreinte attendue : `IIB_LOCATION_SHA256`, ou celle de la liste des empreintes du code de la configuration (`marqueurs.EMPREINTES_CODE_IIB` de `config.json`) ; les deux présentes doivent être égales. Absente, illisible ou différente : aucune création (code 2), aucune destruction (code 4, aucun appel), réponse de création gardée entière et non lue (code 4). | `test_erratum_n4_…_refus` (6 cas, dont le module menteur du contre-lecteur) ; `test_erratum_n4_empreinte_lue_dans_la_configuration_cas_sain` |
| 5. Journaux de la surveillance | À la fin de la surveillance (`FIN`, `ARRET`, `REFUS`), une copie datée, avec empreinte, de `surveillance.txt`, `progres.txt`, `journal-dernier.txt` et `journal-instance.txt` va dans `traces-location/` (`fin-de-surveillance-*`). Rien d'autre ne change au régime. | `test_erratum_surveillance_copie_datee_…` (fin, puis arrêt : deux copies, aucune écrasée) |
| 6. Attestation du rapatriement | Une ligne `rapatriement_atteste <date UTC> RAPATRIEMENT_VERIFIE=oui instance=<ID> par=<compte>@<machine>` est écrite dans `lancement.txt`, une fois toutes les gardes passées, juste avant la commande de destruction. | `test_erratum_rapatriement_atteste_…` (absente après deux refus, présente et de la forme attendue après une destruction) |

Les attaques en version 2 du contre-lecteur, rejouées telles quelles depuis son fichier : 12 sur 12 tenues (N1 et N2, qui échouaient, passent).

## Ce que l'erratum change au rapport en version 2

- **§ 5, points à trancher** : le point 3 (porte `IIB_DESTRUCTION_ETATS_ARRET`) est clos, la variable n'existe plus. Le point 2 (journal de la surveillance) est réduit : le régime reste, une copie datée est gardée à la fin. Le point 5 (attestation) est réduit : elle laisse une ligne écrite ; elle reste une parole de l'exécutante, pas un fait lu par le programme. Restent ouverts les points 1, 4 et 6, et ces deux restes.
- **§ 6** : `src/controle_ia/iib/location_v1.py` **entre dans la liste des empreintes du code** de la configuration ; c'est de là que le lanceur lit l'empreinte attendue. Tant que la configuration en version nouvelle n'existe pas, il faut `IIB_LOCATION_SHA256` dans `ENVI`, sinon tout refuse.
- **§ 6, `ENVI` de l'ordre neuf** : retirer toute mention de `IIB_DESTRUCTION_ETATS_ARRET` ; `IIB_INSTANCES_INTOUCHABLES` doit être non vide (les machines des autres chantiers relevées à l'inventaire), ou `IIB_AUCUNE_INTOUCHABLE=oui` posée à dessein.
- **Condition avant emploi réel, renforcée** : si l'outil réel nomme l'arrêt autrement que `exited` ou `stopped`, la destruction refusera et il faudra une version nouvelle du code. À relever sur le poste de l'exécutante avant l'ordre neuf, avec l'option `-y` et la forme des sorties.

## Sortie brute des essais

Fichier : `sortie-essais-cibles-v2-erratum-1.txt`, dans ce dossier.

```
$ PYTHONPATH=src python3 -m pytest -q --tb=line -rfE tests/test_iib_lanceur_forme_v2.py tests/test_iib_scripts_v1.py tests/test_iib_amorce_v1.py
4 failed, 220 passed in 56.35s      (les quatre échecs, dans tests/test_iib_amorce_v1.py : ModuleNotFoundError: No module named 'torch')

$ PYTHONPATH=src python3 -m pytest -q tests/test_iib_lanceur_forme_v2.py
156 passed in 33.77s

$ attaques en version 2 du contre-lecteur, fichier tel quel
12 passed in 2.50s

tests/test_iib_lanceur_v1.py : non collecté (torch absent), comme avant.
```
