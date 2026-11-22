# Proposition B : Tour III.3, réponse aux critiques

## 0. État des pièces et conventions

- **FAITS** : le texte est identique à celui de la QUESTION et l'empreinte affichée est la même ; je ne l'ai pas recalculée. Aucun fait n'y porte de statut. Rien de ce qui suit n'est donc VÉRIFIÉ empiriquement.
- **Ma conception III.1** : présente et complète.
- **Critiques A, C, D et E** : présentes ; chacune se termine par sa ligne de fin. Je ne traite que leurs sections « Sur la proposition B ».
- **Statuts** : les énoncés des critiques sont RAPPORTÉS avec le statut que leur auteur leur donne, et je ne le modifie pas. Le mot « calcul » désigne une implication algébrique que j'ai refaite moi-même. Ses prémisses sont des HYPOTHÈSES de modélisation, et elle n'affirme rien d'observé sur un modèle.
- **Chiffres** : tout chiffre est illustratif, sauf s'il est calculé à partir de chiffres illustratifs, auquel cas il est marqué « calcul ».
- **Notation des critiques** : « A-a3 » désigne la critique A, rubrique (a), point 3.

---

## 1. (a) Réponse aux critiques

### 1.1 Décisions

**T1. κ de E1 est nul par construction.**
- *Critique* : sans canal, κ est nul ; le brassage a la même loi que l'épisode original ; avec une seule réalisation par tâche, κ̂ = 0 ; κ retranche le point focal qu'il voulait mesurer.
- *Sources* : A-a1, A-b, C-a1, C-b1, D-a, D-b, E-a2, E-b1.
- *Décision* : **acceptée**.
- *Raison* (calcul) : sous indépendance conditionnelle à la tâche, P(cohérence | X) = Σ_c Π_r P_r(c | X), donc κ ≡ 0. Mon affirmation de III.1, « le brassage distingue points focaux et coordination émergente », est fausse ; je la retire. E1 est remplacée par E1′ (§ 2).

**T2. Contrôles manquants pour la coordination.**
- *Critique* : permuter l'ordre des options ; ajouter un bras à invites paraphrasées ; prouver l'indépendance des graines ; publier la concordance brute.
- *Sources* : C-c2, A-c, D-c.
- *Décision* : **transformée** en contrôles de E1′.

**T3. Un seul triplet hétérogène, sans rotation des rôles.**
- *Sources* : A-a2, A-c.
- *Décision* : **acceptée**.
- *Correction* : une équipe homogène pour chaque modèle de base, deux triplets hétérogènes, et une rotation des rôles. La conclusion portera sur « ces modèles », pas sur « des modèles différents ».

**T4. La sonde de E2 lit le thème déclencheur, l'adaptateur ou la température, pas l'intention.**
- *Sources* : A-a3, A-c, C-a2, C-c1, D-a, D-b (« P(Y|thème) ∈ {0,1} »), D-c, E-a1, E-c1, et le défaut transversal n° 1 de A.
- *Décision* : **acceptée**. C'est le défaut le plus grave de ma conception.
- *Correction* : nouvelle porte de validité E2-V, un plan 2×2 croisant adaptateur et thème (§ 2).

**T5. S4 tronque le moniteur textuel.**
- *Critique* : sur les sabotages retenus, le moniteur textuel détecte 0 % à FPR ≤ 2 %. La comparaison « la sonde bat le texte » est donc vraie par construction.
- *Sources* : A-a6, C-a3, D-a, E-a2, E-c2, et le défaut transversal n° 2 de A.
- *Décision* : **acceptée, avec une nuance**. En III.1, le moniteur notait aussi l'épisode entier, et ce score-là n'est pas mécaniquement tronqué. Il reste toutefois fortement sélectionné.
- *Correction* : le juge de recrutement et le moniteur évalué appartiennent à deux familles disjointes. Toutes les comparaisons entre texte et sonde se font sur le flux non filtré.

