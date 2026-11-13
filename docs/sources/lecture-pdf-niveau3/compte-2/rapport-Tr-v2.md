# Rapport du lecteur — Tr, « transposition du jeton à l'action » (papier A) — v2

- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Écrit le** : 2026-11-13T23:33:29Z (heure relevée par `date -u` dans la commande qui l'a inscrite). Version 2 commencée à 2026-11-13T23:26:32Z, reprise après un redémarrage du conteneur à 2026-11-13T23:30:03Z (heures relevées par `date -u`).
- **Remplace** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-Tr-v1.md`, sha256 `d04e2ef3660e50e1542e4b11e548897c6efe7516fc1f3c51d61a813df5f6a670` (archive `fichiers-de-travail-Tr-v1.tar`, `c0805da602799ec12157339d627b2be97f5f6294edef6e146e450cb1668c1cd7`). La version 1 reste en place, non modifiée.
- **Intègre la contre-lecture** : `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-Tr-v1.md`, sha256 `2a530bfe34f97a3c5a00677d839e865439ebc6c6fefba7ec20d8413e5425cb44` (vérifiée) ; archive `fichiers-de-travail-contre-lecture-Tr-v1.tar`, sha256 `956e62f7d1782b05cf30dc342afed24bdc51fff245c30945fc2e14eb806114dc` (vérifiée, extraite dans un sous-dossier neuf du dossier de travail). Verdict du contre-lecteur sur le rapport : « tient avec corrections » ; six constats majeurs (A, B, C, E, F, G), quatre mineurs (D, H, I, J), aucun bloquant.
- **Mandat** : verdict d'antériorité sur Tr par lecture intégrale de trois PDF versés (constat M6 de la contre-lecture du niveau 3) ; version 2 demandée pour intégrer la contre-lecture.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (vérifiée) ; interdits communs v2 lus et tenus.
- **Noms de modèles** : aucun n'est écrit ici (consigne, ligne 14) ; les modèles lus par les pièces sont désignés par leur taille et leur ouverture.

## Déclarations

- Aucune commande git, aucun appel réseau, aucun appel de modèle, aucune dépense. Aucun refus de permission. Aucune ouverture fautive.
- À la reprise, j'ai listé (sans récursion) le seul dossier de sortie : ni `rapport-Tr-v2.md` ni `fichiers-de-travail-Tr-v2.tar` n'existaient. La même commande a aussi listé, par mégarde, les noms de fichiers du dossier des pièces `lot10/` (dossier de travail hors du dépôt) : noms seulement, aucun autre PDF ouvert.

## Empreintes des PDF (vérifiées contre les compagnons `.sha256`, et revérifiées à la reprise : conformes)

| pièce | fichier | pages | sha256 |
|---|---|---|---|
| « Constitutional Classifiers++ » | `lot11/2601.04603v1.pdf` | 17 | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` |
| « Monitoring Emergent Reward Hacking During Generation via Internal Activations » | `lot10/2603.04069v1.pdf` | 14 | `4c035a3c362fbaa36ba8ad1127249566e216d8ccb567f0375707d409e139895f` |
| « Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations » | `lot10/2609.19101v2.pdf` | 39 | `c8ab50452ea3effc7865bb6b53f4c6159b150cafcd1864e3103f4da877f8ae3f` |

## Fichiers lus (liste exacte) et étendue

- `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md` (en entier).
- `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (en entier, demandé par la consigne commune).
- `docs/programme-controle-ia-v2.md`, lignes 85 à 125 et 180 à 200.
- `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 130 à 151.
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 183 à 191.
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 442 à 471.
- Mon rapport version 1 et son archive ; la contre-lecture en entier et son archive.
- Les trois PDF ci-dessus et leurs compagnons `.sha256`. Aucun autre fichier.

Étendue réellement lue :
- **2601.04603v1** : p. 1 à 17 ligne à ligne (`pdftotext -layout`), références (p. 11 à 13) parcourues par mots ; figures 2 (p. 7) et 5 (p. 16) lues sur l'image. **Relues pour la version 2** : p. 5, 6, 7, 8, 9, 10, 11, 15, 16, 17 (passages signalés par la contre-lecture) ; recherche par mots sur les 17 pages (moyenne mobile exponentielle, coefficient, décroissance, demi-vie, facteur de lissage) : aucun coefficient imprimé.
- **2603.04069v1** : p. 1 à 14 ligne à ligne ; références parcourues par mots ; figures lues par légendes et axes. **Relues** : p. 4, 5, 6, 9.
- **2609.19101v2** : p. 1 à 18 et 25 à 39 ligne à ligne ; références (p. 19 à 24) parcourues par mots ; figure 7 (p. 9) lue sur l'image ; recherche par mots sur les 39 pages. **Relues pour la version 2** : p. 3, 5, 6, 9, 10, 11, 13, 14, 17, 18, 24, 28, 37.

**Citations contrôlées par programme : 86 ; échecs : 0** (les 49 de la version 1 et 37 nouvelles ; script testé sur un cas juste, réussi, et sur trois cas altérés, en échec comme attendu ; contrôle relancé sur la version finale). Fichier `citations-Tr-v2.json` dans l'archive seulement.

---

## Verdicts

### Noyau de Tr : **non trouvé dans les pièces lues**

Le noyau (programme, l. 98) : la robustesse d'agrégations de scores de sondes, établie au grain du jeton, tient-elle au grain de l'action et de la trajectoire d'un agent, sous accumulation séquentielle, face à un attaquant adaptatif ? Dans les trois pièces lues, aucune ne compare des règles d'agrégation au grain de l'action ou de la trajectoire, avec ou sans attaquant ; aucune n'oppose un attaquant adaptatif à une sonde à ce grain ; aucune n'accumule séquentiellement des scores de sondes sur une trajectoire ; aucune ne porte une conclusion de robustesse du jeton à l'action. Le contre-lecteur, qui a cherché pour trouver, aboutit au même constat.

### Composantes faites, hors du noyau (verdicts par composante)

1. **(b) et (e) — 2609.19101** : sonde par jeton lue au grain du passage (un canal d'un pas : raisonnement, message ou appels d'outil) dans de longs déroulés d'agents, détection mesurée à ce grain, et sonde employée au grain du déroulé ; sans attaquant ; règle du jeton au passage et du passage au déroulé non imprimées pour la sonde. (b) **occupée en partie** ; (e) **occupée**.
2. **(d) — 2601.04603** : humains adaptatifs, en boîte noire, par le contenu, contre un système de production dont la première porte est une sonde lissée au fil des jetons ; au grain de l'échange, hors agent ; une seule règle, résultat non attribué à la règle. **Occupée en partie, à un autre grain que celui de Tr.**
3. **(a) — 2601.04603** : comparaison de variantes de lissage du score de sonde (fenêtre de 1 à 64 jetons ; maximum cumulé comme perte) au grain du jeton vers l'échange, sur des attaques humaines transférées (non adaptées aux règles comparées). **Occupée en partie**, avec un contre-indice à la prémisse « maximum robuste ».

### Lettre de la table fermée pour l'énoncé : **non trouvé dans les pièces lues** — divergence maintenue avec le contre-lecteur (« occupé en partie »)

Les faits concordent entre lecteur et contre-lecteur ; l'écart porte sur la place des trois composantes faites. Mes motifs, écrits :
1. **L'objet de Tr est le noyau.** L'énoncé (programme, l. 98) est une question conjointe dont chaque terme porte le grain de l'action ou de la trajectoire et l'attaquant adaptatif ; aucune composante faite n'y répond, même en partie, au grain qui la définit.
2. **(a) est la prémisse, pas la revendication.** L'énoncé tient la robustesse au jeton pour « établie » ; trouver de la matière à ce grain ne prend rien à Tr (elle la conteste plutôt : voir le nœud ci-dessous).
3. **(b) sans attaquant est rangée « voisin » par la convention du niveau 3.** L’état de l’art du niveau 3 (l. 185-187) classe « Agrégations au niveau de l'action sans attaquant adaptatif » parmi les voisins, sous un verdict « libre dans les pièces lues ; voisins ». 2609.19101 apporte exactement cette classe de faits. Changer d'étiquette pour elle ferait varier le verdict selon le lot lu, non selon les faits.
4. **(d) est faite au grain de l'échange**, avec une seule règle, sans comparaison ni attribution : hors du grain qui définit Tr.

Motif du contre-lecteur (rapporté tel quel) : la consigne définit « occupée en partie » par « composantes faites, non faites » ; trois composantes de l'énoncé ont de la matière faite, donc « occupé en partie » ; il admet que « non trouvé » se défend pour le seul noyau sous la convention du niveau 3, si les composantes faites sont écrites à côté (ce que fait ce rapport). **Divergence non résolue sur la lettre, à arbitrer ; elle ne change ni la pièce libre ni les gardes.**

Condition commune aux deux lectures : le verdict vaut pour trois pièces ; Wilhelm et Kao 2026, Yang et al. 2025 et « What the Monitor Saw », non lus, peuvent le renverser.

### Nœud pour le directeur (décrit, non tranché)

L'énoncé de Tr (programme, l. 98) écrit : « La robustesse des agrégations max et attention, établie au niveau token ». 2601.04603 plaide le contraire pour le **maximum brut** par jeton : par un motif imprimé, « Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as harmful. » (p. 6), et par des mesures à taux de refus égal (figures 2b, p. 7, et 5b, p. 16 : la variante sans lissage a un taux de succès d'attaque plus haut que la variante lissée à 16 jetons, figure). Ces mesures sont confondues (la fenêtre change aussi l'entraînement), sans barre d'erreur, non monotones, et portent sur des attaques transférées, pas adaptées. L'état de l'art du niveau 2 relevait déjà une « prémisse affaiblie » (`anteriorite-v1.md`, ligne « Prémisse affaiblie », dans les lignes 130 à 151). Toucher à l'énoncé est une modification d'hypothèse, donc un nœud de décision du directeur : je le décris, je ne propose rien.

---

## Suite donnée à la contre-lecture

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — formulation « revendicable » ambiguë, ne séparant pas de 2601.04603 | majeur | corrigé | « Ce qui reste revendicable » | Accepté : l'équipe rouge apprend le moniteur par l'usage (« We provide red-teamers with API access to the defended model. », 2601.04603 p. 15) ; ce qui sépare Tr de cette pièce est le grain, la comparaison de règles, l'accumulation et l'attaque par les poids. Reformulé par grain, comparaison, attaquant et accumulation, avec ce qui est fait et donc non revendicable. |
| B — « la sonde seule n'est jamais attaquée » trompeur ; (d) faite en partie à un autre grain | majeur | corrigé | Pièce 1, « Attaquant » ; table des composantes | Relu p. 9 : « When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » et « Otherwise, we rely solely on the probe. » ; « We applied the same red-teaming methodology described in previous sections. » La règle lissée est dans la boucle de chaque tentative. (d) : « occupée en partie, à un autre grain que celui de Tr ». Phrase remplacée par « la sonde n'est jamais attaquée isolément ; elle l'est comme première porte du système de production ». Ajout : d'autres équipes ont attaqué des versions du système (p. 11), sans résultat rapporté. |
| C — comparaison des lissages : pas « hors attaque », sur attaques transférées ; contre-indice non « léger » | majeur | corrigé | Pièce 1, « Agrégations » ; table ; nœud ; phrase publique | Relu p. 7 : « We assess robustness using a dataset of jailbreaks collected from human red-teaming, comprising approximately 7,000 exchanges » ; « We use only exchanges produced by red-teamers whose exchanges were never used for classifier training. » (a) devient « occupée en partie » ; contre-indice « confondu et fragile » (« We did not experiment with EMA during training », p. 6 ; « For evaluation, we compute predictions using an exponentially weighted moving average. », p. 7). Une réserve gardée dans la correction : que la fenêtre 1 soit, à l'inférence, le maximum brut est une lecture, car le lien entre la fenêtre d'entraînement et la moyenne mobile exponentielle d'inférence n'est pas imprimé. |
| D — « seul indice » faux pour la règle jeton → passage | mineur | corrigé | Pièce 3, « Grain » | Relu : seuil par position (p. 6), « every time the probe fires, the decision is then escalated to the LLM monitor » (p. 9), seuils réglés au grain du passage (p. 9), « Namely, we take the top 100 false positives as ranked by the probe » (p. 11), « max-activating examples for a probe are examined by an LLM » (p. 13), pic (p. 10) : six indices convergents vers un maximum par jeton, règle non imprimée. Incohérence ajoutée : produit scalaire (p. 6, formule) contre « Probe threshold (cosine similarity) » (p. 14). |
| E — grain de la trajectoire omis ; (b) faite en partie | majeur | corrigé | Pièce 3 ; table ; phrase publique | Relu p. 10 : « if we replaced some percentage of rollouts graded by an LLM monitor with probe grading » ; p. 28 : « Do not judge the transcript as a whole; the runtime aggregates your passage findings deterministically. » ; p. 37 : « the transcript shows reward hacking exactly when at least one of its passages is positive » (règle des juges, pas de la sonde). (b) devient « occupée en partie » (détection au grain du passage et du déroulé, sans règle explicite, sans robustesse, sans accumulation). |
| F — rien sous attaque, confirmé ; disparition du signal sous entraînement et voisin par les poids non relevés | majeur | corrigé | Pièce 3, « Attaquant » ; voisins | Relu p. 17-18 : « training procedures that suppress or erase representations of undesirable concepts may simultaneously incentivize the model to learn new representations of the same concepts » … « thus removing the original signal used to detect them ». Limite reconnue, travail futur : ni trou du champ (règle R8) ni occupation. Ajout du voisin Yang et al. 2025 (« incorporate projections onto these directions directly into the RL reward », p. 17 ; titre p. 24) en priorité haute ; observations spontanées de conscience d'évaluation (p. 3, 18) signalées, plus proches de H8 que de Tr. |
| G — bases pour E1.5 : deux non imprimées telles quelles, trois manquantes | majeur | corrigé | « Bases nommées pour E1.5 » | Recherche par mots sur les 17 pages de 2601.04603 : coefficient de la moyenne mobile exponentielle non imprimé. La « lecture par pic » de 2609.19101 n'est pas une règle imprimée. Section réécrite avec les seules règles imprimées (moyenne glissante de 16 jetons à l'entraînement, maximum cumulé et maximum cumulé recuit, combinaison pondérée de production, moyenne sur l'empan, seuil par position, « au moins un passage » des juges, pondération douce attribuée à une autre source), et ce qui ne l'est pas, dit. |
| H — 2603.04069 : F1 de 1,000 non expliqué ; (b) « voisin » et non « ne touche pas » | mineur | corrigé | Pièce 2 ; table | Accepté : « The monitor produces one decision per generation. » (p. 5) ; une génération est l'analogue, hors agent, d'une action : (b) « voisin ». Raison du F1 trop propre ajoutée (classe positive, effectifs et taux de faux positifs non imprimés ; accord possiblement dégénéré). Deux incohérences ajoutées (juge à la fois vérité et évalué, p. 5 ; axe de la figure 3 jusqu'à 60 tranches pour des raisonnements de 64 à 512 jetons, p. 6). |
| I — réserves R4 incomplètes | mineur | corrigé | « Réserves » | Ajouts : sondes choisies sur données étiquetées (« We select two probes per model: one with the highest AUROC on a held out set of 250 rollouts », p. 9) parmi 54 directions (tableau 3, p. 26, auteurs), ou par le taux de tir le plus haut sans vérité (p. 13) ; passages sans consensus exclus (p. 5) ; poids de l'ensemble optimisé sur le jeu de test (2601.04603, p. 8) ; figures sans barre d'erreur ; avertissement des auteurs sur le surajustement (p. 17). |
| J — voisins non lus à compléter | mineur | corrigé | « Voisins nommés et non lus » | Ajouts : Yang et al. 2025 (haute) ; Bergen et al. 2026 ; Zou et al. 2024 ; Casper et al. 2024 ; Wilhelm et Kao étendu à une collision possible sur (c). McKenzie et al. 2025 : vérifié dans mes lignes (`anteriorite-v1.md`, l. 141, section Tr du niveau 2) — lu au niveau 2 contre Tr, verdict « voisin (niveau jeton seulement) ». |

---

## Pièce 1 — 2601.04603v1, « Constitutional Classifiers++ »

**Venue imprimée** : arXiv 2601.04603v1 [cs.CR], 8 janvier 2026 (p. 1). La pièce 3 la cite comme parue à la quatorzième Conférence internationale sur les représentations apprises, 2026 (2609.19101, p. 20).

**Ce qu'elle fait.** Défense de production contre les contournements universels (domaine des armes chimiques, biologiques, radiologiques et nucléaires) : (i) classifieur d'échange qui lit la réponse pendant la génération dans le contexte de la demande, « evaluating tokens in batches as they are sampled » (p. 3) ; (ii) cascade à deux étages (p. 4-5) ; (iii) sondes linéaires sur les activations du modèle protégé, toutes couches concaténées (p. 7), ensemble sonde et classifieur externe (p. 8-9) ; (iv) système final : la sonde surveille tous les échanges pendant la génération et fait monter les échanges suspects au second étage ; score final des échanges montés pondéré 0,55 sonde et 0,45 classifieur (p. 9, auteurs) ; sinon, la sonde décide seule (« Otherwise, we rely solely on the probe. », p. 9, pour la cascade de la section 5.3).

**Modèle lu** : le modèle protégé lui-même (modèle propriétaire de l'éditeur, taille non publiée) ; activations de toutes les couches (p. 7, p. 9).

**Grain** : score par jeton, lu en flux ; décision au grain de l'**échange** ; « Crucially, these labels are exchange-level labels » (p. 5). Une alarme coupe la suite (« reflecting how a single flag blocks all subsequent content for streaming classification », p. 6). L'attaque est parée si le classifieur « flags at any point during model sampling » (p. 7) — règle qui équivaut, à la lecture, au maximum courant du score lissé comparé à un seuil (lecture, non imprimée sous ce nom).

**Agrégations et comparaisons** :
- Entraînement : moyenne glissante des logits sur M jetons (« we average logits over a sliding window of M tokens during training », p. 6), M = 16 (p. 7, auteurs) ; perte pondérée par une fonction exponentielle normalisée (p. 6).
- Inférence : « During inference, we use an exponential moving average (EMA) instead of a sliding window mean for computational convenience. » (p. 6) ; « For evaluation, we compute predictions using an exponentially weighted moving average. » (p. 7). **Le coefficient de cette moyenne n'est imprimé nulle part** (recherche sur les 17 pages) ; « We did not experiment with EMA during training » (p. 6). Le lien entre la fenêtre M d'entraînement et le lissage d'inférence n'est pas imprimé.
- Motif imprimé du lissage : « Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as harmful. » (p. 6).
- Données de comparaison : **attaques humaines transférées**, non adaptées aux règles comparées : « We assess robustness using a dataset of jailbreaks collected from human red-teaming, comprising approximately 7,000 exchanges » ; « We use only exchanges produced by red-teamers whose exchanges were never used for classifier training. » (p. 7) ; tronquées à 20 000 jetons (p. 7) ; seuils « calibrated to 0.1% refusal rates on WildChat » (légende de la figure 2, p. 7), donc à taux de refus égal. Les auteurs les disent statiques : « All evaluations were conducted on static jailbreak datasets of CBRN-related queries. » (p. 7).
- Comparées : fonctions de perte (lissage et pondération, l'un, l'autre, aucun : figure 2b, p. 7 ; plus « par jeton », maximum cumulé, maximum cumulé recuit : figure 5a, p. 16) ; taille de fenêtre de 1 à 64 (figure 5b, p. 16 : « Performance improves as we increase the window size from no smoothing », « However, excessive smoothing degrades performance. ») ; nombre de couches (figure 2c).
- Valeurs lues sur la figure 5b (figure) : fenêtre 1 environ 0,041 ; 2 environ 0,027 ; 4 environ 0,022 ; 8 environ 0,026 ; 16 environ 0,014 ; 32 environ 0,020 ; 64 environ 0,060 — non monotone, sans barre d'erreur. Figure 2b (figure) : lissage et pondération environ 1,4 ; pondération seule environ 4 ; lissage seul environ 13 ; aucun environ 14,5. Meilleure sonde « approximately 1.4% » (p. 8, auteurs).
- Le maximum cumulé est comparé **comme prédicteur d'entraînement** : « We explore using the cumulative maximum of probe probabilities as the predictor for the full sequence label. » ; résultat : « We find that our softmax loss-weighting with activation smoothing achieves stronger performance than these additional loss functions. » (p. 16).
- 2601.04603 distingue sa pondération de l'agrégation d'une autre pièce : « While they aggregate token scores into single sequence-level predictions, we build streaming classifiers with continuous predictions during generation. » ; « We use a softmax to weight per-token losses, not to aggregate predictions over tokens. » (p. 10).

**Attaquant** : équipe rouge **humaine**, adaptative au sens où elle itère contre le système défendu avec retour (« We provide red-teamers with API access to the defended model. », p. 15), avec primes ; contre le système de production à sonde en première porte : « We applied the same red-teaming methodology described in previous sections. » ; « The system underwent an estimated 1736 cumulative hours » ; « Only one high-risk vulnerability was discovered » (p. 9). Comme un échange non monté n'est lu que par la sonde, toute attaque réussie a soit tenu le score lissé sous le seuil à chaque jeton, soit battu la combinaison pondérée (lecture). **La sonde n'est jamais attaquée isolément ; elle l'est comme première porte du système de production.** Boîte noire, par le contenu ; aucune connaissance déclarée de la sonde ; aucune attaque par les poids ; aucune attaque conçue contre le lissage ; aucune comparaison de règles sous cette attaque ; résultat au grain du système, non attribué à la règle. D'autres équipes ont attaqué des versions du système (« for red teaming various versions of our system », p. 11), sans résultat rapporté. Hors programme de primes, des experts « were nonetheless able to discover universal jailbreaks for this system » (p. 5, système à deux étages sans sonde). Attaques de reconstruction (fragmentation d'une demande sur des segments bénins) et d'obfuscation de sortie contre la génération précédente (p. 2-3) : voisin conceptuel du sabotage diffus, contre des classifieurs externes.

**Cadre agentique** : aucun. **Transposition explicite jeton → action** : aucune.

**Limites reconnues** : le critère « alarme à tout point » « may underestimate the attack success rate » (note 6, p. 7) ; plus d'alarmes de la sonde sur des requêtes scientifiques bénignes (p. 8) ; « relying solely on synthetic benchmarks can lead to overfitting on limited test cases » (p. 17).

**Incohérence interne** : la figure 5 dit employer « the same evaluation datasets and methodology as described in the main paper » (p. 16), mais ses valeurs sont environ 100 fois plus petites que celles de la figure 2b pour des variantes identiques (calcul) ; probablement une fraction notée en pourcentage. Sans effet sur Tr.

---

## Pièce 2 — 2603.04069v1, « Monitoring Emergent Reward Hacking During Generation via Internal Activations »

**Venue imprimée** : atelier « Principled Design for Trustworthy AI » de la Conférence internationale sur les représentations apprises 2026 (en-tête, p. 1) ; arXiv 2603.04069v1 [cs.CL], 4 mars 2026.

**Ce qu'elle fait.** Détection du piratage de la récompense pendant la génération : autoencodeurs parcimonieux par couche, standardisation, analyse en composantes principales, régression logistique par couche, entraînée « to distinguish activations originating from hack versus control adapters » (p. 4), sur les deux adaptateurs extrêmes seulement (« trained only on activations from the benign control adapter and the fully reward-hacking adapter », p. 5). Mélanges intermédiaires traités comme inédits : « Mixed-ratio adapters are trained on datasets containing 5%, 10%, 50%, or 90% School of Reward Hacks examples » (p. 5).

**Modèles lus** : trois modèles ouverts de 7 à 8 milliards de paramètres, de trois familles (p. 5) ; quatre dernières couches (p. 13).

**Grain** : jeton (« token-level estimates of reward-hacking activity », p. 1) → **moyenne** sur l'empan (« To obtain a stable behavior-level signal, token-level probabilities are aggregated over a predefined token span » ; « we compute the mean probability over tokens in the selected span », p. 4) → moyenne sur les couches → seuil fixe 0,5 : « The monitor produces one decision per generation. » (p. 5). Tranches de 64 jetons et statistiques de fin de génération : descriptives (p. 6, 11-13).

**Agrégations comparées** : aucune. **Attaquant** : aucun. **Agent** : aucun (génération à un tour). **Transposition** : aucune.

**Résultats** : F1 contre un juge externe de 0,760 à 1,000 (tableau 1, p. 5, auteurs) ; structure temporelle propre à chaque famille (p. 6) ; « We emphasize that this evidence is correlational » (p. 8).

**Limites reconnues** : « Our experiments focus on a single reward-hacking benchmark and a limited set of model families and sizes » (p. 8) ; « judges may decrease the reliability of results » (p. 9).

**Réserves (règle R4)** :
- Construit : le classifieur peut lire l'identité de l'adaptateur plutôt que le comportement ; la montée avec la proportion de données de piratage (figure 2, p. 5) est compatible avec les deux lectures ; non discuté.
- F1 = 1,000 pour l'adaptateur témoin dans les trois familles (tableau 1, p. 5, auteurs) : la pièce n'imprime ni la classe comptée comme positive, ni les effectifs, ni un taux de faux positifs ; si presque toutes les générations du témoin sont dites « témoin » par le juge comme par le moniteur, l'accord est dégénéré et ne prouve pas une discrimination (lecture).
- Incohérences : adaptateur « fine-tuned on reward-hacking examples » (p. 3) contre « For LoRA-Finetuning the GRPO Algorithm is used » (p. 13 ; optimisation de politique relative par groupe, apprentissage par renforcement) ; le juge externe est la vérité terrain (p. 5) et, phrase suivante, « output-based judgments achieve good performance for control adapters » (p. 5) ; « For each model family, we evaluate CoT lengths of 64, 128, 256, and 512 tokens. » (p. 6) avec des tranches de 64 jetons, alors que l'axe de la figure 3 va jusqu'à 60 (figure).

---

## Pièce 3 — 2609.19101v2, « Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations »

**Venue imprimée** : arXiv 2609.19101v2 [cs.CL], 9 octobre 2026 (p. 1) ; aucune venue imprimée.

**Ce qu'elle fait.** Mesure du piratage de la récompense de modèles ouverts de très grande taille dans des évaluations agentiques (génie logiciel, puis achats, conversation, cybersécurité) ; sondes par **différence des moyennes** construites sur des paires minimales synthétiques (5 285 conversations de 9 tours, tableau 4, p. 27, auteurs) ; comparaison avec un moniteur fondé sur un grand modèle de langue ; cascade sonde → moniteur et « ou » sonde–moniteur (p. 9) ; pilotage causal (p. 8) ; découverte de comportements guidée par la sonde (p. 13-16).

**Modèles lus** : trois modèles ouverts dits « frontière », jusqu'à 2,8 billions de paramètres (p. 3), un quatrième au tableau 1 (p. 6), un modèle ouvert de 27 milliards pour le pilotage (p. 8) ; une couche par sonde.

**Grain** :
- Jeton : « we use it as a linear token-level probe by scoring each position » ; « flagging positions whose score exceeds a threshold » (p. 6).
- **Passage** : « A passage is one channel of one step: » (p. 31) ; « Reasoning traces, assistant messages, and tool calls each receive their own labels. » (p. 5) ; « These comparisons use passage-level ground truths that include both contemplated and attempted/completed hacks. » (p. 9).
- **Déroulé** : la sonde y est employée (« if we replaced some percentage of rollouts graded by an LLM monitor with probe grading », p. 10 ; figure 9, p. 11) ; unité de la figure 9 ambiguë.
- **Règle jeton → passage : non imprimée.** Six indices convergent vers un maximum par jeton comparé à un seuil : seuil par position (p. 6) ; « every time the probe fires, the decision is then escalated to the LLM monitor » (p. 9) ; « we select probe thresholds that match the LLM monitor’s false positive rate » (p. 9) ; « Namely, we take the top 100 false positives as ranked by the probe » (p. 11) ; « max-activating examples for a probe are examined by an LLM » (p. 13) ; « identify the peak probe location within each passage » (p. 10). Lecture, non imprimée. Aucune autre règle essayée ni comparée.
- **Règle passage → déroulé : imprimée pour les juges seulement**, et c'est « au moins un » : « Do not judge the transcript as a whole; the runtime aggregates your passage findings deterministically. » (p. 28) ; « the transcript shows reward hacking exactly when at least one of its passages is positive » (p. 37). Rien d'imprimé pour la sonde ; aucune accumulation séquentielle.
- Faux ami écarté : « In addition, we test several poolings over individual datasets. » (p. 7) porte sur la mise en commun des jeux synthétiques (tableau 3, p. 26) ; « When harvesting activations, we consider several locations that apply to all environments. » (p. 7) porte sur la construction de la sonde.

**Attaquant** : aucun ; aucune évaluation sous obfuscation, consigne d'évitement, réglage contre la sonde, ni modèle averti d'une surveillance. Nommés comme travail futur : l'obfuscation du raisonnement (« A further challenge is that models may learn to obfuscate undesirable behavior from their reasoning traces », p. 17) et la disparition du signal sous un entraînement qui efface les représentations (« training procedures that suppress or erase representations of undesirable concepts may simultaneously incentivize the model to learn new representations of the same concepts », p. 17, « thus removing the original signal used to detect them », p. 18) — limite reconnue, ni trou du champ (règle R8) ni occupation. Voisin nommé, non lu : Yang et al. 2025, dont la pièce dit qu'ils « incorporate projections onto these directions directly into the RL reward » (p. 17). Observations spontanées sans protocole : modèles « largely evaluation aware » (p. 3) ; « our probes for reward hacking tend to fire near or on these positions » (p. 18) ; « Indeed, we already found some rollouts from this work to be obscure for some models and settings. » (p. 17) ; « Our study does not control for evaluation awareness in any of our experiments » (p. 18). Ces points regardent H8 plus que Tr.

**Cadre agentique** : oui (déroulés de plus de 100 000 jetons, p. 10 ; appels d'outil, p. 5, 15).

**Transposition explicite jeton → action** : aucune conclusion d'agrégation ou de robustesse portée d'un grain à l'autre. Lien temporel seulement : « DoM vectors run on the chain-of-thought also predict reward hacks in the model’s subsequent actions » (p. 1) ; rééchantillonnage au pic : 28,6 % contre 1,1 % et 14,1 % contre 1,5 % de piratages tentés (figure 10, p. 11, auteurs).

**Résultats chiffrés** : aire sous la courbe de fonctionnement du récepteur de 0,74 à 0,97 (figure 8, p. 10, auteurs) ; « probes catch 3.0 and 33.1 percentage points more hacks on DeepSWE and ImpossibleBench respectively » (p. 9) ; sonde ajoutée au moniteur : vrais positifs de 41,1 % à 80,2 % pour 1 point de faux positifs en plus (p. 9, auteurs).

**Limites reconnues** : « A trained probe would almost certainly perform better than our diff of means vectors. » (p. 18) ; moniteur non optimisé (p. 18).

**Incohérences internes** : résumé « catching 3.1% more hacks in » [premier modèle], 7,9 % de moins pour le second (p. 1), contre 3,0 points (p. 9) et rappels 0,41 → 0,44 et 0,41 → 0,33 (p. 10) : +3 et −8 points (calcul) ; score défini par un produit scalaire (p. 6, formule) mais seuils en « Probe threshold (cosine similarity) » (figure 14, p. 14).

---

## Table composante × article (version 2)

| composante | 2601.04603v1 | 2603.04069v1 | 2609.19101v2 |
|---|---|---|---|
| (a) robustesse des agrégations au grain du jeton (prémisse) | **occupée en partie** : lissages comparés au taux de succès d'attaque sur environ 7 000 attaques humaines transférées, à taux de refus égal ; **contre-indice** au maximum brut, confondu avec l'entraînement, sans barre d'erreur, non monotone ; non fait : attaquant adapté aux règles comparées (p. 6, 7, 16) | ne touche pas | ne touche pas |
| (b) transposition au grain de l'action | ne touche pas (grain de l'échange, p. 5) | **voisin** : une décision par génération, par moyenne, hors agent (p. 4-5) | **occupée en partie** : détection au grain du passage (appels d'outil compris) et du déroulé, dans des agents ; règles non imprimées ; non fait : règle explicite, comparaison, robustesse (p. 5, 6, 9, 10, 31) |
| (c) comparaison des agrégations au grain de l'action | ne touche pas (comparaison au grain du jeton seulement : voir (a)) | ne touche pas | ne touche pas (p. 7, 26) |
| (d) attaquant adaptatif | **occupée en partie, à un autre grain** : humains adaptatifs, boîte noire, par le contenu, contre un système à sonde lissée en première porte ; non fait : comparaison de règles sous attaque, attaquant informé, attaque par les poids, grain de l'action, agent, attribution à la règle (p. 6, 7, 9, 15) | ne touche pas | ne touche pas ; obfuscation et effacement du signal nommés comme travail futur (p. 17-18) |
| (e) dans un agent | ne touche pas | ne touche pas | **occupée** (composante isolée, non distinctive de Tr) (p. 3, 5, 10) |
| (f) accumulation séquentielle sur la trajectoire | ne touche pas | ne touche pas | ne touche pas ; seule règle imprimée au déroulé : « au moins un passage positif », pour les juges (p. 28, 37) |

## Ce qui reste revendicable (formulations exactes, séparées)

Ces formulations disent l'état des trois pièces lues ; elles ne sont pas la phrase publique (rôle exclu).
- **Grain** : « Non trouvé dans les pièces lues : la mesure de la robustesse d'une règle d'agrégation de scores de sondes au grain de l'action d'un agent (un pas, un appel d'outil) ou de sa trajectoire. Trouvé, donc non revendicable : la lecture d'une sonde par jeton à ces grains pour la détection, sans attaquant (2609.19101). »
- **Comparaison** : « Non trouvé dans les pièces lues : une comparaison de règles d'agrégation de scores de sondes (maximum, lissage, moyenne, pondération de type attention, accumulation séquentielle) au grain de l'action ou de la trajectoire, avec ou sans attaquant. Trouvé, donc non revendicable : la comparaison de lissages au grain du jeton vers l'échange, sur des attaques humaines transférées (2601.04603). »
- **Attaquant** : « Non trouvé dans les pièces lues : un attaquant adaptatif, par le contenu ou par les poids, opposé à une sonde au grain de l'action d'un agent. Trouvé, donc non revendicable : des humains adaptatifs, en boîte noire, contre un système dont la première porte est une sonde lissée au fil des jetons, au grain de l'échange (2601.04603). »
- **Accumulation** : « Non trouvé dans les pièces lues : l'accumulation séquentielle de scores de sondes sur la trajectoire d'un agent. »
- **Transposition** : « Non trouvé dans les pièces lues : une conclusion de robustesse portée du grain du jeton au grain de l'action. »

## Bases nommées pour E1.5 (règles imprimées seulement ; le périmètre de E1.5 reste au directeur)

Imprimées :
1. **Moyenne glissante des logits sur 16 jetons** (2601.04603, p. 6-7 ; formule 2), règle d'entraînement ; alarme en un point quelconque de la génération (p. 7).
2. **Maximum cumulé** des probabilités lissées (2601.04603, p. 16 ; formule 5), et **maximum cumulé recuit** (formule 6), imprimés comme prédicteurs d'entraînement.
3. **Combinaison pondérée de production** : 0,55 sonde et 0,45 classifieur sur les échanges montés (2601.04603, p. 9) — cascade, non une agrégation temporelle.
4. **Moyenne sur l'empan puis sur les couches, seuil 0,5** (2603.04069, p. 4-5 ; formules 2 à 4) — le programme ne la permet qu'en bras de diagnostic.
5. **Seuil par position de jeton** (2609.19101, p. 6 ; formule 1).
6. **« Au moins un passage positif »** au grain du déroulé (2609.19101, p. 28, 37) — imprimée pour des juges qui lisent le texte, pas pour la sonde.
7. **Pondération douce agrégeant des scores par jeton** — imprimée dans 2601.04603 (p. 10) seulement comme description de McKenzie et al. 2025 (lu au niveau 2 contre Tr) ; à prendre dans la source.

Non imprimé, à fixer et déclarer par nous si on s'en sert : le coefficient de la moyenne mobile exponentielle d'inférence de 2601.04603 et son lien avec la fenêtre d'entraînement ; la règle jeton → passage et passage → déroulé de la sonde de 2609.19101 (un maximum par jeton est une lecture, appuyée sur six indices) ; toute règle d'accumulation séquentielle de sondes.

## Ce qu'une phrase publique sur Tr ne doit pas affirmer

- Être les premiers à lire une sonde au grain du pas ou de l'appel d'outil dans des déroulés d'agent (2609.19101, p. 5, 9, 31).
- Être les premiers à porter une sonde par jeton au grain du déroulé entier d'un agent (2609.19101, p. 10).
- Être les premiers à lire des sondes pendant la génération pour détecter le piratage de la récompense (2603.04069, p. 1 ; 2609.19101, p. 1).
- Être les premiers à agréger des scores de sonde au fil des jetons en production, ou que l'agrégation en flux n'a jamais été éprouvée par des attaquants adaptatifs (2601.04603, p. 6, 9 : 1736 heures d'équipe rouge humaine contre un système à sonde en première porte).
- Qu'aucune règle de lissage ou d'agrégation de scores de sonde n'a été comparée sur des données d'attaque (2601.04603, p. 7 et 16 : attaques humaines transférées).
- Que le maximum brut par jeton est la règle de référence au grain du jeton (2601.04603, p. 6, 16 ; voir le nœud pour le directeur).
- Que l'évasion d'une sonde par un entraînement qui efface les représentations n'a été nommée par personne (2609.19101, p. 17-18).
- Que la question est « libre dans le champ » : « non trouvé dans les pièces lues » seulement (règle R8).

## Voisins nommés dans les pièces et non lus (avec la page où ils sont nommés)

- **Priorité haute** : Wilhelm et Kao 2026, « From reward-hack activations to agentic risk states: Context-calibrated mechanistic monitoring in LLM agents », atelier « Agents in the Wild » (2609.19101, p. 17 et 24) — collision possible sur (b), (c) et (e).
- **Priorité haute** : Yang et al. 2025, arXiv 2510.17431, « Agentic reinforcement learning for search is unsafe » (2609.19101, p. 17 et 24) — projections sur des directions linéaires mises dans la récompense d'un agent : mécanique d'un attaquant par les poids, collision possible sur (d) au grain de l'agent.
- **Priorité haute, déjà signalé** : « What the Monitor Saw » (état de l'art niveau 3, l. 188-189), non obtenu.
- Priorité moyenne : Bergen et al. 2026, arXiv 2606.12360 (2609.19101, p. 17 et 19) ; Zou et al. 2024, arXiv 2406.04313, et Casper et al. 2024, arXiv 2403.05030 (2601.04603, p. 10, 12, 13) ; Sharma et al. 2025, arXiv 2501.18837, maximum cumulé recuit pour le flux (2601.04603, p. 16 et 13) ; Cunningham et al. 2025, billet « Cost-effective constitutional classifiers via representation re-use » (2601.04603, p. 10 et 12) ; Hua et al. 2025, arXiv 2507.15886 (2601.04603, p. 10 et 12) ; Zhou et al. 2026, arXiv 2606.24251 (2609.19101, p. 17 et 24).
- Priorité basse (moniteurs de texte ou garde-fous) : Baker et al. 2025, arXiv 2503.11926 (2603.04069, p. 2 et 9 ; 2609.19101, p. 1-2 et 19) ; Arnav et al., « CoT red-handed » (2609.19101, p. 2 et 19) ; Drori et al., arXiv 2511.11584 (2609.19101, p. 20) ; Youstra et al. 2025, arXiv 2508.17158 (2601.04603, p. 13) ; Chennabasappa et al. 2025, arXiv 2505.03574 (2603.04069, p. 3 et 9) ; Goldowsky-Dill et al. 2025 (2609.19101, p. 17 et 20).
- Lu au niveau 2 contre Tr : McKenzie et al. 2025, arXiv 2506.10805 (2601.04603, p. 10 et 12 ; 2609.19101, p. 22) — `anteriorite-v1.md`, l. 141, « voisin (« niveau jeton seulement ») » ; porteur de l'agrégation « attention » de la prémisse.

## Réserves (règles R4 et R8)

- Le verdict repose sur trois pièces ; la zone est séduisante et se vérifie plus durement ; trois voisins non lus peuvent le renverser (ci-dessus).
- 2601.04603 : un travail interne non publié sur l'attaque de l'agrégation est plausible et invisible ici ; poids de l'ensemble « optimized per pair to minimize attack success rate on the test set » (p. 8) ; figures 2 et 5 sans barre d'erreur.
- 2609.19101 : sondes choisies sur données étiquetées (« We select two probes per model: one with the highest AUROC on a held out set of 250 rollouts », p. 9) parmi 54 directions (tableau 3, p. 26, auteurs) ; hors vérité, choisies par le taux de tir le plus haut (« select the probe with the highest firing rate at that threshold on these two non-SWE environments », p. 13) ; « Non-consensus passages are not considered when measuring performance. » (p. 5) ; vérité terrain par un juge fondé sur le même grand modèle de langue que le moniteur comparé (p. 4).
- 2603.04069 : construit (adaptateur contre comportement) et F1 dégénéré possible (ci-dessus).
- Les attaques de reconstruction de 2601.04603 (p. 2-3) sont l'analogue du sabotage diffus contre une agrégation ; elles visent des classifieurs externes : voisin, pas occupation.

## Formules (lues sur le PDF, non contrôlées par programme)

- 2601.04603, éq. 2 (p. 6) : z̄_t = (1/M) Σ_{k=0}^{M−1} [Wᵀ ψ_{t−k} + b] ; éq. 5 (p. 16) : p(y = 1 | x_{1:t}) = max_{τ ≤ t} σ(z̄_τ) ; éq. 6 (p. 16) : (1 − ω)·σ(z̄_t) + ω·max_{τ ≤ t} σ(z̄_τ) ; p. 9 : z_final = 0,55 · z_probe + 0,45 · z_classifier.
- 2603.04069, éq. 2-4 (p. 4-5) : m_ℓ = (1/|T|) Σ_{t∈T} p_{t,ℓ} ; P(hack) = (1/|L|) Σ_ℓ m_ℓ ; décision si P ≥ 0,5.
- 2609.19101, éq. 1 (p. 6) : v_hack = E_{t∈P}(x_t) − E_{t∈N}(x_t) ; s_t = ⟨v_hack, x_t⟩, position signalée si s_t dépasse un seuil.

## Archive

`docs/sources/lecture-pdf-niveau3/compte-2/fichiers-de-travail-Tr-v2.tar` : script de contrôle des citations, `citations-Tr-v2.json` (86 citations), sortie du contrôle, essais juste et altéré avec leurs sorties, journal du lecteur version 2 ; sans PDF, ni textes extraits, ni images.
