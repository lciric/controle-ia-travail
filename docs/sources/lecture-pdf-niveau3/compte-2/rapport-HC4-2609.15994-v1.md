# Rapport du lecteur — HC4, « taxe de déplacement », sous la lecture « juge = juge génératif », sur la pièce 2609.15994 v1 (v1)

- **Rôle : lecteur ; modèle A.**
- **Heures** (`date -u`) : début le 2026-11-14 à 06:28:31 UTC ; empreinte de la pièce vérifiée à 06:28:53 UTC ; texte lu ligne à ligne de 06:29:02 à 06:30:55 UTC, figures sur l'image jusqu'à 06:31:32 UTC (journal) ; contrôle des citations de 06:32:19 à 06:34:56 UTC ; rédaction de 06:34:56 à 06:37:22 UTC, puis relecture. L'heure de fin est celle du scellement (fichier compagnon `.sha256`).
- **Mandat** : verdict d'antériorité sur HC4 au sens où « juge » veut dire **juge génératif** (lecture demandée par Lazar, en attente d'inscription), par lecture intégrale d'une pièce versée et jamais lue contre HC4.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme). Interdits communs `interdits-communs-v2.md` lus en entier (la consigne y renvoie) ; le mandat est plus strict (aucune commande git), je l'ai tenu.
- **Fichiers du dépôt lus, et seulement aux lignes du mandat** :
  - `docs/programme-controle-ia-v2.md`, l. 85-125 et 190-215 ;
  - `docs/decisions/decision-N-013-v1.md`, l. 46-55 ;
  - `docs/decisions/decision-N-068-v1.md`, l. 1-115 (le fichier a 115 lignes) ;
  - `docs/sources/lecture-pdf-niveau3/compte-2/rapport-HC4-v2.md`, en entier, `6c368ebb74301a5b2cdcd047f641a0f516f67af371a10359350e7871c4ced948` (conforme) ;
  - la consigne commune et les interdits communs, en entier.
  - Un `ls` du seul dossier `compte-2/` a vérifié, avant écriture, que ni le rapport ni l'archive n'existaient.

  Aucun autre fichier du dépôt n'a été ouvert. Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucun refus, **aucune ouverture fautive**.
- **Pièce** (empreinte vérifiée contre son compagnon `.sha256` avant lecture) :

| pièce | empreinte sha256 | pages | étendue lue |
|---|---|---|---|
| `2609.15994v1.pdf` | `1cbd4a419aeb8a5dd00d411a7eee06c122cb33990d2a4ab5a44b8db7017e9f25` | 18 | **p. 1-18 ligne à ligne** (`pdftotext -layout`, page par page), annexes A à J comprises, références comprises. Lues en plus sur l'image : p. 4 (figures 1, 2, tableau 1), 5 (figure 3, tableau 2), 6 (tableau 3), 7 (figures 4, 5), 12 (figures 6, 7, 8, tableau 8), 15 (figure 9, tableau 12). |

