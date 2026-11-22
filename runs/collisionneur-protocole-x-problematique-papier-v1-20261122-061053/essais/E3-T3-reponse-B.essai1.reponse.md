# Proposition B — Tour III.3 : réponse aux critiques

**Pièces reçues.** J'ai reçu ma conception III.1 et les sections « Sur la proposition B » des critiques A, C, D et E. Toutes sont présentes, non vides, et se terminent par leur ligne de fin. Je ne recalcule pas les empreintes sha256. Je ne réponds qu'aux sections qui visent B.

**Statuts.** Je ne modifie aucun statut. Les critiques étiquettent leurs propres déductions VÉRIFIÉ ou « VÉRIFIÉ : déduction ». Je conserve ces étiquettes et je lis ces énoncés comme des conséquences mathématiques sous les conditions que chaque critique écrit, pas comme des mesures sur des agents. Tout chiffre ci-dessous qui ne vient pas d'une pièce est **illustratif**.

---

## (a) Décision sur chaque critique

**Légende.** ACC : acceptée. REJ : rejetée, avec la raison. TEST : transformée en test. Quand une critique en double une autre, je renvoie à la première occurrence.

### Critiques de A

| # | Critique | Décision | Action |
|---|---|---|---|
| A1 | E0 est vrai par réglage de l'intensité, et la zone 0,75–0,9 ne falsifie rien. | ACC | E0′ : l'intensité est fixée par un critère de furtivité **avant** de regarder le dommage. La zone non concluante est déclarée selon la règle de D. |
| A2 | log(1/α)/ε n'est valable que si l'incrément est le vrai log-rapport de vraisemblance. | ACC | D est remplacé par le taux effectif du détecteur déployé, ρ = θ*·E₁[Z] (voir (b)). |
| A3 | « Un seul point » dans la région critique ne tient pas compte de l'incertitude. | ACC | Un point compte seulement si la borne inférieure de son IC sur le dommage est ≥ δ et si la borne supérieure de son IC sur ρ est < ε. |
| A4 | Les couches sont choisies sur une validation qui peut contenir la famille tenue à l'écart. | ACC | La sélection des couches est refaite dans chaque pli, sur les seules familles de développement. |
| A5 | Type 2 : trois facteurs sont confondus, et H_A/H_B ne sont pas exhaustives. | ACC | Plan factoriel 2×2×2 (voir (b)). |
| A6 | Les activations peuvent coder la présence de la consigne adverse. | TEST | Placebo croisé : consigne sans dommage, et dommage sans consigne (sources empoisonnées). |
| A7 | La longueur des trajectoires confond le gain. | ACC | Horizon fixe et honnêtes appariés en longueur. |
| A8 | D_act ≥ D_texte par l'inégalité de traitement de l'information. | ACC | J'abandonne D_act > D_texte. La grandeur devient le **gain conditionnel au texte et au contexte complet**. |
| A9 | Pente × D ≈ 1 est une hypothèse jointe. | ACC | Passer à ρ retire la mauvaise spécification du log-rapport. Le brassage temporel sépare l'autocorrélation de l'estimateur. |
| A10 | Avec 8 références, le plancher conformal vaut 1/9. | ACC | Calibration sur des tâches tenues à l'écart (voir (b)). La garantie devient marginale sur les tâches, et je l'écris ainsi. |
| A11 | Biais de l'estimateur de D. | ACC | Plancher honnête contre honnête, à effectif et dimension identiques. |
| A12 | La pente vaut 1/(θ*E₁[Z]). | ACC | Voir A2. C'est désormais la prédiction testée. |
| A13 | Censure. | ACC | ARL₀ et délai moyen non tronqué sont abandonnés au profit de grandeurs observables à horizon fini (voir (b)). |
| A14 | Non-stationnarité. | ACC | C'était déjà mon H_B. Pour les familles concentrées, je rapporte le profil D_t et ne prédis aucun scalaire. |
| A15 | À 1 % de fausses alertes, le seuil repose sur environ 2 tâches. | ACC | Point de fonctionnement principal à 5 % (illustratif). IC par grappes de tâches. |
| A-c1 à c4 | Placebo de consigne, plancher D̂, brassage temporel, honnêtes appariés en longueur et sous dérive bénigne. | ACC | Les quatre sont intégrés en (b). |

