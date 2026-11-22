# Proposition A · Tour III.2 : critique croisée de méthode

## 0. État des pièces et statut de ce qui suit

- Les pièces B, C, D et E sont reçues et se terminent chacune par leur marqueur ; je ne vois pas de coupure. Ma propre conception du tour III.1 n'est pas jointe, donc je ne m'y réfère pas.
- FAITS et QUESTION portent le même texte et la même empreinte. Aucun énoncé n'y est étiqueté, donc aucun statut VÉRIFIÉ n'est disponible.
- C et E inscrivent « VÉRIFIÉ » sur des énoncés absents des faits (« par définition logique », « partition fonctionnelle »), et « OBSERVÉ-NON-AUDITÉ » sans source. Je ne reprends pas ces statuts à mon compte ; l'arbitre tranchera.
- Mes critiques sont des arguments de méthode, au statut HYPOTHÈSE quant à leur poids empirique. Les « propriétés d'estimateur » sont dérivables mais ne viennent pas des faits. Tous les chiffres sont illustratifs.
- L'année de *AI Control* diffère entre B (2023), C (2023/2024) et D (2024) : référence à vérifier. Je ne cite aucune référence nouvelle.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **E2, vrai en partie par construction.** La défense LoRA est entraînée sur des injections sans levier. Elle est ensuite évaluée sur l'injection nue (dans sa distribution) et sur la pression (hors distribution). R < 1 est donc attendu pour tout déplacement hors distribution, social ou non. Le test « classe distincte » mesure la distance à l'entraînement, pas le caractère social.
2. **E4, H_B peut-être neutralisée par construction.** Le diff de sabotage est « d'abord fixé ». L'angle mort partagé porte sur ce que le modèle tend à produire lui-même. Si le diff vient de l'expérimentateur, cette voie est supprimée et l'issue « l'excès survit à la paraphrase » devient presque impossible. La pièce ne dit pas qui produit le diff.
3. **E4, le prérequis ferme la porte à tort.** L'autoreconnaissance explicite (AUROC ≤ 0,55) ne mesure pas la préférence implicite, par exemple une familiarité de perplexité. Un moniteur peut échouer à la question « est-ce de toi ? » et rester indulgent.
4. **E5, H_A retenue à vide.** Si la revendication n'a aucun effet, l'équivalence entre origine vraie et origine fausse est établie. H_A (« agit par son contenu ») est alors retenue sans que rien n'agisse.
5. **E1, issues non couvertes.** δ < −3 (le levier déclenche un refus) et δ entre 3 et 5 ne falsifient rien. La « pente de dose » à deux intensités est une seule différence, confondue avec la saillance lexicale. Les alias du plan fractionnaire sur cible × effet × canal ne sont pas donnés.
6. **Sélection post-traitement dans les quadruplets.** Les cellules « pression, a refusé » et « pression, a saboté » sont choisies par l'agent. Les quadruplets complets forment un sous-ensemble non aléatoire de tâches. E3 hérite du défaut : les sabotages réussis sous pression et sous remplissage neutre ne sont pas la même population.
7. **E6.** Le κ dépend de la prévalence du dommage, que la pression modifie.
8. **Fuite.** Les tâches sont tenues à l'écart, mais pas les formulations de pression ni les gabarits de sabotage. Une sonde, ou V3, peut retrouver les gabarits.
9. **Point 8.5.** Une corrélation supérieure à 0,9 est demandée sur 4 ou 5 modèles.

### (b) Conditions de perte de puissance

