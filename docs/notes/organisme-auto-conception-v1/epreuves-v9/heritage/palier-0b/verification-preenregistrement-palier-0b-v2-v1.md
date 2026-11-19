# Vérification des corrections — préenregistrement de l'épreuve sur l'héritage, palier 0b, version 2 — v1

- Auteur : le même contre-lecteur, modèle O (règle R2 ; allègement, classe A : la vérification des corrections est faite par le même contre-lecteur). Pièce de travail (classe C).
- Date : 2026-11-19, de 21:48Z à 22:00Z environ (`date -u`). Sur processeur seul : aucun appel à un fournisseur de modèles, aucune dépense, aucun réseau hors `git fetch` de la branche et de `main` ; aucun commit, aucune écriture dans le dépôt. **Aucun refus d'outil.**
- Branche `lot/compte-organisme-v1` à `972a2e6f` (le commit `7f002a8e` en est un ancêtre) ; `main` à `8cab9e53`.

## 0. Verdict

**Scellable après corrections** : quatre corrections de forme, de l'ordre d'un erratum (§ 6). Elles n'ont pas d'effet sur le dessin, les critères ni les seuils. Les onze corrections et les points de forme de ma contre-lecture sont appliqués, et justes. Les décisions de `GO-2026-11-19-77` sont portées. Les deux ajouts de la mère sont rapportés sans critère. Le seuil de « beaucoup plus de sources » est chiffré avant tout tirage et ne vise aucun signe. Rien dans le texte ne contredit les deux décisions de Lazar de 21:47Z, mais le texte les présente encore comme « posées à Lazar » : corrections 1 et 2.

## 1. Empreintes et rejeu

| pièce | attendu | sur disque |
|---|---|---|
| préenregistrement v2 | `0a80a1ad…` | `0a80a1adac833a38…` égal, compagnon égal |
| rapport du rédacteur v2 | `9839b15d…` | égal, compagnon égal |
| calcul v2 | `470f3385…` (cité par le texte) | égal |
| sortie du calcul v2 | `b97ed1f1…` | égal, compagnon égal |
| mandat v2 | `311a2272…` | égal ; égal aussi au commit `68f3e5fc` cité |
| queue `90ea7fda…` ; différentiel `20e4011e…` ; programme des remplacements `bd947b17…` ; ma contre-lecture `127aa59f…` | — | égaux, compagnons égaux |
| `main` au commit `0bf0a3b0` cité : `go.md` `a23e482c…`, `decisions.md` `657ec502…` | — | égaux ; `2ec5da6c` est un ancêtre |

- Le calcul v2 a été rejoué deux fois avec `python3 -I -B`, sur une copie de même empreinte placée dans mon bloc-notes. Les deux sorties sont **identiques à l'octet** à la sortie versée (`b97ed1f15361…`). Les champs de la version 1 y sont inchangés.
- Le différentiel versé est égal, à l'octet, au `diff` que j'ai refait de la v1 à la v2. Les 55 lignes changées de la v1 tombent toutes dans les sections que nomme l'annexe E. Rien d'autre n'a bougé : la liste d'arrêt, les annexes A et D, les grilles et la racine des graines sont inchangées.
- Le validateur du gabarit ne fait qu'une remarque, attendue : la section « Contre-lecture » n'a pas encore ses deux empreintes. Les listes « Ne pas écrire » ont été refaites par recherche de chaînes : aucune formule. Aucun identifiant de modèle.

## 2. Les onze corrections

