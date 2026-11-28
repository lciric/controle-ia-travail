# Erratum 1 du programme v3 — le lemme d'additivité, revendiqué dans sa seule application au contrôle de l'intelligence artificielle — v2

v2 : corrections de la contre-lecture d'Opus 5.5 (`contre-lecture-erratum-lemme-opus-v1.md`, verdict « conforme sous corrections ») ; défauts 1 à 6 corrigés, écarts motivés en section 7 ; deux variantes selon la portée, seul nœud qui reste. La v1 (`959c4266…`) reste archivée sans modification.

Écrit le 2026-11-24 vers 11:34Z (`date -u`). Rédacteur : Claude Fable 5.2, effort maximal, sur la consigne `consigne-fable-enonce-lemme-application-v1.md` du même dossier, puis sur le mot de la session mère après contre-lecture. Pièce de travail : non scellée. Les corrections restent à vérifier par le même contre-lecteur avant tout usage (GO-2026-11-24-18).

**Verdict.** L'énoncé revendiqué tient en trois phrases, une règle de lecture à trois issues et cinq hypothèses ; c'est une prévision à éprouver, non un constat. Deux variantes sont prêtes, selon la portée : le temps et les agents (neuf entrées), ou le temps seul (huit entrées). Pour la forme mesurée, les pièces lues ne suffisent pas à écrire « non trouvé dans les pièces lues » ; la section 3 nomme les lectures qui manquent.

**Lu.** Le programme v3 tel qu'il sera scellé : copie du bloc-notes de la session, empreinte `70df808ada9e67ba766eeb8e091b6ab843b7e83651ce120477e7ad799d7eefb1`. La décision d'octobre sur les énoncés du théorème négatif et du lemme (N-003 et N-004). Sur origin/main, commit `5fd8fc305` : les mots de Lazar des 22 et 24 novembre (GO-2026-11-22-24, -40, -42, -64 ; GO-2026-11-24-18) et les lignes de décision R-4767 à R-4769, R-4771 et R-5265. La seconde lecture de la thèse. La recherche d'antériorité sur la transposition, version 2. Les réponses 9 et 22A de Fable. La contre-lecture de la table des revendications, en entier (57 lignes). Pour la v2 : la contre-lecture de la v1 de cet erratum, en entier.

**Non lu.** Aucun PDF, aucun résultat. Ni la note de première lecture des six travaux de stéganographie et de comptabilité des matières, ni les décisions sur l'issue et le plancher d'audit (N-075) et sur la référence honnête (N-076), ni la table des revendications, ni le complément de la demande 27, ni le programme qui applique les errata. Je n'ai pas lu non plus la décision qui retire la marge asymétrique (N-077) : pour elle, je m'en remets à la contre-lecture, qui l'a lue.

## 1. L'énoncé revendiqué

Deux variantes, selon la portée (section 6, point 1). Elles ne diffèrent que par les mots sur les agents.

**Variante A — le temps et les agents.**

> Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions ou d'agents entre lesquels le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition.

**Variante B — le temps seul.**

> Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions entre lesquelles le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition.

**Règle de lecture.** La conservation est dite tenue si l'intervalle de confiance à 95 % de l'écart de déplacement entre niveaux de fragmentation tient tout entier dans plus ou moins la marge ; réfutée s'il en sort tout entier, vers le haut ou vers le bas ; indéterminée sinon. La marge est relative au déplacement du niveau le moins fragmenté. Si elle est réfutée, le sens de l'écart est le résultat. L'énoncé n'est dit tenu que s'il tient dans les deux modes d'induction du sabotage, consigne cachée et adaptateur (familles (i) et (ii) de la section 7 du programme) ; sinon le verdict se rapporte par mode. Raison, supposée selon la décision N-077 : une mesure faite sur nos organismes peut lire leur fabrication.

Le préenregistrement fixe la marge, la statistique d'écart (pente, ou plus grand écart entre niveaux), la correction pour plusieurs sondes et familles, la règle qui dit où l'énoncé tient, l'emploi du témoin, la lecture du rappel et le calcul de puissance. Un dommage inégal entre niveaux s'ajuste (déplacement par unité de dommage, si la proportionnalité tient) ou se déclare.

