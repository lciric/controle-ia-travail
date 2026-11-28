# Contre-lecture des réponses aux questions 6 et 8 (découverte, plasticité) et 10 (forme de l'anomalie) (v1)

- **Nature** : pièce de travail (classe C), contre-lecture. Aucune dépense, aucun appel externe, calculs sur processeur seulement. Les réponses ne sont pas modifiées. Non committée.
- **Heure** : `2026-11-28T06:25:19Z` (`date -u`, début de rédaction).
- **Auteur** : Claude Opus 5.5, sous-agent neuf, qui n'a écrit aucune des pièces relues.
- **Pièces relues** (empreintes vérifiées par leurs compagnons `.sha256`, toutes conformes) : `reponse-q6-q8-decouverte-et-plasticite-v1.md` (`2ba05ea6…`) ; `enumeration-allocation-decouverte-v1.py` (`5c57a810…`) et sa sortie (`2ddf8af0…`) ; `simulation-plasticite-bifurcation-v1.py` (`cb69ac93…`) et sa sortie (`ce1f8618…`) ; `reponse-q10-forme-anomalie-objet-manquant-v1.md` ; `forme-anomalie-objet-manquant-v1.py` (`47da91c6…`) et sa sortie (`b2cfaa0e…`).
- **Demandes et notations** : `demandes-reformulees-quatre-points-v1.md` (`52d1cc47…`, section de la question 6) ; `demandes-reformulees-quatre-points-q8-q11-v1.md` (`632c7af2…`, questions 8 et 10) ; `complement-questions-10-11-et-apport-q5-v1.md` (`43716a8a…`) ; `erratum-notations-kappa-et-hypergraphe-v1.md` (`72afe693…`). Pour juger les erreurs relevées : `docs/notes/idee-interessante-v1/reponse-fable-max-v1.md` (ligne 47) ; `docs/notes/protocole-x-boucle-organisme-controle-v1/reponse-approfondie-carbon-boucle-organisme-controle-v1.md` (sections 2.1 et 2.3) ; `reponses-google-v1/reponse-carbon-meta-espace-v1.md` (lignes 20, 36, 48) ; `reponse-q9-expose-graphe-meta-mathematique-v1.md` (ligne 90) et son erratum 2.
- **Sources** : PDF de `docs/sources/pdf/q6-q8-2026-11-28/` et `docs/sources/pdf/q10-2026-11-28/`, empreintes conformes à leurs compagnons et à l'annexe B de la réponse aux questions 6 et 8 ; lus comme texte (`pdftotext`, page par page), rien exécuté qui en vienne.
- **Rien ouvert** sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Classes** : *bloquant* = une conclusion ou un chiffre cité est faux, ou une règle gelée est violée d'une manière qui fausse la pièce ; *majeur* = démonstration incomplète, écart à la demande, fuite ou sur-revendication qu'il faut corriger avant tout versement ; *mineur* = précision, page, notation, cohérence interne.

## Verdict

Aucun point bloquant. Les trois scripts se rejouent à l'identique, octet pour octet, et leurs sorties portent tous les chiffres cités que j'ai contrôlés. Les démonstrations refaites tiennent (dérivées de la distance optimale, lemme d'échange, critère du filtre et son plafond, allocation de Koopman, pli et hystérésis du champ moyen, précession au premier ordre, énoncé sur les graphes à transports). Les citations de la réponse à la question 10 sont exactes à la page dans 20 contrôles sur 20. Celles de la réponse aux questions 6 et 8 le sont dans 15 cas sur 18 : les trois erreurs sont des pages ou une portée mal dite. **Douze points majeurs**, surtout trois choses : des résultats de jouet présentés comme des faits dans les verdicts ; une fuite possible dans le test daté de la question 8 ; des écarts à la demande de la question 10 (longueur dépassée d'un tiers, pièces de Carbon non lues, « tu ne lances rien »). **Vingt points mineurs.**

## 1. Rejeu des scripts

Rejoués par `python3 -I <script>` depuis un dossier vide du bloc-notes (Python 3.13, numpy 2.5.3), puis comparés par `diff` aux sorties versées.

