# Relecture affectée — « Référence hors course » et critères de lecture, course « seuil et moniteurs » — mode « épreuve qui ne peut pas échouer, ou pas réussir » — v1

- Relecteur neuf, hostile et aveugle, 2026-11-21. Mandat : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/reference-hors-course-v1/contre-lecture-v1/mandat-relecteur-reference-hors-course-epreuve-v1.md` (`6771d552e92440214868f72acf5be8064947aaa4a08b07a560b900c67406e429`).
- Pièces relues (empreintes recalculées par moi) : section `section-reference-hors-course-seuil-et-moniteurs-v1.md` (`9fb4e28c75f8184f1ce18f7bd98efbed939fb0a347b91524df4b7eb824f8acbb`) ; critères `criteres-de-lecture-en-vigueur-course-seuil-et-moniteurs-v1.md` (`ea5f224fed794aededf7917caaaee6cb38772de8605725aa3942254d72fa0c27`) ; calculs `calculs-reference-hors-course-v1.py` (`77910593…6802b`, égale à celle que la section cite) et sa sortie (`685045b7…c1c8`) ; texte extrait (`f33888492ac37171da80af7b0161afd82aef48a1bf71211202c2e5e8417210c6`, égale à celle de la section, § 2) ; mandat du concepteur (`4569acaf…7b11`). Sources : arbitrage des six points, point 8 (`44d1e86f…dd06`, par `git show origin/main` redirigé) ; `registres/go.md`, GO-2026-11-21-35 à -37 ; pièce de scellement de la conception (`4286bf39…`) et son erratum 1 (`64e06388…`) ; ordre de course v6 (`208454c5…b940`). Non ouvert : le préenregistrement court v6 (son chemin n'est donné par aucune pièce lue, et je ne liste pas hors de mon dossier).
- Aucun appel, aucune dépense, aucun commit. Aucune autre relecture lue. Ni table de vérité des témoins, ni source de la liste scellée.

## Tête

**Cassé.**

**Pas visé** : section, § 9, ligne « vrai » (garde de la référence), lue avec § 11, arrêt n° 20, et critères, § 9, dernière ligne de la table (« garde de la référence manquée »).

**Preuve.** La garde de l'arrêt n° 20 est déclenchée par « une prédiction de l'objet vrai du § 9 est manquée ». Ces prédictions sont deux intervalles à 99 % par monde, tranche et valeur de m (« l'intervalle à 99 % […] contient cette valeur » ; « son intervalle de Clopper-Pearson la contient »), écrites comme des certitudes. Ce sont des événements aléatoires, qui manquent environ une fois sur cent chacun **sur un générateur parfaitement sain**. Aucune règle de multiplicité n'est écrite. Rejoué (`verif-epreuves-reference-v1.py`, sortie `verif-epreuves-reference-v1.txt`, bloc [1]) :

| ce qui est mesuré, générateur sain, V1★ ~ Beta(k, m + 1 − k) exactement | valeur |
|---|---|
| couverture exacte de Clopper-Pearson 99 % à 2 000 tirages, m = 200 / m = 400 | 0,99061 / 0,99056 |
| rouge d'une cellule (moyenne ou part), m = 200 / m = 400, 20 000 répliques | 0,0181 / 0,0165 |
| rouge d'un couple monde et tranche (m = 200 et 400 joués) | 0,0344 |
| garde rouge au moins une fois : 1 famille continue (3 couples) | 0,100 |
| 3 familles (A, dérive, grappes : le minimum de l'ordre v6, § 7 bis) | 0,270 |
| 4 / 5 / 6 familles | 0,343 / 0,408 / 0,467 |
| 8 / 10 familles (familles libres et tenues à l'écart comprises) | 0,568 / 0,650 |

Les mondes scellés comptent au moins trois familles continues (monde sain, dérive, grappes), plus au moins une des familles C, D, E (ou G, à part), plus une ou deux tenues à l'écart (ordre v6, § 7 bis ; critères, § 6, lignes 11 et 18). **La garde rougit donc, sans aucun défaut, avec une probabilité de l'ordre d'un tiers à deux tiers.** Ce qu'elle déclenche n'est pas anodin : « référence non lisible », incident nommé, audit de symétrie du générateur et de la mesure, et « le rapport d'issue des candidates ne sort pas avant la fin de cet audit » (§ 11, arrêt 20). Son cas sain (règle R5 : vue verte sur un cas sain) n'est vert qu'avec une probabilité de 0,35 à 0,73. C'est une garde qui ne peut pas, de façon fiable, réussir.

Ce qui tient dans la même ligne : le pouvoir de la garde contre un vrai défaut est grand. Sur l'artefact nommé (objet faux, § 9 et § 11), la moyenne de V1★ est à 49 erreurs types de k / (m + 1) à m = 200 et à 70 à m = 400 (bloc [2]) : rouge à coup sûr.

## Cas manquants

1. **Garde de la référence (arrêt n° 20)** : la prédiction de son taux de rouge sur le cas sain, écrite d'avance, et la règle qui dit combien de prédictions manquées font une garde manquée parmi les 2 × (nombre de couples monde et tranche) × 2 intervalles joués. Sans elle, l'issue « garde verte » du cas sain n'est pas écrite d'avance : elle est seulement espérée.
2. **Témoins « doit mourir » dont la valeur vient des mondes** (critères, § 5 : T09, T10, T14, T17 ; § 6, ligne 14 : témoins libres). La sorte « doit mourir » est donnée par le signe de la valeur vraie contre le seuil (« sort calculé »), sans aucune marge de détectabilité à 2 000 tirages et 99 %. Rejoué (bloc [3]) : sous garantie « en moyenne » (écart type par tirage de l'ordre de Beta(3, 298), 0,0057), un taux vrai moyen de 0,0102 ne meurt que 16 fois sur 100, 0,0104 que 71 fois, et il faut 0,0105 pour passer 0,9 ; sous « confiance dite » à 5 %, une part vraie de 0,060 ne meurt que 27 fois sur 100, et il faut environ 0,070 pour passer 0,88. Un « doit mourir » qui survit déclare **l'épreuve morte** (critères, § 4, point 1 ; arrêt n° 16). T14 est le cas écrit : « attendue "morte, invalide" si le gonflement partiel suffit » ; s'il suffit de peu, l'épreuve meurt par manque de puissance, non par défaut de la mesure. L'angle mort existe pour les engagements « certifié à 95 % » (ordre v6, § 7 bis : témoins « de marge »), mais aucune règle ne range en « de marge » un témoin fourni par les mondes qui tombe dedans, ni n'en définit l'analogue pour « en moyenne » et « à tout instant ». De plus, la sorte de T14 n'est pas fixée : s'il sort « tient » au recalcul, on ne sait pas s'il entre dans W (critères, § 4, point 2).
3. **Arrêt n° 21** (« aucun score du suspect dans l'étalonnage d'un seuil ») : ni artefact, ni cas sain nommés, et aucun mécanisme qui le détecte pour la base, la référence ou une grandeur du noyau. La phrase générale du § 11 (« chaque garde s'éprouve sur un cas sain et sur un artefact ») ne nomme d'artefact que pour les arrêts 19 et 20. Telle qu'écrite, cette garde ne peut pas rougir.
4. **Ligne « monde à valeurs répétées » de la garde** (§ 9, deuxième ligne) : épreuve unilatérale sans artefact où elle doit rougir (par exemple une décision à inégalité large sur des ex æquo). L'objet faux ne diffère de l'objet vrai que dans la famille à dérive ; sur la famille à valeurs répétées, rien ne montre que cette ligne peut rougir.
5. **Épreuve d'invariance** des candidates « seuil recalé sur le flux du suspect » (critères, § 9) : aucun témoin rouge ni vert. La pièce le dit (« tant que cette épreuve […] n'est pas écrite et contre-lue, la marque n'est pas posée ») ; c'est noté, non reproché.

## Ce qui tient, dans ma question

- Objet faux (§ 9, ligne « faux ») : la mort « invalide, en moyenne » tombe dans 2 000 répliques sur 2 000 aux deux valeurs de m, sous loi normale (bloc [2] : moyenne 0,02892 et 0,02943, égales au bloc [D] du concepteur). Prédiction écrite d'avance ; puissance suffisante.
- Valeurs « sans loi » des témoins imposés : le programme du concepteur rejoué rend une sortie d'empreinte identique (`685045b7…c1c8`). Les parts 0,5954 et 0,5675 de la garde sont retrouvées par une autre voie (bloc [1]).
- Témoins « doit tenir » au bord exact : T02 meurt avec la probabilité 0,0031, T03 avec 0,0023 (bloc [3] (c)) : sous 0,005, comme la borne c(W) le suppose.
- Issues attendues écrites d'avance pour seize témoins imposés sur dix-sept ; T14 est le seul dont l'issue n'est pas écrite (voir cas manquant 2).
- Cas de bord m = 98 : prédiction écrite (« abstention ») et rejouée (bloc [C] du concepteur : k = 0).

## Relevé de méthode

### Chaîne de raisonnement

1. La garde n° 20 rougit si « une prédiction de l'objet vrai du § 9 est manquée » ; ces prédictions sont, par monde à scores continus, tranche et m, l'inclusion de k / (m + 1) dans l'intervalle de Student à 99 % de la moyenne de V1★ et l'inclusion de P(Bin(m ; 0,01) ≥ k) dans l'intervalle de Clopper-Pearson à 99 % (section `9fb4e28c…`, § 9 et § 11 ; critères `ea5f224f…`, § 3).
2. Pour une loi continue et des témoins de la loi d'usage, V1★ = 1 − F(k-ième plus grand de m) suit exactement Beta(k, m + 1 − k) (statistique d'ordre de lois uniformes ; calcul rejouable, bloc [1]).
3. Un intervalle à 99 % calculé sur 2 000 valeurs indépendantes manque sa valeur vraie avec une probabilité voisine de 0,01 ; mesuré : 0,0107 et 0,0103 (Student), 0,00939 et 0,00944 (Clopper-Pearson, exact) (bloc [1]).
4. Aucune règle de multiplicité n'est écrite dans la section ni dans les critères (lecture des deux pièces entières, pas 1).
5. Par cellule, l'une ou l'autre prédiction manque avec 0,0181 (m = 200) et 0,0165 (m = 400) ; par couple monde et tranche, 0,0344 (bloc [1]).
6. Le nombre de couples est d'au moins 9 (trois familles continues imposées, trois tranches), plus vraisemblablement 12 à 30 (ordre `208454c5…`, § 7 bis ; critères, § 6, lignes 11, 14 et 18 ; section, § 6). Les tirages de couples différents sont indépendants (section, § 5, « graine […] par monde, tranche, m et tirage ») ; supposé : que l'indépendance des graines vaut indépendance des tirages.
7. Donc P(garde rouge | générateur sain) va de 0,27 à 0,65 selon le nombre de familles (pas 5, 6 ; bloc [1]).
8. La garde rouge bloque le rapport d'issue des candidates jusqu'à la fin d'un audit (section, § 11, arrêt 20). Son cas sain n'est donc pas vu vert de façon fiable : R5 n'est pas tenue pour cette garde (CLAUDE.md, R5).
9. Sur l'artefact nommé (objet faux), l'écart à k / (m + 1) est de 49 et 70 erreurs types (bloc [2]) : la garde y rougit ; ce côté tient.
10. Pour un témoin « doit mourir » fourni par les mondes, aucune pièce lue n'exige une marge de détectabilité (critères, § 4, § 5, § 6 lignes 13, 14, 18 ; ordre, § 7 bis) ; la probabilité de mort à 2 000 tirages et 99 % tombe à 0,16 pour un taux moyen vrai de 0,0102 et à 0,27 pour une part vraie de 0,060 contre 0,05 (bloc [3]).
11. Un « doit mourir » qui survit rend l'épreuve morte (critères, § 4, point 1) ; T14 est explicitement au bord (« si le gonflement partiel suffit », critères, § 5).
12. Arrêt 21 : aucune pièce lue ne nomme son artefact, son cas sain ni son mécanisme de détection (section, § 11 ; critères, § 9).

### Objets de contrôle

Mécanisme éprouvé : mon programme de vérification, qui mesure le taux de rouge d'une garde par intervalles.
- Objet où « la garde rougit » est **faux par construction** : générateur sain, V1★ ~ Beta(k, m + 1 − k) exact. Prédit d'avance : chaque intervalle manque environ 1 fois sur 100, Clopper-Pearson un peu moins (méthode conservatrice). Rendu : 0,0107 / 0,0103 (Student) et 0,00939 / 0,00944 (Clopper-Pearson exact). Conforme.
- Objet où « la garde rougit » est **vrai par construction** : l'objet faux de la section (témoins de la loi de calibration, usage sous dérive de 0,4456 écart type). Prédit d'avance : rouge à coup sûr et moyenne égale au bloc [D] du concepteur. Rendu : 49 et 70 erreurs types ; moyennes 0,02892 et 0,02943, égales à [D]. Conforme.
- Contrôle de la fonction de puissance : à un taux vrai égal au seuil (0,0100), elle doit rendre 0,005 ; elle rend 0,0050 (bloc [3] (a)).

### Premier pas non justifié

Pas 6 : le nombre de couples monde et tranche n'est fixé qu'au scellement des mondes, et l'indépendance des tirages entre couples est supposée depuis la règle de graines. Le justifierait : la liste scellée des familles retenues et le code du générateur. La conclusion ne dépend pas de ce pas au-delà de son ordre de grandeur : même une seule famille continue donne 0,100 (bloc [1]).

### Mode d'échec affecté

Épreuve qui ne peut pas échouer, ou pas réussir. **Cassé** au pas visé ci-dessus (garde de la référence, arrêt n° 20) : sur un cas sain, elle rougit avec une probabilité de 0,27 à 0,65. Cas manquants : 1 (taux de rouge du cas sain et multiplicité), 2 (marge de puissance des « doit mourir » fournis par les mondes ; sorte de T14), 3 (arrêt 21 sans artefact ni cas sain), 4 (ligne « valeurs répétées » sans artefact), 5 (épreuve d'invariance, que la pièce reconnaît non écrite).

### Trouvaille de côté

- Borne c(W) (critères, § 4, point 2) : calculée en supposant les morts de témoins « doit tenir » indépendantes. Si des témoins partagent les mêmes tirages de calibration (appariement, section § 5), la borne peut être dépassée : W = 30 en quinze paires liées donne 0,072 au lieu de 0,01 (bloc [4]). Non poursuivi.
- La borne c(W) ne compte que les morts « invalide » au bord (taux 0,005) ; un « doit tenir » peut aussi mourir « sans gain », avec une probabilité qui n'est pas bornée par 0,005. Pour T13 (monde du déploiement), je n'ai trouvé dans les pièces lues ni la base ni la taille de calibration (400) contre lesquelles se lirait sa mort « sans gain ». Non vérifié dans le préenregistrement court v6, que je n'ai pas ouvert.
- T07 (la base contre elle-même) : écart apparié nul à chaque tirage, donc écart type nul ; l'intervalle de Student y est dégénéré. Le programme de mesure doit le traiter comme « borne basse = 0 », non comme une division par zéro.

### Évaluateur et conseil

Ma pièce est jugée par la mère, puis par le concepteur au retour, sur pièces : mon programme et sa sortie sont rejouables (`verif-epreuves-reference-v1.py`, `43124c214f7f7c4b2d90d99e092cdb70e49cd175ee0b7e068c4e08debed546d6` ; sortie `822e3c76357cf02269069a566c1b3615449d55f0cc261a5cbfc88028d8052d2d` ; numpy 2.5.3, graine `SeedSequence(20261121)`). Il est admis sur les objets de contrôle ci-dessus, non contre-lu. Par où ma pièce pourrait être bien jugée sans le mériter : si les familles retenues étaient moins nombreuses que trois, le chiffre baisserait (0,100 pour une) ; l'erreur de Monte-Carlo sur 0,018 est de l'ordre de 0,001 à 20 000 répliques ; le quantile de Student est pris par développement en série (2,5783 à 1 999 degrés de liberté), non par une table.
