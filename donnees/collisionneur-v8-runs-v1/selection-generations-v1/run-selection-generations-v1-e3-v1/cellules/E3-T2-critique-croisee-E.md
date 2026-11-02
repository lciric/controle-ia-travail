# Proposition E — critique croisée de méthode

**RAPPORTÉ —** Les conceptions A, B, C et D sont présentes ; le code du pont et ses essais ne sont pas servis.

**Convention.** Les descriptions des propositions ci-dessous sont **RAPPORTÉES**, sans modification des statuts qu’elles attribuent à leurs sources. Mes objections, conditions mathématiques et contrôles proposés sont des **HYPOTHÈSES méthodologiques**, non des résultats expérimentaux.

Pour chaque comparaison recommandée, préenregistrer un paramètre \(\theta\), une marge \(\delta\), et le duel exclusif \(H_A:\theta>\delta\) contre \(H_B:\theta\leq\delta\). Une borne inférieure dépassant \(\delta\) réfute \(H_B\) au risque fixé ; une borne supérieure ne dépassant pas \(\delta\) réfute \(H_A\). Un intervalle chevauchant \(\delta\) ne tranche pas. **Absence de significativité et équivalence ne sont pas interchangeables.**

Les constantes dans les identités mathématiques ne sont pas des chiffres expérimentaux. Aucun nouveau seuil numérique n’est proposé.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSE méthodologique —**

- **E1 : les hypothèses ne couvrent pas les possibilités.** Les bandes de puissance proposées laissent un intervalle intermédiaire ; une puissance élevée accompagnée d’erreurs excessives n’appartient pas davantage aux deux issues annoncées. Comparer une ancienne épreuve à une nouvelle confond exposition, difficulté et distribution. Leur différence ne mesure pas exclusivement une fuite.
- **E2 : les contrôles négatifs ne sont pas garantis nuls.** Une fille de parents faux peut être vraie ; une fille de parents éliminés reste conditionnée par un verdict sur l’épreuve. Les éliminées ne constituent donc pas une population « non sélectionnée ». Enfin, une fréquence de faux témoins promus n’est pas le FDR.
- **E3 : l’instrument participe au résultat qu’il doit mesurer.** Définir la redite par le refus de la mémoire ne permet pas d’évaluer les erreurs de cette mémoire. Les raisons permutées peuvent devenir incohérentes ou plus difficiles à comprendre : elles contrôlent imparfaitement l’effet du contenu informatif.
- **E4 : Fisher ne teste pas le rendement monétaire.** Il teste une association entre comptes binaires sous ses conditions, pas un ratio incorporant coûts aléatoires. Les filles partageant des parents ne sont pas nécessairement des observations indépendantes. Une épreuve fraîche empêche une réutilisation directe, mais n’empêche pas la sélection d’hypothèses particulièrement compatibles avec le juge choisi comme mesure finale.
- **E5 : nouveauté et survie sont deux propriétés distinctes.** Une même proportion de « neuves » parmi promues et éliminées ne constitue pas un échec de la grille. Une loi tautologique n’est pas automatiquement « neuve mais non décisive ». L’accord interlecteurs ne mesure pas leur exactitude.
- **E6 : le monde plat peut se concentrer par dérive.** Interdire toute concentration dans ce monde transforme un phénomène d’échantillonnage possible en « artefact » par définition. Le comptage des lignées doit aussi traiter les descendances à plusieurs parents.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSES conditionnelles —** Notations : \(S\), promotion ; \(T\), vérité ; \(R\), redite ; \(L\), étiquette d’un lecteur ; \(C\), coût ; \(Y\), nombre de sorties.

