# Vérification habilitée des corrections du lanceur de l'étape de discrétion du bras A, version 2 — sans interne — v1

Écrit par le lecteur habilité côté moniteurs (Claude Fable 5.2, le même que pour la contre-lecture), le 20 novembre 2026, sous GO-2026-11-20-21. Verdicts, comptes, chemins et empreintes seulement. Ce qui les fonde est dans une pièce interne, qui ne sort pas : `docs/notes/bras-a-moniteurs-v1/verification-habilitee-lanceur-discretion-v2-v1.md`.

## Verdict

**Les treize corrections et les deux décisions sont faites ; une porte une réserve, sans effet sur un calcul.** Commit vérifié : `848c17649d3c324461747daa99fb8784c88a8baa`.

| | objet | verdict |
|---|---|---|
| C1 | seconde reprise du même moniteur après une panne de transport | corrigée |
| C2 | reprise comptée et inscrite à chaque relance | corrigée |
| C3 | vérification de la lecture commune remontée avant la production | corrigée |
| C4 | configuration de la base comparée à sa ligne du registre | corrigée |
| C5 | quatre modules appelés cités par leur empreinte | corrigée |
| C6 | relevé des jetons de fin sur une configuration de relevé | corrigée |
| C7 | énoncé de la tâche gardé à l'identique de celui de l'agent | corrigée |
| C8 | douze gardes sans artefact | corrigée (onze artefacts ; une garde redondante devenue assertion, admis) |
| C9 | versions et commit au manifeste du lanceur | corrigée avec réserve : un champ du manifeste reste vide si la production s'arrête sur une panne |
| C10 | cas de refus sans réparation dit dans la notice | corrigée |
| C11 | empreintes vérifiées avant l'import du module d'entrée | corrigée |
| C12 | précision ajoutée à l'attestation, par erratum | corrigée |
| C13 | deux phrases de la pièce sans interne | corrigée ; aucune fuite dans la version 2 |
| D1 | sorties de lecture scellées morceau par morceau | corrigée |
| D2 | registre propre au bras | corrigée |

## Pièces vérifiées, chacune égale à son compagnon

| pièce | chemin | empreinte |
|---|---|---|
| lanceur, version 2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v2.py` | `c3840745ccaad9b889b676ff7ac2450397f60192b72391e2c42ec37eb5e5ca7e` |
| ses essais | `tests/test_bras_a_v2_habilite_lanceur_discretion_v2.py` | `7729f5bdd09c99af56170663b37899365ef985395d61ec3363b1c9e9141e7760` |
| gabarit de la configuration, version 2 | `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-gabarit-v2.json` | `9a944d74986445deb096f13cc834456e624592a08ab24fd5f164c78d2d1e25e9` |
| notice, version 2 | `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-lanceur-discretion-v2.md` | `9d91578e3fc688f76615464dfcbef103076dfa17f0a149cb9e0910f356c334f6` |
| erratum 1 de l'attestation | `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1-erratum-1.md` | `6acac663ec798300211f83e45a1bf1c298f498a58b56716d5b33a1fb03b7d41f` |
| pièce sans interne du développeur, version 2 | `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v2.md` | `f9c935d12cff2a4c9e24f47835081a1ca3ec30da868db23193bff43054b63387` |
| script de l'épreuve par retrait, version 2 | `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-lanceur-discretion-v2/epreuve_retraits_lanceur_v2.py` | `cb7a10354bbb93b760ed30978f678a664587d9f639a9073bd93786d8dc9f0e7d` |
| ses relevés, première et seconde passe | même dossier | `c3791dd4e1db6afa373ae45e9c94a2df3dba644a41993b7ae787e5f27a0952a1` ; `e5c9495a478c54a49c97556ae55c9ca0ced7b06477810476d11a50a452188a5b` |

## Comptes

| épreuve | compte |
|---|---|
| essais du lanceur, version 2 | 30 passent sur 30 |
| les trois fichiers ciblés ensemble | 42 passent sur 42 |
| épreuve par retrait, rejouée en entier sur le fichier d'essais final | 70 retraits mordent sur 70, en une passe ; fichiers remis à l'identique |
| modules cités par empreinte dans le gabarit | 13 |

## Demande 19

**6 programmes** nomment le fichier des rangs sous `src` et `scripts`, recompté : quatre versions du module des autres moniteurs, deux versions du lanceur. Le sixième est la version 1 du lanceur, gardée en place ; aucun programme neuf ne lit ce fichier. Tous sont sous des dossiers dont le nom commence par `bras_a_v2_habilite`. Aucun n'ouvre le fichier après son écriture ni ne parcourt son dossier. Trois fichiers d'essais le nomment aussi, sous `tests/`, hors du compte demandé.

## Ce qui reste, hors des corrections

1. Un essai du chemin réel sur la machine de calcul, avant la course.
2. Le module de graines qu'importe le module d'entrée n'est pas cité par empreinte : à trancher par la session principale.

Non ouvert : aucun résultat, aucun texte du préenregistrement, aucun module de graines, aucun fichier interdit par le mandat. Aucun poids chargé, aucune dépense, aucun refus d'outil. Ni commit ni poussée.