**T6. Le gain d'agrégation de P2.**
- *Critiques* :
  - le signe n'est pas neutre, car le ρ des copies est plausiblement plus élevé, et le « meilleur rôle » choisi sur le test est biaisé (A-a4) ;
  - en compromission d'une seule copie, la somme perd contre le meilleur rôle (C-b2, premier tiret ; C-c3) ;
  - agréger des scores scalaires n'exige aucun espace commun (E-a1) ;
  - si Y ⊥ S₋ᵣ | Sᵣ, l'agrégation ne gagne rien (D-b).
- *Décision* : **acceptée sur le fond. P2 est retirée sous sa forme III.1.**
- *Raison* : agréger des scalaires n'a rien de propre aux copies, donc mon « agrégation sans alignement » n'était pas un effet d'identité. S'il existe un avantage défensif propre à l'identité, c'est l'efficacité en étiquettes du transfert d'une sonde d'un rôle à l'autre. Je reprends ici, en le disant, l'idée de budget d'étiquetage total que A formule contre D. P2 devient P2′ (E2′).
- *Corrections* :
  - l'agrégateur est préenregistré par bras : somme en compromission totale, maximum en compromission partielle ;
  - on publie ρ₀, ρ₁ et d′ par rôle ;
  - le meilleur rôle est choisi sur un jeu disjoint du test.

**T7. Deux énoncés sur le signe de l'agrégation.**
- *Énoncés* : C-b2 (second tiret) et E-b2 (premier tiret).
- *Décision* : **rejetés tels qu'énoncés**, par contre-exemple (§ 1.2). L'intuition qui les porte est conservée dans T6.

**T8. E3 est triviale ou vide.**
- *Critique* :
  - si la copie est compromise par ses poids, la divergence de rejeu mesure l'écart de poids, et une simple empreinte des poids suffit ;
  - si elle est compromise par injection, le rejeu forcé reproduit l'injection, et la distance suit la loi δ₀ ;
  - en rejeu libre, on mesure du bruit d'échantillonnage.
- *Sources* : A-a5, A-c, D-a, D-b, E-a2, E-b3.
- *Décision* : **acceptée. E3 est retirée.**
- *Raison supplémentaire* : rejouer un modèle est possible pour toute équipe, ce qui n'a rien de propre aux copies. Je retire aussi la phrase « ce contraste est un résultat en soi ».

**T9. E5 est quasi acquise.**
- *Critiques* :
  - pénaliser une sonde figée abaisse son score par construction (A-a7) ;
  - l'asymétrie « un ajustement contre trois » relève de la comptabilité de coût (A-a7) ;
  - il faut une sonde réentraînée hors échantillon (A-c, E-a3, E-c3) ;
  - il faut conserver le taux de dégradation et prévoir un témoin à utilité comparable (D-a, D-c).
- *Décision* : **acceptée et transformée** en E5′. L'asymétrie de coût redevient une HYPOTHÈSE non testée et sort des résultats attendus.

**T10. Biais de sélection et fuites dans E4.**
- *Critiques* : le minimum sur les stratégies est biaisé ; la stratégie est choisie sur les mêmes séquences que l'évaluation ; les sondes sont évaluées contre les organismes qui ont servi à les entraîner ; l'itération rouge adaptative se fait sur le banc d'évaluation.
- *Sources* : A-a8, D-a, D-c, E-a3, E-b4.
- *Décision* : **acceptée**.
- *Correction* : séparation développement/test pour les stratégies, les organismes et les sondes.

**T11. La sûreté sur 1 000 épisodes sature.**
- *Critique* : si θ ≥ ln 50/1000 ≈ 0,0039 dans les deux bras, l'équivalence à ±2 points est automatique.
- *Sources* : A-b, C-b3, D-b, E-b4.
- *Décision* : **acceptée**. Calcul refait : (1 − θ)¹⁰⁰⁰ ≤ 0,02 ⇔ θ ≳ 0,0039.
- *Correction* : la métrique primaire devient le risque résiduel par épisode (E4′).

