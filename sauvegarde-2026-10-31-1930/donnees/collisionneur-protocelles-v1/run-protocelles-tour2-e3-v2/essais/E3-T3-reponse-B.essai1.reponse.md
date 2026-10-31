# Proposition B — Tour III.3 : Réponse aux critiques

---

## (a) Réponse critique par critique

Je traite ci-dessous chaque critique adressée à la proposition B, d'abord celles de C, puis celles de D. Les critiques visant les propositions C ou D ne me concernent pas et sont ignorées.

---

### Critiques de C sur B

**C-(a)1 : Vrai par construction dans le classement de P4 en (S).**

**Acceptée.** C a raison : si q_B = 0 et qu'il n'y a pas de copies rapides non filtrables déjà dans le vivier, un bain à θ′ = 1,2 ≥ min(θ,1) dégrade le plafond d'au moins −ln(1−τ) (synthèse, Corrections N2 : p. 56, l. 4078–4080). Comparer par Δρ ≥ +0,02 revient à prédire une impossibilité algébrique sous le noyau du papier. Mon classement (S) était prématuré. P4 passe de **(S) à (F)** : elle doit être reformulée pour conditionner le bras « bain » à une mesure préalable de q_B > 0 hors ligne, ou pour tester si le bain atténue la chute face à un fond imposé de copies rapides.

**C-(a)2 : Fuite entre étalonnage de l'instrument et seuil de décision (P2 et P3).**

**Acceptée en partie, transformée en contrôle.** C identifie correctement le risque de confondre seuil de détectabilité statistique et seuil dynamique de bifurcation (ρ = 1). J'accepte que fixer δ uniquement comme quantile du bruit instrumental est insuffisant. **Correction** : pour P2, le seuil doit être ancré sur le seuil dynamique — le c_eff = 2q_vf β/q_vv comparé au seuil de copie de soi c ≈ 4n/R (synthèse, section 5 : p. 13, l. 1195) — et la résolution instrumentale (α − β) doit être vérifiée comme suffisante pour atteindre ce seuil. Pour P3, la marge δ de D doit être calibrée sur le bruit de branchement simulé *et* rester au-dessus du seuil dynamique. Le risque inverse (effet dynamiquement sous-critique mais statistiquement détectable) est réel mais moins grave : il conduit à une fausse alarme, pas à un faux résultat.

**Cependant**, je rejette l'implication que cette fuite invalide entièrement mes classements. P2 et P3 sont déjà en (F) — à corriger — précisément pour ces raisons.

**C-(a)3 : Variable confondante bipartite dans l'identification de q_vv.**

**Acceptée.** La synthèse (section 2, trait 2) note que les paires sont prises dans deux espaces éloignés et qu'aucune espèce ne modélise des paires bipartites (F_A · F_B au lieu de F(F−1)). C a raison que traiter q_vv comme un scalaire suffisant sans contrôler la répartition (F_A, F_B) entre espaces confond fidélité de l'opérateur et topologie d'appariement. **Correction** : l'esquisse du §3.1 (point 3) doit être refaite avec des paires bipartites (la synthèse le note déjà : « Avec des paires bipartites, le calcul est à refaire avec F_A · F_B »). Avant le préenregistrement, l'audit du code (section 8 (i)) doit révéler si les lots contiennent des sous-espaces structurés et si l'appariement est bien bipartite. Cette critique renforce la nécessité de l'étape (i) comme préalable absolu.

**C-(a)4 : Confusion lot/fusion dans les journaux.**

**Acceptée en substance, nuancée sur la conclusion.** C a raison de distinguer l'unité lot (M = 3, non jugeable) et l'unité fusion (24 au total). Je n'ai pas explicitement séparé les estimands par niveau. Cependant, ma position (a.5 et c.2) subordonne déjà la lecture des journaux à la jugeabilité, et mon P6 est abandonné. **Correction de formulation** : je précise que la jugeabilité des journaux doit être évaluée estimand par estimand. Au niveau des lots : non jugeable pour ρ̂ (3 lots, puissance nulle). Au niveau des fusions : potentiellement jugeable pour q_vf ou τ par type de paire, *sous réserve* que la corrélation intra-lot (ρ_ICC) laisse un N_eff suffisant. C'est exactement le calcul que je demandais, mais je n'avais pas nommé le risque de pseudo-réplication. Je l'accepte.

