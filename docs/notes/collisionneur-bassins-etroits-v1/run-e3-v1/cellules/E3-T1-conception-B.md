# Proposition B — Pousser l'organisme vers les bassins étroits et profonds

---

## (1) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Source / commentaire |
|---|---|---|---|
| S1 | Il existe, dans les mondes plantés considérés, des **bassins étroits et profonds** — c'est-à-dire des composantes à la fois rares sous la loi des propositions spontanées des modèles **et** à fort gain une fois trouvées. | **HYPOTHÈSE**. La composante conditionnelle ([C4] §2.1) est conçue pour être « presque invisible à une loi sans condition » et « trouvable une fois sa condition archivée » ; que le gain soit *grand* n'est pas établi — il dépend de paramètres de monde non transmis. Qu'elle soit *profonde* au sens du gain net par rapport au nul est une conjecture de conception. |
| S2 | Les proposeurs *raffinent effectivement* les bassins larges plutôt que d'explorer les bassins étroits. | **OBSERVÉ-NON-AUDITÉ** pour v67 ([F12] §2 : « variantes proches d'un même constat »). Généralisé ici sans preuve à d'autres mondes. Le chiffre « 47 % ne quittent jamais leur premier bassin » ([B]) vient d'un contexte différent (tâches de ML, agents avec feedback de score, 24 h), **non reproduit** dans l'organisme d'idéation — lequel n'a ni feedback de score ni historique inter-appels. |
| S3 | Un « bassin » est identifiable mécaniquement (sans oracle) avec assez de fidélité pour qu'une méthode mathématique puisse le cibler. | **HYPOTHÈSE**. Le regroupement par doublons ([C3] §3.1–3.4) opère sur la distance en nats entre formes canoniques, mais la question parle d'« idée de fond », notion plus large qu'une forme canonique identique. La correspondance bassin ↔ groupe de doublons n'est pas prouvée. |
| S4 | Il est possible de rediriger la masse de probabilité des propositions vers les bassins étroits **sans affaiblir la garde**. | **HYPOTHÈSE**. Le premier tour a rejeté toute récompense numérique de la nouveauté dans le juge et tout signal servi à l'agent ([S1]). Le levier restant est la **formulation des vues** ou la **composition du pool de proposeurs**, mais l'effet de ces leviers sur la couverture des bassins étroits est inconnu. |
| S5 | Le gain d'un bassin étroit, une fois découvert, compense le surcoût d'exploration pour l'atteindre. | **HYPOTHÈSE**. Le chiffre « neuf fois le gain d'un pas de raffinement » ([B]) est observationnel, non reproduit ici, et porte sur des tâches de ML à score continu — pas sur des tests statistiques à seuil. |
| S6 | Des « méthodes mathématiques sophistiquées » agissant sur l'organisme existent et sont compatibles avec les contraintes (pas de signal de score servi aux proposeurs, pas de juge piloté, pas de feedback). | **HYPOTHÈSE**. C'est l'objet de la question ; la réponse doit le trancher. |

---

## (2) Méthodes proposées

### Méthode M1 — Repulsive Structured Prompting par noyau de Stein (DPP sur l'espace des vues)

**Objet mathématique.** Un *processus ponctuel déterminantal* (DPP) sur un espace fini de vues proposées aux modèles. Soit $\mathcal{V} = \{v_1, \dots, v_K\}$ un ensemble de vues candidates, toutes dérivées mécaniquement de la vue publique par des transformations pré-enregistrées (permutation de l'ordre des lois d'archive, sélection de strates différentes à mettre en avant, variation du cadrage). On définit un noyau $L_{ij} = q_i\,q_j\,\kappa(v_i, v_j)$ où $q_i$ est une qualité a priori uniforme et $\kappa$ mesure la similarité sémantique entre vues (par exemple : recouvrement des sous-ensembles de strates mises en avant). Un DPP de noyau $L$ échantillonne un sous-ensemble $S \subseteq \mathcal{V}$ avec $\Pr(S) \propto \det(L_S)$, ce qui **garantit** la diversité : les sous-ensembles de vues mutuellement distinctes sont exponentiellement favorisés.