**Hypothèses.**
1. *Position.* Le sabotage déplace la position des scores, et ce déplacement croît avec le dommage. S'il est nul à tous les niveaux, l'énoncé est sans objet : la question « position ou dépendance » (Q) décide. S'il ne suit pas le dommage, la conservation ne dit rien du sabotage.
2. *Dommage hors des scores.* Le dommage est celui de l'épisode entier ; il n'a pas à s'additionner fragment par fragment. Il est chiffré, et constaté par la vérité de terrain de l'environnement. Sinon la conservation est circulaire. L'énoncé ne vaut donc que pour un sabotage à dommage chiffré.
3. *Taille fixe.* À tous les niveaux de fragmentation, le nombre n d'actions surveillées, la tâche, la sonde, gelée avant la mesure, et, en variante A, le nombre d'agents sont les mêmes. La référence honnête est déclarée : taille m, dans l'unité de n.
4. *Lecture en fin d'épisode.* Rien n'est dit d'un franchissement séquentiel.
5. *Organismes tels qu'ils sont construits.* Le montage fixe la fragmentation, souvent par la consigne. Rien n'est affirmé d'un saboteur qui choisit sa répartition, ni d'un saboteur réel.

**Témoin.** Un organisme qui reçoit la consigne de fragmentation et n'exécute aucun sabotage ; son déplacement, par niveau, dit ce que la sonde lit de la consigne seule. Sans lui, une conservation lue sous consigne, ou son échec, ne s'attribue pas au sabotage.

**Ce qui se mesure.** Le déplacement cumulé de chaque paire, puis sa moyenne et sa dispersion, par sonde, par mode d'induction et par niveau de fragmentation. Le niveau est le nombre d'actions, et en variante A d'agents, qui portent le sabotage. Le rappel d'une alarme sur la somme, à taux de fausses alertes déclaré, lit la troisième phrase : moyenne et dispersion ne fixent la puissance que sous approximation normale. À côté, hors de l'énoncé : le maximum par action, qui relève de la question de la transposition du jeton à l'action (Tr) ; la part du déplacement portée par les actions de sabotage. Un déplacement égal sur toutes les actions, quel que soit le dommage, lirait l'état de l'organisme (sa consigne cachée ou son intention), non ses actes : la conservation tiendrait sans rien dire de la fragmentation.

**Unité d'observation.** La paire formée d'un épisode saboté entier et de son jumeau honnête sur la même tâche, à un niveau de fragmentation donné. L'épisode réunit les n actions surveillées d'un agent, ou, en variante A, d'un essaim. L'incertitude se calcule en rééchantillonnant les tâches.

**Ne pas écrire.** La conservation chez un saboteur réel ; une conservation lue sur le seul organisme à consigne cachée, présentée comme une propriété des sondes.

**Statut.** Une prévision, écrite sans lire aucun résultat : j'ignore ce que disent les mesures déjà faites, s'il y en a. Elle demande un préenregistrement scellé avant toute lecture décisive (règle R1).

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

Deux jeux complets, un par variante : n'en appliquer qu'un. Les entrées L-1 à L-7 gardent leurs numéros de la v1, aux lignes 27, 51, 66, 70, 111, 197 et 284 de la copie lue. L-8 corrige la phrase des deux précautions, ligne 74 (défaut 6). L-9, en variante A seulement, inscrit le lemme dans la colonne du papier B, ligne 51 (défaut 4). Les deux jeux ne diffèrent qu'en L-4 et L-5, et par L-9.

Vérifié par programme sur la copie lue (empreinte `70df808a…`), pour chaque variante : chaque texte d'origine y figure une fois, sur une seule ligne, au moment de son application, les entrées étant appliquées dans l'ordre ; il n'y figure plus ensuite. Aucun texte neuf ne porte de guillemet français, de saut de ligne ni la marque de simulation : le compte de deux passages marqués, en tête du programme, reste vrai. Les deux textes corrigés ne diffèrent qu'aux lignes 51, 70 et 111.

