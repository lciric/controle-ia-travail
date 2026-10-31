# Proposition B — Tour 2 — Collisionneur « protocelles »

---

## (a) Résolution des divergences non résolues

### a.1 — Valeur de n

**Position : n ne peut pas être fixé ; je retire n = 3.**

Au tour 1, j'avais posé n = 3 comme HYPOTHÈSE. La synthèse (section 9, I4) montre que cette valeur, combinée à la loi asymptotique R_min ≃ 0,22n, produit un chiffre (0,66) inférieur à la borne nécessaire R > e^U/(2 − e^U) ≈ 2,08 (synthèse, section 9 : p. 40, l. 2788-2789), ce qui est une contradiction interne. Le même problème frappe n = 6 de C (I10). L'erreur n'est pas dans la valeur de n elle-même mais dans l'application hors domaine de la loi asymptotique ; toutefois, poser une valeur de n sans connaître la règle de formation des lots de l'orchestrateur reste une conjecture non contrainte.

**Ce qui trancherait :** l'audit du code de l'orchestrateur (section 8, étape (i)), qui révèle la taille et la règle de formation des lots. Sans cet audit, toute valeur de n est SUPPOSÉE et rend les prédictions qui en dépendent non interprétables.

### a.2 — Identité de q côté organisme

**Position maintenue : q n'est pas identifié, mais je précise ce qu'il faudrait pour l'identifier.**

La fidélité q du papier est la probabilité qu'une réplicase copie fidèlement un modèle dans un événement catalytique unique (synthèse, section 2 : p. 3, éq. 1 ; p. 17, l. 1577-1580). Côté organisme, l'événement élémentaire est une fusion entre deux fiches, gérée par un bisociateur. Pour que q ait un sens, il faut :
1. que la fusion soit un événement discret avec un résultat classable (fiche vraie / fiche fausse) — HYPOTHÈSE, plausible mais non vérifié ;
2. que le bisociateur ne s'adapte pas entre fusions au sein d'un même lot (stationnarité intra-lot) — HYPOTHÈSE, non vérifié ;
3. que la probabilité de produire une fiche vraie dépende principalement du type des parents (paire vraie-vraie, vraie-fausse, fausse-fausse) et non de leur contenu particulier — HYPOTHÈSE forte.

C définit q comme la probabilité qu'une paire vraie donne une fiche vraie (synthèse, section 2). C'est une instanciation raisonnable sous les conditions ci-dessus, mais elle suppose la réponse à la question trans/cis : si un seul parent suffit, q n'est plus un paramètre de paire.

**Ce qui trancherait :** l'expérience P2 (synthèse, section 4), mesure des taux par type de paire parente, après audit de l'orchestrateur et scellement des prédictions.

### a.3 — Applicabilité à la pince et à l'arène

**(i) Pince.** Je maintiens que les théorèmes ne donnent pas de prédiction directement testable dans la pince, mais je reconnais la nuance de la synthèse.

Le levier r̄ du papier est une propriété de la *règle de division* : il mesure combien la règle favorise les protocelles riches en réplicases (synthèse, section 5 : p. 13, l. 1187-1191 ; p. 68, l. 5013-5016). Un juge de la pince qui promeut ou rejette des fiches individuelles n'opère pas au niveau de la division d'un lot mais au niveau de la sélection intra-lot. La réserve du lecteur (synthèse, section 5) est bien fondée : promouvoir des fiches n'est pas une règle de division au sens du papier.

C maintient que la condition nécessaire r̄ > 2^(−2Λ) s'applique (synthèse, section 5 ; corrigé de I11 : condition nécessaire seulement, p. 68, l. 4991). Même comme condition nécessaire, elle présuppose que la pince peut être décrite comme une division aveugle augmentée d'un levier r̄, ce qui est lui-même une HYPOTHÈSE non vérifiée. La pince pourrait opérer hors du cadre des divisions aveugles — auquel cas la condition nécessaire ne s'applique tout simplement pas.

**Si l'on voulait tester malgré tout :** il faudrait d'abord démontrer que la pince peut se décomposer en « division aveugle + levier r̄ mesurable », puis mesurer r̄ et vérifier la condition. C'est un programme de recherche, pas une prédiction prête à signer.

**(ii) Arène.** Les paramètres sont non stationnaires par construction : le générateur s'adapte, la population d'attaques évolue, la défense se met à jour. Aucun théorème du papier ne couvre ce régime. Le papier exige une fidélité q constante et un poids θ fixe (synthèse, section 3 : « stationnarité »). Je ne vois pas de sous-régime naturel où ces conditions seraient remplies dans une arène adversariale.

### a.4 — Extinction quadratique à fécondité infinie avec deux parents

