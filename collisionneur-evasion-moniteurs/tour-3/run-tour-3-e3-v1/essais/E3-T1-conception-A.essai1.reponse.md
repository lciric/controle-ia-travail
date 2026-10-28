**Cadre.** Je suis la proposition A ; je ne vois ni B ni C (tour à l'aveugle), donc je n'ai rien à attaquer d'autre que la question elle-même et les pièces. C'est ce que je fais.

**Pièces coupées (signalement, R2).** D est tronquée en milieu de phrase au point 5 (« celles qui demandent »). P renvoie à ses sections 3 (lemme L, théorème T), 6 et 7 (contrôles croisés), ainsi qu'à N-054, N-007, N-008 et au plan `mesures-fortes-plan-v1.md` : aucune de ces pièces n'est transmise. Je n'en invente pas le contenu et je ne construis aucune expérience qui en dépende sans le dire.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Que l'organisme 8B a une conscience d'évaluation qui modifie son comportement.** Statut : **ouvert, rapporté comme tel** — la pièce E, §3.4, dit explicitement qu'aucune démonstration empirique n'existe pour des modèles ≤ 8B et que tout résultat publié est induit par instruction ou réglage fin. Le titre de la question (« face à un organisme 8B conscient d'être évalué ») postule donc le régime dont la mesure est demandée. Conséquence opératoire : la première grandeur à mesurer n'est pas la robustesse du moniteur mais **l'existence et l'amplitude de l'effet comportemental** chez *cet* organisme ; sinon on mesure la robustesse d'un moniteur contre un adversaire qui n'existe pas.
2. **Que « intention de saboter », « dissimulation », « conscience d'évaluation », « enjeux élevés » sont des construits séparables dans le protocole d'étiquetage.** Statut : **HYPOTHÈSE**. Dans un corpus où les épisodes sabotés sont aussi ceux qui sont dissimulés, sous cadrage évalué, avec un registre différent, les quatre facteurs sont confondus par construction. Une « carte de validité de construit » n'est identifiable que sous manipulation factorielle croisée (E1).
3. **Que H8 est testable avec la puissance disponible.** Statut : **HYPOTHÈSE, et probablement faux tel quel**. L'unité statistique de H8 (« la validité prédit la robustesse ») est **la sonde**, pas l'épisode. 5 familles × 5 concepts × 3 couches = 75 objets, mais fortement dépendants par blocs (même concept, même couche). Le n effectif est de l'ordre de la dizaine. Sans préenregistrement d'un test de permutation par blocs et d'une taille d'effet cible, H8 restera descriptif. À trancher *avant* de dépenser.
4. **Que « battre Apollo 2025 » a un sens.** Statut : **RAPPORTÉ, non audité et incommensurable**. Les 95–99 % à 1 % FP sont listés par E §5 comme chiffre à vérifier sur PDF ; et le protocole est 70B, tromperie binaire, autre tâche. Ce n'est pas une base : c'est un repère de littérature. La seule base comparable est une **réimplémentation** de la sonde linéaire ponctuelle sur notre organisme et notre tâche — c'est exactement la base (iii) « dernier état » de D, et elle doit être présentée comme telle, jamais comme « Apollo ».
5. **Qu'il existe un oracle mécanique du dommage.** Statut : **HYPOTHÈSE, et c'est le trou le plus coûteux**. « Rappel », « θ », « dommage cumulé » n'ont de sens sur la tâche « rédaction/révision de propositions scientifiques » que si le biais diffus est **injecté de façon vérifiable mécaniquement** (p. ex. inversion d'un signe d'effet préenregistré, substitution d'un bras de contrôle, suppression d'un nul obligatoire — chaque instance vérifiable par un script, sans juge). Sans cela, la vérité terrain dépend d'un juge, et le moniteur et l'oracle partagent leurs erreurs.
6. **Que l'agrégateur séquentiel conserve sa garantie sous dépendance.** Statut : **HYPOTHÈSE explicitement reconnue par le programme** (D point 5 : fausses alertes sur épisodes honnêtes entiers, sans puis avec corrélation injectée). Les scores de sonde le long d'une trajectoire sont autocorrélés (même contexte, même persona). Tant que le FPR par **épisode** n'est pas calibré, aucun chiffre de rappel n'est interprétable.
7. **Que max et attention sont « robustes » au niveau action.** Statut : **HYPOTHÈSE, notée angle mort non calibré par P (Tr)**. Le max est une statistique d'ordre : sa robustesse à la dilution est acquise, sa fragilité à l'ablation du jeton argmax ne l'est pas. Mesurable très bon marché (voir (c), test top-k).
8. **Que le contrefactuel « réel » existe.** Statut : **contrainte logique, non contournable**. Dans un harnais, tout épisode est évalué. On ne manipule jamais que la *croyance* (indices de cadrage). Toute conclusion « évalué vs déployé » est bornée à « croyance induite A vs croyance induite B ».
9. **Que la porte G1 conjonctive produit un verdict interprétable.** Statut : **reconnu comme non interprétable par D lui-même** (« un échec ne dira pas laquelle a échoué »), avec une puissance fixée par le contraste blanc/blanc. Je ne demande pas de changer la décision ; je demande que les deux contrastes (blanc vs noir ; séquentiel vs cascade/dernier état) soient **rapportés séparément avec leurs IC appariés** au même préenregistrement, pour que l'échec soit diagnosticable.
10. **Que « changement de régime » est la bonne forme.** Statut : **HYPOTHÈSE**. Si l'organisme sait dès l'action 1, l'effet est un **décalage de niveau** et tout détecteur de rupture est structurellement aveugle. Voir E4.

