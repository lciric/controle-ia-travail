# Démonstrations du cycle v4 — puissance des filles, marchepieds, redites — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 12:51 UTC (heure lue sur `date -u`). Sans
préenregistrement (R-546) ; plan et lecture dans l'en-tête de `../orchestrateur-pole-v4/demonstrations/demo_cycle_v4.py`,
poussé avant les exécutions (commit `b357564`, orchestrateur v4, 127 essais « OK », empreintes `1f790dc2…`). Exécutions
de 12:44 à 12:49 UTC (A : 181 s ; C : 86 s ; B : 288 s), graines 1 à 20 ; résumés `resultats-v1/` (les archives des
courses restent dans le conteneur : elles se refont par le script). **Ajout déclaré après l'exécution de C** : le bras
« sans mémoire » (`bras-sans-memoire-v1/`). Essais de fumée avant : déclarés dans l'en-tête du script.

## Verdict

1. **Les deux remèdes marchent (A)** : avec deux traits, la part des vraies filles neuves promues passe de 0,53 à 0,90
   quand on passe de 120 à 500 tirages ; avec quatre traits, elle vaut 0,92 à 120 tirages et **1,00 à 500**. Aucune
   fille triviale promue (0 sur 131), aucune fausse découverte, dans les quatre bras.
2. **La mémoire empêche les découvertes en double (C)** : sans mémoire, 11 redites d'idées déjà promues sont promues à
   nouveau, comptées comme des découvertes ; avec la garde prédictive, 0. Aucune fausse découverte parmi les redites, dans
   aucun bras (trop peu de redites d'idées fausses pour montrer l'inflation que l'héritage empêche).
3. **Deux réserves, que je corrige en v5** :
   - **les marchepieds n'apportent rien ici (B)**, même quand les lignées sont fécondes (71 vraies filles contre 75) :
     dans ce petit monde (six fiches de départ, trois paires par génération), le tirage stratifié prend déjà presque toutes
     les paires valides ; il faut un vivier plus grand pour qu'un choix de paires compte (la piste 3 avait 400 candidates) ;
   - **avec deux traits, la garde prédictive fusionne à tort de vraies filles neuves** avec des fiches archivées (31 et 39
     refusées, contre 5 et 6 avec quatre traits) : le seuil de 0,30 nat tient 5 % de fausses fusions **par paire**, mais
     une nouvelle fiche est comparée à toute l'archive. Correction : un seuil qui tient 5 % **par fiche**, donc qui se
     resserre quand l'archive grandit.

## Chiffres (sommes sur 20 courses)

**A — puissance des filles** (tirage stratifié, `p_triviale` 0,4)

| bras | vraies filles promues / testées | triviales promues | refusées par la garde | témoins vrais éliminés |
|---|---|---|---|---|
| 2 traits, 120 tirages | 9 / 17 (0,53) | 0 / 15 | 31 | 9 / 49 |
| 2 traits, 500 tirages | 18 / 20 (0,90) | 0 / 19 | 39 | 9 / 55 |
| 4 traits, 120 tirages | 22 / 24 (0,92) | 0 / 48 | 6 | 0 / 57 |
| 4 traits, 500 tirages | **23 / 23 (1,00)** | 0 / 49 | 5 | 0 / 57 |

**B — marchepieds** (4 traits, 500 tirages)

| monde | stratifié : vraies filles promues | avec marchepieds | fausses promues |
|---|---|---|---|
| lignées fécondes | 75 | 71 | 0 |
| plat | 78 | 86 | 0 |

**C — redites** (2 traits, 120 tirages, `p_redite` 0,5, six générations)

| politique | redites proposées | refusées | testées | découvertes en double | fausses parmi les redites |
|---|---|---|---|---|---|
| héritage | 21 | 12 | 9 | **0** | 0 |
| refus | 22 | 22 | 0 | 0 | 0 |
| rien (garde des survivantes gardée) | 24 | 15 | 9 | 0 | 0 |
| **sans mémoire** (ajout déclaré) | 40 | 0 | 40 | **11** | 0 |

## Lecture (fixée avant l'exécution)

- A1 aucune triviale promue : **tenu** ; A2 la part monte avec les tirages et les traits : **tenu** (0,53 → 0,90 ; 0,92 →
  1,00) ; A3 aucune fausse découverte : **tenu**.
- B1 marchepieds supérieurs dans le monde fécond : **non tenu** (71 contre 75) ; B2 pas d'avantage dans le monde plat :
  tenu à la lettre (86 contre 78, écart de 10 %) ; B3 aucune fausse découverte : **tenu**.
- C1 : héritage et refus sans double : **tenu** ; « rien » au moins un double : **non tenu**, parce que ma garde refuse la
  redite d'une survivante quelle que soit la politique — défaut de conception de la démonstration, d'où le bras « sans
  mémoire » ajouté, qui montre 11 doubles ; C2 : **tenu** (0 et 0, sans dents).

## Ce que cela dit, et ce que cela ne dit pas

- **Dit** : plus de traits et plus de tirages rendent au juge sa puissance sans rien lâcher sur la sévérité ; la mémoire
  évite de compter deux fois une même idée.
- **Ne dit pas** : que les marchepieds servent (le monde de démonstration est trop petit pour le dire) ; que le seuil de
  la signature convienne à une grande archive (il ne convient pas en deux traits).
- **Suite (v5)** : seuil de signature à 5 % par fiche, calibré sur la taille de l'archive ; un vivier de démonstration
  plus grand pour les marchepieds ; et, pour un premier lancement réel, une graine du noyau tirée hors de la graine du
  pôle.