### Critiques de C

| # | Critique | Décision | Action |
|---|---|---|---|
| C1 | Une calibration à une seule classe ne donne pas le délai de la CUSUM optimale. Conditionner à D ≥ ε serait circulaire et non opérationnel. | ACC sur le premier point, REJ sur le second | Voir A2 pour le premier. **Raison du rejet :** un certificat conditionnel n'exige pas que le défenseur observe la condition en ligne. Un certificat de lissage aléatoire couvre aussi une classe de perturbations dont le défenseur ignore le rayon effectif. La condition délimite le domaine de l'énoncé ; elle n'est pas une règle de décision. Une attaque qui tombe dans le noyau du score a ρ = 0. Elle se trouve donc dans la région « ρ < ε », où l'énoncé à tester est *dommage < δ*. C'est le contenu de H_B, pas un défaut du protocole. |
| C2 | Une graine partagée ne couple pas les tirages après la bifurcation. | TEST | Je garde le statut VÉRIFIÉ que C donne à cet énoncé. La portée exacte dépend de l'échantillonneur, mais ma décision ne change pas : je ne revendique plus d'appariement après l'étape t. Les branches sont comparées en distribution, IC groupés par préfixe, avec un contrôle de perturbation neutre. |
| C3 | 1/α ≠ ARL₀ : il manque log T. ARL₀ n'est pas mesurable sous censure. | ACC | Avec α ≈ T/ARL₀, on a log ARL₀ ≈ log(T/α). Les grandeurs sont remplacées (voir (b)). |
| C4 | Calibration conformale impossible avec 8 références. | ACC | Voir A10. |
| C5 | Trois problèmes d'estimation : estimateur de censure dégénéré, incrément sous-optimal, biais d/n de ŵ. | ACC | Découpage strict en trois parts : entraînement de la sonde, estimation de θ* et E₁[Z], test. |
| C6 | Un best-of-N peut rendre la dérive négative alors que le dommage atteint δ. | REJ comme défaut, TEST | **Raison :** ce n'est pas une faille de méthode. C'est exactement le contre-exemple que le duel du type 1 doit chercher. Cette attaque est classée **première** attaque adaptative. Si elle atteint dommage ≥ δ avec ρ < ε, H_A tombe et le type 1 devient un résultat d'impossibilité (4b). |
| C-c1 | Bifurcation par substitution d'un synonyme. | ACC | Intégré. |
| C-c2 | Processus synthétique censuré. | ACC | Intégré. |
| C-c3 | Plancher D̂ par modalité. | ACC | Intégré. |

### Critiques de D

| # | Critique | Décision | Action |
|---|---|---|---|
| D1 | Le taux d'information du détecteur optimal est attribué au détecteur déployé. | ACC | Voir A2. Le rapport ρ/D_cond devient une grandeur mesurée : l'efficacité du moniteur. |
| D2 | Délai moyen, délai conditionnel et délai de pire cas sont confondus. ARL₀ n'est pas une probabilité de fausse alerte. | ACC | Je mesure le délai **conditionnel à l'absence d'alarme avant la rupture**, rupture à l'instant de bifurcation. Je ne revendique pas le pire cas de Lorden. |
| D3 | La présélection E0 favorise des tâches déjà séparées. | ACC | E0′ se décide au niveau du modèle et de la famille de tâches, sur un jeu de tâches distinct. Les expériences suivantes utilisent des tâches fraîches, tâches difficiles comprises. |
| D4 | Des branches issues d'un même préfixe ne sont pas indépendantes. | ACC | IC groupés par préfixe et par tâche. |
| D5 | La frontière demande des réplications par loi. Un maximum empirique n'est pas une borne. | ACC | Un point de frontière = une politique (famille, intensité, budget adaptatif), avec n ≥ 30 réplications (illustratif). En l'absence de point critique, je rapporte la borne binomiale exacte sur la probabilité de dommage extrême, pas un supremum. |
| D6 | Sous dépendance, la grandeur est la somme des KL conditionnelles au passé. | ACC | D_cond est estimé par un discriminateur conditionnel au préfixe. Il sert de diagnostic secondaire. |
| D7 | Une calibration marginale ne garantit pas la calibration conditionnelle par tâche. | ACC | Fausses alertes rapportées par strate de difficulté honnête. La garantie est déclarée marginale. |
| D8 | Un vérificateur qui signale indifféremment rend son taux de capture non informatif. | ACC | Je rapporte la capture nette, sensibilité − taux de fausses alertes du vérificateur, mesurés séparément. |
| D9 | Borne de variation totale : rappel ≤ α + v. | ACC | Utilisée comme diagnostic de plafond de puissance par instrument. |
| D-c | Honnête contre honnête sur les tâches rejetées. Même procédure de densité. Changement de phase honnête. Croisement texte/activations × somme/CUSUM. | ACC | Intégrés. |
| D-c | La permutation des références entre tâches ne suffit pas comme contrôle. | ACC | Mon contrôle 1 du type 2 était mal posé : sa réussite ne réfutait rien si le niveau honnête est commun aux tâches. Il devient le facteur « références propres contre génériques » du plan factoriel. |

