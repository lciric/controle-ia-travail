# Erratum 1 du programme v3 — le lemme d'additivité, revendiqué dans sa seule application au contrôle de l'intelligence artificielle — v1

Écrit le 2026-11-24 vers 11:15Z (`date -u`). Rédacteur : Claude Fable 5.2, effort maximal, sur la consigne `consigne-fable-enonce-lemme-application-v1.md` du même dossier. Pièce de travail : non scellée, non contre-lue. La décision de Lazar veut une contre-lecture avant tout usage (GO-2026-11-24-18).

**Verdict.** L'énoncé revendiqué tient en trois phrases et cinq hypothèses ; c'est une prévision à éprouver, non un constat. Le programme v3 dit le lemme non revendiqué, ou seulement mentionné, dans sept phrases et non quatre : sept entrées. Pour la forme mesurée, les pièces lues ne suffisent pas à écrire « non trouvé dans les pièces lues » ; la section 3 nomme les lectures qui manquent.

**Lu.** Le programme v3 tel qu'il sera scellé : copie du bloc-notes de la session, empreinte `70df808ada9e67ba766eeb8e091b6ab843b7e83651ce120477e7ad799d7eefb1`. La décision d'octobre sur les énoncés du théorème négatif et du lemme (N-003 et N-004). Sur origin/main, commit `5fd8fc305` : les mots de Lazar des 22 et 24 novembre (GO-2026-11-22-24, -40, -42, -64 ; GO-2026-11-24-18) et les lignes de décision R-4767 à R-4769, R-4771 et R-5265. La seconde lecture de la thèse. La recherche d'antériorité sur la transposition, version 2. Les réponses 9 et 22A de Fable. La contre-lecture de la table des revendications : j'ai lu le fichier entier (57 lignes), non la seule question 3, et j'en tire deux renvois.

**Non lu.** Aucun PDF, aucun résultat. Ni la note de première lecture des six travaux de stéganographie et de comptabilité des matières, ni les décisions sur l'issue et le plancher d'audit (N-075), sur la référence honnête (N-076) et sur le retrait de la marge asymétrique (N-077), ni la table des revendications, ni le complément de la demande 27, ni le programme qui applique les errata.

## 1. L'énoncé revendiqué

> Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions ou d'agents entre lesquels le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, l'énoncé central cité s'applique aux sondes : à déplacement total donné, la somme lue en fin d'épisode est indifférente à la répartition.

**Réfutation.** La conservation est réfutée si le déplacement cumulé monte ou baisse avec la fragmentation au-delà d'une marge fixée au préenregistrement, après calcul de puissance. Le sens de l'écart est alors le résultat ; une issue indéterminée est possible.

**Hypothèses.**
1. *Position.* Le sabotage déplace la position des scores, et ce déplacement croît avec le dommage. S'il est nul à tous les niveaux, l'énoncé est sans objet : la question « position ou dépendance » (Q) décide. S'il ne suit pas le dommage, la conservation ne dit rien du sabotage.
2. *Dommage hors des scores.* Le dommage est celui de l'épisode entier ; il n'a pas à s'additionner fragment par fragment. Il est chiffré, et constaté par la vérité de terrain de l'environnement. Sinon la conservation est circulaire. L'énoncé ne vaut donc que pour un sabotage à dommage chiffré.
3. *Taille fixe.* À tous les niveaux de fragmentation, le nombre n d'actions surveillées, la tâche, le nombre d'agents et la sonde, gelée avant la mesure, sont les mêmes. La référence honnête est déclarée : taille m, dans l'unité de n.
4. *Lecture en fin d'épisode.* Rien n'est dit d'un franchissement séquentiel.
5. *Organismes tels qu'ils sont construits.* Le montage fixe la fragmentation. Rien n'est affirmé d'un saboteur qui choisit sa répartition.

**Ce qui se mesure.** Le déplacement cumulé de chaque paire, puis sa moyenne et sa dispersion, par sonde, par famille d'organismes et par niveau de fragmentation. Le niveau est le nombre d'actions, ou d'agents, qui portent le sabotage. À côté, hors de l'énoncé : le rappel d'une alarme sur la somme, à taux de fausses alertes déclaré ; le maximum par action, qui relève de la question de la transposition du jeton à l'action (Tr) ; la part du déplacement portée par les actions de sabotage. Un déplacement égal sur toutes les actions, quel que soit le dommage, lirait l'état de l'organisme (sa consigne cachée ou son intention), non ses actes : la conservation tiendrait sans rien dire de la fragmentation.

