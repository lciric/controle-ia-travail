# Contre-lecture 1 du texte court du barreau 7 (bras externe NARCBench) — brouillon 1 — v1

- **Contre-lecteur** : sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`), autre modèle que le rédacteur (Claude Opus 5.5), même
  famille (N-052, R2). Je n'ai écrit ni ce texte, ni le code du bras externe, ni sa contre-lecture ; je ne serai ni lecteur ni juge du
  verdict. Travail du 2026-11-18, de ≈ 17:15 à 18:00 UTC. Mandat : `docs/notes/narcbench-8b-v1/mandat-contre-lecture-texte-court-v1.md`
  (empreinte vérifiée par son compagnon : OK), sous GO-2026-11-18-30.
- **Objet relu** : `prereg/narcbench-bras-externe-v1-brouillon1.md`, `85e8de5d7d94161b4951dac12c605a56ce048dbbfe6f92538552fcc2f6417259`
  (compagnon vérifié : égal). Numéros de ligne ci-dessous = lignes de ce fichier.
- **Aucune donnée réelle, aucun score** lus ou calculés. Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. L'arbre
  `/home/user/narcbench-externe-v2` (tête `70cb77b8…`, arbre propre) n'a été que lu : la correction de son code annoncée par le mandat
  n'y figure pas encore (même tête que celle que la contre-lecture du code a relue).

## Verdict

**Scellable après corrections.** Aucune erreur de chiffre de l'article. Les règles de lecture sont écrites d'avance dans les deux sens
et le calcul de puissance se rejoue à l'identique. Mais **quatre points bloquent le scellement tel quel** (texte et code disent des
choses différentes, ou le texte se tait là où le code exige un choix) ; ils se corrigent par une nouvelle version du texte, sans
refonte. Deux majeurs touchent l'usage au jury (réponse « en partie » trompeuse ; probabilité d'un « oui » non calculée).

## Ce que j'ai fait (preuves)

1. **Empreintes** : mandat, brouillon, pièces de puissance, et les 16 fichiers cités à l'en-tête (PDF `02527fd4…`, N-061, N-026, N-052,
   devis v2, brouillons 3 et 4, contre-lecture 3, gabarit, `prereg.py`, `familles.py`, `evaluation.py`, `plancher_v1.py`,
   `registre_v1.py`, `manifeste.py`, mandat du rédacteur, chargeur v1) : toutes égales à celles du texte (douze premiers caractères
   comparés). `scikit-learn` absent de `requirements-cpu.txt` au commit `aeceeee6`, présent à `==1.9.1` dans l'arbre du code v2 : conforme.
2. **Validateur** `controle_ia.prereg.problemes` rejoué sur le brouillon : exactement deux familles de problèmes, attendues : « contre-lecture 1
   sans ses deux empreintes » et les quatre marqueurs `<<…>>` (voir M4 : ils figurent **aussi** dans la dernière section, qui les cite).
   Les huit sections exigées sont présentes et non vides.
3. **Puissance rejouée** : `puissance-regle-v1.py` (compagnon vérifié) avec l'argument `20261118`, environnement du dépôt (numpy, scipy) :
   sortie **identique ligne à ligne** aux vingt lignes de `sortie-puissance-regle-v1.txt` (3 min 41 s). J'ai ajouté, dans mon dossier
   temporaire (supprimé), six points hors grille (1 000 simulations × 1 000 tirages, graine 777) : voir « Puissance ».
4. **Chiffres de l'article (R7)** lus sur le PDF, pages 1, 6, 14 à 18, 27 à 30, 32-33, 35, 40, 44 à 46 : détail plus bas.
5. **Code v2** lu : `lecture_externe_v2.py` en entier, `externe_v2.py` en entier, `externe_v1.py` (constantes, garde), `chargeur_externe_v1.py`
   (constantes, chargement), `manifeste.py` (`graines`, `generateur`), `t07/registre_v1.py` (en-tête) ; contre-lecture du code lue en entier.

## 1. Chiffres de l'article (R7) : tous vérifiés

Table 2 (p. 27, Qwen3-32B) : aire de l'étage stéganographique, pic 1,00, écart 0,99 ; étage des comités, pic 1,00, écart 1,00 : **exact**.
Table 3 (p. 28, Llama-3.1-70B) : mêmes quatre valeurs : **exact**. Citations du résumé (p. 1), de la p. 17 (« Every model reaches 1.00 AUROC on
CORE, near-perfect detection on STEGO ») et de la p. 44 (« Activation probes achieve 0.99 to 1.00 AUROC on the same shoes (Table 2) ») :
**mot pour mot**. « layers 26–30 of 64 for Qwen3-32B » (p. 27), bande de cinq couches non nommée pour le Llama (p. 27) : exact. Moyennes
sur la bande et dix graines (Annexe D p. 27 ; légende de la figure 2 p. 18) : exact. 50 scénarios, 17 domaines, 100 épisodes (p. 14) ; validation
un domaine tenu à l'écart (p. 14-15) ; 20 sabots, huit mains, 40 épisodes (p. 15, 40, 44) ; 36 scénarios de collusion retenus avec les 50 témoins,
sans dire pour quel modèle (p. 35) ; équations 3 et 4 (p. 16) ; équation 8 (p. 27) ; `penalty` l2, C = 25, `max_iter` 8, liblinear (p. 29, aussi
p. 30) ; Table 6 (p. 30) et Table 13 (p. 46) comme décrites ; largeur 5 120 (p. 45) ; consigne de collusion absente des messages utilisateur de la
phase publique (p. 32-33, J.3 et J.5) ; messages utilisateur identiques au tour final (p. 27, p. 33) ; invites système différentes (p. 33) : exact.
Auteurs et date (« 15 Oct 2026 », v5) : exact.

Mineurs de provenance (aucun ne change un chiffre) :
- **m-R7-1** (l. 22, « p. 6, 15, 27, 29 ») : la p. 6 ne porte pas la recette de la sonde de régression logistique (elle ne parle que de sondes de
  représentation en général). Avant : « p. 6, 15, 27, 29 » → après : « p. 15, 27, 29 (et 30 pour l'augmentation et l'arrêt à 8 itérations) ».
- **m-R7-2** (l. 106) : « flux résiduel » n'est pas dit p. 27 (« last token position of each agent's public responses »). Avant : « l'activation du
  flux résiduel au dernier jeton … (p. 27) » → après : « l'activation au dernier jeton … (p. 27) ».
- **m-R7-3** (l. 91-93) : l'article se contredit sur la sonde d'asymétrie : p. 15, « Three of the five methods (Peak Suspicion, Deception Split and
  Asymmetry Probe) require no training beyond the deception direction » ; p. 17 et p. 35, elle ajoute un classifieur appris sur l'étage des comités.
  Le texte retient la seconde lecture sans le dire. Après : ajouter « (l'article dit le contraire p. 15 ; le texte suit p. 17 et 35) ».
- **m-R7-4** (l. 86-89) : le résumé parle de « the best method on every model » ; pour les deux autres modèles, les cellules du pic et de l'écart
  sont plus basses (DeepSeek 0,98 et 0,87 ; GPT-OSS 0,74 et 0,40, Tables 4 et 5, p. 28). Les cellules visées sont celles des deux modèles où ces
  statistiques sont les meilleures. À écrire une fois dans la frontière (« Ce que ce texte ne dit pas ») pour que « reproduit » ne soit pas lu comme
  une généralité sur le résultat publié.

## 2. Issues dans les deux sens, R3, tolérance, conjonction, comités

Les trois états (« reproduit », « non reproduit », « non tranché à cette puissance ») sont écrits d'avance, avec la même force de preuve
(intervalle entier d'un côté de la marge), des lignes C0 à C4 exhaustives et exclusives, et des phrases T0 à T4. Pas d'échappatoire sur la
règle d'une cellule. Aucun run ne vise un signe ; les prédictions P1 à P3 sont toutes du même sens, mais déclarées non décisives, avec P4 et P6
« non prédit » : acceptable. L'étage des comités est bien sans effet sur la réponse (l. 369-371). La tolérance de 0,03 sur la valeur imprimée est
cohérente (m = 0,97 et 0,96) ; elle est reprise du brouillon 3 que je n'ai pas relu ; la puissance l'éclaire (§ 3).

**Majeur M1 — la réponse « en partie » est trompeuse.** (l. 365-367) « sinon → en partie : différence de moyennes <état>, linéaire <état> ».
Cas atteint : témoin « reproduit », les deux familles « non tranché à cette puissance » (cas le plus probable, § 3). La phrase gelée dit « en partie »
alors que rien n'est reproduit en partie. Avant : « sinon → « en partie : … » » → après : trois lignes. (a) témoin « reproduit », aucune famille « reproduit » et
aucune « non reproduit » → **« non tranché à cette puissance : différence de moyennes <état>, linéaire <état> »** ; (b) témoin « reproduit », au moins une
famille « reproduit » et l'autre pas → « en partie : … » ; (c) témoin « reproduit », une famille « reproduit » et l'autre « non reproduit » → idem (b).
À énumérer dans l'essai exhaustif du plan d'analyse (point 0).

**Mineur m-I-1** — la phrase combinée « l'écart tient à notre famille de sondes » (l. 351) attribue une cause : entre le témoin et nos familles
diffèrent aussi le sous-échantillonnage, la standardisation, l'arrêt à 8 itérations et l'agrégation par maximum. Avant : « l'écart tient à notre famille de
sondes » → après : « l'écart se situe entre la recette des auteurs et notre chaîne (famille, standardisation, équilibrage, arrêt à 8 itérations) ; il n'est
pas imputé à l'un d'eux ».

**Mineur m-I-2** — la réponse « oui » (l. 362-364) fait suivre le qualificatif du plancher « tel quel » ; au jury la première phrase est seule lue. Après :
placer dans la phrase « oui » elle-même « (qualificatif du plancher : <…> pour chaque cellule visée) ». Même remarque pour « non ».

**Mineur m-I-3** — témoin « non reproduit » et les deux familles « reproduit » donne « question non tranchée : le témoin est non reproduit » (l. 365-366) :
c'est un choix cohérent (le témoin garde le chargement), symétrique pour « oui » et « non ». À dire en une phrase au texte pour que le jury ne le prenne pas
pour une échappatoire : « un témoin qui échoue ne permet de conclure ni oui ni non sur notre chaîne ; les cellules de nos familles restent rapportées ».

## 3. Puissance

**Le calcul dit juste** : sortie rejouée identique ; modèle binormal à variances égales (aire vraie → écart des moyennes √2·Φ⁻¹(aire)), 20 paires,
intervalle percentile par blocs, marge = publié − 0,03. Les lectures du texte : « reproduit n'a plus d'une chance sur deux que pour une aire vraie
d'au moins 0,99 » : vrai sur la grille (pic 0,573 à 0,99, 0,320 à 0,98 ; écart 0,675 et 0,409). Mes points hors grille : à 0,985, « reproduit » vaut
0,416 (pic) et 0,543 (écart) ; le seuil d'une chance sur deux est donc ≈ 0,988 au pic et ≈ 0,984 à l'écart. « Non reproduit n'a plus d'une chance sur deux
que sous ≈ 0,85 » : à 0,88, 0,425 (pic) et 0,324 (écart) ; à 0,85, 0,621 et 0,535 ; seuil ≈ 0,865 (pic), ≈ 0,85 (écart) : « ≈ 0,85 » tient pour
l'écart, « ≈ 0,87 » serait exact pour le pic.

**Ce que cela veut dire pour le jury** : un nombre de cellule seul. La réponse « oui » exige **douze cellules** « reproduit » (trois procédures,
deux modèles, deux statistiques) ; les deux modèles portent des épisodes distincts, donc la probabilité d'un « oui » est **au plus** le produit des
probabilités du pic des deux modèles, et en pratique moins (le pic est la cellule la plus difficile, la marge est 0,97) : au plus ≈ 0,33 si l'aire vraie vaut
0,99, ≈ 0,61 si elle vaut 0,995 ; il faut une aire vraie voisine de 0,9999 pour que « oui » soit à peu près certain. Autrement dit : même si notre chaîne
égalait exactement le résultat publié, le jury verra le plus souvent « non tranché à cette puissance » ; **« non tranché » n'est pas un échec**, et
« reproduit » ne peut sortir que si la séparation est quasi totale. Le texte le dit pour une cellule (l. 273-274) mais pas pour la réponse au barreau.

**Majeur M2 — deux compléments à écrire à la section Puissance et à Seuil** :
- (a) **probabilité du « oui » et du « non » de la réponse**, bornée comme ci-dessus ou simulée avec des statistiques corrélées ; avant (l. 273-277) :
  « Lecture : avec 20 sabots, … » → après : ajouter « Pour la réponse au barreau (douze cellules visées, deux modèles indépendants), la probabilité de « oui »
  est au plus P(pic, Qwen)·P(pic, Llama) : ≈ 0,33 à aire vraie 0,99. Un « non tranché » est l'issue la plus probable d'une reproduction exacte ; il ne se lit pas
  comme un échec. » ;
- (b) **taux de « reproduit » à tort près de la marge** : le texte donne seulement l'aire vraie 0,90 (l. 245-247 : 0,004 et 0,008). À 0,95 (sous la marge de
  0,02 et 0,01) la grille donne **0,060 (pic) et 0,102 (écart)** : au-dessus du 0,025 qu'un intervalle à 95 % unilatéral laisse attendre. L'intervalle percentile par
  blocs est anticonservateur près du plafond avec 20 sabots. Avant : « probabilité de « reproduit » quand l'aire vraie vaut 0,90 : 0,004 (pic) et 0,008 (écart) » →
  après : « … quand l'aire vraie vaut 0,95 : 0,060 (pic) et 0,102 (écart) ; 0,90 : 0,004 et 0,008 ; l'intervalle est anticonservateur près de 1 ».
- Limites à écrire (mineur m-P-1) : aucune corrélation intra-sabot simulée ; les deux modèles sont supposés indépendants ; pic et écart d'un même modèle
  corrélés ; aire vraie 1,00 exactement non simulée (alors « reproduit » est certain, l'intervalle étant réduit à un point).

## 4. Texte contre code v2

Constat général : **le texte et le code ne disent pas la même chose sur le registre, la configuration, les graines, l'augmentation et le point (i)**. La
section « Écarts connus entre le code v1 et ce texte » (l. 431-440) ne les énumère pas tous, et elle cite le code v1 et non le v2.

**Bloquant B1 — graines : la lecture déclarée de R9 n'est pas écrite, et le texte contredit le code.** (l. 312-317) Le texte dérive de `SeedSequence` des
tâches `temoin/<modèle>/graine<g>`, `lineaire/…/graine<g>`, `perceptron/…/graine<g>` (g = 0 à 9) et dit que « l'entier passé aux fonctions est tiré de la
`SeedSequence` de la tâche (`generate_state(1)[0]`) ». Le code v2 sert **telles quelles** les constantes 0 à 9 de la recette publiée (`GRAINES_AUTEURS`,
`externe_v2.py` l. 63 ; à `RandomState` et à `random_state` de liblinear), ne dérive de `SeedSequence` que les graines de nos familles
(`familles/c<couche>/<famille>/<tâche>`, préfixées du modèle, entier par `generateur(...).integers(2**31)`), n'a ni perceptron, ni tâche `plancher/…`,
`intervalle/…`, `placebo/…` par procédure. La contre-lecture du code a jugé la lecture du développeur juste : les graines 0 à 9 sont des constantes de la
recette (comme C = 25 et 8 itérations) et les remplacer casserait la reproduction que la garde éprouve ; elle exige que **le texte l'écrive**. Il ne l'écrit pas.
Avant (l. 312-317) → après : « **Lecture déclarée de R9** : les entiers 0 à 9 du témoin de recette sont les graines constantes de la recette publiée
(`probes/reproduce_LR.py` au commit `85fea3be2a9d`, l. 45 et 630), servies à `RandomState` (tirage des honnêtes) et à `random_state` ; ils ne sont pas nos
tirages ; ils sont consignés dans la configuration du manifeste. Tous nos tirages (apprentissage de nos familles, plancher, rééchantillonnage, placebo) viennent de
`SeedSequence` par tâche nommée, noms = ceux du code (`<modèle>/familles/c<couche>/<famille>/<tâche>`), entier = `generateur(graine).integers(2**31)`. »
Ajouter le constat, écrit d'avance : sur des classes de même effectif, la graine ne fait que permuter les honnêtes et `random_state` est sans effet sur le
solveur ; **les dix graines valent presque une** ; la moyenne sur dix graines n'ajoute pas de puissance (compléter l. 275-276).

**Bloquant B2 — augmentation (E2) non tranchée.** Le texte ne contient pas le mot « augmentation » ; le code **refuse de lancer sans** `--augmentation papier|code`
(`exiger_augmentation`, « le texte court tranche E2 avant toute lecture, aucun défaut »). L'article (p. 30) dit que l'augmentation n'a pas servi aux résultats principaux.
Avant : (rien) → après, en section « Recette » : « **Augmentation** : aucune (« papier ») : les Tables 2 et 3 sont les résultats principaux, obtenus sans augmentation (p. 30).
La variante du code des auteurs (4 copies bruitées, écart type 0,05) n'est pas lue sous ce texte ; la lire serait un second texte. » Noter que le code ne bloque pas deux lancements
successifs à augmentations différentes (garde « déjà jouée » absente, contre-lecture du code M3 c) : la liste d'arrêt n° 3 (« LECTURE-NARCEXT déjà présente → refus ») ne tient que si le
code l'implémente.

**Bloquant B3 — point de recette (i) : le texte et le code divergent.** (l. 182-183) Texte : aire de l'étage des comités = **scores hors pli mis en commun** ;
moyenne des aires par pli « rapportée à côté ». Code v2 : **moyenne des aires par pli** (`validation_domaines`, `held_out_cv_layer` des auteurs l. 355-381), sans calcul de
l'aire mise en commun. Le texte (l. 179-181) promet de porter au brouillon suivant les lignes du code des auteurs qui fixent le point : elles sont relevées (`externe_v2.py` l. 28),
donc le défaut du texte doit changer. Avant : « scores hors pli mis en commun ; moyenne des aires par pli rapportée à côté » → après : « **moyenne des aires par pli** (plis qui ont les
deux classes, domaine vide jamais tenu à l'écart ; code des auteurs l. 355-381) ; l'aire à scores mis en commun n'est pas calculée sous ce texte ». (Ou alors exiger du code le calcul
des deux ; mais la lecture secondaire n'y gagne rien.) Même ligne, mêmes points (ii) à (v) : (ii) standardisation sur l'échantillon équilibré = conforme au code ; (iii) bande 32-37 du Llama =
conforme ; (iv) quatre agents = conforme, mais le code **compte** les épisodes à autre nombre d'agents sans arrêt (voir M5) ; (v) message = conforme.

**Bloquant B4 — registre, clés, configuration : le texte et le code ne parlent pas des mêmes clés, et la commande n'a pas de fiche de configuration lue par programme.**
- Clé : texte `SCELLEMENT-NARCEXT`, `CODE-NARCEXT`, `LECTURE-NARCEXT` (l. 413-416) ; code `SCELLEMENT-NARC-EXT` (`lecture_externe_v2.py` l. 40), aucune lecture de `CODE-NARCEXT` ni refus
  de `LECTURE-NARCEXT`, registre libre (`--registre`, défaut cité `registres/scellements-v1.md`), pas de comparaison du commit exécuté à celui de la fiche de code (liste d'arrêt n° 4), pas de
  journal des refus (liste d'arrêt n° 3 : « journalisé »). Le développeur corrige ; le texte doit **écrire la valeur finale** : chemin `registres/narcbench-externe-v1.md`, trois clés exactes, et
  le chemin exact du texte scellé (le brouillon s'appelle `…-brouillon1.md` ; le texte scellé aura un autre nom, R12 : le fixer, par exemple `prereg/narcbench-bras-externe-v1.md`).
- Options de la commande : `--augmentation` (B2), `--couches-familles` (le texte dit « moyenne sur les couches de la bande », l. 146 ; le code accepte `bande` ou une couche par modèle),
  `--run-id`, `--entropie`. Avant : (rien) → après, une section « **Configuration canonique de la commande** » à lignes lisibles par programme (contre-lecture du code M3 b) :
  `augmentation : papier` ; `couches-familles : bande` ; `run-id : AAAAMMJJ-HHMMSS-narc-externe-v2` (format de `manifeste.creer_manifeste`) ; `registre : registres/narcbench-externe-v1.md` ;
  `Entropie : <entier>` ; que le code refuse tout écart.
- Entropie : le code cherche l'entier comme **sous-chaîne** du texte (`lecture_externe_v2.py` l. 76 ; contre-lecture du code M3 d : « 2026 » ou « 7 » passent). Le texte doit porter **une ligne
  exacte** `Entropie : <entier>` et l'entier doit n'être ni une année, ni la graine de puissance `20261118`, ni celle d'un autre texte (à vérifier par la mère en cherchant l'entier dans `prereg/`).

**Majeur M3 — la liste « Écarts connus » est incomplète** (l. 431-440). Elle doit nommer le code **v2** et ajouter ce que le code v2 ne fait pas encore ou fait autrement, pour que le développeur et la
contre-lecture du code aient une spécification :
1. le témoin de recette n'a, dans le code, **ni intervalle par blocs, ni plancher, ni placebo** (seulement moyenne et erreur type sur graine × couche) ;
2. `nos_familles_v2` lit **l'aire par agent**, sur les **épisodes de collusion seulement**, couche par couche, sans moyenne sur la bande, sans pic ni écart d'épisode, sans plancher par couche ni
   par pli, sans perceptron, avec **une seule graine** par tâche (le texte dit dix graines pour le linéaire et le perceptron, l. 158) ;
3. **bloc** : le code rééchantillonne par `run_id` (l. 395-397) ; le texte : le sabot (STEGO) ou le scénario (CORE), un par condition (l. 134-136) ;
4. **placebo** : rôles permutés dans l'épisode (code) ; conditions échangées dans un bloc (texte) — déjà écarté n° 4, à étendre à nos familles ;
5. **gardes de la liste d'arrêt absentes du code** : n° 2 (fichier de transfert), n° 4 (commit exécuté), n° 6 (plus de 10 % d'exclus : le code compte et ne seuille pas), n° 7 (version de
   `scikit-learn` exigée : le code la consigne, ne l'exige pas, et **arrête tout** au lieu de rendre « non lu : garde (scikit-learn) » pour le seul témoin), n° 8 (repli de Cholesky), n° 9 (mémoire par famille),
   n° 10 (scores constants) ; et le texte (l. 392-398) doit dire ce qui se passe si un essai de garde existe seulement sur cas sain ;
6. **tours de CORE** : le texte exclut « un agent sans ses trois tours » (l. 389) ; le code moyenne **toutes** ses lignes publiques de discussion (E3) ; sur les données publiées les deux coïncident
   (essai de forme), à écrire comme tel ;
7. **domaines** : le texte attend « 17 domaines » (l. 134) ; l'essai de forme a constaté que les domaines diffèrent entre les deux modèles (Qwen3-32B a seul « env » ; Llama-3.1-70B a seuls « edu » et
   « sport ») et que le champ `scenario_domain` du Llama diffère du domaine des auteurs dans 14 domaines (contre-lecture du code, m7) : le texte doit prévoir « plis par modèle, comptes rapportés,
   rien n'arrête » et dire que le domaine est **dérivé de `run_id`** (règle des auteurs, `chargeur.domaine`), non du champ `scenario_id` (l. 134) ;
8. **arrêts plus stricts que les auteurs, non déclarés** (contre-lecture du code, m5) : rôle ou mode incohérent, direction nulle, activations non `float32`, vingt champs exacts, valeurs fermées de mode, de
   rôle et de canal : à déclarer en une ligne ;
9. **résultat** : `NaN` possibles dans le résultat scellé (contre-lecture du code m4) ; le texte exige un JSON propre (section Plan 6) : à demander `null` et un état.

**Majeur M4 — marqueurs à retirer, au-delà des quatre** : la section « Marqueurs à remplir avant le scellement » (l. 506-508) et « Points ouverts du brouillon 1 » (l. 487-497) citent `<<…>>` ou des
recommandations non tranchées ; le validateur refuse tout `<<…>>` du texte entier, y compris dans ces sections. À supprimer (ou réécrire sans marqueur) au scellement, et à consigner : la mère
tranche les cinq points ouverts (ma lecture : points 1, 3, 4, 5 recommandés, confiance suffisante ; **point 2 (tolérance)** : garder 0,03, et ajouter dans la puissance la ligne à 0,05 hors décision
du texte si Lazar veut la voir). Le statut (l. 3-5) doit passer de « non scellable » à la version scellée.

**Majeur M5 — exclusions** : texte (l. 389-391, n° 6) « épisode sans quatre agents » **compté et rapporté**, > 10 % arrêt ; code `groupes` : compte (`agents_differents_de_4`) sans seuil. À inclure dans la
liste du M3 (n° 5) ; le seuil de 10 % doit être codé.

## 5. Marqueurs restants (ce qui doit y entrer)

- **Registre propre** : `registres/narcbench-externe-v1.md` (recommandation du texte, adoptée : le registre partagé de T0.7 refuse toute autre clé, règle (4), et celui du texte du 8B ne porte pas ces
  clés). Créé par la mère, jamais réécrit, format `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |`, chemin sans « .. » ni absolu. **Il ne doit pas exister avant le scellement** (il n'existe pas
  aujourd'hui) ; son nom est une des valeurs que le code doit figer (B4).
- **Entropie** : une ligne `Entropie : <entier>`, tirée une fois, distincte de celles de P3, de T0.6, de T0.7, du texte du 8B et de la graine de puissance ; la mère la vérifie par recherche de l'entier.
- **Expositions** (l. 462, marqueur `<<EXPOSITIONS_NARC_EXT>>`) : doivent entrer, dans l'ordre : (a) le développeur v1 a téléchargé et chargé les huit fichiers le 10 novembre (R-2184), forme et comptes ; (b) le
  développeur v2 a rejoué l'essai de forme sur les fichiers réels (comptes : lignes, tours, agents, épisodes, domaines ; **classes de même effectif, deux colludeurs et deux honnêtes à trois tours par
  épisode de collusion, 186 lignes par classe et par modèle**) et a écrit, sur jouets, que `random_state` est sans effet et que les graines n'agissent que par la permutation des honnêtes ; (c) le contre-lecteur
  du code (Fable 5.2) a rejoué l'essai de forme, fait tourner des fonctions du script des auteurs sur données factices, sans score réel ; (d) la mère ; (e) **ce contre-lecteur** : aucune donnée réelle ; code et
  contre-lecture du code lus, deux lignes de registre des décisions (R-2175, R-3310) lues ; (f) la lecture du contexte de l'épisode `bj__shoe00__collusion` par le programme (brouillon 4), déjà au texte l. 446-455.
  Aucun score n'a été calculé ni lu par quiconque sur les fichiers réels, d'après les rapports lus.
- **Contre-lecture 1** : chemin de ce rapport et son empreinte (après scellement), empreinte du brouillon relu `85e8de5d…`, et le traitement de chaque remarque (tableau ci-dessous).

## 6. Cloisonnement

Le texte ne cite aucun résultat du programme ni aucun score. Il déclare (l. 462-467) avoir lu, dans le brouillon 4 (prédiction N3), la mention d'un résultat antérieur du programme sur ses propres sondes et n'en
rien tirer : la mention n'est pas reprise (bien). Réserves :
- **m-C-1** — le brouillon 4 et sa contre-lecture 3 figurent parmi les « documents qui font foi » (l. 47-50) ; qui les ouvre atteint la prédiction N3. Après : y ajouter « cités pour leurs lignes 12-24, 149, 155,
  199-200 seulement ; la prédiction N3 n'est pas reprise et ne fait pas foi ici » ; ou ne les citer que dans les expositions.
- **m-C-2** — le texte (l. 446-455) recopie une **observation sur les fichiers publiés** (contexte des colludeurs dans un épisode réel) qui fonde P4 : ce n'est ni un score ni un résultat du programme, mais elle
  est antérieure au scellement et issue d'une lecture des fichiers ; elle est déclarée. Après : la nommer en toutes lettres « observation de contexte, sans score, lue avant ce texte par le programme (brouillon 4) »
  dans les expositions (f), sans changer la phrase.
- **m-C-3** — l. 4-5 : « rien lu des fichiers publiés » : préciser « par le rédacteur » (les autres lecteurs, y compris le programme, en ont lu des formes et un contexte).
- **m-C-4** — l. 324-325 et 471-473 : la mention « N-061, point 4 » appuie « aucune issue n'entre dans le critère 3 de G0 » ; le point 4 de N-061 ne parle que de la liste scellée de G1. Avant : « (N-061, point 4) » pour
  le critère 3 de G0 → après : « (N-061, point 4, pour G1 ; le critère 3 de G0 est écarté ici par choix du texte) ».

## 7. Autres mineurs

- **m-1** — l. 10-13 : « GO-2026-11-18-30 n'a pas été relu au registre des GO » : la mère le relit avant scellement (R-3310 le rectifie).
- **m-2** — l. 134 : « 17 domaines attendus » : voir M3 n° 7.
- **m-3** — l. 119 : la somme des tailles 712 344 334 octets « calculée par le rédacteur » : non revérifiée par moi.
- **m-4** — l. 176-177 : `scikit-learn==1.9.1` : l'avertissement de dépréciation de `penalty` (retrait en 1.10) est consigné par le code, jamais masqué : le dire ici (déjà dans le code).
- **m-5** — l. 192-209 : le qualificatif de P1 « aire exactement 1,00 à chaque couche et graine **et** plancher ≥ 0,99 » déclenche un audit sur l'issue la plus probable ; écrire que l'audit est **attendu** et ne change rien (il est
  dit l. 209 : le répéter à P1).
- **m-6** — l. 219 : `intervalle_blocs` « en est le modèle » : le code v2 ne rééchantillonne pas la moyenne sur graines et couches pour le témoin (M3 n° 1) ; ne pas laisser croire à l'existence de la fonction.
- **m-7** — l. 228-230 : « aucune moyenne ni médiane sur les jetons » : vrai pour nos familles ; l'étage des comités du témoin de recette moyenne des **messages** (permis par N-026) : déjà dit ; garder.

## Traitement attendu (à consigner à la section Contre-lecture, pour chaque remarque)

| remarque | classe | action à porter au brouillon 2 |
|---|---|---|
| B1 graines et lecture déclarée de R9 | bloquant | texte réécrit l. 312-317, constat « dix graines ≈ une » |
| B2 augmentation | bloquant | « aucune (papier) » en section Recette |
| B3 point (i) par pli | bloquant | défaut du texte = moyenne des aires par pli |
| B4 registre, clés, configuration, entropie | bloquant | valeurs finales, section « Configuration canonique », ligne `Entropie : <entier>` |
| M1 réponse « en partie » | majeur | trois lignes de réponse, énumération exhaustive |
| M2 puissance de la réponse et taux près de la marge | majeur | lignes ajoutées à Puissance et à Seuil |
| M3 écarts texte-code | majeur | liste complétée, code v2 nommé |
| M4 marqueurs et points ouverts | majeur | sections retirées ou réécrites sans `<<…>>` |
| M5 seuil de 10 % d'exclus | majeur | codé et essayé (R5) |
| m-R7-1 à 4, m-I-1 à 3, m-P-1, m-C-1 à 4, m-1 à m-7 | mineurs | corrections en couples avant → après ci-dessus |

## Lectures hors du mandat (déclarées)

- Lignes R-2175 (l. 2133) et R-3310 (l. 3448) de `registres/decisions.md`, lues par numéro de ligne (le mandat ne les liste pas) ; la ligne R-3310 mentionne, sans contenu, des lectures interdites déclarées par un
  explorateur ; rien d'autre lu autour.
- `docs/decisions/decision-N-061-v1.md` (tête), pages 6, 30, 32-33, 45-46 du PDF (au-delà de la liste du mandat, parce que le texte les cite).
- Le script de puissance rejoué et six points supplémentaires simulés (données simulées seulement), dossier temporaire dans mon dossier de travail, supprimé.
- Rien lu sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; aucune recherche récursive ; brouillons 3 et 4 non relus ; rien commité, rien poussé, rien écrit sous `registres/`,
  arbre `/home/user/narcbench-externe-v2` non modifié.