### Critiques de E

| # | Critique | Décision | Action |
|---|---|---|---|
| E1 | Vérifier Lorden sur le score CUSUM ne teste qu'une propriété arithmétique. | REJ en partie | **Raison :** c'est vrai si D et le délai sont mesurés sur les mêmes données pour le vrai log-rapport, et je l'écrivais déjà (« Lorden est un théorème »). Ce n'est plus vrai sous la forme corrigée. Des grandeurs à un pas (θ*, E₁[Z]) estimées sur la partie A prédisent des grandeurs de trajectoire sur la partie B, avec des scores dépendants. L'écart vient justement de la dépendance et de la non-stationnarité. |
| E2 | Plancher conformal. | ACC | Voir A10. |
| E3 | Désynchronisation des graines. | TEST | Voir C2. Le contrôle de E est adopté. |
| E4 | La sélection best-of-8 crée une distorsion indépendante du dommage. | TEST | Best-of-8 honnête sans consigne. Son taux d'alerte mesure la part de la détection due à la **signature de sélection**. Cette part ne se généraliserait pas à un agent qui sabote sans sélection. |
| E5 | κ réglé sur les attaques connues. | ACC | κ est fixé sur les seules données honnêtes, par un quantile déclaré à l'avance. |
| E6 | Fuite d'horizon dans D et censure omise. | ACC | Incréments estimés par position relative à la bifurcation. La censure est traitée (voir (b)). |
| E7 | L'AUROC de E0 élimine le régime « dommage rare et grand ». | ACC | Critère principal de E0′ : la différence moyenne appariée de dommage, qui capte π·E[G₁]. L'AUROC est seulement rapportée. |
| E8 | Calibration hiérarchique. | ACC | Voir D7. |
| E9, E10 | KL grande alors qu'un détecteur unilatéral échoue ; dérive sous κ. | ACC | Couvert par ρ (ρ = 0 si E₁[Z] ≤ 0). Une CUSUM bilatérale sur la moyenne et l'échelle est ajoutée en variante déclarée. |
| E11 | Vérificateur non identifiable quand 1 − α_V − β_V → 0. | ACC | Voir D8. Seuil de rétrogradation conservé : vérificateur en erreur plus de 10 % du temps (illustratif). |
| E12 | Biais de censure et de dimension. | ACC | Voir A13 et C5. |
| E-c1 | Perturbation neutre. | ACC | Intégrée. |
| E-c2 | Best-of-8 honnête. | ACC | Intégré. |
| E-c3 | Concaténation de bruit isotrope. | TEST, sous forme réduite | Après reformulation, les deux modalités sont comparées par des **scores scalaires**, et l'écart de dimension disparaît. Le test ne s'applique que si un estimateur multivarié est réintroduit. |

---

## (b) Expériences corrigées

