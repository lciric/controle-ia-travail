# Contre-lecture 3 (vérification courte) du texte court du barreau 7 (bras externe NARCBench) — brouillon 3 — v1

- **Vérificateur** : sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`), autre modèle que le rédacteur (Claude Opus 5.5), même famille
  (N-052, règle R2). Je n'ai écrit ni ce texte, ni le code du bras externe, ni leurs contre-lectures 1 et 2 ; je ne serai ni lecteur ni juge
  du verdict. Travail du 2026-11-18, de ≈ 19:36 à ≈ 19:50 UTC. Mandat : `docs/notes/narcbench-8b-v1/mandat-verification-courte-brouillon3-texte-court-v1.md`
  (empreinte `097a9e21…` vérifiée par la commande du dépôt : conforme).
- **Objet relu** : `prereg/narcbench-bras-externe-v1-brouillon3.md`, `fae8a96ccc75e592e8ca12c5b156a19775388c14f345d94fbf77d6fd8cbc0a90`
  (compagnon vérifié : égal). Brouillon 2 `7bb21dc0…` et contre-lecture 2 `f813ece0…` : compagnons vérifiés, égaux. Les numéros de ligne
  sont ceux du brouillon 3.
- **Aucune donnée réelle, aucun score.** Rien sous `/home/user/narcbench-donnees-v2/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`,
  `registres/`. Aucun fichier existant modifié, ni commit, ni poussée. L'arbre `/home/user/narcbench-externe-v2` n'a été lu que par
  `git show` / `git archive` au commit `cde3b9906881b6a26dba2d8486b46ac734d92371` (extraction dans un dossier temporaire à moi, supprimé à la fin).
  Empreintes des trois modules de lecture à ce commit, recalculées : `lecture_externe_v2.py` `f5a8c97b…`, `cellules_externe_v2.py` `9d81fdf9…`,
  `externe_v2.py` `b1054e22…`, `chargeur_externe_v1.py` `9193b787…`, `externe_v1.py` `69dfdd24…`, `statistiques_v1.py` `fa9970d7…`,
  `requirements-cpu.txt` `d236a393…` : **toutes égales à celles du texte**.

## Verdict

**Scellable après ces couples exacts** (§ 7). Aucun bloquant. Les cinq majeurs de la contre-lecture 2 sont traités aux endroits que dit le
tableau, sauf un point : la correction de M3 introduit une phrase que le calcul de puissance scellé ne soutient pas (« non tranché est
l'issue la plus probable », fausse à une aire vraie de 0,995). Le reste : un écart texte-code (la « révision du jeu » n'est pas gardée par le
code) et trois différences mineures. La réserve de la phrase « oui » est exacte (rejouée). La commande `verifier-texte` répond code 0. Le
validateur ne signale que les trois marqueurs prévus.

## 1. Les remarques de la contre-lecture 2 : traitement

Chaque ligne du tableau « Contre-lecture 2 » (lignes 926-947) relue contre le texte et le code.

- **M1** (configuration illisible par le code) : traité à l'endroit dit. Voir § 4 : code 0. Le brouillon 2, essayé de même, est refusé (code 2,
  prose dans la section), comme le tableau le dit. Les quatre points (a) à (d) de la contre-lecture 2 sont fermés : six lignes seules, clé `texte`
  lue par le code, `run-id` donné comme forme (l. 315-317), entropie ≥ 2³² (l. 321). **Mineur** : la note dit « avec la date et l'heure UTC du
  lancement » ; le code ne vérifie que la validité de la date et de l'heure, pas qu'elles sont celles du lancement (§ 7, C5).
- **M2** (tolérance d'arrondi) : traité (l. 392-396) ; les quatre comparaisons sont celles du code (`regle_c` : `bas >= m - ARRONDI`,
  `haut < m - ARRONDI` ; `au_dessus_du_plancher` : `bas > q95 + ARRONDI` ; `placebo_declenche` : `bas <= q95 + ARRONDI` ; `ARRONDI = 1e-9`). Les
  lignes de la table C (l. 553-557) restent écrites « bas ≥ m », « haut < m » sans la tolérance ; elles renvoient à « Seuil » (l. 387-396), où elle est
  dite. Acceptable ; une demi-phrase « (à 10⁻⁹ près, section « Seuil »)» dans la table fermerait toute lecture littérale (suggestion, pas un couple).
- **M3** (phrase trop générale) : **traité, mais la formule adoptée est elle-même non soutenue** : § 2, point F. Couple C1.
- **M4** (réserve hors des phrases gelées) : adopté pour la phrase de réponse R1, non adopté pour la ligne C2, avec une raison écrite (l. 931 et
  600-603 : « reproduit » est l'étiquette que lisent les règles T et R ; la réserve voyage avec la phrase de réponse que recopie le lecteur des
  issues). Raison recevable. Valeur de l'écart à sa marge : 0,160, **rejouée avec le script scellé** (§ 2, point A). Reste une lacune de
  cohérence, non bloquante : la phrase par famille F1 (« notre chaîne (famille F) reproduit le résultat publié… ») est gelée sans la réserve ; le lecteur
  qui ne lit que F1 ne la voit pas. Au choix de la mère : ajouter la réserve à F1 (changement de phrase gelée, que le code devrait suivre) ou la
  laisser telle quelle, la réponse au barreau étant la phrase qui porte la conclusion.
- **M5** (écarts texte-code A19 à A30) : lus un à un contre le code (§ 4, § 5) ; tous fermés comme le texte le dit (A19 `comptes_structurels` ;
  A20 `exiger_roles_episodes` appelée pour les deux étages de chaque modèle ; A21 `MemoryError` attrapée dans `main`, arrêt code 1 ; A22 `constants` :
  non finis → `GardeArret`, constants → « non lu : garde (scores constants) » ; A23 `journaliser` ; A24 toute autre clé du registre refusée ; A25
  `exiger_scikit_learn` arrêt avant toute lecture ; A26 `exiger_code_de_la_fiche`, paquet exécuté comparé fichier pour fichier ; A28 exclusions et
  rôles sur les métadonnées avant le manifeste ; A29 numéros du brouillon 2 cités par le code ; A30 `fullmatch` sur la ligne). Restent seules la phrase
  R1 et la tête finale, comme le texte le dit (l. 744-750). Aucun module de `src/` n'a changé entre `cde3b990` et la tête actuelle de la branche
  (`b46c678d` : deux commits d'essais et de pièces ; `git diff --stat` entre les deux commits, lecture seule).
- **Mineurs m-D1 à m-D6, m1, m2, m4, m5, m6, pièces hors de `main`, précision de la p. 30** : tous au tableau, à l'endroit dit. Contrôle des
  empreintes des pièces citées existantes dans `main` (vingt-deux fichiers : `prereg.py`, `familles.py`, `evaluation.py`, `plancher_v1.py`,
  `registre_v1.py`, `manifeste.py`, gabarit, N-026, N-052, N-061, brouillons 1, 3 et 4, contre-lectures, devis, mandat du rédacteur, PDF) :
  **toutes égales au texte**. Les quatre pièces de la branche (rapport du développeur, relevé de recette, manifeste des données, relevé des
  licences) sont **absentes de `main`** : le texte le dit (l. 91-99 et plan n° 0) ; la mère doit les y faire entrer avant le scellement, comme elle
  le sait.

## 2. Aucune échappatoire neuve (R3) ; la réserve de la phrase « oui »

Comparaison du brouillon 2 au brouillon 3 (diff de 595 lignes modifiées) : ce qui touche aux issues, à la tolérance et à la règle d'une cellule.

- **Issues écrites dans les deux sens** : inchangées. Règle C (C0 à C4), règle T, lignes R0 à R5 : exhaustives et exclusives (énumérations du code
  rejouées : règle C : 84 combinaisons sur cinq lignes ; règle T : 625 combinaisons sur cinq lignes, T1 et T2 à un cas chacune ; réponses : 32 805 combinaisons sur six lignes, R1, R2 et R5 à un cas chacune). Rien de neuf
  qui permette de choisir l'issue après coup.
- **Tolérance de 0,03** : inchangée (marges 0,97 pic, 0,96 écart ; `TOLERANCE = 0.03`, `PUBLIES` du code : 1,00 / 1,00 en comités, 1,00 / 0,99 à
  l'étage stéganographique, pour les deux modèles : égal aux Tables 2 et 3).
- **Comparaisons à 10⁻⁹ près** : symétriques (elles élargissent « reproduit » de 10⁻⁹ et élargissent « non reproduit » de 10⁻⁹ **dans le même sens**, sous
  la marge : `haut < m − 10⁻⁹`). Effet pratique nul hors égalité exacte à l'arrondi près ; aucune porte dérobée.
- **Deux familles en conjonction** : inchangée (R1 exige les huit cellules, R2 les huit ; le témoin d'abord, R0).
- **Nouveautés du brouillon 3 qui touchent au jeu d'issues** : (i) la réserve ajoutée à R1 ; (ii) gardes n° 8 et 9 jouées avant le manifeste (un arrêt
  avant le manifeste ne lit aucun score : aucune relance ne dépend d'un résultat ; le texte l'écrit, l. 625-630) ; (iii) règle DF-02 (le commit exécuté
  peut être un descendant du commit de la fiche, à paquet égal) : le paquet exécuté doit être identique fichier pour fichier, et la ligne « déjà jouée »
  ferme toute relance : pas d'échappatoire ; (iv) journal tenu par le code (A23). Aucune ne favorise un signe.
- **Asymétrie de la réserve** : R1 porte une réserve sur son taux d'erreur, R2 n'en porte pas. Elle est justifiée par les nombres scellés : « non
  reproduit » à tort quand l'aire vraie vaut la marge : 0,002 (pic) et 0,001 (écart), contre 0,185 et 0,160 pour « reproduit » à tort. Pas
  d'échappatoire ; le texte pourrait le dire en une phrase (suggestion).

**A. La réserve est-elle exacte au regard du calcul scellé ? Oui.** Rejeu, données simulées seulement :
- `puissance-marge-ecart-v1.py` (`99d71a59…`, compagnon vérifié ; il vérifie lui-même l'empreinte de `puissance-regle-v1.py` `fa482dd9…`),
  lancé avec l'argument `20261118` : « reproduit 0,160, non reproduit 0,004, non tranché 0,836 », **identique** à la sortie scellée
  `sortie-puissance-marge-ecart-v1.txt` (`4f51889f…`). La table de « Puissance » (l. 424-435) recopie **exactement** les vingt lignes de
  `sortie-puissance-regle-v1.txt` (`0c1e9d7a…`).
- Borne « au plus 16 fois sur 100 » : la probabilité de la conjonction ne dépasse pas celle de la cellule la plus faible ; entre le pic (0,185) et l'écart
  (0,160) au point marge, c'est 0,160. Borne « environ 3 fois sur 100, deux modèles indépendants » : 0,160² = 0,0256 (les deux cellules de l'écart,
  une par modèle, sont des conditions nécessaires du « oui »). Les chiffres de la phrase R1 sont exacts. La condition « si toutes les aires vraies étaient
  à la marge » est bien celle du calcul ; une aire vraie sous la marge donne moins (monotone sur la grille). « À tort » signifie ici aire vraie ≤ marge.
- Les phrases de « Seuil » (l. 401-409) : 0,004 et 0,008 à 0,90 ; 0,060 et 0,102 à 0,95 ; 0,185 et 0,160 à la marge ; « non reproduit … ≤ 0,001 » quand l'aire vraie
  vaut la valeur publiée ou plus (0,000 à 0,9999, 0,995 et 0,99 sur la grille) : exactes.
- Les bornes « oui » (0,573² ≈ 0,33 ; 0,783² ≈ 0,61 ; 0,999² ≈ 0,998) et « non » (0,193² ≈ 0,04 ; 0,771² ≈ 0,59 ; 0,978² ≈ 0,96) : exactes ; « au plus »
  est la bonne lecture (bornes supérieures).

**F. Mais la phrase adoptée pour M3 n'est pas soutenue.** Lignes 452-456 : « si l'aire vraie de chaque cellule vaut 0,99 à 0,995 …, « oui » sort au plus 33
à 61 fois sur cent **et « non tranché à cette puissance » est l'issue la plus probable** » ; ligne 860-862 (Frontière n° 8) : « c'est l'issue la plus probable » ;
ligne 930 (tableau) : « « non tranché » le plus probable ». Ce que le calcul scellé donne : des probabilités **par cellule**, et une borne **supérieure** sur « oui ».
Il ne donne ni la loi des états des huit cellules, ni la probabilité de la ligne R5 (« non tranché à cette puissance », aucune cellule « reproduit » ni « non reproduit »),
ni celle de la ligne R3 (« en partie »). Trois faits : (1) à une aire vraie de 0,995, la ligne R5 exige que la cellule de l'écart soit « non tranché » (0,149 par cellule sur la grille) : elle ne
peut pas dépasser 0,149, alors que « oui » vaut au plus 0,61 sans être borné par le bas ; l'issue « la plus probable » est donc, au moins en partie,
autre chose que R5 ; (2) à 0,99, R5 ≤ 0,325 (cellule de l'écart) et le reste se répartit entre « oui » (≤ 0,33), R3 et R5 de façon non simulée ; (3) la
proposition de la contre-lecture 2 (§ 7, M3) portait la même formule : l'erreur vient de là, le rédacteur a repris le texte proposé. Une phrase
non soutenue sur ce que le lecteur doit attendre est ce que R4 (symétrie) et R7 (aucun chiffre non vérifié) interdisent ; elle n'est pas une
porte dérobée (elle excuse « non tranché », pas « oui »), d'où un couple exact et non un blocage. Couple C1, § 7.

## 3. Chiffres de l'article (R7) : valeurs ajoutées ou changées au brouillon 3

Lus sur le PDF `docs/sources/pdf/2604.01151v5.pdf` (`02527fd4…`), pages 17, 18, 27, 28, 29, 30 :
- **p. 17, section 6** : « Figure 2 reports per-probe AUROC for all four models on Transfer and Stego, with the full per-family breakdown given in Appendix D.
  Each model uses a single linear deception probe trained on its own NARCBench-Core activations and evaluated zero-shot on the OOD tiers.
  Hyperparameter-tuning details are in Appendix F. » : citation exacte (avec les crochets du texte).
- **p. 18, figure 2** : légende « Means are taken across the model's probe-layer range and 10 seeds » ; barres STEGO de Qwen3-32B (1,00, 1,00, 1,00, 0,99,
  1,00) et de Llama-3.1-70B (1,00, 1,00, 1,00, 0,99, 1,00) : conformes. « Figure 3 » : courbes ROC ; « Table 1 » : collusion émergente (Verdict) : exact.
- **p. 27** : « the per-tier breakdown that underlies Figure 2 » ; annexe C « Activation extraction and probe training » ; Table 2 : OOD Mean **0,85, 0,55, 0,86,
  0,89, 0,89** (Qwen3-32B) ; STEGO pic 1,00, écart 0,99 ; CORE tout 1,00. Exact.
- **p. 28** : Table 3 : OOD Mean **0,91, 0,77, 0,92, 0,93, 0,94** ; STEGO pic 1,00, écart 0,99 ; Tables 4 et 5 : STEGO pic/écart 0,98/0,87 (DeepSeek) et 0,74/0,40 (GPT-OSS) : exact.
  Moyennes recalculées : (0,85 + 0,55 + 0,86 + 0,89 + 0,89)/5 = 0,808 → 0,81 ; (0,91 + 0,77 + 0,92 + 0,93 + 0,94)/5 = 0,894 → 0,89 : exact. Contrôle
  de la définition de la moyenne : OOD Mean du pic de Qwen3-32B = (0,32 + 1,00 + 0,94 + 0,97 + 0,82 + 1,00 + 1,00)/7 = 0,864 → 0,86 : conforme à « six familles de
  transfert plus STEGO ».
- **p. 29** : `penalty=l2`, `C=25`, `max_iter=8`, `solver="liblinear"` ; « Reported numbers are averaged across the five probe techniques and ten random seeds » : exact.
- **p. 30** : Table 6, ligne « Logistic Regression » : **0,81** (Qwen3-32B) et **0,89** (Llama-3.1-70B), en gras : égal aux moyennes ci-dessus ; annexe F : « Another strategy we tried
  for improving generalisation is data augmentation. We used 4 noisy copies per original data point and a standard deviation of 0.05 for the Gaussian noise.
  It slightly reduced OOD mean AUROC score (by less than 0.001) and wasn't used for the main results. » : **citation exacte** ; le membre qui décide est bien « wasn't used for the main results »,
  et la précision du rédacteur (la baisse chiffrée porte sur la moyenne hors distribution) est exacte.

**L'argument pour garder « augmentation selon l'article » tient, dans ses limites déclarées.** Chaîne : (a) les Tables 2 et 3 sont le détail de la figure 2, qui porte les résultats
principaux (p. 17 et 27) ; (b) l'annexe F dit que l'augmentation n'a pas servi aux résultats principaux (p. 30) ; (c) les moyennes des Tables 2 et 3 égalent la
ligne « Logistic Regression » de la Table 6, donc les Tables 2 et 3 sont celles de la sonde réglée à l'annexe F. Les trois maillons sont sur le PDF. Le maillon (c) prouve
seulement que Tables 2, 3 et 6 sortent de la même configuration, pas que celle-ci est sans augmentation ; seul (b) le dit, et il le dit de « the main results ». Le texte
l'avoue (l. 233-237, Frontière n° 10). La force de (b) est modeste (une phrase), mais le script publié par défaut (`AUG_ENABLED = True`) ne la contredit pas de façon
vérifiable : son fichier d'accueil le range sous « LR probe variant ».

**Avis : ce n'est pas un nœud pour le directeur.** Raisons : (1) la mère a déjà tranché (R-3341) et le texte garde sa décision ; (2) aucune hypothèse, revendication ni porte ne
change (le témoin de recette est un bras de diagnostic, N-026, jamais une porte ; la lecture est descriptive) ; (3) l'effet attendu d'une augmentation, moins de 0,001 sur la
moyenne hors distribution selon l'article, est environ trente fois sous la tolérance de 0,03 : l'état du témoin de recette, qui ne se joue qu'une fois (liste d'arrêt n° 4), ne
peut pas basculer pour cette seule raison, sauf si l'effet sur l'étage stéganographique seul était très supérieur à celui sur la moyenne hors distribution, ce que l'article ne dit pas
et que le texte déclare. **Suggestion non bloquante** : ajouter à la ligne 236-237 « (trente fois sous la tolérance de 0,03) » pour que le lecteur voie pourquoi le choix ne se joue pas à l'unité. Si la mère veut
quand même une trace pour Lazar, une ligne d'information suffit, pas une décision.

## 4. Texte et code

**Commande `verifier-texte`** (code du commit `cde3b990`, extrait par `git archive` ; `PYTHONPATH=<extraction>/src:/home/user/narcbench-paquets-v2`, interpréteur
`/home/user/controle-ia-travail/.venv/bin/python`). Aide lue : `verifier-texte <chemin du texte>`, sans registre ni données.
- Sur une **copie** du brouillon 3 où seul le marqueur `<<ENTROPIE_NARC_EXT>>` est remplacé par `9876543210123` (le diff de la copie à l'original : une seule ligne, l. 301) :
  **code de sortie 0** ; configuration rendue : `augmentation papier`, couches Qwen3-32B 26 à 30 et Llama-3.1-70B 32 à 37 (`bande`), forme du `run-id`
  `AAAAMMJJ-HHMMSS-narc-externe-v2`, registre `registres/narcbench-externe-v1.md`, texte `prereg/narcbench-bras-externe-v1.md`, entropie lue en entier.
- Sur le brouillon 3 **lui-même** : code 2, **seul refus** : l'entropie `'<<ENTROPIE_NARC_EXT>>'` (« entier (chiffres seuls) ≥ 2³² … attendu »). Rien d'autre.
- Contre-épreuve : le brouillon 2, même copie : code 2 (« <clé> : <valeur> » seule attendue : la prose de la section).

**Fonctions et codes de sortie.** Texte et code s'accordent sur : exit 2 pour `RefusRegistre` (n° 3, 4, 5), exit 1 pour `GardeArret` ou `MemoryError`
(n° 1, 2, 6, 7, 8, 9, 10 à 12) ; l'ordre de `lire` (n° 3, 5, 6, 4, 7, 2, 1, puis 8 et 9 sur les métadonnées, puis manifeste) ; le journal : `REFUS-NARC-EXT` avant
l'ouverture, `OUVERTURE-NARC-EXT` à la création du manifeste, `ARRET-NARC-EXT` après ; le seuil de 10 % comparé en entiers (`den * exclus > num * épisodes`,
exactement 10 % passe) ; le repli de Cholesky (`plancher_avec_repli`) ; `None` au lieu de `NaN` et arrêt sur toute valeur non finie du résultat (`valeurs_non_finies`) ;
aucune option `--registre` (l'analyseur n'en a pas) ; les six options, `--entropie` comparée en entiers.

**Liste des 503 tâches.** `lecture_externe_v2.taches` appelée avec `bande` et des noms de plis factices (14 pour Qwen3-32B, 15 pour Llama-3.1-70B) : **503 tâches, 503 distinctes**,
dont 225 pour Qwen3-32B ; décompte du texte (60 + 140 + 5 + 14 + 6 = 225 ; 72 + 180 + 6 + 14 + 6 = 278) : exact. Noms : `<modèle>/familles/c<couche>/<famille>/{apprentissage,plancher,reechantillonnage,placebo}`,
`…/apprentissage/pli-<domaine>` (familles co-principales), `<modèle>/temoin/c<couche>/plancher`, `<modèle>/cellules/<procédure>/<étage>/<statistique>/reechantillonnage` et `…/placebo`
(procédures visées, étage `stego`) : conformes à la section « Graines » (l. 522-529).

**Phrases gelées : texte contre code, mot pour mot** (exécution des fonctions du code `phrase_cellule`, `QUALIF_PLANCHER`, `signe`, `regle_t`, `phrase_famille`, `reponse`,
`GARDE_CONSTANTS`, `LECTURE_SECONDAIRE`, comparées au texte après normalisation des espaces et des accents graves). **Identiques** : « non lu : garde (scores constants) » ; « non calculable à cet effectif » ;
les trois états de signe ; les trois qualificatifs de plancher (« au-dessus du plancher apparié », « pas au-dessus du plancher apparié : des directions tirées au hasard dans la même covariance
atteignent la même séparation ; rien n'est établi sur la direction apprise », « sans plancher ») ; « lecture secondaire, sans effet sur la réponse » ; les cinq phrases par famille F1 à F5 ; la ligne R0 ;
les lignes R2, R3, R4 et R5 (y compris « aucune » dans R3 ; « ce n'est pas un échec (section « Puissance »)» dans R5) ; la partie de R1 qui précède la réserve (de « oui : notre chaîne reproduit … » à
« plancher apparié : <liste> »).

**Liste exacte des différences** :
1. **Phrase R1 : le code n'a pas la réserve** (connue ; le développeur l'aligne). Texte (l. 592), à ajouter après `plancher apparié : <liste>`, mot pour mot :
   ` ; réserve : « reproduit » veut dire « compatible avec la valeur publiée à 0,03 près, à cette puissance », pas « égal » ; si toutes les aires vraies étaient à la marge, ce « oui » sortirait à tort au plus environ 3 fois sur 100 avec deux modèles indépendants, au plus 16 fois sur 100 sinon (section « Seuil »)`.
   Le code (`cellules_externe_v2.reponse`, ligne R1) finit après la liste. Rien d'autre à changer dans cette phrase.
2. **Liste des planchers de R1 et R2** : le texte écrit `<au-dessus ou pas au-dessus, pour chacune des douze cellules visées, nommées>` ; le code écrit aussi « sans plancher »
   (`planchers[...] or SANS_PLANCHER`) quand le plancher manque (double échec du tirage). Le texte omet cette valeur possible. Couple C3.
3. **Garde sur la révision du jeu** (liste d'arrêt n° 1, l. 632-633, « ou révision du jeu différente → arrêt ») : **le code ne compare aucune révision** ; `REVISION_JEU` n'est que consignée
   au manifeste (`lecture_externe_v2.lire`, config) ; seuls la taille et l'empreinte des huit fichiers sont comparées (`verifier_fichiers`). Garde promise non codée (R5 : pas de garde sans essai).
   Couple C2 (texte), ou garde à ajouter au code ; les empreintes fixent déjà la révision.
4. **Place de la ligne `LECTURE-NARC-EXT` du registre** : le texte (l. 616-617, 640) range « déjà jouée » (n° 4) quatrième ; le code **lit la ligne `LECTURE-NARC-EXT` à l'étape du registre**
   (`lire_registre_externe`, avant les n° 5 et 6) ; seule la détection par dossier `runs/` ou `diag/` (`exiger_jamais_jouee`) vient après le n° 6. Même code de sortie (2), même refus,
   même journal : différence d'ordre seulement. Couple C4.
5. **Forme de l'identifiant** : voir § 1 (M1) : le texte dit « avec la date et l'heure UTC du lancement » ; le code ne compare pas au lancement. Couple C5.
6. **Phrases des règles T0, T3, T4** : le texte donne le schéma (« non lu (cellule nommée) », « reproduit en partie (cellules nommées) », « non tranché à cette puissance (cellules nommées, état des autres) ») ;
   le code écrit un détail plus long mais conforme (`reproduit en partie (reproduit : … ; non reproduit : …)`, `non tranché à cette puissance (nom : état ; …)` pour toutes les cellules). Ce
   ne sont pas des phrases gelées mot pour mot dans le texte ; pas de couple ; la fiche du code fixera la forme.

Aucune autre différence trouvée.

## 5. Ce que le texte dit du code : lectures faites

- **Gardes** : n° 3 (registre fixé, deux clés exactement une fois, antériorité stricte, `CODE` après `SCELLEMENT`, sceaux, texte cité, gabarit) ; n° 5 ; n° 6 (racine du dépôt, arbre propre, commit présent,
  HEAD ou ancêtre, liste et empreintes des fichiers de `narcbench/`, paquet exécuté égal fichier pour fichier) ; n° 7 (version 1,9.1 exigée de l'installée **et** de la fiche) ; n° 2 (segment `transfer`) ;
  n° 1 ; n° 8 et 9 (métadonnées) : conformes au texte, sauf les points 3 et 4 de la liste ci-dessus.
- **Manifeste** : `creer_manifeste(…, decisif=False, prereg=…, commande=…)`, graines depuis l'entropie du texte : conforme (l. 326-329 et 519-521).
- **Ce que je n'ai pas fait** : exécuter `lire` ; jouer les essais du développeur (167 « passés » selon la mère) ; relire la recette du témoin contre le code des auteurs (relevé `8be99220…` absent de
  `main`, non lu).

## 6. Validateur

`controle_ia.prereg.problemes` rejoué sur le brouillon 3 : **deux lignes**, qui sont les trois marqueurs prévus : « contre-lecture 3 sans ses deux empreintes (brouillon relu et rapport) » et
« marqueurs de gabarit restants : `<<CONTRE_LECTURE_3_NARC_EXT>>`, `<<ENTROPIE_NARC_EXT>>`, `<<TETE_FINALE_CODE_NARC_EXT>>` » (lignes 47, 301, 949 ; un seul exemplaire de chacun). Sur la copie à entropie remplie :
mêmes deux lignes, sans `<<ENTROPIE_NARC_EXT>>`. **Rien d'autre ne manque.**

## 7. Couples exacts avant → après

Sous l'hypothèse que ces couples s'appliquent au brouillon 3 pour fabriquer le texte à sceller (nouvelle version du brouillon, ou copie scellée corrigée, au choix de la mère ; toute correction
nécessite une nouvelle contre-lecture de la seule différence si la mère le juge utile ; je ne vois pas de risque nouveau dans ces cinq couples).

**C1 — M3 : formule non soutenue (majeur ; trois endroits).**
- Puissance (l. 452-456). Avant : « « oui » sort au plus 33 à 61 fois sur cent et « non tranché à cette puissance » est l'issue la plus probable ; si elle vaut 0,9999 ou plus … ». Après :
  « « oui » sort au plus 33 à 61 fois sur cent (deux modèles indépendants ; au plus 57 à 78 fois sur cent sinon) ; les autres issues (« en partie », « non tranché à cette puissance ») se partagent le reste, que la simulation
  ne répartit pas ; si elle vaut 0,9999 ou plus … ».
- Frontière n° 8 (l. 860-862). Avant : « : si l'aire vraie de chaque cellule vaut 0,99 à 0,995 (la valeur publiée, arrondie), c'est l'issue la plus probable ; si elle vaut 0,9999 ou plus, « oui » sort presque toujours ».
  Après : « : si l'aire vraie de chaque cellule vaut 0,99 à 0,995 (la valeur publiée, arrondie), « oui » sort au plus 33 à 61 fois sur cent et les autres issues se partagent le reste ; si elle vaut 0,9999 ou plus, « oui » sort presque toujours ».
- Tableau de la contre-lecture 2, ligne M3 (l. 930). Avant : « adoptée : « non tranché » le plus probable si l'aire vraie vaut 0,99 à 0,995 ; « oui » presque toujours à 0,9999 ou plus ». Après :
  « adoptée avec correction de la contre-lecture 3 : « oui » borné à 33–61 % (0,99 à 0,995), le reste réparti entre « en partie » et « non tranché », non simulé ; « oui » presque toujours à 0,9999 ou plus ».
  (Les bornes 57 et 78 : 0,573 et 0,783, sans hypothèse d'indépendance, l. 452.)

**C2 — liste d'arrêt n° 1 : garde non codée (écart texte-code).** Avant (l. 632-633) : « Fichier publié de taille ou d'empreinte différente de `EMPREINTES_PUBLIEES`, ou révision du jeu différente → arrêt avant toute lecture (R11). ».
Après : « Fichier publié de taille ou d'empreinte différente de `EMPREINTES_PUBLIEES` → arrêt avant toute lecture (R11) ; la révision du jeu (`REVISION_JEU`) est consignée au manifeste, non comparée : les empreintes des huit fichiers la fixent. ».
(Autre voie : le code compare la révision ; non recommandée, il n'a rien à comparer à une révision lue sur le disque.)

**C3 — listes de planchers de R1 et R2 (l. 592-593).** Avant : « <au-dessus ou pas au-dessus, pour chacune des douze cellules visées, nommées> » (deux fois). Après : « <au-dessus, pas au-dessus ou sans plancher, pour chacune des douze cellules visées, nommées> ».

**C4 — ordre des gardes (l. 616-617 et 484-485).** Avant (l. 616-617) : « n° 3 (registre et texte cité), n° 5 (configuration), n° 6 (code), n° 4 (déjà jouée), … ». Après : « n° 3 (registre et texte cité ; la ligne `LECTURE-NARC-EXT` du registre est
lue ici et refusée au titre du n° 4), n° 5 (configuration), n° 6 (code), n° 4 (déjà jouée : dossier `runs/` ou résultat sous `diag/`), … ». Plan n° 2 (l. 484-485) : même ajout, une demi-phrase.

**C5 — forme du `run-id` (l. 315-317).** Avant : « avec la date et l'heure UTC du lancement (date et heure valides) ». Après : « avec une date et une heure valides (la mère y met celles du lancement ; le code ne le compare pas) ».

**Suggestions non bloquantes** (pas des couples) : « (à 10⁻⁹ près, section « Seuil »)» dans les lignes C2 et C3 de la table C ; réserve sur F1 ou son absence assumée (§ 1, M4) ; une phrase qui dit pourquoi la réserve de R1 n'a pas son pendant
pour R2 (0,002 et 0,001 à la marge) ; « trente fois sous la tolérance » à la ligne 236-237 (§ 3).

**Après ces couples** : « scellable » ; marqueurs à remplir par la mère (entropie, tête finale du code, entrée de cette contre-lecture) ; le contrôle `verifier-texte` code 0 est à rejouer sur la copie à sceller (plan n° 0).

## Lectures hors du mandat (déclarées)

- `git log` et `git diff --stat` entre `cde3b990` et la tête actuelle de la branche du développeur (`b46c678d`), en lecture seule, pour établir que les modules de `src/` n'ont pas changé depuis la tête lue.
- Empreintes (sans ouvrir le contenu) de vingt-deux fichiers cités par l'en-tête du texte, dans `main`, pour contrôler le texte ; existence (sans ouvrir) des quatre pièces de la branche citées comme absentes de `main`.
- Exécution de fonctions du code (`phrase_famille`, `reponse`, `regle_t`, `taches`, énumérations) sur des entrées factices : aucune donnée, aucun fichier publié.
- Lancement du script de puissance `puissance-marge-ecart-v1.py` (données simulées) avec `PYTHONDONTWRITEBYTECODE=1` (état de l'arbre inchangé).
- Aucune lecture sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; aucun accès à `/home/user/narcbench-donnees-v2/`. Dossier temporaire supprimé à la fin.
