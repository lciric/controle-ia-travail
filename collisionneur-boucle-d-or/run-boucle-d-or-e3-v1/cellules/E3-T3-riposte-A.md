# Proposition A — Tour III.3 : riposte

Pièces reçues : les faits (A, P, R1, R2, T, C), la question, ma conception E3-T1-A, les deux équipes rouges E3-T2-B et E3-T2-C. Toutes présentes, lisibles, sans coupure. Je ne réponds qu'aux sections qui visent A ; je me sers de deux contrôles que B et C adressent à d'autres propositions, en le disant.

## 0. Correction d'intégrité (B, « manquements »)

Acceptée sans réserve. J'avais étiqueté « VÉRIFIÉ (attribution) » des références citées de mémoire (Uzzi et collègues 2013 ; Fleming 2001 ; Wang, Veugelers, Stephan 2017 ; Foster, Rzhetsky, Evans 2015 ; Boudreau et collègues 2016 ; Rzhetsky et collègues 2015 ; Swanson 1986 ; Shi et Evans 2023). Aucun fait servi ne les vérifie. Leur statut est **« référence à vérifier »** pour chacune, titre, revue, année et pages compris. Ce qui reste vérifié dans ma pièce : l'arithmétique sur P (82,5 % des filles hors bande), et l'identité des classements par H₂(p)·4p(1−p) et par |p − ½|.

## (a) Les attaques, une par une

