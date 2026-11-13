# Contre-lecture du rapport d'antériorité sur le lemme d'additivité « L » (lot 8) — v1

- Début du travail : 2026-11-13T22:11:12Z UTC ; fichier écrit le 2026-11-13T22:20:47Z UTC (les deux heures relevées par `date -u`, la seconde dans la commande qui écrit ce fichier).
- Contre-lecteur : sous-agent neuf, modèle B ; auteur du rapport : modèle A ; A ≠ B. Je n'ai écrit ni le programme, ni les décisions, ni le rapport contre-lu.
- Objet : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-L-lot8-v1.md`.
- Empreintes vérifiées (sha256, égalité constatée) :
  - rapport : `130283adeceff8ee8a3bae0487e5ac17a69b80c24884e3e5b4aec41c5d64e6ab` (égale à la valeur attendue et au compagnon `.sha256`) ;
  - archive du rapport `fichiers-de-travail-L-lot8-v1.tar` : `e643d527c4056def09ee227d89dd572a8c0b3cba429b8c6f9d6aa96e24b87c69` (égale à la valeur attendue) ; `citations-L-v1.json` qu'elle contient : `d424b59fc0ced791f9297b91251eb938d4175d3ce616c82a2ae94df754d110b2` (égale à celle que le rapport imprime) ;
  - `1906.08938v2.pdf` : `3fbaedd9705420fff23cbadb9c7d3de2240c2714c23440cbf133718534194ea9` ; `2605.16140v1.pdf` : `1f70a3284a2eca0b62cded4dd43e6f88cc6930e3275349a17bee76850860a72a` ; `math-0410072v1.pdf` : `cfcca06ea5e2b3852549dd896f381b2141c82fffa787787fc6fb6a5db560cbbf` (toutes trois égales à leur compagnon `.sha256`).
- Citations : **45 citations propres contrôlées par programme, 0 échec** au contrôle final (script `controle_citations_contre_lecture_v1.py`, lancé par `python3 -I` ; essai préalable : cas juste réussi, cinq cas altérés tous refusés). Un premier passage a donné 3 échecs (deux formes de texte, une page fausse de mon fait : 13 au lieu de 14) ; les trois ont été corrigées, journal gardé. En plus : **rejeu, par mon script, des 55 citations du rapport : 0 échec.**
- Convention : un texte anglais entre « » suivi de [Kn] est une de mes citations contrôlées (annexe) ; [Cn] renvoie à la numérotation du rapport contre-lu.

## Fichiers lus (liste exacte)

1. `docs/sources/lecture-pdf-niveau3/compte-2/rapport-L-lot8-v1.md` (en entier) et son compagnon `.sha256`.
2. `docs/sources/lecture-pdf-niveau3/compte-2/fichiers-de-travail-L-lot8-v1.tar`, extraite dans mon dossier de travail ; ouverts : `calcul_shewhart_v1.py`, `calcul_shewhart_v1.txt`, `controle_citations_v1.py`, `journal-v1.txt`, `journal-essais-controle-v1.txt` ; `citations-L-v1.json` lu par programme (rejeu) ; les autres fichiers de l'archive n'ont pas été ouverts.
3. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 53 à 77.
4. `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 85.
5. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 137 à 152.
6. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 368 à 407.
7. `…/scratchpad/pieces-10016a61/docs/sources/lecture-pdf-niveau3/consignes-v1/consigne-commune-lecture-v1.md` (en entier). Les fichiers que cette consigne renvoie à lire (interdits communs, programme, antériorité du niveau 2) ne sont pas dans ma liste : je ne les ai pas ouverts.
8. Dans `…/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot8/` : `ls` du dossier, les compagnons `.sha256` (affichés ensemble par une seule commande, ceux des autres pièces du lot compris, sans ouvrir aucun autre PDF), et les trois PDF nommés, par `pdftotext` page par page (texte brut, et avec `-layout` pour le contrôle des citations) :
   - `1906.08938v2.pdf` : les 16 pages lues en entier ; page 11 vue en image (figure 4) ;
   - `2605.16140v1.pdf` : pages 1 à 10 lues en entier ; pages 11 à 36 lues sur les lignes de prose (les lignes de formule courtes écartées par un filtre de longueur) ; pages 19 à 22 vues en image (équations (81) à (115)) ;
   - `math-0410072v1.pdf` : pages 1 à 34 lues sur les lignes de prose (même filtre) ; pages 9 et 10 vues en image (figure 1, théorème 1.3).
   - Puis recherche par mots sur le texte complet des trois pièces (budget, total, énergie, invariance, « ne dépend que de », allocation, étalement, garantie toujours valide, martingale, dépendance, plusieurs émetteurs, compensation, report, fragmentation, échantillon fini, racine carrée).

Aucune ouverture fautive. Aucune recherche récursive dans le dépôt, aucune commande git, aucun appel réseau ni de modèle, aucune dépense. Aucun refus de permission, de crochet ni de classifieur.

**Limite de ma lecture, dite d'emblée.** Les formules des pages 11 à 18 et 23 à 33 de `2605.16140v1.pdf` et celles des preuves de `math-0410072v1.pdf` n'ont été lues que par le texte extrait, filtré ; un énoncé qui ne tiendrait que dans une formule sans phrase d'accompagnement a pu m'échapper. Les énoncés nommés (lemmes, théorèmes, remarques, corollaires) ont tous leur phrase d'accompagnement, que j'ai lue.