**Où elle agit.** En amont des proposeurs : l'orchestrateur tire un sous-ensemble de vues diversifiées *avant* chaque génération et assigne une vue distincte à chaque appel de proposeur. Aucun signal n'est servi *au* proposeur ; seule la *question posée* change.

**Ce qui est une preuve et ce qui est conjecture.** La théorie des DPP (Kulesza & Taskar, 2012 — *référence à vérifier* pour l'édition exacte) prouve que le sous-ensemble tiré maximise la diversité volumique dans l'espace du noyau. **Conjecture** : la diversité des vues entraîne la diversité des bassins couverts par les propositions. C'est non trivial — un modèle peut ignorer la strate mise en avant.

**Pourquoi elle atteindrait un bassin étroit mieux que des tirages indépendants.** Si les vues sont i.i.d. la même vue publique, les proposeurs voient le même prompt et convergent vers le même bassin (v67 : 11 variantes du même constat). Le DPP force des vues orthogonales ; sous l'hypothèse que certaines vues rendent visible une composante conditionnelle (par exemple, une vue restreinte à la strate où le trait conditionnant est positif), la probabilité de couvrir le bassin étroit croît comme $1 - (1-p_s)^{|S|}$ au lieu de $1 - (1-p_0)^{|S|}$ avec $p_s > p_0$ (la strate pertinente rend l'effet visible).

**Compatibilité avec les contraintes.** Aucun score de juge ni verdict n'entre dans $L$ : le noyau ne dépend que de propriétés publiques des vues. N-053 respecté. La garde n'est pas touchée — les propositions passent le même juge. N-058 respecté car la composition est évaluée par l'oracle après la course. **Risque** : si le noyau $\kappa$ est mal calibré, le DPP peut forcer des vues pathologiques (strates marginales, masse nulle) et gaspiller des appels.

---

### Méthode M2 — Anti-concentration par exploration conditionnelle séquentielle (« chaîne de conditions »)

**Objet mathématique.** Soit $\mathcal{A}_g$ l'archive à la génération $g$. On construit, sans oracle, un **graphe de dépendance potentielle** entre traits publics : pour chaque paire de traits $(t_i, t_j)$, on calcule (par programme, pas par modèle) la divergence KL conditionnelle $D_{\text{KL}}(\hat{p}(Y|t_i, t_j) \| \hat{p}(Y|t_i)\hat{p}(Y|t_j))$ sous les lois de l'archive. Les arêtes à divergence $> 0$ indiquent des interactions déjà archivées. Les **arêtes à divergence nulle dans l'archive mais non testées** (aucune carte archivée ne conditionne sur $(t_i, t_j)$ conjointement) forment un ensemble de conditions candidates.

À chaque génération, la **vue enrichie** donnée à un sous-ensemble de proposeurs inclut une invitation explicite : « Explorez si l'issue dépend de $t_j$ *conditionnellement à* $t_i$. » Ceci est pré-enregistré ; les conditions candidate sont énumérées mécaniquement.

**Garantie.** Si la composante plantée est conditionnelle de profondeur 1 sur un trait $t_i$ déjà archivé, et que la paire $(t_i, t_j)$ est dans la liste candidate, la vue la met en avant. La probabilité de couverture est alors bornée inférieurement par la probabilité qu'au moins un proposeur exploite l'invitation — non garantie, mais strictement supérieure à la probabilité spontanée (HYPOTHÈSE testable).

**Compatibilité.** Pas de score servi. Pas de verdict. Calculé par l'orchestrateur. La garde est inchangée. **Risque** : le nombre de paires non testées croît en $O(d^2)$ ; il faut un budget d'appels suffisant ou un filtrage par l'orchestrateur (par exemple : ne garder que les paires dont au moins un trait est impliqué dans une carte archivée).

