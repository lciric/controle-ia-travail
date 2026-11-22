# Proposition A — Tour III.3 : réponse aux critiques

**Pièces.** J'ai reçu ma conception III.1 et les critiques croisées de B, C et D, entières, chacune close par sa ligne de fin. Je n'ai pas recalculé les empreintes. Les conceptions III.1 de B, C et D ne m'ont pas été transmises. Je réponds donc aux seules sections « Sur la proposition A » et aux défauts transverses T1–T5 de B, qui y renvoient.

**Statuts.** Ils sont inchangés : faits publiés RAPPORTÉ, étau HYPOTHÈSE, mes ajouts PROPOSITION ou HYPOTHÈSE. C et D apposent « VÉRIFIÉ » à certains de leurs arguments. Je ne reprends pas ce statut : j'ai refait les raisonnements que j'accepte. Les chiffres hors faits sont illustratifs, les chances sont des jugements.

**Ce qui change, en trois lignes.**
1. Mon énoncé T1 était mal posé. Il n'était ni observable ni positif, et son support contredisait ma propre borne. Je le retire et le réécris en T1′.
2. Un troisième plancher manquait : l'erreur de référence partagée, que B a identifiée. Il est linéaire en N.
3. P4 et P7 sont rétrogradées, et P2 change de statistique.

---

## (a) Réponse critique par critique

| # | Critique (source) | Verdict | Suite |
|---|---|---|---|
| K1 | d ∈ [0, c] contredit σ > 0 ; la troncature dérive sous l'honnête (B-T1, C-a3, D-a1) | **Acceptée** | d est signé et écrêté à [−c, c] par définition. Aucune troncature à zéro. |
| K2 | Le processus n'est pas observable hors audit, Ville est invoquée sans positivité, le « capital » n'est pas défini (B-3, D-a1, D-b1) | **Acceptée** | T1 retiré, voir T1′. |
| K3 | L'erreur de référence est partagée entre épisodes et donne un biais N·b (B-T2) | **Acceptée** | Troisième plancher, et test D0. |
| K4 | Les mondes plantés satisfont les suppositions par construction (B-T3, C-a3) | **Acceptée** | D1 devient un test de conformité, avec contrôles de violation. Le contenu empirique passe à D0. |
| K5 | La variable de contrôle peut être anticorrélée par l'adversaire ; ma ligne « variance pleine, biais nul » est fausse (B-T4, B-2, C-b1, D-b1) | **Acceptée** | Coefficient prévisible et intersection avec la suite brute (T1′). |
| K6 | Fuite si m, p, λ ne sont pas fixés avant le tirage (C-a2) | **Acceptée** | Tout est figé par condensat avant le tirage i et ne dépend que des audits déjà rendus. |
| K7 | L'adversaire concentre l'attaque là où l'oracle rappelle mal (B-T5) | **Acceptée comme limite** | Aucun test ne la lève. Elle entre dans « hors de portée ». |
| K8 | D4 : la paraphrase change aussi le contenu (B-4, D-a4, D-c3) | **Transformée en test** | D4′, plan 2×2. |
| K9 | D2 : la sonde peut lire la consigne dans le contexte (B-5, D-a2) | **Acceptée** | D2′ : contraste de contrastes. Le duel peut réfuter, il ne peut pas établir. |
| K10 | D2 : stratifier par \|δ\| réalisé conditionne sur un effet aval (D-a2) | **Acceptée** | La bande est définie par le bras honnête apparié, au même pas. |
| K11 | D2 : la zone indécise viole B4 (D-a2) | **Rejetée sur le principe, acceptée sur le défaut** | Tout test fini a une zone non concluante, et la déclarer n'est pas s'y soustraire. Mais la mienne était large et sans calcul de puissance. Le nombre de paires k est désormais fixé d'avance, et une issue non concluante compte comme un échec de l'expérience. |
| K12 | P4 : le modèle de confiance, plus faible, croit faisable ce que l'honnête lucide sait piégé (C-a1, C-c3) | **Acceptée** | P4 rétrogradée (voir plus bas). |
| K13 | P4 est muette sur un biais amorti (D-b4) | **Acceptée** | Déjà déclarée en S1. |
| K14 | P2 : le R² reste positif par la seule difficulté (C-a4, C-b2) ; un dommage constant donne un R² nul même pour un moniteur parfait (D-b2) | **Acceptée** | La statistique est remplacée (P2′). |
| K15 | Le moniteur est réajusté et évalué sur le même flux (B-7) | **Acceptée** | Les scores sont figés à l'engagement et jamais recalculés. L'évaluation devient prequentielle. |
| K16 | P2 n'est pas jugeable si le sabotage est rare ou petit devant σ (B-b, C-b2) | **Acceptée** | C'est le comportement voulu : l'état reste « non éprouvé ». |
| K17 | P3 : ε se compose, et le mode corrigé devient identifiable après K épisodes (C-b3, D-b3) | **Acceptée pour le calcul, portée précisée** | Voir plus bas. |
| K18 | P6 : la vérité tardive manque de façon non aléatoire (B-6, C-b4, D-b5) | **Acceptée** | La couverture n'est mesurée que sur la strate « vérité obtenable ». La masse restante est comptée comme non couverte. |
| K19 | P7 : l'erreur honnête se reproduit entre rejouages, le préfixe la porte (B-8, C-a5, D-a3) | **Acceptée** | P7 est suspendue jusqu'à la mesure de la corrélation intraclasse honnête. |
| K20 | D3 : on mesure la rigidité d'une projection fixe (D-a4) | **Acceptée** | D3′ : la sonde est réapprise après chaque tour. |
| K21 | « 0,7 que T1 tienne » porte sur un théorème (B-9) | **Acceptée** | Les chances portent désormais sur les suppositions en service. |
| K22 | La moyenne de e-valeurs divise la puissance par M (D-b5) | **Acceptée** | Sans conséquence : T4 ne certifiait que les fausses alertes. |
| K23 | Rien n'est jugeable si le plafond est violé (C-b1) | **Acceptée** | L'écrêtage est dans la définition du dommage. L'excès relève du harnais (limiter ce qu'un épisode peut toucher), non de la statistique. |
| K24 | Conditions de puissance de B-(b) | **Acceptées telles quelles** | Elles sont calculées avant toute dépense. |