**Position : l'extinction est plausible mais pas démontrée ; le résultat dépend d'une hypothèse sur le taux d'événements.**

L'argument de C (synthèse, section 5) repose sur le fait qu'à fécondité infinie, seule la suite des copies compte (p. 16, l. 1558), et qu'avec deux parents, les paires vraie-vraie se forment en O(1/N²) si le tirage est uniforme. D objecte que ce calcul requiert une loi explicite du taux d'événements par pas — autrement dit, combien de fusions ont lieu par cycle en fonction de la composition du lot.

Les deux positions sont cohérentes sous leurs hypothèses respectives :
- **Si** le nombre de fusions par cycle est fixe (ou borné inférieurement), **et si** le tirage des parents est uniforme sans remplacement au sein du lot, alors la proportion de paires v-v parmi les fusions est bien O(p²) où p est la fréquence des fiches vraies, et l'argument de C tient.
- **Si** le nombre de fusions par cycle dépend de la composition (par exemple, proportionnel au nombre de paires v-v disponibles), le taux effectif change et l'argument tombe.

**Ce qui trancherait :** c'est un cas du duel trans/cis (P3 / E-B2). L'audit de l'orchestrateur révèle la règle de tirage des parents et le nombre de fusions par cycle. Si le tirage est uniforme et le nombre fixe, l'argument de C est validé formellement par un calcul de probabilité standard (pas besoin de simulation). Sinon, il faut un modèle de branchement adapté.

### a.5 — Source de la première mesure

**Position modifiée : expérience prospective d'abord, en accord avec D ; je retire ma position du tour 1.**

Au tour 1, je demandais de nouveaux appels comme première source. La synthèse (section 8) et l'argument de D montrent que lire les journaux de la course 2 avant d'avoir scellé les prédictions est une source de biais de confirmation. Mais de nouveaux appels *non préenregistrés* posent le même problème en plus coûteux.

L'ordre correct est :
1. Audit du code de l'orchestrateur (pas les journaux, pas les résultats — juste la mécanique).
2. Étalonnage de l'estimateur spectral, calculs de puissance, noyaux exacts.
3. Préenregistrement scellé et contre-lu des prédictions.
4. *Ensuite* lecture des journaux ou nouveaux appels, selon ce que le préenregistrement spécifie.

**Biais de chaque source :**
- Journaux avant scellement : adaptation post hoc des seuils ; confirmation narrative.
- Nouveaux appels avant scellement : même risque si les résultats informent les prédictions ; coût supplémentaire inutile.
- Expérience prospective après scellement : pas de biais de confirmation ; coût à budgéter mais le seul design propre.

### a.6 — Destruction contre archivage des fusions inachevées

**Position modifiée : j'adopte « archiver hors du vivier » comme défaut, en remplacement de « perdu ».**

L'argument décisif est celui de la synthèse (section 6) : pour la dynamique du vivier, archiver sans puiser est équivalent à détruire (les fiches ne participent pas aux fusions). Mais archiver préserve l'option de mesurer θ′ et q_B sur épreuve séparée, ce qui a une valeur informationnelle strictement positive à coût de stockage négligeable. « Perdu » ferme cette option sans bénéfice. C'est un argument de dominance faible, pas de modèle.

**Ce qui trancherait :** la comparaison n'est pas entre « détruire » et « archiver » (dynamiquement identiques) mais entre « hors du vivier » et « dans le vivier sous condition ». C'est l'objet de P4 ou P5 (section 4), après mesure de θ′ et étalonnage de l'estimateur spectral.

---

## (b) Politique consolidée sur les fusions inachevées

### b.1 — Acceptation de la politique consolidée

**J'accepte la politique consolidée avec une modification mineure.**

La politique proposée (synthèse, section 6) dit : hors du vivier par défaut ; réinjection après mesure de θ′ et q_B sur épreuve séparée ; garde dans le vivier permise seulement si θ′ < 2(1 − τ), sans re-troncation.

