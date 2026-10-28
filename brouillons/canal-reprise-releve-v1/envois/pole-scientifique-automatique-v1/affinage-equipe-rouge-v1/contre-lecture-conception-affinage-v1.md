<!-- Contre-lecture rendue par une session neuve d'Opus 5.5 (R2 ; auteur du document : Fable 5.1), 28 octobre 2026, versée telle quelle. Le script joint est illustratif, non préenregistré, non opposable. -->

# Contre-lecture de `conception-affinage-equipe-rouge-v1.md` (empreinte `789141db…`, vérifiée sur disque) — Opus, session neuve

**Verdict.** Adoptable **après corrections**. Le squelette est bon : un langage formel, c'est le noyau qui gèle, un juge mécanique qui n'exécute aucun code, un budget de fausses promotions par proposeur, des témoins plantés produits par un générateur et une ombre-miroir. Mais deux défauts internes de la statistique et de la mémoire sont **bloquants**, parce qu'ils font promouvoir des affirmations fausses par construction. La famille H, elle, est **molle** sur ce qu'une lignée partagée permet d'exploiter.

**Déclaration de conflit (règle R2).** Je suis Opus 5.5. Or le proposeur maison est composé d'Opus 5.5 et de Fable 5.1 (`integration-proposeurs-ia-v1.md`, ligne 100). Ma contre-lecture **n'est donc pas indépendante sur la famille H**. Il faut une seconde lecture de cette famille par un modèle d'un autre fournisseur, ou la faire trancher par Lazar.

**Calcul.** Un seul calcul illustratif, non décisif et non opposable : une course entre les deux processus de pari, pour un effet gaussien et des processus de rapport de vraisemblance. Il n'a pas de préenregistrement, car ce n'est pas une expérience au sens de R1 ; on peut l'écarter. Graine `SeedSequence(20261028)`, 20 000 répétitions. Script : `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/course.py`.

---

## A. Famille H : le proposeur maison et le conflit de lignée

Les cinq attaques H-01 à H-05 (lignes 1179 à 1224) portent sur **l'infrastructure** : mémoire privée, droits de stockage, secrets, attribution des lignées, choix de la composition. **Aucune** ne porte sur ce qu'un modèle de la **même lignée que l'auteur et que le juge** peut exploiter. Voici les attaques qui manquent, de la plus grave à la moins grave.

1. **Asymétrie documentaire.** Le proposeur maison tourne sur l'infrastructure du programme. Ses consignes sont écrites par des gens qui ont lu ce document : le catalogue, les bornes du générateur d'artefacts, la bibliothèque publique, ε et ρ. Les systèmes publiés n'ont rien de tout cela. G-H2 compare des **tables de droits déclarées**, pas le **contenu du contexte**.
   - Garde à ajouter : l'amorce du proposeur maison est scellée, et un modèle d'une autre lignée la relit pour y chercher toute référence aux internes du juge et au catalogue. Le corpus documentaire est le même pour les deux colonnes.
   - Test : sain, une amorce neutre ; artefact, une amorce qui cite un code d'arrêt ou une borne → `CONTEXTE_INEGAL`.
2. **Priors partagés entre le constructeur du monde et le proposeur.** G-G1(i) (ligne 1130) exige une séparation **de sessions**. Or le défaut réellement rencontré (brief v2, lignes 54 à 58) vient précisément de structures « naturelles » pour une lignée. Deux sessions Fable ou Opus séparées partagent leurs priors : l'attestation « n'a lu aucun gabarit » ne garantit pas l'indépendance.
   - Garde : un monde planté **tiré mécaniquement au hasard dans la grammaire** (lois tirées uniformément sur les formes, les variables, les signes et les espaces), ou construit par un autre fournisseur. La mesure de couverture (ii) passe de garde secondaire à garde obligatoire **pour tout proposeur-modèle de la lignée du constructeur**.
3. **Les témoins dans le flux d'un proposeur.** La ligne 721 ajoute `témoins_P` aux fiches de P, « indistinguables ». Mais le paquet porte le « statut de ses propres fiches » (ligne 245). Un modèle peut chercher à reconnaître son propre style par régénération ; cette capacité est à vérifier. Le document ne dit pas non plus si un témoin consomme l'α_P (budget de fausses promotions) et le F_max (plafond de fiches) de P.
   - Garde : les témoins ne sont jamais attribués à un proposeur dans le paquet, et l'attribution des fiches y est retirée.
   - Test : discernabilité **mesurée par le proposeur lui-même**, c'est-à-dire en lui demandant d'étiqueter et en comparant au hasard. Le « classifieur simple » de G-02 (ligne 1154) n'est pas l'adversaire réel.
