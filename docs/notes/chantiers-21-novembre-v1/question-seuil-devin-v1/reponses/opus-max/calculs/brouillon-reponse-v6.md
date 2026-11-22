# Réponse — seuil et budget de l'épreuve d'admission par prédicteur adverse

Opus 5.5, effort maximal, 22 novembre 2026. [FAIT RAPPORTÉ] Écrite de la seule question ; chiffres refaits par quatre scripts Python, empreintes en fin de note.

## 1. Choix : une option (d)

[PROPOSITION] **Seuil corrigé de 0,0125 par test, 8 000 épisodes par test, confirmation exacte avant toute suspension durable, statistiques de queue pour le secret d'audit.** Un rejet suspend la garantie et déclenche une confirmation : le seul prédicteur qui a rejeté, figé, éprouvé sur 4 000 épisodes neufs au seuil 0,05 ; la suspension ne dure que si la confirmation rejette aussi. Parmi les options écrites : (b) si seules les fuites de plus de 0,12 en équilibré sont dangereuses ; (c) en deçà, car aucun seuil ne rattrape un budget manquant ; (a) seulement si une suspension ne coûte presque rien.

Pourquoi :
- [CALCUL] Le seuil est un levier faible sur la sensibilité : de 0,05 à 0,0125, la plus petite fuite retrouvée ne croît que de 10,8 %, le maximum sur trente prédicteurs plaçant déjà le seuil loin dans la queue ; doubler le budget la réduit de 29 %. C'est un levier fort sur les fausses suspensions (18,5 % → 4,9 %). À sensibilité égale, le seuil corrigé coûte 23 % d'épisodes de plus.
- [CALCUL] La confirmation, sans multiplicité ni moitié d'apprentissage, retrouve une fuite de la taille du criblage avec une puissance de 0,99 ; le protocole en deux temps garde une plus petite fuite retrouvée de 0,066 et ne laisse que 0,25 % de suspensions durables à tort par admission, sous toute dépendance. Elle ferme aussi la réépreuve « jusqu'au succès » (point 5).
- [HYPOTHÈSE] Je double le budget : une fuite de 0,06, qu'(a) et (b) manquent plus d'une fois sur deux, peut être un signe parfait sur 6 % des épisodes (point 5), assez pour être dangereuse.

## 2. Confiance

[PROPOSITION] 0,65 sur l'option (d) ; 0,85 sur les constats qui la portent. L'incertitude tient au coût d'une suspension et à la fuite jugée dangereuse, absents de la question.

## 3. Ce qui me ferait changer d'avis

- [CALCUL] Coût : si une suspension provisoire coûte, en plus de sa confirmation, moins d'environ 8 000 épisodes (quatre tests sur les mêmes épisodes) ou 44 000 (épisodes propres à chaque test), le seuil 0,05 au criblage devient moins cher à sensibilité égale ; je passerais à (c) plus confirmation, 1 % de suspensions durables par admission.
- [PROPOSITION] Budget plafonné à 4 000 : apprentissage croisé avec permutation de toute la chaîne, si réapprendre les trente prédicteurs est bon marché. [CALCUL] Simulation gaussienne, dix traits, un prédicteur, fuite 0,07, 300 répétitions : puissance 0,72 en moitié-moitié à 4 000, 0,87 en croisé à 4 000, 0,98 en moitié-moitié à 8 000 ; niveau sous le nul 0,050.
- [PROPOSITION] Conséquence : si toute levée exige une correction et une réadmission, chaque rejet devient durable ; je garderais le seuil corrigé et contrôlerais sur la vie (point 4).
- [CALCUL] Taille dangereuse : à 0,12 et plus en équilibré, (b) suffit (puissance 0,98) ; à 0,05, il faut 11 000 à 14 000 épisodes par test selon le seuil, 60 000 à 74 000 à 5 % d'audit : changer de plan, pas de seuil.
- [HYPOTHÈSE] Propriété du test : si les quatre tests partagent leurs épisodes et sont très corrélés, le maximum conjoint par permutation remplace Bonferroni ; si la confirmation ne peut pas réutiliser le prédicteur figé, elle perd son avantage.

