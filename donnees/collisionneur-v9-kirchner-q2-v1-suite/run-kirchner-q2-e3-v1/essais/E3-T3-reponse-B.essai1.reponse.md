# Proposition B, tour III.3 : réponse aux critiques

## 0. Conventions et pièces

**Statuts.**
- Les faits tirés de la pièce Kirchner sont **RAPPORTÉS**.
- Pour la pièce « nos résultats », je garde le statut **RAPPORTÉ** que j'ai employé au tour III.1. A, C et D emploient **OBSERVÉ-NON-AUDITÉ** pour la même pièce. Je ne change pas le statut et je ne tranche pas : la divergence est signalée à l'arbitre.
- E qualifie ses dérivations de « VÉRIFIÉ — calcul analytique ». Je ne reprends pas ce statut. Les identités que je réutilise ci-dessous, je les ai relues à la main et je les marque « calcul ».
- Mes inférences sont des **HYPOTHÈSES**. Tout seuil ou effectif que je fixe est **illustratif**.

**Pièces.**
- Ma conception III.1 et les quatre critiques croisées (A, C, D, E) sont présentes.
- Annexes F et G et figure 32 de 2608.28945 : absentes.
- Annexe E.1 : coupée au milieu d'une phrase.
- Annexe A.4 : contenu absent.
- `moisson-candidats-v1.md` : non servie.

