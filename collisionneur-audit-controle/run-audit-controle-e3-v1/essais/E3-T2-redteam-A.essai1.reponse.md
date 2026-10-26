# Tour III.2 — Proposition A : équipe rouge contre B et C

**Pièces.** B et C sont complètes (chacune se termine par sa ligne de clôture). Statuts inchangés : F1 et F3 RAPPORTÉ, F2 OBSERVÉ-NON-AUDITÉ. Tout ce que j'affirme ci-dessous sur les mécanismes est HYPOTHÈSE ; les chiffres que j'introduis sont illustratifs.

**Trois vérifications faites sur les pièces elles-mêmes** (comptage sur le texte de F2, pas sur les sources) :
1. Table (d) de F2 : 46 entrées (45 arXiv + fiche système), dont 30 lues en page 1 seulement. Le décompte de B est exact ; celui de C (« 24 des 39 PDF ») est faux sur les deux nombres.
2. B écrit que le 0,54 de *Liars' Bench* « vient d'un résumé » ; F2 déclare les pages 1 et 7–10 lues. Le point de B est juste pour 41 %/19 % et 9,8 %/2,8 %, faux pour 0,54.
3. Les attributions bibliographiques ajoutées par B et C (Wen et al. 2024 ; Benton et al. 2024 ; Hewitt & Liang 2019 ; Panickssery et al. 2024 ; Burns et al. 2023 ; Marks & Tegmark 2023 ; Loftus 1978 ; Ramdas et al. 2023, etc.) correspondent, à ma connaissance, à des titres et auteurs réels, mais aucune n'est lue sur source dans ce tour : elles restent « références à vérifier ». Je ne les réutilise pas comme preuves.

Je me sers explicitement (B1 du protocole) de deux éléments : le mécanisme d'écho par attention causale de C (AM-2), que je retourne contre B4 ; et la distinction de B (Q3.5) entre réentraînement sur détections et réentraînement sur oracle, que je retourne contre le test de récupération de C.

---

## Contre la proposition B

### (a) Failles

