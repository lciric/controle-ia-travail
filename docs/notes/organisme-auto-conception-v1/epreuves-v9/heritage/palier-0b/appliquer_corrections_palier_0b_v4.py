"""Produit la version 4 (erratum de conception) du préenregistrement du palier 0b par remplacements exacts sur la version 3.

Usage : python3 -I -B appliquer_corrections_palier_0b_v4.py CHEMIN_V3 CHEMIN_V4 HEURE_FIN
Chaque chaîne cherchée doit être trouvée une seule fois ; sinon le programme s'arrête sans rien écrire.
Aucun tirage, aucun réseau. La version 3 n'est jamais modifiée (R12) ; la cible ne doit pas exister.
"""
import hashlib
import sys
from pathlib import Path

EMPREINTE_V3 = "a4535a67e99cd0babfb580a731868c0670ffab55be803b8aa7979f3ded84ebc6"
GO = "`GO-2026-11-19-84`"
DOSSIER_DEV = "`palier-0b/code-v1-inacheve-arrete-refus-outil-20261119/`"
COPIE = "`docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/`"

REMPLACEMENTS = [
    # --- en-tête ---------------------------------------------------------------------------------------------------------
    ("en-tête, titre", "aucun appel de modèle — v3\n", "aucun appel de modèle — v4\n"),
    (
        "en-tête, version",
        "aucun code d'analyse n'existe encore. **Version 3 (erratum)** : elle remplace la version 2 (",
        "aucun code employable n'existe encore. **Version 4 (erratum de conception)** : elle remplace la version 3 "
        "(`palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v3.md`, `" + EMPREINTE_V3 + "`), qui reste "
        "intacte (règle R12). Elle tranche par écrit, avant tout tirage, cinq points que le développeur du code a trouvés "
        "impossibles à coder à la lettre, un sixième de même nature, et inscrit les silences qu'il a comblés (annexe F). "
        "**Aucun des six critères, aucun seuil chiffré, aucune valeur de la table des valeurs gelées, aucune issue n'est "
        "changé.** Sont changés : la construction du générateur des mondes (B1), la définition de M12 et ce que la couche "
        "statistique en reçoit, la conduite des proposeurs dans la course source, le balisage de la description, et les "
        "traits de l'audit de présentation, qui devient plus sévère à seuil égal. La version 3 (erratum) remplaçait la "
        "version 2 (",
    ),
    (
        "en-tête, dates",
        "version 3 de 22:00Z à 22:03Z environ (`date -u`)",
        "version 3 de 22:00Z à 22:03Z environ, version 4 de 22:50Z à @HEURE_FIN@ environ (`date -u`)",
    ),
    (
        "en-tête, commit du code",
        "- Commit du code d'analyse : **aucun à ce jour.** Le code s'écrit après la contre-lecture de ce texte (annexe C).",
        "- Commit du code d'analyse : **aucun à ce jour.** Le code s'écrit après la contre-lecture de ce texte (annexe C). "
        "Un travail inachevé d'un premier développeur est versé, non employable en l'état (annexe C, annexe F) ; un "
        "développeur neuf le reprend après la relecture de cette version 4 (ligne " + GO + ").",
    ),
    (
        "en-tête, mandat de la version 4",
        "- Mandat de la version 3 : ",
        "- Mandat de la version 4 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/"
        "mandat-redacteur-preenregistrement-palier-0b-v4-erratum-conception-v1.md` "
        "(`64917211a6ebadd774b6d60816daa4d51ca292813a031a1554d1d8f995ebf4ec`, branche `lot/compte-organisme-v1`, "
        "commit `da864e996ae39952819f79ccd71ade30ed62e117`). Ligne d'accord relue sur `main` au commit "
        "`45653e962f835a1e22334f2c7a0279976b280777` (`registres/go.md`, "
        "`edb78e2110c3a09d39cae4355eb56bab9a28a5c9d68362d790f005018ed82d88`) : " + GO + ", mot de Lazar du 19 novembre "
        "vers 22:42Z — reprise après le refus d'outil du développeur, option (a) : erratum de conception du texte du "
        "palier 0b (quatre points, et le lecteur qui ne compose pas ses entrées), relu par le même contre-lecteur, puis "
        "reprise du code par un développeur neuf depuis le dossier versé ; aucune dépense.\n"
        "- Mandat de la version 3 : ",
    ),
    (
        "en-tête, pièces de la version 4",
        "§ 6 ; dit ici « la vérification ».\n",
        "§ 6 ; dit ici « la vérification » ;\n"
        "  - relecture de l'erratum de la version 3, par le même contre-lecteur : "
        "`palier-0b/relecture-erratum-palier-0b-v3-v1.md` "
        "(`43b802baad5cbb91c8a7770d9fc66aeaea9e5fda6c1b4d39ad5bc48336909ef8`) ; dit ici « la relecture » ;\n"
        "  - **travail inachevé du développeur, versé** : " + DOSSIER_DEV + " — LISEZ-MOI "
        "(`d28759a5cb50995fff2159255b98698925e3a2ac5d0d76f91e122ed340b293c5`), inventaire de son bloc-notes "
        "(`96b03c17f5209af4777ae7332290508be977af5b68e547932268f5776f23a3a8`), et, sous "
        "`src/controle_ia/heritage_etage_processeur_v1/` : `mondes.py` "
        "(`92f269612f668feac765c0149ef795b77c7834378d44b817aee8099e74fc5cf7`), `mecanique.py` "
        "(`eee25361e2d94721d1faa0e3319bc3fbad004ddc552cf4ff4db52df25277a95b`), `proposeurs.py` "
        "(`9b369622681be0e7b62cfaad677c40d06aa8b861a3c8a8d4b429118477fdfb89`), `statistique.py` "
        "(`3be4c79d17d75716777ea84d62f45ef79c61539ef6d65307670fc47b85576228`), `registre.py` "
        "(`f10ccdf199aaf111eb4a7947d24055f50cc9c5cefe467c7c38c7e278bd7e8315`), `lois.py` "
        "(`fb24a9eaffdc98ee080db835d77ee2c419242ad4108ef60b440df8f1cb387536`) ; sous `outils-dev/` : "
        "`diagnostic_marges.py` (`4ba71b7fff7e90b0332173d21e45c631082cc4719abc483aa602078a026bb7dd`), "
        "`diagnostic_sous_lois.py` (`4ab6ad2fad3bf11236115c089d9d9689005e7ed443579704bafbe7ad54a1dd5d`), "
        "`essai_equivalence.py` (`f236ece074801c0b775f509ff535db407e61810ae9e2f841d087db5dfd34bcc1`) ; mandat du "
        "développeur : `palier-0b/mandat-developpeur-code-palier-0b-v1.md` "
        "(`9221822842b2fe537d0a9fdb89a6a468694b8a2bc6aa127b691f2bda6c5807b1`) ; dit ici « le dossier versé » ;\n"
        "  - copie du code de l'organisme, au dépôt (même branche) : " + COPIE + " — `tests_de_mort_v2.py` "
        "(`363a3725885da08412f25b28defba7a8d204d883c3637f1de1df83686d93a41a`), `protocole_outils.py` "
        "(`0657eec8e0b1a3d2a3f57f37aad59c34554a2352be4e42ed2c3395e9e94fe2b5`), `a_blanc_v59.py` "
        "(`606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c`).\n",
    ),
    (
        "en-tête, non lus",
        "non d'une lecture du code (réserve 1).\n",
        "non d'une lecture du code (réserve 1). **À la version 4** : une copie du code de l'organisme est au dépôt "
        "(chemin et empreintes ci-dessus) ; le rédacteur n'y a lu que trois passages, pour le point 5 de l'annexe F ; "
        "le reste tient toujours au rapport du palier 0a et à la lecture du développeur. Le rapport de fin du "
        "développeur n'est pas au dossier versé (réserve 21).\n",
    ),
    # --- hypothèse, métriques, seuils --------------------------------------------------------------------------------------
    (
        "hypothèse de travail (iii)",
        "par loi et par type (M12), mesurées sur la couche mécanique, valent pour la couche statistique",
        "par loi, par type et, pour les lois non plantées, par origine de l'engagement (M12), mesurées sur la couche "
        "mécanique, valent pour la couche statistique",
    ),
    (
        "M1, ensemble exclu",
        "(toute loi plantée du monde final appariée à une tentative du registre de la source ; fixé par source",
        "(toute loi plantée du monde final appariée à une tentative du registre de la source, l'appariement étant lu "
        "ici sans égard au domaine que nomme la tentative, ce qui est plus strict ; fixé par source",
    ),
    (
        "M12",
        "par type — loi vraie plantée, loi fausse plantée, loi non plantée (appariée à rien) —, une loi engagée plusieurs "
        "fois sur un même monde comptant une fois, puisque le même engagement sur la même tranche d'épreuve rend le même "
        "verdict ; et, par composition examinée et par monde, le taux de faux passage du criblage (B7).",
        "par type — loi vraie plantée, loi fausse plantée, loi non plantée (appariée à rien) — **et, pour les lois non "
        "plantées, par origine de l'engagement** : recherche de base, composition passée au criblage, copie d'une entrée "
        "du registre (version 4 ; annexe F, point 4). Une loi engagée plusieurs fois sur un même monde compte une fois, "
        "puisque le même engagement sur la même tranche d'épreuve rend le même verdict ; son origine est celle de la "
        "première tentative qui l'engage, dans l'ordre du scellement. Et, par composition examinée et par monde, deux "
        "taux du criblage (B7) : le **taux de passage** des compositions qui sont une loi dépendante du monde en cours "
        "(passée, et retenue sur son propre domaine), et le **taux de faux passage** des autres. Sont rapportées à côté, "
        "sans être servies à la couche statistique : la fréquence regroupée des lois non plantées, toutes origines "
        "réunies (la seule que la version 3 nommait), et la fréquence de « tient » des lois vraies, à part pour les "
        "dépendantes et pour les indépendantes.",
    ),
    (
        "S8",
        "garde un risque global d'alarme à tort de l'ordre de 5 %.",
        "garde un risque global d'alarme à tort de l'ordre de 5 %. **Version 4** (annexe F, point 4) : le fichier gelé "
        "des fréquences porte sept valeurs — « tient » des lois vraies ; des lois fausses ; des lois non plantées de "
        "chacune des trois origines ; passage et faux passage du criblage. La forme de la garde, son niveau et ses "
        "comparaisons ne changent pas. Une strate de M12 sans aucune loi engagée sur la couche mécanique n'a pas de "
        "fréquence : si la couche statistique en a besoin pour un proposeur d'une famille jouée, c'est un arrêt (liste "
        "d'arrêt, point 4), jamais un repli sur la fréquence regroupée. Aucune strate de plus ne s'ajoute sans un "
        "erratum contre-lu.",
    ),
    (
        "marges du générateur, précisions",
        "exactitude équilibrée au plus 0,55 en validation croisée.",
        "exactitude équilibrée au plus 0,55 en validation croisée. **Précisions de la version 4, seuils inchangés** "
        "(annexe F, points 1 et 2). La séparation de deux lois est la plus petite des deux divergences moyennes, d'un "
        "sens et de l'autre, calculée sur les 4 000 instances de l'oracle du monde audité. Le classifieur est le plus "
        "proche centre de classe sur des traits centrés et réduits, en validation croisée à cinq plis, sur les lois des "
        "mondes cibles et finaux de 50 suites par dose, tirées sous la couche de graines « audit » (50 : valeur du "
        "rédacteur). Ses traits sont de deux sortes. *De forme* : les comptes des jetons du texte canonique de la loi, "
        "répartis en 64 cases, tout nombre d'au moins quatre décimales comptant pour un même jeton, et la longueur du "
        "texte. *De contenu* : pour chaque sous-population, la norme des poids, la norme des biais et l'entropie moyenne "
        "de la loi, en nats, sur les instances de l'oracle du monde. Chacun des trois audits — vraies contre fausses ; "
        "dépendantes contre indépendantes, sur les lois vraies des mondes à dose non nulle ; mondes par dose, sur la "
        "moyenne des traits des lois de chaque monde — est lu sur les traits de forme seuls, de contenu seuls, puis "
        "réunis : **neuf exactitudes, chacune au plus 0,55**. Les traits de contenu sont un ajout de cette version : "
        "sous la forme unique des lois (B1), les traits de forme ne varient presque plus et l'audit ne pourrait plus "
        "échouer ; or le générateur constructif (B1) agit sur le contenu.",
    ),
    # --- B1 ------------------------------------------------------------------------------------------------------------
    (
        "B1, épisodes",
        "(trois issues, deux traits, deux sous-populations ; rapport du palier 0a, § 3.3). Seize domaines par monde",
        "(trois issues, deux traits, deux sous-populations ; rapport du palier 0a, § 3.3) : **400 épisodes par domaine**, "
        "la taille de la tranche du tour fermé de l'organisme ; deux traits tirés d'une loi normale centrée réduite, "
        "arrondis à six décimales ; une sous-population tirée à pile ou face (version 4 : le texte ne les chiffrait "
        "pas). Seize domaines par monde",
    ),
    (
        "B1, lois fausses",
        "une loi fausse reprend la loi vraie de son domaine sur une sous-population et s'en écarte sur l'autre.",
        "une loi fausse reprend la loi vraie de son domaine sur une sous-population et s'en écarte sur l'autre. La "
        "sous-population gardée est tirée à pile ou face ; l'autre reçoit une sous-loi neuve (version 4).",
    ),
    (
        "B1, rang",
        "la loi de plus petit rang d'abord.",
        "la loi de plus petit rang d'abord, le rang d'une loi de la source étant l'ordre de son domaine.",
    ),
    (
        "B1, audit, forme unique, générateur constructif",
        "un monde qui manque une marge est rejeté et retiré, et le nombre de rejets est rapporté.",
        "un monde qui manque une marge est rejeté et retiré, et le nombre de rejets est rapporté. **L'audit ne se fie "
        "pas au générateur** : il recalcule, par une fonction qui ne partage rien avec la construction, la séparation "
        "de toutes les paires de lois, loi entière contre loi entière, au seuil inchangé de 0,25 nat.\n"
        "- **Forme unique des lois (version 4 ; annexe F, point 2).** Toute loi plantée — vraie ou fausse, du monde "
        "source ou d'un monde cible, dépendante ou indépendante — et toute loi neuve engagée par la recherche de base "
        "(B7) s'écrit sous **une seule forme** de la grammaire de l'organisme : `par_sous_population`, deux sous-lois "
        "`softmax`, une par sous-population. La composition de deux lois (dose de dépendance, ci-dessus) rend cette même "
        "forme. Les poids d'une sous-loi sont tirés d'une loi normale d'écart-type 1,5 et ses biais d'une loi normale "
        "d'écart-type 0,3, arrondis à six décimales : les valeurs du générateur de lois de l'organisme, selon la lecture "
        "du développeur. Une loi est identifiée par son texte canonique (clés triées, sans espace). Raison : une "
        "composition par sous-population est par nature de cette forme ; si les lois indépendantes s'écrivaient "
        "autrement, une loi dépendante se reconnaîtrait à sa seule forme, et l'audit de présentation échouerait par "
        "construction. Les domaines sans structure ont une loi génératrice fixe, qui n'est ni plantée ni engagée.\n"
        "- **Générateur constructif (version 4 ; annexe F, point 1).** Tirer des lois au hasard puis rejeter le monde "
        "entier ne passe presque jamais : une loi dépendante ne diffère de chacune de ses deux lois mères que sur une "
        "sous-population, une loi fausse de sa loi vraie aussi, deux lois dépendantes qui partagent une mère de même ; "
        "la séparation de telles lois ne tient qu'à une moitié. Le générateur **construit** donc les marges, loi par "
        "loi, à une marge de construction de **0,30 nat** — 1,2 fois le seuil de l'audit, pour absorber l'écart entre "
        "les instances de l'oracle d'un monde et celles d'un autre —, puis l'audit, inchangé, juge à 0,25 nat. "
        "(a) *Monde source* : sur chaque sous-population, huit sous-lois sont tirées une à une, chacune retirée tant "
        "qu'elle n'est pas séparée d'au moins 0,30 nat de toutes les précédentes, la séparation étant ici la part de la "
        "divergence moyenne que porte cette sous-population, c'est-à-dire la séparation de deux lois qui ne diffèrent "
        "que sur elle ; la loi de rang r réunit la r-ième sous-loi de chaque sous-population. (b) *Lois dépendantes* : "
        "composées comme ci-dessus, sans tirage. (c) *Lois indépendantes* d'un monde cible : deux sous-lois neuves, "
        "retirées ensemble tant que la loi entière n'est pas séparée d'au moins 0,30 nat de toute loi déjà posée — lois "
        "vraies de la source, lois dépendantes du monde, lois indépendantes précédentes. (d) *Lois fausses* : la "
        "sous-loi neuve est retirée tant que la loi fausse n'est pas séparée d'au moins 0,30 nat de toute loi déjà "
        "posée, sa loi vraie comprise. (e) *Compositions de la source* : chacune des vingt-huit compositions de deux "
        "lois vraies de la source est séparée d'au moins 0,25 nat de chaque loi vraie de la source, sinon le monde "
        "source est retiré. **Bornes, gelées** (valeurs du développeur) : 400 tirages par loi, après quoi l'essai du "
        "monde est abandonné ; 200 essais par monde ; un monde cible que seules ses lois dépendantes font échouer fait "
        "retirer la suite entière, source et paires comprises, 200 tours au plus ; au-delà, arrêt (liste d'arrêt, "
        "point 2). **Ce que cela change à la loi des lois, dit** : les lois ne sont plus tirées indépendamment les unes "
        "des autres ; elles se repoussent. Une sous-loi proche d'une sous-loi déjà posée est écartée — donc, plus "
        "souvent que les autres, une sous-loi peu tranchée —, et les sortes de lois ne passent pas le même filtre : les "
        "sous-lois de la source, dont sont faites les lois dépendantes, sont filtrées par moitié, entre elles ; les lois "
        "indépendantes et les lois fausses le sont loi entière, contre davantage de lois. **Comment l'audit le "
        "contrôle** : (i) les marges sont rejugées sur le produit fini, au seuil inchangé ; (ii) l'audit de présentation "
        "lit aussi des traits de contenu (section « Seuil »), et une sorte de lois que le filtre aurait rendue "
        "reconnaissable arrête le générateur ; (iii) sont rapportés, par sorte de loi, le taux d'acceptation des "
        "tirages et la distribution des trois traits de contenu, et, par niveau, le nombre d'essais de monde abandonnés "
        "et de tours de suite. Les fréquences M12 et les réglages sont mesurés sur ces mondes mêmes : aucun critère ne "
        "suppose des lois tirées indépendamment.",
    ),
    (
        "B1, réserve de faisabilité",
        "la définition de la composition se change par un erratum contre-lu, avant tout tirage (liste d'arrêt, point 2).",
        "la définition de la composition se change par un erratum contre-lu, avant tout tirage (liste d'arrêt, point 2). "
        "**Version 4** : le développeur a lu la grammaire, et elle admet la composition (type `par_sous_population` de "
        "l'évaluateur de lois de l'organisme ; son essai l'a vu au vert une fois, non relancé depuis).",
    ),
    # --- B2, B3 ----------------------------------------------------------------------------------------------------------
    (
        "B2, réglages de l'étape 4",
        "Taille gelée : 24 sources par dose et par proposeur.",
        "Taille gelée : 24 sources par dose et par proposeur. **Réglages de la mesure des fréquences (version 4 : le "
        "texte ne les disait pas, et l'étalonnage, qui passe par la couche statistique, a besoin des fréquences avant "
        "d'exister)** : à l'étape 4, les proposeurs réglables sont joués au milieu de leur plage — K = 128, τ = 2, "
        "φ = 2, γ = 0,5 —, valeurs du rédacteur sans appui mesuré. Une fréquence par strate est la propriété d'une loi "
        "sur un monde : elle ne dépend du réglage que par le hasard de l'échantillon, ce qu'une fréquence regroupée ne "
        "garantit pas.",
    ),
    (
        "B2, couche statistique",
        "selon les fréquences M12 mesurées **par loi** sur la couche mécanique, puis reprise pour toute tentative qui "
        "engage la même loi sur le même monde",
        "selon les fréquences M12 mesurées **par loi** sur la couche mécanique — par type et, pour une loi non plantée, "
        "selon l'origine de la tentative (version 4) —, puis reprise pour toute tentative qui engage la même loi sur le "
        "même monde ; une loi non plantée y est tenue pour distincte à chaque tentative, ce qui est exact pour la "
        "recherche de base et les compositions, approché pour les copies, dont M1 ne dépend pas",
    ),
    (
        "B3, sens de la divergence",
        "sinon elle n'est appariée à rien ;",
        "sinon elle n'est appariée à rien (version 4, précision : la divergence est prise de la loi plantée vers la loi "
        "de la tentative, le sens de l'oracle de l'organisme, en moyenne sur les 4 000 instances de l'oracle du monde, "
        "tirées comme l'organisme les tire ; si deux lois plantées du domaine passaient le seuil, la plus proche serait "
        "retenue, cas que la marge du générateur exclut) ;",
    ),
    # --- B4 --------------------------------------------------------------------------------------------------------------
    (
        "B4, statistique et seuil de la forme imposée",
        "la statistique « moyenne », un seuil « au moins », la loi gelée dans le texte du test.",
        "la statistique « moyenne », un seuil « au moins », la loi gelée dans le texte du test. La statistique et le "
        "seuil sont ceux du tour fermé (version 4 : le texte ne les chiffrait pas) : le gain moyen par épisode du "
        "log-score de la loi sur la marginale empirique de la tranche (comptes plus un demi), en nats, et le seuil "
        "« au moins 0,02 ».",
    ),
    (
        "B4, balisage unique",
        "**La description bornée est portée par le champ `enonce` de la fiche**, entre balises de donnée, à la place de "
        "l'hypothèse neutre que le tour fermé y écrit",
        "**La description bornée est portée par le champ `enonce` de la fiche**, à la place de l'hypothèse neutre que le "
        "tour fermé y écrit, **sans balise ajoutée** : l'étage sert déjà le préenregistrement court entier, `enonce` "
        "compris, dans une section de données, entre ses deux balises ; « entre balises de donnée » se lit, ici et dans "
        "la table des valeurs gelées, « dans cette section balisée par l'étage », et la description n'est jamais balisée "
        "une seconde fois (version 4 ; annexe F, point 5)",
    ),
    # --- B6 --------------------------------------------------------------------------------------------------------------
    (
        "B6, règle de la version 1",
        "(devis de la version 3, § 2 bis ; `calcul_devis_heritage_v2.py`, fonction `appels_perdus`).",
        "(devis de la version 3, § 2 bis ; `calcul_devis_heritage_v2.py`, fonction `appels_perdus`). Le coût d'un appel "
        "y comprend sa provision d'épreuve, comme dans la règle de la version 2 (version 4, précision ; ne touche que le "
        "point 8).",
    ),
    (
        "B6, course source",
        "**La course source** tient un registre né vide, servi et payé comme au bras 2, sur trois générations du monde "
        "source.",
        "**La course source** tient un registre né vide, servi et payé comme au bras 2, sur trois générations du monde "
        "source. **Conduite des proposeurs dans la course source (version 4 ; annexe F, point 3).** Chaque proposeur "
        "s'y conduit comme au bras 2 d'un registre né vide : **aucune entrée n'y est héritée**. Le lecteur réglé pour "
        "l'héritage n'y compose donc rien et n'y fait que la recherche de base : il ne compose jamais les entrées de sa "
        "propre course. Les autres conduites s'y appliquent comme au bras 2 — le multiplicateur de la tenue dès qu'une "
        "entrée de sa propre course est gardée, le suiveur et le généraliste selon la taille de ce qui est servi, le "
        "copieur dès que le registre n'est plus vide. Au monde source, qui n'a pas de loi dépendante, la recherche de "
        "base tire parmi les huit lois vraies.",
    ),
    # --- B7 --------------------------------------------------------------------------------------------------------------
    (
        "B7, recherche de base",
        "sinon une loi qui n'est appariée à rien.",
        "sinon une loi qui n'est appariée à rien : une loi neuve tirée au hasard, de la forme unique (B1), engagée sur "
        "un domaine tiré au hasard parmi les seize.",
    ),
    (
        "B7, lecteur, entrées héritées",
        "il lit, dans le registre servi, les entrées **venues de la source** dont `gardee` vaut oui ;",
        "il lit, dans le registre servi, les entrées **héritées** dont `gardee` vaut oui — héritées : écrites par la "
        "course de la source (de la source étrangère au bras 4a) et reçues au départ de la continuation ; une course "
        "source n'en a aucune (B6) ; ailleurs dans ce texte, « venues de la source » se lit de même ;",
    ),
    (
        "B7, lecteur, deux sens et criblage",
        "compose la loi et la crible sans frais sur la **part servie** des domaines du monde en cours ;",
        "compose la loi **dans les deux sens** (il ne connaît pas les rangs : chaque loi de la paire sur la première "
        "sous-population, l'autre sur la seconde) et crible les deux compositions sans frais sur la **part servie** des "
        "domaines du monde en cours — une composition passe le criblage sur un domaine si la statistique du test de "
        "mort (B4), calculée sur la part servie de ce domaine, atteint le seuil de 0,02 — ;",
    ),
    (
        "B7, lecteur, moitié",
        "dans la limite de la moitié de ses tentatives,",
        "dans la limite de la moitié de ses tentatives (entier inférieur),",
    ),
    (
        "B7, lecteur, sans entrée héritée",
        "Sans entrée venue de la source (bras 1 et 2), il ne fait que la recherche de base",
        "Sans entrée héritée (bras 1 et 2, et toute course source), il ne fait que la recherche de base",
    ),
    (
        "B7, K",
        "par un tirage semé, de moyenne K",
        "par un tirage semé, de moyenne K, un par génération ; une paire examinée compte pour un, ses deux compositions "
        "comprises",
    ),
    (
        "B7, repli",
        "sur les lois distinctes de **toutes** les entrées venues de la source",
        "sur les lois distinctes de **toutes** les entrées héritées",
    ),
    (
        "B7, criblage",
        "ce taux de faux passage est mesuré sur la couche mécanique avec M12, **par composition et par monde** (une "
        "composition examinée plusieurs fois sur un même monde rend le même criblage), et injecté de même dans la couche "
        "statistique.",
        "ce taux de faux passage, et le taux de passage des compositions qui sont une loi dépendante du monde "
        "(version 4), sont mesurés sur la couche mécanique avec M12, **par composition et par monde** (une composition "
        "examinée plusieurs fois sur un même monde rend le même criblage), et injectés de même dans la couche "
        "statistique.",
    ),
    (
        "B7 bis, marge face à la source étrangère",
        "et l'audit du générateur vérifie la marge (section « Seuil »).",
        "et l'audit du générateur vérifie la marge (section « Seuil »). **Version 4 (annexe F, point 6).** Attendue "
        "d'un rejet, cette marge souffrirait du défaut de celles de B1. Elle est donc construite, pour les seules "
        "sources de la couche mécanique où les bras 4a et 4b se jouent (garde 27 ; jeu de sources à part, sous sa "
        "propre étiquette de graines) : les lois indépendantes et les lois fausses d'un monde cible y sont tirées "
        "séparées aussi, à 0,30 nat, des lois vraies de la source étrangère et des compositions de deux d'entre elles, "
        "dans les deux sens ; une loi dépendante qui manque la marge fait retirer la suite, dans les bornes de B1. "
        "L'audit juge à 0,25 nat. Sur la couche statistique aucune loi n'est écrite, et la marge y est sans objet. Ce "
        "point n'a été éprouvé par personne, même sur des graines d'essai (réserve 20).",
    ),
    # --- B8, B9 -----------------------------------------------------------------------------------------------------------
    (
        "B8, champs d'étiquette",
        "numéro de tirage, de source, de bras, de génération, de jumelle)",
        "numéro de tirage, de lot de sources, de source, de bras, de génération, de jumelle, d'essai et de tour du "
        "générateur)",
    ),
    (
        "B8, couches disjointes",
        "l'étalonnage, la couche mécanique, les tirages décisifs et les tirages de confirmation ont des étiquettes "
        "disjointes.",
        "l'étalonnage, la couche mécanique, sa reprise aux réglages gelés, l'audit du générateur, l'essai de forme, les "
        "essais du code, les tirages décisifs et les tirages de confirmation ont des étiquettes disjointes ; aucune "
        "graine des tirages décisifs ou de confirmation ne se dérive avant le scellement de ce texte et l'erratum du "
        "code (liste d'arrêt, point 1).",
    ),
    (
        "garde 11, cas sain",
        "seuls l'engagement et la description (portée par `enonce`), entre balises de donnée, la part de données gelée "
        "en B4",
        "seuls l'engagement et la description (portée par `enonce`), entre les balises de donnée que pose l'étage et "
        "elles seules (la fiche projetée n'en porte aucune), la part de données gelée en B4",
    ),
    (
        "garde 11, artefact",
        "une justification, une prédiction du registre ou une autre entrée glissée dans la projection : arrêt",
        "une justification, une prédiction du registre ou une autre entrée glissée dans la projection : arrêt ; une "
        "balise de donnée écrite dans un champ de la fiche projetée : arrêt (version 4)",
    ),
    (
        "garde 25, artefact de contenu",
        "une dose inscrite dans la présentation : exactitude équilibrée au-dessus de 0,55, rejet",
        "une dose inscrite dans la présentation : exactitude équilibrée au-dessus de 0,55, rejet ; les poids des lois "
        "dépendantes doublés par un générateur fautif planté : exactitude au-dessus de 0,55 sur les traits de contenu, "
        "rejet (version 4)",
    ),
    # --- ordre, rapporté, liste d'arrêt ------------------------------------------------------------------------------------
    (
        "ordre des opérations, étape 1",
        "vérification des corrections par le même contre-lecteur (à faire).",
        "vérification des corrections par le même contre-lecteur (faite), erratum de la version 3 et sa relecture "
        "(faits), erratum de conception de cette version 4, puis sa relecture par le même contre-lecteur (à faire).",
    ),
    (
        "ordre des opérations, étape 2",
        "2. Écriture du code (annexe C) par un développeur,",
        "2. Écriture du code (annexe C) par un développeur — un développeur neuf, qui reprend le travail inachevé versé "
        "après la relecture de la version 4 (ligne " + GO + ") —,",
    ),
    (
        "ordre des opérations, étape 3",
        "3. Audit du générateur (B1). 4. Couche mécanique",
        "3. Audit du générateur (B1 : marges sur chaque monde ; présentation sur 50 suites par dose de la couche "
        "« audit »). 4. Couche mécanique",
    ),
    (
        "ce qui est rapporté",
        "Les fréquences M12, dont la part de lois fausses tenues.",
        "Les fréquences M12, dont la part de lois fausses tenues ; celles des lois non plantées par origine et leur "
        "fréquence regroupée ; celle des lois vraies par classe. Les rejets du générateur par niveau, le taux "
        "d'acceptation des tirages et la distribution des traits de contenu par sorte de loi ; les neuf exactitudes de "
        "l'audit de présentation. La taille de l'ensemble exclu, par source.",
    ),
    (
        "liste d'arrêt, point 2",
        "le générateur ne peut pas être écrit comme B1 le définit (grammaire des lois), ou son audit échoue",
        "le générateur ne peut pas être écrit comme B1 le définit (grammaire des lois), ou son audit échoue, ou les "
        "bornes de sa construction sont épuisées (200 essais d'un monde, ou 200 tours d'une suite ; B1)",
    ),
    (
        "liste d'arrêt, point 4",
        "S8 : l'épreuve simulée ne discrimine pas, ou les deux couches ne s'accordent pas",
        "S8 : l'épreuve simulée ne discrimine pas, ou les deux couches ne s'accordent pas, ou une strate de M12 dont la "
        "couche statistique a besoin est vide",
    ),
    # --- contre-lecture -----------------------------------------------------------------------------------------------------
    (
        "contre-lecture, état",
        "**La relecture du seul erratum par le même contre-lecteur n'est pas faite à l'heure où cette version 3 est "
        "rendue ; ce texte ne peut pas être scellé avant elle**, ni avant l'erratum qui inscrit le commit du code.",
        "**Relecture de l'erratum de la version 3 faite** (même contre-lecteur, modèle O ; la relecture, chemin et "
        "empreinte en tête de ce texte) : « scellable tel quel » — verdict qui porte sur la version 3, non sur celle-ci. "
        "**Cette version 4 change le banc (annexe F) ; sa relecture par le même contre-lecteur n'est pas faite à l'heure "
        "où elle est rendue, et ce texte ne peut pas être scellé avant elle**, ni avant l'erratum qui inscrit le commit "
        "du code.",
    ),
    (
        "contre-lecture, fichiers",
        "la ligne `GO-2026-11-19-81`, le rapport du rédacteur de la version 3.",
        "la ligne `GO-2026-11-19-81`, le rapport du rédacteur de la version 3. Pour la relecture de la version 4 : "
        "cette version et la version 3, leur différentiel, le mandat de la version 4, la ligne " + GO + ", le rapport "
        "du rédacteur de la version 4, le dossier versé (LISEZ-MOI, les six modules et les trois outils nommés en tête) "
        "et, dans la copie du code de l'organisme, les trois passages cités à l'annexe F, point 5.",
    ),
    (
        "contre-lecture, points de la version 4",
        "(g) les deux précisions faites aux gardes 23 et 26.\n",
        "(g) les deux précisions faites aux gardes 23 et 26.\n\n"
        "Points de la version 4 à vérifier en premier : (a) que le générateur constructif, tel qu'écrit, donne les "
        "marges que l'audit juge, et qu'il ne change que la loi des lois ; (b) les traits de contenu ajoutés à l'audit "
        "de présentation, seule sévérité de plus, et leur artefact (garde 25) ; (c) la règle de la course source, et "
        "qu'elle rend l'ensemble exclu vide par construction ; (d) la stratification de M12 : qu'elle tient à la "
        "construction et non à un chiffre, et ce qu'elle laisse à la garde d'équivalence ; (e) le balisage unique ; "
        "(f) le point 6 de l'annexe F, que personne n'a éprouvé ; (g) les réglages de l'étape 4, valeurs du rédacteur ; "
        "(h) qu'aucun critère, aucun seuil chiffré, aucune valeur de la table des valeurs gelées n'a changé.\n",
    ),
    # --- annexe C -----------------------------------------------------------------------------------------------------------
    (
        "annexe C, état du code",
        "Ce texte ne contient aucun code.\n",
        "Ce texte ne contient aucun code.\n\n"
        "**Version 4.** Un premier développeur a écrit quinze modules et deux fichiers d'essais, puis s'est arrêté à un "
        "refus d'outil ; son travail est versé, inachevé, ni contre-lu ni éprouvé en entier (le dossier versé, en tête "
        "de ce texte). Cette version tranche les choix qu'il a dû faire (annexe F) ; elle ne valide pas ce code. Un "
        "développeur neuf le reprend sur la version relue (ligne " + GO + "). **Le code suit ce texte, non l'inverse** : "
        "là où le dossier versé s'en écarte, c'est le dossier qui se corrige.\n",
    ),
    (
        "annexe C, essais",
        "(rapport du palier 0a, § 1, et sa sortie).\n",
        "(rapport du palier 0a, § 1, et sa sortie) ; (version 4) le lecteur ne compose rien dans une course source, et "
        "l'ensemble exclu d'un générateur sain y est vide ; la couche statistique lit les sept fréquences, et une "
        "strate vide dont elle a besoin l'arrête.\n",
    ),
    # --- réserves ------------------------------------------------------------------------------------------------------------
    (
        "réserve 1",
        "Le développeur confirme à la lecture du code, et s'arrête s'il trouve autre chose.",
        "Le développeur confirme à la lecture du code, et s'arrête s'il trouve autre chose. **Version 4** : une copie du "
        "code de l'organisme est au dépôt ; je n'y ai lu que trois passages (annexe F, point 5). Le développeur a "
        "confirmé le champ `enonce` et la grammaire des lois ; son travail est inachevé.",
    ),
    (
        "réserve 2",
        "Si elles ne tiennent pas, c'est un arrêt et un erratum, non un arrangement.",
        "Si elles ne tiennent pas, c'est un arrêt et un erratum, non un arrangement. **Version 4** : la grammaire les "
        "admet ; ce qui ne tenait pas est le tirage par rejet de mondes entiers, d'où cet erratum (annexe F, point 1).",
    ),
    (
        "réserve 7",
        "elle éprouve le reste de la mécanique, non ces fréquences.",
        "elle éprouve le reste de la mécanique, non ces fréquences. **Version 4** : sept fréquences au lieu de cinq "
        "viennent de la couche mécanique ; la garde éprouve d'autant moins ce qu'elles portent. Elle se joue sur une "
        "reprise de la couche mécanique dont les graines sont disjointes de celles où les fréquences sont mesurées "
        "(étapes 4 et 6 bis) : stratifier ne la fait pas passer par construction.",
    ),
    (
        "réserve 14, accord",
        "écrite avant tout tirage et motivé par deux chiffres",
        "écrite avant tout tirage et motivée par deux chiffres",
    ),
    (
        "réserves 17 à 21",
        "la description reste servie et la garde 11 est éprouvée sur les deux listes.\n",
        "la description reste servie et la garde 11 est éprouvée sur les deux listes.\n"
        "17. **Le générateur constructif change la loi des lois** (version 4 ; B1) : elles se repoussent, et les sortes "
        "de lois ne passent pas le même filtre. L'étage ne dit donc rien de lois tirées indépendamment. La marge de "
        "construction de 0,30 nat et les bornes (400, 200, 200) sont des valeurs du développeur, sans autre appui que "
        "ses essais sur des graines « essai », que je n'ai pas rejoués.\n"
        "18. **L'audit de présentation, avec ses traits de contenu, peut échouer** (version 4). Je m'attends à ce qu'il "
        "passe pour les lois vraies contre les fausses ; je ne sais pas le dire pour les dépendantes contre les "
        "indépendantes, dont les filtres diffèrent. S'il échoue, c'est un arrêt (liste d'arrêt, point 2) ; la voie à "
        "écrire alors, par un erratum contre-lu, serait de faire passer toutes les sous-lois d'une suite par un même "
        "filtre ; personne ne l'a éprouvée.\n"
        "19. **La stratification de M12 a été écrite après un diagnostic** (version 4). Sa raison tient à la "
        "construction — le criblage choisit des compositions qui passent sur une moitié des données, et elles tiennent "
        "donc plus souvent sur l'autre que des lois tirées au hasard —, mais le rédacteur connaissait le désaccord des "
        "deux couches, vu par le développeur sur des graines « essai ». Trois garde-fous : la garde d'équivalence se "
        "joue sur des graines disjointes ; aucune strate ne s'ajoute sans erratum contre-lu ; un nouveau désaccord est "
        "un arrêt, non une strate de plus.\n"
        "20. **Le point 6 de l'annexe F** (marge face à la source étrangère, B7 bis) est une construction du rédacteur "
        "que personne n'a éprouvée ; le dossier versé n'a que la fonction d'audit, non branchée. Si elle ne passe pas "
        "dans les bornes de B1, c'est un arrêt et un erratum.\n"
        "21. **Ce que je n'ai pas** (version 4) : le rapport de fin du développeur, absent du dossier versé — je "
        "m'appuie sur son LISEZ-MOI, sur les mentions « SILENCE » de son code et sur le mandat ; les sorties de ses "
        "outils de diagnostic, non versées — les chiffres que je cite viennent du mandat et du LISEZ-MOI ; un "
        "lancement quelconque de son code, qui m'est interdit. Les réglages de l'étape 4 (B2) et les 50 suites de "
        "l'audit sont des valeurs du rédacteur, sans appui mesuré.\n",
    ),
]

