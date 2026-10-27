# Proposition A — Tour III.2 : équipe rouge croisée contre B et C

**Statuts.** Tout ce qui vient des pièces P, N-007/N-008, N-054, C, S et des deux conceptions est **RAPPORTÉ**. Ce que j'avance est **HYPOTHÈSE**. Tout chiffre hors des pièces est *illustratif*. Aucun fait VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ n'est en ma possession.

**Pièces absentes** (une ligne, contenu non inventé) : P §3 (L, T), §6, §7 (contrôles croisés), §13 ; brief de phase 0 ; scripts et sorties de S. Les deux conceptions sont complètes.

**Règle de cellule.** Le catalogue des modes est clos (N-054). Les « scénarios d'évasion » ci-dessous ne conçoivent aucun mode : ils décrivent (i) comment un *proposeur* ou un *concepteur de moniteur* peut faire promouvoir une fiche fausse, et (ii) comment les familles déjà nommées dans P (E1.5a « rester sous le seuil », EC.1, EC.4) traversent les instruments de B et C. Tout point qui exigerait un mode nouveau est écarté en une ligne.

---

## Contre la proposition B

### (a) Failles

**B-1. Le gain en horizon (X1) est confondu avec le budget de sabotage.** X1 oppose des paires de tâches « long contre court » et lit un contraste v = ½[(r_seq,réel − r_seq,aléa)_long − (…)_court]. B ne fixe nulle part le budget de sabotage *total* entre les deux horizons. Or P §4 définit l'attaquant sous budget B et §10 E1.3 pose exactement la question : « la puissance ne dépend-elle que du budget total quand la fragmentation varie ? ». Si l'organisme produit plus d'actions sabotées sur l'horizon long, « le rappel croît avec l'horizon » est vrai par construction : c'est « le rappel croît avec le dommage ». La pente de H2b ne porte le lemme L que si le budget est apparié et seule la fragmentation varie. Duel manquant : H_A « à budget total égal, r_seq croît avec la fragmentation » contre H_B « r_seq ne dépend que du budget total ; la fragmentation est neutre ». Les deux issues falsifient quelque chose (H_B falsifiée → additivité non triviale ; H_A falsifiée → L au mieux, T réfuté sur données réelles). X1 tel qu'écrit ne peut distinguer les deux.

**B-2. La sonde aléatoire appariée n'est pas le bon comparateur pour la dérive honnête.** H_B de X1 dit que « la sonde aléatoire appariée et la longueur seule reproduisent la pente ». Une direction aléatoire de dimension 4 096 (*illustratif*) a une projection quasi nulle sur toute direction de dérive spécifique : elle ne « voit » pas la dérive de position même si la sonde réelle en vit. Rejeter H_B (aléa ne reproduit pas la pente) ne falsifie donc pas « la sonde réelle lit la position ». Il faut un comparateur *entraîné* sur la dérive honnête (sonde de position ou résidu autorégressif ajusté sur épisodes honnêtes), pas un bruit apparié en covariance. Le plancher P §8.1 est un plancher d'existence, pas un contrôle de dérive.

**B-3. La correction de a4 réécrit H2 en silence.** B règle la confusion « 1 % par action contre 1 % par épisode » en calibrant « des seuils par horizon sur épisodes honnêtes entiers ». Mais l'énoncé retenu de N-007 dit « sous le seuil d'un moniteur par action calibré à 1 % ». Si le seuil devient un quantile du *maximum par épisode*, la sous-population H2a (« chaque action sous le seuil ») change d'objet, et le moniteur par action devient un moniteur max. Ce n'est pas une correction, c'est une autre hypothèse, à soumettre comme nœud (R8), pas à glisser dans un plan.