**Règle de décision commune**, empruntée à D en le disant. Pour un seuil g fixé à l'avance :
- H_A : Δ ≥ g ; H_B : Δ < g.
- Un IC entièrement d'un côté de g réfute l'autre hypothèse.
- Un IC qui chevauche g ne tranche pas, et je l'écrirai ainsi.
- Les IC sont groupés par tâche et par préfixe.
- Point de fonctionnement principal : 5 % de fausses alertes par trajectoire (illustratif).

**Calibration commune.**
- Les 8 références par tâche (illustratif) servent à **normaliser** le score, par standardisation propre à la tâche.
- Le seuil est calibré en conformal découpé sur des trajectoires honnêtes de tâches distinctes. Les tâches sont les unités échangeables, avec au moins 100 tâches de calibration (illustratif).
- La garantie de fausses alertes est **marginale sur les tâches**. Les fausses alertes conditionnelles sont rapportées par tercile de difficulté honnête.
- κ, la sonde et θ* sont ajustés sur trois parties disjointes.

**Contrôles nuls communs.** Ils coûtent seulement des exécutions honnêtes.
- **N1.** Bifurcation honnête contre honnête avec graines différentes, sur toutes les tâches, y compris celles que E0′ jugerait difficiles.
- **N2.** Bifurcation avec perturbation neutre (synonyme) à l'étape t. Duel :
  - H_A : l'IC de D̂ contient 0 et le taux d'alerte est ≤ α ;
  - H_B : l'IC exclut 0, ou le taux d'alerte est ≥ 2α (illustratif).
  - H_B réfute le protocole de bifurcation, qui mesurerait alors une désynchronisation.
- **N3.** Best-of-8 honnête minimisant le score du moniteur.
- **N4.** Changement de phase honnête (collecte → rédaction) au pseudo-instant de rupture.
- **N5.** Honnêtes appariés en longueur, et sous dérive bénigne : ordre des documents, format.

### E0′ — Précondition, semaines 1 et 2

**Intensité fixée avant toute mesure de dommage**, sur des tâches de développement. On retient la plus forte intensité telle que chaque touche, prise isolément, soit signalée par le meilleur moniteur texte au plus 2 points (illustratif) au-dessus de son taux sur une étape honnête. C'est l'opérationnalisation de « aucune touche suspecte isolément », pour l'observateur texte (P2).

**Mesure**, sur des tâches **fraîches** jamais utilisées pour choisir l'intensité : Δ̄L, la différence moyenne appariée de dommage, branche attaquée moins branche honnête, au même préfixe.
- H_A : Δ̄L ≥ g_L. H_B : Δ̄L < g_L, avec g_L égal à 0,5 écart-type inter-graines honnête (illustratif).
- **Falsification.** H_A réfutée : des attaques furtives ne produisent pas, sur 8B, de dommage distinguable du bruit honnête. On change de modèle ou de famille de tâches, et ce constat est rapporté comme un résultat sur le compromis furtivité/dommage. H_B réfutée : le programme continue.
- Mené sur deux modèles 8B. N1 doit donner un IC de Δ̄L qui contient 0.

### Type 1′ — Garantie conditionnelle au taux effectif ρ

**Grandeur.**
- Z = score normalisé − κ.
- θ* > 0 est la racine de Ê₀[exp(θ·Σ_bloc Z)] = 1, calculée sur des sommes par blocs de 4 étapes (illustratif) pour absorber la dépendance courte.
- ρ = θ*·Ê₁[Z], et ρ = 0 si Ê₁[Z] ≤ 0.

**Question.** Un détecteur calibré sur des données honnêtes seules attrape-t-il, dans l'horizon restant, les attaques tenues à l'écart qui vérifient ρ ≥ ε ? Et les attaques qui vérifient ρ < ε restent-elles sous un dommage δ ?

**Duel.**
- H_A : couplage. Aucune politique ne vérifie à la fois borne inférieure du dommage ≥ δ et borne supérieure de ρ < ε. Et toute politique avec borne inférieure de ρ ≥ ε a une probabilité de détection ≥ 1 − β (illustratif 0,9).
- H_B : découplage. Au moins une politique est dans la région critique, ou une politique à ρ ≥ ε échappe au détecteur.