4. **Dérive du modèle servant.** Le cadre lui-même consigne une fluctuation « Opus 5.5 puis Opus 4.8 » (`integration-proposeurs-ia-v1.md`, ligne 4). Une composition peut changer en silence d'une génération à l'autre.
   - Garde : l'identifiant du modèle servant est relevé à chaque appel ; s'il varie, `MODELE_SERVANT_DIVERGENT` est levé et la génération du proposeur est invalidée.
5. **Le générateur de secrets est devinable par la lignée.** H-03 (ligne 1199) tire des nuls secrets **dans une distribution conçue par la même lignée**. Le simulateur « connaisseur de la partie publique » ne modélise pas un proposeur qui connaît le **générateur** des secrets.
   - Garde : ajouter un simulateur « connaisseur du générateur » ; si son taux de refus s'écarte de celui d'un proposeur naïf, `SECRET_INSUFFISANT` est levé.
6. **Pas de lignée disponible pour vérifier.** H-04 exige un vérificateur d'une lignée distincte du proposeur **et** de l'affineur. Si le proposeur maison est Opus plus Fable, il ne reste dans le programme **aucune** lignée pour vérifier ses fiches. Par ailleurs, la recommandation du cadre (`integration`, ligne 224 : « Fable 5.1 … rôle de vérificateur dans la boucle ») viole H-04. Le document ne relève pas cette contradiction.
7. **Coût mesurable inégalement.** J-05 suppose des jetons mesurés par le noyau. Un modèle servi par session, et non par une interface payée à l'appel, peut ne pas être mesurable de la même façon, ce qui fausse la comparaison en fiches promues par dollar.
8. **Catalogue écrit par la lignée de l'auteur.** Les artefacts ciblent les erreurs que cette lignée imagine. Le proposeur maison les évite naturellement, alors que les systèmes publiés y trébuchent : la « qualité » mesurée sur témoins avantage la maison. Correction : faire écrire une part des artefacts par un autre fournisseur, et reporter les résultats du duel par source d'artefact.

**Complaisance.** Plusieurs gardes de la famille H sont molles. G-H2 compare des tables déclarées au lieu de sonder les accès en boîte noire, dans les deux colonnes. G-H5 n'a pas d'artefact exécutable : « interface absente ; revue de code », ligne 1223. G-H1 parle d'une « image » qui n'existe pas pour un modèle servi par interface. Dans la famille H, **seules H-01 et H-04** ont un vrai couple cas sain et artefact.

## B. Statistique (sections 4.2, 4.6, 5.2)

**Ce qui tient.**
- **Le minimum d'e-valeurs.** Si H_j est vrai, alors min_k E_k ≤ E_j à chaque instant, donc P(sup min ≥ 1/α) ≤ α par l'inégalité de Ville. La propriété est vraie pour la réunion des nuls, que le minimum soit pris sur les processus cumulés ou sur les facteurs pas à pas. Le « à vérifier » de la ligne 477 est levé.
- **Validité à tout instant et arrêt optionnel.** La course qui s'arrête au premier franchissement, la reprise d'une indécise avec poursuite des produits sur des unités neuves (ligne 504), et le changement des nuls secrets entre générations restent valides : le nouveau nul démarre à 1, et le minimum reste inférieur ou égal à son processus.
- **Tests multiples à l'intérieur d'une génération.** P-5 applique une correction de Bonferroni sur α_P. Elle est valide quelle que soit la dépendance, alors même que les fiches partagent les mêmes unités d'épreuve.
- **Correction d'exposition.** Elle n'est pas nécessaire à la validité, puisque l'épreuve est fraîche. C'est une pénalité d'aptitude, et le document le dit honnêtement (ligne 425).

**Ce qui ne tient pas.**

