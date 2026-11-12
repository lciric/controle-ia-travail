# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces reçues.** Quatre pièces (B, C, D, E), toutes closes par la ligne FIN-DE-CELLULE ; aucune coupure visible. La pièce D commence par « ## (a) » sans titre de proposition ; je la traite comme complète. Ma propre pièce de III.1 n'est pas transmise ici ; je ne m'y réfère pas.

**Conventions.** Les statuts des faits sont ceux du fichier FAITS. Tout nombre que je dérive porte la mention « calcul » (dérivé de faits RAPPORTÉS) ou « illustratif ». Un calcul utilisé plusieurs fois : au seuil log e ≥ 6,09 sur 200 tirages (RAPPORTÉ), le gain moyen de log-vraisemblance contre la meilleure loi du nul doit être de l'ordre de 6,09/200 ≈ 0,03 nat par épisode, à variance près (calcul). C'est la frontière de puissance du juge ; plusieurs métriques ci-dessous s'y heurtent.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Exp. 1 confond monde et opportunité.** Comparer S-V1 (2 traits) à un monde « ≥ 5 traits, ≥ 2 interactions » change simultanément le nombre de traits listés dans la description publique, le gain total disponible et la loi de départ K1. Si le monde riche contient ≥ 3 effets séparément détectables et que les proposeurs énumèrent simplement les traits publics un à un, « ≥ 3 clusters » est obtenu par construction : la métrique mesure l'offre du monde, pas une propriété des proposeurs. Les hypothèses ne sont pas exhaustives : l'issue « 2 clusters » ne falsifie rien.
2. **Métrique sur les lois promues.** Le nombre de clusters est compté parmi les promues ; la promotion dépend de la distance de la loi à l'enveloppe du nul v8, pas de sa distance aux autres fiches. Deux fiches prédictivement distinctes mais toutes deux proches d'une recombinaison du nul disparaissent du compte. La mesure de diversité hérite ainsi de la puissance du juge sans la séparer.
3. **Contrôle négatif d'Exp. 1 inexploitable.** « K1-riche couvre tous les traits ⇒ aucune promotion, sinon le juge fuit » : couvrir tous les traits n'est pas être la loi vraie. Une loi qui corrige les coefficients de K1-riche apporte une information hors du nul (qui ne contient que K1-riche et ses recombinaisons) et sera promue légitimement. La conclusion « le juge fuit » serait fausse par construction.
4. **Exp. 2 : fuite entre choix du représentant et jugement.** Le représentant est « la fiche à la plus grande e-valeur » du cluster. Sélectionner le maximum de k e-valeurs sur les mêmes 200 tirages puis rapporter cette e-valeur comme si elle était celle d'un test unique détruit la propriété E[e] ≤ 1 sous le nul. Il faut soit choisir le représentant avant les données (C, D et E le font), soit prendre la moyenne des e-valeurs du cluster, qui reste une e-valeur. En l'état, le regroupement affaiblit la garde qu'il prétend préserver.
5. **Exp. 2 : rejouer les proposeurs est un confondant inutile.** Pour G1, le regroupement est une transformation a posteriori des mêmes réponses ; rejouer avec « même seed API si disponible » ajoute la variance des proposeurs à la comparaison. Pour G2 le rejeu est nécessaire (l'archive diffère), mais alors l'appariement « même tirage » est impossible et la pièce ne le dit pas.
6. **Exp. 3 : la classe hors nul n'est pas détectable par l'oracle.** La pièce propose une « détection a posteriori par l'oracle » des recombinaisons par morceaux. L'appartenance à la classe non couverte est une propriété syntaxique de la fiche relative à l'archive, pas une propriété de la loi du monde ; l'oracle n'y donne pas accès.
7. **Exp. 4 confond trois facteurs** : nombre d'appels, plafond de fiches par appel (6 contre 2) et la consigne qui le demande. La règle « > baseline sur ≥ 4 graines sur 5 » a, sous absence d'effet et sans ex æquo, une probabilité 6/32 ≈ 0,19 (calcul) : un critère à presque un sur cinq de faux positif.
8. **Exp. 5 : calibration vraie ou fausse par construction.** Les « lois adversariales (constat différent, prédictions proches) » sont construites par l'oracle à une distance que personne ne fixe : construites sous 0,05 elles font échouer H_A, au-dessus elles la confirment. Sans distribution préenregistrée des distances des cas, le test ne teste que la main qui a construit les cas.
9. **Coût unitaire.** Le passage de « 4 appels ≈ 0,17 USD » à « ~0,04 USD/appel » divise 1,99 par 46 appels dont 42 ne sont pas des appels de proposeurs ; les deux chiffres cités sont incompatibles entre eux. Marqués illustratifs, mais la dérivation est fausse.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **d_L1 moyenne.** Si deux lois f, g ne diffèrent que sur une région A de l'espace des traits de masse μ(A) = ε sous la loi des traits, alors d_L1(f,g) ≤ ε (la variation totale par point est bornée par 1). Dès que ε < 0,05, elles sont déclarées doublons quelle que soit l'ampleur de leur désaccord sur A. C'est exactement le régime « effets de tailles variées, sous-populations » visé par le directeur.
- **Linkage non spécifié.** Avec single linkage, une chaîne de lois espacées de 0,04 forme un seul cluster ; avec complete linkage, plusieurs. Le « nombre de clusters » n'est pas jugeable tant que la méthode n'est pas gelée.
- **Puissance du juge.** Si la divergence par épisode entre la loi vraie et la meilleure loi du nul est inférieure à ≈ 0,03 nat (calcul), rien n'est promu et le compte de clusters vaut 0 pour toute configuration : la métrique mesure la puissance, pas la diversité.
- **Exp. 3, taux de faux positifs oracle.** En v67, 0 fausse loi selon l'oracle parmi les promues (RAPPORTÉ). Le taux de base est ≈ 0 ; l'estimateur de « baseline + 0,05 » sur ≈ 60 fiches (5 graines × 12, illustratif) bascule sur 3 fiches. Et si la consigne ne pousse pas vers la classe hors nul, la différence est identiquement nulle : le test ne détecte que la brèche, qui dépend de la forme des fiches, pas de la consigne.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Pilote A/A sur les proposeurs** (N-045) : aucune répétition à l'identique pour estimer la variance du nombre de clusters ; sans elle les seuils « ≥ 3 contre ≤ 1 » n'ont pas d'échelle.
- **Monde apparié à traits leurres** : même nombre de traits publics que le monde riche, un seul effet vrai. Sans lui, Exp. 1 ne sépare pas « plus d'effets » de « plus de traits à lister ».
- **Baseline grammaticale aléatoire** pour le nombre de clusters (B la cite en C3 mais ne l'intègre pas aux expériences) : des lois tirées au hasard dans la grammaire ont une d_L1 élevée entre elles ; un compte de clusters sans ce plancher ne mesure rien.
- **Paires proches globalement, divergentes localement** pour Exp. 2 (contrôle de la fusion abusive).
- **Lois identiques en prédiction, syntaxe différente** pour Exp. 5 : d_L1 doit valoir 0 exactement ; vérifie la canonisation numérique avant tout seuil.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **M1, partition syntaxique : la forme devient la variable, pas l'idée.** Imposer 2 `si_sinon`, 2 `par_sous_population`, 2 `softmax` garantit par construction que tout comptage de formes et toute distance prédictive augmentent : une loi `si_sinon` fausse à seuil arbitraire est très éloignée en Jensen-Shannon de tout le reste. N_eff sur les propositions brutes (Exp. 3, critère 1) est donc gonflé par les lois fausses. C corrige par Couv, mais annonce N_eff « des propositions brutes » comme critère.
2. **M1, masquage de l'archive : fuite inverse et confondant.** Servir à chaque fournisseur un sous-ensemble aléatoire des lois retenues leur cache des membres du nul contre lequel ils seront jugés ; ils reproposent ce qui est déjà dans le nul et sont rejetés : perte de puissance mécanique. De plus, deux fournisseurs reçoivent des vues différentes : toute comparaison Kimi/Argon devient non appariée, ce que N-058 interdit de lire.
3. **M2, distance sur le jeu factice du Gardien.** Le jeu factice est fixé pour valider la grammaire ; rien ne dit que sa distribution de traits reflète la loi des traits du monde, en particulier les sous-populations rares. Deux lois égales sur le jeu factice peuvent différer sur le support réel.
4. **M3, N_eff : la matrice n'est pas garantie semi-définie positive.** K_ij = 1 − d_JS/ln 2 n'est pas un noyau PSD en général ; ce qui est établi à ma connaissance concerne la racine de la divergence de Jensen-Shannon comme métrique et des noyaux de la forme exp(−t·JSD) (référence à vérifier). Une valeur propre négative rend λ ln λ indéfini et N_eff non calculable. Il faut une preuve ou un noyau PSD avant tout préenregistrement.
5. **Couv par ablation : procédure non définie et Goodhartable.** « Ablation de chaque trait/interaction dans les lois de S » suppose que la contribution d'un trait soit séparable dans la loi des issues ; dans un `softmax` la normalisation couple les traits ; dans un `melange` l'ablation n'a pas de sens unique. Et un coefficient fantôme 0,001·z2 « capture » z2 selon la procédure ? C note ce défaut pour la baseline qu'il veut battre, mais sa cible en souffre tout autant tant que le seuil d'ablation n'est pas fixé.
6. **Exp. 1 : H_A et H_B ne sont pas exhaustives.** Le seuil conjonctif (N_eff ≥ 2,5 ET ≥ 5/10 mondes) falsifie H_A sur deux voies différentes ; aucune ne confirme H_B telle que formulée (« effondrement modal »). Une troisième cause, le juge sans puissance sur les effets moyens, n'est pas isolée. Le « contrôle négatif S-V1 à 0/12 » est un fait rapporté de v67, pas une exécution du nouveau dispositif.
7. **Exp. 3 : les deux bras passent à 2 appels par génération** alors que v67 en avait 1 ; le changement de budget est appliqué des deux côtés mais rend la comparaison avec v67 non interprétable. Le monde « nul pur » n'est spécifié que pour le bras M1 ; sans le témoin IID dans le même monde nul, le taux de promotions y mesure le juge, pas M1.
8. **Exp. 4 : fuite construction/évaluation.** Le nul v9 inclut des `si_sinon` « sur les seuils quartiles de z0, z1 » et la batterie de « 24 tricheries hors classe » est construite par la même conception. Un nul qui couvre exactement les attaques qu'on lui présente les bloque par construction ; de plus la classe v9 est indexée sur les traits de S-V1 et ne dit rien d'un monde à z2, z3. La batterie doit être construite indépendamment et scellée avant v9.
9. **Génération procédurale dans la grammaire v62.** Si la loi plantée est un arbre de la grammaire, elle est énumérable : une recherche mécanique bornée pourrait l'atteindre. La « découverte » change alors de nature (identification exacte dans un espace fini) et le témoin N-045 pertinent devient l'énumération mécanique, que C ne propose pas.
10. **Calibration circulaire de τ.** Les 11 lois de v67 servent de cas positifs (« réduction à ≤ 2 clusters ») alors que leur proximité n'est établie que qualitativement par le verdict ; calibrer τ sur elles puis mesurer N_eff sur elles revient à vérifier le réglage.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **d_JS moyenne.** Si f et g ne diffèrent que sur A de masse ε sous la distribution du jeu factice, d_JS ≤ ε ln 2 ; sous τ = 0,01 nat pour ε < 0,0144 (calcul), fusion aveugle à toute différence locale.
- **Loi du monde proche de l'uniforme.** Si p(y|x) a une entropie proche de ln 3 partout (effets faibles), toutes les lois raisonnables ont d_JS ≈ 0 entre elles : N_eff → 1 indépendamment du contenu ; la mesure perd sa puissance exactement dans les mondes à petits effets.
- **Lois concentrées.** Avec coefficients proches de ±4 (bornes RAPPORTÉES), un déplacement de seuil `si_sinon` fait basculer des points du jeu factice de probabilités quasi 0 à quasi 1 : d_JS grande pour une différence d'idée nulle ; sur-compte.
- **Exp. 4, puissance.** Avec des interactions à KL dans [0,03 ; 0,08] nat (illustratif de C) et une frontière de promotion ≈ 0,03 nat/épisode (calcul), la puissance sous v8 est déjà incertaine ; le seuil « ≥ 70 % sous v9 » peut être inatteignable à cause du monde, pas du nul. Le duel n'est jugeable que si la puissance sous v8 est mesurée comme témoin sur les mêmes 24 lois.
- **Couv.** Non identifiable si deux traits sont corrélés dans la loi des traits ou si deux mécanismes se compensent dans p*.

### (c) Contrôles négatifs dont l'absence serait fatale

- **A/A sur les proposeurs**, pas seulement sur « la graine de regroupement » (M2 est déterministe : cet A/A-là est trivial).
- **Monde dont la vérité est strictement additive `softmax`** sous M1 : les `si_sinon` imposés doivent tous être rejetés ; sinon la brèche est ouverte par la partition elle-même.
- **Batterie d'attaques construite indépendamment de v9**, scellée avant lui.
- **Lois à coefficients fantômes** sur traits inertes : Couv et N_eff doivent rester inchangés.
- **Énumération mécanique bornée** dans la grammaire sur les mondes procéduraux : si elle atteint la loi plantée, les proposeurs ne sont pas nécessaires et le compte de découvertes n'a pas de sens.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **D_u dépend du regroupement qu'il doit évaluer.** D_u compte les groupes contenant au moins une fiche au-dessus de δ ; les groupes sont ceux du regroupement par (d_m, d_M). En E4, le critère « conservation de 90 % des groupes D_u » est donc mesuré avec l'instrument sous test : si le regroupement fusionne deux mécanismes utiles, D_u ne contient déjà qu'un groupe et la perte est invisible. Il faut une partition de référence définie par l'oracle (mécanismes plantés), indépendante de la distance.
2. **Contextes mécaniques dérivés de l'archive : vrai par construction.** « Couverture mécanique des traits et formes déjà présents dans l'archive » indique en creux les traits non encore utilisés. Dans un monde où tous les traits publics sont causaux, c'est une instruction « cherchez z2 » ; la hausse de D_u en E2 est alors assurée sans aucune diversité propre aux proposeurs. Ce n'est pas une fuite de l'oracle, mais une fuite de la structure du monde par la liste des traits publics.
3. **E3 n'est pas distinct d'E2.** Une « phrase de récompense » sans conséquence sur la sélection est une variante de consigne ; le duel E3 compare deux consignes, pas une récompense à son absence.
4. **E0 : même fuite que C.** « Copies couvertes et hors classe » plantées pour tester le nul élargi, sans dire qui les construit ni quand elles sont scellées par rapport à la définition du nul.
5. **E1 : gain total apparié mais détectabilité non appariée.** D exige l'appariement du gain total (bien) ; mais répartir G en k parts ≈ G/k peut faire passer chaque part sous la frontière ≈ 0,03 nat (calcul). D recommande de « simuler la puissance » dans le texte libre, mais le duel E1 ne conditionne pas sur ce résultat : un monde riche indétectable falsifierait H_A pour la mauvaise raison.
6. **Devis incohérent avec les expériences.** Le § (d) chiffre un harnais Qwen local ; E1–E4 portent sur Kimi et Argon par relais. Le devis ne couvre pas les expériences décisives.
7. **Mesure sur la grille X non pondérée.** Si X couvre « le domaine public » uniformément, d_m pondère les régions hors support réel comme les régions denses ; deux lois égales en distribution sur le support du monde mais divergentes en extrapolation sont séparées. La mesure sur X doit être fixée (uniforme, ou loi publique des traits).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **d_M avec lois discontinues.** Deux `si_sinon` identiques sauf un seuil déplacé de η ont d_M proche de la variation totale entre les deux branches dès qu'un point de grille tombe entre les seuils ; D_p gonfle avec la finesse de la grille. La spécificité du maximum dépend du rapport entre pas de grille et écart de seuils.
- **D_u à δ unique.** Un mécanisme vrai dont le gain de log-score oracle contre la bibliothèque est < δ n'entre jamais dans D_u : la « diversité utile » devient la diversité des gros effets, à l'opposé de l'objectif « effets de tailles variées ». Il faut δ stratifié par taille plantée, ou rapporter le gain continu.
- **E0, « perte de détection ≤ 10 % ».** Différence de deux taux estimés sur quelques dizaines de cas ; l'intervalle traverse le seuil par construction à cette taille. D le reconnaît comme « inconclusif », ce qui rend E0 non décisif au dimensionnement annoncé.
- **E4, « sans hausse des fausses promotions ».** Taux de base ≈ 0 (v67, RAPPORTÉ) : non jugeable sans injection de cas sous le nul.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Traits publics inertes (leurres)** : indispensable pour E2 ; sans eux, les contextes mécaniques et les rôles « effets simples » gagnent par construction. D propose « traits permutés », ce qui n'est pas la même chose (une permutation conserve le nombre de traits causaux).
- **Bibliothèque d'attaques indépendante du nul élargi.**
- **Vérification que la bibliothèque mécanique de D_u ne contient pas déjà le mécanisme** (sinon D_u = 0 par construction) : D liste les cas F mais pas ce contrôle.
- **Lois identiques en distribution sur le support** : d_m = d_M = 0 exactement sur X.
- A/A, monde témoin renommé et propositions aléatoires : présents ; je le constate.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Mission « trait encore peu mobilisé » : même fuite de structure que D.** Elle dépend de l'archive et pointe vers les traits restants ; vrai par construction si tous les traits publics sont causaux. E ne prévoit pas de traits leurres.
2. **Décomposition en mécanismes par le générateur.** E_r repose sur des opérateurs T_r définis par l'oracle à partir de sa paramétrisation. Une proposition peut porter la même information prédictive sous une autre décomposition (interaction exprimée par `par_sous_population`) ; comme T_r agit sur les prédictions q et non sur la syntaxe, ce cas est bien traité — à condition que les T_r soient des contrastes de prédictions, ce que le texte laisse implicite. Point à geler.
3. **Normalisation de E_r.** Diviser par E‖T_r p*‖² donne une échelle commune en apparence ; pour un effet faible le dénominateur est petit et E_r explose sous le moindre bruit d'ajustement : les petits mécanismes ne sont jamais « couverts ». Le biais est le même que D_u mais masqué par la normalisation. E le reconnaît partiellement (« contrastes non nuls et séparables ») sans en tirer une stratification de δ.
4. **Duel « fausses nouveautés » saturé par construction.** La strate « hors classe » part d'un taux de base 24/24 sur un autre monde (RAPPORTÉ). Si le juge cède déjà à 1, la différence avec/sans diversification y est nulle par plafond et ε = 0,02 n'a pas de sens ; le duel mesure l'état du juge, pas l'effet de la diversification. Il faut d'abord E0-équivalent (ou l'extension de nul que E demande) puis seulement ce duel.
5. **Sentinelles : borne supérieure, pas détectabilité.** Les sentinelles sont « écrites à partir de l'oracle » ; si elles utilisent les paramètres vrais, leur promotion mesure la puissance maximale du juge, pas l'existence d'une loi exprimable depuis la vue publique. E conclut « exprimables et détectables » ; seule la seconde est testée, et seulement si la sentinelle est écrite dans la grammaire v62, ce qui n'est pas précisé.
6. **Ancrage matériel découplé.** Modèles 7B pour le devis alors que les duels concernent Kimi et Argon ; le taux de fiches invalides des 7B (rejets du gardien) devient un confondant du coût que E ne mesure pas.
7. **Distances stratifiées sur régions publiques.** Sans oracle, le choix des régions est un pari ; si la sous-population rare du monde privé ne coïncide pas avec une région préspécifiée, la protection annoncée contre la fusion des effets faibles n'existe pas.
8. **A/A en équivalence sans marge chiffrée.** Le duel de calibration est non jugeable tant que la marge et la température des proposeurs ne sont pas fixées.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E_r.** Non jugeable quand E‖T_r p*‖² → 0 ; avec estimation Monte-Carlo sur points privés, la variance relative de l'estimateur croît comme l'inverse du contraste au carré. Le seuil 0,5 admet une loi d'amplitude 30 % du vrai contraste (E_r = 0,49, calcul) : le sens de « couvert » est arbitraire sans justification du seuil.
- **Non-identifiabilité.** Si deux mécanismes se compensent dans p*, T_r p* ≈ 0 ; E les exclut, mais la « couverture accessible » change alors et le δ relatif du duel rôles avec elle.
- **Duel rôles, δ = 0,10 relatif.** Avec 12 mondes × 2 graines (illustratif de E), un intervalle simultané sur une différence appariée de couverture traverse δ dès que l'écart-type inter-graines des proposeurs dépasse ≈ 0,1 (illustratif) : inconclusif par construction.
- **Distances stratifiées.** Si une région a masse ε sous la loi des traits mais poids 1/R dans la stratification, puissance contre les doublons mais faux rejets de doublons dus à l'extrapolation hors support.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Traits publics inertes** pour les missions.
- **Étalonnage de E_r sur lois aveugles** : uniforme, marginale, K1 doivent donner E_r ≈ 1 ; une loi de bruit doit dépasser 1. Sans cela, 0,5 n'a pas d'échelle.
- **Sentinelles écrites dans la grammaire v62** et **énumération mécanique bornée** (E la liste dans le tableau ; elle doit entrer dans le duel « mondes riches »).
- **Attaques construites indépendamment** de toute extension du nul.
- **Taux de fiches invalides** des modèles ouverts avant toute comparaison de coût.
- A/A : présent, mais à marge fixée.

---

## Ce que les quatre pièces ont en commun, dit sans les fusionner

Les quatre propositions acceptent qu'une distance prédictive définisse « le même constat » et qu'un critère oracle définisse « l'utile » ; aucune ne contrôle le cas où la liste des traits publics suffit à produire la diversité attendue par construction (traits leurres), et deux (C, D) testent une extension du nul avec des attaques dont la provenance n'est pas indépendante. B seule choisit le représentant après les données, ce qui est fatal à la garde ; C, D, E le choisissent avant. Aucune ne mesure la puissance du juge sur les mondes riches comme préalable conditionnel aux duels : c'est la condition sous laquelle toutes leurs métriques valent 0 quelle que soit la diversité.

FIN-DE-CELLULE