**Cadre de décision (j'utilise ici, en le disant, le préambule B4 de E).**
- Chaque duel devient exhaustif : H_A : θ ≤ δ contre H_B : θ > δ.
- Un intervalle entièrement d'un côté de δ réfute l'autre hypothèse.
- Un intervalle qui chevauche δ donne « non concluant ». On augmente alors n jusqu'à un maximum fixé d'avance, puis on s'arrête.
- Une absence de significativité ne réfute rien.

---

## (a) Réponse à chaque critique visant B

| # | Critique (source) | Verdict | Raison ou transformation |
|---|---|---|---|
| 1 | Fiche 1 : r dépend des taux marginaux de ratage. Un moniteur faible tire r vers 1 (A ; C a1 ; D a1 ; E a, b). | **Acceptée** | Calcul relu : r_ij = 1 + Cov(X_i, X_j)/(p_i·p_j), donc la différence de deux r n'isole pas un effet de famille. Remplacée par un log-rapport de cotes à marges égalisées, plus une dépendance résiduelle mesurée sous un modèle de difficulté (b, fiche 1). |
| 2 | Égaliser les marges suffit (C c1). | **Acceptée comme nécessaire, rejetée comme suffisante** | C montre lui-même (b2), comme D (b), que la forme des fonctions de réponse aux items crée de la covariance même à marges égales. J'ajoute un modèle de difficulté fixé d'avance et une analyse de sensibilité. Je ne conclus que si les deux statistiques concordent. |
| 3 | Famille, rôle et modalité d'entrée sont confondus. Si une triche est invisible dans le code, M_code la rate toujours et r = 1 (C a2 ; D a2 ; E c). | **Acceptée** | Calcul relu : conditionner sur un événement certain donne r = 1. L'estimand principal devient la dépendance **à entrée identique**. La dépendance entre étages réels devient secondaire, restreinte aux classes dont l'élément probant est mécaniquement présent dans les deux modalités. |
| 4 | Fuite de la famille génératrice : l'équipe rouge peut écrire avec un modèle d'une des familles surveillantes (A). | **Acceptée** | Les items sont écrits par des humains ou par une famille exclue du panel de moniteurs. La variante d'auto-indulgence passe en plan croisé famille génératrice × famille moniteur. |
| 5 | Contrôle positif vide : deux appels identiques donnent r = 1/P(rate) à température nulle (A ; E). | **Acceptée** | Calcul relu : c'est la borne supérieure, pas un test. Remplacé par un **angle mort partagé construit** : sur un sous-ensemble tiré au hasard, l'élément probant est retiré de l'entrée des deux moniteurs. La dépendance est alors connue et doit être détectée. |
| 6 | La permutation intra-classe ne crée pas l'indépendance : elle conserve la composante entre classes (A c ; D c ; E a, b). | **Acceptée** | Ma règle du tour III.1, « r > 1 sous permutation intra-classe, on arrête », était fausse : elle aurait arrêté l'expérience sous la nulle. Elle devient deux contrôles distincts (b, fiche 1). |
| 7 | Le bootstrap sur items surestime la précision s'il y a des gabarits, des jumeaux ou des tâches communs (D b). | **Acceptée** | Bootstrap par grappes (gabarit × tâche). |
| 8 | Fiche 2 vraie par construction si le score des tricheries est assigné ou si l'intensité règle à la fois gain et visibilité (préambule et a de A). | **Acceptée** | Point le plus coûteux pour B. Le score de chaque méthode plantée est désormais **obtenu par exécution réelle** sur le banc. La grille d'intensités est fixée avant toute lecture des moniteurs. La covariance est rapportée **à intensité et classe fixées**. |
| 9 | Une covariance négative n'impose pas le signe de Δ(k) (D a3 ; E a, b). | **Acceptée** | J'avais écrit que « l'enrichissement Δ en découle mécaniquement ». C'est faux si d(u) = P(détection \| violation, score u) n'est pas monotone. Δ devient l'estimand principal ; la covariance devient descriptive. |
| 10 | Pseudo-réplication : mille classements rejoués ne sont pas mille observations (A ; D b ; E b). | **Acceptée** | L'unité est l'item planté distinct. Le rejeu est abandonné comme source d'intervalles. |
| 11 | P(détection) est estimée sur un seul verdict binaire (A). | **Acceptée** | Cinq appels par item à température fixée non nulle (illustratif), ou score de suspicion continu. |
| 12 | Absence d'un contrôle de covariance score–suspicion **chez les honnêtes** (A c). | **Acceptée, rendue fatale** | Si cette covariance est non nulle, le moniteur lit le score et non la triche : la fiche 2 n'est pas interprétable. |
| 13 | Le bras naturel n'audite que les non signalées : vérification dépendante du verdict, qui confond prévalence, gain et détectabilité (D a4 ; E c). | **Acceptée** | Audit aléatoire des signalées **et** des non signalées, à probabilités d'inclusion connues, pondéré par l'inverse de ces probabilités. L'auditeur est d'abord validé sur vérité plantée et travaille à l'aveugle du rang et du verdict. |
| 14 | Le ratio T de la fiche 3 a des queues lourdes ; l'intervalle de Fieller peut être non borné (A ; C b1 ; D a5 ; E b). | **Acceptée** | T n'est plus qu'une description, avec son intervalle de Fieller. La décision porte sur une différence, sous condition d'un gain frais minimal fixé d'avance. |
| 15 | d′ suppose normalité et homoscédasticité, et diverge aux bords (C a3, b3 ; D). | **Substance acceptée, intitulé rejeté** | C intitule ce point « fuite… par sélection du seuil » mais ne montre aucune fuite. Sur le fond : d′ est remplacé par le taux de détection à 5 % de fausses alertes, seuil calibré par moniteur sur une partition honnête séparée, avec la courbe ROC complète en annexe. Cette échelle de probabilité rend aussi M_s et M_h comparables (objection de D). |
| 16 | T confond changement de classe et changement de moniteur (E a). | **Acceptée** | Plan 2 × 2 : classe (interne ou externe) × moniteur (de sélection ou d'audit). |
| 17 | Une variante tirée au hasard n'est pas un témoin nul : elle peut avoir un vrai gain (D c ; E a). | **Acceptée** | Elle devient l'estimation du gain moyen de la famille de variantes. Le témoin nul est une sélection répétée sur étiquettes permutées. |
| 18 | Les 16 variantes ont pu être écrites en connaissant C4 et C5 (A). | **Acceptée** | Variantes figées et empreintées **avant** que C4 et C5 soient construites par une équipe séparée. |
| 19 | Pas d'anti-sélection pour établir le signe de la sélection (A c). | **Acceptée** | Une variante choisie pour minimiser le taux de détection sur le banc. |
| 20 | Si v* viole moins, les épisodes à violation se raréfient (C c3). | **Acceptée** | Condition de jugeabilité : au moins N_min épisodes à violation par cellule (illustratif : 60). |
| 21 | Fiche 4 : avec des scripts non adaptatifs, la cellule R1 est vraie pour H_A par construction ; la borne 1 − (1 − α)ⁿ supposerait n tentatives adaptatives (A a, b). | **Transformée ; raisonnement partiellement rejeté** | Calcul : 1 − 0,95¹⁶ = 0,560, compatible avec α = 0,05 (α n'est pas donné dans la pièce). Cette borne est la **multiplicité** de n essais indépendants, pas un effet de l'adaptation. Le vrai défaut est ailleurs : mon estimand ne disait pas s'il comptait par soumission (≈ α sans adaptation, comme le dit A) ou par course avec arrêt à la première promotion (≈ 0,56 sous indépendance, même sans adaptation). L'effet de réutilisation est l'**excès** de l'adaptatif sur le non-adaptatif à n égal : c'est une interaction (b, fiche 4). |
| 22 | R1 et R2 changent à la fois la règle, le budget et l'information (D a6 ; E a). | **Acceptée** | Même statistique et même procédure de promotion, mêmes candidats préengagés, même budget. Seul change le renouvellement des observations (banc réservé fixe ou tirages frais). |
| 23 | Duel secondaire W2 (H_A′/H_B′) : vrai par construction (C a4) ; des tirages frais n'élargissent pas la nulle (D a6). | **Conclusion acceptée, raison de C rejetée** | Je retire le duel : il ne sépare pas réutilisation et couverture. Mais E a raison contre la formulation de C : hors nulle signifie **absence de garantie**, pas promotion certaine. H_B′ n'était donc pas vrai « par construction mathématique », seulement peu informatif. |
| 24 | « Rappel attendu nul hors nulle par construction » (ma ligne 9 de la partie c) (E a). | **Acceptée** | Corrigé en : « hors nulle, aucune garantie ; observé 12 sur 12 en W2 (RAPPORTÉ, nos résultats §3) ». |
| 25 | Exiger qu'un moniteur de langage batte seul la vérification mécanique manque sa valeur de complément (E a). | **Acceptée** | Le critère devient l'apport conditionnel P(B = 0, M = 1 \| Y = 1), à son coût P(B = 0, M = 1 \| Y = 0), où B est la vérification mécanique et M le moniteur (formule écrite par E dans sa section sur D ; je m'en sers en le disant). |
| 26 | 1 − (1 − α)ⁿ n'est pas universel ; des données fraîches ne suffisent pas à la validité séquentielle (D b ; E b). | **Acceptée** | La validité du juge sur tirages frais (inégalité de Ville, procédure multiple) reste RAPPORTÉE par le README et n'est pas auditée par moi. La fiche 4 corrigée la teste en partie, empiriquement, sur les classes couvertes. |

---

## (b) Expériences corrigées

### Fiche 1 : dépendance des ratages entre moniteurs de même famille

**Banque d'items.**
- Tricheries plantées par classe, sans mode d'emploi : les trois classes du §7 et les deux classes du faible-vers-fort, toutes RAPPORTÉES.
- Chaque tricherie a un jumeau honnête produit **par la même procédure d'insertion**, à l'élément fautif près. J'emprunte ce point à la critique de D par A, en le disant.
- Items écrits par des humains ou par une famille hors panel (critique 4).
- Partitions : calibration, ajustement du modèle de difficulté, test. Elles sont disjointes par gabarit.

**Moniteurs.**
- Trois familles (Qwen2.5-72B-Instruct, GLM-4-32B, Llama-3.1-8B-Instruct).
- Chaque famille est instanciée deux fois, dans le **même rôle et sur la même entrée**, avec deux invites distinctes.
- Le seuil de chaque instance est fixé sur la partition de calibration à un taux de ratage commun m₀ = 0,4 (illustratif, dans la fenêtre [0,2 ; 0,6] que A donne pour la jugeabilité). Le taux de fausses alertes est rapporté à part.

**Estimand principal.** θ₁ = ψ(même famille) − ψ(familles différentes), où ψ est le log-rapport de cotes de co-ratage sur la partition de test, à entrée identique.

**Sensibilité.**
- Corrélation résiduelle des ratages sous un modèle de réponse à l'item à deux paramètres, ajusté sur la partition dédiée et fixé d'avance. Statistique de dépendance locale de type Q3 : référence à vérifier.
- Je ne conclus que si ψ et la statistique résiduelle concordent. Sinon : non concluant (critique 2).

**Duel.**
- H_A : θ₁ ≤ δ₁ ; H_B : θ₁ > δ₁, avec δ₁ = 0,5 en log-cote (illustratif).
- Intervalles par bootstrap en grappes (critique 7).

**Jugeabilité.** Taux de ratage de test dans [0,2 ; 0,6] et au moins 40 items par classe (illustratif). Sinon la classe est déclarée non jugeable, pas « sans effet ».

**Contrôles.**
- *Négatif 1* : permutation des verdicts sur tout le pool. On attend θ₁ ≈ 0 ; sinon l'estimateur est biaisé.
- *Négatif 2* : permutation des étiquettes de famille à marges fixées (D). On attend θ₁ ≈ 0.
- *Validation du modèle* : permutation intra-classe. On attend la valeur prédite par le modèle de difficulté, pas 1 (critique 6).
- *Positif* : angle mort partagé construit (critique 5). Il doit donner θ₁ > δ₁ avec un intervalle qui exclut δ₁. Sinon la métrique n'a pas de dents et l'expérience s'arrête.

**Estimand secondaire (pertinence pour le pipeline de Kirchner).** Même mesure entre M_code et M_traj d'une même famille, restreinte aux classes visibles dans les deux modalités (critique 3).

**Variante d'auto-indulgence.** Plan croisé famille génératrice × famille moniteur. On compare le taux de détection à 5 % de fausses alertes.

**Ce qui me ferait changer d'avis.** Si l'intervalle de θ₁ est entièrement sous δ₁, avec le contrôle positif réussi, alors empiler deux étages du même modèle ne coûte pas plus qu'empiler deux familles, pour ces classes. L'argument « même modèle » tombe.

### Fiche 2 : le haut du classement concentre-t-il les violations non détectées ?

**Pool.**
- Méthodes honnêtes issues d'une grille, plus des méthodes plantées.
- **Toutes exécutées réellement** sur une tâche faible-vers-fort à cible de moins de 8 milliards de paramètres, environ 30 minutes de carte par méthode (D.3, RAPPORTÉ).
- Intensités fixées d'avance, sans lecture des moniteurs (critique 8).

**Estimand principal.**
- Δ_c(q) = r_c(violations au-dessus du quantile q du score) − r_c(toutes les violations), par classe c.
- Agrégation à poids de classe fixés d'avance.
- Décomposition entre composition et effet intra-classe rapportée. Je reprends ce point de la critique de D par C, en le disant.
- q = 0,9 et q = 0,99 (illustratif), plutôt qu'un top-3 dont le dénominateur serait vide.

**Unités et variance.** L'unité est l'item distinct ; bootstrap en grappes par méthode hôte (critique 10). La détection est estimée par cinq appels par item ou par score continu (critique 11).

**Duel.** H_A : Δ ≥ −δ₂ ; H_B : Δ < −δ₂, avec δ₂ = 0,10 (illustratif).

**Jugeabilité.** Au moins 50 violations au-dessus de q par strate agrégée (illustratif). Sinon : non jugeable, jamais « rappel nul ».

**Contrôles.**
- *Fatal* : covariance score–suspicion chez les honnêtes (critique 12).
- *Négatif* : score permuté au sein des pools et des classes. On attend Δ ≈ 0.
- *Placebos* : violations sans effet sur le score, conservées en complément. E rappelle, dans sa critique de A, que leur détectabilité peut rester liée au score de la méthode hôte : elles ne suffisent donc pas seules.
- *Positif* : anticorrélation construite. On attend Δ < −δ₂.

**Étage 2, chez Kirchner.**
- Audit aléatoire stratifié par rang des méthodes signalées et non signalées, à probabilités d'inclusion connues, pondéré par l'inverse de ces probabilités (critique 13).
- Auditeur validé d'abord sur vérité plantée.

**Ce qui me ferait changer d'avis.** Si, dans le bras naturel pondéré, l'intervalle de Δ est entièrement au-dessus de −δ₂, la lecture rassurante de « Only one reached the top three » est soutenue pour Opus 4.8.

### Fiche 3 : un gain de surveillabilité obtenu par sélection transfère-t-il ?

**Matériel.**
- 16 variantes honnêtes (illustratif), figées et empreintées avant la construction de C4 et C5 (critique 18). Aucune n'est entraînée contre un moniteur.
- Agent : Llama-3.1-8B-Instruct, avec vérité de terrain mécanique.

**Mesure.**
- Taux de détection à 5 % de fausses alertes, seuil calibré par moniteur sur une partition honnête séparée.
- Gains G(classe, moniteur) = TPR(v*) − TPR(base), mesurés sur **épisodes frais**, dans les 4 cellules (classes C1–C3 ou C4–C5) × (moniteur M_s ou M_h) (critique 16).

**Condition préalable.** La borne inférieure de G(interne, M_s) dépasse g_min = 0,10 (illustratif). Sinon on rapporte « pas de gain à transférer » et on s'arrête (critique 14).

**Duel.** Sur G(externe, M_h) : H_A : G > δ₃ (transfert) ; H_B : G ≤ δ₃ ; δ₃ = 0,05 (illustratif).

**Localisation d'un échec.**
- G(interne, M_h) élevé et G(externe, M_h) faible : l'échec tient à la classe.
- G(externe, M_s) élevé et G(externe, M_h) faible : l'échec tient au moniteur.
- T n'est rapporté qu'en description, avec son intervalle de Fieller.

**Contrôles.**
- Sélection sur étiquettes permutées, répétée 20 fois (illustratif). Elle donne la loi de la malédiction du gagnant sous la nulle.
- Anti-sélection (critique 19).
- Variante aléatoire, qui estime le gain moyen de la famille de variantes (critique 17).

**Jugeabilité et rapport.**
- Au moins 60 épisodes à violation par cellule (critique 20).
- Le taux de violation et les fausses alertes sur les honnêtes sont rapportés à part.

### Fiche 4 : réutilisation du banc réservé, séparée de la multiplicité

**Estimand.** Probabilité de fausse promotion **par course**, avec arrêt à la première promotion et n fixé (n = 16, illustratif), sur les classes couvertes par la nulle v8.

**Plan factoriel.**
- *Observations* : banc réservé fixe, ou tirages frais. Même statistique, même procédure, même budget (critique 22).
- *Proposeur* : non adaptatif à candidats préengagés, ou adaptatif. Le proposeur adaptatif choisit sa soumission suivante en fonction des verdicts passés ; je le décris par son rôle seulement. Il est d'abord scripté, puis c'est un agent de langage comme en A1.

**Effet de réutilisation.** θ₄ = [P(adaptatif, fixe) − P(non adaptatif, fixe)] − [P(adaptatif, frais) − P(non adaptatif, frais)].

**Duel.** H_A : θ₄ ≤ δ₄ ; H_B : θ₄ > δ₄ ; δ₄ = 0,05 (illustratif). 1 000 courses par cellule pour les scripts (illustratif).

**Contrôles.**
- Monde sans signal dans les quatre cellules.
- Témoin non adaptatif à budget et information égaux : c'est la cellule « non adaptatif » elle-même (D).
- La ligne de base de multiplicité est **mesurée**, pas posée à 0,560. Sur un banc fixe, les essais ne sont pas indépendants (critique 26).

**Duel W2 : retiré** (critique 23).

**Ce qui me ferait changer d'avis.** Si l'intervalle de θ₄ est entièrement sous δ₄, le risque d'une boucle à la Kirchner tient à la couverture et non à la réutilisation. Je cesse alors de recommander des tirages frais et je recommande une équipe rouge des classes.

### Corrections à la table des instruments (partie c du tour III.1)

- Ligne 9 corrigée comme indiqué (critique 24).
- Partout, « battre la vérification mécanique » devient « apport conditionnel à la vérification mécanique, à coût en fausses alertes rapporté » (critique 25).

---

## (c) Réponse à la question de l'arbitre

**Problème sous-estimé.** Le chiffre de triche du harnais de Kirchner est un comptage **de ce qu'un moniteur du même modèle signale**. On ne sait ni combien il rate, ni si ses ratages coïncident avec ceux de l'étage qui filtre, ni s'ils se concentrent là où le classement choisit.

**Ce qui est établi (tout est RAPPORTÉ, rien n'est VÉRIFIÉ).**
- 39 méthodes sur 1 601 sont signalées, soit 2,4 % (§7).
- Le moniteur avant exécution et la relecture finale sont Opus 4.8, comme les agents (§3.2, §7).
- « Only one reached the top three » porte sur les méthodes **signalées** (§7, fig. 32a).
- Le texte lu ne contient ni rappel ni taux de faux négatifs. L'annexe G n'est pas lue, donc cette absence n'est pas établie.
- Anthropic se dit « cautiously optimistic » ; ses propres auteurs écrivent « our AARs are not strongly trying to evade detection » (§8.2).
- L'échafaudage de Kale et coll. rapporte que savoir qu'on est surveillé dégrade le moniteur.
- Au-delà de la médiane, le classement ne prédit plus Petri (D.3).
- Chez nous : un trou de couverture a fait promouvoir une fausse loi 12 fois sur 12 en W2 ; nos juges de modèles de langage ont κ = 0 au plafond.

**Ce qui ne l'est pas (HYPOTHÈSES).**
- Que les 1 601 méthodes aient toutes passé l'avant-exécution.
- Que deux étages du même modèle ratent les mêmes cas au-delà de la difficulté commune.
- Que le haut du classement soit enrichi en violations non détectées.
- Qu'un gain sur banc de surveillabilité transfère hors banc.
- Que le rappel sur tricheries plantées renseigne sur la triche naturelle : 2604.23488 rapporte le contraire pour la triche née de l'entraînement (référence à vérifier pour auteurs et titre).

**L'expérience à faire en premier : la fiche 1 corrigée.** Trois raisons :
- elle est décisive sans agent ni accès au harnais : inférence seule sur trois familles ouvertes, de l'ordre de quelques dizaines d'heures-H100 (illustratif) ;
- sa banque d'items est le goulot commun des fiches 2 et 3 : tricheries plantées, jumeaux honnêtes de même procédure, verdict mécanique, auteurs hors panel ;
- les critiques ont rendu sa mesure plus propre (marges égalisées, entrée identique, contrôle positif construit), sans la vider de son objet.

**Résultat chiffré qui ferait changer d'avis.** Avec des taux de ratage de test dans [0,2 ; 0,6], au moins 40 items par classe et le contrôle positif réussi : si l'intervalle de θ₁ est entièrement sous 0,5 en log-cote (seuil illustratif), et que la statistique résiduelle concorde, alors je cesse de soutenir que le partage de modèle affaiblit la défense en profondeur du pipeline. Je ne recommande plus d'étage d'une autre famille.

**Inversement.** Un intervalle entièrement au-dessus de 0,5 ferait de « même modèle » une limite mesurée de « Better control scaffolding ». Les fiches 2 et 3 devraient alors employer un moniteur d'audit d'une autre famille.

**Ce que la fiche 1 ne réfute pas.** Elle ne vaut que pour la triche plantée. Seul le bras naturel de Kirchner, audité au hasard sur signalées et non signalées, peut transporter la conclusion à Opus 4.8.

FIN-DE-CELLULE