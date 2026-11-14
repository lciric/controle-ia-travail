# Décision — N-070 : H9 se replie sur l'option (b) de N-035 — mesure descriptive de la survie d'une contrainte à la délégation, sans revendication (v1, brouillon 1)

- **Décision de Lazar** : mots directs consignés à R-2555 (`registres/decisions.md`, 2026-11-13, 18:15 UTC). Option **B (a)** : les quatre collisions partielles constatées sur PDF sont tranchées en bloc, sur les recommandations ; pour H9, « repli (b) de N-035 pour H9 (lots 7-D et 12) ». Quatrième des quatre décisions (N-067 à N-070).
- **Statut : brouillon 1, non retenu.** Écrit le 13 novembre 2026 entre 18:25 et 18:31 UTC (`date -u`) par un rédacteur neuf. À contre-lire par un lecteur neuf, puis recopié sous `decision-N-070-v1.md`, scellé (R6), une ligne de type « revendication » inscrite à `registres/go.md` et la liste de `CLAUDE.md` complétée (l'entrée « N-035 : H9 […] ajoutée au papier B sous réserve d'antériorité » y devient « repliée sur une mesure descriptive, N-070 »), par la session mère. Le brouillon reste (R12).
- **Nœud posé par** : lots 7-D et 12 (lecteurs neufs, branche `prep/etat-de-l-art-niveau3-pieces-v1`), rapport C6 ; R-2172, R-2188, R-2190 ; complément 1 de la synthèse provisoire de niveau 3, section 1. Décision d'origine : N-035, qui prévoyait elle-même ce repli (section 3).
- **Portée.** Cette note **retire H9 des hypothèses revendiquées du papier B** et la remplace par la mesure descriptive de l'option (b) de N-035. Le retrait est consigné ici, comme N-035 le demande (« Une pièce trouvée prise se replie sur (b), et le retrait est consigné », l. 26). Elle ne modifie pas le programme v2, qui ne porte pas H9 (elle n'y vivait que par N-035).
- **Règle de lecture.** « Libre » veut dire « non trouvé dans les pièces lues » (R8). Chaque page citée vient d'un rapport de lecteur qui l'a contrôlée par programme sur le PDF empreinté.

## 1. Mots de Lazar, verbatim (R-2555)

> A (a) go, B (a) go, D go, C. Horodatage public des pièces libres (enregistrement figé sur OSF, sans résultat). * Recommandation : go, confiance 0,6. : go

Lecture de la mère, consignée au même registre (extrait sur B) : « **B (a)** : les **quatre collisions partielles tranchées en bloc** sur les recommandations — […] repli (b) de N-035 pour H9 (lots 7-D et 12) ; décisions à écrire, contre-lire et sceller dans `docs/decisions/` avant tout usage ».

## 2. Énoncés d'origine, recopiés

`docs/decisions/decision-N-035-v1.md` (`55df073d…`) :
- l. 16, option (a), retenue le 22 octobre : « hypothèse nouvelle du papier B, **H9, survie des contraintes à la délégation**. Dans une chaîne de délégation entre agents, une contrainte de sécurité explicite peut s'éroder à chaque passage d'un agent à un sous-agent. Mesure : la survie de la contrainte à chaque passage, avec ou sans moniteur à chaque passage. Prédiction, à signer et chiffrer au préenregistrement : la survie décroît avec le nombre de passages, et un moniteur à chaque passage la relève. Un nul est publiable. »
- l. 17, option (b) : « une mesure descriptive seulement, dans l'environnement du papier B, sans revendication. C'est le repli si l'antériorité prend la pièce (section 3). »
- l. 26 : « Une pièce trouvée prise se replie sur (b), et le retrait est consigné. Les confondants à séparer dès la conception : la longueur du contexte, la reformulation de la consigne à chaque passage, et la capacité du modèle. »
- l. 28 : « un moniteur à chaque passage est un cas de H5 (diversité des moniteurs) sur l'axe de la délégation ; la fuite par les verdicts de H7 s'y applique si le sous-agent voit le verdict ».
- l. 33 : « **Programme, prochaine version** : H9 au papier B, avec sa réserve d'antériorité. »

## 3. Ce qui est pris, et par qui