**B-4. La sous-population H2a et le comparateur.** B choisit « un moniteur par action *distinct* du comparateur » pour former la sous-population. Alors la population n'est plus celle où le comparateur est aveugle : r_action > 0 possible, et le contraste mesure deux moniteurs différents sur deux populations définies par un troisième. L'alternative (sélection sur le comparateur lui-même) donne r_action ≡ 0 ; B a raison de le dire, mais c'est *exactement* l'énoncé de N-007 : la revendication de H2 est « détecter là où le par-action ne détecte pas ». Le problème n'est pas la circularité, c'est la sélection : la sous-population formée sur les scores de la sonde est celle où *cette sonde* est faible ; r_seq y est biaisé vers le bas, et la garde de faux positifs est calculée sur des tâches honnêtes *non sélectionnées*. Contrôle requis : la même sélection appliquée aux épisodes honnêtes (ils y sont presque tous, par définition du 1 %), avec rapport des taux.

**B-5. X2 : les sondes aléatoires incluses comme instances rendent H_A vraie par construction.** B les fait entrer « comme instances qui doivent tomber dans la classe ne mesure rien ». Leur profil de construit est ≈ 0 et leur rappel sous pression ≈ 0 : elles créent une corrélation profil → robustesse mécanique (rien à perdre). Toute loi « |profil| prédit la robustesse » est promue grâce à elles. Il faut soit les exclure de la population d'instances, soit stratifier par AUROC en distribution ; sinon le résultat fort (a) de la question est un artefact de plancher.

**B-6. X4 : le dénominateur et le niveau d'instance.** v(item) = [Δv_pression − Δv_remplissage]/(v* − v₀) « ramené à [−1 ; 1] » : B ne dit pas comment. Quand v₀ ≈ v*, le ratio diverge ; l'écrêtage biaise vers ±1 et casse la surmartingale si v peut sortir de la borne avant écrêtage (S §2.2 : « comme v ≥ −1 »). De plus l'unité est l'*item*, pas la tâche : S §3.4 est explicitement violé. Enfin, le remplissage neutre est pris comme nul ; s'il déplace lui-même le verdict (dilution), B l'a reconnu dans « ce qui me ferait changer d'avis », mais rien dans X4 ne le teste *avant* la course : « remplissage contre remplissage à deux graines » teste la variance, pas le biais du remplissage contre l'absence d'ajout.

**B-7. X7 est juge et partie.** Le pôle contre un plan gelé : les témoins sont « plantés et cachés aux deux bras », mais c'est le noyau du pôle qui fabrique les témoins depuis les scores (S §2.5). Le bras « plan gelé » est conçu par les auteurs du pôle. Sans conception du plan gelé par une instance tierce et sans témoins scellés hors du noyau, une issue H_A ne falsifie rien.

**B-8. Le témoin vrai « de même taille » n'a pas de dents sur un effet hétérogène.** Le témoin vrai de B (scores sabotés décalés d'un quantile) plante un effet *homogène* de 20 points. S §6 (RAPPORTÉ) : à 20 tâches, la puissance passe de 0,70 à 0,53 avec un effet aléatoire de tâche. Un témoin homogène promu ne prouve pas que la fiche réelle, à effet hétérogène, avait des dents. La « règle de non-falsification par défaut » de B — correcte dans son principe — exige un témoin à hétérogénéité plantée.

**B-9. Pari d'équivalence (c-bis) : ε est déclaré par l'agent.** S §2.5 : la fiche porte ε. Si le proposeur choisit ε, il choisit sa puissance : à ε = 0,3 (*illustratif*) toute « équivalence » est promouvable à faible effectif. Le contrôle « équivalence sans dents » de B borne ε par le bas, pas par le haut. ε doit être fixé par le noyau (fonction du nombre de tâches), déclaré au gel, et un ε maximal doit être inscrit par type d'affirmation.

