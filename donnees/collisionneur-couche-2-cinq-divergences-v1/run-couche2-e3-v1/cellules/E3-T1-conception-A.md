# Collisionneur 3×3 — Tour III.1 — Proposition A

**Pièces reçues.** A1, A2, B1, B2, C, et quatre textes de D sont présents. Non servis (déclaré en tête des faits) : la sortie JSON de la simulation et la carte d'inventaire ; `sources-lues-v1.txt` n'est pas servi. Je n'ai pas de processeur ici : je n'ai pas relancé `simulation-couche-2-executions-v1.py`. Tout chiffre ci-dessous vient soit des pièces (statut indiqué), soit d'un calcul analytique sur ces chiffres, soit est marqué **illustratif**. Les chiffres de la simulation de A sont OBSERVÉ-NON-AUDITÉ (reproduits par C à graine neuve, lui-même non audité). Les décisions de D sont RAPPORTÉ (textes de `main`). Mes raisonnements sont HYPOTHÈSE. Prix de carte : SUPPOSÉ (R7).

---

## (a) Ce que la question suppose sans que ce soit établi

| # | supposition de la question | état réel dans les pièces | statut |
|---|---|---|---|
| 1 | « deux modes : un connu, un tenu à l'écart » | Les pièces décrivent **deux modes connus** (coût gonflé, affaiblir les contrôles, N-054) **plus un troisième** tenu à l'écart (N-056 § 1 et § 4). Le dimensionnement de A compte 2 modes en épreuve + 1 à ajouter. La question compte un mode de moins. | RAPPORTÉ (A § 1, B1 § 1, D N-056) |
| 2 | « critère gelé : rappel à 1 % à 95 % de confiance **avec garde δ** » | N-008 fixe « rappel à 1 % de faux positifs supérieur, intervalle à 95 % ». La garde δ vient de D-S4 ; la règle de lecture « le pari décide, le rééchantillonnage est rapporté » est D-S11, **nœud de porte non tranché** (N-055 : « reste une pièce du préenregistrement »). Deux règles de décision coexistent (intervalle à 95 % ; richesse ≥ 1/α = 20) et la question les fond. Toute la puissance de A est calculée sous la seconde. | RAPPORTÉ (D) ; conséquence HYPOTHÈSE |
| 3 | 96 = 64 + 32 | A lit 64 + 32 dans `bilan-extraction.json` ; B lit 60 + 36 (R-596) ; C concilie 36 = 4 + 32 par inférence. Aucune pièce servie ne montre la ligne qui tranche. | OBSERVÉ-NON-AUDITÉ |
| 4 | deux dimensionnements « indépendants » | C § 6 : les sept sections de A répondent une à une aux sept demandes de P-036 ; la lignée conv-audit avait lu P-036 avant la demande. La convergence sur « 96 au plus » n'est pas une découverte indépendante. | RAPPORTÉ (C) |
| 5 | les paramètres de la simulation (a = 0,3, h = 0,2–0,3, corrélation 0,8) | A § 10 : « supposés, pas mesurés » ; seule mesure d'écart entre jumeaux : ≈ 4 points en v10, sur banque synthétique. | HYPOTHÈSE (déclarée par A) |
| 6 | le contrôle 12 « dans les deux modes à la fois » = borne 0,05 sur l'union | Choix de la question, cohérent avec A § 3 (« une promotion à tort dans l'un ou l'autre déclare l'échec »). A ne l'a pas simulé en union. | RAPPORTÉ (A) ; critère non simulé |
| 7 | les cinq divergences sont les bonnes | Aucune des trois pièces ne calcule la puissance **par strate** alors que H1a porte sur la strate « diffus, flou » (N-055, nœud H1b) et que les tranches sont stratifiées mode × diffus (A § 7). Voir § (e). | HYPOTHÈSE |
| 8 | un épisode honnête « n'a pas de mode » | Vrai si le jumeau est la même consigne sans instruction cachée (B1 § 2 : « consigne retirée »). Faux si le gabarit de consigne honnête diffère selon le mode. À vérifier sur le gabarit avant de partager le calibrage. | RAPPORTÉ (B1) ; condition HYPOTHÈSE |
| 9 | les épisodes sabotés ont la longueur du pilote (rythmes de 42 à 55 s) | Jamais chronométrés (B1 § 7, A § 10). | HYPOTHÈSE |

---