## 0. Verdict

**Le rapport tient avec corrections.** Aucun constat bloquant : je n'ai trouvé, dans les trois pièces, aucune occupation d'une composante que le rapport dit « non trouvée ». Les 55 citations du rapport figurent bien aux pages dites. Quatre constats majeurs, tous de libellé ou de classement, aucun ne change la case d'ensemble :

1. **(majeur, occupation surestimée)** l'occupation partielle de L1 par `2605.16140` est **trop forte dans son libellé** : la pièce ne montre pas qu'une grandeur de détection « ne dépend que du budget cumulé quelle que soit l'allocation » ; côté guetteur elle montre une borne **quadratique**, qui dépend de la répartition et de l'état du canal ; côté information, l'identité linéaire porte sur les observations du sondeur, pas sur ce que le guetteur détecte. Case juste : **voisin (outil)** pour L1, et **rappel du cœur classique déjà cité** (borne par une divergence additive) ;
2. **(majeur, voisin manqué)** le calcul « Shewhart » est juste en chiffres mais ne prouve pas ce que le rapport en tire : il ne dit rien de L1 (aucune statistique somme), et sa « non-monotonie » vient de la fenêtre qui s'allonge. À fenêtre fixe, la formule du théorème 1 de `1906.08938` redonne la **forme de L2** (détecteur instantané, produit sur les pas, alarme décroissante avec la fragmentation, plancher au-dessus du niveau nul). La case L2 × `1906.08938` doit passer de « ne touche pas » à **voisin** ;
3. **(majeur, liste incomplète)** deux familles de voisins **nommés dans les pièces et non lus** manquent à la liste du rapport : la stéganographie par lots (Ker, pièce [2] de `2605.16140`, p. 1 et 34) et l'émetteur discret dont le guetteur ignore l'instant de départ (Bash, Goeckel et Towsley, pièces [9] et [10] de `1906.08938`, p. 1, 2, 15) ;
4. **(majeur, phrase publique)** la liste « ce qu'une phrase publique ne doit pas affirmer » a quatre manques (section 6).

**Mon verdict sur L, table fermée : « occupé en partie »** — case inchangée, et occupée **par le seul cœur classique** (échelle en racine carrée, borne par une divergence additive, dichotomie somme contre maximum). Les composantes de l'énoncé adverse (égalité exacte en loi de L1, L4, L2 au seuil exact et à n fini, borne invariante, coût du report et prix de la garantie toujours valide de L3, comparaison processus e cumulé contre détecteur de rupture, non-compensation, validité sous dépendance, application aux sondes) sont **non trouvées dans les trois pièces lues** — ce qui n'est pas un trou du champ : trois voisins plus proches sont nommés et non lus.

## 1. Les pages citées portent-elles ce que le rapport leur fait dire ?

Relu : chaque page citée à l'appui d'une occupation ou d'un verdict (sections 0 à 3 du rapport). Bilan : porté, sauf les points ci-dessous.

### 1.1 Constat A — majeur — L1 × `2605.16140` : « occupée en partie » est trop fort dans son libellé

Pages : 7, 9, 14, 16, 17, 18, 21, 22.

Le rapport écrit (section 0, point 1) : « **Fait** : dépendance au seul budget cumulé, quelle que soit l'allocation causale, en borne (côté discrétion) et en espérance (côté information) ». Les pages disent autre chose, sur les deux versants.

- **Côté guetteur (discrétion).** La grandeur bornée est l'entropie relative entre ce que voit le guetteur sous sondage actif et sous sondage innocent ; la borne est l'espérance d'une somme de **carrés** des probabilités de sondage, pondérés par un coefficient qui **change avec l'état du canal** (équations (104) à (106), p. 21, vues en image). Le rapport cite [C28] en s'arrêtant à « depends only on the current probing probability » ; la phrase continue : « where the instantaneous cost depends only on the current probing probability βi and channel state » [K25] (p. 14). La coupe retire la moitié de la dépendance : sonder avant ou après la rupture ne coûte pas pareil, et la part d'avant la rupture n'est écartée que par un argument asymptotique (« dropping the pre-change part of ECB » [K30], p. 21 ; « intuitively the ECB is overwhelmingly dominated by the post-change detection period » [K33], p. 32). Les auteurs lisent eux-mêmes ce coût comme une affaire d'intensité et de structure, non de total : « the probing sequence should both use low probing intensity and avoid inducing statistically detectable structure » [K24] (p. 14). À total **linéaire** de sondage fixé, cette borne **dépend de la répartition** : c'est l'objet même du lemme VI.2 (« On the other hand, from Cauchy-Schwarz inequality, » [K31], p. 21) et de la remarque VI.3 (« allocate a flat sequence between » [K32], p. 22). Dire qu'une borne « ne dépend que de » la fonctionnelle qui la définit est une tautologie ; l'invariance de L1 est l'invariance à **total linéaire fixé**, et la page porte le contraire. Le rapport le dit lui-même en 1.2 (« contre-indice ») : les deux passages se contredisent.
- **Côté information (identité linéaire).** L'identité « entropie relative = D × effort total » (« Second, we claim that the relative entropy between P and Q is exactly the product of » [K28], p. 18) compare la loi vraie des observations **du sondeur** à une loi de référence « bruit pur » (« Under Q, we maintain Γ ∼ Geo(ρ), but the observations are drawn from the pre-change distribution for all t ≥ 1, regardless of Γ. » [K27], p. 17), pour un observateur fictif qui connaît l'instant de rupture (« representing the history of Alice’s causal information joined with oracle knowledge of the changepoint » [K29], p. 18). Ce n'est pas une grandeur de détection **par le guetteur** : c'est l'information que le sondeur tire de ses propres sondes, linéaire en leur nombre attendu (règle de chaîne et identité de Wald). Personne n'y répartit un budget **contre** un détecteur. Elle sert à borner un délai moyen (lemme VI.1), pas la puissance d'un test.
- **Rôles.** Le guetteur fait un test binaire hors ligne en connaissant la politique (« we assume that Eve has full knowledge of Alice’s active policy » [K23], p. 7) : ni séquentiel, ni toujours valide. Le rapport le dit ; cela éloigne encore de L.