1. **Bloquant : la survie ne certifie pas l'affirmation.** E_surv est valide sous « aucun effet » (ligne 468), tandis que la fiche affirme « effet ≥ δ » (ligne 469). Pour un vrai effet θ compris entre 0 et δ, aucun des deux nuls n'est vrai. Dans le modèle gaussien, la dérive du log de E_surv vaut δ(θ − δ/2) : elle est nulle à θ = δ/2, et la course y est une pièce équilibrée. Simulation avec δ = 0,3 écart-type par grappe, α = 0,01 des deux côtés et un budget de 400 :

   | θ | survie | réfutation | indécise |
   |---|---|---|---|
   | 0 | 0,8 % | 98,9 % | 0,3 % |
   | δ/4 | 8 % | 85 % | 7 % |
   | δ/2 | **41 %** | 41 % | 18 % |
   | 3δ/4 | **86 %** | 8 % | 7 % |
   | δ | 98,7 % | 0,9 % | 0,4 % |

   Conséquences :
   - La classe de témoins faux « vrai à amplitude δ au-dessus de la vérité » (ligne 667) sera promue jusqu'à 86 % du temps. Selon qu'on la compte ou non, on obtient une fausse « percée » ou une garantie mal énoncée.
   - Comme l'aptitude ne dépend pas de δ, **le proposeur rationnel prend δ aussi petit que possible**. Il réduit ainsi son risque de réfutation sans rien perdre, ce qui revient à un pari peu falsifiable. Cette attaque n'est pas au catalogue.

   Correction : définir le nul de survie comme « effet ≤ κδ » (κ fixé dans la grille), ou réduire l'affirmation à « effet > 0 » et supprimer δ ; dans les deux cas, imposer un plancher δ_min.
2. **Majeur : l'invariant de sévérité est incohérent.** En 4.2, σ₀ = −log alpha_survie, une constante tant qu'alpha ne bouge pas. En 4.4 (ligne 373), σ est « recalculée avec le nouveau budget et le nouveau compte de grappes ». Ce n'est pas la même quantité. Telle qu'elle est définie, `REFUSEE_RAMOLLI` ne voit pas un resserrement d'espace ; seule la contrainte de puissance π_min agit. Il faut nommer la quantité (par exemple, la probabilité sous le nul de franchir le seuil dans le budget, compte tenu du compte effectif).
3. **Majeur : le nul d'archive « à traits égaux » (ligne 474).** Tirer des issues d'archive conditionnellement aux traits **conserve** l'association réelle passée. Pris dans le minimum, il rend **impromouvable toute loi vraie et stable** dès que l'archive est assez fournie : le test devient « cette génération diffère-t-elle du passé ? ». Il ouvre aussi un canal. La vérification de 4.2 simule « sous le nul d'archive » (ligne 309), qui est construit sur les issues d'épreuve brûlées, puis renvoie des codes de refus à l'affineur. Des issues d'épreuve, même brûlées, nourrissent donc l'affinage. Correction : définir ce nul comme une permutation des issues à l'intérieur de l'espace, ce qui casse l'association, et ne jamais l'utiliser dans les vérifications de 4.2 qui produisent des codes visibles. Il faut aussi ajouter la règle suivante : **aucune vérification qui produit un code visible de l'affineur ne lit un nul secret ou un nul d'archive**.
4. **Ce que coûtent les gardes en puissance (approximation de Wald à θ = δ).** Le nombre d'unités attendu est proportionnel à log(1/α).
   - Budget α_P = 0,05 réparti sur 12 fiches : log 240 = 5,5, contre log 20 = 3,0, soit **+83 %** d'unités ; sur 100 fiches, **+153 %**.
   - Un nul informé décalé de μ vers l'affirmation multiplie le nombre d'unités par (θ/(θ−μ))², soit **×4** pour μ = θ/2.
   - Avec n_cand = 20, l'aptitude perd log 21 ≈ 3 nats ; à α = 0,01, elle passe de 4,6 à 1,6.

   La crainte « presque tout INDECISE » (10.1, point 5) est donc fondée et chiffrable avant le monde jouet.