**Unité d'observation.** La paire formée d'un épisode saboté entier et de son jumeau honnête sur la même tâche, à un niveau de fragmentation donné. L'épisode réunit les n actions surveillées d'un agent, ou d'un essaim. L'incertitude se calcule en rééchantillonnant les tâches.

**Statut.** Une prévision, écrite sans lire aucun résultat : j'ignore ce que disent les mesures déjà faites, s'il y en a. Elle demande un préenregistrement scellé avant toute lecture décisive (règle R1) : niveaux de fragmentation, marge, calcul de puissance.

**Lien avec l'ancienne lettre (ma lecture).** L'hypothèse 1 reprend son hypothèse (a), sans exiger un déplacement à chaque action. L'hypothèse 3 reprend son hypothèse (c). Son hypothèse (b) devient ce qu'on mesure : le déplacement total suit-il le dommage, et non sa répartition ?

**Place dans la thèse (ma lecture).** Le bilan mesuré du papier A porte sur le bruit honnête. Cet énoncé porte sur le signal du sabotage. Il donne le nul de la fragmentation ; l'écart à ce nul est le résultat.

## 2. Ce qui n'est pas revendiqué

- **L'énoncé central.** L'indifférence de la somme à la répartition, à taille fixe. Il est occupé : Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7 (lecture sur PDF du 22 novembre, R-4767). Il se cite.
- **Toute forme théorème.** L'ancienne lettre du programme : une puissance qui ne dépendrait que du budget et de la variance. L'énoncé adverse complet de la décision d'octobre (N-004) : invariances exactes, borne toujours valide, coût du report, détection à temps, validité sous dépendance. Toute invariance pour un processus e ou un franchissement séquentiel : la question de l'étalement reste ouverte. Toute garantie contre un saboteur qui choisit sa répartition.
- **Le repli de la décision d'octobre (N-004).** Il présentait le lemme comme corollaire cité, l'effort portant sur la mesure, et restait disponible sans décision nouvelle. Cet erratum ne l'active pas et ne le ferme pas. L'état nouveau lui ressemble, mais il vient d'une décision neuve de Lazar, non du repli. La marque du repli reste où elle est (fixée par GO-2026-11-24-15 selon la contre-lecture de la table ; je n'ai pas lu cette ligne). Sa fermeture revient à Lazar.
- **Ce qui est hérité ou classique.** L'unité du temps et de l'espace (Avenhaus et Jaech 1981). L'opposition de la somme et du maximum, classique selon la décision d'octobre. La baisse du maximum quand l'attaque se répartit (Makins et al. 2026, p. 1).
- **L'idée de départ.** L'additivité interne reste mentionnée, non revendiquée.
- **Toute nouveauté.** Ni « premier à transposer », ni zone libre (R-4771).

## 3. Antériorité (règle R8)

Les pages sont celles que rapportent les pièces lues. Je n'ai ouvert aucun PDF.

