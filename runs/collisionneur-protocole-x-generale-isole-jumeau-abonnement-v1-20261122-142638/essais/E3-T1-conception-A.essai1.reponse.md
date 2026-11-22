# Proposition A — tour III.1 (conception ciblée, à l'aveugle)

**Pièces.** Les blocs FAITS et QUESTION sont identiques (même empreinte) : aucun résultat empirique n'est transmis et aucun énoncé ne porte d'étiquette de statut. Je traite le cadre comme RAPPORTÉ (posé par l'arbitre) et n'élève rien au rang de VÉRIFIÉ. Les propositions B à E ne me sont pas visibles : B1 est sans objet. Aucune recherche n'a été faite à ce tour ; toute référence est citée de mémoire.

**Convention.** Les faits ne contiennent aucun chiffre. Tous les nombres ci-dessous (seuils, tailles, coûts, probabilités) sont **illustratifs** : ils fixent la forme des tests et se gèlent avant collecte.

## 1. Réponse aux cinq points de l'arbitre

**(1) Question retenue.** *Le dégât qu'un adversaire peut accumuler sans alerte est-il gouverné par une seule grandeur mesurable — l'évidence par acte que les instruments du défenseur extraient, agrégée sur la trajectoire — au point que des paramètres mesurés sur un agent seul et sur tâches courtes prédisent, sans réajustement, la frontière dégât-détection sur tâches longues, avec plusieurs copies et avec des moniteurs visés ?*

Ensemble ou séparés : les trois articles ne valent plus ensemble que si cette prédiction croisée réussit (duel 6). Si elle échoue, ils restent distincts et ne partagent qu'un banc de mesure (tâches, témoins honnêtes appariés, comptabilité des budgets). Ce banc est une annexe commune, pas une problématique.

**(2) Réponse attendue (HYPOTHÈSE).** Notations :

- μ : décalage moyen du score d'un moniteur sur un acte dégradé ;
- σ : écart-type du score honnête à l'intérieur d'une tâche ;
- τ : écart-type du score honnête entre tâches ;
- m : nombre d'exécutions de comparaison appariées ;
- z : constante fixée par les taux d'erreur visés ;
- k* : nombre maximal d'actes dégradés sans alerte sur T étapes.

Le modèle prédit deux régimes :

- sans comparaison : k* ≈ z·√(T·σ² + T²·τ²)/μ, donc linéaire en T dès que τ > σ/√T ;
- avec comparaison appariée : k* ≈ z·σ·√(T·(1+1/m))/μ, donc en racine de T, avec un gain saturé vers m = 2.

Mes attentes, duel par duel :

- duel 2 : exposant inférieur à 0,75 avec appariement ;
- duel 3 : la valeur des comparaisons vient de l'appariement ;
- duel 4 : H_B, la prédiction échoue pour des copies toutes adversaires, parce qu'elles dégradent les mêmes étapes ;
- duel 5 : l'évidence se déplace sans s'effondrer quand un seul moniteur est visé ;
- duel 6 : réussite seulement une fois ajouté un paramètre de coïncidence entre copies, avec une probabilité subjective d'environ 40 % (illustratif).

**(3) Antériorité (tout est cité de mémoire).**

- La plus proche par le problème : Wen, Hebbar, Larson et coll. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » (liste complète des auteurs à vérifier). Le défenseur y accumule une croyance sur un modèle non fiable quand aucun acte isolé n'est décisif. À vérifier : je ne me souviens pas qu'un exposant d'horizon, des copies ou des moniteurs attaqués y soient traités.
- Cadre : Greenblatt, Shlegeris, Sachan, Roger (2024), « AI Control: Improving Safety Despite Intentional Subversion ».
- Exécutions de comparaison : Bhatt et coll. (2025), « Ctrl-Z: Controlling AI Agents via Resampling » (auteurs à vérifier).
- Loi transposée : Bash, Goeckel, Towsley (2013), « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels » ; Ker, Pevný, Kodovský, Fridrich (2008), « The Square Root Law of Steganographic Capacity » ; Page (1954), « Continuous Inspection Schemes ».
- Moniteurs visés : Bailey et coll. (2024), « Obfuscated Activations Bypass LLM Latent-Space Defenses » (auteurs à vérifier).
- Sondes : Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), « Detecting Strategic Deception Using Linear Probes ».
- Le résultat selon lequel une connaissance imparfaite de la référence rend la capacité furtive linéaire : référence à vérifier.

