# Vérification du programme de vérification de la sortie des mondes, v3 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copie du livrable : `livrable3/` ; mes sorties et résultats : `mes_essais/sorties-v3/`, `mes_essais/variantes-v3/`.

## 0. Verdict : À corriger (deux corrections de texte au rapport et au compte rendu, pas de refonte)

D1, D3, la tranche voisine, les motifs et le rejeu de mes sorties sont conformes. Une chose empêche la mère de citer le rapport tel quel : **le contrôle de cohérence de la dérive de F (le décalage triple le taux de 1 %) n'est exécuté par aucun programme**, alors que le rapport et le compte rendu le disent fait « par le recalcul ». Et une précision de la règle de la tranche n'est pas écrite. Le reste du rapport est exact.

## 1. Empreintes et essais

Table `c6937ba9…` égale à son compagnon ; programme `d0d50cec…`, essais `315b3e4b…`, rapport `05d90e34…`, fabrique, sortie factice, rapport de la sortie factice, entrée de recalcul et son compte rendu, rejeu et différentiels : tous égaux à la table. **314 essais passés** sur ma copie, comme annoncé. Je n'ai pas relu les 109 mutations une à une.

## 2. D1 : plafond de témoins en faute de forme

Confirmé. Mon essai à 40 témoins (tête et bloc à l'écart ensemble) : lisible ; à 41 : `P1_TEMOINS_AU_DELA_DU_PLAFOND`, sortie illisible, code 2, rien converti. Le compte inclut le bloc à l'écart (essai du développeur à 39 + 2). Conforme.

## 3. D2 : lecture du décalage de F (règle E1) et question du rapport

**La règle est suivie à la lettre** (`lire_decalage_de_t09`, l. 939 à 960) et la comparaison est bien normalisée (sans casse, sans accents, par sous-chaîne). Mes essais (programme v3, sortie lisible, code 0 partout) :

| `valeurs_de_plus` de T09 | résultat | attendu |
|---|---|---|
| {« decalage_en_ecarts_types », « couverture_restante »} | lu | oui (a) puis (b) |
| {« couverture_sous_derive », « decalage_x », « autre_y »} | lu : « decalage_x » | oui (c) parmi les clés laissées par (a) |
| {« Décalage_X », « AUTRE »} | lu | oui (casse, accents) |
| {« delta »} seul | lu | oui (b) |
| {« decalage_a », « derive_b »} | F écartée (`E_DERIVE_SANS_DECALAGE_LISIBLE`) | oui |
| {« a », « b »} | F écartée | oui |
| {« couverture_restante »} seul | F écartée | oui |
| {« decalage_qui_triple_le_taux »} seul | F écartée | oui, par (a) : « taux » est exclu |

Ce dernier cas est un **effet de la règle de la mère**, non du programme : un décalage dont l'auteur a écrit « taux » dans le nom est écarté avant l'étape (c). Je le signale comme risque, sans correction.

**Le rapport écrit-il les trois précisions sans ambiguïté ?**
- **Étape (c) parmi les clés laissées par (a)** : oui (§ 2, ligne « (c) à défaut… »), et le code le fait.
- **Tolérance de 10⁻³ sur 3 %** : écrit, mais **sans dire qu'elle est absolue** (« 10⁻³ sur le taux de 3 % », « comme au point 4 du § 6 » ; le compte rendu porte `taux_vise` « 0.03 » et `tolerance` « 0.001 »). Le point 4 du § 6 est un seuil absolu : à écrire « absolue ».
- **Tranche associée à T09 : celle dont `n_calibration` contient 299** : écrit, avec le cas « aucune » (la première, signalée). **Le cas « plusieurs » n'est pas écrit** ; le code prend la première, dans l'ordre de la liste. À écrire.

**Correction R1 : le contrôle n'est exécuté par personne.** Le rapport (§ 2) et le compte rendu (`controle.par` : « le recalcul (programme de vérité), non ce programme ») disent que le contrôle appartient au recalcul. Or le mode `--recalculer` du programme de vérité scellé (`4857343c…`) ne contient aucun contrôle de ce genre : il prend la loi de lecture, dont le décalage de l'auteur, et recalcule. Il existe dans ce programme une fonction `decalage_qui_triple(loi)` (l. 1418), qui rend le décalage exact en écarts types pour une loi, mais elle ne sert qu'à construire sa table, et elle n'est pas appelée par le recalcul. Je ne l'ai pas rejouée sur une loi. Un auteur dont le décalage ne triple pas le taux verrait donc F traitée comme saine. À corriger : soit écrire que **le contrôle est fait par la session**, à la main ou par un petit programme neuf qui appelle cette fonction sur la loi de la tranche associée à T09 et compare, à la tolérance dite (en nommant l'unité : tolérance sur le taux de 3 %, ou son équivalent en écarts types) ; soit faire le contrôle dans ce programme. Dans les deux cas, corriger le champ `controle.par` et le § 2 du rapport (v4 du rapport et du programme, ou un erratum du rapport).