Modification : ajouter une condition de réinjection plus conservatrice. Même si θ′ < 2(1 − τ), la réinjection ne devrait être permise que si le lot cible contient au moins n_min fiches vraies (seuil fixé par l'étalonnage de P4/P5). Justification : le bain stationnaire du papier est un résultat numérique dont le seuil est conjectural (synthèse, section 6 : p. 21, l. 1782). Injecter des brouillons dans un lot déjà fragile (peu de fiches vraies) revient à tester une conjecture en production.

Référence : la synthèse note que le seuil du bain stationnaire est conjectural (section 6) et que le bain ne bat que la perte des seules copies lentes face à des copies rapides présentes, pas le rejet de toutes les inachevées (I12, section 9). La prudence est donc du côté du maintien hors vivier sauf preuve contraire.

### b.2 — Testabilité des trois options avant lecture des journaux

- **Détruire** : testable par simulation (processeur, sans journaux). On simule un branchement multitype avec le noyau exact aux tailles en jeu, en supprimant les copies inachevées. Données de classe (a).
- **Archiver hors vivier** : dynamiquement identique à « détruire » pour le vivier ; testable de la même façon. La différence (conservation pour mesure) est une question de design, pas de dynamique.
- **Garder dans le vivier sous condition** : testable par simulation si θ′ et τ sont fixés, mais les valeurs de θ′ dans l'organisme ne sont connues qu'après audit de l'orchestrateur. Si l'orchestrateur fixe θ′ (par exemple, poids de tirage uniforme → θ′ = 1), le test est possible. S'il est endogène (avantage par la longueur ou le temps), il faut des données empiriques. **Conclusion : la troisième option n'est pleinement testable avant lecture qu'à θ′ fixé par l'orchestrateur.**

### b.3 — Origine de ma position : papier ou cadrage ?

Ma position du tour 1 (« perdu » par défaut) venait d'une lecture conservatrice du papier : les identités (i) et (ii) (synthèse, section 6 : p. 56) montrent que perdre une copie inachevée ne coûte rien sur la charge à fécondité infinie (p. 10, l. 863), et que les risques augmentent avec θ′. J'avais interprété « ne coûte rien à perdre » comme « il faut les perdre », ce qui est un pas logique non justifié : l'absence de coût ne justifie pas la destruction, elle justifie seulement l'indifférence — et face à l'indifférence, conserver l'option de mesure domine.

La question (« t'es sûr ? ») et la conclusion du papier (p. 16, l. 1542-1543) ont contribué au doute, mais le changement de position au tour 2 vient de l'argument de dominance faible exposé en a.6, pas du cadrage. La réserve R4 de la synthèse est pertinente : l'unanimité du tour 1 sur « jeter n'est pas établi » était en partie induite.

---

## (c) Prédictions à signer et ordre des travaux

### c.1 — Tri des prédictions

| N° | Verdict | Commentaire |
|---|---|---|
| P1 | **(F)** | Paramètres n, R, U sont SUPPOSÉS ; l'estimateur de ρ est invalidé (D-T2, accepté par C-T3). À corriger : remplacer par le noyau exact à la taille réelle (après audit), étalonner l'estimateur. |
| P2 | **(S)** | Signée et prête. Les taux par type de paire parente sont mesurables ; le seuil 0,02 est illustratif mais le protocole (intervalle à 95 %, dérive de densité) est opérationnel après scellement. |
| P3 | **(F)** | Le duel trans/cis est la bonne première expérience, mais ma version (B-T3 E-B2) n'a pas de seuil signé ; celle de D (E0, avec δ fixé par le bruit de branchement simulé) est mieux spécifiée. À corriger : fixer δ avant les données par simulation de puissance. Aussi : j'avais déclaré E-B2 « sans coût », ce qui est faux (synthèse, section 11, réserve 6) — elle demande des appels au bisociateur. |
| P4 | **(F)** | Seuils illustratifs (θ′ = 1,2, θ′ = 2,5, seuil +0,02 sur ρ) et n = 6 non établi. À corriger après audit de l'orchestrateur. Structure du protocole (bras × 40 lots, noyau exact recalculé) est solide. |
| P5 | **(S)** | Signée : Δρ = ρ_vivier − ρ_quarantaine, seuil 0, estimateur étalonné par simulation. Dépend de l'étalonnage (étape (ii) de la section 8) mais le design est complet. |
| P6 | **(A)** | J'abandonne P6 (ma propre prédiction). La puissance est nulle à trois lots par bras (je l'ai reconnu en T3) ; requérir 6 à 10 lots par bras est un run prospectif coûteux pour un résultat que P5 couvre mieux. |
| P7 | **(S)** sous condition | Signée si les journaux permettent de séparer l'injection exogène du travail endogène du bisociateur. Cette séparation est un pré-requis non trivial : à vérifier lors de l'audit du code. Si l'injection est indissociable, **(A)**. |
| P8 | **(S)** sous condition | Signée conditionnelle : dépend de la validation du noyau littéral à θ = 1, elle-même dépendant de l'audit de l'orchestrateur. Si le noyau est validé, le seuil q = 1/2 (Théorème 2, synthèse : p. 4, l. 355-358) est exact et non illustratif. |
| P9 | **(F)** | La correspondance pince-levier est contestée (a.3 ci-dessus). Le protocole 2×2 (attaquant gelé/adaptatif × tri réel/fictif) est bien conçu, mais repose sur une identification que je rejette. À corriger : redéfinir ce que la mesure teste sans présupposer l'équivalence pince-levier. |
| P10 | **(S)** | Signée, asymétrique (un échec ne réfute pas H2 : synthèse, section 4). Les trois boîtes non certifiées sont un objectif computationnel bien défini. Résultat : certificat vérifié par un second code indépendant (D), ou contre-exemple reproduit. |
| P11 | **(A)** | J'abandonne P11 (ma propre prédiction). Devenue qualitative en T3, non signée, non falsifiable. |
| P12 | **(A)** | Ne dérive pas du papier (synthèse, section 4) ; hors du cadre du collisionneur. |

**Résumé :** 4 signées (P2, P5, P8, P10), 1 signée sous condition (P7), 4 à corriger (P1, P3, P4, P9), 3 abandonnées (P6, P11, P12).

### c.2 — Ordre des travaux

J'accepte l'ordre proposé en section 8 avec deux ajustements :

1. **L'étape (i) (audit du code) doit inclure explicitement la séparabilité de l'injection exogène** (pour P7), en plus des points déjà listés (parents consommés ou conservés, règle de tirage, taille des lots). Sans cette information, P7 est indécidable.

2. **L'étape (v) (certification des trois boîtes de H2) peut être conduite en parallèle** des étapes (ii)-(iv), car elle est indépendante de l'organisme et ne requiert que du calcul arithmétique exact. Elle n'a pas besoin d'attendre les noyaux exacts.

L'étape 3 (lecture des journaux) reste après le préenregistrement — je me rallie à D sur ce point (a.5).

### c.3 — Recodabilité des noyaux exacts

**Difficulté : modérée.**

Le noyau K = BH + 2^(1−2n)I est défini explicitement (synthèse, section 9 : p. 17, l. 1577-1586). B est la matrice de transition des types de filles sous la distribution binomiale, H la matrice de copie par réplicase, et le terme 2^(1−2n)I est le bruit de fond. Les entrées sont des sommes combinatoires fermées. Pour n = 3 ou n = 6, les matrices sont de taille finie (2^n = 8 ou 64 types de protocelles selon la composition en réplicases). Le rayon spectral peut être calculé par diagonalisation exacte à cette taille.

Ce qui rendrait le recodage plus qu'élémentaire :
- Le papier mentionne l'arithmétique exacte avec Brent à 10^−7 pour la racine de ρ(K) = 1 (synthèse, section 9 : p. 17, l. 1586) ; à n = 6, la matrice 64×64 est gérable mais requiert une implémentation soigneuse de la distribution binomiale multivariée pour éviter les erreurs d'arrondi.
- Les tables S1a-S1c (p. 42) fournissent des valeurs de contrôle pour vérifier l'implémentation.

**Estimation de coût** (illustratif) : ≈ 2-4 heures de développement avec un langage à précision arbitraire (Python/mpmath, ou SageMath), plus ≈ 1 heure de vérification contre les tables publiées.

### c.4 — Impact des inexactitudes majeures sur le classement des prédictions

| Inexactitude | Impact |
|---|---|
| **I4** (B-T1 : R_min ≈ 0,66 à n = 3) | Affecte P1 (déjà classée F) et affectait P11 (déjà classée A). N'affecte pas P6 (classée A pour d'autres raisons). Mon propre chiffre, ma propre erreur. |
| **I10** (C-T1 : R_min ≈ 1,32 à n = 6) | Même nature que I4 ; affecte P1 de C (classée F). Confirme que les extrapolations asymptotiques aux petites tailles sont inutilisables et que l'étape (iv) (noyaux exacts) est un pré-requis. |
| **I11** (C-T1 : condition du levier suffisante → nécessaire seulement) | Affecte P9 (classée F). La prédiction de C sur la pince passait de « maintient ρ > 1 » à « condition nécessaire seulement, atteinte pour le tri partiel à y = 0 » (synthèse, section 9 : p. 69, l. 5095-5100). Cela affaiblit mais ne détruit pas P9 ; P9 reste F (à reformuler), pas A. |
| **I12** (C-T1 : bain « plus viable que le rejet pur ») | Affecte la justification de l'option « dans le vivier » de P4. Le comparateur correct (bain vs. perte des seules copies lentes, pas vs. rejet de toutes les inachevées) restreint le domaine d'utilité du bain. P4 reste F (seuils à recalculer après correction du comparateur), pas A : le protocole expérimental (bras × 40 lots) est sain, seule l'interprétation du résultat change. |

**Changement de classement :** aucune prédiction ne passe de S à F ou de F à A à cause de ces inexactitudes seules. I4 et I10 confirment que P1 est F (déjà classée ainsi). I11 et I12 maintiennent P9 et P4 en F avec des corrections plus profondes que prévu.

---

FIN-DE-CELLULE