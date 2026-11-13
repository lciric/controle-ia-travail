# Rapport du lecteur — Tr, « transposition du jeton à l'action » (papier A) — v1

- **Écrit le** : 2026-11-13T23:13:28Z (heure relevée par `date -u` dans la commande qui l'a inscrite). Lecture commencée à 2026-11-13T23:05:59Z (`date -u`).
- **Rôle** : lecteur. **Modèle** : modèle A.
- **Mandat** : verdict d'antériorité sur Tr par lecture intégrale de trois PDF versés et jamais lus contre elle (constat M6 de la contre-lecture du niveau 3).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme) ; interdits communs v2 lus et tenus.
- **Noms de modèles** : conformément à la consigne (ligne 14), aucun nom de modèle n'est écrit ici ; les modèles lus par les pièces sont désignés par leur taille et leur ouverture.

## Empreintes des PDF (vérifiées contre les compagnons `.sha256`, toutes conformes)

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
- Les trois PDF ci-dessus et leurs compagnons `.sha256`. Aucun autre fichier ; aucun rapport d'un autre lecteur.

Étendue réellement lue (détail dans le journal de l'archive) :
- **2601.04603v1** : p. 1 à 17 ligne à ligne (`pdftotext -layout`), références (p. 11 à 13) parcourues par mots ; figures 2 (p. 7) et 5 (p. 16) lues sur l'image.
- **2603.04069v1** : p. 1 à 14 ligne à ligne ; références (p. 9-10) parcourues par mots ; figures lues par légendes et axes.
- **2609.19101v2** : p. 1 à 18 et 25 à 39 (annexes, grilles des juges) ligne à ligne ; références (p. 19 à 24) parcourues par mots ; figure 7 (p. 9) lue sur l'image ; recherche par mots sur les 39 pages (agrégation, mise en commun, maximum, pic, moyenne, fenêtre, adversaire, attaque, évasion, obfuscation, adaptatif, robuste).

**Citations contrôlées par programme : 49 ; échecs : 0** (script testé d'abord sur un cas juste, réussi, et sur trois cas altérés, en échec comme attendu). Fichier des citations dans l'archive seulement.

---

## Verdict d'ensemble (table fermée)

**Tr : non trouvé dans les pièces lues.**

Aucune des trois pièces ne compare des agrégations de scores de sondes au grain de l'action, aucune ne met un attaquant adaptatif face à une règle d'agrégation, aucune ne porte une conclusion du grain du jeton au grain de l'action. Deux composantes **isolées** sont faites et doivent être dites :
- **2609.19101** lit une sonde (vecteur de différence des moyennes) dans de longs déroulés d'agents et évalue au grain du « passage », c'est-à-dire un canal d'un pas (raisonnement, message, appels d'outil du pas) : composante (e) faite, composante (b) voisine (application au grain du pas, sans agrégation comparée ni robustesse).
- **2601.04603** déploie en production une sonde lue au fil des jetons, lissée par moyenne mobile exponentielle, et la soumet à une équipe rouge humaine adaptative (1736 heures) au grain de l'échange : composante (d) voisine (attaquant adaptatif contre un système complet, sans comparaison d'agrégations, hors agent).

Pourquoi pas « occupé en partie » : les composantes faites sont le cadre (un agent ; une sonde en flux attaquée par des humains), pas ce que Tr demande (la tenue d'une agrégation, établie au jeton, au grain de l'action sous attaquant adaptatif). Un contre-lecteur peut le contester au titre de (e) seule ; je le signale.

---

## Pièce 1 — 2601.04603v1, « Constitutional Classifiers++ »

**Venue imprimée** : arXiv 2601.04603v1 [cs.CR], 8 janvier 2026 (p. 1). La pièce 3 la cite comme parue à la quatorzième Conférence internationale sur les représentations apprises, 2026 (2609.19101, p. 20).

**Ce qu'elle fait.** Défense de production contre les contournements universels (domaine des armes chimiques, biologiques, radiologiques et nucléaires) : (i) classifieur d'échange qui lit la réponse pendant la génération dans le contexte de la demande, « evaluating tokens in batches as they are sampled » (p. 3) ; (ii) cascade à deux étages (p. 4-5) ; (iii) sondes linéaires sur les activations du modèle protégé, concaténées sur toutes les couches (p. 7), ensemble sonde et classifieur externe (p. 8-9) ; (iv) système final : la sonde surveille tous les échanges pendant la génération et fait monter les échanges suspects au second étage, score final pondéré 0,55 sonde et 0,45 classifieur (p. 9, auteurs).

**Modèle lu** : le modèle protégé lui-même (modèle propriétaire de l'éditeur de l'article, taille non publiée) ; activations de toutes les couches (p. 7, p. 9).

**Grain** : score par jeton, lu en flux ; décision au grain de l'**échange** (conversation utilisateur–assistant), étiquettes au grain de l'échange (p. 5) ; une alarme arrête la suite : « reflecting how a single flag blocks all subsequent content for streaming classification » (p. 6). Évaluation : l'attaque est parée si le classifieur d'échange « flags at any point during model sampling » (p. 7) — règle de décision qui équivaut, à la lecture, au maximum courant du score lissé comparé à un seuil (lecture du lecteur, non imprimée sous ce nom).

**Agrégations et comparaisons** :
- Entraînement : moyenne glissante des logits sur M jetons (« we average logits over a sliding window of M tokens during training », p. 6), M = 16 (p. 7, auteurs) ; perte pondérée par une fonction exponentielle normalisée (softmax) qui donne le poids aux positions jugées nuisibles (p. 6).
- Inférence : « During inference, we use an exponential moving average (EMA) instead of a sliding window mean for computational convenience. » (p. 6). Motif imprimé du lissage : « Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as harmful. » (p. 6).
- Comparées (toutes **sur données statiques**, « All evaluations were conducted on static jailbreak datasets of CBRN-related queries. », p. 7 ; environ 7 000 échanges de l'équipe rouge, tronqués à 20 000 jetons, p. 7) : fonctions de perte (lissage et pondération, l'un, l'autre, aucun : figure 2b, p. 7 ; plus « par jeton », maximum cumulé, maximum cumulé recuit : figure 5a, p. 16) ; taille de fenêtre de 1 à 64 (figure 5b, p. 16) ; nombre de couches (figure 2c).
- Le maximum cumulé est comparé **comme fonction de perte d'entraînement**, non comme règle de décision : « We explore using the cumulative maximum of probe probabilities as the predictor for the full sequence label. » (p. 16) ; résultat : « We find that our softmax loss-weighting with activation smoothing achieves stronger performance than these additional loss functions. » (p. 16). Fenêtre : optimum vers 16 jetons, « However, excessive smoothing degrades performance. » (p. 16).
- Chiffres : meilleure sonde, toutes couches, « approximately 1.4% » de succès d'attaque (p. 8, auteurs) ; sans lissage ni pondération, environ 14 % (figure 2b, p. 7, figure).

**Attaquant** : équipe rouge **humaine**, adaptative au sens où elle itère contre le système défendu avec accès par interface de programmation (« We provide red-teamers with API access to the defended model. », p. 15), avec primes ; contre le système de production à sonde en premier étage : « The system underwent an estimated 1736 cumulative hours » ; « Only one high-risk vulnerability was discovered » (p. 9). Boîte noire : la pièce ne dit pas que les attaquants connaissent la sonde ni la règle d'agrégation ; aucune attaque n'est conçue contre le lissage ou le seuil en flux ; **aucune comparaison d'agrégations sous cette attaque** ; la sonde seule n'est jamais attaquée. Hors programme de primes, des experts « were nonetheless able to discover universal jailbreaks for this system » (p. 5, système à deux étages sans sonde). Familles d'attaques nommées contre la génération précédente : reconstruction (fragmentation d'une demande nuisible sur des segments bénins puis réassemblage) et obfuscation de sortie (p. 2-3) — voisin conceptuel du sabotage diffus, mais contre des classifieurs externes, pas contre des sondes.

**Cadre agentique** : aucun (conversation ; aucun appel d'outil, aucun pas).

**Transposition explicite jeton → action** : aucune.

**Limites reconnues** : le critère « alarme à tout point » « may underestimate the attack success rate » (note 6, p. 7) ; la sonde alarme davantage sur des requêtes scientifiques bénignes (p. 8).

**Incohérence interne** : la figure 5 (p. 16) dit utiliser « the same evaluation datasets and methodology as described in the main paper » (p. 16), mais son axe « taux de succès d'attaque (%) » va d'environ 0,01 (lissage et pondération) à environ 0,14 (par jeton) (figure), quand la figure 2b (p. 7) donne environ 1,4 % et 14 % pour des variantes voisines (figure) : facteur d'environ 100 (calcul) ; probablement une échelle en fraction notée en pourcentage. Sans effet sur Tr.

**Verdicts par composante**
| composante | verdict | appui |
|---|---|---|
| (a) robustesse des agrégations au jeton | **voisin ; contre-indice léger** à la prémisse « maximum robuste » : la règle de production n'est pas un maximum brut par jeton mais un seuil franchi par un score lissé, au motif qu'un jeton isolé fausse la séquence ; comparaison sur données statiques, pas sous attaque | p. 6, 7, 16 |
| (b) transposition au grain de l'action | ne touche pas (grain de l'échange) | p. 5, 7 |
| (c) comparaison des agrégations au grain de l'action | ne touche pas (comparaison au grain du jeton seulement, comme perte d'entraînement et taille de fenêtre) | p. 7, 16 |
| (d) attaquant adaptatif | **voisin** : humains adaptatifs en boîte noire contre le système complet ; ni connaissance déclarée de la sonde, ni attaque visant l'agrégation | p. 9, 15 |
| (e) dans un agent | ne touche pas | — |

