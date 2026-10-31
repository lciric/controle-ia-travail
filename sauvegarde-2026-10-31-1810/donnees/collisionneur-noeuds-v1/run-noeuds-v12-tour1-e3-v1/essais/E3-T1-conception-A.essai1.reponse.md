# Cellule A — tour III.1 — nœuds de décision du 31 octobre 2026 (question v12)

Pièces lues : les 26 pièces des faits v2. Aucune pièce absente ni coupée au sens de la règle 2, hormis les retraits déclarés « [retiré, règle 2] » et la phrase retirée de la pièce 24. Je n'ai pas vu l'annexe du tour 2. Convention : VÉRIFIÉ = chiffre ou citation d'une pièce scellée et contrôlée par un lecteur neuf ; RAPPORTÉ = écrit dans une pièce, non recontrôlé ; OBSERVÉ-NON-AUDITÉ = mesure d'un auteur sans contre-calcul ; HYPOTHÈSE = conjecture (la mienne ou celle d'une pièce).

## 0. Ce que la question suppose sans que ce soit établi (livrable a)

| # | Supposition | Statut | Conséquence |
|---|---|---|---|
| S1 | L'échec de V5 vient de la définition, non du code | OBSERVÉ-NON-AUDITÉ (pièce 2, 200 mondes, une graine de flux ; le verdict R13, pièce 1 § A.3, dit ne pas l'avoir vérifié par calcul) | N1 : toute option A, B, D repose dessus |
| S2 | Le seuil 0,5 est « au niveau du bruit » même à lois égales | OBSERVÉ-NON-AUDITÉ (erreurs types naïves, pièce 2 § 1.4) | N1 : D est condamnée par un chiffre non audité |
| S3 | Le vocabulaire du contrôle des IA est absent des 37 960 concepts | OBSERVÉ-NON-AUDITÉ (comptes de chaînes, pièce 20 SD-4 § 5 ; la question le marque SUPPOSÉ) | N3, N9 : le « substitut » est acquis, mais non son étalonnage |
| S4 | La loi a priori des niches (n6 = 0,05) | HYPOTHÈSE déclarée (pièce 11 § 6 ; contredite par la contre-lecture CA1-06) | N4 : 0,59–0,67 et 0,25–0,36 sont des fourchettes sous hypothèse |
| S5 | L'intention de A21 est « aucune décision ne dépend d'un résultat ni de son rattachement » | RAPPORTÉ (CL19, pièce 12, lecture de CP5-08) | N5 : l'option (a) n'est compatible qu'avec cette lecture |
| S6 | Un classement de bras sur mondes synthétiques vaut pour le domaine réel | HYPOTHÈSE (nulle pièce ne le mesure) | N11 (3) |
| S7 | Les dates de coupure des proposeurs sont connues | HYPOTHÈSE (aucune pièce) | N11 (2) : « ponts publiés après la coupure » n'est pas opérationnel tel quel |
| S8 | « À 8 fusions par bras, un retrait est hors de portée » | HYPOTHÈSE de la question, calculable (voir N11 (1)) | N11 |
| S9 | Le prix de l'évasion pour l'attaquant est transférable hors de Llama-3-8B et de SQLEval | HYPOTHÈSE ; les extraits p. 3, 23, 26 sont VÉRIFIÉS sur PDF (pièce 24), leur portée non | N10 |
| S10 | Le calendrier N6 (verdict vers le 27 novembre) | SUPPOSÉ par l'auteur (pièce 15, DL-2) | N6, DL-2 |

## N1 — Bisociation à deux espaces

**Option : B, complétée par une option manquante F.** Confiance 0,65.

Argument. (i) La liste d'arrêt elle-même prescrit, pour « validation ratée », une nouvelle version R12 (pièce 3, ligne 1 de la liste ; VÉRIFIÉ par le verdict, pièce 1). La ligne « paramètre modifié après lecture → R1 » vise une modification *dans le même run* ; les deux lignes ne s'opposent que si l'on confond version nouvelle et correction en route. Redéfinir après lecture est donc défendable, à quatre conditions : (1) V5 est une garde de plomberie, pas un contraste de décision : aucun monde de décision n'a été tiré (journal « ARRET validation (code 2) », pièce 1, VÉRIFIÉ) ; la v3 doit montrer, ligne par ligne, que le changement ne touche aucun booléen des tables 1 et 2 ; (2) graines de validation neuves (les indices 0–299 et 990000–990199 sont lus) ; (3) l'ancienne grandeur reste rapportée (B) ; (4) **puissance** : le seuil de la nouvelle V5 doit être ≥ 3 erreurs types au-dessus de la valeur attendue à lois égales, sinon on reproduit le défaut de S2. T2 (erreur type 0,04–0,11, RAPPORTÉ) satisfait (4) ; D (0,33 pour 0,29–0,46) ne la satisfait pas ; C est insuffisante sur ses propres chiffres ; E n'est pas motivée, l'échec n'étant pas un échec du générateur sous S1.