## 4. Unité de contrôle de l'erreur

- [CALCUL] Le test : chaque garantie jugée seule ; 18,5 % de fausses suspensions par admission, 87 % sur dix admissions sous (a). [PROPOSITION] Engage à vivre avec des suspensions fréquentes ; ne convient qu'à un criblage bon marché et confirmé.
- [CALCUL] L'admission : au plus 5 % sur les quatre tests (Bonferroni, Holm, Šidák à 0,01274, ou maximum conjoint) ; engage 10,8 % de sensibilité ; l'erreur reste cumulative : 40 % sur dix admissions sous (b). [PROPOSITION] L'unité « secret » (deux tests à 0,025) se défend aussi, un rejet ne suspendant qu'une garantie.
- [PROPOSITION] La vie : au plus, par exemple, 5 % de fausse suspension sur toute la vie. Engage un plan fixé d'avance : dépense de ce niveau au fil des admissions, chacune plus sévère, ou test séquentiel à validité permanente (e-valeurs, inégalité de Ville), qui accumule en retour la preuve d'une fuite persistante ; suppose un nul défini pour toutes les versions du dispositif.
- [PROPOSITION] Ma recommandation : l'admission pour la suspension ; la vie pour deux règles. Aucune levée par simple réépreuve, seulement par la confirmation préétablie ou par correction documentée puis réadmission ; et en production, un test séquentiel sur les audits réels, à fausse alerte bornée sur la vie, contre la fuite apparue après l'admission.

## 5. Erreurs dans les chiffres et le raisonnement

- [CALCUL] Les six fuites du tableau se retrouvent avec précision équilibrée, Bonferroni sur trente prédicteurs, test unilatéral, approximation normale, variation totale égale au double de l'avantage (binomiale exacte : 0,085 et 0,094). Une seule s'écarte : (c) à 5 % donne 0,137, soit environ 0,14, pas 0,13.
- [CALCUL] 18,5 % vaut sous indépendance et n'est pas une borne : jusqu'à 20 % sous dépendance quelconque ; 9,75 % si les deux cibles d'un secret sont parfaitement liées.
- [CALCUL] La supposition « bras équilibrés » ne vaut que pour la colonne pile ou face : la colonne 5 % correspond à 100 épisodes audités sur 2 000.
- [CALCUL] Deux suppositions cachées tirent en sens contraires. Bonferroni sur trente est prudent : à corrélation 0,8 entre statistiques, le maximum exact donne 0,073 au lieu de 0,085. Le prédicteur appris égal à celui de Bayes est optimiste : dans la simulation, puissance 0,72 contre 0,92. [HYPOTHÈSE] À 5 %, avec une centaine d'audités dans l'apprentissage, l'écart grandit.
- [CALCUL] La variation totale mesure mal le danger du secret d'audit : un signe parfait (l'agent se sait non audité) sur une fraction f des épisodes non audités vaut f. Les 0,19 que (a) manque une fois sur cinq peuvent donc être un agent sûr de son impunité dans 19 % de ces épisodes. Une statistique de queue, le nombre d'audits parmi les k épisodes que chaque prédicteur juge les plus sûrs (trois valeurs de k, dans le maximum), retrouve un tel signe dès 7,4 % sous (a), contre 19 %, et dès 4,5 % sous (d), contre 15 % ; [HYPOTHÈSE] si le prédicteur isole la région. [CALCUL] Tirer l'audit à pile ou face pendant l'épreuve ramènerait 0,15 à 0,066, [HYPOTHÈSE] si la loi des observations n'en dépend pas.
- [HYPOTHÈSE] Pour la lecture du détecteur, si ce que voit l'agent détermine ses activations, la fuite en variation totale vaut 1 par construction : le test mesure une fuite utilisable par la famille, à rapporter comme telle ; l'agent, qui calcule ses propres états, peut faire mieux.
- [CALCUL] Si une épreuve neuve réussie lève la suspension sans rien combiner, la puissance d'une suspension durable tombe à 0,64 après une réépreuve, vers 0 sans borne.
- [PROPOSITION] Le non-rejet décrit le plan, pas le dispositif : rapporter une borne supérieure de confiance de l'avantage de la famille, jamais « fuite inférieure à 0,085 ». Une puissance de 0,8 est faible pour une garantie ; [CALCUL] à 0,95, (a) ne retrouve que 0,102.
- [HYPOTHÈSE] Les prédicteurs voient des épisodes produits par la politique réelle de l'agent ; un agent qui sonde activement (latences, traces d'audit) échappe à l'épreuve. L'exactitude vient du tirage pour le secret d'audit ; pour le détecteur, elle suppose des épisodes échangeables.

