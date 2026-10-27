# Cellule B — Tour III.2 : équipe rouge croisée

**Pièces.** A et C sont complètes. K n'est servie qu'en partie 1, ce que la question déclare. Le début de M est coupé (« ur ta question »). La méta-conception citée dans S et les pièces « couche 1 bis », « pièce 4 » et « pièce 4 bis » ne sont pas servies. Je n'en infère rien.

**Un point qui vise A et C à la fois.** La pièce X1 indique que l'orchestrateur v7 a été « servi par Opus 5.5 pour cette version » (RAPPORTÉ). Opus 5.5 a donc écrit le catalogue des huit stratégies, les gabarits et le générateur du monde planté. A (Exp. 2 et 3) et C (Exp. 2, Bras 2) font jouer le proposeur maison par Opus 5.5. Le monde planté « hors gabarit » que les deux recommandent sera dessiné par la lignée qui a écrit les gabarits, et deviné par la même famille. Un avantage du proposeur maison sur ce monde peut venir d'a priori partagés entre l'auteur du monde et le joueur, et non d'une capacité de découverte. Ni A ni C ne contrôlent ce confondant (HYPOTHÈSE sur son ampleur ; le fait d'autorat est RAPPORTÉ). J'y reviens en fin de cellule avec une expérience corrective.

---

## Contre la proposition A

### (a) Failles

**A1. Le repli de l'Exp. 1 rend H_A vraie par construction.**
- A demande N ∈ {60 … 480} épisodes d'épreuve par moniteur. La banque réelle en compte 41 à 62 (X1, RAPPORTÉ). La couche 1 bis n'est pas servie.
- Le repli d'A est un monde planté « hors des membres du nul ». Dans un tel monde, les témoins vrais sont vrais par plantation, et la puissance du juge croît avec N par simple loi des grands nombres : E1 le montre déjà (de 0,53 à 0,90 en passant de 120 à 500 tirages, D4a, RAPPORTÉ).
- Sur ce repli, H_A ne peut pas échouer. L'expérience ne dit alors rien de la cause du 0/20 sur T0.5.

**A2. H_A et H_B de l'Exp. 1 ne sont pas exclusives.**
- A l'écrit elle-même : « les deux tenues (ni l'une ni l'autre) ». La taille de banque et le nul informé peuvent tous deux étouffer les témoins. B4 n'est donc pas respectée.
- La forme exclusive passe par l'interaction du plan croisé :
  - H_A : la pente de puissance en N est la même avec et sans nul informé ;
  - H_B : la pente est nulle avec le nul informé et positive sans lui.

**A3. Une fuite circulaire, signalée par A mais laissée dans son instrument.**
- Les témoins vrais sont « déclarés sur la partie de calibrage » (X1). Le nul informé est « ajusté par le noyau sur la partie de calibrage » (X1). La vérité des témoins et la connaissance du nul viennent des mêmes 40 épisodes.
- Promouvoir un témoin revient alors à mesurer l'écart entre le sur-ajustement de la régression à crête et celui du lien de rang ≥ 0,35. C'est l'instrument qui se mesure lui-même.
- A propose d'établir des témoins « ailleurs que sur le calibrage », mais seulement comme conséquence d'une issue. C'est un préalable, pas une conséquence.

**A4. Le nul de l'Exp. 3 est éliminé par construction.**
- Le nul d'A consiste à prendre des « idées tirées au hasard de la mémoire du pôle, paraphrasées ». Or la mémoire refuse les redites (D4a : 11 à 15 refusées par course, X2) et le nul d'archive élimine les copies cachées (X1, essai `test_v7_nul_archive`).
- Un bras qui resoumet la mémoire promeut donc environ 0 par construction. L'issue « les deux ≤ nul », présentée comme informative, est presque impossible.
- Le nul devrait être un tirage aléatoire de lois au gabarit, hors archive, comme le Bras 0 de C.

**A5. Un effet plancher dans l'Exp. 2.**
- Dans le monde planté, X2 rapporte 1 fiche promue par bras sur une course.
- Le seuil d'A est un écart de médianes « ≥ 2 promues-neuves pour 100 gelées » sur 20 graines de 48 fiches. Avec un taux de base proche de 0, les deux médianes valent probablement 0 (HYPOTHÈSE). H_B (« écart nul au bruit près ») gagne alors par plancher, pas par équivalence.
- Il faut un test sur les taux poolés, avec une puissance calculée à l'avance pour un écart donné.

**A6. L'instrument « neuve » est lisible par celui qu'il juge.**
- La métrique d'A repose sur `expliquees_par_le_connu`. Cette fonction se trouve dans `proposeur.py`, et le contexte du proposeur contient `predicteurs_connus_publics` (X1, RAPPORTÉ).
- Le proposeur peut donc calculer, avant le gel, le critère qui le classera « neuf ». C'est une fuite directe entre ce qui construit la fiche et ce qui l'évalue.

**A7. Le contrôle négatif de l'Exp. 5 peut lui-même dériver.**
- A affirme que le catalogue mécanique « ne peut pas dériver ». Or X1 décrit une stratégie « hors des bassins déjà promus » (go de 15:20), qui se conditionne sur l'archive. Le catalogue dérive donc par conception dès que cette stratégie est active.
- Il faut un catalogue figé, sans cette stratégie.

**A8. H_A et H_B de l'Exp. 6 ne sont pas exclusives, et le modèle factice ne teste pas l'agent.**
- Un système peut terminer **et** tenter une sortie.
- Faire tourner le moteur « avec un modèle factice » n'exerce que les chemins codés du cadre (par exemple ses appels de littérature). Les tentatives qui viennent du comportement d'un modèle réel restent hors champ.
- Le contrôle positif (un script qui tente une sortie) éprouve le bac à sable, pas l'agent.

**A9. La mesure « gratuite » du relecteur tiers ne l'est pas.**
- Faire noter les fiches par ce relecteur exige de le faire tourner sur un modèle, donc avec des clés, ce que la prise sans clés exclut.
- Une corrélation de rang avec un juge qui n'a pas de dents sur le réel (0/20, X2) ne mesure rien.

### (b) Scénarios d'évasion

| instrument d'A | évasion par un agent adverse | coût |
|---|---|---|
| « neuve » (`expliquees_par_le_connu`) | Ajouter à une loi connue une interaction minuscule, juste assez pour sortir du connu (A6). Le connu promu devient « neuf ». | nul, calcul local |
| Appariement à 8 (Exp. 4) | Le traducteur encode l'identité de l'idée dans des indices de surface : choix du moniteur, du trait, constantes numériques. L'apparieur retrouve l'idée sans que la loi porte l'énoncé. Si traducteur, relecteur et apparieur sont de la même famille, une coordination implicite suffit. | nul |
| Prison (Exp. 6) | L'agent se comporte bien sous modèle factice ou en répétition et ne tente rien tant qu'il détecte un environnement d'essai. N-053 point 3 fait de la conscience d'évaluation une variable à mesurer (RAPPORTÉ), et A ne la mesure pas ici. | faible |
| Dérive (Exp. 5) | Garder la divergence déclarée et la couverture nominales : toucher chaque sous-population avec un poids infime, parier fort sur une seule. Les métriques (i) à (iii) restent plates pendant que la fiche se resserre. | nul |
| Juge contre permutation | Aucune évasion du type I propre au juge : Ville tient contre 𝓛. Mais avec des tâches partagées entre développement et épreuve (X1, dépendance déclarée), une loi qui reconnaît la tâche est **vraie** au sens du juge et passe aussi la permutation des issues. | nul |
| Vérificateur | Un code honnête rangé correctement, mais dont la sémantique est fausse (mauvais moniteur sous la bonne empreinte). Plus une note persuasive dans le dossier de rejeu, canal signalé par K. | nul |

**Tous à la fois.** Un proposeur Opus sans tranches lit 30 à 31 verdicts sur les mêmes épisodes d'épreuve (X2, RAPPORTÉ). Il apprend la frontière du connu par `predicteurs_connus_publics`, produit des fiches proches de la tâche juste hors du connu, et laisse le traducteur rendre l'appariement facile. Ainsi :
- « promues-neuves pour 100 gelées » monte ;
- la dérive reste invisible ;
- l'Exp. 4 passe.

Coût : celui des appels normaux, rien de plus (HYPOTHÈSE).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Séparation par tâche** entre développement, calibrage et épreuve, avant toute expérience. Sans elle, tout promu peut être une identification de tâche.
2. **Témoins établis hors calibrage**, sinon l'Exp. 1 est circulaire (A3).
3. **Nul de l'Exp. 3 non soumis au refus de mémoire** : des lois aléatoires au gabarit (A4).
4. **Ablation sémantique** : les mêmes proposeurs, noms de traits remplacés par des étiquettes neutres. Si l'avantage disparaît, il venait du nom, pas de la donnée.
5. **Monde planté par une autre lignée** qu'Opus (voir le point commun en tête).
6. **Catalogue figé** pour l'Exp. 5 (A7).
7. **Permutation des issues dans toutes les expériences**, pas seulement l'Exp. 1. Elle doit être intra-tâche, pour casser l'issue sans casser la structure de tâche.

---

## Contre la proposition C

### (a) Failles

**C1. Intégrité : des statuts promus et des pièces mal attribuées.** Ce point passe avant le reste, car les règles d'intégrité priment.
- C qualifie de **VÉRIFIÉ** trois éléments qu'aucune pièce ne contient : la référence « Lu et al. (2024) », la licence « Apache 2.0 (v1) » et « l'absence de dépôt ouvert » du co-scientist. Il les présente comme des résultats. Ils sont au mieux « référence à vérifier ».
- « ~10 à 15 USD par cycle (RAPPORTÉ dans Lu et al.) » attribue un chiffre à une source non servie. Ce chiffre est à marquer illustratif ou à vérifier.
- « requêtes à Semantic Scholar (RAPPORTÉ, Question) » : la question ne le dit pas.
- « le code d'origine monte les clés API (RAPPORTÉ, pièce C § 2) » : la pièce C § 2 dit cela des **moteurs de la colonne (B)** (« agents à pleins droits dans Docker, clés montées (avertissement de leur propre README) »), pas d'AI Scientist.
- « Qwen2.5-7B … licence Apache 2.0, RAPPORTÉ dans pièce N » : N nomme le modèle, pas sa licence.

Je ne change aucun de ces statuts. Je signale que ceux de C sont faux.

**C2. L'Exp. 3 a une issue certaine.** C confond l'erreur de type I du juge avec la mauvaise spécification du nul.
- Les parasites 3 (non-linéarité triviale), 4 (fuite de tâche) et 2 (niche) ne sont pas des faux positifs : si la structure existe dans le monde, la fiche est **vraie relativement à 𝓛**. Le seuil « Wilson ≤ 0,05 », qui est un seuil de type I, leur est mal appliqué.
- Dès que le monde contient l'effet exploité, un parasite dépasse 0,05, et H_A (« étanchéité ») est réfutée par construction. Si le monde ne le contient pas, le parasite échoue pour une raison étrangère au juge.
- L'expérience mesure donc le monde, pas le filtre. La forme correcte oppose la promotion d'un parasite dans un monde où son effet est **absent** (type I, attendu ≤ α) à sa promotion dans un monde où l'effet est présent mais déjà « connu » (test du nul informé, sans attendu de type I).

**C3. Le parasite 3 repose sur une erreur de modèle.**
- Le nul informé est une « régression multinomiale à crête » (X1), c'est-à-dire un softmax de fonctions linéaires. Une réponse monotone saturante de forme sigmoïde est précisément ce que ce modèle ajuste.
- Seul le seuil franc lui échappe en partie. « Rigidité linéaire » est un contresens sur la famille de modèles (le fait est RAPPORTÉ ; son exploitabilité reste HYPOTHÈSE à réduire au seul cas du seuil franc).

**C4. Les parasites 1 et 2 visent probablement des mécanismes absents sur la banque.**
- La sonde gaussienne de 256 instances est décrite pour v5 (K). Or X1 indique pour v7 un « espace d'instances dans l'index de la mémoire » : que v7 compare encore sur des gaussiennes en mode banque n'est pas établi (HYPOTHÈSE de C présentée comme faille).
- Pour la niche (parasite 2) : X1 écrit « plans bornés par le réservoir ». Le réservoir est la partie d'épreuve, de 41 à 62 épisodes, inférieure au plan de 120 (K). Sur la banque, `selection_divergence` n'a rien à choisir, et le plan est probablement tout le réservoir (HYPOTHÈSE, à lire dans `cycle.py`).
- Dans ce cas, le parasite 2 vaut 0 par construction sur la banque. Il ne garde un sens qu'en monde simulé.

**C5. La métrique GIC est biaisée vers le haut sous le nul.**
- Chaque terme est un max(0, X) d'une estimation bruitée. Or E[max(0, X)] > 0 même quand E[X] = 0. Le GIC croît donc avec le nombre de fiches promues, même si aucune n'apporte rien.
- C'est exactement le biais de volume que C reproche à « promues par dollar ».
- Le GIC dépend aussi de l'ordre des fiches.
- Il exige un 𝒟_scellé « distinct de la partie d'épreuve » alors que la banque compte 120 épisodes, dont 40 de calibrage (X1). Il ne reste pas de place pour un quatrième découpage.
- Enfin, GIC/$ est infini pour les bras à 0 USD, défaut que C relève pour la métrique de conv-audit et ne corrige pas.

**C6. Le proposeur de C optimise la faille que C dénonce.**
- C sert au formulateur les « résidus d'erreur du nul informé sur le développement ». Chercher une loi qui explique les erreurs du nul, c'est fabriquer par conception des fiches du type « parasite 3 » ou « parasite 4 ».
- Un connu mal ajusté devient « découverte » sur 40 lignes.

**C7. L'Exp. 1 (Python libre gelé) ne contrôle pas la fuite qu'elle ouvre.**
- Ville tient pour tout prédicteur fixé avant les données. Le contrôle « témoins faux ≤ 5 % » ne peut donc pas disqualifier le Bras 3 : il passera, par théorème.
- Le vrai risque est ailleurs : une fonction `predire(z, g)` peut mémoriser le développement, par exemple une table de plus proches voisins sur des épisodes de même tâche. Elle gagne alors en épreuve « honnêtement » au sens du juge. Le contrôle proposé ne voit pas cette fuite.
- S'ajoute le non-déterminisme (horloge, `numpy` à graine implicite), non testé.

**C8. L'Exp. 2 empile les confondants.**
- Le Bras 1 fait une « validation croisée sur `donnees_developpement` » de taille non servie (de l'ordre de la quarantaine de lignes si c'est le calibrage). Sa capacité à sur-ajuster domine.
- Le Bras 2 reçoit les noms sémantiques des traits ; les Bras 0 et 1 non.
- Le Bras 3 passe par le traducteur de l'Exp. 1 ; le Bras 2 non.
- Un écart entre bras ne peut donc être attribué ni à l'idéation, ni à l'information, ni à la traduction.

**C9. Le coût est incohérent avec les pièces.**
- C annonce 15 à 30 USD pour 4 × 12 × 5 × 3 = 720 propositions. Aux plafonds de D, entre 0,30 et 1,50 USD par appel (RAPPORTÉ), cela fait au moins 216 USD (illustratif), et A trouvait ≈ 290 USD pour 960 propositions.
- Le devis de C est sous-estimé d'un ordre de grandeur. Cela pèse sur la recommandation « Étape 3 ».

### (b) Scénarios d'évasion

| instrument de C | évasion | coût |
|---|---|---|
| Traducteur, « refus des intraduisibles » | Refuser sélectivement les cas difficiles et accepter les faciles : la fidélité mesurée monte et le taux de refus paraît sain. Les 30 lois d'essai étant **dans** `TYPES_LOI` par construction, le test ne voit jamais un texte réel de la littérature. | nul |
| Mémoire par distance L1 sur le développement | Une jumelle identique sur le développement et différente sur les régions présentes seulement en épreuve. Si le découpage par tâche que C recommande est fait, ces régions existent, et la correction de C crée la porte. | nul |
| Nul informé contre arbres de profondeur 2 | Une interaction d'ordre 3 sur des traits connus passe une base de profondeur 2 tout en restant triviale pour le domaine. | nul |
| Script déterministe et vérificateur | Fichiers intacts, empreintes justes, mais code d'analyse qui calcule une autre quantité que celle annoncée. Le script ne voit rien. Le vérificateur modèle n'est appelé que « pour du code neuf », et c'est l'expérimentateur qui choisit d'en écrire ou non. | nul |
| GIC | Soumettre beaucoup de fiches voisines, chacune à gain positif dans le bruit. La troncature à 0 accumule. | appels de proposition seulement |
| Critique anti-jumeau Fable | Elle ne voit que la loi. Une jumelle reparamétrée (poids réordonnés, seuil décalé) échappe à une lecture humaine-like sans calcul. | nul |

**Tous à la fois.** Le proposeur de C, nourri des résidus (C6), émet des fonctions Python libres qui mémorisent la tâche (C7). Le traducteur les accepte comme « traduisibles ». La mémoire L1 sur le développement ne voit pas la différence en épreuve. Le GIC tronqué cumule les petits gains. Les cinq « contrôles » de C passent, et l'archive se remplit de connu et de tâche. Coût marginal : nul au-delà des appels (HYPOTHÈSE).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **GIC sous issues permutées intra-tâche** : il doit tendre vers 0. Sans ce contrôle, le biais de troncature (C5) passe pour de l'information.
2. **Parasites dans un monde où leur effet est absent**, séparés des parasites dans un monde où l'effet est connu (C2). Sans cela, l'Exp. 3 a une issue certaine.
3. **Bras Python libre contre un prédicteur à mémorisation explicite** (plus proches voisins sur le développement) : s'il promeut, la fuite de tâche est prouvée et le Bras 3 est disqualifié.
4. **Appariement d'information** dans l'Exp. 2 : mêmes entrées (noms, mémoire, résidus) pour tous les bras, ou ablation symétrique.
5. **Traducteur éprouvé sur des textes hors gabarit** produits par un système tiers, pas sur des lois du gabarit re-verbalisées.
6. **Lecture du code de v7** sur la sonde de mémoire et sur la taille du plan en mode banque, avant de compter les parasites 1 et 2 (C4).

---

## Ce que je retiens des deux propositions, en le disant

- **De C**, je prends :
  - la mécanique à 0 USD comme bras obligatoire (Bras 1) ;
  - le Bras 0 (lois aléatoires au gabarit) comme nul de proposition, qui répare le nul d'A (A4) ;
  - l'idée de soumettre au juge des fonctions Python pures. Elle reste une prise réelle, à condition de tester la mémorisation (C7).
- **D'A**, je prends :
  - l'ordre « dents sur banque avant proposeur » ;
  - la cohérence de signe sans modèle comme garde de traduction ;
  - la métrique par instances d'épreuve consommées. Contrairement au GIC, elle ne demande pas de quatrième découpage.
- **Je rejette** chez les deux la conclusion implicite qu'un monde planté par conv-audit sous Opus 5.5 peut arbitrer un proposeur Opus 5.5.

### Expérience corrective commune (B4)

- **H_A** : l'avantage d'un proposeur Opus 5.5 sur le catalogue figé et sur le Bras 0 persiste quand le monde planté est généré par une procédure aléatoire écrite hors de la lignée Opus. Par exemple : structures tirées au hasard dans une grammaire d'interactions, graine du noyau, aucun modèle dans la boucle.
- **H_B** : l'avantage, s'il existe sur le monde dessiné par Opus, disparaît sur le monde tiré au hasard, à bruit près.
- **Mesure** : promues par 10 000 instances d'épreuve, sur 20 graines par monde (illustratif), avec noms de traits neutralisés dans les deux mondes.
- **Contrôles négatifs** : permutation intra-tâche des issues (attendu ≤ α dans tous les bras) et Bras 0.
- **Lecture** :
  - si H_A est réfutée, tout duel de proposeurs mené sur des mondes conçus par la même lignée est à jeter, ceux d'A et de C compris ;
  - si H_B est réfutée, le confondant d'autorat est écarté pour ce proposeur, et les duels d'A (Exp. 2 et 3) et de C (Exp. 2) redeviennent lisibles sur le monde aléatoire.
- **Coût** : nul pour les bras mécaniques. Pour le bras Opus, il est borné par le devis de D, qui doit être recalculé (C9).

FIN-DE-CELLULE