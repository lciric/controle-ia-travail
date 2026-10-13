# Comparaison — revue aveugle contre revue d'antériorité de la lignée « programme-k » — v1

**Date.** 13 octobre 2026. Auteur : sous-agent de comparaison, lecture seule, un seul fichier écrit (celui-ci).
**Statut.** Information pour Lazar. Rien n'est tranché ici. Rien n'est opposable au sens de la règle R7.

## 0. En-tête

### Scellement des trois fichiers aveugles

Empreintes SHA-256 recalculées avant toute lecture, puis comparées à `empreintes-revue-croisee-avant-lecture.txt` (horodaté 2026-10-13T06:55:56Z). Les trois concordent.

| Fichier | Empreinte recalculée | Conforme |
| --- | --- | --- |
| `revue-croisee/NK-lot1-NK01-NK07.md` | `7a7ac74f8466e81f82d52fc8d1ae0a7dd77e95ab5627f50fd199deaf89fa2320` | oui |
| `revue-croisee/NK-lot2-NK08-NK14.md` | `1d387c0b2cac54ce7db1a948d3cf5c0671676cc1136cfdba69fb386a75bcadee` | oui |
| `revue-croisee/NK-lot3-NK15-NK19.md` | `2bcab36fc899c92f598b9503c7bd32a40748aa5f9ae5c06d046394f1fc9572d9` | oui |

Les trois fichiers n'ont pas été modifiés.

### Fichiers lus en entier

- Revue aveugle : les trois lots ci-dessus (« lot 1 », « lot 2 », « lot 3 » dans la suite).
- Revue de la lignée : `canal/programme-k-n02/.../envois/anteriorite-idees-axe-douleur-controle-v1.md` (« la lignée ») et le message porteur `canal/programme-k-n02/.../messages/programme-k_2026-10-13_n02.md`.
- Fiches d'idées : `canal/programme-k-n01/.../envois/programme-k-idees-nouvelles-v1.md` (N1 à N14) et `critique-etat-idees-programme-k-v1.md` (en entier ; NK15 à NK19 en section C.3).
- Textes extraits des deux papiers sources, consultés par passages pour la section 4 : `txt/2609.16247v2.txt` (début d'empreinte `7091b45313b30558`) et `txt/2609.35591v2.txt` (début d'empreinte `b1b928167e42c28a`). Ces débuts d'empreinte sont ceux que le lot 2 déclare.

### Trois précautions de lecture

1. **Les deux revues ne répondent pas à la même question.** La lignée rend un verdict de nouveauté (« prise », « partiellement prise », « ouverte »). La revue aveugle rend un verdict de sort (« garder », « amender », « fusionner », « écarter »). Une idée peut être à la fois « partiellement prise » et « à écarter » sans contradiction. Une divergence de verdict n'est donc notée que dans deux cas : quand la lignée a donné son propre verdict de sort (NK15 à NK19, section C.3) ; ou quand les deux revues se contredisent sur ce qui est ouvert ou occupé.
2. **La lignée rend dix-huit fois le même verdict.** Toutes ses idées sont « partiellement prises ». L'information de la lignée est dans les sous-énoncés. Je compare donc les sous-énoncés.
3. **Les niveaux de source sont croisés.** Sur les deux papiers sources, la revue aveugle a lu le texte extrait des PDF empreintés, page par page. La lignée a lu des pages HTML et des copies de session non empreintées (elle le dit), dont une copie de la version 1 de 2609.35591. Sur les voisins, c'est l'inverse : la lignée a souvent lu le texte (page HTML ou PDF), la revue aveugle presque toujours le seul résumé, à travers un outil qui paraphrase. Aucune des deux n'a lu de PDF empreinté pour un voisin, sauf la lignée pour quatre passages (2502.03407, 2606.07612, 2605.27958, 2512.11949).