**C-(b)1 : Non-identifiabilité de q̂_vv sous juge imparfait.**

**Acceptée comme risque, transformée en test.** La formule de variance de l'estimateur de Rogan-Gladen est correcte et montre que la puissance s'effondre quand α − β → 0. **Test ajouté** : avant le préenregistrement, calculer au processeur la variance attendue de q̂_vv en fonction de (α, β, m_vv, m_+, m_−) pour les effectifs réels. Si la résolution ne permet pas de distinguer q_vv = 0,45 de q_vv = 0,55 (les deux côtés du seuil 1/2 du Théorème 2), déclarer P8 non jugeable sur les journaux et exiger des runs prospectifs avec un juge plus discriminant ou davantage de cas plantés. Le point sur la non-identifiabilité de q_vf si β_vv ≠ β_vf est important : il signifie que l'estimation de q_vf (P2) exige que les taux de faux positifs du juge soient les mêmes par type de paire parentale, ce qui est un contrôle négatif supplémentaire à vérifier sur mondes plantés.

**C-(b)2 : Perte de la surmartingale sous tirage bipartite ou retrait sélectif.**

**Acceptée.** C'est la formalisation de la critique (a)3. Sous tirage bipartite avec N_A = N_B = N/2 et F_A = F_B = F/2, on a p_vv^bip = F²/N² > F(F−1)/(N(N−1)) et la borne q_vv ≤ 1/2 ne suffit plus à garantir la surmartingale. De même, un retrait sélectif (ω < 1 pour les fiches vraies) brise la dérive. **Conséquence** : P8 doit être conditionnée non seulement à la validation du noyau littéral mais aussi à la vérification que l'appariement n'est pas bipartite (ou, s'il l'est, au recalcul de la borne sur q_vv dans le cas bipartite) et que le retrait est indépendant du statut. Ces conditions rejoignent l'audit du code.

**C-(b)3 : Corrélation intra-lot et effondrement de N_eff.**

**Acceptée.** L'exemple chiffré (ρ_ICC ≥ 0,5 → N_eff ≤ 5,33 → puissance < 0,24 pour tester q_vf = 0,05) confirme que les journaux de la course 2 sont probablement non jugeables même au niveau des fusions pour P2. **Conséquence** : la lecture des journaux pour q_vf ne doit être tentée qu'après estimation de ρ_ICC sur données synthétiques du noyau ou par le plan d'échantillonnage connu via l'audit du code.

**C-(c)1 : Contrôle de troncature exogène aveugle.**

**Acceptée.** Sans un bras où l'interruption est tirée selon une Bernoulli(τ_0) indépendante du contenu et du temps, on ne peut pas séparer le coût dynamique 1/(1−τ) d'un biais de sélection éliminant les concepts difficiles. **Ajouté** comme contrôle obligatoire dans les runs prospectifs de P4 et P5.

**C-(c)2 : Contrôle de juge par rembourrage inerte.**

**Acceptée.** Le bras « un parent vrai + rembourrage inerte de même longueur » et l'évaluation à l'aveugle (juge reçoit seulement la fille) sont des contrôles que j'aurais dû nommer explicitement dans P2 et P3. La convergence T3 les incluait (synthèse, section 10), mais je les avais omis dans ma formulation de c.1. **Corrigé.**

**C-(c)3 : Contrôle à budget d'appels constant dans le vivier.**

**Acceptée.** Si le bras « bain » ajoute des brouillons sans réduire le quota d'appariements pour les fiches complètes, l'effet confond complémentation et dilution du budget. Le contrôle par jetons fantômes inertes consommant le même quota est nécessaire. **Ajouté** comme contrôle obligatoire dans P4.

---

### Critiques de D sur B

**D-(a)1 : L'audit du code ne suffit pas à identifier n.**