---

### Méthode M3 — Bayesian Quadrature sur l'espace des lois, avec acquisition anti-concentration

**Objet mathématique.** On modélise l'espace des lois prédictives possibles comme un espace fonctionnel $\mathcal{F}$. On place un processus gaussien (GP) sur la fonction de gain $g : \mathcal{F} \to \mathbb{R}$ (gain = distance au nul, mesurée en nats). Les lois déjà évaluées (archive + cartes rejetées) fournissent des observations. La **fonction d'acquisition** est de type *maximum de variance* (pas UCB, pas EI — on ne maximise pas le gain mais l'*information*) : on propose les lois là où l'incertitude du GP est la plus grande.

**Difficulté fondamentale.** Le GP est sur un espace de fonctions paramétriques (les six formes grammaticales), pas sur $\mathbb{R}^d$. Il faut un noyau sur les formes canoniques. Un candidat : le noyau de Fisher entre lois paramétriques (distance de Hellinger au carré comme proxy). C'est calculable par l'orchestrateur.

**Où elle agit.** L'orchestrateur suggère aux proposeurs, dans la vue, des régions de $\mathcal{F}$ à explorer (« Considérez une loi qui diffère de l'archive surtout dans la strate $X$, par un écart d'au moins $\delta$ »). Le proposeur reste libre.

**Compatibilité.** Le GP n'utilise que des informations publiques (formes canoniques, distance au nul public). Pas de verdict du juge dans l'acquisition. N-053 respecté. **Risque majeur** : le GP est un modèle du gain *sans accès au gain réel* (pas d'oracle, pas de verdict). La surface d'incertitude est donc très mal calibrée — le GP ne voit que les lois soumises, pas leur performance. Cela rend la méthode **faible en pratique** tant que le nombre de générations est petit (< 10). Je la classe troisième pour cette raison.

---

### Méthode M4 — Couverture par codes correcteurs d'erreurs sur l'espace des traits

**Objet mathématique.** Identifions chaque « idée » à un sous-ensemble de traits conditionnant (un sous-ensemble de $\{t_1, \dots, t_d\}$). L'espace des idées est $2^d$. Un *code couvrant* (covering code) de rayon $r$ dans cet espace est un ensemble $C$ tel que toute idée est à distance de Hamming $\leq r$ d'un élément de $C$. On veut que les vues (ou les invitations) couvrent $C$ en un nombre d'appels minimal.

**Borne.** Par la borne de sphère, $|C| \geq 2^d / V(d, r)$. Pour $d = 10$ traits et $r = 2$, $|C| \geq 1024 / 56 \approx 19$. Avec 5 proposeurs × 6 cartes = 30 appels par génération, on peut couvrir l'espace en une génération.

**Compatibilité.** Purement mécanique, pré-enregistrable. Ne touche ni la garde ni le juge. **Risque** : l'espace des « idées » n'est pas $2^d$ — une idée peut être une *fonction* des traits (conditionnelle, transformée), pas un sous-ensemble. Le code couvrant ne couvre donc que les idées additives par trait, pas les composantes conditionnelles de profondeur $\geq 1$.

---

### Méthode M5 — Mutation topologique par homologie persistante du paysage des lois

**Objet mathématique.** Construire le complexe de Vietoris-Rips sur les lois archivées (distance : Hellinger). Calculer l'homologie persistante $H_0, H_1$. Les composantes $H_0$ à grande durée de vie signalent des clusters isolés de lois. Les « trous » ($H_1$) signalent des régions non couvertes entre clusters.

**Où elle agit.** Descriptif pur (D1 dans [C3] §4.1) — elle ne dirige pas la sélection, mais elle peut alimenter la construction de vues : « les lois archivées laissent un trou entre les strates $X$ et $Y$ ; explorez cette région. »

**Compatibilité.** Pas de score servi. **Risque** : avec 11 lois archivées ([F12] §2), le complexe est trop petit pour que l'homologie persistante soit informative (bruit topologique dominant). Utile seulement à partir de ~50 lois. Je la classe dernière.

---

## (3) Ce qui est impossible en principe, et sous quelles hypothèses un gain existe

**Impossibilité 1 (No Free Lunch pour l'exploration).** Sans *aucune* structure sur la distribution des bassins, aucune stratégie d'exploration ne bat le tirage i.i.d. uniforme en espérance. Preuve : si les bassins sont placés par un adversaire après choix de la stratégie, toute stratégie déterministe est battue. **Condition nécessaire pour un gain** : la structure du monde (traits publics, strates, grammaire) est corrélée avec l'emplacement des bassins étroits. C'est le cas par construction pour la composante conditionnelle ([C4] §2.1) — son trait conditionnant est public.

**Impossibilité 2 (garde et exploration).** Si on pousse *via le juge* (prime de nouveauté dans la valeur e), on viole la garantie E[e] ≤ 1 sous H₀. Le premier tour l'a rejeté ([S1]). Les méthodes M1–M5 agissent toutes **en amont** (vue) ou **en aval descriptif** (D1), jamais dans le juge.

**Impossibilité 3 (dilution).** Par la borne de dilution ([S1]), une distance globale entre lois efface une différence confinée à une strate de masse $r$. Toute méthode qui évalue la diversité globalement (par exemple, M3 avec un noyau global) est aveugle aux bassins étroits confinés à des strates rares. **Condition suffisante pour un gain** : la méthode opère par strates (M1 par sélection de strates dans les vues, M2 par paires de traits).

---

## (4) Expérience décisive la moins chère

### Monde planté de contrôle

Un monde à $d = 6$ traits publics binaires, contenant :
- **Composante A** (bassin large) : effet additif du trait $t_1$, visible dans toutes les strates. Probabilité spontanée de découverte par un proposeur : $p_L$ (illustratif : ~0.8).
- **Composante B** (bassin étroit) : effet de $t_3$ conditionnel à $t_2 > 0$, nul en moyenne. Probabilité spontanée : $p_E$ (illustratif : ~0.1).
- Profondeur de B ≥ profondeur de A (en nats par instance).

Le monde est écrit par programme à graine scellée. Les paramètres $(p_L, p_E)$ sont calibrés sur un pilote de 5 courses (coût : illustratif ~50 $ par course, 250 $ au total).

### Duel

| | H_A (traitement actif) | H_B (tirages indépendants) |
|---|---|---|
| **Bras** | M2 (exploration conditionnelle séquentielle) : vues enrichies avec paires candidates | Vues standard identiques pour tous les proposeurs, comme dans v67 |
| **Contrôle négatif** | Vues enrichies avec des paires *non pertinentes* (traits sans interaction plantée) — pour mesurer l'effet de l'invitation per se vs. l'effet du ciblage correct |

**Métrique principale** : $C_E$ = proportion de courses (sur $N \geq 30$ courses par bras) où la composante B est couverte par au moins un représentant retenu après le test de mort, en $\leq 3$ générations.

**Seuil** : $C_E(\text{M2}) - C_E(\text{standard}) > 0.2$, testé par un test exact de Fisher bilatéral, $\alpha = 0.05$, pré-enregistré.

**Issue qui falsifie chaque hypothèse** :
- Si $C_E(\text{M2}) \leq C_E(\text{standard}) + 0.05$ (intervalle de confiance à 95 %) : M2 est falsifiée comme méthode utile.
- Si $C_E(\text{M2}) > C_E(\text{standard}) + 0.2$ **et** le contrôle négatif ne montre pas le même gain : H_B (les tirages indépendants suffisent) est falsifiée.

**Métrique secondaire** : nombre de fausses découvertes (cartes retenues ne correspondant à aucune composante plantée). Si le bras M2 a un taux de fausses découvertes > 1.5× le bras standard, la garde est affaiblie et la méthode est rejetée même si $C_E$ est supérieur.

---

## Calibration des instruments nommés

### Regroupement par doublons ([C3] §3.1–3.4) comme détecteur de bassins

**Mesure minimale de fonctionnement** :
- **Taux de détection (recall)** : sur un monde planté à $k$ composantes connues, proportion de paires de cartes ciblant la même composante qui sont classées dans le même groupe. Cible : > 0.9.
- **Taux de fausses alertes (false merge)** : proportion de paires de cartes ciblant des composantes *différentes* classées dans le même groupe. Cible : < 0.05.
- **Cas honnêtes appariés** : 100 paires de cartes générées par des proposeurs réels (pas synthétiques), annotées par l'oracle, sur le monde planté de contrôle.
- **Vérification mécanique à battre** : un détecteur trivial qui regroupe par identité de forme grammaticale (même forme = même groupe).

### Graphe de dépendance conditionnelle (M2)

- **Taux de détection** : parmi les paires de traits $(t_i, t_j)$ pour lesquelles il existe une composante conditionnelle plantée, proportion identifiée comme « non testée et candidate ».
- **Taux de fausses alertes** : parmi les paires sans interaction plantée, proportion classée candidate.
- Ce calcul est purement mécanique (KL conditionnel sur l'archive) ; la vérification de base est un calcul exact sur les lois archivées, faisable par l'orchestrateur.

---

## (d) Ancrage matériel

| Poste | Détail | Coût (illustratif) |
|---|---|---|
| Pilote de calibration (5 courses × 2 bras) | 10 courses, ~6 appels proposeurs × 5 modèles × 3 générations = 900 appels ; à ~0.10 $/appel (illustratif, modèles ouverts type Llama 3.x 70B ou Mistral Large via API) | ~90 $ |
| Expérience décisive (30 courses × 3 bras) | 90 courses, ~16 200 appels | ~1 620 $ |
| Orchestrateur + juge (CPU) | Calculs de KL, doublons, DPP, tests : ~100 h CPU standard | ~20 $ |
| **Total** | | **~1 730 $** (illustratif) |

**Modèles ouverts utilisables** : Llama 3.1 70B, Mistral Large 2, Qwen 2.5 72B — tous accessibles via API ou auto-hébergés sur 2×A100. Le protocole exige des sessions neuves sans historique ; les API sans état conviennent.

---

## (5) Ce qui me ferait changer d'avis

1. **Si le pilote montre que $p_E > 0.5$ sans intervention** (les proposeurs trouvent spontanément la composante conditionnelle dans > 50 % des courses) : le bassin « étroit » n'est pas étroit dans cet organisme, et la question est mal posée. Aucune méthode n'est nécessaire.

2. **Si le contrôle négatif (invitations sur paires non pertinentes) produit le même gain que M2** : le mécanisme n'est pas le ciblage mathématique mais le simple fait de diversifier le prompt. M1 (DPP sur les vues) serait alors suffisant et M2 inutilement complexe.

3. **Si le taux de fausses découvertes augmente dans le bras M2** : la pression vers l'exploration pousse effectivement vers `si_sinon` et `melange`, c'est-à-dire vers la classe que le nul ne couvre pas ([S1] « danger commun »). La garde doit être renforcée avant toute relance.

4. **Si l'homologie persistante (M5) identifie correctement les trous dès $\leq 20$ lois** (contre mon scepticisme) : je la remonterais en priorité devant M3.

5. **Si un résultat d'impossibilité est prouvé** montrant que, dans la classe de mondes considérés, aucune stratégie de vues ne peut augmenter $C_E$ de plus de $\epsilon(d, k)$ par rapport au tirage i.i.d. : toute l'entreprise est vaine et le budget doit aller ailleurs.

FIN-DE-CELLULE