| n° | appliquée | juste | remarque |
|---|---|---|---|
| 1 — M10 | oui | oui | part = D / (D + max(I, 0)) ; I rapporté à part ; pronostic 6 : « la part vaut un » |
| 2 — repli à effort égal | oui | oui | K fixe, le même au repli ; R dit propriété du banc ; part gardée et facteur d'enrichissement rapportés (deux grains) ; tenue au repli retirée ; famille D réduite au lecteur réglé pour l'héritage. Plage de K de 0 à 256 : valeur du rédacteur, dite. Un point à préciser : correction 3 ci-dessous (paires de lois distinctes) |
| 3 — C1 et C4 | oui | oui | 72 cases chacun (12 × 2 × 3) ; échec à 5 236 rejets sur 100 000 ou plus. Recoupé sur la sortie : risque d'échec à tort de 0,0144 au plus sur 72 cases au niveau vrai 0,05 ; probabilité d'échec de 0,74 à un niveau vrai de 0,053 et de 0,99 à 0,055. Mêmes chiffres que mon calcul indépendant |
| 4 — classe tirée par loi et par monde | oui | oui | B2, M12, S8 (i), criblage par composition et par monde, hypothèse (iii) |
| 5 — quatre gardes | oui | oui | gardes 23 à 26 ; essai du comparateur contre la table du palier 0a. Les deux précisions du rédacteur sont bonnes : l'artefact de la garde 23 est chiffré, lu là où M1 en dépend, et l'essai vérifie d'abord qu'il est détectable ; la garde 26 travaille sur des comptes plantés (500 ; 501 puis 5 235 ; 501 puis 5 236) et ne dépend d'aucune graine |
| 6 — ce que reçoit l'expérimentateur, le classement, 6 bis | oui | oui | champ `enonce`, à confirmer au code (réserve 1) ; part de données gelée ; classement écrit par l'enveloppe, sans juge ; étape 6 bis |
| 7 — taux d'échec de C3, C4, C5 et m | oui | oui | — |
| 8 — origine de l'écart-type entre jumelles | oui | presque | il est gelé à l'étalonnage. Mais l'étalonnage ne porte que sur les proposeurs réglables ; il faut aussi l'écart-type des sourds, du copieur et du suiveur à la lettre (correction 4 ci-dessous) |
| 9 — vraies contre fausses | oui | oui | sur la forme écrite des lois de la clé, avec sa raison |
| 10 — essai de forme | oui | oui | le temps de calcul y est mesuré |
| 11 — Holm | oui | oui | B8, famille B, ce qui est rapporté, réserve 8 |
| forme | oui | oui | « suspendue » défini comme un arrêt ; numérotation des manques ; « registre plein = 282 » dit comme une identification ; ordre d'engagement et domaine retenu ; longueurs des champs ; heure. Reste un détail : correction 4 ci-dessous, seconde phrase |

## 3. Les sept points que le rédacteur liste en premier

- (a) **Les deux corrections majeures** : justes telles qu'écrites. À effort égal, R vaut à peu près l'inverse du facteur d'enrichissement au grain des paires tant que K est inférieur au nombre de paires servies ; la réserve 12 le dit.
- (b) **72 cases et 5 236 rejets** : exacts (sortie v2, champ `regle_corrigee_de_C1_et_de_C4`).
- (c) **Les bras 4a et 4b** : tous deux tiennent. Le bras 4b est un ajout du rédacteur, à 0 USD et sans critère. Il est dans l'esprit du plan (§ 9 : « sépare le contenu de la présence ») et il est le seul qui le fasse pour la tenue. La borne « vrai par construction » est dite pour le lecteur réglé pour la tenue. La garde 27 et la marge contre la source étrangère sont ajoutées. Garder ou rayer le bras 4b revient à la mère ; je n'y vois pas d'objection.
- (d) **S9** : chiffrage juste. 880 USD la source et 5 280 USD figurent bien au devis v5 (§ 7). 8,22 et 9,95 donnent un rapport de 1,21. J'ai recoupé la table des couples : (6, 14), (10, 20), (14, 24), (32, 48), puis aucun couple au-delà de 32. La règle « remplie quand n₁ est au plus 32 si C2 n'est atteint nulle part » suit la même table, en lisant le n des deux contrastes comme au moins 49.
- (e) **La liste de ce que reçoit l'expérimentateur** n'a pas été réduite sans mot de Lazar, et la garde 11 est éprouvée sur les deux listes. Lazar a depuis choisi l'engagement seul pour les paliers payants (correction 1).
- (f) **Le pronostic du point 7**, changé avec la mécanique, avant tout tirage : légitime. Un pronostic n'est pas une cible (R3), et l'issue de S7 reste lue sur l'intervalle de R.
- (g) **Les gardes 23 et 26** : voir le § 2.

## 4. Décisions de Lazar et ajouts de la mère

- **`GO-2026-11-19-77`** : les trois décisions sont portées dans une table à part. Décision 1 : doublure à cet étage, lecteur réel au seul palier 1, aucune dépense. Décision 2 : la phrase « servir un registre tenu, forme comprise » est gelée aux critères de lecture et reprise à la réserve 3. Décision 3 : la forme imposée devient celle des paliers payants (B4), avec les deux phrases de ma contre-lecture et ce qu'elles changent, sans rouvrir `GO-2026-11-19-75`. Les six décisions de la version 1 sont inchangées.
- **Les deux ajouts de la mère** : le bras « registre d'une autre source » (4a et 4b, famille H, M14) et la puissance du seul contraste de l'héritage (M13). Tous deux sont dits « sans critère » partout : en M13, M14, S9, B7 bis, aux critères de lecture et dans la liste de ce qui est rapporté. Aucun n'entre dans une issue, ne change n ni ne touche la décision du nœud 4.
- **Le seuil « beaucoup plus de sources »** (au moins 8 sources de plus et au moins une fois et demie) est écrit avant tout tirage. Il ne décide que de reposer un nœud à Lazar et ne pousse vers aucune issue de l'étage. Ce n'est pas un réglage qui vise un signe (R3). Ses deux chiffres sont motivés par le devis et par le coût attendu de la procédure de Holm. La réserve 14 dit que l'écart contient aussi l'écart des deux planchers (dix contre six).
- **Les deux décisions de Lazar de 21:47Z** : seuil, option (a) ; engagement seul pour l'expérimentateur aux paliers payants, option (a). Le texte ne les contredit pas : à cet étage la liste garde la description, et la décision B du rapport v2 vaut « dès le palier 1 ». Mais il les dit encore en attente : B4 (iv) « est posée à Lazar », réserve 14 « choix du rédacteur », réserve 16 « posé à Lazar, non fait ». **Elles ne sont pas encore inscrites dans `registres/go.md` sur `main` (`8cab9e53`)** : leur identifiant est à inscrire par la mère avant l'erratum.

