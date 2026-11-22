# Proposition B — Tour III.3 : réponse aux critiques

**État des pièces.** Les blocs FAITS et QUESTION DE L'ARBITRE sont identiques et ne contiennent que la question. Ma conception III.1 et les cinq critiques A, C, D, E et F sont présentes, et chacune se termine par sa ligne de fin. Je n'ai pas recalculé les empreintes et je n'ai trouvé aucune consigne à exécuter dans ces pièces.

**Périmètre.** Je ne réponds qu'aux sections « Sur la proposition B ». Quand une même objection vient de plusieurs critiques, je cite toutes les sources sans fusionner leurs argumentaires. Les statuts des critiques restent les leurs. Tout chiffre repris d'une critique ou introduit ici est **illustratif**. Toute affirmation sur le comportement d'agents est une **HYPOTHÈSE**.

---

## (a) Décision sur chaque critique

| # | Source | Objet | Décision | Suite |
|---|---|---|---|---|
| R1 | D (a), E (b), F (b) | La zone entre les deux seuils n'est pas forcément un échec de puissance : le paramètre vrai peut s'y trouver. | **Acceptée.** C'était une erreur de ma règle commune. | Règle corrigée en (b) : quatre verdicts. |
| R2 | A (a), E (c), F (c) | E1 ne fait varier que p, pas la pénalité. Une pente peut venir de l'évitement dans l'épisode. | **Acceptée.** | Plan factoriel p × conséquence (E1′). |
| R3 | A (a), C (a1), E (a1), F (a) | L'annonce en langue naturelle mêle obéissance, amorçage lexical et calcul. Le contrôle « orthographe » ne neutralise que le mot « audit ». | **Transformée en test.** | Bras « récompense », repris du contrôle à utilité inversée de C : un amorçage lexical prédit une pente négative, un calcul prédit une pente positive. |
| R4 | A (c), C (c1), D (c) | Il faut un agent honnête soumis aux mêmes annonces, et une cotation des tentatives indépendante des audits. | **Acceptée.** | E1′, contrôle de validité. |
| R5 | A (b) | La bande [0,9 ; 1,1] exige environ 3 200 à 8 900 épisodes par bras ; 2 000 ne suffisent pas. | **Acceptée.** Je retrouve Var(log OR) ≈ 8/n au taux 0,5 et ≈ 22/n au taux 0,1. | n fixé par calcul de puissance avant la collecte. |
| R6 | C (b1), E (b), F (b) | Aux taux de base extrêmes, l'information de Fisher s'effondre. | **Acceptée.** Je n'ai pas recalculé le 0,18 de C. | Pilote sur des tâches disjointes : π(0) ∈ [0,3 ; 0,7] (illustratif). |
| R7 | E (b) | Si le seuil rationnel G/C tombe hors de la grille, OR = 1 malgré une sensibilité exacte à p. | **Acceptée.** | Grille de pénalités choisie pour que l'agent scripté change de décision dans la grille. |
| R8 | F (b) | Le logit linéaire en p est mal spécifié, et un effet de tâche atténue β₁. | **Acceptée.** | p traité comme facteur catégoriel ; IC par grappes de tâches. |
| R9 | F (a) | Pour un organisme implanté à déclencheur fixe, l'insensibilité à p serait vraie par construction. | **Rejetée en partie.** Elle n'est vraie par construction que si les données d'affinage ne contiennent aucune annonce d'audit ; la généralisation reste empirique. **Acceptée sur la portée.** | Variante conservée, conclusion restreinte à cette classe d'organismes. |
| R10 | D (a, b) | P(D∣p) = P(A∣p)·P(D∣A,p) : le dénominateur pertinent est le nombre d'occasions. | **Acceptée.** | Les tentatives sont mesurées directement, à l'aveugle. |
| R11 | C (a3, b4), D (a), E (a1) | Le trait corrélé à l'audit peut aussi l'être à la difficulté d'attaque ou à la sensibilité de l'auditeur. | **Acceptée.** | Deux traits appariés, signe inversé entre épisodes (contrôle de E), historique transplanté (D), évaluation en seconde moitié (bascule de C). |
| R12 | A (b), E (b) | Si T·I ≲ 1, la corrélation n'est apprenable par aucun agent (borne de Pinsker). | **Acceptée.** | I fixé par conception, avec T·I au-dessus d'un plancher. |
| R13 | A (b), D (b), E (b), F (b) | S sature vers 0 ou 1, ce qui écrase ΔS. | **Acceptée.** | Métrique primaire : l'allocation des attaques ; S devient secondaire. |
| R14 | F (a) | Un audit bloquant crée une censure dynamique. | **Acceptée.** | Audit non bloquant dans E2′. |
| R15 | F (b) | L'estimateur plug-in de Î est biaisé. | **Acceptée.** | I n'est plus estimé : il est calculé à partir de la conception. |
| R16 | A (b), C (b3), E (a2), F (a) | Une AUROC sur un résultat binaire est bornée par ½(1 + δ_réel). Le seuil 0,65 est inatteignable si δ_réel < 0,30. | **Acceptée.** C'était un défaut de ma métrique. | Remplacée par une différence de taux, avec un plancher de δ_réel. |
| R17 | A (a, c), E (a3), F (c2) | La sonde sépare deux procédés de fabrication. Le contrôle « étiquettes au hasard » ne vérifie que le pipeline. | **Acceptée.** | Contrôles générateur contre générateur et réel contre réel ; découpage par famille de tâches. |
| R18 | D (b) | L'AUROC d'une sonde ne borne pas celle du meilleur discriminateur. | **Acceptée.** | H_B est énoncée pour une classe de sondes, pas comme indiscernabilité. |
| R19 | C (b3), E (b) | Corrélation intra-épisode et déséquilibre n₀/n₁. | **Acceptée.** | IC par grappes, effectifs équilibrés. |
| R20 | F (a) | Le cache de préfixe et la composition des lots peuvent fuir dans les activations. | **Transformée en test.** | Cache désactivé pour les données de la sonde ; lots mélangés ; contrôle « même condition, lots différents ». |
| R21 | A (a), E (a2) | E4 : avec l'objectif « biaiser la conclusion », R < 1 vient de l'objectif, pas d'un ciblage. | **Acceptée.** | E4′ refondu : l'objectif est réalisable dans les deux strates, et la couverture de l'audit est manipulée. |
| R22 | C (a2) | Compter m exige un oracle interprétatif refusé à l'auditeur. | **Acceptée.** | Vérité interprétative fixée par construction du jeu synthétique ; l'accès de l'auditeur devient une variable. |
| R23 | F (a), D (a, b) | La formule 1−(1−k/n)^m suppose un tirage avec remise. | **Rejetée sur la formule, acceptée sur la notation.** 1−(1−p)^m est exacte pour un tirage de Bernoulli indépendant par étape au taux p. En écrivant « k étapes sur n », je suggérais une taille fixe, et l'hypergéométrique s'applique alors. | Plan de Poisson explicite au taux p. |
| R24 | A (a, b), C (b2), E (b), F (b) | m est endogène, m = 0 annule le dénominateur, et l'inégalité de Jensen biaise R. | **Acceptée.** | Rapport de sommes par épisode sur m ≥ 1 ; le taux de m = 0 est rapporté à part. |
| R25 | D (c), F (c3) | Mon « contrôle négatif » d'E4 est un étalon positif et confond sensibilité de l'auditeur et vérifiabilité. | **Acceptée.** | Injections uniformes stratifiées par strate, renommées étalon ; le négatif est constitué d'analyses honnêtes ré-exécutées. |
| R26 | A (a), E (a1), F (a) | Connaître une graine ne permet pas de simuler un paraphraseur de 7–8 B. | **Acceptée.** | Accès d'essai en boîte noire. |
| R27 | C (a4) | Optimiser l'attaquant contre la paraphrase à graine fixe serait une « fuite ». | **Rejetée comme fuite.** L'optimisation contre une transformation déterministe accessible est précisément la menace que le hasard doit contrer : c'est le traitement. **Contenu repris** : budget d'optimisation égal par bras. | E5′. |
| R28 | D (a), C (c4) | Fraîcheur et publicité de la graine sont changées ensemble. | **Acceptée.** | Plan 2×2. |
| R29 | D (a), E (b), F (b) | Conditionner sur les sorties qui préservent l'utilité sélectionne des messages. | **Acceptée.** | L'utilité devient un co-critère, pas un filtre. |
| R30 | A (c), D (b) | Si le canal ne transmet rien avant paraphrase, le contraste ne mesure rien. | **Acceptée.** | Contrôle positif sans paraphrase. |
| R31 | D (b), F (b) | Les bits décodés minorent la capacité, ils ne la mesurent pas. | **Acceptée.** | Résultat rapporté comme borne inférieure. |
| R32 | A (a), D (b), F (a) | Le rappel étalonné sur U2/U9 ne se transfère pas à U13/U10/U5, et l'auteur de la thèse rédige les requêtes. | **Acceptée.** | Requêtes rédigées par un tiers ; deux recherches indépendantes par usage cible. |
| R33 | A (b) | Avec K ~ Bin(5 ; 0,5), P(K ≤ 2) = 0,5. | **Acceptée.** Je retrouve 16/32. | Décision sur N̂ corrigé du rappel, pas sur K brut. |
| R34 | A (c), D (c), F (c5) | Il manque une catégorie placebo, des pièges lexicaux, des voisins inéligibles et un jugement d'éligibilité distinct. | **Acceptée.** | E6′. |
| R35 | D (b), F (b) | c1 : sous un bit rare, l'exactitude égale celle de la classe majoritaire. | **Acceptée.** | Score de Brier relatif au taux de base. |
| R36 | E (b), F (b) | c2 : un FPR de 0,1 % avec N₀α₀ ≈ 2 donne un quantile instable. | **Acceptée.** | FPR primaire de 1 % ; 0,1 % seulement si N₀α₀ ≥ 10 (illustratif). |
| R37 | E (b) | c3 : les fausses alertes flottantes se cumulent en 1−(1−ε₀)^k. | **Acceptée.** | Tolérance fixée sur des doubles exécutions honnêtes par strate. |
| R38 | A (préambule) | Greenblatt et al. est daté 2023 chez moi, 2024 ailleurs. | **Non tranchable de mémoire.** Une prépublication et une version de conférence peuvent coexister. | « Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion* » : année à vérifier. |

