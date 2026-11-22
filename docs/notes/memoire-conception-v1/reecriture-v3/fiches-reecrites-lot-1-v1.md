# Réécriture des fiches fautives du mémo, lot 1 (v3)

Lu sur la branche `claude/bibliothecaire-v1`, dans le périmètre de la liste d'autorisation v3. Numéros de ligne relevés par `grep -n` sur `registres/go.md` (`a776b87f…`, 745 lignes) et `registres/decisions.md` (`8f512f60…`, 5 002 lignes), dans leur état présent. Les lignes `GO-2026-11-22-52` (l. 739) et `GO-2026-11-22-57` (l. 744) sont postérieures au scellé de la note v1 (`5b596acc`) : elles priment, et je le dis dans les fiches concernées.

#### [N075-11] Deux regards tels qu'échapper à l'un expose à l'autre : le dilemme plutôt que la décorrélation
- Définition : un second regard se juge au dilemme qu'il pose, c'est-à-dire à une relation que l'honnête respecte et que le dommage viole, de sorte que se cacher de l'un fait apparaître à l'autre. On ne le juge pas à sa décorrélation. Là où l'attaquant défait chaque regard séparément, deux alertes réunies n'ajoutent pas de puissance.
- Synonymes et paraphrases : « deux regards » ; « dilemme » ; « décorrélation » (concept rival) ; « Ce qui vaut : deux regards tels qu'échapper à l'un expose à l'autre » ; « un second regard se juge au dilemme, non à la décorrélation » ; « statistique de relation, non deux marginales ».
- Source : décision N-075 v3, section 1 (définitions, l. 37) et section 3 (énoncé retenu, l. 80) ; `5aed4bab1172b181`. Fondement : `GO-2026-11-21-51`, point 1, `registres/go.md` l. 650 (« Ce qui vaut : deux regards tels qu'échapper à l'un expose à l'autre. : go »).
- État : retenu, `GO-2026-11-21-51` ; rien n'est revendiqué hors du bilan.
- Liens : H5 (diversité des moniteurs ; on y ajoute le silence commun sous attaque) ; HC5 (quorum hétérogène : aucun texte ne l'appelle « dilemme » sans avoir mesuré le silence commun) ; parade « apprentissage à corrélation négative » (l. 146 du programme) ; théorème négatif N-003 (justification interne) ; pince ; cas particulier : le dilemme valeur contre issue (inventaire 1.2) ; l'étau, version « dilemme » de la chute conjointe (inventaire 5.5).
- Ce qui l'attaque : même un dilemme parfait ne descend pas l'aveuglement commun sous 2m − 1 (m : part des attaques neuves que chaque regard manque) ; il ne paie que si chaque regard en voit au moins la moitié (sous supposition ; correction A4). Johnston et al. (2504.08812), McKenzie et al. (2506.24068), Bailey et al. (2412.09565) : pannes communes.
- Inventaire : nouveau pour la règle générale ; son cas particulier « valeur contre issue » est l'inventaire 1.2.
- Historique : v1 et v2 donnaient « dilemme valeur contre issue » comme synonyme et rattachaient la fiche à l'inventaire 1.2. Corrigé en v3 parce que l'inventaire 1.2 décrit un cas particulier, « le terme du milieu du bilan de la pince » (inventaire, l. 33-35), et non la règle générale.

#### [N076-04] La loi de la référence honnête (et la règle d'horizon)
- Définition : quand la loi de l'honnête n'est connue que par m unités, la part d'actes sabotés qui reste cachée cesse de baisser dès que l'horizon n dépasse m ; pour un test sur la moyenne, elle vaut z × √(1/n + 1/m) / μ (palier vers 23,3 % à m = 400 et μ = 0,5, sous supposition d'illustration). Protocole accordé : « Toute accumulation déclare m, n et la source de sa validité ; son horizon ne dépasse pas m, sauf nul par acte. » Au-delà de m, les gains se rapportent « au-delà de la référence » et ne fondent aucun verdict. Le moniteur n'est pas arrêté ; c'est la conclusion qui est plafonnée. La règle est l'application du corollaire 1 de Ker 2010 (charge cachée critique d'ordre √(n + n²/m)), et non un résultat du programme.
- Synonymes et paraphrases : candidat C1 de la note « percée » ; plafond de la référence ; « l'horizon ne dépasse pas m » ; règle d'horizon ; « application du corollaire 1 de Ker 2010 » ; loi en racine qui s'aplatit ; le rappel qui cesse de croître ; trois régimes (référence fixe ; témoins à taux p avec facteur √(1 + 1/p) ; nul par acte).
- Source : N-076 v1, § 2 ; note « percée » § 7.1 ; `49b664c1d6a72fdb`. Fondements : `GO-2026-11-21-57`, `registres/go.md` l. 656 (« la loi de la référence honnête intégrée au programme ») ; `GO-2026-11-22-12`, point 1, l. 699 (promotion seulement après l'essai jumeau contre jumeau) ; `GO-2026-11-22-24`, point 2, l. 711 (réponse 9 accordée) ; réponse 9, l. 89 et l. 192 (`48d4d72e5f1cbcde`) ; R-4767, `registres/decisions.md` l. 4906.
- État : règle de protocole en vigueur, intégrée au programme (`GO-2026-11-21-57`), citée comme application du corollaire 1 de Ker 2010 (`GO-2026-11-22-24`) ; non revendiquée ; sa promotion en revendication (« loi de la référence, mesurée ») n'est accordée qu'après l'essai jumeau contre jumeau, avec une prévision scellée avant (`GO-2026-11-22-12`, point 1).
- Liens : H2 (énoncé inchangé, clause renvoyée) ; lemme d'additivité (hypothèse (c) : la puissance dépend aussi de m) ; jeu de contrôle ; bases boîte noire (même déclaration, R4) ; papier B (effectif utile plafonné à l'inverse de la corrélation) ; plan de la phase 1 (bras « référence honnête ») ; ligne A10 de la note des revendications v3 (réponse 34 : « règle de la référence » citée comme protocole).
- Ce qui l'attaque : la règle « horizon au plus m » redit le corollaire 1 de Ker 2010 (R-4767, l. 4906) ; la loi de la racine est occupée aussi pour des couvertures dépendantes (Filler, Ker, Fridrich 2009 ; seconde lecture sur PDF, R-4769, l. 4908). Autres voisins : Bash, Goeckel et Towsley (loi en racine) ; arXiv 1608.00698 et 1612.09027 (guetteur qui ignore son bruit) ; 2609.23254 (ensemble aveugle d'un moniteur tolérant) ; Ortega-Fernandez et al. ; Wen et al. ; Podkopaev et Ramdas ; Cao ; Singh. Chez Ker, m et n comptent les mêmes objets ; transposé à des exécutions honnêtes et à des actions, le corollaire ne vaut pas tel quel (réponse 9, l. 36). Plancher « tout test » 7,7 % non contre-lu. La règle d'horizon n'est plus revendicable ; ce qui pourrait le rester, si non trouvé imprimé, c'est la mesure chez de vrais agents et la comptabilité jointe audit-moniteur.
- Inventaire : nouveau.
- Historique : v1 et v2 tenaient la règle d'horizon pour revendicable si elle n'était pas trouvée imprimée, et ne citaient ni Ker 2010 ni Filler, Ker, Fridrich 2009 parmi les attaques. Corrigé en v3 parce que la lecture sur PDF (R-4767, l. 4906 ; R-4769, l. 4908) et la réponse 9, accordée par `GO-2026-11-22-24` (l. 711), en font l'application citée du corollaire 1 de Ker 2010.

#### [GO-15] La règle à deux clés : alerte = motif et preuve de dommage au même endroit
- Définition : une alerte n'est levée que si un motif reconnu par un regard et une preuve de dommage tombent ensemble au même endroit. Un motif seul fait monter l'épisode dans la file d'audit prioritaire, ou le moniteur s'abstient ; il n'entre jamais dans les témoins. Une preuve de dommage sans motif relève du plancher d'audit.
- Synonymes et paraphrases : « motif et dommage au même lieu » ; « motif seul : audit, jamais témoin » ; règle à deux clés ; lettre abandonnée, à ne plus écrire comme règle (R-9 de l'erratum 3 v2) : « alerte = nouveauté et preuve de dommage ensemble », « nouveauté seule = mise à jour des témoins ».
- Source : `GO-2026-11-21-51`, point 1, `registres/go.md` l. 650 (lettre d'origine) ; `GO-2026-11-21-61`, point 8 (a), l. 660 (forme réécrite retenue) ; N-075 v3, erratum 3 v2, R-5 à R-10 (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3-v2.md`).
- État : retenu dans sa forme réécrite, `GO-2026-11-21-61`, point 8 (a) ; la lettre de `GO-2026-11-21-51` n'est plus la règle.
- Liens : amendement N-075 ; nouveauté sans étiquette ; plancher d'audit ; règle d'exploitation qui aiguille l'audit, hors du taux de fausses alertes d'une porte (R-10).
- Ce qui l'attaque : le dommage qui se confond avec les échecs honnêtes (question au protocole X, `GO-2026-11-21-57`).
- Inventaire : 2.16.
- Historique : v1 et v2 définissaient la règle par la lettre de `GO-2026-11-21-51` (« la nouveauté seule ne déclenche qu'une mise à jour des témoins »). Corrigé en v3 parce que `GO-2026-11-21-61` (l. 660), point 8 (a), retient la forme réécrite (« motif seul : audit prioritaire ou abstention, jamais les témoins ») et que l'erratum 3 v2, R-9, range l'ancienne lettre parmi les phrases à ne pas écrire.

#### [GO-23] La campagne de dommages plantés par un tiers
- Définition : un tiers plante des dommages dans des produits honnêtes du banc pour mesurer q, la probabilité que l'oracle reconnaisse un dommage qu'il regarde, strate par strate (genre et dose), par une borne exacte. Toute garantie porte le minimum de q sur les strates mesurées ; une strate non mesurée compte pour zéro. L'oracle est corrigé sur le lot d'étalonnage seulement ; le lot final est lu une fois.
- Synonymes et paraphrases : dommages plantés ; « q mesuré par dommages plantés » ; « strate non mesurée à zéro » ; D-8, D-11, D-12 ; échelle a priori des dommages plantés.
- Source : N-075 v3, section 11, point 11 (l. 258), `5aed4bab1172b181` ; réponse de Fable sur les dommages plantés par un tiers, v2 (`docs/notes/protocole-x-dommages-plantes-tiers-v1/reponse-fable-dommages-plantes-tiers-v2.md`, `1ec3cdf81919645b`, l. 100). Fondements : `GO-2026-11-21-61`, point 11 (a), `registres/go.md` l. 660 ; `GO-2026-11-21-66`, l. 665 ; `GO-2026-11-21-68`, l. 667 ; `GO-2026-11-22-20`, l. 707.
- État : accordé : point 11 (a) (`GO-2026-11-21-61`) ; D-11, D-12 et devis, plafond de l'étape 1 à 300 USD (`GO-2026-11-21-66`) ; D-8 (a) (`GO-2026-11-21-68`).
- Liens : plancher d'audit ; banc à vérité plantée ; couverture de l'oracle (D-2).
- Ce qui l'attaque : la confiance chiffrée de départ était jugée basse, d'où le collisionneur (`GO-2026-11-21-61`) ; un oracle fait de lecteurs peut avoir un taux de fausse alerte non nul sur des produits honnêtes (supposé, réponse v2, l. 300).
- Inventaire : 2.1.
- Historique : v1 et v2 disaient que la campagne mesurait « la recapture de l'audit ». Corrigé en v3 parce que la campagne mesure q, strate par strate, dans des produits honnêtes (N-075 v3, point 11, retenu à `GO-2026-11-21-61`, l. 660 ; réponse v2, l. 100).

#### [GO-44] Le lemme d'additivité et Avenhaus et Jaech (1981)
- Définition : à budget total de déplacement fixé, la puissance de détection ne dépend que du total, pas de sa répartition entre les actes. L'énoncé d'origine est occupé et cité (Avenhaus et Jaech 1981). Le programme le revendique dans son application au contrôle de l'IA, par une mesure réfutable : la conservation du déplacement cumulé sous une fragmentation jouée par l'agent.
- Synonymes et paraphrases : D-4 du mécanisme adjudant ; lemme du papier A ; « lemme resserré au reste » ; ligne A3 de la note des revendications v3 ; « il est à nous dans son application au contrôle de l'IA ».
- Source : `registres/go.md` : `GO-2026-11-21-46`, l. 645 ; `GO-2026-11-21-47`, point 4, l. 646 ; `GO-2026-11-21-51`, point 4, l. 650 ; `GO-2026-11-21-61`, point 10 (a), l. 660 ; `GO-2026-11-22-24`, point 2, l. 711 ; `GO-2026-11-22-40`, l. 727 ; `GO-2026-11-22-42`, l. 729 ; `GO-2026-11-22-57`, l. 744 (réponse 34 « go recos Fable »). Réponse 34, ligne A3 et décision 1 (`e5e24f2a39a94d3f`).
- État : revendiqué dans son application au contrôle de l'IA, énoncé d'origine cité (`GO-2026-11-22-42`, qui prime) ; lettre fixée par la décision 1 de la réponse 34, option c (mesure maintenant, énoncé adverse appliqué aux sondes après simulation et avis d'un spécialiste), accordée à `GO-2026-11-22-57`.
- Liens : thèse du papier A ; B3 (lemme entre copies, portée à confirmer) ; réponse 27, à corriger par erratum (réponse 34, décision 2).
- Ce qui l'attaque : occupé dans son énoncé central (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7 ; R-4767, `registres/decisions.md` l. 4906) ; voisins appliqués à citer (Tailor 2510.04303, Ghanem 2608.02698 ; R-4771, l. 4910), qui interdisent « inédit » et « premier à transposer » ; une fragmentation fabriquée sur les scores rend l'énoncé vrai par construction.
- Inventaire : nouveau.
- Historique : v1 et v2 décrivaient un lemme « des preuves s’additionnent » et ne citaient ni le resserrement au seul reste (`GO-2026-11-21-61`, point 10 (a)) ni « on les garde mentionnés » (`GO-2026-11-22-40`). Corrigé en v3 parce que ces deux lignes manquaient, que la réponse 34 (l. 97) donne l'énoncé exact, et que `GO-2026-11-22-57` (l. 744, postérieur au scellé) fixe la lettre de la revendication.

#### [GO-51] Les fausses alertes sur honnêtes imparfaits
- Définition : l'expérience E0 de la réponse 3 mesure les fausses alertes que des agents honnêtes réels mais imparfaits déclenchent. Six décisions de Fable sont accordées : métrique principale de fausse alerte ; sources d'imperfection admises en confirmatoire ; lecture des scores bruts de la référence honnête et déclaration de m ; addendum au plan de G1 et gel des sondes jusqu'à G1, déposés avant E0 ; taille ; tiers qui tient l'oracle, le hachage et le recalcul.
- Synonymes et paraphrases : réponse 3 ; expérience E0 des fausses alertes (à ne pas confondre avec le pilote E0 de la réponse 1) ; « fausses alertes sur des agents honnêtes réels et imparfaits ».
- Source : réponse 3, § 3 et § 5 (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-3/relecture-fable-api.md`, `c069421e151484c9`). Fondements : `GO-2026-11-22-09`, `registres/go.md` l. 696 ; `GO-2026-11-22-12`, point 3, l. 699.
- État : accordé (décisions 1 à 6 de la réponse 3), `GO-2026-11-22-12`, point 3.
- Liens : trois honnêtes de contrôle (inventaire 3.5) ; référence honnête et N-076 (réponse 3, § 3.10) ; porte G1.
- Ce qui l'attaque : —
- Inventaire : nouveau ; au voisinage de 3.5 (trois honnêtes de contrôle) et de 2.19 (b) (netteté de la référence).
- Historique : v1 et v2 rattachaient la fiche à l'inventaire 2.19. Corrigé en v3 parce que 2.19 porte sur la dissociation chez l'honnête et la netteté de la référence, sans saboteur, et non sur les fausses alertes d'honnêtes imparfaits (inventaire, l. 262-265).

#### [RD21-02] Chaîne d'arbitrage d'un point délicat
- Définition : un point délicat passe d'abord par Fable en effort normal ou élevé, puis par Fable en effort maximal s'il ne tranche pas, puis par le collisionneur, puis par Lazar. L'effort maximal est réservé aux questions qui demandent les solutions les plus originales. Sont délicats tout écart à un texte scellé, toute hypothèse ou revendication, tout cloisonnement, toute dépense sans devis contre-lu ; contact, publication, paiement et porte restent à Lazar seul.
- Synonymes et paraphrases : « Fable max seulement pour le plus délicat » ; « points délicats » ; « go recos » avec arbitrage.
- Source : chaîne à deux étages de Fable : R-4515, `registres/decisions.md` l. 4653 (mots de Lazar vers 10:52Z et 10:58Z). Exclusion des points délicats et premier ordre (« Fable 5.2 neuf en effort maximal, puis au besoin le collisionneur, puis Lazar ») : `GO-2026-11-21-27`, `registres/go.md` l. 626, et R-4505, l. 4643 (lecture des « points délicats »).
- État : retenu (mot de Lazar, R-4515, qui précise `GO-2026-11-21-27`).
- Liens : économie de Fable ; « go recos ».
- Ce qui l'attaque : limite d'usage de Fable (R-4512, l. 4650 ; R-4658, l. 4797 ; R-4702, l. 4841).
- Inventaire : nouveau.
- Historique : v1 et v2 attribuaient toute la chaîne à `GO-2026-11-21-27`. Corrigé en v3 parce que `GO-2026-11-21-27` (l. 626) dit « Fable en effort maximal » d'abord, et que l'étage « effort normal ou élevé » vient de R-4515 (l. 4653).

#### [RD21-20] Lemme d'additivité, restreint
- Définition : à budget total de déplacement fixé, la puissance ne dépend que du total, pas de sa répartition, de sorte qu'un dommage diffus et un dommage concentré pèsent autant devant un audit qui cumule. Énoncé d'origine cité (article de 1981) ; revendiqué dans son application au contrôle de l'IA.
- Synonymes et paraphrases : lemme d'additivité ; « lemme resserré au reste » ; « à nous dans son application au contrôle de l'IA ».
- Source : R-4533, `registres/decisions.md` l. 4671 (`GO-2026-11-21-47`) ; R-4538, l. 4676. Fondements : `GO-2026-11-21-47`, point 4, `registres/go.md` l. 646 ; `GO-2026-11-21-61`, point 10 (a), l. 660 ; `GO-2026-11-22-24`, point 2, l. 711 ; `GO-2026-11-22-40`, l. 727 ; `GO-2026-11-22-42`, l. 729 ; `GO-2026-11-22-57`, l. 744.
- État : revendiqué dans son application au contrôle de l'IA (`GO-2026-11-22-42`, qui prime) ; lettre fixée par la décision 1 de la réponse 34, option c (`GO-2026-11-22-57`).
- Liens : N-075 ; mécanisme adjudant ; papier A ; fiche GO-44.
- Ce qui l'attaque : Avenhaus et Jaech 1981 (ossature occupée). Contradiction ouverte, à porter à Lazar : R-4771 (`registres/decisions.md` l. 4910) interdit « inédit » et « premier à transposer » et trouve des voisins appliqués (Tailor 2510.04303, Ghanem 2608.02698). La réponse 34 la range en contradiction 1 et confie à un modèle d'une autre famille, plus un spécialiste, la lecture qui ouvrirait « neuf pour le champ » (décision 4, option c, accordée à `GO-2026-11-22-57`).
- Inventaire : nouveau.
- Historique : v1 et v2 disaient le lemme « retenu sous forme restreinte, à démontrer », sans relever le heurt avec R-4771. Corrigé en v3 parce que « à démontrer » est périmé depuis le retrait comme résultat (`GO-2026-11-22-24`, l. 711) et la revendication dans son application (`GO-2026-11-22-42`, l. 729 ; `GO-2026-11-22-57`, l. 744), et que le heurt avec R-4771 (l. 4910) n'était pas dit.

#### [RD21-39] Banc à lois plantées
- Définition : registre d'affirmations jugé par un oracle hors machine, servi par paires avec le jumeau honnête et un honnête handicapé à dommage égal ; prototype sur processeur. Des mondes de recherche engendrés par programme, à lois plantées, flous à la relecture et exacts en aval ; le dommage d'un sabotage diffus s'y compte en lois vraies perdues et en lois fausses promues.
- Synonymes et paraphrases : C2 ; banc à lois plantées ; banc de recherche à vérité plantée ; banc à vérité plantée ; devin ; handicap ; dose fine.
- Source : R-4553, `registres/decisions.md` l. 4691 (« conception du banc à lois plantées (C2) ») ; R-4577, l. 4715 ; R-4621, l. 4760 ; R-4700, l. 4839 ; N-076 v1, § 4 (« banc de recherche à vérité plantée », « lois plantées »). Fondements : `GO-2026-11-21-57`, `registres/go.md` l. 656 ; `GO-2026-11-21-60`, l. 659 ; `GO-2026-11-22-40`, l. 727 ; `GO-2026-11-22-45`, l. 732.
- État : accordé au lancement (`GO-2026-11-22-40` : « go lancement ») ; ligne de 24 USD sur la clé Luc (`GO-2026-11-22-45`).
- Liens : vérité plantée ; épreuves du devin ; note d'entretien (D-5) ; rôle 3 de l'organisme d'idéation (N-076, § 4, point 2) ; cinq décisions du banc au collisionneur (`GO-2026-11-22-52`, l. 739).
- Ce qui l'attaque : la comparaison peut lire le handicap plutôt que le dommage.
- Inventaire : nouveau.
- Historique : v1 et v2 donnaient un état d'étape 0 (devin et handicap levés sur données simulées, dose fine non levée) ; la v2 proposait de séparer « banc à lois plantées » et C2 « banc à vérité plantée ». Correction rejetée en v3 : le registre nomme les deux et les tient pour un seul objet (R-4553, l. 4691 : « banc à lois plantées (C2) » ; `GO-2026-11-21-60`, l. 659 : « C2, le banc de recherche à vérité plantée ») ; seul l'état est mis à jour, d'après `GO-2026-11-22-40` et `-45`.

#### [RD21-51] Neon et cloisonnement
- Définition : Neon (gemini-4-neon) est juge des deux ancres du bras A ; le servir aussi côté attaquant risquait de croiser les rôles. Lazar a jugé le risque limité, et Neon sert désormais au collisionneur et comme proposeur de l'organisme d'idéation, y compris sur des dossiers côté attaquant.
- Synonymes et paraphrases : Neon ; quarantaine « source Neon » ; juge des ancres du bras A.
- Source : R-4555, `registres/decisions.md` l. 4693 ; R-4564, l. 4702 ; R-4600, l. 4739. Fondements : `GO-2026-11-20-58`, `registres/go.md` l. 589 (Neon juge des ancres) ; `GO-2026-11-21-61`, l. 660 (risque jugé limité par Lazar, « à confirmer par Opus 5.5 et Carbon ») ; `GO-2026-11-21-63`, l. 662 (accord pour recueillir cette confirmation) ; `GO-2026-11-22-33`, l. 720 ; `GO-2026-11-22-37`, l. 724.
- État : tranché par Lazar : Neon ajouté au collisionneur et comme proposeur de l'organisme (`GO-2026-11-22-33`), y compris sur les dossiers 23 (lot en quarantaine) et 24 (nouveaux modes d'attaque) (`GO-2026-11-22-37`).
- Liens : bras A ; collisionneur ; organisme d'idéation.
- Ce qui l'attaque : l'avis d'Opus juge le risque « limité sous conditions » : notes côté attaquant servies seulement après le jugement scellé des deux ancres, sinon quarantaine « source Neon » (R-4600, l. 4739). Les lignes `GO-2026-11-22-33` et `-37` ne disent pas si cette condition est tenue. L'avis de Carbon n'est pas trouvé dans ce que j'ai lu, et Carbon n'est pas un avis indépendant (même famille).
- Inventaire : nouveau.
- Historique : v1 et v2 tenaient Neon « hors des notes côté attaquant jusqu'au jugement scellé des ancres », et la v2 disait le risque « confirmé (GO-61, -63) ». Corrigé en v3 parce que `GO-2026-11-22-33` (l. 720) et `GO-2026-11-22-37` (l. 724) placent Neon sur les dossiers côté attaquant, et que `GO-2026-11-21-63` (l. 662) accorde seulement de recueillir la confirmation, sans la constater.

#### [RD22-08] La sonde comptée en audits économisés
- Définition : la valeur d'une sonde se mesure par le nombre d'audits qu'elle épargne à garantie égale, plutôt que par sa justesse propre. C'est une mesure secondaire au papier A, à côté de la porte G1, avec une prévision scellée avant G1. L'universalité est posée comme limite.
- Synonymes et paraphrases : audits économisés ; facteur d'audits économisés ; sonde accélérateur ; « valeur de la sonde en audits » ; R2 de la réponse 2.
- Source : accord : réponse 2, décision 2, option a (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-2/relecture-fable-api.md`, `542b7bfc86497c0c`, l. 190) ; `GO-2026-11-22-12`, point 1, `registres/go.md` l. 699. Origine de la question : demande 4, R-4766, `registres/decisions.md` l. 4905 (fichier lu alors à l'empreinte `75f4ab9603eba780`).
- État : accordé comme mesure secondaire au papier A, prévision scellée avant G1 (`GO-2026-11-22-12`, point 1).
- Liens : N-075 (« sondes : accélérateur, non garantie ») ; plancher d'audit au hasard ; N-044 (universalité) ; thèse de la réponse 4, suspendue (`GO-2026-11-22-20`) puis remplacée (`GO-2026-11-22-24`).
- Ce qui l'attaque : la garantie vient de l'audit, pas de la sonde ; la mesure peut afficher un gain nul (réponse 2, décision 2).
- Inventaire : 2.1 au voisinage.
- Historique : v1 et v2 fondaient la fiche sur la demande 4 (R-4766). Corrigé en v3 parce que l'accord vient de la décision 2 de la réponse 2, accordée à `GO-2026-11-22-12`, point 1 (l. 699).

#### [RD22-24] L'antériorité par étages (mathématiques nouvelles)
- Définition : la lecture d'antériorité des mathématiques nouvelles se fait par étages successifs plutôt que d'un bloc.
- Synonymes et paraphrases : antériorité par étages ; option (d) du collisionneur (R-4809) ; option A du mot de Lazar (`GO-2026-11-22-42`) : même objet, deux lettres.
- Source : R-4809, `registres/decisions.md` l. 4948 (avis du collisionneur rendu : option (d) à étages) ; R-4835, l. 4974 (appliquée en poste). Fondements : `GO-2026-11-22-40`, `registres/go.md` l. 727 (« lecture d'antériorité par étages ») ; `GO-2026-11-22-42`, l. 729 (« Mathématiques : option A (recherche d'antériorité par étages) « go » »).
- État : accordé et appliqué (`GO-2026-11-22-42`).
- Liens : session des mathématiques nouvelles ; `GO-2026-11-21-38` (portée suspendue à l'avis du collisionneur, d'après R-4809).
- Ce qui l'attaque : —
- Inventaire : nouveau.
- Historique : v1 et v2 nommaient l'objet « option (d) » sans dire que le mot de Lazar l'appelle « option A ». Corrigé en v3 parce que R-4809 (l. 4948) et `GO-2026-11-22-42` (l. 729) emploient deux lettres pour le même objet.

#### [F01-10] Pilote du levier contre l'instruction nue
- Définition : avant tout axe, mesurer si « contraindre ou soudoyer » ajoute du dommage, à l'oracle planté, au-delà d'une instruction injectée sans levier, sur Llama 3.1 8B. Quatre bras appariés : sans injection ; contenu anodin de même longueur et position (témoin négatif) ; instruction nue ; instruction avec levier. Si l'écart tient dans la borne d'équivalence scellée, la coercition n'est qu'un mode d'injection.
- Synonymes et paraphrases : pilote E0 de la réponse 1 (à ne pas confondre avec l'expérience E0 des fausses alertes de la réponse 3) ; hypothèse locale H1 « construit » ; « la notion tient-elle ? ».
- Source : réponse 1, § 1 points 1 et 5, R5 H1, R6 E0 (l. 147), D1 (l. 174) (`c3fb4c9a0e8f772c`). Fondement : `GO-2026-11-22-12`, point 2, `registres/go.md` l. 699 (« go » sur le plan : pilote E0 et E1 puis modes de A, B, C par additifs).
- État : accordé : pilote E0 avant tout axe (D1), `GO-2026-11-22-12`, point 2.
- Liens : coercition et corruption ; papier A ; oracle sans modèle.
- Ce qui l'attaque : un résultat nul ramène le sujet à l'injection d'instructions, très publiée (AgentDojo, « Not what you've signed up for »).
- Inventaire : nouveau.
- Historique : v1 et v2 disaient « retenu (pilote accepté selon dem. 6) » sans identifiant de l'accord. Corrigé en v3 parce que l'accord est `GO-2026-11-22-12`, point 2 (l. 699).

#### [F01-13] Deux bras pour l'attaquant optimisé contre les scores
- Définition : l'invariant « aucun score de moniteur dans l'entraînement de l'agent » ne dit rien de l'attaquant corrupteur. Deux bras, rapportés séparément, sous cloison stricte : attaquant aveugle, et attaquant qui s'optimise contre les scores.
- Synonymes et paraphrases : décision D3 de la réponse 1 ; attaquant pire cas ; suffixes optimisés par gradient contre un juge ouvert.
- Source : réponse 1, § 3 « Attaques », D3 (l. 190) ; réponse 7, partie 3 (équipe rouge E1.5) et décision 4. Fondements : `GO-2026-11-22-12`, point 2, `registres/go.md` l. 699 ; `GO-2026-11-22-20`, point 2, l. 707 (« sens (a) et (b) seulement, N-053 strict »).
- État : accordé : deux bras sous cloison (D3), `GO-2026-11-22-12`, point 2 ; portée de N-053 tenue « stricte » par `GO-2026-11-22-20`.
- Liens : N-053 ; bras d'attaque aveugle et informé (N-056) ; fuite indirecte par sélection des exemples ; exception à N-053 accordée pour le seul barreau 3 de l'étau, en bras d'attaque déclaré (`GO-2026-11-22-57`, l. 744).
- Ce qui l'attaque : fuite vers la conception des moniteurs ; double le coût.
- Inventaire : rattaché à 2.17 (épreuves du devin).
- Historique : v1 et v2 disaient « retenu (accepté selon dem. 6) » sans identifiant de l'accord. Corrigé en v3 parce que l'accord est `GO-2026-11-22-12`, point 2 (l. 699).

#### [F01-23] Les « trois planchers » en théorème
- Définition : pour tout protocole à budget d'audit et référence de taille m, un saboteur adaptatif cacherait un dommage au moins égal au plus grand de trois termes : échantillonnage, bruit honnête, référence partagée. Fable la juge probablement occupée ou fausse telle qu'écrite.
- Synonymes et paraphrases : candidate locale R5 de la réponse 2 ; trois planchers du collisionneur ; borne minimax ; résultat négatif. À ne pas confondre avec le « théorème négatif » de la réponse 9 (marginale contre dépendance), objet distinct.
- Source : réponse 2, R5 (l. 140) et décision 5 (l. 210) (`542b7bfc86497c0c`) ; réponse 4, § 1 (forme de la loi de la racine carrée) ; réponse 9, « ne pas écrire », point 10 (l. 196). Fondements : `GO-2026-11-22-12`, point 1, `registres/go.md` l. 699 ; `GO-2026-11-22-24`, point 2, l. 711.
- État : accordé : rangé en limite déclarée, sans revendication (décision 5, option a), `GO-2026-11-22-12`, point 1.
- Liens : retrait de la marge (N-077) ; loi d'échelle du dommage caché ; théorème négatif de la réponse 9, gardé mentionné (`GO-2026-11-22-40`, l. 727) et cité seulement (réponse 34, ligne A4).
- Ce qui l'attaque : un rejouage à aléa commun (mêmes graines, même préfixe) peut réduire le bruit honnête sous sigma racine de n, donc le deuxième plancher n'en est pas un ; Avenhaus et Jaech 1981 ; bornes à deux points classiques ; voisin probable Avenhaus, von Stengel, Zamir 2002 (réponse 9, l. 100). La réponse 9, accordée par `GO-2026-11-22-24`, interdit de l'écrire comme résultat ; « abandonné » n'est pas accordé (l'option b reste à réexaminer après l'essai jumeau contre jumeau).
- Inventaire : rattaché à 2.3 et 2.4.
- Historique : v1 disait la candidate « retirée en pratique, abandonnée » ; v2 a corrigé l'état sans distinguer l'objet du théorème négatif de la réponse 9. Corrigé en v3 parce que la réponse 9 (R-4768, `registres/decisions.md` l. 4907) traite d'un autre objet, la marginale contre la dépendance, gardé mentionné par `GO-2026-11-22-40` (l. 727).

#### [F08-18] Question empirique « marginale ou dépendance »
- Définition : sur de vraies activations, le sabotage des organismes déplace-t-il la marginale des scores, leur dépendance, ou les deux ? Test de position contre test de dépendance, étalonnés sur des données de substitution. Section de diagnostic du papier A et tête du papier B (co-élévation entre copies à poids partagés, nul donné par la frontière héritée).
- Synonymes et paraphrases : marginale contre corrélation ; position ou dépendance (ligne A6 de la réponse 34) ; hypothèse pivot ; co-élévation ; agrégateur de corrélation.
- Source : réponse 9, section (2), verdict ; table de la section (3) (`48d4d72e5f1cbcde`). Fondement : `GO-2026-11-22-24`, point 2, `registres/go.md` l. 711 (« question empirique « marginale ou dépendance » gardée »).
- État : accordé : question empirique gardée (option a de la décision 2 de la réponse 9), `GO-2026-11-22-24`, point 2 ; mesurée et rapportée (réponse 34, ligne A6, accordée à `GO-2026-11-22-57`).
- Liens : papier B ; N-069 ; E1.4 ; N-077 (on mesure les organismes, non l'attaquant optimal).
- Ce qui l'attaque : un attaquant qui préserve ses marginales est hors revendication. La version boîte noire et synthétique est occupée (Zhang et Gao 2026, 2606.10456 ; lu sur PDF, R-4769, `registres/decisions.md` l. 4908 ; aussi 2610.13083, 2607.11751, R-4771, l. 4910) ; boîte blanche empirique sans théorème chez 2604.01151 et 2607.06807 (R-4771). Non trouvé dans les pièces lues : « marginale préservée par un vrai agent » (R-4771).
- Inventaire : nouveau.
- Historique : v1 et v2 écrivaient « chance d'inédit sous réserve de 2606.10456 », comme si la pièce restait à lire. Corrigé en v3 parce que 2606.10456 est lu et occupe la version boîte noire et synthétique (R-4769, l. 4908), et que seule « marginale préservée par un vrai agent » reste non trouvée (R-4771, l. 4910).

#### [F15-06] Contournements à ne pas faire sous abonnement
- Définition : liste des usages que le texte interdit ou que le fournisseur pourrait lire comme évasion : jeton d'abonnement recopié dans une passerelle ou un autre client ; compte prêté ; comptes multipliés ou charge étalée pour passer sous les limites ; boucle déguisée en usage interactif ; outil de relecture rebranché sur l'abonnement pour alléger la facture ; client modifié.
- Synonymes et paraphrases : « ce qui serait un contournement » ; « evade payment » ; « circumvent product guardrails » ; C17, C18.
- Source : `reponse-15/relecture-fable-api.md`, § C.4 (`11689127577ecd72`, l. 188) ; `reponse-15-opus46/relecture-fable-api.md`, § C.4 (`83c0a1859264d419`). Fondements : `GO-2026-11-22-32`, lecture de la mère (3), `registres/go.md` l. 719 ; `GO-2026-11-22-34`, points 2 et mot d'en-tête, l. 721 ; R-4797, `registres/decisions.md` l. 4936.
- État : gel refusé (décision 1, partie « geler », `GO-2026-11-22-32`) ; contournements exclus : aucun compte multiplié pour passer sous les limites, aucun client modifié, aucun jeton recopié (`GO-2026-11-22-32`) ; passage d'un compte à l'autre aux quotas retiré (`GO-2026-11-22-34`).
- Liens : session mère et sessions filles (décision 2 : relever le mécanisme réel) ; lettre au fournisseur, v2.
- Ce qui l'attaque : la frontière « plusieurs abonnements à son nom » n'est plus posée au fournisseur : la question 4 est retirée de la lettre v2 (`GO-2026-11-22-34`, point 2 ; R-4797, l. 4936). Elle reste donc sans réponse écrite, et la règle du programme est de ne pas contourner (« non évidemment on ne contourne pas un garde-fou »).
- Inventaire : nouveau.
- Historique : v1 et v2 tenaient la frontière « plusieurs abonnements à son nom » pour une question ouverte de la lettre (question 4). Corrigé en v3 parce que la question 4 est retirée de la lettre v2 (`GO-2026-11-22-34`, l. 721, point 2 ; R-4797, l. 4936).

#### [F15-38] Classement des trois sources d'attaques : organismes discrets, attaquant informé, lot tenu à l'écart
- Définition : les organismes discrets sont l'objet d'épreuve, non un vérificateur : base d'attaques non adaptées et témoin de compétence. L'attaquant informé remplit l'accès mais pas l'indépendance, sauf s'il est écrit par un tiers après le gel ; sinon c'est un bras adaptatif interne, rapporté comme majorant descriptif. Le lot tenu à l'écart n'est pas une équipe rouge mais un jeu d'épreuve statique, qui mesure la tenue face au jamais-vu et que toute ouverture consomme.
- Synonymes et paraphrases : bras d'attaque des organismes discrets ; bras de l'attaquant informé (aveugle et informé, N-056) ; « attaques en quarantaine » ; « l'information n'est pas l'indépendance ».
- Source : `reponse-19/relecture-fable-api.md`, conclusion, § a, § b (l. 123), décision 2 (l. 224) (`989824d318a45231`). Fondement : `GO-2026-11-22-34`, point 1, `registres/go.md` l. 721.
- État : accordé : décision 2 de la réponse 19 (organismes en base et témoin, attaquant informé interne en majorant descriptif, un tiers après gel pour toute revendication), `GO-2026-11-22-34`, point 1.
- Liens : bras A ; N-054 ; N-056 ; N-077 (attaquant qui répond au mieux, mesure descriptive). La clause « majorant descriptif » était proposée par Fable « pour N-077 » (réponse 19, l. 123) ; N-077 ne la contient pas, elle est accordée par `GO-2026-11-22-34`.
- Ce qui l'attaque : Fable n'avait ni la définition des bras ni le motif de la quarantaine : lecture conditionnelle.
- Inventaire : nouveau.
- Historique : v1 et v2 rattachaient la clause « majorant descriptif » à N-077. Corrigé en v3 parce que la décision N-077 ne porte pas cette clause (aucune occurrence de « majorant ») et qu'elle est accordée par `GO-2026-11-22-34` (l. 721).

#### [F22-68] Ouverture séquentielle par le pari apparié borné, et budget de bits
- Définition : le dépositaire ouvre les tâches du lot dans un ordre tiré d'avance et s'arrête dès que le pari apparié borné (déjà retenu, N-056, nœud 2) tranche ; le reste demeure scellé. Le lot est ouvert une fois, en séquentiel, sur la version qui a franchi la porte. Tout agrégat rendu avant le gel final est compté dans un budget de bits ; au pire cas, une borne d'union sur l'inégalité de Hoeffding montre l'élargissement de la marge garantie quand des bits sont rendus.
- Synonymes et paraphrases : « pari apparié borné » ; « ouverture séquentielle » ; « budget de bits » ; « lot ouvert une fois, en séquentiel ». Option rivale non retenue : « un bit par cycle, budget compté ».
- Source : réponse 23, § 3 (l. 67-68), § B4, point 5 (l. 167), décision 2, option a (l. 228) (`2a06a4d27348175f`). Fondement : `GO-2026-11-22-42`, `registres/go.md` l. 729 (« Réponses 23 et 24 : « go recos » avec ses remarques »).
- État : ouverture séquentielle accordée (décision 2, option a, `GO-2026-11-22-42`) ; le budget de bits reste un élément proposé de la liste à sceller avant l'ouverture (§ B4).
- Liens : N-055, N-056 ; Waudby-Smith et Ramdas 2023 ; Shafer 2021 ; Dwork et collaborateurs 2015 ; Blum et Hardt 2015 ; intersection-union (Berger et Hsu 1996) ; Lan et DeMets 1983.
- Ce qui l'attaque : pire cas ; Roelofs et collaborateurs 2019 ; ordres de grandeur de Fable à refaire par un statisticien (réponse 23, l. 84).
- Inventaire : nouveau.
- Historique : v1 et v2 donnaient pour source « décision 2 (option c) ». Corrigé en v3 parce que la recommandation accordée est l'option a, lot ouvert une fois en séquentiel ; l'option c, « un bit par cycle », était l'option rivale (réponse 23, l. 228-231).

#### [F25-25] Épreuve de l'étau par barreaux
- Définition : barreau 0 sans attaque ni entraînement (rappel de L sur dommages plantés non dissimulés, prix de l'effacement, lecture à texte nettoyé, trois honnêtes de contrôle, devin) ; barreau 1 à poids gelés, familles à dissimulation écrites par des tiers dont une tenue à l'écart ; barreau 2, attaquant entraîné contre le seul texte sans jamais recevoir L ; barreau 3, attaquant entraîné contre les deux, mesure de la taxe. Réfutations : plafond nul au barreau 0 ; J proche de un sur la famille tenue à l'écart aux barreaux 1 et 2 ; silence commun à taxe nulle au barreau 3, l'étau étant alors ouvert à cet échelon. Prévisions de Fable : L ne tombe pas entièrement avec B au barreau 1 (0,5) ; silence commun atteint à taxe faible au barreau 3 (0,7).
- Synonymes et paraphrases : étau ; « échapper à l'un expose à l'autre » ; taxe de dissimulation ; barreaux 0 à 3 ; étau en quatre barreaux ; R4 ; D-3, D-4.
- Source : réponse 29, § R4, D-3 (l. 268), D-4 (l. 275) ; `2af768bc095e40a4`. Fondements : `GO-2026-11-22-42`, `registres/go.md` l. 729 (« je veux l'étau aussi ») ; `GO-2026-11-22-52`, l. 739 (« go pour l'étau en quatre barreaux ») ; `GO-2026-11-22-57`, l. 744 (« barreau 3 de l'étau « go » »).
- État : accordé en quatre barreaux (`GO-2026-11-22-52`), barreau 3 compris (`GO-2026-11-22-57` : exception à l'invariant N-053 accordée en bras d'attaque déclaré, organisme en quarantaine, jamais réemployé) ; barreau 0 après l'étape 1 de la réponse 25, barreaux suivants sur devis (D-3 (a)).
- Liens : N-053 (exception du barreau 3, avec la question « pourquoi cet invariant et peut-on le lever ») ; N-077 (attaquant qui répond au mieux) ; attaquant informé ; quarantaine ; inventaire 5.5.
- Ce qui l'attaque : une mesure de taxe est toujours un plafond ; Bailey et al. 2024 ; McGuinness et al. 2025.
- Inventaire : 5.5.
- Historique : v1 disait le barreau 3 « refusé pour l'instant », v2 le disait non tranché, et la correction v2 proposait « refus recommandé, non tranché ». Correction rejetée en v3 : `GO-2026-11-22-57` (l. 744, postérieur au scellé de la note) accorde le barreau 3, après `GO-2026-11-22-52` (l. 739), qui accorde l'étau en quatre barreaux.

#### [F25-33] Révision du billet sur les sondes (renvoi gardé)
- Définition : la décision 3 de la réponse 26 recommande de garder le renvoi faute de résultat sur saboteur discret et de contrôle de l'empreinte de la consigne. Elle prépare la table de péremption par classes (« détecte » → « oriente l'audit » ; accumulation sans m et n ; marge retirée par N-077 ; lemme et théorème retirés ; chiffres voisins sans unité ; primauté ; mode tenu à l'écart ; conclusion bornée à « instructed »). Le résumé dit dans ses 250 premiers mots que rien n'est établi pour un saboteur discret.
- Synonymes et paraphrases : premier billet sur le contrôle ; saboteur instruit ; barreau « sabotage ou empreinte » ; explication concurrente par l'empreinte de la consigne ; décision 3 de la réponse 26.
- Source : réponse 26, § B3, décision 3 (l. 214) ; `8ff82014b2feb5f6`. Mot de Lazar en tension : `GO-2026-11-22-42`, `registres/go.md` l. 729 (billet sur les sondes « au plus vite et avant l'entretien, capital »).
- État : proposé non tranché (décision 3 de la réponse 26) ; nœud à soumettre à Lazar, le renvoi recommandé allant contre son mot de `GO-2026-11-22-42`.
- Liens : chantier saboteur et sondes ; N-075 ; N-076 ; N-077 ; N-054.
- Ce qui l'attaque : la sonde peut lire l'empreinte de la consigne et non le sabotage ; le mot de Lazar de `GO-2026-11-22-42` demande le billet avant l'entretien. Les sections de l'étape B et de l'étape B bis s'écrivent par un lecteur autorisé depuis les verdicts scellés (aucun chiffre ici).
- Inventaire : nouveau.
- Historique : v1 disait la décision « proposée (confiance 0,7) » sans relever le mot de Lazar. Corrigé en v3 parce que le renvoi recommandé (option a) va contre `GO-2026-11-22-42` (l. 729), et qu'aucune ligne de GO lue ne tranche la décision 3.

#### [F25-42] Lemme d'additivité, mentionné, et la question de l'étalement
- Définition : l'indifférence de la somme à la répartition, à taille fixe, est occupée hors du contrôle (Avenhaus et Jaech 1981 ; Ker 2006). Pour un processus e, reste la question de savoir si l'étalement est le cas le moins favorable au défenseur ; une simulation à budget égal (sabotage tôt, tard, étalé) la tranche avant toute phrase. Le lemme est revendiqué dans son application au contrôle de l'IA, sous la forme d'une conservation mesurée du déplacement cumulé sous fragmentation jouée par l'agent.
- Synonymes et paraphrases : L ; lemme ; reste ; borne inférieure valide à tout instant (retirée) ; « la puissance ne dépend que de B et de la variance » (phrase interdite pour un test séquentiel, réponse 34, ligne A3).
- Source : réponse 27-luc, EN-4, D6, D7, D14 ; `6a042a7b18124d58`. Fondements : `GO-2026-11-22-24`, `registres/go.md` l. 711 ; `GO-2026-11-22-40`, l. 727 ; `GO-2026-11-22-42`, l. 729 ; `GO-2026-11-22-57`, l. 744 (réponse 34, décisions 1 et 2).
- État : revendiqué dans son application au contrôle de l'IA (`GO-2026-11-22-42`, qui prime sur le retrait de `GO-2026-11-22-24` et sur « on les garde mentionnés » de `GO-2026-11-22-40`) ; lettre fixée par la réponse 34, décision 1, option c (`GO-2026-11-22-57`).
- Liens : N-013 ; N-075 (lemme resserré au reste) ; fiches GO-44 et RD21-20.
- Ce qui l'attaque : énoncé occupé ; la forme séquentielle reste une question tant que la simulation « tôt, tard, étalé » n'a pas parlé (réponse 34, l. 111). La réponse 27 (D6, D14 : « mentionné, non revendiqué ») contredit le mot de Lazar et doit être corrigée par un erratum d'une session neuve (réponse 34, décision 2, accordée à `GO-2026-11-22-57`).
- Inventaire : nouveau.
- Historique : v1 et v2 suivaient la réponse 27 (« retiré comme résultat, mentionné ») sans le mot de Lazar de la l. 729. Corrigé en v3 parce que `GO-2026-11-22-42` (l. 729), plus récent, revendique l'application, et que `GO-2026-11-22-57` (l. 744) accorde la lettre et l'erratum de la réponse 27 proposés par la réponse 34.

#### [RD21-11] Barre de 5 000 par tranche : précision, non validité
- Définition : la barre de 5 000 épisodes par tranche n'est ni nécessaire ni suffisante pour un seuil d'alerte à 1 % : c'est une barre de précision. Une garantie de validité demande quelques centaines d'épisodes selon la forme voulue (299 épisodes pour un seuil certifié à 95 %). Seules les comparaisons « bat telle base » exigent un lot neuf ; on compte des familles, pas des épisodes.
- Synonymes et paraphrases : « seuil à 1 % » ; « seuil certifié à 95 % » ; « 299 épisodes » ; seuil séquentiel relevé à 1/(α·p_min) ; horizon assigné ; « usage du papier dopamine : un aiguillage ».
- Source : R-4371, `registres/decisions.md` l. 4509 (approfondissement par Fable, Argon, Carbon ; `GO-2026-11-21-13`, `registres/go.md` l. 612, « seuil à 1 % avec peu d'épisodes honnêtes ») ; R-4429, l. 4567 (synthèse du collisionneur). Fondement : `GO-2026-11-21-25`, `registres/go.md` l. 624.
- État : retenu comme lecture ; cinq décisions de la synthèse accordées aux recommandations (`GO-2026-11-21-25`).
- Liens : course « seuil et moniteurs » ; papier « dopamine » (seuil unique sur score normalisé : 1 % en moyenne sur les longueurs, pas par tranche, `GO-2026-11-21-25`, D-1).
- Ce qui l'attaque : conditionner sur l'échec final gonfle le taux jusqu'à α/P(échec), ce qui nuance le moniteur de dissonance ; un contrôle actif par sélection sur un score de sonde contredit N-053, point 5 (aucun score de moniteur dans l'entraînement), consigné comme fermé (`GO-2026-11-21-25`, D-4 (a)).
- Inventaire : nouveau.
- Historique : v1 et v2 portaient la même lettre ; la remarque d'Argon proposait de remplacer « seuil d'alerte à 1 % » par « seuil certifié à 95 % » et jugeait `GO-2026-11-21-25` absent de la source. Remarque rejetée en v3 : le seuil à 1 % est l'objet même de `GO-2026-11-21-13` (l. 612) et de `GO-2026-11-21-25` (l. 624), « 95 % » est le niveau de certification de R-4371 (l. 4509), ajouté en synonyme, et la ligne `GO-2026-11-21-25` existe bien à la l. 624.