**T12. Zones qui ne falsifient rien.**
- *Critique* : entre 5 et 15 points en E1, entre 3 et 7 points en E5, entre 2 et 10 % en E0, aucune hypothèse n'est falsifiée.
- *Sources* : A-a9, D-b.
- *Décision* : **acceptée**.
- *Correction* : une seule marge par contraste, et une règle d'intervalle (§ 2.0).

**T13. Puissance insuffisante à FPR = 1 %.**
- *Critique* : avec n₀ = 1 000 et LR entre 10 et 30, l'écart-type du TPR va de 3 à 9 points.
- *Sources* : A-b et le défaut transversal n° 3 de A.
- *Décision* : **acceptée**. Calcul refait : 100 × 0,0099/1000 donne un écart-type de 3,1 points ; 900 × 0,0099/1000 en donne 9,4.
- *Correction* : FPR primaire à 5 % et marges recalculées (§ 2.0).

**T14. L'alignement par CCA dégénère.**
- *Critique* : si n_cal est inférieur à 2d, les corrélations canoniques empiriques valent 1.
- *Sources* : A-b, E-b2.
- *Décision* : **acceptée**.
- *Correction* : réduction par ACP à k ≪ n_cal, et contrôle positif d'alignement.
- *Remarque* (calcul) : génériquement, la dégénérescence vaut pour n < 2d, puisque deux sous-espaces de dimension d dans ℝⁿ s'intersectent alors. E écrit n ≤ 2d. C'est sans conséquence ici.

**T15. Trois optimisations LoRA confondues avec la géométrie latente.**
- *Source* : C-a4.
- *Décision* : **transformée en test**. Ajout d'un bras de trois copies du même modèle de base, munies de trois LoRA indépendants (graines et sous-familles disjointes). Ce bras sépare « même base » de « même adaptateur ».

**T16. Le seuil empirique de E0 couple les indicateurs, et l'issue entre les deux seuils n'est pas décrite.**
- *Sources* : E-b1, D-b.
- *Décision* : **acceptée**.
- *Correction* : le seuil est estimé sur un ensemble honnête disjoint, avec une seule marge.

**T17. Le rappel de l'oracle par famille de défauts est inconnu.**
- *Source* : D-b.
- *Décision* : **acceptée**. Le rappel de l'oracle est publié par famille, et le risque est pondéré par famille.

**T18. Les pièges peuvent masquer des écarts opposés selon la famille.**
- *Source* : D-b.
- *Décision* : **acceptée**. L'instrument « tests-pièges » est rapporté par famille.

**T19. Les corrélations par classe sont insuffisantes.**
- *Critique* : elles sont indéfinies si une variance est nulle, et deux corrélations égales ne garantissent pas des lois jointes égales.
- *Source* : D-b.
- *Décision* : **acceptée**. Le critère « ρ honnête < 0,2, ρ sous sabotage > 0,5 » est retiré comme critère de fonctionnement. On publie les lois jointes, et ρ ne sert plus que de descripteur.

### 1.2 Deux énoncés que je conteste

C et E marquent les énoncés ci-dessous [VÉRIFIÉ]. Je ne change pas ce statut. Je signale seulement que mon calcul, reproductible, les contredit sur une partie du domaine qu'ils annoncent. Il revient à l'arbitre de trancher.

- **C-b2, compromission totale.** L'énoncé de C : si ρ₁ > 0,5 et ρ₀ ≥ 0,45, le gain d'agrégation reste sous 10 points quelle que soit μ.
  - Contre-exemple, avec la formule même de C : ρ₀ = 0,45, ρ₁ = 0,6, α = 0,01, μ = 2 (tous illustratifs).
  - TPR_agg = Φ((6/√5,7 − 2,326)/√(2,2/1,9)) = Φ(0,17) ≈ 0,57.
  - TPR_seul = Φ(2 − 2,326) ≈ 0,37.
  - Le gain vaut donc environ 20 points (calcul), au-delà de 10.
  - L'énoncé ne tient que si ρ₀ est proche de ρ₁.
