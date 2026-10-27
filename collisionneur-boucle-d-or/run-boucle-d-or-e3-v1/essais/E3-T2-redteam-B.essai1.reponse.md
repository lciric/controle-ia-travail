# Proposition B, tour III.2 : équipe rouge croisée contre A et C

J'ai reçu les faits (A, P, R1, R2, T, C), la question et les deux conceptions (E3-T1-A, E3-T1-C). Toutes sont présentes et lisibles, sans coupure visible. Le fichier joint de Gemini (`27841389…`) n'est pas versé, comme les faits le disent : je n'en dis rien.

**Deux manquements d'intégrité, à corriger avant tout usage :**
- A étiquette « VÉRIFIÉ (attribution) » des références citées de mémoire : Uzzi et collègues, Fleming, et d'autres. Aucun fait servi ne les vérifie. Leur statut reste « référence à vérifier sur PDF ».
- C requalifie le juge v1 en « OBSERVÉ-NON-AUDITÉ » alors que P le transmet comme RAPPORTÉ. C invente aussi un statut « RAPPORTÉ (littérature) » pour Wang et collègues, Bromham et collègues, Leahey et collègues. Ces contenus ne figurent pas dans les faits : ils restent HYPOTHÈSE ou « référence à vérifier ».

---

## Contre la proposition A

### (a) Failles

**A1. Le duel 1 est vrai par construction, et son verdict tient au choix de la loi de c.**
- A tire le centre c uniformément sur [0,06 ; 0,74] et la demi-largeur w sur [0,04 ; 0,12]. La fenêtre fixe [0,12 ; 0,26] ne touche la bande vraie que si |c − 0,19| < 0,07 + w.
- Avec w ≈ 0,08, cela donne c ∈ [0,04 ; 0,34] ∩ [0,06 ; 0,74]. Le recouvrement, même partiel, survient donc dans environ 41 % des répétitions (calcul sur les bornes illustratives de A).
- Le résultat « la fenêtre fixe perd en moyenne » découle donc de la loi de c que choisit l'expérimentateur, pas d'une propriété de l'allocateur. Centrez c sur 0,19 et la fenêtre gagne ; étalez-le et elle perd.
- C'est une fuite entre la construction et l'évaluation. L'instrument mesure le recouvrement entre deux intervalles, et la vraie question (« où est la bande dans le monde réel ? ») n'y entre jamais.
- Le duel ne se justifie que couplé au duel 3, qui doit fournir une loi empirique de c. A le présente comme indépendant.

**A2. Le duel 1 hérite d'un artefact de P, et la fenêtre molle en dépend.**
- Je me sers ici de C, en le disant. Les huit cases de largeur 0,1 de Thompson et du tri chevauchent les bords de [0,12 ; 0,26]. Dans le monde « cloche » de P, le meilleur taux de vérité accessible par case vaut 0,41, contre 0,50 dans la fenêtre. L'arithmétique est juste, sur les paramètres RAPPORTÉS de P.
- Le « Thompson à a priori informé » de A ne dit pas sur quelles cases porte l'a priori. S'il garde les cases de P, la fenêtre molle est mal alignée par construction et perd une partie de ce qu'elle devait conserver.
- La conclusion de A en dépend (« seule la fenêtre molle ne perd pas », prédite à 0,6).

**A3. Le duel 2 est vrai par construction, et sa variable σ est payée par un budget gratuit.**
- *Vrai par construction.* La vérité dépend « de σ seul » dans le monde « synergie ». Que σ y batte s ne dit rien du pôle. Dans le monde générateur de P, une fille vraie vaut « parent A sur la sous-population 0, loi neuve sur la 1 » : la nouveauté ne vient d'aucun des deux parents. La synergie des parents n'y a aucun lien causal avec la vérité de la fille. A l'écrit lui-même en réserve, sans en tirer la conséquence : le duel 2 ne peut départager que des mondes qu'il a écrits.
- *Budget.* σ est estimé « sur les 50 tirages de calibrage du juge, donc avant le test frais ». Dans P, ces 50 tirages font partie du test à un dollar. Estimer σ sur les 300 candidates avant d'allouer revient à consommer 300 × 50 tirages, soit l'équivalent de 60 tests, pour un budget de 40.
- A compare donc un allocateur qui voit des données à un allocateur qui ne voit que s, à coût déclaré nul. C a compté ce coût (n₀ = 15 dans le budget) ; A ne le fait pas.

