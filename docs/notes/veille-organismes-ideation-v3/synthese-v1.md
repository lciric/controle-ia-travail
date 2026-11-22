# Veille « exploration d'idées originales par les modèles de langue » — relance du 22 novembre 2026 — synthèse v1

*Agent de veille neuf (Opus 5.5). Lu d'abord : synthèses des veilles `veille-exploration-idees-v1`, `veille-organismes-ideation-v2`, `veille-voisins-yu-v1`, décisions N-073 et compléments 1 à 3, `registres/veille.md`. Dédoublonnage contre 574 identifiants du dépôt. Source : listes arXiv de la semaine du 13 au 20 novembre (intelligence artificielle, langue, apprentissage, multi-agents), 26 résumés, 9 PDF. « Lu » = texte du PDF par passages, page citée ; « résumé » = page arXiv seule. Aucune dépense, aucun commit.*

## 1. Verdict

1. **Aucune collision avec un énoncé retenu de N-073 et de ses compléments.** Trois travaux serrent des pièces de méthode non revendiquées : la porte « séquentiel contre meilleur de N », l'audit du générateur de mondes plantés, la mémoire transmise.
2. **Deux indices contraires comptent le plus** : la sélection par notes d'évaluation ne bat pas le hasard (Zeng et al.) ; réécrire sans retour un savoir transmis le tire vers ce que le modèle sait déjà (Guo et al.).
3. **« A Society of AI Scientists » est un voisin à citer**, pas une collision : description, sans tirage au hasard, d'une communauté d'agents qui communiquent.

## 2. Travaux retenus (15)