Ce qui reste vrai : la pièce porte, une fois de plus, le **cœur classique** déjà cité au niveau 3 (borne de la détectabilité par une divergence additive dans le temps, ici sous forme quadratique et pour toute politique causale) et l'**échelle en racine carrée** (lemme VI.2, p. 21 : l'effort linéaire total admissible croît comme la racine de la durée). La phrase que le rapport cite en [C29], « the ECB constraint fundamentally limits the total probing effort that can be expended covertly. » [K26] (p. 16), dit cela et rien de plus : la contrainte **plafonne** le total linéaire ; elle ne dit pas que la détectabilité en est fonction. Aucune composante propre à L1 (identité trajectorielle, égalité en loi, puissance fonction de (B, n₀, F₀, α)) n'est « faite ».

Jugement demandé : **trop forte** dans le libellé et dans la ligne de table où elle est rangée ; **juste** seulement si « occupée en partie » veut dire « rappel du cœur classique » au sens de la synthèse du niveau 3 (forme quadratique). Le rapport écrit d'ailleurs « le verdict d'ensemble ne change pas de case » : sur ce point il a raison.

Texte corrigé proposé (section 0, point 1 du rapport) :

```text
1. **Voisin (outil), et rappel du cœur classique — `2605.16140v1` (Lo et Bloch).** Pour toute politique causale, l'article
   borne ce que le guetteur peut distinguer par un coût cumulé QUADRATIQUE en les probabilités de sondage, pondéré par
   l'état du canal (p. 14, 21) : à total linéaire fixé, cette borne dépend de la répartition (allocation plate optimale,
   p. 21-22). Il établit par ailleurs que l'information que le sondeur tire de ses propres sondes vaut exactement
   D × nombre attendu de sondes après la rupture (p. 18) : identité de Wald, côté détecteur, sans adversaire qui
   répartit. Aucune composante propre à L1 n'est faite (ni identité trajectorielle, ni égalité en loi, ni puissance
   fonction de (B, n₀, F₀, α), ni budget linéaire face à une statistique somme). C'est la même nature que la borne par
   la divergence déjà portée au niveau 3 : le verdict d'ensemble ne change pas de case.
```

Texte corrigé proposé (table, ligne L1, colonne `2605.16140`) :

```text
voisin (outil) : borne quadratique de la détectabilité, additive dans le temps, pour toute politique causale, p. 14, 21 ;
identité « information du sondeur = D × effort total », p. 18 ; contre-indice à l'invariance face au détecteur optimal
(répartition plate optimale, p. 21-22) ; non fait : égalité en loi, statistique somme, budget linéaire
```

Texte corrigé proposé (section 3 du rapport, seconde phrase) : remplacer « dépendance au seul budget cumulé pour toute allocation causale, en borne et en espérance, dans 2605.16140 » par « borne quadratique additive de la détectabilité pour toute politique causale, dans 2605.16140, qui est le cœur classique déjà cité ».

Texte corrigé proposé (section 4 du rapport, avant-dernière proposition) : remplacer « la dépendance d'une grandeur de détection au seul budget cumulé, pour toute allocation causale, existe comme outil (identité de Wald, budget de discrétion attendu de Lo et Bloch) » par « la borne de la détectabilité par une divergence additive dans le temps, pour toute allocation causale, est classique (forme quadratique chez Lo et Bloch) ; face au détecteur optimal la répartition compte ».

### 1.2 Constat B — majeur — le calcul « Shewhart » : chiffres justes, conclusion mal placée ; L2 × `1906.08938` est un voisin

Pages : 4, 5, 6, 7, 10, 13 ; calcul : `calcul_shewhart_contre_lecture_v1.py` et sa sortie `.txt` (archive).