## Antériorités

[FAIT RAPPORTÉ] † : antériorité citée de mémoire, non vérifiée ; vaut aussi pour les procédures nommées plus haut.
- Classifieurs comme tests : Lopez-Paz et Oquab, 2017, « Revisiting Classifier Two-Sample Tests » † ; Kim, Ramdas, Singh et Wasserman, 2021, « Classification accuracy as a proxy for two-sample testing » † ; Gagnon-Bartsch et Shem-Tov, 2019, « The classification permutation test » (équilibre des covariables) † ; Ojala et Garriga, 2010, « Permutation tests for studying classifier performance » †.
- Multiplicité, deux temps, admission : Westfall et Young, 1993, « Resampling-Based Multiple Testing » † ; Bauer et Köhne, 1994, « Evaluation of experiments with adaptive interim analyses » † ; Dodge et Romig, 1929, « A method of sampling inspection » (risques du producteur et du client) † ; Schuirmann, 1987, « A comparison of the two one-sided tests procedure and the power approach… » † ; Hoenig et Heisey, 2001, « The abuse of power » †.
- Vie : Ville, 1939, « Étude critique de la notion de collectif » † ; Lan et DeMets, 1983, « Discrete sequential boundaries for clinical trials » † ; Vovk et Wang, 2021, « E-values: calibration, combination and applications » † ; Podkopaev et Ramdas, 2023, « Sequential predictive two-sample and independence testing » †.
- Le plus proche du choix posé : Goodwill, Jun, Jaffe et Rohatgi, 2011, « A testing methodology for side-channel resistance validation » (seuil de 4,5 écarts-types, confirmation sur deux jeux indépendants) † ; Whitnall et Oswald, 2019, « A critical analysis of ISO 17825 » (faux positifs et puissance) † ; Jagielski, Ullman et Oprea, 2020, « Auditing Differentially Private Machine Learning » † ; Steinke, Nasr et Jagielski, 2023, « Privacy auditing with one (1) training run » (une attaque ne borne la fuite que par en dessous) †.
- Fuite utilisable : Xu, Zhao, Song, Stewart et Ermon, 2020, « A theory of usable information under computational constraints » †.
- [HYPOTHÈSE] Je ne connais pas de travail sur le contrôle des agents qui traite ce choix de seuil et de budget ; l'absence dans ma mémoire n'est pas une absence dans le champ.

## Empreintes des calculs

[FAIT RAPPORTÉ] Bloc-notes de la session, non versé : `calculs_v1.py` f4b18fcb88549343cb463361d16a3ff0cf8d84a7cebdf5dcb59f2389799f8620 ; `calculs_v2.py` 15d206d86063fd6ee1e757dd3dade3932263fbebfc3a20cad516ce9c5107ac58 ; `calculs_v3.py` b9b620080be872e2028402f9eec6d132700e9eaa3cf0c39af2951b9f7ed2f92d ; `calculs_v4.py` 9a556ffbece22a13ab202082a582e243d824d17c6fcd377ff156ccc835f6ed74.
