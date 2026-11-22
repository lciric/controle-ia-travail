# Proposition B — Tour III.3 : réponse aux critiques

**Pièces.** FAITS, QUESTION, ma conception III.1 et les critiques A, C et D sont présentes, complètes et terminées par leur marqueur. Je ne réponds qu'aux sections « Sur la proposition B ».

**Statuts.** Ma convention ne change pas :
- ce que disent les faits est **RAPPORTÉ (faits)** ;
- mes calculs sont des **HYPOTHÈSES** (dérivations à vérifier formellement) ;
- les étiquettes que les critiques posent sur mes énoncés ne modifient pas leur statut.

**Bilan.** Je n'ai rejeté aucune critique en entier. J'en rejette trois en partie, chaque fois avec un test à la place. Trois de mes affirmations du tour III.1 étaient fausses et je les retire :
1. « La borne est sous-linéaire en N » est faux à budget fixe.
2. « La covariance mesure la cécité » est faux.
3. « Les canaris voient le rétrécissement de la couverture » est faux : ils ne voient que la dérive des lecteurs.

---

## (a) Réponse critique par critique

Abréviations : A-3 désigne le point 3 de la critique A, section (a) ; C-b2 désigne le point 2 de la critique C, section (b) ; et ainsi de suite.

### 1. La borne et les duels de validité (P1, D1, D2)