**Le calcul est juste.** La formule de la page 7 (fin de la preuve du théorème 1, lue sur le texte extrait) est Q = (1 − (1/γ)^{1/(1+q)})^L ; je la retrouve aussi en la redérivant (seuil d'énergie ln γ, énergie reçue de loi exponentielle de moyenne 1 + q). Mon script, écrit sans reprendre celui du rapport, redonne ses valeurs : à qL = 3 et γ = 500, Q = 0,7885 (L = 1), 0,9192 (L = 10), 0,7866 (L = 100) (calcul). γ = 500 est bien le réglage de l'article (« set the ARL2FA of Willie’s detector γ = 500 » [K14], p. 12).

**Il ne prouve pas ce que le rapport en tire.**

- *Il ne dit rien de L1.* Le test de Shewhart est un détecteur **instantané** : « only depends on the instantaneous sample observation and is » [K6] (p. 4), équivalent à un seuil sur l'énergie de chaque pas (« the detection procedure is equivalent to sequentially comparing the received signal power to a pre-designed threshold » [K7], p. 5). Sur une fenêtre, c'est un **maximum**, pas une somme. Qu'un maximum ne soit pas invariant à la répartition est le contenu de L2, pas un constat sur L1. Le rapport range ce calcul dans la ligne L1 de sa table (« non invariante à énergie fixée, calcul ») : mal placé. L'article ne contient **aucune statistique somme** ; il ne peut ni occuper ni contredire L1. De plus « l'énergie totale qL » n'est pas une grandeur de l'article (son objectif est L·ln(1 + q/σ²), p. 6).
- *La « non-monotonie » est un effet de fenêtre.* Q est la probabilité qu'**aucune** alarme ne sonne pendant les L pas d'émission, fausses alarmes comprises. Sans aucune émission, une fenêtre de L = 100 pas donne déjà (1 − 1/γ)^{100} = 0,8186 (calcul). La remontée puis la baisse de Q comparent des fenêtres de longueurs différentes. L'écart à cette base (la détection due à l'émission seule) vaut 0,2095 (L = 1), 0,0610 (L = 10), 0,0319 (L = 100) : il **décroît de façon monotone** sur L = 1 à 200 (calcul, vérifié par programme).
- *À fenêtre fixe, on retrouve la forme de L2.* Sur une fenêtre fixe de n = 100 pas, la probabilité d'alarme vaut 1 − (1 − 1/γ)^{n−m}·Q_m(E/m) : même forme produit que la formule de L2 dans la note v2 (1 − Φ(c)^{n−m}·Φ(c − B/(mσ))^m), dans un modèle de variance au lieu d'un modèle de moyenne. À E = 3 : 0,3532 (m = 1), 0,2324 (m = 10), 0,2134 (m = n), contre 0,1814 sans émission ; **décroissante en m, plancher strictement au-dessus du niveau nul** (écart 0,0319) (calcul). C'est, en une multiplication à partir du théorème 1 (« With the Shewhart test, the following theorem characterizes » [K10], p. 6 ; produit sur les pas : « (b) follows from the fact that {yν+k : 1 ≤ k ≤ L} are i.i.d. » [K11], p. 7), la forme qualitative de L2. L'article ne l'écrit pas (il ne fixe jamais q·L et ne raisonne pas à fenêtre fixe) ; il écrit seulement la monotonie séparée (« monotonically decreasing in both q and L. » [K13], p. 10) et l'optimum intérieur en durée (« is maximized in the middle of the feasible region of L. » [K16], p. 13).

Conséquence : **L2 × `1906.08938` n'est pas « ne touche pas » mais « voisin »** (forme close du détecteur instantané sous émission répartie sur L pas, théorème 1, p. 6-7 ; ni budget total fixé, ni seuil du maximum sur n, ni énoncé de l'effondrement, ni plancher). Ce n'est pas une occupation : la décroissance et le plancher sont **mon** calcul, pas un énoncé de l'article.

Texte corrigé proposé (section 1.1 du rapport, puce « Répartition dans le temps à budget fixé ») :

```text
- **Répartition dans le temps à budget fixé** : non étudiée ; l'article ne contient aucune statistique somme et ne dit
  donc rien de L1. Sous le test de Shewhart (détecteur instantané, c'est-à-dire un maximum sur la fenêtre), la formule
  de la p. 7 donne, à q·L = 3 et γ = 500 : 0,79 (L = 1), 0,92 (L = 10), 0,79 (L = 100) (calcul). La baisse aux grands L
  vient des fausses alarmes d'une fenêtre plus longue (0,82 sans émission pour L = 100) ; à fenêtre fixe de 100 pas,
  l'alarme décroît avec la fragmentation, de 0,35 (1 pas) à 0,21 (100 pas), au-dessus de 0,18 sans émission (calcul) :
  c'est la forme de L2, que l'article n'énonce pas. Voisin de L2, sans objet pour L1.
```