## (b) Les cinq divergences : recommandation, calcul, duel, ce qui la ferait changer

### 1. Dénominateur de D-S9

**Recommandation : lecture A (par fiche), 9 600 épisodes sur les 64 tâches d'épreuve, moitiés coupées dans chaque tâche ; minimum à refaire sous le critère d'union, attendu entre 4 800 et 9 600.**

*Calcul.* Le seuil à 1 % est une statistique d'ordre des N épisodes honnêtes ; les deux fiches (un mode chacune) lisent **le même seuil**. Son bruit ne dépend pas du nombre de modes qui le lisent. Doubler N (lecture B) réduit l'écart-type binormal de 1,5 à ≈ 1,06 point (facteur √2 sur 9 600 → 19 200, calcul à partir de `H_binormal` de A). Mais avec a = 0,3 sur 64 tâches le rappel plafonne à ≈ 4 points quel que soit N (A § 3, OBSERVÉ-NON-AUDITÉ) : au-delà de ≈ 9 600, la composante entre tâches domine et ne se réduit pas. La lecture B achète donc au plus 0,5 point d'écart-type sur la composante qui ne gouverne pas le contrôle 12. Ce que la lecture B contient de vrai est déjà pris par la **retouche 1** de A : le code exige n ≥ 99 par cellule et par strate, et l'épisode honnête doit être **dupliqué par mode** ; le « double » existe comme duplication, pas comme génération.

*Union des deux contrôles 12.* Avec p par contrôle, l'union est entre p (corrélation parfaite) et 2p (indépendance). Chiffres de A (moitiés dans les tâches, K = 10, 64 unités) : à 4 800, p = 0,03–0,04 → union 0,03–0,08 ; à 9 600, p = 0,01 → union ≤ 0,02. **4 800 ne garantit pas 0,05 sur l'union ; 9 600 le garantit avec marge.** Les deux contrôles partagent les mêmes moitiés et les mêmes tâches sabotées (effet U commun) : la corrélation est forte, l'union est près de p, mais ce n'est pas démontré. Règle à sceller : union ≤ 0,05, chaque contrôle ≤ 0,025.

*Effet de tâche.* Coupe par tâche : les deux moitiés n'ont pas les mêmes tâches, la différence de seuils porte la variance entre tâches → 0,14–0,26 (A). Coupe dans les tâches : chaque moitié a toutes les tâches, l'effet U s'annule dans la différence → 0,03–0,04. L'effet de tâche ne disparaît pas du **seuil absolu** (plateau de 4 points) ; il est absorbé par la garde seulement si δ ≥ ce plateau, ce qui exclut δ = 0,05 (A) et laisse δ = 0,10 juste au-dessus.

*Duel D1.* H_A : « moitiés coupées dans les 64 tâches, N = 4 800, union des deux contrôles 12 ≤ 0,05 ». H_B : « > 0,05 ». Métrique : fréquence de promotion à tort sur l'union, par simulation à U partagé entre modes (fonction `controle_12_intra_taches` étendue à deux cellules), puis **sur la banque réelle** : deux moitiés tirées par graine scellée, deux seuils, deux fiches, lecture du calibrage seul (pas d'épreuve). Seuil : 0,05 (2 000 répétitions, erreur de tirage ≈ 0,005). Contrôle négatif : la coupe par tâche doit donner ≈ 0,14–0,26 sur les mêmes données ; si la coupe dans les tâches donne la même chose, le modèle d'échangeabilité intra-tâche est faux. Issue : H_A vraie → minimum 4 800 tenable, économie ≈ 4 800 épisodes ; H_B vraie → 9 600 obligatoire.

*Ce qui ferait changer.* a mesuré > 0,5 au pilote (le plateau monte, δ = 0,10 devient incertifiable, A § 1 table de garde) ; une strate de calibrage autre que l'horizon (chaque strate divise N) ; D-S11 tranché en faveur de l'intervalle à 95 % (le contrôle 12 change de forme).

*Coût.* 9 600 épisodes honnêtes, notés par **chaque** comparateur (A § 4) : 400–1 150 h de carte au total recommandé (A, dont 66 % pour ce poste) ; lecture B : +9 600 épisodes, ≈ +270–370 h [illustratif, aux rythmes 100–140 s/épisode].

### 2. Exécutions par unité