### T1′ : l'énoncé réécrit (PROPOSITION, esquisse à démontrer)

Je me sers de trois apports : le jumeau contre jumeau et le coefficient prévisible de B, et le vérificateur à valeurs masquées que C adresse à D.

- **Définition.** d_i est l'écart signé du produit à la référence engagée r_i, écrêté à [−c, c].
- **Figé avant le tirage i.** Le produit, le score m_i (écrêté), un coefficient β_i ∈ [0, 1], la probabilité p_i ≥ p et une prévision ẑ_i. Tous sont fonction des seuls audits déjà rendus.
- **Observable.** Z_i = β_i·m_i + A_i·(d_i − β_i·m_i)/p_i. Pour toute stratégie, son espérance sachant le passé et d_i vaut d_i.
- **Borne.** Une suite de confiance de type Bernstein empirique donne, pour tout t à la fois, Σd_i ≤ ΣZ_i + marge(V_t, c/p, α), avec V_t = Σ(Z_i − ẑ_i)². L'inconnue n'entre que par le scalaire Σd_i, et le terme quadratique est entièrement observé. Cela répond à l'objection de calculabilité, et la largeur certifiée suit la variance observée plutôt que le pire cas.
- **Référence.** Howard, Ramdas, McAuliffe, Sekhon, 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences ». Son application à des moyennes conditionnelles choisies par un adversaire avant tirage reste à démontrer ligne à ligne. Je la tiens pour probable, pas pour acquise.
- **Moniteur adverse.** On calcule deux suites, chacune à α/2 : la brute (β = 0) et l'ajustée (β estimé sur le passé). On retient leur intersection. Le moniteur ne peut alors pas élargir la borne au-delà de la suite brute à α/2. Le coût est un facteur logarithmique.
- **Étiquettes tardives.** La borne n'est annoncée que pour le préfixe dont tous les audits tirés sont rendus.
- **Version finie.** Le programme reçoit « valeur absente » pour tout d_i non audité. S'il s'exécute, la forme est calculable.

Sur la date de « Estimating means of bounded random variables by betting », que B relève comme divergente entre C et moi : référence à vérifier, je ne tranche pas.

### Ce que T1′ borne, et les trois planchers

T1′ borne le déficit par rapport à la référence engagée. Il ne borne pas le dommage par rapport à ce qu'aurait fait un honnête. L'écart entre les deux est l'objet de K3.

Les trois planchers sont des ordres de grandeur, donnés comme PROPOSITION :