Texte corrigé proposé (table) : ligne L1, colonne `1906.08938` : « ne touche pas (aucune statistique somme ; discrétion fonction de q et L séparément) ; échelle √n citée comme classique, p. 1 [C5] ». Ligne L2, colonne `1906.08938` : « voisin : forme close du détecteur instantané, produit sur les pas (théorème 1, p. 6-7) ; à fenêtre fixe elle donne la décroissance avec la fragmentation et un plancher (calcul du contre-lecteur, non énoncé par l'article) ».

### 1.3 Constat C — mineur — le calendrier face aux détecteurs de rupture : sens juste, portée à préciser

Pages : 5, 6, 10, 13, 14, 15.

« Commencer tard nuit à l'émetteur discret » est porté par les pages ([C13], [C16], [C17] ; figure 4 vue en image : somme cumulée de Page à ν = 40 et 300, Shiryaev-Roberts à ν = 100 et 300, comme le dit le rapport). Trois précisions manquent :

- l'effet est **conditionnel à l'absence de fausse alarme avant le départ** (définition (7), p. 6 : probabilité sachant T > ν ; l'émetteur perçoit les alarmes, [C8]) ;
- il **sature** : « converges to a quasi-stationary distribution » [K17] (p. 14) ; le mécanisme est l'état initial de la statistique, pas une accumulation sans fin (« This is because the detector accumulates more noise samples before Alice starts to transmit to Bob as ν increases. » [K15], p. 13 ; « SR test is not sensitive to a statistical change that occurs at the beginning of the detection procedure » [K18], p. 14) ;
- le seul énoncé **démontré** sur le calendrier est le corollaire 3 : « Corollary 3: Under the SR test, if ν < γ − 2 − µ for some positive real number µ, then for any pre-given θ (0 < θ < 1), there exists a θ-covert (q, L)-system. » [K12] (p. 10) ; le rapport le range parmi les « conditions nécessaires de faisabilité » sans voir qu'il porte sur l'instant de départ. Le reste est numérique.

« Sens opposé à L3 (a) » et « cohérent avec L3 (d) » sont des rapprochements du lecteur entre détecteurs différents et horizons différents (pas d'horizon fixe dans l'article) : à marquer comme tels. La case « voisin » est juste.

Texte corrigé proposé (fin de la puce « Calendrier » du rapport) : ajouter « Portée : effet conditionnel à l'absence de fausse alarme avant le départ, qui sature quand la statistique atteint sa loi quasi stationnaire (p. 14) ; seul énoncé démontré : corollaire 3 (p. 10, Shiryaev-Roberts, départ précoce) ; le reste est numérique. Le rapprochement avec L3 est le mien, entre détecteurs et horizons différents. »

### 1.4 Constat D — mineur — « exactement l'échelle de cette loi » (section 0, point 2)

Pages : `1906.08938` p. 1 ; `2605.16140` p. 2.

Les pages portent la loi de la racine carrée pour un **nombre de bits** (« bits covertly and reliably to Bob in n channel usages » [K3], p. 1, rappel d'une pièce non lue) et pour un **gain de délai** en racine du logarithme du niveau ([C25], p. 2). Aucune ne l'écrit pour un budget linéaire de décalage face à une statistique somme. La mise en garde du rapport (« ne peut pas être présentée comme un apport ») est prudente et je la garde ; « exactement » est à remplacer par « analogue d'échelle ». La pièce d'origine (Bash, Goeckel et Towsley, 2013) reste non lue.

### 1.5 Constat E — mineur — `2605.16140`, notation de D

Page 19 (vue en image). L'équation (91) écrit D(P₁¹‖P₁⁰) alors que la définition (p. 8) et les équations (81) à (83) (dénominateur P₀ à action donnée) imposent D(P₁¹‖P₀¹). Coquille, comme le dit le rapport ; mais sa parenthèse (« P₁⁰ = P₀⁰ par l'hypothèse ») ne justifie rien : cette hypothèse égalise les lois sous action **innocente**, pas P₁⁰ et P₀¹. Texte corrigé : supprimer la parenthèse, écrire « coquille probable : (81)-(83) imposent P₀¹ au dénominateur ».

### 1.6 Constat F — mineur — `math/0410072` : une incohérence interne oubliée, et la portée de « la somme »

Pages 4, 9, 10, 11.

- La légende de la figure 1 dit : « Two detection boundaries are only different when » [K40] (p. 9) suivi de ¾ < β < 1 (vu en image), alors que le texte de la page 10 dit l'inverse : égalité sur [¾, 1) (« so that Mn is effective in the range of very sparse alternatives, while » [K41]) et écart pour β < ¾ (« so that Mn is inefficient if » [K42]) ; la figure elle-même donne raison au texte. À ajouter aux incohérences relevées (le rapport lit juste : il suit le texte).
- « La somme ne voit rien » : la pièce ne démontre rien sur la somme simple des scores ; elle a une phrase d'intuition ([C43], p. 4) et un théorème sur la combinaison de Fisher (« Fn is unable to separate H1 and H0 » [K43], p. 11). Le théorème 1.3 (p. 10, vu en image) n'énonce que le succès du maximum au-dessus de sa frontière. À écrire ainsi. Le verdict « voisin et contre-indice de formulation » pour L2 est juste ; tout est asymptotique (« Section 4 describes some simulation experiments. » [K44], p. 14 : une seule expérience à n = 10⁶), sans budget total (« so that the fraction of nonzero means is small but not vanishingly small » [K39], p. 4).
- L4 × `math/0410072` : « ne touche pas » est défendable ; le modèle est celui de n unités observées en même temps (« there are n independent tests of unrelated hypotheses » [K38], p. 2), analogue lointain de la répartition entre agents au même pas, sans budget ni invariance. Je laisse la case.

## 2. Recherche active d'une occupation des composantes dites « non trouvées »

Méthode : lecture, puis recherche par mots sur le texte complet des trois pièces, puis relecture des passages trouvés.

| composante dite « non trouvée » | ce que j'ai cherché et trouvé | mon verdict |
|---|---|---|
| L4 — répartition entre agents au même pas | un seul émetteur (`1906.08938`), un seul sondeur (`2605.16140`), n unités sans budget (`math/0410072`) ; aucun des mots « plusieurs émetteurs, agents, capteurs » | non trouvée |
| L2 — seuil exact, n fini, plancher | `math/0410072` : asymptotique, pas de budget total ; `1906.08938` : forme close du détecteur instantané (théorème 1), dont on tire la forme de L2 en une ligne (constat B) | non trouvée comme énoncé ; **un voisin de plus que ne dit le rapport** |
| L3 — borne inférieure invariante fonction de (B, n₀) | aucune borne de détectabilité fonction d'un seul total : `1906.08938` n'a ni « budget » ni « total » au sens d'une contrainte (recherche par mots : 0 occurrence utile) ; `2605.16140` : borne quadratique, dépendant de la répartition | non trouvée |
| L3 — coût du report, prix de la garantie toujours valide | aucune garantie toujours valide, aucune martingale de test, aucun processus e (0 occurrence) ; les trois détecteurs de `1906.08938` sont réglés par la durée moyenne avant fausse alarme | non trouvée |
| effet du report du début | `1906.08938` : effet de l'instant de départ sur la somme cumulée de Page et Shiryaev-Roberts (figure 4, figure 8, corollaire 3, conclusion p. 15) ; sens : départ tardif défavorable à l'émetteur ; nul sous Shewhart | **voisin** (le rapport le dit) ; le constat générique « le calendrier compte face à un détecteur séquentiel » est **publié** |
| processus e cumulé contre détecteur de rupture | aucun processus e ; le critère « alarme pendant l'émission » est posé : « We refer to such an event as timely detection. » [K8] (p. 5), « Willie’s detection process makes sense only when timely detection occurs » [K9] (p. 6) | comparaison non trouvée ; **le critère est publié** |
| non-compensation | 0 occurrence | non trouvée |
| validité sous dépendance | observations indépendantes partout ; `2605.16140` : dépendance des seules actions de sondage, traitée par majoration ([C27]) | non trouvée |
| application aux sondes internes | sans objet dans les trois pièces | non trouvée |

Je confirme donc le point 3 de la section 0 du rapport, avec la réserve du constat B pour L2 et deux précisions (critère « alarme pendant l'émission » et constat générique sur le calendrier : publiés).

**Voisins nommés dans les pièces, non lus, que le rapport ne signale pas (constat G — majeur).**

- **Stéganographie par lots.** `2605.16140` ouvre sur « from steganography [1]–[3] to covert communications [4]–[6] » [K21] (p. 1) et cite « A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [K34] (p. 34). Par son seul titre, c'est la répartition d'une charge cachée entre plusieurs objets et sa capacité : le voisin le plus direct de « un budget total réparti, face à un détecteur qui agrège » (L1, L4, L2). De mémoire, donc **non opposable et à vérifier sur PDF** : cette littérature étudie les stratégies de répartition (concentrer ou étaler) face à des détecteurs groupés et une loi de la racine carrée de la capacité. `math/0410072` nomme aussi le domaine (« such as in watermarking and steganography, could reasonably use the model » [K45], p. 22). Zone séduisante dite libre : à vérifier plus durement.
- **Guetteur qui ignore l'instant de départ.** `1906.08938` rappelle que la loi de la racine carrée peut être battue « when Willie does not exactly know when Alice starts to transmit (if she does) [9]–[11] » [K4] (p. 1), dans un modèle où l'émission occupe un bloc fini, « the beginning of which is random and unknown to Willie » [K5] (p. 2). Pièces : « B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” » [K20] et « B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” » [K19] (p. 15). C'est le levier « calendrier » de l'attaquant et la dilution dans un horizon plus long (L1 « décroît avec n₀ », L3). Le rapport ne nomme que « Bash et collègues (2013 et suivants) », sans ce levier.
- **Attaques furtives sous contrainte de détectabilité en commande** : « ability to perform stealthy attacks in cyber-physical systems [15], [16] » [K22] (p. 1), dont « Security in stochastic control systems: Fundamental limitations and performance » [K35] (p. 35). Voisin d'un attaquant à budget de furtivité borné ; priorité moindre.

Texte corrigé proposé : voir section 6 (lignes à ajouter) et, dans la section 6 du rapport (« Ce que je n'ai pas fait »), ajouter à la liste des pièces citées non versées : « [2] de 2605.16140 (Ker, stéganographie par lots), [15] et [16] de 2605.16140 (attaques furtives en commande), [9] et [10] de 1906.08938 (guetteur ignorant l'instant de départ) ».

## 3. Occupation partielle de L1 par `2605.16140` : jugement

**Trop forte** (constat A). Case juste pour L1 : « voisin (outil) » ; la pièce rappelle le cœur classique déjà cité et fournit un contre-indice à toute lecture « pour tout détecteur ». La case d'ensemble de L ne bouge pas.

## 4. Affirmation d'identité de la pièce « Huang, Wang et Poor »

**Juste, et bien bornée.** `1906.08938v2.pdf` imprime quatre auteurs en page 1 : « Ke-Wen Huang, Hui-Ming Wang, Senior Member, IEEE, » [K1] et « Don Towsley, Life Fellow, IEEE, and H. Vincent Poor, Fellow, IEEE » [K2]. La bibliographie de `2605.16140` (p. 35) distingue deux pièces : « K.-W. Huang, H.-M. Wang, D. Towsley, and H. V. Poor, “LPD communication: A sequential change-point detection perspective,” » [K36] et « K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” » [K37]. Une pièce à exactement trois auteurs existe donc, sous un autre titre, ce qui s'accorde avec la mention « titre différent » du constat M4. « Probablement » est le bon mot : ni le rapport ni moi n'avons lu le rapport C2. Le constat M4 **n'est pas clos** pour cette pièce ; elle est à verser et à lire avant toute phrase publique sur L3 (mineur : le rapport pourrait le dire comme une action, pas seulement comme un doute).

## 5. Verdict sur le rapport et sur L

- Rapport : **tient avec corrections** (constats A, B, G et section 6 : majeurs ; C, D, E, F : mineurs ; aucun bloquant).
- L, table fermée : **occupé en partie** (par le seul cœur classique ; composantes de l'énoncé adverse non trouvées dans les trois pièces lues ; M4 non clos tant que la pièce à trois auteurs, la stéganographie par lots et les pièces sur l'instant de départ ne sont pas lues).

## 6. « Ce qu'une phrase publique ne doit pas affirmer » : manques et lignes à reprendre

**Lignes du rapport.** Les six lignes sont fondées. Deux sont à reformuler :

- ligne 1 (échelle en √n₀) : fondée ; écrire « analogue d'échelle » (constat D) ;
- ligne 2 (« faux face à un détecteur fondé sur la divergence… ») — mineur : les pages portent une **borne** qui dépend de la répartition, pas la performance exacte d'un détecteur ; et l'allocation plate est donnée comme indication, sous réserve (« if possible »). Texte corrigé : « que “la détectabilité ne dépend que du budget total” pour tout détecteur : non porté, et contredit au niveau des bornes publiées, qui sont quadratiques et dépendent de la répartition (2605.16140, p. 21-22) » ;
- lignes 3 à 6 : fondées telles quelles (ligne 3 : ajouter les conditions du constat C).

**Lignes manquantes (constat H — majeur).** Une phrase publique ne doit pas non plus affirmer :

```text
- que Lo et Bloch établissent qu'une grandeur de détection ne dépend que d'un budget total quelle que soit la
  répartition : leur borne côté guetteur est quadratique et dépend de la répartition ; leur identité linéaire porte sur
  l'information du sondeur (2605.16140, p. 14, 18, 21) — ne pas les citer comme précédent de l'invariance ;
- que la forme de L2 (détecteur instantané, produit sur les pas, alarme qui baisse quand on fragmente) est sans
  précédent de forme : la forme close existe pour le test de Shewhart (1906.08938, théorème 1, p. 6-7) ; seuls le
  seuil exact du maximum, le budget total fixé et le plancher à n fini restent non trouvés ;
- que « le calendrier compte face à un détecteur séquentiel » est un constat nouveau (1906.08938, p. 10, 13, 14, 15),
  ni que le critère « alarme avant la fin du dommage » l'est (« timely detection », 1906.08938, p. 5-6) ;
- que la répartition d'un budget caché entre plusieurs objets face à un détecteur qui agrège n'a pas de voisin :
  la stéganographie par lots (Ker, 2007, citée par 2605.16140, p. 34) et les pièces sur le guetteur qui ignore
  l'instant de départ (Bash, Goeckel et Towsley, citées par 1906.08938, p. 1, 2, 15) sont nommées et non lues.
```

Et compléter la ligne 5 du rapport par ces mêmes pièces.

## 7. Ce que je n'ai pas fait

- Je n'ai pas lu le rapport C2, ni les autres pièces du lot 8, ni aucune pièce citée non versée ; ce que je dis de la stéganographie par lots au-delà de son titre vient de ma mémoire et n'est pas opposable.
- Je n'ai pas relu les formules de `2605.16140` hors des pages 19 à 22 vues en image, ni les preuves de `math/0410072` (voir « Limite de ma lecture »).
- Je n'ai refait aucun calcul de L lui-même ; un seul calcul, sur la formule de la page 7 de `1906.08938` (trois lectures : reproduction, part de fausse alarme, fenêtre fixe).
- Je n'ai pas vérifié les chiffres de T0.3 cités par N-004 (hors de mes fichiers).

## 8. Refus

Aucun refus de permission, de crochet ni de classifieur. Aucune ouverture fautive.

## Annexe — mes citations contrôlées (numérotation de `citations-contre-lecture-L-v1.json`)

| n° | pièce | page | citation exacte |
|---|---|---|---|
| K1 | `1906.08938v2.pdf` | 1 | Ke-Wen Huang, Hui-Ming Wang, Senior Member, IEEE, |
| K2 | `1906.08938v2.pdf` | 1 | Don Towsley, Life Fellow, IEEE, and H. Vincent Poor, Fellow, IEEE |
| K3 | `1906.08938v2.pdf` | 1 | bits covertly and reliably to Bob in n channel usages |
| K4 | `1906.08938v2.pdf` | 1 | when Willie does not exactly know when Alice starts to transmit (if she does) [9]–[11] |
| K5 | `1906.08938v2.pdf` | 2 | the beginning of which is random and unknown to Willie |
| K6 | `1906.08938v2.pdf` | 4 | only depends on the instantaneous sample observation and is |
| K7 | `1906.08938v2.pdf` | 5 | the detection procedure is equivalent to sequentially comparing the received signal power to a pre-designed threshold |
| K8 | `1906.08938v2.pdf` | 5 | We refer to such an event as timely detection. |
| K9 | `1906.08938v2.pdf` | 6 | Willie’s detection process makes sense only when timely detection occurs |
| K10 | `1906.08938v2.pdf` | 6 | With the Shewhart test, the following theorem characterizes |
| K11 | `1906.08938v2.pdf` | 7 | (b) follows from the fact that {yν+k : 1 ≤ k ≤ L} are i.i.d. |
| K12 | `1906.08938v2.pdf` | 10 | Corollary 3: Under the SR test, if ν < γ − 2 − µ for some positive real number µ, then for any pre-given θ (0 < θ < 1), there exists a θ-covert (q, L)-system. |
| K13 | `1906.08938v2.pdf` | 10 | monotonically decreasing in both q and L. |
| K14 | `1906.08938v2.pdf` | 12 | set the ARL2FA of Willie’s detector γ = 500 |
| K15 | `1906.08938v2.pdf` | 13 | This is because the detector accumulates more noise samples before Alice starts to transmit to Bob as ν increases. |
| K16 | `1906.08938v2.pdf` | 13 | is maximized in the middle of the feasible region of L. |
| K17 | `1906.08938v2.pdf` | 14 | converges to a quasi-stationary distribution |
| K18 | `1906.08938v2.pdf` | 14 | SR test is not sensitive to a statistical change that occurs at the beginning of the detection procedure |
| K19 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” |
| K20 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” |
| K21 | `2605.16140v1.pdf` | 1 | from steganography [1]–[3] to covert communications [4]–[6] |
| K22 | `2605.16140v1.pdf` | 1 | ability to perform stealthy attacks in cyber-physical systems [15], [16] |
| K23 | `2605.16140v1.pdf` | 7 | we assume that Eve has full knowledge of Alice’s active policy |
| K24 | `2605.16140v1.pdf` | 14 | the probing sequence should both use low probing intensity and avoid inducing statistically detectable structure |
| K25 | `2605.16140v1.pdf` | 14 | where the instantaneous cost depends only on the current probing probability βi and channel state |
| K26 | `2605.16140v1.pdf` | 16 | the ECB constraint fundamentally limits the total probing effort that can be expended covertly. |
| K27 | `2605.16140v1.pdf` | 17 | Under Q, we maintain Γ ∼ Geo(ρ), but the observations are drawn from the pre-change distribution for all t ≥ 1, regardless of Γ. |
| K28 | `2605.16140v1.pdf` | 18 | Second, we claim that the relative entropy between P and Q is exactly the product of |
| K29 | `2605.16140v1.pdf` | 18 | representing the history of Alice’s causal information joined with oracle knowledge of the changepoint |
| K30 | `2605.16140v1.pdf` | 21 | dropping the pre-change part of ECB |
| K31 | `2605.16140v1.pdf` | 21 | On the other hand, from Cauchy-Schwarz inequality, |
| K32 | `2605.16140v1.pdf` | 22 | allocate a flat sequence between |
| K33 | `2605.16140v1.pdf` | 32 | intuitively the ECB is overwhelmingly dominated by the post-change detection period |
| K34 | `2605.16140v1.pdf` | 34 | A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. |
| K35 | `2605.16140v1.pdf` | 35 | Security in stochastic control systems: Fundamental limitations and performance |
| K36 | `2605.16140v1.pdf` | 35 | K.-W. Huang, H.-M. Wang, D. Towsley, and H. V. Poor, “LPD communication: A sequential change-point detection perspective,” |
| K37 | `2605.16140v1.pdf` | 35 | K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” |
| K38 | `math-0410072v1.pdf` | 2 | there are n independent tests of unrelated hypotheses |
| K39 | `math-0410072v1.pdf` | 4 | so that the fraction of nonzero means is small but not vanishingly small |
| K40 | `math-0410072v1.pdf` | 9 | Two detection boundaries are only different when |
| K41 | `math-0410072v1.pdf` | 10 | so that Mn is effective in the range of very sparse alternatives, while |
| K42 | `math-0410072v1.pdf` | 10 | so that Mn is inefficient if |
| K43 | `math-0410072v1.pdf` | 11 | Fn is unable to separate H1 and H0 |
| K44 | `math-0410072v1.pdf` | 14 | Section 4 describes some simulation experiments. |
| K45 | `math-0410072v1.pdf` | 22 | such as in watermarking and steganography, could reasonably use the model |