**A4. Le duel 2 laisse fuir le calibrage du juge.**
- Si l'on choisit les filles d'après leurs 50 tirages de calibrage, et que le juge ajuste sur ces mêmes tirages son nul augmenté (poids du mélange, enveloppes), la sélection retient les filles dont le calibrage a eu de la chance.
- Le nul ajusté sur un échantillon favorable n'a plus son niveau nominal : on risque une inflation de α sur les promues. C'est une HYPOTHÈSE, mais aucun contrôle de A ne l'exclut.

**A5. Dans le duel 3, la distance n'est pas séparée du score lui-même ni de la fréquence. La sélection des paires candidates peut aussi fabriquer une cloche.**
- d = 1 − cosinus des vecteurs de contexte d'avant porte presque la même information que les voisins communs, Adamic-Adar et l'allocation de ressources : une proximité de second ordre.
- Sur des paires dont deux termes partagent beaucoup de contextes, la cooccurrence lexicale future monte mécaniquement. T RAPPORTE que la tête de RA est faite de mots courants, et que l'attachement préférentiel seul atteint 5,62 % à 10 000 contre un taux de base de 0,28 %. La fréquence est donc le premier facteur confondant, et A ne la neutralise pas.
- **Effet de sélection (HYPOTHÈSE).** Les paires candidates de T sont, par définition, celles qui ne cooccurrent jamais avant 2011. À très forte similarité de contexte, une paire qui n'a jamais cooccurré est souvent formée de **substituts** : variantes graphiques, synonymes, notations concurrentes. Des substituts cooccurrent rarement ensuite. Le conditionnement par la non-cooccurrence peut donc creuser le haut de la courbe et produire un pic intérieur, stable au placebo puisqu'il est structurel. Le critère de stabilité de A (même vingtile ± 2 aux deux découpages) ne protège pas contre un artefact stable.

**A6. La validation croisée du duel 3 fuit par les termes.**
- A forme ses dix plis en découpant les paires. Un même terme apparaît alors dans l'apprentissage et dans le test, et la régression unimodale peut apprendre des effets propres à chaque terme.
- Les plis doivent être disjoints en termes, ou formés par blocs de termes.

**A7. Le duel 4 partage l'angle mort du juge.**
- L'objectif E[(−log p_nul)·1{promue}] calcule la sévérité **sous le nul composite du juge**. Contre une fille qui exploite un trou de ce nul (« parent + loi aveugle », exclu de P et dit), p_nul est faux par construction : la fille paraît sévère, et l'objectif la récompense.
- A présente cet objectif comme la parade à « la survie facile ». Il n'en protège que si le nul est complet, et c'est précisément ce que le duel 5 ne vérifie pas (A8).

**A8. Le duel 5 oublie le seul tricheur connu.**
- Sa batterie compte « copies, enveloppes aveugles, mélanges ». Le trou nommé par P, « parent + loi aveugle », n'y figure pas.
- Un juge qui passe le duel 5 de A peut donc rester franchissable par le seul tricheur dont on sait qu'il le franchit. Le préalable que A met en tête de l'ordre des opérations est incomplet là où il compte.

**A9. Inférence forte (B4) : des issues ne falsifient rien.**
- Au duel 1, H_B est une conjonction (« la fenêtre fixe perd **et** seule la fenêtre molle ne perd pas »). L'issue « fenêtre fixe indistincte » ne falsifie ni H_A ni H_B.
- La règle doit attribuer l'issue « indistincte » à l'une des deux hypothèses avant le lancement.

### (b) Scénarios d'évasion

Agent adverse : un générateur de fiches, ou un défenseur de la fenêtre qui écrit le monde.