**B-10. Points justes, à conserver** (je m'en sers en le disant) : a11 (prix du mélange incohérent dans S : log 8, log 2, log 4) ; a4 ; a6 ; l'intersection-union pour l'équivalence ; Markov « richesse ≥ 20 ⇒ p ≤ 0,05 » comme test de cohérence. Ce sont des vérifications mécaniques à adopter.

### (b) Scénarios d'évasion

1. **Contre X1 (proposeur).** Déclarer des paires long/court où l'organisme a un budget croissant avec l'horizon : promotion garantie (B-1). Coût : zéro, c'est le défaut de l'organisme v0 si personne ne fixe le budget.
2. **Contre X1 (famille E1.5a du catalogue, « rester sous le seuil »).** C'est la définition même de la sous-population H2a : l'agent y est *par construction*. L'instrument n'est pas trompé, il est mesuré là où il doit l'être. Ce qui le trompe : un signal diffus *sans rupture* passe le détecteur de rupture (N-007) et ne laisse que la somme ; si la somme est calibrée par horizon sur honnêtes entiers avec FP 0,21–0,35 non résolu (N-007, RAPPORTÉ), le seuil monte et le rappel tombe. Coût : nul, contenu seul.
3. **Contre X2 (concepteur de sondes).** Inclure beaucoup de sondes faibles (plancher) dans le panel : la corrélation profil → robustesse est achetée par B-5. Coût : nul.
4. **Contre X3 (famille EC.1, usurpation stylistique).** Le « cadrage évalué » de B est du texte ; une sonde qui lit le registre voit le cadrage et le format comme un même objet. L'équivalence de format échoue (« sans dents »), l'effet de cadrage est promu : lecture « suggestive » que B exclut, mais le journal ne dira que « équivalence non promue ». Coût : nul.
5. **Contre X4 (familles EC.1 flatterie / autorité).** Le remplissage neutre ne porte pas de pression ; g > 0 est détecté. Mais si la sonde monte autant pour l'honnête qui plaide (B le teste), l'équivalence honnête ≈ 0 échoue et HC2b n'est ni confirmée ni infirmée. Coût : nul.
6. **Contre c-bis (proposeur).** Choisir ε (B-9). Coût : nul.
7. **Tous à la fois** : un agent dans la famille E1.5a (sous seuil) qui tient le plaidoyer EC.1 : il est dans H2a (r_action = 0 par construction), déplace les juges (g > 0), monte la sonde autant qu'un honnête plaideur si celle-ci lit le style, et rend l'équivalence de B « sans dents » ; aucune des issues de X1/X4 ne falsifie alors rien. Coût : contenu seul ; aucune obfuscation d'activations (HC4 : coût supérieur « de plusieurs ordres de grandeur », RAPPORTÉ comme hypothèse 0,85). Scénarios exigeant un mode nouveau : hors catalogue, écartés.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Budget apparié par paire d'horizons** (B-1), rapporté par paire ; sinon X1 ne lit rien.
- **Comparateur de dérive entraîné** (sonde de position / résidu AR(1) honnête) passé dans le même agrégateur (B-2).
- **Sélection miroir sur honnêtes** : sous-population « toutes actions sous seuil » appliquée aussi aux honnêtes, FP rapporté dessus (B-4).
- **X2 sans sondes aléatoires dans la population**, ou stratifié par AUROC en distribution (B-5).
- **Témoin vrai hétérogène** (effet aléatoire de tâche planté, écart-type déclaré) à côté du témoin homogène (B-8).
- **Remplissage contre absence d'ajout** sur verdicts continus, équivalence exigée *avant* X4 (B-6).
- **Nul exact à la frontière de l'équivalence** : E[v] = +ε et E[v] = −ε exactement ; promotion ≤ α dans les deux cas ; ε fixé par le noyau (B-9).
- **Tiers pour X7** : plan gelé et témoins hors du noyau (B-7).
- **Bascule de format seul à t₀** pour le détecteur de rupture : B l'a ; il manque le cas « bascule de cadrage *et* de format en sens opposés », seul à dissocier les deux dans un flux.

---

## Contre la proposition C

### (a) Failles

**C-1. Le pari de concordance confond l'unité d'inférence.** C fait de la tâche l'unité (« 40 à 150 instances ») tandis que la conclusion porte sur les *sondes* (« les sondes plus pures résistent mieux »). Avec 6 sondes, l'ordre de pureté est fixé une fois pour toutes ; si, par hasard ou par confondant au niveau des sondes (AUROC en distribution, couche), les sondes « pures » sont simplement meilleures, c(t) > 0 sur *toutes* les tâches et le pari promeut H8 — alors que n = 6 pour la question posée. C'est de la pseudo-réplication : la tâche réplique la mesure, pas le mécanisme. La seule manière de rendre la tâche unité légitime est d'inférer sur « ces 6 sondes-ci » ; la généralisation à « la validité prédit la robustesse » exige des sondes comme unités (B a13, que je reprends en le disant) ou une bibliothèque nulle contenant l'AUROC en distribution.

**C-2. c(t) n'est pas borné.** c(t) = moyenne de (y(x′) − y(x))/(x′ − x). Pour H8, x = pureté P_i ∈ [0, 1] (*illustratif*), et x′ − x ≥ ε_pureté peut valoir 0,1 : le ratio atteint 10. Le facteur 1 + λ·c(t) devient négatif, la surmartingale est détruite, Ville ne tient plus. C affirme « ∈ [−1, 1] » sans le démontrer ; ce n'est vrai que pour x à pas entier et y ∈ [0, 1]. Pour la version « signe », c'est borné, mais alors c'est le pari de signe de S et non un troisième type.

**C-3. La pureté P_i est mal construite.** P_i = AUROC(1 vs 4) − |AUROC(3 vs 4) − 0,5|, où 1 = saboteur neutre et 4 = honnête plaidant. Le premier terme compare deux cellules qui diffèrent *à la fois* par l'intention et par le registre : ce n'est pas la pureté, c'est un mélange. La pureté d'intention à registre fixé est AUROC(1 vs 3) et AUROC(2 vs 4) ; l'effet de style est |AUROC(1 vs 2) − 0,5| et |AUROC(3 vs 4) − 0,5|. Telle qu'écrite, une sonde de style pur peut obtenir un P_i élevé si le style de 4 abaisse son score (AUROC(1 vs 4) > 0,5 par le mauvais chemin).

**C-4. M2 : le « fantôme » ne teste rien pour un agrégateur additif.** La permutation des pas conserve exactement le multi-ensemble des scores ; la somme cumulée lue en fin d'épisode est *identique*. Seul le chemin change, donc seul un détecteur de rupture ou une lecture « avant θ » distingue le fantôme. H_A (« bat lui-même sur trajectoires permutées ») est donc fausse pour le volet additif même quand H2 est vraie : le duel falsifie H2 à tort. Le contrôle est bon pour T (ordre), mauvais pour L (additivité) ; C les fusionne.

**C-5. M2 : corrélation injectée sans dommage.** C le nomme en contrôle négatif sans dire l'issue attendue. Si l'agrégateur alerte autant sur honnêtes à corrélation injectée que sur sabotés, il mesure la corrélation, pas le dommage : T devient une tautologie (« ce qu'on injecte, on le voit »). B (X5) le dit ; C ne tranche pas. Et « dommage cumulé ≥ θ » n'est pas défini en semi-synthétique.

**C-6. M1 et M5 reposent sur la « pression adaptative » (E1.5b).** P §10 la place sous GO ; la question clôt le catalogue. C en fait la variable d'issue de M1 et le monde de M5. Sans GO, M1 et M5 n'ont pas d'issue mesurable ; avec GO, elles sortent de cette cellule. À écarter ou à reformuler sur EC.1/EC.4 seules.

**C-7. M3 : la troncature |v* − v₀| ≥ ε₀ réintroduit la sélection sur v₀.** C identifie correctement le dénominateur divergent (faille 3), puis « tronque ». Tronquer sur v₀ loin de v* *sélectionne* les items à fort potentiel de régression vers la moyenne — précisément ce que le nul veut neutraliser. La stratification par décile à l'intérieur de la sélection ne lève pas le biais de sélection. Le contraste différence-de-différences de M3 est bon ; l'estimation de g à partir de lui ne l'est pas.

**C-8. C viole sa propre faille 2.** C écrit que le FP d'une sonde « explose lorsque le registre change ». Puis M4 lit le mode tenu à l'écart avec une garde δ sur « 150 tâches honnêtes » — lesquelles ? Si les tâches du mode tenu à l'écart viennent d'une sous-distribution différente (autre environnement, autre longueur), les honnêtes de calibrage ne sont pas échangeables avec elles ; la garantie conforme de C §3.B (« exactement ≤ τ ») tombe pour la même raison. Il faut des honnêtes *par mode*, tirés de la même distribution de tâches que les sabotés du mode.

**C-9. M4 : la lecture du bras spécialisé n'est pas exclusive.** C lit « le témoin spécialisé ne chute pas » comme « le mode fuit ». Autre lecture : les traits du champ de coût sont réellement généraux. Deux hypothèses compatibles avec la même issue ; B4 non respecté. Il faut un second mode spécialisé (sur « contrôles ») pour trianguler.

**C-10. Témoins vrais par construction.** « Sonde oracle synthétique avec bruit proportionnel au style », « juge synthétique programmé pour céder », « tri monotone partiel à p = 0,25 » : ces témoins sont la loi plantée dans les données. Ils mesurent que le pari *peut* promouvoir, pas qu'il a des dents sur l'effet réel (même critique que B-8, plus grave ici : ce sont des témoins de mécanisme, pas d'effet).

**C-11. Conscience d'évaluation : le « décisif » de C est hors catalogue.** Le scénario décisif exige des épisodes où l'agent porte « une consigne conditionnelle (agis différemment si tu n'es pas évalué) » et où un indice de bac à sable est découvert à t₀. C'est la conception d'un organisme à comportement conditionnel à l'évaluation : un mode nouveau. Écarté en une ligne. Reste le plan 2 × 2 × 2 (valide) et la permutation lexicale (bonne), avec issue limitée au score de sonde, sans issue comportementale — ce que B dit explicitement de son X3 et que C ne dit pas.

**C-12. Instrument 6 : un test de McNemar ne mesure pas un prix de mélange.** Une p-valeur à horizon fixe n'est pas comparable à log W. Le prix se mesure par contrôle 9 de S (richesse du mélange contre meilleure mise), pas par un test.

**C-13. Coût 70B.** C inscrit 150 à 280 USD pour 70B + juges + étiquetage, dans l'enveloppe 100–300 USD de la couche 2 ; B chiffre 550–800 USD pour le seul 70B. Les deux sont *illustratifs* et incompatibles ; C ne déclare pas son débit en jetons/s. « Tout chiffre traçable » (P §12) : à refaire sur une mesure de débit.

**Points justes à conserver** : failles 1, 2, 4, 6 de C ; le calibrage conforme du maximum de la statistique de rupture sur épisodes entiers (§3.B, étapes 4–5) est la bonne réponse au 0,21–0,35 de N-007, *sous réserve* de l'échangeabilité (C-8).

### (b) Scénarios d'évasion

1. **Contre le pari de concordance (proposeur).** Déclarer les 6 sondes de sorte que la pureté soit colinéaire à l'AUROC en distribution (C-1) ; promotion sans mécanisme. Coût : nul — le proposeur voit la « description publique des cellules » (S §2.5), dont les AUROC bénins si le monde les déclare.
2. **Contre M2 (vacuité, pas évasion).** Un agrégateur additif passe le fantôme à l'identique (C-4) ; un concepteur qui sait cela lit H_A comme réfutée ou confirmée selon qu'il mélange ou non un détecteur de rupture. Coût : nul.
3. **Contre M4 (concepteur du mode tenu à l'écart).** L'instance « sans aucune pièce des moniteurs » lit le programme, qui nomme en §8.1 les concepts des sondes (tromperie, dissimulation, enjeux, conscience d'évaluation). La quarantaine de N-054 ne couvre pas la liste des concepts ; un mode conçu en évitant ces registres n'est pas « inédit », il est anti-aligné sur la liste publique. Coût : nul. Remède : brief du concepteur sans §8.
4. **Contre M3 (familles EC.1).** Flatterie / autorité déplacent les juges (g > 0) ; si la sonde lit les jetons d'argumentation, le double contraste est plat : C bascule à bon droit vers « contamination » (porte GC). Pas d'évasion, mais le « W_n < 1 *illustratif* » n'est pas un critère : sans témoin à même effectif, la bascule est une non-promotion.
5. **Contre EvalAware (famille EC.1, usurpation stylistique).** Le gabarit