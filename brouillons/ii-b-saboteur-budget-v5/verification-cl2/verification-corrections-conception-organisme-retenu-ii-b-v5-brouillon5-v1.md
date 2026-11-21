EXPLORATOIRE, NON OPPOSABLE (R-522)

# Vérification courte des corrections — conception de l'organisme retenu, v5, brouillon 5

**Verdict : scellable en l'état**, une fois les sept nœuds tranchés ou passés à leur défaut. Il ne reste ni bloquant, ni majeur, ni mineur obligatoire. Deux précisions de rédaction sont facultatives (section 5).

- **Pièce vérifiée** : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-brouillon5.md`, sha256 `748cfcc268fa78651f626b894934a7dc9b9521d456f649dd6537c9dcdde8426c`. Les compagnons de l'outil, du fichier des différences, de la table de traitement et du journal v8 se vérifient.
- **Outil d'assemblage** : `assembler-brouillon5-v1.py`, relancé sur le brouillon 4 (`1a11b635…`), applique 23 retouches. Il redonne le brouillon 5 et la table de traitement **à l'octet**. Les deux copies de contrôle sont dans mon dossier, sous `rejeu-b5/`.
- **Périmètre** : comme demandé, je n'ai vérifié que le reste R1, mes cinq mineurs, les trois retouches faites au-delà de la demande et l'absence de liberté après l'étalonnage. Le reste du texte n'est pas relu.
- Aucun refus d'outil. Je ne tranche aucun nœud.

## 1. Le reste R1 — nœud 7 : traité

Le nœud 7 dit si l'oracle que l'issue n'a pas nommé joue encore après l'étalonnage. Il a maintenant quatre options : (a), (b), (b') et (c). Le défaut est (b'), et le texte courant porte (b') : je l'ai vérifié en 5.1, 10.6, 11, 6 point 4 et dans la table des nœuds.

- **Nombres d'actions.** 960 + 2 560 = 3 520 actions hors tours. À 12 tours, 10 240 + 3 520 = 13 760 en tout. Pour mémoire, (a) donne 10 240 + 6 400 = 16 640, et ces 6 400 se décomposent en 12 × 320 (les tours) + 2 560 (l'évaluation). Tout est cohérent avec la section 12.
- **Plafond de tours et coût fixe, en formule** (10.2, ligne de l'option (b')). Le calcul est mécanique, à partir des entrées scellées (un oracle par tour ; 3 520 actions hors tours). Le coût fixe est dit pour chaque option. L'affirmation « au moins égal à (a) dès trois tours » est juste : (a) dépense 2 560 + 320 R actions, (b') en dépense 3 520, et les deux s'égalent à R = 3.
- **L'option (b) retire bien la promesse partout.** Ses points (i) à (v) en section 17 récrivent :
  - les deux cases de la table des revendications de 5.1 ;
  - la phrase de 10.6 pour l'issue du jumeau au contexte de l'agent ;
  - la dernière phrase de la section 11 ;
  - une ligne de la section 18.

  L'option (c) reprend ces mêmes points (ii) à (v) et retire la mesure du point 4 de la section 6. Sous (b'), les phrases « rapporté à côté » sont tenues, puisque l'oracle à contexte réécrit joue à l'évaluation (élève, témoin, modèle de base).

## 2. Mes cinq mineurs : traités

| mineur | où | état |
|---|---|---|
| m-a : options 1 (c) et 4 (b) dimensionnées en partie | table des nœuds, lignes 1 et 4 ; 17 | traité. Les 98,8 % sont ceux que j'avais relevés (sortie du contrôle du premier coût, ligne 292) ; 4 (c) reporte le scellement d'un devis |
| m-b : reprise rapportée avec l'étalonnage qui l'a précédée | 5.1, point 5 ; 15, deux lignes | traité |
| m-c : k_P à la place de k_R dans la phrase d'arrêt au tour de contrôle sous le nœud 2 (b) | 17, nœud 2 (b), point (iii) | traité |
| m-d : ce que porte le coût fixe sous (b) et (c) | 10.2 ; 17, nœud 7 | traité |
| m-e : copie laissée hors du dossier du rédacteur | journal v8 | déclarée ; rien dans la pièce |

## 3. Les trois retouches faites au-delà de la demande (journal v8)

1. **Le défaut du nœud 7 passe de (b) à (b').** C'est une recommandation, non une décision. Sa raison est écrite en 17 : c'est la moins chère des options qui tiennent les promesses de 5.1 et 10.6. Le nœud reste à trancher par Lazar. Acceptable.
2. **Sous (b), la promesse symétrique est retirée aussi.** Pour l'issue de l'oracle à contexte réécrit, « ajout par pas de l'élève rapporté par l'autre oracle » est retiré en 5.1, avec une ligne de plus en 18. C'est juste : ma remarque R1 demandait de retirer la promesse partout.
3. **Section 6, point 4, précisée** : le niveau du maître est lu sur ses épisodes acceptés, après l'étalonnage, avec une variante par option. C'est la même promesse, côté maître ; juste.

L'arrondi « 1,95 % écrit 1,9 % » de la section 8 n'est pas retouché, et c'est déclaré. Il était hors des restes : sans effet.

## 4. Aucune liberté après l'étalonnage

Aucune retouche n'introduit de choix après l'étalonnage :
- le nœud 7 est fixé dans le fichier d'entrées scellé avant l'étalonnage, quelle que soit l'option ;
- la reprise après « ne part pas » ou « non calculable » est une course neuve, sous devis neuf, rapportée avec l'étalonnage qui l'a précédée ;
- les quatre issues de la règle composée sont inchangées depuis le brouillon 4.

## 5. Précisions facultatives (n'empêchent pas le scellement)

- **5.1, table des revendications, issue de l'oracle à contexte réécrit** : sous (b'), « rapporté par [P] sur les mêmes épisodes » pourrait dire « … sur les épisodes acceptés du maître et à l'évaluation ».
- **5.5, dernière phrase** : « sous l'issue [N], tout ce que [P] aurait rendu est rapporté, et inversement ». Elle vaut pour l'étalonnage ; pendant la course, elle vaut dans la mesure où le nœud 7 joue l'autre oracle. Elle pourrait renvoyer au nœud 7.