1. **Fenêtre et similarité s.** s se calcule sur le texte de domaine des fiches. R2 RAPPORTE qu'un changement de pondération (TF-IDF ou fréquences brutes) déplace les cosinus de 0,11 à 0,28. Un générateur qui choisit son vocabulaire de domaine place ses filles dans [0,12 ; 0,26] à volonté, pour un coût nul : quelques mots ajoutés ou retirés.
2. **Variable o (recouvrement d'opérateurs).** Il suffit de semer sur plusieurs fiches une étiquette d'opérateur rare inventée. R1 a déjà nommé cette attaque : « jargon rare fabriqué ». Coût nul.
3. **Synergie σ.** Si l'agent qui formule la fille voit les tirages de calibrage, ou leur effet par la sélection d'A4, il peut ajuster la fille au calibrage. σ et le juge sont alors tous deux faussés.
4. **Objectif de sévérité (duel 4).** Il est trompé par le tricheur « parent + loi aveugle » (A7).
5. **Rétrodiction (duel 3).** Pas d'agent adverse ici, mais une évasion par l'analyste : vingtiles, choix de d (cosinus de contexte ou profil de sous-catégories), seuil de pic. Plusieurs chemins mènent à un pic à volonté si leur liste n'est pas scellée.
6. **Tous à la fois, coût nul.** Le tricheur scripté « parent A + loi aveugle », habillé d'un vocabulaire qui le place dans la fenêtre et d'une étiquette rare partagée, passe tous les instruments ensemble : le juge (trou connu, au-delà de α par hypothèse), l'objectif de sévérité (p_nul mal spécifié), la fenêtre (s choisi) et le recouvrement d'opérateurs (étiquette semée). Aucun appel de modèle n'est nécessaire, comme pour les tricheurs de R1.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel 1 : sensibilité à la loi de c.** Courir au moins deux lois préenregistrées : c centré sur la bande de Gemini, et c uniforme. Si le signe de D₁ change de l'une à l'autre, conclure que le duel ne dit rien sans la loi empirique du duel 3.
2. **Duel 1 : cases alignées.** Refaire Thompson, le tri et la fenêtre molle sur une grille dont les bords tombent à 0,12 et 0,26. Sinon, A2 reste confondu.
3. **Duel 2 : coût et monde nul.** Facturer σ dans le budget. Puis courir un monde v ≡ 0 où les filles sont sélectionnées sur leur calibrage : le taux de promotion doit rester ≤ α.
4. **Duel 3 : fréquence appariée.** Au minimum, ranger d à l'intérieur de strates de produit des degrés (attachement préférentiel). Un pic qui disparaît à fréquence fixée était un effet de fréquence.
5. **Duel 3 : substituts retirés.** Retirer les paires de variantes (racine commune, bigramme contenant l'unigramme, distance d'édition faible), puis refaire la courbe.
6. **Duel 3 : plis disjoints en termes.**
7. **Duels 4 et 5 : le tricheur connu partout.** Injecter « parent + loi aveugle » dans chaque monde d'allocation et mesurer la part du budget qu'il capte. Sans ce contrôle, toute supériorité de l'objectif de sévérité est ininterprétable.

---

## Contre la proposition C

### (a) Failles

**C1. L'expérience 1 confond la vérité v(s) et la probabilité de promotion p.**
- Le défaut d'entropie que C veut exhiber suppose que la fenêtre fuit le cœur à v = 0,85 pour les flancs à v = 0,5. Or l'allocateur de P vise p (promotion), pas v. Approximativement, p = v·π + (1 − v)·f, où π est la puissance moyenne du juge (force tirée sur [0,3 ; 1,5]) et f ≤ α le taux de fausses promotions.
- Avec π ≈ 0,6 et f ≈ 0,02 (illustratifs), on obtient p ≈ 0,51 au cœur et 0,31 sur les flancs. Le cœur est plus proche de 0,5 : la fenêtre entropique **choisit le cœur**, et le monde « cloche à cœur riche » la **favorise**.
- L'issue de C dépend donc de π, que C ne fait pas varier. Le monde ne teste pas l'entropie : il teste la puissance du juge.
- Le point 4 de A (l'entropie confond l'incertitude de mesure et l'incertitude épistémique) est la bonne formulation. Je m'en sers ici contre C.

**C2. Le chiffrage des pertes passe aussi de v à p, et contredit C.**
- « Le pur hasard a une espérance de 0,196 » : c'est un taux de **vérité** (0,325 × 0,5 + 0,675 × 0,05, arithmétique juste sur P). Ce n'est pas un taux de découvertes, qui doit être multiplié par la puissance.
- « Jusqu'à −75 % » et « perte permanente et non détectable » contredisent C (la pièce) : les témoins plantés de chaque génération mesurent justement le taux de bonne élimination. Le cas « fenêtre épuisée → hasard » est rare dans P (52,5 candidates attendues pour 40 tests), mais l'archive enregistre aussi les éliminées.
- « Non détectable » est une affirmation sans mesure, à retirer.

**C3. L'expérience 2 transforme une corrélation en preuve.**
- C écrit que RA « prouve » que les ponts suivent le couplage structurel le plus fort plutôt qu'une bande médiane. T ne mesure aucune distance par bande. T RAPPORTE en outre que la tête de RA est faite de mots courants et que l'issue est une cooccurrence lexicale, « pas une découverte féconde ».
- Le succès de RA est compatible avec un pic intérieur sur une autre variable. Le statut est HYPOTHÈSE, et le mot « prouve » est un superlatif sur la portée.

**C4. La restriction aux déciles médians n'a pas de témoin.**
- « RA restreint à Q₂–Q₄ » revient à classer les 10 000 meilleures paires de RA dans 30 % du vivier seulement. La précision à 10 000 y change mécaniquement, par la composition et le taux de base du sous-vivier. T RAPPORTE des taux de base de 0,11 % à 0,76 % selon la strate.
- Sans une restriction au hasard de même taille, l'écart RA_fenêtre − RA mélange l'effet de la fenêtre et l'effet de la troncature.
- La correspondance « centiles 10–40 % = Boucle d'or » n'est étalonnée sur rien : c'est le reproche que A et la question font à Gemini, et C le reproduit.
- Les facteurs confondants A5 (fréquence, sélection des substituts) et A6 (bootstrap sur paires, qui fuit par les termes) s'appliquent à C à l'identique.

**C5. L'expérience 3 est vraie par construction, et elle fuit par le calibrage.**
- **Vrai par construction.** Δ_syn est le gain de la fille sur l'enveloppe de ses parents, mesuré sur 15 tirages. C'est une version réduite du test du juge, qui prédit donc la promotion par construction.
- Ce que l'expérience compare vraiment, c'est un plan en deux étapes (criblage puis test complet) contre un plan en une étape. La similarité de domaine n'y est plus en cause.
- L'issue « le bras 2 gagne » ne départage donc pas « s contre synergie ». Elle dit qu'un test séquentiel bat un test fixe à budget de tirages égal, ce qui est une question différente.
- **Fuite.** Les 15 tirages de criblage sont pris « sur les 50 de calibrage ». C contrôle qu'ils ne sont pas réutilisés dans les 200 tirages frais, pas qu'ils ne servent pas au calibrage du nul. Si le juge ajuste ses mélanges sur ces 50 tirages, A4 s'applique.
- **Unité de coût.** C passe du dollar par test (P) au tirage élémentaire. Il suppose que les 120 filles criblées existent déjà, gratuitement, dans le réservoir. Or, dans C (la pièce), une fille doit d'abord être produite par fusion. A le signale (point 6) : si la fusion domine le coût, cribler 120 filles en coûte trois fois plus que d'en tester 40, et le bras 2 est favorisé par la comptabilité.

**C6. Le Thompson quadratique ne contient pas les mondes de P.**
- C affirme que la famille logit quadratique « contient exactement » les cinq mondes. Ce n'est pas le cas :
  - « cloche » et « bords » sont des fonctions en escalier ;
  - « bords » est asymétrique (7,5 % à gauche, 25 % à droite) ;
  - « croissant » est linéaire en v, pas en logit.
- L'erreur de spécification coûte quelque chose, et le sens de ce coût n'est pas connu d'avance.

**C7. Inférence forte (B4) : des issues ne falsifient rien.**
- *Expérience 1.* H_A n'est falsifiée que par une conjonction (pertes hors cloche **et** perte dans le cœur riche) ; H_B ne l'est que si la fenêtre bat TQ dans les deux cloches. L'issue « perte hors cloche, victoire dans le cœur riche », précisément celle que C1 rend probable, ne falsifie ni l'une ni l'autre.
- *Expérience 2.* H_B affirme la monotonie, mais un pic intérieur avec un gain inférieur à 2 points ne la falsifie pas selon la règle de C. La monotonie est donc affirmée sans être exposée.

### (b) Scénarios d'évasion

1. **Couplage d'opérateurs pondéré.** La somme des 1/freq(o) récompense la rareté. Une étiquette inventée et partagée maximise le score, comme pour A. Coût nul.
2. **Orthogonalité des résidus.** Deux parents dont l'un prédit du bruit ont des log-vraisemblances décorrélées : l'instrument lit de la « synergie » là où il n'y a que du vide. Coût nul : il suffit d'un parent sans contenu qui survit au α du juge.
3. **Criblage.** Le tricheur « parent A + loi aveugle » est évalué contre la **même famille** de nul (enveloppe convexe des parents) que le juge. S'il franchit le juge, il franchit le criblage par construction. L'échec est corrélé, pas indépendant.
4. **Allocateur TQ ou bandit récompensé par la promotion.** Si p_triche > α, le bandit se concentre sur la case du tricheur, ce que C dit lui-même.
5. **Pondération par les témoins.** La parade de C (soustraire le taux de fausses promotions mesuré sur des témoins plantés) ne vaut que contre des tricheurs que l'on sait planter. Un tricheur d'une forme non plantée la contourne.
6. **Filtre de compatibilité (vérification de satisfiabilité).** Le filtre ne vérifie que les plages **déclarées**. Il suffit de déclarer des plages compatibles et fausses : coût nul.
7. **Tous à la fois, coût nul.** Le même tricheur scripté, muni d'une étiquette rare semée et d'une plage déclarée compatible, passe tous les instruments ensemble : couplage d'opérateurs, criblage, juge, TQ et filtre de compatibilité. C est la seule des deux propositions à injecter ce tricheur (contrôle 2 de l'expérience 3). Mais elle le mesure dans **un seul** bras d'**une seule** expérience, pas dans l'expérience 1 ni dans l'expérience 2.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Expérience 1 : puissance variée.** Courir le cœur riche à deux niveaux de force (petits effets, grands effets). Sans cela, l'issue mesure π et non l'entropie (C1).
2. **Expérience 1 : grille alignée et fenêtre décalée.** Aligner les cases sur 0,12 et 0,26, **et** décaler la fenêtre d'un demi-pas de case. Il faut séparer l'artefact de grille que C a trouvé de la valeur propre de la fenêtre. C diagnostique cet artefact sans prévoir le contrôle qui l'élimine.
3. **Expérience 2 : restriction au hasard.** Restreindre RA à un sous-vivier aléatoire de 30 %, préenregistré, et comparer la fenêtre à cette restriction plutôt qu'à RA global. Ajouter aussi l'appariement sur la fréquence et le retrait des substituts (comme A5).
4. **Expérience 3 : criblage aveugle.** Courir un bras qui crible 120 filles au hasard, puis teste 32 filles au hasard. Il isole la part du gain qui vient de Δ_syn de celle qui vient du nombre de filles touchées.
5. **Expérience 3 : calibrage séparé.** Prendre les 15 tirages de criblage hors des 50 de calibrage du juge. Puis courir un monde v ≡ 0 avec sélection : le taux de promotion doit rester ≤ α.
6. **Expérience 3 : coût de fusion explicite.** Faire varier le rapport « coût de fusion / coût de test » sur au moins deux valeurs préenregistrées (illustratives) et lire si le signe de D se maintient.
7. **Partout : le tricheur connu.** Injecter « parent + loi aveugle » dans les expériences 1 et 3 pour tous les bras, et mesurer la part du budget qu'il capte.

---

## Ce qui reste commun et non couvert (attaque, pas fusion)

- **Le juge d'abord, dans les deux propositions.** A et C bâtissent leurs comparaisons d'allocateurs sur le juge v1, dont P exclut le seul trou connu. R1 a déjà posé que la première expérience est « le critère résiste-t-il aux tricheurs ? ».
  - Si « parent + loi aveugle » est promu au-delà de α, **toutes** les métriques « découvertes vraies par dollar » de A et de C cessent d'être interprétables : elles comptent des filles que le juge promeut, pas des filles vraies.
  - Si ce tricheur reste ≤ α et qu'une fille vraie de force 1,0 est promue souvent, les duels d'allocation deviennent lisibles.
  - Ni A ni C ne pose ce préalable sous cette forme exacte.
- **Un biais de P hérité par A et C.** Dans P, D₁ compare la fenêtre au « meilleur des deux appris choisi par sa moyenne dans ce monde ». C'est une sélection faite après coup, que l'intervalle par rééchantillonnage ne corrige pas. Elle avantage les comparateurs, donc pénalise la fenêtre. Le meilleur doit être choisi à l'intérieur de chaque rééchantillonnage, ou fixé d'avance.

FIN-DE-CELLULE