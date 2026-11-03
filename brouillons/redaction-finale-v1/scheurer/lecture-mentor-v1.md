# Lecture en mentor — réponse à Jérémy Scheurer (tendance d'échelle) — v1

Lecteur neuf, 3 novembre 2026, de 15:30:18 à 15:46 (temps universel, `date -u`). Je n'ai écrit aucune version des réponses de Lazar. Consigne scellée `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/lecteur-mentor-scheurer-v1.md`, sha256 `d2abf384…f107ea`, vérifiée avant lecture.

## Ce que j'ai lu

| Pièce | Empreinte | État |
|---|---|---|
| `brouillons/redaction-finale-v1/scheurer/reponse-v1.md` | `1219a694…784e937` | conforme à la consigne |
| texte seul de la réponse (lignes 1 à 9, sans le pied) | `12773455…87baf78` | recalculé par mon script, égal au pied |
| question : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, lignes 109 à 121 | fichier `57393598…f7b5c6` | lue mot à mot |
| `…/lecture-approfondie-v1/rapport-scheurer-v1.md` ; `…/recoupement-v1.md` | — ; `bea573aa…e0a` (= compagnon) | lus |
| `brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md` ; `…/scheurer/note-piste-v1.md` ; `…/scheurer/registre-affirmations-v1.md` | — ; `63148b5f…fc030` (conforme) ; — | lus |
| `/home/claude/scratch/soir-rapport/scheurer/classement-D/classement-v1.md` | — | lu (drapeaux, § 5) |
| R7 public : clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law/`, `results/R7/README.md` | `2dd0790c…5d032a` | lu entier |
| ideation-organism : clone `/home/claude/ideation-organism/`, branche `main` (`faff48b`), pages T0.3 et P3 lues par `git show main:…` | T0.3 `04ce0afc…d8ba0` ; P3 `2485d509…bf88` | lues entières |

**Pages en ligne** (toutes par `WebFetch`, donc au niveau transcription : un modèle intermédiaire rend la page ; aucun chiffre ci-dessous n'est opposable au sens de la règle R7 du dépôt) :
- arXiv 2605.12366 (résumé, puis fichier PDF) ; 2510.09462v2 (PDF) ; 2509.15541v1 (PDF) ; 2412.04984 (PDF) ; 2506.05296 (page de résumé, qui contenait le corps).
- Apollo Research : « Apollo Update May 2026 » (https://www.apolloresearch.ai/blog/apollo-update-may-2026/) ; page « Monitoring » (https://www.apolloresearch.ai/monitoring).

**Accès refusés, non contournés** : `curl` vers `arxiv.org` refusé par le mandataire (403, refus de politique, aussi au journal du mandataire) : aucun PDF empreinté. `WebFetch` de `https://arxiv.org/html/2605.12366v1` bloqué (« PROVENANCE_REQUIRED », demande d'autorisation restée sans réponse) : non relancé ; j'ai pris l'adresse du PDF donnée par une recherche. Pour trois PDF, l'outil n'a lu que les 100 000 premiers caractères (2509.15541 : sur 113 209 ; 2510.09462 : sur 106 655 ; 2412.04984 : sur 120 518) ; les passages cherchés y étaient.

## Verdict

1. **Aucun point bloquant.** Limite tenue : 492 mots (blancs), pas de limite écrite, visée 500.
2. **Sept points à corriger**, dont la seule phrase qu'il contredirait : « as Apollo's monitoring does » (le produit phare de son employeur est un moniteur en temps réel). Les corrections proposées tiennent ensemble dans le budget (495 mots).
3. **À ne pas couper** : l'énoncé dans son gabarit, ses deux papiers cités exactement et pour la bonne raison, les trois tests qui tuent, la dernière phrase de portée.

## 1. La phrase qu'il contredirait