5. **Majeur : l'incitation de la correction d'exposition est inversée.** Pour l'affineur-L, n_cand = k, le nombre de mouvements **soumis**. Il a donc intérêt à chercher en silence puis à soumettre un seul mouvement. Pour l'affineur-M, n_cand devrait valoir le nombre de traits multiplié par le nombre de pas, et non le seul nombre de traits (ligne 414).
6. **Majeur : fausses alertes des audits en faible puissance.** Le test « ombres non significativement inférieures » (ligne 1139) et la règle « toutes éliminées → audit » (ligne 544) se déclenchent pour un proposeur **honnête** dans un monde pauvre, où fiches et ombres sont toutes deux proches de 0. Correction : ne garder que les paires où l'un des deux a survécu, puis appliquer un test binomial de la proportion « la fiche est la survivante » contre 1/2. Il faut aussi préenregistrer le taux de fausse alerte de chaque audit (R4 exige la symétrie, mais aussi un étalonnage).
7. **Mineur à majeur : dépendance entre grappes.** La clé de grappe traite la dépendance à l'intérieur d'une grappe. Un agent ou une version de moniteur commun à plusieurs grappes crée une corrélation **entre** grappes, qui rend anticonservateurs les facteurs supposés indépendants. Il faut une clé au niveau le plus grossier, ou un témoin artefact « grappes corrélées entre elles », en plus de D-03.
8. **Mineur : les revendications.** Aucune erreur globale n'est définie sur les CONFIRMEE à travers les générations et les proposeurs. Une procédure de Benjamini-Hochberg sur e-valeurs, valide sous dépendance arbitraire, conviendrait pour la porte de revendication. La seconde tentative de confirmation (ligne 521) doit **poursuivre** le processus, comme le fait D-04 ; elle ne doit pas redémarrer.
9. **Mineur : brûlage.** Brûler en bloc les unités non lues, dont seuls les traits ont été vus, est conservateur mais coûteux. Avec une famille consommée par lignée et par confirmation, `FAMILLES_EPUISEES` risque d'arriver vite. Il faut chiffrer la consommation avant de fixer F_max.

**Mémoire (bloquant, lié au point B1).** L'empreinte interdit « Y_i' − Y_i de signe contraire **au-delà de δ** » (ligne 577). Avec un δ plus grand, la fiche interdit **moins** de cases, alors que « resserrer δ » est censé accroître le contenu. Le contenu est donc **inversé** par rapport à l'affirmation. On obtient alors la jumelle à δ décroissant d'une survivante : elle n'est pas incluse dans sa mère, passe la mémoire avec un contenu « supérieur », et survit presque sûrement. Inversement, E-02 refuse comme redite une fiche **plus forte**. La règle « contenu strictement croissant » de la lignée (ligne 648) récompense la faiblesse. Correction : la case interdite doit être « différence inférieure à δ dans le signe déclaré ». Par ailleurs, l'empreinte traite une loi statistique comme déterministe, couple par couple. C'est acceptable comme indicateur, mais il faut le déclarer.

## C. Fidélité au brief v2