ANNEXE_F = """
## Annexe F — Erratum de conception de la version 4 : les cinq points du développeur, un sixième, les silences comblés

Mandat : `mandat-redacteur-preenregistrement-palier-0b-v4-erratum-conception-v1.md` (empreinte en tête). Ligne d'accord : `GO-2026-11-19-84`. La version 3 (`@EMPREINTE_V3@`) n'est pas modifiée. **Tout ce qui n'est pas nommé dans cette annexe est repris à l'octet de la version 3** : cette version est produite par @N@ remplacements exacts sur la version 3, chacun trouvé une seule fois, et par l'ajout de cette annexe ; le programme (`appliquer_corrections_palier_0b_v4.py`) et le différentiel ligne à ligne sont dans le dossier de travail du rédacteur, à verser avec ce texte.

**D'où viennent ces points.** Le développeur du code (modèle L′) s'est arrêté à un refus d'outil, après avoir trouvé que le texte, à la lettre, ne se code pas sur cinq points. Son travail inachevé est versé (le dossier versé, en tête de ce texte). **Aucun choix de cette annexe ne s'appuie sur un chiffre d'une course décisive : il n'y en a aucune**, et aucune graine des couches « décisif » ou « confirmation » n'a été dérivée. Les chiffres du développeur cités ci-dessous viennent de ses outils de diagnostic (`outils-dev/`), sur des graines de la couche « essai » ; leurs sorties ne sont pas versées ; je les reprends du mandat et du LISEZ-MOI sans les avoir recalculés. Ils illustrent ; chaque choix est motivé par la construction du banc.

### Point 1 — les marges de B1 : le générateur constructif

- **Ce que le texte disait** : des lois tirées, des marges jugées par l'audit, « un monde qui manque une marge est rejeté et retiré ».
- **Ce que le développeur a trouvé** : par rejet de mondes entiers, 0 monde source sur 41 passe à la force des lois de l'organisme (1,5), et 1 sur 41 à la force 4 (`outils-dev/diagnostic_marges.py`, graines d'essai). Cause : les lois que le banc lie entre elles — une loi dépendante et chacune de ses mères, une loi fausse et sa loi vraie, deux lois dépendantes de même mère — ne diffèrent que sur une sous-population.
- **Ce que le texte dit** : le générateur construit les marges loi par loi, à 0,30 nat, et l'audit, inchangé, juge à 0,25 nat le produit fini (B1, « Générateur constructif »).
- **Pourquoi cette voie et non une autre.** *Baisser la marge de 0,25 nat* changerait un seuil gelé et rapprocherait les lois du seuil d'appariement de 0,05 nat : écarté. *Durcir la force des lois* change aussi leur loi et ne suffit pas (1 sur 41). *Renoncer aux lois liées par moitié* défait la dose de dépendance et les lois fausses « demi-vraies » du plan (§ 5). Construire garde le seuil, l'audit et le dessin ; seul change le tirage des lois.
- **Ce que cela change, et comment c'est contrôlé** : la loi des lois (elles se repoussent ; les sortes de lois ne passent pas le même filtre). Contrôle : marges rejugées sur le produit fini ; traits de contenu ajoutés à l'audit de présentation ; taux d'acceptation et distributions rapportés (B1 ; section « Seuil » ; réserves 17 et 18).
- **Ce que cela touche** : aucun seuil (0,25 nat et 0,55 inchangés), aucun critère. L'audit de présentation est **plus sévère** qu'en version 3 (neuf exactitudes au lieu de trois, dont six sur le contenu) : il peut arrêter le générateur là où la version 3 ne l'aurait pas arrêté (liste d'arrêt, point 2 ; garde 25, un artefact de plus). La liste d'arrêt, point 2, reçoit une cause de plus (bornes épuisées).

### Point 2 — la forme unique des lois

- **Ce que le texte disait** : « une loi génératrice de la classe que l'organisme sait déjà évaluer », sans dire sa forme écrite.
- **Ce que le texte dit** : toute loi plantée et toute loi neuve engagée s'écrit `par_sous_population`, deux sous-lois `softmax` (B1, « Forme unique des lois »).
- **Pourquoi** : une loi composée est de cette forme par nature ; avec une autre forme pour les lois indépendantes, l'audit « dépendantes contre indépendantes » échouerait par construction, et un proposeur réel lirait la classe d'une loi dans sa forme.
- **Revers, dit** : sous une forme unique, les traits de forme ne varient presque plus (mêmes champs, mêmes comptes de nombres) et l'audit de forme ne peut plus guère échouer ; d'où les traits de contenu (point 1).
- **Ce que cela touche** : aucun critère, aucun seuil. Une loi indépendante est désormais faite de deux sous-lois tirées à part, et non d'une loi commune aux deux sous-populations.

### Point 3 — le lecteur ne compose pas ses propres entrées dans la course source

- **Ce que le texte disait** : le lecteur « lit, dans le registre servi, les entrées venues de la source dont `gardee` vaut oui ». Dans la course source, toutes les entrées servies viennent de la source : à la lettre, le lecteur y composerait ses propres entrées.
- **Ce que le développeur a trouvé** : ces compositions de deux lois vraies de la source sont, aux doses non nulles, les lois dépendantes mêmes des mondes cibles ; écrites au registre de la source, elles entrent dans l'ensemble exclu, qui cesse d'être vide (4 lois du monde final exclues sur son essai, graines d'essai) ; l'effet planté est effacé, et la garde 13 l'a vu.
- **Ce que le texte dit** : « héritée » veut dire écrite par la course de la source et reçue au départ d'une continuation ; une course source n'a aucune entrée héritée, et le lecteur n'y fait que la recherche de base ; les autres proposeurs s'y conduisent comme au bras 2 d'un registre né vide (B6, « Conduite des proposeurs dans la course source » ; B7, ligne du lecteur).
- **Pourquoi** : c'est le dessin du plan (§ 6) : l'ensemble exclu « doit être vide » par construction, les lois dépendantes étant composées de lois de la source et non identiques à une entrée de son registre. La lettre de la version 3 le rendait non vide chez le proposeur même qui porte C2 et C5.
- **Ce que cela touche** : la conduite d'un proposeur du banc ; aucun critère, aucun seuil. M1 est précisée sur un point plus strict (l'ensemble exclu se lit sans égard au domaine).

### Point 4 — M12 et l'accord des deux couches

- **Ce que le texte disait** : une fréquence de « tient » par type de loi — vraie, fausse, non plantée.
- **Ce que le développeur a trouvé** : avec une seule fréquence pour les lois non plantées (environ 0,09, regroupée), les deux couches ne s'accordent pas (bras 3 du lecteur : 7,5 lois sur la couche mécanique contre 4,25 sur la couche statistique ; `outils-dev/essai_equivalence.py`, graines d'essai), et S8 (ii) arrêterait le run.
- **La cause, qui tient à la construction** : « loi non plantée » réunit trois populations. Une loi neuve de la recherche de base, tirée au hasard, tient rarement. Une composition engagée a passé le criblage sur la part servie : elle a été choisie pour passer, et tient donc plus souvent sur la tranche d'épreuve. Une copie est une troisième population. La fréquence regroupée dépend du mélange — du proposeur, du bras, de K — et non du banc. Or la couche statistique l'applique aussi à la course source, où il n'y a que des lois de base : elle y garde trop de lois non plantées, donc trop de paires, et les paires de lois vraies y sont diluées parmi les K examinées (lecture du rédacteur sur le code versé, non recalculée).
- **Ce que le texte dit** : la fréquence des lois non plantées est mesurée et servie **par origine** — recherche de base, composition, copie (M12 ; B2 ; S8). Les lois vraies et les lois fausses gardent une fréquence chacune ; celle des lois vraies est rapportée aussi par classe.
- **Pourquoi cette voie et non la lettre** : à la lettre, l'arrêt est connu d'avance et ne dit rien de l'instrument ; il dit que le modèle réduit regroupe ce que le banc sépare. Stratifier par origine est le plus petit changement qui rende à chaque fréquence la population où elle s'applique. Je n'ai pas stratifié davantage : rien, dans la construction, ne sépare d'autres populations de cette taille, et chaque strate de plus est un réglage de plus pris à la couche à laquelle on se compare.
- **Ce que cela change à la garde d'équivalence** : ni sa forme, ni son niveau (99,9 %), ni ses comparaisons. Le fichier gelé porte sept fréquences au lieu de cinq. La garde éprouve d'autant moins ce que ces fréquences portent (réserve 7) ; elle garde sa prise parce qu'elle se joue sur une reprise de la couche mécanique à graines disjointes (étape 6 bis). Une strate vide dont la couche statistique a besoin arrête (liste d'arrêt, point 4, une cause de plus). Les réglages auxquels les fréquences sont mesurées, que le texte ne disait pas, sont fixés (B2).
- **Ce que cela touche** : la définition d'une métrique (M12) et les mots de l'hypothèse de travail (iii) ; aucun critère, aucun seuil. S8 (i) et la garde 23 lisent les fréquences des lois vraies et fausses, inchangées.

### Point 5 — le balisage de la description servie à l'expérimentateur

- **Ce que le texte disait** : la description bornée est « portée par le champ `enonce` de la fiche, entre balises de donnée ».
- **Ce que le développeur a fait** : il a entouré la description de balises dans le champ même ; or l'étage sert déjà le préenregistrement court entier, `enonce` compris, dans une section de données entre ses deux balises (`tests_de_mort_v2.py`, l. 334 à 347 pour ce qui est extrait de la fiche, l. 2166 pour la section ; `protocole_outils.py`, l. 32-33 et 170 à 178 ; `a_blanc_v59.py`, l. 62, pour la correspondance de `enonce`). La description était balisée deux fois.
- **Ce que le texte dit** : une seule fois, par l'étage ; la fiche projetée ne porte aucune balise (B4 ; garde 11).
- **Pourquoi** : une balise de fin écrite à l'intérieur d'une donnée est ce qu'un texte hostile écrirait pour faire croire que la donnée s'arrête là ; la règle d'usage est qu'une donnée ne contient jamais le délimiteur qui l'entoure. Le second balisage n'ajoute aucune protection et installe ce motif. La garde 11 reçoit l'artefact correspondant.
- **Ce que cela touche** : C6 par un artefact de plus à la garde 11 ; aucun seuil. La ligne « ce que l'expérimentateur reçoit » de la table des valeurs gelées n'est pas changée : sa lecture est écrite en B4.

### Point 6 — trouvé par le rédacteur : la marge face à la source étrangère (B7 bis)

La version 3 demande que toute loi d'un monde cible soit séparée d'au moins 0,25 nat des lois vraies de la source étrangère et de leurs compositions. Le dossier versé a la fonction d'audit, non branchée, et aucune construction : attendue d'un rejet, cette marge aurait le défaut du point 1. La version 4 la construit pour les seules sources de la couche mécanique où les bras 4a et 4b se jouent (B7 bis). **Personne ne l'a éprouvée** (réserve 20). Elle ne touche aucun critère : les bras de diagnostic sont rapportés sans critère, et la garde 27 porte sur le registre servi, non sur cette marge.

### Les autres silences comblés par le développeur

Source : le LISEZ-MOI et les mentions « SILENCE » du code versé ; le rapport de fin du développeur n'est pas au dossier (réserve 21).

**Écrits au texte, parce qu'ils touchent ce qui est jugé ou lu.**

| silence | choix repris | où |
|---|---|---|
| nombre d'épisodes par domaine ; tirage des traits et de la sous-population | 400 ; loi normale, six décimales ; pile ou face | B1 |
| force des lois | poids d'écart-type 1,5, biais d'écart-type 0,3 | B1, forme unique |
| rang d'une loi de la source | l'ordre de son domaine | B1, dose |
| sous-population gardée par une loi fausse | pile ou face | B1 |
| sens de la marge | le plus petit des deux sens, sur les 4 000 instances de l'oracle du monde | section « Seuil » |
| sens de la divergence à l'appariement ; deux lois sous le seuil | de la loi plantée vers la tentative ; la plus proche | B3 |
| ensemble exclu | lu sans égard au domaine (plus strict) | M1 |
| statistique et seuil de la forme imposée | gain moyen de log-score sur la marginale empirique ; « au moins 0,02 » | B4 |
| criblage du lecteur | la statistique du test de mort sur la part servie, même seuil ; les deux sens de composition d'une paire | B7 |
| taux de passage des compositions vraies | mesuré et servi comme le taux de faux passage | M12 ; B7 |
| « la moitié de ses tentatives » ; K non entier | entier inférieur ; un tirage par génération | B7 |
| loi « appariée à rien » de la recherche de base ; monde source | loi neuve sur un domaine tiré au hasard ; les huit lois vraies | B7 ; B6 |
| origine d'une loi engagée plusieurs fois | celle de la première tentative | M12 |
| loi non plantée dans la couche statistique | distincte à chaque tentative | B2 |
| règle de retrait de la version 1 | le coût d'un appel comprend la provision d'épreuve | B6 |
| monde ou suite retirés | étiquette de graine propre (essai, tour) | B8 |
| réglages de la mesure des fréquences (silence trouvé par le rédacteur) | milieu de chaque plage | B2 |

**Acceptés sans entrer au texte, parce qu'ils ne touchent ni ce qui est jugé ni ce qui est lu** : le vecteur fixe de la prédiction (0,3 ; 0,5 ; 0,2, dans l'ordre des classes) ; les textes fixes de la description, de la justification et des champs neutres de la fiche ; le lot de 2 000 sources du calcul vectorisé ; les noms des couches de graines et l'ordre des champs d'une étiquette ; l'objet qui refuse de dériver une graine décisive sans le texte scellé et l'erratum du code ; la tolérance du contre-calcul et le plancher des probabilités, repris de l'organisme ; les équivalences de loi employées par la couche statistique (comptes multinomiaux, loi hypergéométrique pour les paires examinées), que la garde d'équivalence éprouve.

### La réserve 14

« motivé » devient « motivée » (point de forme de la relecture).

### Ce que cette version touche, en une table

| objet | touché ? | comment |
|---|---|---|
| énoncé de l'hypothèse, décisions de Lazar, écart déclaré à N-058 | non | — |
| hypothèse de travail (iii) | mots | « par origine » pour les lois non plantées |
| pronostics | non | — |
| M1 | précision | ensemble exclu lu sans égard au domaine ; de nouveau vide par construction |
| M12 | définition | lois non plantées par origine ; taux de passage ; deux fréquences rapportées à côté |
| table des valeurs gelées, six critères C1 à C6, S7, S9, les trois issues, n et m | non | — |
| S8 | forme inchangée | sept fréquences ; strate vide : arrêt |
| marges du générateur | seuils inchangés | audit de présentation précisé et plus sévère (traits de contenu) |
| gardes de C6 | deux artefacts de plus | garde 11 (balise dans la fiche) ; garde 25 (contenu) |
| liste d'arrêt | deux causes de plus | point 2 (bornes de la construction) ; point 4 (strate vide) |
| banc | oui | générateur constructif ; forme unique ; course source ; balisage unique ; marge de B7 bis construite |

### Ce qui revient à Lazar

**Aucun critère ni aucun seuil n'est changé : rien, ici, n'est un écart déclaré à un critère.** La ligne `GO-2026-11-19-84` couvre cet erratum. Trois choses sont portées à Lazar pour information, par la mère, parce qu'elles changent ce que l'étage dit ou peut arrêter : (1) les lois des mondes ne sont plus tirées indépendamment ; (2) l'audit de présentation est plus sévère, par choix du rédacteur — s'il préfère que les traits de contenu soient rapportés sans arrêter, c'est une phrase à changer avant le scellement ; (3) M12 est stratifiée après un diagnostic (réserve 19).

### Ce qui n'est pas changé par la version 4

L'hypothèse et son objet ; les pronostics ; M2 à M11, M13 et M14 ; les grilles, les 10 000 tirages, le taux d'échec, les tailles, les doses ; les six critères et leurs seuils ; S7, S9 ; les trois issues, n et m ; l'audit de symétrie ; les familles de B8 ; les gardes hors des deux artefacts ajoutés ; l'annexe A, l'annexe B, l'annexe D, l'annexe E ; les réserves 3 à 6, 8 à 13, 15 et 16 ; la racine des graines.
"""


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    source, cible, heure = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    octets = source.read_bytes()
    if hashlib.sha256(octets).hexdigest() != EMPREINTE_V3:
        sys.exit("la source n'a pas l'empreinte de la version 3 : arrêt, rien n'est écrit")
    if cible.exists():
        sys.exit("la cible existe déjà : arrêt, rien n'est écrasé (R12)")
    texte = octets.decode("utf-8")
    manques = []
    for nom, ancien, _ in REMPLACEMENTS:
        n = texte.count(ancien)
        if n != 1:
            manques.append(f"{nom} : trouvé {n} fois")
    if manques:
        sys.exit("remplacements non uniques, rien n'est écrit :\n" + "\n".join(manques))
    for nom, ancien, nouveau in REMPLACEMENTS:
        if texte.count(ancien) != 1:
            sys.exit(f"{nom} : n'est plus unique après les remplacements précédents ; rien n'est écrit")
        texte = texte.replace(ancien, nouveau.replace("@HEURE_FIN@", heure))
    if not texte.endswith("\n"):
        texte += "\n"
    annexe = ANNEXE_F.replace("@EMPREINTE_V3@", EMPREINTE_V3).replace("@N@", str(len(REMPLACEMENTS)))
    texte += annexe
    if "@N@" in texte or "@HEURE_FIN@" in texte or "@EMPREINTE_V3@" in texte:
        sys.exit("marqueur de substitution restant ; rien n'est écrit")
    cible.write_text(texte, encoding="utf-8")
    print(len(REMPLACEMENTS), "remplacements ;", hashlib.sha256(texte.encode("utf-8")).hexdigest(), cible)


if __name__ == "__main__":
    main()