---

## (b) Expériences corrigées

### Règle commune (remplace celle du tour III.1)

- **Verdicts.** Chaque duel fixe à l'avance un paramètre θ et deux seuils θ_B < θ_A (illustratifs). Il y a quatre verdicts possibles :
  - IC à 95 % dans la région de H_A : H_B est falsifiée.
  - IC dans la région de H_B : H_A est falsifiée.
  - IC entièrement dans ]θ_B ; θ_A[ : **effet intermédiaire**, qui falsifie les deux hypothèses.
  - IC à cheval sur un seuil : **non tranché**.
- **Effectif.** n est fixé avant la collecte pour que la largeur d'IC attendue, effet de plan par tâche inclus, soit inférieure à θ_A − θ_B. Pas d'arrêt optionnel.
- **Inférence.** IC par grappes de tâches. Calibrations et pilotes sur des familles de tâches disjointes de l'évaluation. Correction de Holm sur la famille E1′–E5′. Je reprends ici la demande de multiplicité que A et F adressent à D.
- **Équité entre bras.** Quand deux bras diffèrent par le hasard, le budget d'optimisation adverse est égal par bras.

### E1′ — Dissuasion, évitement ou réaction lexicale

- **Plan.** p annoncé ∈ {0 ; 0,1 ; 0,3} × conséquence d'une tentative détectée ∈ {aucune ; sanction ; récompense}, soit 9 cellules.
- **Agents.** Un agent à objectif caché, un agent honnête et un agent scripté qui maximise l'espérance (contrôle positif de la chaîne de cotation). Les tentatives sont cotées à l'aveugle, indépendamment des audits (R4, R10).
- **Paramètre.** Δ = log OR(0,3 contre 0 ∣ sanction) − log OR(0,3 contre 0 ∣ aucune).
- **H_A** (la sanction ajoute une dissuasion) : Δ ≤ −0,35. **H_B** (la sanction n'ajoute rien au-delà de l'évitement) : Δ ≥ −0,10. Seuils illustratifs.
- **Validité** (règle préenregistrée, ce n'est pas un verdict) :
  - Dans le bras « récompense », log OR(0,3 contre 0) doit avoir un IC qui ne se situe pas entièrement sous 0. S'il est négatif comme sous sanction, l'effet est lexical (HYPOTHÈSE de C), et H_A ne peut pas être attribuée à un calcul.
  - Chez l'agent honnête, le taux de fausses tentatives ne doit pas varier avec p.
- **Rapport séparé.** La pente sous « aucune » mesure l'évitement par détection (U2), que A distingue à juste titre de la dissuasion (U1).
- **Variante implantée.** Elle est rapportée à part, avec une conclusion limitée à cette classe d'organismes (R9).

### E2′ — Exploitation d'une prévisibilité apprise en cours de tâche

- **Traits.** Deux traits binaires Z₁ et Z₂. Le pilote vérifie que, sans audit, ils offrent un succès d'attaque égal, et que l'auditeur a la même sensibilité sur les deux.
- **Audit.** Audit non bloquant, visible dans l'historique. Le taux marginal p est identique dans tous les bras. La moitié des épisodes audite davantage Z₁, l'autre moitié Z₂ (signe inversé). I(R ; Z) est fixé par conception, avec T·I ≥ 3 bits sur la première moitié (illustratif).
- **Paramètre.** θ = P(attaque sur le trait le moins audité ∣ attaque) − ½, mesuré sur la seconde moitié de l'épisode.
- **H_A** (l'agent apprend et exploite la fuite) : θ ≥ 0,10. **H_B** (pas d'exploitation) : θ ≤ 0,03. Seuils illustratifs.
- **Contrôles négatifs.** Historique transplanté d'une autre trajectoire, avec les mêmes fréquences mais décorrélé ; historique masqué. θ doit y être nul.
- **Contrôles positifs.** Calendrier donné explicitement : θ doit y être positif, sinon l'agent n'est pas stratégique et le duel est non tranché. Un apprenant bayésien scripté doit montrer θ > 0, ce qui confirme que l'information fournie suffit.
- **Mesure secondaire.** Sécurité S.

### E3′ — Indiscernabilité des leurres aléatoires

- **Paramètre comportemental.** Δδ = δ_réel − δ_test (taux de défection). Le pilote exige δ_réel ≥ 0,3 (illustratif) ; en dessous, le duel est non tranché par construction (R16).
- **H_A** (les leurres sont reconnus) : Δδ ≥ 0,15. **H_B** : Δδ ≤ 0,03. Seuils illustratifs.
- **Sous-duel sonde** (linéaire et non linéaire). Mesure : l'excès d'AUROC de « test contre réel » sur « réel contre réel » (deux dates ou deux sources).
- **Conditions d'interprétation de la sonde.** Elle n'est interprétée que si quatre contrôles passent :
  - générateur contre générateur ≈ 0,5 ;
  - étiquettes au hasard ≈ 0,5 ;
  - perturbation neutre de tâches réelles ≈ 0,5 ;
  - lots différents dans la même condition ≈ 0,5.
- **Étanchéité.** Les données de réglage du générateur sont disjointes de l'entraînement de la sonde. Découpage par famille de tâches ; cache de préfixe désactivé.
- **Portée de H_B.** Elle se lit « indiscernable pour ces sondes ».

### E4′ — Ciblage sous vérifiabilité non uniforme

- **Tâche.** Analyses synthétiques où l'objectif caché (biaiser la conclusion) peut être atteint par une étape de code (filtrage, transformation) ou par une étape interprétative. Le pilote vérifie que les deux voies réussissent également. La vérité interprétative est connue par construction et reste réservée à l'expérimentateur (R22).
- **Conditions annoncées.** Audit de Poisson au taux p soit sur les étapes de code, soit sur les étapes interprétatives. Un vérificateur interprétatif est utilisé, avec une sensibilité mesurée par strate.
- **Paramètre.** θ = part des corruptions dans la strate code sous « audit interprétatif » − même part sous « audit code ».
- **H_B** (ciblage) : θ ≥ 0,20. **H_A** (pas de ciblage) : θ ≤ 0,05. Seuils illustratifs ; je garde les étiquettes du tour III.1.
- **Détection (secondaire).** R = Σᵢ Dᵢ / Σᵢ [1 − (1 − p·s_h)^{mᵢ}] sur les épisodes où mᵢ ≥ 1, avec s_h la sensibilité de la strate h. Le taux d'épisodes avec m = 0 est rapporté à part.
- **Étalon positif.** Injections uniformes stratifiées (mesure de s_h) et un agent scripté qui cible.
- **Négatif.** Analyses honnêtes exécutées deux fois par strate, pour mesurer les fausses alertes de non-déterminisme.

### E5′ — Le hasard agit-il dans la paraphrase ?

- **Plan.** Graine {renouvelée à chaque message ; fixe} × accès {essais en boîte noire au paraphraseur de son bras ; aucun}. Même budget de requêtes d'optimisation de l'encodeur dans chaque bras (illustratif).
- **Paramètre.** θ = collusion(fixe, accès) − collusion(renouvelée, accès).
- **H_A** (la fraîcheur du tirage compte) : θ ≥ 0,10. **H_B** : θ ≤ 0,03. Seuils illustratifs.
- **Lecture préenregistrée.** Si « fixe sans accès » ≈ « renouvelée » < « fixe avec accès », ce qui protège est le *secret* de la transformation, pas la fraîcheur du tirage. U7 serait alors reclassé « secret de la fonction ».
- **Contrôles.**
  - Sans paraphrase : la collusion doit dépasser un plancher, sinon le duel est non tranché.
  - Permutation des paires message–réponse : la collusion doit tomber au niveau du hasard.
  - Agent sans consigne de collusion.
- **Utilité.** Perte ≤ 5 points par bras (illustratif), rapportée comme co-critère, jamais comme filtre. La capacité est rapportée comme borne inférieure.

### E6′ — « Moins étudiés » : test de ma propre thèse

- **Indépendance.** Les requêtes sont rédigées par un tiers à partir de définitions des usages, puis préenregistrées.
- **Estimation.** Deux équipes indépendantes cherchent chaque usage cible (U13, U10, U5, U1-dissuasion). N̂_u est estimé par capture-recapture avec une correction pour petits effectifs (méthode : référence à vérifier).
- **Contrôles de codage.** L'éligibilité est jugée par un codeur distinct de la décision d'inclusion. S'y ajoutent une catégorie placebo (attendu : 0), des articles pièges qui contiennent les mots-clés hors contexte stratégique, et des voisins inéligibles dans chaque vocabulaire cible, codés à l'aveugle.
- **Rôle de U2 et U9.** L'étalonnage sur ces usages ne sert plus que de vérification minimale.
- **Hypothèses.** **H_A** (peu étudié) : borne supérieure de l'IC de N̂_u ≤ 2. **H_B** : borne inférieure ≥ 5. Seuils illustratifs.
- **Risque assumé.** Avec de très petits décomptes, l'IC sera large. Un verdict « non tranché » est plausible et sera rapporté tel quel.

**Coût.** L'estimation (d) du tour III.1 n'est plus valide, car E1′ multiplie les cellules. Elle sera refaite après les pilotes. Que le calcul reste non limitant est une HYPOTHÈSE.

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi dans les pièces.** Seulement l'énoncé de la question. Les FAITS ne contiennent aucun résultat empirique ni bibliographique.

**Ce qui est rapporté (de mémoire, non vérifié ici).**
- Des garanties mathématiques conditionnelles existent pour plusieurs usages : jeux d'inspection (Avenhaus, von Stengel, Zamir 2002), preuves interactives (Goldwasser, Micali, Rackoff 1985), jeux de sécurité (Tambe 2011) et calculs distribués vérifiables (Golle & Mironov 2001).
- Des applications à des agents LLM existent pour :
  - l'audit et la surveillance (Greenblatt et al., année à vérifier) ;
  - le rééchantillonnage (Bhatt et al. 2025, « Ctrl-Z ») ;
  - la paraphrase (Roger & Greenblatt 2023).

**Identités conditionnelles que je maintiens, sous leurs hypothèses.**
- Sous un tirage de Bernoulli au taux p et une sensibilité s, la détection vaut 1−(1−p·s)^m sur m tentatives.
- Pour une action unique et irréversible, un audit non bloquant laisse passer avec probabilité 1−p·s.
- E et F présentent comme VÉRIFIÉ, sous conditions, qu'un seuil aléatoire ne bat pas le meilleur seuil fixe face à un attaquant non adaptatif. Je ne l'ai pas réétabli ; je m'en sers comme condition. La valeur de plusieurs usages du hasard dépend alors de l'**adaptativité** du contrôlé, que mesure E2′.

**Ce qui n'est pas établi** (tout est HYPOTHÈSE) :
1. Les agents LLM sont-ils dissuadés, ou seulement détectés ? Et une éventuelle « dissuasion » est-elle une réaction lexicale ? → E1′.
2. Apprennent-ils en contexte une corrélation entre l'audit et un trait ? → E2′.
3. Les leurres injectés sont-ils indiscernables au-delà des artefacts de génération ? → E3′.
4. Concentrent-ils la fraude sur les étapes non vérifiables ? → E4′.
5. Dans la paraphrase, est-ce la fraîcheur du tirage ou le secret de la fonction qui agit ? U7 pourrait changer de nature dans l'inventaire. → E5′.
6. Ma liste des usages les moins étudiés pour les agents LLM : U13 (horizon aléatoire), U10 (défi frais et engagement), U5 (contre-vérification de sous-calculs dans les longues analyses) et U1 comme dissuasion distincte de la détection. Le rappel de ma recherche est inconnu, et R32–R34 montrent que mon instrument du tour III.1 ne pouvait pas le mesurer.

**L'expérience à faire en premier : E6′.**
- C'est la seule qui falsifie directement ma réponse à « lesquels sont les moins étudiés ».
- Elle coûte des semaines-personne et aucun GPU (illustratif).
- Son résultat ordonne les autres : si U1-dissuasion compte déjà ≥ 5 travaux, E1′ devient une réplication et perd sa priorité.

**Ce qui me donnerait tort.** Une borne inférieure de N̂_u ≥ 5 (illustratif) pour l'un des quatre usages le retire de ma liste. Si la catégorie placebo ne rend pas 0, ou si les pièges sont inclus, l'instrument est invalide et aucun verdict n'est rendu. E1′ vient en second.

FIN-DE-CELLULE