---

## Pièce 2 — 2603.04069v1, « Monitoring Emergent Reward Hacking During Generation via Internal Activations »

**Venue imprimée** : atelier « Principled Design for Trustworthy AI » de la Conférence internationale sur les représentations apprises 2026 (en-tête, p. 1) ; arXiv 2603.04069v1 [cs.CL], 4 mars 2026.

**Ce qu'elle fait.** Détection du piratage de la récompense pendant la génération : autoencodeurs parcimonieux par couche, standardisation, analyse en composantes principales, régression logistique par couche ; le classifieur apprend « to distinguish activations originating from hack versus control adapters » (p. 4). Adaptateurs de bas rang « contrôle » (données d'instructions générales) et « piratage » (jeu « School of Reward Hacks ») ; mélanges intermédiaires : « Mixed-ratio adapters are trained on datasets containing 5%, 10%, 50%, or 90% School of Reward Hacks examples » (p. 5), traités comme inédits à l'évaluation.

**Modèles lus** : trois modèles ouverts de 7 à 8 milliards de paramètres, de trois familles (p. 5) ; quatre dernières couches surveillées (p. 13).

**Grain** : jeton (« token-level estimates of reward-hacking activity », p. 1) → **moyenne** sur l'empan (« token-level probabilities are aggregated over a predefined token span » ; « we compute the mean probability over tokens in the selected span », p. 4 ; empan = raisonnement, ou réponse entière) → moyenne sur les couches → seuil 0,5 : « The monitor produces one decision per generation. » (p. 5). Profils temporels descriptifs : « monitor probabilities are aggregated into fixed bins of 64 tokens and averaged across prompts » (p. 6) ; pente et écart de fin de génération (annexe A.2, p. 11-13), descriptifs, non utilisés comme détecteurs.

