# Contre-lecture du banc de calibration complet MR-2 (règles v1 et devis v4) — tour 1

- **Lecteur** : modèle C, contre-lecteur neuf (R2) ; je n'ai écrit aucune des pièces (rédacteur : modèle A). Première contre-lecture, lecture entière des deux pièces.
- **Heures** (`date -u`) : début 2026-11-17 03:15:32 ; fin de la rédaction : dernière ligne.
- **Pièces lues** (empreintes recalculées, égales à leur compagnon) :
  - règles `docs/notes/organisme-multi-generations-v1/banc-calibration-mr2-v1/regles-banc-calibration-mr2-v1.md`, `87d7536ee10a4f240aec7fe1ee4200e1a5d7d168daab816a4e8ca7e6139d87f7` ;
  - devis `…/devis-banc-calibration-mr2-v4.md`, `a64ad4069761564c8897d3da6bc13d1e92acde764165b482f61ba3ae658d0412` ;
  - la mesure des durées (`.py` `7fe05002…`, `.json` `d0c3e21a…`, `.stdout` `1863044f…`) et le calcul du devis (`.py` `1cccc7d4…`, `.json` `892fe8d4…`, `.stdout` `e2dc58e8…`), empreintes égales aux compagnons ; code du calcul lu en entier et sortie relue ;
  - contre-lectures du devis v3 (tour 3 et fin du tour 1), pour les mineures m8, m9, m10 ;
  - brouillon 6 du préenregistrement (`4deec525…`) : sections Métrique, Seuil, Points ouverts, gardes 25 et 35, V-6, V-12, V-22 à V-24, V-36 ; conception v7 (`1f1b64df…`) : §3.4 ; conception v3 (`386d48ba…`) : table de détection ; sortie `sorties-v5/calcul-regle-v5.json` (`10ff446d…`) ; `outils-v4/monde_riche_v4.py` (fonction `course`) et `outils-v2/verifier_monde_v2.py` (C7) ;
  - verdict v2 du pilote (`e64458e8…`, par `git show` de la branche `verdict/pilote-mr2-v74-v14-v1` dans un dossier neuf du bloc-notes) : prix, heures de création et de destruction, `P_CACHEE_banc = 0,0`, manifeste 12:14:34 et 12:59:07, 0,074757 ; rapport du développeur (`6635e43a…`, branche `prep/pilote-mr2-v1`) : « 882 s ». Rien d'autre de la sortie du pilote ; aucune branche `calcul/pilote-mr2-v74-entree-*`, aucun secret, aucun monde.

## Verdict : **corrections** (0 majeure, 6 mineures exigées ; 7 remarques facultatives)

La conception tient : l'ordre D-2 est dans l'ordre (f, fusion, n, forme, τ, règle en dernier), les critères et les replis sont écrits avant toute lecture, le dénominateur est « tous les mondes tirés », et l'arithmétique du devis se refait. Le pire du devis tient sous 3 USD. Les corrections ci-dessous sont des mises en cohérence ou des oublis ; aucune ne change une valeur ni une règle. La pièce des règles ne se scelle pas comme finale pour une autre raison, déjà dite par elle : le sous-choix de τ est un nœud de Lazar.

## 1. Vérification (1) : règles du banc complètes, ordre D-2, critères avant lecture