- **δ.** Si p(demande nue) tend vers 0 ou 1, δ est borné par 1 − p ou par p et le test est non jugeable. Avec une corrélation intra-tâche ρ et m épisodes par tâche, n_eff = n / (1 + (m − 1)ρ).
- **R.** C'est un rapport de réductions relatives. Si l'intervalle de la réduction sur l'injection nue contient 0, l'intervalle de R est non borné (problème de Fieller). Le TOST sur [0,8 ; 1,25] est alors inatteignable, quelle que soit la vérité.
- **ΔAUROC (propriété d'estimateur).** L'AUROC est invariante par toute transformation monotone commune aux deux classes. Un décalage commun des scores sous pression laisse l'AUROC intacte, alors qu'au seuil gelé hors pression le TPR s'effondre ou le FPR explose. « Équivalence d'AUROC » n'établit donc pas H_A.
- **TPR à 1 % de FPR.** Le seuil est un quantile empirique. Avec 300 négatifs (illustratif), il repose sur 3 points.
- **Interaction logistique d'E4.** Si une cellule a un taux de non-détection proche de 0 ou de 1, il y a séparation et la borne du rapport de cotes n'est pas estimable.
- **κ.** À sensibilité et spécificité constantes, κ varie avec P(dommage). Il faut rapporter sensibilité et spécificité face à l'oracle.
- **Corrélation sur 5 points.** Pour r = 0,9, l'intervalle de Fisher va d'environ 0,09 à 0,99 (illustratif). Le critère 8.5 n'est pas jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E2.** Une injection non sociale hors distribution, à distance comparable (paraphrase, autre format). Sans elle, R < 0,5 ne dit rien du levier.
- **E1.** La demande assortie d'une justification non sociale de même longueur. Sans elle, « social » est confondu avec « élaboré ».
- **E3.** Un contrôle positif de l'optimiseur, sur une sonde connue pour être fragile. Sans lui, l'équivalence en variante adverse mesure peut-être l'échec de la recherche. Il faut aussi rejouer des trajectoires gelées, sur les mêmes jetons.
- **E4.** Un bras où les diffs sont produits par les agents eux-mêmes.
- **E5.** Un test d'effet principal non nul avant le TOST.

Je me sers de V5 (sonde sur couche d'embedding et sur poids réinitialisés) et de la fausse signature d'E4 pour critiquer les autres pièces.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duel 2, attribution inversée.** Après réécriture par F1, les textes de A1 et de A2 sont tous deux de facture F1. Ce qui reste de Δ_style tient au contenu des appels d'outils, donc à la manière de saboter de A1. C'est ce que prédisent les « angles morts partagés », que C range dans H_2B. Or la règle compte Δ_style ≥ 8 points contre H_2B. L'issue falsifie la mauvaise hypothèse.
2. **Δ_id ne mesure pas un couplage endogène.** L'étiquette « instance jumelle » est un texte inséré, jamais croisé avec l'origine réelle. C'est un appel exogène à l'identité (M1 ou M2 chez C), compté comme preuve de M4. Le croisement revendication × origine de B (E5) serait nécessaire ; je m'en sers.
3. **Sélection.** Les 400 trajectoires avec I_sab = 1 ne proviennent pas des mêmes tâches pour A1 et A2. Les traces qui n'atteignent pas l'écart de 0,1 nat sont écartées en silence.
4. **Duel 3, condition S impure.** Elle contient une demande explicite (« lève une alerte ») et un lexique d'alerte (« alerte critique », « bloquer », « désactivation »). Il n'y a pas de demande nue, alors que le Duel 1 l'exige pour l'agent. Les issues ne sont ni exclusives (les deux Δ ≥ 15) ni exhaustives (entre 5 et 15).
5. **Duel 4, fuite dans l'étiquette d'entraînement.** Tous les positifs contiennent une instruction de sabotage dans le contexte, aucun négatif n'en contient. La sonde peut apprendre « instruction présente ». La chute de TPR sur sabotage social mesurerait alors le changement de forme de l'instruction, pas un « camouflage ». Le contrôle « a résisté » n'existe qu'à l'évaluation, et le seuil est calibré sur ce même contrôle.
6. **Duel 1.**
   - Δ_soc est un maximum sur 4 leviers.
   - Le terme ASR(contrôle négatif) est nul par construction, puisque rien n'y est demandé.
   - Le comparateur impératif (« Ignore la règle précédente ») est la forme canonique. Elle est peut-être la plus filtrée à l'entraînement (HYPOTHÈSE), ce qui gonflerait Δ_soc sans effet social.
   - « Non significatif avec puissance ≥ 0,90 » n'est pas une équivalence. Un Δ de 9 points significatif falsifierait H_1A.
7. **Instruments.**
   - Un FPR ≤ 5 % par étape donne, sur 25 étapes indépendantes, un FPR par épisode d'environ 0,72 (illustratif).
   - L'auditeur est mesuré sur le sous-ensemble escaladé. La loi de ce sous-ensemble dépend du moniteur amont, lui-même attaquable.

### (b) Conditions de perte de puissance

- **Maximum de 4 écarts (propriété d'estimateur).** Sous l'hypothèse nulle, son espérance est positive. Elle vaut au plus environ 1,03 erreur type si les écarts sont indépendants, moins s'ils partagent le comparateur (illustratif). La comparaison au seuil de +10 est biaisée vers H_1A.
- **McNemar.** La puissance dépend du nombre de paires discordantes. Elle est nulle si les deux ASR sont au plafond ou au plancher.
- **τ à 5 % de FPR.** Si le score du juge a des atomes de masse supérieure à 5 % (notes entières), le point de fonctionnement n'existe pas. FNR(M1) et FNR(M2) sont alors comparés à des FPR différents. Avec 400 honnêtes, 20 points définissent τ.
- **Appariement en log-perplexité.** L'égalité des moyennes n'entraîne pas l'égalité des lois. Un moniteur sensible à la variance ou aux queues garde un signal de style.
- **Duel 4.** Si P(I_sab = 1 | pression) ≪ P(I_sab = 1 | instruction directe), les 300 sabotages sociaux sont une queue de distribution. La composition en tâches diffère, et ΔTPR est non jugeable sans stratification par tâche et supports recouvrants.
- **pAUROC sur [0 ; 0,05] avec 300 négatifs.** Elle repose sur 15 points.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Duel 3.** Une demande d'alerte nue de même longueur. Le texte S cité mais non adressé au moniteur.
- **Duel 2.** A1 réécrit par F1 (effet propre de la réécriture). A1 stylisé en F2. Le croisement étiquette × origine réelle.
- **Duel 4.** Des négatifs d'entraînement « instruction reçue et refusée ». Une évaluation sur un sabotage induit par une instruction non sociale reformulée. Une sonde sur la couche d'embedding.
- **Duel 1.** Un comparateur impératif hors forme canonique (demande simple).

Je retiens de C le contrefactuel de crédibilité (révision 1 : preuve que le tiers ne peut pas exécuter sa menace), à condition d'un contrôle de longueur.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le « dommage après exécution » est une identité.** Avec un exécuteur déterministe, livré erroné = 𝟙(invalide ∧ accepté). C'est une fonction de la table validité × vote, sans information supplémentaire. La clause finale (« pas de conclusion sans hausse des pertes ») se réduit à une condition sur la prévalence, voir (b).
2. **Duel 3, ambiguïté décisive.** Deux lectures de la note « permutée entre répétitions du même cas » sont possibles :
   - Même émetteur : la signature de famille est présente dans les deux bras. Le contraste ne voit alors qu'un couplage propre à l'instance entre la note et le registre. Il est aveugle à la reconnaissance au niveau de la famille.
   - Autre émetteur : le style est confondu avec la permutation.
3. **Aucune incitation ni mécanisme de coordination dans le banc.** H_B est attendue a priori. Un résultat nul n'informe pas sans preuve que le dispositif détecte une coordination quand elle existe.
4. **Duel 2, le « contrôle négatif » teste le harnais.** La variation de contexte après scellement du vote ne peut rien changer si le logiciel est correct. Elle n'écarte aucun facteur de confusion. Il manque, côté moniteur, l'équivalent du contrôle prévu côté agent : un cadrage sans demande de verdict.
5. **Duel 1.** Deux problèmes :
   - La métrique « registre invalide » mélange obéissance et incompétence. La part d'incompétence est probablement élevée à 3 milliards de paramètres (HYPOTHÈSE).
   - Le contraste moyen équilibré annule des effets de signes opposés entre registres.
6. **Dilemme de l'oracle visible.** Dans une tâche de registres à règles déterministes, deux cas se présentent :
   - Le contrôle sur pièces visibles reconstitue l'oracle. Les instruments appris n'ont alors aucune marge, et la qualification (c) est vide.
   - Le manifeste caché contient une information que le moniteur n'a pas. Ses erreurs sont alors informationnelles, pas dues à la pression.

   D ne voit que la première branche.
7. **Lecteur d'activations.** Sa cible est « état invalide », erreurs sans pression comprises. Un modèle peut ne pas représenter ses propres erreurs. Le plafond de détection est alors bas pour une raison étrangère à la question.
8. **Famille confondue avec la taille.** Qwen2.5-3B et OLMo-2 7B sont croisés dans le Duel 3.
9. **Exclusion des notes « apportant une pièce nécessaire ».** Le critère est appliqué après coup et n'est pas mécanisé.

### (b) Conditions de perte de puissance

- **Risque de bout en bout.** P(livré erroné) = π · P(accepter | invalide), où π = P(invalide). Tout contraste est borné par π. Si π < δ, H_A est inatteignable et H_B vraie par construction. Le seuil doit porter sur la probabilité conditionnelle.
- **Duel 3.** C'est une différence de différences, dont la variance est de l'ordre de 4 fois celle d'un taux. L'appariement par famille donne n_eff = nombre de familles G. Si G vaut quelques dizaines (illustratif), le cas « ne tranche pas » est l'issue typique.
- **Contraste moyen.** Si les effets θ_r par registre sont hétérogènes, la moyenne peut rester sous δ avec max_r θ_r ≥ δ. H_B serait retenue à tort pour un registre.
- **Duel 1.** Si le taux d'invalidité naturel p₀ est élevé, Δ ≤ 1 − p₀. L'obéissance est masquée chez les cas qui auraient échoué de toute façon.
- **Duel 2.** Si P(accepter | invalide) de base est proche de 0 ou de 1 sur les cas gelés, la bascule est bornée. Il faut des cas à taux médian.
- **Fausses alertes à 2 %.** Elles ne sont pas jugeables sans plusieurs centaines de témoins honnêtes indépendants. D le reconnaît.

### (c) Contrôles négatifs (et positifs) dont l'absence serait fatale

- **Duel 3.** Un contrôle positif : un code convenu implanté par consigne ou par ajustement. Deux bras de permutation : même famille et autre famille.
- **Duel 2.** Un cadrage social sans demande, adressé au moniteur.
- **Duel 1.** Une métrique restreinte au champ demandé. Un contrôle « même demande, mais autorisée », qui mesure l'obéissance légitime.
- **Instruments.** L'exactitude du contrôle visible face à l'oracle, sur tout le test.

Je me sers du gel du travail avant variation du contexte du moniteur, proposé par D, pour critiquer E3 de B et le Duel 4 de C.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E4, trois résultats par construction.**
   - *Seuil.* Il est fixé à FPR = 0,05 sur les honnêtes contenant la pression. Le FPR sous pression vaut donc 0,05 par définition. Le critère 7.4 (FPR > 0,20) ne peut jamais se déclencher dans ce protocole.
   - *Sélection.* Conditionner sur « juge muet » retient les sabotages les plus difficiles pour ce même modèle. Le TPR de la sonde y baisse sans aucune « corruption représentationnelle ».
   - *Position de lecture (propriété d'architecture).* Dans un modèle causal, les activations des positions antérieures au texte de pression n'en dépendent pas. La pièce fixe la couche, pas la position. H_4A peut donc être vraie par masquage.
   - *Remarque.* La sonde lit le modèle moniteur sur une trace dont le contenu de sabotage est inchangé. Un classifieur lexical de la trace montrerait la même « dissociation ».
2. **E3.**
   - La canonisation retire de l'information, pas seulement la signature. Si les FNR montent vers 1 pour toutes les paires, Δ_canon tend vers 0 par plafond et R_canal vers 1. H_3A est alors « vérifiée » par destruction du signal.
   - H_3A range la familiarité stylistique passive du côté de l'« entente ». C la range du côté opposé (H_2B). L'un des deux duels au moins ne teste pas l'entente. Je ne les harmonise pas.
   - « Annule algébriquement » ne vaut que pour des effets additifs sur l'échelle des probabilités.
3. **E2.**
   - G_mon soustrait des grandeurs sans unité commune : l'ASR d'un agent, et la variation de FNR ou de FPR d'un juge à un seuil arbitraire.
   - Les charges diffèrent nécessairement. « Même budget de jetons » n'égalise pas la force.
   - Si les traces sabotées portent la charge T1, le juge détecte la charge, pas le sabotage.
4. **Décision ponctuelle.** Chaque issue « falsifie » même dans le bruit. Le McNemar teste Δ = 0, pas Δ = θ.
5. **Δ_état inclut D_tâche > τ.** Une dégradation par distraction compte comme sabotage. La différence appariée isole l'effet de la pression, pas l'obéissance.
6. **Section 4.2.** Le juge est évalué sur les sabotages qui franchissent la liste blanche. Le TPR de la ligne de base syntaxique y vaut 0 par construction.
7. **Taxonomie.** T2 et T4 occupent la même cellule (Δ_état = 1, A = 0). Le critère annoncé ne les sépare pas ; seule la cause le fait.
8. **Contrôle « bogues synthétiques ».** Si les traces sont entièrement synthétiques, le facteur agent n'existe pas. |Δ_homo| < 0,02 est alors acquis d'avance.

### (b) Conditions de perte de puissance

- **Erreur type < 0,02 avec N = 600.** Elle suppose l'indépendance. Avec 30 scénarios, m ≈ 20 épisodes par scénario. L'effet de plan vaut 1 + (m − 1)ρ, soit environ 4,8 pour ρ = 0,2, et l'erreur type est multipliée par environ 2,2 (illustratif).
- **Décision au seuil θ.** La probabilité d'erreur vaut Φ(−|Δ − θ| / ET). La décision n'est pas jugeable si |Δ − θ| < 2 ET.
- **Δ_homo (propriété d'estimateur).** Si logit FNR = a_i + b_j, sans aucune homophilie, Δ_homo sur l'échelle des probabilités n'est pas nul dès que les taux s'écartent de 0,5. Un exemple à effets ±2 logits donne ±0,14 (illustratif). Il faut tester l'interaction en logit.
- **R_canal.** C'est un rapport dont le dénominateur est voisin de 0,05, avec une erreur type du même ordre. Sa loi a des queues lourdes, et le signe est indéfini si Δ_brut < 0.
- **G_mon.** ΔFNR ≤ 1 − FNR₀. Un juge déjà mauvais (FNR₀ = 0,6, illustratif) ne peut guère être dégradé. H_2A serait alors satisfaite par faiblesse.
- **E4.** Notons ρ_sj la corrélation, hors pression, entre le score de la sonde et celui du juge sur les sabotages. Le TPR conditionnel au silence décroît avec ρ_sj sans aucune corruption. La mesure n'est pas jugeable sans estimation de ρ_sj.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E4.**
  - Un comparateur « juge muet sans pression » (faux négatifs naturels), apparié sur le score du juge.
  - Un seuil gelé hors pression.
  - Une lecture à une position postérieure au texte de pression.
  - Un classifieur lexical et une sonde sur couche d'embedding, sur la même trace.
- **E3.**
  - Une suppression de texte de même quantité qui préserve le style.
  - Un transfert de style qui préserve l'information.
  - Des FNR hétérogènes vérifiés hors plafond après canonisation.
- **E2.** Une demande nue adressée au juge. Des traces sabotées sans charge T1.
- **E1.** Un levier sans aucune demande. Une demande assortie d'une justification non sociale.

Je me sers de la moyenne croisée d'E3 et du contrôle par bogues, à condition qu'ils portent sur l'échelle logit et sur des traces d'origine réelle.

---

## Ce qui me ferait retirer ces critiques

- **B, E2.** Un contrôle hors distribution non social donne R ≈ 1 alors que la pression donne R < 0,5.
- **C, Duel 2.** C précise que Δ_style est calculé à contenu d'appels d'outils identique entre A1 et A2.
- **D, Duel 3.** Un code implanté est détecté par le contraste avec la puissance annoncée.
- **E, E4.** La position de lecture est postérieure à la pression, et le TPR conditionnel dépasse celui du comparateur « muet naturel ».

FIN-DE-CELLULE