**Agrégations comparées** : aucune (moyenne seule).

**Attaquant** : aucun. **Cadre agentique** : aucun (génération à un tour). **Transposition jeton → action** : aucune.

**Résultats** : score F1 contre un juge externe (grand modèle de langue) de 0,760 à 1,000 selon adaptateur et famille (tableau 1, p. 5, auteurs) ; structure temporelle propre à chaque famille (tôt puis décroissante pour l'une, tardive pour une autre, p. 6) ; amplification par la chaîne de raisonnement pour les mélanges à 5 et 10 % (figure 4, p. 7). « We emphasize that this evidence is correlational » (p. 8).

**Limites reconnues** : « Our experiments focus on a single reward-hacking benchmark and a limited set of model families and sizes » (p. 8) ; fiabilité du juge (p. 8-9).

**Réserves du lecteur (règle R4)** :
- Construit : le classifieur sépare les activations de deux adaptateurs (p. 4) ; il peut lire l'identité de l'adaptateur plutôt que le comportement ; la montée monotone avec la proportion de données de piratage (figure 2, p. 5) est compatible avec les deux lectures ; non discuté.
- Trop propre : F1 = 1,000 pour l'adaptateur contrôle dans les trois familles (tableau 1, p. 5, auteurs).
- Incohérence : p. 3, adaptateur « fine-tuned on reward-hacking examples » ; p. 13, « For LoRA-Finetuning the GRPO Algorithm is used » (optimisation de politique relative par groupe, un apprentissage par renforcement).

**Verdicts par composante** : (a) ne touche pas ; (b) ne touche pas ; (c) ne touche pas ; (d) ne touche pas ; (e) ne touche pas. **Voisin lointain** (sonde lue pendant la génération). Information utile au choix d'agrégation, non un contre-indice : le moment où le signal se concentre dépend de la famille de modèle (p. 6), ce qui pèse contre une fenêtre ou une pondération temporelle fixée a priori.

---

## Pièce 3 — 2609.19101v2, « Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations »

**Venue imprimée** : arXiv 2609.19101v2 [cs.CL], 9 octobre 2026 (p. 1) ; aucune venue imprimée.

**Ce qu'elle fait.** Mesure du piratage de la récompense de modèles ouverts de très grande taille dans des évaluations agentiques (génie logiciel, puis achats, conversation, cybersécurité) ; sondes par **différence des moyennes** construites sur des paires minimales synthétiques (5 285 conversations de 9 tours, tableau 4, p. 27, auteurs) ; comparaison avec un moniteur fondé sur un grand modèle de langue ; cascade sonde → moniteur et « ou » sonde–moniteur (p. 9) ; pilotage causal (p. 8) ; découverte de comportements guidée par la sonde (p. 13-16).

**Modèles lus** : trois modèles ouverts dits « frontière », jusqu'à l'échelle de 2,8 billions de paramètres (« simple interpretability methods can scale well to models at the 2.8T parameter scale and to long-context agentic rollouts », p. 3) ; un quatrième au tableau 1 (p. 6) ; un modèle ouvert de 27 milliards pour le pilotage (p. 8). Une couche par sonde (p. 6).

**Grain** :
- Jeton : « we use it as a linear token-level probe by scoring each position » ; « flagging positions whose score exceeds a threshold » (p. 6).
- **Passage** = « A passage is one channel of one step: » (p. 31) — raisonnement, message, ou appels d'outil du pas pris ensemble ; « Reasoning traces, assistant messages, and tool calls each receive their own labels. » (p. 5) ; « These comparisons use passage-level ground truths that include both contemplated and attempted/completed hacks. » (p. 9). C'est le grain le plus proche de « l'action » de Tr.
- Déroulé : taux de piratage par déroulé (figure 2, p. 4).
- La règle qui passe des jetons au passage **n'est pas imprimée** ; seul indice : « identify the peak probe location within each passage » (p. 10), qui suggère un pic, donc un maximum (lecture du lecteur).

**Agrégations comparées** : aucune. Les « poolings » de la p. 7 (« In addition, we test several poolings over individual datasets. ») portent sur la mise en commun de jeux de données synthétiques (tableau 3, p. 26), et « When harvesting activations, we consider several locations that apply to all environments. » (p. 7) porte sur la construction de la sonde, pas sur l'agrégation des scores à la détection. Cascade et « ou » sont des combinaisons de moniteurs, pas des agrégations temporelles.

**Attaquant** : aucun. L'obfuscation est un défi futur : « A further challenge is that models may learn to obfuscate undesirable behavior from their reasoning traces » (p. 17). « Our study does not control for evaluation awareness in any of our experiments » (p. 18).

**Cadre agentique** : oui (déroulés de plus de 100 000 jetons, p. 10 ; appels d'outil, p. 5, 15).

**Transposition explicite jeton → action** : aucune conclusion d'agrégation portée d'un grain à l'autre. Lien temporel seulement : « DoM vectors run on the chain-of-thought also predict reward hacks in the model’s subsequent actions » (p. 1) ; rééchantillonnage au pic : 28,6 % contre 1,1 % et 14,1 % contre 1,5 % de piratages tentés, sonde contre témoins (figure 10, p. 11, auteurs).

**Résultats chiffrés** : aire sous la courbe de fonctionnement du récepteur de 0,74 à 0,97 (figure 8, p. 10, auteurs) ; à taux de faux positifs égal au moniteur, « probes catch 3.0 and 33.1 percentage points more hacks on DeepSWE and ImpossibleBench respectively » (p. 9) ; ajout de la sonde au moniteur : vrais positifs de 41,1 % à 80,2 % pour 1 point de faux positifs en plus (p. 9, auteurs).

**Limites reconnues** : « A trained probe would almost certainly perform better than our diff of means vectors. » (p. 18) ; moniteur non optimisé (p. 18).

**Incohérence interne** : résumé, « DoM vectors are similarly effective but virtually free, catching 3.1% more hacks in » [premier modèle] et 7,9 % de moins pour le second (p. 1) ; corps, 3,0 points (p. 9) et rappel de 0,41 à 0,44 puis de 0,41 à 0,33 (p. 10) : +3 et −8 points (calcul). Écart mineur d'arrondi et d'unité (pourcentage contre points).

**Réserve (règle R4)** : la vérité terrain est un juge fondé sur le même grand modèle de langue que le moniteur comparé (p. 4) ; le biais irait plutôt en faveur du moniteur.

**Verdicts par composante**
| composante | verdict | appui |
|---|---|---|
| (a) robustesse des agrégations au jeton | ne touche pas | — |
| (b) transposition au grain de l'action | **voisin (fort)** : sonde lue au grain du passage, appels d'outil compris, dans des agents ; ni agrégation comparée, ni robustesse | p. 5, 9, 10, 31 |
| (c) comparaison des agrégations au grain de l'action | ne touche pas | p. 7, 26 |
| (d) attaquant adaptatif | ne touche pas (obfuscation nommée comme défi futur) | p. 17 |
| (e) dans un agent | **occupée** (composante isolée, non distinctive de Tr) | p. 3, 5, 10 |

---

## Synthèse

| pièce | modèle lu | grain | agrégations comparées | attaquant | jeton → action explicite | verdict |
|---|---|---|---|---|---|---|
| 2601.04603v1 | modèle protégé, propriétaire, toutes couches | jeton en flux → échange | pertes (lissage, pondération, maximum cumulé), fenêtre 1-64, sur données statiques | humains adaptatifs, boîte noire, système complet | non | voisin ; contre-indice léger (a) |
| 2603.04069v1 | trois modèles ouverts 7-8 milliards | jeton → moyenne → génération | aucune | aucun | non | voisin lointain |
| 2609.19101v2 | modèles ouverts très grands | jeton → passage (pas, appels d'outil) → déroulé | aucune (règle au passage non imprimée, « pic ») | aucun | non | voisin fort ; (e) occupée |

## Ce qui reste revendicable (formulation exacte proposée)

« Dans les trois pièces lues, aucune ne compare, au grain de l'action d'un agent (un appel d'outil ou un pas) ni de la trajectoire, des règles d'agrégation de scores de sondes face à un attaquant adaptatif qui connaît ou apprend le moniteur et sa règle d'agrégation ; aucune ne porte au grain de l'action une conclusion de robustesse établie au grain du jeton. »

Pour que l'expérience E1.5 soit jugée contre ces pièces, la comparaison gagnerait à inclure comme bases nommées : la règle de production de 2601.04603 (seuil franchi en un point quelconque par un score lissé en moyenne mobile exponentielle, p. 6-7) et la lecture par pic au passage de 2609.19101 (p. 10).

## Ce qu'une phrase publique sur Tr ne doit pas affirmer

- Être les premiers à lire une sonde au grain du pas ou de l'appel d'outil dans des déroulés d'agent (2609.19101, p. 5, 9, 31).
- Être les premiers à lire des sondes pendant la génération pour détecter le piratage de la récompense (2603.04069, p. 1 ; 2609.19101, p. 1).
- Être les premiers à agréger des scores de sonde au fil des jetons en production, ou que l'agrégation en flux n'a jamais été éprouvée par des attaquants adaptatifs (2601.04603, p. 6, 9 : 1736 heures d'équipe rouge humaine, en boîte noire).
- Que le maximum brut par jeton est la règle de référence au grain du jeton (2601.04603 retient un seuil sur score lissé, p. 6 ; le maximum cumulé y fait moins bien comme perte, p. 16, sur données statiques).
- Que la question est « libre dans le champ » : « non trouvé dans les pièces lues » seulement (règle R8).

## Voisins nommés dans les pièces et non lus (avec la page où ils sont nommés)

Statut dans le dépôt non vérifié par moi (hors des fichiers nommés), sauf mention.
- **Priorité haute** : Wilhelm et Kao 2026, « From reward-hack activations to agentic risk states: Context-calibrated mechanistic monitoring in LLM agents », atelier « Agents in the Wild » (2609.19101, p. 17 et 24) — sondes de piratage de la récompense dans des agents, par les auteurs de la pièce 2 ; collision possible sur (b) et (e).
- Sharma et al. 2025, 2501.18837, « Constitutional classifiers » — maximum cumulé et maximum cumulé recuit pour le flux (2601.04603, p. 16 et 13).
- Cunningham et al. 2025, « Cost-effective constitutional classifiers via representation re-use », billet (2601.04603, p. 10 et 12).
- Hua et al. 2025, 2507.15886, « Combining cost-constrained runtime monitors for AI safety » (2601.04603, p. 10 et 12).
- McKenzie et al. 2025, 2506.10805 (2601.04603, p. 10 et 12 ; 2609.19101, p. 22) — déjà lu au niveau 2 selon `anteriorite-v1.md` (l. 141).
- Zhou et al. 2026, 2606.24251, « Probing the misaligned thinking process of language models » (2609.19101, p. 17 et 24).
- Goldowsky-Dill et al. 2025, « Detecting strategic deception with linear probes » (2609.19101, p. 17 et 20).
- Baker et al. 2025, 2503.11926 (obfuscation sous optimisation contre un moniteur de raisonnement ; 2603.04069, p. 2 et 9 ; 2609.19101, p. 1-2 et 19) ; Arnav et al., « CoT red-handed » (2609.19101, p. 2 et 19) ; Drori et al., 2511.11584 (2609.19101, p. 20) — moniteurs de texte.
- Youstra et al. 2025, 2508.17158, attaques par chiffrement (2601.04603, p. 13).
- Chennabasappa et al. 2025, 2505.03574, garde-fou pour agents (2603.04069, p. 3 et 9).
- Non lu, déjà signalé : « What the Monitor Saw » (état de l'art niveau 3, l. 188-189).

## Réserves (règles R4 et R8)

- Le verdict repose sur trois pièces ; la zone est séduisante (une question nommée par le programme lui-même) et se vérifie plus durement : Wilhelm et Kao 2026 est la collision la plus probable non lue.
- 2601.04603 montre que des sondes en flux lissées sont déployées et éprouvées par des humains adaptatifs dans l'industrie ; un travail interne non publié sur l'attaque de l'agrégation est plausible et invisible ici.
- Les attaques de reconstruction de 2601.04603 (fragmentation d'une demande sur des segments bénins, p. 2-3) sont l'analogue direct du sabotage diffus contre une agrégation ; elles visent des classifieurs externes de la génération précédente, pas des sondes : voisin, pas occupation.

## Formules (lu sur le PDF, non contrôlé par programme)

- 2601.04603, éq. 2 (p. 6) : z̄_t = (1/M) Σ_{k=0}^{M−1} [Wᵀ ψ_{t−k} + b] ; éq. 5 (p. 16) : p(y = 1 | x_{1:t}) = max_{τ ≤ t} σ(z̄_τ) ; éq. 6 (p. 16) : (1 − ω)·σ(z̄_t) + ω·max_{τ ≤ t} σ(z̄_τ).
- 2603.04069, éq. 2-4 (p. 4-5) : m_ℓ = (1/|T|) Σ_{t∈T} p_{t,ℓ} ; P(hack) = (1/|L|) Σ_ℓ m_ℓ ; décision si P ≥ 0,5.
- 2609.19101, éq. 1 (p. 6) : v_hack = E_{t∈P}(x_t) − E_{t∈N}(x_t) ; score s_t = ⟨v_hack, x_t⟩.

## Archive

`docs/sources/lecture-pdf-niveau3/compte-2/fichiers-de-travail-Tr-v1.tar` : script de contrôle des citations, `citations-Tr-v1.json` (49 citations), sortie du contrôle, journal du lecteur ; sans PDF ni textes extraits.