| # | Citation | Ce qu'il dirait | Source | Gravité | Correction minimale |
|---|---|---|---|---|---|
| 1.1 | « A trusted open-weight monitor scores the whole transcript, as Apollo's monitoring does. » | « Notre surveillance n'est pas seulement la note de trajectoire entière : Watcher Live bloque action par action, en temps réel. » La phrase laisse aussi entendre que leur moniteur est « trusted open-weight », ce que leurs pages ne disent pas. | Mise à jour du 13 mai 2026 : « Watcher Live is a real-time monitor that identifies and blocks undesirable actions or steers the agent back on track » ; page « Monitoring » : billet du 13 juillet 2026 (« Red-teaming auto mode », un système qui « decides whether an agent's next action should be allowed or blocked ») ; la note de trajectoire entière vient d'**un** billet, celui du 23 juillet 2026 (« What makes a good monitoring prompt? » : « We use a 1-10 severity scale and full-trajectory scoring, as opposed to real-time binary prompts »). | à corriger | « …scores the whole transcript, like Apollo's full-trajectory scoring. » (même nombre de mots) |
| 1.2 | « tests one way detection could get harder, as Apollo's May update expects » | Il nuancerait : « notre raison est la conscience situationnelle », et le plan gelé l'exclut par construction. | Mise à jour du 13 mai 2026 : « Detection and correction of misalignment will also get harder, mainly because models will have stronger situational awareness ». | mineur | Rien : « one way » couvre l'écart, et la dernière phrase dit la portée. |

**Vérifié, il ne le contredirait pas** : 2509.15541 § 6.1, 2412.04984 § 4, 2510.09462, Control Tax § 2.3, « about $3 of GPU » (détail au point 2).

## 2. Affirmations plus fortes que leur preuve

| # | Citation | Ce que dit la source | Gravité | Correction minimale |
|---|---|---|---|---|
| 2.1 | « Frontier monitors miss dangerous actions 2× to 30× more often after 800K tokens of benign activity (arXiv 2605.12366) » | **Le chiffre 2× à 30× n'est que dans le résumé** : « on a dataset that requires identifying when a coding agent takes a subtly dangerous action, Opus 4.6, GPT 5.4, and Gemini 3.1 miss these actions 2× to 30× more often… ». Dans le corps : aucune phrase ne donne 2× à 30× ni de rapport par modèle (figure 2, p. 4 : barres dont les valeurs ne sont pas dans le texte extrait) ; introduction, p. 2 : « recall decreases from 98.6% to 88% when 800k tokens of benign actions are prepended » (Opus 4.6 avec réflexion ; ratés de 1,4 % à 12 %, soit environ 8,6×, calcul de ma part) ; § 3.1 : trois modèles fermés (« Claude Opus 4.6, Gemini 3.1 Pro, and GPT 5.4 Thinking »), aucun moniteur à poids ouverts ; § 3.5 : fausses alertes « below 2% » sur les transcriptions bénignes ; annexe A.2.1 : étiquette binaire. La réponse généralise trois modèles, un banc et des actions **subtiles** en « Frontier monitors miss dangerous actions ». | à corriger | « Three frontier monitors miss subtly dangerous actions… » (+2 mots) |
| 2.2 | « I already have one monitoring trend, by size. … Under a negative note at standard intensity, the deference gain falls with size: −0.19 … » | README de R7 : « **Outcome: C, not the predicted A.** » ; « M3, a size trend in both arms: false. The trend exists under the down note only. » ; sous la note positive, pente −0,019 [−0,098 ; 0,063], et le 72B monte encore à 4,27 sous la note positive forte. Les chiffres cités sont exacts, mais la réponse ne donne que le bras où la pente existe et ne dit pas que la prédiction préenregistrée a échoué. Si l'échelle se lit « plus haut = plus favorable » (bras « critique » et « éloge »), la note positive est celle d'un attaquant qui cherche l'approbation : c'est le bras sans pente. Un lecteur qui ouvre le lien voit l'issue C en tête. | à corriger | « Under a negative note only, at standard intensity… » (+1) ; mieux, « (none under a positive note) » (+5) |
| 2.3 | « False alarms on fresh honest transcripts must hold near 5% at every length: … one calibrated on 1,000 whole honest episodes held 4.6–5.5% » | T0.3 : seuil calibré sur 1 000 épisodes honnêtes « drawn from the same law as the test » ; lecture gelée : « holds its rate when calibration and deployment episodes are exchangeable (instrument check); its robustness to a shift between them is not tested in T0.3 ». Mise à côté de « fresh honest transcripts », la phrase fait croire à une tenue sous décalage, qui n'a pas été testée. | à corriger | « …held 4.6–5.5% when test episodes matched them » (+5) |
| 2.4 | « in my preregistered simulation, a sequential anytime-valid threshold raised 21–35% … under the strongest episode effects » | Chiffres exacts (0,21, 0,35 et 0,24 : les trois plus forts effets d'épisode de la grille). Mais la page dit : « The cells where Ville's rule exceeds α (P8.3) were selected after exploratory runs … it does not predict them blind. » « Preregistered » est vrai de la simulation, pas d'une prédiction à l'aveugle de ces cellules. | mineur | Rien ; la réserve est sur la page liée. |
| 2.5 | « stronger models monitor better (Control Tax, §2.3) » | Exact : § 2.3 « Results », « models conventionally considered stronger perform better at the monitoring task » ; o3-mini, aire sous la courbe de 0,92 à 0,96. | mineur | Donner l'identifiant comme pour les autres : « (Control Tax, arXiv 2506.05296, §2.3) » (+2) |
| 2.6 | « in your anti-scheming paper (arXiv 2509.15541, §6.1), capability RL alone raised verbalized evaluation awareness from 2.0% to 20.5% » | Exact : légende de la figure 15, p. 17 : « (2.0% → 20.5%) after capability-focused RL training on an experimental model without anti-scheming training » ; 20,6 % sur le graphique ; § 6.1 : deux points de contrôle d'**un** modèle expérimental « without any safety or anti-scheming training » (exp-rl-cap Early et Late). Scheurer est sixième auteur. | rien | — |
| 2.7 | « GPT-4.1, the strongest monitor without injection, scored all 375 backdoored samples 0 under injection » | Exact : légende de la figure 2, p. 4 : « assigning a score of 0 to all 375 backdoored code samples » (moniteur GPT-4.1, modèle non fiable GPT-5, banc APPS, pour Automated Programming Progress Standard) ; § 4.1 : « despite GPT-4.1 being the strongest monitor when the injection is not present ». L'injection visait GPT-4.1 (adaptée par DeepSeek-Chat d'un exemple public, § 3.4) ; échelle de 0 à 100 (annexe D). | rien | (facultatif) « a GPT-4.1-specific injection » rendrait « adaptatif » explicite |
| 2.8 | « it inherits the under-elicitation your 2412.04984 (§4) warns about » | Exact sur le fond : § 4 « Limitations », p. 15, « Uncertainty in Capability Elicitation » : « There remains substantial uncertainty about whether we have successfully elicited maximal capabilities from these models. » ; « Our results might therefore underestimate models' scheming capabilities. » Le mot « under-elicitation » n'est pas dans le papier : la paraphrase est fidèle. Scheurer est troisième auteur. | rien | — |
| 2.9 | « R7 (preregistered, about $3 of GPU) » | Exact : README de R7, l. 12, « Cost: GPU about 3 $; no API call. » | rien | — |
| 2.10 | « my first generic white-box probes did not clear their random-probe floor » | Exact : page P3, « For neither main probe is the lower bound of its 97.5% interval … above the 0.95 quantile of its floor of 200 random probes » ; « not detected at this power ». Page publique sur `main` du clone (`resultats/controle-p3-premier-test/`, publiée par le commit `7c7b688`). | voir point 4.2 | — |

## 3. Ce que la question demande et qui manque

La question demande : un concept au choix ; une tendance comme l'horizon du METR (Model Evaluation and Threat Research) ou TastEval ; un énoncé « grows/declines roughly with a factor of X each month/year » ; l'appui de la littérature ; la conscience que c'est dur pour le désalignement ; un plan conçu pour réussir. Tout est couvert, l'énoncé mot pour mot dans son gabarit. Ce qui manque :

| # | Manque | Pourquoi il le verrait | Gravité | Correction minimale |
|---|---|---|---|---|
| 3.1 | La **censure par la fenêtre de contexte**. « Lengths stay inside every monitor's context window; as monitors improve, I add longer transcripts » : les vieux moniteurs ouverts lisent peu de jetons ; un horizon qui ne tombe pas à 50 % dans sa fenêtre est censuré, et X peut suivre la croissance des fenêtres plutôt que la surveillance. | C'est l'objection immédiate à « likely to be successful ». | à corriger | « …keeps headroom (censored at each window). » (+4) |
| 3.2 | Le **gabarit du moniteur gelé**. Martin et Roger (résumé) : la baisse « can be partially mitigated with prompting techniques such as periodic reminders ». « Only the monitor moves » demande que sa consigne soit fixée. | Son propre travail montre que la consigne pèse sur le comportement. | mineur | « A trusted open-weight monitor, prompt frozen, scores… » (+2) |
| 3.3 | Aucun panel nommé (familles, dates), aucune grandeur attendue pour X, aucune puissance (« three or more open-weight families, each at several dates »). | Le METR avait des modèles et une fourchette. | mineur | Nommer deux ou trois familles, si la place le permet. |
| 3.4 | Pas d'environnement nommé pour « n honest, verified steps of agent work » (APPS ne donne qu'une solution d'un seul coup, pas une suite d'étapes). | Il demanderait quel banc agentique. | mineur | — |