| Mesures concernées | Conditions, paramètres et estimateurs |
|---|---|
| E1 : sensibilité, faux positifs | \(\pi=P(S=1\mid T=1)\), \(q=P(S=1\mid T=0)\). Sous indépendance, \(P(\widehat\pi=0)=(1-\pi)^n\). Avec corrélation intraclasse \(\rho\) et groupes de taille \(b\), \(n_{\mathrm{eff}}\approx n/[1+(b-1)\rho]\). |
| E2 : réutilisation | Pour \(D\sim P_D\), \(D'\sim P_{D'}\), \(\Delta=E[S(h(D),D)-S(h(D),D')]\). Si \(P_D\neq P_{D'}\), \(\Delta\) ne sépare pas dépendance adaptative et changement de loi. |
| E2 : erreur multiple | \(FDR=E[V/(R_s\vee1)]\), contre \(FPR=E[V]/m_0\), où \(R_s\) est le nombre de rejets. Ces paramètres ne coïncident pas en général. |
| E3 : mémoire et distances | \(P(\widehat R=1)=sP(R=1)+fP(R=0)\), avec \(s=P(\widehat R=1\mid R=1)\), \(f=P(\widehat R=1\mid R=0)\). Si \(s=f\), \(\widehat R\) n’identifie pas \(P(R=1)\). Si deux lois coïncident \(Q\)-presque sûrement mais diffèrent sous \(P\), toute distance intégrée sous \(Q\) est aveugle à cette différence. |
| E4 : rendement | \(r=E[Y]/E[C]\), généralement différent de \(E[Y/C]\). Pour \(\widehat r=\bar Y/\bar C\), \(\operatorname{Var}(\widehat r)\approx\operatorname{Var}(Y-rC)/(nE[C]^2)\). Une variance infinie, un dénominateur quasi nul ou un faible \(n_{\mathrm{eff}}\) invalide l’approximation usuelle. |
| E5–E6 : accord et diversité | \(\kappa=(p_o-p_e)/(1-p_e)\) est indéfini si \(p_e=1\). \(P(L_1=L_2)=1\) reste compatible avec \(P(L_1=T)=0\). Pour des fréquences \(p_\ell\), \(H=-\sum_\ell p_\ell\log p_\ell\) dépend de la partition ; une partition non fixée rend \(H\) non identifiable. |

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE méthodologique —**

- Pour E2 : descendants dont la nullité est définie par le générateur, indépendamment de celle des parents ; campagne non adaptative sur les mêmes lois d’échantillonnage.
- Pour E3 : raisons exactes, raisons non informatives mais cohérentes, et texte neutre apparié en longueur ; annotations de redite indépendantes de la mémoire.
- Pour E4 : sélection aléatoire à budget égal, répétitions au niveau des populations parentales, évaluation terminale commune et non utilisée pour choisir les parents.
- Pour E5–E6 : plan croisant nouveauté et vérité ; distribution de concentration obtenue sous reproduction neutre avec le même graphe de parenté.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSE méthodologique —**

- **E1 confond événement et puissance.** Une promotion démontre une réalisation possible, non une probabilité de promotion suffisante. Une « force » donnée ne détermine pas la puissance sans distribution des traits, fréquence de l’issue et précision du nul informé.
- **E2 établit au mieux une capacité locale.** Une sortie avec accord ne démontre ni fidélité sémantique ni capacité à produire ensuite les épisodes nécessaires. Un échec des témoins invalide l’instrument ; il ne réfute pas directement l’hypothèse portant sur les fiches réelles.
- **E3 oppose des hypothèses mal définies.** Pour que l’intersection soit strictement plus petite que chacun des ensembles, il faut des discordances dans les deux directions. Une seule discordance ne suffit pas. Surtout, une restriction supplémentaire peut être constituée uniquement de faux négatifs : elle ne prouve aucune utilité.
- **E4 sélectionne les filles avant de mesurer leur inflation.** La médiane « parmi les filles promues » est soumise à une troncature par le résultat. Les mères, déjà sélectionnées sur l’épreuve partagée, ne sont pas un contrôle négatif.
- **E5 ne relie pas correctement mécanisme et rendement.** Le pôle peut éliminer des faux sans accroître le rendement ; il peut accroître le rendement sans éliminer de fiche supplémentaire, par une autre sélection parentale. Choisir « au moins un axe » après observation ajoute une sélection.
- **E6 n’éprouve qu’un cas facile de distinction.** Changer le signe ou le moniteur ne couvre pas les lois différentes sur des régions rares, les reparamétrisations équivalentes ou les filles meilleures uniquement sur le développement.

### (b) Conditions probabilistes

**HYPOTHÈSES conditionnelles —** \(A\) et \(B\) désignent ici les indicatrices de passage des deux filtres, non les propositions.

| Mesures concernées | Conditions, paramètres et estimateurs |
|---|---|
| E1 : présence d’une promotion | \(P(\sum_{i=1}^nS_i\ge1)=1-(1-\pi)^n\) sous indépendance. Cette probabilité peut être élevée pour une puissance individuelle \(\pi\) faible lorsque \(n\) augmente. |
| E1 : force et information | Pour \(P_\beta(Y=1\mid X)=\sigma(a+\beta X)\), l’information par observation vaut \(I_\beta=E[X^2\sigma(a+\beta X)(1-\sigma(a+\beta X))]\). À \(\beta\) fixé, \(I_\beta\to0\) lorsque \(X\to0\) ou les probabilités saturent. |
| E2 : flux traduit | Avec \(u=P(\text{sortie admissible})\), \(P(K=0)=(1-u)^n\). Avec \(f=P(\text{traduction fidèle}\mid\text{accord})\), le rendement fidèle est \(uf\) ; \(u\) seul n’identifie pas \(uf\). |
| E3 : complémentarité | \(p_{ab}=P(A=a,B=b)\). Restriction stricte relativement aux deux filtres : \(p_{10}>0\) et \(p_{01}>0\). Utilité discriminante : comparer ces probabilités conditionnellement à \(T\), pas seulement marginalement. |
| E4 : richesse | Si \(S=\mathbf1\{W_R\ge c\}\), la loi \(P(W_R/W_F\mid S=1)\) diffère de \(P(W_R/W_F)\), même lorsque \(W_R,W_F\) ont la même loi marginale. Si \(P(W_F=0)>0\), le ratio peut être indéfini. |
| E5–E6 : rendement, mémoire | Pour des axes \(j\), \(\max_j\widehat\Delta_j\) est un estimateur sélectionné. Pour deux lois \(P,Q\), la somme des erreurs d’un test est au moins \(1-\operatorname{TV}(P^n,Q^n)\) ; si cette distance tend vers zéro, leur distinction perd sa puissance. |

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE méthodologique —**

- Pour E1–E2 : répétitions indépendantes à vérité connue ; traductions consensuelles mais sémantiquement fausses, issues d’un banc construit indépendamment des traducteurs.
- Pour E3 : fiches vraies rejetées par un seul filtre, fiches fausses acceptées par un seul filtre, et filtres artificiellement indépendants de la vérité.
- Pour E4 : toutes les filles gelées avant évaluation, y compris non promues ; lois non adaptées évaluées sur deux épreuves échangeables.
- Pour E5–E6 : sélection aléatoire terminalement évaluée ; lois équivalentes sous écritures différentes et lois différentes sous vocabulaire identique.

Le duel utile pour E3 porte sur un **gain de discrimination à coût fixé**, non sur une réduction mécanique du nombre de survivantes.

## Sur la proposition C

### (a) Défauts de méthode

**HYPOTHÈSE méthodologique —**

- **E1 favorise son second bras par définition.** Compter les fiches « gelées en attente » comme des découvertes retenues, mais exiger une promotion expérimentale dans l’autre bras, compare deux événements différents. Architecture, disponibilité des données et pondération statistique changent simultanément.
- **Le produit des puissances exige une condition.** La puissance conjointe n’est le produit des puissances marginales qu’en cas d’indépendance conditionnelle appropriée. De même, retirer des promotions par un second filtre ne garantit pas une réduction du FDR : ce filtre peut supprimer surtout les vraies.
- **FDP observé, FDR et FPR sont interchangés.** Aucun faux témoin promu dans un petit lot ne démontre une borne de FDR. Pour la pondération, la disjonction des données ne suffit pas : il faut préciser normalisation des poids et validité conditionnelle des e-valeurs.
- **E2 inverse une règle de décision.** Une borne supérieure dépassant le seuil ne démontre pas une inflation. Un test non significatif ne prouve pas l’équivalence. Sous nullité globale et reproduction réservée aux survivantes, l’extinction peut empêcher précisément l’adaptation que l’expérience veut étudier.
- **E3 modifie aussi le budget de recherche.** Le bras qui redemande après rejet reçoit potentiellement davantage de propositions et un retour informatif supplémentaire. Une sonde utilisée pour construire les signatures puis mesurer leur diversité crée une dépendance instrument–évaluation.
- **E4 mesure notamment le dépassement du seuil d’arrêt.** Une somme des excès de \(\log W\) peut refléter la granularité des incréments et la règle d’arrêt davantage que l’information prédictive. Une e-valeur n’est pas, sans construction supplémentaire, un facteur de Bayes. L’évaluation e-BH commune couple aussi les promotions des deux bras.
- **La porte de sortie contient une contradiction de vérité terrain.** Des hypothèses du programme simplement masquées sont des témoins de redondance, pas des témoins positifs de nouveauté. L’identification du modèle de la banque à celui d’un article cité n’est pas établie par les pièces.

### (b) Conditions probabilistes

**HYPOTHÈSES conditionnelles —**

| Mesures concernées | Conditions, paramètres et estimateurs |
|---|---|
| Conjonction | \(\pi_{AB}=P(A=1,B=1\mid T=1)=\pi_A P(B=1\mid A=1,T=1)\). Bornes : \(\max(0,\pi_A+\pi_B-1)\le\pi_{AB}\le\min(\pi_A,\pi_B)\). |
| Pondération | Avec une information préalable \(\mathcal F\), conditions suffisantes : \(w_i\ge0\), \(\sum_iw_i\le m\), et \(E[E_i\mid\mathcal F]\le1\) sous chaque nul. Alors \(E[w_iE_i]\le E[w_i]\). Sans cette inégalité conditionnelle, la pondération peut perdre sa garantie. |
| E1 : attente et confirmation | \(u=P(\text{retenue})\), \(v=P(\text{confirmée}\mid\text{retenue})\). Le rendement confirmé vaut \(uv\). Si \(v\) est inconnu, \(u\) ne l’identifie pas. |
| E2 : extinction | Si \(N_{g+1}=0\) lorsque \(R_g=0\), alors \(P(R_{g+1}>0)\le P(R_g>0)\). Sous nullité globale, \(FDR_g=P(R_g>0)\). Une faible valeur marginale peut coexister avec \(P(R_{g+1}>0\mid R_g>0)\) élevé. |
| E3 : diversité | \(D_Q=E_{X\sim Q}[\operatorname{JS}(p_i(\cdot\mid X),p_j(\cdot\mid X))]\). Si \(Q(A)=0<P(A)\), \(D_Q\) n’identifie pas la diversité sur \(A\). Si \(Q=Q(p_i,p_j)\), \(\widehat D_Q\) est adaptatif. |
| E4 : arrêt et rendement | \(\tau=\inf\{t:\log W_t\ge c\}\), \(O=\log W_\tau-c\). Si les incréments sont bornés par \(\varepsilon\), \(0\le O\le\varepsilon\) au franchissement. Si la taille des incréments varie entre bras, \(E[O]\) n’identifie pas leur différence de gain prédictif. |

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE méthodologique —**

- E1 : même définition de confirmation dans tous les bras ; variation séparée de la pondération, du filtre et du statut administratif. Témoins en attente sans effet réel.
- E2 : propositions nulles renouvelées indépendamment de la survie, avec compte explicite des lignées éteintes ; campagne non adaptative.
- E3 : mêmes nombres d’appels et possibilités de nouvelle proposition ; sonde d’évaluation indépendante ; raisons neutres appariées.
- E4 : scores prédictifs à horizon terminal fixé, doublons et descendants sans gain conditionnel ; même exposition d’évaluation.
- Sortie : paraphrases du programme comme négatifs de nouveauté ; cas réellement distincts annotés indépendamment.

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSE méthodologique —**

- **E1 ne peut réfuter une existence populationnelle par absence dans un échantillon.** Toutes les fiches échantillonnées immédiatement testables n’excluent pas une classe rare de différées. Le duel mélange également disponibilité des données et fidélité du pont.
- **E2 attribue trop au renouvellement.** Des épreuves fraîches ne suffisent pas, seules, à contrôler l’erreur cumulée d’une campagne. Il faut définir l’événement contrôlé et la politique d’allocation. Une borne supérieure exigée sous la borne nominale sera difficile à certifier lorsque le taux réel est proche de cette borne.
- **E3 conclut trop vite d’une absence de gain.** Il manque une marge d’équivalence et une règle d’incertitude. « Codes minimaux » et « motifs complets » changent simultanément longueur, contenu et précision.
- **E4 peut récompenser le descripteur qu’il impose.** Une garde construite pour remplir des cellules augmente leur couverture par construction. « Familles indépendantes » n’est pas défini par une partition lexicale ou généalogique.
- **E5 reste dépendante du budget et de l’arrêt.** À budget égal, les nombres de propositions, parents et tests peuvent différer : c’est acceptable pour comparer des politiques complètes, pas pour isoler l’effet du filtre. Une génération descendante peut informer un effet d’héritage à court terme ; elle ne démontre pas sa persistance.
- **La confirmation finale n’efface pas automatiquement toutes les sélections.** Les objets, critères et allocations choisis adaptativement doivent rester gelés avant cette confirmation.

### (b) Conditions probabilistes

**HYPOTHÈSES conditionnelles —**

| Mesures concernées | Conditions, paramètres et estimateurs |
|---|---|
| E1 : classe différée | Si \(d=P(\text{différée})>0\), \(P(K=0)=(1-d)^n>0\) pour tout \(n\) fini et \(d<1\). L’événement \(K=0\) ne réfute pas \(d>0\). |
| E2 : campagne | Sous nullité globale, \(FDR_{\mathrm{camp}}=P(\bigcup_g\{R_g>0\})\). Si ces événements sont indépendants et de probabilités \(\alpha_g\), cette quantité vaut \(1-\prod_g(1-\alpha_g)\). |
| E3 : gain | \(\Delta=E[Y_{\mathrm{complet}}]-E[Y_{\mathrm{minimal}}]\). Si \(|\Delta-\delta|\ll SE(\widehat\Delta)\), le signe relativement à \(\delta\) n’est pas jugeable. |
| E4 : familles | Avec classes latentes \(Z\), labels observés \(\widehat Z\) et matrice \(M_{ab}=P(\widehat Z=a\mid Z=b)\), une matrice \(M\) de rang insuffisant n’identifie pas les fréquences latentes. |
| E5 : rendement et arrêts | Pour \(\tau_B=\inf\{t:\sum_{j\le t}C_j\ge B\}\), \(Y_B=\sum_{j\le\tau_B}S_j\). Si \(C_j\) et \(S_j\) dépendent d’une difficulté commune, modifier leur loi jointe modifie \(E[Y_B]\), même à \(P(S_j=1)\) constant. |

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE méthodologique —**

- E1 : classes rares de différées injectées indépendamment ; pont fidèle sur fiches non immédiatement exécutables.
- E2 : nullité globale **et** mélange de nuls et d’alternatives, avec épreuves fraîches dans les deux cas ; comptabilité cumulative des erreurs.
- E3–E4 : textes neutres de longueur égale ; quotas aux descripteurs permutés ; partitions indépendantes de la garde.
- E5 : politique aléatoire à budget égal ; distribution indépendante des coûts pour distinguer sélection scientifique et avantage économique ; confirmation terminale commune.

**HYPOTHÈSE méthodologique — Conclusion E :** je ne retiendrais aucune décision « la boucle fonctionne/ne fonctionne pas » avant séparation de trois paramètres : **validité de l’erreur, puissance conditionnelle à la testabilité, rendement de la politique complète**. Les confondre rend plusieurs issues annoncées vraies par construction ou impossibles à interpréter.

FIN-DE-CELLULE