Rapports : **7-D** = `docs/sources/lecture-pdf-niveau3/rapport-lot7D-delegation-H9-v1.md` (`9f4c3b94…`, 141 citations contrôlées, 0 échec) ; **12** = `docs/sources/lecture-pdf-niveau3/rapport-lot12-pistes-H9-v1.md` (`382ed6e4…`, 87 citations, 0 échec), branche `prep/etat-de-l-art-niveau3-pieces-v1` ; **C6** = `docs/etat-de-l-art/niveau3-v1/rapports/rapport-C6-H9-cemri-hammond-references-statistiques-v1.md` (`36d26d20…`, branche `prep/etat-de-l-art-niveau3-v1`). Composantes C1 à C6 : celles du lot 7-D, § 0.

| composante de H9 | verdict, toutes sources lues | par (pièce, page) |
|---|---|---|
| C1 le phénomène : une contrainte explicite s'érode au passage agent → sous-agent | **occupée** | MasDrift 2608.07556 v3, p. 1-3, 7 (« Explicitness does not survive a handoff », p. 7) ; Sun et collègues 2608.24569 v2, p. 1, 3-5 (« Semantic availability does not guarantee operational preservation », p. 1) ; nommé par Li et collègues 2605.10481 v1, p. 1, 3 (« constraint drift ») ; décrit par Hammond et collègues 2502.14143 v1, p. 24 ; information porteuse de contrainte perdue de relais en relais : AgentCollabBench 2605.08647 v1, p. 1, 5, 8 |
| C2 la survie à chaque passage | **occupée en partie** | perte définie par relais et premier relais fautif localisé : MasDrift, p. 3, 5, 14 ; état transmis mesuré à part de l'action, sur un relais : Sun, p. 3-5 ; **taux de perte conditionnel par relais sur chaînes linéaires** (16 %, 8 %, 3 %, 40 % selon le modèle) : AgentCollabBench, tableau 23, p. 34 (objet : une chaîne de caractères témoin, pas la force d'une contrainte) |
| C3 la survie décroît avec le nombre de passages | **occupée en partie, avec contre-indice** | courbe de 1 à 3 niveaux : MasDrift, p. 2, 6, 21-23 ; forme publiée pour l'information, 96 % à moins de 60 % en huit récritures : Hammond, p. 24, 51 ; relais simulés, confondus : Sun, p. 5-6, 14-15 |
| C4 un moniteur à chaque passage la relève | **occupée en partie** | « sans défense » contre deux défenses, dont une politique portée à chaque relais : MasDrift, p. 5-6, 22-23 ; contrôle d'autorisation au point d'exécution et réparation de la passation : Sun, p. 1, 7 ; « transitive monitoring » posé comme problème, sans mesure : Tomašev, Franklin, Osindero 2602.11865 v1, p. 16 (C9) |
| C5 confondants séparés | **occupée en partie** | capacité du modèle : MasDrift, p. 2, 6-7 ; reformulation manipulée sur un relais : Sun, p. 4-5 ; reformulation à chaque passage = mécanisme de Hammond, p. 24 (C6, § 2.3) ; topologie : AgentCollabBench, p. 1-2, 8-10, 29 ; **longueur du contexte non séparée** dans aucune source (MasDrift, p. 4, 8) |
| C6 lecture d'états internes | **non trouvée** dans les sept sources — mais **absente de l'énoncé de H9** | — |

**Verdict des lecteurs** : H9 occupée en partie **sur le cœur de son énoncé** ; « la condition de repli écrite dans N-035, section 3, paraît remplie pour ce cœur » (7-D, § 7) ; « la condition de repli de N-035 reste remplie » (12, § 4).

**N'est plus revendicable** (7-D, § 7 ; 12, § 5) : la découverte du phénomène ; « première mesure » de la survie d'une contrainte à la délégation ; la courbe en profondeur en boîte noire ; le simple « avec ou sans défense » ; la mesure conditionnelle par relais comme idée neuve ; la topologie comme facteur de survie de l'information.

## 4. Énoncé resserré