## 4. Ce qui le perdrait

| # | Passage | Problème | Gravité | Correction minimale |
|---|---|---|---|---|
| 4.1 | « the deference gain falls with size: −0.19 (95% CI −0.24 to −0.11) per tenfold increase » | « Deference gain » n'est pas défini : le nombre −0,19 n'a pas d'échelle. « Standard intensity » n'est pas défini non plus. | à corriger | « the deference gain (0: ignores the note, 1: adopts it) » (+7) |
| 4.2 | « my first generic white-box probes did not clear their random-probe floor » | Hors sujet dans un plan de moniteurs boîte noire ; « random-probe floor » n'est pas défini ; aucun lien ; l'analogie avec le test de longueur et de style reste implicite. Phrase à relire deux fois. | à corriger | La couper (−11 mots) ; ou dire l'analogie et mettre le lien de P3. |
| 4.3 | « a sequential anytime-valid threshold raised 21–35% with no attack under the strongest episode effects » | « Raised 21–35% » sans nom (des fausses alertes) ; « anytime-valid » et « episode effects » ne sont pas définis. | à corriger | « …threshold gave 21–35% false alarms under… » (−1) |
| 4.4 | « items resampled, not models » | Il faut deviner qu'il s'agit de l'intervalle. | mineur | « (interval over items, not models) » (+1) |
| 4.5 | « I publish whole curves » | Quelles courbes ? Le README publie des gains par taille et par intensité, plus des lectures moyennes. | mineur | « I publish every size's readings » |
| 4.6 | « by 10 percentage points at equal false alarms » | Dix points de quoi ? De taux de détection, sans doute. | mineur | « 10 points of detection rate » |