(ii) Ce que T2 abandonne : le risque CB-05 (« la rareté ne doit pas séparer vrai de faux ») sur l'étiquette *retenue*, celle que les bras voient ; vrai d'opérateur et proche y diffèrent d'environ 1,4 (pièce 2, OBSERVÉ-NON-AUDITÉ). **Option F (manquante) : remplacer la moyenne par statut par une épreuve directe du risque** — en validation, un bras placebo « rareté seule » (choisit les 12 paires dont l'étiquette retenue est la plus rare, sans lire κ) ; V5′ = sa précision ne dépasse pas celle de c (tirage uniforme) de plus d'une marge gelée (illustratif : 1,5 point, deux erreurs types à 300 mondes avec σ ≈ 11, pièce 3 S14). Un déclencheur d'audit, non un arrêt, parce que d1c lit déjà « la plus rare », et qu'une précision du placebo proche de celle de d1c dirait que la rareté porte la vérité à elle seule.

**Duel (B4).** H_A : à lois égales, V5 scellée échoue par bruit ≥ 30 % du temps (S2 vraie). H_B : V5 scellée échoue < 10 % à lois égales (le seuil était discriminant, le générateur est en cause). Métrique : part de jeux de 300 mondes où l'écart max > 0,5, sur mondes où S16d est forcée pour tous les statuts (variante G3 avec λ = 0, exclue de l'expérience mais admise pour cette seule calibration). Contrôle négatif : le même calcul sur les trois statuts à concept rare du générateur scellé. H_A falsifiée si < 10 % ; H_B falsifiée si ≥ 30 %. Issue H_B : option C redevient recevable et B perd son motif.

**Pire cas** : V5-T2 passe, la fuite par rareté existe, les bras l'exploitent → verdict « N adoptée » sur un artefact. Garde : F, plus l'audit N_PCg déjà écrit.

**Pièce sans dépense** : rejeu du diagnostic avec une seconde graine de flux, 300 mondes, erreurs types par bootstrap de mondes (non naïves), et le tableau « précision de c, d1c et placebo rareté par statut » sur les mondes d'essai.

## N3 — D-j (Gu-Krenn sans reproduction préalable)

**Option : oui, sous condition.** Confiance 0,6.

La condition de reproduction est logiquement déconnectée du bras : HA (pièce 20 N9-1) valide leur modèle sur leur domaine ; le bras de la course sera, sous S3, un substitut sur une autre source, qui teste « leur méthode, pas leur modèle » (pièce 20 SD-4 § 5, RAPPORTÉ). Reproduire ne dit rien du substitut ; ne pas reproduire ne l'invalide pas. **Option manquante : « oui, conditionné à une épreuve propre du substitut à É0 »** : essai de S31 sur la moisson (déjà exigé, CP5-01) complété d'un nul — les paires retenues par S31 doivent différer d'un tirage uniforme parmi les paires candidates sur une grandeur sans juge (part de paires « jamais reliées » à degré apparié) ; sinon le bras est le bras hasard retiré par R-634 sous un autre nom.

Duel : H_A : S31 classe les paires jamais reliées au-dessus de l'uniforme (aire appariée > 0,6, illustratif, à geler) ; H_B : aire ≤ 0,55. Contrôle négatif : S31 sur un vocabulaire permuté entre fiches. H_A falsifiée → bras compté « substitut non discriminant », gardé en exploratoire mais hors de toute comparaison N11. Pire cas : bras indiscernable du hasard pendant toute la génération 1 ; garde : étiquette « exploratoire » et la règle N11 qui le retire sur l'oracle, non sur le juge. Pièce : la sortie de l'essai S31 (sans dépense, moisson déjà là).

## N4 — Annexe du bras méta

**Option : (a), avec deux corrections qui ne sont pas des options et une mesure ajoutée.** Confiance 0,55.

