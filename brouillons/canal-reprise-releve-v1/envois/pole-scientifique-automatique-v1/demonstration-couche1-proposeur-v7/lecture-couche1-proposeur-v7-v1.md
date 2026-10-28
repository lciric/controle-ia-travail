# v7 avec proposeur et phase exploratoire — couche 1 en simulation d'agents, banque réelle T0.5 et monde planté — lecture v1 (exploratoire)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 14:49 UTC (heure lue sur `date -u` : 14:48:29). Sur le
« go » de Lazar de 15:38 heure de Paris (« lance v7 immédiatement après lecture comparaison d'échelle » ; la lecture de la
comparaison tourne encore, la course est lancée en attendant, sans dépense). Plan et lecture E1 à E4 fixés dans l'en-tête
de `../orchestrateur-pole-v7/demonstrations/demo_couche1_proposeur_v7.py` avant l'exécution. **Deux exécutions** : la
première (14:43 UTC) portait l'erreur de la règle e-BH (erratum `../erratum-multiplicite-e-bh-v1.md`) ; la seconde,
après correction (14:46 à 14:47 UTC, 94 s), est celle qu'on lit ici. Résumé scellé : `resultats-v1/`.

## Verdict

1. **La méthode a des dents dans le monde planté** : témoins vrais promus **8 sur 8** dans chaque bras à proposeur (2 sur 2
   dans la référence), témoins faux **0 sur 8** ; la règle de multiplicité retient ce qu'il faut. Dans la banque réelle
   T0.5 : **pas de dents** (0 témoin vrai promu sur 20), aucune promue : rien à conclure sur le fond (banque trop petite ;
   couche 1 bis en cours chez session-depot).
2. **L'exploration n'a pas montré d'avantage ici (E2 non tenu)** : dans le monde planté, chaque bras a trouvé la
   structure une fois — l'explorateur par une loi ajustée sur le développement (stratégie `ajustee_sur_developpement`),
   l'aveugle par la stratégie `difference_sous_populations`, qui **épouse exactement la structure plantée** (un effet de
   trait qui change de signe selon la sous-population) et l'a pariée dans le bon sens par chance (une chance sur deux à
   chaque essai). Défaut de conception de la démonstration, pas une mesure : le monde planté ne doit pas coïncider avec un
   gabarit du proposeur aveugle.
3. **Le proposeur fait ce qu'il doit** : 12 fiches par génération au gabarit, aucun refus de gabarit, stratégies
   comptées ; la mémoire refuse les redites (11 à 15 par course) ; l'exposition adaptative est comptée (30 et 31 verdicts
   montrés au proposeur, sans tranches).

## Lecture (fixée avant l'exécution)

- E1 aucun témoin faux promu : **tenu** (0 sur 48 servis dans les six courses).
- E2 monde planté, exploration ≥ 1 promue par sous-population et aveugle moins : **non tenu** (1 contre 1).
- E3 monde réel : 0 promue dans les trois bras, « pas de dents » à chaque génération : **aucune conclusion de fond**.
- E4 par stratégie (monde planté) : `ajustee_sur_developpement` 1 promue sur 3 fiches (bras exploration) ;
  `difference_sous_populations` 1 sur 6 (bras aveugle), 0 sur 6 (bras exploration) ; toutes les autres 0.

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : la chaîne proposeur → gel → banque → juge (nul informé, nul d'archive, e-BH, témoins sans agents) fonctionne
  et a des dents quand le monde a de la structure ; la correction d'e-BH était nécessaire.
- **Ne dit pas** : que l'exploration aide (une course, un monde planté mal choisi) ; rien sur T0.5.
- **Suite** : (1) un monde planté que les gabarits aveugles ne couvrent pas (par exemple une interaction à seuils non nuls,
  ou un effet porté par une combinaison de traits), 20 graines, lecture par taux ; (2) la banque complète (couche 1 bis) ;
  (3) le pari à fraction.