| Attaque | Verdict | Raison ou transformation |
|---|---|---|
| **B-A1 / C-2** : le duel 1 est vrai par construction ; son verdict suit la loi de c | **Acceptée** | Un verdict « en moyenne sur c » mesure le recouvrement de deux intervalles, pas une propriété de l'allocateur. Transformée : le duel 1' rend une **courbe gain(recouvrement)** sous deux lois préenregistrées (B-c-1), et un seul verdict binaire, sur la robustesse au décalage partiel (§ b). Le couplage au duel 3 est dit : seul le duel 3 peut fournir une loi empirique de c, et il ne parle que de cooccurrence. |
| **B-A2 / C-2 (pseudo-comptes)** : cases non alignées ; a priori non spécifié | **Acceptée** | Grille alignée sur 0,12 et 0,26 pour tous les bras, plus une fenêtre décalée d'un demi-pas (je reprends le contrôle 2 que B adresse à C). A priori spécifié : Bêta(2, 2) dans la bande (moyenne 0,5, k = 4), Bêta(1, 1) ailleurs ; variante k = 12 pour lire le regret. Mondes hostiles de P (bords, décroissant) courus sur ce bras (C-c-1). |
| **B-A3 (i)** : le duel 2 ne départage que des mondes qu'il a écrits | **Acceptée en partie** | Le monde de P n'a aucun lien causal parents → fille ; c'est une critique de P que j'avais lue sans en tirer la conséquence. Le duel 2 ne dira pas « quelle variable compte dans le monde réel » ; il dira **si une synergie, quand elle existe, est détectable à coût compté, et si s la remplace**. C'est une question d'instrument, pas de monde ; je la pose comme telle. La question « quelle variable dans le réel » n'a pas de test sans archive du pôle, et l'archive est filtrée (C contre B, faille 2 : j'y souscris). |
| **B-A3 (ii) / C-1 / C-3** : σ est payé par un budget gratuit ; fuite de l'oracle ; σ exige la fille générée | **Transformées** | Ma définition était ambiguë ; je la fixe : **σ est une propriété de la paire de parents**, calculée sur les tirages **déjà payés** lors du test des parents (survivants, donc testés), tenus hors des agents. Coût marginal nul par construction, aucune issue de la fille observée, et σ est disponible **avant la fusion** — ce qui répond à C-3 : σ sert à choisir quelles paires fusionner, et répond à mon propre point a-6. C-1 a raison que σ est alors constante pour toutes les sœurs : c'est voulu. Pour la variante « σ par fille » (après fusion), le coût est facturé : n₀ ∈ {5, 15} tirages par fille dans un budget total fixé en tirages (B-c-3). |
| **B-A4 / C-c-2** : fuite par le calibrage ; σ sur bruit | **Acceptées** | Tirages de σ disjoints des tirages sur lesquels le juge ajuste le nul. Contrôle v ≡ 0 avec sélection sur σ : promotion ≤ α. σ nul par permutation des issues (C-c-2) ; R² ajusté ; parents colinéaires bruités comme témoin de fausse synergie. |
| **C-4** : s modélisé linéairement perd par erreur de forme | **Acceptée** | Le modèle sur s est à **cases** (8, alignées), non linéaire par construction ; même forme sur σ. La log-perte s'estime sur les tests agrégés de 100 mondes, validation croisée par monde. |
| **B-A5 / C-5 / C-évasion 5** : fréquence confondante, substituts, troncature (Berkson) | **Acceptées** | Le support de d est tronqué des deux côtés (K > 0, jamais cooccurrent) : une monotone peut y faire un pic. Le duel 3' ne teste plus « cloche globale » mais **« non-monotonie conditionnelle à fréquence et K fixés »**, avec strates de produit de degrés et de K, retrait des substituts, et deux signaux injectés : monotone saturé et unimodal (je reprends le contrôle 2 que C adresse à B). Si l'instrument déclare « cloche » sur la monotone injectée, il est invalidé avant toute lecture. |
| **B-A6** : plis fuyant par les termes | **Acceptée** | Plis disjoints en termes (blocs de termes). |
| **B-A7** : l'objectif de sévérité partage l'angle mort du juge | **Acceptée** | Je retire la formulation « parade à la survie facile » : l'objectif pèse la survie facile *sous le nul tel qu'il est*, et rien de plus. Le tricheur « parent + loi aveugle » est injecté dans tous les bras de tous les duels, part du budget captée mesurée (B-c-7, C-évasion 6). |
| **C-6** : −log p_nul est constant, ou dépend de la force déclarée | **Rejetée sur le premier point, acceptée sur le second** | p_nul n'est ni α ni la p-valeur réalisée : c'est la probabilité, **sous le nul composite, de passer le seuil propre à la fiche** (C, § 1, « sévérité attendue »), calculée par le juge hors des agents. Elle varie avec la prédiction chiffrée. Mais C-évasion 1 (bluff de force) est juste : l'allocateur lit une grandeur que l'agent écrit. Transformée en monde « force déclarée décorrélée » (C-c-4) et en règle d'admission (§ b, duel 4'). |
| **B-A8** : le duel 5 oublie « parent + loi aveugle » | **Acceptée** | Batterie complétée par la liste de R1 : parent + loi aveugle, enveloppe harmonique, copie renommée, pari couvert, adimensionnement, jargon rare, fille constante, mélange dilué (C-évasion 3). |
| **B-A9** : « indistincte » ne falsifie rien | **Acceptée** | Règle fixée : l'issue « indistincte » est attribuée à H_B dans tous les duels où H_A affirme une supériorité (la charge revient à la politique informée). |
| **B-scénario 1 / C-évasion 4** : s manipulable lexicalement à coût nul | **Acceptée, et élargie** | C'est un argument contre s comme **entrée d'allocation visible des agents**, quelle que soit la fenêtre. Transformée en test de l'instrument s (§ b, mesure préalable). |
| **C-évasion 2** : sur-apprentissage des 50 tirages par la fille | **Rejetée pour σ-paire, acceptée pour σ-fille** | σ-paire ne dépend pas de la fille ; les tirages des parents sont hors des agents. Pour σ-fille, le pompage est possible : d'où le contrôle v ≡ 0 et la facturation. Le cas « parent sans contenu qui survit à α » (C contre B, évasion 2) s'applique à σ-paire : témoin « parent-bruit » ajouté. |
| **C-évasion 3** : dilution pour viser p = 0,5 | **Acceptée** | Attaque contre l'entropie, que je combats ; elle devient un monde du duel 4' : le tricheur dilué doit capter plus de budget sous l'entropie que sous la sévérité (sinon mon point a-4 est sans effet pratique). |
| **B « commun »** : D₁ choisit le meilleur comparateur après coup | **Acceptée** | Comparateur **fixé d'avance** (Thompson plat sur grille alignée) ; le tri est rapporté à part. |
| **B « commun »** : le juge d'abord | **Acceptée** | C'est déjà mon duel 5 ; il devient le duel 0, élargi (B-A8), et condition d'interprétation de tout « découvertes vraies par dollar ». |