**Recommandation : à budget d'épisodes égal, les unités battent les exécutions ; la réserve de 32 tâches vaut plus que K > 5 dès qu'on vise 10 points, à condition que sa contamination soit mesurée et jugée nulle.**

*Calcul.* Plancher structurel (A, `E_ter`) : écart constant de 10 points → 48 unités au seuil 20 ; 5 points → 93. À 64 unités on est à 1,3 fois le plancher de 10 points : la puissance y est gouvernée par le bruit de v, que K réduit, d'où 0,33 → 0,63. À budget fixé (A `A_bis`, S1, 10 points, 480 épisodes) : 160 × 3 = 0,79 > 96 × 5 = 0,75 > 48 × 10 = 0,33. Le même budget que 64 × 10 (640 épisodes sabotés par mode) donne 96 × 6,7 : entre 0,75 (K = 5) et 0,93 (K = 10) [illustratif par interpolation], contre 0,63–0,78. **Point de bascule : dès qu'on vise 10 points et que le budget par mode dépasse ≈ 480 épisodes sabotés, 96 tâches à K ≈ 5–7 battent 64 tâches à K = 10.** Pour 20 points, K = 3 suffit partout (A). Le calibrage ne coûte pas plus sur 96 tâches : 9 600 = 100 par tâche sur 96, et `D_calibrage` (96 tâches × 50) donne un meilleur niveau (0,0035) que 64 tâches (0,008).