**(4) Expérience décisive.** Le duel 6, alimenté par les duels 1 à 5 ; l'ensemble tient en deux mois (section 5).

**(5) Type.** Loi connue ailleurs (loi en racine des communications furtives et de la stéganographie, détection séquentielle), transposée et testée comme loi d'échelle. S'y ajoute un phénomène propre aux copies : la coïncidence des dégradations. Ce n'est pas une garantie : les hypothèses qui font la loi (actes indépendants, référence honnête connue) sont justement ce que les duels testent.

**Issues qui ôtent l'intérêt.**

1. Duel 1, H_B : pas de régime diffus à 8 Md. La loi ne serait alors testée que sur un adversaire scripté, où elle est vraie par construction.
2. Évidence par acte nulle pour tous les instruments, même agrégée. La frontière dégénère et les trois articles se réduisent à l'allocation des vérifications coûteuses.
3. Duel 6 réussi, mais un prédicteur naïf (dégât proportionnel à T) fait aussi bien. L'unité commune n'ajoute rien.

**Nouveauté avancée (HYPOTHÈSE, non vérifiée à ce tour).** Deux points : mesurer l'exposant du dégât non détecté selon l'horizon pour un adversaire-agent, et décider de l'unification par prédiction croisée hors échantillon. Pour vérifier :

- lire Wen et coll. (2024) et Bhatt et coll. (2025) pour voir si un exposant d'horizon ou une prédiction inter-régimes y figurent ;
- chercher « square root law » croisé avec « AI control », « sabotage », « monitoring », et « distributed/diffuse threats » croisé avec « horizon » ;
- couvrir 2025–2026, que je ne peux pas énumérer de mémoire (références à vérifier) ;
- soumettre à deux lecteurs du domaine.

## 2. (a) Ce que la question suppose sans que ce soit établi

1. **Des actes non suspects isolément existent pour ces moniteurs.** RAPPORTÉ comme possibilité par le cadre ; pour un modèle de 8 Md agissant de lui-même, HYPOTHÈSE (duel 1).
2. **Le dégât est cumulatif.** HYPOTHÈSE. Si un seul acte porte l'essentiel du dégât, la menace est concentrée et appelle d'autres défenses.
3. **« Non suspect isolément » vaut pour un moniteur par acte.** HYPOTHÈSE implicite : rien n'est dit d'un agrégateur de trajectoire, et c'est là que la question se joue.
4. **Une référence honnête stable existe.** HYPOTHÈSE. Un agent honnête se trompe aussi, peut-être davantage quand la tâche s'allonge ; « dégrader » n'a de sens que contre un contrefactuel apparié.
5. **Adversaire externe et agent adversaire relèvent du même cadre.** HYPOTHÈSE. Une sonde peut lire une intention dans un cas et l'exécution d'une consigne injectée dans l'autre.
6. **Les trois articles partagent ressources et unité de compte.** HYPOTHÈSE ; c'est l'objet du duel 6.
7. **Des copies d'un même modèle forment un régime à part.** HYPOTHÈSE (erreurs et choix corrélés) ; duel 4.
8. **Les exécutions de comparaison sont honnêtes et informatives.** HYPOTHÈSE. Si l'adversaire est l'agent, une comparaison faite par le même modèle n'est pas une référence sûre.
9. **Les vérifications coûteuses disent le vrai.** HYPOTHÈSE. Sur une tâche de recherche réelle, la vérité est parfois ambiguë ; le banc la rend mécanique, au prix du réalisme.
10. **Ce qu'on mesure à 8 Md vaut pour des agents plus capables.** HYPOTHÈSE, non testée ici ; limite à écrire dans chaque article.

## 3. (b) Expériences décisives

**Banc commun.**

