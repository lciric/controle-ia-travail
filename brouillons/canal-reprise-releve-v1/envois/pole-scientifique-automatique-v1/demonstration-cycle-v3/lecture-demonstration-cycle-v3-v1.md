# Démonstration du cycle v3 — le pôle complet en simulation — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 12:28 UTC (heure lue sur `date -u`). Sans
préenregistrement (mot de Lazar, 12:02 heure de Paris) ; plan et lecture dans l'en-tête de
`../orchestrateur-pole-v3/demonstrations/demo_cycle_v3.py` (`246ad2df…`), poussé avant l'exécution (commit `3851b0f`,
orchestrateur v3, 120 essais « OK », empreintes `EMPREINTES-orchestrateur-pole-v3-v1.txt` `b6c6019a…`). Exécution de
12:22:07 UTC, 81 s, graines 1 à 20, quatre générations, `p_triviale` 0,4 ; résumé `resultats-v1/demo-cycle-v3.json`
(les archives complètes des 60 courses, 177 Mo, restent dans le conteneur : elles se refont à l'identique par le script).
**Ajout déclaré après cette exécution** : le bras « v3 souple » (`bras-souple-v1/`, mêmes graines). Deux essais de
fumée avant (2 et 6 graines, déclarés dans l'en-tête du script).

## Verdict

1. **Le pôle tourne de bout en bout avec le nouveau juge** : générations 0 à 3, recombinaison stratifiée, ordre secret
   imposé par le noyau, nul des filles v2. **Aucune fille triviale promue sous v3 (0 sur 32)**, contre 3 sur 38 avec le
   nul de v0 et 6 sur 34 avec le système v0 complet. Aucune fausse découverte nulle part (filles fausses et témoins faux :
   0 promu, dans les trois bras).
2. **Le prix : des vraies filles neuves perdues** dans ce monde jouet à deux traits et 120 tirages : 18 sur 24 promues
   sous v3 (0,75), contre 24 sur 27 avec le nul de v0 (0,89) et 29 sur 29 sous v0. L'option souple de la décision n° 1
   n'y change presque rien (19 sur 25, 0,76) : **le coût vient des membres ajustés eux-mêmes, pas du produit des
   parents**. Critère 3 de la lecture (écart ≤ 0,1) : **non tenu**.
3. **Remède à essayer** : plus de tirages pour les filles (l'essai de puissance donne 0,91 à 500 tirages en option
   stricte, 0,98 en souple) ou des espaces de traits plus riches (1,0 dès 4 traits).

## Chiffres (sommes sur 20 courses)

| bras | filles triviales promues | autres filles vraies promues | autres filles fausses promues | témoins faux gardés | témoins vrais éliminés |
|---|---|---|---|---|---|
| v3 (juge v1, nul v2 strict, tirage stratifié) | **0 / 32** | 18 / 24 (0,75) | 0 | 0 / 57 | 11 / 57 |
| v3 souple (ajout déclaré) | **0 / 35** | 19 / 25 (0,76) | 0 | 0 / 59 | 11 / 59 |
| v3 avec le nul de v0 | 3 / 38 (0,08) | 24 / 27 (0,89) | 0 | 0 / 64 | 11 / 64 |
| v0 (juge v0, nul v0, noyau corrigé) | 6 / 34 (0,18) | 29 / 29 (1,00) | 0 | 0 / 58 | 9 / 58 |

Les bras ne sont appariés qu'au départ (mêmes graines) : dès qu'une promotion diffère, les courses divergent (autres
survivantes, autres paires, autres filles) ; les comparaisons sont descriptives.

## Lecture (fixée avant l'exécution)

- (1) Aucune triviale promue sous v3 : **tenu** (0 sur 32).
- (2) Le nul de v0 en promeut au-delà de 0,05 : **tenu** (0,08 ; 0,18 sous v0 complet). La prédiction d'origine
  (environ 0,4, comme à l'expérience 2) était déjà corrigée vers le bas par les essais de fumée (déclarés) : à 120
  tirages sur un plan choisi par divergence, la fille triviale a moins de prise qu'à 200 tirages.
- (3) Autres filles vraies comparables (écart ≤ 0,1) : **non tenu** (0,75 contre 0,89).
- (4) Témoins vrais éliminés : 11 sur 57 sous v3, 9 sur 58 sous v0 : le coût de l'urne à 120 tirages est faible ici.

## Ce que cela dit, et ce que cela ne dit pas

- **Dit** : le juge v1 et le nul v2 fonctionnent dans le cycle réel de l'orchestrateur (agents simulés qui écrivent et
  rejouent du code, ordre imposé, vérificateur d'un autre modèle) ; le trou « parent + loi aveugle » est fermé dans le
  cycle comme dans l'expérience 2 ; la sévérité a un coût en puissance sur les vraies filles dans un monde pauvre.
- **Ne dit pas** : ce que feraient de vrais agents (les agents simulés ne lisent pas la mémoire et proposent des filles
  au hasard) ; l'apport du juge v1 contre la dérive (le monde simulé n'en a pas : c'est l'expérience 1 qui le montre).
- **Suite** : (a) filles à 300 tirages ou plus dans le cycle, puis rejouer la démonstration ; (b) porter la mémoire
  (signature brute, héritage de la preuve, marchepieds) dans le cycle ; (c) premier essai avec de vrais agents (dépense :
  devis et mot de Lazar chez session-depot).