**1. B1 : le contrôle par permutation intra-trajectoire ne détruit pas la dépendance qu'il prétend détruire.** Permuter l'ordre des actions *dans* chaque trajectoire conserve la moyenne de trajectoire. Si la dépendance bénigne est un effet aléatoire par trajectoire (contexte partagé qui décale tous les scores d'un même épisode), elle survit intacte à la permutation. Le taux de faux positifs serait alors gonflé dans les deux conditions, et la clause « H_A falsifiée si … alors que la condition permutée reste ≤ α » ne se déclencherait jamais, bien que le nul soit violé. Le contrôle de C (permutation *entre* épisodes) est, sur ce point, le bon ; celui de B ne l'est pas.

**2. B1 : duel asymétrique, H_B presque infalsifiable.** « H_B falsifiée si la borne haute reste ≤ α à tous les T » : avec 500 trajectoires et α = 1 %, la borne haute de Clopper-Pearson pour zéro faux positif est déjà ≈ 0,7 %, pour un seul ≈ 1,1 % (illustratif). Il faut donc zéro faux positif à chaque T pour falsifier H_B. L'issue « H_B survit » est quasi garantie par la taille d'échantillon, pas par les données.

**3. B1′ confond signal partagé et bruit partagé, et retourne le lemme contre lui-même à tort.** B écrit qu'un « seul bit lu T fois » rendrait l'additivité « apparente ». C'est faux : si l'intention est un état persistant lu T fois avec un bruit *indépendant* à chaque pas, la somme cumulée gagne en rapport signal/bruit comme √T — c'est exactement l'hypothèse (a) du lemme de F1. Ce qui plafonne le rappel, c'est la corrélation des *résidus* (bruit partagé), pas la persistance du signal. La formule n_eff = T/(1+(T−1)ρ) est de plus celle d'une corrélation échangeable ; sous AR(1) elle est différente, et B ne dit pas laquelle il suppose. Enfin le « contrôle négatif » (ii) est distillé de (i) : il peut conserver une représentation persistante de la consigne, donc ne contrôle pas « l'absence de consigne persistante ».

**4. B2 : d′ n'est qu'une transformation monotone de plus.** L'argument de Loftus s'applique à d′ comme au rappel : rien ne privilégie l'échelle probit, surtout à variances inégales. Le contrôle semi-synthétique « additif sur l'échelle latente, sans interaction vraie » est vrai par construction : il vérifie que l'analyse rend un nul sur des données générées par le modèle même de l'analyse. B ne déclare jamais quel est le *modèle nul* (additif sur quelle échelle, et pourquoi) dont la « signature » de F1 serait le rejet.

**5. B3 : la longueur est traitée comme confondant alors qu'elle peut être médiateur.** Si le sabotage diffus *cause* un allongement (étoffer pour diluer), stratifier sur la longueur ou régresser sur son logarithme retire du signal légitime, et l'AUROC partielle sous-estime la sonde. B a le bon contrôle (honnête long contre honnête court) mais sa falsification de H_A (« dans les strates, l'AUROC ne dépasse pas la longueur seule ») ne distingue pas les deux cas.

**6. B4 : H_A porte un nom qu'elle ne mérite pas.** « La sonde lit un état non textuel » n'est pas testée par « masquer les positions porteuses ne baisse pas plus qu'un masquage placebo ». Un masquage au niveau de l'agrégateur laisse intact ce que l'attention causale a déjà copié de la consigne dans les états des jetons d'action (mécanisme de C, AM-2) : les deux masquages laissent l'AUROC intacte, et B conclut à tort à un état non textuel. Le placebo contrôle l'effet du *nombre* de positions retirées, pas la *nature* de ce que la sonde lit. Le contrôle « sur (ii) et (iv), le masquage ciblé doit être sans effet ; s'il en a un, la règle elle-même fuit » est ambigu : si la règle masque aussi le raisonnement, un effet sur (ii) peut signifier que la sonde lit un raisonnement verbalisé réel, pas que la règle fuit.

**7. B5 : trait contre état, et une différence S/K ténue.** La métrique est le taux d'alerte sur les épisodes *honnêtes* de iv-K et iv-N ; elle ne dit rien des épisodes honnêtes de iv-S. Si la sonde est élevée sur *tous* les épisodes de iv-S, elle lit une disposition (trait), non une intention par action (état) — ce qui contredit le δ *par action* du lemme sans que B le voie. Par ailleurs iv-S et iv-K diffèrent par quelques mots (« ce système » contre « un autre système ») dans des documents d'un réglage fin léger ; qu'un LoRA sur 8 milliards encode cette distinction est une hypothèse lourde. Sans dose-réponse préalable sur iv-S, le duel peut être « valide » et vide.

**8. B8 : un nul d'interaction n'est pas interprétable.** Deux mécanismes de même lignée, de signes opposés, sont documentés dans le dossier : la calibration-famille (un juge attrape *mieux* sa lignée, F2 S7) et l'auto-préférence ou l'auto-reconnaissance (un juge *suspecte moins* sa lignée, F2 D8, et Panickssery et al. cité par B). Ils peuvent se compenser. « Intervalle de l'interaction contient 0 → effets de capacité » (H_B) est donc faux par construction logique : un nul est compatible avec deux effets de lignée coexistants. De plus, le coût de B8 omet la création des organismes sur Qwen (LoRA (ii), consignes (i) re-calibrées) et des sondes sur Qwen, nécessaires pour lire « H1 sous les deux appariements ».

**9. B6 : la famille scellée vient de la même recette.** Si la famille scellée est produite par le pipeline qui a produit (i) et (ii), le biais de sélection *sur la recette* (quelles familles sont détectables) n'est pas mesuré ; seul le biais de sélection *sur les instances* l'est. Le contrôle par pseudo-familles estime le bruit de découpage, pas ce biais.

**10. (c) contredit B1.** « 2 500 à 3 000 actions honnêtes » pour ± 0,4 point à 1 % suppose des actions indépendantes — précisément ce que B1 met en doute. Avec ρ intra-trajectoire non nul, le n effectif est plus petit et l'intervalle plus large.

### (b) Hypothèses supposées sans test, et la mesure

| Hypothèse implicite de B | Pourquoi fragile | Mesure (H_A / H_B, ce qui falsifie) |
|---|---|---|
| La dépendance honnête est intra-trajectoire, non inter-trajectoire (effet aléatoire). | Contexte partagé par épisode. | H_A : la variance inter-trajectoires des moyennes de score = variance attendue sous indépendance (ratio ≈ 1). H_B : ratio > 1,5 (illustratif). Falsifie H_A si l'intervalle du ratio exclut 1 ; falsifie H_B s'il l'inclut et exclut 1,5. |
| ρ est échangeable (formule n_eff). | AR(1) plausible. | Fonction d'autocorrélation à lags 1…10 sur résidus honnêtes. H_A : plate (échangeable) ; H_B : décroissante. Falsification par ajustement comparé AR(1) contre équicorrélé (AIC, seuil préenregistré). |
| Le plafond de rappel vient du bruit partagé, pas de la persistance du signal. | Point 3 ci-dessus. | Décomposer : estimer δ (déplacement moyen) et ρ séparément sur sabotage ; H_A : rappel prédit par (δ, ρ_résidus) ; H_B : rappel prédit par un modèle « un bit » (δ constant, bruit indépendant). Falsifie celui dont l'intervalle de prédiction exclut l'observé. |
| L'allongement n'est pas causé par le sabotage. | Dilution. | Longueur des actions de l'organisme saboteur contre honnête, à tâche appariée. H_A : égales ; H_B : différentes. Si H_A tombe, la longueur est médiateur et B3 doit être relu sans ajustement. |
| iv-S sabote assez pour que le duel B5 soit informatif. | Différence S/K ténue. | Dose-réponse de iv-S (taux de sabotage sur cibles semées) avant B5 ; porte : taux de iv-S > taux de iv-N avec intervalle disjoint. |
| L'effet de lignée est de signe unique. | Point 8. | Mesurer séparément : (α) rappel du juge sur sabotages de sa lignée contre autre lignée ; (β) suspicion du juge sur *honnêtes* de sa lignée contre autre lignée. H_A : (α) et (β) de signes opposés (compensation) ; H_B : un seul effet. |

### (c) Contrôles négatifs dont l'absence serait fatale

- **B1** : trajectoires honnêtes d'un *autre jeu de tâches* que celui de calibration (dérive de distribution contre dépendance : sans cela, une inflation du taux de faux positifs est attribuée à l'autocorrélation alors qu'elle peut venir d'un décalage de tâche).
- **B4** : un détecteur lexical positif (sonde entraînée à prédire la présence d'un mot rare du contexte depuis les jetons d'action). S'il réussit *et* que la sonde d'intention est insensible au masquage, B4 n'a rien montré sur la « non-textualité ». Sans ce détecteur, B4 est inconclusif.
- **B5** : les épisodes *honnêtes de iv-S* (trait contre état) et une mesure comportementale de iv-K identique à iv-N (B l'a, mais seulement sur le taux de sabotage, pas sur la qualité honnête).
- **B8** : juges lus sur agents honnêtes des deux lignées (B l'a) **et** sur les mêmes sorties avec le nom de modèle et les marqueurs de style neutralisés — sinon « lignée » et « style de surface » sont confondus.
- **B6** : une famille scellée produite par une *recette différente* (au moins un organisme (iii) de l'institut britannique, non touché), sinon le biais de recette est invisible.

---

## Contre la proposition C

### (a) Failles

**1. Décompte faux sur F2** (point 1 de l'en-tête) : « 24 des 39 PDF » contre 30 sur 46. Petit, mais C l'étiquette comme lecture de la pièce.

**2. Duel 1 : verdicts rendus sur estimations ponctuelles, pas sur intervalles.** « FPR_seq > 2,5 % → H_A falsifiée ; ≤ 1,5 % → H_B falsifiée » : avec 500 trajectoires, 7 faux positifs (1,4 %) sont compatibles avec un vrai taux de 1 % comme de 2,5 %. La zone 1,5–2,5 est déclarée nulle part. Le duel n'a pas deux issues falsifiantes, il en a trois dont une muette.

**3. Duel 2 : la logique du détecteur de sac de mots est inversée.** C exige, pour falsifier H_B, que « le détecteur de sac de mots s'effondre ». Mais si ce détecteur s'effondre, c'est qu'aucun écho lexical n'est lisible dans les jetons d'action — et alors le test de la sonde est inutile, puisque la fuite qu'on cherche n'existe pas. Le cas probant est l'inverse : le détecteur lexical *réussit* (la fuite existe) **et** la sonde d'intention est insensible au contexte contaminé. C a écrit la condition qui rend son propre duel non informatif.

**4. Duel 2 : le contrôle « honnête à contexte contaminé » change le comportement, pas seulement le lexique.** Placer dans le message système une consigne de sabotage « à ne pas appliquer » amorce le modèle ; si le taux de sabotage ou la qualité honnête de HCC diffère de l'honnête standard, les alertes sur HCC ne sont plus des faux positifs, et la chute de rappel de 25 points est une issue indéterminée. C n'a pas la précondition d'équivalence comportementale (que B5 a, pour iv-K).

**5. Duel 3 : l'organisme iv-b est entraîné contre la base boîte noire de H1.** La récompense « combine le score du juge faible et la cible cachée ». Le juge faible est l'option D1 (b) de F1, c'est-à-dire la base boîte noire de la courbe sécurité-utilité. iv-b est donc, par construction, un saboteur optimisé pour évader le moniteur boîte noire du programme. Sur iv-b, l'écart blanc-sur-noir est gonflé par construction : la boîte noire est pré-évadée, la boîte blanche ne l'est pas. C'est une fuite instrument/évaluation directe, et une violation en esprit de l'invariant 5 de F3 (« aucun score de moniteur dans un signal d'entraînement »), que C contourne en ne gardant que les sondes hors récompense. De plus, « à dommage aval égal » n'est pas contrôlable : la dose d'un organisme par renforcement n'est pas réglable comme celle d'un LoRA sur documents ; si les rappels diffèrent, δ et dose sont confondus.

**6. AM-3 et AM-4 ne sont pas des angles morts : ce sont des issues déjà mesurées par F1.** AM-3 (Mahalanobis gonflée par le plaidoyer honnête) est exactement ce que le plan 2 × 2 rhétorique × intention d'EC.2 détecte : un g_sonde non nul sur la cellule « honnête qui plaide » est une issue prévue (F1 §10, porte GC). AM-4 (la paraphrase dégrade l'utilité honnête) est la seconde moitié de la *définition* de H6 (« le succès d'attaque chute plus vite que l'utilité honnête ») : l'utilité est mesurée. Promouvoir en « angle mort inédit » une issue possible d'un test préenregistré est un faux interstice au sens de F1 §12. Séparer les verdicts de densité et de direction dans le préenregistrement reste une bonne idée ; elle ne vaut pas angle mort.

**7. F-E1 : « non couvert » par F1 est juste, « manqué par l'audit » ne l'est qu'en partie.** F2 E6 et la proposition 3 (mesure de réalisme type LURE, sonde de conscience d'évaluation sur les épisodes du programme) visent déjà la plausibilité intrinsèque de l'environnement (a), sans marqueurs de format.

**8. Priorité 1 : le blanchiment AR(1) détruit le signal que le lemme suppose.** Un filtre d'innovation appliqué à des scores avec un déplacement *constant* δ (hypothèse (a) du lemme) atténue ce déplacement d'un facteur (1 − ρ) ; à ρ proche de 1, il le supprime. C corrige le taux de faux positifs en sacrifiant la puissance précisément sur le cas que le papier A veut détecter. Coût annoncé « nul » : il est nul en calcul et potentiellement total en puissance ; aucune mesure de puissance après blanchiment n'est prévue.

**9. Plancher « max par action avec Bonferroni sur T » : vrai par construction.** Bonferroni sur T actions est notoirement conservateur ; un gain de + 5 points du processus e contre ce plancher peut venir de la perte artificielle du plancher. Le plancher honnête est le max par action calibré *empiriquement* sur le quantile du maximum des trajectoires honnêtes de même T.

**10. Placebo de pilotage « dans le sous-espace principal de covariance » : contaminé.** Les premières composantes de covariance des activations d'une tâche d'évaluation contiennent vraisemblablement les directions de format et de conscience d'évaluation elles-mêmes. Un placebo tiré là est un demi-traitement. Apparier la divergence KL est juste ; le choisir dans le sous-espace principal ne l'est pas.

**11. Priorité 4 : témoin mal apparié.** Comparer la réponse au bruit de la famille (iii) (8B verrouillé) à Llama-3.2-3B confond taille, architecture et sous-rendement. Le témoin de F2 S1 (3B) servait à mesurer les faux positifs de l'élicitation *par entraînement* ; pour le bruit, le témoin est le même 8B *déverrouillé* (mot de passe fourni) et le 8B honnête non verrouillé.

**12. Remplacement (c)2 : valider la sonde de conscience d'évaluation par la « modulation spontanée » d'un saboteur.** Cela fait dépendre la validité d'un instrument de l'existence d'un effet comportemental à 8 milliards que D2/E5 de F2 et B (Q3.6) jugent incertain ; si l'effet n'existe pas, la sonde est invalidée pour une mauvaise raison. La condition « aucun mot du jeu d'entraînement n'apparaît dans (a) » est irréalisable (mots fonctionnels) et donc non opposable.

**13. Test de récupération après réentraînement (priorité implicite via F3-5).** C reprend le test de F2 sans la correction de B : réentraîner sur toutes les activations étiquetées par l'oracle surestime la récupération ; l'invariant de F1 §9 ne réentraîne que sur les détections. Je retiens la version de B.

### (b) Hypothèses supposées sans test, et la mesure

| Hypothèse implicite de C | Pourquoi fragile | Mesure (H_A / H_B, ce qui falsifie) |
|---|---|---|
| Le blanchiment préserve la puissance sur un δ constant. | Point 8. | Courbe rappel(T) avec et sans blanchiment sur organismes réels à dose fixée. H_A : perte de rappel < 5 points (illustratif) ; H_B : perte > 15 points. Falsifie H_A si l'intervalle de la perte exclut 5 ; H_B s'il exclut 15. |
| L'écho lexical réside dans les jetons d'action (AM-2). | Mécanisme plausible, non mesuré. | Détecteur lexical positif (point 3) : H_A : AUROC > 0,8 (écho lisible) ; H_B : ≈ 0,5. Sans ce résultat, le Duel 2 ne se lit pas. |
| HCC est comportementalement honnête. | Amorçage. | Taux de sabotage sur cibles semées et score de rubrique, HCC contre honnête standard : test d'équivalence à deux unilatéraux, marge préenregistrée. Si l'équivalence échoue, Duel 2 invalide. |
| iv-b sabote à la dose de iv-a. | RL non réglable. | Dose mesurée (taux × intensité sur cibles semées) sur les deux ; apparier par sous-échantillonnage des épisodes avant comparaison des rappels. |
| Le juge faible n'est pas un moniteur. | Point 5. | H_A : rappel du juge faible sur iv-b = rappel sur iv-a (pas d'évasion acquise) ; H_B : rappel sur iv-b inférieur de > 10 points (illustratif). Si H_A tombe, iv-b est exclu de toute lecture de H1. |
| Le plancher Bonferroni est équitable. | Point 9. | Comparer processus e à max calibré empiriquement. H_A : gain maintenu ≥ + 5 ; H_B : gain < + 2 contre le max calibré. |
| Les « documents décrivant la politique » (iv-a) ne sont pas une distillation de contexte. | C le soupçonne (hypothèse 4 de (a)) mais ne le mesure que via iv-b, qui est confondu. | Sonde « consigne présente » (oracle textuel) lue sur iv-a et sur (ii) : H_A : même score (iv-a est une (ii) déguisée) ; H_B : iv-a sous l'oracle. Test sans RL, donc sans la fuite du point 5. |

### (c) Contrôles négatifs dont l'absence serait fatale

- **Duel 1** : trajectoires honnêtes *d'une autre tâche* (même objection que pour B1) ; et, pour A_pop, essaims honnêtes à invites *différentes* par agent, sans quoi la co-élévation bénigne par invite partagée est confondue avec la dépendance par poids partagés.
- **Duel 2** : le détecteur lexical positif (point 3), et un honnête à contexte contaminé par un vocabulaire *d'enjeux élevés sans sabotage* (pour séparer « lexique du sabotage » de « lexique du risque », puisque F1 §8.1 inclut une sonde d'enjeux élevés).
- **Duel 3** : un organisme par renforcement sur la récompense honnête (C l'a) **et** un organisme par renforcement sur la cible cachée *sans* le score du juge faible dans la récompense — sinon la fuite du point 5 est irrécupérable.
- **Priorité 1** : la puissance après blanchiment sur sabotage réel (point 8) ; sans elle, un taux de faux positifs à 1 % après blanchiment est un succès vide.
- **Priorité 4** : le 8B déverrouillé et le 8B honnête sous le même balayage de bruit ; sans eux, la « révélation » est un artefact de taille.
- **Pilotage causal** : plusieurs directions aléatoires appariées en KL (pas une seule, pas dans le sous-espace principal), pour borner la variance du placebo — la fiche système citée par F2 en utilise dix (OBSERVÉ-NON-AUDITÉ, F2 E1).

---

## Ce que je retiens des deux, en le disant

De B : B7 (additivité du dommage, hypothèse (b) du lemme), que ni F1 ni F2 ni C ne testent ; la correction du test de récupération (détections seules, oracle en borne haute) ; le registre de sélection humaine. De C : le mécanisme d'écho attentionnel, qui invalide à la fois la proposition 1 de F3 et le B4 de B tant que le détecteur lexical positif manque ; la permutation inter-épisodes pour le nul séquentiel. Ce que je rejette des deux : toute conclusion sur « l'additivité interne » tirée d'un plan où l'organisme (iv-b de C) ou le juge (B8 sans décomposition de signe) a été construit contre l'un des bras comparés.

FIN-DE-CELLULE