**Acceptée en partie.** D a raison qu'une règle de renouvellement peut ne pas correspondre au couple (n, division) du papier. Plusieurs processus peuvent produire les mêmes tailles de lots avec des noyaux différents. **Cependant**, je n'ai pas dit que l'audit « fixe n » — j'ai dit qu'il fixe n *et la règle de division ensemble* (ma réponse a.1 : « La règle de formation des lots — combien de fiches entrent, combien en sortent, comment sont-elles réparties — fixe n et la règle de division ensemble »). Le risque identifié par D est que la règle observée n'appartienne pas à la classe de noyaux pour laquelle n est défini. **Correction** : j'ajoute une étape intermédiaire entre l'audit et le préenregistrement — démontrer (ou réfuter) que la règle observée est isomorphe à un processus croissance-division à taille fixe. Le contrôle négatif proposé par D est adéquat : simuler deux orchestrateurs (croissance-division vs capacité fixe) produisant les mêmes tailles de lots et vérifier si la procédure les distingue.

**D-(a)2 : B déplace l'identification de q sans la résoudre.**

**Acceptée.** La critique est juste : q_vv n'est un paramètre stable que relativement à une loi de tirage, une population de parents, une définition de la fille vraie et un horizon d'observation. Si q_vv dépend du contenu, du domaine ou du budget, le scalaire estimé est une moyenne contingente. L'épreuve trans/cis teste une structure causale mais ne certifie pas un q_vv constant. **Correction** : P2 et P3 doivent inclure un test de stationnarité de q_vv par blocs temporels (versions, lots) et un contrôle par domaine (si les espaces éloignés sont identifiables). L'estimand doit être défini comme « q_vv moyen sur la population de paires à la distribution d'appariement réelle de l'orchestrateur, sur un horizon fixé ».

**D-(a)3 : Deux équivalences confondues dans la politique d'archivage.**

**Acceptée.** D distingue correctement : (1) l'équivalence trajectoire « détruire = archiver si l'archive est inaccessible au tirage », qui est vraie par construction et n'a aucune puissance scientifique ; (2) l'assimilation du sort perdu à un débit R(1−τ), qui exige les conditions sur τ de la synthèse (§3.1 et §6 : p. 56, l. 4043–4052). J'ai parfois subordonné (1) à des conditions qui appartiennent à (2). **Correction** : dans le préenregistrement, séparer explicitement les deux affirmations. L'audit du code teste (1) par vérification déterministe ; les conditions de (2) — même τ pour tous les modèles, retrait indépendant du statut — sont des hypothèses testables empiriquement sur les runs prospectifs ou les journaux.

**D-(a)4 : Le classement de P4 en (S) est prématuré.**

**Acceptée** (cohérent avec C-(a)1). P4 passe en (F). Les corrections nécessaires : distinguer brouillons stériles et complémentation fertile, ne pas importer n = 6, égaliser les budgets entre bras. I12 impose un passage en (F), non l'abandon.

**D-(a)5 : La puissance comme certificat de validité trop général.**

**Acceptée.** Une puissance adéquate ne répare ni censure informative, ni erreur de mesure différentielle, ni confusion entre familles. Inversement, des journaux sans puissance pour un test causal peuvent rester jugeables pour un estimand descriptif borné. **Correction** : le critère de lecture des journaux est reformulé comme « estimand identifiable et incertitude maîtrisée », pas la seule puissance.

**D-(a)6 : Instruments et évaluations non suffisamment séparés.**

**Acceptée.** Pour P3, P5 et P7, les familles servant à choisir le noyau, le seuil et l'estimateur doivent être disjointes de celles servant à conclure. **Correction** : tout préenregistrement doit spécifier un partage familles de réglage / familles de test, scellé avant les données.

**D-(b) : Conditions de perte de puissance.**

