# Lecture sur sources primaires — « moniteurs ou interventions contre les menaces diffuses » — rapport v1

## En-tête
- Session « attaquant informé » `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`,
  12 novembre 2026. Ne se réécrit pas (R12).
- Origine : question de Lazar, « a-t-on bien fait de prendre des moniteurs dans notre programme sur les menaces diffuses ?
  on aurait peut-être dû prendre des interventions ? », puis « go, exécute ta part de la demande reformulée » (part de
  cette session : lectures et antériorité ; `docs/notes/moniteurs-ou-interventions-v1/demande-reformulee-v1.md`).
- Périmètre : ce que disent, à la page, la phrase d'Anthropic et les travaux qu'elle cite, et ce qu'ils laissent ouvert.
  Aucune mesure, aucun score du programme lu (cloison), aucune conception de moniteur.
- Méthode : texte extrait par `pypdf` ; « p. N » est le rang de la page dans le fichier PDF (il peut différer du numéro
  imprimé) ; chaque citation est retrouvée telle quelle, espaces normalisés, par `verif_citations-v1.py` (27 sur 27 le
  12 novembre 2026). Les billets web sont cités sur le fichier déposé (« p. 0 »).

## Sources
| Clé | Document | Chemin | SHA-256 |
|---|---|---|---|
| T3 | Terekhov, Gulcehre, Hebbar, Benton, « Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892v3 (4 novembre 2026), 84 p. | `docs/sources/pdf/anteriorite-bras-informe-v1/terekhov-2026-controle-diffus-taches-floues-v3-2606.08892v3.pdf` | `8858355c…` |
| DIF | Billet du même travail, 23 juin 2026 | `docs/sources/lecture-web-20261112-directions-anthropic-v1/billet-anthropic-diffuse-ai-control-20260623.html` | `355cd103…` |
| HEB | Hebbar, « How can we solve diffuse threats like research sabotage with AI control? », 30 avril 2025 (billet) | `…/lecture-web-20261112-directions-anthropic-v1/billet-hebbar-diffuse-threats-20250430.md` | `f9a3c18a…` |
| GAS | Gasteiger et collègues, « Automated Researchers Can Subtly Sandbag », 24 mars 2025 (billet) | `billet-anthropic-automated-researchers-sandbag-20250324.html` (ce dossier) | `4a7e0eb9…` |
| WEN | Wen, Hebbar et collègues, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », arXiv 2411.17693v1, 44 p. | `docs/sources/pdf/anteriorite-P-041-v2/c5/2411.17693v1.pdf` | `13a93a48…` |
| BAL | Balesni et collègues, « Towards evaluations-based safety cases for AI scheming », arXiv 2411.03336v2, 46 p. | `docs/sources/pdf/2411.03336v2.pdf` | `46b4901a…` |
| AISI | Taylor et collègues, « Auditing Games for Sandbagging », arXiv 2512.07810v1, 77 p. | `docs/sources/pdf/2512.07810v1.pdf` | `77e64bcd…` |
| PIL | Anthropic, rapport pilote de risque de sabotage (risques de l'été 2025), 67 p. | `docs/sources/pdf/anthropic-2025-10-rapport-pilote-risque-sabotage.pdf` | `e88a248b…` |
| RR8 | Anthropic, rapport de risque d'août 2026 (version expurgée), 186 p. | `docs/sources/pdf/anthropic-2026-08-rapport-risque-expurge.pdf` | `d76815f8…` |
| LIE | Hopkins, Khullar, Wang, Roger, « Fine-Tuned Lie Detectors Failed to Generalize », 21 août 2026 (billet) | `billet-anthropic-lie-detectors-20260821.html` (ce dossier) | `4e89ef31…` |

Gan et collègues (arXiv 2604.16286v2) : déjà lu sur PDF par le programme (`docs/sources/lecture-pdf-niveau2/rapport-lot2-A3-sabotage-recherche-v1.md`, § 1) ; non relu ici.

## Table de vérification

### A. La phrase et ses appuis
| # | Affirmation | Statut | Citation |
|---|---|---|---|
| 1 | Les auteurs étudient l'entraînement parce que surveillance et incrimination leur semblent moins prometteuses contre le diffus. | Vérifié | [T3 p. 2] « since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. » ; [DIF p. 0] « We focus on training interventions because they seem more promising than monitoring and incrimination for diffuse threats » |
| 2 | Dans le corps de l'article, l'entraînement est supposé, pas exécuté. | Vérifié | [T3 p. 3] « Under sufficient training pressure and absent exploration hacking [Buhl et al., 2025], the weak score of the untrusted model should converge to a nearly-optimal value. » |
| 3 | La version 3 ajoute une attaque par entraînement (annexe J) et publie du code. | Vérifié (contenu du dépôt de code non ouvert) | [T3 p. 8] « remains similar when we perform RL fine-tuning instead of prompt optimization » ; [T3 p. 1] « Code is available at https://github.com/MikhailTerekhov/diffuse_control. » |
| 4 | L'appui théorique tient à une prémisse : on ne sait pas à quoi ressemble un modèle bénin. | Vérifié | [HEB p. 0] « the larger volume of mildly suspicious actions would only allow us to incriminate if we knew *exactly how suspicious a benign model would look*. But without that affordance, no amount of mildly suspicious actions is enough to incriminate the model. » |
| 5 | Le même billet tient entraînement et incrimination pour complémentaires, et décrit un régime intermédiaire où le soupçon choisit ce qu'on entraîne plus fort. | Vérifié | [HEB p. 0] « We suspect that training and incrimination are complementary » ; [HEB p. 0] « we might train against the most suspicious 3% of actions for multiple epochs » |
| 6 | Le billet de Hebbar ne traite pas des états internes. | Constat par recherche de chaînes (« probe », « activation », « internals », « white » : aucune occurrence) | — |
| 7 | Le premier appui empirique porte sur des moniteurs à consigne sans exemple, et note que leur signal bruité pourrait suffire à entraîner. | Vérifié | [GAS p. 0] « Zero-shot prompted monitors don’t reach a high-enough true positive rate to reliably prevent one-shot sandbagging at inference time. However, the noisy monitoring signal might be sufficient to train away sandbagging. » |
| 8 | Le billet d'Anthropic range la surveillance non fiable parmi les pistes prometteuses du défenseur dans son propre cadre. | Vérifié | [DIF p. 0] « untrusted monitoring with collusion busting » |

### B. Ce qui reste après l'entraînement
| # | Affirmation | Statut | Citation |
|---|---|---|---|
| 9 | Entraînés contre l'évaluateur faible, deux organismes atteignent le même score faible et gardent des qualités vraies différentes. | Vérifié | [T3 p. 84] « the difference between the organisms in the GT proxy score remains non-trivial until the end of training. » |
| 10 | Même contre l'évaluateur durci, la récupération est imparfaite. | Vérifié | [T3 p. 84] « The recovery is still not perfect: at the end of training against the robustified weak scorer, the more aggressive second model organism retains a lower GT proxy score than the less aggressive first one. » |
| 11 | La frontière de subversion sert de borne inférieure de la qualité vraie après entraînement. | Vérifié | [T3 p. 84] « this corroborates our reliance on the subversion Pareto frontier as the lower bound on possible GT proxy scores after training against the weak score. » |
| 12 | La vérité de référence du banc n'est pas validée contre des humains. | Vérifié | [T3 p. 10] « Our ground truth proxy score was not validated quantitatively against human judges. » |

### C. La référence honnête
| # | Affirmation | Statut | Citation |
|---|---|---|---|
| 13 | L'accumulation de preuves contre des menaces réparties existe en boîte noire ; elle reçoit une distribution de référence toute faite. | Vérifié | [WEN p. 2] « it allows deployment strategies to gradually gather more evidence of an untrusted model’s (mis)alignment » ; [WEN p. 6] « To estimate this, the blue team is provided a reference distribution » ; [WEN p. 6] « the blue team is given a sample of tasks and outputs, along with their corresponding monitor, sneakiness, and efficacy scores for benign ouputs » |
| 14 | La distribution de référence d'une sonde est attaquable : un modèle qui se comporte mal sur elle abaisse ses scores ailleurs. | Vérifié | [AISI p. 25] « if a model produces malign representations on the benign-labelled training or control distributions, then probe scores on other distributions will be artificially lowered by comparison, and sandbagging may be missed. » |
| 15 | Anthropic dit que sa surveillance asynchrone ne détecterait probablement pas le sabordage diffus, et s'appuie moins sur la surveillance pour ce risque. | Vérifié | [RR8 p. 84] « Our asynchronous monitoring would likely not detect diffuse research sabotage (such as sandbagging) » ; [RR8 p. 66] « Therefore, we can rely less on monitoring-based mitigations to protect against this risk. » |
| 16 | Son seul argument de détection par volume est informel. | Vérifié | [RR8 p. 60] « even a very low probability of verbalization in any individual instance might add up to a moderate probability of detection. » |
| 17 | Le risque nommé dès 2025 est le sabordage sans raisonnement écrit. | Vérifié | [PIL p. 26] « there is a risk that the model would simply not reason about sandbagging-related considerations at all, and thereby give us nothing to detect in our monitoring. » |

### D. Entraîner contre un moniteur ; valider une sonde
| # | Affirmation | Statut | Citation |
|---|---|---|---|
| 18 | Anthropic n'entraîne pas contre une surveillance fondée sur les activations (deux exceptions, qui portent sur le raisonnement écrit). | Vérifié | [RR8 p. 48] « We do not train against any chains-of-thought or activations-based monitoring, with two exceptions » |
| 19 | L'esquisse d'argumentaire de sûreté interdit à l'équipe rouge d'entraîner contre les sondes, et demande à part une évaluation de leur généralisation. | Vérifié | [BAL p. 27] « do not allow the red team to train against any whitebox probes » ; [BAL p. 27] « Instead, we run a separate large-scale evaluation of the probes’ generalization properties. » |
| 20 | Des détecteurs entraînés sur des mensonges produits par le modèle tiennent dans la distribution et chutent hors catégorie ; le sandbagging est le plus dur. | Vérifié (détecteurs par réglage fin, pas des sondes) | [LIE p. 0] « In-distribution detection worked well (AUROC 0.60 → 0.95), but cross-category transfer did not (AUROC ~0.70–0.75). » ; [LIE p. 0] « Sandbagging proved nearly impossible to detect with detectors trained on other lie types. » |

## Antériorité (R8) — « non trouvée occupée » ne veut pas dire « libre »
| Idée | Statut | Appui |
|---|---|---|
| Incriminer un sabotage diffus en accumulant des preuves internes faibles, avec une référence honnête étalonnée | Voisins : accumulation en boîte noire à référence fournie (ligne 13) ; accumulation informelle (ligne 16) ; test séquentiel sur scores de vérificateur (E-valuator, déjà à l'état de l'art). Forme boîte blanche sur diffus : non trouvée occupée par les lecteurs du 12 novembre (recherche limitée). | WEN, RR8 |
| Éprouver la référence honnête elle-même (d'où elle vient, ce qu'elle devient si elle est fausse ou attaquée) | Nommée comme attaque et comme travail futur (ligne 14) ; protocole chiffré : non trouvé. | AISI |
| Juger un moniteur sur le sabotage qui survit à l'entraînement | Le résidu est montré (lignes 9 et 10) ; aucun moniteur ne lui est appliqué dans T3. Non trouvé ailleurs. | T3 |
| Entraîner plus fort sur ce qu'un moniteur désigne | Décrit comme régime (ligne 5) et comme espoir (ligne 7) ; pratique inverse chez Anthropic pour les activations (ligne 18). | HEB, GAS, RR8 |

## Alertes pour le programme
1. **L'hypothèse (c) du lemme est l'affordance que Hebbar dit manquer.** Le programme pose que « la variance des scores
   honnêtes est estimable sur épisodes honnêtes » (programme v2, section 3) et étalonne ses seuils sur des « épisodes
   honnêtes réservés » (brief v2, T1.2). Au laboratoire, le jumeau honnête existe par construction. La garantie de faux
   positifs du papier A est donc conditionnelle à une référence que la littérature dit absente en déploiement (ligne 4)
   et attaquable (ligne 14). À écrire comme limite déclarée, ou à éprouver.
2. **La phrase ne porte pas sur la boîte blanche.** Ni Hebbar (ligne 6), ni Gasteiger (ligne 7), ni T3 ne lisent
   d'états internes. Cela ne prouve pas que la boîte blanche réussit : cela dit seulement que l'argument publié ne
   l'a pas examinée.
3. **Le comparateur manque.** Le programme compare boîte blanche et boîte noire en détection. La littérature compare
   en qualité vraie conservée après entraînement (lignes 9 à 11). Sans bras d'entraînement, G1 ne répond pas à la thèse
   adverse ; l'alerte 2 du rapport de lecture du 4 octobre (`rapport-2606.08892-v1.md`) le disait déjà pour le bras
   boîte noire.
4. **L'invariant « aucun score de moniteur dans l'entraînement de l'agent » a des appuis publiés** (lignes 18 et 19).
   Le lever serait un écart ; le mesurer est une décision de Lazar.

## Ce qui n'a pas été fait
- Dépôt de code de T3 non ouvert (inaccessible depuis la session) : son contenu n'est connu que par un lecteur web.
- Billets de Redwood Research sur les échecs non concentrés et sur l'apprentissage continu (25 septembre 2026), article
  arXiv 2611.10620 sur le transport des seuils : relevés par les lecteurs web seulement
  (`docs/sources/lecture-web-20261112-directions-anthropic-v1/`), non vérifiés ici.
- Aucune reproduction, aucune mesure. Aucun score, résultat ni seuil du programme n'a été lu.