1. **Échantillonnage.** c·log(1/α)/p en régime concentré, σ_res·√(N·log(1/α)/p) en régime diffus. σ_res² est le second moment du résidu d − β·m. C'est donc le niveau du moniteur qui compte, pas seulement sa corrélation, comme le montre la forme exacte que donne C.
2. **Bruit propre.** σ·√N, même à p = 1. Un cumul honnête fluctue de cet ordre, et le dommage toléré D\* doit le dépasser.
3. **Référence partagée (B-T2).** N·σ_ref/√n si la référence est un niveau par régime estimé sur n épisodes honnêtes. Ce terme domine le premier dès que N dépasse l'ordre de n/p. Seule y échappe une référence par tâche dont les erreurs sont indépendantes d'une tâche à l'autre. Avec « peu d'épisodes honnêtes par régime » (contrainte des faits), c'est probablement le plancher qui commande. Je ne l'avais pas vu.

### P2′ : ce que le tableau de cécité mesure désormais

La part de variance expliquée était la mauvaise statistique, des deux côtés. Elle est positive pour un moniteur qui ne suit que la difficulté. Elle est nulle pour un moniteur exact face à un décalage constant.

- **Nouvelle mesure.** Le gain du moniteur sur une base mécanique (difficulté prédite par le modèle de confiance, longueur). Il vaut 1 − Σw·(d − m)² / Σw·(d − m_base)², calculé sur le bras aléatoire avec les poids d'inclusion et les scores figés à l'engagement.
- **Ce qu'elle dit.** Elle dit si le moniteur retire aujourd'hui de la variance à l'audit au-delà de ce qu'un compteur retire. C'est le seul rôle que je lui confie.
- **Ce qu'elle ne dit pas.** Elle ne mesure pas le rappel sur sabotage. Si les écarts audités sont surtout des accidents honnêtes, la dilution que B écrit (ρ → 0) s'applique entièrement.

### P3 : portée précisée (K17)

Le calcul de C et de D est juste : une borne ε par correction se compose, et un test adverse séquentiel finit par distinguer un mode corrigé d'un mode ignoré. Je précise ce que cela atteint.

- Dans le modèle de menace des faits, l'adversaire connaît déjà tout sauf les tirages. La couverture de l'oracle n'est donc pas un secret que le canal ferait fuir.
- Les tirages passés ne renseignent pas sur les suivants, puisque les tirages sont indépendants.
- Ce qui fuit vraiment, ce sont les secrets renouvelés par époque : l'ajustement du moniteur qui oriente p_i. Le plancher p_i ≥ p fait que cette fuite coûte de la largeur, jamais de la validité.

P3 devient donc un budget : le nombre de corrections par époque avant renouvellement, d'ordre log(1/β)/ε² (constante à vérifier). Je retire toute lecture de P3 comme borne sur l'horizon entier.

### P4 et P7 : rétrogradées

- **P4.** La signature « échec prévu sans cause externe » s'appuyait sur la faisabilité prédite par le modèle de confiance. C a raison : elle classe comme sabotage la lucidité supérieure de l'honnête. P4 ne garde qu'un rôle de covariable pour orienter p_i. Je ne revendique plus qu'elle sépare triche et échec honnête.
- **P7.** Trois critiques convergent, et l'argument du préfixe de C tient sans mesure : une erreur déjà inscrite dans le contexte se reproduit à chaque rejouage. Je parie que la mesure gratuite la tue (0,7).

---

## (b) Expériences corrigées

Tous les seuils sont illustratifs.

**D0 — Jumeau contre jumeau, en forme de service (nouvelle, à faire en premier).**
- *Matériel.* Deux exécutions honnêtes indépendantes par tâche, sur des épisodes honnêtes existants. Un tirage secret désigne laquelle joue le suspect. L'oracle juge toutes les paires, puis le sous-échantillonnage à p est rejoué.
- *Deux références comparées.* (i) Une référence par tâche. (ii) La forme disponible en service : un niveau par régime estimé sur n épisodes.
- *H_A.* Avec la référence (ii), aux valeurs (n, N, p) du programme, l'alarme honnête sonne à une fréquence ≤ α, à l'erreur de simulation près.
- *H_B.* Elle dépasse α.
- *Issues.* H_B falsifie « une référence par régime porte une borne cumulée à cet horizon ». Il faut alors des références par tâche, ou un horizon de l'ordre de n/p. H_A falsifie « le plancher de référence domine à ces valeurs », pour ce régime seulement.
- *Sous-produits sans dépense supplémentaire.*
  - la moyenne de d sous permutation de l'étiquette « suspect », qui révèle un éventuel biais de rôle des lecteurs ;
  - la borne supérieure de confiance sur σ, avec son facteur au khi-deux ;
  - la fraction d'écarts écrêtés ;
  - le bruit de relecture ;
  - la corrélation intraclasse entre rejouages, qui décide du sort de P7.