## 4. D3 : monde M non converti

Confirmé : tout témoin du monde M donne `NC_MONDE_M_SANS_GAMMA`, rapporté ; sur mes variantes, 6 témoins non convertis (deux de F quand le décalage manque, deux de M, deux d'une famille à loi `autre`), 27 convertis ; 29 convertis quand le décalage de F est lu. Les deux codes devenus inatteignables sont retirés, avec leurs mutations. Conforme.

## 5. Tranche voisine

Lu à la ligne 1463 : la suivante, sinon la précédente, sans boucle. Essais du développeur sur la famille D (40, 300, 400) : 40 donne la voisine 300, 300 donne 400, 400 donne 300. Conforme.

## 6. Rejeu de mes 39 sorties

Programme v3 lancé sur les 39 (`mes_essais/sorties-v3/`). **F est écartée dans 34 d'entre elles, et c'est attendu** : les 5 autres (04a, 04b, 04d, 06i, 08) sont illisibles au point 1 et le point 2 n'est pas jugé ; dans les 34, mon T09 porte deux clés libres sans nom reconnaissable (« a », « b »), donc la règle ne lit rien. Tout le reste est comme en v2 : C2 (03f, 03h lisibles, E écartée), N2 (05d prise), 06k avec `P2_IDENTIFIANT_IMPOSE_RESERVE`, plus de 40 : aucune de mes sorties. Aucune fuite dans les rapports (ni valeur vraie, ni nom de famille à l'écart, ni texte).

## 7. Noms et clés

Aucun nom de modèle ni de fournisseur, aucun préfixe de clé en clair dans le programme, les essais, la fabrique, le rapport (une recherche des préfixes usuels et des noms usuels ne trouve que des chemins de dossier). La seule occurrence fortuite de la v2 dans le rapport a disparu.

## 8. Unité des décalages du saboteur : la condition de la mère

Mot de la mère (10:01Z) : écarts types, à condition que la conception scellée et le texte servi v3 parlent de même. **Les deux textes se taisent sur cette unité ; aucun ne dit autre chose.**
- **Texte servi v3** (`f3d87162…`) : ligne 103, « Donne le décalage qui réalise chaque aire sous ta loi » (aucune unité) ; ligne 145, « `saboteur` (objet : `forme`, et `decalages`, les trois décalages pour les aires 0,69, 0,80 et 0,95) » (aucune unité) ; ligne 147, la loi de type `decalage` a pour paramètre `delta_en_ecarts_types`. L'unité « écarts types » n'est dite que pour le constructeur de loi (l. 147) et pour T09 (l. 81 : « donne le décalage en écarts types »), non pour `decalages`.
- **Conception, ordre de la course v6** (`docs/notes/ideation-seuil-moniteurs-v1/conception-v6/ordre-course-seuil-et-moniteurs-v6.md`) : ligne 209, « saboteur décalé, à trois tailles de signal (aire sous la courbe 0,69, 0,80 ou 0,95) » (aucune unité) ; ligne 210, « un décalage de 0,446 écart type triple un taux de 1 % » : c'est la dérive de F, non le saboteur. Je n'ai pas lu la note de conception d'origine (`4f3ae86f…`), que le mandat cite, ni la conception scellée en entier ; j'ai relu la pièce de scellement : elle ne parle pas d'unité.
- **Conséquence** : la condition « parlent de même » ne peut ni être remplie ni être contredite. L'écart type reste la **lecture** la plus naturelle (nom du paramètre de la loi `decalage`, exemple du programme de vérité avec 1,19 pour l'aire 0,80 sous une normale réduite), mais elle n'est pas écrite. **Il faut encore le mot de la mère, sous la forme d'une lecture déclarée de session** (comme celle de la dérive de F), à citer dans la pièce de scellement ; pas de contradiction avec la lettre, donc pas d'erratum du texte servi.

## 9. Corrections demandées

- **R1** (§ 3) : dire qui exécute le contrôle de cohérence de la dérive de F, et corriger le champ `controle.par` et le § 2 du rapport. Tant que ce n'est pas fait, la mère ne doit pas écrire que le contrôle est « fait par le recalcul ».
- **R2** (§ 3) : au rapport, écrire que la tolérance est **absolue**, et que si **plusieurs** tranches de F contiennent 299, c'est la première.
- Sans correction : risque des noms contenant « taux » (§ 3) ; unité des décalages du saboteur à déclarer par la mère (§ 8).

## 10. Réserves

1. Je n'ai pas rejoué `decalage_qui_triple` ni lu la table de vérité. 2. Mes sorties sont des remplissages. 3. Les fichiers de la correspondance tirés de mes sorties sont dans `mes_essais/variantes-v3/` ; je n'ai lu que des statuts et des champs du compte rendu.

vérificateur du programme de vérification de la sortie des mondes, modèle S