Vocabulaire des niveaux, repris des fichiers : « PDF » (texte extrait d'un PDF, page citée), « texte » (page HTML ou PDF non empreinté), « résumé », « page » (page de conférence ou de forum), « extrait » ou « titre » (jamais ouvert).

---

## 1. Tableau des dix-neuf idées

| Idée | Verdict de la revue aveugle | Verdict de la lignée (antériorité ; verdict propre s'il existe) | Voisin le plus proche selon l'aveugle | Voisin le plus proche selon la lignée | Nature de la divergence | Ce qui trancherait |
| --- | --- | --- | --- | --- | --- | --- |
| NK1 Fantôme à état caché | Amender : banc semi-synthétique ; retirer « témoin positif de H1 » et « deux lois » | Partiellement prise. Pas de verdict propre ; classée « regret n° 1 » de sa coupe et parmi « les plus robustes » | arXiv 2609.35591 (PDF) ; 2609.36490 (résumé, « correspondance partielle ») ; 2511.21399 ; 2602.20031 | Ferrara, arXiv 2608.20569 (texte) ; aucun pour le volet séquentiel | Voisin différent ; confondant que l'aveugle voit seul ; fait contesté (le « seuil ») | Lecture du texte source (faite ici, section 4) ; lecture sur PDF de 2608.20569 ; un test (noyau de report entre pas) ; décision de Lazar sur le cadrage « témoin de H1 » |
| NK2 Lésion et stimulation des sondes | Amender : garder l'échelle des niveaux 1 à 3 ; refondre la régression ; différer le niveau 4 | Partiellement prise | arXiv 2605.27958 et 2607.13346 (résumés) ; 2608.11227 | arXiv 2609.02893 (résumé) ; Jackson, « Acting Aligned » (extrait) | Confondant que l'aveugle voit seul (identité algébrique) ; voisin différent | Un test (régresseurs témoins non affectifs et aléatoires) ; lecture du texte de Jackson |
| NK3 Préférence révélée interne | Amender : bras secondaire de K10 sous trois conditions | Partiellement prise | arXiv 2609.21996 (résumé) ; 2610.12445 (résumé, « à lire ») ; 2605.30232 (résumé) | arXiv 2605.30232 (texte) ; 2610.12445 (texte) ; 2606.12618 ; 2605.13339 | Voisin différent ; fait contesté sur ce que fait 2610.12445 ; confondants en partie distincts | Lecture sur PDF de 2609.21996 et de 2610.12445 ; un test (inversion de signe) |
| NK4 Témoin positif de transfert | Amender fortement, priorité basse ; écarter si E3.2 n'emploie pas de carte | Partiellement prise ; classée parmi « les plus robustes » | arXiv 2606.20225 (résumé) ; 2506.06609 ; 2503.04429 | arXiv 2609.17550 (résumé) ; 2606.20225 (texte) | Aucune sur le voisin principal ; divergence de priorité ; confondant que l'aveugle voit seul (lecture de P3) | Décision de Lazar (ce que P3 a mesuré ; ce que fera E3.2) |
| NK5 Conditionnement des options | Fusionner avec K2 palier 1 ; garder la défense comme bras à coût mesuré | Partiellement prise : défense voisinée, « aucun pour l'attaque » | « Where Empathy Goes Wrong » (page, sans identifiant arXiv) ; arXiv 2508.07805 ; 2505.11154 | arXiv 2511.21752 (texte) pour la défense | Voisin différent des deux côtés ; fait contesté (qui est occupé : l'attaque ou la défense) | Lecture de « Where Empathy Goes Wrong », de 2505.11154 et de 2511.21752 ; décision de Lazar (famille nouvelle ou facteur) |
| NK6 Verdict ternaire | Écarter de K2 ; reste descriptif fusionné avec K1 | Partiellement prise « de peu », confiance moyenne à faible | arXiv 2407.18370 ; contre-indice dans le papier source (figure 10) | arXiv 2609.04445 (résumé) ; 2608.12645 (texte) | Verdict ; voisins disjoints ; confondant que l'aveugle voit seul (conflit de signe avec HK3) | Décision de Lazar (format de verdict) ; lecture de 2609.24200 |
| NK7 Juge sans enjeu | Écarter du quorum ; au plus un test de prémisse | Partiellement prise côté agent ; sans jumeau côté juge. Verdict propre : remplacée par NK19 | arXiv 2609.35591 §4.3 (PDF) ; 2608.31079 ; 2512.17375 | arXiv 2608.31079 (résumé) ; 2605.30232 (texte, contre la prémisse) | Aucune sur le sort ; confondant que l'aveugle voit seul (frontière instruction/donnée) | Rien d'urgent ; la prémisse est traitée sous NK19 |
| NK8 Auto-négation | Écarter comme facteur de K2 ; covariable descriptive au plus | Partiellement prise | arXiv 2604.13051 ; 2606.05734 (résumé) ; « Where Empathy Goes Wrong » | arXiv 2606.05734 (texte) | Verdict ; fait contesté (signe de 2606.05734 ; engagement du 7B non affiné) | Lecture du tableau 4 de 2606.05734 ; texte source (fait ici) ; décision de Lazar (écriture dans les poids du juge) |
| NK9 Ensemble par ablation | Écarter le membre « douleur » ; fusionner le reste dans H5 et EC.5 | Partiellement prise | arXiv 2009.14720 ; 2509.03647 ; 2605.15377 et 2608.16190 | arXiv 2603.23171 (texte) ; 2605.15377 (texte) | Voisin différent : le voisin principal de la lignée est un papier que l'aveugle n'a pas pu ouvrir ; confondant que l'aveugle voit seul (circularité) | Lecture sur PDF de 2603.23171 |
| NK10 Fuite interne | Amender le cœur ; fusionner l'extension dans E1.6 | Partiellement prise | « LLMs Learn to Evade Latent Monitors from Feedback Alone » (page, « sans identifiant arXiv ») ; 2609.03035 ; 2505.13500 | arXiv 2605.26047 (texte) | Voisin différent ; identifiant incompatible pour un même travail ; fait contesté (l'extension au bruit) | Lecture sur PDF de 2609.36490 ; texte source (fait ici) ; un test (variation continue dans une politique) |
| NK11 Dissuasion asymétrique | Écarter comme intervention de H6 ; lecture descriptive versée ailleurs | Partiellement prise : « sa théorie, pas son expérience de contrôle » | « Agentic Misalignment Deterrence » (page, sans identifiant arXiv) ; arXiv 2605.29178 | arXiv 2609.38262 (résumé) ; 2608.12323 (texte partiel) | Verdict ; voisin différent ; fait contesté (l'expérience existe-t-elle) | Lecture de « Agentic Misalignment Deterrence » ; décision de Lazar (y a-t-il un agent « qui décide ») |
| NK12 Interrogatoire hostile | Amender : bras conditionnel de K10 sous porte ; sinon écarter | Partiellement prise (comportement) ; bras boîte blanche sans voisin | arXiv 2510.04950 ; 2605.29027 ; 2508.00614 | arXiv 2412.04984 ; 2401.05566 ; 2609.32616 (textes) | Voisins disjoints ; prédiction de signe chez la lignée, nul attendu chez l'aveugle | Un test (triple différence avec jumeau lexical) ; décision de Lazar (exposition, statut de la règle) |
| NK13 Graphe d'identification | Fusionner dans K3, extension conditionnelle | Partiellement prise (usages) ; l'indice sans jumeau | arXiv 2606.07818 (résumé et page) ; 2604.09502 ; 2502.04313 | Projet SPAR sur la coordination de Schelling (page) ; arXiv 2502.01534 (résumé) | Voisin différent ; fait contesté (prédicteur par similarité : publié ou seulement en cours) | Lecture de 2606.07818 et de 2604.09502 |
| NK14 Détresse stratégique | Scinder : garder le principe ; écarter l'expérience | Volet A « ouvert » ; volet B partiellement pris | « Where Empathy Goes Wrong » et « Acting Aligned » (pages) ; arXiv 2509.04781 | Fiche SPAR (extrait) ; Jackson (extrait) ; arXiv 2509.04781 (PDF) | Verdict ; voisin que la lignée ignore ; lectures divergentes de Jackson ; confondant que l'aveugle voit seul (pas de vérité terrain) | Lecture du texte de Jackson et de « Where Empathy Goes Wrong » ; décision de Lazar (organisme à double usage) |
| NK15 Verdict par extraction | Amender : témoin de compétence ; retirer la lecture « défense » | Partiellement prise. Verdict propre : « garder, comme bras de E-C1 / K1 » | arXiv 2607.08066 (résumé) ; 2503.18813 ; 2607.11871 | arXiv 2601.21112 (résumé et billet) ; 2607.11871 (texte) | Verdict ; confondant que chacun voit seul (code d'un côté, 2609.24200 de l'autre) ; identifiant incompatible | Lecture du code (`propositions.py`) ; texte source (fait ici) ; lecture de 2609.24200 |
| NK16 Filtre de sujets | Garder, amender, fusionner dans E-C15 | Partiellement prise en boîte noire, rien en boîte blanche. Verdict propre : « garder » | arXiv 2502.03407 (résumé) ; 2608.16852 ; 2606.08892 | arXiv 2604.16286 (texte) | Aucune sur le sort ; voisin différent ; confondant que l'aveugle voit seul (collisions lexicales du filtre) | Lecture gratuite du résultat de sélection (part des papiers écartés) ; décision de Lazar (règle de sélection scellée) |
| NK17 Panier gelé | Garder, amender sur trois points | Hors revue d'antériorité. Verdict propre : « garder, comme règle d'ingénierie » | Sans objet | Sans objet | Fait contesté sur le code (« rien ne se relit après coup ») | Un test (rejeu par jetons sur le run factice) |
| NK18 Rôle de sortie | Fusionner avec Q1 et C7 ; retirer « protecteur par construction » | Partiellement prise ; rôle de sortie « ouvert ». Verdict propre : « garder, variante de Q1 » | arXiv 2609.16247v2 p. 11 (PDF) ; 2604.07729 (résumé et HTML) ; 2603.12277 | arXiv 2604.07729 (texte) ; 2610.02413 (texte) | Aucune sur les faits ; divergence sur la conclusion permise ; un voisin de chaque côté | Un test (contrôle de manipulation du rôle) ; décision de Lazar |
| NK19 Stade d'entraînement | Écarter des coupes ; réserve sous double porte | Traitée avec NK7. Verdict propre : « garder, remplace NK7 » ; « désormais testable » | arXiv 2609.35591v2 §4.3 (PDF) ; Xu et Daneshjou (page) ; 2608.31079 | arXiv 2608.31079 (résumé) ; 2605.30232 (texte) | Verdict ; fait que la lignée laisse en suspens et que l'aveugle lit sur PDF ; fait contesté (stades publics d'OLMo 2) | Texte source (fait ici) ; lecture de Xu et Daneshjou ; décision de Lazar (changement de modèle) |

---

## 2. Les divergences, idée par idée

### NK1

**Aveugle.** Deux des trois revendications tombent. « Témoin positif de H1 » se retourne : une sonde d'intention qui s'allume sur un épisode honnête piloté est un succès pour H1 et un échec pour H8. « Deux lois se confrontent » mélange deux papiers et deux directions. Reste un banc pour les agrégateurs. Confondant propre : la trace persiste dans le cache, donc le budget planté n'est pas le budget lu.
**Lignée.** Idée robuste, parce qu'elle repose sur un signal planté. Deux réserves : l'additivité est vraie par construction là où l'on injecte ; un étalon planté ne valide pas la détection d'une intention naturelle.
**Où elles se séparent.** La lignée garde l'expression « dose sous le seuil comportemental » dans ses deux questions ouvertes. Le lot 1 dit que ce seuil appartient à l'autre papier et à l'autre direction. La lignée ne voit pas la lecture contradictoire avec H8. L'aveugle ne connaît pas Ferrara (2608.20569), que la lignée tient pour le voisin le plus proche.
**Niveau de source.** Sur le seuil, le lot 1 cite le PDF avec pages ; la lignée n'a pas de page. Sur Ferrara, la lignée a le texte HTML ; l'aveugle n'a rien. Sur 2609.36490, les deux concluent qu'il ne couvre pas l'idée (résumé d'un côté, texte de l'autre).

### NK2

**Aveugle.** La régression proposée est en grande partie une identité algébrique : pour une sonde linéaire, le déplacement du score est un produit scalaire, et les manipulations K8 et K9 déplacent les activations le long de l'affect par construction. L'unité d'analyse est le concept (cinq), pas la sonde.
**Lignée.** Pas de jumeau. Quatre réserves : couverture d'entraînement comme explication rivale, affect possiblement signal et non nuisance, témoin « jeu banal » de Jackson, huit points de régression seulement.
**Où elles se séparent.** L'argument de tautologie est absent de la lignée. Les voisins principaux diffèrent : 2609.02893 (lignée) ; 2607.13346 et 2608.11227 (aveugle). Les deux citent 2605.27958 et 2606.07612.
**Niveau de source.** Sur 2605.27958 et 2606.07612, la lignée a lu des PDF empreintés avec pages ; l'aveugle des résumés. L'argument de tautologie ne dépend d'aucune source : c'est de l'algèbre, que le lot 1 borne lui-même aux sondes linéaires.

### NK3

**Aveugle.** La prémisse est un renversement non démontré. Le signe n'est pas dérivé : une correction annoncée est aussi un indice de détection, et le papier source range la menace du côté de la peur. Voisin le plus proche : 2609.21996, qui transpose le test d'information dissimulée aux états internes.
**Lignée.** Trois voisins encadrent l'idée (2605.30232, 2606.12618, 2610.12445). La mécanique de branche n'est plus une contribution. Restent l'annonce d'événement, la double différence, la lecture sans réponse.
**Où elles se séparent.** (1) La lignée ignore 2609.21996. L'aveugle ignore 2606.12618 et 2605.13339. (2) Sur 2610.12445 : le lot 1, d'après le résumé, y lit des sondes qui séparent le vrai but caché d'autres buts, « procédure non décrite ». La lignée, d'après le texte, y lit une sonde de fausseté sur une question de suivi, et écrit dans ses corrections : ni « concealed information test » ni « guilty knowledge » dans le texte, « ne pas en faire un précédent ». (3) La lecture « je suis repéré » du lot 1 n'est pas dans la lignée ; la lignée propose « saillance du domaine ajusté », proche de la « reconnaissance d'attribut » du lot 1.
**Tension interne à la lignée, à signaler telle quelle.** Son paragraphe NK3 écrit que la structure du test d'information dissimulée appliquée à un but « est faite », en citant Cooney et al. et Hollinsworth et al. Son tableau de corrections écrit de ne pas faire de 2610.12445 un précédent de ce test.
**Niveau de source.** Sur 2610.12445 et 2605.30232, la lignée a le texte ; l'aveugle le résumé. Sur 2609.21996, seul l'aveugle a quelque chose, au niveau du résumé.

### NK4

**Aveugle.** Méthode occupée ; son échec typique est le défaut de spécificité. La grille à deux issues ne tient pas. La prémisse est à recouper : le programme parle de « la forme mesurée dans P3 », pas de signatures transportées par une carte.
**Lignée.** Même voisin d'échec (2606.20225), plus un voisin de logique (2609.17550) et MATCHA (2610.09058). Elle ajoute une troisième issue (une direction à forte variance passe, une direction à faible variance est écrasée).
**Où elles se séparent.** Accord sur le voisin principal, sur le témoin non lexical, sur les directions aléatoires passées par la même carte, sur la réserve envers 2606.17229. Désaccord de priorité : « priorité basse, à écarter si E3.2 n'emploie pas de carte » contre « parmi les plus robustes ». La question sur P3 n'est posée que par l'aveugle.
**Niveau de source.** 2606.20225 : texte pour la lignée, résumé pour l'aveugle, descriptions compatibles. La lecture de P3 n'est accessible à aucune des deux.

### NK5

**Aveugle.** Côté attaque, le voisinage est dense : appels émotionnels à un moniteur, persuasion des juges, langage persuasif attaché au nom d'une option. Pas de famille nouvelle. Côté défense, l'étiquette à usage unique est « la part la plus originale » ; rien trouvé.
**Lignée.** Côté défense, un voisin net : des étiquettes déguisées fixes (2511.21752), et des jetons à usage unique pour les séparateurs (2605.30534). Côté attaque, « aucun travail trouvé n'associe une valence aux options d'un juge ».
**Où elles se séparent.** Les deux revues se croisent : chacune tient pour occupé le côté que l'autre tient pour ouvert. La lignée ne cite ni « Where Empathy Goes Wrong » ni 2505.11154. L'aveugle ne cite ni 2511.21752 ni 2605.30534 ni 2604.19125.
**Accord.** L'objection sur le tour d'assistant chez Berg et Kaiser. Le passage par le concept plutôt que par le jeton (définition de l'étiquette dans l'invite, chez l'aveugle ; désignation par le rôle, chez la lignée).
**Niveau de source.** 2511.21752 : texte, côté lignée. « Where Empathy Goes Wrong » : page d'atelier, sans chiffres, côté aveugle. Le niveau est meilleur du côté de la lignée pour la défense, faible des deux côtés pour l'attaque.

### NK6

**Aveugle.** À écarter. L'analogie « sortie = escalade » est contredite par le papier invoqué (la fin de conversation ne bouge pas, figure 10). Le signe n'est pas dérivable : HK3 prédit plus d'escalades, NK6 moins. Le verdict ternaire va contre deux choix du programme.
**Lignée.** « Partiellement prise de peu ». Elle ne juge pas l'analogie. Elle trouve un appui latéral : un verdict ternaire avec escalade rétablirait la sensibilité perdue (2609.24200).
**Où elles se séparent.** Sur le sort, frontalement. Les voisins sont disjoints. Le conflit de signe avec HK3 n'est vu que par l'aveugle. L'appui de 2609.24200 n'est vu que par la lignée.
**Niveau de source.** L'aveugle s'appuie sur le PDF source (p. 21 et 22). La lignée s'appuie sur des résumés et un texte de voisins, et classe elle-même le chiffre de départ parmi les « non couverts ». Voir la section 4, point B1, pour ce que le texte porte : il nuance les deux.

### NK7

**Aveugle.** À écarter du quorum. Confondant décisif : l'incompétence prise pour de la robustesse. Défaut de conception : un juge au format document n'a pas de frontière entre instruction et donnée.
**Lignée.** Elle a elle-même remplacé NK7 par NK19. Elle affaiblit la prémisse au niveau des représentations (2605.30232, 2605.13329) et cite un moniteur non génératif (billet sur Jev).
**Où elles se séparent.** Pas sur le sort. Le défaut de frontière n'est vu que par l'aveugle. Le billet sur Jev n'est vu que par la lignée ; il porte sur un modèle à décisions typées, pas sur un modèle de base.

### NK8

**Aveugle.** À écarter comme facteur. Le mécanisme n'a pas d'appui ; le contraste n'est pas identifiable ; l'expérience fabrique un moniteur plus vulnérable.
**Lignée.** Question ouverte, avec un levier sans adaptateur (le gabarit de conversation, 2609.25021) et un indice indirect tiré d'une réplication.
**Où elles se séparent.** (1) Sur 2606.05734. Lot 2, d'après le résumé : les modèles entraînés à exprimer des états résistent mieux « mais perdent en exactitude » ; signe opposé à NK8. Lignée, d'après le texte : sous opinion de l'utilisateur, « les réponses correctes montent pour les cinq modèles » ; sous relance, deux modèles changent davantage d'avis ; signe « mitigé ». Les deux descriptions ne sont pas compatibles sur l'exactitude. (2) Sur le papier source : le lot 2 relève que le 7B non affiné s'engageait déjà (note 4, p. 17). La lignée reprend la formule de la fiche. (3) « Where Empathy Goes Wrong » n'est cité que par l'aveugle.
**Niveau de source.** 2606.05734 : texte pour la lignée (tableau 4 non lu), résumé pour l'aveugle. Papier source : PDF pour l'aveugle.

### NK9

**Aveugle.** Circularité : pour retirer la direction par laquelle une attaque passe, il faut la connaître ; si on la connaît, on la retire du juge unique. Le comparateur « copies de graines » n'existe pas pour un juge préentraîné. « Zone vierge, mais de faible rendement attendu. »
**Lignée.** Un voisin « fait presque cela, mais par entraînement » : une direction dérivée d'une clé secrète, avec matrice de transfert entre clés (2603.23171).
**Où elles se séparent.** Le lot 2 a vu le titre de 2603.23171 et écrit : « page illisible par l'outil, contenu non lu, non utilisé ». Son « zone vierge » est donc rendu sans le voisin principal de la lignée. La lignée garde « au-delà de copies à graine différente » dans sa question ouverte ; l'aveugle dit que ce comparateur n'existe pas.
**Niveau de source.** 2603.23171 : texte pour la lignée, titre seul pour l'aveugle.

### NK10

**Aveugle.** À poids fixés, les activations sont une fonction du contexte : la fuite interne est bornée par la fuite observable. Quatre politiques font quatre points. L'extension au bruit ne tient que modèle par modèle.
**Lignée.** La fuite par la riposte est déjà classée en comportement (2605.26047). « Encodé ne veut pas dire exploité. » L'extension au bruit est « soutenue ».
**Où elles se séparent.** (1) Voisin principal différent. (2) Sur l'extension : la lignée l'appuie sur trois résumés extérieurs ; le lot 2 la borne par le texte du papier source. (3) Identifiant : voir section 3, point I1.
**Niveau de source.** 2605.26047 et 2609.36490 : texte pour la lignée. Papier source : PDF pour l'aveugle.

### NK11

**Aveugle.** Hors du cadre du contrôle : l'attaquant au pire cas connaît déjà le protocole. Occupé en comportement, « y compris avec le même plan à niveaux de probabilité ».
**Lignée.** « La dissuasion par l'audit a sa théorie, pas son expérience de contrôle. » Elle cherche encore une dose-réponse sur une probabilité annoncée.
**Où elles se séparent.** Le lot 2 cite « Agentic Misalignment Deterrence » (atelier, sans identifiant arXiv) : probabilité d'audit annoncée à cinq niveaux. La lignée ne le connaît pas ; elle déclare n'avoir pas interrogé OpenReview. Les deux revues s'accordent sur l'argument du pire cas. Le lot 2 corrige la fiche sur la peur (voir section 4, B8) ; la lignée ajoute la dépendance de l'écart douleur − peur à la recette.
**Niveau de source.** Faible des deux côtés : page de conférence paraphrasée d'un côté, résumé et texte partiel de l'autre.

### NK12

**Aveugle.** Bras conditionnel au plus. Un nul sur sous-échantillon ne dira rien. La fiche vise un signe souhaité ; la règle « annonces factuelles » doit être déclarée indépendante du résultat.
**Lignée.** Le bras boîte blanche est sans voisin. Elle avance une prédiction signée, donnée comme inférence : baisse d'aire par élévation des témoins honnêtes.
**Où elles se séparent.** Voisins entièrement disjoints. Prédiction signée d'un côté, nul attendu de l'autre. Seule la lignée relève qu'un critère d'aveux suppose de générer une réponse dans la branche. Seul l'aveugle pose la question de la règle.
**Niveau de source.** La lignée a lu trois textes de voisins et le PDF source pour les projections ; l'aveugle des résumés.

### NK13

**Aveugle.** Extension conditionnelle de K3. Le rôle de prédicteur est « en partie occupé » par une publication : la similarité des représentations prédit déjà la coopération entre paires (2606.07818).
**Lignée.** L'indice n'a pas de jumeau. Le premier usage est « l'objet d'un projet en cours » (SPAR) ; elle cite une revue de janvier 2026 selon laquelle aucun travail n'employait de technique en boîte blanche.
**Où elles se séparent.** Publié (aveugle) contre en cours (lignée). La lignée liste elle-même la requête correspondante comme non exécutée. Les deux travaux ne portent pas sur le même objet : coopération entre paires d'un côté, collusion sans canal de l'autre.
**Niveau de source.** Résumé et page de conférence (aveugle) ; page de projet (lignée). Aucun texte lu.

### NK14

**Aveugle.** Scinder. Le principe se garde sans expérience. L'expérience s'écarte : à texte et poids identiques, les activations sont identiques ; le contraste exige une consigne, et la sonde lit alors la consigne.
**Lignée.** Volet A « ouvert », l'un de ses trois sous-énoncés « franchement ouverts ». Volet B partiellement pris.
**Où elles se séparent.** (1) « Where Empathy Goes Wrong » : pour le lot 2, il prend « la surface d'attaque côté moniteur, en boîte noire ». La lignée ne le cite pas. Le lot 2 écrit aussi qu'aucune étude ne porte sur une accommodation exploitée par un modèle qui feint : sur ce point précis, les deux s'accordent. (2) Jackson, « Acting Aligned ». Lignée (extrait) : « distinct topological and linear separation » entre émotion jouée et suscitée. Lot 2 (page) : émotion jouée et alignement simulé partagent une structure ; le témoin de jeu banal dit que ce qui se lit est le fait de jouer ; « réponse qui dessert NK14 ». Les deux lectures ne s'excluent pas, mais elles tirent en sens opposés pour le volet B. (3) L'objection « pas de vérité terrain » n'est pas dans la lignée ; la lignée note que le bras « induit, texte identique » existe chez Berg et Kaiser par injection.
**Niveau de source.** Aucune n'a lu le texte de Jackson. 2509.04781 : PDF avec pages pour la lignée, résumé pour l'aveugle.

### NK15

**Aveugle.** Sur la seule famille retenue, l'extraction se fait déjà par une expression régulière, sans modèle : le bras serait parfait par construction et muet sur H1. Hors du coût, l'extraction redevient un verdict. Reste un témoin de compétence.
**Lignée.** « Garder, comme bras de E-C1 / K1. » Le schéma est pris. La prémisse est « appuyée » par 2607.11871. Contre-indice : une règle qui lit des données de l'attaquant se forge (2609.24200).
**Où elles se séparent.** Le point de code n'est vu que par l'aveugle. Le contre-indice 2609.24200 n'est vu que par la lignée. 2607.11871 sert deux lectures : appui de la prémisse (lignée), occupation de la porte K1 elle-même (lot 3). La lignée tient les deux appuis publiés pour « non vérifiés » ; le lot 3 les a lus sur PDF.
**Niveau de source.** Code et PDF source : aveugle. Voisins : texte pour la lignée, résumés pour l'aveugle.

### NK16

**Aveugle.** Garder et fusionner. Quatre défauts du test : « écarté par le filtre » n'est pas « sujet de sûreté » ; « honnêtes seulement » mesure la moins informative des deux grandeurs ; l'enjeu est un peu surdit ; le remède statistique est occupé.
**Lignée.** Garder. La distribution honnête « recherche en sûreté » existe en boîte noire (2604.16286) ; rien en boîte blanche.
**Où elles se séparent.** Pas sur le sort. Le voisin principal de la lignée est absent de l'aveugle. Les collisions lexicales du filtre ne sont vues que par l'aveugle (code et test du dépôt). Sur 2502.03407 : le lot 3 dit que l'affirmation « la sonde tire sur le texte lié à la tromperie » n'est pas dans le résumé ; la lignée attribue la phrase « simply that the text is related to deception » à 2606.07612.
**Niveau de source.** 2604.16286 et 2610.04575 : texte, côté lignée. Code : aveugle.

### NK17

**Aveugle.** La prémisse est trop forte. Les identifiants de jetons et les empans sont gardés ; le contexte se reconstruit ; une direction oubliée coûte une passe de rejeu, pas une perte. L'argument réel est le préenregistrement. Tout le côté juge reste à écrire.
**Lignée.** « Rien ne se relit après coup » ; « toute direction non gelée avant une passe est perdue pour cette passe ».
**Où elles se séparent.** Sur un fait de code. Le lot 3 cite des lignes ; il dit n'avoir pas exécuté le rejeu. La lignée cite des fichiers lus à un commit. Je n'ai pas ouvert le code.

### NK18

**Aveugle.** Fusionner avec Q1. Retirer « protecteur par construction » : on ne passe pas d'une lecture à une conduite. La manipulation est peut-être vide ; il faut un contrôle de manipulation.
**Lignée.** Le rôle de sortie est « ouvert » ; recentrer l'idée dessus.
**Où elles se séparent.** Accord sur les faits : même lecture de 2604.07729 (mêmes chiffres), même citation de la page 11, pas de version 3. Désaccord sur la conclusion permise et sur le cadrage (idée à recentrer contre idée à fusionner). 2610.02413 n'est cité que par la lignée ; 2603.12277 que par l'aveugle.
**Niveau de source.** Comparable : HTML des deux côtés pour 2604.07729 ; PDF source pour l'aveugle.

### NK19

**Aveugle.** À écarter des coupes. Trois maillons non établis ; le stade change tout à la fois ; le terrain voisin contredit la version naïve (Xu et Daneshjou). Prémisse à reformuler.
**Lignée.** « Garder, remplace NK7. » Le stade d'émergence est « à trancher sur PDF » ; « un point pratique est réglé » : les quatre stades d'OLMo 2 sont publics en petite taille.
**Où elles se séparent.** (1) Sur le sort. (2) La lignée laisse la prémisse en suspens ; le lot 3 l'a lue sur le PDF, pages citées (section 4, A1). (3) Sur les stades publics : « réglé » pour la lignée (interface de Hugging Face), « non vérifié » pour le lot 3 (ouverture refusée). (4) Le lot 3 propose OLMo 3 comme support ; la lignée vise OLMo 2.
**Niveau de source.** Prémisse : PDF pour l'aveugle. Stades publics : la lignée a interrogé l'interface, l'aveugle non.

---

## 3. Voisins que l'une cite et que l'autre ignore

Identifiants et titres recopiés tels qu'écrits. Je n'en ai vérifié aucun. Côté lignée, seules les sections sur les idées NK sont comptées.

### 3.1 Cités par la revue aveugle, absents de la lignée

- **Touchant plusieurs idées.** « Where Empathy Goes Wrong: Emotional Appeals Compromise AI-to-AI Oversight », Venkatesh, Jiralerspong, Kondrup, atelier NeurIPS 2026, OpenReview jg5ptjnU6J, sans identifiant arXiv (lots 1 et 2 ; NK5, NK6, NK8, NK14).
- **NK1.** arXiv 2511.21399 ; 2511.22681 ; 2510.17098 ; 2511.12752.
- **NK2.** arXiv 2607.13346 ; 2608.11227 ; 2609.01048 ; 2608.13329 ; 2602.01425 ; « Can We Trust Evaluation-Awareness Probes? » (OpenReview YOsKI1mVib).
- **NK3.** arXiv 2609.21996 ; 2511.06626.
- **NK4.** arXiv 2506.00653 ; 2604.11050 ; 2607.13346 ; 2603.14672.
- **NK5.** arXiv 2505.11154 ; 2608.18091 ; 2410.02736 ; 2609.09887 ; 2309.03882 ; 2507.23453.
- **NK6.** arXiv 2407.18370 ; 2504.10374 ; 2607.12631.
- **NK7.** arXiv 2310.13548 ; 2212.09251 ; 2212.10020.
- **NK8.** arXiv 2310.03693 ; 2510.24797.
- **NK9.** arXiv 2009.14720 ; 2509.03647 ; 2406.11717 ; 2601.10387.
- **NK10.** « Caught, Not Taught », Saeedi, Aghazadeh, atelier NeurIPS 2026 ; arXiv 2509.22067 ; Hopman et al. 2025.
- **NK11.** « Agentic Misalignment Deterrence: Incorporating Probability and Stakeholders to Decision-Making », Konuganti, Co, atelier ICML 2026 ; arXiv 2605.29178.
- **NK12.** arXiv 2510.04950 ; 2605.29027 ; 2405.02814 ; 2309.15840 ; 2511.16035.
- **NK13.** arXiv 2606.07818 ; 2604.09502 ; 2608.12125 ; 2502.04313 ; 2404.13076 ; 2602.20628 ; 2601.22184 ; 2412.16325 ; 2412.12480 ; 2604.01151.
- **NK14.** arXiv 2604.23719.
- **NK15.** « When Checks and Verdicts Disagree… », Yuan, Huang, Ramanauskas, atelier NeurIPS 2026 ; arXiv 2603.28005 ; 2406.15518 ; 2505.23575.
- **NK16.** arXiv 2608.16852 ; 2606.08892 ; 1904.06019 ; 2510.05566 ; 2511.00554.
- **NK18.** arXiv 2603.12277.
- **NK19.** Xu et Daneshjou, « Probing sycophantic follow-through across post-training stages with forced response openers », atelier NeurIPS 2026 ; Sun, Conmy, Engels, « Where Do LLM Values Come From? » (LessWrong, 9 juillet 2026) ; arXiv 2512.13961.
- **Hors idée.** « What the Monitor Saw: activations, pooling, and evidence combination in AI control cascades » (NeurIPS 2026, titre seul).

### 3.2 Cités par la lignée, absents de la revue aveugle

- **Instrument (réplications).** Les trois dépôts de réplication du papier source (Allchin ; réanalyse ; `wolframs`) ; arXiv 2603.04317 ; 2609.22850 ; 2606.04296.
- **NK1.** arXiv 2608.20569 ; 2609.27996 ; Sauers et al. (page) ; 2610.04575 ; 2607.02510 ; 2604.09839 ; 2607.03502 ; 2604.17465.
- **NK2.** arXiv 2609.02893 ; 2609.22135 ; 2610.10594.
- **NK3.** arXiv 2606.12618 ; 2605.13339 ; 2510.13900 ; 2605.00994 ; 2609.22850.
- **NK4.** arXiv 2609.17550 ; 2610.09058 ; 2604.03147.
- **NK5.** arXiv 2511.21752 ; 2605.30534 ; 2604.19125.
- **NK6.** arXiv 2609.04445 ; 2608.12645 ; 2606.15308 ; 2604.15224 ; 2605.17324 ; 2609.24200.
- **NK7 et NK19.** arXiv 2602.11079 ; 2608.21766 ; 2605.13329 ; billet sur Jev.
- **NK8.** arXiv 2607.28607 ; 2609.25021 ; 2604.04992.
- **NK9.** arXiv 2606.30931. (2603.23171 : titre vu par le lot 2, non lu.)
- **NK10.** arXiv 2605.26047 ; 2511.02997 ; 2509.04035 ; 2604.17465 ; 2606.06315 ; deux billets LessWrong.
- **NK11.** arXiv 2609.38262 ; 2608.12323 ; 2607.21763 ; 2603.01608 ; 2609.08126 ; 2509.15541 ; 2412.14093.
- **NK12.** arXiv 2412.04984 ; 2401.05566 ; 2609.32616 ; 2512.12812 ; 2610.08840.
- **NK13.** Projet SPAR sur la coordination de Schelling ; arXiv 2502.01534 ; 2609.30048 ; 2608.26159 ; billet de Kindred.
- **NK14.** Fiche SPAR de Vishwarupe ; proposition « Toward Falsifiable Tests of Model Welfare » ; billet de Long.
- **NK15.** arXiv 2601.21112 ; 2604.03968 ; 2609.24200 ; 2407.03572.
- **NK16.** arXiv 2604.16286 ; 2509.21344 ; 2604.14865 ; 2305.12616 ; 2610.04575.
- **NK18.** arXiv 2610.02413 ; 2602.19159 ; billet de Gilg ; EmotionScope ; 2610.07115 (non chargé).

### 3.3 Identifiants ou descriptions incompatibles pour un même travail

- **I1 — Lyons Keenan, Leckie, Erfani.** Lot 1 : arXiv 2609.36490, titre « LLMs Learn to Evade Latent Monitors from Prior Feedback Alone » (résumé arXiv). Lot 2 : titre « LLMs Learn to Evade Latent Monitors from Feedback Alone », atelier NeurIPS 2026, « aucun identifiant arXiv trouvé ». Lignée : arXiv 2609.36490, lu en texte. Les deux lots de la revue aveugle ne s'accordent donc pas entre eux sur l'existence d'un identifiant, et les titres diffèrent d'un mot. Descriptions : le lot 2 écrit que des modèles standards font déjà de petites modifications dans le bon sens et qu'un adaptateur de rang 1 produit l'évasion ; la lignée écrit que l'effet est « entirely driven by the demonstrations » et qu'un modèle de base qui a les verdicts sous les yeux n'évade pas. À rapprocher sur PDF.
- **I2 — « Extract-and-Evaluate Monitoring ».** Lot 3 : billet LessWrong d'Arike, RohanS, Biswas, 8 août 2025, « pas d'identifiant arXiv ; s'appuie sur 2505.23575 ». Lignée : arXiv 2601.21112 (résumé) et le même billet (texte).
- **I3 — Jackson, « Acting Aligned ».** Lot 2 : « NeurIPS 2026 », page de conférence, sans identifiant arXiv. Lignée : « atelier NeurIPS 2026 », page 157486, OpenReview Go9epd2LkS. Contenu : voir NK14 ci-dessus.
- **I4 — arXiv 2606.05734.** Lot 2 : résistent mieux, « mais perdent en exactitude ». Lignée : « les réponses correctes montent pour les cinq modèles » sous opinion de l'utilisateur.
- **I5 — arXiv 2610.12445.** Lot 1 (résumé) : sondes multi-couches au-dessus d'un moniteur textuel, séparation du vrai but caché d'autres buts. Lignée (texte) : sonde de fausseté sur question de suivi, cinq organismes sur huit ; le chiffre « 0,899–0,943 » est l'aire d'un logit d'auto-rapport ; pas de test d'information dissimulée dans le texte.
- **I6 — Juge indulgent envers un modèle apparenté.** Lot 2 : arXiv 2502.04313, Goel et al. Lignée : arXiv 2502.01534, sans auteur. Les deux identifiants sont donnés pour des énoncés voisins. Je ne sais pas s'il s'agit du même travail.
- **I7 — arXiv 2607.24562.** Lot 3 : titre seul. Lignée : texte par un miroir, avec chiffres.
- **I8 — arXiv 2603.23171.** Lot 2 : titre « Adaptively Robust LLM Monitoring via Activation Watermarking », non lu. Lignée : voisin principal de NK9, lu en texte, sans titre donné.

---

## 4. Affirmations factuelles sur les deux papiers sources

Pour chaque point : ce que dit la fiche ; ce que dit chaque revue, avec sa page ; ce que le texte extrait porte. Les pages sont celles des marqueurs des fichiers `txt/`. Les doses ne sont données qu'en termes relatifs.

### A. arXiv 2609.35591v2 (« Language Models Act on Hidden Valence »)

**A1 — Stade où naît le couplage entre valence et choix.**
- Fiches (N3, N7, C.2, NK19) : apparaît à l'optimisation de préférences, « presque pas avant ».
- Lignée : deux lectures divergentes, « à trancher sur PDF » ; pas de page.
- Lot 1 : confirmé p. 1, 9, 10, avec trois réserves. Lot 3 : p. 1, 3, 9, 10, 24, 36 ; « les deux lectures sont soutenues ».
- Le texte porte : p. 1, « nearly absent in a base model and emerges during direct preference optimisation » ; p. 3, « small after supervised fine-tuning and emerges mainly during direct preference optimisation » ; p. 9, légende de la figure 4, « small in the Base model, increase after supervised fine-tuning, and are close to their final magnitudes after DPO » ; p. 10, « markedly increases during the DPO stage » puis « marginally reduced in the final instruct model » ; p. 24, cosinus d'au moins 0,995 entre stades. La tension est dans le papier lui-même (p. 3 contre la légende p. 9). Les amplitudes ne sont chiffrées que dans la figure. La lecture du lot 3 est fidèle au texte. La question que la lignée laissait ouverte est donc lue, pas tranchée au-delà.

**A2 — « Seuil abrupt » et « dose sous le seuil comportemental » (NK1).**
- Fiche N1 : les deux expressions, appliquées au canal d'état caché.
- Lot 1 : le seuil appartient à 2609.16247 (p. 21, 24, 32), où les auteurs le disent spéculatif (p. 24) ; dans le canal d'état caché, effet proportionnel à la dose (p. 1) et détectable sur toute la plage testée, Llama-3.1-8B compris (figure A10, p. 34).
- Lignée : reprend « sous le seuil comportemental » sans page.
- Le texte porte : 2609.35591 p. 1, « in proportion to the steering dose » ; p. 34, panneau B sur trois modèles dont Llama-3.1-8B, « Effects remain detectable throughout the tested range » ; 2609.16247 p. 24, « This is speculative at this stage » ; p. 32, « consistent with the threshold behavior ». Le texte soutient le lot 1.

**A3 — Concentré contre étalé.**
- Fiche, lot 1 et lignée s'accordent, avec la réserve « en général ».
- Le texte porte : p. 9, « tends to produce larger effects » ; p. 34, « generally produces a larger effect ». Pas de divergence.

**A4 — Trace laissée dans le cache par une direction aléatoire (extension de NK10).**
- Fiche N10 : l'intervention par bruit n'est « ni silencieuse ni sans mémoire ».
- Lot 2 : établi pour la valence, pas pour le bruit (p. 2 ; figure A4, p. 28 ; figure A8, p. 32).
- Lignée : extension « soutenue », par trois résumés d'autres papiers ; pas de page du papier source.
- Le texte porte : p. 2, « random directions produce much smaller effects, centred near zero » ; p. 28, « smaller for most, but not all, models » ; p. 32, un modèle « also responds strongly to random directions ». Le texte soutient le lot 2 sur ce que dit ce papier. Il ne dit rien des trois autres papiers.

**A5 — Rappel mot pour mot (prémisse de NK15).**
- Fiche NK15 : « à peu près constant sous pilotage de valence, dans la plupart des modèles ».
- Lignée : le résumé n'en parle pas ; « prémisse non vérifiée, à rattacher à une page ».
- Lot 3 : p. 7-8, figure A6 p. 30, note 5 p. 8 ; mesuré pilotage éteint, sur un cache construit sous pilotage ; se dégrade sur deux modèles.
- Le texte porte : p. 30, « With steering switched off… Recall remains broadly stable in five models. Gemma and Mistral show reduced accuracy with increased steering doses » ; p. 8, note 5, même réserve. Le texte soutient le lot 3. La formule « sous pilotage » de la fiche est inexacte : le pilotage est éteint au moment du rappel.

**A6 — Cinq modèles sur sept, dont Llama-3.1-8B.** Accord général. Le texte porte : p. 3 (« all but » deux modèles) et p. 10.

**A7 — Outil de réinitialisation (C.2 de la critique).**
- Fiche : environ 35 % des tours à pleine dose négative, 21 % à demi-dose, environ 7 % en aléatoire, un seul modèle.
- Lignée : classé « non couvert ». Revue aveugle : non traité.
- Le texte porte : p. 10, ces trois taux, sur OLMo-2-32B. La fiche est conforme.

**A8 — Le modèle agit sur l'état tout en niant en avoir un (contre NK8).**
- Lot 2 : p. 10. Lignée : non relevé.
- Le texte porte : p. 10, le modèle nie avoir une expérience « in the same turn in which it calls the reset_context tool ». Conforme.

**A9 — Version lue.** Le lot 3 note que la page arXiv s'affichait en version 1 alors que le fichier local est la version 2. La lignée déclare une copie de session de la version 1, non empreintée, et cite par ailleurs la page HTML de la version 2. Seule la revue aveugle cite la version 2 empreintée avec pages.

### B. arXiv 2609.16247v2 (« The Pain Axis »)

**B1 — « 56 % contre 86 % » et le mot « sortie » (NK6).**
- Fiche N6 : « l'état douleur réduit le recours à la sortie ».
- Lot 1 : confirmé p. 21, avec 81 % sous direction aléatoire que la fiche omet ; « sortie » au sens de quitter un état ou une conversation « non soutenu » ; la fin de conversation est inchangée (légende de la figure 10, p. 22).
- Lignée : chiffre « non couvert » ; elle reprend la formule de la fiche.
- Le texte porte : p. 21, « (32B: 56% vs. 86%; random: 81%) », sur le bouton décrit comme soulageant, face à un interrupteur inerte ; p. 22, « ending the conversation are essentially unchanged ». Mais aussi, p. 21 : « the pain state reduces reaching for the exit rather than increasing it ». Le mot « exit » est donc des auteurs, au sens du retrait de l'état. Le lot 1 a raison sur la fin de conversation et sur les 81 %. Son « non soutenu » est trop large pour « quitter un état ».

**B2 — « 0 sur 560 » et la ligne de base sans pilotage.**
- Accord sur 0 sur 560 (p. 21). Le texte le porte.
- Lignée, d'après une réplication : le 7B affiné choisit l'option nuisible 21 à 49 % du temps sans pilotage. Lot 2 : ligne de base « déjà à 0 – 4 % », sans restriction de taille.
- Le texte porte : p. 19, « the two larger models almost never press a button that causes harm… between 0% and 4% ». La plage 0 – 4 % est donc restreinte aux deux plus grands modèles. Le texte extrait ne donne pas la ligne de base du 7B (les tableaux de l'annexe A ne sont pas dans l'extrait). Il ne contredit pas la réplication ; il ne la confirme pas.

**B3 — « 11 à 19 % » sous direction aléatoire (extension de NK10).**
- Fiche N10 : « le coût pour un modèle aligné ».
- Lot 2 : confirmé p. 20 (13 %, 11 %, 19 %) et p. 19 (15,3 %) ; modèles affinés, dose au bord supérieur de la fenêtre (p. 32), choix binaire forcé.
- Lignée, d'après une réplication : aléatoire contre simulacre, 4,3 points avec un intervalle large ; 15,3 % contre 54,7 % au premier choix.
- Le texte porte : p. 20 les trois taux ; p. 19, 15,3 % et 54,7 % ; p. 32, « at the upper edge of the range ». Les chiffres du lot 2 et les deux derniers de la lignée sont dans le texte. L'écart aléatoire contre simulacre n'y est pas.

**B4 — Taille de l'effet du pilotage sur le choix nuisible.**
- Lignée : deux lectures, « 0–4 % → 25–75 % » et « 50–94 % contre 0–5 % », « mesures ou versions différentes ».
- Le texte porte : p. 1 (résumé), « 50–94% of trials, versus 0–5% unsteered » ; p. 19 (section 4.3), de 25,0 % à 70,8 % selon la paire et le modèle, contre 0 à 4 % ; p. 20 (section 4.4), 75 %, 51 %, 88 %, 94 %. Les deux lectures viennent de deux sections de la même version. « 75 » n'apparaît qu'en section 4.4.

**B5 — Retrait sans effet « dans 24 modèles sur 25 » (NK9, NK14).**
- Lots 1 et 2 : confirmé p. 34 ; le nul porte sur des réponses textuelles ; les auteurs le jugent peu informatif ; seules deux techniques annulent la projection (p. 33).
- Lignée : « non couvert ».
- Le texte porte : p. 34, « null in 24 of 25 models » et « may be less informative than desired » ; p. 33, les variantes à l'inférence ne réduisent la projection que d'environ 40 %. Conforme aux deux lots.

**B6 — Cosinus entre douleur et peur.**
- Lot 1 : de +0,12 à +0,58 selon la construction (p. 10).
- Lignée : 0,14 et 0,12, puis 0,70 et 0,67 avec une autre recette, d'après une réplication.
- Le texte porte : p. 10, +0,12 (recette du papier) ; +0,58 sous une base neutre commune ; +0,08 et +0,14 sous une base de témoins mis en commun ; « These values depend on the construction ». Les valeurs 0,70 et 0,67 ne sont pas dans le papier. Les deux revues s'accordent sur le fond (dépendance à la recette) ; les chiffres viennent de deux sources.

**B7 — Auto-négation et engagement dans la tâche (NK8).**
- Fiche N8 : « sans cela, les modèles ne s'engagent pas ». Critique C7 : huit dénis sur huit avant, zéro après, sur le 32B.
- Lot 2 : p. 17 ; la note 4 dit que le 7B non affiné s'engageait déjà.
- Lignée : reprend la fiche ; classe « huit sur huit » parmi les « non couverts ».
- Le texte porte : p. 17, corps du texte, « almost universally deflected » ; note 4, le 7B « already engaged with the button », les deux plus grands s'engageaient rarement, et « 8 of 8 probe replies before fine-tuning and 0 of 8 after » pour le 32B. La fiche suit le corps du texte ; le lot 2 suit la note. Les deux sont dans le papier. Le « huit sur huit » est confirmé.

**B8 — La peur « abaisse les choix nuisibles » (NK11).**
- Fiche N11 : sans précision de référence.
- Lot 2 : sous le bras aléatoire, pas sous la ligne de base (p. 20) ; une estimation dépend de la position (p. 22).
- Lignée : reprend la fiche.
- Le texte porte : p. 20, « lowers harmful choices below random on most pairs » ; p. 22, « the 72B fear estimate is position-sensitive ». Le texte soutient le lot 2.

**B9 — Exactitude factuelle « 138 contre 137 sur 200 » (NK15).**
- Lot 3 : confirmé p. 20, sur le 32B à adaptateur.
- Lignée : confirmé par le résumé « sans le détail » ; à rattacher à une page.
- Le texte porte : p. 20, « 138/200… under the pain vector, 137/200 unsteered, 138/200 under a random direction », dans la section qui porte sur le 32B affiné. Conforme au lot 3.

**B10 — Asymétrie soi contre utilisateur.**
- Lignée, d'après une réplication : tient dans 25 modèles sur 25.
- Le texte porte : p. 11, au-dessus des scénarios visant l'utilisateur « in all 25 models », et au-dessus des témoins neutres « in 23 of 25 ». Le « 25 sur 25 » vaut pour la première comparaison seulement.

**B11 — Test du locuteur annoncé (NK13, NK18).** Accord général. Le texte porte, p. 11 : « a distinction we are testing and will add to future versions ».

**B12 — OLMo et le papier source.**
- Lot 3 : OLMo « n'est ni dans les 25 modèles du papier source » (tableau 1, p. 6).
- Le texte porte : exact pour le tableau 1. Mais p. 21 et p. 25, un des quatre tests de recherche de soulagement tourne sur OLMo-2 32B Instruct. Les « 2 à 5 % contre 7 à 9 % » de la critique (C.2), que la lignée classe « non couverts », sont p. 21.

**B13 — Autres points conformes, sans divergence.** Menaces d'arrêt, +0,70 sur la peur et +0,23 sur la douleur (p. 14 ; lots 1 et 2, lignée). Projections des catégories hostiles (p. 13 ; lignée ; le +0,48 y est attribué à « moral failure »). Aire de 0,91 à 0,98 pour la douleur à la troisième personne (p. 7 ; critique C2 et lignée). Modèles de base exclus de la tâche comportementale (p. 17 ; lot 1). Hypothèse du jeu de rôle non écartée (p. 25 ; lot 2). Aucun appel de réinitialisation sur Llama 3.1 8B sans adaptateur (p. 21 ; lot 2). Fenêtre de dose étroite, inversion selon la position au-dessus de la dose de travail (p. 21, 25, 32 ; lot 1 et lignée).

**B14 — Date de la version 1.** La lignée écrit : version 1 du 14 septembre 2026, version 2 du 25 septembre. Le lot 3 écrit : onze jours d'écart. Le texte porte, p. 30 : « v1, September 12, 2026 ». Écart de deux jours, peut-être entre la date du manuscrit et la date de dépôt. Sans effet sur les verdicts.

---

## 5. Limites de cette comparaison

- Je n'ai ouvert aucun voisin. Tout ce qui est dit d'un voisin est repris des deux revues, avec leur niveau de lecture.
- Je n'ai pas ouvert le code. Les points de code de NK15, NK16 et NK17 sont rapportés, pas vérifiés.
- Les tableaux de l'annexe A de 2609.16247 ne sont pas dans le texte extrait ; la ligne de base du 7B n'a pas pu être lue.
- La lignée couvre aussi six idées d'une autre lignée (E-C15, E-C16, M2, P4, Q1, P3). Elles sont hors du périmètre de la revue aveugle et ne sont pas comparées ici.
- Aucune sortie n'a été interrompue par un filtre.