|Script|Durée observée (annoncée)|Sortie|
|---|---|---|
|`enumeration-allocation-decouverte-v1.py`|9 s (« dix secondes »)|identique|
|`simulation-plasticite-bifurcation-v1.py`|36 s (« moins d'une minute »)|identique|
|`forme-anomalie-objet-manquant-v1.py`|77 s (« 75 secondes »)|identique|

J'ai aussi recalculé à part, hors des scripts : les quatre probabilités sous latent de loi bêta (0,3217 ; 0,5810 ; 0,7979 ; 0,9349) et les trois répartitions (0,4882 ; 0,5848 ; 0,6296) ; la part finale du vivier fini (0,5828) ; la composante géante bipartie (0,164 à `c_A·c_B = 1,5`) ; les valeurs de réserve avec délai (0,919 et 0,769) ; le seuil `α_o < 0,742` ; `h_pli = 0,2075` et une largeur d'hystérésis de 2,607 à `J/T = 3` ; la somme du χ² de Mercure, Vénus et la Terre (1,02 ; 23,0) ; les trois décompositions du clair de lune monstrueux ; les six produits de signe −1 de la section de Pauli. Tout concorde.

## 2. Citations contrôlées dans les PDF versés

✓ = passage trouvé à la page dite ; ✗ = écart (renvoi au point qui le traite).

|Réponse|Citation|Contrôle|
|---|---|---|
|6-8|Weitzman, équation 7, p. 9|✓ (page imprimée 9)|
|6-8|Weitzman, `z = V−c/p`, p. 7 ; théorème, p. 6-7|✗ (mineur m1)|
|6-8|Nishihara et collègues, théorème 11, p. 4|✓|
|6-8|Hamilton et Pryadko, théorème 4, p. 3|✓ pour le texte ; ✗ pour la portée (m2)|
|6-8|Karrer, Newman et Zdeborová, p. 1 et 3 (exact si localement arborescent, borne basse sinon)|✓|
|6-8|Newman, Strogatz et Watts, seuil biparti, p. 1 et 3|✗ (critère à la p. 12 du fichier ; m3)|
|6-8|Kuhn, p. 52, 65, 71, 84, 91|✓ (5 sur 5)|
|6-8|Cartwright et Harary, p. 286, 288, 289|✓|
|6-8|Thagard 1989, harmonie p. 443, conservatisme p. 441|✓|
|6-8|Uzzi et collègues, 9,11 contre 5 %, p. 470|✓|
|6-8|Funk et Owen-Smith, de −1 à 1, p. 795|✓|
|6-8|Park, Leahey et Funk, 91,9 à 100 % et 93,5 à 96,4 %, p. 3|✓|
|6-8|Pesquita et Couto, mesure F 0,79, p. 1 ; « reorganization of an entire branch », p. 13|✓|
|6-8|Ustyuzhanin et collègues, avance de 25 et de 14 à 19 trimestres|✓ (p. 3 et 9 du fichier)|
|6-8|Dakos, p. 19, 21, 31|✓|
|6-8|Benaych-Georges et Nadakuditi, Wigner déformée, p. 11|✓|
|6-8|Lakatos, I p. 12 et 15, II p. 130|✓|
|6-8|Chen 2004, « does not include any algorithms to detect such nodes computationally »|✓ (page web)|
|10|Hatcher, propositions 1.31 à 1.33 p. 61, théorème 1.38 p. 67, proposition 1.39 p. 71, p. 63 et 69|✓ (pages imprimées)|
|10|Milne, *Fields and Galois Theory* 5.10 : 3.17 p. 39, 3.29 p. 45, 5.27 p. 74, 5.34 p. 77|✓|
|10|Milne, *Group Theory* 4.01 : 4.33 p. 69, 6.2 p. 88|✓|
|10|Milne, *Class Field Theory* 4.03, exemple 1.18 (b), p. 65|✓ (page imprimée ; p. 74 du fichier)|
|10|Etingof et collègues, corollaire 3.7, p. 35|✓|
|10|Krajnović, p. 3 et 5 (325°58′, 326°57′), tableau 2 p. 14 (36,15 ; 30,11 ; 0,00011 ; 0,0000515), p. 12|✓|
|10|Constantin, 38,3″ par siècle, p. 1 ; Hall, 43″ et exposant 2,00000016|✓|
|10|Will 2014, p. 45 (Vulcain, anneau, quadrupôle, loi de puissance écartés)|✓|
|10|Berche et Medina, tableau 3 p. 15 (43,11 ± 0,45 ; 8,4 ± 4,8 ; 5,0 ± 1,2)|✓ (source seconde, signalée)|
|10|Bridgman, p. 7 à 10 (1868, 1895, 1927-1928, 1942, gaz nobles)|✓|
|10|Brown, p. 23-24 (« without giving up the energy theorem », Bohr contre Pauli)|✓|
|10|Gannon, p. 1, 2, 3, 5, 6, 19|✓|
|10|Borcherds, théorème 1.1|✓|
|10|Collaboration OPERA, 73,2 ns, câble mal connecté, p. 18|✓|
|10|Batygin et Brown, 0,007 %, au moins dix masses terrestres, p. 1|✓|
|10|Falkenhainer, Forbus et Gentner, entité hypothétique, p. 22 ; exemple p. 35|✓|
|10|Silva et collègues, tétrades, p. 194 et 199|✓|
|10|Kim et Leskovec, nombre de nœuds manquants supposé connu, p. 3|✓|
|10|Abramsky, Mansfield et Barbosa, obstruction suffisante non nécessaire, p. 1|✓ (portée : m17)|
|10|Banc DiscoverPhysics, échecs sur les structures latentes, p. 3 et 9|✓|

## 3. Points bloquants

Aucun.

## 4. Points majeurs

**M1. Partie II, verdict (l. 134) et section 1 (l. 147-151) : l'aire 0,998 est presque une identité du jouet, et l'opposition « mollesse = désordre » n'est pas établie hors de lui.**
*Preuve.* Dans la partie E du script, les anomalies plantées viennent d'une seule bipartition, la classe de restructurations éprouvée est exactement celle des bipartitions, et le jumeau, comme le nul de placement, met le même nombre d'anomalies au hasard. La part compressible `1−E_min/E_0` est alors la statistique de vraisemblance du générateur : elle sépare par construction. Les trois autres grandeurs sont basses dans la région plantée parce qu'une région équilibrée est rigide par construction (optimum unique). Le jouet ne contient jamais deux restructurations rivales. Or la réponse cite elle-même Kuhn : en crise, « the proliferation of competing articulations » (p. 91 ; « versions », p. 71). Une dégénérescence haute, avec plusieurs restructurations presque aussi bonnes, est donc *aussi* un signe de crise. Le verdict (« désigne le désordre », « la bonne grandeur … aire 0,998 ») généralise ce que le jouet ne peut pas départager.
*Correction.* Dans le verdict, écrire « dans un jouet où la classe de restructurations est celle du générateur ». Ajouter au monde planté un bras à deux distinctions rivales presque aussi bonnes (crise simulée), où la dégénérescence devrait *monter* dans la région féconde. Garder les trois grandeurs comme hypothèses rivales au test daté, non comme bases réputées perdantes.

**M2. Partie II, verdict (l. 134) et section 3 (l. 176) : un seuil avec hystérésis présenté comme fait.**
*Preuve.* Le verdict écrit « Entre anomalies et ouverture, le lien est un seuil avec hystérésis », et la section 3 répond « Non : un seuil ». Or ce seuil est une propriété du modèle de champ moyen *posé* à la section 4, que la section 4 elle-même range sous « transposé par analogie, non démontré » (l. 191) et la section 7 sous « une analogie » (l. 231).
*Correction.* « Dans le modèle de champ moyen, le lien est un seuil avec hystérésis ; sur données, non mesuré. »

**M3. Partie II, section 5, « Gel » et section 2, tableau (l. 159-161, 196) : fuite possible par la normalisation des entités.**
*Preuve.* La demande exige une extraction « sans modèle de langage postérieur à la date de gel », et la réponse assure « sans modèle postérieur au gel ». Mais PubTator 3 et SemMedDB livrent des entités normalisées sur les versions récentes des vocabulaires (MeSH, métathésaurus médical unifié), et PubTator 3 extrait ses relations avec des modèles récents. Les identifiants de descripteurs créés, scindés ou déplacés après `t`, c'est-à-dire l'issue même du test, entreraient ainsi dans les prédicteurs à `t`.
*Correction.* Renormaliser chaque relation sur la version de MeSH valide en `t`, ou retirer tout descripteur et tout lien de hiérarchie postérieurs à `t`. Dire quel extracteur et quelle version sont admis. Ajouter un témoin de fuite : la mesure calculée sur des régions dont l'issue est permutée doit tomber au hasard.

**M4. Partie II, section 5, « Puissance » (l. 204) et script G : la puissance n'est pas celle de la règle de décision.**
*Preuve.* La partie G éprouve « aire > 0,5 » au seuil unilatéral de 5 %, avec des classes équilibrées (125 + 125 pour 250 régions) et sans effets fixes. La prédiction exige au contraire une borne basse au-dessus de 0,55 *et* un gain d'au moins 0,05 sur la meilleure base. Et l'issue « descripteur créé, scindé, fusionné ou déplacé en dix ans » est sans doute fréquente dans un sous-arbre de MeSH : classes déséquilibrées, taux de base à mesurer. Les « 0,86 pour 250 régions à 0,60 » surestiment donc la puissance du test écrit.
*Correction.* Refaire la puissance pour la règle exacte (borne basse > 0,55, gain apparié sur la base, effets fixes par champ, taux de base de l'issue mesuré sur des versions passées de MeSH). Envisager d'exclure la simple création de descripteur de l'issue principale.

**M5. Partie II, section 1, « Lecture » et nœud 3 (l. 149-151, 244) : glissement de la notation de l'étroitesse.**
*Preuve.* L'erratum des notations fixe l'étroitesse comme la réponse à une perturbation locale des appariements φ. La réponse appelle « puits étroit au sens de la note » l'unicité de l'optimum dans le paysage des *restructurations* σ (affectations de rôles), qui ne sont pas des appariements. La conjecture 7 de la partie I (profondeur et étroitesse vont ensemble) en devient ambiguë.
*Correction.* Écrire « rigidité de la restructuration σ », et réserver « étroitesse » à φ. Ou bien montrer que σ induit un φ et dire laquelle des deux on perturbe.

**M6. Réponse à la question 10, en-tête « Longueur » (l. 11) : 4 508 mots déclarés pour 3 500 au plus, sans signaler l'écart.**
*Preuve.* La demande dit « en 3 500 mots au plus, énoncés et démonstrations compris ». Mon compte du « Verdict » aux « Nœuds pour Lazar » donne 4 672 mots en locale UTF-8, soit un tiers de plus. L'en-tête donne le compte sans le comparer à la borne.
*Correction.* Signaler l'écart en tête, ou réduire, par exemple en renvoyant l'énoncé 6 et une partie des cas historiques en annexe.

**M7. Réponse à la question 10, en-tête « Lus » (l. 7) et section 7 : pièces demandées non lues, Laudan absent, Carbon jamais discuté.**
*Preuve.* La demande impose de lire `complement-questions-8-9-et-corrections-note-v1.md`, la réponse à la question 5 (section 7) et la réponse de Carbon sur le méta-espace (sections 2 et 3 : homomorphismes frustrés, symbole-réservoir). Aucune ne figure dans la liste des pièces lues, et le mot « Carbon » n'apparaît nulle part dans la réponse. Or l'« amorçage » de Carbon (`reponse-carbon-meta-espace-v1.md`, l. 48) adjoint « un symbole-réservoir défini par les seules relations requises pour annuler l'obstruction » : c'est l'énoncé 1 (le profil est le rôle) et l'énoncé 4 (extension) sous un autre nom. Laudan, nommé à l'item 7 de la demande, manque aussi de l'antériorité.
*Correction.* Lire ces pièces. Confronter les énoncés 1 et 4 au symbole-réservoir de Carbon (accord, et ce que les énoncés ajoutent : unicité à isomorphisme près, non-injectivité). Ajouter Laudan, marqué « à vérifier ».

**M8. Réponse à la question 10, énoncé 2, « Traduction » (l. 53) : « il n'en reste qu'un plus grossier, dans le quotient de G par le sous-groupe normal qu'engendre Hol » est faux pour un groupe non commutatif.**
*Preuve.* Un attribut à valeurs dans un ensemble `X` sur lequel `G` agit, avec `h(v) = g_e·h(u)`, existe si et seulement si `Hol` fixe un point de `X` (même argument que le point (a)). Contre-exemple : `G` = permutations de trois objets, agissant sur {1, 2, 3}, et `Hol` engendré par la transposition (1 2). Le sous-groupe normal engendré est `G` tout entier, donc le quotient est trivial. Pourtant `Hol` fixe 3, et un attribut à trois valeurs existe. Ce groupe figure dans la vérification (partie A, 14 cas d'holonomie d'ordre 2), qui ne teste pas cette affirmation. La frontière entre attribut caché (T2) et dédoublement (T3) est donc mal placée hors du cas commutatif.
*Correction.* « Les attributs à valeurs dans un ensemble muni d'une action de `G` existent si et seulement si `Hol` y fixe un point, à conjugaison près ; le quotient par le sous-groupe normal engendré n'en est qu'un cas. » Ajouter ce cas à la partie A.

**M9. Réponse à la question 10, verdict 1 (l. 17) : « fixe l'objet manquant à isomorphisme près » sur-revendique l'énoncé 2.**
*Preuve.* L'énoncé 2 détermine à isomorphisme près le *plus petit revêtement* qui rend les transports cohérents, non l'objet manquant. La réponse le dit elle-même (l. 55 et 143) : une relation fausse a la même holonomie qu'un dédoublement, et la forme ne départage pas T3 de T6. L'énoncé 3 non plus : « le groupe donne le plan du recollement, non la nature des feuillets » (l. 63).
*Correction.* « … fixe à isomorphisme près la réparation minimale *d'un type choisi d'avance* (revêtement, extension, module) ; le choix du type reste un choix de modèle. »

**M10. Réponse à la question 10, nœud 2 (l. 159) : la thèse reformulée est réfutée par le jumeau de la réponse elle-même.**
*Preuve.* La reformulation dit : « la forme prédit le type quand le résidu a plus de dimensions que la famille rivale la moins contrainte ». Or dans le jumeau de la partie D, le résidu a six dimensions et les familles rivales un ou deux paramètres, et l'exactitude vaut 0,53 (puis 0,50). La règle répond « loi » 571 fois sur 600, parce que les deux familles coïncident.
*Correction.* Ajouter la condition manquante : « … et que les familles rivales ne se recouvrent pas sur les corps d'épreuve disponibles (distance entre familles au-dessus du bruit) ».

**M11. Réponse à la question 10, section 5, « Volet 0 » (l. 128) et verdict 2 : l'épreuve ne pouvait guère mourir, et ses témoins faux meurent par construction.**
*Preuve.* Dans `MODELES` (script, l. 503-508), les familles candidates sont exactement les génératrices, et leurs pentes sont séparées (−3,5 ; +1,5 ; −1,5 ; −2,5). Atteindre le critère de mort (0,60 ou moins avec quatre corps) était presque impossible. Les témoins faux tombent au hasard par construction. Avec un corps, `ln K = 0` annule toute pénalité, tous les ajustements sont exacts et le tirage départage : 0,5 assuré. Dans le jumeau, les deux familles coïncident et la pénalité tranche toujours pour la loi : 0,5 assuré sur des classes équilibrées. Ni l'un ni l'autre ne pouvait détecter une fuite. Enfin, la demande dit du test « Tu décris ; tu ne lances rien », et le volet 0 a été lancé sans que l'écart soit signalé. La partie E de la question 8 relève du même écart (« prototype »).
*Correction.* Signaler l'écart à la demande. Dans le verdict, écrire « 0,997 dans un monde où les familles sont connues et séparées : ce n'est pas une épreuve de la thèse ». Ajouter un bras mal spécifié (famille génératrice absente des candidates) et un témoin de fuite qui *pourrait* échouer, par exemple un bruit dont la loi dépend du type.

**M12. Partie I, énoncé 5, contre-exemple (i) (l. 75) et section 5 (l. 95) : paramètres cachés et « coûts de Carbon » inexacts.**
*Preuve.* La partie F3 du script prend une sensibilité de 0,90 pour les idées ordinaires (et non le `q_o = 0,75` dont la section 5 tire « `α_o < 0,74` »), une part de profondes `π_d = 0,004` et un coût de génération `c_g = 0,05` *en plus* du coût de filtre `c_f = 0,05`. Chez Carbon (section 2.1), le seul coût par candidat vaut 0,05. Le texte ne dit aucun de ces choix. Or le « 13,3 » et le « 1,5 » en dépendent.
*Correction.* Écrire les paramètres de F3 dans le texte. Remplacer « aux coûts de Carbon » par « coûts inspirés de Carbon, plus un coût de génération de 0,05 ».

## 5. Points mineurs

- **m1. Partie I, section 1 (l. 30) et énoncé 1 (l. 67), Weitzman.** La forme close `z = V−c/p` est l'équation 8, p. 12 du rapport (p. 16 du fichier), non la p. 7. La règle de Pandore est énoncée p. 10 (p. 14 du fichier), non p. 6-7, où l'on lit l'exemple alpha-oméga et la récurrence (2). *Corriger* les pages ; l'équation 7, p. 9, est juste.
- **m2. Partie I, énoncé 6 (d) (l. 77).** Le théorème 4 de Hamilton et Pryadko porte sur la percolation *de sites* (résumé et conclusion, p. 1 et 5). Le contre-exemple du réseau triangulaire porte sur la percolation *de liens* (seuil exact 0,3473). La borne basse pour les liens est soutenue par Karrer et collègues (p. 1), non par Hamilton et Pryadko. *Écrire* « de sites » et attribuer la borne pour les liens à [24].
- **m3. Partie I, énoncé 6 (c) (l. 77) et référence 22.** Le critère biparti est à la p. 12 du fichier (« f0″(1)g0″(1) = f0′(1)g0′(1) ») ; les p. 1 et 3 ne font qu'annoncer le cas biparti. *Citer* la p. 12 et écrire la ligne qui en déduit `c_A·c_B = 1` pour des degrés de Poisson.
- **m4. Partie I, erreur relevée 3 (l. 60).** « La version pondérée n'y figure pas (à vérifier ailleurs) » : Hamilton et Pryadko affirment, sans preuve, que leurs résultats « can be easily extended » à la percolation non uniforme (p. 5). *Le dire.*
- **m5. Partie I, énoncé 6, « Dans le modèle de Fable » (l. 77).** « Il faut `M_φ ≥ 50` » donne `n = 1` à `M_φ = 50`, cas d'extinction certaine que l'erreur relevée 4 reproche justement à Fable. *Écrire* `M_φ > 50`.
- **m6. Partie I, énoncé 4 (a) (l. 73).** « Égalité si et seulement si `H` est constant » ne vaut que pour `n ≥ 2` ; à `n = 1` l'égalité est toujours vraie. *Ajouter* « pour `n ≥ 2` ».
- **m7. Partie I, énoncé 4 (d).** La sous-modularité et la croissance de l'espérance du maximum supposent des valeurs positives ou nulles et une valeur nulle pour l'ensemble vide. *L'écrire* dans les hypothèses.
- **m8. Partie I, corollaire de l'énoncé 5.** Le seuil `q_d > (c_g+c_f+u·c_v)/(c_g+c_v)` suppose un taux de passage `u` inchangé quand on regarde la strate profonde (strate négligeable dans le flux). *Le dire.*
- **m9. Partie I, erreur relevée 2 (l. 59).** Le jugement est juste : la table de Carbon le contredit elle-même, puisque le filtre « faible » (`α_o = 0,25 > π₀ = 0,04`) passe de 0,36 à 0,94. Mais le « critère exact » invoqué, l'énoncé 5, est celui d'un modèle à flux et coût par unité. Dans le modèle de Carbon, à candidats fixés et épreuves plafonnées à neuf, le filtre aide dès que la précision dépasse `π₀`, c'est-à-dire dès que `q_o > α_o`, tant que les promus dépassent la capacité. *Donner* les deux critères.
- **m10. Partie II, section 1, « Lecture » (l. 149).** Les « logarithmes 0,00 ; 0,42 contre 1,76 » comptent les seuls optimums (`E = E_min`), alors que la dégénérescence définie au tableau et utilisée pour l'aire compte les états « à une anomalie de l'optimum » (0,85 ; 2,00 ; 4,50 dans la sortie). *Dire* laquelle est citée, ou citer la seconde.
- **m11. Partie II, section 1 et script E.** L'écart réduit au nul (4,84 ; minimum 2,47) repose sur 8 placements par graphe, avec l'écart type de population. C'est trop peu pour un écart réduit stable. *Préférer* un rang sur au moins 200 placements, ou rapporter la valeur p empirique.
- **m12. Partie II, section 2, résultat (i) (l. 164).** « Autant dans le jumeau permuté » est une identité : le jumeau permute les mêmes entrées, et le script l'écrit (« mêmes entrées »). Seule la comparaison au bruit seul (3 620) informe. *Le dire.*
- **m13. Partie II, section 2 (l. 164).** Baik, Ben Arous et Péché [53] traitent des matrices de covariance (lu : résumé seul) ; la formule `θ + 1/θ` d'une matrice de Wigner déformée vient de [54, p. 11]. *Citer* [54] seul pour ce chiffre.
- **m14. Partie II, section 5, « Réserve » (l. 199).** « La rubrique 13F60 a été créée quand 17 notices … étaient déjà dispersées » : la réponse à la question 9 (l. 90) et son erratum 2 (point 2) laissent la date de création de 13F60 « à vérifier » (révision de 2010 probable). *Reporter* la réserve.
- **m15. Partie II, sections 1 et 6.** Le nom proposé, « part compressible des anomalies » (`1−E_min/E_0`), est une normalisation de l'indice de frustration. Des normalisations voisines existent (degré d'équilibre de Cartwright et Harary, p. 288 ; indice de frustration normalisé d'Aref et Wilson, 2018, *à vérifier*). Voisin possible de la prédiction par la structure : Chen 2012, « Predictive effects of structural variation on citation counts » (*à vérifier*). *Citer* ces voisins avant de proposer le nom (nœud 3) ; la question reste ouverte (règle R8).
- **m16. Réponse à la question 10, limite 2 (l. 87) : homonymies proscrites par l'erratum des notations.** `κ` y désigne la fréquence radiale (« `κ² = 3g/a + g′(a)` », « `Ω − κ` »), alors que κ n'a qu'un sens dans le dossier. `ρ` y désigne à la fois le résidu (section 1) et une densité (limite 1), et `Φ` à la fois l'application des formes vers les types et le noyau newtonien. *Renommer*, par exemple `ω_r` pour la fréquence radiale, `μ` pour la densité, `G_N` pour le noyau.
- **m17. Réponse à la question 10, section 3, tableau (l. 94).** « Hors des groupes, l'obstruction cohomologique est suffisante mais non nécessaire » : Abramsky, Mansfield et Barbosa (p. 1) le disent de *leur* obstruction (cohomologie de Čech à coefficients entiers du préfaisceau des supports), non « hors des groupes ». *Reprendre* leur formulation.
- **m18. Réponse à la question 10, énoncé 1 (b) et (c) (l. 35).** (b) n'est vrai que si « porte exactement ce profil » interdit aussi toute relation avec les nœuds *hors* de l'image. Sinon (c) fournit deux comblements non isomorphes. Énoncé 1 et énoncé 6 : il manque le contre-exemple « quand une hypothèse tombe » que demande l'item 2 (pour l'énoncé 6, la caractéristique `p`, où le caractère ne détermine plus la représentation). *Préciser* (b) ; *ajouter* les deux contre-exemples.
- **m19. Réponse à la question 10, sections 4 et 7.** (a) Neptune (l. 114) : « la dégénérescence entre masse et distance (limite 1) » mélange deux choses. La limite 1 dit que le champ extérieur ne fixe pas la répartition *interne* d'une masse. Le couple masse-distance d'un perturbateur extérieur est une autre dégénérescence, d'ajustement d'orbite. *Retirer* le renvoi à la limite 1. (b) Cases vides : le décompte « trois réussies, onze autres moins bien » sert à corriger le directeur (erreur relevée 6) alors qu'il vient d'une notice non lue (référence 12, **N** et **V**). C'est contraire à la règle R7. *Le retirer* de l'erreur relevée, ou le dire « à vérifier ». (c) La demande veut, cas par cas, le risque que le cas soit cité parce qu'il a réussi, et un cas ouvert *parmi les cas* : l'un et l'autre sont renvoyés au bilan et au volet 2. *Ajouter* une colonne. (d) L'en-tête des références dit « les pages sont celles du fichier » ; pour Hatcher et Milne (*Class Field Theory*) ce sont les pages imprimées (p. 65 imprimée = p. 74 du fichier). *Corriger* l'en-tête.
- **m20. Les deux réponses, en-têtes, annexes et scripts : traçabilité.** (a) Les annexes renvoient aux PDF du bloc-notes (`/tmp/…/scratchpad/pdf-q6-q8/`, `…/pdf-q10/`), qui n'est pas durable. Les fichiers sont maintenant sous `docs/sources/pdf/q6-q8-2026-11-28/` et `…/q10-2026-11-28/`, aux mêmes empreintes : *renvoyer* à ces chemins. (b) Les scripts finaux portent le même nom `-v1` que les scripts partiels de `partiel-fable-q6-q8-coupe-quota-v1/`, de contenu différent (`ba598160…` et `bc6423c4…` contre `5c57a810…` et `cb69ac93…`). C'est contraire à la règle R12 : *nommer* les finaux `-v2` par erratum, ou le signaler. (c) « Critères de mort écrits avant la première exécution » (question 10, en-tête et script) : ce n'est pas vérifiable, puisque le script n'a été ni scellé ni committé avant l'exécution. *Sceller* l'en-tête des critères avant de lancer, la prochaine fois. (d) Le script de la question 10 dit du jumeau que les familles « coïncident par construction », la réponse (l. 128) qu'elles donnent « presque la même pente ». *Aligner* les deux.

## 6. Les erreurs relevées chez Fable et Carbon : jugement

|Erreur relevée|Vérification|Jugement|
|---|---|---|
|Carbon, « théorème de rendement décroissant », hypothèse munie d'un optimum (partie I, 1)|Carbon pose `V_réel(E)` (section 2.3), puis dérive `E*`. J'ai refait `E* = ln(κP_maxλ/((1−κ)p_baseτ))/(λ−τ)`, et `E* = 108,6` à `κ = 0,5`.|Juste. Le symbole `kappa` de Carbon (part des classes couvertes) est bien à renommer.|
|Carbon, « tant que `α_o > π₀`, le budget est brûlé » (partie I, 2)|Contredit par sa propre table (filtre « faible »). Plafond `1/π₀` démontré (`u ≥ π₀·q`).|Juste ; le critère de remplacement est à adapter au modèle de Carbon (m9).|
|Carbon, seuil spectral pondéré (partie I, 3)|Karrer et collègues : occupation uniforme. Hamilton et Pryadko : extension non uniforme affirmée, non prouvée (p. 5).|Juste en substance (m4).|
|Fable, « avalanche si `n ≥ 1` » (partie I, 4)|`reponse-fable-max-v1.md`, l. 47 : « avalanche si `n≥1` ». À `n = 1`, extinction presque sûre.|Juste ; la réponse refait la même faute (m5).|
|Pistes du directeur, question 10, erreurs 1 à 7|1, 2, 3, 4, 5 et 7 sont vérifiées sur Hatcher, Gannon (p. 6 : « (3.2b) alone certainly doesn't uniquely determine V »), Borcherds, Krajnović (36,15/30,11 = 1,20 ; 0,00011/0,0000515 = 2,1) et Milne.|Justes, sauf l'erreur 6, qui s'appuie sur un chiffre non lu (m19 b).|

## 7. Ce que je n'ai pas vérifié

L'attribution à Fable et Carbon des lignes du tableau « Où Fable et Carbon divergent » (partie I, section 2), sauf les lignes « Conflits » et « Émergence ». La phrase « ce qu'aucune des deux réponses ne dit » (partie I, section 2, (iii)). Les références marquées « notice » ou « résumé », faute de PDF versé. La compilation des deux énoncés Lean de l'annexe A : je les ai seulement relus, et ils sont vrais sous leurs hypothèses (les dénominateurs sont strictement positifs puisque `c_v > 0` et `p0·q > 0`). Les parties B4, C, D (exemples position-échelle) et G3 du premier script n'ont été relues que par leurs sorties et par mes recalculs.