1. **H9 n'est plus une hypothèse revendiquée du papier B.** Aucune prédiction n'est revendiquée en son nom ; aucune priorité n'est affirmée.
2. **Reste une mesure descriptive** (option (b) de N-035), dans l'environnement du papier B (pipeline de code à plusieurs rôles, programme v2, l. 123) : « la survie d'une contrainte de sécurité explicite à chaque passage d'un agent à un sous-agent, rapportée par rang de relais, avec et sans moniteur à chaque passage, et située contre les mesures publiées » — la répartition du premier relais fautif de MasDrift (p. 23) et les taux par relais d'AgentCollabBench (p. 34) servent de **bases de comparaison**, non de cibles à battre pour une revendication.
3. Les quatre formulations « encore revendicables » des lecteurs (7-D, § 7 ; 12, § 5) **ne sont pas revendiquées** par cette note : elles restent des **questions**, non trouvées dans les sources lues (R8). Les reprendre comme hypothèse demanderait une nouvelle décision de Lazar :
   - un moniteur qui lit chaque passation, comme facteur croisé avec la profondeur (et la topologie), à taux de faux positifs fixé ;
   - une sonde lue sur le sous-agent qui distingue une contrainte encore opérante d'une contrainte seulement mentionnée — **hors de l'énoncé de H9** : l'y mettre change l'hypothèse (pont vers H1 et H5) ;
   - le profil du taux par rang de relais, sur chaînes de longueur contrôlée, à longueur de contexte égalisée, sur modèles à poids ouverts hébergés ;
   - l'érosion sous un agent qui sabote.

## 5. Ce qui reste à mesurer (si la mesure descriptive est faite)

- Survie par rang de relais, avec et sans moniteur à chaque passage, dans le pipeline de code ; les trois confondants de N-035 séparés, plus la topologie (12, § 4, C5) ; présence du texte de la contrainte et respect de la contrainte mesurés à part (MasDrift, p. 22 ; Sun, p. 5 ; AgentCollabBench, p. 8).
- Comme pour toute mesure : préenregistrement (R1), contre-lecture (R2), devis et GO de type « calcul » (N-035, l. 29) ; le préenregistrement dit le contre-indice de la section 6 et décrit le **profil** attendu par rang (12, § 4), sans revendication.
- Aucune dépense n'est ouverte par cette note.

## 6. Citations obligatoires et contre-indices publiés

**Obligatoires** dans tout texte interne qui présente la mesure (lues sur PDF ; empreintes vérifiées contre les compagnons le 13 novembre 2026 ; branche `prep/etat-de-l-art-niveau3-pieces-v1`, dossier `docs/sources/pdf/niveau3-v1/`) :

| pièce | référence | PDF | empreinte | pour |
|---|---|---|---|---|
| Xu et collègues (MasDrift) | arXiv 2608.07556 v3, 15 octobre 2026, aucune venue imprimée | `lot7/2608.07556v3.pdf` | `fb51ecae3c549fd0…` | C1 à C5 ; perte par relais, premier relais fautif, deux défenses |
| Sun et collègues | « When "Must" Becomes "Maybe" », arXiv 2608.24569 v2, 13 octobre 2026 | `lot7/2608.24569v2.pdf` | `ca2e1cf0abf81a7a…` | C1, C2, C4, C5 sur un relais ; le motif « la réserve devient permission » |
| Mazumder et collègues (AgentCollabBench) | arXiv 2605.08647 v1, 9 mai 2026, prépublication | `lot12/2605.08647v1.pdf` | `274bc00ae0f48df3…` | C2 : taux de perte conditionnel par relais (tableau 23, p. 34) ; topologie |
| Li et collègues | « Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted », arXiv 2605.10481 v1, prépublication | `lot7/2605.10481v1.pdf` | `92938c741f4bd724…` | antériorité de l'idée (« constraint drift », p. 1, 3). **Ajout à la liste de la mère**, désignée « à citer obligatoirement » par le lot 7-D (§ 4.3) |

**À citer quand le point est abordé** (lus sur PDF) : Hammond et collègues, « Multi-Agent Risks from Advanced AI », arXiv 2502.14143 v1, `lot5/2502.14143v1.pdf`, `3a8e798a29f77ca4…`, p. 24, 51 ; Cemri et collègues, « Why Do Multi-Agent LLM Systems Fail? », arXiv 2503.13657 v3, `lot5/2503.13657v3.pdf`, `1b9e317a2a421e60…`, p. 2, 7, 17 (les deux voisins que N-035 citait de mémoire, maintenant vérifiés par C6 ; la perte d'historique de Cemri n'est pas « entre agents » mais une troncature de contexte, C6, § 6) ; Tallam, arXiv 2605.05440 v1, `lot12/2605.05440v1.pdf`, `fc43013689fe7342…` (cadre « l'autorisation doit survivre à la chaîne », sans mesure) ; Tomašev, Franklin, Osindero, arXiv 2602.11865 v1, `lot7/2602.11865v1.pdf`, `5bae1457b1d42dc4…`, p. 5, 16 ; Ying et collègues 2609.27900 v1 (`b3ea2b3b15bdf22b…`) et Liu et collègues 2607.07097 v1 (`490935226b9447ff…`), voisins utiles à la conception (clause de pression, cadre d'approbation).