Pourquoi (a) : à ≤ 10 fiches et une paire méta, le pré-pilote ne peut de toute façon éprouver ni le classement ni le contraste profil / hors profil (pièce 10 § C, RAPPORTÉ) ; il éprouve la chaîne. (b) change le plan et le devis ; (c) et (d) vident le profil de sens ; (e) rouvre R-638. Corrections obligatoires avant approbation : CA1-01 (n1–n2 dans le profil alors que le programme les fusionne : relever c(n1, n2) ou fusionner) et CA1-03 (n5 sans partenaire : à écrire en tête). **Mesure ajoutée (option manquante f)** : le pré-pilote lit les niches des 28 rendus (les lecteurs sont déjà payés pour les fiches non aiguillées ; pour les autres, coût à chiffrer, illustratif < 2 USD aux bases de 60 lectures à 1,5 USD, pièce 9) et **mesure la loi a priori des niches**, qui remplace S4 avant la course. C'est la pièce qui tranche la fréquence du profil ; le pré-pilote devient utile au profil même sans le tester.

**CA1-04** : règle cohérente plutôt que liste ad hoc — ne compter aucune structure *imposée par le texte I* (D1, plancher apparié, et les trois structures séquentielles si le glossaire les impose, CA1-04), compter les autres, jeux de données D2 et D3 compris (R-638 les nomme). Le critère « imposé » est décidable d'avance sur le texte I, sans lire de fiche.

Duel : H_A : la loi mesurée donne P(zéro paire du profil à 10 fiches) ≤ 0,2 ; H_B : ≥ 0,4. Contrôle négatif : lecteurs sur fiches à niches permutées (doit donner la fréquence attendue sous le prior uniforme). Pire cas : le repli seul éprouvé, le bras « méta » n'est pas méta en génération 1 ; garde : nom du résultat « chaîne éprouvée, profil non éprouvé » et compte « hors profil » dans N11.

## N5 — Règle A21

**Option : (b)**, avec (d) manquante. Confiance 0,6.

Sous (a), le processus qui détient la clé écrit lui-même le journal qui atteste qu'il ne l'a lue qu'en É5 : l'aveugle repose sur le code (pièce 13, VÉRIFIÉ comme inconvénient écrit). Sous (b), la clé ne franchit jamais la frontière du processus : A21 reste vrai à la lettre et l'artefact R5 est simple (la boîte qui renvoie une liste par témoin est refusée par un validateur de schéma côté orchestrateur). Le coût est une pièce et une interface, éprouvables sans dépense. **(d) manquante** : S18/S19 (indiscernabilité P/N par la forme) se calculent à la construction des témoins (É1, côté session-depot, avant tout rôle), pas en É5 ; il ne reste à la boîte que S20/A6/S6, trois comptes. Cela réduit l'interface. (c) change M1 : à écarter.

