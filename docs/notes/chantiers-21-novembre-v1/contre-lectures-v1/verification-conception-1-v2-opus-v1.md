# Vérification courte des corrections : conception du hasard du défenseur, v2 — par Opus 5.5 — v1

- **Date** : 22 novembre 2026. **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), auteur de la contre-lecture. Classe B. Aucun appel réseau, aucun commit.
- **Pièces** :
  - v1 : `docs/notes/chantiers-21-novembre-v1/reponses-fable-v1/demande-1/relecture-fable-api.md`, `6b94a099…4599`, égale à son compagnon ;
  - contre-lecture : `contre-lectures-v1/contre-lecture-reponse-1-hasard-du-defenseur-opus-v1.md`, `25d090e5…c590` ;
  - v2 : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v2.md`, `47387ebf64c1569fce45a75c31aeae03fc4315c21b43f7581eefd4866e2ed51f`, recalculée ;
  - rapport : `conceptions-v2/conception-1-hasard-du-defenseur-v2-rapport-portage.json`.
- **Méthode** : `diff` intégral de la v1 et de la v2 ; chaque bloc changé est confronté à sa correction ; recherche, dans le texte non touché, des phrases que les corrections rendent fausses.

## Verdict : conforme après corrections

- **Constats** : les 18 constats sont portés, en 28 remplacements, et le texte n'a pas d'autre changement que l'en-tête de portage.
- **Effets de bord** : trois phrases restées telles quelles contredisent désormais les corrections. Ce sont les couples E1 à E3 ci-dessous : deux ont un effet sur le fond, une est de cohérence.
- **Mise en forme** : trois couples, F1 à F3, ne changent rien au sens.

## Les 18 constats

| constat | état dans la v2 |
|---|---|
| 1 | fermé (§ 2, « Nul testé ») ; effet de bord E2 |
| 2 | fermé (§ 1, « Tirage » et « Graine de l'agent ») |
| 3, bloquant | **porté fidèlement**, les deux remplacements à la lettre (G1 ; test de mort 1). Un effet de bord, E3, est dans l'ordre d'écriture. La validation du fond revient au concepteur. |
| 4 | fermé (§ 3, « Nul ») ; effet de bord E1 |
| 5 | fermé ; voir le premier cas de lecture ci-dessous |
| 6 | fermé ; voir le second cas de lecture ci-dessous (F2) |
| 7 | fermé (§ 5, deux remplacements) |
| 8 | fermé (§ 5, trois remplacements) ; effet de bord dans la conclusion, couvert par E1 |
| 9 | fermé (G3) |
| 10 | fermé ; voir le second cas de lecture ci-dessous (F1) |
| 11 | fermé (G6) |
| 12 | fermé (G5) |
| 13 | fermé ; voir le second cas de lecture ci-dessous (F3) |
| 14 | fermé (§ 2, « Loi sous le nul ») |
| 15 | fermé (§ 1, « Engagement ») |
| 16 | fermé (table, ligne 1 ; « Multiplicité ») |
| 17 | fermé (§ 8) |
| 18 | fermé (décision 2, option b) |

## Les deux cas de lecture signalés par le correcteur

- **Constat 5 : les deux lignes réunies par un saut de ligne.** C'est mon sens exact : deux lignes distinctes de la table de lecture, en place de l'ancienne ligne 3. La table de la v2 en a cinq, bien formées. Le test de mort 2 (« le jumeau rejette et p_Δ ne rejette pas ») est désormais d'accord avec la ligne de mort. Rien ne trahit le sens.
- **Constats 6, 10 et 13 : les puces écrites en ligne.** Le sens est intact : chaque élément est présent, à sa place. Mais dans une liste, « … ; - Krakovna … » se lit comme un seul élément, et un développeur peut manquer l'« Appariement » ou les « Grandeurs secondaires plantées », collés à une autre puce. Les couples F1 à F3 les remettent en vraies puces, sans changer un mot.

## Couples restants

Chaque ancien texte figure une seule fois dans la v2 (vérifié par `grep -cF`).

### E1 — Conclusion : le contraste dit « exact », et la trouvaille sans ses suppositions (suite des constats 4 et 8, effet sur le fond)

Ancien :
```
Le contraste avec le jumeau se teste exactement par la même permutation, appliquée à la différence appariée saboteur moins jumeau.
```
Nouveau :
```
Le contraste avec le jumeau se teste par la même permutation, appliquée à la différence appariée saboteur moins jumeau, avec une statistique studentisée : exact pour le nul en loi, approché pour le seul nul des moyennes (§ 3).
```
Ancien :
```
la détection par l'audit ne dépend pas de la stratégie du saboteur
```
Nouveau :
```
la détection par l'audit ne dépend pas, au premier ordre et en régime de signature, de la stratégie du saboteur
```

### E2 — Multiplicité : le « nul strict » qu'on n'emploie plus (suite du constat 1, effet sur le fond)

Ancien :
```
(Westfall et Young), exact sous le nul strict global.
```
Nouveau :
```
(Westfall et Young), exact sous le nul en loi global (§ 2).
```

### E3 — Ordre d'écriture, pièce 6 : la mort par désaccord à toute corrélation (suite du bloquant, constat 3, et du constat 12 ; cohérence)

La pièce 6 dit encore « désaccord : mort » à toute corrélation, contre le nouveau test de mort 1. Elle ne nomme pas non plus le cas de G5 dont la garde a besoin.

Ancien :
```
| 6. Table de puissance simulée | accord avec la table du § 4 à 0,10 près | désaccord : mort |
```
Nouveau :
```
| 6. Table de puissance simulée, cas sain de G5 compris | à corrélation intra-tâche 0, accord avec la table du § 4 à 0,10 près | à corrélation 0, désaccord : mort ; aux corrélations positives, la table simulée remplace l'approximation, sans mort (test de mort 1) |
```

### F1 — Antériorités en vraies puces (constat 10, mise en forme)

Les trois couples suivants remplacent « ; - » par un point-virgule, un saut de ligne et un tiret.

Ancien : `section 11) ; - Krakovna` → nouveau :
```
section 11) ;
- Krakovna
```
Ancien : `section 11) ; - voisins` → nouveau :
```
section 11) ;
- voisins
```
Ancien : `2610.37055) ; - Chung` → nouveau :
```
2610.37055) ;
- Chung
```

### F2 — « Appariement » en puce propre (constat 6, mise en forme)

Ancien : `vérifications. - **Appariement.**` → nouveau :
```
vérifications.
- **Appariement.**
```

### F3 — « Grandeurs secondaires plantées » en puce propre (constat 13, mise en forme)

Ancien : `N/6. - **Grandeurs secondaires plantées**` → nouveau :
```
N/6.
- **Grandeurs secondaires plantées**
```

## Ce que je n'ai pas fait

- Je n'ai pas rejoué le script de portage ; je me suis fié au `diff` des deux textes, qui suffit.
- Je n'ai pas rejugé le fond du bloquant ; la consigne le réserve au concepteur.
- La phrase « aucun code n'a tourné », dans la conclusion, reste vraie du concepteur. Les chiffres du rejeu ajoutés à la v2 y sont attribués au contre-lecteur : je n'y touche pas.
