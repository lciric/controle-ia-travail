# Lecture 07 sur source — « LLM Evolutionary Search Strategies Should be Compared by Tokens » (Tal Oved, Roi Pony, Oshri Naparstek, Udi Barzelay, arXiv 2610.23977) — v1

Écrite le 18 novembre 2026 (vers 06:05 UTC). Aucun commit, aucune dépense, aucun résultat sous embargo ouvert. Lecture entière sur PDF : pages 1 à 11 (texte, bibliographie, annexes A à G, tableaux 1 à 9). La figure 2 (p. 7) a été regardée à l'œil sur une image rendue de la page ; les autres figures par leurs légendes. Un compagnon des mêmes auteurs (arXiv 2609.19799) lu en partie sur PDF ; cinq autres travaux lus **par leur notice d'arXiv seulement** (dit à chaque fois ; rien d'eux n'est opposable, R7). Revendication visée : 9 de `revendications-v1.md` (le séquentiel doit battre le meilleur de N tirages indépendants, à budget égal, avant toute voie chère ; source : N-045 v2, énoncés 4 et 6).

## 0. Verdict en trois lignes

1. **Le protocole de la porte est pris, et l'était avant la décision.** Comparer une recherche séquentielle (un modèle réécrit les meilleurs programmes) au meilleur de N tirages indépendants, à coût égal compté en jetons, est fait ici le 13 octobre 2026, douze jours avant N-045 v2 (25 octobre) ; la comparaison elle-même, à nombre de propositions égal, est plus ancienne (compagnon du 17 septembre 2026 ; Gideoni, Risi, Gal, 18 février 2026, notice seulement). Rien à revendiquer sur ce protocole.
2. **L'attente d'un gain n'est pas contredite dans son signe ; elle l'est dans sa taille, sur ce terrain et avec un modèle.** À jetons égaux, avec gpt-5-mini, l'évolution garde un écart de 5 % ou moins sur 12 paires tâche-méthode sur 15 et de 23 à 28 % sur les 3 autres, toutes sur une seule tâche (p. 1 et tableau 2, p. 4) ; avec un troisième modèle l'écart moyen remonte à 1,30 (p. 8). Le mot « contredit » de la table de veille est trop fort : verdict d'ensemble **occupé en partie**.
3. **Le travail ne touche pas l'objet propre de la porte** : pas de familles tenues à l'écart, pas de témoin « un modèle, vote à k », pas de pilote de bruit ni de test A/A, et ce qui se transmet est un programme sous un correcteur fixe, pas la conception d'un organisme de proposeurs et de juges. Sur ces points il est **voisin** — mais deux compagnons les abordent (notices seulement) et restent à lire avant de dire quoi que ce soit de « libre » (R8).