Choix de code : 1 — confirmer (la v55 n'ouvre rien après un nœud). 5 — exclure, mais compter « défaut non vu » à part de « ambigu » dans A5, sinon A5 mélange deux défauts de construction. 8 — lecture littérale acceptable, C12 recalculée dans le brouillon suivant. 10 — geler au préenregistrement, la crête comprise. Plafond : par génération, ligne de GO ≥ N × S17.

Duel : H_A : la boîte tenue par session-depot rend « passe / nœud + comptes » identiques à `_boite_e5` sur un jeu de témoins d'essai (cas sain) et refuse toute sortie par témoin (artefact) ; H_B : écart ou fuite. Pire cas : la boîte n'est pas prête au 7 novembre ; garde : le pré-pilote attend déjà l'annexe (D-h a), le chemin critique ne change pas si la boîte est écrite en parallèle. Pièce : spécification d'interface + ses deux essais R5.

## N6 — DL-1 à DL-13

| DL | Option | Conf. | Raison ; garde ; pièce |
|---|---|---|---|
| 1 | (2) | 0,6 | Seule option où l'iVAE est jugé là où son théorème s'applique ; B-hors descriptif garde la robustesse. Garde : la portée écrite « latentes seulement ». |
| 2 | (2) | 0,5 | Le temps mural (S10) est SUPPOSÉ ; garde existante : arrêt avant mondes de décision si σ̂ ou temps dépasse. Pièce : mesure des temps unitaires sur 20 mondes (déjà au plan). |
| 3 | (2), avec déclencheur d'audit | 0,5 | R2⁻ teste une symétrie de plomberie ; une ligne décisionnelle sans puissance propre peut disqualifier une méthode juste. Déclencheur : recouvrement en R2⁻ < 0,5 × recouvrement en R2. |
| 4 | (1) | 0,7 | Donner la cible, c'est donner l'identification. |
| 5 | (1), sous condition | 0,55 | Condition (VS5-03) : PUISθ et « puissance réalisée » écrits pour ρ = 0,70, niveau de qualification de la Table Bθ, non pour 0,85. (1 bis) si le calcul à 0,70 ne passe pas à 16 ans. |
| 6 | (1) pour les trois PDF versés ; LiNGAM reste SUPPOSÉ | 0,7 | Aucun chiffre LiNGAM n'entre dans une règle ; marquer M3 « hypothèse non lue sur PDF ». |
| 7 | (2) | 0,7 | Cinq seuils vraiment ouverts. |
| 8 | (4) | 0,6 | Une définition, aucun choix après lecture ; l'inconvénient (années de référence dans u) est déclaré sans conséquence. |
| 9 | (2) | 0,6 | Seuils 0,20 et 0,05 sans source : descriptif. |
| 10 | (3) | 0,6 | (2) est « presque vraie par construction » (pièce 15). |
| 11 | (1) | 0,7 | 1,25 h pour le contrôle commun manquant. |
| 12 | (1), raison réécrite | 0,5 | VS5-01 : l'argument M1 est inexact ; il reste le chemin κ fermé au premier ordre (M § 26, RAPPORTÉ). Garde : audit d'équilibre par strate ; pour T1, rapporter le résidu non linéaire. Pièce : rejeu du monde jouet avec pentes différentes par strate. |
| 13 | (1), plus déclencheur d'audit à la place de l'option 2 | 0,5 | Option manquante : l'écart > 0,15 sur D_amp déclenche un audit R4, non une perte de qualification sur 30 mondes sans puissance. |

Duel transversal pour N6 (la hiérarchie « périmètre interne » de DL-2, 4, 6) : H_A : aucun des trois ne change une table ; H_B : au moins un en change une. Sur le texte, DL-4 (1) change la Table A (méthodes) : DL-4 n'est pas « interne ». DL-2 et DL-6 le sont.

## N9 — D-GK-1

**Option : (a).** Confiance 0,7.

(b) conditionne sur l'issue 2023 et retire d'abord les positives les mieux classées (pièce 20 N9-1, RAPPORTÉ) ; (a) est le test propre, et la lettre « 2024–2026 » est servie par la ligne d'information. **Option manquante (c)** : (a) avec l'aire rapportée par cohorte de première liaison (2023 ; 2024 ; 2025–2026). Elle rend lisible le pire cas de (a) : des positives 2023 « déjà dans le tuyau » (articles soumis en 2022) qui gonflent l'aire ; si l'aire 2023 dépasse l'aire 2024–2026 de plus que l'attente écrite (0,01–0,05, SUPPOSÉ), déclencheur d'audit. Duel : H_A : aire par cohorte décroissante de plus de 0,05 (fuite de proximité temporelle) ; H_B : aires à 0,03 près. Contrôle négatif : étiquettes permutées entre paires de même case degré × âge (aire ≈ 0,5). Garde R5 déjà au texte (attachement préférentiel, Simpson). Pièce : le texte v3 avec la cohorte.

## N10 — Robustesse adaptative dans la course

**Option : (b), avec une pièce de préparation sans fusion.** Confiance 0,65. Les éléments v10 et v11 ne changent pas l'option : ils la motivent. (a) rouvre un texte que le pré-pilote doit éprouver ; (c) est un devis sans résultat de pilote lu. Le mot du directeur (« si c'est confirmé ») situe la question après le calcul décisif du pilote (N = 100, R-739), donc en génération 2. Ce qui peut se faire avant : verser Bailey et collègues (arXiv 2412.09565, PDF empreinté) et le verdict du pilote dans les pièces de la génération 2, avec Q2 « non exercée » marquée résultat local (pièce 22 « Portée », VÉRIFIÉ).

