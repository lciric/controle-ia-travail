# Démonstrations du cycle v5 — seuil par fiche, marchepieds sur le vivier de 60, redites — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1 au moment de la lecture), écrit à partir de 13:36 UTC
(heure lue sur `date -u` : 13:36:00). Sans préenregistrement (R-546) ; plan et lecture fixés dans l'en-tête de
`../orchestrateur-pole-v5/demonstrations/demo_cycle_v5.py` (`a457a8e2…`), poussé avant les exécutions (commit `0f4f297`,
orchestrateur v5, 130 essais « OK », empreintes `142a7c1f…`). Exécutions lancées à 12:58 UTC, finies à 13:09 (A, 654 s),
13:17 (C, 463 s) et 13:25 UTC (B, 1 608 s) ; graines 1 à 20 ; résumés dans `resultats-v1/` (empreintes compagnons ; les
archives des courses restent dans le conteneur : elles se refont par le script, à graines égales).

## Verdict

1. **Le seuil de signature par fiche corrige la réserve de v4 (A)** : avec deux traits, les vraies filles neuves refusées
   à tort par la garde prédictive tombent de 31 et 39 (v4) à **4 et 5** ; avec quatre traits, 6 et 5 (inchangé). Les parts de
   vraies filles promues restent celles de v4 : 0,56 et **0,97** (2 traits, 120 et 500 tirages), 0,92 et **1,00** (4 traits).
   Aucune fille triviale promue (0 sur 181), aucune fausse découverte.
2. **Les marchepieds servent quand le vivier est assez grand (B)** : sur 60 fiches à quatre traits, six paires par
   génération, cinq générations, le tirage avec marchepieds promeut **282 vraies filles contre 212** (+33 %) dans le monde
   à lignées fécondes, et **236 contre 245** (−4 %, dans la bande des 10 %) dans le monde plat ; aucune fausse promue, aucun
   témoin vrai éliminé (200 témoins par bras). Les deux faces de la lecture tiennent : l'avantage apparaît là où il doit,
   et seulement là. C'est le mécanisme construit pour cela qui est vérifié, pas une découverte sur le monde.
3. **La mémoire empêche les découvertes en double (C)** : héritage, refus et « rien » : **0** double sur 31 redites
   proposées ; sans mémoire : **11** doubles sur 40. Aucune fausse parmi les redites, dans aucun bras (toujours sans dents
   pour C2).

## Chiffres (sommes sur 20 courses)

**A — puissance des filles** (tirage stratifié, `p_triviale` 0,4 ; v4 entre parenthèses)

| bras | vraies filles promues / testées | triviales promues | refusées par la garde | témoins vrais éliminés |
|---|---|---|---|---|
| 2 traits, 120 tirages | 14 / 25 (0,56) | 0 / 36 | **4** (31) | 10 / 52 |
| 2 traits, 500 tirages | 29 / 30 (0,97) | 0 / 48 | **5** (39) | 10 / 60 |
| 4 traits, 120 tirages | 22 / 24 (0,92) | 0 / 48 | 6 (6) | 0 / 57 |
| 4 traits, 500 tirages | **23 / 23 (1,00)** | 0 / 49 | 5 (5) | 0 / 57 |

Les témoins vrais éliminés à deux traits (10 sur 52 et 60) sont ceux des fiches sans parents à 120 tirages (le plan des
fiches de départ ne change pas avec `taille_plan_filles`) : même constat qu'en v4 (9 sur 49 et 55), lié à la pauvreté du
monde à deux traits, pas à la mémoire.

**B — marchepieds** (vivier de 60 fiches, 4 traits, 500 tirages, six paires par génération, cinq générations)

| monde | stratifié : vraies filles promues / testées | avec marchepieds | fausses promues | refusées par la garde |
|---|---|---|---|---|
| lignées fécondes | 212 / 215 | **282 / 287** | 0 | 9 ; 11 |
| plat | 245 / 246 | 236 / 241 | 0 | 7 ; 8 |

**C — redites** (2 traits, 120 tirages, `p_redite` 0,5, six générations)

| politique | redites proposées | refusées | testées | découvertes en double | fausses parmi les redites |
|---|---|---|---|---|---|
| héritage | 31 | 20 | 11 | **0** | 0 |
| refus | 31 | 31 | 0 | 0 | 0 |
| rien (garde des survivantes gardée) | 31 | 20 | 11 | 0 | 0 |
| sans mémoire | 40 | 0 | 40 | **11** | 0 |

## Lecture (fixée avant l'exécution)

- A1 aucune triviale promue : **tenu** ; A2 la part monte avec les tirages et les traits : **tenu** (0,56 → 0,97 ; 0,92 →
  1,00) ; A3 aucune fausse découverte : **tenu** ; mesure ajoutée (refusées par la garde à deux traits « de l'ordre de
  quelques unités ») : **tenu** (4 et 5).
- B1 marchepieds supérieurs dans le monde fécond : **tenu** (282 contre 212) ; B2 pas d'avantage dans le monde plat (au
  plus 10 % d'écart) : **tenu** (236 contre 245, −4 %) ; B3 aucune fausse découverte : **tenu**.
- C1 héritage et refus sans double, sans mémoire au moins un : **tenu** (0, 0, 11) ; C2 fausses parmi les redites,
  héritage au plus sans mémoire : **tenu** (0 et 0, sans dents : le monde de démonstration ne produit pas de redites
  d'idées fausses).

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : les trois réserves de v4 sont levées dans le monde simulé — le seuil par fiche tient la fausse fusion sans
  perdre de puissance ; les marchepieds exploitent les lignées fécondes quand il y a assez de paires parmi lesquelles
  choisir ; la mémoire évite le double comptage.
- **Trop beau ?** B tient exactement comme prévu parce que le monde fécond est construit pour cela (une fille d'une fille
  est vraie avec probabilité 0,85, sinon 0,35) et que les marchepieds choisissent précisément les paires qui ont une fille
  survivante : c'est une vérification de mécanisme, dont la valeur dépend de l'existence de lignées fécondes dans un
  monde réel, que rien ici ne mesure. Les parts à 1,00 (4 traits, 500 tirages) répètent v4 : puissance saturée dans un
  monde où les lois vraies sont exactement celles des fiches (vérité binaire ; limite relevée par la contre-lecture
  d'aptitude du 27 octobre, `../premier-lancement-reel/contre-lecture-aptitude-v1/`).
- **Ne dit pas** : que la loi de référence du seuil (softmax de force 1,5) convienne à de vraies fiches ; que les
  marchepieds servent sur un monde réel ; que la mémoire reconnaisse deux hypothèses de contrôle qui partagent le
  vocabulaire (garde textuelle) ou deux recettes d'attaque qui évadent pareil (signature sur la loi, pas sur la recette).
- **Suite** : v6 (premier lancement réel préparé sans dépense : monde tenu par le noyau, relais de clé réel, répétition
  générale, dépôt unique par engagement) ; v7 (monde du programme sur banque en cache, nul informé, rôle proposeur,
  moissonneur), selon la contre-lecture d'aptitude.