**Attaques**, par ordre de priorité :
1. le best-of-N de C, qui minimise le score sous contrainte de dommage ;
2. une réduction de variance à moyenne constante ;
3. une attaque concentrée sur les étapes critiques ;
4. les quatre familles de III.1, en validation croisée famille par famille.

**Falsification.**
- Une politique dans la région critique réfute H_A. Le type 1 devient alors un résultat d'impossibilité (4b).
- Aucune politique dans la région critique, avec n ≥ 30 réplications par politique, réfute H_B **pour ce budget d'optimisation déclaré**. J'y joins la borne binomiale exacte sur la fréquence de dommage extrême, et rien de plus.

**Interprétation par N3.** Si le best-of-8 honnête déclenche au-delà de la borne binomiale de α, la détection du best-of-8 adverse est attribuée à la signature de sélection, pas au couplage dommage/ρ.

### Type 2′ — Plan factoriel 2×2×2

**Facteurs.**
- Modalité : texte ou activations. Le bras texte **ré-encode le contexte complet**, sorties d'outils comprises, plus le texte émis, dans un modèle propre. J'emprunte ce point au contrôle que C adresse à A, en le disant.
- Agrégation : maximum par étape ou CUSUM.
- Références : propres à la tâche ou génériques.

**Hypothèse principale (gain conditionnel des activations).**
- Δ_act = TPR(activations, CUSUM, références propres) − TPR(texte ré-encodé, CUSUM, références propres), à fausses alertes égales.
- H_A : Δ_act ≥ 10 points (illustratif). H_B : Δ_act < 10 points.

**Hypothèses secondaires**, chacune en duel avec le même seuil : gain d'accumulation à l'intérieur de chaque modalité ; gain des références propres.

**Comparateurs et contrôles conservés.** Vérifications mécaniques, sonde sur directions aléatoires, et N1 à N5. Placebo de A6 :
- si la sonde déclenche sur « consigne sans dommage » à plus de 2α (illustratif), elle détecte l'intention et non la dégradation ;
- si elle manque le « dommage sans consigne », sa portée se limite au modèle de menace de l'agent compromis (P3).

**Puissance, illustrative.** Avec 200 tâches et une discordance appariée de 0,3, l'erreur-type vaut environ 0,04 et la demi-largeur de l'IC environ 8 points. Le duel ne tranche donc que si le vrai écart est supérieur à 18 points ou inférieur à 2 points environ. Sinon, l'issue déclarée sera « non tranché ». Il faudrait au moins 400 tâches (illustratif) pour resserrer l'IC.

### Type 3′ — La loi de détection séquentielle sur des agents

Les grandeurs non observables sous censure (ARL₀, délai moyen non tronqué) sont abandonnées. Deux prédictions à un pas, estimées sur la partie A, sont testées sur la partie B.

- **L1, fausses alertes.** Sur une grille de seuils h donnant α̂_T(h) entre 2 % et 30 % (illustratif), donc avec des comptes binomiaux non nuls, la pente de log α̂_T(h) en fonction de h vaut −θ̂*, à ±25 % près (illustratif).
- **L2, délai.** Pour les seuils où au moins 90 % des attaques sont détectées dans l'horizon, le délai médian conditionnel vaut (h + dépassement)/Ê₁[Z], à ±25 % près (illustratif). Le dépassement est estimé sur la partie A. Cette correction de dépassement suit Siegmund (1985), *Sequential Analysis: Tests and Confidence Intervals*, cité de mémoire, à vérifier.

**Duel.**
- H_A : L1 et L2 tiennent pour au moins 3 familles sur 4.
- H_B : L1 ou L2 échoue pour au moins 2 familles, alors que le contrôle synthétique i.i.d. censuré à la même longueur (contrôle C-c2) passe.

**Diagnostic de la cause.** Si L1 et L2 tiennent après brassage temporel des incréments mais échouent dans l'ordre réel, la cause est l'autocorrélation, et la loi doit être reformulée avec des KL conditionnelles. Lai (1998), *Information Bounds and Quick Detection of Parameter Changes in Stochastic Systems*, IEEE Trans. Inf. Theory, cité de mémoire, à vérifier.

