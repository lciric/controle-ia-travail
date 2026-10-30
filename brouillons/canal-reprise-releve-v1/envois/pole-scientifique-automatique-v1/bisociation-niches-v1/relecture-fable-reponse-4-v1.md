# Relecture de `reponse-conv-audit-question-4-v1.md` — v1

Relecteur : sous-agent neuf et indépendant (règle R2), n'ayant lu que `question-1` à `question-4` et `reponse-conv-audit-question-4-v1.md` ; aucune autre réponse ni relecture lue ; rien lu sous `donnees/`.
Modèle : Fable 5.1 (claude-fable-5-1).
Date (`date -u`) : Fri Oct 30 20:23:08 UTC 2026 (lecture du fichier relu faite à 17:20 UTC ; fichier inchangé depuis, empreinte compagnon datée 18:20 heure locale).
Vérifications en ligne faites pendant la relecture : Gu et Krenn 2024 (arXiv 2402.08640, page de résumé v3) ; Krenn et al. 2023 (arXiv 2210.00881, page de résumé) ; existence de Benson et al. 2018 (arXiv 1802.06916) et de Poursafaei et al. 2022 (NeurIPS, jeux de données et bancs). Tout le reste est cité de mémoire et marqué SUPPOSÉ.

## Verdict (une ligne)

Réponse compacte et juste dans ses réflexes (fuites, témoins, interprétabilité, prédire ≠ causer), mais la reformulation n'est pas encore testable : pas de critère de mort chiffré, pas de référence à battre nommée, étiquette « lien futur » confondue avec « lien fertile », et l'antériorité la plus proche de la revendication « fertilité calibrée » (Gu et Krenn 2024) manque.

## (a) Les quatre points et la reformulation sont-ils tenus, sans allonger ?

Oui sur la forme. Les quatre points demandés par Lazar sont présents, dans l'ordre, et la réponse tient en 27 lignes : la consigne « plus approfondie, pas plus longue » est respectée. La reformulation reprend les six étapes attendues. Deux réserves de fond sur le point (4), voir RL4-06.

## (b) Affirmations fausses, références mal attribuées ou inventées, antériorités manquées

Rien de faux au sens strict. Les références nommées existent et sont bien attribuées (Shi-Evans, Sourati-Evans, Krenn / Science4Cast, Derex et Boyd, marche de Swanson, Adamic-Adar, node2vec, Leiden). Les problèmes sont des antériorités manquées et une attribution imprécise.