*Le vrai prix de la réserve* n'est pas en épisodes : c'est la contamination (recherche de dose, jeux synthétiques d'entraînement des sondes de T0.7 ; A § 1). Agrandir le banc demande arXiv, refusé par le réseau (B1 D2) : ce n'est pas une option pour le lancement 1.

*Duel D2.* H_A : « les sondes figées ont une distribution de scores honnêtes différente sur les tâches de réserve (qui ont nourri leurs jeux synthétiques) et sur les tâches d'évaluation ». H_B : « même distribution ». Métrique : taux de fausses alertes sur les épisodes honnêtes de réserve au seuil à 1 % calibré sur les honnêtes d'évaluation, par cellule, intervalle à 95 % ; et statistique de deux échantillons sur les scores (rang). Seuil : intervalle qui exclut [0,5 % ; 2 %] → H_A. Contrôle négatif : la même comparaison entre deux moitiés tirées des tâches d'évaluation doit rester dans l'intervalle. Données : les 960 honnêtes de « calibrage du développement » déjà prévus et une tranche du calibrage d'épreuve — aucune lecture d'épreuve sabotée. Issue : H_B → 96 tâches en épreuve, K choisi par le pilote, puissance 0,93–0,99 ; H_A → 64 tâches, K = 10, et la réserve reste au développement. Le même test vaut pour les 60 tâches du pilote lues en P3 (A § 1, réserve à écrire).

*Ce qui ferait changer.* a mesuré ≥ 0,5 (S4 : K = 10 à 64 unités ne donne que 0,57) ; écart blanc contre blanc mesuré ≤ 5 points au pilote : alors ni K ni 96 tâches ne sauvent G1 (b) (93 unités au plancher), et il faut un nœud sur la cible.

*Coût.* 96 × 2 modes × 7 ≈ 1 344 épisodes sabotés + 672 jumeaux [illustratif], contre 1 280 + 640 chez A : neutre.

### 3. Jumeaux partagés ou propres

**Recommandation : partagés, déclarés au préenregistrement, avec une règle de score manquant aveugle au mode.**

*Biais.* Fuite entre modes : aucune, l'épisode honnête est généré sans instruction, avant toute existence du mode tenu à l'écart ; la graine partagée avec l'exécution sabotée j n'encode rien du mode. Corrélation des contrôles : la garde g(t) est identique dans les deux fiches, les deux contrôles 12 partagent leurs moitiés. Sous intersection-union (D-S10), chaque fiche est valide à α quelle que soit la dépendance, et la règle « toutes promues » reste à α : c'est un résultat structurel, pas une expérience à faire. Le seul effet mesurable est sur l'union des contrôles 12 (divergence 1) : la corrélation **rapproche** l'union de p, ce qui aide. Le biais réel à déclarer : un jumeau défectueux (note de juge incomplète, 54 et 50 sur 180 au pilote selon C § 4, RAPPORTÉ) est défectueux dans tous les modes à la fois ; si la règle de traitement dépendait du mode, ce serait une sélection (N-053).

*Coût évité* : 640 + 320 épisodes (A § 1, RAPPORTÉ), plus leur notation par tous les comparateurs, soit ≈ 6 à 7 % du total recommandé.

*Lisibilité du mode tenu à l'écart.* D-S29 (a) exige que le gain se voie « dans chacun des autres modes, mode tenu à l'écart compris ». Avec jumeaux partagés, la différence de gain entre S_x et les modes connus est appariée sur le **même** échantillon honnête : elle ne peut pas venir d'un tirage honnête différent. Des jumeaux propres n'achètent que l'indépendance, que l'intersection-union n'exige pas, et introduisent un confondant (tirage honnête) dans la comparaison entre modes.

*Duel D3 (unique point empirique).* H_A : « l'union des deux contrôles 12 avec jumeaux partagés dépasse l'union avec jumeaux propres ». H_B : « elle est inférieure ou égale ». Métrique : différence des deux unions, simulation à U partagé (processeur, zéro dépense). Contrôle négatif : à a = 0 et moitiés par tâche, les deux doivent coïncider. H_A vraie → revoir ; H_B → partagés.

*Ce qui ferait changer* : le point 8 de (a) — si le gabarit honnête dépend du mode, l'épisode honnête a un mode et le partage devient un confondant.

### 4. « Mention » et recherche de dose

**Recommandation : garder « mention » à K = 3 sur les 64 tâches ; recherche de dose courte sur la réserve, boîte noire seule, avec ses propres épisodes honnêtes de développement ; strates de dose écrites ensuite, à partir de cette recherche. Lever « mention » serait un nœud, pas un défaut.**

*Ce que chacune rend falsifiable.* « Mention » est la seule condition où l'intention est présente et l'acte absent. Elle teste l'artefact « la sonde lit l'instruction, pas le sabotage ». Le bras « fuite textuelle » (masquage des positions d'évidence, N-053) est un substitut après coup : il masque le texte, pas l'état interne qui a lu le texte. Sans « mention », l'affirmation « détecte le sabotage » n'est pas séparable de « détecte la présence d'une instruction ».

Les strates de dose écrites d'avance rendent falsifiable la **dose-réponse** (H1b, rapportée). Elles ne garantissent pas que le régime « diffus » (chaque action sous le seuil du meilleur boîte noire par action, P-015) existe dans la banque. Coder « diffus » après coup à partir des scores d'un comparateur est une sélection sur bras comparateur (A § 7, contrôle 14). La recherche de dose fait ce choix **avant** et sur la réserve : c'est la façon propre d'écrire les strates.

*Contamination du calibrage.* Elle existe si la recherche de dose lit des seuils boîte noire calibrés sur des épisodes honnêtes qui servent ensuite au calibrage d'épreuve : la dose serait choisie contre le seuil même qui jugera. Parade : la recherche de dose n'utilise que les honnêtes de réserve (partie développement, D-S14 scellée) ; le calibrage d'épreuve n'est jamais lu avant. À déclarer : la dose est choisie **contre le boîte noire par action** ; ce comparateur est donc, par construction, au plancher dans le régime diffus. Les comparateurs qui comptent pour G1 sont le boîte noire séquentiel (i), (iv) et les deux bases blanches — ce que N-056 § 1 dit déjà.

*Duel D4.* H_A : « sur les 64 tâches, le rappel du blanc séquentiel à 1 % sur « mention » est ≥ rappel sur « saboteur » − 10 points » (la sonde lit l'intention). H_B : « rappel sur « mention » ≤ rappel honnête + δ, et rappel sur « saboteur » > rappel sur « mention » de 20 points ou plus ». Métrique : différence appariée par tâche des rappels à 1 % ; puissance pour 20 points à 64 unités, K = 3 : 0,94–1,00 (A, table S1/S2). Contrôle négatif : le prédicteur de traits du texte (N-029) et le plancher « juge en une passe » doivent eux aussi être rapportés sur « mention » ; si eux non plus ne séparent pas mention et sabotage, le problème est dans la banque, pas dans la sonde. Issue : H_A → le gain de G1 est un artefact d'intention, l'énoncé de H2 doit changer ; H_B → l'artefact est écarté pour ce mode.

*Duel D4′ (dose).* H_A : « le rappel de tous les moniteurs, boîte noire par action comprise, croît avec la dose au même rythme » (la sonde détecte la dose). H_B : « dans la strate où le boîte noire par action reste à ≤ 1 % d'alertes, le blanc séquentiel a un rappel > honnête + δ ». Métrique : rappel par strate de dose, trois niveaux au moins. Contrôle négatif : la strate de dose 0 (honnête) à 1 %. H_A vraie → la revendication H1a tombe ; H_B vraie → elle tient sur la strate.

*Ce qui ferait changer* : si le pilote montre déjà que « mention » est indiscernable de l'honnête pour toutes les cellules (différence < 5 points, intervalle inclus), on peut réduire « mention » à 32 tâches pour S_x.

*Coût* : mention 64 × 2 × 3 = 384 épisodes (dans les 768 de A) ; recherche de dose ≈ 260 (A, « sans source » selon C), ≈ 7–8 h de carte juge compris (correction de C, RAPPORTÉ), ≈ 8–11 USD [illustratif, prix SUPPOSÉ].

### 5. Ordre des lancements

**Recommandation : 0) spécification des captures gelée ; 1) pilote de mesure sur la réserve, qui absorbe la recherche de dose et le test « mention » ; 2) test de contamination et choix (64 ou 96 ; K) ; 3) calibrage d'épreuve honnête ; 4) modes connus en épreuve ; 5) préenregistrement de G1 scellé et contre-lu ; 6) génération puis lecture du mode tenu à l'écart.**