## 1. Source versée

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/lecture-07-arxiv-2610.23977/` (chaque pièce a son compagnon `.sha256`).

| Pièce | Empreinte SHA-256 |
|---|---|
| `arxiv-2610.23977v1.pdf` (11 pages, 338293 octets) | `aa439be406da477b13b21d9c2243d216acf76bcec2b03923236846e0a0058a84` |
| `page-abs-arxiv-2610.23977.html` (page de résumé d'arXiv) | `70f127d7754dfd5e4aeec82e8b42d6309824ab4d821e453975ddbba46cf56c24` |
| `compagnon-arxiv-2609.19799v1.pdf` (mêmes auteurs, 12 pages) | `daaa9353563eca9ca0ced77bb68ce73dc604b96936dafd870ceb4d22af4434a0` |
| `page-abs-arxiv-2609.19799.html`, `-2607.12227.html`, `-2607.04108.html`, `-2610.22466.html`, `-2606.13003.html`, `-2602.16805.html` | dans `adresse.txt` |
| `adresse.txt` (adresses, dates de récupération, versions, jusqu'où lu) | `fb671e0fd25aad1ef1a95adbbe2de76a09a83cec7a0fd61d44d4012f24e938b3` |

Le PDF a la même empreinte que la copie déjà versée par la voie adverse (`../adverse-arxiv-2610.23977v1.pdf`, dont la provenance disait « pages 1, 2, 5, 6 et 7 lues ») : la table de veille le disait « absent du dépôt », il l'était des notes et des registres, pas des sources. Récupération le 18 novembre 2026 entre 05:55 et 05:59 UTC par `curl`, sans contournement ; l'interface `export.arxiv.org/api/query` a répondu 429 et n'a pas été insistée. Documents traités en données : jamais exécutés, lus par `pdftotext` puis Python lancé avec `-I` ; **aucune consigne adressée à un lecteur n'y a été relevée**. Une précision postérieure au scellement de `adresse.txt` : ce fichier dit les figures « non lues à l'œil » ; la figure 2 l'a été ensuite (image de la page 7 rendue par `pdftoppm`, non versée).

## 2. Date de première version

- arXiv 2610.23977 : **une seule version, v1, mardi 13 octobre 2026, 12:47:59 UTC**, déposée par Tal Oved (page de résumé versée). Aucun commentaire, aucun lieu de publication, aucun lien vers du code dans la notice. Aucun dépôt de code propre au travail : pas de premier commit à dater.
- Antériorité de la comparaison, au-delà de ce travail : le compagnon des mêmes auteurs, arXiv 2609.19799 v1, **17 septembre 2026**, trace déjà une ligne « no-evolve best-of-N » (8 000 appels) contre les trois méthodes, comme repère à nombre d'appels égal : « The no-evolve best-of-N line is a reference, not part of the strategy comparison » (légende de la figure 4, p. 7 de ce compagnon). Sa bibliographie (p. 5) cite Gideoni, Risi, Gal, « Simple Baselines are Competitive with Code Evolution », arXiv 2602.16805, v1 **18 février 2026**, v2 12 octobre 2026 (notice versée, PDF non lu), que le travail lu ici **ne cite pas**.
- Décision du programme : N-045 v2, 25 octobre 2026. Elle est donc postérieure aux trois.

## 3. Ce que le travail fait

Il rejoue des journaux d'exécutions d'évolution de programmes par modèle de langue et recompte la comparaison en jetons au lieu de la compter en « propositions » (programmes candidats).

- **Dispositif** (p. 2) : moteur ADRS, modèle gpt-5-mini ; trois méthodes — OpenEvolve (« islands plus archive, population 40 »), EvoX (qui fait co-évoluer sa règle de sélection), AdaEvolve (variante adaptative) ; cinq tâches — trois tâches de systèmes d'ADRS-Bench (PRISM, un ordonnanceur de service de modèles ; Cloudcast, un planificateur de diffusion ; un ordonnancement de transactions) et deux constructions mathématiques (empilement de cercles dans un carré ; problème du triangle de Heilbronn) ; 40 graines indépendantes de 200 itérations par paire tâche-méthode, soit 8 000 propositions par paire et 600 exécutions journalisées. Deux autres modèles en annexe : Claude Haiku 4.5 sur les deux tâches mathématiques (annexe C, p. 6-8), gemini-2.5-flash sur les trois tâches de systèmes (annexe D, p. 8-9) ; 1 200 exécutions en tout (p. 5).
- **Le témoin** (p. 2) : « 8,000 independent programs drawn from the task description alone, with no history or archive, scored by the same evaluator ».
- **Les trois questions de la table de veille.**
  - *L'unité de budget* : les jetons d'invite, de complétion et de raisonnement, sommés sur **tous les appels** qui précèdent un programme, relances et appels de pilotage compris — « a proposal is not one call: retries and the occasional meta-call that a strategy makes to steer itself are charged here » (p. 2-3). Compter les appels ne suffit pas : un appel tardif est un appel plus gros (annexe F, p. 8-9).
  - *Les tâches* : les cinq ci-dessus, chacune optimisée par son score natif `combined_score` (p. 2). Aucune tâche tenue à l'écart.
  - *Ce qui est hérité* : « an evolve prompt carries the current program and part of the archive and both grow as the run proceeds » (p. 1). Le tirage indépendant ne reçoit que la description de la tâche. **Non dit** : si un programme de départ est fourni à l'un des deux côtés.
- **La comparaison à coût égal** (p. 3) : pour un budget B de jetons, k graines se le partagent, chaque courbe est lue à B/k, on prend le meilleur des k, **puis on maximise sur k** ; le choix des k graines parmi 40 est moyenné par statistique d'ordre exacte. Le témoin reçoit B divisé par le coût d'un tirage, et l'espérance de son meilleur est aussi une statistique d'ordre exacte. Tout budget est plafonné à ce que couvre le lot de tirages, « between 28 and 48 million tokens ».
- **L'audit des programmes** (p. 3) : trois des cinq correcteurs acceptent des programmes qui ne font pas la tâche ; les auteurs ré-exécutent les candidats et appliquent le même contrôle de couverture aux deux côtés.

## 4. Les chiffres, lus sur le PDF

- Coût d'une proposition : 23,0 milliers de jetons (OpenEvolve), 27,0 (EvoX), 33,9 (AdaEvolve), de 15,6 à 38,6 selon la paire ; 1,3 à 1,8 appel par proposition (tableau 1 et texte, p. 3). Un tirage indépendant : 4,1 à 6,0 milliers de jetons. Rapport : 4,6 (empilement de cercles), 4,8 (PRISM), 5,8 (Cloudcast), 6,0 (Heilbronn), 7,2 (transactions), moyenne 5,7 (p. 3). Avec le troisième modèle le rapport tombe à 3,3–4,4 (p. 8).
- Évolution divisée par tirages indépendants, à jetons égaux, gpt-5-mini (tableau 2, p. 4 ; intervalles à 95 %, tableau 7, p. 9) : Heilbronn 1,28, 1,27, 1,23 ; Cloudcast 1,05, 1,05, 0,99 ; empilement de cercles 1,04, 1,04, 1,01 ; transactions (après audit) 1,04, 1,02, 1,02 ; PRISM 1,00 trois fois ; moyenne 1,07 contre 1,09 à propositions égales. Une seule paire a un intervalle qui contient la parité (Cloudcast avec OpenEvolve, 0,97–1,12).
- Audit : sur l'ordonnancement de transactions, le meilleur programme « scored 5× the baseline by placing 3 of 300 transactions » ; l'audit fait passer le rapport de 5,06 à 1,02 (p. 3 ; tableau 9, p. 11).
- Haiku 4.5 : 1,01 à 1,07 sur l'empilement de cercles, 1,17 à 1,26 sur Heilbronn (tableau 4, p. 8). gemini-2.5-flash : de 1,06 à 1,59, moyenne 1,30, Cloudcast 1,53–1,59 (tableau 6, p. 9 ; texte p. 8).
- Fenêtre : « evolution is measured using about a fifth of its logged corpus. Its curves are still rising there, so the window favours sampling and our margins are lower bounds » (p. 5 ; même phrase p. 4). Gain du dernier doublement du nombre de tirages : +0,00 % (cercles), +0,38 % (PRISM), +0,44 % (transactions), +1,37 % (Heilbronn), +3,63 % (Cloudcast) (p. 4).

Les quatre chiffres repris par la voie adverse (600 exécutions, environ six tirages pour une proposition, 5 % ou moins sur 12 paires sur 15, fenêtre favorable aux tirages) sont **confirmés sur le PDF**, pages 1, 3, 4 et 5.

## 5. Lecture dure, dans les deux sens

### 5.1 Ce qui va contre l'attente d'un gain : est-ce solide ?

- **Le compte en jetons fait peu ; l'audit et le témoin font presque tout.** La moyenne passe de 1,085 à propositions égales à 1,069 à jetons égaux (p. 9) : le changement d'unité retire environ un cinquième de l'avantage moyen au-dessus de la parité [calcul de moi : 0,016 sur 0,085]. À propositions égales déjà, après audit, 11 paires sur 15 sont à 1,05 ou moins [décompte de moi sur la colonne « prop. » du tableau 2] ; les jetons en ajoutent une. La phrase du résumé, « the performance margin justifying these systems is often an accounting artifact », dépasse donc ses propres tableaux. Le fait qui pèse contre l'attente est plus simple et plus fort que le titre : **un témoin de tirages indépendants bien fait égale presque l'évolution sur quatre tâches sur cinq, quelle que soit l'unité**, une fois les programmes tricheurs écartés.
- **« 5 % ou moins » est une estimation ponctuelle.** Deux des paires de Cloudcast ont des intervalles qui montent à 1,19 et 1,18 (tableau 7, p. 9). Les paires dont l'intervalle entier ne dépasse pas 1,06 sont neuf [décompte de moi], pas douze.
- **Le rapport est un rapport de scores bruts**, sans échelle commune entre tâches et sans rapport à la marge de progrès disponible : « 4 % » sur une somme de rayons et « 4 % » sur un débit ne se comparent pas. Le seuil de 5 % est choisi par les auteurs, sans justification.
- **Le résultat dépend du modèle**, les auteurs le disent : « the same task pays very differently on a different model […] how much search is worth is not settled by either » (p. 8).

### 5.2 Ce qui nous arrange : vérifié plus durement (R8)

- **Le signe en faveur du séquentiel est fragile là où l'écart est petit.** Le côté « évolution » est maximisé après coup sur le nombre de graines k (p. 3) ; le témoin n'a pas ce degré de liberté. Un maximum pris sur des espérances estimées avec 40 graines est optimiste [inférence de moi ; le document ne mesure pas ce biais]. Des bornes basses à 1,0009 (PRISM, légende du tableau 7, p. 9) ou 1,00 à 1,02 ne prouvent pas un gain.
- **« Nos marges sont des bornes basses » est affirmé plus que mesuré.** La saturation du témoin est chiffrée (dernier doublement, p. 4) ; la hausse de l'évolution au bord de la fenêtre ne l'est pas. À l'œil sur la figure 2 (p. 7, axe des jetons logarithmique) : sur PRISM, les trois courbes d'évolution sont plates dès le premier million de jetons et c'est le témoin qui monte encore et les rejoint ; sur Cloudcast, le témoin monte encore nettement au bord droit (+3,63 % au dernier doublement) pendant que deux des trois courbes d'évolution ne montent presque plus au-delà d'une dizaine de millions de jetons. L'affirmation tient à l'œil pour les transactions, Heilbronn et une méthode sur l'empilement de cercles ; **pas pour PRISM ni Cloudcast** [lecture graphique de moi, sans chiffre].
- **Le troisième modèle, qui remonte l'écart à 1,30, est le résultat le moins documenté** : pas d'intervalles, pas de taille du lot de tirages valides, trois tâches seulement (tableau 6, p. 9).
- **Avantage de la recherche ou avantage de partir d'un programme valide ?** Avec Haiku, sur Heilbronn — la tâche où l'évolution gagne le plus — seuls 1 612 tirages sur 8 000 donnent un programme valide (p. 7) ; avec gpt-5-mini sur Cloudcast, 4 898 sur 8 000 (p. 5). Le document ne sépare pas « l'édition d'un bon programme paie » (p. 4-5, explication donnée sans essai) de « un tirage sans historique échoue souvent à produire un programme valide » [question de moi].
- **Le bras séquentiel est lui-même un meilleur de k lignées indépendantes.** Dans trois paires le meilleur partage est k = 40, la largeur maximale (annexe E, p. 8) ; le compagnon dit que « depth saturates early » et que la meilleure profondeur est « often well short of the full two hundred iterations » (2609.19799, p. 3, texte et légende de la figure 2). Ce que le travail compare n'est donc pas « une lignée contre N tirages » mais « k lignées courtes contre N tirages » : une part du gain du côté séquentiel est déjà un gain de tirages indépendants.
- **Aucune mesure de généralisation.** Le score lu est celui du correcteur qui a servi à choisir, et l'on prend un maximum ; l'audit n'écarte que les tricheries que les auteurs ont su reconnaître (une sur Cloudcast n'est visible que par comparaison de graphes, p. 4). Rien ne dit ce que valent les gagnants hors de la tâche.

## 6. Verdicts sur la revendication 9

**D'ensemble : occupé en partie.** Trois composantes :

| Composante de la revendication 9 | Verdict | Preuve |
|---|---|---|
| Le protocole : séquentiel contre meilleur de N tirages indépendants, à budget égal | **occupé** (dans l'évolution de programmes ; antérieur à N-045 v2) | p. 2, contributions : « The comparison against independent sampling redone at equal token cost, with exact order statistics on both sides » ; p. 2 : « This is the control used in prior work (Oved et al., 2026); our contribution is to charge both sides the same way » |
| L'issue attendue : le séquentiel bat le meilleur de N à budget égal | **occupé en partie** — déjà mesurée sur un terrain voisin, réponse « selon la tâche et le modèle » ; le signe n'est pas contredit, la taille l'est avec un modèle sur quatre tâches sur cinq | p. 4-5 : « evolutionary search beat independent sampling by 5% or less on 12 of 15 pairs, and by 23–28% on the other 3, all Heilbronn. The difference was the task rather than the method » ; p. 8 : « the mean ratio is 1.30 at equal tokens against 1.07 on gpt-5-mini » |
| L'objet et les gardes de la porte : apprentissage de la conception d'un organisme de génération en génération ; familles tenues à l'écart ; témoin « un modèle, vote à k, coût apparié » ; pilote de bruit et test A/A | **voisin** — absents du travail lu | p. 2 : toute tâche est « optimized through its native combined_score » et lue sur ce même score ; aucun des mots « held-out », « vote », « majority » n'apparaît dans les 11 pages ; les intervalles par rééchantillonnage (annexe E, p. 8) ne sont pas un test A/A |

Ce que la troisième ligne ne permet **pas** de dire : que ces gardes soient libres dans le champ. D'après leurs notices seulement (non opposable) : Wang et al. (arXiv 2607.12227, v1 14 juillet 2026) comparent l'évolution de harnais à des témoins simples « under matched feedback and inference budgets » **et** sur tâches tenues à l'écart, avec une issue selon le terrain (pas de gain sur Terminal-Bench 2.1, gain sur des jeux à horizon long) ; Ding et al. (2610.22466, 15 octobre 2026) décomposent le gain d'une évolution de harnais en surajustement, calcul ajouté et reste ; Jwalapuram et al. (2606.13003, 11 juin 2026) opposent des systèmes à plusieurs agents conçus automatiquement à un seul modèle avec vote par auto-cohérence ; Gideoni, Risi, Gal (2602.16805, 18 février 2026) disent qu'en conception de harnais d'agents un simple vote majoritaire fait mieux que toutes les recherches automatiques ; Pan Li (2607.04108, 5 juillet 2026) dit l'évolution conditionnée par les parents « indistinguishable from fresh independent sampling » à nombre d'appels égal en découverte d'équations. **Les gardes de la porte — familles tenues à l'écart, témoin à vote — sont donc très probablement prises elles aussi** ; à lire sur PDF avant toute phrase publique (2607.12227 et 2602.16805 d'abord).

Hors de la revendication visée, une ligne : la revendication 11 (surajustement adaptatif) reçoit ici un appui empirique de plus — « taking the maximum over many runs is how you find the exploits » (p. 2) ; dans la pire graine de l'ordonnancement de transactions, « the top 69 distinct programs are identical exploits » (p. 4).

## 7. Ce qui est mesuré, ce qui est affirmé

- **Mesuré** : le coût en jetons d'une proposition et d'un tirage, par méthode, par tâche et pour trois modèles (tableaux 1, 3, 5) ; les rapports évolution sur tirages à trois unités de budget (tableaux 2 et 8), avec intervalles pour gpt-5-mini seulement (tableau 7 ; 2 000 répliques qui rééchantillonnent les deux côtés, sous-échantillonnage de 20 sur 40 quand le meilleur k vaut 40, annexe E) ; l'effet de l'audit par ré-exécution (tableau 9).
- **Sur quoi, jugé par qui** : cinq tâches d'optimisation de programmes ; le juge est le correcteur programmé de chaque tâche, complété par les contrôles de couverture écrits par les auteurs. Aucun juge humain, aucun juge modèle, aucune vérité tenue à l'écart.
- **Affirmé sans mesure** : que les marges sont des bornes basses (§ 5.2) ; que Heilbronn « has a long improvement path where editing a good program keeps paying » (p. 4, explication sans essai) ; que l'écart est « a property of the task and not of the model » (légende du tableau 4, p. 8), que l'annexe D dément ensuite.
- **Données et code** : rien de publié. L'annexe A (p. 6) dit seulement que tout tourne sur SkyDiscover, « an open framework », ce qui « keeps our pipeline reproducible » ; ni les journaux, ni les lots de tirages, ni les scripts de rejeu ne sont accessibles. Les chiffres ne sont pas vérifiables par un tiers à ce jour.

## 8. Limites

- Celles que les auteurs disent (p. 5) : quinze paires, pas une distribution large ; un modèle principal ; fenêtre plafonnée par la taille du lot de tirages ; coûts en jetons, pas en dollars.
- Celles que j'ajoute : document court (moins de cinq pages de texte principal), sans lieu de publication annoncé dans la notice ; le budget de la colonne « à propositions égales » n'est pas défini avec précision ; il n'est pas dit si un tirage en erreur compte comme un essai dans la statistique d'ordre du témoin (le coût est donné « per attempt », p. 7) ; le coût d'une paire est dit de « 108–309 million tokens » (p. 3) alors que 8 000 propositions au coût minimal annoncé donnent 125 millions [calcul de moi], écart non expliqué par le document ; la couleur de chaque méthode sur la figure 2 n'a pas été identifiée, d'où l'absence de nom dans ma lecture graphique.
- De ma lecture : les compagnons autres que 2609.19799 ne sont connus que par leur notice ; le compagnon 2609.19799 n'est lu en entier que pour son texte principal (p. 1 à 5).

## 9. Une idée à prendre

**Écrire dans le préenregistrement de la porte « le séquentiel bat le meilleur de N » (N-045 v2, énoncé 4) ce que « à budget égal » veut dire et comment le témoin est payé — six lignes gelées avant la course, sans dépense.**

1. *Unité* : le budget se compte en jetons facturés (invite, complétion, raisonnement), sommés sur tous les appels du bras, relances et appels de pilotage compris, lus dans le journal des appels — jamais en générations, en propositions ni en appels (p. 2-3 ; annexe F). Comme l'organisme mêle plusieurs modèles, le compte se tient par modèle et se convertit en dollars à un barème gelé (ce que N-045 v2, énoncé 2, consigne déjà : il manque seulement de dire que c'est **cette** grandeur qui apparie les bras).
2. *Taille du témoin* : N = budget du bras séquentiel divisé par le coût mesuré d'un tirage indépendant, et non N = nombre de générations. Dans le travail lu cela donne 4,6 à 7,2 fois plus de tirages que de propositions (p. 3) ; une génération qui hérite d'un historique croissant coûtera de même plusieurs tirages.
3. *Nombre de lignées* : le nombre k de lignées du bras séquentiel est gelé d'avance, ou choisi sur une moitié des graines et lu sur l'autre — jamais maximisé sur les données lues (§ 5.2).
4. *Même contrôle de validité sur les deux bras avant de prendre un maximum*, et lecture sur la part tenue à l'écart (N-049, N-050) : prendre le meilleur de beaucoup, c'est sélectionner les tricheries du correcteur (p. 2, p. 10).
5. *Qui la fenêtre favorise* : rapporter le gain du dernier doublement du budget **pour chacun des deux bras** (le travail lu ne le donne que pour le témoin, p. 4).
6. *Calcul* : espérance du meilleur de k parmi n graines journalisées par statistique d'ordre exacte, sans bruit de rééchantillonnage (p. 3 ; la formule, Σ x₍ᵢ₎·C(i−1, k−1)/C(n, k) pour i de k à n sur les valeurs triées, est de moi, le document ne l'écrit pas) ; intervalle par rééchantillonnage des deux côtés, par sous-échantillonnage quand k = n (annexe E, p. 8).

Premier pas possible sur processeur, sans ouvrir aucun score : relire les **comptes de jetons** des journaux d'appels des courses passées pour mesurer ce que coûte une génération selon son rang, et en déduire le N que la porte devra payer au témoin (devis à soumettre à Lazar avant tout tirage).

En second, à peser : un bras « départ valide sans héritage » — des tirages indépendants qui reçoivent le même matériau de départ que la première génération — pour séparer l'avantage de l'héritage de l'avantage de partir d'un objet valide (§ 5.2, taux de validité p. 5 et 7). Il demande des appels : sur devis seulement.

## 10. À signaler au directeur de la veille

- Gideoni, Risi, Gal, arXiv 2602.16805 (18 février 2026), **absent des notes et des registres du dépôt** (recherche par nom et par identifiant dans `docs/notes`, `docs/decisions`, `registres/veille.md`) : antécédent probable de la revendication 9 **et** du témoin à vote ; à lire sur PDF.
- La ligne 7 de `table-fusionnee-v1.md` dit « contredit l'attente » : après lecture, « prend le protocole ; issue selon la tâche et le modèle, écart faible avec un modèle sur quatre tâches sur cinq » est plus juste.
- La recherche bibliographique que N-045 v2 exige avant de revendiquer est donc, pour l'énoncé 4, conclue dans le sens non flatteur : la porte est une **pratique publiée à citer**, pas une idée à revendiquer. Dire cela à Lazar relève de sa décision (modification de revendication) ; cette note ne change rien au programme.