**Acceptées comme risques.** Le tableau de D est méthodologiquement solide. Je note les points les plus critiques pour mes prédictions :
- q_vv, q_vf non transportables si varient avec contenu ou temps → test de stationnarité requis.
- Contraste trans/cis confondu sans recouvrement des distributions → randomisation et rembourrage inerte.
- ρ̂ non jugeable près de ρ = 1 si biais > écart à trancher → étalonnage incluant ρ = 1 (point que j'avais omis, accepté de D-(c)).

**D-(c) : Contrôles négatifs.**

- **Identification du noyau** : accepté (voir D-(a)1).
- **Trans/cis avec rembourrage et randomisation** : accepté (cohérent avec C-(c)2). Le contrôle fausse–fausse est un ajout pertinent que je n'avais pas explicité.
- **Estimateur spectral incluant ρ = 1** : accepté. Mon étalonnage ne mentionnait que ρ = 0,95 et 1,05 ; inclure ρ = 1 exactement et la permutation des étiquettes de bras est nécessaire pour contrôler le taux de fausse alerte au seuil.
- **Archivage avec troncature exogène randomisée et brouillons sentinels** : accepté (cohérent avec C-(c)1). Les brouillons sentinels dont le retour au vivier serait détectable sont un contrôle que je n'avais pas nommé.
- **Certification P10 avec implémentation indépendante et énoncé altéré** : accepté. La certification doit échouer sur un énoncé volontairement muté pour éviter qu'une erreur commune de spécification passe inaperçue.

---

## (b) Expériences corrigées

Les corrections intègrent toutes les critiques acceptées ci-dessus. Je ne reproduis que les prédictions dont le classement ou la structure change.

| N° | Classement révisé | Corrections apportées |
|---|---|---|
| P2 | **(F)** | (1) Seuil ancré sur c_eff = 2q_vf β/q_vv vs c ≈ 4n/R, pas sur le bruit instrumental seul. (2) Résolution (α − β) vérifiée au processeur via variance de Rogan-Gladen aux effectifs réels. (3) Contrôle de rembourrage inerte + évaluation à l'aveugle. (4) Test de stationnarité de q_vv par blocs. (5) Cas bipartite : refaire l'esquisse avec F_A · F_B si l'audit révèle deux sous-espaces. (6) Familles de réglage ≠ familles de test. (7) Aucune lecture des journaux avant scellement. |
| P3 | **(F)** | (1) Adopter la structure de D (δ fixé par branchement simulé *et* ≥ seuil dynamique). (2) Bras : deux parents vrais / un parent vrai + rembourrage inerte / paire fausse–fausse / paire entièrement inerte. Assignation randomisée. (3) Juge reçoit seulement la fille, sans trace des mères ni du bras. (4) Reconnaître le coût en appels. (5) Conditionner à l'audit du code (non-consommation, budget constant). (6) Familles de réglage ≠ familles de test. |
| P4 | **(F)** — rétrogradé de (S) | (1) Ne pas figer n = 6 avant l'audit. (2) Conditionner le bras « bain » à une mesure préalable hors ligne de q_B > 0, *ou* reformuler pour tester le bain face à un fond imposé de copies rapides. (3) Jetons fantômes inertes dans le bras bain consommant même quota d'appels au bisociateur. (4) Troncature exogène randomisée (Bernoulli(τ_0)) dans les deux bras. (5) Déconvolution de ρ̂ des erreurs du juge. (6) Capacité ajustée : si capacité fixe N, ajouter un bras quarantaine à capacité réduite appariée (critique de C sur P5, applicable ici). |
| P5 | **(F)** — rétrogradé de (S) | Même corrections que P4. Ajout : troisième bras « quarantaine à capacité N − B » pour séparer effet de taille finie et coût dynamique des brouillons. |
| P7 | **(F)** | (1) Audit du code pour séparer injection exogène. (2) Étalonnage de ρ̂ incluant ρ = 1, matrices brouillées par la confusion du juge, et permutation des étiquettes de bras. (3) Budget du bisociateur vérifié constant. |
| P8 | **(F)** → **(S conditionnelle)** après corrections | (1) Condition complète : q_vv ≤ min(θ,1)/2. (2) Esquisse §3.1 contre-lue, étendue au cas bipartite et retrait non sélectif. (3) Conditionné à l'audit montrant que l'appariement est uniforme ou, sinon, borne recalculée. |
| P10 | **(S)** | Ajout : implémentation indépendante + énoncé volontairement altéré comme contrôle de spécification (D-(c)). |

Les classements (A) restent inchangés : P1, P6, P9, P11, P12 sont abandonnés pour les raisons du tour III.1.

---

## (c) Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

1. **Le plafond ln 2 + max(0, ln(1/θ)) est prouvé pour toute division aveugle et toute taille**, sous fiche seule stérile (synthèse, section 3 : p. 32, l. 2358–2365). Il ne dépend ni de n, ni de la règle de division, ni de la fécondité. C'est la seule borne du papier transposable sans connaître le code de l'orchestrateur.

2. **La borne du prix R > e^U/(2 − e^U) est prouvée à toute taille pour θ ≥ 1** et toute règle aveugle (synthèse, section 4 : p. 40, l. 2786–2789). Elle donne des fécondités minimales calculables sans n.

3. **Le sort « perdu » pour les fusions inachevées ne coûte rien sur la charge à fécondité infinie** et coûte 1/(1−τ) en fécondité (synthèse, section 6 : p. 10, l. 863 ; p. 8, l. 703). Détruire et archiver hors du vivier sont dynamiquement équivalents sous archive étanche (VÉRIFIÉ par le papier, vérifiable par audit du code).

4. **Le bain de brouillons dans le vivier ne bat pas le rejet pur** dans le modèle du papier en l'absence de copies rapides non filtrables (I12 corrigée). Une réinjection n'a de domaine que sous q_B > 0 et θ′ < 2(1−τ).

5. **Cinq inexactitudes majeures (I4, I10, I11, I12, I21)** invalident les prédictions chiffrées qui s'appuyaient sur des extrapolations asymptotiques hors domaine ou des lectures fausses de tables.

### Ce qui n'est pas établi

1. **Aucune correspondance terme à terme** entre le papier et l'organisme n'est démontrée (synthèse, Verdict ligne 1). Le q du papier n'existe pas dans l'organisme ; n n'est pas connu ; le débit de copie est porté par un opérateur extérieur, non par les fiches fertiles ; les paires sont possiblement bipartites.

2. **La surmartingale de la densité de paires sous le noyau à deux parents** est une esquisse vérifiée algébriquement mais annotée « à contre-lire, jamais un résultat » (synthèse, §3.1). Elle suppose tirage uniforme dans une seule population et retrait indépendant du statut — deux conditions non vérifiées et possiblement violées (tirage bipartite, retrait sélectif).

3. **L'extinction quadratique à fécondité infinie** est plausible mais pas démontrée au standard du papier : la surmartingale n'implique pas seule l'absorption (critique D-(a)1 du tour précédent, critique D sur C dans ce tour), et le cas avec retrait ou budget fini reste ouvert.

4. **L'applicabilité du papier à la pince et à l'arène** n'est pas établie. P9 est abandonnée. Le levier r̄ est une propriété de division, pas de jugement.

5. **Aucun estimateur spectral n'est validé** aux effectifs de la course 2, a fortiori avec les erreurs du juge (biais de faux positifs créant des lots apparemment fertiles, critique C-(b)1). La course 2 est non jugeable pour l'allumage au niveau des lots.

### L'expérience à faire en premier

**L'audit du code de l'orchestrateur**, au processeur, sans dépense, sans journaux.

C'est l'étape (i) de la section 8 de la synthèse, renforcée par les critiques acceptées. Elle tranche simultanément :

- **n et la règle de division** (ou leur inexistence au sens du papier — critique D-(a)1) ;
- **θ et θ′** : fixés par l'orchestrateur ou endogènes ;
- **la consommation des parents** (si le bisociateur consomme les parents, l'allumage est exclu par l'argument du §3 de la synthèse, indépendamment de q) ;
- **le budget du bisociateur** : constant ou dépendant du vivier ;
- **la structure bipartite de l'appariement** : une ou deux populations ;
- **le retour possible d'un brouillon au vivier** et le critère d'abandon (voit-il le contenu ?) ;
- **le retrait des fiches** : uniforme ou sélectif.

Sans ces réponses, aucune prédiction ne peut être signée (le noyau n'est pas spécifié), aucun seuil ne peut être fixé (n et la règle de division changent U_c), et aucun estimateur ne peut être étalonné (la dimension de la matrice dépend de n). L'audit est déterministe, gratuit, et sa réalisation ou son impossibilité (code non obtenu) est elle-même un résultat : si le code n'est pas accessible, la correspondance papier–organisme est déclarée non testable en l'état.

**Immédiatement en parallèle** : la certification P10 des trois boîtes de (H2), qui ne dépend que du papier et peut être scellée et exécutée dès le jour 1.

FIN-DE-CELLULE