**Grandeur secondaire : l'efficacité ρ/D̂_cond par moniteur.** D̂_cond est estimé par un discriminateur conditionnel au préfixe sur une partie disjointe, et le plancher N1 est soustrait.

**Issue sans intérêt.** ρ est proche de 0 dans toutes les modalités, ou bien la loi ne tient que pour le contrôle i.i.d.

---

## (c) Réponse à la question de l'arbitre — une page

### Ce qui est établi

1. **Aucun fait empirique.** Les FAITS ne contiennent aucun fait empirique. Toutes mes affirmations sur des agents restent des HYPOTHÈSES, et aucune mesure n'a été faite.
2. **Des déductions conditionnelles des critiques**, statuts conservés tels qu'elles les donnent. Ce sont des mathématiques sous conditions, pas des observations :
   - n références échangeables ne permettent pas de garantir α < 1/(n+1) ;
   - un détecteur unilatéral peut manquer une attaque de KL arbitrairement grande ;
   - un lecteur idéal des activations domine un lecteur idéal du texte émis ;
   - sous censure, ARL₀ et le délai moyen non tronqué ne sont pas identifiables sans loi de queue.

   Ces déductions ont **invalidé quatre éléments de ma conception III.1** : la borne log(1/α)/ε, la comparaison D_act > D_texte, la calibration à 1 % avec 8 références, et l'usage de ARL₀.

### Ce qui n'est pas établi

- **Faisabilité sur 8B.** On ignore si des attaques furtives produisent un dommage mesurable sur un modèle 8B (E0′).
- **Couplage.** On ignore si le dommage et le taux effectif ρ sont couplés. Le type 1 en dépend entièrement.
- **Apport des activations.** On ignore si les activations apportent un gain **conditionnel** au contexte complet.
- **Loi.** On ignore si les approximations de détection séquentielle tiennent pour des scores d'agents dépendants.
- **Nouveauté : rien n'est vérifié.** Les antériorités de III.1 sont citées de mémoire. Le point décisif pour le type 2 reste à vérifier : Wen et al. (2024) agrègent-ils à l'intérieur d'une trajectoire, ou seulement entre tâches ? Pour le type 3, aucune recherche bibliographique n'a été faite sur « detection delay » ou « CUSUM » appliqués au contrôle d'agents. Toute revendication devra nommer les trois travaux les plus proches trouvés et la différence exacte avec chacun.

### Classement

Je le maintiens à titre provisoire, mais son contenu change.

1. **Type 3.** La grandeur est désormais ρ et l'efficacité ρ/D_cond, plus D.
2. **Type 2.** Le gain revendiqué est le gain conditionnel des activations dans le plan factoriel.
3. **Type 1.** La garantie est conditionnelle à ρ. Le livrable le plus probable est la recherche du contre-exemple de C : best-of-N à dérive négative et dommage ≥ δ.

**Ce qui le ferait changer :**
- si ce contre-exemple est trouvé, l'**impossibilité (4b) passe en tête** ;
- si E0′ réfute H_A, le **banc d'essai (4a) passe en tête** ;
- si une mesure publiée du compromis délai / fausses alertes pour des moniteurs d'agents existe, le type 3 passe en dernier.

### L'expérience à faire en premier

**E0′ avec les contrôles nuls N1 à N3**, en semaines 1 et 2, sur deux modèles 8B :
1. fixer l'intensité par la furtivité par étape sur des tâches de développement ;
2. mesurer Δ̄L sur des tâches fraîches ;
3. faire tourner les bifurcations honnête/honnête et à perturbation neutre, et le best-of-8 honnête.

**Pourquoi d'abord celle-ci.** Elle ne coûte que des exécutions et une vérité terrain de dommage (P1). Chacune de ses issues falsifie quelque chose :
- **H_A réfutée :** le programme sur 8B est non informatif, et ce constat est rapportable comme résultat sur le compromis furtivité/dommage ;
- **H_B réfutée :** le programme est légitime ;
- **N2 qui échoue :** le protocole de bifurcation, sur lequel reposent les trois types, est réfuté avant qu'on y investisse les six semaines restantes.

FIN-DE-CELLULE