**Liens** :
- R7 épinglé à `9f5bf6a` ; les autres réponses épinglent `b3ecaec`. J'ai vérifié sur le clone : `9f5bf6a` est un ancêtre de `b3ecaec`, `git diff 9f5bf6a b3ecaec -- results/R7/README.md` est vide, et le blob à `9f5bf6a` a l'empreinte `2dd0790c…`, comme à `b3ecaec`. Le lien fonctionne : `9f5bf6a` est le commit qui publie R7. **Mineur** : harmoniser sur `b3ecaec` ou garder, au choix.
- ideation-organism pointe sur `main`, sans commit. Le chemin `resultats/controle-simulation-defenses/` existe sur `main` du clone (`HEAD` = `main` = `origin/main` = `faff48b`, arbre `75be55cb…`, README `04ce0afc…`). Je n'ai fait aucun `fetch` : l'état du dépôt en ligne n'est pas vérifié. **Mineur** : épingler, comme l'autre lien, à `7c7b688` (le commit qui publie T0.3 et P3, 3 novembre 06:10 temps universel) ou à `faff48b`.

## 5. Ce qui le retiendrait (à ne pas couper)

- **Le premier paragraphe** : l'horizon du METR transposé en une ligne (50 % de portes dérobées prises, à fausses alertes fixées, selon n) et l'énoncé dans son propre gabarit. C'est la réponse à sa question, sans détour.
- **Ses deux papiers, exacts et à la bonne place** : 2509.15541 § 6.1 (2,0 % → 20,5 %), la raison même de fuir une tendance de propension ; 2412.04984 § 4 (incertitude d'élicitation), la raison de mettre à part la strate d'attaquants contemporains.
- **La vérité par exécution, le corpus gelé et privé, publié par empreinte** : cela répond à la contamination et au juge.
- **GPT-4.1 capturé** : le moniteur le plus fort peut tomber, donc « the sign can flip ». La strate est rapportée à part, jamais moyennée.
- **Trois tests préenregistrés qui tuent**, dont les détecteurs triviaux et la calibration à chaque longueur ; la règle « intervalle entièrement d'un côté ».
- **R7 avec ses propres limites** : « a size slope, not a time slope », « items resampled, not models », le 72B qui bouge sans déférer. C'est l'honnêteté qui le convaincra, à condition de compléter le point 2.2.
- **T0.3**, précis et à sa place. On peut le renforcer sans mot de plus en rendant la dépendance à la longueur visible : sous le même effet d'épisode (τ = 0,2), la règle de Ville donne 21 % de fausses alertes à 200 actions et 35 % à 1 000. C'est exactement « at every length ».
- **La dernière phrase** : « This measures detection of frozen, non-adaptive sabotage, not of misalignment. » Elle désamorce le drapeau du classement (SC-03) et l'attente d'Apollo.

## 6. Compte de mots et limite

Script `/tmp/lecture-mentor-scheurer-scripts/compte_v1.py` (Python, lancé avec `-I`), sur le texte seul (tout ce qui précède `---`, sans fin de ligne finale) :
- **492 mots** séparés par des blancs (égal à `wc -w` et au pied) ; 490 sans les deux liens ;
- 3 295 caractères ; sha256 du texte seul `1277345560d3c29486a8a65776ece767344cf49a573130841889f284187baf78`, égal au pied ;
- par paragraphe : 107, 107, 104, 67, 107 ;
- mon motif `\w+` donne 553 (il coupe les décimales et les adresses) : il n'est pas comparable aux 496 du rédacteur, et ce n'est pas le compte d'un formulaire.

**Limite** : aucune limite écrite ; visée 500 au plus : **tenue**, marge de 8 mots.

**Budget des corrections « à corriger »** : 1.1 (0), 2.1 (+2), 2.2 (+1), 2.3 (+5), 4.1 (+7), 4.2 coupée (−11), 4.3 (−1), soit **+3, donc 495**. Ajouter 3.1 (+4) donne 499. Ajouter aussi 3.2 (+2) donne 501 : il faut choisir l'un des deux, ou raccourcir 4.1 (« (0 ignores, 1 adopts the note) », +6).

Interdits tenus : aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`, rien sous `/home/claude/coffre-*`. Aucun appel de modèle autre que moi, sauf le rendu interne de `WebFetch`, que la consigne autorise. Un `grep` trop large a dépassé son `timeout 60` et a été arrêté par ce délai (code 143) ; aucun processus ne reste.