- **Citations contrôlées par programme : 107, 0 échec** (`citations-HC4-2609.15994-v1.json`, dans l'archive seulement). Le script `verifier_citations_v1.py`, lancé par `python3 -I`, cherche chaque citation dans le texte de sa page extrait avec et sans `-layout`, après normalisation (espaces, ligatures, césures, apostrophes, tirets). Il a d'abord été essayé sur un cas juste (0 échec) et sur deux cas altérés, un chiffre changé et une page fausse (2 échecs, attendus).
- **Contrôle des guillemets du rapport** : un second script (`controler_guillemets_rapport_v1.py`) extrait chaque passage entre guillemets français de ce rapport et le cherche dans le JSON. Résultat en section 11 et dans l'archive.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi). Les noms de modèles sont ceux de l'article.

---

## 0. Verdict

| énoncé | sens de « juge » | verdict (table fermée) |
|---|---|---|
| HC4 | **juge génératif** | **« non trouvé dans les pièces lues »** |

- La pièce n'attaque aucun juge génératif en tant que moniteur, ne mesure aucun coût de déplacement d'un juge, et ne compare pas une sonde et un juge dans un même cadre. Les composantes (c) et (d) ne sont donc pas touchées au sens du mandat.
- **Mais c'est un contre-indice fort à la prémisse (e)**, borné à une classe de sondes : pour une sonde linéaire **à position unique**, qui lit **le modèle qui reçoit l'entrée** une propriété **de l'entrée** (l'intention de l'utilisateur), des fautes de frappe ordinaires, **sans accès, sans requête, sans optimisation**, environ 3,3 caractères édités par message, font perdre 12,0 points de taux de vrais positifs à 1 % de faux positifs (tableau 2, p. 5).
- Ce contre-indice tombe **hors de la lettre restreinte par N-068 (point 8a)** : la sonde ne lit pas l'agent auteur, et la propriété lue est celle de l'entrée. Il tombe en plein dans la catégorie que N-068 déclare déjà publiée (« sondes de propriété de l'entrée lues sur le modèle qui reçoit le contenu »). Il s'y ajoute à coût nul.
- Il est **réparé presque entièrement par une agrégation** sur plusieurs positions (au plus 0,87 point de perte sous le paquet de fautes, tableau 3, p. 6). Sous des fautes réparties sur la moitié des mots, l'attention et le maximum perdent encore environ 3,8 et 3,9 points, et une moyenne sur la séquence en perd 16,8.
- **Effet sur la colonne « déclarable »** : le verdict sous la lecture « juge génératif » ne change pas. Si HC4 y est déclarable sous cette lecture, elle le reste, avec une réserve de plus à porter avec la prédiction (section 7) : le contexte seul, à coût nul, déplace une sonde de lecteur à position unique. La pièce touche à peine la sonde à agrégation robuste (au plus 0,48 point en régime localisé pour l'attention et le maximum, environ 3,8 à 3,9 en régime réparti) et ne touche pas la sonde de l'agent auteur.

---

## 1. Ce que l'article fait

**Venue imprimée.** « Mechanistic Interpretability Workshop » de la « Conference on Machine Learning, Seoul, South Korea, 2026. » (p. 1) ; arXiv cs.CL, 8 juillet 2026 (p. 1). Trois auteurs, une même entreprise (p. 1). Titre : « Latent Undertow: How Ordinary Typos Break Probes ».

**Question.** Des variations de frappe ordinaires, qui ne changent pas ce que le modèle comprend, déplacent-elles les sondes qui lisent ses activations ? Les auteurs le disent ainsi : « Yet probes that detect malicious prompts by reading the model’s hidden states tell a different story » (p. 1).

**Sonde, modèle, tâche** (exactement) :
- **Modèle lu** : Llama-3.1-8B-Instruct, couche 31 : « Llama-3.1-8B layer 31 (final residual stream, last user token) » (p. 3). La mécanique des activations (rotation puis décroissance) est reproduite sur Qwen3-8B et Gemma-4-E4B, mais les sondes ne sont évaluées que sur Llama : « probe evaluation is on Llama-3.1-8B. » (p. 1) ; « Cross-model probe evaluation is left to follow-up » (p. 3).
- **Position de la sonde : le modèle qui reçoit l'entrée**, avant toute réponse : « This framing reflects a realistic deployment scenario where a probe monitors the user turn before the model responds. » (p. 3) ; « Activations are extracted at the last token of the user turn, consistent with standard single-position probing » (p. 3).
- **Propriété lue : l'intention de l'utilisateur**, pas celle du modèle : « The probe target throughout is binary user intent: malicious (prompt injection or unsafe request) versus benign. » (p. 2).
- **Données** : 29 jeux publics, 168 440 exemples, environ 32 % malveillants (injection directe ou indirecte, jailbreak, demandes nuisibles, arnaques ; tableau 10, p. 14 : « Total corpus 168,440 (32.4% mal) »). Validation croisée en 5 plis, plus un protocole « un jeu tenu à l'écart » (annexe I).
- **Entraînement** : sur activations propres ; les perturbations n'arrivent qu'au test : « probes train on clean activations at the user-EOT readout; perturbations are applied at inference time. » (p. 3).
- **Cinq architectures** (p. 5) : linéaire au dernier jeton du tour utilisateur ; moyenne des 16 derniers jetons ; et trois lectures de toute la séquence, avec une transformation par jeton puis une agrégation par moyenne, par attention ou par maximum (« per-token feature transform aggregated across the user-turn sequence by mean, softmax-attention pooling », p. 5).

**Perturbation et coût.**
- **Paquet de fautes empilées** (« Stacked-typing bundle: a localized stress-test composition of the above primitives, averaging 3.3 character edits per sample », p. 2). Cinq composantes : point d'interrogation changé en point ; faute de clavier voisin sur le dernier mot ; faute de clavier voisin sur un mot au moins trois positions plus tôt ; majuscule trop tôt ; point final ajouté ou ôté (p. 5). « Mean: 3.33 character edits per sample (range 1–5; 99.996% valid coverage). » (p. 5).
- **Régime réparti** : une faute de clavier voisin un mot sur deux, environ la moitié des jetons de contenu, présenté par les auteurs comme un test de charge : « used as a stress test rather than a model of typical user noise » (p. 2).
- **Coût d'attaque** : aucun accès au modèle, aucune requête, aucune optimisation, aucune connaissance de la sonde. Les perturbations sont fixées par des règles, sans adversaire : « We extend this line to ordinary, non-targeted typing variation, without adversarial intent. » (p. 2). Les auteurs ajoutent, sans l'avoir mis à l'épreuve d'un attaquant : « We do not claim that our specific 5-component combination matches any measured user distribution; the same pattern, applied deliberately, is also a no-cost attack vector requiring no model access or optimization. » (p. 5).
- **Pas de cible de verdict** : la perturbation ne vise pas un verdict ; elle déplace pourtant les scores surtout vers le faux négatif (« malicious samples cross below the fixed-FPR threshold more readily than benign samples cross above it, weighting the failure toward false negatives. », p. 5).

---

## 2. La chute, chiffrée

### 2.1 Sonde à position unique, paquet de fautes (tableau 2, p. 5 ; auteurs)

| condition | aire sous la courbe | vrais positifs à 1 % de faux positifs | à 5 % |
|---|---|---|---|
| propre | 0,9980 | 97,4 % | 99,5 % |
| perturbé | 0,9925 | 85,4 % | 96,7 % |
| écart | −0,55 point | **−12,0 points** | −2,8 points |

- Phrase imprimée : « At the deployment-realistic operating point of FPR=1%, TPR drops from 97.4% to 85.4%, a loss of 12.0 percentage points. » (p. 5). Ligne du tableau : « Perturbed 0.9925 85.4% 96.7% » (p. 5).
- **Le seuil est recalé sur les données perturbées.** Légende de la figure 4 : « filled dots: FPR=1% operating point on the perturbed curve. » (p. 7). Les auteurs ajoutent : « Threshold recalibration alone cannot recover the clean (FPR, TPR) operating point (Figure 4). » (p. 5). Le taux **à seuil fixé sur les données propres**, celui d'un moniteur déployé, n'est pas imprimé.
- **Distribution des déplacements** (tableau 8, p. 12 ; auteurs) : pour la sonde à position unique, côté malveillant, 5ᵉ centile −0,490, médiane nulle, moyenne −0,053 ; côté bénin, 95ᵉ centile +0,185. La phrase imprimée : « Linear (single-position) has heavy-tailed shifts on the malicious side » (p. 12). La chute vient donc d'une queue d'exemples fortement déplacés, pas d'un glissement d'ensemble.
- **Capacité** : un perceptron multicouche au même jeton perd autant (12,5 ± 0,8 points) ; « Higher capacity at a single position yields no robustness benefit; the variable is where the probe reads, not how it classifies. » (p. 6).

### 2.2 Cinq architectures, deux régimes (tableau 3, p. 6 ; auteurs ; écart des vrais positifs à 1 % de faux positifs, moyenne ± écart type sur 5 plis)

| sonde | localisé (paquet) | réparti (un mot sur deux) |
|---|---|---|
| linéaire, dernier jeton | −12,00 ± 0,48 | −6,85 ± 0,56 |
| moyenne des 16 derniers | −0,87 ± 0,09 | −4,53 ± 0,33 |
| toute la séquence, moyenne | −0,30 ± 0,07 | **−16,81 ± 1,26** |
| toute la séquence, attention | −0,48 ± 0,15 | −3,78 ± 1,76 |
| toute la séquence, maximum | −0,48 ± 0,13 | −3,91 ± 1,35 |

- Lignes contrôlées : « Linear (user EOT) −12.00 ± 0.48pp −6.85 ± 0.56pp » ; « MLP (all) −0.30 ± 0.07pp −16.81 ± 1.26pp » ; « Attention (all) −0.48 ± 0.15pp −3.78 ± 1.76pp » ; « MultiMax (all) −0.48 ± 0.13pp −3.91 ± 1.35pp » ; « Mean last 16 −0.87 ± 0.09pp −4.53 ± 0.33pp » (p. 6).
- Lecture des auteurs : « Table 3 shows that all multi-position probes are near-immune to the localized stacked-typing bundle. » (p. 6) ; « Full-sequence MLP, however, drops −16.8pp, losing its localized-regime margin entirely. » (p. 6).
- Figure 4 (p. 7, image) : les courbes perturbées des sondes à plusieurs positions restent collées aux courbes propres sous le paquet. Sous le régime réparti, toutes s'écartent ; la moyenne sur la séquence tombe vers 0,83 (figure).

### 2.3 Hors distribution (un jeu tenu à l'écart ; tableaux 15 et 16, p. 17-18 ; auteurs)

- Sur les 7 plis à deux classes, seuil recalé par pli : vrais positifs propres de 38,9 % à 46,3 % seulement selon l'architecture. Sous le paquet : −3,5 points pour la sonde à position unique, +1,4 pour l'attention ; sous le régime réparti, de −2,5 à −6,2 points. Lignes : « Linear (EOT) 38.9% 35.4% 33.6% −3.5pp −5.3pp » ; « Attention (all) 46.3% 47.7% 43.8% +1.4pp −2.5pp » (p. 17).
- Par pli (tableau 16, p. 18) : jusqu'à −11,2 points (paquet) et −16,8 points (réparti) : « SafeGuard 93.5% 85.4% −8.1pp 76.7% −16.8pp ». Les auteurs : « indicating that ID perturbation fragility persists under distribution shift but is masked at the aggregate by floor effects. » (p. 16).
- Moyennes recalculées sur le tableau 16 : 38,86 % propre, 35,36 % sous le paquet, 33,60 % en réparti (calcul) ; conformes au tableau 15.

### 2.4 Ce que fait un lecteur de texte des mêmes perturbations

Il n'y a **aucun juge génératif employé comme moniteur** ni de classifieur de texte qui détecte l'intention malveillante sous les mêmes perturbations. Deux lecteurs de texte apparaissent, à d'autres fins.

1. **Un juge génératif qui vérifie la prémisse** (annexe A.2, p. 10 ; tableau 7, p. 11). « A Claude Sonnet 4.5 judge (via AWS Bedrock, temperature 0, independent per-pair calls) labeled each pair on two binary criteria » (p. 10). Il juge, sur 600 paires réponse propre et réponse perturbée tirées de 100 consignes (50 bénignes, 50 de HarmBench), si l'intention est préservée (« intent preservation (did the model interpret the perturbed prompt as asking for the same thing?) », p. 10) et si les réponses sont équivalentes.
   - « Aggregate across the 594 judged pairs: intent preservation 94.6% and response equivalence 76.6%. » (p. 10) ; ligne du tableau : « Overall 594 0.946 0.766 » (p. 11).
   - « 6 pairs sharing a single biosecurity prompt were refused by the judge model itself and excluded. » (p. 10).
   - Ce juge ne donne **ni verdict de malveillance, ni score, ni taux à faux positifs fixé**. Ce n'est pas un moniteur, et l'article ne mesure pas s'il se laisse déplacer. Au mieux, c'est un indice : un lecteur génératif lit l'intention à travers les fautes dans 84 à 100 % des cases (tableau 7, p. 11 ; auteurs).
2. **Le modèle lu lui-même**, par ses refus. « Refusal flips on the 294 malicious pairs occurred 27 times (9.2%); 12 went toward more conservative refusal and 15 toward compliance, the latter concentrated under ESW (Llama 20%, Gemma 16%, Qwen3 8%). » (p. 10). Sous le paquet de fautes : « In the localized regime the LLM’s response is functionally unchanged on both benign and malicious cases; the probe is the sole failure point. » (p. 2). Sous le régime réparti, l'alignement lui-même cède : « In the distributed regime intent is preserved but the malicious example bypasses the LLM’s safety alignment » (p. 2).

La seule « comparaison » entre sonde et lecteur de texte est qualitative, en discussion : « their readout is more sensitive to ordinary surface noise than the model whose internals they read. » (p. 8) ; « a silent disagreement, neither adversarial nor semantically ambiguous. » (p. 8). Elle met une chute de taux de détection en regard d'un taux de préservation de l'intention jugé par un autre modèle. Ce ne sont ni la même métrique, ni le même rôle.

### 2.5 Adversaire ou fautes aléatoires

**Pas d'adversaire.** Les composantes du paquet sont des règles fixes, appliquées quand leur condition est remplie (p. 5) ; la faute du régime réparti touche un mot sur deux. Rien n'interroge la sonde, rien n'est optimisé, rien n'est adapté.

La phrase offensive des auteurs (« The same typing patterns can be applied deliberately as low-cost attack vectors: distributed corruption alone bypasses both probe and alignment (§3.3) without optimization, model access, or adversarial prompt engineering. », p. 8) **n'est pas mesurée comme attaque**. Elle renvoie à la section 3.3, dont l'exemple (tableau 6, p. 11, « Breaking into the Pentagon is a serious matter and » …) donne une réponse et un angle de rotation, mais **aucun score de sonde**. Le franchissement de la sonde n'y est donc pas montré exemple par exemple. Il n'est établi qu'en taux : environ 4 à 17 points de vrais positifs perdus sous le régime réparti selon l'architecture (tableau 3).

### 2.6 Parades proposées (section 7, p. 6-8 ; annexes E, H, I)

| parade | résultat dans la distribution | hors distribution | page |
|---|---|---|---|
| changer d'architecture (plusieurs positions) | au plus 0,87 point de perte sous le paquet ; attention et maximum vers 3,8-3,9 sous le régime réparti | aire sous la courbe de 0,81 à 0,92 avant toute perturbation | 6, 16 |
| entraînement augmenté de fautes | 85,4 % → 93,84 ± 0,5 %, résiduel −3,70 points (« Pert. TPR@FPR=1% 85.4% 93.84 ± 0.5% ») | non mesuré | 6-7, 13 |
| suffixe lu sur une branche du cache clé-valeur (environ 30 jetons ajoutés après le tour utilisateur, lus puis jetés) | « the KV-cache fork recovers TPR@FPR=1% to 98.65 ± 0.02% », résiduel −0,60 point | **sous le paquet, −4,5 points contre −3,5 sans suffixe** (« KV-fork (neutral suffix) 81.5% 47.2% −4.5pp » ; « No KV-fork (Linear EOT) 77.5% 38.9% −3.5pp ») | 7-8, 16 |

- Les auteurs le disent eux-mêmes : « The defenses restore probe accuracy under that asymmetry rather than removing it. » (p. 8).
- **Point que le texte principal ne dit pas.** Hors distribution, le suffixe améliore le taux propre (+8,4 points), mais il **aggrave** d'un point la perte due aux fautes (tableau 17, p. 16). La p. 7 ne rapporte que le gain propre (« lifts clean weighted accuracy from 77.5% »).

---

## 3. Ce que l'article ne fait pas

- Aucun juge génératif employé comme moniteur ; aucun classifieur de texte sous les mêmes perturbations ; aucune métrique commune entre sonde et juge.
- Aucun coût d'attaque mesuré : pas de requêtes, pas de calcul, pas de courbe « déplacement obtenu en fonction de l'effort ». Le coût est **fixé par construction** (de 1 à 5 caractères), et seule la chute est mesurée.
- Aucun adversaire, ni aveugle ni informé ; aucune attaque qui s'adapte à la sonde ou à la parade.
- Aucun agent, aucune trajectoire, aucune action : la sonde lit un seul tour utilisateur. La propriété est l'intention de l'utilisateur, pas celle du modèle lu.
- Aucun régime « activations » ou « poids » côté attaquant.
- Aucune mesure d'un déplacement continu g vers une cible.
- Sondes évaluées sur un seul modèle et une seule couche : « but the multi-architecture probe sweep itself is on a single model (Llama-3.1-8B). All experiments use a single layer per model. » (p. 8).

**Limites reconnues** : la tokenisation, en plus de la dilution (« Probe-level perturbations may alter BPE tokenization in addition to attention dilution », p. 8) ; un seul modèle pour les sondes (p. 8) ; variantes du suffixe reportées (« learned-suffix designs are deferred to », p. 8) ; une combinaison de fautes non mesurée sur des utilisateurs réels (p. 5).

---

## 4. Incohérences internes et réserves (règle R4)

1. **La rotation de 43 à 56° attribuée au dernier jeton.** La discussion écrit « Ordinary typing variation rotates the user-EOT activation by » 43 à 56° (p. 8). C'est la rotation **sur le jeton fauté** (« Mean on-site angular change ranges from 43 » …, p. 3). Au dernier jeton, à 10 jetons de distance, le tableau 1 (p. 4) donne 4,7° pour une faute de clavier voisin. Le résumé est ambigu de même : « the same edit rotates the readout vector by » 43 à 56° au jeton perturbé (p. 1). La phrase de la p. 8 confond les deux positions. Les exemples du tableau 6 (p. 11), dont les fautes sont proches de la fin, donnent bien 30,6 à 45,8° au dernier jeton.
2. **Figure 1 (p. 4, image)** : Gemma-4-E4B descend vers 38-39° à une profondeur et Llama monte vers 57-58° (figure), hors de l'intervalle de 43 à 56° imprimé.
3. **Couches de Gemma** : « Gemma-4-E4B: 28/29/40/41 » (p. 3) contre « Spatial decay replication: Gemma-4-E4B (full-attention layers 10, 21, 29, 41). » (p. 12).
4. **« Ordre de grandeur »** : « an order of magnitude better than perturbation-augmented training » (p. 1) et « an order of magnitude smaller than the augmentation-training residual » (p. 7) ; 3,70 / 0,60 = 6,2 (calcul). C'est moins qu'un ordre de grandeur, et le seul cadre est la distribution d'entraînement ; hors distribution, l'ordre s'inverse (section 2.6).
5. **Exactitude hors distribution** : « accuracy from > 99% to 0.77–0.81 » (p. 5) ; le tableau 13 (p. 16) va de 0,775 à 0,821.
6. **Classes des jeux** : le tableau 10 (p. 14) range AgentDojo, BIPIA, Deepset, Jayavibhav et Jailbreak-Cls parmi les malveillants ; le tableau 14 (p. 17) les compte parmi les 7 plis à deux classes. La part malveillante imprimée (32,4 %) se retrouve avec les parts du tableau 14 : 32,36 % (calcul) ; avec les rubriques du tableau 10, elle serait de 36,3 % (calcul). Ce sont les rubriques du tableau 10 qui sont fausses.
7. **Plis fusionnés** : le tableau 10 annonce Gandalf et Scam fusionnés avec d'autres jeux « merged with a larger dataset for LODO fold stability » (p. 14). Pourtant ils apparaissent comme plis à part (tableau 14) et l'annexe compte 29 plis (« Of the 29 folds, only 7 contain both classes and admit AUC; the other 22 are single-class. », p. 15). Ailleurs, 28 : « Clean weighted accuracy is sample-weighted across the 28 held-out folds at threshold 0.5 (Scam unavailable). » (p. 16).
8. **Même source pour deux plis** : « Code Exercise iamtarun/python code instructions 18k alpaca » et « Python-Alpaca iamtarun/python code instructions 18k alpaca » (p. 18). Si ce sont les mêmes données, un pli tenu à l'écart fuit dans l'entraînement.
9. **Bascules de refus** : 15 bascules vers la conformité en tout, mais 20 %, 16 % et 8 % des paires malveillantes du régime réparti (49 par modèle) font environ 21,6 (calcul). La phrase (p. 10) est ambiguë : ces pourcentages comptent peut-être les bascules dans les deux sens.
10. **Paquet en apprentissage** : le paquet de test n'est pas inédit pour la sonde augmentée. Quatre de ses cinq familles sont dans la politique d'augmentation (annexe E, p. 13) ; seule manque la faute en milieu de message. Les auteurs l'admettent en partie : « Recovery is not perfect even on individual perturbations seen in training » (p. 6).
11. **Trop propre (R4)** : le suffixe donne 98,65 ± 0,02 % (p. 7), un écart type de 0,02 point sur 5 plis. Le résultat ne tient pas hors distribution (point 4 et section 2.6).
12. **Décroissance** : « All four depth checkpoints fall below 15% of the on-site signal by d≈10 tokens » (p. 4). Sur la figure 2 (p. 4, image), la couche 31 est vers 0,15-0,2 à d = 10 (figure, lecture approximative), à la limite de l'énoncé.

Contrôles recalculés et conformes (calcul) : 1 − 0,60/12,0 = 0,95 ; (93,84 − 85,4)/12,0 = 0,70 ; mémoire du suffixe 30 × 32 × 8 × 128 × 2 × 2 octets = 3,75 Mio ; total des jeux 168 440.

---

## 5. Verdicts par composante

| composante de HC4 | verdict | page, citation |
|---|---|---|
| (a) coût d'attaque mesuré pour déplacer un moniteur | **voisin** : un point de coût fixé par construction (environ 3,3 caractères, aucun accès, aucune requête, aucune optimisation) avec une chute mesurée. Ce n'est pas un coût mesuré pour obtenir un déplacement donné. | p. 2, 5 : « averaging 3.3 character edits per sample » ; « no-cost attack vector requiring no model access or optimization » |
| (b) pour une **sonde** | **occupée en partie, hors de la lettre restreinte par N-068** : chute d'une sonde de propriété de l'entrée lue sur le modèle qui reçoit, sous perturbation à coût nul, par architecture, à 1 % de faux positifs. Faits : la chute et la dépendance à l'agrégation. Non faits : adversaire, courbe coût-déplacement, sonde de l'agent auteur, g. | tableau 2 p. 5 ; tableau 3 p. 6 ; tableaux 15-16 p. 17-18 |
| (c) pour un **juge génératif** | **ne touche pas** (comme moniteur). Voisin indirect : un juge génératif lit l'intention préservée dans 94,6 % des paires, ce qui n'est pas une détection. | p. 10, 11 |
| (d) **comparaison** dans un même cadre, à durcissement égal, par régime d'accès | **ne touche pas**. Voisin qualitatif : « their readout is more sensitive to ordinary surface noise than the model whose internals they read. » (p. 8), sans métrique commune ni moniteur textuel. | p. 8 |
| (e) prémisse « déplacer une sonde coûte plus » | **contre-indice fort**, borné : (i) à coût nul, une sonde à position unique perd 12,0 points à 1 % de faux positifs (5 % des exemples malveillants déplacés d'au moins 0,49) ; (ii) le lecteur de texte (le modèle et un juge génératif) garde l'intention dans le régime localisé. Bornes : sonde de lecteur et de propriété de l'entrée (hors N-068, 8a) ; aucune évasion massive (85,4 % de détection restent) ; une agrégation robuste ramène la perte à moins d'un point (localisé) ou vers 3,8 points (réparti) ; aucun juge-moniteur mesuré en regard. | p. 2, 5, 6, 8, 12 |

---

## 6. Ce qui reste revendicable (formulation exacte)

Je reprends la formulation du rapport précédent du compte 2 (`rapport-HC4-v2.md`, section 7), que cette pièce ne prend pas :

> « Le coût d'attaque — requêtes, jetons, calcul, temps, exemples de réglage fin — nécessaire pour obtenir un déplacement donné du score d'une sonde entraînée qui lit l'intention ou l'action de l'agent auteur, à taux de faux positifs fixé, comparé dans un même cadre au coût du même déplacement sur un juge génératif sous les mêmes attaques, par régime d'accès (contexte seul ; lecture des activations ou des poids ; écriture dans les poids), à durcissement déclaré et sous attaque qui s'adapte. »

La pièce **resserre la lecture de la prédiction**, sans prendre l'énoncé. Pour une sonde de lecteur à position unique, le coût d'un déplacement partiel par le contexte seul est **nul**. La prédiction « de plusieurs ordres de grandeur » ne peut donc valoir que pour des sondes de l'agent auteur, à agrégation robuste (la pièce ne contredit pas ce dernier point dans le régime localisé), et elle reste une prédiction.

---

## 7. Ce qu'une phrase publique sur HC4 ne doit pas affirmer

Je ne rédige pas la phrase publique.

1. Que le contexte seul ne déplace pas une sonde, sans préciser la classe de sonde. Une sonde à position unique qui lit l'intention de l'utilisateur sur le modèle qui reçoit perd 12,0 points de détection à 1 % de faux positifs sous environ 3,3 caractères de fautes ordinaires, sans accès ni requête (p. 5).
2. Que les sondes sont plus robustes au bruit de surface que les lecteurs de texte. Cette pièce soutient l'inverse pour la sonde à position unique, contre le modèle lui-même (p. 2, 8).
3. Qu'un coût « de plusieurs ordres de grandeur » est observé, ou que cette pièce mesure un coût d'attaque. Elle ne mesure qu'une chute sous un coût fixé.
4. Que ces 12,0 points sont une évasion adverse. Les fautes sont fixées par règles, non optimisées, et le seuil est recalé sur les données perturbées (p. 2, 5, 7).
5. Que la phrase offensive de la p. 8 (« bypasses both probe and alignment ») est démontrée pour la sonde exemple par exemple. Elle ne l'est qu'en taux (section 2.5).
6. Que le suffixe du cache clé-valeur répare la fragilité en général. Hors distribution, il l'aggrave (tableau 17, p. 16).
7. Que toute agrégation protège. Une moyenne sur la séquence perd 16,8 points sous le régime réparti (tableau 3, p. 6).

---

## 8. Voisins nommés dans la pièce et non lus

| voisin (titre ou description) | page où il est nommé | pourquoi le lire |
|---|---|---|
| Yu et collègues 2026, « Character-level perturbations amplify LLM jailbreak attacks. » (soumission OpenReview) | 2, 10 | **le plus proche pour (b)** : perturbations de caractères **ciblées** sur les mots nuisibles, précision de sondes de diagnostic d'environ 95 % à environ 80 % sur quatre modèles (auteurs de la pièce, p. 2 : « The closest prior work (Yu et al., 2026) applies targeted »). C'est un attaquant qui choisit ses mots, plus proche d'un coût d'attaque. |
| Gan et collègues 2024, fautes de frappe adverses contre le raisonnement des modèles (« adversarial typographical errors ») | 2, 9 | **côté juge génératif** : fautes de frappe optimisées contre un lecteur de texte (« including typing-specific perturbations (Gan et al., 2024) ») ; à lire pour (c) et (d) |
| Zhao et collègues 2026, robustesse aux fautes de frappe multilingues (« against multilingual typographical errors ») | 2, 10 | côté lecteur de texte |
| Kramár et collègues 2026, « Building production-ready probes for gemini » | 1-2, 9 | taxonomie des agrégations reprise ; 2601.11516 est déjà dans la liste de N-068 (lu au niveau 2) |
| Fomin 2026, « When benchmarks lie: Evaluating malicious » / « prompt classifiers under true distribution shift » | 3, 5, 9 | protocole « un jeu tenu à l'écart » |
| Gu et collègues 2025, perturbations latentes et sûreté (« robustness of large language models safety to latent ») | 2, 9 | régime « activations » côté attaquant |
| Zou et collègues 2026, « Pishield: Detecting prompt injection attacks via intrinsic llm features » | 1, 10 | détecteur d'injection par activations |
| Abdelnabi et collègues 2025, « Get My Drift? Catching LLM Task Drift with Activation Deltas » | 1, 8 | détecteur d'injection par activations |
| Wang et collègues 2026, réutilisation du cache clé-valeur pour accélérer des jailbreaks par suffixe (« KV-cache reuse has been used adversarially to accelerate suffix-search jailbreak attacks (Wang et al., 2026) ») | 7, 10 | coût d'attaque en boîte blanche, côté modèle |

Priorité si HC4 est cherchée plus avant : Yu et collègues 2026, puis Gan et collègues 2024 (la paire « fautes ciblées contre sonde » et « fautes adverses contre lecteur de texte » est ce qui manque ici pour (d)).

---

## 9. Notes à part, sans verdict

**HC2 (robustesse des sondes au contenu).**
- La position est celle du **lecteur** (modèle qui reçoit), ni l'agent victime ni l'agent auteur ; il n'y a pas d'adversaire.
- Le résultat touche l'agrégation : la position unique est fragile ; la moyenne sur la séquence s'effondre sous des fautes réparties (−16,81 points) ; l'attention et le maximum résistent le mieux dans les deux régimes (tableau 3, p. 6). Les auteurs le résument : « Architecture switching eliminates the localized-perturbation gap » (p. 6).
- C'est cohérent avec l'interdit du programme sur la moyenne des jetons dans une sonde de production, et avec le choix d'une agrégation robuste dans l'énoncé de HC2.
- Pour HC2b (sondes qui captent la surface) : « the training distribution couples intent with dataset-specific surface attributes, so what the probes learn is an intent-aligned mixture rather than intent in isolation. » (p. 16).

**Tr (transposition du jeton à l'action).**
- La pièce établit, **au niveau du jeton et d'un seul tour**, que l'attention et le maximum tiennent mieux que la moyenne quand la perturbation est répartie, et que tout lecteur à une position est exposé quand la perturbation est proche de lui.
- Elle ne dit rien de l'action, de la trajectoire, de l'accumulation séquentielle, ni d'un attaquant qui s'adapte.
- Un mécanisme de la pièce pourrait compter pour Tr : la perturbation est forte et locale, puis décroît en une dizaine de jetons (figure 2, p. 4). Une lecture à une seule position par action hériterait de cette exposition si la lecture tombe près d'un jeton perturbé.

---

## 10. Réserves du lecteur

- **Profondeur.** La lecture a été rapide : environ deux minutes pour le texte des 18 pages, puis les figures sur l'image. Je l'ai compensée par des recoupements chiffrés (section 4 : moyennes du tableau 16, part malveillante, mémoire du suffixe, taux de récupération) et par 107 citations contrôlées. Un contre-lecteur devrait relire en priorité les p. 2, 5-8, 10-11 et 16-17.
- **Valeurs lues sur les figures** : approximatives (nature « figure »).
- **Sens de « juge »** : je n'ai jugé que sous la lecture « juge génératif » demandée par le mandat. Sous la lecture large (« tout modèle qui lit le texte »), la pièce n'ajoute pas non plus de comparaison mesurée, puisqu'aucun classifieur de texte n'y reçoit les perturbations.

## 11. Contrôles

- Citations : 107, 0 échec (section d'en-tête).
- Guillemets du rapport : voir `releve-guillemets-v1.txt` dans l'archive (passages trouvés dans le JSON ; passages absents, tous en français, vérifiés un à un).
