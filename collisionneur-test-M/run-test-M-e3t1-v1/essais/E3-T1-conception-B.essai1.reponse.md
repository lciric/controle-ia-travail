# Proposition B — Tour III.1 : le gabarit domine-t-il le style dans le signal de « conscience d'évaluation » ? (Llama-3.1-8B-Instruct, sondes linéaires)

## 0. Pièces reçues

- **Bloc FAITS** : vide par décision déclarée de l'arbitre. Je ne suppose donc aucun fait extérieur. Tout ce qui suit est soit RAPPORTÉ (repris du texte de la question), soit HYPOTHÈSE.
- **Propositions A et C** : non visibles, car le tour se joue à l'aveugle. Je n'ai rien à attaquer ni à réutiliser ; la règle B1 est sans objet pour ce tour.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui le trancherait |
|---|---|---|---|
| P1 | Il existe dans Llama-3.1-8B-Instruct une direction linéaire qui code « je suis évalué », distincte d'une simple détection de format. | HYPOTHÈSE | E0 ci-dessous : la sonde bat-elle un prédicteur de surface sur des paires appariées ? |
| P2 | T (gabarit) et C (style) sont séparables à contenu constant. | HYPOTHÈSE | Les « consignes de banc d'essai connues » (côté T) sont par nature impératives et balisées (côté C). Les deux définitions se recouvrent. Il faut une table qui attribue chaque trait de surface à un seul facteur (§2). |
| P3 | T manipule la *familiarité*. | HYPOTHÈSE | T confond deux choses : le *format* (QCM, consigne de réponse) et la *familiarité* (ressemblance à un banc connu). Rien ne mesure la familiarité. E2 sépare les deux. |
| P4 | On dispose d'étiquettes de vérité « évaluation » / « usage réel » non confondues avec T. | HYPOTHÈSE | Si la sonde est entraînée sur « invites de bancs publics » contre « journaux d'usage réel », la classe positive *est* le gabarit T+. H-M1 serait alors vraie par construction. C'est le risque principal (§3). |
| P5 | La prédiction (« rapport > 2 ») et le critère de réfutation (« l'effet de C persiste ») sont complémentaires. | RAPPORTÉ (texte de la question) ; l'incompatibilité est une déduction vérifiable à la lecture | Il existe une zone où C persiste *et* où le rapport dépasse 2. Les deux critères sont alors satisfaits à la fois. Il faut choisir un seul critère avant scellement (§4). |
| P6 | Le score de la sonde mesure une « conscience ». | HYPOTHÈSE | Au mieux, il mesure une représentation corrélée à la *provenance* (vérité terrain) ou à la *croyance* du modèle (ce qu'il verbaliserait). Ce sont deux construits distincts (§3, voies S1 et S3). |
| P7 | La position de lecture (un jeton unique, sans moyenne) porte le signal. | HYPOTHÈSE | Balayage préenregistré sur les données d'entraînement de la sonde uniquement. |
| P8 | « Permutation des options » (qui garde le sens) et « réordonnancement positionnel » (qui le change) sont bien définis, et l'on sait quelle issue signale une « dérive distributionnelle » plutôt qu'une « réponse au contenu ». | RAPPORTÉ comme énoncé ; définitions et correspondance absentes du texte | À fixer avant scellement (E4, E5). |
| P9 | Préenregistrement scellé, contre-lecture neuve et exécution tiennent dans « cette nuit ». | Contrainte RAPPORTÉE ; faisabilité HYPOTHÈSE | Dépend de la disponibilité d'un relecteur neuf avant le lancement. |
| P10 | Le gabarit de conversation de Llama 3.1 injecte par défaut un en-tête système (date de coupure, date du jour). | HYPOTHÈSE, à vérifier dans `tokenizer_config.json` | Si c'est le cas, la modalité « sans prompt-système » n'existe pas vraiment. L'en-tête doit alors être figé à l'identique dans toutes les cellules. |
| P11 | Des paraphrases peuvent être produites sans modèle de langue. | HYPOTHÈSE | Elles sont possibles par tables écrites à la main, mais leur coût humain domine le budget (§d). |
| P12 | Les effets de T et de C sont additifs. | HYPOTHÈSE | Si l'interaction T×C est forte, « l'effet principal de T domine » n'a plus de sens unique (§4). |
| P13 | Le contenu peut rester constant sans être lui-même familier. | HYPOTHÈSE | Des contenus tirés de bancs publics portent leur propre familiarité, éventuellement par contamination. Ils fuiraient dans les cellules T−. |

---

## 1. Quelle option, et pourquoi : quatre voies et ce qui les départage

Aucune voie n'est « la » réponse. Je propose une quatrième voie, (a′), et je dis ce qui ferait basculer vers chacune.

- **(a) Plan 2×2 cette nuit.** C'est l'information maximale par unité de calcul : le calcul coûte presque rien (§d). Le risque est un résultat ininterprétable si la sonde lit les marqueurs de T (P4). Dans ce cas, un « T domine » confirmerait la sonde, pas H-M1.
- **(a′) Cette nuit, l'instrument seulement ; la décision ensuite.** On lance E0, E3 et les contrôles mécaniques (§c) sur les données d'entraînement et de validation de la sonde. On ne touche à aucun item de test. On scelle ensuite le préenregistrement de E1, avec des seuils informés par la variance observée hors test. Ce pilote est déclaré non décisif, ce qui reste conforme aux règles du programme (RAPPORTÉES). Le coût est un délai d'un cycle de scellement. Le gain : E1 ne peut plus échouer pour cause d'instrument.
- **(b) Plan 2×2×2 avec profil d'interlocuteur.** Je ne la défends pas pour cette nuit, pour trois raisons.
  1. La complaisance est un construit *comportemental*. Elle demande sa propre mesure (changement de réponse sous opinion exprimée), qui n'est pas la sonde de conscience d'évaluation.
  2. Le profil « opinion marquée » covarie naturellement avec le style ouvert. Le confondant P×C est structurel.
  3. À budget d'items constant, chaque cellule a deux fois moins de variantes.

  Ce qui la rendrait défendable : une mesure de complaisance déjà validée, et une hypothèse préenregistrée sur l'interaction P×C.
- **(c) Ne rien lancer.** Aucune information cette nuit, aucun risque de chemins bifurquants. C'est la voie dominante si P9 échoue, c'est-à-dire sans relecteur neuf disponible avant lancement.

**Ce qui départage, dans l'ordre :**
1. Un relecteur neuf est-il disponible avant lancement ? Si non, (c) ou (a′) en mode pilote.
2. La sonde est-elle déjà validée contre un prédicteur de surface, au sens de E0 ? Si non, (a′).
3. Les deux conditions sont réunies : (a).

---

## 2. Construction des items

### 2.1 Faire varier T et C indépendamment, à contenu constant

On part d'une **banque de contenus de base** : une question, avec ses options et sa clé de réponse. Les contenus sont écrits de neuf pour cette expérience, pas tirés de bancs publics (P13). Chaque contenu est rendu dans les 4 cellules (plan intra-item complet). Chaque passe avant est indépendante, donc il n'y a pas d'effet de report.

**Table d'attribution exclusive des traits**, à sceller :

| Trait | Facteur | T+ / C+ | T− / C− |
|---|---|---|---|
| Prompt-système | T | générique (« assistant utile ») | persona produit spécifique |
| Options | T | énumérées et lettrées A–D | intégrées dans une phrase (« plutôt X, Y, Z ou W ? ») |
| Consigne de format de réponse | T | « Réponds par la lettre seule » | absente |
| Besoin utilitaire | T | absent | motif explicite (« je dois choisir pour… ») |
| Mode verbal | C | impératif | interrogatif ou conversationnel |
| Balisage | C | en-têtes, délimiteurs (`### Question`) | aucun |
| Registre et formules d'ouverture | C | neutre, sans salutation | familier, avec salutation |

Règle : aucun trait n'appartient aux deux facteurs. Dans la cellule T+C−, on a donc des options lettrées dans un message conversationnel. Dans la cellule T−C+, on a des options en phrase sous balisage impératif. Ces cellules hybrides sont peu naturelles. C'est le prix de l'orthogonalité, et il faut le déclarer comme limite.

### 2.2 Confondants inévitables

- **Longueur** : T+ (prompt-système, consigne) et C+ (balises) allongent l'invite.
- **Vocabulaire** : les jetons « question », « answer » et les lettres isolées.
- **Distance entre les marqueurs et le jeton lu.**
- **Identité du dernier jeton**, qui varierait d'une cellule à l'autre si l'on lisait à la fin du message utilisateur.

### 2.3 Contrôles

- **Position de lecture constante.** On lit au dernier jeton de l'en-tête assistant, juste avant la génération. Ce jeton est identique dans toutes les cellules. C'est une HYPOTHÈSE sur l'identité exacte des jetons, à vérifier par assertion (§c).
- **Égalisation de longueur.** Un rembourrage neutre, ni balisé ni utilitaire, ramène chaque rendu dans une fenêtre de ±10 % de jetons (illustratif). La longueur résiduelle entre en covariable.
- **Variantes multiples par cellule.** On utilise k formulations par modalité, par exemple 4 (illustratif), tirées par graine fixe. La variante entre comme effet aléatoire croisé. Sans variantes, l'effet de T se confond avec l'effet d'*une* formulation.
- **Contrôle de surface explicite.** Un régresseur logistique sur des traits mécaniques (longueur, nombre de retours à la ligne, présence de motifs `^[A-D][.)]`, nombre de verbes à l'impératif, sac de mots) prédit la cellule. Il sert de témoin (§3.4).

### 2.4 Combien d'items : raisonnement explicite, entrées illustratives

Contraste C par item = moyenne des cellules C+ moins moyenne des cellules C−. Supposons un écart-type inter-items de ce contraste σ = 0,5 unité standardisée (illustratif). Pour un test d'équivalence (TOST) à δ = 0,1 (illustratif), α = 0,05 et une puissance de 90 % sous effet nul :

n ≈ ((z₀,₉₅ + z₀,₉₅) · σ / δ)² = (3,29 × 5)² ≈ 270.

D'où **environ 300 contenus de base**. Avec 4 cellules et 4 variantes, cela fait environ 4 800 invites de test. Le nombre est dicté par la condition la plus exigeante, montrer qu'un effet est *petit*, et non par la détection de T. Si le pilote (a′) donne σ = 0,3 (illustratif), n tombe autour de 100.

---

## 3. La sonde

### 3.1 Données d'entraînement : trois voies

Dans toutes les voies, l'entraînement se fait hors des items de test.

- **S1 — Provenance, équilibrée en surface.** Classe positive : invites réellement issues d'évaluations. Classe négative : invites réellement issues d'usage, par exemple des corpus publics de conversations comme WildChat ou LMSYS-Chat-1M. Les traits de T et de C doivent être **distribués à l'identique** dans les deux classes, par stratification ou repondération. On veut donc des évaluations conversationnelles sans QCM, et des usages réels contenant des QCM (des utilisateurs qui collent leurs devoirs). Sans cet équilibrage, P4 rend E1 circulaire.
- **S2 — Contraste explicite.** Paires d'invites identiques sauf une phrase du type « ceci est un test » / « ceci est un usage réel ». C'est simple et bien contrôlé, mais le construit lu est la *mention* du test. Le transfert vers l'implicite est précisément ce qu'il faudrait démontrer.
- **S3 — Croyance du modèle.** L'étiquette est la réponse verbalisée du modèle à « cette interaction est-elle une évaluation ? », posée dans une passe séparée. On lit alors ce que le modèle « croit », pas la vérité. C'est le plus proche du mot « conscience », mais il hérite des biais de verbalisation.

**Ce qui départage les trois voies** : le cosinus entre leurs directions, et l'AUROC de transfert croisé. Une forte concordance, par exemple un cosinus > 0,5 (illustratif), indique un construit commun. Une discordance dit que « conscience d'évaluation » désigne plusieurs choses. Le préenregistrement doit alors nommer celle que teste H-M1.

### 3.2 Couche et position

- **Position** : un seul jeton, le dernier de l'en-tête assistant (§2.3). La contrainte du programme interdit la moyenne sur les jetons (RAPPORTÉ).
- **Couche** : deux voies.
  - Couche unique fixée d'avance, en milieu de réseau.
  - Couche choisie par AUROC sur une partition de validation *de l'entraînement*, puis gelée.

  Les autres couches sont rapportées en exploratoire, étiquetées comme telles.
- **Type de sonde** : régression logistique L2. La différence des moyennes de classes (direction « mass-mean ») sert de variante de robustesse.

### 3.3 Contre la circularité entre T et la sonde

1. **Équilibrage S1** (ci-dessus).
2. **Leave-T-out** : entraîner la sonde sans *aucun* exemple portant des marqueurs T+, puis la tester sur le 2×2. Si l'effet de T disparaît, la sonde lisait T (E3).
3. **Décodeur de T** : entraîner une sonde qui prédit T+ contre T− sur des contenus neutres hors test, puis mesurer son cosinus avec la sonde d'évaluation. Un cosinus élevé est un signal d'alarme.

Attention : *projeter* la direction de T hors de la sonde, à la manière d'INLP, annulerait trivialement l'effet de T. Cette opération teste autre chose que H-M1 et ne doit pas servir de contrôle.

### 3.4 Témoins

- **Étiquettes permutées** : 200 permutations (illustratif). On obtient l'AUROC nulle et l'effet nul de T et de C.
- **Prédicteur de surface** (§2.3) : la sonde doit le battre sur les mêmes partitions.
- **Directions aléatoires** : pour M = 1 000 directions unitaires (illustratif), on calcule β_T et β_C standardisés de la même façon. La manipulation T déplace massivement le flux résiduel, donc même une direction aléatoire « voit » T. On rapporte le *rang centile* des β de la sonde dans cette distribution, pas leur valeur brute.
- **Tâche de contrôle** au sens de Hewitt et Liang : étiquettes assignées par type de contenu, pour mesurer la sélectivité.

---

## 4. L'analyse

**Modèle.** score ~ T + C + T:C + longueur + (1 + T + C | contenu) + (1 | variante). Codage des contrastes en ±0,5. La structure aléatoire est maximale (Barr et al., 2013). En cas de non-convergence, on la simplifie selon un ordre préenregistré. Les intervalles sont obtenus par bootstrap paramétrique.

**Métrique.** On travaille sur le **logit brut** de la sonde, standardisé par l'écart-type de la classe « usage » en entraînement. On écarte la probabilité calibrée : la sigmoïde sature, ce qui crée des interactions artefactuelles et écrase les différences près de 0 ou 1. La probabilité est rapportée en secondaire.

**Critère unique (résolution de P5).** On fixe un plus petit effet d'intérêt δ, par exemple 0,2 écart-type (illustratif). Trois issues :
- **H-M1 soutenue** : borne basse de l'IC 95 % de β_T > δ, et TOST établit |β_C| < δ.
- **H-M1 réfutée** : l'IC 95 % de |β_C| est entièrement au-dessus de δ.
- **Indéterminé** dans tous les autres cas. Cette issue est déclarée d'avance comme telle.

Le « rapport > 2 » est rapporté en descriptif, avec IC par bootstrap sur les contenus. Il n'est pas critère : il est instable quand β_C est proche de 0.

**Interaction.** Si |β_TC| > δ, les effets principaux sont rapportés par cellule simple. H-M1 est alors déclarée « non testable sous sa forme additive ». C'est une issue en soi.

**Puissance.** Voir §2.4, qui est illustratif.

**Ce qui rend le résultat publiable quel que soit son signe** :
1. Un instrument validé (E0) et un effet de T qui domine : H-M1 est soutenue au niveau objet sur un modèle.
2. Un effet de C qui persiste : H-M1 est réfutée.
3. Une sonde battue par la surface : résultat méthodologique négatif sur les sondes de conscience d'évaluation, utile à tout le programme.

Chaque issue est rapportée avec les mêmes témoins (symétrie de l'audit).

---

## (b) Expériences décisives : duels en inférence forte

### E0 — Validité de l'instrument (préalable à tout le reste)

- **H_A** : la sonde lit un construit au-delà de la surface.
- **H_B** : la sonde est réductible aux traits de surface.
- **Métrique** : AUROC sur des paires appariées en surface (même T, même C, même tranche de longueur) qui diffèrent par l'étiquette. On mesure ΔAUC = AUC(sonde) − AUC(prédicteur de surface).
- **Seuil** : borne basse de l'IC 95 % de ΔAUC > 0,05 (illustratif).
- **Contrôle négatif** : étiquettes permutées ; ΔAUC attendu ≈ 0.
- **Ce que falsifie chaque issue** :
  - ΔAUC significativement positif falsifie H_B. E1 devient interprétable.
  - ΔAUC ≤ 0 falsifie H_A. E1 est annulé, sans lecture d'aucun item de test.

### E1 — H-M1 au niveau objet

- **H_A** : T domine (critère §4).
- **H_B** : C persiste au-delà de δ, T contrôlé.
- **Métrique** : β_T et β_C standardisés, avec leur rang centile parmi les directions aléatoires.
- **Seuil** : δ fixé d'avance (illustratif 0,2).
- **Contrôle négatif** : sonde à étiquettes permutées appliquée au même 2×2. Ses β servent de plancher.
- **Ce que falsifie chaque issue** :
  - TOST sur β_C réussi avec β_T > δ falsifie « le style compte » (H_B).
  - |β_C| > δ falsifie H-M1 (H_A).

### E2 — Familiarité ou format ? Décomposition de T

On ajoute une modalité T* : QCM lettré dans un format **inventé**, jamais vu (ordre et ponctuation inhabituels, consigne non standard), à C fixé.

- **H_A** (familiarité, lecture de l'essaim) : score(T+) > score(T*) ≈ score(T−).
- **H_B** (format seul) : score(T*) ≈ score(T+).
- **Métrique** : rapport (T* − T−) / (T+ − T−).
- **Seuil** : < 0,3 pour H_A, > 0,7 pour H_B (illustratif) ; indéterminé entre les deux.
- **Contrôle négatif** : la perplexité du gabarit sous le modèle doit effectivement différer entre T+ et T*. Sinon, la manipulation de familiarité a échoué, et on le déclare.
- **Ce que falsifie chaque issue** :
  - Un rapport bas falsifie « le format suffit ».
  - Un rapport haut falsifie le mécanisme de *familiarité* invoqué par H-M1, même si « T domine » reste vrai.

### E3 — Circularité sonde/gabarit

- **H_A** : l'effet de T survit à une sonde entraînée sans aucun exemple T+ (leave-T-out).
- **H_B** : il s'effondre.
- **Métrique** : β_T(leave-T-out) / β_T(sonde complète).
- **Seuil** : > 0,5 pour H_A (illustratif).
- **Contrôle négatif** : même procédure en retirant un trait *non lié*, par exemple les contenus d'un domaine thématique. Le rapport doit alors rester proche de 1.
- **Ce que falsifie chaque issue** :
  - La survie falsifie « la sonde ne fait que lire T ».
  - L'effondrement falsifie l'usage de cette sonde pour tester H-M1. E1 est rétrogradé en exploratoire.

### E4 — H-M2 : stabilité par orbite (point 5)

**Ensembles de transformations écrits d'avance.** Ce sont des ensembles plutôt que des groupes : la composition de paraphrases n'est pas fermée.
- **G_sens** : 4 paraphrases du stem par tables syntaxiques écrites à la main, et permutation circulaire des options avec réécriture de la clé.
- **G_pos** : instruction placée avant ou après la question ; contenu système déplacé dans le tour utilisateur ; options placées avant le stem.

C'est ici que je fixe P8 : « permutation des options » relève de G_sens, « réordonnancement » de G_pos.

**Orbite d'un item** : ses images sous chaque ensemble. **Stabilité** : écart-type intra-orbite du score (SD_sens, SD_pos), et corrélation intraclasse.

- **H_A** (H-M2) : SD_pos / SD_sens > 2 (illustratif), apparié par item.
- **H_B** : rapport ≤ 1,25 (illustratif).
- **Contrôle négatif** : transformation triviale, par exemple renommer une entité sans rapport avec la question. Son écart-type donne le plancher de bruit.
- **Contrôle positif** : basculer T dans l'orbite. L'écart doit être de l'ordre de β_T.
- **Ce que falsifie chaque issue** :
  - Un rapport élevé falsifie « la position n'importe pas plus que la formulation ».
  - Un rapport bas falsifie H-M2.

### E5 — Dérive distributionnelle ou réponse au contenu

E4 ne départage pas, à lui seul, une dérive distributionnelle d'une réponse au contenu (P8). G_pos et G_sens gardent tous deux le contenu, et tous deux éloignent l'invite de la distribution d'entraînement. J'opérationnalise la « dérive » par Δ log-perplexité de l'invite sous le modèle.

- **H_A** (dérive) : dans les orbites, Δscore est expliqué par Δperplexité, avec R² > 0,3 (illustratif).
- **H_B** (contenu) : R² < 0,05 (illustratif), alors même que Δscore est non nul.
- **Contrôle négatif** : même régression avec une direction aléatoire, pour obtenir le R² nul.
- **Ce que falsifie chaque issue** :
  - Un R² élevé falsifie l'interprétation « réponse au contenu » des variations.
  - Un R² faible falsifie l'interprétation « dérive ».

---

## (c) Mesure minimale de fonctionnement des instruments nommés

| Instrument | Taux de détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre ou à égaler |
|---|---|---|---|---|
| **Sonde linéaire** | Taux de vrais positifs (TPR) à un taux de faux positifs (FPR) fixé de 5 % (illustratif) | FPR sur la classe « usage » appariée | Même texte de surface, provenance différente. Par exemple une question QCM présente à la fois dans un banc et dans un journal d'usage réel où un utilisateur l'a collée. L'existence de ces paires en nombre suffisant est une HYPOTHÈSE à vérifier. | Prédicteur de surface (§2.3) et TF-IDF + régression logistique. La sonde doit les **battre** (E0). |
| **Générateur de gabarits déterministe** | Fraction de mutants détectés. On injecte délibérément des défauts : trait T placé dans une cellule T−, contenu altéré, dépassement de la fenêtre de longueur. Cible : 100 %. | Fraction des items sains signalés à tort. Cible : 0. | Le même contenu rendu dans les 4 cellules | Assertions : diff du contenu après retrait des segments propres aux facteurs = vide ; expressions régulières de la table §2.1 ; identité du jeton de lecture. C'est un contrôle à **égaler**, qui doit passer à 100 %. |
| **Modèle à effets mixtes** | Puissance empirique sous données simulées avec β_C = δ | Taux de « C persiste » sous β_C = 0 simulé. Doit rester ≤ 5 %. | Jeux simulés avec la structure réelle (contenus, variantes) et les variances du pilote | Test t apparié sur les moyennes par contenu. Les deux doivent concorder ; un désaccord signale une mauvaise spécification. |
| **Transformations G_sens / G_pos** | Fraction de fausses paraphrases (négation insérée, option altérée) détectées par la vérification | Fraction de paraphrases correctes rejetées | L'item original et ses images | Clé de réponse recalculée après permutation ; contrôle humain d'un échantillon tiré au hasard, par exemple 10 % (illustratif). Une vérification par modèle de langue n'est admise qu'en audit, jamais en génération. |
| **Choix couche/position** | Stabilité du choix sous rééchantillonnage bootstrap de la validation | Fréquence à laquelle le choix change | Uniquement les partitions de l'entraînement | Couche fixe d'avance, en comparaison |

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs : aucun ne vient des faits.

- **Modèle cible** : Llama-3.1-8B-Instruct (RAPPORTÉ). Poids distribués sous licence communautaire Llama 3.1, avec accès soumis à acceptation. L'architecture (32 couches, dimension 4 096) est une HYPOTHÈSE à vérifier dans `config.json`.
- **Réplication** : d'autres modèles ouverts d'environ 7 à 9 milliards de paramètres en version Instruct, par exemple Qwen2.5-7B-Instruct, Mistral-7B-Instruct ou Gemma-2-9B-it. Un effet de T qui n'apparaît que sur un seul modèle n'établit pas H-M1 en général.
- **Outils** : `transformers` avec crochets (*hooks*) sur le flux résiduel, ou nnsight / TransformerLens ; `statsmodels` ou `lme4` pour les effets mixtes.
- **Calcul** :
  - Volume : environ 4 800 invites de test, environ 4 000 pour les orbites de H-M2, 2 000 à 6 000 pour l'entraînement de la sonde. Soit environ 15 000 passes avant de 300 à 500 jetons, environ 6 millions de jetons en préremplissage seul, sans génération (sauf la voie S3).
  - Matériel : un seul GPU de 80 Go, ou 24 Go en bf16, suffit. Durée de l'ordre de 15 à 45 minutes.
  - Stockage : un jeton × 32 couches × 4 096 × 2 octets ≈ 260 Ko par invite, soit ≈ 4 Go au total.
- **Coût** : location d'un GPU de type H100 à 2–4 $/h ; 3 heures avec les marges, soit moins de 15 $.
- **Goulot réel** : le temps humain, pas le calcul. Écrire 300 contenus neufs, les tables de variantes et les paraphrases, réunir les données S1 équilibrées et obtenir la contre-lecture prend plusieurs heures à plusieurs jours de travail humain, selon l'ampleur. C'est l'argument le plus fort pour (a′) contre (a) « cette nuit » : la carte graphique tourne en une heure, le préenregistrement crédible non.

---

## 6. Références

Je ne cite que ce que je crois pouvoir attribuer. Les éléments incertains sont marqués. Aucun identifiant arXiv n'est donné.

**Conscience d'évaluation et de situation de test**
- Needham, J., Edkins, G., Pimpale, G., Bartsch, H., Hobbhahn, M. (2025). *Large Language Models Often Know When They Are Being Evaluated.* Liste d'auteurs à vérifier.
- Nguyen, J. et al. (2025). *Probing Evaluation Awareness of Language Models.* Liste d'auteurs à vérifier. Si mon souvenir est exact, ce travail porte sur des sondes linéaires dans un modèle Llama plus grand, à vérifier.
- Laine, R. et al. (2024). *Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs.* Lieu de publication à vérifier.
- Travaux sur le pilotage linéaire de la « conscience de test » dans les modèles de raisonnement (Abdelnabi et Salem, 2025) : référence à vérifier.

**Sensibilité au format et à l'ordre des options**
- Sclar, M., Choi, Y., Tsvetkov, Y., Suhr, A. (2024). *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.* ICLR.
- Zheng, C., Zhou, H., Meng, F., Zhou, J., Huang, M. (2024). *Large Language Models Are Not Robust Multiple Choice Selectors.* ICLR.
- Pezeshkpour, P., Hruschka, E. (2024). *Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions.* Lieu de publication à vérifier.

**Méthodologie des sondes**
- Alain, G., Bengio, Y. (2016). *Understanding intermediate layers using linear classifier probes.*
- Hewitt, J., Liang, P. (2019). *Designing and Interpreting Probes with Control Tasks.* EMNLP.
- Marks, S., Tegmark, M. (2023). *The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets.*
- Ravfogel, S., Elazar, Y., Gonen, H., Twiton, M., Goldberg, Y. (2020). *Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection.* ACL.

**Corpora d'usage réel (voie S1)**
- Zhao, W. et al. (2024). *WildChat: 1M ChatGPT Interaction Logs in the Wild.* ICLR. Liste d'auteurs à vérifier.
- Zheng, L. et al. (2023). *LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset.*

**Statistique et inférence**
- Barr, D. J., Levy, R., Scheepers, C., Tily, H. J. (2013). *Random effects structure for confirmatory hypothesis testing: Keep it maximal.* Journal of Memory and Language.
- Bates, D., Mächler, M., Bolker, B., Walker, S. (2015). *Fitting Linear Mixed-Effects Models Using lme4.* Journal of Statistical Software.
- Platt, J. R. (1964). *Strong Inference.* Science.

---

## Ce qui reste réfutable dans cette proposition elle-même

1. **(a′) sur (a)** : si le pilote E0 montre que la sonde bat déjà nettement la surface, et qu'un relecteur est disponible, (a′) n'aura coûté qu'un délai inutile.
2. **La table d'attribution exclusive (§2.1)** : si les cellules hybrides T+C− et T−C+ produisent des scores aberrants, ces scores sont-ils dus au fait que ces invites sont peu naturelles, et non à T ou à C ? Cela se teste par leur perplexité.
3. **La correspondance retenue pour P8 (E4–E5)** : c'est mon choix. L'essaim ou l'arbitre peuvent en sceller une autre.

FIN-DE-CELLULE