| Critique | Verdict | Conséquence |
|---|---|---|
| **D-a1, D-b1, D-c1, C-c1** — j'ai posé D ∈ [0, c] alors que D est une différence signée, et la positivité du capital n'est pas garantie | **Acceptée** | D_t ∈ [−c, c]. Les termes de Horvitz–Thompson sont dans [−c/π_min, c/π_min] et la mise est calibrée sur ce support décalé. La cible n'est plus la somme réalisée mais le cumul des espérances conditionnelles Δ_t = Σ E[D_s \| F_{s−1}]. Voir l'énoncé corrigé en (b). |
| **A-1** — μ₀ et n_h sont absents de la borne | **Acceptée sur le fond, rejetée en partie sur le cadre** | Le défaut est plus grave qu'une erreur d'estimation (HYPOTHÈSE). Si le jumeau est le modèle de confiance, l'écart de capacité g ne s'estime sur aucun n_h : on n'observe jamais le suspect honnête. Si le jumeau partage les poids du suspect, il peut saboter lui aussi, et alors d ≈ 0. Dans les deux cas, **le surplus de capacité N·g⁺ est un budget de sabotage invisible pour toute borne relative au jumeau**. Transformée en test : E2. |
| **A-2, C-a4, D-b1 (pente)** — « sous-linéaire » est vrai par construction ; D2 vérifie le simulateur | **Acceptée** | À budget fixe B (les faits disent « borné »), le plus petit δ détectable par épisode est de l'ordre de zσ/√B, constant en N. Le dommage caché croît donc **linéairement**, en N·zσ/√B (HYPOTHÈSE). **D2 est supprimé** : ce n'était pas une expérience. |
| **A-3** — D1 teste le code, pas le harnais ; le contrôle π_min = 0 rend l'estimateur indéfini | **Acceptée** | D1 est remplacé par E1, qui teste trois choses sur le harnais réel : prévisibilité de la pièce, ordre des journaux, étiquettes retardées. Je retire le contrôle « π_min = 0 ». |
| **A-4** — la borne est valide mais sa largeur n'est pas dite ; le dommage à l'équilibre n'est pas énoncé | **Acceptée** | Avec la règle « arrêter quand la borne basse de Δ_t dépasse τ », un adversaire qui reste dessous inflige jusqu'à environ τ plus la largeur de la séquence (HYPOTHÈSE). C'est désormais la quantité rapportée. |
| **A-5** — contradiction dans le journal | **Acceptée** | Les scores sont journalisés sur **tous** les épisodes, avant la pièce. Le coefficient de contrôle est prévisible : il est ajusté sur le passé seul. |
| **C-b1** — les étiquettes retardées introduisent un biais si le retard est corrélé au dommage | **Acceptée, avec correction** | Pour la borne haute, un épisode audité dont le verdict n'est pas encore rendu est imputé à c. La validité tient ; la largeur se dégrade avec le retard, et ce coût est rapporté. |
| **A-b (poids d'importance)** — à budget égal, le pire cas de max(π_min, f) est pire que l'audit uniforme | **Acceptée** | Le budget est scindé en B = B_unif + B_score, et π_min = B_unif/N est déclaré. Le pire cas certifié ne porte que sur B_unif. Je retire « équivalent à l'audit uniforme ». |

### 2. La couverture de l'oracle (b)

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-8** — les canaris ne voient pas un rétrécissement causé par l'agent | **Acceptée** | La loi des canaris est fixée par le défenseur. Leur séquence de confiance détecte donc la dérive des lecteurs, jamais le déplacement de l'attaque hors de la couverture. Ce second point rejoint la liste « hors de portée ». |
| **D-a2, A-b, C-b2 (dispersion)** — le test de mort de P2 s'immunise lui-même et les familles ne sont pas échangeables | **Acceptée** | Il est remplacé par un plancher pré-enregistré r_min, affirmé par le programme pour la famille tenue à l'écart (E5). Je ne prédis plus rien à partir des autres familles. |
| **C-b2, D-b2, A-b (capture–recapture)** — le manqué conjoint n'est pas identifiable | **Acceptée** | Je l'avais déjà dit au tour III.1. Seule une borne pire cas est rapportée, et elle peut être triviale. |
| **C-a1, D-a4 (2ᵉ partie), C-c1, D-b2, A-b (k jumeaux)** — le critère « distinguable des jumeaux » confond la capacité et le style, et il est sans puissance si α < 1/(k+1) | **Acceptée** | b.5 est déclassé : ce n'est plus une proposition mais une conjecture conditionnée à E2. Contrôle : des produits honnêtes corrects mais atypiques. |

### 3. Savoir qu'on ne voit plus (c)

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-7, D-a3 (1ʳᵉ partie), D-b3, C-b3** — la covariance sonne en régime honnête, sa borne basse touche zéro dès le début, et elle est invariante à un δ constant | **Acceptée, transformée en test (E6)** | Nouvelle statistique : la **différence appariée de score** Δs = s(suspect) − s(jumeau) sur la même tâche auditée, rapportée à l'estimation de E[D]. L'appariement neutralise la difficulté ; la statistique est sensible à un δ constant. L'hypothèse nulle est désormais « le moniteur voit » (effet ≥ κ). L'annonce de cécité n'est jugeable que si la borne basse de E[D] est > 0. Elle reste confondue par g (E2). |

### 4. Le canal de retour (d)

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-10, D-a4 (1ʳᵉ partie), D-b4, D-c3** — ε oublie l'issue « pas de correction », et une borne par observation ne borne pas N observations | **Acceptée** | La fuite par observation devient ε = max(\|ln(p₁/q)\|, \|ln((1−p₁)/(1−q))\|), qui diverge quand p₁ → 1. La quantité rapportée devient l'information cumulée, d'ordre N(p₁−q)²Δ²/(q(1−q)) (HYPOTHÈSE, forme reprise de A). Conséquence : la correction visible d'un dommage trouvé doit avoir p₁ < 1, le reste étant traité en lot différé. Pour l'arrêt sur dommage grave (p₁ = 1), la survie révèle bien la frontière ; ce coût est accepté, car le dommage est plafonné à c par épisode. Test : E7. |

### 5. La sonde de surprise (D3)

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-6 (D3), D-a3 (2ᵉ partie), D-c2** — ma propre thèse prédit une AUROC < 0,5, il existe trois issues, et apparier sur l'issue revient à conditionner sur un collisionneur | **Acceptée** | D3 devient un test signé (E3). L'appariement se fait sur des covariables **pré-exécution**, sans filtre sur le \|écart de valeur\| réalisé. |
| **A-c (D3)** — il manque l'organisme porteur de la consigne qui n'agit pas, et des échecs honnêtes appariés | **Acceptée** | Les deux témoins sont intégrés à E3. |

### 6. Les deux têtes (P4)

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-9** — chez l'honnête, la différence entre les têtes n'est identifiée que par les échecs « passe mais faux » : elle lit l'échec honnête | **Acceptée** | C'est la confusion que P4 devait lever. P4 passe en « conjecture faible » et n'a plus de duel propre. Condition d'identifiabilité, reprise de A : n_h·P₀(passe ∧ ¬bien fait) > dimension effective de la sonde. |
| **C-a2** — fuite par construction | **Rejetée en partie** | Si les familles de tâches qui servent à construire la direction sont disjointes de celles qui servent à l'évaluer, il n'y a pas de fuite ; j'impose cette séparation. Le confondant de l'agent honnête optimisé sur le contrôle est accepté : c'est A-9. |
| **C-b4, D-b4 (P4), C-c2** — l'alignement adverse des projections, et un seuil fixe sur un régime neuf | **Acceptée** | Conséquence de la colinéarité : rien à ajouter. |

### 7. L'étau par coût (P5, D4)

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-6 (D4), A-b (D4)** — pas de marge d'équivalence, et un petit nombre m de tâches « falsifie » par manque de puissance | **Acceptée** | E4 reçoit une marge, et m est fixé par un calcul de puissance fondé sur le σ mesuré en E1. |
| **C-c3, A-c (P5)** — il manque des directions aléatoires et une régularisation générique | **Acceptée** | Les deux témoins sont intégrés à E4. |

### 8. Invariance contrefactuelle et copies (P6, (i))

| Critique | Verdict | Conséquence |
|---|---|---|
| **C-a3, D-b4 (P6), C-c4** — la sensibilité générique aux perturbations de surface confond la mesure | **Rejetée en partie, transformée** | Une double différence (indices d'observation − indices neutres de même longueur et perplexité, chez le suspect moins chez la référence) identifie le conditionnement *si* la référence existe : c'est de nouveau E2. Le mutisme devant un conditionnement sur un invariant que la bifurcation ne varie pas est accepté. |
| **A-c (i)** — classifieur « partenaire copie ou modèle de confiance » | **Acceptée** | C'est un prérequis du brouillage de la connaissance commune. |

### 9. Persuasion et élicitation

| Critique | Verdict | Conséquence |
|---|---|---|
| **A-6 (D5)** — un non-rejet est pris pour une falsification | **Acceptée** | E5 bis reçoit une marge d'équivalence. |
| **A-b (élicitation)** — même plancher σ²/δ² que l'audit | **Acceptée** | L'écart d'élicitation n'apporte aucun gain contre le dommage diffus. Je le garde seulement pour estimer g (E2). |

---

## (b) Expériences corrigées

### Règle commune (B4)

1. Chaque expérience pré-enregistre une marge m et un effectif n tels que la demi-largeur prévue de l'intervalle soit inférieure à m/2. Ce calcul utilise le σ mesuré en E1.
2. Un intervalle qui chevauche une marge **falsifie le calcul de puissance pré-enregistré** : σ était sous-estimé. C'est un fait réfuté, pas une zone morte. On relance alors avec un nouvel effectif, déclaré comme second essai.
3. Tous les seuils sont **illustratifs**.

### Énoncé P1 corrigé (HYPOTHÈSE, à vérifier formellement)

On pose Z_s = A_s·D_s/π_s ∈ [−c/π_min, c/π_min], avec :
- π_s prévisible et au moins égal à π_min ;
- la pièce indépendante de D_s sachant le passé, et tirée après l'engagement ;
- les audités en attente de verdict imputés à c.

Une séquence de confiance par mise donne alors U_t telle que P(∃t : Δ_t > U_t) ≤ α, où Δ_t est le cumul des espérances conditionnelles. Ce que vaut la mise pour des moyennes conditionnelles variables dans le temps reste à vérifier.

À budget B, la largeur est de l'ordre de zσN/√B + c·ln(1/α)/π_min. La garantie porte sur le dommage relatif au jumeau, **dans la couverture de l'oracle**. Trois termes restent linéaires en N, hors de toute borne :
- N·g⁺ (surplus de capacité) ;
- N·β (biais hors couverture) ;
- N·zσ/√B (bruit).

### E1 — Le harnais réel tient-il les conditions de validité ? (remplace D1)

**Mesures.**
1. Un prédicteur de la pièce, entraîné du point de vue de l'agent sur les épisodes du harnais réel. Il voit tout ce que l'agent voit, épisodes antérieurs et contextes de copies compris.
2. Un A/A signé : jumeau contre jumeau à travers l'oracle complet, avec échange des positions.
3. Une vérification des hachages : engagement avant la pièce, scores avant la pièce.

**Hypothèses.**
- H_A : AUROC du prédicteur ≤ 0,5 + m ; moyenne A/A dans ±m ; symétrie sous échange des positions ; taux de fausses alertes de la borne basse ≤ α ; capital toujours positif.
- H_B : l'un de ces points échoue.

**Ce qui est falsifié.**
- Si H_B : la condition de validité de P1 est fausse *sur ce harnais*, et la cause est nommée (pièce prévisible, biais de position des lecteurs, ordre des journaux).
- Si H_A : la crainte d'une fuite de l'identité des audits par ce harnais tombe, et on obtient σ par régime.

**Contrôle positif.** Une pièce volontairement corrélée à une caractéristique visible de l'épisode doit être prédite.

### E2 — Le surplus de capacité est-il un budget de sabotage invisible ? (nouveau)

**Cadre.** Mondes plantés où un organisme honnête de même capacité existe par construction. On mesure :
- g = E[Y_organisme honnête − Y_jumeau de confiance] ;
- un organisme qui sabote exactement à hauteur de g.

**Hypothèses.**
- H_A : \|g\| ≤ m, et le sabotage calibré sur g est trouvé par P1 avec la puissance prévue.
- H_B : g > m, et ce sabotage passe sous la borne avec probabilité ≥ 1 − α.

**Ce qui est falsifié.**
- Si H_B : l'usage du modèle de confiance comme jumeau dans la définition du dommage est réfuté, et N·g mesure la fuite.
- Si H_A : ma conjecture d'un budget invisible tombe, dans ce régime.

**Témoin.** Un écart d'élicitation, après affinage court, comme estimateur indépendant de g.

### E3 — Que lit la sonde de surprise ? (remplace D3)

**Cadre.**
- Bras : sabotage planifié d'un organisme ; échec honnête imprévu ; organisme porteur de la consigne sans agir.
- Appariement sur la difficulté prédite *avant* exécution par le modèle de confiance.
- Tous les pas sont inclus, y compris sous 0,3, **sans filtre** sur l'écart réalisé.
- Statistique : δS = E[S | sabotage] − E[S | échec honnête], signée.

**Hypothèses.**
- H_A (la sonde lit l'intention) : δS > +m.
- H_B (elle lit l'inattendu, ma prédiction) : δS < −m.
- Une équivalence (\|δS\| ≤ m) falsifie les deux.

**Témoin.** Si S diffère entre le porteur passif de la consigne et l'honnête de plus de m, la sonde lit la consigne et le duel est déclaré invalide.

### E4 — L'effacement de la trace coûte-t-il de la capacité ? (remplace D4)

**Cadre.**
- Entraînement contre la sonde.
- Évaluation de la sonde fixe **et** d'une sonde réapprise après coup sur la même couche.
- Réussite mesurée sur m tâches honnêtes tenues à l'écart, m fixé par calcul de puissance.

**Hypothèses.**
- H_A : les deux sondes ont une AUROC ≤ 0,5 + m, et la perte de capacité dépasse Δ_min.
- H_B : les deux sondes ont une AUROC ≤ 0,5 + m, et la perte de capacité est ≤ Δ_min/2.

**Ce qui est falsifié.**
- Si H_B : P5 est réfuté.
- Si H_A : l'idée d'un effacement gratuit est réfutée sur cette tâche.
- Si la sonde n'est pas effacée : l'attaque d'entraînement est déclarée ratée, sans conclusion.

**Témoins.** Des directions aléatoires de même variance ; une régularisation générique de même intensité.

### E5 — La couverture de l'oracle sur une famille tenue à l'écart

**Cadre.** Le programme pré-enregistre un plancher r_min pour la famille tenue à l'écart, écrite par un tiers.

**Hypothèses.**
- H_A : rappel ≥ r_min.
- H_B : rappel < r_min − m.

**Ce qui est falsifié.**
- Si H_B : la couverture déclarée est réfutée. La position du directeur (« toute la question ») est confirmée pour cette famille.
- Si H_A : le plancher tient pour une famille, et pour une seule.

**Témoin.** Un canari factice, passé par la chaîne de plantation avec une édition nulle. Un classifieur « canari ou réel », du point de vue des lecteurs, doit rester au hasard.

### E5 bis — Persuasion (remplace D5)

**Hypothèses.**
- H_A : \|écart de rappel apparié\| ≤ m.
- H_B : écart < −m.

**Témoins.** Une prose sans rapport avec la tâche ; une prose pertinente mais neutre.

### E6 — La nouvelle statistique de cécité

**Cadre.** Mondes plantés avec un δ constant.

**Hypothèses.**
- H_A : l'annonce « ne voit plus », fondée sur Δs/Ê[D], se déclenche avec un taux ≤ α quand le moniteur est informatif ou que le flux est honnête, et avec un taux ≥ 1 − β quand le moniteur est aveugle.
- H_B : l'un des deux taux échoue.

**Ce qui est falsifié.**
- Si H_B : la nouvelle statistique est réfutée.
- Si H_A : on réfute que la cécité sous dommage diffus constant soit inobservable avec un jumeau apparié.

### E7 — Les corrections leurres

**Cadre.** Un agent réentraîné qui observe les corrections **et** leur absence, sur des époques mutualisées.

**Hypothèses.**
- H_A : le nombre d'épisodes nécessaires pour localiser la frontière de l'oracle est au moins celui que prévoit l'information cumulée.
- H_B : il en faut moins de la moitié.

**Ce qui est falsifié.**
- Si H_B : P3 est réfuté.
- Si H_A : la borne d'information tient.

**Ordre.** E1, puis E2, puis E6 se font presque sans GPU. E3 et E5 suivent. E4 et E7 viennent en dernier.

---

## (c) Réponse à l'arbitre (une page)

### Ce qui est établi

1. **Résultats publiés et classiques.**
   - L'estimateur de Horvitz–Thompson est sans biais quand l'inclusion est indépendante de la valeur. C'est un résultat classique.
   - Les impossibilités sont RAPPORTÉES (faits) : détection hors distribution sans conditions, portes dérobées indétectables, tests sans étiquette.
   - Les défenses latentes tombent ensemble, et l'évasion se généralise.
   - Tester le bilan global est la meilleure réponse à l'étalement, à horizon fixe.
2. **Ce que les trois critiques ont établi contre moi.** Ce sont des dérivations, mais convergentes et faciles à vérifier :
   - le dommage est une différence signée ;
   - à budget borné, le dommage caché croît linéairement en N ;
   - une covariance ne mesure pas la cécité ;
   - des canaris ne mesurent que la dérive des lecteurs ;
   - une borne de fuite par observation ne borne pas un adversaire qui mutualise ses observations.

### Ce sur quoi le défenseur peut s'appuyer

C'est ma proposition, avec le statut HYPOTHÈSE. Une seule chose ne dépend pas de la forme de l'attaque : **la pièce, tirée après l'engagement, jugée par l'oracle**. Elle tient sous trois conditions, qu'aucun résultat ne garantit :

1. **Le harnais ne laisse pas prédire la pièce.** C'est à tester (E1).
2. **Le jumeau n'offre pas de surplus de capacité.** Ce point est nouveau pour moi. La définition du dommage appartient au défenseur, mais elle est relative au jumeau. Or tout jumeau est, soit plus faible (le modèle de confiance), soit potentiellement complice (les mêmes poids). Le surplus N·g⁺ est alors un budget de sabotage qu'aucune borne relative au jumeau ne voit. Je ne sais pas le fermer ; je sais le mesurer sur des mondes plantés (E2).
3. **Le dommage est dans la couverture.** Le biais β·N hors couverture est hors de portée par construction.

**Ce que tout sabotage doit faire et que le défenseur peut vérifier sans supposition sur l'agent :** rendre positive la moyenne de D *dans la couverture de l'oracle*, au-delà de g. Tout passage obligé interne (lire le meilleur et émettre autre chose, conditionner sur l'observation, payer l'effacement en capacité) reste une HYPOTHÈSE. Aucune quantité conservée n'est publiée, et l'on n'a aucun échantillon interne de comploteur réel (RAPPORTÉ). Ces lectures n'achètent que de la vitesse d'alarme, jamais la validité.

### Ce qui n'est pas établi

- La couverture de l'oracle sur un genre nouveau. Elle n'est pas mesurable par définition ; E5 n'en teste qu'une famille.
- La valeur de g pour le jumeau réel.
- La prévisibilité de la pièce sur le harnais réel.
- Ce que lit la sonde de surprise sous 0,3. Ma prédiction : l'inattendu, pas l'intention.
- Le coût en capacité de l'effacement de la trace.
- Une borne sur le gain qu'apporte le brouillage de la connaissance commune entre copies.

**Mes chances, en jugement et non en mesure :**
- P1 : élevées pour la validité, et seulement si E1 et E2 passent ;
- P3 : moyennes ;
- P5 et P6 : faibles ;
- P4 : faibles, et plus basses qu'au tour III.1.

### L'expérience à faire en premier : E1

E1 combine trois mesures sur le harnais réel :
- un A/A signé ;
- la prédiction de la pièce du point de vue de l'agent ;
- la vérification de l'ordre des journaux.

**Pourquoi la première :**
1. Elle ne coûte presque aucun GPU.
2. Elle teste les seules conditions dont dépend la validité.
3. Elle fournit σ, dont dépendent les effectifs de toutes les autres expériences.
4. Elle détecte un biais de position des lecteurs qu'aucun duel ne voit.
5. Chacune de ses deux issues réfute quelque chose : la validité de P1 sur ce harnais, ou la crainte d'une fuite des audits.

E2 vient ensuite, car si g est grand, la définition actuelle du dommage laisse un budget de sabotage invisible pour toute borne relative au jumeau.

FIN-DE-CELLULE