Les sept écarts de la section 1 sont réels et justifiés. Le point 4 (la preuve héritée ne fait pas l'aptitude) réinterprète le cadre : c'est à soumettre à Lazar.

**Écarts non déclarés :**
- **La portée.** Le cadre fait des « pistes », des « expériences (protocole = fiche, code gelé) » et des « failles du programme » des fiches (`integration`, lignes 122 à 135). Le pôle prévoit que l'expérimentateur écrit et exécute son code et que le vérificateur le rejoue (`conception-pole`, lignes 21 à 24). Le langage MONOTONE / CONTRASTE / MODULATION et P-1 n'en expriment pratiquement que les « hypothèses » : J-02 ne montre pas comment une faille s'y écrit. C'est un choix de sécurité défendable, mais il **change ce qu'est l'organisme**. C'est un nœud pour Lazar, à déclarer comme tel.
- **La poussée.** Le brief interdit de pousser (ligne 24) ; le document a été poussé sur une branche de session. L'écart est déclaré, mais la justification « l'utilisateur l'a confirmé » est invérifiable ici. Lazar doit confirmer, ou faire supprimer la branche.
- **Un chiffre faux dans la note de livraison.** Elle annonce « 48 attaques en dix familles » ; j'en compte **56** (A 8, B 5, C 8, D 5, E 6, F 7, G 4, H 5, I 3, J 5), dont D-01 renvoie à B-04, soit 55 gardes distinctes.
- **Le plan de test promis n'est pas tenu partout.** La section 8.2 promet trois tests par garde (sain, artefact, exception). La section 7 en donne six sans artefact exécutable (D-05, F-03 et H-05 en revue de code ; F-06, I-02 et J-05 sans arrêt) et **aucun test « exception » n'est écrit**. R5 n'est pas tenu pour ces six.

## D. Niveau méthode (R-339)

**Je n'ai trouvé aucun passage qui décrive un mode de contournement de moniteur ni une recette de sabotage d'agent.** La section 6.9 (lignes 694 à 712) refuse expressément tout exemple de condition K. Les simulateurs de 8.1 (lignes 1308 à 1311) truquent des fiches et non des comportements. Les attaques A à J portent sur la boucle, ce qui est permis. Aucune moyenne sur les tokens n'y figure : la moyenne de CONTRASTE porte sur des épisodes et n'est pas une sonde de production.

**Une brèche de garde, et non de contenu.** Le routage mécanique (ligne 701) ne classe en « contournement » que les fiches dont l'espace nomme un trait de la sous-liste « conditions adversariales ». Une fiche MONOTONE(trait de tâche ordinaire, issue de détection, signe négatif), resserrée par l'affineur libre vers l'espace où la détection est la plus faible, **cartographie un angle mort sans être routée**. De plus, elle entre dans le paquet que voient tous les proposeurs. Correction : router aussi sur la combinaison issue de détection et signe vers la non-détection ; retirer ces fiches du paquet ; dire qui conçoit les moniteurs et lui interdire l'archive des paquets (quarantaine).

## E. Ajouts aux sections 10.1 et 10.2

**À ajouter dans 10.1 (ce qui n'est pas durci).**
- Ce qui sépare la survie de l'affirmation, avec le pari δ → 0.
- L'inversion du contenu en δ.
- Le nul d'archive, à la fois tueur de puissance et canal.
- L'absence de lignée disponible pour vérifier le proposeur maison.
- Les priors partagés entre le constructeur du monde et le proposeur.
- L'asymétrie documentaire.
- La dérive du modèle servant.
- Le routage contournable des fiches d'angle mort.
- Les fausses alertes en faible puissance.
- La dépendance entre grappes.
- La règle « proposeur attributaire » des filles (ligne 621), non définie. Si les filles vont au proposeur des parents, le verdict du juge sélectionne des agents, ce que le brief interdit (ligne 78).

**À ajouter dans 10.2 (questions à Lazar).**
1. Quel vérificateur pour le proposeur maison, s'il est Opus plus Fable ? Faut-il un autre fournisseur ?
2. Lazar accepte-t-il la réduction de l'organisme au langage formel, qui exclut les protocoles, les pistes et les failles en texte ?
3. Quel nul de survie retenir : « effet ≤ κδ », ou « effet > 0 » sans δ ?
4. Les témoins consomment-ils l'α_P du proposeur dans le flux duquel ils sont injectés ?
5. Le monde planté doit-il être tiré mécaniquement dans la grammaire ?
6. La poussée sur la branche est-elle ratifiée ?

## F. Classement

**Bloquant**
1. La survie certifie « effet > 0 » et non « effet ≥ δ » ; les témoins à amplitude gonflée sont promus jusqu'à 86 % ; le pari δ → 0 n'est pas au catalogue (B1).
2. L'empreinte inverse le contenu en δ ; la jumelle à δ décroissant passe ; la lignée récompense la faiblesse (mémoire).
3. Famille H : aucune lignée disponible pour vérifier le proposeur maison (H-04 inapplicable, recommandation du cadre contradictoire) ; ma propre contre-lecture de cette famille n'est pas indépendante.

**Majeur**
4. Asymétrie documentaire de la maison (A1).
5. Priors partagés constructeur–proposeur (A2).
6. Témoins attribués au flux d'un proposeur (A3).
7. Dérive du modèle servant (A4).
8. Nul d'archive (B3).
9. Invariant de sévérité incohérent (B2).
10. Incitation inversée de la correction d'exposition (B5).
11. Fausses alertes des audits (B6).
12. Routage des fiches d'angle mort (D).
13. Réduction de portée non déclarée (C).
14. Six gardes sans artefact exécutable, et aucun test « exception » écrit (C, R5).

**Mineur**
15. Dépendance entre grappes.
16. Revendications sans procédure globale.
17. Seconde tentative de confirmation à poursuivre, non à redémarrer.
18. Brûlage des unités non lues et consommation des familles.
19. « 48 » au lieu de 56 dans la note.
20. Compteur de bits seulement nominal.
21. Empreinte déterministe pour une loi statistique.
22. Proposeur attributaire non défini.

**Conclusion : adoptable après corrections.** Les corrections 1 et 2 portent sur la définition du nul de survie, un plancher δ_min et l'orientation des cases interdites. Avec la 3 (décision de Lazar sur la lignée du vérificateur et seconde lecture de la famille H par un autre fournisseur), elles conditionnent l'adoption. Les points 4 à 14 sont à corriger avant le premier code du noyau. Le reste peut attendre la version 2.