**1. A Society of AI Scientists** — Ahmad, Anderson, … Schmidgall (43 auteurs), 21 nov. 2026, [alphaXiv 2611.society-ai-scientists](https://www.alphaxiv.org/abs/2611.society-ai-scientists). *Question* : des agents indépendants forment-ils une communauté de recherche ? *Résultat* : 936 études, 9 500 messages (p. 1) ; registre reliant chaque nombre au fichier qui l'a produit, fichiers indexés par empreinte (p. 5) ; exécuter 156 objections majeures sur les données renverse 77 conclusions, 49,4 % (p. 19-20) ; scores des pairs visibles : 88 % de suivisme du premier en tête, contre 30 % cachés (p. 13, 21-22) ; deux juges-modèles mettent l'humain devant en nouveauté (−0,39 sur 10), l'avance des agents vient du seul premier laboratoire (p. 29-30) ; observationnel (p. 6). *Lu*. *Pour nous* : voisin ; appuie les témoins « même effectif sans échange » (N-073 § 5) ; registre proche de notre registre des tentatives, sans prédiction scellée ni bras d'héritage ; papier C : juge qui exécute contre juge qui lit.

**2. The Resolution Hypothesis** — Zeng, Lan, Lu et al., 17 nov., [arXiv 2611.23068](https://arxiv.org/abs/2611.23068). *Question* : l'évolution d'agents bloque-t-elle à la proposition ou à la sélection ? *Résultat* : sept méthodes, six modèles, plus de 10 millions d'appels (p. 1, 4) ; le sélecteur choisit le meilleur de deux 49,7 % du temps ; régressions : 30,5 % du vivier, 62,1 % des acceptés (p. 8) ; meilleur de K : 49,2 % à K = 1, 61,8 % à K = 100 (p. 6) ; écart médian publié entre méthodes, 3,4 points, sous l'écart entre deux courses d'une même méthode (p. 5). *Lu*. *Pour nous* : voisin à citer pour la porte et ses six lignes ; contre-indice pour toute sélection par un juge dans l'organisme.

**3. Openhagen Worlds** — Lorup, 18 nov., [arXiv 2611.24711](https://arxiv.org/abs/2611.24711). *Résultat* : 27 familles générées, vérité cachée ; un niveau n'est admis que si l'oracle réussit au moins 0,75, la meilleure politique non déductive au plus 0,25, chaque raccourci au plus 0,35 (p. 1, 4-5) ; l'auteur ne connaît pas d'autre banc qui le fasse (p. 3) ; un raccourci non écrit reste possible (p. 24). *Lu*. *Pour nous* : voisin serré de l'audit du générateur (N-073 § 4) et de la table d'éligibilité ; l'admission par politiques témoins se cite.

**4. How Feedback-Free Self-Evolution Reshapes Agent Skills** — Guo, Chen, Xu et al., 19 nov., [arXiv 2611.25534](https://arxiv.org/abs/2611.25534). *Résultat* : après trente réécritures sans retour, chaque modèle fait moins bien sur chaque banc, −15 points en moyenne sur le banc des compétences ; la réécriture perd d'abord ce qui sort du prior du modèle (p. 1-3). *Lu*. *Pour nous* : contre-indice pour une mémoire réécrite par un modèle ; appuie le registre écrit par programme (complément 3).

**5. OpenKAGE** — Yuan, Yuan, Jia et al., 18 nov., [arXiv 2611.24302](https://arxiv.org/abs/2611.24302). *Résultat* : le savoir d'un groupe, servi à un groupe neuf sur un autre modèle, améliore sa survie (p. 1, 3) ; dix courses par bras ne départagent pas les composantes (p. 11) ; retirer le partage retire les deux canaux (p. 30). *Lu*. *Pour nous* : voisin de l'énoncé 5 (hérité contre rien), sans séparer héritage et tenue ; à citer.

**6. When Does Interaction Help?** — Wu, Yang, Kang, Yin, 16 nov., [arXiv 2611.20773](https://arxiv.org/abs/2611.20773). *Résultat* : contre un témoin sans communication déclaré, des systèmes aux moments égaux jusqu'au degré trois ont des gains de signe opposé (p. 1-2). *Lu*. *Pour nous* : le témoin « sans échange » se mesure, il ne se prédit pas.

**7. Embedding Cosine Measures Text Length Before It Measures Homogenization** — Liu, Shu, 16 nov. (v2 18 nov.), [arXiv 2611.21519](https://arxiv.org/abs/2611.21519). Un témoin à longueur égale reproduit 81 % de l'effet annoncé (résumé). Garde pour toute mesure de diversité des idées (N-044).

**8. Twice-Told Critiques** — Gusev, 19 nov., [arXiv 2611.26286](https://arxiv.org/abs/2611.26286). *Résultat* : recouvrement des critiques à ICLR de 12,0 % (2026) à 21,3 % (2027) ; une troisième revue apporte 5,46 problèmes neufs contre 6,12 (p. 1, 3) ; découpage comptable, non causal (p. 3). *Lu*. *Pour nous* : papier C ; juges divers à mesurer.

**9. When Reviews Gate Access** — Li, Li, Yong, Tran, 14 nov., [arXiv 2611.19054](https://arxiv.org/abs/2611.19054). Cercle de 20 complices : 0,8 % de ses papiers acceptés sous affectation au hasard, 71 % si 30 % des choix des alliés sont accordés (résumé). Papier C, voisin lointain.

**10. Ground, Iterate, Trace** — Yu, Zou, Lim, Shah, Goyal, Liu, 18 nov., [arXiv 2611.24887](https://arxiv.org/abs/2611.24887). Aucun contraste de nouveauté ne survit à la correction de Holm (plus petit p = 0,076, p. 8). *Lu*. Rien de pris ; matière pour l'atelier d'idées.

**11. EvoDisco** — Liu, Kang, Kai et al., 17 nov., [arXiv 2611.22102](https://arxiv.org/abs/2611.22102). Évolution apprise de la mémoire, hors découverte (résumé). Voisin lointain.

**12. Asking the right question is key to AI discovery** — Cang, 15 nov., [arXiv 2611.19841](https://arxiv.org/abs/2611.19841). Pic omis des données : les deux scientifiques-modèles le visitent moins que le hasard, l'un le manque 32 fois sur 32 (résumé). Témoin « recherche au hasard » pour les mondes plantés.

**13. Values Shape What Self-Improving Coding Agents Build** — Liang, Waldner, Miikkulainen, 17 nov., [arXiv 2611.23067](https://arxiv.org/abs/2611.23067). Laisser l'agent réviser sa phrase de valeurs réduit les écarts entre bras (résumé). Voisin de la diversité de consignes.

**14. DiscoveryAgent** — Queen, Ciuca, Dann et al., 16 nov., [arXiv 2611.21950](https://arxiv.org/abs/2611.21950). Agents d'audit : 14 fois plus d'erreurs valides trouvées (résumé). Voisin de l'audit après coup (N-075, N-076).

**15. Causal Discovery with False Positive Error Control** — Jahn, Chandrasekaran, Eberhardt, Schulman, 19 nov., [arXiv 2611.25376](https://arxiv.org/abs/2611.25376). Contrôle des fausses découvertes à échantillon fini (résumé). Périphérie du juge au nul formé des lois connues.

*Déjà au dépôt, non repris* : Inventa (2611.21847), Self-Improvement Memory (2611.18856), Qin et al. (2611.05108), Re-Search (2611.14487).

## 3. Couverture

Bonne du 13 au 20 novembre (listes lues au titre) ; faible avant (moteur web peu frais, interface de requête d'arXiv refusée). Forums et OpenReview : rien de neuf trouvé, ce qui ne prouve rien (R8). Aucune zone dite libre.

## 4. Décisions pour le directeur

**D1. Citer Zeng et al. dans la porte « séquentiel contre meilleur de N » et y rapporter la variance entre courses ?**
Enjeu : leurs écarts entre méthodes sont sous le bruit d'une course. Options : (a) citer et ajouter une septième ligne « bruit d'évaluation et variance entre courses rapportés, nombre de courses fixé par la puissance » (lecture plus dure ; plus de courses, sur devis) ; (b) citer seulement (gratuit ; faiblesse gardée). Recommandation : (a), confiance moyenne-haute.

**D2. Présenter l'admission par politiques témoins (Openhagen Worlds) comme pratique publiée de l'audit du générateur ?**
Enjeu : notre audit avant banque sœur lui ressemble. Options : (a) citer et fixer au préenregistrement « oracle au moins, naïf et raccourcis au plus » (critère net ; politiques de raccourci à écrire) ; (b) citer seulement. Recommandation : (a), confiance moyenne.

**D3. Citer Guo et al. (indice contraire) et OpenKAGE (voisin) pour l'énoncé 5, et geler « aucun modèle ne réécrit le registre des tentatives » ?**
Enjeu : une mémoire réécrite sans retour perd ce qui sort du prior. Options : (a) citations, règle, et bras « registre résumé par un modèle » à l'étape 2, sur devis ; (b) citations seules. Recommandation : (a), confiance moyenne.

**D4. Rendre obligatoire le témoin à longueur égale dans toute mesure de diversité des idées ?**
Enjeu : une similarité de plongements peut mesurer la longueur. Options : (a) oui, garde testée sur cas sain et artefact (R5), processeur seul ; (b) non. Recommandation : (a), confiance haute sur le principe.

**D5. Faire lire en entier par un lecteur neuf Society, Zeng et al. et Openhagen avant toute phrase sortante ?**
Enjeu : lectures faites par passages. Options : (a) les trois, avec contre-lecture ; (b) Zeng et al. seul. Recommandation : (a), confiance haute.

## Annexe : empreintes des PDF lus (bloc-notes de session, non versés)

- Society (alphaXiv) : `1c1d3d84347d7736b31cae6951af435ee9332ed5aa431be55e7ccdbbfc578f5d`
- arXiv 2611.20773 : `e116634e984c17ebcda48769677287571e714c06765ebc2f6026b26f07bd8a49`
- arXiv 2611.21519 : `0f9c4732efbcdad56526f92e079b26527712c36db3b4fcc66c68ae5c4c0da694`
- arXiv 2611.23068 : `3ee67c72ccbf3a3a65a5018a79de074fa0319ca617bd2e77251d573be2782bcd`
- arXiv 2611.24302 : `0034a638ba2a33471f8192ee5bb63e8eb54deff3895798c9e9761fddb6319438`
- arXiv 2611.24711 : `de958721ff1fa11cef675c894e0dd241e7bf054a4af39b06a216bd30586ff86d`
- arXiv 2611.24887 : `a50bf3f52dc4b6e83b4f4dce5c8c9b62c011b5f0df1407293e480ba188a7dbcb`
- arXiv 2611.25534 : `7c819b8905451de0843263fecacc1179bbc7ab55923c2baeea05094c3487c559`
- arXiv 2611.26286 : `4dcffba96a712e00392cc7e90140ae35ea39eb3b9fa59ed4a7657f015b55642f`
