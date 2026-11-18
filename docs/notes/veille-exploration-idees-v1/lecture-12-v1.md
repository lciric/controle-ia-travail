# Lecture 12 sur source — « From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? » (Qin, Deng, Ahmed, Tung, Feng ; arXiv 2611.05108) — v1

Écrite le 18 novembre 2026 (vers 06:40 UTC) par un sous-agent lecteur. Aucun commit, aucune dépense, aucun résultat sous embargo ouvert, rien dans `registres/`. Le PDF de la version 1 (la seule) a été lu en entier : 27 pages, annexes comprises ; les figures 3, 4, 10 et 11 ont été lues sur image.

Vocabulaire de cette fiche. « Instance persistante » : le même agent garde sa session, son espace de travail, ses fichiers et ses traces d'une tâche à la suivante (« stateful »). « Instance remise à zéro » : session et espace de travail neufs à chaque tâche (« stateless », « reset »). « Suite de tâches » : trois à cinq tâches apparentées servies dans un ordre fixe (« stream ») ; il y a neuf suites, une par « famille ». « Tâche de transfert » : toute tâche d'une suite sauf la première (32 par agent). « Récompense » : la métrique de la tâche ramenée entre 0 et 1, lue sur une part de test cachée ; un « point » vaut un centième. Les trois gains, toujours « persistante moins remise à zéro » : « gain de résultat final » (la solution que l'agent choisit à la fin ; « outcome gain »), « gain de première solution » (la première solution valide ; « initialization gain »), « gain de vitesse de convergence » (l'aire sous la courbe du meilleur score caché atteint au fil du budget ; « time-convergence gain »). « Fiches d'enseignements » : résumés écrits par l'agent lui-même sur ses essais passés (« insight cards ») ; « fiches appariées » : celles de la même suite ; « fiches mélangées » : autant de fiches, venues d'une suite sans rapport ; « aucune fiche ».

## 0. Verdict en trois lignes

1. **Revendication 10 (mémoire de l'organisme) : occupée en partie, rien n'y est contredit à la lettre.** Ce qui est pris : la mesure de ce que vaut une mémoire entre tâches pour un agent de recherche, contre le même agent remis à zéro, à tâches et budget appariés, avec un témoin de mémoire factice (fiches mélangées). Ce qui n'est que voisin : notre règle « la mémoire ne sert ni verdict, ni clé, ni témoin » (ici les scores cachés n'entrent jamais dans l'état persistant, mais pour une autre raison, et il n'y a ni juge ni témoin planté). Le travail est bien un **second contre-indice, indépendant** de celui de Qu, Chen et Wang, à l'utilité attendue d'une mémoire — mais sur un autre objet (un agent seul qui écrit du code d'apprentissage automatique, pas un organisme d'idéation) et **plus mince que son résumé** : aucune épreuve statistique, une seule paire de courses par configuration, et l'essai sur les fiches tient sur quatre tâches d'une seule famille.
2. **Revendication 8 (héritage récompensé sur plusieurs générations) : voisin, avec un contre-indice partiel sur la prémisse.** Rien ici ne récompense un concepteur sur plusieurs générations ; ce qui est mesuré, c'est ce que rapporte l'état hérité. Il rapporte au départ de la tâche suivante (une solution valide plus tôt) et s'efface à l'échéance ; une fois la première solution retirée, aucun des cinq agents ne garde d'avantage. La phrase qui nous arrangerait — l'avantage croît avec la position dans la suite — n'est pas établie (section 4).
3. **La « raison du choix » est à corriger sur un mot.** Il n'y a pas d'« ablation de ce qui est retenu » : l'essai fait varier la pertinence d'un seul type de contenu (les fiches), dans des sessions neuves ; les auteurs le disent eux-mêmes (p. 9 : « Future work should separately test insights, code, transcripts, and execution state »).