- **Ordre** : sections 0, 4.3, 7, 10, 11 et 13 donnent les mêmes six étapes dans le même ordre ; chaque valeur est scellée avant l'étape suivante (B-5, T-2) ; la passe P_CACHÉE = 0 est jouée et scellée la première (B-9, T-11) ; la règle est lue en dernier (section 10, ordre de lecture). Conforme à GO-2026-11-17-05 et au brouillon 6 (« Ordre d'application au banc »).
- **Objet, simulation, mesure, décision, repli** : présents pour chaque règle (7.1 à 7.6). Comparés au brouillon 6 : f (égalité à 0,01 près : 0,75), n (plus petit n tel que médiane ≥ 0,5 et part ≤ 0,25 ; repli 400 ; repli à moins de 8 mondes), forme (marge 0,02 en faveur de la moyenne ; repli moyenne), τ (part d'ensemble, sans marge), règle (2·G ≥ 24) : identiques, avec les trous fermés signalés E-3 à E-9.
- **Dénominateur** : G sur les 24 mondes tirés, g_r = 0 sans tirage conforme, sans arrêt (B-11) ; T-4 essaie 12 + 12 (tenue) et 11 + 13 (non tenue). Bon. Seuil : « moins de la moitié » = G < 12 ; G = 12 est tenu, comme le texte de Lazar.
- **Prédictions** : refaites, 1 − (1 − 0,5⁸)²⁴ = 0,0897 et 1 − (1 − 0,6⁸)²⁴ = 0,3340 ; « G = 24, 0,91 » égale (1 − 0,5⁸)²⁴ = 0,9103 (la part gardante 0,996 de la conception v7 est 1 − 0,5⁸, tous les mondes conformes gardent à P_CACHÉE = 0 dans le modèle réduit) ; borne haute 1 − 0,025^(1/84) = 0,042965 (recalculée). Les chiffres sont recoupés avec `calcul-regle-v5.json` et le tableau de la conception v7 §3.4. Aucune prédiction n'est ancrée sur l'état de l'art (R7 tenue).
- **Audit de symétrie (R4)** : A0 se déclenche à G = 24 comme à G < 12 ; A-f, A-n, A-forme, A-τ présents. Bon.
- **Preuves des trois formes (annexe A, D-3)** : je les juge **valides sous les hypothèses (a) et (b) écrites** (arrêt optionnel d'une martingale positive à temps borné ; moyenne de valeurs e = valeur e ; groupe et représentant indépendants des tirages du juge ; e-BH valide sous dépendance quelconque avec m ≥ nombre d'hypothèses). Les trois formes sont donc éligibles au sens de la section 7.4 point 3, sous deux réserves que la pièce dit déjà : (a) n'est établie que pour la classe linéaire du nul v8 (le membre tempéré et incliné « au second ordre près », sans preuve), réserve **commune aux trois formes** donc sans effet sur le choix entre elles ; (b) est à vérifier sur le code (V-23) par la contre-lecture du code. La validité ne tient qu'« au sens de H₀ » (hypothèse (c)), ce que la pièce écrit.
- **Écarts E-1 à E-16** : listés ; ceux qui reviennent à la mère (E-1, E-2, E-10, E-11) sont dits comme tels. Je n'y vois pas d'écart caché de plus, sauf l'oubli signalé en correction 3 (Q-5, Q-8).

## 2. Vérification (2) : devis, arithmétique refaite

Refaits à la main et par un petit programme, valeurs égales à `calcul-devis-banc-mr2-v4.json` :
- total par monde : attendu 281,3 + 1,9 + 10,0 + 883,0 + 428,4 + 134,0 + 280,9 + 123,2 + 422,5 + 15,0 = **2 580,2 s** ; pire : 674,6 + 2,4 + 35,0 + 2 130,8 + 1 797,0 + 201,6 + 422,6 + 1 345,5 + 1 846,6 + 18,8 = **8 474,9 s** ;
- S0 attendu : 219,6 + 62,2 × (0,5 + … + 0,5⁷) = 281,3 ; S3 : 2 × 200 × (0,25 + 0,3035 + 0,357 + 0,478 + 0,599) = 795,0, plus 76,95 + 11 = 883,0 ; S4 : 1 200 × 0,357 = 428,4 ; S5 : 35,1 + 41,85 + 41,85 + 3 × 5,053 = 134,0 ; S6 : 8 × 35,1 = 280,9 ; M7 : 20 × (15 × 0,1 + 21 × 0,357 + 21 × 0,506) + 30 = 422,5 ; surcharge attendue (47 min 37 s − 882 s + 2 min 4 s) = 0,583 h ;
- calcul d'un processus : 24 × 2 580,2 / 3 600 = **17,20 h** ; au pire 24 × 8 474,9 / 3 600 × 1,5 = **84,75 h** ;
- durées : 17,20 / (4 × 0,8) + 0,583 = 5,96 h ; 17,20 / (6 × 0,8) + 0,583 = 4,17 h ; 17,20 / (8 × 0,8) + 0,583 = 3,27 h ; au pire 28,48 h, 19,66 h, 15,24 h ; minuteries (× 1,15, arrondi au-dessus) 33, 23, 18 h ; prix relus maximaux 0,09, 0,13, 0,166 USD/h ; **pire : 2,97 ; 2,99 ; 2,988 USD** ;
- attendu : 5,96 × 0,052222 = 0,311 ; 4,17 × 0,052222 = 0,218 ; 3,27 × 0,052222 = 0,171 USD.

Entrées recoupées au verdict v2 (prix 0,052222 USD/h, 1,5706 h, création 11:26:57, destruction 13:01:11, manifeste 12:14:34 → 12:59:07, 0,074757 USD d'une tentative antérieure) et au rapport du développeur (882 s) : **égales**. Le recoupement avec le journal de la conception v4 (424 s contre 415,8 s, 2 %) se refait.

- **Crédits et hors crédits séparés** : oui, section 5 (0 et 0 sur crédits, car aucun appel de modèle ; machine hors crédits). Aucune ligne sur crédits.
- **3 USD tenu ou nœud dit** : **tenu par construction** (minuterie × prix relu maximal ≤ 3 USD pour chaque nombre de processus) ; le nœud de dépense n'existe pas ; la règle de la seconde machine (coupure iv) garde le cumul sous 3 USD. Le pire est un plafond de dépense, non un pire durée : si la durée dépasse la minuterie, le banc est « non jugeable » et un second banc est un nœud ; le devis le dit (section 8, point 2). La ligne « calcul » de la section 9 peut être inscrite par la mère, une fois la correction 5 prise et le devis lu d'une autre lignée que A (cette lecture en est une).
- Une seule incohérence : la fourchette de l'attendu (correction 5).
- **Attendu et juge de la course** : l'attendu repose sur des durées du juge simplifié ; la pièce des règles retient le juge de la course (E-2). Le devis le dit (× 2 au pire seulement) et prévoit la garde de durée avant location. À l'attendu, le surcoût resterait de l'ordre de quelques dixièmes d'USD : sans effet sur le 3 USD. Remarque facultative 7.

## 3. Vérification (3) : mineures du tour 3 reprises

Section 12 du devis v4 : **m8** reprise mot pour mot (« recalculées : 1 − (1 − 0,5^8)^24 = 0,0897 ; 1 − (1 − 0,6^8)^24 = 0,3340) », une occurrence, tableau du tour 1) ; **m9** reprise mot pour mot en deux endroits (« à ce tour, le même modèle a peut-être lu et corrigé (provenance non établie, comme au tour 1). » et « (peut-être le même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1 », une occurrence chacune) ; **m10** reprise en substance (section 4 : base de chaque chiffre dite, facteur de la machine seulement au pire). Bien.

## 4. Vérification (4) : aucune lecture interdite, aucun identifiant de modèle

- Aucun identifiant de modèle dans les deux pièces (recherche des noms de modèles et de fournisseurs : aucune occurrence ; seul « crédits de Claude » désigne le service, non un modèle ; les rôles C1, C2, X1, X2 sont des rôles). Le nom du fichier de vérification v3 n'est pas recopié (dit). Bien.
- Les pièces ne déclarent ni n'emploient rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du mode tenu à l'écart (mention seulement dans la déclaration « interdits tenus »), ni de `diag/`, `runs/`, `donnees/`, ni de branche `calcul/pilote-mr2-v74-entree-*`. Du pilote : seuls le verdict v2 et du code de la branche `prep/pilote-mr2-v1` sont cités, comme permis.
- **Incident à dire (provenance)** : l'historique git de la pièce porte quatre états (`2687202c`, `48497ef3`, `c70b2261`, `a0993b93`) ; les trois premiers sont des états non scellés committés par un autre processus de la session pendant la rédaction ; le contenu du dernier égale la version scellée (empreinte relue sur le commit : `87d7536e…`). Le devis v4 a un cas semblable (`82cbb568`, `45eedb55`) et la sortie texte de la mesure a d'abord été committée vide ; la tête égale les versions scellées (sortie relue : 1 899 octets, empreinte égale). Les pièces disent « rien committé » (vrai de la main du rédacteur) sans dire l'incident : correction 4.

## 5. Corrections exigées (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans sa pièce, vérifié par comptage exact)

Les pièces étant scellées, ces corrections s'appliquent dans une v2 (fichier neuf, R12).

### Pièce des règles (`regles-banc-calibration-mr2-v1.md`)

**Correction 1 (mineure) — la mesure de C7 (M3) n'est pas « après la règle » ni « sans décision »** : C7 est un contrôle du tirage ; la pièce écrit elle-même qu'une égalité à six décimales est un refus du tirage. Elle joue donc avant l'étape 1 et peut changer l'ensemble des mondes, ce que la section 8 (« jouées après la règle », « ne décident rien ») et l'écart E-10 contredisent. De même, M5 (a) et M6 sont des relevés pris pendant le tirage et les étapes 3, 5, 6. Il faut le dire, et dire qu'une exception de C7 est une exception d'étape (B-6).

- Ancien : `Elles se jouent **après** la règle (dont la passe qui décide est déjà scellée) : ainsi la règle reste la dernière étape de D-2 et`
  Nouveau : `Elles se jouent **après** la règle (dont la passe qui décide est déjà scellée), sauf trois relevés qui ne coûtent aucun calcul de plus et ne sont que rapportés après elle : M3 (C7 est un contrôle du tirage, étape de tirage S0, donc avant l'étape 1 ; seule une égalité à six décimales refuse un tirage, règle du vérificateur v2 inchangée, ce qui fait partie de la définition des mondes, non d'une mesure qui décide ; une exception de C7 est une exception d'étape : « banc non jugeable »), M5 (a) (relevé sur les tirages de S0) et M6 (durées relevées pendant les étapes 3, 5 et 6) : ainsi la règle reste la dernière étape de D-2 et`
- Ancien : `mesures jouées après la règle, lues avant elle (section 8, section 10)`
  Nouveau : `mesures jouées après la règle, sauf M3, M5 (a) et M6 relevées pendant le tirage et les étapes 3, 5 et 6 (section 8), toutes lues avant elle (section 10)`
- Ancien : `dans une mesure hors D-2 → mesure « en échec », cause écrite`
  Nouveau : `dans une mesure hors D-2 (M3 exceptée : C7 relève du tirage, une exception y est une exception d'étape) → mesure « en échec », cause écrite`

**Correction 2 (mineure) — les passes ne sont couplées que si chaque carte a sa propre sous-suite** : dans le code de la v4 (`course`), un seul flux tire, carte après carte, les uniformes puis les bruits (`_bruiter(spec, S, 0.15, rng)`) ; la taille de S d'une carte (donc la présence d'une conditionnelle à un seuil donné) décale tout ce qui suit. La section 4.2 affirme que deux passes « ne diffèrent que par le seuil appliqué à la même uniforme » et T-3 demande des cartes égales « là où les uniformes le permettent » : avec le flux indexé par g seulement, cela ne tient qu'avant la première carte qui diffère. Indexer par le rang de carte rend l'énoncé vrai (les égalités de contrôle entre étapes, elles, tiennent déjà : mêmes valeurs, même consommation).

- Ancien : `| `proposition` | g | cartes synthétiques de la génération (une uniforme par composante et par carte, tirée quelle que soit sa probabilité) |`
  Nouveau : `| `proposition` | g, rang de carte | cartes synthétiques de la génération : une sous-suite par carte, qui tire d'abord une uniforme par effet du monde, connu ou non, quelle que soit sa probabilité, puis les bruits de la carte ; la taille de S d'une carte ne décale ainsi aucune autre carte, et deux passes ne diffèrent que par le seuil appliqué à la même uniforme (le code de la v4 tire uniformes et bruits d'un seul flux : à ne pas porter tel quel) |`

**Correction 3 (mineure) — oubli de l'étendue de Q-5 et de Q-8** : le brouillon 6 (point ouvert 11) laisse ouverts « Q-4 (nul v8), Q-6 (retirage automatique) **et l'étendue de Q-5 et de Q-8** » ; la pièce n'en reprend que deux, alors que le banc applique la règle de n (Q-5) et le regroupement avant le juge (Q-8).

- Ancien : `confirmation de Q-4 et Q-6 (Lazar ou la mère, brouillon 6, point`
  Nouveau : `confirmation de Q-4, de Q-6 et de l'étendue de Q-5 et de Q-8 (Lazar ou la mère, brouillon 6, point`
- Ancien : `2. **Q-4 (nul v8) et Q-6 (retirage automatique)** : le banc en dépend (juge, tirage des mondes) ;`
  Nouveau : `2. **Q-4 (nul v8), Q-6 (retirage automatique) et l'étendue de Q-5 (règle de n) et de Q-8 (regroupement avant le juge)** : le banc en dépend (juge, tirage des mondes, règle de n, regroupement) ;`

**Correction 4 (mineure) — incident de provenance non déclaré** (R12, R6) : voir section 4 ci-dessus.

- Ancien : `aucun fichier existant modifié ; rien committé ;`
  Nouveau : `aucun fichier existant modifié ; rien committé de la main du rédacteur (voir Incidents) ;`
- Ancien : `des `__pycache__` ignorés par git peuvent en naître.`
  Nouveau : `des `__pycache__` ignorés par git peuvent en naître ; un autre processus de la session a committé des états non scellés de cette pièce pendant sa rédaction (commits `2687202c`, `48497ef3`, `c70b2261`, puis `a0993b93` dont le contenu égale la version scellée, `87d7536e…`) : seule la version scellée fait foi (R12).`

### Devis (`devis-banc-calibration-mr2-v4.md`)

**Correction 5 (mineure) — fourchette de l'attendu contraire à la règle du devis** : la section 6 n'autorise, pour P = 4, qu'un prix relu au plus 0,09 USD/h et, pour P = 6, 0,13 ; or le devis chiffre l'attendu à 0,15 USD/h (0,89 et 0,63 USD), prix que sa propre règle exclut, et annonce « de 0,17 à 0,89 USD ». Au prix relu maximal de chaque choix, l'attendu est 5,96 × 0,09 = 0,54 ; 4,17 × 0,13 = 0,54 ; 3,27 × 0,166 = 0,54 USD (la fourchette est donc 0,17 à 0,54). Erreur par excès, sans effet sur le 3 USD, mais Lazar lit cette fourchette.

- Ancien : `0,89 USD selon la machine et son prix)`
  Nouveau : `0,54 USD selon la machine, au prix relu maximal de chaque choix de P)`
- Ancien : `0,89 à 0,15 USD/h`
  Nouveau : `0,54 à 0,09 USD/h (prix relu maximal de P = 4)`
- Ancien : `0,63 à 0,15 USD/h`
  Nouveau : `0,54 à 0,13 USD/h (prix relu maximal de P = 6)`
- Ancien : `0,49 à 0,15 USD/h`
  Nouveau : `0,54 à 0,166 USD/h (prix relu maximal de P = 8)`
- Ancien : `(0,17 à 0,89)`
  Nouveau : `(0,17 à 0,54)`

**Correction 6 (mineure) — mêmes oublis que les corrections 3 et 4, dans le devis** :

- Ancien : `sous-choix de τ ; Q-4 et Q-6 s'il ne laisse pas la mère les confirmer ;`
  Nouveau : `sous-choix de τ ; Q-4, Q-6 et l'étendue de Q-5 et de Q-8 s'il ne laisse pas la mère les confirmer ;`
- Ancien : `aucun fichier existant modifié ; aucun commit ; aucun`
  Nouveau : `aucun fichier existant modifié ; aucun commit de la main du rédacteur (un autre processus de la session en a fait sur des états non scellés ; la tête égale les versions scellées) ; aucun`

## 6. Remarques facultatives (aucune n'est exigée)

1. **Valeur de δ_bas (7.3 point 4)** : prendre le milieu de [0 ; 0,01[ (0,005) et la médiane des mondes rend le point (ii) très clément : les données de la conception v3 (0,08 à n = 400 et 0,21 à n = 800 pour la tranche [0 ; 0,01[) disent qu'il ne mordra presque jamais, donc n sera fixé par (i) seul. C'est le choix déclaré du rédacteur (E-5) et il est recevable ; la lecture stricte de « à moins de 0,01 nat » serait la borne haute (0,0099). Le brouillon 6 dit « la part », sans dire médiane ou part mise en commun : la médiane est cohérente avec (i).
2. **τ non mesurable** : la section 7.5 dit « nœud » ; la table de lecture (section 10) ne dit pas où cette issue tombe quand G ≥ 12. Une ligne « τ non mesurable : la règle tient, la ligne de la course n'a pas de τ, nœud » suffirait.
3. **Sous-choix de τ** : la pièce écrit que, si Lazar retient la borne haute de Wilson, « la pièce est refaite (v2) ». Comme elle calcule et rapporte déjà les deux, il suffit de changer le mot de la règle 5 ; la pièce doit être refaite de toute façon (corrections ci-dessus), le coût est nul.
4. **Garde de durée et de mémoire** (devis, section 6) : elle est une condition de location et figure dans la section 13 de la pièce, mais pas dans la liste d'arrêt B-1 à B-14 ; une ligne B-15 « avant location » l'alignerait avec B-14.
5. **Marqueurs [GRAINES-BANC] et [CHAMP-BORNE-HAUTE]** restent ouverts dans une pièce « finale » ; c'est dit, et le champ n'a pas à être lu par le lecteur, mais le code gelé devra les lever avec une empreinte avant la poussée (garde B-2).
6. **Doublons exacts de la règle de forme** : trois copies exactes jugées sur des tirages indépendants sont le cas le plus défavorable à la moyenne (≈ p³) et le plus favorable aux deux autres formes ; les groupes réels sont de quasi-doublons. C'est le choix du brouillon 6 (E-6) ; la mesure M4 (paires difficiles) en rapporte déjà l'esprit.
7. **Attendu du devis et juge de la course** : l'attendu pourrait être donné aussi avec le facteur × 2 sur les jugements (de l'ordre de 0,5 à 0,6 USD à 4 processus au prix du pilote) pour que Lazar n'ait pas à le déduire ; sans effet sur le 3 USD.

## 7. Points pour la session mère

- **Rien à trancher sur la dépense** : le pire tient sous 3 USD par construction ; aucune dépense avant la ligne « calcul », que la mère inscrit sur le devis (v5 corrigé, ou v4 avec la correction 5) lu d'une autre lignée.
- **Mot de Lazar nécessaire, sans défaut** : sous-choix de τ (part d'ensemble ou borne haute de Wilson). Sans lui, la pièce ne se scelle pas comme finale (elle le dit). Q-4, Q-5 (étendue), Q-6 et Q-8 (étendue) : mot de Lazar ou décision de la mère consignée au registre, **avant le banc**.
- **À confirmer par la mère** (écarts à des textes scellés, tous signalés par la pièce) : E-1 (module neuf égal à la v4 : lecture cohérente avec le mot de GO-2026-11-17-05, « code v68 de la course ») ; E-2 (juge de la course et non « juge simplifié » de la conception v7 §3.2 : écart de lettre, sans effet attendu à P_CACHÉE = 0) ; E-10 et E-11 (avec la correction 1) ; le texte candidat de la course doit égaler la pièce.
- **À dire à Lazar en clair** (la pièce le demande, je confirme) : la règle tient presque par construction à P_CACHÉE = 0 (0,91 pour G = 24, plus de 0,9999 pour la règle, sous le modèle réduit) ; à la borne haute du pilote elle ne tient qu'avec la probabilité 0,09 à 0,17 ; elle ne garde pas contre des proposeurs qui ne masquent pas ; MR-2 ne satisfait pas la lettre de Q-13 (c). Un succès au banc ne dit rien sur le progrès.
- **Risque principal** : le code de la course et du banc n'existe pas (juge, regroupement, représentant, oracle, jeu planté, lanceur, essais T-1 à T-14) et doit être écrit, essayé, muté, contre-lu et gelé avant le 30 novembre ; le calcul, lui, est petit (≈ 17 h d'un processus attendues). Les durées du devis viennent du juge simplifié ; la garde de durée à l'essai à blanc les relit avant toute location.
- **Contre-lecture du code** : l'hypothèse (b) des preuves (arrêt au premier instant de lecture où W ≥ seuil) et l'indépendance des flux `choix` et `juge` (garde 25) ne se vérifient que sur le code ; la contre-lecture de la pièce ne les clôt pas.
- **Provenance** : la correction 4 règle la déclaration ; la mère peut vouloir que les commits intermédiaires d'un autre processus ne se reproduisent pas pendant la v2 (R12).

## Déclaration

- **Rôle** : contre-lecteur neuf (R2), modèle C, sous-agent d'un script d'orchestration ; aucune autorité de décision. Je n'ai modifié aucune pièce, rien committé, aucune machine, aucun appel à un loueur ni à un fournisseur de modèles, aucune dépense.
- **Interdits tenus** : branches du pilote lues par `git fetch` à profondeur 1, sans contenu de fichier (filtre `blob:none`), dans deux dossiers neufs du bloc-notes, fichiers tirés un à un par `git show` (verdict v2 ; rapport du développeur, une recherche de « 882 »). Rien sous `diag/`, `runs/`, `donnees/` ; aucune branche `calcul/pilote-mr2-v74-entree-*` ; aucun secret ni monde ; aucune valeur de clé, ni `env` ni `printenv` ; aucun git avec `GIT_DIR`, `GIT_WORK_TREE` ou `GIT_INDEX_FILE`. Pas de git de ma main sur le dépôt principal hors lectures de l'historique (`git log`, `git show` de versions committées des deux pièces, `git remote get-url`).
- **Incidents de ma main** : (i) une première tentative de `git fetch` a échoué sur un conflit de nom de référence locale (dossier jetable, sans effet) ; (ii) pour retrouver le chemin du verdict dans la branche, j'ai listé les **noms** de fichiers de l'arbre de la branche (`git ls-tree --name-only`, filtré) : la sortie a montré quelques noms de fichiers sous `diag/` et `docs/` sans rapport ; je n'en ai ouvert aucun et n'en tire rien ; (iii) la première lecture de la pièce des règles a été tronquée par la limite de l'outil de lecture (424 lignes sur 603) ; j'ai lu la suite en entier avant de conclure.
- Fin de la rédaction : voir la ligne suivante.

Fin de la rédaction : 2026-11-17 03:24:25 (`date -u`, relevée juste avant le scellement).
