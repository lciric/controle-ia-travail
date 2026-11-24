# Faits publics

Chaque fait ci-dessous a le statut VÉRIFIÉ : il a été lu sur le document public en ligne, et la page donnée est celle du fichier PDF. Tout le reste de ce qui t'est transmis (le cadre et les thèses décrites dans la question) est une description ou une hypothèse, pas un fait établi.

Source unique : Xuemei Gu et Mario Krenn, « Generating Interesting Scientific Ideas using Knowledge Graphs and LLMs: Evaluations with 100 Research Group Leaders », prépublication arXiv 2405.17044, version 4 du 24 septembre 2026 (https://arxiv.org/abs/2405.17044v4).

## Fait 1 : un graphe de concepts daté, construit sur un corpus scientifique

- Les nœuds sont des concepts scientifiques extraits de 2,44 millions de titres et résumés d'articles par un algorithme d'extraction de mots-clés, puis épurés ; la liste finale compte 123 128 concepts (page 3, légende de la figure 2).
- Un lien relie deux concepts quand ils apparaissent ensemble dans le titre ou le résumé d'un même article, sur un corpus de plus de 58 millions d'articles de la base ouverte OpenAlex ; les liens portent aussi les citations des articles qui les créent (page 3, légende de la figure 2).
- Le graphe final a 123 128 sommets et plus de 168 millions de liens (bâtis à partir de 1,52 milliard de liens multiples), avec une date de coupure en avril 2023 ; il retrace une partie de l'histoire des sciences depuis 1666 (page 4).
- Les auteurs notent que l'intention d'une citation n'y est pas distinguée (page 4).

## Fait 2 : une évaluation de l'intérêt d'idées générées, par des responsables d'équipe

- Sur 267 responsables d'équipe invités, 110 ont participé (page 7).
- Chaque participant a reçu 48 propositions de projets de recherche personnalisées, 16 dans chacune de trois conditions : paire de concepts à fort impact prédit en citations, paire de concepts tirée au hasard, et un témoin rédigé par un modèle de langage à partir des seuls titres (page 7). Les paires de concepts et des informations sur les travaux des chercheurs sont données à GPT-4, qui rédige les propositions (page 4).
- Chaque proposition est notée de 1 (« not interesting ») à 5 (« very interesting ») ; sur 5 280 notes possibles, 4 451 ont été recueillies, de moyenne 2,403 ± 0,020 (page 7).

## Fait 3 : intérêt et connectivité du concept de départ

- L'analyse des traits du graphe porte sur 2 996 propositions bâties sur une paire de concepts ; le témoin rédigé à partir des seuls titres en est exclu, faute de paire (page 8).
- Les propositions sont classées selon chaque trait du graphe et réparties en 50 classes de même taille ; les pentes sont ajustées sur les moyennes des classes (page 8).
- Le degré et le PageRank du premier concept, tiré de la liste de concepts du chercheur qui évalue, ont des pentes négatives avec l'intérêt : pour le degré, pente −0,213 ± 0,030, coefficient de détermination sur les classes 0,480, corrélation de rang de Spearman au niveau de l'idée −0,166 ; pour le PageRank, pente −0,192 ± 0,028, coefficient de détermination 0,474, corrélation de rang −0,176 (page 8).
- Lecture des auteurs, mot pour mot : « the more connected a concept is within the knowledge graph, the less interesting the resulting research project tends to be » (page 8).