## 1. Source versée

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/lecture-12-arxiv-2611.05108/` (chaque fichier a son compagnon `.sha256` ; détail dans `adresse.txt`).

| Pièce | Fichier | Empreinte SHA-256 |
|---|---|---|
| PDF d'arXiv, version 1, 27 pages, 664 874 octets (lu en entier) | `arxiv-2611.05108v1.pdf` | `aae125654c66cfb53ad1a01edf7daa3f7d3bfebf6534b4b59aa7ea195dd279eb` |
| Page de résumé d'arXiv (historique des versions) | `page-abs-arxiv-2611.05108.html` | `c0f302805541107684782ac058762820610bc627e5a67eaaa737a90f10dfd865` |
| Page de l'affiche à NeurIPS 2026 | `page-neurips-2026-affiche-169860.html` | `ff06e3356aeb2c3fab7946d02d6ff95bdf9a9c9f1f7def27bb4d9bd9031dafe9` |
| Page du site de l'atelier (dates) | `page-site-atelier-meta-agents.html` | `9b3730114d99442a87d063fef8b1cfd80ce0cbe44542da9b28098756cd0d15c6` |
| Provenance | `adresse.txt` | `a8d81427994386895b4888ada7440f20835c60c66cd67c869d28cdfddbfad95f` |

Le même PDF (même empreinte) était déjà versé à plat par la recherche « adverse » (`adverse-arxiv-2611.05108v1.pdf`, lu alors p. 1 et 2). Récupération le 18 novembre 2026 entre 06:22 et 06:27 UTC, par `curl`, sans contournement. Données non fiables, jamais exécutées ; lues par `pdftotext`, `pdftoppm` et Python lancé avec `-I`. Aucune consigne adressée à un lecteur automatique n'a été relevée.

Dans cette fiche, « p. N » renvoie aux pages du PDF (numéros imprimés et numéros du fichier coïncident). **Tout chiffre marqué d'une page a été lu sur le PDF** (règle R7). « Calcul de ma main » : déduit des tableaux par moi, absent de l'article. « Lecture d'image » : lu à l'œil sur une figure, donc approximatif et non opposable.

## 2. Ce que le travail fait

- **La question** (p. 1-2) : un agent de recherche automatique qui garde son état d'une tâche à l'autre fait-il mieux que le même agent remis à zéro ? Sans toucher aux poids : « We study this setting without updating model weights, in which case experience is transferred only through the state accumulated during execution » (p. 1).
- **Le montage** (p. 3, figure 1 p. 2) : une suite ordonnée de tâches ; pour chaque tâche, une consigne, des données d'entraînement et de développement, un budget de temps d'horloge (30 minutes par défaut, p. 6). L'agent soumet autant de solutions qu'il veut et en choisit une. Toutes sont notées après coup sur un test caché. Deux bras appariés : instance persistante (« We resume the same native agent session and workspace across the stream », p. 3) et instance remise à zéro. Aucune mémoire écrite par le banc : « We do not provide an additional harness-written memory or summary » (p. 3).
- **Les tâches** (p. 5, annexe A p. 13-15) : neuf familles — trois suites synthétiques de classification sur une même matrice de 6 000 lignes et 150 colonnes dont la règle cible change (facteurs latents partagés, petit lot de variables utiles partagé, variable de régime partagée) ; une suite de régression symbolique (cinq équations qui se simplifient après un changement de variables, dont une tâche témoin asymétrique) ; trois suites de prévision de séries temporelles (transformateurs électriques, capteurs de trafic, systèmes d'énergie) ; deux suites tabulaires réelles (cinq jeux du lot d'évaluation de SELA, trois de MLE-bench). Les jeux publics sont servis sous des noms neutres (p. 13).
- **Les agents** (p. 6) : Sonnet 4.6 et Opus 5 par Claude Code, GPT-5.4 et GPT-5.6-Sol par Codex, Kimi K3 par OpenCode — chacun dans son outil en ligne de commande d'origine.
- **Les mesures** (p. 4) : les trois gains du vocabulaire ci-dessus, moyennés par famille puis entre familles ; la première tâche de chaque suite est exclue.
- **Les essais annexes** : trois répétitions pour un seul agent (p. 6, figure 4 p. 17) ; budget de 15, 30 et 60 minutes pour un agent sur une famille (p. 7-8) ; fiches appariées, mélangées ou absentes sur une famille (p. 8, p. 23) ; longueur de la suite, une course par condition (p. 22) ; sept études de cas choisies (p. 23-27).
- **Hors sujet, une ligne** : la discussion note qu'un état persistant peut propager aux tâches suivantes un contenu trompeur introduit pendant une tâche, sans l'évaluer (p. 9).

## 3. Ce qui est mesuré, ce qui est seulement affirmé

**Mesuré, par programme, sans juge modèle** (p. 14 : « parses and evaluates the expression without an LLM judge » ; partout ailleurs une métrique sur test caché).

| Résultat | Chiffres (page) | Taille de la preuve |
|---|---|---|
| Le gain de vitesse de convergence est positif en moyenne pour les cinq agents | +21,3 (Kimi K3), +20,9 (Sonnet 4.6), +7,5 (Opus 5), +6,1 (GPT-5.6-Sol), +3,0 (GPT-5.4) — tableau 2, p. 7 | 32 tâches de transfert par agent, **une seule paire de courses** par agent et par famille (p. 6 : « all other comparisons use a single matched run pair ») |
| Le gain de résultat final est proche de zéro pour quatre agents sur cinq | −0,9 ; −0,8 ; +0,4 ; +7,6 (Sonnet 4.6) ; +0,2 — tableau 2, p. 7 | idem |
| L'avance de l'instance persistante fond au fil du budget | écart moyen du meilleur score caché : +24,0 au quart du budget, +15,7 à la moitié, +6,5 aux trois quarts, +1,2 à l'échéance, où seuls Kimi K3 et Sonnet 4.6 restent positifs — tableau 8, p. 21 | idem |
| L'avance vient de la première solution, pas de la recherche qui suit | délai avant la première solution valide, persistante contre remise à zéro : 7,7 contre 11,1 minutes (Opus 5), 9,5 contre 18,7 (Kimi K3), 7,7 contre 16,3 (Sonnet 4.6) — tableau 7, p. 21 ; à nombre de candidats égal le gain tombe à −0,5 ; +0,1 ; +1,7 ; +6,5 ; +1,2 (même tableau) ; une fois la première solution retirée, le gain d'aire est négatif pour les cinq : −1,0 ; −0,3 ; −0,2 ; −0,2 ; −3,2 — tableau 10, p. 22 | idem |
| Les fiches pertinentes ne font pas mieux que des fiches sans rapport sur le résultat final | fiches appariées contre mélangées, résultat final : +1,0 ; −3,2 ; −0,2 ; +0,2 (tableau 12, p. 23) ; contre aucune fiche : Sonnet 4.6 +14,7 avec les appariées et +14,9 avec les mélangées, GPT-5.4 +5,0 et +4,8 (p. 23) | **quatre tâches de transfert d'une seule famille** (systèmes d'énergie), quatre agents (Kimi K3 absent), aucune répétition annoncée |
| Variabilité d'une répétition à l'autre | « Outcome and initialization gains varied by at most 0.75 points, and time-convergence gains by at most 7.14 » (p. 6) | trois répétitions, **un seul agent** (GPT-5.6-Sol) ; la figure 4 (p. 17) ne montre que huit familles sur neuf : la régression symbolique, la plus dispersée du tableau 6, n'y est pas |

**Seulement affirmé, ou appuyé trop court.**
- « to our knowledge, the first study of a continual AI R&D setting » (p. 2) : affirmation de priorité, dans un texte qui cite lui-même six bancs voisins (p. 3).
- « suggesting that accumulated experience becomes more useful as the stream progresses » (p. 6) : repose sur les figures 10 et 11, lues durement en section 4.
- « Transfer gains also depend on model capability » (p. 7) : deux paires de modèles, et l'outil d'origine est confondu avec le modèle (les auteurs l'admettent, p. 9).
- « our findings favor persistent execution when compute or time budgets are limited » (p. 9) : l'essai de budget porte sur un agent et une famille (figure 3, p. 8) ; aucun coût en jetons ni en dollars n'est rapporté nulle part, et l'appariement se fait en temps d'horloge seulement.
- Les mécanismes d'échec (ancrage, mauvais choix final, leçon appliquée trop fort) : sept cas « selected for interpretability », qui « should not be read as a systematic or causal decomposition » (p. 23) ; l'un d'eux est brouillé par la charge de la machine (p. 27 : « Host contention also affected this stream »).
- **Aucune épreuve statistique et aucun intervalle dans tout le document** (recherche des motifs « significan », « confidence interval », « bootstrap », « p-value » : zéro occurrence). « Do not consistently translate » décrit des signes mêlés, pas une nullité éprouvée.

**Données et code.** Non publiés. P. 10 : « The code will be released alongside the camera-ready version ». Aucun dépôt nommé. Les jeux réels sont publics ; les générateurs synthétiques sont donnés par leurs formules (p. 13-14) ; les traces des agents, les consignes et les fiches ne sont pas publiées, bien que la déclaration de reproductibilité dise que les consignes sont dans l'article (p. 10). Les suites d'où viennent les fiches mélangées (« weekly-health and daily-currency forecasting tasks », p. 24) et la tâche de météo de l'essai de longueur (p. 22) ne sont décrites nulle part.

## 4. Lecture dure

**Ce qui nous arrange, lu plus durement.**

*« La mémoire n'améliore pas le résultat final »* (cela conforte le statut le plus dur déjà retenu pour la revendication 10).
- Les gains de résultat final de quatre agents (−0,9 à +0,4) sont de l'ordre de la variabilité que les auteurs mesurent eux-mêmes (0,75 point, p. 6) : c'est une absence de signal dans une seule paire de courses, pas la preuve d'une absence d'effet.
- L'exception, Sonnet 4.6 (+7,6), tient à deux familles sur neuf : régression symbolique +41,2 et systèmes d'énergie +18,5 (tableau 6, p. 16) ; sans elles la moyenne des sept autres est +1,2 (calcul de ma main), et la médiane par tâche est +1,3 (tableau 2). Elle tient aussi aux pannes du bras remis à zéro : 71 essais échoués contre 15 pour l'instance persistante (tableau 4, p. 15 ; taux d'échec 30,7 % contre 7,7 %, p. 22). Une partie de ce gain est donc de la fiabilité d'exécution, pas du savoir transféré.
- Budgets de 30 minutes, suites de trois à cinq tâches (p. 9) : rien n'est dit de suites longues, où la mémoire aurait le temps de compter ou de nuire.
- Le taux de « transfert négatif » des tableaux 4 à 6 est le complément du taux de victoire dans toutes les lignes : les égalités y sont donc comptées comme transfert négatif (exemple : Opus 5, régression symbolique, médiane +0,0, victoire 25 %, transfert négatif 75 %, p. 16). Le « 65,7 % » d'Opus 5 ne se lit pas comme « nuit deux fois sur trois » (lecture de ma main).

*« Les fiches sans rapport rapportent autant que les fiches pertinentes »* (cela conforte notre méfiance envers une mémoire de contenu).
- Quatre tâches, une famille, pas de répétition : les écarts de vitesse de convergence entre fiches appariées et mélangées vont de −27,3 à +25,6 selon l'agent (tableau 12, p. 23), sans mesure du bruit de ce montage. Le signe change d'un quart du budget à l'autre pour trois agents sur quatre (tableau 13, p. 23).
- La référence « aucune fiche » est dite « independent » (légende du tableau 12) : elle n'est pas appariée aux deux autres bras de la même façon.
- Ce que l'essai établit : dans ce montage, on ne sépare pas « avoir des fiches » de « avoir les bonnes fiches » sur le résultat final. Il n'établit pas que le contenu d'une mémoire est sans valeur.

*« L'avantage croît avec la position dans la suite »* (cela conforterait la prémisse de la revendication 8 : ce qu'une génération lègue compte davantage plus tard).
- La figure 11 (p. 20) mesure l'avantage de chaque position **par rapport à la première tâche**. Or à la première tâche les deux bras sont dans la même condition (aucun état antérieur, p. 3) : leur écart est un tirage de bruit. Et ce tirage est grand : sur la figure 10 (p. 20), la courbe de la première tâche descend vers −50 à −60 points sur une partie du budget pour Opus 5, GPT-5.6-Sol et Kimi K3, et monte vers +55 pour Sonnet 4.6 (lecture d'image). Les deux agents dont la « croissance » est la plus forte (Opus 5, Kimi K3) sont ceux dont la première tâche est la plus négative ; Sonnet 4.6, dont la première tâche est positive, est l'exception que le texte signale (p. 6).
- Après la deuxième tâche, les courbes de la figure 11 sont plates (lecture d'image) : il y a une marche entre « pas d'état » et « un état », pas une accumulation.
- Seulement les trois familles synthétiques, une paire de courses. L'essai de longueur de suite va dans l'autre sens : avec six tâches antérieures, le gain de vitesse de convergence tombe à −31,44 (tableau 11, p. 22 ; une course).
- Verdict : non établi. Nous ne pouvons pas citer ce travail à l'appui d'un effet différé de l'héritage.

**Ce qui ne nous arrange pas, lu de même.**

*« L'état persistant améliore l'efficacité des cinq agents »* (titre de la section 5.2, résumé).
- Net pour deux agents (Kimi K3, Sonnet 4.6, autour de +21). Pour les trois autres (+7,5 ; +6,1 ; +3,0), le gain est de l'ordre de la variabilité mesurée sur un agent (7,14 points, p. 6).
- Par famille, la dispersion entre répétitions est de plusieurs dizaines de points et le signe change dans plusieurs familles (figure 4, p. 17, lecture d'image). Pour la famille des transformateurs électriques, les trois répétitions de GPT-5.6-Sol paraissent toutes négatives sur la figure alors que le tableau 6 donne +7,4 : incohérence apparente, à l'œil, que je ne peux pas trancher.
- Ce que le gain contient : surtout le délai avant la première solution valide, c'est-à-dire la familiarité avec le contrat de livraison et l'outillage déjà en place, plus que des enseignements sur le problème. Les auteurs le disent : « The current results do not show a general improvement in optimization after initialization » (p. 7).

**Incohérences relevées dans le document.**
- Gain de première solution de Sonnet 4.6 et de GPT-5.4 : +6,8 et +3,7 dans le texte (p. 7) et le tableau 9 (p. 22) ; +7,0 et +3,0 dans les tableaux 2 et 7 (p. 7, p. 21). Deux agrégations, non dites.
- Le résumé annonce un essai qui fait « vary what information agents retain » (p. 1) ; l'essai fait varier la provenance des fiches, pas la nature de ce qui est retenu (p. 8, p. 9).

## 5. Verdicts sur les revendications visées

### Revendication 10 — mémoire de l'organisme

Rappel : « La mémoire ne sert ni verdict, ni clé, ni témoin aux agents ; les juges sont aveugles aux notes antérieures. » Statut retenu : « occupée dans son principe » ; contre-indice publié à dire (Qu, Chen, Wang).

| Pièce | Verdict | Preuve (page, citation courte) et lecture dure |
|---|---|---|
| **La mémoire ne porte aucun verdict** | **voisin** | Les scores cachés n'entrent jamais dans l'état persistant : « intermediate submissions test scores are hidden » (p. 3) ; la courbe « is never shown to the agent in case it tries to reward hack » (p. 4). Mais la raison donnée est d'empêcher le trucage de la récompense, pas une règle sur la mémoire ; et l'état persistant porte librement les scores de développement (« Feedback from earlier tasks remains visible in this state », p. 3). Les fiches portent même des scores : « The best known result is a correction model at RMSE=0.837 » (p. 25), dans le cas où la mémoire ancre l'agent sur une famille de modèles plus faible. Cas unique et choisi : il illustre notre règle, il ne la prouve pas. |
| **Ni clé, ni témoin ; juges aveugles aux notes antérieures** | **libre dans cette pièce** (non trouvé ; règle R8 : cela ne dit rien du champ) | Pas de juge, pas de témoin planté, pas de clé : la note est une métrique calculée par programme. |
| **Mesurer ce que vaut une mémoire, contre le même système sans mémoire, avec une mémoire factice** | **occupé** (sur des tâches d'ingénierie d'apprentissage automatique, agent seul) | Bras appariés p. 3 ; fiches appariées, mélangées, absentes p. 8 : « Comparing matched with shuffled memory tests whether the relevance of the transferred content matters ». Notre dépôt ne revendiquait pas ce montage ; il est à citer si nous le reprenons. |
| **Contre-indice à dire** | **confirmé, à dire avec ses limites** | « these gains do not consistently translate into better final solutions » (p. 1) ; « Retaining relevant knowledge and using it effectively are therefore separate capabilities » (p. 2). Indépendant de Qu, Chen et Wang : autres auteurs, autre objet, et leur travail n'est pas dans la bibliographie (p. 10-12). Limites à dire avec lui : section 4. |

**Verdict d'ensemble : occupé en partie.** Le statut « occupée dans son principe » est confirmé et un second contre-indice s'ajoute. Rien n'est contredit : la revendication 10 n'affirme pas que la mémoire aide. Non trouvé dans cette pièce : une mémoire d'organisme à plusieurs agents, des juges, la règle « sans verdict » posée comme règle.

### Revendication 8 — organisme à plusieurs générations, héritage récompensé

Rappel : le signal rendu à ce qui conçoit porte sur K générations (K ≥ 3) pour que la mémoire transmise et les instruments à effet différé comptent ; expérience « poids contre archive » (concepteur figé avec archive consultable, contre concepteur entraîné, à information égale).

| Pièce | Verdict | Preuve (page, citation courte) et lecture dure |
|---|---|---|
| **Récompenser l'héritage sur plusieurs générations** | **voisin** | Aucune récompense, aucun concepteur, aucune génération : une suite de tâches et un agent figé. Le lien est la mesure de ce que rapporte l'état hérité. |
| **Prémisse : ce qui est légué compte** | **voisin, contre-indice partiel à dire** (je ne retiens pas « contredit ») | Ce qui est légué compte pour la vitesse, pas pour le résultat à budget égal : écart de +24,0 au quart du budget, +1,2 à l'échéance (p. 6, tableau 8 p. 21) ; « Under a stricter control that also subtracts each run's first-valid reward, the gain becomes negative for every agent » (p. 7). Pourquoi pas « contredit » : notre énoncé dit comment récompenser l'héritage, pas qu'il améliore le résultat ; et la preuve est d'une seule paire de courses, sur 30 minutes. |
| **Effet différé qui grandit au fil des générations** | **non établi par cette pièce** | Figures 10 et 11 (p. 20), lues en section 4 : marche entre la première tâche et les suivantes, mesurée contre un tirage de bruit ; plat ensuite. |
| **« Poids contre archive »** | **voisin** | Seul le bras sans mise à jour des poids existe ici (p. 1 : « without updating model weights »). La comparaison elle-même n'est pas prise par cette pièce. Indice utile pour notre bras « archive » : une archive de fiches écrites par l'agent ne bat pas une archive sans rapport sur le résultat final (p. 23), sur quatre tâches. |

**Verdict d'ensemble : voisin.**

### En passant, hors des revendications visées (une ligne chacune)

- Revendication 9 (le séquentiel doit battre le meilleur de N tirages indépendants à budget égal) : voisin. L'instance remise à zéro rattrape l'instance persistante à l'échéance (p. 6), mais ce n'est pas un « meilleur de N », et le budget est apparié en temps d'horloge, pas en coût.
- Revendication 11 (sélection lue une fois) : voisin. Un cas de surajustement à la part visible : R² de développement 0,99979, R² caché −1,354 (p. 26) ; un seul cas.
- Revendication 6 (mondes plantés) : voisin. Suites synthétiques à règle connue et régression symbolique à « private ground-truth manifest » (p. 14) ; le taux de structures retrouvées est dit enregistré (p. 14) mais n'est rapporté nulle part.

## 6. Date de première version

- **Vérifié sur la page de résumé d'arXiv versée** : une seule version, v1, mardi 3 novembre 2026, 16:02:34 UTC.
- **Avant arXiv, non vérifié par moi** : la recherche de littérature grise de cette veille a relevé une soumission à ICLR 2027 sur OpenReview datée du 18 septembre 2026 (`openreview.net/forum?id=OPHp9Aei9U`). OpenReview m'a servi un défi de navigateur ; je n'ai pas insisté.
- **Trouvé par cette lecture** : le travail est aussi une affiche de l'atelier « Managing Agents that Manage Agents » de NeurIPS 2026 (11 décembre 2026, Sydney ; page versée), avec une seconde fiche OpenReview (`forum?id=L7zk8dPc1k`). Le site de l'atelier (page versée) donne une date limite de soumission au 29 août 2026 reportée au 5 septembre, des soumissions privées pendant l'évaluation et une notification au plus tard le 29 septembre. Si la date limite a été tenue, une version existait donc début septembre 2026, non publique ; son contenu m'est inconnu.
- **À retenir** : première date publique établie, 3 novembre 2026 ; première date publique probable, 18 septembre 2026 (non vérifiée) ; existence privée probable dès début septembre 2026 (déduite). Toutes sont antérieures à N-067 (13 novembre 2026) ; les deux dernières sont antérieures à N-045 v2 (25 octobre 2026).

## 7. Une idée à prendre

**Un bras « archive mélangée » dans toute mesure d'héritage ou de mémoire, et l'héritage lu en trois temps.**

1. Dans l'expérience « poids contre archive » et dans toute course où une génération lègue des notes, ajouter un bras où l'organisme reçoit une archive de même taille et de même forme, venue d'une famille sans rapport. Ici, ce bras rapporte autant que l'archive pertinente sur le résultat final (p. 23) : sans lui, nous attribuerions au contenu de l'héritage ce qui tient à la seule présence d'un texte de départ.
2. Lire l'héritage séparément sur la première proposition de la génération suivante, sur l'aire sous la courbe du meilleur score au fil du budget, et sur le résultat final, avec les deux contrôles du tableau 7 (même nombre de candidats ; départ à la première solution valide). Une récompense sur K générations qui ne regarde que l'aire paierait la vitesse de démarrage, pas le savoir.
3. La première génération (ou la première tâche), où les bras ne diffèrent pas encore, donne sans coût l'essai à bras identiques que N-045 demande ; ce travail l'avait sous la main et ne l'a pas chiffré.

C'est une proposition : l'ajout d'un bras à un préenregistrement est une décision de Lazar.

## 8. Réserves de cette lecture

- Les lectures d'image (figures 3, 4, 10, 11) sont approximatives et non opposables ; l'incohérence apparente entre la figure 4 et le tableau 6 n'est pas tranchée.
- Les dates d'OpenReview ne sont pas vérifiées (accès refusé).
- Je n'ai pas relu Qu, Chen et Wang : l'indépendance des deux contre-indices est établie par les auteurs, l'objet et l'absence de citation, pas par une comparaison des deux textes.
- « Non trouvé dans cette pièce » ne veut jamais dire « libre dans le champ » (règle R8).