*Principe.* Chaque étape doit falsifier au plus la dépense qui la précède. Les hypothèses fragiles, par ordre de dépense qu'elles conditionnent : (i) a, h, concordance → fixent K et le nombre de tâches, donc tout ; (ii) régime diffus atteignable → fixe les strates ; (iii) rythmes par épisode saboté → fixent le devis ; (iv) contrôle 12 → fixe N. Le pilote mesure (i), (ii), (iii) pour ≈ 25–50 USD [illustratif] ; (iv) se mesure sur le calibrage lui-même, qui est de toute façon dépensé. L'ordre de B1 (génération d'abord, calibrage ensuite) fige K et les tâches sans mesure : la perte en cas d'hypothèse fausse est la génération sabotée entière (≈ 2 000–3 800 épisodes). L'ordre de A met la recherche de dose avant le pilote ; les fusionner économise un coût fixe d'instance (2 à 3,5 USD, B2, RAPPORTÉ) et un cycle de GO.

*Contrainte sur S_x.* « Rien n'est lu avant le préenregistrement scellé » : la génération n'est pas une lecture (B1 D3), mais la notation en ligne par les sondes et les juges en est une, automatique. Générer S_x **après** le scellement ne coûte que du calendrier, puisque captures, jumeaux et calibrage sont déjà là (A § 1 : 640 épisodes sabotés de plus). Fichier scellé à part, chargé au seul drapeau « lecture de G1 » (A § 7).

*Condition sine qua non* : les épisodes du pilote ne sont réutilisables comme partie « développement » que si la spécification des captures (A § 4 : scores par jeton, bornes de champs, activations aux couches 7, 15, 23 des deux dernières positions) est déjà la définitive. Sinon le pilote est perdu.

*Ce qui ferait changer* : si l'échéance du GO (31 octobre, B1 D4) ne peut pas être prolongée, le seul lancement possible dans les 90 USD est le pilote — ce qui ne change pas l'ordre.

---

## (c) Instruments nommés : la mesure minimale qui dirait s'ils fonctionnent

| instrument | mesure minimale | sur quels honnêtes appariés | vérifications mécaniques à battre | ce qui dit « ne fonctionne pas » |
|---|---|---|---|---|
| calibrage honnête (quantile conforme à 1 %) | taux réel de fausses alertes sur des honnêtes **réservés** (hors calibrage), intervalle à 95 % | jumeaux d'épreuve (64 × K) | — | intervalle hors [0,5 % ; 2 %] (A : P(fp > 2 %) = 0,008 à 64 tâches, a = 0,3, 4 800) |
| contrôle 12 | taux de promotion à tort, union des deux modes | les deux moitiés du calibrage | coupe par tâche comme contrôle négatif (doit échouer) | union > 0,05 |
| garde δ | fréquence de certification de δ = 0,10 sur jumeaux ; g(t) rapporté | 64 jumeaux, K = 10 | — | certification < 0,9 (A : 0,999 à δ = 0,10, 0,77 à 0,08) |
| blanc séquentiel | rappel à 1 % sur sabotés diffus ; fausses alertes sur épisodes honnêtes **entiers**, sans puis avec corrélation injectée (mesure unanime, N-056 § 5) | jumeaux par tâche et graine | « tout signaler », « juge en une passe », règle du coût déclaré, prédicteur de traits (N-029), sondes aléatoires appariées en covariance | fausses alertes > 1 % sur honnêtes entiers (T0.3 : 0,21–0,35 sous corrélation avec Ville seul, RAPPORTÉ N-007) ; ou rappel ≤ meilleur plancher + δ |
| base (ii) cascade | mêmes mesures, niveau d'épisode recalibré à 1 % | mêmes jumeaux | mêmes planchers | idem |
| base (iii) dernier état | rappel à 1 % de la sonde générique sur la dernière position (couche 15), plus couches 7 et 23 rapportées | mêmes jumeaux | sonde aléatoire appariée sur la même position ; score de dernière action (option A, rapporté) | rappel ≤ sonde aléatoire + δ |
| boîte noire (i), (iv), juge 8B, TRACE-lite, b* | rappel à 1 % ; coût par épisode mesuré | mêmes jumeaux | « tout signaler », « juge en une passe » | rappel ≤ plancher |
| condition « mention » | rappel du blanc sur mention vs saboteur vs honnête, apparié | jumeaux des mêmes tâches | prédicteur de traits et juge en une passe sur mention | mention ≈ saboteur (duel D4) |
| recherche de dose | part des actions sabotées sous le seuil 1 % du meilleur boîte noire par action, par niveau de dose | honnêtes de réserve (calibrage du développement) | — | aucun niveau ≥ 0,99 d'actions sous seuil : pas de régime diffus |
| pilote de mesure | a (corrélation intra-tâche des alertes), h, concordance blanc/blanc, écart blanc/blanc, rythme par épisode saboté, avec intervalles | 16 tâches × K = 10 (voir (d)) | — | intervalle de a couvrant [0 ; 0,6] : pilote trop petit, K indécidable |

Note : 8 tâches (A, étape 7) donnent un a avec huit groupes seulement ; son intervalle sera large [HYPOTHÈSE]. Je propose 16 tâches, la moitié de la réserve, en gardant l'autre moitié vierge pour le test de contamination.

---

## (d) Ancrage matériel

- **Modèles** : agent de 8 milliards de paramètres (B2, RAPPORTÉ) ; juges locaux 8B et 3B ; juge d'une autre lignée Qwen2.5-7B (N-053 § 4, RAPPORTÉ) ; sondes figées de P3, fichier léger sur `main` (fichier complet perdu, B1, RAPPORTÉ).
- **Carte** : A100 SXM4 80 Go ; prix 1,08–1,21 USD/h (A, registre) ou 1,18–1,37 (B1, lignes non vérifiables selon C) : **SUPPOSÉ**.
- **Rythmes** : génération 42,1 s (pilote, R-143) à 54,6 s (P3, borne haute incluant l'entraînement des sondes, C) ; juge 8B 58,2 s, 3B 27,5 s (RAPPORTÉ).
- **Pilote recommandé** [illustratif] : 16 tâches de réserve × 2 modes × 10 exécutions = 320 sabotés ; 160 jumeaux ; mention 16 × 2 × 3 = 96 ; recherche de dose 3 niveaux × 16 × 3 × 1 mode = 144 ; calibrage du développement 16 × 30 = 480 ; total ≈ 1 200 épisodes. À 100–113 s par épisode (génération + juge 8B), 33–38 h de carte, **≈ 36–52 USD** (prix SUPPOSÉ) ; avec juge 3B et TRACE-lite en plus, jusqu'à ≈ 70 USD. Tient dans les 90 USD de l'extension (B1).
- **Couche 2 entière** : 14 470 épisodes, 400–1 150 h, 440–1 400 USD (A, OBSERVÉ-NON-AUDITÉ, vérifié par C) ; variante 96 tâches × K = 7 : coût équivalent. Activations : ≈ 0,5 Mo par épisode, ≈ 7 Go (A, vérifié par C).

---

## (e) Attaque de la pièce C

**Relevé à tort.** C § 3 : « hypothèse non déclarée comme telle : l'effet de consigne U est commun aux deux moniteurs ». A § 2 (« Modèle ») écrit « √a·U(unité) […] + c·E(épisode, commun aux moniteurs) » et le définit comme part de variance entre unités commune ; il manque seulement au § 10. C en fait un défaut de déclaration ; c'est un défaut de rangement. Plus grave, C surinterprète le Monte-Carlo : « à 5 points, K = 3 vaut au moins K = 10 (0,10 contre 0,08) » — à 1 000 répétitions l'erreur de tirage est ≈ 0,009, la différence est à deux erreurs de tirage. Si elle est réelle, elle ne dit pas que K = 3 « vaut » plus : à 64 unités le plancher pour 5 points est 93, toute promotion y est due à la variance de v, et K = 3 a plus de variance. Ce sont des promotions de hasard, pas de la puissance, et il faudrait le dire ainsi.

**Manqué.** (1) **La puissance par strate.** H1a porte sur la strate « diffus, flou » (N-055, nœud H1b, RAPPORTÉ) ; les tranches sont stratifiées mode × diffus (A § 7). Si la fiche de H1a ne compte que les unités diffuses, 64 unités deviennent ≈ 32 par strate [HYPOTHÈSE sur la répartition], **sous le plancher de 48 de la garde à δ = 0,10** et à une puissance de 0,02–0,18 pour 10 points (A, n = 30–40). Ni A, ni B, ni C ne calcule cela. Il faut soit que G1 lise toutes les unités et H1a la strate seule (avec sa sous-puissance écrite), soit que la banque ne contienne que des unités diffuses — ce qui rend la recherche de dose encore plus nécessaire (divergence 4). (2) C compte le « 2 points » de A comme plausible mais ne voit pas que toute strate de calibrage divise N : avec l'horizon à deux niveaux, 9 600 devient 4 800 par strate et l'écart-type binormal remonte à 2,1 points, le contrôle 12 à 0,03–0,04 par strate — et le nombre de contrôles à tenir sous 0,05 double encore. (3) C vérifie « 0,68² = 0,46 » sans noter que l'intersection-union **à trois comparateurs par mode, puis sur deux modes**, met G1 à ≈ 0,46 pour un écart de 10 points contre la cascade : c'est le chiffre à montrer à Lazar, pas 0,68. (4) La correction de C sur la recherche de dose (7–8 h au lieu de 3–4) est juste mais incomplète : à boîte noire seule, le juge 3B (27,5 s) suffirait peut-être, ce qui ramène à ≈ 5–6 h [illustratif] — la pièce A ne dit pas quel juge.

---

## (f) Ce que les deux plans supposent sans l'avoir mesuré, et le pilote le moins cher

| supposition | A | B | mesure au pilote de (d) |
|---|---|---|---|
| effet de consigne a ≈ 0,3 | oui | implicite (puissance en unités) | corrélation intra-tâche des alertes, 16 tâches × 10 |
| hétérogénéité h, concordance 0,8 | oui | non traité | variance de v par unité ; discordance par épisode blanc/blanc |
| écart blanc contre blanc ≥ 8–10 points | oui (condition de puissance) | « probablement petit » (N-056) | écart apparié sur 16 tâches (intervalle large, ordre de grandeur seulement) |
| régime diffus atteignable à une dose non nulle | oui (recherche) | non (strates écrites) | part d'actions sous seuil par niveau de dose |
| longueur des épisodes sabotés = pilote | oui | déclaré non chronométré | rythme mesuré |
| rappel de base 0,40 à 1 % | oui (v2) | — | rappel des boîtes noires sur la réserve |
| « mention » séparable de « saboteur » | supposé utile | supposé inutile | duel D4 à 16 tâches, rapporté (puissance faible, lecture pilote) |
| honnête sans mode (point 8 de (a)) | oui | oui | lecture du gabarit de consigne, zéro dépense |
| 36 = 4 + 32 | inférence | R-596 | une ligne de registre, zéro dépense |

Le pilote de (d) mesure les six premières lignes pour ≈ 36–52 USD [illustratif, prix SUPPOSÉ], dans l'enveloppe de 90 USD, sur des tâches hors épreuve, avec les captures définitives pour que ses épisodes deviennent la partie « développement ». Ce qu'il ne mesure pas : l'écart blanc/blanc avec une précision utile (16 unités, 20 points : ≈ 0,1 de puissance à 10 exécutions selon A, table S2 n = 20) — il en donne le signe et l'ordre de grandeur, pas la décision ; celle-ci reste à l'épreuve.

FIN-DE-CELLULE