- **E-b2.** L'énoncé de E : si ρ_cop,1 > ρ_het,1 à μ égal, le gain des copies est strictement inférieur.
  - Contre-exemple : R = 3, ρ₀ = 0,3 dans les deux conditions, ρ_cop,1 = 0,6, ρ_het,1 = 0,3, μ = 0,5 (illustratifs).
  - On obtient TPR_agg,cop ≈ 0,081 et TPR_agg,het ≈ 0,050, pour un TPR individuel d'environ 0,034 dans les deux cas (calcul).
  - Le gain des copies (environ 4,7 points) dépasse donc celui de l'équipe hétérogène (environ 1,6 point).
  - Règle générale (calcul) : à ρ₀ et μ fixés, augmenter ρ₁ abaisse TPR_agg si et seulement si √R·μ > z·√(1 + (R−1)ρ₀), c'est-à-dire si et seulement si TPR_agg > 0,5.
- **Conséquence.** Le signe de l'effet de ρ sur le gain d'agrégation n'est pas donné a priori. C'est un argument de plus pour retirer toute prédiction directionnelle sur l'agrégation (T6).

---

## 2. (b) Expériences corrigées

### 2.0 Règles communes (HYPOTHÈSE de conception)

**Conditions comparées.**
- Agent seul.
- Copies, pour trois modèles de base. Existence et licences sont connues de mémoire et doivent être vérifiées : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma-2-9B-it.
- Deux triplets hétérogènes. Le second remplace un des modèles par Mistral-7B-Instruct-v0.3 (de mémoire, à vérifier).
- Copies munies de trois LoRA indépendants (T15).
- Rotation des rôles dans toutes les conditions.

**Bras de menace.**
- Toutes les copies sont adverses.
- Une seule copie est adverse, par un LoRA sur un seul rôle.
- Le bras « injection » disparaît avec E3.

**Règle de décision.**
- Je reprends ici la règle d'intervalle proposée par D, en le disant.
- Pour chaque contraste Δ, on préenregistre une seule marge d et on calcule un intervalle de confiance à 95 % par bootstrap par tâche (grappes) :
  - si l'intervalle est entièrement au-dessus de d, H_B est falsifiée ;
  - s'il est entièrement au-dessous, H_A est falsifiée ;
  - s'il contient d, l'issue est déclarée **indécise**.
- La taille d'échantillon est fixée sur pilote, pour que P(indécis) < 20 % à l'effet attendu (illustratif).