- **Gu et Krenn 2024, « Forecasting high-impact research topics via machine learning on evolving knowledge graphs », arXiv 2402.08640** (vérifié : Xuemei Gu et Mario Krenn, soumis le 13 février 2024, v3 du 7 janvier 2025 ; DOI 10.1088/2632-2153/add6ef, donc publié chez IOP, vraisemblablement *Machine Learning: Science and Technology* 2025, SUPPOSÉ pour le nom de revue). Graphe construit sur plus de 21 millions d'articles, combinant un réseau sémantique et un réseau d'impact (citations) ; prédiction de l'évolution du réseau avec aire sous la courbe supérieure à 0,9 sur la plupart des expériences. C'est exactement « prédire non pas le lien, mais le lien qui aura de l'impact », c'est-à-dire la version la plus proche de la « fertilité calibrée » que la réponse déclare « neuve chez nous ». Manque grave, car la phrase « Neuf chez nous : […] traiter la sortie comme une fertilité calibrée » est, en l'état, une zone revendiquée déjà occupée (R8).
- **Krenn et al. 2023, Science4Cast** (vérifié sur arXiv 2210.00881 : plus de 64 000 concepts, plus de 100 000 articles ; revue *Nature Machine Intelligence* d'après le DOI, SUPPOSÉ). La réponse écrit « graphe de concepts d'IA de Science4Cast 2015-2021 » : les bornes 2015-2021 ne sont pas confirmées par la page de résumé ; à vérifier sur le PDF (R7) avant de les réutiliser.
- **Prédiction de liens d'ordre supérieur sur hypergraphes temporels** : Benson, Abebe, Schaub, Jadbabaie et Kleinberg 2018, « Simplicial closure and higher-order link prediction » (PNAS, SUPPOSÉ pour la revue ; arXiv 1802.06916 vérifié). C'est le cadre de référence pour « prédire quelle hyperarête apparaîtra » avec partage temporel et lignes de base d'ordre supérieur (voisins communs, Adamic-Adar généralisés). Non cité, alors que la réponse propose précisément cette tâche.
- **Apprentissage de représentations sur hypergraphes** : aucune référence. De mémoire (SUPPOSÉ) : Feng et al. 2019 (réseaux de neurones sur hypergraphes, AAAI), Yadati et al. 2019 (HyperGCN, NeurIPS), Chien et al. 2022 (AllSet, ICLR). Pour le point « identifier l'hypergraphe » de Lazar, le voisin le plus proche est l'inférence conjointe d'hyperarêtes et de communautés : Contisciani, Battiston et De Bacco 2022 (*Nature Communications*, SUPPOSÉ) et les modèles à blocs stochastiques sur hypergraphes (Chodrow, Veldt et Benson 2021, SUPPOSÉ). Cela répond directement à « chapelles apprises plutôt que décrétées », mieux que « Leiden puis partition apprise comparée ».
- **Témoins durs en prédiction de liens dynamiques** : Poursafaei, Huang, Pelrine et Rabbany 2022 (NeurIPS, jeux de données et bancs ; vérifié) montrent que les témoins aléatoires rendent la tâche triviale et introduisent les témoins « historiques » et « inductifs ». Pour les hypergraphes, Patil, Sharma et Murty 2020 (AAAI, SUPPOSÉ) sur l'échantillonnage négatif. Yang, Lichtenwalter et Chawla 2015 (SUPPOSÉ) sur l'évaluation de la prédiction de liens sous fort déséquilibre : l'aire sous la courbe ROC y est jugée trompeuse. Non cités ; or c'est le cœur du « tout le soin va dans les témoins ».
- **Modèles à goulot de concepts** : Koh et al. 2020 (ICML, SUPPOSÉ). Non cité ; la réponse décrit la méthode sans la nommer.
- **Régression symbolique** : Cranmer et al. 2020 (NeurIPS, SUPPOSÉ), Udrescu et Tegmark 2020 (AI Feynman, SUPPOSÉ), outil PySR. Non cités.
- **Découverte fondée sur la littérature avec coupure temporelle** : Sybrandt, Tyagin et Safro 2020 (AGATHA, CIKM, SUPPOSÉ), qui évaluent précisément des prédictions de liens futurs entre termes biomédicaux avec coupure et témoins. Non cité.
- **Attribution imprécise** : « redécouvertes étalons d'Arrowsmith ». Arrowsmith est l'outil de Smalheiser et Swanson ; les redécouvertes étalons sont celles de Swanson (huile de poisson et maladie de Raynaud 1986 ; magnésium et migraine 1988, SUPPOSÉ) reprises comme banc par la communauté. À réécrire « les redécouvertes de Swanson, utilisées comme étalon ».
- **Nouveauté revendiquée trop large** : « apprendre la représentation elle-même […] au lieu de la coder à la main » — Sourati et Evans 2023 apprennent déjà des plongements par marches aléatoires sur hypergraphe ; Krenn 2023 apprend des représentations de nœuds. Ce qui serait neuf, et qu'il faut dire, c'est l'apprentissage conjoint de la partition en niches, de la fonction de reprise et de la loi de transition, sous préenregistrement.

## (c) Ce qu'un expert aurait dit et qui manque

- **Fuite par les étiquettes** : les « concepts » et « sujets » d'OpenAlex sont assignés par un classifieur entraîné après coup ; Semantic Scholar assigne l'intention des citations par un modèle postérieur. Un graphe « d'avant T1 » construit avec ces étiquettes contient déjà du futur. Il faut soit des concepts extraits par des méthodes datées (vocabulaire figé avant T1), soit une mesure de la fuite par comparaison. Non dit.
- **Fuite par la croissance exponentielle** : Krenn 2023 insiste sur le fait que le réseau croît exponentiellement ; une calibration faite sur T1-T2 ne se transfère pas à > T2 parce que le taux de base change. La réponse propose des diagrammes de fiabilité sans dire qu'ils doivent être refaits par fenêtre et comparés.
- **Métrique sous déséquilibre** : l'aire sous la courbe ROC est quasi inutilisable quand les liens positifs sont rares ; l'expert demande l'aire sous la courbe précision-rappel et la précision dans les k premiers avec k fixé par le budget du bisociateur. La réponse mentionne « avec taux de base », ce qui est insuffisant.
- **Étiquette de fertilité** : « lien apparu après T2 » n'est pas « lien fertile ». L'expert fixe l'étiquette (lien apparu ET repris au-delà d'un seuil de citations ou de réutilisation à horizon fixe, fenêtre figée), comme Gu et Krenn. Voir RL4-02.
- **Transfert** : mentionné deux fois mais jamais défini. L'expert précise : entraîner sur un champ (physique quantique de Krenn), tester sur un autre (intelligence artificielle), et mesurer la perte ; sinon on apprend les manies d'un champ.
- **Transition de phase lue sur les données, pas sur le modèle** : un classifieur à sortie sigmoïde fabrique toujours une forme en seuil ; la transition doit être montrée sur le taux empirique de liens fertiles par classe du paramètre de contrôle, avec intervalles, puis comparée aux formes (droite, seuil, cloche d'Uzzi 2013). Voir RL4-03.
- **Témoins pour la loi** : pour distinguer « cloche » de « seuil », il faut des paires de niches sur toute la plage du paramètre, y compris celles qui ne se rencontrent jamais ; la réponse le dit pour la fonction mais pas pour la loi.
- **Multiplicité** : apprendre dimensions, chapelles, fonction et loi en même temps multiplie les degrés de liberté ; un expert exige un ordre (partition gelée avant la fonction, fonction gelée avant la loi) et une pénalité ou des jeux de test distincts par étage.

## (d) Confusions

- « Probabilité de reprise d'une paire » (point 1) contre « prédire les liens futurs » (reformulation, étape 2) : deux cibles différentes présentées comme une seule.
- « Tests de mort » rangés dans « vérification hors de nous » (point 4) alors qu'ils sont les nôtres ; seuls le futur, les bancs publics avec classement et la reproduction par un tiers sont hors de nous.
- « Transition de phase comme propriété de la fonction apprise » : la fonction apprise est un objet du modèle ; la propriété doit être celle des données.

## (e) La reformulation est-elle testable ?

Pas encore. Il manque : (i) un critère de mort chiffré, par exemple « si, sur le banc Science4Cast rejoué avec témoins historiques, le modèle n'améliore pas la précision dans les k premiers d'au moins X points sur la meilleure ligne de base publiée, l'hypothèse “la fertilité s'apprend au-delà de la popularité” est morte » (X à fixer au préenregistrement après lecture du PDF de Krenn 2023) ; (ii) une référence à battre nommée (Krenn 2023 pour les liens ; Gu et Krenn 2024 pour les liens à impact ; Benson 2018 pour les hyperarêtes), avec le chiffre vérifié sur PDF (R7) ; (iii) le témoin « popularité seule » : un modèle n'ayant que degré, âge et taux de croissance, qui doit être battu pour que le mot « fertilité » ait un sens ; (iv) l'étiquette de fertilité gelée (horizon, seuil de reprise). Sans ces quatre éléments, l'étape 2 et l'étape 4 de la reformulation ne peuvent pas entrer dans un préenregistrement (R1).

## Constats numérotés

| N° | Constat | Gravité |
|---|---|---|
| RL4-01 | Antériorité manquée : Gu et Krenn 2024 (arXiv 2402.08640, vérifié) prédisent déjà les liens à fort impact sur graphe sémantique et d'impact ; la revendication « neuf : fertilité calibrée » est occupée en l'état (R8). | Majeure |
| RL4-02 | Cible confondue : « reprise d'une paire » (point 1) et « lien futur » (reformulation) ; l'étiquette de fertilité (horizon, seuil) n'est pas définie. | Majeure |
| RL4-03 | Transition de phase cherchée dans la fonction apprise, qui par construction (sigmoïde) montre un seuil ; à lire sur le taux empirique par classe du paramètre, avec témoins sur toute la plage. | Majeure |
| RL4-04 | Reformulation sans critère de mort chiffré, sans référence à battre nommée et sans témoin « popularité seule » ; non préenregistrable en l'état (R1). | Majeure |
| RL4-05 | Fuite par les étiquettes (concepts et sujets OpenAlex, intentions de citation Semantic Scholar assignés après coup) non traitée ; fuite par croissance exponentielle sur la calibration non traitée. | Majeure |
| RL4-06 | Point (4) : « tests de mort » ne sont pas une vérification hors de nous ; à retirer ou à remplacer par la reproduction par un tiers sur les mêmes coupures. | Moyenne |
| RL4-07 | Témoins durs sans antériorité : Poursafaei et al. 2022 (vérifié), Patil et al. 2020 et Yang et al. 2015 (SUPPOSÉ) ; aire sous la courbe ROC à remplacer par précision-rappel et précision dans les k premiers, k fixé par le budget du bisociateur. | Moyenne |
| RL4-08 | Hypergraphes : Benson et al. 2018 (vérifié) non cité pour la prédiction d'hyperarêtes ; inférence conjointe hyperarêtes et communautés (Contisciani et al. 2022, SUPPOSÉ) non citée, alors qu'elle répond à « identifier l'hypergraphe » et « chapelles apprises ». | Moyenne |
| RL4-09 | Goulot de concepts (Koh et al. 2020), régression symbolique (Cranmer et al. 2020 ; Udrescu et Tegmark 2020), découverte fondée sur la littérature avec coupure (Sybrandt et al. 2020) : méthodes décrites sans antériorité nommée (toutes SUPPOSÉ). | Mineure |
| RL4-10 | « Redécouvertes étalons d'Arrowsmith » : attribuer à Swanson (l'outil Arrowsmith est de Smalheiser et Swanson). | Mineure |
| RL4-11 | « Science4Cast 2015-2021 » : bornes non confirmées par la page de résumé d'arXiv 2210.00881 ; à vérifier sur PDF avant réemploi (R7). | Mineure |
| RL4-12 | Transfert entre domaines cité deux fois sans protocole (champ source, champ cible, perte tolérée). | Mineure |
| RL4-13 | Nouveauté « apprendre la représentation » trop large : Sourati-Evans 2023 et Krenn 2023 apprennent déjà des plongements ; la nouveauté défendable est l'apprentissage conjoint partition, fonction, loi, sous préenregistrement et avec ordre des étages. | Moyenne |

## Ce qu'il faudrait pour une v2 (sans allonger)

Ajouter trois lignes à la reformulation : l'étiquette de fertilité gelée ; la référence à battre (Krenn 2023 ; Gu et Krenn 2024) avec chiffre vérifié sur PDF ; le critère de mort chiffré contre le témoin « popularité seule ». Déplacer « tests de mort » hors du point (4). Remplacer « propriété de la fonction apprise » par « propriété du taux empirique ». Aucune décision prise par le relecteur.