**Leviers, niveau méthode (HYPOTHÈSES, sauf mention).** Le fait VÉRIFIÉ : l'évasion contre des sondes sur plus de couches dégrade SQLEval (p. 3, p. 23), l'orthogonalité coûte une sortie incohérente (p. 26). Le levier n'est donc pas un moniteur plus riche (qui tombe aussi, RAPPORTÉ via la question), mais le **couplage détection–tâche** : (i) un second canal qui mesure la qualité de la tâche sur la sortie (hors de l'espace latent) ; l'attaquant ne peut l'améliorer sans réduire l'obfuscation ; (ii) sondes sur beaucoup de couches, parce que le prix croît avec leur nombre (corrélation négative, IC entièrement négatif, p. 23) ; (iii) archive des attaques en réentraînement (OAT renchérit ×64 en pas de gradient, 256 → 16 384, p. 26, RAPPORTÉ) sans fermer. **Mesure** : la courbe prix–évasion ; duel : H_A : il existe un budget d'attaque B où rappel < 5 % à 1 % de fausses alertes **et** performance de tâche ≥ 95 % de la référence (le prix est bas) ; H_B : sous B, tout point à rappel < 5 % a une performance < 80 % (le prix est élevé). Contrôle négatif : attaque contre un moniteur aléatoire (rappel nul sans perte de tâche attendue). Chaque issue falsifie l'une des deux. **Vérification hors programme** : reproduire sur Llama-3-8B-Instruct (modèle ouvert nommé dans l'extrait, VÉRIFIÉ) par une équipe sans accès au programme ; ordre de grandeur RAPPORTÉ : 10 h sur une carte graphique pour une attaque contre OAT (p. 26), 10 min sans OAT ; coût illustratif 20–50 USD par courbe sur une carte louée.

Pire cas de (b) : la génération 2 reçoit « le tirage est inutile » comme acquis ; garde : la lecture R-739 (1) (« plafond de la classe, non preuve ») recopiée dans la question de génération 2.

## N11 — Règle de reconduction et ponts plantés

**(1) La règle.** Grandeurs par bras sur l'oracle synthétique, par condition M_bien et M_moyen : précision sur 12 (vrai conceptuel et vrai d'opérateur comptés vrais ; proche et surface comptés faux mais rapportés à part comme « erreur de proximité » et « erreur de surface » : un bras qui n'échoue qu'en proche est plus réparable qu'un bras qui promeut la surface) ; faux rejetés = part des ponts faux plantés absents de la sélection ; coût par vrai trouvé = dépense + calcul ÷ vrais promus. **Critère de retrait** : bras i retiré si ub95 Δ(i, meilleur) < −θ dans **les deux** conditions synthétiques **et** si son rang sur E1′ et sur les ponts plantés n'est pas meilleur que sur le synthétique (concordance, point 3). θ illustratif : 3 points de précision. **Part d'exploration** : jamais moins de deux bras ; un bras retiré revient si une génération ultérieure change la classe de fiches (règle écrite, pas automatique). **Puissance** : avec σ ≈ 11 à 15,3 points (pièce 3, S14–S15, RAPPORTÉ), un écart apparié de 3 points est détecté avec 0,99 à 600 mondes contre 2 400 (A4, A6 : même raison) ; l'expérience v3 fournit donc la puissance pour un retrait à 3 points sans monde supplémentaire. Pour les fusions : à 8 par bras et une issue binaire, l'erreur type d'une proportion vaut au moins 0,17 ; distinguer 0,5 de 0,25 exige ≈ 60 fusions par bras à puissance 0,8 (illustratif, binomial) ; S8 est confirmée : la course 2 ne décide aucun retrait, elle rapporte. E1′ : puissance à calculer sur la taille de la base de ponts datés, non servie (pièce 19 : « A et D désignent une base assez grande », sans nombre).

**(2) Ponts plantés.** Source : la seule qui ne suppose pas S7 (dates de coupure inconnues) est un pont réel **dont le proposeur ne reconnaît pas la source** : vérification mécanique à É0, titre et résumé de l'article-pont soumis au proposeur, réponse « connu / inconnu » et date ; un pont reconnu est exclu. Plantation : les deux fiches-parents sont réécrites au gabarit par le rédacteur (comme les témoins), insérées dans le vivier à l'insu des rôles ; S18/S19 (indiscernabilité par la forme) s'appliquent aux parents comme aux témoins P/N. Nombre : illustratif 4 ponts, 8 parents, ≤ 15 % du vivier, pour borner la contamination (un pont planté retiré au tirage ne doit pas vider le vivier d'un bras). « Trouve » : premier niveau mécanique — le bras apparie les deux parents (identifiants opaques, aucun juge) ; second niveau — un juge de correspondance, aveugle au bras, compare l'hypothèse de la fusion à celle de l'article-pont (tolérance : même affirmation centrale, avec 4 leurres par pont, précision du juge mesurée sur ces leurres). **Risque de dissemblance** : les ponts publiés sont « trouvables » par construction ; mesure : taux de découverte d'un tirage uniforme et du bras basique ; un pont trouvé par l'uniforme à plus de 50 % (illustratif) est trop facile et sort du compte.