Un principe sort de ces seize réponses, que je pose comme règle de conception (HYPOTHÈSE, à éprouver par les scénarios conjoints) : **une entrée d'allocation n'est admise que si elle est calculée hors des agents, sur des tirages tenus hors des agents, ou observée après paiement**. s lexical, force déclarée et étiquette d'opérateur ne satisfont pas cette règle ; σ-paire et p de promotion observée la satisfont. Le scénario conjoint de B (6) et de C (6) est alors contré non pas par un instrument de plus, mais par le refus des entrées qu'il manipule — reste le juge, que seul le duel 0 mesure.

## (b) Les expériences corrigées

Tout est sur processeur, sans appel de modèle, préenregistré et scellé avant exécution, graine d'exploration 20261027 (P), graine distincte pour confirmation. Budget commun à tous les bras d'un duel, exprimé en **tirages** (un test = 250 tirages ; B-c-3). Dans chaque duel, le tricheur « parent + loi aveugle » est présent dans le réservoir (part illustrative : 10 % des candidates), et la part du budget qu'il capte est une mesure obligatoire. Issue « indistincte » → H_B.

### Duel 0 — Le juge écarte-t-il les tricheurs ? (préalable à tout)

- Batterie (R1 + B-A8 + C-évasion 3) : parent + loi aveugle ; enveloppe harmonique aveugle ; copie renommée ; pari couvert ; adimensionnement ; jargon rare ; fille constante ; mélange dilué « vraie loi × bruit » ; et un **nul exact** (fille aléatoire), pour étalonner la règle (je reprends le contrôle 1 que C adresse à B : une règle « borne supérieure < α » rejette un juge parfait ; j'utilise une **marge d'équivalence** α + Δ, Δ = 0,01 illustratif).
- H_A : chaque tricheur est promu à un taux dont la borne supérieure de Clopper-Pearson est < α + Δ, et le nul exact aussi. H_B : au moins un tricheur a une borne inférieure > α + Δ.
- Contrôle positif : fille vraie à force 1,0 promue à un taux ≥ 0,8 (illustratif) ; sinon le juge n'a pas de puissance et « ≤ α » ne prouve rien.
- 2 000 mondes par forme (illustratif).
- Si H_B : **arrêt** ; aucune métrique « découvertes vraies par dollar » n'est lisible, et l'allocateur doit porter une part du filtrage (la fenêtre retrouve un rôle, mais le juge est à refaire d'abord). Si H_A : la fenêtre ne peut plus se réclamer d'« éviter les triviales » ; il lui reste le duel 1'.

### Mesure préalable — l'instrument s résiste-t-il à la réécriture lexicale ?

Sur les mondes de R2 (vecteur de domaine en fréquences brutes, cosinus 0,54 / 0,28 / 0,03, RAPPORTÉ) : remplacer une fraction f ∈ {0,2 ; 0,4 ; 0,6} des termes de fond d'un article par des termes d'un domaine tiers ; mesurer le déplacement de s. **Seuil** : si, à f = 0,4, s traverse une bande de largeur 0,14 pour plus de 50 % des paires (illustratif), s est **inadmissible** comme entrée visible des agents, et toute fenêtre sur s est hors sujet tant que s n'est pas calculé par le noyau sur un vocabulaire figé hors des agents. Ce n'est pas un duel : c'est une mesure de fausse alerte de l'instrument.

### Duel 1' — Que vaut une bande supposée connue, quand elle est décalée ?

- Monde : contraste v = 0,5 dans la bande vraie [c − w ; c + w], 0,05 dehors, w uniforme sur [0,04 ; 0,12] (illustratif). **Deux lois de c préenregistrées** (B-c-1) : (L1) c uniforme sur [0,06 ; 0,74] ; (L2) c ∼ 0,19 + bruit normal d'écart-type 0,05 (illustratif).
- Bras, tous sur la **grille alignée** (bords à 0,12 et 0,26 ; B-A2) : hasard ; Thompson plat (comparateur fixé d'avance) ; fenêtre fixe de P ; fenêtre fixe décalée d'un demi-pas ; Thompson informé k = 4 (Bêta(2, 2) dans la bande, Bêta(1, 1) ailleurs) ; Thompson informé k = 12.
- Mesure : D₁ = fenêtre − Thompson plat, apparié, par répétition ; 100 répétitions par loi ; en outre, **courbe de D₁ en fonction du recouvrement** r = |bande vraie ∩ [0,12 ; 0,26]| / |bande vraie|, par tranches de r.
- **H_A** : la fenêtre fixe bat Thompson plat dès que r ≥ 0,5 (intervalle de D₁ au-dessus de 0 dans la tranche r ∈ [0,5 ; 1[). **H_B** : elle ne le bat que si r = 1.
- Falsifie H_A : D₁ non au-dessus de 0 pour r ∈ [0,5 ; 1[ → la fenêtre ne tolère aucun décalage ; comme personne n'a mesuré la position de la bande (A, R2, T), elle n'est pas une politique mais un pari. Falsifie H_B : D₁ > 0 dès r ≥ 0,5 → une bande approximative vaut 40 tests d'exploration, et la question devient « d'où vient la bande ? » (duel 3').
- Contrôles : monde plat (aucun bras ne se distingue du hasard, sinon instrument en défaut) ; mondes bords et décroissant de P sur les Thompson informés (C-c-1 : regret des pseudo-comptes, rapporté en découvertes perdues par rapport à Thompson plat) ; si Thompson plat ne bat pas le hasard sous L1, budget trop petit, augmenter avant lecture (P le prévoit).
- Prédiction signée : H_B sous L1 (0,7) ; regret du k = 4 dans « bords » borné par 4 tests sur 40 (0,7).

### Duel 2' — σ-paire est-il détectable, et s le remplace-t-il ?

- Monde : la vérité de la fille est **engendrée par les parents** : parents = lois sur sous-populations ; une fille est vraie avec probabilité g(σ_vrai) (monde « synergie »), h(s) à cases non monotone (monde « domaine »), ou produit (monde « mixte ») ; corrélation s–σ de 0,3 (illustratif) ; monde « indépendant » comme contrôle négatif.
- σ-paire : variance des issues expliquée par les deux prédictions parentales jointes moins la somme des parts séparées, R² ajusté, sur les tirages **du test des parents** (déjà payés, hors agents, disjoints des tirages où le juge ajuste le nul ; B-A4). σ nul par permutation des issues (C-c-2). Témoins : parents colinéaires bruités ; parent-bruit survivant à α.
- Bras : Thompson à cases sur s ; Thompson à cases sur σ ; Thompson à cases sur (s, σ) ; hasard.
- **H_A** : à budget de tirages égal, l'allocateur sur s fait autant de découvertes vraies par dollar que celui sur σ dans les mondes « synergie » et « mixte ». **H_B** : σ bat s dans ces deux mondes, et (s, σ) ne bat pas σ.
- Mesure secondaire : log-perte hors échantillon des modèles à cases sur s, σ, (s, σ), validation croisée par monde sur 100 mondes.
- Falsifie H_A : σ bat s → la similarité de domaine n'est pas la variable, et une entrée admissible (calculée hors agents, gratuite) existe. Falsifie H_B : s fait jeu égal → σ-paire est trop bruité aux tailles de test des parents pour servir, et l'allocation reste sur s — à condition que s passe la mesure préalable.
- Contrôle : monde « indépendant » (aucun bras ne bat le hasard) ; monde v ≡ 0 avec sélection sur σ (promotion ≤ α + Δ, sinon fuite).
- Ce que ce duel ne dit pas : si la synergie compte dans le pôle réel. Il dit si l'instrument la voit quand elle est là.

### Duel 3' — Sur arXiv : non-monotonie conditionnelle de la cooccurrence future

- Données : artefacts empreintés de T (scores, issues, matrices d'avant ; RAPPORTÉ). d = 1 − cosinus des vecteurs de contexte d'avant.
- **Conditionnement** (B-A5, C-5, C-c-3) : strates croisées de produit des degrés (déciles) × nombre de voisins communs K (déciles) ; courbe taux(d) **à l'intérieur** des strates, agrégée par pondération inverse de la taille des strates. Substituts retirés : racine commune, bigramme contenant l'unigramme, distance d'édition ≤ 2 (illustratif). Plis disjoints en termes (B-A6).
- **H_A** : dans la majorité des strates (≥ 8 plis sur 10, pic au même vingtile ± 2 au placebo 2003-2006 / 2007-2010), la régression unimodale bat la régression isotone en log-vraisemblance hors échantillon. **H_B** : l'isotone fait au moins aussi bien, ou le pic est instable au placebo, ou il disparaît à fréquence et K fixés.
- Contrôles d'instrument, **avant** lecture : (i) issues permutées (les deux régressions se valent) ; (ii) signal **monotone saturé** injecté (p = min(c₀ + c₁d, c_max), illustratif) : l'isotone doit gagner, sinon l'instrument fabrique des cloches et le duel est annulé ; (iii) signal unimodal injecté d'amplitude 3 × taux de base (illustratif) : l'unimodale doit le retrouver, sinon l'instrument est aveugle.
- Portée : même sous H_A, l'issue est une cooccurrence lexicale (T), sur un support tronqué (C-5), entre math–physique et cs–physique pour l'essentiel. Elle fournit au mieux un étalonnage de position pour le duel 1' sous L2 ; elle ne dit rien de la vérité. L'impact par citations exige OpenAlex (décision de Lazar).
- Prédiction signée : H_B (0,7) ; le contrôle (ii) retient mon attention plus que le verdict.

### Duel 4' — Allocation après fusion : entropie contre espérance de sévérité, sous bluff

- Étage : filles **déjà générées** (C-3 : c'est le second étage d'allocation ; le premier, avant fusion, est le duel 2'). Chaque fiche porte une prédiction chiffrée ; la sévérité p_nul est calculée **par le juge** hors agents sous le nul composite, à partir de la prédiction (C-6).
- Trois mondes de déclaration : (M1) force déclarée = vraie + bruit centré ; (M2) force déclarée **décorrélée** de la vraie (C-c-4, bluff) ; (M3) M1 plus 10 % de filles « mélange dilué » visant p = 0,5 (C-évasion 3) ; plus le tricheur « parent + loi aveugle » partout.
- Bras : entropie du verdict (P) ; espérance de sévérité gagnée par dollar, estimée en ligne par case ; espérance de promotion par dollar ; hasard.
- **H_A** : l'entropie fait au moins autant de découvertes vraies par dollar que la sévérité dans M1 et M3. **H_B** : la sévérité bat l'entropie dans M3 (le dilué capte le budget de l'entropie) et ne perd pas dans M1.
- Mesure obligatoire : part du budget captée par les dilués, par les bluffeurs (M2) et par le tricheur de nul, par bras. Dans M2, un bras dont la part captée par les bluffeurs dépasse celle du hasard est **inadmissible**, quel que soit son score : c'est la règle d'admission du § a, mesurée.
- Falsifie H_A : l'entropie perd dans M3 → la confusion épistémique/aléatoire (a-4) a un effet pratique à ce budget. Falsifie H_B : entropie ≥ sévérité dans M3, ou sévérité inadmissible dans M2 → la sévérité lue sur la fiche est manipulable et doit être réestimée après paiement seulement ; l'entropie, qui ne lit que des promotions observées, reste admissible.
- Contrôle : monde à forces égales (les deux objectifs se valent, sinon l'écart vient d'ailleurs).

### Ordre

Duel 0 → mesure préalable sur s → duels 1', 2', 4' (en parallèle, même infrastructure que P) → duel 3' (artefacts de T, sans réseau). Coût : processeur seul, de l'ordre de quelques minutes par duel (illustratif ; R2 : 4 000 mondes en 93 s, RAPPORTÉ), 0 USD hors orchestration.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (dans les faits servis).**
- Dans nos essais, la similarité de domaine n'a rien expliqué : le noyau corrigé vaut un tirage uniforme (R2, § 3, RAPPORTÉ), et « champs éloignés » se réduit sur arXiv à math–physique et cs–physique (T, RAPPORTÉ). Toute fenêtre sur s porte donc sur une variable qui, à ce jour, n'a pas de pouvoir mesuré chez nous.
- Le classement « entropie × 4p(1−p) » est identique au classement par |p − ½| (VÉRIFIÉ, mathématique) : le second facteur n'ajoute rien.
- La fenêtre de P exclut 82,5 % des filles (VÉRIFIÉ par arithmétique sur P). P construit son monde « cloche » sur la bande même de l'allocateur (VÉRIFIÉ par lecture) : il mesure une bande juste, pas une bande supposée.
- Le juge v1 exclut le trou « parent + loi aveugle » **par décret** (P, RAPPORTÉ). Rien, dans les faits, n'établit qu'il écarte les triviales : la batterie de tricheurs de R1 est « en cours », C4 absente.
- Sur la littérature : aucune des études que j'ai citées n'est vérifiée sur PDF dans ce tour (statut « référence à vérifier » pour toutes). Ce que j'en retiens comme HYPOTHÈSE : les mesures publiées portent sur des citations ou des brevets, pas sur la vérité d'une hypothèse ; la forme récurrente est une **variance** croissante avec la nouveauté, pas une cloche sur la moyenne ; et une courbe impact–distance observée est filtrée par une évaluation qui pénalise la distance. Une loi de variance, pour un pôle dont l'aptitude est la sévérité survécue (C), appelle un portefeuille, pas une exclusion.

**Ce qui n'est pas établi.**
- Qu'un scalaire de distance entre deux fiches existe et que s le mesure (HYPOTHÈSE) ; et, pire, que s soit admissible : il se déplace avec la pondération lexicale (R2, § 9, 0,11 → 0,28, RAPPORTÉ) et un agent peut le choisir à coût nul (B, C : accepté).
- Que l'entropie du verdict mesure une incertitude sur la vérité plutôt qu'une sous-puissance du test (mon a-4, HYPOTHÈSE), et qu'elle résiste à une fille diluée visant p = 0,5 (C-évasion 3, HYPOTHÈSE).
- Que l'espérance de sévérité soit une parade : elle hérite de l'angle mort du nul (B-A7) et se laisse bluffer par la force déclarée (C-évasion 1). Je retire ma formulation initiale.
- Que la synergie des parents soit la bonne variable : mon duel 2 ne peut le dire que sur des mondes où elle est plantée ; il mesure un instrument, pas le monde.
- Que la rétrodiction de T puisse voir une cloche : son support est tronqué des deux côtés (C-5), et son issue est une cooccurrence lexicale (T).

**Ce que les attaques ont changé dans ma position.** La question « fixer ou apprendre » est mal posée tant que l'entrée d'allocation est manipulable : la vraie ligne de partage passe entre les grandeurs **calculées hors agents sur des tirages tenus hors agents** (σ-paire, promotion observée) et celles que l'agent écrit (s lexical, force déclarée, étiquette d'opérateur). Une fenêtre, fixe ou molle, sur une grandeur de la seconde classe est franchissable à coût nul par un tricheur scripté — c'est le scénario conjoint de B et de C, et je l'accepte. Ma forme « a priori informé » n'y échappe pas : elle ne vaut qu'après la mesure préalable sur s.

**L'expérience à faire en premier.** Le **duel 0** : le juge contre la batterie complète de tricheurs, « parent + loi aveugle » compris, avec un nul exact pour étalonner la règle et une marge d'équivalence. Elle est la condition de lisibilité de toute mesure « découvertes vraies par dollar », chez A, B et C indistinctement ; elle coûte quelques minutes de processeur ; et chacune de ses deux issues décide quelque chose : si un tricheur passe, l'allocation n'est pas le sujet et la fenêtre retrouve un rôle de filtre à mesurer ; si aucun ne passe, la fenêtre perd son argument « éviter les triviales » et doit gagner le duel 1' sous décalage, sur une variable qui aura d'abord passé la mesure préalable. Ensuite, et seulement ensuite, les duels 1', 2' et 4', puis le duel 3' pour une position empirique de bande — avec la réserve que cette position parlera de cooccurrence, pas de vérité.

**Question 5, corrigée.** Adopter une fenêtre fausse : perte bornée par le contraste du monde et mesurée par la ligne « fausse alerte » (mondes bords, décroissant, plat). Écarter une fenêtre juste : perte égale au coût d'exploration de Thompson plat, 15 à 35 % de 40 tests (illustratif), que les pseudo-comptes ramènent à k tests. Mais le coût qui domine les deux, et que ni P ni ma première pièce ne comptaient, est celui d'une entrée d'allocation que les agents contrôlent : il n'est pas borné, puisqu'un tricheur peut capter tout le budget. C'est lui que le duel 0, la mesure préalable sur s et la mesure « part du budget captée » de chaque duel rendent visible.

FIN-DE-CELLULE