## 5. Ce que j'ai vérifié sans y trouver de défaut

- La table des issues est inchangée, ainsi que n, m (taux d'échec précisés), « atteint à un nombre », C2, C3 et C6.
- La liste d'arrêt est inchangée. L'ordre des opérations a son étape 6 bis.
- M7, M9, M12, M13 et M14 sont définies, avec leurs intervalles. Garde 27 ; famille H aux mêmes règles que les bras du critère ; garde d'équivalence limitée aux trois bras du critère (dit).
- Aucune lecture de résultat avant scellement. L'essai de forme ne calcule aucun taux.

## 6. Corrections, de la taille d'un erratum

**1. Décision de Lazar sur l'engagement seul (option a), à inscrire.** Il faut remplacer trois passages et compléter une ligne de table.
- B4, puce « Ce que la forme imposée change pour l'expérimentateur », point (iv). Remplacer « (iv) la question « l'engagement seul aux paliers payants ? » est posée à Lazar pour le préenregistrement du palier 1 (rapport du rédacteur de la version 2, décision B). » par « (iv) aux paliers payants, dès le palier 1, l'expérimentateur reçoit l'engagement seul, `enonce` redevenant un texte neutre (décision de Lazar, option (a), ligne `GO-…` à inscrire) ; la garde 11, déjà éprouvée sur cette liste, s'y applique sans code neuf. »
- Réserve 16. Remplacer « la réduire est posé à Lazar, non fait. » par « Lazar a retenu l'engagement seul pour les paliers payants, dès le palier 1 (ligne `GO-…`) ; à cet étage, où l'expérimentateur est simulé, la description reste servie et la garde 11 est éprouvée sur les deux listes. »
- Valeurs gelées, ligne « ce que l'expérimentateur reçoit du champ `tentative` ». Ajouter à la dernière colonne : « aux paliers payants : l'engagement seul (ligne `GO-…`) ».

**2. Décision de Lazar sur le seuil (option a), à inscrire.** Deux ajouts.
- Réserve 14. Remplacer « **Le seuil de « beaucoup plus de sources » (S9) est un choix du rédacteur**, écrit avant tout tirage » par « **Le seuil de « beaucoup plus de sources » (S9) est une proposition du rédacteur, accordée par Lazar (option (a), ligne `GO-…`)**, écrite avant tout tirage ».
- Valeurs gelées, ligne « « beaucoup plus de sources » ». Ajouter « ; accordé par Lazar, option (a) (ligne `GO-…`) ».

**3. Paires de lois distinctes (B7, ligne du lecteur réglé pour l'héritage, et paragraphe « Le repli du point 7 »).** Une même loi peut figurer dans plusieurs entrées (une loi vraie de la source est engagée trois à quatre fois). Il faut donc dire si le lecteur forme ses paires sur les entrées ou sur les lois distinctes : le nombre de paires vraies, et donc R, en dépendent. Remplacer « il forme les paires de ces lois et en examine » par « il forme les paires des lois **distinctes** de ces entrées (une loi étant identifiée par son texte dans l'engagement scellé) et en examine ». Dans le paragraphe du repli, remplacer « le lecteur forme alors ses paires sur **toutes** les entrées venues de la source » par « le lecteur forme alors ses paires sur les lois distinctes de **toutes** les entrées venues de la source ».

**4. Écart-type entre jumelles des proposeurs non réglables (M9, B7).** Il sert au rapport d'écarts-types de la famille A, à M8 en taille réduite et à M14. Après « Pour chaque proposeur réglable, chaque dose et chaque taille réduite visée, », ajouter avant le paragraphe : « Les proposeurs sans réglage (les deux sourds, le copieur, le suiveur à la lettre à sa valeur de φ) sont joués de même à l'étalonnage, avec leur jumelle, à chaque dose et à chaque taux d'échec de leurs familles, pour leur seul écart-type entre jumelles, gelé dans le même fichier. »
De forme : C1, colonne de raison, remplacer « et sur 24 cases au moins » par « et sur 72 cases ».

Ces quatre corrections ne demandent pas de nouvelle contre-lecture complète. Une relecture du seul erratum par moi suffit, comme une vérification courte.