Empreintes après application, entrées appliquées dans l'ordre par simple remplacement :
- variante A : `bc24579ea627e24cd2424deabcc396341d2f8e0052fe2a4225fca8ab443453c2` ;
- variante B : `14f6e426c786555ccb6ca3084a81c6dac122ef29f13dd66df032f257fa4f3644`.

L'empreinte de la v1 (`42cf39de…`) ne vaut plus.

Phrases laissées telles quelles :
- section 0, décision 2 : l'ancienne colonne vertébrale théorique reste retirée ; l'application ne la rétablit pas ;
- section 3, l'idée de départ, et l'expérience du plan deux par deux (E1.2) : la décision vise le lemme, non l'additivité interne ;
- section 3, hypothèses et énoncé de l'ancienne lettre : ils restent hors revendication ;
- section 3, question de l'étalement ; section 5, prévision du papier B sur la somme globale (H3) ; section 10, comparaison à la somme globale (E3.1) : inchangées.

### Variante A — le temps et les agents (neuf entrées)

<!-- variante A : début -->

Cible : docs/programme-controle-ia-v3.md

**L-1.** ANCIEN : « (défaut de la version 2, caduc : le lemme n'est plus revendiqué, section 3) »
NOUVEAU : « (défaut de la version 2, caduc : le lemme n'est plus revendiqué comme théorème ; il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, section 3) »
Raison : GO-2026-11-24-18. La phrase excluait aussi l'application. Le défaut reste caduc : aucun théorème n'est tenté.

**L-2.** ANCIEN : « L et T mentionnés, non revendiqués »
NOUVEAU : « L revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée (énoncé central cité, non revendiqué) ; T mentionné, non revendiqué »
Raison : GO-2026-11-24-18. Le statut du lemme change ; celui du théorème négatif ne change pas.

**L-3.** ANCIEN : « L'additivité interne, le lemme et le théorème ne sont plus des résultats ; ils restent mentionnés, chacun à son statut. »
NOUVEAU : « L'additivité interne, le lemme et le théorème ne sont plus des résultats ; l'additivité interne et le théorème restent mentionnés, chacun à son statut ; le lemme reste cité pour son énoncé central, et il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, comme prévision à éprouver, non comme résultat. »
Raison : GO-2026-11-24-18. Le lemme n'est plus seulement mentionné. Il reste retiré comme résultat (GO-2026-11-22-24) : il est revendiqué comme prévision.

**L-4.** ANCIEN : « **Lemme d'additivité (mentionné, non revendiqué).** Énoncé occupé hors du contrôle de l'intelligence artificielle : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981 ; Ker 2006). »
NOUVEAU : « **Lemme d'additivité (énoncé central cité, non revendiqué ; application au contrôle de l'intelligence artificielle revendiquée sous la forme mesurée, décision du 24 novembre 2026, GO-2026-11-24-18).** Énoncé central, occupé hors du contrôle de l'intelligence artificielle et non revendiqué : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7). Application revendiquée, sans théorème, comme prévision à éprouver par la mesure. Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions ou d'agents entre lesquels le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition. La conservation est dite tenue si l'intervalle de confiance à 95 % de l'écart de déplacement entre niveaux de fragmentation tient tout entier dans plus ou moins la marge ; réfutée s'il en sort tout entier, vers le haut ou vers le bas ; indéterminée sinon. La marge est relative au déplacement du niveau le moins fragmenté. Si elle est réfutée, le sens de l'écart est le résultat. L'énoncé n'est dit tenu que s'il tient dans les deux modes d'induction du sabotage, consigne cachée et adaptateur (familles (i) et (ii) de la section 7) ; sinon le verdict se rapporte par mode. Raison, supposée selon la décision N-077 : une mesure faite sur nos organismes peut lire leur fabrication. Le préenregistrement fixe la marge, la statistique d'écart (pente, ou plus grand écart entre niveaux), la correction pour plusieurs sondes et familles, la règle qui dit où l'énoncé tient, l'emploi du témoin, la lecture du rappel et le calcul de puissance. Un dommage inégal entre niveaux s'ajuste (déplacement par unité de dommage, si la proportionnalité tient) ou se déclare. Hypothèses : (1) le sabotage déplace la position des scores et ce déplacement croît avec le dommage (s'il est nul à tous les niveaux, l'énoncé est sans objet et la question Q décide) ; (2) le dommage, celui de l'épisode entier, est chiffré et constaté hors des scores ; (3) à tous les niveaux de fragmentation, n, la tâche, le nombre d'agents et la sonde, gelée avant la mesure, sont les mêmes, et la référence honnête est déclarée (taille m, dans l'unité de n) ; (4) la somme est lue en fin d'épisode, et rien n'est dit d'un franchissement séquentiel ; (5) le montage fixe la fragmentation, souvent par la consigne, sur les organismes tels qu'ils sont construits, et rien n'est affirmé d'un saboteur qui choisit sa répartition ni d'un saboteur réel. Témoin : un organisme qui reçoit la consigne de fragmentation et n'exécute aucun sabotage ; son déplacement, par niveau, dit ce que la sonde lit de la consigne seule. Mesuré par sonde, par mode d'induction et par niveau de fragmentation (le nombre d'actions ou d'agents qui portent le sabotage) : le déplacement cumulé et sa dispersion ; le rappel d'une alarme sur la somme, à taux de fausses alertes déclaré, qui lit le corollaire sur la puissance ; à côté, le maximum par action et la part du déplacement portée par les actions de sabotage. Unité d'observation : l'épisode entier, apparié à son jumeau honnête sur la même tâche ; l'incertitude se calcule par tâche. Ne pas écrire : la conservation chez un saboteur réel ; une conservation lue sur le seul organisme à consigne cachée, présentée comme une propriété des sondes. Voisins à citer : bornes en divergence totale, en boîte noire (Tailor 2025, arXiv 2510.04303, p. 12 ; Ghanem 2026, arXiv 2608.02698, p. 5) ; baisse du maximum du soupçon quand l'attaque se répartit entre plus d'agents (Makins et al. 2026, arXiv 2607.07368, p. 1 ; la somme n'y est pas testée, selon notre lecture). Antériorité de cette forme non établie : aucune phrase de nouveauté. La prévision de H3 sur la somme globale garde son statut. »
Raison : GO-2026-11-24-18, avec GO-2026-11-22-42 (application au contrôle) et GO-2026-11-22-64 (forme mesurée : conservation du déplacement cumulé sous fragmentation). L'énoncé central reste cité, non revendiqué ; ses pages viennent de R-4767. Voisins à citer : R-4771. Règle de lecture, modes d'induction, témoin et phrases à ne pas écrire : contre-lecture du 24 novembre, défauts 1 à 3.

**L-5.** ANCIEN : « **L — lemme d'additivité** (mentionné, non revendiqué ; la note 0,75 est caduque). Section 3. »
NOUVEAU : « **L — lemme d'additivité** (revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; dans le temps ici, entre agents au papier B, à côté de H3 ; énoncé central cité, non revendiqué ; la note 0,75 est caduque ; application non calibrée). Section 3. »
Raison : GO-2026-11-24-18. La note 0,75 reste caduque. L'application n'est pas calibrée : son antériorité n'est pas établie. La portée est dite : le temps et les agents.

**L-6.** ANCIEN : « (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués, section 3) »
NOUVEAU : « (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués comme théorèmes ; le lemme est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; section 3) »
Raison : GO-2026-11-24-18. La phrase disait le lemme non revendiqué, sans réserve. La tâche et son nom ne changent pas.

**L-7.** ANCIEN : « sans objet pour le lemme, qui n'est plus revendiqué (section 3) »
NOUVEAU : « sans objet pour le lemme, qui est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée et sans théorème (section 3) »
Raison : GO-2026-11-24-18. La phrase excluait aussi l'application. La question reste sans objet : l'application est une mesure.

**L-8.** ANCIEN : « Deux précautions à traiter dans l'énoncé : »
NOUVEAU : « Deux précautions, pour l'ancienne lettre : »
Raison : Contre-lecture du 24 novembre, défaut 6. Après l'entrée L-4, on ne savait plus quel énoncé ces précautions visaient.

**L-9.** ANCIEN : « H3, H4′, H5, H7 »
NOUVEAU : « H3, L (entre agents, à côté de H3), H4′, H5, H7 »
Raison : Contre-lecture du 24 novembre, défaut 4. L'énoncé couvre aussi la répartition entre agents ; le lemme n'était inscrit qu'au papier A.

<!-- variante A : fin -->

### Variante B — le temps seul (huit entrées)

<!-- variante B : début -->

Cible : docs/programme-controle-ia-v3.md

**L-1.** ANCIEN : « (défaut de la version 2, caduc : le lemme n'est plus revendiqué, section 3) »
NOUVEAU : « (défaut de la version 2, caduc : le lemme n'est plus revendiqué comme théorème ; il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, section 3) »
Raison : GO-2026-11-24-18. La phrase excluait aussi l'application. Le défaut reste caduc : aucun théorème n'est tenté.

**L-2.** ANCIEN : « L et T mentionnés, non revendiqués »
NOUVEAU : « L revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée (énoncé central cité, non revendiqué) ; T mentionné, non revendiqué »
Raison : GO-2026-11-24-18. Le statut du lemme change ; celui du théorème négatif ne change pas.

**L-3.** ANCIEN : « L'additivité interne, le lemme et le théorème ne sont plus des résultats ; ils restent mentionnés, chacun à son statut. »
NOUVEAU : « L'additivité interne, le lemme et le théorème ne sont plus des résultats ; l'additivité interne et le théorème restent mentionnés, chacun à son statut ; le lemme reste cité pour son énoncé central, et il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, comme prévision à éprouver, non comme résultat. »
Raison : GO-2026-11-24-18. Le lemme n'est plus seulement mentionné. Il reste retiré comme résultat (GO-2026-11-22-24) : il est revendiqué comme prévision.

**L-4.** ANCIEN : « **Lemme d'additivité (mentionné, non revendiqué).** Énoncé occupé hors du contrôle de l'intelligence artificielle : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981 ; Ker 2006). »
NOUVEAU : « **Lemme d'additivité (énoncé central cité, non revendiqué ; application au contrôle de l'intelligence artificielle revendiquée sous la forme mesurée, décision du 24 novembre 2026, GO-2026-11-24-18).** Énoncé central, occupé hors du contrôle de l'intelligence artificielle et non revendiqué : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7). Application revendiquée, sans théorème, comme prévision à éprouver par la mesure. Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions entre lesquelles le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition. La conservation est dite tenue si l'intervalle de confiance à 95 % de l'écart de déplacement entre niveaux de fragmentation tient tout entier dans plus ou moins la marge ; réfutée s'il en sort tout entier, vers le haut ou vers le bas ; indéterminée sinon. La marge est relative au déplacement du niveau le moins fragmenté. Si elle est réfutée, le sens de l'écart est le résultat. L'énoncé n'est dit tenu que s'il tient dans les deux modes d'induction du sabotage, consigne cachée et adaptateur (familles (i) et (ii) de la section 7) ; sinon le verdict se rapporte par mode. Raison, supposée selon la décision N-077 : une mesure faite sur nos organismes peut lire leur fabrication. Le préenregistrement fixe la marge, la statistique d'écart (pente, ou plus grand écart entre niveaux), la correction pour plusieurs sondes et familles, la règle qui dit où l'énoncé tient, l'emploi du témoin, la lecture du rappel et le calcul de puissance. Un dommage inégal entre niveaux s'ajuste (déplacement par unité de dommage, si la proportionnalité tient) ou se déclare. Hypothèses : (1) le sabotage déplace la position des scores et ce déplacement croît avec le dommage (s'il est nul à tous les niveaux, l'énoncé est sans objet et la question Q décide) ; (2) le dommage, celui de l'épisode entier, est chiffré et constaté hors des scores ; (3) à tous les niveaux de fragmentation, n, la tâche et la sonde, gelée avant la mesure, sont les mêmes, et la référence honnête est déclarée (taille m, dans l'unité de n) ; (4) la somme est lue en fin d'épisode, et rien n'est dit d'un franchissement séquentiel ; (5) le montage fixe la fragmentation, souvent par la consigne, sur les organismes tels qu'ils sont construits, et rien n'est affirmé d'un saboteur qui choisit sa répartition ni d'un saboteur réel. Témoin : un organisme qui reçoit la consigne de fragmentation et n'exécute aucun sabotage ; son déplacement, par niveau, dit ce que la sonde lit de la consigne seule. Mesuré par sonde, par mode d'induction et par niveau de fragmentation (le nombre d'actions qui portent le sabotage) : le déplacement cumulé et sa dispersion ; le rappel d'une alarme sur la somme, à taux de fausses alertes déclaré, qui lit le corollaire sur la puissance ; à côté, le maximum par action et la part du déplacement portée par les actions de sabotage. Unité d'observation : l'épisode entier, apparié à son jumeau honnête sur la même tâche ; l'incertitude se calcule par tâche. Ne pas écrire : la conservation chez un saboteur réel ; une conservation lue sur le seul organisme à consigne cachée, présentée comme une propriété des sondes. Voisins à citer : bornes en divergence totale, en boîte noire (Tailor 2025, arXiv 2510.04303, p. 12 ; Ghanem 2026, arXiv 2608.02698, p. 5) ; baisse du maximum du soupçon quand l'attaque se répartit entre plus d'agents (Makins et al. 2026, arXiv 2607.07368, p. 1 ; la somme n'y est pas testée, selon notre lecture). Antériorité de cette forme non établie : aucune phrase de nouveauté. Entre agents, rien n'est revendiqué ici ; la prévision de H3 sur la somme globale garde son statut. »
Raison : GO-2026-11-24-18, avec GO-2026-11-22-42 (application au contrôle) et GO-2026-11-22-64 (forme mesurée : conservation du déplacement cumulé sous fragmentation). L'énoncé central reste cité, non revendiqué ; ses pages viennent de R-4767. Voisins à citer : R-4771. Règle de lecture, modes d'induction, témoin et phrases à ne pas écrire : contre-lecture du 24 novembre, défauts 1 à 3.

**L-5.** ANCIEN : « **L — lemme d'additivité** (mentionné, non revendiqué ; la note 0,75 est caduque). Section 3. »
NOUVEAU : « **L — lemme d'additivité** (revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; énoncé central cité, non revendiqué ; la note 0,75 est caduque ; application non calibrée). Section 3. »
Raison : GO-2026-11-24-18. La note 0,75 reste caduque. L'application n'est pas calibrée : son antériorité n'est pas établie.

**L-6.** ANCIEN : « (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués, section 3) »
NOUVEAU : « (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués comme théorèmes ; le lemme est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; section 3) »
Raison : GO-2026-11-24-18. La phrase disait le lemme non revendiqué, sans réserve. La tâche et son nom ne changent pas.

**L-7.** ANCIEN : « sans objet pour le lemme, qui n'est plus revendiqué (section 3) »
NOUVEAU : « sans objet pour le lemme, qui est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée et sans théorème (section 3) »
Raison : GO-2026-11-24-18. La phrase excluait aussi l'application. La question reste sans objet : l'application est une mesure.

**L-8.** ANCIEN : « Deux précautions à traiter dans l'énoncé : »
NOUVEAU : « Deux précautions, pour l'ancienne lettre : »
Raison : Contre-lecture du 24 novembre, défaut 6. Après l'entrée L-4, on ne savait plus quel énoncé ces précautions visaient.

<!-- variante B : fin -->

## 5. Ligne pour la table des revendications, version 2

Une seule ligne à garder, selon la variante choisie.

| Variante | Revendication | Énoncé | Statut | Décision |
|---|---|---|---|---|
| A | L — lemme d'additivité, application au contrôle de l'intelligence artificielle : dans le temps (papier A) et entre agents (papier B, à côté de la prévision sur la somme globale, H3) | Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions ou d'agents entre lesquels le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition. | revendiquée (application) | GO-2026-11-24-18 (mots antérieurs : GO-2026-11-22-42 et GO-2026-11-22-64) |
| B | L — lemme d'additivité, application au contrôle de l'intelligence artificielle : dans le temps seul (papier A) | Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions entre lesquelles le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition. | revendiquée (application) | GO-2026-11-24-18 (mots antérieurs : GO-2026-11-22-42 et GO-2026-11-22-64) |

Condition, pour l'une comme pour l'autre. La conservation est dite tenue si l'intervalle de confiance à 95 % de l'écart de déplacement entre niveaux de fragmentation tient tout entier dans plus ou moins la marge ; réfutée s'il en sort tout entier, vers le haut ou vers le bas ; indéterminée sinon. La marge est relative au déplacement du niveau le moins fragmenté. Si elle est réfutée, le sens de l'écart est le résultat. L'énoncé n'est dit tenu que s'il tient dans les deux modes d'induction du sabotage, consigne cachée et adaptateur (familles (i) et (ii) de la section 7 du programme) ; sinon le verdict se rapporte par mode. Raison, supposée selon la décision N-077 : une mesure faite sur nos organismes peut lire leur fabrication. Un témoin à consigne de fragmentation, sans sabotage exécuté, accompagne la mesure. La mesure est à préenregistrer. L'antériorité de la forme mesurée n'est pas établie : aucune phrase de nouveauté. L'énoncé central est cité, non revendiqué (R-4767) ; des voisins sont à citer (R-4771). Ne pas écrire : la conservation chez un saboteur réel ; une conservation lue sur le seul organisme à consigne cachée, présentée comme une propriété des sondes.

Je n'ai pas lu la table : ses colonnes sont à reprendre. Le statut de l'énoncé central (cité, non revendiqué) est à garder, sur cette ligne ou sur la sienne.

## 6. Points pour Lazar et confiance

1. **Seul nœud : la portée.** Variante A, le temps et les agents : fidèle à « sous fragmentation » et au montage le plus proche, qui répartit entre agents ; mais une part de la mesure attend le papier B. Variante B, le temps seul : tout se mesure dans le papier A ; mais le cas entre agents sort de la revendication. Recommandation : A. Confiance : 0,6. Les deux textes sont prêts : tu n'as qu'à choisir.
2. **Signalé, sans décision demandée : trois garde-fous qui ne sont pas dans tes mots.** « À dommage total égal », constaté hors des scores. Un déplacement qui croît avec le dommage. La part du déplacement portée par les actions de sabotage, rapportée à part. La contre-lecture juge qu'ils explicitent ton énoncé et n'exigent pas ton mot.
3. **Signalé : une lecture plus dure qu'en v1.** L'objection qui a retiré la marge asymétrique (N-077) s'applique : une mesure faite sur nos organismes peut lire leur fabrication. Cette décision dit elle-même la raison « supposée ». D'où trois ajouts. L'énoncé n'est dit tenu que dans une marge, sur un intervalle de confiance. Il doit tenir dans les deux modes d'induction du sabotage, consigne cachée et adaptateur. Un témoin reçoit la consigne de fragmentation sans exécuter de sabotage. Deux conséquences : plus d'épisodes à produire ; et le préenregistrement devra dire comment le montage fixe la fragmentation dans le mode à adaptateur, qui n'a pas de consigne à l'inférence. Faute de quoi l'énoncé ne pourra pas être dit tenu.
4. **La conservation est un cas limite, non un fait attendu.** Le score par action agrège les jetons par maximum ou par attention : il n'est pas additif par construction (mon raisonnement). Si chaque fragment garde une trace d'intention, le cumul monte quand on fragmente, à l'avantage du défenseur. Si les petits fragments n'en laissent pas, il baisse, à l'avantage du saboteur. Tes mots disent « conservation » : je l'ai gardée, réfutable dans les deux sens. Une forme à un seul sens existe (« le cumul ne baisse pas ») : elle porte ce qui compte pour le défenseur, mais ce n'est plus le lemme, c'est l'idée de départ. À l'entretien : le mot « lemme » désigne l'énoncé cité ; ce qui est à nous est son application, une prévision sur des sondes et sa mesure. Dire « nous mesurons si elle tient », jamais « nous montrons qu'elle tient ».
5. **Antériorité.** Les quatre lectures de la section 3 sont de routine. Je recommande de les lancer avant l'entretien. D'ici là : la phrase tenable, et rien sur la nouveauté.
6. **À ta main, hors de l'énoncé : le plan.** Dans le plan du programme v3, aucune expérience ne fait varier la fragmentation dans le temps à dommage égal ; je n'ai pas lu les préenregistrements. Je recommande d'ajouter au bilan sur données réelles (E1.3) « déplacement cumulé selon la fragmentation, à dommage égal, dans les deux modes d'induction, avec témoin », et, en variante A, de lire la même mesure sur la réplication de l'effet de fragmentation (E2.1). Préenregistrement d'abord, dépense sur devis. Confiance : 0,7. Je n'ai rien ajouté au plan.
7. **À ta main : le repli de la décision d'octobre (N-004).** Une ligne au registre suffirait : repli fermé ; énoncé adverse complet non revendiqué ; seule l'application mesurée l'est.
8. **Suites d'écriture.** D'après la contre-lecture de la table, la décision sur l'issue, le plancher d'audit et les deux regards (N-075) parle du lemme et attend son erratum : il devra reprendre cet énoncé. L'idée de départ reste « mentionnée, non revendiquée » : à confirmer.

**Pour la session mère.** Chaque variante a sa ligne de cible et son jeu de blocs, entre deux repères en commentaire : n'en donner qu'un au programme d'application. La forme des blocs est celle de la v1, que la contre-lecture a appliquée par programme : trois lignes consécutives par bloc, une ligne vide entre les blocs. Les textes d'origine sont vérifiés sur la copie du bloc-notes ; à revérifier sur le fichier scellé. L'en-tête du programme ne cite pas cet erratum. Si le texte corrigé doit le dire, deux retouches hors blocs, à ta main : dans « Ce que ce texte applique », après `des renvois corrigés).`, ajouter ` Puis l'erratum 1 du 24 novembre 2026 : le lemme d'additivité est revendiqué dans sa seule application au contrôle de l'intelligence artificielle (GO-2026-11-24-18).` ; dans « Périmètre », `Hors de ce que vise cette demande` deviendrait `Hors de ce que visent cette demande et l'erratum 1`.

**Confiance.** Fidélité de l'énoncé aux mots de Lazar : 0,85. Exactitude des textes d'origine : 0,95, vérifiée par programme. Forme lisible par le programme d'application : 0,85. Jugement d'antériorité : 0,85. Ensemble : 0,8.

## 7. Corrections de la v2, et écarts motivés

| Défaut | Correction faite | Écart à la lettre de la contre-lecture |
|---|---|---|
| 1, troisième phrase | Elle porte sur la puissance, sous deux conditions : la conservation, et une dispersion qui ne dépend pas de la fragmentation. Le rappel devient la lecture de ce corollaire. Section 1, L-4, table. | Deux retouches. « De ce déplacement » pour « du cumul » : une seule variable, celle de l'énoncé. « Sous approximation normale » ajouté : moyenne et dispersion égales ne fixent pas seules la puissance. |
| 2, règle de confirmation | Règle à trois issues sur l'intervalle de confiance à 95 % ; marge relative au niveau le moins fragmenté ; renvois au préenregistrement ; dommage inégal ajusté ou déclaré. | Deux ajouts. « Si la proportionnalité tient » : diviser par le dommage suppose un déplacement proportionnel au dommage. Le préenregistrement fixe aussi l'emploi du témoin et la lecture du rappel. |
| 3, objection de la décision N-077 | Énoncé tenu seulement dans les deux modes d'induction ; témoin à consigne sans sabotage ; « Ne pas écrire » ; raison gardée comme « supposée » ; hypothèse 5 complétée. Section 1, L-4, table, point 3. | Aucun. Je n'ai pas lu cette décision : je m'en remets à la contre-lecture. |
| 4, portée | Deux variantes complètes. A : colonne du papier B (L-9). B : « ou d'agents » retiré partout. | Un ajout en A : L-5 dit la portée, parce que la liste de la section 5 n'inscrit le lemme qu'au papier A. |
| 5, entrée L-3 | « comme prévision à éprouver, non comme résultat ». | Aucun. |
| 6, entrée L-4 | Entrée L-8 : « Deux précautions, pour l'ancienne lettre : ». | Aucun. |

Aucun désaccord de fond. Sur la question 1 de la contre-lecture, les garde-fous sont signalés à Lazar sans demande de décision (point 2).