1. **Énoncé central** (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7). Même mathématique : rien ne sépare, rien n'est revendiqué. Là, le total réparti est une donnée ; ici, on le mesure, sur des scores de sondes d'agents (ma lecture de l'énoncé, non des pages).
2. **Bornes en boîte noire** (Tailor 2025, arXiv 2510.04303v2, théorème 3, p. 12 ; Ghanem 2026, arXiv 2608.02698v1, p. 5). Elles bornent l'erreur de tout test par la divergence totale : des bornes, non une égalité mesurée, et sans sondes. Selon la note de recherche, elles occupent l'esprit de l'énoncé : à citer.
3. **Montage le plus proche** (Makins et al. 2026, arXiv 2607.07368v2, p. 1). Répartie entre plus d'agents, l'attaque abaisse le maximum du soupçon ; la somme n'est pas testée. Soupçon en boîte noire là, scores de sondes ici. Cette absence est la limite d'un article, non un trou du champ.
4. **Autres objets** (Khilar 2026, arXiv 2610.13083v1, proposition 3, p. 5 ; Li et al. 2026, arXiv 2607.13003v1, p. 1 ; Wen et al. 2024, arXiv 2411.17693v1, p. 1 et 10). Extraction par des comptes ; filigrane, où le total paie l'attribution et la répartition la localisation ; menace distribuée, sans invariance. Aucun ne porte sur un sabotage d'agent lu par des sondes.
5. **Sondes** (Parrack, Attubato et Heimersheim 2025, arXiv 2507.12691v3, p. 3-4 et 7, 13 pages lues sur 39 ; Rose et al. 2026, arXiv 2604.01151v5, p. 1, 3 et 17 ; Zhang et Gao 2026, arXiv 2606.10456v2, p. 3 et 8). Unité : la réponse, sans cadre séquentiel ; statistiques de groupe empiriques ; boîte noire, attaque fabriquée sur les scores. Les notes n'y rapportent aucun cumul de scores de sondes selon la fragmentation.

**Les pièces lues ne suffisent pas pour la forme mesurée.** Trois raisons.
- Les lectures du 22 novembre cherchaient l'énoncé. Les douze requêtes sur le lemme sont en vocabulaire de stéganalyse, de comptabilité des matières et de tests. D'après leurs intitulés, aucune ne nomme les sondes ; la seule requête qui les nomme, sur trente-six, vise la corrélation entre copies.
- Quatre arbres de citations restaient à parcourir, dont ceux des deux sources de l'énoncé central (Ker 2006 ; Avenhaus et Jaech 1981). Une application au contrôle les citerait. Je ne sais pas s'ils l'ont été depuis.
- La note de recherche a lu ses PDF pour trois objets : le lemme comme énoncé, la loi en racine, le théorème négatif. La seconde lecture visait la thèse. Aucune ne dit avoir cherché, dans les travaux sur sondes, un cumul selon la fragmentation.

Ce qui est vrai, et rien de plus : les deux notes lues ne rapportent aucune mesure, chez des agents, du cumul de scores de sondes selon la fragmentation.

Ce que la note de recherche permet d'écrire (son § 5) porte sur l'énoncé, non sur la mesure : « après la recherche décrite », aucun énoncé de cette invariance n'a été trouvé pour des moniteurs d'agents de langue, et des bornes existent en boîte noire ; quatre arbres de citations restaient à parcourir. La troisième phrase de l'énoncé revendiqué s'y adosse : elle applique l'énoncé cité, elle n'ajoute pas un théorème.

**Lectures qui manquent.**
1. Relire pour cette seule question cinq voisins : Rose et al. (2604.01151v5) ; arXiv 2607.06807v1 ; arXiv 2611.10620v1 ; Makins et al. (2607.07368v2, annexes comprises) ; Parrack et al. (p. 12 et 15 à 39). Une somme ou une moyenne de scores y est-elle rapportée selon le nombre d'actions ou d'agents qui portent l'attaque ?
2. Parcourir les arbres de citations de Ker 2006 et d'Avenhaus et Jaech 1981, puis de Ker 2007 et d'Arias-Castro, Bubeck et Lugosi 2012.
3. Chercher en vocabulaire de sondes et d'activations : cumul de scores le long d'une trajectoire ou entre agents, attaque fragmentée, vrais agents.
4. Vérifier le travail qui fonde l'environnement des propositions d'expériences (Terekhov et al., arXiv 2606.08892) : les deux notes ne le citent pas pour cet objet.

**Phrase tenable d'ici là.** « L'énoncé est connu (Avenhaus et Jaech 1981 ; Ker 2006). Nous l'appliquons aux scores de sondes, et nous mesurons si sa condition tient chez des agents qui sabotent. Notre recherche d'antériorité n'a pas encore visé cette mesure. »

## 4. Entrées d'erratum

Sept entrées, dans l'ordre du texte : lignes 27, 51, 66, 70, 111, 197 et 284 de la copie lue. La consigne en attendait quatre (sections 0, 3, 5 et 15) ; trois autres phrases disent la même chose (sections 2, 3 et 10).

Vérifié par programme sur la copie lue (empreinte `70df808a…`) : chaque texte d'origine y figure une fois, sur une seule ligne, au moment de son application, les entrées étant appliquées dans l'ordre ; il n'y figure plus ensuite. Aucun texte neuf ne porte de guillemet français, de saut de ligne ni la marque de simulation : le compte de deux passages marqués, en tête du programme, reste vrai.

Phrases laissées telles quelles :
- section 0, décision 2 : l'ancienne colonne vertébrale théorique reste retirée ; l'application ne la rétablit pas ;
- section 3, l'idée de départ, et l'expérience du plan deux par deux (E1.2) : la décision vise le lemme, non l'additivité interne ;
- section 3, hypothèses et énoncé de l'ancienne lettre : ils restent hors revendication ;
- section 3, les deux précautions : elles visent l'ancienne lettre et toute forme séquentielle ; les hypothèses 4 et 5 de l'énoncé les écartent ;
- section 3, question de l'étalement ; section 5, prévision du papier B sur la somme globale (H3) ; section 10, comparaison à la somme globale (E3.1) : inchangées.

Cible : docs/programme-controle-ia-v3.md

**L-1.** ANCIEN : « (défaut de la version 2, caduc : le lemme n'est plus revendiqué, section 3) »
NOUVEAU : « (défaut de la version 2, caduc : le lemme n'est plus revendiqué comme théorème ; il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, section 3) »
Raison : GO-2026-11-24-18. La phrase excluait aussi l'application. Le défaut reste caduc : aucun théorème n'est tenté.

**L-2.** ANCIEN : « L et T mentionnés, non revendiqués »
NOUVEAU : « L revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée (énoncé central cité, non revendiqué) ; T mentionné, non revendiqué »
Raison : GO-2026-11-24-18. Le statut du lemme change ; celui du théorème négatif ne change pas.

**L-3.** ANCIEN : « L'additivité interne, le lemme et le théorème ne sont plus des résultats ; ils restent mentionnés, chacun à son statut. »
NOUVEAU : « L'additivité interne, le lemme et le théorème ne sont plus des résultats ; l'additivité interne et le théorème restent mentionnés, chacun à son statut ; le lemme reste cité pour son énoncé central, et il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée. »
Raison : GO-2026-11-24-18. Le lemme n'est plus seulement mentionné. Il reste retiré comme résultat (GO-2026-11-22-24).

**L-4.** ANCIEN : « **Lemme d'additivité (mentionné, non revendiqué).** Énoncé occupé hors du contrôle de l'intelligence artificielle : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981 ; Ker 2006). »
NOUVEAU : « **Lemme d'additivité (énoncé central cité, non revendiqué ; application au contrôle de l'intelligence artificielle revendiquée sous la forme mesurée, décision du 24 novembre 2026, GO-2026-11-24-18).** Énoncé central, occupé hors du contrôle de l'intelligence artificielle et non revendiqué : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7). Application revendiquée, sans théorème, à éprouver par la mesure. Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions ou d'agents entre lesquels le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, l'énoncé central cité s'applique aux sondes : à déplacement total donné, la somme lue en fin d'épisode est indifférente à la répartition. La conservation est réfutée si le déplacement cumulé monte ou baisse avec la fragmentation au-delà d'une marge fixée au préenregistrement, après calcul de puissance. Le sens de l'écart est alors le résultat ; une issue indéterminée est possible. Hypothèses : (1) le sabotage déplace la position des scores et ce déplacement croît avec le dommage (s'il est nul à tous les niveaux, l'énoncé est sans objet et la question Q décide) ; (2) le dommage, celui de l'épisode entier, est chiffré et constaté hors des scores ; (3) à tous les niveaux de fragmentation, n, la tâche, le nombre d'agents et la sonde, gelée avant la mesure, sont les mêmes, et la référence honnête est déclarée (taille m, dans l'unité de n) ; (4) la somme est lue en fin d'épisode, et rien n'est dit d'un franchissement séquentiel ; (5) le montage fixe la fragmentation, sur les organismes tels qu'ils sont construits, et rien n'est affirmé d'un saboteur qui choisit sa répartition. Mesuré par sonde, par famille d'organismes et par niveau de fragmentation (le nombre d'actions ou d'agents qui portent le sabotage) : le déplacement cumulé et sa dispersion ; à côté, le rappel de la somme, le maximum par action et la part du déplacement portée par les actions de sabotage. Unité d'observation : l'épisode entier, apparié à son jumeau honnête sur la même tâche ; l'incertitude se calcule par tâche. Voisins à citer : bornes en divergence totale, en boîte noire (Tailor 2025, arXiv 2510.04303, p. 12 ; Ghanem 2026, arXiv 2608.02698, p. 5) ; baisse du maximum du soupçon quand l'attaque se répartit entre plus d'agents (Makins et al. 2026, arXiv 2607.07368, p. 1 ; la somme n'y est pas testée, selon notre lecture). Antériorité de cette forme non établie : aucune phrase de nouveauté. La prévision de H3 sur la somme globale garde son statut. »
Raison : GO-2026-11-24-18, avec GO-2026-11-22-42 (application au contrôle) et GO-2026-11-22-64 (forme mesurée : conservation du déplacement cumulé sous fragmentation). L'énoncé central reste cité, non revendiqué ; ses pages viennent de R-4767. Voisins à citer : R-4771.

**L-5.** ANCIEN : « **L — lemme d'additivité** (mentionné, non revendiqué ; la note 0,75 est caduque). Section 3. »
NOUVEAU : « **L — lemme d'additivité** (revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; énoncé central cité, non revendiqué ; la note 0,75 est caduque ; application non calibrée). Section 3. »
Raison : GO-2026-11-24-18. La note 0,75 reste caduque. L'application n'est pas calibrée : son antériorité n'est pas établie.

**L-6.** ANCIEN : « (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués, section 3) »
NOUVEAU : « (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués comme théorèmes ; le lemme est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; section 3) »
Raison : GO-2026-11-24-18. La phrase disait le lemme non revendiqué, sans réserve. La tâche et son nom ne changent pas.

**L-7.** ANCIEN : « sans objet pour le lemme, qui n'est plus revendiqué (section 3) »
NOUVEAU : « sans objet pour le lemme, qui est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée et sans théorème (section 3) »
Raison : GO-2026-11-24-18. La phrase excluait aussi l'application. La question reste sans objet : l'application est une mesure.

## 5. Ligne pour la table des revendications, version 2

| Revendication | Énoncé | Statut | Décision | Condition |
|---|---|---|---|---|
| L — lemme d'additivité, application au contrôle de l'intelligence artificielle (papier A pour le temps ; entre agents, à côté de la prévision du papier B sur la somme globale, H3) | Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions ou d'agents entre lesquels le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, l'énoncé central cité s'applique aux sondes : à déplacement total donné, la somme lue en fin d'épisode est indifférente à la répartition. | revendiquée (application) | GO-2026-11-24-18 (mots antérieurs : GO-2026-11-22-42 et GO-2026-11-22-64) | La conservation est réfutée si le déplacement cumulé monte ou baisse avec la fragmentation au-delà d'une marge fixée au préenregistrement, après calcul de puissance. Le sens de l'écart est alors le résultat ; une issue indéterminée est possible. Énoncé à contre-lire avant tout usage. Mesure à préenregistrer. Antériorité de la forme mesurée non établie : aucune phrase de nouveauté. Énoncé central cité, non revendiqué (R-4767). Voisins à citer (R-4771). |

Je n'ai pas lu la table : ses colonnes sont à reprendre. Le statut de l'énoncé central (cité, non revendiqué) est à garder, sur cette ligne ou sur la sienne.

## 6. Points pour Lazar et confiance

1. **Portée : le temps et les agents, ou le temps seul.** Nœud, sans défaut. Enjeu : la table et l'entretien. Option a, les deux axes (rédaction actuelle) : fidèle à « sous fragmentation » et au montage le plus proche, qui répartit entre agents ; mais une part de la mesure attend le papier B. Option b, le temps seul : tout se mesure dans le papier A ; mais le cas entre agents sort de la revendication. Il suffirait alors de retirer les mots « ou d'agents » et « le nombre d'agents » partout où ils figurent. Recommandation : a. Confiance : 0,6.
2. **Inscrire la mesure au plan.** Sans défaut : le plan et la dépense sont à toi. Enjeu : une revendication sans mesure prévue. Dans le plan du programme v3, aucune expérience ne fait varier la fragmentation dans le temps à dommage égal ; je n'ai pas lu les préenregistrements. Option a : ajouter au bilan sur données réelles (E1.3) « déplacement cumulé selon la fragmentation, à dommage égal » pour le temps, et lire la même mesure sur la réplication de l'effet de fragmentation (E2.1) pour les agents ; préenregistrement d'abord, dépense sur devis. Option b : ne la mesurer qu'entre agents, au papier B. Option c : la laisser sans mesure planifiée. Recommandation : a. Confiance : 0,7. Je n'ai rien ajouté au plan.
3. **Trois garde-fous qui ne sont pas dans tes mots.** « À dommage total égal », constaté hors des scores. Un déplacement qui croît avec le dommage. La part du déplacement portée par les actions de sabotage, rapportée à part. Sans eux, la conservation peut tenir pour une mauvaise raison : une sonde qui lit la consigne cachée de l'organisme donne le même cumul à toute fragmentation. Je les garderais. À toi de dire.
4. **Objection à prévoir.** Celle qui a retiré la marge asymétrique (N-077) : une mesure faite sur nos organismes peut lire leur fabrication. L'énoncé y répond en partie : il ne dit rien d'un saboteur qui répond au mieux, et la mesure se rapporte par famille d'organismes. Je n'ai pas lu N-077 : à faire vérifier par le contre-lecteur.
5. **La conservation est un cas limite, non un fait attendu.** Le score par action agrège les jetons par maximum ou par attention : il n'est pas additif par construction (mon raisonnement). Si chaque fragment garde une trace d'intention, le cumul monte quand on fragmente, à l'avantage du défenseur. Si les petits fragments n'en laissent pas, il baisse, à l'avantage du saboteur. Tes mots disent « conservation » : je l'ai gardée, réfutable dans les deux sens. Une forme à un seul sens existe (« le cumul ne baisse pas ») : elle porte ce qui compte pour le défenseur, mais ce n'est plus le lemme, c'est l'idée de départ. À l'entretien : le mot « lemme » désigne l'énoncé cité ; ce qui est à nous est son application, une prévision sur des sondes et sa mesure. Dire « nous mesurons si elle tient », jamais « nous montrons qu'elle tient ».
6. **Antériorité.** Les quatre lectures de la section 3 sont de routine. Je recommande de les lancer avant l'entretien. D'ici là : la phrase tenable, et rien sur la nouveauté.
7. **Repli de la décision d'octobre (N-004).** Sa fermeture te revient. Une ligne au registre suffirait : repli fermé ; énoncé adverse complet non revendiqué ; seule l'application mesurée l'est.
8. **Suites d'écriture.** D'après la contre-lecture de la table, la décision sur l'issue, le plancher d'audit et les deux regards (N-075) parle du lemme et attend son erratum : il devra reprendre cet énoncé. L'idée de départ reste « mentionnée, non revendiquée » : à confirmer.

**Pour la session mère.** La forme des blocs suit la description de la consigne : trois lignes consécutives par bloc, une ligne vide entre les blocs. Je n'ai lu ni le complément de la demande 27 ni le programme d'application : une application à blanc s'impose. Les textes d'origine sont vérifiés sur la copie du bloc-notes ; à revérifier sur le fichier scellé. Valeur de contrôle : les sept remplacements faits dans l'ordre sur cette copie donnent un texte d'empreinte `42cf39de86c137de513070c576a6c189ded02fa3ac7eb86e9c474320daec6261`. L'en-tête du programme ne cite pas cet erratum. Si le texte corrigé doit le dire, deux retouches hors blocs, à ta main : dans « Ce que ce texte applique », après `des renvois corrigés).`, ajouter ` Puis l'erratum 1 du 24 novembre 2026 : le lemme d'additivité est revendiqué dans sa seule application au contrôle de l'intelligence artificielle (GO-2026-11-24-18).` ; dans « Périmètre », `Hors de ce que vise cette demande` deviendrait `Hors de ce que visent cette demande et l'erratum 1`.

**Confiance.** Fidélité de l'énoncé aux mots de Lazar : 0,8. Exactitude des sept textes d'origine : 0,95, vérifiée par programme. Forme lisible par le programme d'application : 0,7. Jugement d'antériorité : 0,85. Ensemble : 0,75.