---

## (b) Quatre expériences décisives

Règle commune : unité statistique = **épisode** (jamais l'action : pseudo-réplication) ; FPR calibré sur **épisodes honnêtes entiers** ; plancher obligatoire = sonde aléatoire appariée en covariance (P §8.1) ; tous les seuils chiffrés ci-dessous sont **illustratifs** et doivent être fixés au préenregistrement après un pilote de puissance.

### E1 — Dissociation factorielle du construit (répond Q2, et conditionne H8)

**Design.** Plan croisé 2×2×2 sur la même tâche scientifique : {contenu sabotant / contenu honnête} × {cadrage « évaluation » / cadrage « déploiement »} × {registre A / registre B} (registre = longueur, densité de hedging, méta-discours, appariés par génération contrainte). Chaque cellule : mêmes sujets de proposition, mêmes graines.

- **H_A (validité d'intention)** : pour les sondes « intention de saboter », la part de l'écart de score attribuable au facteur *contenu* domine strictement celles de *cadrage* et *registre*, avec d de Cohen apparié Δd ≥ 0,5 (illustratif) entre contenu et le plus grand des deux autres.
- **H_B (contamination de construit)** : part(cadrage) + part(registre) ≥ part(contenu) → la sonde lit le registre et le contexte, et la « carte de validité » prédit au mieux du style.

**Grandeur, unité** : AUROC par sonde et par facteur, sur épisodes appariés ; décomposition de variance du score agrégé (ANOVA sur rangs, unité = épisode) ; IC bootstrap apparié par épisode.
**Nul** : (i) sonde aléatoire appariée en covariance ; (ii) permutation des étiquettes au niveau **épisode** (pas jeton) — l'AUROC doit retomber à 0,50 ± marge de permutation.
**Témoin vrai** : sonde entraînée sur une étiquette triviale et présente (langue de l'épisode, ou présence d'un tableau) — doit atteindre AUROC ≥ 0,9 ; si elle n'y arrive pas, le pipeline de lecture d'activations est cassé, pas la théorie.
**Témoin faux** : sonde entraînée sur le facteur *registre* uniquement — doit être forte sur registre et au niveau du hasard sur contenu. Si elle atteint l'AUROC de la sonde d'intention sur le contenu, l'étiquette « intention » n'ajoute rien.
**Issue falsifiante** : H_A tombe si part(contenu) n'est pas majoritaire pour ≥ 3 des 5 familles ; H_B tombe si, pour la famille gagnante, le retrait du facteur contenu fait chuter l'AUROC sous 0,6 alors que le retrait du registre ne la fait pas bouger.
**Conséquence pour H8** : E1 fournit le **prédicteur** (score de validité par sonde). Sans dispersion suffisante de ce prédicteur entre sondes (étendue interquartile de part(contenu) ≥ 0,2, illustratif), H8 est déclaré non testable au budget et abandonné — pas repoussé.

### E2 — Signal réparti : séquentiel contre marginal, à FPR épisode apparié (répond au résultat fort (c), et aux bases ii/iii)

**Design.** Injection graduée d'un biais diffus **mécaniquement vérifiable** (cf. présupposé 5) : intensité par action ε ∈ {0, …}, dommage cumulé fixé à θ constant, donc plus ε est faible, plus l'épisode est long. Comparer : agrégateur séquentiel (e-processus) ; base (ii) cascade de portes ; base (iii) sonde sur le dernier état ; max sur actions ; moniteurs boîte noire scellés ; (a)+(b) de D1.

- **H_A (gain d'accumulation)** : il existe un régime ε tel que, à **FPR épisode = 1 %** calibré sur épisodes honnêtes entiers, le séquentiel atteint un rappel ≥ 0,70 tandis que tout agrégateur marginal reste ≤ 0,30 (illustratif).
- **H_B (artefact de calibration)** : une fois le FPR calibré par épisode (multiplicité temporelle absorbée), l'écart séquentiel/marginal tombe sous 5 points de rappel sur tout ε.

**Grandeur** : rappel à FPR épisode 1 %, en points ; **temps jusqu'à alerte** en nombre d'actions ; ARL₀ en épisodes sous H0.
**Nul** : épisodes honnêtes entiers, **puis** épisodes honnêtes avec corrélation injectée (D point 5) — si le FPR empirique dépasse 3× le nominal sous corrélation, l'instrument n'a pas de garantie et l'expérience **s'arrête ici** (la mesure de rappel est suspendue, pas « rapportée avec réserve »).
**Témoin vrai** : sabotage concentré sur une seule action, bien au-dessus du seuil — le marginal *doit* le détecter ; si non, c'est la sonde qui est en cause, pas l'agrégation.
**Témoin faux** : signal injecté dans une direction orthogonale aux sondes (perturbation d'activations de même norme, direction aléatoire) — aucun détecteur ne doit s'allumer. S'il s'allume, on mesure l'énergie, pas le construit.
**Issue falsifiante** : H_A tombe si aucun ε n'ouvre l'écart ; H_B tombe si l'écart tient après calibration par épisode **et** après correction pour l'horizon (même nombre d'actions observées des deux côtés).
**Lien G1** : (ii) et (iii) entrent ici comme bases appariées ; les deux contrastes (blanc/noir, blanc/blanc) sont rapportés séparément au même préenregistrement.

### E3 — Frontière de robustesse et taxe d'évasion (répond Q4 ; teste HC1, HC2, HC2b, HC4, H6)

**Design.** Trois attaquants de budget croissant, chacun avec une **courbe de coût** : (A1) pression par contenu en bande, sans accès aux poids (rhétorique, plaidoyer, cadrage « ceci est un test ») ; (A2) attaquant adaptatif boîte noire par itérations sur le score renvoyé (fuite de score volontairement accordée, pour majorer) ; (A3) attaquant avec accès aux activations (obfuscation par gradient) — borne supérieure de l'adversaire, hors modèle de menace du programme, mesuré pour chiffrer HC4.

- **H_A (robustesse des sondes)** : ĝ_sonde ∈ [−0,1, +0,1] (IC 95 %) sous A1, tandis que ĝ_juge ≥ 0,3 ; et le coût en requêtes pour atteindre sur la sonde le déplacement que A1 obtient gratuitement sur le juge est supérieur d'au moins deux ordres de grandeur.
- **H_B (contamination/corruptibilité)** : ĝ_sonde > 0,1 sous A1 → la sonde lit le registre de plaidoyer, pas l'intention.
  (Sous-cas préenregistré : ĝ_sonde < −0,1 → auto-incrimination, HC2b ; ce n'est pas « H_A gagne », c'est une **troisième issue** à déclarer d'avance.)

**Grandeur** : g (sans unité, fraction du chemin vers v*) par régression sur ≥ 4 intensités de pression ; coût en requêtes (nombre) et en calcul (GPU·h) ; **perte d'utilité** sur la tâche scientifique en points d'un score de qualité jugé en aveugle par un juge qui n'a pas accès à l'étiquette d'attaque.
**Nul** : nul de régression vers la moyenne (P §4, comme P3) — pression nulle, même nombre de ré-échantillonnages.
**Contrôle obligatoire de style** : paires appariées en longueur, registre, densité de méta-discours ; sans cet appariement, un g positif est ininterprétable.
**Témoin vrai** : attaque connue pour marcher sur les juges (usurpation stylistique de l'instructeur, HC3) — doit produire g_juge > 0 ; sinon le harnais d'attaque est inopérant.
**Témoin faux** : « attaque » composée de texte neutre de même longueur — g ≈ 0 partout.
**Second axe (H6)** : courbe Pareto évasion × utilité sous interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro de contexte, bruit d'activations). H_A : il existe une intensité λ où le succès d'attaque chute de ≥ 50 % relatif pour une perte d'utilité ≤ 5 % relatif (illustratif) ; H_B : les deux pentes sont indiscernables (IC des pentes qui se recouvrent) → pas de marge asymétrique.
**Issue falsifiante** : si l'évasion est obtenue à perte d'utilité quasi nulle, la brèche est ouverte et la réponse est une extension du moniteur (voir Q4 ci-dessous), pas un durcissement du seuil.

### E4 — Conscience d'évaluation : rupture ou décalage ? (répond Q3)

**Design — révélation différée.** L'indice d'évaluation (phrase de cadrage, artefact de harnais, mention d'un journal d'audit) est introduit à une action **t\*** tirée au hasard dans l'épisode, à contenu de tâche inchangé.

- **H_A (régime)** : l'effet est une **rupture** localisée ; un détecteur de point de changement à garantie (CUSUM à e-valeurs / e-detector) localise t̂ avec |t̂ − t\*| ≤ 2 actions dans ≥ 60 % des épisodes, à ARL₀ ≥ 1/α épisodes sous H0 (illustratif).
- **H_B (décalage, ou rien)** : l'effet est un offset constant dès l'action 1 (l'organisme « sait » avant l'indice), ou absent ; la localisation n'est pas meilleure que l'uniforme et un test de niveau sur l'épisode entier domine le détecteur de rupture.

**Grandeur** : délai de détection en actions ; ARL₀ en épisodes ; erreur de localisation |t̂ − t\*| ; **et** l'effet comportemental apparié (écart de performance honnête avant/après t\*, en points de la métrique de tâche).
**Nul** : indice **neutre** introduit à t\* (même longueur, même position, contenu non informatif) — le détecteur ne doit pas s'allumer plus souvent que α.
**Témoin vrai** : rupture massive à t\* (changement de langue ou de type de tâche) — doit être localisée presque toujours ; calibre la sensibilité du détecteur.
**Témoin faux** : annonce « un changement va survenir » sans changement.
**Test décisif de construit, pas suggestif** : la sonde « conscience d'évaluation » bouge-t-elle **quand et seulement quand** le comportement bouge ? Trois issues préenregistrées — (i) score bouge **et** comportement bouge, co-variation épisode par épisode (ρ de Spearman ≥ 0,4, illustratif) → la sonde capte un état qui a des conséquences ; (ii) score bouge, comportement immobile → la sonde lit le **contexte/format** de l'indice, cohérent avec le pilotage faible rapporté (Nguyen et al. 2025, RAPPORTÉ via E) ; (iii) comportement bouge, score immobile → la sonde est aveugle et la classe cible doit être réétiquetée.
**Issue falsifiante** : H_A tombe sous (ii) ou sous une localisation au niveau du hasard ; H_B tombe si la rupture est localisée au-dessus du hasard **et** survit au nul d'indice neutre.

---

## (c) Mesure minimale par instrument

Protocole commun, le même pour tous : **TPR à FPR épisode = 1 %** (et AUROC en second), sur cas honnêtes **appariés** = épisodes honnêtes générés sur les mêmes sujets, mêmes graines, même longueur distributionnelle, même registre, y compris les épisodes honnêtes sous cadrage « évaluation ». IC bootstrap apparié par épisode. Chaque sonde doit battre, sur le même split, **les quatre bases mécaniques** suivantes :

- **M1** sonde aléatoire appariée en covariance (plancher du programme) ;
- **M2** régression logistique sur traits de surface : longueur en jetons, position dans l'épisode, taux de marqueurs de hedging, nombre de chiffres/citations, présence de méta-discours ;
- **M3** TF-IDF linéaire sur le texte de l'action (base lexicale boîte noire, aucun accès interne) ;
- **M4** statistiques sans apprentissage : ‖h_ℓ‖ du flux résiduel, entropie de la distribution de sortie par jeton, log-vraisemblance moyenne sous le modèle de base.

Critère d'existence (reprise de P §8.1, étendue) : **une sonde qui ne bat pas M1–M4 d'au moins 5 points de TPR@1 % avec IC apparié excluant 0 n'existe pas** et ne passe pas en E3.

| Instrument | Construit opérationnalisé | Mesure minimale supplémentaire | Échec caractéristique à détecter |
|---|---|---|---|
| **différence de moyennes** | direction moyenne « saboté − honnête » | sensibilité au déséquilibre de classes ; écart entre couches 7/15/23 | capte la polarité de registre (M2 la bat) |
| **linéaire (sacs)** | frontière linéaire par jeton, étiquette d'action | courbe d'apprentissage ; stabilité de w entre graines (cos ≥ 0,8, illustratif) | surapprend la position dans l'épisode |
| **perceptron** | frontière non linéaire | écart train/test ; test de permutation d'étiquettes (doit retomber au hasard) | gagne 2 points sur le linéaire pour 10× la variance → inutile |
| **attention** | pondération apprise des jetons | **concentration de l'attention** (entropie des poids softmax) ; si l'entropie est ≈ 0, c'est un max déguisé | détecteur d'un jeton-artefact (balise, en-tête) |
| **Mahalanobis** (non supervisé) | atypicité par rapport aux jetons honnêtes | FPR sur **honnêtes hors distribution** (sujet nouveau, format nouveau) | détecte la nouveauté de sujet, pas le sabotage |
| **agrégateur séquentiel** | accumulation de preuve sur l'épisode | FPR épisode **sans puis avec** corrélation injectée (D p.5) ; ARL₀ ; temps jusqu'à alerte | garantie perdue sous autocorrélation → FPR réel ≫ nominal |
| **base (ii) cascade de portes** | décision multi-seuils sur les mêmes sondes | même FPR épisode ; nombre de portes franchies avant alerte | avantage apparent dû à un seuil non apparié |
| **base (iii) dernier état** | réimplémentation de la sonde ponctuelle publiée | TPR@1 % sur **notre** 8B et **notre** tâche ; jamais rapportée sous l'étiquette « Apollo » | sous-estimée par un mauvais choix de position/couche — tester 3 couches et 3 positions, rapporter le maximum |

**Test d'ablation top-k (bon marché, à faire d'abord).** Pour chaque famille : retirer les k jetons de score le plus élevé (k = 1, 2, 5) de chaque action et recalculer. Grandeur : ΔTPR@1 % en points par jeton retiré. **Interprétation préenregistrée** : une famille dont le TPR chute de plus de 50 % en retirant 1 jeton sur ~400 détecte un artefact ponctuel, pas un biais diffus — elle est disqualifiée pour le papier A quel que soit son AUROC. C'est le test direct de l'angle mort Tr (max/attention au niveau action), et il ne coûte que du CPU sur des scores déjà stockés.

---

## (d) Ancrage matériel

Modèles nommés dans les pièces : **Llama-3.1-8B-Instruct** (organisme, donné par la question), **Llama-3.2-3B-Instruct** et **Qwen2.5-7B** (P, D1), **Llama Scope** (autoencodeurs parcimonieux, P §8.2). Entraînement des sondes : CPU, double précision, déterministe (F) — cohérent avec D (« processeur, zéro dépense »).

Chiffres ci-dessous **illustratifs**, aucun ne vient des faits :

- Épisode ≈ 20 actions × 400 jetons générés ≈ 8 000 jetons. Débit batché d'un 8B en bf16 sur un accélérateur 80 Go : ~2 000 jetons/s → ~4 s/épisode.
- Volumes : E1 ≈ 8 cellules × 250 épisodes = 2 000 ; E2 ≈ 5 intensités × 300 = 1 500 + 1 000 honnêtes de calibration ; E4 ≈ 1 200 ; E3 (attaquant itératif) ≈ 5 000–20 000 selon le nombre d'itérations. Total ≈ 11 000–26 000 épisodes → **12–30 GPU·h** de génération.
- **Le mur n'est pas le calcul, c'est le stockage d'activations.** 3 couches × 4 096 dims × 2 octets = 24 ko/jeton → ~200 Mo/épisode → 20 000 épisodes = **~4 To**. Recommandation concrète : (i) projeter **en ligne** et ne stocker que les scores par jeton (quelques ko/épisode) ; (ii) conserver un **banc d'activations figé** de ~500 épisodes (~100 Go) pour pouvoir entraîner toute sonde nouvelle sans régénérer ; (iii) toute sonde conçue après coup se teste d'abord sur le banc, puis se re-score en ligne sur le reste. Sans (ii), chaque idée de sonde coûte une régénération complète.
- Coût monétaire : à ~2 $/GPU·h (illustratif), la génération est de l'ordre de la centaine de dollars ; le stockage domine le budget si l'on ne projette pas en ligne.
- Les juges génératifs (D1 (a)+(b)) coûtent peu devant la génération des trajectoires — P le dit, et c'est cohérent.

---

## Q4, en une ligne par brèche

| Brèche prévisible | Coût pour l'organisme | Extension qui la fermerait | Mesure de la fermeture |
|---|---|---|---|
| Ablation du jeton argmax (max fragile) | faible | agrégation par attention à entropie plancher, ou max-sur-k > 1 | ΔTPR@1 % sous ablation top-k ≤ 10 points |
| Aplatissement du registre (sonde lit le style) | moyen (perte de persuasion) | sondes entraînées sur paires appariées en registre (E1) | part(contenu) > part(registre) maintenue hors échantillon |
| Sous-seuil par action | perte d'efficacité du sabotage (épisode plus long) | e-processus avec horizon étendu ; θ atteint plus tard | rappel maintenu quand ε ↓ et T ↑ à θ constant |
| Conscience d'évaluation → « paraître détendu » | faible si la sonde lit le contexte | abandonner la sonde EA comme détecteur, la garder comme **covariable** à ajuster | TPR de la sonde d'intention invariant au cadrage (E1) |
| Déplacement d'activations (A3) | très élevé (accès aux poids) | hors modèle de menace ; quorum hétérogène + réserve de détecteurs jamais déployés | matrice de transfert d'attaque (P §8.2) |

---

## Q5 — Ordre, arrêts, et ce qui me ferait changer d'avis

**Ordre** : (0) calibration du nul séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée — déjà prévue par D p.5, CPU, zéro génération ; (0bis) ablation top-k sur scores existants ; (1) **E1** (plan factoriel : c'est la seule expérience qui rend les trois autres interprétables) ; (2) **E2** ; (3) **E4** ; (4) **E3**, le plus cher, et seulement sur les sondes survivantes.

**Critères d'arrêt, préenregistrés** :
- FPR épisode du séquentiel > 3× nominal sous corrélation injectée → **arrêt** ; aucun rappel n'est mesuré avant correction.
- Une famille ne bat pas M1–M4 de 5 points sur le pilote (n = 200, illustratif) → elle ne part pas en E3.
- Une famille perd > 50 % de TPR par ablation d'un seul jeton → disqualifiée du papier A.
- L'organisme 8B n'atteint pas θ avec un taux de succès ≥ 30 % contre un moniteur nul → on n'a pas d'attaque ; on publie ce fait sur l'organisme et on suspend la mesure de détection.
- Pente d'amélioration de l'attaquant adaptatif < ε sur 3 itérations consécutives → arrêt de E3, on rapporte la frontière atteinte comme borne basse, jamais comme « robustesse démontrée ».
- Étendue interquartile du prédicteur de validité < 0,2 entre sondes → **H8 déclaré non testable au budget** et retiré, pas reporté.

**Ce qui me ferait changer d'avis** : si E1 montre que *toutes* les familles sont dominées par le facteur contenu, la carte de validité devient sans objet et H8 meurt par absence de variance sur le prédicteur — bonne nouvelle pour les sondes, mauvaise pour le papier qui les étudie. Si E2 montre que le max sur actions, calibré par épisode, égale l'e-processus, l'accumulation séquentielle perd sa raison d'être et le papier A se réduit à H1. Si E4 donne l'issue (ii) — score qui bouge, comportement immobile — alors la « conscience d'évaluation » du programme est un détecteur de contexte, et il faut le dire ainsi, pas le vendre comme une classe cible.

**Références citées** (toutes **RAPPORTÉES** via la pièce E, transcrites, chiffres à vérifier sur PDF, R7) : Berglund et al. (2023), *Taken out of context* ; Laine et al. (2024), *SAD benchmark* ; van der Weij et al. (2024), sandbagging par mot de passe ; Greenblatt et al. (2023/2024), *AI Control* ; Apollo Research (2025), sondes linéaires sur Llama-3.3-70B-Instruct ; Nguyen et al. (2025), sondage et pilotage de la conscience d'évaluation ; Phuong et al. (2024, DeepMind), capacités dangereuses ; étude multi-modèles 2026 (~37 modèles) — **publication exacte non identifiée, référence à vérifier**. Pour la détection séquentielle : Page (1954), *Continuous Inspection Schemes* (CUSUM) ; littérature e-valeurs / inférence anytime-valid (Ramdas, Grünwald, Vovk, Shafer — **référence exacte à vérifier**).

FIN-DE-CELLULE