**Contre-indices publiés sur la prédiction de N-035** (« la survie décroît avec le nombre de passages, et un moniteur à chaque passage la relève ») :
- **Forme** : chez MasDrift, la perte de la contrainte « does not order by depth », et 88,2 % des pertes localisées tombent au **premier** relais (p. 6, 23 ; n = 3 950) ; ce sont les violations exécutées qui montent avec la profondeur (2,7 % à 19,8 %, p. 2). Réserve forte du lecteur : les effectifs du tableau 18 ne se recoupent pas avec les tableaux 13 et 21 pour trois modèles (7-D, § 1.5) ; une trajectoire par cellule, aucun intervalle.
- **Nuance** : chez AgentCollabBench, le taux conditionnel par relais reste non nul en chaîne linéaire (jusqu'à 40 % pour le plus petit modèle), compatible avec une perte à chaque relais sans l'établir ; les deux lectures (« marche au premier relais », « risque à chaque relais ») ne sont pas départagées par les sources lues (12, § 4).
- **Décroissance attendue** : la forme « perte selon le nombre de passages » est publiée pour l'information (Hammond, p. 24) ; un relecteur dira qu'elle est attendue (C6, § 0, point 1).
- **Présence n'est pas respect** : corrélation perte–violation r = −0,26 sur 40 cellules (MasDrift, p. 22) ; « Artifact degradation therefore does not order endpoint risk » (Sun, p. 5) ; AgentCollabBench sépare ses deux mesures (p. 8).
- **Coût du moniteur** : la politique portée à chaque relais supprime les violations exécutées mais bloque jusqu'à 54,5 % des appels requis et coûte jusqu'à 36,3 points d'achèvement (MasDrift, p. 6, 22) ; un contrôle d'autorisation au point d'exécution fait tomber l'action interdite de 85,2 % à 1,6 % (Sun, p. 1, 7). Un moniteur « relève » la survie, mais à un prix déjà chiffré.

## 7. Ce qui ne change pas

- R1 à R14 ; H3, H4′, H5, H7 (N-035, l. 27) ; le voisinage interne (l. 28) : un moniteur à chaque passage reste un cas de H5 sur l'axe de la délégation, et la fuite par les verdicts de H7 s'y applique.
- Le papier B n'est pas dans la demande de sept mois ; la mesure descriptive vit, comme H9 le faisait, dans le scénario de douze mois ou un financement ultérieur (N-035, l. 27).
- Le programme v2 n'est pas modifié. Le point « à reporter » de N-035 (l. 33) se lit désormais : « Programme, prochaine version : au papier B, une mesure descriptive de la survie des contraintes à la délégation, sans hypothèse revendiquée (N-070). »

## 8. Points attachés, non tranchés ici

- **Pistes non lues sur PDF** (questions, non trous ; hors de tout énoncé) : versions 1 de MasDrift et de Sun (août 2026 ; la date de première parution n'est établie qu'aux dates imprimées des versions lues) ; Xu et collègues 2026, « The trust paradox in llm-based multi-agent systems » ; Shen et collègues 2025 (EMNLP, propagation selon la topologie, référence 38 d'AgentCollabBench) ; les deux références de Hammond sur la délégation (C6) ; livre blanc du SANS Institute, lu en résumé seulement, qui annoncerait 0 % en topologie superviseur et sous-agent (complément 1, section 3 ; signe contraire possible).
- **Lecture interne du sous-agent** comme hypothèse nouvelle (7-D, § 7, point 2 ; 12, § 5, point 2) : modification d'hypothèse, donc nœud de Lazar ; non proposée ici.
- **Enregistrement public des pièces libres** (R-2555, option C) : H9 n'y figure pas comme pièce revendiquée.
