# Répétition d'entretien : les questions du jury

Candidature au Transformative AI Fund, proposition v2 du 7 octobre 2026.
Rôle : membre du jury. Seul texte lu : `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` (421 lignes). Les numéros de ligne renvoient à ce fichier. Aucun autre document consulté, aucune recherche sur le réseau. Quand j'invoque un souvenir de la littérature, je le signale comme tel : c'est ce qu'un jury compétent dirait, pas un fait vérifié.

## Lecture d'ensemble, avant les questions

- **Ce qui joue pour toi.** La discipline de préenregistrement. L'échec de P3 rapporté en détail (l. 368–370). Une dépense de calcul frugale (l. 283). Des revendications déjà rétrécies après vérification (l. 260–264). Une issue écrite à chaque porte.
- **Le point de rupture.** Aucune donnée sur la question centrale : δ > 0 sur des organismes réalistes (l. 94). Tout repose sur trois choses : un environnement reconstruit sans code ni données (l. 119–120), des organismes de 8 milliards de paramètres, et une personne seule qui délègue l'ingénierie et la relecture à des agents d'une même famille (l. 256–258).
- **Le résultat principal annoncé.** C'est la porte G1 : la surveillance séquentielle boîte blanche doit battre la meilleure base boîte noire, en rappel à 1 % de faux positifs. Elle tombe **à la fin du mois 4, soit fin mars 2027** (l. 110, 159, 297), le mois où l'article C doit paraître sur arXiv. La porte GC de l'article C tombe à la fin du mois 2, soit fin janvier 2027 (l. 110, 205, 292). Le jour de l'entretien, seul le pilote peut avoir produit des données, puisqu'il doit tourner avant le début de la bourse (l. 278).

## 1. Les dix questions, de la plus dangereuse à la moins dangereuse

### Q1. Que décide vraiment G1 : de l'accumulation, ou une asymétrie d'information ?

- **Question (anglais).** « In family (i) the sabotage instruction sits in the system prompt, and your probes "read the agent's private context too". Any probe placed after the system prompt can simply detect the instruction. Does your black-box baseline see that same context? If it doesn't, a white-box win on family (i) measures access to the prompt, not accumulated invisible evidence. Which organism families enter the G1 test, and with what weight? For family (ii), distilled from (i), what result would tell you that the probe reads an artefact of how you built the organism rather than an intent? »
- **Traduction.** « Dans la famille (i), la consigne de sabotage est dans l'invite système, et tes sondes "lisent aussi le contexte privé de l'agent". N'importe quelle sonde placée après l'invite système peut simplement détecter la consigne. Ta base boîte noire voit-elle ce même contexte ? Sinon, une victoire de la boîte blanche sur la famille (i) mesure l'accès à l'invite, pas une preuve invisible qui s'accumule. Quelles familles d'organismes entrent dans le test de G1, et avec quel poids ? Pour la famille (ii), distillée de (i), quel résultat te dirait que la sonde lit un artefact de fabrication de l'organisme plutôt qu'une intention ? »
- **Lignes qui la provoquent.**
  - l. 122 : consigne cachée dans l'invite système.
  - l. 123 : adaptateur LoRA distillé de (i).
  - l. 125–126 : la prédiction de validité.
  - l. 127 : les sondes ne sont « jamais entraînées et évaluées sur les mêmes organismes ». Mais entraînées sur quoi ?
  - l. 135–136 : H1 compare « à agrégation égale et à taux de faux positifs égal », pas « à information égale ».
  - l. 139–140 : les sondes lisent le contexte privé.
  - l. 159–161 : la porte G1.
- **Pourquoi elle est dure.** C'est le résultat principal.
  - Si la famille (i) entre dans G1, un G1 positif est acquis d'avance et ne dit rien de l'accumulation.
  - Si seule la famille (ii) compte, le risque se déplace. Un adaptateur distillé d'un modèle sous consigne peut porter une direction nette de « saboteur sous consigne », qu'aucun modèle réellement désaligné n'aurait. La sonde réussirait alors sur (i) comme sur (ii) en lisant la même trace de fabrication. La prédiction de validité (l. 125–126) ne sépare pas ce cas d'une intention.
  - Les deux contrôles croisés (l. 126–127) séparent la conscience d'évaluation de l'intention. Ils ne séparent pas l'intention de l'artefact de construction.
  - Une sonde peut aussi lire les traits du texte saboté que l'agent est en train d'écrire. C'est une information que la boîte noire possède aussi.
