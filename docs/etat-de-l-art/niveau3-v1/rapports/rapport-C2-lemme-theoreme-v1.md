# Rapport C2 — lemme d'additivité (L) et théorème négatif (T) : antériorité sur PDF — v1

Lot C2 de l'état de l'art, niveau 3. Lecteur neuf (il n'a écrit ni la note mathématique, ni les décisions, ni les rapports antérieurs).
Heure de fin de lecture relevée par `date -u` : 2026-11-10, 10:52 UTC.
Consigne commune lue en entier : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`.

## 0. Verdict en tête

**Pas de collision entière.** Aucune des sept pièces lues n'occupe en entier ce que le programme revendique encore pour L ou pour T.

- **L : occupé en partie.** Quatre morceaux sont pris, chacun par une pièce différente, toujours en boîte noire : borne supérieure par la divergence (2608.02698, p. 5) ; calibrage du seuil sur le maximum d'épisodes entiers quand l'inégalité de Ville ne tient plus (2512.03109, p. 4 et 8) ; dommage cumulé avant détection et nécessité d'un détecteur de rupture (2601.20022, p. 4, 10, 11) ; effondrement du maximum quand le dommage s'étale, la moyenne restant plate (2606.10456, p. 6 et 8, en simulation). Restent libres dans les pièces lues : l'invariance exacte à la répartition (temps, agents), la borne toujours valide fonction du seul budget, le coût chiffré du report, et la mesure sur activations.
- **T : occupé en partie.** Le contraste marginale contre corrélation dans le temps, en boîte noire, pour un seul agent, est pris par 2606.10456 (p. 1 à 4), y compris l'idée « fonction du multi-ensemble, donc aveugle » (p. 1) et un adversaire adaptatif contre l'autocorrélation dans une forme à un paramètre (p. 6-7). La moitié négative entre agents est prise par 2607.11751 (p. 3 et 10). Restent libres dans les pièces lues : la distinction entre préserver le multi-ensemble (classe C) et préserver les marginales (classe K) avec ses signes, l'impossibilité exacte par rebrassage sur un groupe (T2), les garanties trajectorielles des statistiques locales, l'écriture commune du temps et des agents, la mesure sur activations.

**Trois contre-résultats défavorables au programme** (détail en sections 2, 3 et 5) :

1. La phrase du texte envoyé au fonds, « its central statement does not hold for its own construction », est **tracée et exacte sur le fond, mais trop forte telle qu'elle est écrite** : elle ne vaut que pour la somme (ou la moyenne), pas pour le maximum ; l'écart au point phare de l'article est petit (0,072 contre 0,05) ; et la proposition 1 de l'article, prise à la lettre, est vide plutôt que fausse. C'est la proposition 2 (a) qui est fausse pour la construction.
2. Le texte envoyé revendique que les statistiques d'ordre globales « can be neutralised by an adaptive attacker ». 2606.10456 montre déjà, en simulation, un attaquant adaptatif qui fait tomber le détecteur d'autocorrélation près du hasard (p. 6-7). Le mécanisme diffère (il baisse la corrélation au lieu de réarranger), mais la phrase du programme ne dit pas cette différence.
3. « Validité sous dépendance » figure dans la revendication de L (décision N-004). La parade retenue (seuil réglé sur des épisodes honnêtes entiers) est la méthode publiée par 2512.03109 (p. 4), qui constate aussi l'échec de l'inégalité de Ville hors de ses hypothèses (p. 8). Ce morceau est à citer, pas à revendiquer.

**Réserve (R4).** Le tableau « libre » de la section 4 est propre surtout parce que les sept pièces sont étroites. Les composantes libres les plus séduisantes (invariance à la répartition, aveuglement par invariance, rebrassage sur un groupe) sont aussi les plus élémentaires : une ligne d'algèbre ou le principe d'invariance des tests. « Libre » veut dire ici « non trouvé dans les sept pièces lues », rien de plus (R8). Les sources classiques qui pourraient les occuper ne sont pas dans le dépôt (section 7).

## 1. Ce qui a été lu, et comment

Énoncés du programme : `docs/programme-controle-ia-v2.md` § 3 (2fd63badb5af…) ; `docs/decisions/decision-N-003-N-004-v1.md` (cc1be39369bc…) ; `docs/decisions/decision-P-008-v1.md` (ac9551b044c1…) ; `docs/notes/note-mathematique-lemme-theoreme-v3.md` en entier (dfe4fe0fc4d0…) ; texte envoyé, lignes 60 à 95 (`proposal_v2_TAIF_2026-10-07.txt`, b2458c2d209a…) ; `docs/notes/resultats-T0.3-v1.md`, lignes 70 à 95 (9ab618edae17…) ; rapport antérieur `docs/sources/lecture-pdf-niveau1/rapport-2606.10456-v1.md` (9a99fb81f649…).

PDF (dossier `docs/sources/pdf/`, empreintes compagnon vérifiées par `sha256sum`) :

| Pièce | Empreinte | Pages | Étendue de ma lecture |
|---|---|---|---|
| 2606.10456v2 | aaeedd1e7a88… | 11 | en entier |
| 2601.20022v2 | 8d090f3171ef… | 34 | p. 1 à 12 en entier (corps de l'article) ; annexes de preuves p. 12 à 33 parcourues par mots-clés seulement ; références p. 34 lues |
| 2608.02698v1 | 452ae117a681… | 10 | p. 3 à 8 en entier ; p. 1, 2, 9, 10 par mots-clés |
| 2607.11751v1 | eef30ef62b96… | 16 | p. 1 à 4, 7, 8, 10 en entier ; le reste par mots-clés |
| 2208.07610v2 | e9e5fd4e0096… | 31 | p. 1 à 3 en entier ; p. 6, 8 en partie ; le reste par mots-clés |
| 2005.07821v1 | e1532df64652… | 7 | p. 1, 2, 5 en entier ; le reste par mots-clés |
| 2512.03109v2 | b7a46e4cf781… | 27 | p. 1 à 4, 10 en entier ; p. 5 à 8 en partie ; le reste par mots-clés |

**Écart à la consigne du lot, signalé** : seule 2606.10456 a été lue en entier, ligne à ligne. Pour les six autres, les pages qui portent les énoncés ont été lues en entier ; le reste a été balayé par mots-clés (« permutation », « exchangeable », « budget », « activation », « adversary », « multi-agent », etc.). Un énoncé pertinent placé dans une annexe non lue ligne à ligne reste possible.

Lecture par `pdftotext`. Pour les articles sur deux colonnes, la sortie `-layout` mêle les colonnes : le contrôle des citations accepte la page lue avec ou sans `-layout`, espaces et césures normalisés.

**Contrôle des citations.** Script `verif.py` (dossier temporaire du lot). Essai préalable (R5) : citation juste acceptée, citation altérée d'un caractère refusée, citation juste sur une mauvaise page refusée. Le contrôle a aussi attrapé une erreur de page de ma part (citation A22, p. 8 corrigée en p. 6). Compte final : **60 citations contrôlées, 0 échec** (annexe A).

## 2. 2606.10456 — l'antécédent du contraste marginale contre corrélation

### 2.1 Son énoncé central

L'article contient deux propositions et quatre définitions (p. 2 à 4). Son énoncé central est la **proposition 1 (« Monitor-A impotence »), p. 3** [A6] : tout moniteur dont la règle ne dépend que de la fonction de répartition empirique des scores a une puissance égale à son taux de faux positifs contre toute attaque à budget de furtivité nul.

Hypothèses :
- la furtivité est une distance de Kolmogorov-Smirnov entre la marginale **empirique** de la trajectoire attaquée et la marginale bénigne [A5] ;
- budget nul veut dire égalité exacte ; la preuve tient en une phrase [A7] ;
- la marginale bénigne est une loi normale centrée réduite [A8] ; un seul agent, T pas [A3] ; un score scalaire par pas [A17].

L'application à la construction de l'article (copule gaussienne autorégressive d'ordre 1, paramètre relevé de 0,5 à 0,59 [A20], T = 300 [A11]) est la **proposition 2 (a), p. 4** [A9], [A10]. Le résumé et la conclusion la reprennent : les moniteurs de moyenne, de maximum, de queue et de seuil sont « defeated by construction » [A2], « provably blind » [A18].

L'article se présente comme le premier traitement formel de cet écart [A21]. Il rattache lui-même le contraste à la décomposition de Sklar [A4].

### 2.2 La phrase du texte envoyé est-elle soutenue ?

Phrase : « In our simulation, its central statement does not hold for its own construction. »

**Traçage dans le dépôt** (recherche `git grep -n '2606.10456'` sur les chemins donnés) :
- `docs/notes/resultats-T0.3-v1.md`, lignes 81 à 89 : sur la construction de l'article (paramètre honnête 0,5, T = 300), au niveau 0,05, la somme rejette à 0,072 / 0,126 / 0,253 pour un paramètre attaqué de 0,59 / 0,725 / 0,9 ; le maximum à 0,048 / 0,044 / 0,027 ;
- `docs/notes/note-mathematique-lemme-theoreme-v3.md`, ligne 107 (même chiffres) et ligne 172 ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`, lignes 75, 109, 122, 157, 158 ;
- décision N-003, section « Antériorité ».

La phrase est donc **tracée**. Je n'ai pas ouvert `diag/` (interdit) : je n'ai pas vu les sorties brutes du run.

**Vérification indépendante, par calcul (le mien, pas un chiffre d'auteur).** Avec une marginale normale, la somme d'une suite autorégressive gaussienne est exactement gaussienne ; sa variance se calcule en forme close. Script `calcul_somme_ar1.py` (dossier temporaire). Test unilatéral sur la somme, seuil réglé sous le paramètre 0,5, T = 300 :

| Paramètre attaqué | Rapport des écarts-types | Puissance au niveau 0,05 | Puissance au niveau 0,01 |
|---|---|---|---|
| 0,59 (point phare de l'article) | 1,136 | 0,074 | 0,020 |
| 0,725 | 1,442 | 0,127 | 0,053 |
| 0,9 | 2,482 | 0,254 | 0,174 |

Ces valeurs recoupent celles de T0.3 (0,072 / 0,126 / 0,253). Le fait ne dépend donc pas d'une simulation : c'est de l'arithmétique sur la construction publiée. Le tableau 2 de l'article donne lui-même 0,048 pour la moyenne au niveau 0,01, lu par les auteurs comme « indistinguishable from the nominal FPR » [A12].

**Jugement : exacte sur le fond, tracée, mais trop forte dans sa forme.** Quatre nuances manquent :
1. Elle ne vaut que pour **la somme ou la moyenne**. Pour le maximum, l'énoncé de l'article tient, et même par excès (0,027 à 0,048, sous 0,05). La note v3 le dit (ligne 107) ; le texte envoyé ne le dit pas.
2. **L'écart est petit au point que l'article met en avant** : 0,072 (ou 0,074 par calcul) contre 0,05 à l'écart 0,09. Il n'est grand (0,25) qu'à l'écart 0,40, borne haute du balayage de l'article [A15].
3. **La proposition 1, à la lettre, est vide plutôt que fausse** : elle suppose l'égalité de la marginale empirique avec une loi continue, ce que nulle trajectoire finie ne réalise (rapport de niveau 1, section 3 ; raisonnement que je refais et confirme). L'énoncé qui « ne tient pas pour sa propre construction » est la **proposition 2 (a)** [A9], et les phrases du résumé [A2] et de la conclusion [A18].
4. « In our simulation » sous-vend et expose à la fois : un calcul en forme close suffit, et il est plus difficile à contester qu'une simulation.

Forme que les pièces soutiennent sans réserve : « pour sa propre construction, l'énoncé d'aveuglement de l'article est faux pour la moyenne et la somme (taux de rejet de 0,07 à 0,25 au niveau 0,05, par calcul exact et par simulation), et vrai, par excès, pour le maximum ». Je ne modifie aucun document ; la reformulation éventuelle est une décision du directeur.

### 2.3 Trois questions de la consigne

- **Plusieurs agents ?** Non. Un agent, T pas [A3]. Aucune statistique entre agents. Recherche de « multi-agent » dans le texte extrait des 11 pages : aucune occurrence.
- **Activations internes ?** Non. Un score scalaire de moniteur par pas [A17]. Les traces dites réelles sont des scores d'un modèle moniteur sur des plans (p. 8), pas des activations.
- **Adversaire adaptatif contre les statistiques d'autocorrélation ?** **Oui, dans une forme restreinte.** Section 5.5 (p. 6-7), figure 6 (p. 9) : un attaquant qui sait qu'un moniteur de corrélation est déployé baisse son paramètre [A13] ; l'aire sous la courbe du détecteur d'autocorrélation tombe de 1,00 à 0,56 [A15] ; conclusion des auteurs : un attaquant patient échappe même au moniteur de corrélation [A14]. Limites : un seul paramètre, construction synthétique seulement [A16], pas de réarrangement à multi-ensemble fixé, pas de dommage structuré imposé, pas de comparaison avec des statistiques locales.

### 2.4 Ce qu'il occupe, ce qu'il n'occupe pas

Occupé (boîte noire, synthétique, un agent, temps) :
- l'énoncé du contraste : les statistiques de marginales sont des fonctions du multi-ensemble des scores, sans ordre [A1], et un attaquant qui tient la marginale les défait ; la parade est une statistique de corrélation temporelle (p. 3-4) ;
- la démonstration par simulation d'une bande où les unes sont au hasard et les autres détectent (p. 6-7) ;
- l'adversaire adaptatif à un paramètre contre l'autocorrélation (ci-dessus) ;
- une illustration du maximum qui s'effondre quand le dommage s'étale, la moyenne restant proche du hasard (tableau 3, p. 8 [A19] ; [A22]), sous une attaque que le rapport de niveau 1 dit différente de l'attaque à marginale préservée (d'après le code, non relu ici).

Non trouvé dans l'article : la séparation entre préserver le multi-ensemble et préserver les marginales (l'article passe de l'un [A1], [A5] à l'autre [A2] sans le voir, et c'est la source de son erreur) ; les signes sous dépendance positive ; toute impossibilité exacte ; toute garantie trajectorielle ; les processus à garantie toujours valide ; l'invariance au budget ; plusieurs agents ; les activations.

## 3. 2601.20022 — adversaire couvert

**Énoncé exact.** Détection de rupture au plus vite, observations indépendantes [B3], loi après rupture stationnaire choisie par un adversaire qui connaît le paramètre γ de la contrainte de fausses alarmes [B1]. Critère de Lorden ; la procédure de somme cumulée de Page est optimale (p. 4). L'adversaire est dit couvert si le délai optimal au pire cas est d'ordre Θ(γ) [B4], au lieu de log γ dans le cadre classique [B2]. Résultat principal : proposition 3.3 (p. 8), trois régimes selon la limite de γ·D(q‖q_γ) ; corollaire 3.1 (p. 9) : le plus grand ordre est atteint quand ce produit tend vers une constante, et c'est la couverture [B5]. Les résultats valent sous deux conditions de dépassement évanescent (conditions (6)-(7), p. 5), vérifiées pour les lois normales et exponentielles (propositions 4.1 et 4.3, p. 10-11). Dommage : proposition 3.4 (p. 10), pour une fonction de dommage puissance d'exposant ρ entre 0 et 1 [B10], le dommage total avant détection a pour plus grand ordre Θ(γ^(1−ρ)) [B6] ; pour un décalage de moyenne, c'est le décalage total de moyenne avant détection [B7], d'ordre racine de γ (p. 11). La conclusion rappelle le cadre stationnaire [B8].

**Fidélité de l'usage par le programme.**
- Le texte du programme § 3 (« si l'on ne contraint que la furtivité par action — d'où l'hypothèse (b) ») **n'est pas fidèle** : l'article ne pose aucune contrainte de furtivité par action et ne déduit aucune borne de budget. La décision P-008 l'a déjà corrigé.
- La lecture retenue par P-008 et la phrase du texte envoyé (« assumes a stationary adversary that knows the false-alarm constraint γ, and covers neither total budgets nor anytime-valid guarantees ») sont **fidèles**, avec deux précisions :
  1. « ne traite pas de budget total » est exact si « budget » veut dire contrainte imposée à l'attaquant. Mais l'article **mesure** un cumul très proche du budget B du programme : le décalage total de moyenne avant détection [B7]. Un lecteur du jury peut relever le raccourci. Formulation sûre : « il ne borne pas le budget ; il chiffre le dommage cumulé avant détection ».
  2. Dans le régime couvert, ce cumul **croît** comme racine de γ. L'hypothèse (b) du programme (budget borné) écarte donc ce régime par construction ; elle n'en est pas la conséquence. P-008 le dit déjà ; c'est le point à tenir devant un jury.
- L'article cite un travail des mêmes auteurs sur un adversaire **non stationnaire** et sur le dommage total, [12] dans sa liste [B9]. Cette pièce n'est pas dans le lot (section 7) : c'est le voisin le plus probable d'un énoncé à budget.

## 4. Décomposition par composante

Légende : « classique » = cité comme tel par une pièce lue, ou connu des manuels (alors marqué « piste, non vérifiée » si aucun PDF du dépôt ne le porte) ; « occupée en partie » avec pièce, page, citation ; « libre » = non trouvé dans les sept pièces lues.

### 4.1 Lemme d'additivité (L)

| Composante | Verdict | Appui |
|---|---|---|
| Borne de mélange (processus à garantie toujours valide par mélange normal, inégalité de Ville) | **classique** | Les pièces lues s'en servent comme d'un acquis : 2512.03109 bâtit sur les processus e et renvoie au manuel de Ramdas et Wang (p. 2, 11) ; 2208.07610 p. 2 [E1]. La source propre (Howard, Ramdas, McAuliffe et Sekhon) n'est pas dans le lot : piste, non vérifiée. |
| Critère sous garantie toujours valide (la puissance n'est pas le bon critère) | **classique, occupée** par 2208.07610 | p. 2 [E1] ; p. 6 [E2]. Auteurs : Pérez-Ortiz, Lardy, de Heide et Grünwald [E5], et non « Koning et Grünwald » (le programme § 3 porte encore l'ancien nom ; P-008 l'a corrigé). L'article ne chiffre aucun écart. |
| Dichotomie somme contre maximum sous fragmentation (L2) | **classique en théorie (piste, non vérifiée), occupée en partie en simulation** | 2606.10456, p. 6 [A22] et tableau 3, p. 8 [A19] : le maximum passe de 1,000 à 0,504 quand le dommage s'étale. 2607.11751, p. 10 : l'agrégation « alarme si l'une » ne gagne qu'en dépensant du taux de faux positifs [D6], [D3]. La théorie des mélanges rares et denses (critique supérieure) n'est pas dans le lot. La forme exacte de L2 (seuil exact, plancher au-dessus de α) n'est dans aucune pièce lue. |
| Borne supérieure de la puissance de tout test par la divergence | **occupée** par 2608.02698 | Proposition 1, p. 5 [C1] ; les auteurs disent eux-mêmes que les inégalités sont classiques [C2]. Forme additive par message : lemme 1, p. 5 [C3], exacte sous indépendance conditionnelle, prudente sous corrélation positive (p. 6 [C7]). Même borne, par pas, dans 2607.11751, p. 3 [D1]. Le programme ne revendique pas cette borne. |
| Invariance terminale au budget total, quelle que soit la répartition dans le temps (L1) | **libre dans les pièces lues ; élémentaire** | Aucune pièce n'énonce que la somme terminale est translatée exactement du budget. Voisins : additivité de la divergence par message (2608.02698, p. 5 [C3]) ; décalage total de moyenne comme mesure du dommage (2601.20022, p. 11 [B7]). L'énoncé tient en une ligne (linéarité de la somme) : sa valeur de nouveauté seule est faible, ce que N-004 reconnaît. |
| Invariance à la répartition entre agents au même pas (L4) | **libre dans les pièces lues ; élémentaire ; non testée** | Aucune pièce ne traite une somme lue aux frontières de pas sur plusieurs agents. 2608.02698 note que l'étalement entre sessions et principaux reste ouvert (p. 8 [C8]), sur des chiffres qui sont des valeurs d'illustration, non mesurées (p. 6 [C6]). |
| Borne inférieure toujours valide fonction du seul budget ; coût chiffré du report ; prix de la garantie toujours valide (L3) | **libre dans les pièces lues** | 2208.07610 pose la différence de critère sans la chiffrer (p. 6 [E2]). 2601.20022 chiffre un délai, sous une autre hypothèse d'adversaire. |
| Sécurité « avant le dommage » : nécessité d'un détecteur de rupture | **classique, occupée en partie** par 2601.20022 | Cadre de Lorden et de Page (p. 3-4) ; dommage cumulé avant détection (p. 4 ; proposition 3.4, p. 10 [B6]). Ce que le programme ajoute (comparaison chiffrée entre processus cumulé depuis l'origine et détecteur de rupture, à budget borné) n'y est pas. |
| Validité hors hypothèses : seuil réglé sur des épisodes honnêtes entiers | **occupée en partie** par 2512.03109 | p. 3 : les scores ne sont pas indépendants d'un pas à l'autre [G2] ; p. 4 : le seuil est le quantile du maximum de la statistique sur des trajectoires entières du jeu de calibrage [G1] (algorithme 1, proposition 1) ; p. 8 : la variante de Ville ne tient que pour des martingales exactes [G3]. Cadre non adverse, boîte noire [G4] ; l'extension à la détection de trajectoires dangereuses est nommée comme suite possible (p. 10 [G5]). Le programme apporte le chiffrage de l'échec sous effet d'épisode et sous corrélation entre agents, pas la méthode. |
| Non-compensation comme condition empirique (L5) | **libre dans les pièces lues** | Voisin lointain : 2005.07821, p. 5 [F1] (une statistique cumulée est aveugle à l'attaque qui préserve ce qu'elle accumule). |
| Mesure sur activations réelles | **libre dans les pièces lues** | 2606.10456 : score scalaire [A17]. 2608.02698 : aucun accès au modèle [C4]. 2512.03109 : vérifieur en boîte noire [G4]. Attention : 2608.02698 cite une approche par activations pour la collusion (NARCBench, p. 8 [C9]), hors de ce lot. |

**Verdict L : occupé en partie.** Pris : les bornes classiques (2608.02698, p. 5 ; 2607.11751, p. 3 et 10), le critère (2208.07610, p. 2 et 6), le calibrage sur épisodes entiers (2512.03109, p. 4), le dommage avant détection (2601.20022, p. 10). Libre dans les pièces lues : l'énoncé adverse à budget fixé (invariances exactes dans le temps et entre agents, borne toujours valide, coût du report) et sa mesure sur des scores de sondes. Ce qui reste libre est élémentaire dans sa partie exacte : la valeur est dans l'assemblage, le chiffrage et la mesure. L'estimation d'originalité « environ 0,4 » de N-004 me paraît un plafond plutôt qu'un plancher.

### 4.2 Théorème négatif (T)

| Composante | Verdict | Appui |
|---|---|---|
| Décomposition marginale et copule | **classique** | Sklar et Nelsen, cités par 2606.10456, p. 1 [A4] et p. 11. |
| Contraste marginale contre corrélation dans le temps, un agent, boîte noire | **occupée** par 2606.10456 | p. 1 [A1], [A2] ; proposition 1, p. 3 [A6] ; proposition 2, p. 4 [A9] ; revendication de priorité p. 2 [A21]. Énoncé défectueux (section 2), mais l'idée et la démonstration par simulation sont antérieures. Le programme ne la revendique plus. |
| Aveuglement des statistiques invariantes sous une attaque qui préserve le multi-ensemble (T1) | **occupée en partie** par 2606.10456 pour le groupe de toutes les permutations du temps ; **classique** dans son principe | L'idée « fonction du multi-ensemble, sans ordre » est écrite p. 1 [A1] ; la définition 2 porte sur la marginale empirique [A5]. La proposition 1, réparée, est T1 pour ce groupe. Le principe général (un test invariant ne voit que l'invariant maximal ; théorème de Hunt et Stein) est rappelé comme classique par 2208.07610, p. 2 [E3], y compris pour des groupes de permutations (p. 8 [E4]). La version par sous-groupe quelconque n'est dans aucune pièce lue. N-003 reconnaît que T1 est élémentaire. |
| Moitié négative entre agents : un moniteur local est aveugle à un dommage qui n'existe qu'après assemblage | **occupée** par 2607.11751 | Proposition 1, p. 3 [D1] ; proposition 2, p. 10 ; et la phrase qui porte le contraste marginale contre joint entre fragments [D2]. Portée : trois fragments dans un épisode [D4] ; horizons longs et attaquants pleinement adaptatifs hors de la revendication [D5]. Non revendiquée par le programme. |
| Impossibilité exacte par rebrassage uniforme sur un groupe sous lequel la loi honnête est invariante (T2) ; « le groupe compte » | **libre dans les pièces lues ; parenté classique** | Aucune pièce ne l'énonce. Voisin : 2608.02698 utilise l'échangeabilité des identités d'agents sous l'hypothèse nulle comme **test** du défenseur (p. 3 [C5]) ; c'est le même objet vu de l'autre côté. T2 est la réciproque immédiate des tests de permutation : piste, non vérifiée, sources à récupérer (section 7). |
| Classes C (multi-ensemble) contre K (marginales par coordonnée) | **libre dans les pièces lues** | 2606.10456 confond les deux ([A1], [A5] contre [A2]) : c'est exactement ce qui sépare le programme de lui. C'est la composante la mieux défendable de T. |
| Signes sous dépendance positive (somme au-dessus de son taux, maximum à son taux ou en dessous) | **libre dans les pièces lues comme énoncé ; outil classique** | L'inégalité de Slepian n'est portée par aucun PDF du lot : piste, non vérifiée. Voisin : 2608.02698, p. 6 [C7] (corrélation positive entre messages, autre objet). Les chiffres de 2606.10456 (tableau 2, p. 7 ; [A12]) montrent déjà le fait sans que les auteurs le lisent. |
| Statistiques d'ordre globales neutralisables par un attaquant adaptatif | **occupée en partie** par 2606.10456 | Section 5.5, p. 6-7 [A13], [A14], [A15]. Forme à un paramètre, synthétique [A16]. La forme du programme (réarrangement à multi-ensemble fixé, dommage structuré imposé) n'y est pas. |
| Garanties trajectorielles des statistiques locales (balayage, Page, co-élévation) face à cet attaquant (T3) | **libre dans les pièces lues** | Les statistiques de balayage et la somme de Page sont classiques ; leur usage comme garantie face à un réarrangement adverse n'est dans aucune pièce lue. 2607.11751 dit seulement que les moniteurs joints échappent à sa borne (p. 10 [D3]). |
| Somme lue séquentiellement sous arrangements dominés (T4) | **libre dans les pièces lues** | — |
| Unification du temps et des agents par des sous-groupes de permutations | **libre dans les pièces lues** | 2606.10456 : temps seul, un agent [A3]. 2607.11751 : fragments entre agents, un épisode [D4]. 2608.02698 : agents et tours, mais permutation des seules identités (p. 3 [C5]). Aucune n'écrit les deux dans un même groupe. Réserve : c'est une mise en forme (échangeabilité par blocs), pas un théorème nouveau ; un statisticien peut la dire connue. |
| Mesure sur activations réelles | **libre dans les pièces lues** | Comme pour L. |

**Verdict T : occupé en partie.** Pris : le contraste dans le temps en boîte noire, l'idée du multi-ensemble et un attaquant adaptatif restreint (2606.10456) ; la moitié négative entre agents (2607.11751) ; le principe d'invariance (classique, rappelé par 2208.07610). Les quatre pièces de la revendication de N-003 ne sont occupées en entier par aucune pièce lue ; mais la troisième (« garanties locales face à un attaquant adaptatif ») touche 2606.10456 par sa moitié « les statistiques globales sont neutralisables », et la première (unification) est une mise en forme.

## 5. Écarts entre le texte envoyé et les pièces

| Passage du texte envoyé | Jugement | Motif |
|---|---|---|
| « its central statement does not hold for its own construction » | exact sur le fond, trop fort dans la forme | section 2.2 |
| « In our simulation » | exact, incomplet | un calcul exact suffit et recoupe (section 2.2) |
| « A black-box, synthetic precursor » | exact | [A17], [A16] ; les traces « réelles » de la p. 8 sont des scores de moniteur, l'attaque reste construite |
| « Global order statistics (autocorrelation, runs) can be neutralised by an adaptive attacker » parmi les apports | à préciser | 2606.10456, p. 6-7, le montre déjà dans une forme à un paramètre (section 2.3) |
| « Thresholds are therefore calibrated on whole honest episodes » | exact, à citer | méthode de 2512.03109, p. 4 [G1] |
| « GROW (Pérez-Ortiz, Lardy, de Heide and Grünwald, arXiv 2208.07610) » | fidèle | [E1], [E2], [E5] |
| « Ramtin, Nain and Towsley … Θ(γ) instead of log γ … covers neither total budgets nor anytime-valid guarantees » | fidèle, une précision | section 3 : l'article chiffre le décalage total avant détection [B7] |
| « The statistical core is classical and cited » | fidèle | [A4], [C2], [E3] |

## 6. Phrase honnête à dire à un jury sur 2606.10456

« Zhang et Gao (juin 2026) ont posé avant nous, pour un seul agent, des scores de moniteur en boîte noire et des trajectoires simulées, l'idée que des statistiques sans ordre sont aveugles à un sabotage logé dans la corrélation temporelle, et ils ont montré en simulation qu'un détecteur de corrélation le voit, y compris face à un attaquant qui baisse sa corrélation. Leur énoncé confond deux choses que nous séparons : préserver le multi-ensemble des scores, où l'aveuglement est exact, et préserver la marginale de chaque pas, où il est faux pour la somme (0,07 à 0,25 de rejet au niveau 0,05 sur leur propre construction) et vrai par excès pour le maximum. Nous leur devons le contraste ; ce qui nous en sépare est cette distinction et ses signes, les garanties des statistiques locales, l'écriture commune du temps et des agents, et surtout la mesure sur les activations d'un modèle, qu'ils n'ont pas. »

## 7. Pièces à récupérer sur le réseau

Aucune n'est dans `docs/sources/pdf/` à ma connaissance (je n'ai vérifié sur disque que les sept pièces du lot). Identifiants de mémoire là où il y en a : **pistes, non vérifiées**.

| Pièce | Pourquoi |
|---|---|
| Ramtin, Hare, Kaplan, Nain, Veeravalli et Towsley, « Quickest Change Detection in the Presence of Covert Adversaries » (référence [12] de 2601.20022, p. 34) | adversaire non stationnaire et « dommage total » [B9] : voisin le plus probable d'un énoncé à budget borné ; collision possible avec L3 |
| Huang, Wang et Poor, « On Covert Communication Against Sequential Change-Point Detection » (référence [6] de 2601.20022) | même loi d'échelle en racine de γ (p. 11) |
| Howard, Ramdas, McAuliffe et Sekhon, frontières à mélange (arXiv 1810.08240, de mémoire) | source propre de la borne de mélange, encore sur transcription selon la note v3 |
| Donoho et Jin, critique supérieure (2004) ; Arias-Castro, Candès et Plan sur les mélanges rares et denses | source classique de la dichotomie somme contre maximum (L2) |
| Lehmann et Romano, « Testing Statistical Hypotheses », sections sur l'invariance (8.5, citée par 2208.07610, p. 2) et sur les tests de randomisation | T1 et T2 : principe d'invariance et réciproque des tests de permutation |
| Ramdas, Ruf, Larsson et Koolen, test séquentiel de l'échangeabilité ; Vovk, tests de l'aléa en ligne | T2 : impossibilité et tests sous échangeabilité, en séquentiel |
| Slepian (1962), ou un manuel qui porte l'inégalité | signes de la classe K |
| Glaz, Naus et Wallenstein, statistiques de balayage | T3 : garanties des statistiques locales |
| NARCBench (référence [29] de 2608.02698) | sondes d'activations pour la collusion entre agents : voisin de « mesure sur activations » côté agents |
| Koning, tests d'invariance de groupe par valeurs e (identifiant non su) | le programme § 3 écrivait « Koning et Grünwald » ; vérifier qu'aucun article de Koning sur l'invariance de groupe n'occupe l'unification par sous-groupes |

## 8. Refus rencontrés

Aucun. Aucun appel au réseau, aucun modèle, aucune machine. `diag/`, `runs/`, `donnees/` non ouverts. Rien d'écrit hors de ce rapport, de son empreinte compagnon et du dossier temporaire du lot.

## Annexe A — citations exactes contrôlées

Format : identifiant | pièce (dans `docs/sources/pdf/`) | page du fichier | citation.

- A1 | 2606.10456v2.pdf | p. 1 | « each is a function of the multiset of per-step scores that ignores their order »
- A2 | 2606.10456v2.pdf | p. 1 | « the per-step monitor- score marginal is held exactly equal to benign, so mean, max, top-k tail, and threshold monitors (Monitor A) are defeated by construction »
- A3 | 2606.10456v2.pdf | p. 1 | « an agent amortizes a fixed harm budget H across T steps »
- A4 | 2606.10456v2.pdf | p. 1 | « This is the natural worst case for monitoring under Sklar’s copula decomposition [17] »
- A5 | 2606.10456v2.pdf | p. 3 | « where F̂att is the empirical marginal CDF of the attack scores »
- A6 | 2606.10456v2.pdf | p. 3 | « Any monitor whose decision rule depends only on F̂att (i.e., a marginal feature) has detection power equal to its false-positive rate against any zero-stealth-budget attack. »
- A7 | 2606.10456v2.pdf | p. 3 | « At ε = 0, F̂att = Fben by definition. »
- A8 | 2606.10456v2.pdf | p. 3 | « Let the benign marginal be Fben = N (0, 1) »
- A9 | 2606.10456v2.pdf | p. 4 | « For any Monitor A (marginal functional), the detection power equals the FPR (by Proposition 1). »
- A10 | 2606.10456v2.pdf | p. 4 | « with ε = 0 (exactly marginal-preserving) »
- A11 | 2606.10456v2.pdf | p. 5 | « Trajectory length T = 300 steps »
- A12 | 2606.10456v2.pdf | p. 6 | « power at 1% FPR ranges from 0.00 (max) to 0.048 (mean), indistinguishable from the nominal FPR »
- A13 | 2606.10456v2.pdf | p. 6 | « A reactive attacker that knows a correlation monitor is deployed will instead drive its stealth parameter δϕ (the AR(1) elevation that encodes distributed harm) as low as possible. »
- A14 | 2606.10456v2.pdf | p. 7 | « a sufficiently patient adaptive attacker (δϕ < δϕ⋆ ) evades even a correlation monitor »
- A15 | 2606.10456v2.pdf | p. 7 | « falls from AUC 1.00 at δϕ =0.40 to 0.56 (near chance) at δϕ =0.02 »
- A16 | 2606.10456v2.pdf | p. 8 | « the adaptive red-teamer (Section 5.5) is evaluated on the synthetic construction »
- A17 | 2606.10456v2.pdf | p. 9 | « our results are an upper bound on Monitor B power under the scalar-score assumption »
- A18 | 2606.10456v2.pdf | p. 9 | « Monitor A (mean/max/threshold/tail) is provably blind to this attack by construction »
- A19 | 2606.10456v2.pdf | p. 8 | « Harm budget H = 2.0, T = 300, stealth= 0.2, FPR target 1%. »
- A20 | 2606.10456v2.pdf | p. 5 | « The attack sets ϕatt = ϕben + 0.09 ≈ 0.59 »
- B1 | 2601.20022v2.pdf | p. 1 | « we consider a covert adversary who has knowledge of the detector’s false alarm constraint parameter γ and selects a stationary post-change distribution that depends on it »
- B2 | 2601.20022v2.pdf | p. 1 | « ADD = Θ(γ), whereas in the classical setting, ADD grows only as O(log γ) »
- B3 | 2601.20022v2.pdf | p. 3 | « Let X1 , X2 , . . . be mutually independent random variables »
- B4 | 2601.20022v2.pdf | p. 4 | « We say that an attacker is covert if n(γ) = Θ(γ) »
- B5 | 2601.20022v2.pdf | p. 9 | « The largest asymptotic order of n(γ) is reached when γD(q||q0 ) = y + o(1) (γ → ∞), and it corresponds to covertness, i.e., n(γ) = Θ(γ). »
- B6 | 2601.20022v2.pdf | p. 10 | « the total damage d(γ) = n(γ)g(D(q||qγ )) has its largest asymptotic order when γD(q||qγ ) = Θ(1), with d(γ) = Θ(γ 1−ρ ). »
- B7 | 2601.20022v2.pdf | p. 11 | « which corresponds to the total mean shift introduced by the adversary prior to detection »
- B8 | 2601.20022v2.pdf | p. 12 | « analyzing the CuSum procedure in a stationary setting where the post-change distribution qγ depends on the false-alarm constraint γ »
- B9 | 2601.20022v2.pdf | p. 2 | « [12] investigates an adversarial setting against the CuSum procedure under non-stationarity, without assuming that the adversary knows the false-alarm constraint parameter »
- B10 | 2601.20022v2.pdf | p. 10 | « Assume g(x) = xρ with ρ ∈ (0, 1) »
- C1 | 2608.02698v1.pdf | p. 5 | « For any decision rule based on the observed traces and operating at false-positive »
- C2 | 2608.02698v1.pdf | p. 5 | « we claim novelty in its application to agent collusion and in the empirical frontier it predicts, not in the underlying inequalities »
- C3 | 2608.02698v1.pdf | p. 5 | « If the monitor observes an independent fraction ρ ∈ (0, 1] of colluder messages, then under an additive per-message decomposition of relative entropy the observable divergence obeys »
- C4 | 2608.02698v1.pdf | p. 3 | « The monitor cannot read weights, activations, gradients, or private prompts of agents operated by other principals. »
- C5 | 2608.02698v1.pdf | p. 3 | « Under H0 , agent identities are exchangeable with respect to outcome; a covert channel breaks this symmetry. »
- C6 | 2608.02698v1.pdf | p. 6 | « All numeric values in Tables III–VI are illustrative placeholders »
- C7 | 2608.02698v1.pdf | p. 6 | « it is exact when colluder messages are conditionally independent given the payload, and conservative—an over-estimate of what the monitor learns—under positive correlation between messages »
- D1 | 2607.11751v1.pdf | p. 3 | « any possibly randomized decision rule that sees only a single local observation v(xi ) has per-fragment detection advantage (true positive rate minus false positive rate) at most ε »
- D2 | 2607.11751v1.pdf | p. 10 | « It observes a different object, and its benign vs. attack TV can be large even when every local marginal TVi is small. »
- D3 | 2607.11751v1.pdf | p. 10 | « This bound applies only to this alarm-if-any aggregation of per-fragment alarms. It does not rule out monitors that score the fragments jointly. »
- D4 | 2607.11751v1.pdf | p. 3 | « Our main experiments use K=3 fragments within a single episode »
- D5 | 2607.11751v1.pdf | p. 3 | « longer horizons, larger or changing K, session-mediated assembly, covert natural-language self-reassembly, full adaptive attackers, and non-code compositional harms remain outside the main claim »
- D6 | 2607.11751v1.pdf | p. 10 | « If the benign flag events are additionally independent and uniformly calibrated, then FPRtraj = 1 − (1 − α)K exactly. »
- E1 | 2208.07610v2.pdf | p. 2 | « anytime-valid testing, while taking place in a sequential setting, is different from classical, Wald-style sequential testing, in which power is meaningful »
- E2 | 2208.07610v2.pdf | p. 6 | « This criterion cannot be used when the stopping rule is unknown because knowledge of the stopping rule is required by the definition of power. »
- E3 | 2208.07610v2.pdf | p. 2 | « a celebrated theorem of Hunt and Stein (Lehmann and Romano, 2005, Section 8.5) shows that, when looking for a test that has max-min power, no loss is incurred by looking only among group- invariant tests »
- E4 | 2208.07610v2.pdf | p. 8 | « assume for now that G is a finite group, for instance, a group of permutations »
- E5 | 2208.07610v2.pdf | p. 1 | « B Y M URIEL F ELIPE P ÉREZ -O RTIZ1,a , T YRON L ARDY2,b R IANNE DE H EIDE3,c AND P ETER D. G RÜNWALD4,d »
- F1 | 2005.07821v1.pdf | p. 5 | « The CUSIGN detector alone may not be sufficient as an attacker can change the magnitude of a measurement, but still maintain random signed behavior of the test measure zk . »
- F2 | 2005.07821v1.pdf | p. 1 | « An intelligent attacker can design stealthy attacks with knowledge of the system model and noise characteristics to evade detection from state-of-the-art fault detectors by remaining within detection thresholds. »
- G1 | 2512.03109v2.pdf | p. 4 | « it suffices to set cα to the (1 − α) quantile of the distribution of maxt Mt under the null »
- G2 | 2512.03109v2.pdf | p. 3 | « black- box verifier scores are generally not independent samples from a fixed distribution at every step »
- G3 | 2512.03109v2.pdf | p. 8 | « randomized Ville controls the false alarm rate only for exact test martingales, not necessarily approximate ones »
- G4 | 2512.03109v2.pdf | p. 1 | « a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates »
- G5 | 2512.03109v2.pdf | p. 10 | « e-valuator can be used for other applications, such as early detection of unsafe or harmful trajectories »
- C8 | 2608.02698v1.pdf | p. 8 | « detecting payloads spread across sessions and principals remains open »
- C9 | 2608.02698v1.pdf | p. 8 | « The interpretability route behind NARCBench [29] reports the best numbers of the three, but it reads model activations »
- D7 | 2607.11751v1.pdf | p. 3 | « The proof, and an alarm-if-any aggregation with the same limit, are in the supplementary material. »
- A21 | 2606.10456v2.pdf | p. 2 | « We differentiate our contribution as the first formal treatment of this gap and the first demonstrated detectability band that separates the marginal family from the correlation family. »
- A22 | 2606.10456v2.pdf | p. 6 | « At spread = 1 (harm concentrated in one step), Monitor A’s max score achieves AUC = 1.0 »