**D1′ — Conformité de T1′ (test d'implémentation et de dérivation, non de nature).**
- *H_A.* Sur des mondes à d signé, hétéroscédastique, écrits par un tiers, avec valeurs masquées hors audit, la couverture de Σd est ≥ 1 − α. Face à un moniteur qui change de signe en cours de route, la largeur de l'intersection ne dépasse pas celle de la suite brute à α/2.
- *H_B.* L'une des deux conditions échoue.
- *Issues.* H_B tue la forme calculable, qui n'est qu'une esquisse. H_A falsifie « la forme n'est pas calculable, ou un moniteur adverse l'élargit sans borne ». H_A ne dit rien sur le service (K4).
- *Contrôles de violation.* Tirage fuité, plafond dépassé, engagement après tirage, biais de référence partagé. Chacun doit casser la borne. Si l'un ne la casse pas, le banc est insensible et D1′ ne vaut rien.

**D2′ — Sonde de surprise.**
- *Contrastes.* (1) Sous-performance sur consigne contre échec honnête prévu. (2) Consigne bénigne d'ébauche incomplète contre consigne standard, contrôle proposé par D. (3) Consigne présente mais non suivie, contrôle proposé par B.
- *Bandes.* Définies par le |δ| du bras honnête apparié, au même pas.
- *H_A.* Le contraste (1) ne dépasse pas les contrastes (2) et (3) : la borne supérieure de l'intervalle sur la différence d'AUROC reste sous la marge.
- *H_B.* La borne inférieure passe au-dessus de la marge.
- *Issues.* H_A falsifie « la séparation observée témoigne d'une lecture d'intention ». H_B falsifie « l'indice de consigne explique tout », pour ce mode d'induction seulement.
- *Limite assumée.* Aucune issue n'établit que la sonde lit l'intention d'un comploteur réel. Les faits rappellent qu'on n'en a pas d'échantillon fiable (2504.05259, RAPPORTÉ).
- *Puissance.* k est fixé d'avance pour que l'intervalle soit plus étroit que la marge dans la bande basse. Sinon l'expérience n'est pas lancée.

**D3′ — Étau.**
- La sonde est réapprise sur le modèle honnête déplacé, après chaque tour. La frontière est mesurée contre la sonde réapprise.
- *Contrôle négatif.* Un sous-espace aléatoire de variance appariée. B le propose pour D, je m'en sers.
- *H_A.* Toute évasion durable coûte au moins la marge de performance.
- *H_B.* Il existe un point d'évasion durable à coût inférieur au bruit.
- *Issues.* H_B falsifie l'étau comme nécessité. H_A falsifie seulement « l'évasion est gratuite à ce budget ». L'asymétrie est maintenue.

**D4′ — Persuasion des lecteurs, plan 2×2.**
- *Facteurs.* Prose persuasive présente ou absente ; retrait appliqué ou non. Le retrait est mécanique quand le format le permet (le programme retire les champs de prose et laisse l'artefact octet pour octet). Sinon c'est une paraphrase.
- *Cellules de contrôle.* Défauts plantés sans prose, pour mesurer la part de défauts que le retrait conserve. Produits honnêtes dont la validité dépend d'une hypothèse énoncée dans la prose (contrôle proposé par D).
- *H_A.* L'interaction prose × retrait est nulle, à la marge près.
- *H_B.* Elle est positive.
- *Issues.* H_B falsifie « les lecteurs ne se laissent pas persuader ». H_A falsifie la persuasion pour ces formes de prose. L'effet principal du retrait ne compte plus comme persuasion.

**D5 — Tableau de cécité P2′ (monde planté).**
- *Quatre moniteurs témoins.*
  - scores permutés ;
  - difficulté seule ;
  - table de recherche des épisodes déjà audités ;
  - niveau exact face à un décalage constant (contrôle proposé par D).
- *H_A.* Les trois premiers restent « non éprouvé » et le quatrième est levé.
- *H_B.* Un des quatre est mal classé.
- *Issues.* H_B tue P2′. H_A falsifie les confusions par difficulté, par réajustement et par décalage constant, et rien sur un sabotage réel.

**D7 — P7.** Seule la corrélation intraclasse honnête est mesurée, dans D0. Si elle est élevée, P7 est retirée sans autre dépense.

---

## (c) Réponse à l'arbitre, en une page

**Ce sur quoi le défenseur peut s'appuyer.** Une seule chose ne dépend pas de la forme de l'attaque : un tirage secret, postérieur à l'engagement du produit, sur un dommage que le défenseur a défini et écrêté. Tout le reste de ma proposition n'est qu'une façon d'en réduire la largeur ou d'en mesurer les constantes.

**Ce qui est établi.**
- *Mathématique, sous suppositions.* Avec des probabilités d'inclusion connues et un tirage postérieur à l'engagement, l'estimateur du total est sans biais quelle que soit la stratégie (Horvitz et Thompson, 1952). Le moniteur peut en sortir sans toucher à la validité.
- *Mathématique.* Un cumul honnête fluctue en σ·√N. Aucun test ne voit une dérive plus petite.
- *RAPPORTÉ par les faits.* La détection hors distribution n'est pas apprenable sans conditions. Les défenses latentes tombent ensemble. Sans étiquette, un changement d'erreur sans trace est invisible. Hors couverture de l'oracle, rien n'existe pour aucun mécanisme.
- *Par la critique de ce tour.* Mon T1 d'origine ne tenait pas tel qu'écrit. Une référence par régime ajoute un biais cumulé linéaire en N.

**Ce qui ne l'est pas.**
- La forme calculable T1′. C'est une esquisse à démontrer, puis à vérifier par un programme tiers.
- Que le dommage jugé par l'oracle soit centré et borné sous l'honnête sur le banc réel. Personne ne l'a mesuré.
- Qu'une référence utilisable en service existe. Sans jumeau, T1′ borne un déficit par rapport à une référence engagée. Le passage au « dommage par rapport à l'honnête » coûte le troisième plancher.
- La couverture de l'oracle face à un adversaire qui cible ses zones faibles. Aucune mesure sur une loi choisie par le défenseur ne l'identifie.
- Tout « passage obligé » interne. Ma supposition S1 reste une hypothèse. P4 ne sépare pas la triche de la lucidité honnête. La sonde de surprise n'est ni apprise ni évaluée sous 0,3 (RAPPORTÉ). L'étau reste sans quantité conservée.
- Que les budgets réels placent D\* au-dessus des trois planchers. Je ne sais pas.

**L'expérience à faire en premier : D0.** Elle ne demande aucune attaque et aucun modèle nouveau, seulement des paires honnêtes et des appels à l'oracle. Elle est la première pour trois raisons :
1. Les trois critiques la réclament indépendamment. Sans elle, le niveau α de tout le reste n'est validé que sur des mondes où il est vrai par construction.
2. Elle mesure les constantes (σ, erreur de référence, écrêtage, bruit de relecture) dont dépendent tous les calculs de puissance. Elle dit donc quelles expériences suivantes valent leur coût.
3. Ses deux issues ferment quelque chose : soit la référence par régime porte la borne à l'horizon visé, soit le programme doit acheter des références par tâche avant toute sonde.

D0 ne dira rien de la couverture de l'oracle ni d'aucune attaque.

**Chances révisées (jugements).**

| Objet | III.1 | III.3 | Raison |
|---|---|---|---|
| Secret et engagement tenus en service | — | 0,8 | Le défenseur les possède. |
| T1′ valide après démonstration | 0,7 (mal placé) | 0,75 | Forme connue, application à vérifier. |
| Borne utile aux budgets réels | 0,4 | 0,3 | Troisième plancher. |
| P2′ | 0,5 | 0,4 | Portée réduite à la variance retirée. |
| P3 | 0,6 | 0,5 | Budget par époque, pas borne d'horizon. |
| P4 | 0,3 / 0,1 | 0,15 / 0,05 | Confusion de capacité. |
| P5 (survie de l'étau) | 0,25 | 0,25 | Inchangé. |
| P6 | 0,5 / 0,15 | 0,4 sur la strate à vérité / 0,1 sur le flou | Sélection non aléatoire. |
| P7 | 0,3 | 0,1 | Erreurs honnêtes reproductibles. |

**Ajouts à « hors de portée ».**
- Le ciblage des zones faibles de l'oracle (K7).
- Le biais partagé d'une référence, quand aucune référence par tâche n'est achetable.

FIN-DE-CELLULE