- **Ce qui me convaincrait (montré le jour de l'entretien).** Le préenregistrement de G1, même en brouillon daté et empreinté, qui fixe ce qui suit :
  - l'organisme décisif est la famille (ii) seule ; la famille (i) est rapportée à part, comme contrôle de bon fonctionnement ;
  - l'information de chaque bras est écrite noir sur blanc : la boîte noire voit exactement les mêmes jetons que la sonde, invite système comprise pour les deux ou exclue pour les deux ;
  - les données d'entraînement des sondes sont disjointes des organismes décisifs, et la liste des découpages est donnée ;
  - un contrôle négatif : un adaptateur « honnête de même facture », obtenu par la même distillation à la même dose avec un changement de style bénin, sur lequel la sonde ne doit pas s'allumer ;
  - une base « traits du texte » : un prédicteur qui ne lit que les jetons produits, et que la sonde doit battre.
- **Signal d'alarme.**
  - « Les deux familles sont regroupées. »
  - « La boîte noire ne voit pas l'invite système, c'est tout l'intérêt », sans reconnaître que cela rend la famille (i) triviale.
  - Aucun adaptateur témoin.
  - « La sonde d'intention réussit sur les deux familles, c'est la preuve. »
  - Du flou sur les données d'entraînement des sondes.

### Q2. Le sabotage existe-t-il, et comment le sais-tu ?

- **Question (anglais).** « Your agents are 8B models writing ML experiment proposals, scored by an evaluator weaker still. Show me one sabotaged proposal that a competent reviewer would accept, and that your ground truth nevertheless labels as sabotage. Is the label the organism's condition or a measured harm? How is "delayed verification on a subsample" done for proposals that are never run: by whom, on how many items, with what agreement? And if 8B agents are too weak, your pivot is a "simplified rubric". Doesn't that make sabotage less fuzzy and the black-box monitor's job easier, which removes the very regime you claim to study? »
- **Traduction.** « Tes agents sont des modèles de 8 milliards de paramètres qui écrivent des propositions d'expériences d'apprentissage automatique, notées par un évaluateur encore plus faible. Montre-moi une proposition sabotée qu'un relecteur compétent accepterait, et que ta vérité de terrain étiquette pourtant comme sabotage. L'étiquette, est-ce la condition de l'organisme ou un dommage mesuré ? Comment se fait la "vérification différée sur un sous-échantillon" pour des propositions qui ne sont jamais exécutées : par qui, sur combien d'éléments, avec quel accord entre juges ? Et si les agents de 8 milliards sont trop faibles, ton repli est une "grille simplifiée". Est-ce que cela ne rend pas le sabotage moins flou et le travail du moniteur boîte noire plus facile, ce qui supprime le régime même que tu dis étudier ? »
- **Lignes qui la provoquent.**
  - l. 116–118 : l'environnement, l'évaluateur plus faible, la vérité de terrain.
  - l. 119–120 : la reconstruction d'un article qui ne publie ni code ni données.
  - l. 276–279 : l'environnement en v0 et le pilote avant la bourse.
  - l. 325 : le risque « agents 8B trop faibles », avec la grille simplifiée pour repli.
  - l. 257–258 et l. 383 : la validation humaine, 4 000 dollars.
- **Pourquoi elle est dure.** Tout le programme suppose un sabotage qui réunit quatre propriétés :
  - il est réel : il dégrade quelque chose de mesurable ;
  - il est diffus : chaque action reste sous le seuil ;
  - il est produit par un organisme de 8 milliards de paramètres ;
  - il est étiqueté de façon fiable.

  Sur des tâches floues, la vérité de terrain est le maillon le plus faible, et l'environnement source est reconstruit sans code. Si l'étiquette est la condition (« a reçu la consigne ») et non l'effet, le moniteur détecte le saboteur, pas le sabotage : la thèse de l'accumulation de preuves d'actions nuisibles n'est alors pas testée. Enfin, 4 000 dollars de validation humaine paient quelques dizaines d'heures d'expert.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - Les sorties du pilote : 5 à 10 paires « honnête / sabotée » sur un même article. Pour chacune : la cible plantée ; la preuve que le défaut planté est présent et vérifiable, par un script ou par un expert à l'aveugle ; les scores du moniteur par action, sous le seuil.
  - Une courbe dose–réponse : le taux de sabotage selon la dose de l'adaptateur.
  - Le protocole écrit de la vérification différée : nombre d'éléments, nombre et profil des experts, aveuglement, accord visé fixé d'avance (par exemple un kappa de Cohen), et un coût par élément cohérent avec la ligne budgétaire.
- **Signal d'alarme.**
  - « La vérité de terrain, c'est la consigne. »
  - « On le saura après le pilote. »
  - Aucune mesure du succès du sabotage.
  - Un évaluateur de confiance de la même famille que l'agent.
  - Aucun chiffre sur l'accord entre experts.

### Q3. Qu'est-ce que tu fais, toi, que les agents ne font pas ?

- **Question (anglais).** « You write that AI agents do the engineering, the runs, the literature checks and the internal reviews, and that the reviewers share a model family. You ask $35,000 for yourself and $7,000 for tooling. What do you do that the agents cannot? Without notes, show me why, under your lemma, the power of the terminal sum depends only on B, and which assumption breaks first on real activations. Then give me one concrete error by the agents that you caught yourself, and one that you missed and that a test or a human caught. »
- **Traduction.** « Tu écris que des agents d'intelligence artificielle font l'ingénierie, les exécutions, les vérifications de littérature et les relectures internes, et que les relecteurs partagent une même famille de modèles. Tu demandes 35 000 dollars pour toi et 7 000 pour l'outillage. Qu'est-ce que tu fais que les agents ne peuvent pas faire ? Sans notes, montre-moi pourquoi, sous ton lemme, la puissance de la somme terminale ne dépend que de B, et quelle hypothèse casse la première sur de vraies activations. Puis donne-moi une erreur concrète des agents que tu as attrapée toi-même, et une que tu as ratée et qu'un test ou un humain a attrapée. »
- **Lignes qui la provoquent.**
  - l. 256–259 : qui fait quoi ; les erreurs corrélées.
  - l. 334–335 : la parade au risque, soit une validation humaine de la vérité de terrain et « ma propre relecture à chaque porte ».
  - l. 249–250 : les verdicts finissent par ta seule signature.
  - l. 378, 382, 392 : la rémunération fait 59,7 % du budget ; l'outillage coûte 1 000 dollars par mois.
  - l. 380 : le consultant en statistique n'existe que dans le scénario ambitieux.
- **Pourquoi elle est dure.** Le fonds paie surtout un jugement : 60 % du budget est ta rémunération. Or le processus décrit est presque entièrement délégué aux machines.
  - Les 602 tests (l. 281) ont été écrits par les agents qu'ils contrôlent.
  - Les erreurs corrélées sont reconnues, mais la seule parade humaine payée porte sur la vérité de terrain, ni sur le code ni sur les statistiques.
  - Le consultant en analyse séquentielle n'existe que dans le scénario ambitieux, alors que le cœur de l'article A est séquentiel.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Une dérivation au tableau.** Sous un pur décalage de moyenne, la somme attaquée vaut la somme honnête plus B, quelle que soit la répartition. Sa loi est donc la loi honnête translatée de B, et la puissance P(S_honnête + B > c_α) ne dépend que de B, de n₀, de la loi honnête et de α. Puis les limites : la propriété casse dès que le sabotage change la variance ou la dépendance (classe K), ou que la réponse de la sonde n'est pas additive en intensité.
  - **Un registre d'erreurs** daté et empreinté, avec deux ou trois cas réels où tu as contredit les agents.
  - **Ton récit d'une décision** : pourquoi tu es passé du seuil de Ville à l'étalonnage sur épisodes entiers (l. 90–92).
- **Signal d'alarme.**
  - Pas de dérivation.
  - « Les agents l'ont vérifié. »
  - « Les tests passent », donné comme argument.
  - Aucun exemple d'erreur attrapée.
  - Incapacité à dire quelles décisions tu as prises contre l'avis des agents.

### Q4. Ta destination « libre » est-elle le plafond de l'échelle ?

- **Question (anglais).** « Your verdict v is read from verdict-token probabilities, so it lives between 0 and 1, and most attackers want "approve", the top of the scale. Then Δv = g(ĉ − v₀) with ĉ near 1 is what any monotone push with saturation produces. How do you tell "ĉ is the attacker's target" from "ĉ is the ceiling of the scale"? Do you have attacks with intermediate targets? If g varies with intensity, what exactly does the regression over intensities identify? And the law collapsed on Qwen2.5-7B in P3: why should g be rank-stable across monitors? »
- **Traduction.** « Ton verdict v est lu sur les probabilités des jetons de verdict : il vit donc entre 0 et 1, et la plupart des attaquants veulent "approuver", c'est-à-dire le haut de l'échelle. Alors Δv = g(ĉ − v₀) avec ĉ proche de 1, c'est ce que produit n'importe quelle poussée monotone qui sature. Comment distingues-tu "ĉ est la cible de l'attaquant" de "ĉ est le plafond de l'échelle" ? As-tu des attaques à cible intermédiaire ? Si g varie avec l'intensité, qu'est-ce que la régression sur les intensités identifie exactement ? Et la loi s'est effondrée sur Qwen2.5-7B dans P3 : pourquoi g serait-il stable en rang d'un moniteur à l'autre ? »
- **Lignes qui la provoquent.**
  - l. 165–169 : la loi, avec ĉ non imposé.
  - l. 170–174 : les prédictions, soit ĉ égal à la cible plutôt qu'à la moyenne du corpus, et g stable en rang.
  - l. 180–181 : « la revendication est la destination libre ».
  - l. 363–366 : P3, avec 30 items × 10 répétitions et l'effondrement sur Qwen.
- **Pourquoi elle est dure.**
  - L'article C passe en premier, et sa nouveauté revendiquée est la destination libre. Si la cible des attaques coïncide avec une borne de l'échelle, la destination « libre » est forcée par la borne et la nouveauté s'évapore.
  - La nulle de régression vers la moyenne (l. 170–171) ne couvre pas cette confusion.
  - Juste envers toi : dans P3, deux destinations distinctes (1,46 sous critique, 2,94 sous éloge, l. 364–365) plaident contre un pur effet d'échelle. Mais sur un verdict « approuver / rejeter », la cible de l'attaquant et la borne se confondent.
  - La « loi » repose sur un modèle et 30 items, et elle ne s'est pas transférée à Qwen.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Une figure de pilote.** Un juge, une famille d'attaque, et des cibles intermédiaires imposées par l'attaquant : par exemple « note 6 sur 10 », ou un score de risque visé à 0,3, 0,5 et 0,7. Le ĉ estimé, avec ses intervalles, doit suivre la cible et se séparer de la moyenne du corpus.
  - **Une comparaison préenregistrée** entre la forme linéaire et un modèle de saturation sur l'échelle logit.
  - **L'écriture de l'identification.**
    - Par intensité, la régression sur les items, Δv = a(I) − g(I)·v₀, donne g et ĉ = a/g.
    - L'intervalle de ĉ vient de la méthode delta ou du bootstrap.
    - L'hypothèse « ĉ commun à toutes les intensités » est testée, et non supposée.
- **Signal d'alarme.**
  - Toutes les attaques visent l'extrême de l'échelle.
  - Un ĉ annoncé sans intervalle.
  - Une « loi » au singulier, sur un seul modèle.
  - L'effondrement sur Qwen balayé d'un revers de main.

### Q5. Combien d'épisodes honnêtes, et que reste-t-il de « valide à tout instant » ?

- **Question (anglais).** « G1 is recall at a 1% false-positive rate, with a 95% interval on a paired difference. Thresholds are calibrated on whole honest episodes, because your own simulation showed that Ville's threshold fails under episode effects. How many held-out honest episodes do you need to pin a 1% threshold, how many sabotaged episodes to resolve the difference you expect, and what does that cost in GPU hours with 64 source papers? And once calibration is empirical, what is left of the "anytime-valid" guarantee in your summary? Does it survive a shift between calibration and deployment, or horizons longer than those calibrated? »
- **Traduction.** « G1 est un rappel à 1 % de faux positifs, avec un intervalle à 95 % sur une différence appariée. Les seuils sont étalonnés sur des épisodes honnêtes entiers, parce que ta propre simulation a montré que le seuil de Ville échoue sous effets d'épisode. Combien d'épisodes honnêtes tenus à l'écart te faut-il pour fixer un seuil à 1 % ? Combien d'épisodes sabotés pour trancher la différence que tu attends ? Et combien d'heures de processeur graphique cela coûte-t-il avec 64 articles sources ? Enfin, une fois l'étalonnage empirique, que reste-t-il de la garantie "valide à tout instant" de ton résumé ? Survit-elle à un décalage entre étalonnage et déploiement, ou à des horizons plus longs que ceux étalonnés ? »
- **Lignes qui la provoquent.**
  - l. 20–21 : la garantie valide à tout instant, dans le résumé.
  - l. 89–92 : des fausses alertes à 0,21–0,35 et à 0,17 au lieu de 0,05, d'où l'étalonnage sur épisodes entiers.
  - l. 159–161 : le critère de G1.
  - l. 277 : 64 articles pour le pilote.
  - l. 345 : la garantie « convient aux budgets d'audit ».
  - l. 394 : 800 à 1 200 heures équivalent A100.
- **Pourquoi elle est dure.**
  - **L'effectif d'étalonnage.** Un seuil par rang sur n épisodes honnêtes donne un taux réalisé de faux positifs aléatoire. Avec 99 épisodes, son écart-type vaut environ 1 point, autant que la cible. Il faut de l'ordre de 1 000 épisodes pour le ramener à environ 0,3 point.
  - **Le groupement.** Les épisodes sont groupés par article source (64), ce qui réduit l'effectif efficace.
  - **La puissance.** Un intervalle sur une différence de rappel appariée exige une analyse de puissance.
  - **Le budget.** Le calcul du principal (4 000 dollars) n'est rapproché nulle part de ces effectifs.
  - **La garantie.** L'argument de vente « valide à tout instant » devient une garantie empirique sous échangeabilité des épisodes honnêtes. Elle ne tient plus si la distribution de déploiement change.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Une analyse de puissance écrite** dans le préenregistrement de G1. Elle donne :
    - le nombre d'épisodes honnêtes d'étalonnage et de test ;
    - l'effet attendu, tiré du pilote ;
    - la prise en compte du groupement par article, par exemple un bootstrap par grappes ;
    - le coût en heures de calcul par épisode multiplié par les effectifs, qui reste sous le devis.
  - **Une reformulation honnête de la garantie.** Par exemple : une garantie conforme en échantillon fini, valide à tout instant jusqu'à l'horizon étalonné, sous échangeabilité des épisodes honnêtes.
  - **Une épreuve de décalage** : étalonner sur un lot d'articles, tester sur un autre.
- **Signal d'alarme.**
  - « On verra après le pilote. »
  - Le seuil théorique de Ville gardé malgré la simulation.
  - L'étalonnage et le rapport faits sur les mêmes épisodes.
  - Pas de grappes.
  - Un G1 « établi » sur une trentaine d'épisodes.

### Q6. Ta sélection de trajectoires et tes bases boîte noire ne penchent-elles pas d'avance pour toi ?

- **Question (anglais).** « H2 conditions on trajectories where every sabotaged action stays below the 1% threshold of a per-action monitor. Which monitor defines that selection? If it is a black-box monitor, you keep exactly the episodes where black-box evidence is weakest, which tilts the comparison toward white-box before any data is seen. And why is the strongest black-box reader you list, a one-pass judge over the whole trajectory, only a "floor" and not part of "the best black-box baseline" that G1 must beat? Isn't the counterfactual a developer cares about the best affordable black-box monitor, not a weak one? »
- **Traduction.** « H2 se restreint aux trajectoires où chaque action sabotée reste sous le seuil à 1 % d'un moniteur par action. Quel moniteur définit cette sélection ? Si c'est un moniteur boîte noire, tu gardes exactement les épisodes où la preuve boîte noire est la plus faible : la comparaison penche vers la boîte blanche avant même de voir les données. Et pourquoi le lecteur boîte noire le plus fort de ta liste, un juge qui lit toute la trajectoire en un passage, n'est-il qu'un "plancher", et pas une partie de "la meilleure base boîte noire" que G1 doit battre ? Le contrefactuel qui intéresse un développeur, n'est-ce pas le meilleur moniteur boîte noire abordable, plutôt qu'un faible ? »
- **Lignes qui la provoquent.**
  - l. 137–140 : la sélection de H2.
  - l. 130–133 : les bases boîte noire, soit un moniteur faible par action, TRACE-lite réimplémenté et l'accumulation sur scores boîte noire.
  - l. 159–162 : G1, où les « planchers sont rapportés, pas critères ».
  - l. 343–345 : le chemin vers l'impact.
- **Pourquoi elle est dure.**
  - Conditionner sur l'échec d'un des deux bras comparés est un biais de sélection classique. Les épisodes retenus sont ceux où le score boîte noire a été bas, en partie par hasard ; la boîte blanche, elle, n'a pas été filtrée sur son propre bruit. La boîte noire perd donc en partie par construction.
  - Si un juge qui lit toute la trajectoire attrape le sabotage, l'avantage de la boîte blanche n'a pas de valeur pratique, quel que soit le verdict de G1.
  - « Un juge en un passage avec le même modèle » : si c'est le modèle de l'agent non fiable, il faut le dire et le justifier.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - G1 calculé sur tous les épisodes sabotés, le sous-ensemble « sous le seuil » en analyse secondaire.
  - Si une sélection reste nécessaire, elle est faite par un moniteur tiers, qui n'est aucun des bras comparés, et fixée dans le préenregistrement.
  - Un bras boîte noire fort : le meilleur modèle de confiance abordable, qui lit toute la trajectoire, rapporté avec son coût.
  - Une phrase claire sur ce que devient la revendication si ce bras gagne.
- **Signal d'alarme.**
  - La sélection faite par le même moniteur boîte noire par action qui sert de base.
  - Le refus d'un bras fort « parce qu'il n'est pas de confiance » ou « trop cher », sans chiffre.
  - G1 jugé contre des bases faibles seulement.

### Q7. G0 n'est pas franchie : qu'advient-il de l'argent si elle échoue, et que coupes-tu au mois 4 ?

- **Question (anglais).** « On the date of your proposal, G0 is not passed. There are no organisms with a dose–response and no probes above the floor, the environment is at v0, and the harness is validated only up to 1,192 tokens, while research-sabotage trajectories built on arXiv papers will be far longer. Your risk table has no line for "G0 fails". What happens to our money if G0 fails in December? You also say Paper C "does not depend on Paper A's gate", yet HC2, HC2b and HC4 need the acting agent's probes from phase 0. Month 4 holds Paper C's writing, its arXiv release, a workshop, the end of the 2 × 2 design and G1. What do you cut first, concretely? »
- **Traduction.** « À la date de ta proposition, G0 n'est pas franchie. Il n'y a ni organismes avec une dose–réponse, ni sondes au-dessus du plancher ; l'environnement est en v0 ; et le harnais n'est validé que jusqu'à 1 192 jetons, alors que des trajectoires de sabotage de recherche bâties sur des articles arXiv seront bien plus longues. Ton tableau des risques n'a pas de ligne "G0 échoue". Que devient notre argent si G0 échoue en décembre ? Tu dis aussi que l'article C "ne dépend pas de la porte de l'article A", mais HC2, HC2b et HC4 ont besoin des sondes de l'agent construites en phase 0. Le mois 4 contient la rédaction de l'article C, sa mise sur arXiv, un atelier, la fin du plan 2 × 2 et G1. Que coupes-tu en premier, concrètement ? »
- **Lignes qui la provoquent.**
  - l. 9 : G0 tombe au début de la bourse.
  - l. 23–24 : l'article C ne dépendrait pas de la porte de l'article A.
  - l. 112 : les articles A et C partagent organismes et sondes.
  - l. 272–274 : le domaine validé s'arrête à 1 192 jetons.
  - l. 276–279 : l'environnement en construction.
  - l. 284–285 : ce que G0 exige encore.
  - l. 289–297 : le calendrier.
  - l. 321–339 : le tableau des risques, sans ligne pour G0.
- **Pourquoi elle est dure.**
  - La bourse démarre sur une porte non franchie, sans repli écrit.
  - L'indépendance de l'article C est vraie pour les juges (HC1, HC3), fausse pour les sondes (HC2, HC2b, HC4 et une partie de HC5).
  - Le domaine validé du harnais ne couvre pas l'usage prévu.
  - Le mois 4 est surchargé pour une seule personne.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Un état de G0 à jour** depuis le 7 octobre, daté et empreinté : la dose–réponse d'au moins une famille, les sondes comparées au plancher de covariance appariée, une revalidation du harnais sur contextes longs.
  - **Un plan écrit « si G0 échoue ».** Par exemple : bascule sur le scénario minimal, avec un article C limité aux juges ; ou passage à des organismes publics.
  - **Une liste de coupes** ordonnée et chiffrée.
- **Signal d'alarme.**
  - « G0 passera. »
  - Aucun repli.
  - « La longueur de contexte ne change rien. »
  - Le refus de couper.

### Q8. Comment un tiers vérifie-t-il qu'un préenregistrement précède les données ?

- **Question (anglais).** « Your rigour rests on SHA-256 seals. A hash proves that a file has not changed since it was hashed, not when it was hashed. Your repository is private, your counter-readers are instances of one model family, and gate verdicts end with your own sign-off. How can an outsider check that a pre-registration existed before the data? And your record is spotless: 31 of 31 predictions, 0 contrary cells out of 886, 0 failures out of 3,497 quotations. Your own rule says suspiciously clean results trigger an audit. Who audited these, and what did they find? »
- **Traduction.** « Ta rigueur repose sur des sceaux SHA-256. Une empreinte prouve qu'un fichier n'a pas changé depuis qu'on l'a calculée, pas quand on l'a calculée. Ton dépôt est privé, tes contre-lecteurs sont des instances d'une même famille de modèles, et les verdicts de porte finissent par ta propre signature. Comment un tiers peut-il vérifier qu'un préenregistrement existait avant les données ? Et ton bilan est sans tache : 31 prédictions sur 31, 0 cellule contraire sur 886, 0 échec sur 3 497 citations. Ta propre règle dit qu'un résultat trop propre déclenche un audit. Qui a audité ces chiffres, et qu'a-t-il trouvé ? »
- **Lignes qui la provoquent.**
  - l. 26 et l. 89 : 31 sur 31 ; 342 + 544 cellules ; 0 contraire.
  - l. 240–243 : le scellement SHA-256, la contre-lecture par une instance neuve, l'audit des résultats trop propres.
  - l. 249–250 : le verdict soumis à ta signature.
  - l. 267–269 : 3 497 citations, 0 échec.
- **Pourquoi elle est dure.**
  - C'est la promesse distinctive du dossier. Si l'horodatage n'est pas vérifiable par un tiers, la rigueur reste déclarative.
  - Les zéros parfaits appellent l'audit que ta propre règle prévoit.
  - Une vérification de citations par script prouve la transcription, pas la compréhension.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Un dépôt chez un tiers** des empreintes des préenregistrements déjà scellés : dépôt public d'empreintes, enregistrement sur une plateforme de préenregistrement ou horodatage notarié. Et l'engagement de déposer chaque empreinte avant les données.
  - **Le rapport d'audit des résultats propres.** Il doit dire pourquoi 31 sur 31 était attendu : des théorèmes vrais par construction, donc une simulation qui vérifie le code et non la science.
  - **La ventilation des 147 lignes de correction** par type : erreur de fond, de chiffre ou de citation.
- **Signal d'alarme.**
  - « L'empreinte le prouve. »
  - « Des agents l'ont contre-lu. »
  - Aucun dépôt chez un tiers envisagé.
  - Aucun audit des zéros.

### Q9. « Le contexte seul ne suffit pas » : contre quel attaquant ?

- **Question (anglais).** « HC4 predicts a gap of several orders of magnitude between moving a judge and moving a probe that reads the agent, in the context-only regime. But the monitored agent writes its own context: its reasoning and outputs feed its later activations. And the obfuscation work you cite, 2412.09565, if I remember it right, also attacks latent monitors through the input. Which attacker is "context-only" here? How strong is your best context-only optimiser? And how do you put access, queries, compute and success rate on one scale, so as to claim orders of magnitude? »
- **Traduction.** « HC4 prédit un écart de plusieurs ordres de grandeur, dans le régime "contexte seul", entre déplacer un juge et déplacer une sonde qui lit l'agent. Mais l'agent surveillé écrit son propre contexte : son raisonnement et ses sorties nourrissent ses activations suivantes. Et le travail sur l'obscurcissement que tu cites, 2412.09565, si je m'en souviens bien, attaque aussi les moniteurs latents par l'entrée. Quel attaquant est "contexte seul" ici ? Quelle force a ton meilleur optimiseur par le contexte ? Et comment mets-tu l'accès, les requêtes, le calcul et le taux de succès sur une seule échelle, pour parler d'ordres de grandeur ? »
- **Lignes qui la provoquent.**
  - l. 46–48 : « depuis le contexte seul », le décalage est trop faible pour échapper à la sonde.
  - l. 147–151 : Tr, et les travaux qui affaiblissent la prémisse.
  - l. 185–187 : HC2, « robustesse, pas immunité ».
  - l. 194–197 : HC4.
- **Pourquoi elle est dure.**
  - Une sonde « robuste » contre un optimiseur faible n'est pas une sonde robuste. Le résultat négatif (« le contexte ne suffit pas ») ne vaut que ce que vaut l'attaque.
  - « Plusieurs ordres de grandeur » sur des axes sans commune mesure est invérifiable tant que l'unité n'est pas fixée d'avance.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Une échelle d'attaquants écrite**, avec le budget de chaque échelon :
    - la rhétorique de l'agent ;
    - une recherche sur l'invite en N requêtes ;
    - une optimisation par gradient sur les entrées, avec accès à la sonde ;
    - un réglage fin.
  - **Une unité de coût unique** fixée d'avance, par exemple les requêtes ou le calcul nécessaires pour atteindre un décalage cible.
  - **La règle de lecture d'un résultat nul** : « robuste jusqu'à tel budget », jamais « immunisée ».
  - **Une équipe rouge** au moins aussi forte que les attaques publiées.
- **Signal d'alarme.**
  - Seule la rhétorique écrite à la main compte comme attaque par le contexte.
  - Des « ordres de grandeur » obtenus en mélangeant les unités.
  - « L'agent ne contrôle pas ses activations », posé comme une évidence.

### Q10. Que reste-t-il de neuf, et où mènent tes replis ?

- **Question (anglais).** « Your sequential claim is the conjunction of five published pieces, and you have already withdrawn eight others. The blindness result, that a statistic invariant under G cannot see an attack that preserves the multiset up to G, is close to a tautology. And 31 confirmed predictions confirm code against true theorems. What in your theory would surprise an expert in sequential testing? Now look at your pivots. If G1 fails, the main line becomes H8, a correlation across five probe families. If the sequential-probe core is scooped, you pivot to population statistics and data curation, that is Paper B and gate G3, neither funded in the mainline. What do we get in those cases? »
- **Traduction.** « Ta revendication séquentielle est la conjonction de cinq pièces publiées, et tu en as déjà retiré huit autres. Le résultat d'aveuglement, selon lequel une statistique invariante sous G ne voit pas une attaque qui préserve le multiensemble à G près, frôle la tautologie. Et 31 prédictions confirmées confirment du code contre des théorèmes vrais. Qu'est-ce qui, dans ta théorie, surprendrait un spécialiste des tests séquentiels ? Regarde maintenant tes replis. Si G1 échoue, la ligne principale devient H8, une corrélation sur cinq familles de sondes. Si le cœur "sondes séquentielles" est publié par d'autres, tu bascules vers les statistiques de population et la curation de données, c'est-à-dire l'article B et la porte G3, que le principal ne finance ni l'un ni l'autre. Qu'obtenons-nous dans ces cas-là ? »
- **Lignes qui la provoquent.**
  - l. 74–83 : le théorème négatif.
  - l. 84–88 : ce qui est revendiqué, soit l'unification.
  - l. 141–143 : « la conjonction est la revendication ».
  - l. 156–157 et l. 161–162 : H8, repli si G1 échoue.
  - l. 128 : cinq familles de sondes.
  - l. 208 : l'article B est hors de la demande.
  - l. 260–264 : huit pièces retirées.
  - l. 329–330 : le repli en cas de publication externe.
- **Pourquoi elle est dure.**
  - Une nouveauté par conjonction est la plus fragile dans un champ qui publie chaque semaine.
  - Les deux replis principaux tombent l'un sur un effectif dérisoire, l'autre hors du périmètre payé.
- **Ce qui me convaincrait (montré le jour de l'entretien).**
  - **Un énoncé non évident**, dit en une phrase, avec la décision pratique qu'il change. Par exemple : en classe K, sous dépendance positive, la somme monte au-dessus de son taux de faux positifs pendant que le maximum reste dessous ; donc tel agrégateur est à déployer.
  - **Le prix de la validité à tout instant**, chiffré sur un cas.
  - **Un repli « publication externe » interne au principal.** Par exemple : la mesure de δ sur de vraies activations, que personne d'autre n'aura.
  - **H8 avec un effectif qui permette une conclusion** : nombre de sondes, de graines et d'attaques.
- **Signal d'alarme.**
  - « L'unification » présentée comme la contribution principale.
  - L'aveuglement défendu comme un résultat profond.
  - Des replis vers du travail non financé.
  - « Rien de ce que nous revendiquons n'est occupé », répété comme une garantie.

## 2. Les trois affirmations que je crois le moins

1. **HC4, l. 194–197 : « le contexte seul ne suffit pas », avec un écart prévu de « plusieurs ordres de grandeur ».**
   - L'agent surveillé écrit son propre contexte.
   - Les travaux cités par le dossier lui-même affaiblissent la prémisse (l. 149).
   - La prédiction se confirme d'autant plus facilement que l'attaque est faible.
   - L'unité commune aux quatre axes de coût n'est pas définie.

   C'est la prédiction dont la confirmation serait la moins informative.
2. **L. 125–126 : « une sonde d'intention réussit sur les deux » familles.**
   - La famille (ii) est distillée de la famille (i) : une même trace de fabrication peut exister dans les deux.
   - Réussir sur les deux ne distingue donc une intention ni d'un artefact de construction, ni des traits du texte produit.

   Le critère de validité est nécessaire, il n'est pas suffisant.
3. **L. 87–88 : dans notre simulation, l'« énoncé central » du précurseur publié (2606.10456) ne tiendrait pas « pour sa propre construction ».**
   - C'est une affirmation forte contre un travail publié.
   - Elle repose sur une simulation écrite et relue par des agents d'une même famille.
   - Le texte ne dit ni si les auteurs ont été consultés, ni si la reconstruction est fidèle.

   Tant que je n'ai pas vu le code, je l'attribue plus volontiers à une différence de reconstruction qu'à une erreur des auteurs.

Deux autres affirmations m'ont presque fait douter autant :
- le mois 4 (l. 296–297), qui réunit l'article C sur arXiv et à un atelier, la fin du plan 2 × 2 et G1, pour une personne seule ;
- « aucune affirmation revendiquée n'a été trouvée entièrement occupée » (l. 264), dans un champ où huit pièces viennent déjà de tomber.

## 3. Les chiffres que je voudrais voir vérifiés sur leur source

| Ligne | Chiffre | Où le vérifier | Pourquoi |
|---|---|---|---|
| l. 7, 374–388 | 28 160 / 58 630 / 138 600 dollars et les parts du principal | Le tableau du budget | J'ai refait l'arithmétique : les sommes, les 10 % de marge et les parts sont justes. Mais l'ingénieur est à « mi-temps pendant 6 mois » (l. 379), alors que l'article B occupe « les mois 8 à 12 » (l. 304–305), soit 5 mois. |
| l. 26, 89 | 31 prédictions sur 31 ; 342 + 544 cellules ; 0 contraire | Le préenregistrement de la simulation et ses résultats scellés | L'horodatage avant exécution, et ce que « confirmée » veut dire. |
| l. 90–91 | Fausses alertes à 0,21–0,35 et à 0,17 au lieu de 0,05 | Les résultats de la simulation | Les conditions exactes : taille des effets d'épisode, niveau de corrélation entre agents. |
| l. 267–269 | 98 PDF ; 24 rapports ; 3 497 citations ; 0 échec ; 147 lignes de correction | Les rapports de lecture et le script | Ce que le script compare réellement, et la ventilation des 147 corrections. |
| l. 272–274 | H200 ; contextes jusqu'à 1 192 jetons | Le rapport de validation du harnais | Comparer avec la longueur réelle des trajectoires du pilote. |
| l. 276–277 | 18 invites ; 96 articles (64 + 32) | La règle de sélection scellée et le tirage | La graine, et l'absence de retirage. |
| l. 281 | 602 tests | Le dépôt | La couverture, et qui les a écrits. |
| l. 283 | Environ 20 dollars de calcul | Le registre des dépenses et les factures | Cohérence avec une validation sur H200 en plusieurs versions. |
| l. 363–366 | g ≈ 0,70 ; ĉ ≈ 1,46 et 2,94 ; R² = 0,77 / 0,79 ; 30 × 10 ; transfert R² = 0,73 / 0,69 | Le dépôt public de P3 (l. 362) | L'échelle de ĉ n'est pas dite ; vérifier la disjonction des intervalles et la définition du transfert. |
| l. 367 | Moins de 1 % du travail causal pour la direction de la sonde, 68 % pour l'état complet | P3 | La définition du « travail causal ». |
| l. 368–369 | Sycophantie jugée de 61 % à 46,5 % (N = 200) ; Δ = +0,41 ; p = 0,0006 | P3 | L'échelle de Δ, et le test employé. |
| l. 36 | La citation de la page 2 de Terekhov et al. | Le PDF de 2606.08892 | Elle cadre tout le dossier : les auteurs jugent la surveillance moins prometteuse. |
| l. 46–47 | 2609.36490 : évasion bon marché par réglage fin, décalage trop faible depuis le contexte | Le PDF | Le titre (« … from Prior Feedback Alone », l. 409) semble dire autre chose. Vérifier quel régime est « contexte seul ». |
| l. 72–73 | Délai de détection en Θ(γ) au lieu de log γ | Le PDF de 2601.20022 | L'énoncé exact et ses hypothèses. |
| l. 148 | L'apprentissage par renforcement n'échappe pas aux sondes agrégées par maximum ou par attention | Le PDF de 2506.14261 | La portée exacte, et la réserve des auteurs. |
| l. 182 | Panin : poids du conseil « presque binaire dans trois modèles sur cinq » | SSRN 7424179 | Source hors arXiv : provenance et version. |
| l. 192 contre l. 407–408 | 2508.19461 est cité dans le texte mais absent de la liste ; 2508.07805 est dans la liste mais jamais cité | Les deux résumés arXiv | Erreur d'identifiant probable, gênante dans un dossier qui vend sa vérification. |
| l. 153–155 | 2412.01784 (bruit de poids et sous-performance volontaire) ; 2405.05466 (bruit d'activation et faux alignement) | Les PDF | Que les deux résultats disent bien cela. |
| l. 391 | 5 000 dollars ≈ 4 450 euros | Le taux du 7 octobre 2026 | Le taux implicite vaut environ 1,124. |
| l. 394 | 800 à 1 200 heures équivalent A100 ≈ 1 200 à 2 700 dollars | Le devis | Le prix horaire implicite (1,5 à 2,25 dollars) est plausible. Ce volume couvre-t-il l'apprentissage par renforcement contre la sonde et l'effectif de la Q5 ? |
| Toutes | Les identifiants 2026 (2606.*, 2607.*, 2609.36490…) | arXiv | L'existence, le titre et la version citée de chaque identifiant. |

## 4. Ce qui me ferait financer, ou refuser, malgré l'absence de résultat principal

**Le résultat principal annoncé.** C'est la porte G1, à la **fin du mois 4, soit fin mars 2027** (l. 110, 159, 297). L'article C doit paraître sur arXiv le même mois, et sa porte GC tombe à la fin du mois 2, en janvier 2027.

**Je financerais si, le jour de l'entretien, je vois :**
1. **Les sorties du pilote** (l. 278) : quelques paires « honnête / sabotée », avec un sabotage vérifié et chaque action sous le seuil du moniteur par action.
2. **Une dose–réponse de la famille (ii)**, et une sonde au-dessus du plancher de covariance appariée sur un organisme tenu à l'écart, avec son intervalle.
3. **Le préenregistrement de G1.** Il doit prendre la famille (ii) pour organisme décisif, donner la même information aux deux bras, contenir une analyse de puissance, et son empreinte doit être déposée chez un tiers.
4. **Une figure pilote de l'article C** avec des cibles intermédiaires, où ĉ suit la cible et non le plafond.
5. **Le candidat lui-même**, qui dérive le lemme sans notes et raconte une erreur des agents qu'il a attrapée.

**Je refuserais si :**
- la famille (i) compte dans G1, ou la boîte noire est privée du contexte que lit la sonde sans que ce soit dit ;
- il n'y a ni analyse de puissance, ni effectif d'épisodes honnêtes ;
- le candidat ne sait pas expliquer ses propres choix sans les agents ;
- il n'y a aucun repli si G0 échoue ;
- ĉ ne se distingue pas du plafond de l'échelle ;
- l'horodatage est invérifiable, et le candidat refuse de le rendre vérifiable.

## 5. Recommandation provisoire

**Financer sous condition** : le scénario minimal (article C) tout de suite si son préenregistrement comporte des cibles intermédiaires, et le reste du principal une fois G0 franchie, sur présentation d'un préenregistrement de G1 horodaté chez un tiers, doté d'une analyse de puissance et limité à la famille (ii) comme organisme décisif.