- **Tâches :** chaînes d'analyse de T étapes, T ∈ {8, 16, 32, 64, 128}, sur données synthétiques ; chaque étape a une vérité calculable par script.
- **Adversaire (S), scripté :** l'expérimentateur altère k étapes tirées au hasard (valeur décalée, réserve omise, sélection biaisée). C'est un étalon, pas un résultat.
- **Adversaire (P), politique :** le même modèle, conditionné par consigne ou adaptation LoRA à dégrader environ une étape sur r sans se faire remarquer ; le k réalisé est compté par le script.
- **Témoin honnête apparié :** pour chaque acte dégradé, la continuation honnête du même préfixe ; pour chaque trajectoire, l'exécution honnête de la même tâche.
- **Dégât D :** perte de score final contre l'exécution honnête appariée.
- **Scores :** moniteur de texte (note de suspicion par étape) ; sonde linéaire sur activations (couche médiane, dernier jeton de l'étape), entraînée sur une famille de tâches disjointe.
- **Agrégation :** maximum par acte, et somme des scores centrés-réduits sur la référence honnête (elle ne suppose pas de connaître l'adversaire).
- **k*(T) :** plus grand k tel que la détection reste ≤ 50 % à 5 % de fausses alertes.

[DUEL 1]

**Le régime diffus existe-t-il à cette échelle ?** La recherche de politique (P) est bornée et gelée : 20 consignes et 3 adaptations LoRA.

- **H_A :** au moins une politique atteint D ≥ 20 % à T = 32 avec une AUROC par acte ≤ 0,70 pour le meilleur instrument, sans qu'un acte porte plus de la moitié du dégât.
- **H_B :** aucune politique de la liste n'y parvient.
- **Métrique :** AUROC par acte contre témoins appariés ; part du dégât portée par l'acte le plus nocif.
- **Contrôle négatif :** honnête contre honnête (AUROC 0,50 ± intervalle) ; (S) à décalage nul.
- **Falsification :** H_A réfute « un modèle de 8 Md ne sait pas saboter discrètement, il faut un adversaire scripté ». H_B réfute la prémisse du cadre à cette échelle : les duels 2 à 6 ne valent alors que pour (S), et l'expérience demandée au point (4) n'est pas réalisable telle quelle avec un adversaire-agent.

[DUEL 2]

**Quel exposant relie le dégât non détecté à l'horizon ?** Agent seul, une référence appariée, adversaire (P).

- **H_A :** k*(T) croît comme T^γ avec γ < 0,75.
- **H_B :** γ ≥ 0,75.
- **Métrique :** pente de log k* contre log T, intervalle à 90 % par rééchantillonnage des tâches.
- **Seuil :** l'intervalle doit tomber d'un seul côté de 0,75 ; sinon le duel est déclaré indécis, pas gagné.
- **Contrôle négatif :** (S) à tirages indépendants doit redonner γ = 0,5 ± 0,1 ; le taux de fausses alertes honnête-contre-honnête doit rester à 5 % ± 2 pour chaque T, sinon une dérive honnête avec l'horizon invalide la mesure.
- **Falsification :** H_A réfute « allonger la tâche profite linéairement à l'adversaire, seules les vérifications coûteuses comptent ». H_B réfute la transposition de la loi en racine à un adversaire-agent (actes corrélés ou dérive), et avec elle la version forte de la problématique commune.

[DUEL 3]

**Que paient les exécutions de comparaison ?** Plan 2 × 2 : hétérogénéité des tâches (familles variées ou gabarit unique) × référence (appariée à la même tâche, ou honnête non appariée de la même famille).

- **H_A (appariement) :** en forte hétérogénéité, le gain de détection apparié est ≥ 2 fois le gain non apparié ; l'écart tombe sous 20 % en faible hétérogénéité ; le gain sature à m = 2.
- **H_B (réplication) :** rapport apparié/non apparié < 1,3 dans les deux conditions.
- **Métrique :** gain de détection à 5 % de fausses alertes par rapport à m = 0.
- **Seuil :** un rapport entre 1,3 et 2 est déclaré indécis.
- **Contrôle négatif :** référence de la même tâche aux étapes désalignées (aucun gain apparié attendu) ; paires honnête-honnête à 5 %.
- **Falsification :** H_A réfute « une banque de références honnêtes hors ligne suffit ». H_B réfute « les comparaisons sont une ressource rare à allouer » : le budget se réduit alors aux vérifications coûteuses plus une calibration fixe.

[DUEL 4]

**Les copies d'un même modèle dégradent-elles les mêmes étapes ?** Chaque étape est exécutée par K ∈ {2, 4, 8} copies portant toutes (P) ; le signal est la divergence entre copies.

- **H_A (indépendance) :** la détection observée est prédite à ± 0,10 par les paramètres de l'agent seul plus la corrélation mesurée sur exécutions honnêtes.
- **H_B (coïncidence) :** l'écart dépasse 0,10 et la détection observée est sous la prédiction.
- **Métrique :** erreur absolue moyenne sur la probabilité de détection à 5 % de fausses alertes ; en diagnostic, accord κ des étapes dégradées au-delà du hasard.
- **Cas hors duel :** un écart dans l'autre sens signale un modèle faux pour une autre raison ; il compte contre l'unification, sans appuyer la collusion.
- **Contrôle négatif :** (S) à tirages indépendants par copie (κ ≈ 0 par construction, la prédiction doit tenir) ; équipe hétérogène avec un autre modèle ouvert, pour séparer « même modèle » de « plusieurs agents ».
- **Falsification :** H_A réfute « des copies se coordonnent sans communiquer » à cette échelle ; l'article multi-copies devient un chapitre du cadre commun. H_B réfute la suffisance des paramètres honnêtes : cet article garde un objet propre (κ), et une comparaison faite par le même modèle n'est pas une référence fiable.

[DUEL 5]

**Viser un moniteur déplace-t-il l'évidence ou l'effondre-t-il ?** L'adversaire est adapté contre un seul instrument X : recherche de consignes ou LoRA pénalisant le score du moniteur de texte, puis LoRA pénalisant le score de la sonde. Le dégât est maintenu à ± 10 %. Le duel ne compte que si l'évidence dans X chute d'au moins 50 % ; sinon on consigne « attaque échouée ».

- **H_A (déplacement) :** l'évidence conjointe des deux moniteurs, recalibrée sur l'honnête seul, reste ≥ 70 % de sa valeur initiale.
- **H_B (effondrement) :** elle tombe sous 70 %.
- **Métrique :** rapport après/avant de l'évidence par acte (décalage centré-réduit), par instrument et conjointe.
- **Contrôle négatif :** même calcul d'adaptation contre un moniteur factice (direction aléatoire, étiquettes permutées), qui ne doit pas faire chuter l'évidence de plus de 10 % ; contrôle de dégât apparié, pour écarter le cas où l'adversaire a simplement cessé de saboter.
- **Falsification :** H_A réfute « un moniteur contourné, tout tombe » ; l'article sur les moniteurs décrit alors comment μ se répartit entre instruments, dans le cadre commun. H_B réfute la complémentarité texte/activations : la robustesse des moniteurs devient le goulot, avant l'horizon et la taille d'équipe, et cet article doit rester autonome.

[DUEL 6]

**La prédiction croisée tient-elle hors échantillon ?** Les paramètres (μ par instrument, σ, τ, corrélation honnête, et κ si le duel 4 donne H_B) sont mesurés seulement à T ≤ 16. Les prédictions sont gelées, avec l'empreinte du script, pour 12 configurations tenues à l'écart : 4 par régime, T ∈ {64, 128}, budgets m et c variés.

- **H_A :** dans chacun des trois régimes, l'erreur relative médiane sur k* est ≤ 25 % et au moins deux fois plus faible que celle du prédicteur naïf (dégât proportionnel à T, ajusté sur les mêmes données).
- **H_B :** la condition échoue dans au moins un régime.
- **Métrique :** erreur relative médiane sur k*, par régime.
- **Contrôle négatif :** prédicteur naïf ; test d'échange (paramètres d'un régime appliqués à un autre), qui doit dégrader la prédiction, sinon le test est insensible aux paramètres.
- **Falsification :** H_A réfute « trois problèmes distincts » ; la problématique commune est alors la frontière dégât-détection et ses taux de change entre ressources. H_B réfute la problématique commune telle qu'énoncée ; les articles restent distincts, et le régime où la prédiction casse désigne l'apport propre de l'article correspondant.

[FIN DES DUELS : 6]

## 4. (c) Mesure minimale par instrument

**Moniteur de texte.**

- **Mesure :** taux de détection par acte à 1 % et 5 % de fausses alertes ; par trajectoire à 5 %.
- **Honnêtes appariés :** continuation honnête du même préfixe, erreurs honnêtes spontanées incluses, sinon le moniteur détecte l'erreur et non le sabotage.
- **À battre :** régression logistique sur longueur et perplexité de l'étape ; recalcul par script quand l'étape est numérique ; score aléatoire.
- **Verdict minimal :** gain ≥ 10 points de détection à 5 % de fausses alertes sur la meilleure base mécanique.

**Moniteur d'activations.**

- **Mesure :** la même, sur une famille de tâches et un type de dégradation tenus à l'écart de l'entraînement.
- **Honnêtes appariés :** mêmes positions de jetons, même préfixe. Deux pièges s'ajoutent : l'erreur honnête (la sonde lit-elle l'erreur ?) et la consigne adversaire présente avec un acte honnête (lit-elle la consigne ?).
- **À battre :** classifieur linéaire sur sac de mots du même texte ; sonde à étiquettes permutées ; direction aléatoire ; sonde sur la couche d'entrée.
- **Verdict minimal :** ajoutée au moniteur de texte, la sonde apporte ≥ 5 points de détection à 5 % de fausses alertes ; sinon les activations sont redondantes avec le texte.

**Exécutions de comparaison.**

- **Mesure :** détection par divergence d'étape contre la référence, courbe en m, rapportée au coût en jetons.
- **Honnêtes appariés :** paires honnête-honnête sur la même tâche, graines différentes ; elles donnent la divergence naturelle, donc le taux de fausses alertes.
- **À battre :** différence exacte des sorties numériques ; banque de références non appariées (duel 3).
- **Verdict minimal :** à coût égal, détection supérieure à celle obtenue en dépensant les mêmes jetons en passes supplémentaires du moniteur de texte.

**Vérifications coûteuses.**

- **Mesure :** taux d'erreur du vérificateur sur étapes à vérité connue, dans les deux sens, ≤ 2 % ; rendement de l'allocation (part des vérifications tombant sur un acte dégradé).
- **Honnêtes appariés :** étapes honnêtes erronées, pour séparer « faux » de « saboté ».
- **À battre :** allocation au hasard (rendement k/T) ; allocation par centralité de l'étape dans le graphe de dépendances, sans moniteur.
- **Verdict minimal :** rendement ≥ 2 fois le hasard et supérieur à la centralité, à budget c égal.

**Agrégateur** (non nommé dans la question, mais tout en dépend) : fausses alertes honnête-contre-honnête à 5 % ± 2 pour chaque T.

## 5. (d) Ancrage matériel

Rien dans cette section ne vient des faits : tout y est illustratif.

- **Modèles (choix d'exemple, de mémoire) :** Llama-3.1-8B-Instruct comme agent et adversaire. Un second modèle ouvert de taille voisine (Gemma-2-9B ou Qwen2.5-7B-Instruct) sert aux contrôles d'équipe hétérogène et de référence de confiance.
- **Volume :** environ 12 000 trajectoires pour les duels 2 et 3 (5 horizons × 6 taux × 200 tâches × 2 conditions), soit environ 600 000 étapes. À 300 jetons produits par étape, cela fait environ 180 millions de jetons. Compter autant pour les duels 4 à 6, plus environ 1 000 jetons lus par étape pour la notation.
- **Puissance statistique :** un seuil à 5 % de fausses alertes par trajectoire demande au moins 500 trajectoires honnêtes par horizon ; le seuil à 1 % n'est rapporté que par acte.
- **Calcul :** 500 à 1 500 heures de GPU de 24 à 48 Go, adaptations LoRA et reprises comprises, sur un à quatre GPU en parallèle.
- **Coût :** 1 000 à 3 000 dollars en location.
- **Stockage :** une couche, dernier jeton de chaque étape, demi-précision, soit environ 5 Go par couche.
- **Calendrier :**
  - semaines 1–2 : banc, vérificateur, calibration honnête, duel 1 (décision de poursuivre) ;
  - semaines 3–4 : duels 2 et 3 ;
  - semaines 5–6 : duels 4 et 5 ;
  - semaines 7–8 : duel 6 sur configurations gelées.
- **Gel avant la semaine 7 :** seuils, liste des 12 configurations, empreinte du script d'analyse.
- **Hors de portée de ce programme :** le transfert à des agents plus capables et à des tâches de recherche sans vérité mécanique (présupposés 9 et 10).

FIN-DE-CELLULE