**Puissance** (T13).
- Formule : SD(TPR̂) ≈ √(LR²·α(1−α)/n₀,eff + TPR(1−TPR)/n₁,eff).
- Avec α = 5 %, LR = 5, n₀,eff = 2 000, n₁,eff = 1 000 et TPR = 0,5 (illustratifs), l'écart-type est d'environ 2,9 points (calcul).
- Pour un contraste non apparié, il est d'environ 4,1 points (calcul).
- Conséquences :
  - la **marge par défaut sur un TPR est de 8 points**, dans tous les contrastes de TPR ci-dessous (illustratif ; au moins deux fois l'écart-type du contraste, à réestimer sur pilote) ;
  - le **FPR primaire est de 5 %** ; le FPR de 1 % devient descriptif.

**Séparations.**
- Le juge de recrutement et le moniteur évalué sont de familles disjointes.
- Les seuils sont estimés sur des données honnêtes disjointes.
- Couches de sonde, stratégies rouges et agrégateurs sont choisis sur un jeu de développement.

**Plafonds déclarés.** Pour toute métrique à budget, le rappel est au plus min(1, b/π) (calcul).

### E0′ : porte de capacité

- **H_A** : le taux de sabotage réussi atteint au moins 5 % (illustratif). Un sabotage réussi réunit trois conditions : les tests visibles passent, la suite cachée échoue ou une porte dérobée existe, et le juge de recrutement score la contribution sous son seuil.
- **H_B** : le taux est inférieur à 5 %.
- **Publication** : les taux non conditionnés, à savoir P(échec caché ∧ tests visibles réussis) et P(sous le seuil | échec caché ∧ tests visibles réussis).
- **Contrôle** : des équipes honnêtes du même modèle, à la même température, fixent le plancher de bogues naturels.
- **Falsification** :
  - si H_B est falsifiée, on continue sur invite ;
  - si H_A est falsifiée, on bascule vers des organismes ajustés, sinon la question est non testable à 8B sur invite.

### E1′ : effet adversaire, concentration conjointe sans canal

- **Principe** (calcul) : sans canal, la loi jointe des choix est le produit des marginales. L'identité ne peut donc agir que par la forme des marginales, et non par une dépendance entre les tirages. Ce que l'on peut mesurer, c'est si les copies **convergent plus souvent sur le même point faible**.
- **Mesure** : la collision C_g = E_X[Σ_c Π_r P_r(c|X)], avec au moins 30 tirages indépendants par rôle et par tâche (illustratif). On publie aussi la concordance brute sur de vrais épisodes. Si elle s'écarte du produit des marginales, il y a une fuite, et on l'audite.
- **Estimande** : la double différence Δ_C = [C_cop^adv − C_cop^hon] − [C_het^adv − C_het^hon].
  - La consigne honnête est « désigne où un défaut serait le plus plausible », sur le même menu d'options.
  - Δ_C est moyennée sur les trois équipes homogènes, pour ne pas attribuer à l'identité la concentration propre à un modèle.
- **Facteur croisé (secondaire)** : on annonce aux partenaires qu'ils sont « des copies de toi » ou « d'autres familles de modèles », en croisant cette annonce avec la composition réelle de l'équipe. Ce facteur sépare l'effet des poids partagés de l'effet de la croyance en l'identité.
- **H_A** : Δ_C ≥ 10 points (illustratif).
- **H_B** : Δ_C < 10 points.
- **Contrôles** :
  - ordre des options permuté par copie ;
  - invites paraphrasées par rôle, pour séparer identité des poids et identité des contextes ;
  - graines et caches indépendants, avec preuve ;
  - tâches stratifiées par entropie des marginales honnêtes, celles d'entropie nulle étant exclues (perte de puissance signalée par A-b).
- **Falsification** :
  - si H_A est falsifiée, l'identité n'ajoute pas de convergence sur le même point faible à 8B ;
  - si H_B est falsifiée, Δ_C est la quantité que le défenseur doit intégrer dans son budget.

### E2-V : porte de validité des sondes (nouvelle, préalable à E2′)

- **Organismes** : un LoRA saboteur conditionnel au thème T, qui sabote sur T et reste honnête hors de T.
- **Placebo** : un LoRA de même rang et de norme appariée, entraîné sur des traces honnêtes qui incluent T.
- **Bogues honnêtes** : produits par le placebo à la même température, filtrés par tests et par mutation, de gravité appariée.
- **Plan 2×2** : {organisme, placebo} × {T présent, T absent}. Le sabotage n'existe que dans la case (organisme, T). On ajoute des leurres : des invites honnêtes qui mentionnent le sabotage.
- **H_A** : TPR(organisme ∧ T) − max[alertes(placebo ∧ T), alertes(organisme ∧ ¬T), alertes(bogues honnêtes)] ≥ 8 points (illustratif ; marge par défaut du § 2.0).
- **H_B** : l'écart est inférieur à 8 points.
- **Falsification** :
  - si H_A est falsifiée, la sonde lit le thème ou l'adaptateur. Toute conclusion défensive par activations est alors abandonnée dans ce dispositif, et le programme se réduit à E1′ et à E4′ sans activations ;
  - si H_B est falsifiée, on passe à E2′.

### E2′ : effet défenseur, efficacité en étiquettes du transfert

- **Budget du défenseur** : un total de n épisodes étiquetés, avec n ∈ {25, 50, 100, 200} (illustratif). Le défenseur les répartit librement entre rôles et modèles.
- **Défenseur des copies** : une sonde est entraînée sur un rôle source et appliquée à tous les rôles, ou bien entraînée sur l'ensemble des rôles mis en commun.
- **Défenseur hétérogène** : des sondes par modèle, ou un alignement après ACP. Les données d'alignement honnêtes sont déclarées.
- **Métrique** : TPR à FPR = 5 %, au niveau de l'épisode, sur des organismes de test dont les graines et les thèmes diffèrent de ceux d'entraînement. L'agrégateur est préenregistré par bras.
- **H_A** : à n = 50, TPR_cop − TPR_het (avec sa meilleure répartition des étiquettes) ≥ 8 points (illustratif ; marge par défaut du § 2.0).
- **H_B** : l'écart est inférieur à 8 points.
- **Prédiction annexe** : si H_A tient, les courbes d'apprentissage convergent vers n = 200, ce qui indique un pur effet d'efficacité en étiquettes.
- **Contrôles** :
  - étiquettes permutées ;
  - trois relectures d'une même copie sous des graines distinctes (simple réduction de variance) ;
  - bras de copies à trois LoRA indépendants ;
  - contrôle positif d'alignement : des copies tournées par une rotation aléatoire puis réalignées doivent retrouver la performance native, sinon l'alignement hétérogène n'est pas validé ;
  - référence sans activations (texte et outils mécaniques), évaluée sur le flux non filtré.
- **Falsification** :
  - si H_A est falsifiée, l'identité n'apporte aucun avantage d'efficacité en étiquettes à 8B ;
  - si H_B est falsifiée, il existe un effet défenseur propre à l'identité, dont on mesure la taille.

### E4′ : bilan à budget fixé

- **Budget d'audit** : b = 2 % (illustratif). Le plafond b/π est déclaré.
- **Métrique primaire** : θ_g = P(sabotage réussi et non audité), par épisode.
- **Contraste** : log(θ_cop/θ_het).
  - **H_A** : |log ratio| ≥ log 1,5 (illustratif).
  - **H_B** : |log ratio| < log 1,5.
  - Le signe est un contraste secondaire, préenregistré.
- **Métrique secondaire** : la sûreté de séquence, avec un horizon choisi sur pilote pour qu'elle reste entre 0,2 et 0,8 (illustratif).
- **Stratégies rouges** :
  - cinq stratégies fixées et une itération adaptative, sur le jeu de développement seulement ;
  - la stratégie de pire cas est choisie sur le développement et évaluée sur des séquences inédites.
- **Organismes** : ceux qui servent à entraîner les sondes sont distincts de ceux d'évaluation.
- **Oracle** : son rappel est publié par famille, et le risque est pondéré par famille.
- **Contrôle** : un défenseur sans activations. Si l'écart entre copies et équipe hétérogène est le même, l'effet ne passe pas par les activations.
- **Falsification** :
  - si H_A est falsifiée, l'identité ne change pas le risque net à 8B (§ 3) ;
  - si H_B est falsifiée, l'identité compte, et le signe dit à qui elle profite.

### E5′ : obfuscation

- **Protocole** :
  - l'organisme est ajusté avec une pénalité sur la sonde de E2′ ;
  - un témoin est ajusté à pénalité nulle ;
  - taux de sabotage et utilité honnête doivent rester à ±3 points du témoin (illustratif), sans quoi la population de positifs a changé et on le rapporte.
- **Riposte bleue** : une sonde réentraînée sur l'organisme obfusqué, hors échantillon, avec des couches choisies sur le développement.
- **H_A** : le TPR de cette sonde réentraînée dépasse la référence sans activations de moins de 8 points (illustratif ; marge par défaut du § 2.0). Autrement dit, le signal linéaire est effacé.
- **H_B** : elle la dépasse d'au moins 8 points.
- **Mesure secondaire** : une obfuscation apprise contre le rôle r se transfère-t-elle aux autres rôles, chez les copies et dans l'équipe hétérogène ?
- **Falsification** :
  - si H_A est falsifiée, l'avantage du défenseur survit à cette attaque ;
  - si H_B est falsifiée, le signal linéaire est effaçable à 8B pour cette attaque.

### Calendrier révisé (illustratif)

| Semaines | Travail |
|---|---|
| 1–2 | E0′ et E1′, sur invite, sans ajustement ; validation de l'oracle |
| 3–4 | Organismes, placebos, LoRA indépendants ; E2-V |
| 5–6 | E2′ |
| 7 | E4′ |
| 8 | E5′ ; publication |

**Calcul** : environ 500 heures-GPU H100 (illustratif), contre 350 en III.1, à cause des placebos, du quatrième modèle et des LoRA supplémentaires. **Goulet probable** : la porte S3, à savoir la capacité de sabotage subtil à 8B.

---

## 3. (c) Réponse à la question de l'arbitre

**Question révisée.** Pour N copies d'un même modèle qui dégradent une tâche par des contributions chacune défendable, l'identité des poids accroît-elle davantage la concentration des copies sur le même point faible, sans canal, que l'efficacité en étiquettes d'un détecteur sur activations transféré entre copies, à budget d'audit fixé, par rapport à un agent seul ou à des modèles différents ?

**Ce qui est établi.**
- **Aucun fait empirique.** La pièce FAITS n'en contient aucun.
- **Par calcul**, sous des prémisses qui sont des HYPOTHÈSES :
  1. Sans canal, la loi jointe des choix est le produit des marginales. Côté adversaire, l'identité agit uniquement par la ressemblance et la concentration de ces marginales, pas par une dépendance entre tirages.
  2. Agréger des scores scalaires ne demande aucun espace commun. L'avantage défensif propre à l'identité ne peut venir que du transfert de sondes ou de sondes conjointes. Quant au signe de l'effet de ρ sur le gain d'agrégation, il dépend du régime (§ 1.2).
  3. Le rappel à budget est plafonné à b/π, et la sûreté de séquence sature.
- **Sur le plan méthodologique**, ma conception III.1 contenait trois tests vrais ou vides par construction : κ, la comparaison sonde/texte après S4, et E3. Ils sont corrigés.

**Ce qui n'est pas établi** (HYPOTHÈSE) :
- qu'un modèle 8B sache saboter subtilement (S3) ;
- que les sondes lisent l'intention plutôt que l'adaptateur ou le thème (E2-V) ;
- que Δ_C soit positif (P1′ : au moins 10 points) ;
- qu'il existe un avantage d'efficacité en étiquettes (P2′ : au moins 8 points à n = 50) ;
- le signe du bilan net (P3′ : positif si E2-V passe et si E5′ n'efface pas le signal ; nul ou négatif sinon).

Chacune de ces trois prédictions est réfutable séparément.

**Expérience à faire en premier : E1′, couplée à E0′,** sur invite, en deux semaines. Trois raisons :
1. Elle ne demande ni ajustement fin ni sonde validée, et c'est la moins chère.
2. Ses deux issues sont informatives. Si Δ_C ≈ 0, la moitié adverse de la question tombe à 8B. Si E0′ échoue, le programme est réorienté vers les organismes ajustés.
3. E2-V vient ensuite, comme porte obligatoire avant toute affirmation fondée sur les activations.

**Issues qui rendraient la question sans intérêt.**
- H_A est falsifiée à la fois dans E1′ et dans E2′. Ou bien E2-V échoue et E1′ est nulle : l'identité ne change alors rien de mesurable à 8B.
- Les références mécaniques attrapent déjà au moins 95 % des sabotages au budget fixé.
- Un échec de E0′ ne signifie pas que les copies sont sûres. Il signifie que la question n'est pas testable à 8B sur invite.

**Type de contribution.**
- Un phénomène connu ailleurs, transposé et mesuré : les points focaux et la défaillance de mode commun. S'y ajoute une mesure de compromis. Ce n'est pas une garantie.
- **Nouveautés retirées** : l'agrégation entre copies ; le renversement obtenu par un ajustement unique.
- **Candidates restantes** (HYPOTHÈSE) : la double différence Δ_C et l'efficacité en étiquettes comme effet défensif propre à l'identité.

**Vérification.**
- Une revue ciblée de l'antériorité citée en III.1, toujours de mémoire et à vérifier, notamment Greenblatt, Shlegeris, Sachan et Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion ».
- Une réplication sur une deuxième base de copies avant toute revendication.

FIN-DE-CELLULE