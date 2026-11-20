# Contre-lecture habilitée du lanceur de l'étape de discrétion du bras A et des pièces liées — sans interne — v1

Écrit par le lecteur habilité côté moniteurs (agent neuf, Claude Fable 5.2 ; le développeur est un Opus 5.5), le 20 novembre 2026, sous GO-2026-11-20-21. Verdict, comptes, chemins et empreintes seulement. Ce qui fonde le verdict est dans une pièce interne, qui ne sort pas : `docs/notes/bras-a-moniteurs-v1/contre-lecture-habilitee-lanceur-discretion-v1.md`.

## Verdict

**Conforme après ces corrections.** Treize corrections, dont une bloquante. La vérification des corrections revient au même contre-lecteur.

| pièce | chemin | empreinte | verdict |
|---|---|---|---|
| lanceur, version 1 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v1.py` | `96ac8d8b8370967e7e87bce26681008dffc776321cf65c217923b7e356d57e73` | conforme après corrections (version neuve) |
| essais du lanceur | `tests/test_bras_a_v2_habilite_lanceur_discretion_v1.py` | `0bef30a50010ee67e13840b9b91201519741f0cde5f43d6b592fedd4e66abdba` | à compléter |
| préparation des lectures, version 3 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py` | `c0021298c21d027a713b1947d2668ac928f2a856b1a696686dd35b83a9515c45` | conforme : aucune position tirée pour le juge |
| essais de la préparation | `tests/test_bras_a_v2_habilite_preparation_des_lectures_v3.py` | `70badfe1d058b72ab3f8450a3b9271fe97a7ce14a009334200f2e7858bd8a877` | conformes |
| module des autres moniteurs, version 11 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v11.py` | `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda` | conforme : seule l'empreinte inscrite de la préparation change depuis la version 10 (`42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c`) |
| essais du module | `tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py` | `92711976e9ee949b08719b791cafc53932763ab96a04b6c01d34b0068cc3c776` | conformes |
| attestation, de la version 7 à la version 10 | `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1.md` | `6555abc42fbf0465ddbdc5b9d19e70b52f16ac6ce946fa00729abf621f867c6a` | conforme : aucun calcul de moniteur ne change ; une précision à ajouter par erratum |
| différentiel 7 → 10 | `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v7-a-v10.diff` | `aacb9f64341c3278400f34ed8af8843cdabf265bc67653b390a137a1a1b9a402` | régénéré, identique |
| différentiel 10 → 11 | `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v10-a-v11.diff` | `b7ac6de62b8e0c7c5c8619dd29cd7af2b56a6b07fe2cfba27e15639fb4a19d0a` | régénéré, identique |
| gabarit de la configuration | `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-gabarit-v1.json` | `0da610c43edf15eb0b28c361882ea0536dc11bedfcc4cc35cf1254376e062a4b` | conforme après une correction (quatre modules à citer) |
| pièce sans interne du développeur | `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` | `e2f246ebb533ce8a28f4a54c8068723cd30340059c68ff5cf34fc7edd965330b` | aucune fuite ; deux phrases à ajuster après les corrections |

Chaque empreinte a été recalculée et comparée à son compagnon : toutes égales. Pièces de la relance lues, et elles seules, à leur empreinte : l'extrait du lanceur v3 (`5d2a48c0f9b6b8a36b20cc466508c44fe1c2aad84a17b98cfb1190f85c631bed`) et le module d'entrée v2 (`cb668bb95a9c0a37b1a08a91f304e1b756ef5b0ebddc0a3f193be0692e0bfa10`).

## Comptes

| épreuve | compte |
|---|---|
| essais du lanceur | 18 passent sur 18 |
| essais de la préparation, version 3 | 8 passent sur 8 |
| essais du module, version 11 | 4 passent sur 4 |
| épreuve par retrait du développeur, rejouée en entier | 46 retraits mordent sur 46 ; fichiers remis à l'identique |
| retraits de plus, du contre-lecteur | 2 mordent sur 14 : douze gardes à doter d'un artefact |
| scénarios de plus, du contre-lecteur | 5 joués ; 4 montrent un défaut, 1 confirme un refus sans perte |
| essai d'équivalence des versions 7 et 10, rejoué | relevé identique à l'octet ; aucun nombre commun ne diffère, 12 lectures |
| noms du module changés de la version 7 à la version 10 | 12 changés, 35 ajoutés, 0 retiré : la liste de l'attestation |
| noms du module changés de la version 10 à la version 11 | 1 |
| programmes qui nomment le fichier des rangs | 5, recompté |

## Corrections, par leur objet

| | objet | poids |
|---|---|---|
| C1 | une seconde reprise du même moniteur après une panne de transport est refusée | bloquante |
| C2 | une reprise n'est pas toujours comptée ni inscrite | à corriger |
| C3 | une vérification de la lecture commune est à faire avant la production, non après les ouvertures | à corriger |
| C4 | la configuration de la base n'est pas comparée à sa ligne du registre | à corriger |
| C5 | quatre modules appelés ne sont pas cités par leur empreinte | à corriger |
| C6 | la sous-commande qui relève les jetons de fin exige une configuration déjà complète | à corriger |
| C7 | l'énoncé d'une tâche n'est pas gardé à l'identique de celui que voit l'agent | à corriger |
| C8 | douze gardes sans artefact qui morde (R5) | à corriger |
| C9 | le manifeste du lanceur ne porte ni versions ni commit (R9) | à corriger |
| C10 | la notice omet un cas de refus sans réparation | mineure |
| C11 | le module d'entrée est importé avant la vérification de son empreinte | mineure |
| C12 | l'attestation : une précision à ajouter sur ce qui est rendu | mineure |
| C13 | la pièce sans interne : deux phrases à ajuster | mineure |

## Ce qui est tenu

L'ordre des six étapes de l'extrait ; la garde de production avant toute production et avant le premier appel de chaque moniteur à modèle de langue ; l'accord de l'entropie propre appelé par le module d'entrée avant le tirage ; l'engagement de la table inscrit avant toute production ; la séparation de la préparation et de la production ; aucun tirage hors de la table ; aucune suppression ; du code de la relance, le seul module d'entrée.

## Trois points pour la session principale

1. Le lanceur ajoute des clés neuves au registre partagé : vérifier, avant la course, que les autres lecteurs de ce registre les admettent, ou donner au bras A un registre à lui.
2. Le chemin réel (chargement sur la carte, relevé des jetons de fin, module d'entrée) n'est joué que par des doublures : un essai sur la machine de calcul reste à faire avant la course.
3. Trois fichiers anciens du côté habilité n'ont pas de compagnon dans la copie de travail ; leurs empreintes sont celles que les pièces citent.

Non ouvert : aucun résultat, aucun texte du préenregistrement, aucun module de graines, aucun fichier interdit par le mandat. Aucun poids chargé, aucune dépense, aucun refus d'outil. Ni commit ni poussée.