**(3) Transport.** Condition : concordance des classements des trois instruments (synthétique × 2 conditions, E1′, ponts plantés), mesurée par un W de Kendall sur les rangs de bras ; retrait permis seulement si le bras est dernier sur au moins deux instruments et jamais premier. Duel : H_A : W ≥ 0,7 (les bras se classent de même partout) ; H_B : W ≤ 0,3. Contrôle négatif : classements sur bras à sorties permutées (W attendu près de 0). Si H_A est falsifiée, la règle (b) ne porte rien et seul (c) décide — ce qui, par (1), n'est pas décidable à 24 fusions : le directeur doit alors choisir entre attendre E1′ ou financer plus de fusions. Vérification hors programme : les ponts plantés et le juge de correspondance sont une pièce publiable avec ses leurres ; un tiers peut rejouer le second niveau.

**(4) Pré-pilote.** Oui, comme M6b : une étape protégée hors porte, 2 ponts illustratifs, pour éprouver la **chaîne** (insu, appariement mécanique, juge de correspondance sur leurres), non le taux. Cas sain R5 : une paire de parents que le bras basique apparie par construction (concept rare partagé) ; artefact : un parent à titre contenant celui du pont (détecté, comme la ligne 31). Effet sur N4 : aucun si l'étape est hors porte et hors annexe ; le gel du pré-pilote n'en dépend que si le plan des fonds change (D-i (2) tranché : 28 + 4 ; ajouter 8 parents est un changement de plan à chiffrer, nœud de dépense). Ce qui manque : le coût des 8 parents et du juge de correspondance ; la liste des ponts choisie par session-depot hors de la vue de conv-audit (comme DEP2c).

## Instruments nommés (livrable c)

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| V5 (N1) | taux d'échec à lois égales (S2) | mondes G3 λ = 0 contre statuts rares du scellé | aucune : le seuil doit être ≥ 3 erreurs types |
| S31 substitut (N3) | aire appariée, fausses alertes = paires reliées classées « jamais reliées » | paires appariées degré × âge | tirage uniforme |
| Lecteurs de niches (N4) | kappa ≥ S28 ; loi mesurée | 28 rendus | niches permutées |
| Boîte É5 (N5) | identité des comptes, 0 fuite par témoin | témoins d'essai | validateur de schéma |
| Juge de correspondance (N11) | détection sur ponts, fausses alertes sur 4 leurres par pont | parents indiscernables par forme | appariement d'identifiants |
| Courbe prix–évasion (N10) | rappel à 1 % FA contre performance de tâche | même modèle, même tâche, moniteur aléatoire | moniteur aléatoire |

## Ancrage matériel (livrable d)

N1, N4, N5, N11 (1) : processeur seul, aucune dépense (règles du programme). N6 : 113,9–118,6 h de calcul (pièce 15, RAPPORTÉ). N3 : essai S31 sur moisson existante, sans dépense ; la reproduction HA exige une machine louée, 8–30 h de processeur par valeur d'IR (R-873, RAPPORTÉ). N4 (f) : lectures supplémentaires, illustratif < 2 USD. N11 (2) et (4) : rédaction de 8 parents, illustratif 1–2 USD aux bases du rédacteur (É1 1,8 USD pour 28 squelettes, pièce 4, RAPPORTÉ) ; juge de correspondance, illustratif < 1 USD. N10 hors programme : Llama-3-8B-Instruct, une carte graphique, 10 min à 10 h par attaque (p. 26, RAPPORTÉ), illustratif 20–50 USD par courbe.

## Liens et ordre

N1 d'abord (la v3 porte N11 (b) et la décision 1 de la synthèse : la grandeur de V5 est celle de « étiquette de pont indépendante du canal ») ; puis N4 (f) et N11 (4), parce que le gel du pré-pilote en dépend ; N5 (b) en parallèle, hors chemin critique ; N3 et N9 ensemble (le substitut et HB sont deux instruments distincts, à ne pas confondre dans les registres) ; N6 à son calendrier propre ; N10 après le calcul décisif du pilote.

FIN-DE-CELLULE