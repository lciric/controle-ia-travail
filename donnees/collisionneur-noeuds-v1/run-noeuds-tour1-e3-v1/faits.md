# Faits — tour du collisionneur sur les nœuds de décision du 31 octobre 2026 — v1

Assemblés par session-depot le 31 octobre 2026 pour la question v9 de conv-audit (`question-noeuds-decisionnels-collisionneur-v9.md`, sha256 `7df2e92ba9ded34489f38913295cba7fc8e2238bd17c5dc2af4e56f66cecff7b`), selon la liste A de `faits-a-assembler-noeuds-v4.md` (`95e12a34…`) et ses changements v2 et v3, plus les pièces de session-depot que la liste nomme et une pièce par nœud nouveau (N9, N10).

Règles appliquées : (1) ni le mémo des décisions en attente ni les avis de conv-audit ; (2) dans les pièces marquées, toute phrase portant une recommandation, une confiance d'auteur ou un défaut est retirée et remplacée par « [retiré, règle 2 : recommandation ou confiance d'auteur] » ; les recommandations par nœud sont servies au tour 2 par l'annexe ; (3) table des empreintes en fin de document ; (4) balayage avant scellement (fichier `balayage-faits-noeuds-v1.txt`) ; (5) numéros de ligne recoupés sur le contenu des fichiers de la branche `canal/conv-audit-n04` et de `main` au moment de l'assemblage ; chaque bornage corrigé est noté dans l'en-tête de sa pièce. Les pièces citent des versions antérieures à la dernière (pré-pilote brouillon 7, semi-réel brouillon 3, calcul de puissance v6), parce que la question les nomme : une version plus récente existe pour chacune (brouillon 10, brouillon 5, v9), non servie ici.

Total : 43751 mots dans les pièces.

### Pièce 1 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-deux-espaces-v1/experience-v2/lancement-v2/verdict-validation-v1.md` (entier) — nœuds N1

Origine : branche de conv-audit ; empreinte du fichier source `f5bf86b9d5001f363d0768cd88bebcc1f8e842711fa0c4c578d40debf13e8675` ; 1846 mots.

<<<DÉBUT PIÈCE 1>>>
# Verdict R13 — étape de validation, expérience v2 de bisociation à deux espaces — v1

- **Auteur** : sous-agent Sonnet 5.5 neuf, verdict R13 (ni auteur du préenregistrement, ni du code, ni de l'addendum, ni de la lecture de la validation).
- **Date et heure** : 2026-10-30T23:54:25Z (relevé `date -u` avant l'écriture, après toutes les lectures).
- **Non fait** : rien lu sous `donnees/` ; rien lancé ; aucun fichier existant modifié ; aucun `.sha256` écrit ; aucun commit.

## Empreintes vérifiées (SHA-256 recalculées ; « compagnon » = égale au fichier `.sha256` voisin)

| Fichier | SHA-256 | Contrôle |
|---|---|---|
| `prereg/preenregistrement-bisociation-deux-espaces-v2.md` | `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` | compagnon OK ; égale à l'empreinte attendue |
| `prereg/addendum-ecarts-bisociation-deux-espaces-v2-v6.md` | `37f6df2e0f3653088643b4eb1883c2a5b083111227edd3c53a0e411cd187774f` | compagnon OK ; compagnon daté 00:46:58 (heure de Paris) = 23:46:58 UTC, cohérent avec R-656 (« scellé à 23:47 UTC ») |
| `lancement-v2/validation-v2-resultats-v1.json` | `974dfe5e422662a5878f9dfa264f688f3a85113c9d8cf153325974a8820e0286` | compagnon OK |
| `experience-v2/reproduction-temoins-v2-resultats-v3.json` | `946fc397553289d0fd59c801bf529b28245ba5bad29ebea2883ac22671557930` | compagnon OK |
| `lancement-v2/lecture-validation-v1.md` | `8c6dd939907a649d76fe1504a1d439d549435687e456f508af60c7bc3286b4e5` | pas de compagnon (lue, non opposable) |
| `lancement-v2/journal-chaine-v1.txt` | `e55367debec6d8df3fbb9a45d1431f54874fbd9945099ca5d651dd2485cab29a` | pas de compagnon |

Les deux fichiers de résultats portent les mêmes quinze empreintes de code (comparées par lecture). Ordre tenu : reproduction écrite à 23:48:24, validation à 23:48:51, après le scellement de l'addendum (23:47). Le journal de chaîne dit : « ARRET validation (code 2) » ; il n'y a donc pas eu d'invocation des mondes de décision.

## Critères V1 à V9 et reproduction S12

Conditions d'évaluation : Q-05 et Q-06 (`ecarts-et-questions-v1.md`), validées « telles qu'écrites » par l'addendum (point Q-05 à Q-12) : V1 et S8 en M_bien et M_moyen ; V2, V3, V5 en M_bien ; V6 en M_moyen. Tous les chiffres ci-dessous sont recopiés de `validation-v2-resultats-v1.json` (valeurs vérifiées une à une contre le fichier, et la différence de V5 recalculée).

| Critère | Valeur (fichier de résultats) | Seuil gelé (citation du texte, S13, § 6, S8) | Vrai / faux |
|---|---|---|---|
| V1, M_bien | même domaine 0,5390 ; proches 0,2800 ; éloignés 0,0241 | S13 : « [0,51 ; 0,57], [0,25 ; 0,31], [0,00 ; 0,06] » | **vrai** |
| V1, M_moyen | 0,5295 ; 0,2775 ; 0,0246 | idem | **vrai** |
| V2, M_bien | F = −0,0854 (loi nulle rapportée −0,0865) | S13 : « F ≤ 0,10 » | **vrai** |
| V3, M_bien | excès = −0,0595 | S13 : « excès ≤ 0,10 » | **vrai** |
| V4 | concordance 1,000 ; variation moyenne des cosinus 0,2562 | S13 : « concordance des étiquettes de concept ≥ 0,9 et variation moyenne des cosinus de domaine ≥ 0,2 » | **vrai** |
| **V5, M_bien** | **écart maximal entre statuts = 2,8735** (vrai d'opérateur 3,4443 ; proche 4,9313 ; faux 4,9403 ; vrai conceptuel 5,0104 ; surface 6,3178 ; 6,3178 − 3,4443 = 2,8735) | S13 : « écart entre statuts de la fréquence documentaire observée moyenne de l'étiquette de pont ≤ 0,5 » | **FAUX** |
| V5, M_moyen (rapporté ; hors périmètre de Q-05) | 1,9449 | même seuil | faux s'il était évalué ; sans effet sur le verdict |
| V6, M_moyen | 9,00 vraies paires valides par monde (M_bien rapporté : 12,28) | S13 : « ≥ 6 » | **vrai** |
| S8, plafond de l'oracle | 0,9103 (M_bien) ; 0,7172 (M_moyen) | S8 : « précision de l'oracle supérieure ou égale à ce seuil, en M_bien et en M_moyen » ; valeur 0,30 | **vrai** (les deux) |
| V7 | rapport écrit dans le fichier | § 6 : « rapport sans seuil et sans conséquence » | sans seuil |
| V8 | replantation 4,0 % / 4,7 % ; régénération entière 0 ; exclusion 0 ; paires valides 250,31 / 176,83 | § 6 : « rapport sans seuil » | sans seuil |
| V9 | `V9_J_vraie` = false | § 6 : « J … doit être **fausse** » sur les miroirs de M_inertes | **vrai** (J fausse, attendu ; aucun déclencheur d'audit) |
| Reproduction S12 | NR_bien : b 0,2123 ; a 0,1606 ; c 0,1578 ; d1 0,2319. NR_moyen : b 0,1293 ; a 0,1096 ; c 0,1134 ; d1 0,1761. `reproduction_passee` = true | S12 : « 2 points de chaque côté de l'intervalle à 95 % du tableau de B § 1 pour b, a, c et d1 en NR_bien et NR_moyen » ; bornes élargies du fichier (par exemple d1 NR_moyen [0,135 ; 0,195]) : les huit moyennes y sont | **vrai** |

Constat : **V1 à V4 et V6 vrais ; V5 faux (M_bien) ; S8 vrai ; V9 vrai ; reproduction vraie.** Une seule condition fausse.

## Verdict selon la ligne 0 des tables 1 et 2

Définition du texte (Critères de lecture gelés, booléens) : « V0 = validation du générateur passée (V1 à V6) ∧ aucun arrêt de la liste ∧ taux d'exclusion de chaque condition de décision ≤ taux S11 ∧ nombre de mondes exécuté de chaque condition = son nombre gelé (S15, S7) ou n' (S9) ». V5 fait partie de V1 à V6 et est faux : la validation du générateur n'est pas passée, V0 est fausse (la liste d'arrêt est en outre franchie sur sa première ligne, voir plus bas).

- **Table 1, ligne 0** : « V0 non tenue | **non concluant** ; aucune lecture des contrastes ».
- **Table 2, ligne 0** : « V0 non tenue | **non concluant** ».

**Verdict : NON CONCLUANT sur les deux volets (adoption de N et ingrédient manquant).** Les lignes 1 et suivantes ne s'appliquent pas (« la première ligne dont la condition est vraie décide »). Aucun contraste de décision n'existe ni n'a été lu.

## Ce que le texte prescrit (citations, sans ajout)

1. Liste d'arrêt, première ligne : « Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) | arrêt avant les bras candidats (N et ses ablations) ; correction par une nouvelle version du préenregistrement (R12) ».
2. Critères de lecture gelés, dernière phrase : « Le verdict est scellé puis soumis à Lazar pour GO (R13). »
3. § 9 : la validation du générateur précède « une seule invocation du programme » ; l'arrêt de 1. interdit les bras candidats, donc cette invocation.
4. § 6, V7 : « Une version nouvelle motivée par V7 ne peut être écrite qu'après le verdict scellé (R12) » ; liste d'arrêt : « paramètre modifié après lecture … | arrêt et consignation de l'écart (R1) ».

---

## Hors verdict (n'entre pas dans le verdict ; n'est pas une recommandation de correction)

### A. Accord et désaccords avec `lecture-validation-v1.md` (Opus 5.5)

**Accord sur le fond.** Tous les chiffres des sections 1 et 2 de la lecture, y compris V5 = 2,873 en M_bien, concordent avec les fichiers de résultats ; le verdict « non concluant » par la ligne 0 des deux tables et la citation de la première ligne de la liste d'arrêt sont exacts.

**Désaccords et réserves, par ordre d'importance :**

1. **V8, « le texte ne prévoyait nettement plus de paires valides qu'en M_inertes et M_palettes_communes » : inexact tel que formulé.** C'est ce que dit la ligne de V8 (§ 8, ligne 605), mais le texte dit aussi, dans la section « Hypothèse » (ligne 128) et dans « Prédiction » (ligne 142), que « les paires valides seront bien plus nombreuses que les 67 de v1, b et c y sont diluées », et en S16c (ligne 314) que la précision de b et de c baisse. L'**ordre** du phénomène était donc prévu, non son ampleur (3,7 et 2,9 fois) ; l'ampleur n'était pas quantifiée, et la ligne 605 (« le budget de 12 en couvre environ le cinquième », valeur de v1) est démentie par la mesure. Le point à signaler à Lazar reste fondé, mais comme écart d'ampleur, non comme surprise qualitative.
2. **Périmètre de V5.** La lecture présente V5 en M_moyen comme « rapporté, non soumis au seuil selon Q-05 ». C'est exact (Q-05 : V5 sur M_bien). Je note seulement que le texte de S13 ne limite pas V5 à M_bien (« sur graines distinctes (300 mondes "bien", 300 "moyen", 100 jumelles) ») : cette limite est une lecture validée par l'addendum. Sans conséquence ici, V5 étant faux dans les deux (2,873 ; 1,945).
3. **Section 4 de la lecture (causes de l'échec de V5).** Je ne l'ai pas vérifiée par calcul (interdit) ; j'ai vérifié seulement que les moyennes par statut du fichier sont celles qu'elle cite et que G5 (ligne 481) égalise la loi des émetteurs « pour tous les statuts de pont (vrai, faux, proche) » sans citer vrai d'opérateur ni surface, ce qui est compatible avec son hypothèse principale. Elle reste une hypothèse ; elle n'entre pas dans le verdict.
4. **Section 3 point 4 de la lecture** (questions laissées à Lazar) : fondée, le texte étant muet sur ces points. Je n'ajoute rien.

Aucun autre désaccord : pas de chiffre faux, pas de citation inexacte relevée dans les sections 1, 2, 3 et 5 de la lecture.

### B. Points de propreté R4 signalés par la lecture : fondés ou non

- **V2 peu discriminante : fondé.** F = −0,0854 contre une loi nulle de −0,0865 : l'écart est de 0,0012 ; V2 (« F ≤ 0,10 ») passe avec une marge de 0,185 par un F négatif, c'est-à-dire sans que le canal montre d'excès de lien. Ni exactement nulle (pas de déclencheur « fuite mesurée F exactement nulle »), ni au-dessus du seuil : aucune règle écrite ne se déclenche. Fait, non verdict.
- **Paires valides 250 (bien) et 177 (moyen) contre 68 et 60 en v1 : fondé comme écart d'ampleur** (voir A.1) ; la valeur de v1 est dans le texte (67,55 / 60,50), les nouvelles dans V8 (250,31 / 176,83). Aucun seuil ne lit V8 ; aucun déclencheur d'audit n'y est écrit. Les 250 et 177 ne figurent dans aucun critère.
- **Titre de l'addendum v6 « BROUILLON, NON SCELLÉ » alors qu'il est scellé : fondé.** La ligne 1 du fichier porte « (BROUILLON, NON SCELLÉ ; remplace le brouillon v5 …) » et le texte du même fichier dit en fin « Scellement … aucune lecture de résultat avant (R1) » au futur ; mais le compagnon existe avec l'empreinte `37f6df2e…` égale à celle du fichier, R-656 (`registres/decisions.md`) le déclare scellé à 23:47 UTC, et le code l'a accepté. C'est un défaut de libellé d'un fichier scellé ; il n'entre dans aucun critère de la validation.
- **Autres points de la lecture** (V4 concordance 1,000 attendue par construction ; V1 proche de v1 ; V6 et S8 plus hauts qu'en v1 ; reproduction dans la marge, d1 de NR_moyen à 0,1 point au-dessus de l'intervalle brut, dans la marge) : fondés, aucun suspect ; je les ai vérifiés contre le fichier (V4 : 1,0 et 0,2562 ; d1 NR_moyen : 0,1761 contre borne brute 0,175).
<<<FIN PIÈCE 1>>>

### Pièce 2 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-deux-espaces-v1/experience-v2/lancement-v2/diagnostic-v5-v1/diagnostic-v5-v1.md` (entier) — nœuds N1

Origine : branche de conv-audit ; empreinte du fichier source `2875f4adfd79ecb19143e9a583997c987686b9b2e9db4bbad35d2c8a68f064e8` ; 2590 mots.

<<<DÉBUT PIÈCE 2>>>
# Diagnostic de plomberie de l'échec de V5 — expérience v2 de bisociation à deux espaces — v1

- **Auteur** : sous-agent Opus 5.5 neuf, ni auteur du préenregistrement, ni du code, ni de la lecture, ni du verdict de la validation.
- **Date** : 2026-10-31T00:02:21Z (relevé `date -u` après l'exécution, avant la rédaction).
- **Mission** : préparer la v3 du préenregistrement (décision de Lazar) ; **rien corrigé**. Aucun module existant modifié, rien lu sous `donnees/`, validation et invocation non lancées, aucun `.sha256` écrit, aucun commit.
- **Indices employés** : RACINE_VALIDATION = 20261102, **indices 990000 à 990199**, conditions M_bien (code 1) et M_moyen (code 2). Hors de toute plage du § 7 (validation 0 à 299, étape (1) 300 à 499, audit sans indices fixés ; décision sous RACINE seulement), hors de la reproduction NR (0 à 1199) et des plages d'essai déjà déclarées (920000+, 930000+, 950000–956009, 960000–960002, 970000–972399, 980000–980059 ; addendum v6, ligne 9). Une garde du script le vérifie. Les variantes de générateur tirent leurs émetteurs dans un flux à part, `SeedSequence(entropy=RACINE_VALIDATION, spawn_key=(indice, 7777))`, une clé à deux éléments qu'aucune clé du § 7 n'emploie. Ni RACINE ni aucune autre racine.

Fichiers lus (SHA-256 recalculées ; « compagnon OK » = égale au `.sha256` voisin) :

| Fichier | SHA-256 | Contrôle |
|---|---|---|
| `prereg/preenregistrement-bisociation-deux-espaces-v2.md` (§ 1 G5, G6 ; § 2 ; § 6 V5 ; § 7 ; S13 ; S16d) | `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` | compagnon OK |
| `experience-v2/lancement-v2/lecture-validation-v1.md` | `8c6dd939907a649d76fe1504a1d439d549435687e456f508af60c7bc3286b4e5` | compagnon OK |
| `experience-v2/lancement-v2/verdict-validation-v1.md` | `f5bf86b9d5001f363d0768cd88bebcc1f8e842711fa0c4c578d40debf13e8675` | compagnon OK |
| `experience-v2/monde_v2.py` | `0986a0cbfd48478a17d7a0bae1b69f868fea4a98a431b259dc9ec9b94264c8d0` | compagnon OK |
| `experience-v2/validation_v2.py` (`v5_rarete`, `STATUTS_V5`) | `7e872917ed3383d12c6c76613da64901f2d0dff49ebe0477eb6156b88da8e521` | compagnon OK |
| `experience-v2/mesures_v2.py` (extraits : `classe`, `mecanismes_vrais`) | `40a6f23afbdac6b5f8f46685eb29ab7c7e70489f51129c6da6ab3256572a477b` | compagnon OK |
| `experience-v2/graines_v2.py` | `283d93688a3d03b75d2a9c763f6804e5628cd6d971ff8de4f531bfd94e3e8e4e` | compagnon OK |
| `trancher-recombinaison/monde_v1.py` (`BASE`, `NIVEAUX`, `_articles`) | `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c` | compagnon OK |

Produits (sans compagnon, comme demandé) : `diagnostic_v5_v1.py` (`0d1cbfa5c2a9220ddb7ef6f6aaba5bbf63bf1c5e8bc23b3362113999805d3a59`) et sa sortie `diagnostic-v5-v1-sortie.txt` (`faf75a2e941b066fe184c64fbce1d3ab449e073892a5da32902a95f374b95f8c`), environ 50 secondes de calcul. Commande : `PYTHONPATH=<dépôt>/src python3 -B diagnostic_v5_v1.py`. La grandeur de V5 est calculée par la fonction scellée `validation_v2.v5_rarete`, appelée telle quelle. Les variantes de générateur remplacent **en mémoire** trois fonctions de `monde_v2` (`_planter_v2`, pour capter la liste des articles, `_attribuer_rares` et `_observer_operateurs`), dans ce seul processus. Elles sont restaurées ensuite : contrôle dans la sortie, l'écart M_bien après les variantes est égal à celui du générateur scellé.

---

## 1. Ce qui est mesuré sur les mondes d'essai (990000 à 990199, 200 mondes par condition)

### 1.1 Grandeur de V5, générateur scellé

| | vrai conceptuel | vrai d'opérateur | faux | proche | surface | écart, 5 statuts | écart, 3 statuts à concept rare |
|---|---|---|---|---|---|---|---|
| M_bien, essai | 4,737 | 3,674 | 4,949 | 5,068 | 5,954 | **2,280** | 0,331 |
| M_bien, validation (rappel) | 5,010 | 3,444 | 4,940 | 4,931 | 6,318 | 2,873 | 0,079 |
| M_moyen, essai | 5,860 | 4,331 | 6,689 | 6,341 | 5,947 | **2,358** | **0,828** |
| M_moyen, validation (rappel) | 5,709 | 4,434 | 6,207 | 6,379 | 5,944 | 1,945 | 0,670 |

L'échec se reproduit sur des mondes indépendants : le même ordre (vrai d'opérateur le plus bas, surface la plus haute en M_bien) et le même ordre de grandeur.

### 1.2 Décomposition : quelle étiquette est retenue comme pont, et avec quelle fréquence

On classe l'étiquette retenue par l'étage commun (la plus rare des étiquettes partagées, § 2) pour chaque pont planté valide. Part dans le statut, puis fréquence documentaire observée moyenne :

| M_bien | concept rare planté | étiquette d'opérateur exclusive | opérateur de groupe | repli (concept de fond, moyeu) |
|---|---|---|---|---|
| vrai conceptuel | 0,82 ; 2,82 | — | 0,01 | 0,17 ; fond 15,5 |
| faux | 0,82 ; 2,88 | — | — | 0,17 ; fond 16,7 |
| proche | 0,73 ; 2,96 | — | — | **0,27** ; fond 10,9 |
| vrai d'opérateur | 0,32 ; 2,67 | **jumeau `j{t}` 0,36 ; 2,00 exactement** | greffe plantée 0,26 ; 5,32 | 0,05 |
| surface | — | opérateur solo `s…` 0,35 ; 2,88 | **homonyme d'un opérateur de groupe 0,59 ; 7,17** | 0,04 |

En M_moyen, même structure, avec plus de repli : vrai conceptuel 0,34, faux 0,41, proche **0,50**, vrai d'opérateur 0,14, surface 0,12.

Par statut fin (M_bien), en moyenne : greffe avec trace conceptuelle 4,09, greffe sans trace 6,29 ; jumeau avec trace 2,41, jumeau sans trace 2,93. Un pont d'opérateur qui porte aussi une trace (λ = 0,7) a deux étiquettes partagées (1,96 contre 1,39 à 1,42 pour les autres statuts), et l'étage commun garde la plus rare des deux.

**Repli retiré** (moyenne sur les seuls ponts dont l'étiquette retenue n'est ni un concept de fond ni un moyeu) : les trois statuts à concept rare tombent à 2,90 / 2,88 / 2,96 en M_bien (écart 0,07) et à 2,88 / 2,98 / 3,04 en M_moyen (écart 0,16). Le vrai d'opérateur est à 3,15 et la surface à 5,61 ; l'écart sur cinq statuts reste à 2,73.

Ce que les autres variables ne font pas : le degré moyen (nombre d'étiquettes par article, 3,8 à 5,4) et le nombre d'étiquettes partagées ne jouent qu'à travers les deux mécanismes décrits plus bas (deux canaux pour les ponts d'opérateur avec trace ; repli). La règle de tirage de l'étiquette d'opérateur joue directement : le jumeau `j{t}` est exclusif par construction (fréquence 2) ; l'homonyme de surface reprend un opérateur de groupe, porté par beaucoup d'articles, ou un opérateur solo, exclusif.

### 1.3 Hypothèses testées par variante (écarts de V5 ; seuil 0,5)

| Variante | Nature | M_bien, 5 statuts | M_bien, 3 rares | M_moyen, 5 statuts | M_moyen, 3 rares |
|---|---|---|---|---|---|
| générateur scellé | — | 2,280 | 0,331 | 2,358 | 0,828 |
| H1 sans jumeaux | surcharge `ponts.jumeaux = 0` | 1,863 | 0,553 | 1,237 | 0,091 |
| H2 λ = 0 | surcharge | 1,349 | 0,399 | 0,792 | 0,354 |
| H2′ λ = 1 | surcharge | 2,759 | 0,176 | 2,473 | 1,090 |
| H3 sans concept moyeu | surcharge `p_moyeu_concept = 0` | 2,286 | 0,438 | 1,925 | 0,322 |
| G1 : jumeau `j{t}` avec émetteurs selon S16d | générateur en mémoire | 1,728 | 0,272 | 2,187 | 0,889 |
| G2 : surface avec homonyme exclusif `e{t}` et émetteurs selon S16d | générateur en mémoire | 1,532 | 0,233 | 2,434 | 0,799 |
| G3 = G1 + G2 | générateur en mémoire | 1,293 | 0,331 | 2,275 | 0,841 |
| H4 = G3 + λ = 0 (décomposition seulement ; λ = 0 est exclu par S16a) | les deux | **0,473** | 0,412 | 0,920 | 0,413 |
| **T1** : V5 restreinte aux 3 statuts à concept rare | texte | — | **0,331** | — | **0,828** |
| **T2** : fréquence de l'étiquette du **concept rare planté**, vue des deux côtés, statuts qui en portent un (vrai conceptuel, faux, proche, vrai d'opérateur avec trace) | texte | **0,137** | — | **0,134** | — |
| T3 : médiane au lieu de moyenne (rapportée, non proposée) | texte | 3,0 | — | 2,0 | — |

### 1.4 Bruit de la statistique scellée (erreur type naïve, sd/√n, ponts supposés indépendants, 200 mondes)

Erreur type par statut : M_bien 0,22 / 0,10 / 0,40 / 0,19 / 0,19 ; M_moyen 0,28 / 0,13 / 0,53 / 0,24 / 0,20. Pour une différence entre deux statuts à concept rare : 0,29 à 0,46 en M_bien et 0,37 à 0,60 en M_moyen. À 300 mondes, environ 0,24 à 0,49. Pour T2, l'erreur type par statut est de 0,04 à 0,11.

---

## 2. Causes établies (sur ces mondes d'essai)

1. **Cause principale, propre à la définition : l'étiquette retenue pour les deux statuts « d'opérateur » ne suit pas S16d.** Pour le vrai d'opérateur et la surface, l'étiquette de pont la plus rare est le plus souvent une étiquette d'opérateur, qui suit la loi de v1 (G2) et ses règles de plantation :
   - **le jumeau `j{t}` est exclusif par construction** : fréquence 2 exactement, 36 % des ponts vrais d'opérateur valides ;
   - **l'homonyme de surface reprend l'opérateur `o_b`** : 7,17 quand c'est un opérateur de groupe (59 %), 2,88 quand c'est un solo (35 %) ;
   - **double canal** : un pont d'opérateur avec trace (λ = 0,7) a deux étiquettes partagées, et le minimum des deux est plus bas (greffe 4,09 avec trace, 6,29 sans).

   Établi par les variantes. Retirer les jumeaux (H1), retirer la trace (H2), donner la loi S16d aux étiquettes d'opérateur de pont (G1, G2, G3) : chacune réduit l'écart, et seule leur conjonction H4 le ramène à 0,47 en M_bien. L'hypothèse de la lecture R13 est donc confirmée, avec un ajout : le double canal des ponts d'opérateur, qu'aucune égalisation des lois ne supprime.

2. **Cause secondaire, présente dans tous les statuts : le repli.** Quand le concept rare n'est pas observé des deux côtés (couverture 0,85 ; 0,85² ≈ 0,72 en M_bien et 0,65² ≈ 0,42 en M_moyen), la paire reste valide par un concept de fond ou un moyeu partagé (fréquence 10 à 17), qui devient l'étiquette retenue. La moyenne par statut est alors celle d'un mélange : environ 2,9 avec la probabilité 1 − part de repli, environ 13 avec la part de repli. Or cette part dépend du statut :
   - **proche** (même champ, donc palette de fonds commune) : 0,27 en M_bien, 0,50 en M_moyen ;
   - **faux** : la plupart sont filtrés par les contraintes, et les survivants ont une composition différente.

   Sans repli, les trois statuts à concept rare sont égaux à 0,07 et 0,16 près. Le repli est **la cause de l'écart de 0,83 entre les trois statuts que S16d égalise en M_moyen** ; en M_bien, il porte ces trois statuts à 0,33 sur les mondes d'essai (0,08 en validation).

3. **Conséquence établie : avec cette statistique, le seuil de 0,5 est au niveau du bruit.** Le mélange a une queue lourde. L'erreur type d'une différence entre deux statuts gouvernés par la même loi est de 0,3 à 0,6 à 200 ou 300 mondes. Même à lois égales, V5 telle qu'écrite échouerait souvent ; les 0,08 de la validation entre les trois statuts rares étaient en partie une chance d'échantillonnage. Aucune variante de générateur n'y remédie : G3 laisse 0,33 et 0,84 sur les trois statuts rares.

**Ce qui ramène l'écart sous 0,5 sur ces mondes** : seulement **T2**, un changement du **texte** de V5 (0,137 en M_bien, 0,134 en M_moyen, erreur type 0,04 à 0,11). Aucune variante du générateur admissible sous S16a (λ ∈ ]0 ; 1[) ne passe. H4 passe en M_bien (0,47) mais exige λ = 0, exclu par le texte, et échoue en M_moyen (0,92). T1 passe en M_bien (0,33), échoue en M_moyen (0,83), et reste au niveau du bruit.

**M_moyen (1,945 en validation) : même cause, plus le repli.** Le vrai d'opérateur y est toujours le plus bas, par le jumeau exclusif et le double canal (cause 1). Le repli, plus fréquent (couverture 0,65), écarte en plus les trois statuts rares entre eux (cause 2). La surface se retrouve au milieu, parce que le repli relève les autres statuts : l'écart maximal y oppose vrai d'opérateur et faux (ou proche), non vrai d'opérateur et surface.

Réserves : 200 mondes par condition, une seule graine de flux pour les variantes. Les erreurs types sont naïves (elles ignorent la corrélation entre ponts d'un même monde, faible ici, et un pont au plus par statut et par paire). Les variantes G1 à G3 sont **une** façon de donner la loi S16d aux étiquettes d'opérateur (émetteurs par mot de domaine, couverture du lexique d'opérateurs) ; une autre implémentation pourrait donner d'autres chiffres, sans pouvoir lever le double canal.

---

## 3. Ce que la v3 devrait changer — options pour Lazar (aucune recommandation de seuil assoupli)

Le seuil 0,5 (S13) n'est pas en cause dans les options ci-dessous ; c'est la **grandeur** mesurée par V5 qui ne correspond pas à ce que S16d promet.

- **Option A — changer le texte de V5 en T2.** « Pour chaque statut portant un concept rare planté (vrai conceptuel, faux, proche, vrai d'opérateur avec trace), fréquence documentaire observée moyenne de l'étiquette de ce concept, sur les ponts plantés valides où les deux articles l'observent ; écart maximal entre statuts ≤ 0,5. »
  - Avantage : mesure exactement ce que S16d égalise ; passe sur les mondes d'essai avec une erreur type de 0,04 à 0,11, donc un seuil de 0,5 devient discriminant.
  - Inconvénient : c'est un contrôle de plomberie de S16d, presque acquis par construction ; il ne dit plus rien de la rareté de l'étiquette **retenue** par l'étage commun, c'est-à-dire de ce que voient les bras, ni des statuts vrai d'opérateur sans trace et surface.
- **Option B — A, plus un rapport sans seuil de l'ancienne grandeur.** Garder la grandeur scellée (étiquette retenue, cinq statuts) comme **rapport sans seuil**, avec sa décomposition (part de repli, type d'étiquette), à la manière de V7.
  - Avantage : la séparation possible des statuts par la rareté de l'étiquette retenue, qui est le risque visé par CB-05 (« la rareté ne doit pas séparer vrai de faux »), reste visible.
  - Inconvénient : ce risque n'est plus gardé par un seuil, alors qu'il existe : par la rareté de l'étiquette retenue, vrai d'opérateur et proche diffèrent ici d'environ 1,4 en M_bien.
- **Option C — changer le générateur pour que toute étiquette de pont planté suive S16d.** Jumeau à émetteurs, homonyme de surface exclusif à émetteurs (G3), en gardant le texte de V5.
  - Avantage : rapproche les lois des étiquettes d'opérateur et de concept.
  - Inconvénient : **ne suffit pas** (1,29 et 2,27 sur les mondes d'essai). Le double canal des ponts d'opérateur avec trace et le repli restent, et la statistique reste au niveau du bruit. Modifier G2 et G6 change aussi le monde de v1 repris tel quel, donc la non-régression et la force d'une hypothèse (nœud de décision, S16). À combiner avec A ou B, jamais seul.
- **Option D — restreindre V5 aux trois statuts à concept rare (T1), sans changer la grandeur.**
  - Avantage : changement minimal du texte.
  - Inconvénient : échoue en M_moyen sur les mondes d'essai (0,83) et reste au niveau du bruit en M_bien (0,33 pour une erreur type de 0,3 à 0,46). Il faudrait aussi dire si V5 porte sur M_moyen : Q-05 la limite à M_bien, ce que le texte de S13 ne dit pas.

Points à fixer dans la v3, quelle que soit l'option :
1. Déclarer que la grandeur de l'étiquette « retenue » mélange une étiquette rare et un repli (fond, moyeu) dont la part dépend du statut, et nommer ce mécanisme.
2. Déclarer ce qui a été lu : la validation V1 à V9, la lecture et le verdict, ainsi que le présent diagnostic sur les indices 990000 à 990199.
3. Fixer de nouvelles plages de graines de validation, sans réemploi des indices 0 à 299 dont les résultats sont lus (question (c) de la lecture R13).
4. Ne pas toucher à S16 sans décision : λ = 0, la seule variante de générateur qui approche le seuil en M_bien, est exclu par S16a.
<<<FIN PIÈCE 2>>>

### Pièce 3 — `prereg/preenregistrement-bisociation-deux-espaces-v2.md` (l. 283–300 ; 555–586 ; 617–688 ; 689–735) — nœuds N1

Origine : branche de conv-audit ; empreinte du fichier source `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` ; 5560 mots.

<<<DÉBUT PIÈCE 3>>>
**S13 — seuils de validation du générateur (§ 6), sur graines distinctes (300 mondes « bien », 300 « moyen », 100 jumelles)**
- V1 cosinus moyens, même domaine / proches / éloignés ; valeur gelée par Lazar (R-580), égale à la recommandation : [0,51 ; 0,57], [0,25 ; 0,31], [0,00 ; 0,06]. Raison : référence de v1 0,54 / 0,28 / 0,03 (B § 5) ± 0,03.
- V2 fuite de domaine F (formule au § 6) en « bien » ; valeur gelée par Lazar (R-580), égale à la recommandation : F ≤ 0,10. Raison : avis d'Opus (« fuite ≤ 10 points en bien ») ; reprise sans changement.
- V3 queue (formule au § 6) ; valeur gelée par Lazar (R-580), égale à la recommandation : excès ≤ 0,10. Raison : brouillon 1, sans élément pour en changer.
- V4 jumelles (formules au § 6) ; valeur gelée par Lazar (R-580), égale à la recommandation : concordance des étiquettes de concept ≥ 0,9 et variation moyenne des cosinus de domaine ≥ 0,2. Raison : brouillon 1 ; seuil de l'avis d'Opus pour la concordance (0,8) relevé à 0,9 parce que le test porte ici sur un générateur et non sur des annotateurs.
- V5 rareté appariée ; valeur gelée par Lazar (R-580), égale à la recommandation : écart entre statuts de la fréquence documentaire observée moyenne de l'étiquette de pont ≤ 0,5. Raison : brouillon 1.
- V6 vraies paires valides par monde en « moyen », en moyenne ; valeur gelée par Lazar (R-580), égale à la recommandation : ≥ 6. Raison : brouillon 1 ; v1 faisait 5,97 (`daaef112…`), donc le seuil est à la limite de v1, et v2 ajoute des ponts conceptuels visibles par le canal, donc l'attendu est au-dessus.

**S14 — J, condition de jugeabilité : borne basse à 95 % de Δ(d1c, c) strictement supérieure à ce seuil, en M_bien et en M_moyen (J(M_bien) et J(M_moyen))**
- Valeur (gelée par Lazar, R-580) : la recommandation de l'auteur ci-dessous, telle qu'écrite.
- Recommandation de l'auteur : 0 (borne basse > 0).
- Raison : J ne dépend pas de la forme de N (d1c et c sont des témoins) et sépare « canal inexploitable dans ce monde » de « N ne sait pas l'exploiter » (CB2-01). **Portée (CB3-06 ii)** : J lit, comme d1c, l'étiquette de concept partagée la plus rare, non κ ; elle **ne détecte pas** un canal écrasé par les concepts de fond (CB2-03) : sa portée est plus étroite que « canal inexploitable ». **Prédiction (CB3-06 i)** : la chaîne de v1 donne d1c − c ≈ +9,2 « bien » et +6,1 « moyen » (M : +4 − (−5,23) et +4 − (−2,06), `daaef112…`), fourchette +5 à +12 et +3 à +10 (ligne PJ de la section « Prédiction ») : J est presque acquise sous les prédictions ; le script version 2 prend le bas de la fourchette (+5 ; +3) pour les probabilités d'adoption (la version 1 prenait 3 partout). Ordre de grandeur favorable en v1 : d1 − c = +8,75 « bien » et +5,83 « moyen » (M, 3,52 + 5,23 et 3,77 + 2,06, `daaef112…`). Puissance (script § 11, n = 2 400) : un effet vrai de 1,5 point ou plus est détecté avec la probabilité 1,00 ; de 1 point, 0,89 / 0,80 (conjonction des deux conditions, σ « moyen » 11 / 15,3) ; de 0,5 point, 0,22 / 0,13 ; à effet nul, J passe à tort avec 0,02 par condition. Un seuil plus haut (par exemple 1 point) exclut aussi les canaux à peine exploitables ; non recommandé, faute de repère. **Essai R5 d'artefact (CB3-06 iii)** : sur les 300 mondes de validation de `M_inertes`, où J doit être fausse ; fausse alerte 0,02 à effet nul, 0,92 pour un effet parasite de +3 (script § 21 ; V9).

**S15 — nombre de mondes par condition (hors NR, fixé par S7), avant extension éventuelle par S9**
- Valeur (gelée par Lazar, R-580) : la recommandation de l'auteur ci-dessous, telle qu'écrite.
- Recommandation de l'auteur : **2 400** pour M_bien, M_moyen et M_inertes ; **600** pour SP, INV et V_fuite ; **600** pour chacune des **huit** conditions descriptives (M_mal, V_concepts_absents, V_moyeu_conceptuel, V_surface, M_couplage_faible, M_palettes_communes, M_palettes_disjointes, **M_fonds_1ou2**). Total : 11 400 mondes de décision (dont NR 2 400) et 4 800 descriptifs, soit 16 200 ; 23 400 au plus avec l'extension de S9 à 4 800 pour les trois grandes conditions (script § 15). Mondes de validation du générateur, hors S15 : 300 « bien », 300 « moyen », 100 jumelles et 300 miroirs de `M_inertes`.
- Raison : même puissance pour M_bien, M_moyen et M_inertes (A8 : 0,975 à effet nul) ; processeur seul, aucune dépense ; SP reste à 600 parce que la puissance n'y joue pas (la différence vraie y est nulle par construction, CB2-05) ; INV et V_fuite à 600 : A4 et A6 détectent un effet de −3 points avec 0,99 (σ 15,3, M_bien à 2 400, script § 10). M_fonds_1ou2 à 600 : le contraste 39 (différence avec M_bien, descriptive, sans verdict) a une erreur type de 0,50 à 0,70 point (σ 11 à 15,3, script § 24). Ce gel **remplace** le défaut D-g (1 200 mondes). Options : 1 200 (n du brouillon 2 : adoption 0,49 / 0,26 aux centres du brouillon 2, script § 12) ; 4 800 (plafond de S9).

[…]
### 6. Conditions et validation du générateur

Les nombres de mondes sont ceux de S15 (hors NR : S7) ; ceux de M_bien et M_moyen sont étendus par S9 s'il y a lieu ; M_inertes prend celui de M_bien. Les paramètres de monde sont ceux de S16.

| Condition (code de graine) | Mondes | Définition |
|---|---|---|
| M_bien (1), M_moyen (2) | S15, S9 | niveaux bien et moyen du G9 ; paramètres S16 |
| M_mal (3) | S15 | niveau mal ; descriptive, abandonnée si le plafond de l'oracle < S8 |
| SP (4) | S15 | M_bien sans aucun pont planté ; vérité vide ; mesure : précision placebo (**contrôle de plomberie**, A3) |
| INV (5) | S15 | M_bien, monde inversé du G10 |
| V_fuite (6) | S15 | M_bien avec ρ = 0,6 |
| V_concepts_absents (7) | S15 | M_bien sans aucune étiquette de concept (κ = 0 déclaré ; N se réduit à N_β0 par la règle du § 3 : identité **déclarée d'avance** ; d1c non applicable) |
| V_moyeu_conceptuel (8) | S15 | concept moyeu à 0,6 |
| V_surface (9) | S15 | ponts de surface portés à n_e' et (c), (d) ramenés à n_c', n_d' (S16e : 36 articles de ponts) |
| NR_bien (10), NR_moyen (11) | S7 | `monde_v1.py` inchangé, graine de monde = premier mot de `SeedSequence(...).generate_state(1)` passé à `random.Random` ; concept := étiquette d'opérateur ; d1c ≡ d1 |
| **M_inertes (12)** | = n de M_bien | monde miroir du G8 sur les graines de M_bien (rôles 0 à 3 sous le code 1, miroir sous le code 12) |
| M_couplage_faible (13) | S15 | M_bien avec λ_faible (S16a) ; descriptive (dose-réponse P12) |
| M_palettes_communes (14) | S15 | M_bien avec `taille_palette` = 10 (tous les champs partagent les 10 concepts : proximité conceptuelle neutre au champ) ; descriptive |
| M_palettes_disjointes (15) | S15 | M_bien avec palettes disjointes (10 concepts répartis entre champs, au moins 2 par champ : le monde du brouillon 1) ; descriptive |
| M_fonds_1ou2 (16) | S15 | M_bien avec 1 concept de fond par article (probabilité 0,6) ou 2 (probabilité 0,4), la loi du brouillon 2 (CB3-04) ; descriptive (contraste 39 : effet de S16c sur Δ(N, N_β0)) |

**Validation du générateur, avant les bras candidats (N et ses ablations ; seuls les témoins d1c et c y sont calculés, pour V9 ; contre-lecture 4, N4), sur graines de validation (RACINE_VALIDATION, indices 0 à 299, § 7) (300 mondes « bien », 300 « moyen », 100 jumelles, et 300 miroirs de `M_inertes` des 300 « bien », pour l'essai R5 de J (V9)) ; seuils S13.** Formules :
- **V1** cosinus moyens, par paire d'articles du même domaine / de domaines proches / éloignés, moyennés sur les mondes.
- **V2 — fuite de domaine** F = ρ_S(κ_obs, cos_obs) − ρ_S(κ_lat, cos_obs), où ρ_S est la corrélation de rangs de Spearman calculée sur les 780 paires d'articles de chaque monde, puis moyennée sur les mondes « bien » ; κ_lat est le cosinus des vecteurs de concepts **latents** (même pondération par la fréquence documentaire latente). Elle mesure l'excès de lien entre proximité conceptuelle et proximité de domaine introduit par le canal d'observation, au-delà de celui, légitime, des palettes. Loi nulle rapportée : F après permutation des vecteurs de concepts observés entre articles d'un même domaine observé.
- **V3 — queue** : sur les paires valides d'un monde, part de paires du même champ parmi les 10 % de plus fort κ_obs, moins la même part parmi les 10 % de plus fort κ_lat ; moyenne sur les mondes.
- **V4 — jumelles** : le monde est régénéré en échangeant les mots propres de deux domaines pour les articles de ponts, mêmes latents et même flux de graines pour les rôles 1 à 3. Concordance = part des couples (article, étiquette de concept observée) identiques entre le monde et sa jumelle, sur les articles de ponts ; variation des cosinus = moyenne de |cos_obs(monde) − cos_obs(jumelle)| sur les paires plantées. **Ce test ne vérifie que l'absence de couplage dans le code** (par construction des flux de graines, la concordance est attendue proche de 1) ; il ne dit rien du vocabulaire réel, qui relève du préenregistrement sur fiches réelles.
- **V5** rareté appariée : pour chaque statut (vrai conceptuel, vrai d'opérateur, faux, proche, surface), fréquence documentaire observée moyenne de l'étiquette de pont retenue sur les paires plantées valides ; écart maximal entre statuts.
- **V6** vraies paires valides par monde, plafond de l'oracle (S8).
- **V7 (rapport sans seuil et sans conséquence, CB-13)** : loi de κ observé et de cos observé par classe de paire — vrai conceptuel direct, vrai d'opérateur avec trace conceptuelle, vrai d'opérateur sans trace, faux pont, pont proche, paire d'émetteur de surface, fond partagé entre champs, fond partagé dans un champ — moyenne et déciles. Rapportée **avant** les méthodes, pour ne pas régler le monde sur N. **V7 est lu mais ne change rien** : aucun paramètre de monde n'est modifié après sa lecture ; **V7 ne déclenche rien** (contre-lecture 4, N3 : le jugement « monde mal réglé » du brouillon 4 n'avait pas de critère opérationnel, il est retiré) : un canal de concepts mal réglé se lit seulement par les règles écrites — J (Table 1 ligne 8, Table 2 ligne 4), A7 (Table 1 ligne 9) et les déclencheurs d'audit —, jamais par un jugement sur V7 ; aucun paramètre n'est modifié après sa lecture (CB2-03). Une version nouvelle motivée par V7 ne peut être écrite qu'après le verdict scellé (R12).
- **V8 (rapport sans seuil)** : comptes de vraies paires par mécanisme (greffe, jumeau, pont conceptuel direct, expansion), taux d'exclusion, taux de régénération, nombre moyen de paires valides par monde et par condition (en v1 : 67,55 / 60,50 / 53,59).
- **V9 — essai R5 de J (CB3-06 iii)** : sur 300 mondes de validation de `M_inertes` (miroirs des 300 mondes « bien » de validation, mêmes latents), J = borne basse à 95 % de Δ(d1c, c) > 0 doit être **fausse** (les étiquettes de concept y sont inertes). J vraie est un **déclencheur d'audit R4** (probabilité 0,02 à effet nul, 0,92 pour un effet parasite de +3, script § 21), jamais un arrêt ; **l'audit qu'il déclenche est rendu et scellé avant l'invocation unique des mondes de décision (§ 9)**, qui n'a pas lieu tant qu'il ne l'est pas. Ne calcule que les témoins d1c et c, jamais N ; seul le booléen est imprimé.

[…]
## Critères de lecture gelés

Un sous-agent neuf (ni auteur du présent préenregistrement ni de l'analyse, R13) applique ces tables telles qu'elles sont écrites. Les seuils S1 à S17 sont gelés avant scellement. « Les deux » = M_bien et M_moyen. Chaque table se lit **de haut en bas : la première ligne dont la condition est vraie décide** ; les conditions des lignes suivantes supposent les précédentes fausses, de sorte que les lignes sont exclusives et exhaustives (la dernière ligne est le complémentaire).

**Booléens** (X ∈ {M_bien, M_moyen} ; Δ(·, · ; X) = écart apparié dans X ; lb95, ub95 = bornes basse et haute à 95 % ; lb99 = borne basse à 99 %) :
- V0 = validation du générateur passée (V1 à V6) ∧ aucun arrêt de la liste ∧ taux d'exclusion de chaque condition de décision ≤ taux S11 ∧ nombre de mondes exécuté de chaque condition = son nombre gelé (S15, S7) ou n' (S9) ;
- perd(X) = ub95 Δ(N, b ; X) < 0 ;
- A1(X) = estimation de Δ(N, b ; X) ≥ θ_abs ∧ r(N, b ; X) ≥ θ_rel ∧ lb95 Δ(N, b ; X) > 0 ;
- A2(X) = lb95 Δ(N, a ; X) > 0 ∧ lb95 Δ(N, d1 ; X) > 0 ∧ lb95 Δ(N, d1c ; X) > 0 [∧ lb95 Δ(N, b_eloigne ; X) > 0 **si S17 = option 1**] ;
- suffit_d1c(X) = ub95 Δ(N, d1c ; X) ≤ 0 ; **suffit_d1(X) = ub95 Δ(N, d1 ; X) ≤ 0** (CB2-02, symétrique de suffit_d1c : sans elle, ub95 Δ(N, d1) ≤ 0 tombait dans « indécis ») ; **suffit_b_eloigne(X) = ub95 Δ(N, b_eloigne ; X) ≤ 0** (seulement si S17 = option 1) ;
- A7(X) selon S3 : **forme F-A (recommandée) A7(X) = D0(X) = détecte(Δ(N, N_β0 ; X), δ)** sous la règle S4 (R-A : estimation ≥ δ ∧ lb95 > 0) ; forme F-B : A7(X) = lb95 Δ(N, N_β0 ; X) > 0 ; même contraste que P4 ;
- **J(X) = lb95 Δ(d1c, c ; X) > seuil S14** (canal jugeable : un bras simple qui lit les étiquettes de concept bat le tirage uniforme, sans N) ;
- A3 = dans SP, aucun des écarts N − b, N − d1c, N − N_β0 (précision placebo) n'a un intervalle à 99 % qui exclut 0 (contrôle de plomberie : fausse alerte de probabilité 0,03 ; **déclencheur d'audit seulement, il ne figure plus dans la ligne 5 de la Table 1**, CB3-08) ;
- A4 = ub95 (Δ(N, b ; INV) − Δ(N, b ; M_bien)) < 0 ;
- A5 = lb99 Δ(N, b ; NR_bien) ≥ marge S7 ∧ lb99 Δ(N, b ; NR_moyen) ≥ marge S7 ;
- A6 = ub95 (Δ(N, b ; V_fuite) − Δ(N, b ; M_bien)) < 0 ;
- A8 = dans M_inertes, lb95 Δ(N, N_β0) ≤ 0 ∧ ub95 Δ(N, N_β0) < δ_non (contrôle de spécificité, nécessaire mais faible) ;
- détecte(Δ, δ) : selon la règle S4 (R-A ou R-B) ;
- N0(X) = ub95 Δ(N, N_β0 ; X) < δ_non ; NF(X) = ub95 Δ(N, N_filtre ; X) < δ_non ;
- D0(X) = détecte(Δ(N, N_β0 ; X), δ) ; DF(X) = détecte(Δ(N, N_filtre ; X), δ) ; **sous S3 = F-A, A7(X) ≡ D0(X)** ;
- PG(X) = lb95 Δ(N, N_PCg ; X) > 0 ;
- gain_contrôle = (lb99 Δ(N_PCg, N_β0 ; X) > 0 pour au moins un X) ∨ (lb95 Δ(N, N_β0) > 0 dans M_inertes).

**Audit de symétrie (R4)**, déclenché par un résultat trop propre **ou** trop mauvais, un seul seuil pour les deux sens (S10) :
- |Δ(N, b ; X)| ≥ seuil S10 pour au moins un X ;
- précision de N ≥ (rapport S10) × précision de l'oracle dans une condition de décision ;
- N identique au bit près à N_global, N_β0 ou à un témoin **sur tous les mondes d'une condition**, hors identités déclarées d'avance (N ≡ N_β0 dans V_concepts_absents ; d1c ≡ d1 dans NR_bien et NR_moyen) ;
- un écart de contrôle excluant 0 : A3 en défaut, gain_contrôle ;
- **J vraie sur les 300 mondes de validation de `M_inertes`** (V9 : les étiquettes de concept y sont inertes) ;
- **N ne bat pas la forme corrigée de v1** : ub95 Δ(N, a ; X) ≤ 0 pour au moins une condition X (P15 ; CB3-09) ;
- fuite mesurée F exactement nulle (à 10⁻¹² près) ; concordance des étiquettes avec la vérité > 0,99.

Contenu de l'audit : relecture du code par un sous-agent neuf pour vérifier qu'aucune méthode ne lit un champ latent (lecture, exception `AccesLatent`, balayage statique) ; relance sur les graines de validation (RACINE_VALIDATION) ; test de permutation = recalcul du placebo N_PCg (permutation globale des vecteurs de concepts) sur ces graines. **Issue, sans autre jugement (contre-lecture 4, N3)** : « artefact trouvé » si et seulement si le rapport d'audit scellé constate l'une au moins des trois choses suivantes : (i) un bras lit un champ latent (exception `AccesLatent` levée à la relance, ou appel à un champ de `Latent` trouvé par le balayage statique dans le code d'un bras) ; (ii) sur les graines de validation, la borne basse à 99 % de Δ(N_PCg, N_β0) est > 0 en M_bien ou en M_moyen (l'une suffit) ; (iii) une erreur de code nommée (fichier, ligne, effet), avec un essai sain et un essai d'artefact (R5) écrits par le sous-agent d'audit, dont la correction déplace, sur les graines de validation, au moins un contraste décisif du § 7 (1 à 9 et 11 à 15, plus 20 si S17 = option 1) de plus que sa demi-largeur à 95 %. Sinon : « aucun artefact ». « Artefact trouvé » → verdict **non concluant** et version nouvelle du préenregistrement (R12) ; « aucun artefact » → les tables ci-dessous s'appliquent telles quelles, le rapport d'audit étant scellé. **Audit déclenché par V9 (rendu avant l'invocation des mondes de décision, § 9 ; vérification, R2)** : il se limite à la relecture du code et à la relance des seuls témoins d1c et c sur les graines de validation ; aucun bras candidat (N, ses ablations, ses placebos dont N_PCg) n'est exécuté ; (i) s'y applique ; (ii) ne s'y applique pas ; (iii) y porte sur Δ(d1c, c) dans les miroirs de validation de `M_inertes`. Ses issues sont les mêmes. **Note de lecture (vérification, R2 (3))** : si gain_contrôle est vrai sur les mondes de décision alors que (ii) est négatif sur les graines de validation (« aucun artefact »), ce n'est pas une divergence : les tables s'appliquent telles quelles et gain_contrôle décide (Table 1 ligne 5, Table 2 ligne 3 : N non adoptée, direction prudente). La non-régression (C11), sans code de contraste au § 7, n'entre pas dans la liste de (iii).

### Table 1 — volet d'adoption

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | V0 non tenue | **non concluant** ; aucune lecture des contrastes |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant** (audit en attente) |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | perd(M_bien) ou perd(M_moyen) | **N perd contre le stratifié** ; N non adoptée |
| 4 | non (A1(M_bien) et A1(M_moyen)) | **N sous le seuil** ; N non adoptée |
| 5 | A4, A5, A6 ou A8 non tenue, ou gain_contrôle (A3 est un déclencheur d'audit, non une condition de cette ligne : CB3-08) | **contrôle en défaut** ; N non adoptée |
| 6 | suffit_d1c(M_bien) et suffit_d1c(M_moyen) | **« Swanson guidé par concepts suffit »** (issue permise) ; N non adoptée |
| 7 | suffit_d1(M_bien) et suffit_d1(M_moyen) | **« Swanson par opérateur suffit »** (issue permise) ; N non adoptée |
| 8 | non (J(M_bien) et J(M_moyen)) | **non concluant : canal non jugeable** ; aucune lecture du terme de concept ; N non adoptée à ce stade |
| 9 | non (A7(M_bien) et A7(M_moyen)) **ou N0(M_bien) ou N0(M_moyen)** (CB3-01 ; le second terme est redondant sous S3 = F-A et nécessaire sous F-B) | **« l'éloignement suffit : N_β0 ou b_eloigne, pas N »**, ou le terme de concept n'est pas démontré ou n'apporte rien, **le canal étant jugeable** ; N non adoptée |
| 9 bis (seulement si S17 = option 1) | suffit_b_eloigne(M_bien) et suffit_b_eloigne(M_moyen) | **« l'éloignement par strates de v1 suffit : b_eloigne, pas N »** ; N non adoptée |
| 10 | A2(M_bien) et A2(M_moyen) | **N adoptée, sous W1 à W4** (volet d'adoption ; le concept observé porte de la vérité par construction du monde). **N'autorise que le passage descriptif sur fiches réelles (§ 10), jamais la production** |
| 11 | tout autre cas | **indécis** |

### Table 2 — volet « ingrédient manquant, sous W1 à W4 »

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | V0 non tenue | **non concluant** |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant** (audit en attente) |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | gain_contrôle | **non** : un gain apparaît quand le concept est inerte ou permuté, donc il n'est pas celui de la valeur conceptuelle |
| 4 | non (J(M_bien) et J(M_moyen)) | **non concluant : canal non jugeable** (CB2-01) : un échec de N ne se lit pas comme « le concept n'apporte rien » |
| 5 | N0(M_bien) et N0(M_moyen) | **non** : le terme de concept n'apporte rien, **le canal étant jugeable** |
| 6 | D0(M_bien) et D0(M_moyen) et NF(M_bien) et NF(M_moyen) | **non** au sens de la question : le concept **suffit comme filtre** ; son entrée dans l'objectif n'apporte rien de plus |
| 7 | D0 et DF et PG dans les deux, et A8 | **oui, sous W1 à W4** : dans un monde où la proximité conceptuelle observée porte de la vérité, et seulement là, la proximité conceptuelle dans l'objectif apporte plus que l'éloignement seul et que le filtre. Ce verdict ne dit rien du monde réel |
| 8 | tout autre cas | **indécis** |

Notes de lecture : dans la Table 1, les lignes 6 et 7 se lisent dans cet ordre ; la ligne 8 (J) précède la ligne 9 (A7) parce qu'un échec de A7 n'a de sens que si le canal est jugeable. Dans la Table 2, les lignes 5 et 6 sont exclusives parce que N0 suppose une estimation < δ_non < δ et D0 une estimation ≥ δ ; les lignes 6 et 7 le sont parce que NF suppose une estimation < δ_non et DF une estimation ≥ δ. Les deux tables sont indépendantes : « N adoptée » peut coexister avec « indécis » sur l'ingrédient. Une valeur de N − N_filtre entre δ_non et δ donne « indécis ». La ligne 9 bis (seulement si S17 = option 1) suit la ligne 9 et précède la ligne 10 : elle ne s'applique que si le terme de concept est démontré (A7) et que b_eloigne bat tout de même N. **Sous S3 = F-A, A7 ≡ D0 : « N adoptée » (A7 dans les deux) exclut N0 dans l'une et l'autre condition ; la ligne 5 de la Table 2 (« le terme de concept n'apporte rien ») ne peut donc pas coexister avec la ligne 10 de la Table 1. La ligne 6 de la Table 2 (« le concept suffit comme filtre ») le peut (CB3-01).**

Lecture secondaire, sans effet sur le verdict : la valeur du second espace est Δ(N, N_α0) ; la place du déterminant sur les paires est Δ(N_dpp, N_global), Δ(N_dpp, N) et Δ(N_dpp, N_dpp_β0) (P13) ; la valeur de q est Δ(N_q, N) ; la part d'information de domaine et d'article, Δ(N_PC, N_PCg) et Δ(N, N_PC) ; la pente selon le couplage (P12) ; l'axe palettes (M_palettes_communes, M_palettes_disjointes) ; la chaîne de cohérence de la section « Prédiction » (contrastes 33 à 38 du § 7) ; l'écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes) ; la part des 12 paires de chaque bras dont le seul concept partagé est un concept de fond.

Aucune lecture avant scellement ; rien de ces tables ne change après lecture ; toute déviation est écrite comme telle (R1). Le verdict est scellé puis soumis à Lazar pour GO (R13).

[…]
## Liste d'arrêt

| Condition | Action |
|---|---|
| Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) | arrêt avant les bras candidats (N et ses ablations) ; correction par une nouvelle version du préenregistrement (R12) |
| Noyau non défini positif ou pivot choisi ≤ 0, détecté par `cholesky` du noyau entier ou par `glouton_paires` / la copie gardée (N_dpp, N_dpp_β0, N_fiches, a) | arrêt du bras et du run ; **jamais de repli silencieux** (R5) ; consigné |
| Balayage statique : un `except` (spécifique ou générique) autour d'un appel à `cholesky`, `glouton_paires` ou à la copie gardée dans le code des bras | arrêt : le code est refusé |
| NaN, division par zéro ou κ hors [0, 1] (tolérance 10⁻⁹) dans un score | arrêt |
| Vecteur de concepts nul non compté | arrêt |
| Accès d'un bras à `Latent` (`AccesLatent`) | arrêt du run ; audit R4 |
| Plafond de l'oracle < S8 en M_bien ou en M_moyen | arrêt : monde non jugeable |
| Écart-type σ̂ de Δ(N, b) sur les 200 mondes de validation > écart-type de référence de S9, en « bien » ou en « moyen » | **pas d'arrêt** (CB2-06) : extension du nombre de mondes de la condition à n' (S9), calculée et consignée dans le manifeste scellé avant le premier monde de décision ; au plafond de 4 800 : exécution au plafond, erreur type atteinte rapportée |
| Nombre de mondes exécuté d'une condition différent de son nombre gelé (S15, S7) ou de n' (S9) | arrêt |
| Manifeste de S9 scellé après le premier fichier de résultats de décision (horodatage ou empreinte), n' du manifeste différent du calcul à partir de σ̂, ou mondes de décision exécutés en plusieurs invocations ou étendus après une lecture | arrêt ; V0 fausse, verdict « non concluant » (ligne 0) ; contrôle fait par le lecteur de la porte (R13) |
| Taux de mondes exclus > S11 dans une condition de décision | arrêt |
| Taux de mondes régénérés après échec de plantation > S11 | arrêt |
| Bras de sortie vide avant complément sur plus de S11 des mondes ; précision (placebo comprise) hors de [0 ; 1] | arrêt |
| Configuration de monde hors garde (S16e) : 2 × nombre de paires de ponts > 36, ou concepts rares requis > 18, ou loi du nombre de concepts de fond de M_fonds_1ou2 dont les probabilités ne somment pas à 1 | arrêt |
| Latents d'un monde de M_inertes différents de ceux du monde de M_bien de même indice (comparaison bit à bit) | arrêt |
| Écart de contrôle excluant 0 (SP, N_PCg, M_inertes), J vraie sur les miroirs de validation de M_inertes (V9), ou N qui ne bat pas la forme corrigée a (P15) | audit R4 ; verdict « non concluant » tant que non rendu (SP : fausse alerte de probabilité 0,03, CB2-05 ; J sur les miroirs : 0,02 à effet nul) |
| Reproduction : moyennes de b, a, c, d1 sur NR_bien et NR_moyen hors de l'intervalle de B § 1 élargi de la marge S12 | arrêt : le code des témoins diffère de v1 |
| Appel de modèle, réseau ou dépense | arrêt (devis et GO exigés) |
| Lecture d'un résultat ou exécution d'une méthode avant scellement ; paramètre modifié après lecture ; ouverture du fichier de validation avant le verdict | arrêt et consignation de l'écart (R1) |
| numpy < 1.25 | arrêt (R9) |
| Racine du manifeste différente de RACINE ou de RACINE_VALIDATION du § 7, ou monde de décision tiré avec RACINE_VALIDATION | arrêt (R9) ; V0 fausse |
| Marqueur de gel restant dans le texte, ou entrée « Contre-lecture k » sans ses deux empreintes | pas de scellement (**contrôlé** par le validateur `problemes`) |
| **Ligne de gel absente de `registres/decisions.md`, ou valeurs de la ligne différentes de celles du texte ; remarques de contre-lecture non traitées ; contre-lecture 4 ni faite ni déclarée superflue** | pas de scellement ; **contrôle manuel : le validateur ne vérifie ni la ligne de gel ni le traitement des remarques** (CB2-09) |
| Empreinte du code différente entre deux sessions d'un même run | arrêt |

**Gardes testées sur un cas sain et sur un artefact (R5)** avant les mondes de décision :
- **noyau non défini positif à travers le glouton** (CB-03) : `noyau_fautif` de la pièce A injecté dans `glouton_paires` doit lever `NonDefiniePositive` (et non rendre une sélection partielle) ; cas sain : noyau de la forme corrigée, sélection de 12 ; même essai sur la copie gardée de `ordre_glouton` ;
- **balayage statique** : un module de bras contenant `except NonDefiniePositive` est refusé ; cas sain : le module livré passe ;
- **bras qui lit la vérité** : un bras artefact qui demande `Latent` doit lever `AccesLatent` ; un bras artefact qui reçoit le jeton de mesure (score = indicatrice du vrai pont) doit enregistrer un gain proche du plafond **et** déclencher l'audit (précision ≥ 0,9 × oracle) ; cas sain : N s'exécute sans exception ;
- vecteur de concepts nul : κ = 0 compté et rapporté ; cas sain : monde jouet à la main à réponse connue ;
- abstention : un bras qui rend 8 paires est complété par 4 paires uniformes et `n_complete` = 4 ; cas sain : un bras qui rend 12 ;
- monde exclu : un monde construit avec 11 paires valides est exclu pour tous les bras ; cas sain : 12 paires valides ;
- échec de plantation : un paramétrage qui rend le pont (d) impossible provoque une régénération comptée, puis l'arrêt au-dessus du taux S11 ; cas sain : paramètres de décision ;
- monde jouet dont la précision des 12 paires est calculée à la main (vérification des estimateurs, du complément et des intervalles) ;
- reproduction de v1 : copies gardées de `ordre_glouton` identiques à la version de v1 sur 50 mondes.
- **extension de S9** (CB2-06, CB3-07) : σ̂ synthétique ≤ 15,3, n' = n (cas sain) ; σ̂ = 16, n' = ⌈n × (16 / 15,3)²⌉ = 2 625 (artefact : la formule joue dès 15,3) ; σ̂ = 20, n' = ⌈n × (20 / 15,3)²⌉ = 4 101 pour n = 2 400 ; σ̂ = 25, plafond de 4 800 atteint, rapporté, **sans arrêt** (artefact) ;
- **graine du monde inerte** (CB2-01) : latents de M_inertes d'indice m égaux à ceux de M_bien d'indice m, miroir différent (cas sain) ; code de condition 12 mis par erreur aux rôles 0 à 3 : latents différents, détecté (artefact) ;
- **garde de configuration S16e** : 18 paires et 15 concepts rares passent (cas sain) ; 19 paires de ponts, ou 7 / 4 / 4 / 4 ponts, sont refusés (artefact) ;
- **N_filtre** : monde jouet à réponse connue, paires aux fréquences ≤ φ au palier 1 prises d'abord (cas sain) ; monde où aucune paire ne passe le palier 1, passage déclaré aux paliers 2 puis 3 avec les nombres par palier rapportés (artefact : aucun repli silencieux) ;
- **jugeabilité J** : monde jouet où d1c bat c de façon connue, J vraie (cas sain) ; **artefact (CB3-06) : les 300 mondes de validation de `M_inertes`, où J doit être fausse** (les étiquettes y sont inertes ; J vraie y déclenche l'audit R4) ; en outre, dans V_concepts_absents, d1c non applicable et J non calculée, déclarées (aucune lecture silencieuse) ;
- **ordre du manifeste de S9** (CB3-07) : manifeste scellé avant le premier monde de décision, n' égal à la formule, nombre de mondes exécuté égal à n' (cas sain) ; run jouet où le manifeste est écrit après le premier fichier de résultats, où n' est modifié après lecture, ou où le nombre de mondes exécuté diffère de n' : le contrôle du lecteur refuse (artefact) ;
- **loi de M_fonds_1ou2 et option b_eloigne** : probabilités (0,6 ; 0,4) acceptées (cas sain), (0,6 ; 0,5) refusées (artefact) ; monde jouet où N bat b_eloigne : clause de A2 tenue (cas sain) ; monde jouet où b_eloigne bat N : clause fausse et ligne 9 bis, si S17 = option 1 (artefact).
<<<FIN PIÈCE 3>>>

### Pièce 4 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (l. 1–78) — nœuds N3, N4

Origine : branche de conv-audit ; empreinte du fichier source `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` ; 2637 mots ; règle 2 appliquée.

<<<DÉBUT PIÈCE 4>>>
# Préenregistrement — Pré-pilote d'étalonnage des instruments de la course 2 — brouillon 7

**Statut : brouillon 7, non scellé ; présentable à Lazar (vérification VB6 traitée) ; contre-lecture 5 après gel.** Les 11 constats de la vérification courte du brouillon 6 (VB6-01 à VB6-11 ; Sonnet 5.5 neuf, modèle différent de l'auteur, qui est un Fable 5.1 ; verdict « présentable après corrections mineures ») sont traités, chacun à un endroit nommé dans « Ce qui change » ; les 13 constats de la contre-lecture 4 (CP5-01 à CP5-13, Opus 5.5 neuf) et les 17 constats de la contre-lecture 3 restent traités. Rien n'est lancé, aucune dépense, aucun réseau. **Chaque décision de Lazar (43) porte le marqueur de remplissage du gabarit, une fois, dans la ligne qui recevra sa valeur (sections « Seuil » et « Rôles, témoins et dépendances ») ; les six valeurs ou faits à fournir au scellement, qui ne sont pas des décisions de Lazar (commit du code, empreinte de l'annexe, source et essai de S31, k, résumé du tableau, contre-lecture 5), portent un mot distinct en capitales, « à fournir au scellement » (VB6-10) ; aucune mention descriptive n'emploie l'un ni l'autre** (CP5-03). Le brouillon 6 (`c54a105b7c9a9fc39694e8a957003bbf5cc017af20c45bd6ca354d91be24493d`) et les brouillons 1 à 5 sont gardés sans modification (R12). [retiré, règle 2 : recommandation ou confiance d'auteur]

## Résumé pour Lazar (dix lignes)

1. Verdict : **issue la plus probable : nœud, pas de départ.** 40)** ; complément proposé 0,18 ; nœud d'emblée 0,67 ; **0,20 au total si le complément reçoit son GO** (0,22 au brouillon 5 : le brouillon 6 compte ce que la v5 ne comptait pas — une M6 réduite qui ne tient plus sous le plafond ferme C13 avec 0,08, et C12 reçoit ses causes de bras non produit, 0,97 au lieu de 0,99) ; **au défaut R-819 (aiguilleur non étalonné) : 0** (script v6 `b995fb48…`, mêmes graines que les v4 et v5 pour toute simulation reprise : seuls les changements déclarés bougent les chiffres). [retiré, règle 2 : recommandation ou confiance d'auteur]
2. Porte des juges seule (C1-C2) : 0,38 ; juges tous à 0,90 : 0,85 pour les juges, 0,35 pour la porte entière ; à 0,85 : 0,54 et 0,22 (sortie v6). Kimi est prédit exactement à S1 : son étalonnage reste un pile ou face (0,50).
3. Hors juges (produit 0,43) : ce qui ferme la porte : C5 (0,81), aiguilleur C7 (0,85), C10 (0,92 : la course tient à 4 sous-sessions avec 0,07, à 3 avec 0,36, à 2 avec 0,49 ; lecture « 110 − dépense »), **C13 (0,95 × 0,92 : une M6 réduite qui ne tient plus sous le plafond, 0,08, CP5-02)**, débordement C8 (0,92), C6 (0,93 sous sacrifice : la table seule retirée laisse l'axe 7 aux bardeaux seuls), C12 (0,97 : causes de bras non produit chiffrées, CP5-01). **Budget lu selon la règle d'A1, étape par étape, dans l'ordre du Plan (CP5-04), avec le plafond de relais lu comme une réservation et S17 comme seul plafond qui coupe (CP5-09)** : au plafond de 45 USD avec arrêt d'étape à 40, un sacrifice ou une réduction arrive avec 0,24 (fusions 0,13 ; M6 réduite 0,23 ; table seule 0,13 ; passe « tableau » 0,04), **M6 n'est jamais retirée entière** ; dépense médiane 36,3 USD, quantile 90 % 42,8 (44,2). **Sans arrêt d'étape** : C13 budget 0,90 au lieu de 0,92 (l'arrêt réduit M6 à temps), table seule retirée 0,07 au lieu de 0,13 (CP5-06). **Au plafond de 32 USD (information) : porte 0,11, nœud 0,77, 0,92 de sacrifices, C13 budget 0,66.** [retiré, règle 2 : recommandation ou confiance d'auteur]
4. **Ce que le pré-pilote éprouve réellement (CP4-01)** : l'obéissance des trois juges à leur grille sur témoins nets ; la détection d'une **redite entre fiches du lot** (mémoire, axe 7) ; la détection de **références inventées ou altérées** (M6) ; l'aiguillage des détails concrets ; la tenue de niveau méthode de Kimi ; les cloisons du tableau ; la chaîne de bisociation. **Il n'éprouve ni la détection d'une antériorité publiée non citée, ni « très plausible » au sens des tests de mort** : décision **D-g**. [retiré, règle 2 : recommandation ou confiance d'auteur]
5. **Bisociation** : trois bras, une paire chacun — bras méta v1, bras Gu-Krenn (modèle ou **substitut inspiré de Gu et Krenn**), bras basique. **Les paramètres du bras méta (S28, S29 a à f) vivent dans une annexe séparée, écrite après les verdicts des collisionneurs, contre-lue par un modèle différent, scellée et empreintée dans ce préenregistrement avant son gel, et leurs valeurs sont approuvées par Lazar sur proposition de l'annexe** (CP4-02, CP5-07) : décision **D-h**. **Les paramètres du substitut de Gu et Krenn sortent de l'annexe et deviennent le seuil S31 de ce préenregistrement** (CP5-01) : une annexe non conforme à É0 ne fait plus tomber que le bras méta (C12 0,97 ; « non lancé », déclaré, pas un nœud). [retiré, règle 2 : recommandation ou confiance d'auteur]
6. **Plan des fonds (CP4-03)** : décision **D-i** entre (1) 28 fonds uniques (texte actuel), (2) 28 fonds + 4 rendus appariés pour la seule mémoire anti-redite, (3) 24 fonds dont 4 doublés (−0,2 USD, 8 fiches corrélées). **Gu-Krenn sans condition de reproduction** : décision **D-j**. [retiré, règle 2 : recommandation ou confiance d'auteur]
7. Coût : attendu aux bases ≈ 28,4 USD (texte de base) ; D-i (2) 0,5) ; **S17 = plafond 45 USD, arrêt d'étape 40 USD — à geler par Lazar, un seul couple au gel (marqueur en « Seuil »)** ; sans ligne de GO à ce plafond, A15 arrête : **aucun repli à 32** (CP4-07). Complément conditionnel : ≈ 11,6 USD attendus, plafond 17,5 (CP4-10). Devis v4 attendu (n° 266, n° 268) : bases du devis v3, SUPPOSÉ. [retiré, règle 2 : recommandation ou confiance d'auteur]
8. Liste fermée des options du nœud : O0 à O14 inchangées, **O15 ajoutée** (bras non produit, hors porte, CP4-05) ; relâchements R-1 à R-3 inchangés.
9. Inchangé : témoins non ambigus ; aiguilleur avant les juges ; tableau minimal éprouvé ; quatre instances distinctes au bras d'attaque ; arrêt clos ; adjudication de M5 ; notation croisée gardée ; aucune mesure de performance de l'organisme (restes d'A7 et de M9 retirés, CP4-14).
10. À faire : annexe du bras méta (après collisionneur ; valeurs approuvées par Lazar) ; décisions D-g à D-j, D-e, D-f, S1 à S31, lectures L1 à L7 ; mot sur l'étalonnage de l'aiguilleur ; confidentialité ; ligne de GO au plafond gelé ; PDF de Gu et Krenn versé (R7) ; essai de S31 sur la moisson ; vérification courte des corrections (contre-lecture 5) ; scellement ; GO de lancement.

### Seuils et décisions à geler par Lazar [retiré, règle 2 : recommandation ou confiance d'auteur]

| N° | Objet |
|---|---|
| S1 | Exactitude équilibrée minimale de chaque juge (P contre N, témoins non ambigus) |
| S2 | Rappel minimal de chaque juge sur P |
| S3 | Plancher d'échec d'un juge |
| S4 | Accord (Fleiss ; chaque couple ; plancher d'échec) |
| S5 | Alarme de biais résiduel de source (M2) |
| S6 | Fidélité du rendu (ancres ; couples de défaut ; défaut vu par le relecteur) |
| S7 | Fausses alertes de la mémoire anti-redite (visée ; tolérée) |
| S8 | Rappel global de la mémoire sur la vérification |
| S9 | Double garde de l'axe 7, union (rappel ; fausses alertes) |
| S10 | Aiguilleur : rappel minimal sur les concrets écrits ; bande « à corriger » |
| S11 | Aiguilleur : fausses alertes sur 34 fiches de niveau méthode ; sur les 6 difficiles |
| S12 | Débordement de Kimi proposeur (20 fiches au plus) |
| S13 / S14 / S15 | Antériorité : rappel inventées ; rappel altérées ; fausses alertes réelles |
| S16 | Écart toléré coût mesuré ÷ coût supposé |
| S17 | **Plafond ; arrêt d'étape — un seul plafond** |
| S18 | Indiscernabilité témoins / fiches de Kimi (aire) ; effectif minimal de fiches de Kimi |
| S19 | Indiscernabilité P / N par la forme (aire) |
| S20 | Témoins ambigus tolérés ; effectifs primaires minimaux |
| S21 | Tableau minimal : longueur maximale d'un titre ; d'un résumé |
| (S22) | Bisociation, course : k paires par bras et par case — hors gel |
| S23 | Bisociation, pré-pilote : k paires par bras |
| S24 | Accord minimal des lecteurs d'étiquettes de concept (Jaccard moyen) — bras basique |
| S25 | Règle Gu-Krenn (modèle) : nombre m de meilleures paires de concepts |
| S26 | Reproduction de Gu-Krenn |
| S27 | Règle Gu-Krenn : couverture minimale (réserve, non retrait) |
| S28 | Accord minimal des lecteurs de niches et structures (bras méta) |
| S29 | Paramètres du bras méta v1 (a à f) |
| **S31** | **Paramètres du substitut inspiré de Gu et Krenn (ex-S29 g ; CP5-01)** |
| S30 | Si D-g (b) : rappel minimal de M6b (antériorité non citée, 4 fiches) — réserve, hors porte |
| D-e | Lecture de « domaine » et de « concept » (bras basique) |
| D-f | Modèles des rôles neufs : tiers metteur en forme T ; relecteur |
| D-g | Antériorité non citée : (a) vide déclaré ; (b) 4 fiches ajoutées à M6 (M6b, étape protégée hors porte É9b) |
| D-h | Gel : (a) attendre l'annexe du bras méta ; (b) geler à deux bras |
| D-i | Plan des fonds : (1) 28 uniques ; (2) 28 + 4 rendus appariés (mémoire seule) ; (3) 24 dont 4 doublés |
| D-j | Gu-Krenn sans condition de reproduction : oui / non |
| L1 à L7 | Lectures à confirmer qui fixent une règle (passe « tableau » ; table seule ; désaccord hors score ; total 110 ou 123 ; fusions sacrifiées et C12 ; S27 réserve ; brouillon 3 sans contre-lecture) |

- Auteur : sous-agent Fable 5.1 neuf de la lignée conv-audit, 31 octobre 2026, pour Lazar. Réserve d'indépendance (CP1-14) : la session conv-audit est concepteur des moniteurs (R-824) et Opus 5.5 est troisième juge. [retiré, règle 2 : recommandation ou confiance d'auteur]
- Date (UTC) : 2026-10-31 ; le script v6 et sa sortie ont été écrits et joués avant le texte, sans lecture d'aucune donnée de run ; rejeu `python3 -I` dans un dossier vide : sortie identique octet pour octet (même empreinte).
- Commit du code d'analyse : À FOURNIR AU SCELLEMENT (valeur, non une décision de Lazar ; aucun code d'analyse n'existe encore) ; seront nommés : commit du code, nom, version et empreinte des poids du plongement figé (M3), empreintes de la consigne figée de chaque juge et de son nombre d'items k, de l'analyseur programmé (étage 1), du programme de bardeaux de mots, de la consigne de l'aiguilleur, de la consigne de rendu, du constructeur de tableau minimal et de ses gardes, du programme de score de paire du bras basique, de la liste fermée des concepts, du vocabulaire du bras Gu-Krenn, du programme de note Gu-Krenn (modèle ou substitut, lequel déclaré), **de l'annexe scellée du bras méta (grille, S28, S29 a à f, programme de score ; CP4-02)**, de la source gelée de S31 et de son essai sur la moisson (CP5-01), et, si D-g (b), des 4 fiches de M6b, de leurs PDF sources et de la liste scellée des sources (DEP2c).
- Documents qui font foi (chemin + empreinte) :
  - brouillons 1 à 5 de ce préenregistrement, gardés (R12) : `…brouillon1.md` `8d6142eb3be04c1f732f3a148e35d791239fed417897ed82ad0eb49155fdcfdd` ; `…brouillon2.md` `8afb556f5f96e69bdb7ff57cf19ff053c581f71d08274e0e6fc44fd0fd7eb8f9` ; `…brouillon3.md` `dcf937e7ce8e2de3f7aa712416e44400cd386223ab94cb65e78e3bfddf6fd85d` ; `…brouillon4.md` `13d1c031ebc9ac90b192911a9a87577880094bbfe6c4e2bd62be990c47c09719` ; `…brouillon5.md` `96080471abf69c1166a99c993c17c9408dd016a43f916e0ae8a2af63cd5475b3` ; **`preenregistrement-pre-pilote-course-2-brouillon6.md` `c54a105b7c9a9fc39694e8a957003bbf5cc017af20c45bd6ca354d91be24493d` (base de travail de ce brouillon)** ;
  - contre-lectures : 1 `contre-lecture-pre-pilote-course-2-brouillon1.md` `96cf300bed14064a9e4a45d2d2d63474e20bd3e68f26c43df742c059d570c62c` ; 2 `…brouillon2.md` `e5added0e0a589dd0521822a6b2dcbf4cd6a58999b7c69ca87613814e15e7d03` ; 3 `contre-lecture-pre-pilote-course-2-brouillon4.md` `12f3d792e59504dedd462d84025ffeac77e3ef9404e69159d3bfe28a8893da04` (Sonnet 5.5 neuf) ; **4 `contre-lecture-pre-pilote-course-2-brouillon5.md` `226696122aa63fac77865854cee33a0f314cef166ded83302bd2ad3191b381d2` (Opus 5.5 neuf, 2026-10-31 00:19 UTC ; compagnon `.sha256` conforme)** ; **vérification courte des corrections du brouillon 6 : `verification-corrections-brouillon6-v1.md` `27b8e07550a07db1dd2ed7bddcc2b2ab32b143391e61fb693afb466048fc481d` (Sonnet 5.5 neuf, 2026-10-31 00:51 UTC ; `sha256sum` à la lecture, compagnon `.sha256` à écrire par conv-audit)** ;
  - texte I de la course 2, fusion v5 : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v5.md`, `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` (l. 46 : notation, « ni décisif ni inédit n'est noté » ; annexe 3 : étalonnage préalable, critère de mort) — repris du brouillon 4, non relu ;
  - décisions R-552 à R-663 (conv-audit) : `registres/decisions.md` de ce dépôt (contenu vivant ; lignes R-630 à R-643, R-651, R-654, R-662 et R-663 lues telles quelles le 31 octobre) ;
  - décisions R-811, R-818 à R-827 (session-depot) : `registres/decisions.md` de `origin/main`, `afc0a8ee4c26e9921fb36193ee72a88f7a16de2ca730325c432dc5096a7fba2e` à la lecture du 30 octobre (reprise du brouillon 1, non relue depuis) ;
  - devis de la course 2, trois juges, v3 (`74a3f73110ac9b55fa9209ebafdd815597732bbb6b1e97c3da69d47244e4f710`), devis Kimi juges v2 (`88e0325a9848734baf41be633b40ec2afacda3397e76c07122d0d31b2f06a7b2`), dossier de service v1 (`bd88b087ba85a4227d4777ea5e6aa9622867ba8497c6d91bae33ac0eedf5b0ab`) : sur `origin/main` seulement (vérifiés par la contre-lecture 1, non relus ici) ; **devis v4 demandé (n° 266, n° 268), non rendu : les bases du devis v3 restent SUPPOSÉ** ;
  - GO-2026-10-30-07 (110 USD séquencé, pré-pilote ≤ 32 USD, course ≤ 78 USD restants, « sinon réduite à 2 ou 3 sous-sessions ») : `registres/go.md` de `origin/main`, ligne 152, `093fd8cfe4e3e39adee63a0b5d94997486d80bb983f577636140415e0e8a538e` à la lecture du 30 octobre (le `registres/go.md` de l'arbre de travail ne porte pas cette ligne, vérifié par la contre-lecture 3) ; **aucune ligne au plafond de 45 n'existe** : S17 reste à geler et A15 arrête sans elle ;
  - préenregistrement scellé de bisociation v2 (forme du score du bras basique) : `prereg/preenregistrement-bisociation-deux-espaces-v2.md`, `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` ;
  - gabarit et validateur : `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (le validateur refuse le marqueur de remplissage du gabarit partout dans le fichier, dans les sections exigées comme hors d'elles, fonction `problemes` ; c'est le marqueur que porte chaque décision ouverte, et lui seul : table des marqueurs dans « Seuil », CP5-03) ;
  - calcul de puissance de ce brouillon : **`calcul-puissance-pre-pilote-course-2-v6.py` `b995fb48da87ecaa56f3e4464a824a8b58196a3e23ce574986e0190ebbcaef51` et sa sortie `calcul-puissance-pre-pilote-course-2-v6.sortie.txt` `7394ddae54e20aa527c615ff762719ed0a27ec591e08fbd93774536959d6ece3`** (joué par `python3 -I`, python 3.13.18, numpy 2.5.3, scipy 1.18.1) ; v5 (`96ee5852…` / `d342b569…`), v4 (`2a219616…` / `28e0600d…`), v3 (`786a017f…` / `72fd43a5…`) et v2 (`92c0e60d…` / `1c0e702d…`) gardés ; la v2 reste la source des erreurs-types des aires ; **toute simulation gardée des v4 et v5 garde son nom de tâche de graine (`v4-…`, `v5-…`) : ses tirages sont identiques, et les écarts de chiffres entre v5 et v6 viennent des seuls changements déclarés ; les simulations nouvelles portent des noms `v6-…` (M5 sur 10 fiches) et leur bruit de simulation est de l'ordre de ±0,01** (CP4-11) ;
  - Gu, X. et Krenn, M. 2024, « Forecasting high-impact research topics via machine learning on evolving knowledge graphs », arXiv 2402.08640 : **aucun PDF versé** (relecture Fable de la page arXiv : `bisociation-niches-v1/relecture-fable-reponse-3-v1.md`, `556bc9d5f7eb12ef12b4ba2b284eb2ef5fd52acac815a0b0ff26489264e04129`) : aucun chiffre opposable (R7) ; les traits qui fondent le substitut sont ceux que R-635 nomme, à relire sur le PDF empreinté avant le gel ; d'où le nom **« substitut inspiré de Gu et Krenn »** dans tout registre (CP4-09) ;
  - brief de la lignée « bisociateur » : `brouillons/canal-reprise-releve-v1/envois/brief-nouvelle-lignee-bisociateur-v1.md`, `2cdf135fff340960a3499e44977557d5ae49e121d142dca48ec39a1ba01321b1` ;
  - cloche d'Uzzi (Uzzi, Mukherjee, Stringer et Jones 2013, Science 342) : aucun PDF versé, aucun chiffre repris (R7) ;
  - **annexe du bras méta (à écrire)** : `annexe-bras-meta-v1.md`, même dossier, empreinte : À FOURNIR AU SCELLEMENT (CP4-02) ; **source gelée de S31 (substitut inspiré de Gu et Krenn)** : chemin et empreinte de la moisson (ou du graphe publié) et de l'essai de S31 sur elle : À FOURNIR AU SCELLEMENT (CP5-01) ;
  - chiffres de la course 1 repris (R-811, R-820, R-827) tels que consignés, non relus sur les données.
<<<FIN PIÈCE 4>>>

### Pièce 5 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (l. 283–283 ; 296–296) — nœuds N3 (S31)

Origine : branche de conv-audit ; empreinte du fichier source `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` ; 98 mots ; l. 296 (S31) ajoutée par la liste v2 ; règle 2 appliquée.

<<<DÉBUT PIÈCE 5>>>
- **S17** — À REMPLIR — à geler par Lazar : **un seul plafond et un seul arrêt d'étape (ou « sans arrêt »), écrits ici au gel, couverts par une ligne de GO à ce plafond avant tout lancement (A15) ; aucun repli** (CP4-07). [retiré, règle 2 : recommandation ou confiance d'auteur]
[…]
- **S31** — À REMPLIR — à geler par Lazar. **Paramètres du substitut inspiré de Gu et Krenn** (joués seulement si le modèle de Gu et Krenn ne tourne pas à É0, A19 ; croyance 0,7). [retiré, règle 2 : recommandation ou confiance d'auteur]
<<<FIN PIÈCE 5>>>

### Pièce 6 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (l. 336–356) — nœuds N5

Origine : branche de conv-audit ; empreinte du fichier source `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` ; 1102 mots ; fin portée de 360 à 356 : les l. 357 à 360 sont le titre et l'en-tête d'une table hors pièce ; règle 2 étendue (configuration recommandée) ; règle 2 appliquée.

<<<DÉBUT PIÈCE 6>>>
**Ordre des étapes (par dépendance ; jamais par résultat ; révisé au brouillon 5, CP4-15 : les juges sur les 28 rendus passent avant les étapes sacrifiables ; c'est cet ordre, et lui seul, que le script v6 joue — CP5-04 ; l'ordre joué par le script v5 et celui du brouillon 4 sont rejoués en comparaison, sortie v6).** **Règle de lecture (CP5-08) : aucun verdict d'É6 ni d'É7 n'est lu par quiconque, et la clé des classes et la clé des bras ne sont pas ouvertes, avant la fin d'É9 ; seules les consommations (M7 : jetons, durée, coût, modèle servi) sont lues en route, parce que la règle d'A1 en a besoin ; les décisions de sacrifice, de reprise et d'arrêt ne dépendent que des consommations et des gardes (A21 ; garde R5 ligne 30).**
- É0 (sans dépense) : gardes éprouvées sur cas sain et artefact (table R5) ; consigne de l'aiguilleur empreintée **avant** l'écriture des 12 concrets ; consignes, code, liste fermée des concepts empreintés ; **annexe du bras méta : présente, scellée, contre-lue, empreinte égale à celle écrite ici, gardes 22a, 22b, 23, 24 passées — sinon A20, décidé ici et jamais plus tard** ; moissonneur ; **bras Gu-Krenn : « modèle » ou « substitut inspiré » déclaré et écrit au manifeste avant toute dépense (A19)** ; vocabulaire et programme de note empreintés.
- É1 : rédacteur — 28 squelettes et déclarations scellées ; 8 fiches d'antériorité (et 4 fiches M6b si D-g (b)) ; 6 difficiles ; 8 voisines ; 24 éléments de l'axe 7. Ancres contrôlées par programme.
- É2 : Kimi, passe 1.
- É3 : rendus — chaque fond une fois (plus 4 rendus appariés sous D-i (2)) ; fidélité (S6) ; longueur (A8).
- É4 : **aiguilleur** sur les rendus, la passe 1, les 6 difficiles, les 12 concrets ; second lecteur sur la passe 1. Rendus aiguillés : exclus des juges, comptés.
- É5 (avant tout juge) : relecteur → témoins ambigus, S20, A6 ; contrôles S18 et S19 → A7 ; seconde version de témoins s'il y a lieu (É5bis).
- **É6 : trois juges sur les 28 rendus non aiguillés (M1), un appel par fiche, anonyme.**
- É7, dans cet ordre : **É7a** tableau minimal (garde des cloisons, programme) ; Kimi, passe « tableau » ; aiguilleur et second lecteur sur elle ; adjudicateur de M5 sur les fiches en désaccord des deux passes réunies ; **É7b** lecteurs d'étiquettes sur la passe 1 ; accords S24, S28 ; couverture S27 ; paires méta, Gu-Krenn, basique (programmes, 0 USD) ; **É7c** fusions par Kimi (ordre `pp2-bisoc-ordre`) ; aiguilleur puis trois juges sur les fusions non aiguillées (appels isolés, anonymes, même version de modèle qu'en É6) ; **É7d** Opus sur les 24 éléments de l'axe 7 (table seule).
- É8 : paraphrases des rendus par le rédacteur (après É4) ; mémoire et bardeaux sur processeur (M3, M8).
- É9 : vérification d'antériorité (M6, 8 fiches ; réduite : 4).
- **É9b (si D-g (b))** : vérification sur les 4 fiches de M6b, étape protégée hors porte (CP5-05).
- M7 est relevée à chaque étape. Aucune étape de brainstorm n'est ajoutée (option A, R-637, R-640).

**Sacrifice à plafond atteint — règle d'A1 (CP4-15, CP5-02, CP5-04, CP5-09 ; écrite une seule fois ici ; le script v6, fonction `simuler_budget`, la joue mot pour mot, dans l'ordre des étapes ci-dessus).** Avant chaque étape E non retirée :
1. **Projection** = cumul + plafond de relais de E + attendu aux bases des étapes restantes non retirées ; **tant que la projection dépasse le plafond S17**, on prend la prochaine mesure de la liste de sacrifice non encore jouée, dans l'ordre : (1) fusions de bisociation retirées (M9 réduite aux étiquettes, accords et paires, qui sont protégés ; lecture L5) ; (2) **M6 réduite** à 4 fiches (tâche `pp2-reduction-e9`) ; (3) table seule de l'axe 7 retirée (bardeaux seuls) ; (4) passe « tableau » de Kimi retirée (M8 réduite aux gardes sans dépense).
2. **Arrêt d'étape** (si S17 en a un) — si le cumul atteint l'arrêt d'étape : les étapes retirables non jouées (fusions, table seule, passe « tableau ») sont retirées et M6 non jouée est réduite ; rien de protégé ne change.
3. **Plafond** — si cumul + plafond de relais de E dépasse S17 : E retirable est retirée ; E = M6 non encore réduite est réduite puis réexaminée ; E = M6 réduite, ou E protégée, **n'est pas lancée** : « non mesuré (budget) », C13 non satisfaite (nœud ; O12) ; E = M6b (protégée hors porte) n'est pas lancée : réserve, C13 inchangée.
4. Sinon E est jouée. **Le plafond de relais est une réservation** : il sert aux tests 1 à 3 ; le coût réel de E est compté en entier au cumul ; **S17 est le seul plafond qui coupe** : si le cumul franchit S17 pendant E, le relais coupe E à S17 — E protégée est « non mesurée (budget) » (C13), E retirable est retirée. Un relais au-delà de sa réservation sans franchir S17 est une réserve de M7 (ratio > S16 : poste refait), pas une coupure (CP5-09 ; au moins un relais au-delà de sa réservation dans 0,84 des tirages, parce que les réservations du tableau, ×1,3 à ×1,6 des bases, sont sous les bornes hautes de P11 ; DEP4 : le relais doit accepter une réservation dépassée jusqu'à S17 − cumul, SUPPOSÉ).

**M6 n'est jamais retirée entière** (CP5-02) : elle est réduite une fois (par la projection, par l'arrêt d'étape ou par le plafond), réduite elle est protégée, et si elle ne tient pas sous S17 elle est « non mesurée (budget) » et C13 n'est pas satisfaite. **Jamais sacrifiés ni réduits** : rédacteur, Kimi passe 1, rendus, aiguilleur et second lecteur, relecteur, juges sur les 28 rendus, lectures d'étiquettes, paires (programmes), paraphrases, M6b. La seconde version de témoins (A6, A7 ; ≈ 4,9 USD attendus) est protégée et passe par la même règle. Les reprises (A3, A5, A8) sont comprises dans les réservations. Modèle grossier : rapports log-normaux indépendants ; la lecture « chaque relais coupe à son propre plafond » est rejouée pour information (sortie v6 : elle couperait une étape protégée avec 0,80 — Kimi passe 1 0,38, aiguilleur 0,29 — et ferait tomber les sacrifices à 0,05 en cachant ces coupures ; elle n'est pas retenue) ; le modèle « total > plafond » de la v4 est gardé en rappel (0,16 à 45). [retiré, règle 2 : recommandation ou confiance d'auteur]
<<<FIN PIÈCE 6>>>

### Pièce 7 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (l. 543–587) — nœuds N5

Origine : branche de conv-audit ; empreinte du fichier source `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` ; 1883 mots ; fin portée de 585 à 587 : lignes 31 et 32 de la table R5 annoncées par la liste.

<<<DÉBUT PIÈCE 7>>>
| A15 | décision manquante : confidentialité (fiches vers Moonshot et Google), D-f, **ligne de GO au plafond gelé S17** (aucun lancement à un autre plafond), D-g à D-j, ou GO de lancement ; **ou confirmation de DEP4 par session-depot absente** (le relais accepte une réservation dépassée jusqu'à S17 − cumul et coupe à S17 seulement ; sinon la lecture « relais dur » s'applique — étape protégée coupée avec 0,80, sortie v6 — et le Plan est à réécrire dans une version nouvelle, R12 ; VB6-04) | **aucun lancement** |
| A16 | version du texte I, d'une consigne figée, de l'analyseur, du constructeur de tableau, de la grille des niches, de l'annexe du bras méta ou de ses paramètres différente de celle empreintée | arrêt ; nouvelle version du préenregistrement (R12) |
| A17 | une fiche non passée par l'aiguilleur atteint un juge, le tableau ou un lecteur d'étiquettes | arrêt ; notations annulées ; incident (R-819) |
| A18 | entrée du tableau hors de sa case, titre d'une fiche aiguillée, ou entrée au-delà de S21 | arrêt de la passe « tableau » ; tableau reconstruit ; incident |
| A19 (LECTURE À CONFIRMER, D-j, marqueur en « Seuil » ; CP5-12) | modèle de Gu-Krenn absent, non empreinté ou ne tournant pas à É0 | **bascule vers le substitut inspiré de Gu et Krenn (S31)**, déclarée au manifeste à É0 ; bras gardé, compté « substitut » ; **aucun retrait** ; si la source de S31 n'est pas disponible et empreintée à É0 : bras « non produit (source absente) », déclaré à É0, compté, O15 — indépendant de l'annexe du bras méta (CP5-01) |
| A20 | **à É0** : annexe du bras méta absente, non scellée, non contre-lue, non approuvée par Lazar (S28, S29), à empreinte différente de celle écrite ici, ou garde 22b, 23 ou 24 échouée ; sous D-h (b), sans objet (aucune annexe, bras méta hors du pré-pilote) | **bras méta « non produit (annexe non conforme) », décidé à É0, écrit au manifeste ; aucune valeur choisie en route, aucun gel après É0, aucune fenêtre jusqu'à É7** ; les deux autres bras inchangés (S31 ne dépend pas de l'annexe) ; réserve jointe au verdict (pas un nœud) ; O15 (CP4-02, CP5-01) |
| A21 | lecture d'un verdict d'É6 ou d'É7, ou ouverture de la clé des classes ou de la clé des bras, avant la fin d'É9, par quiconque (CP5-08) | incident consigné ; les décisions de sacrifice, de reprise et d'arrêt prises après la lecture sont annulées et rejouées sur les seules consommations ; si une décision ne peut pas être rejouée : mesure concernée « non mesurée (technique) », nœud |

**Table R5 — garde → cas sain → artefact (CP1-19).** Chaque essai est un script empreinté au gel, joué en É0 (22a avant le gel de l'annexe) ; une garde qui échoue arrête sa mesure (A12). Les lignes 22a, 22b, 24 à 29 sont ajoutées ou scindées par le brouillon 5 ; les lignes 30 à 32 par le brouillon 6 (CP5-08, CP5-13).

| N° | Garde | Cas sain (doit passer) | Artefact (doit être arrêté) |
|---|---|---|---|
| 1 | Modèle servi (A2) | réponse du relais au nom du modèle permis | faux amont qui renvoie un autre nom de modèle |
| 2 | Étiquettes (A4) | entrée anonyme | entrée contenant « témoin », une lettre de classe, « exploratoire », « fusion » ou un nom de bras |
| 3 | Longueur (A8) | rendu de 5 000 caractères | rendu de 2 900 et de 8 100 caractères |
| 4 | Empreinte d'un témoin (A13) | témoin scellé intact | témoin modifié d'un caractère |
| 5 | Contrôleur d'ancres (S6) | rendu fidèle | rendu avec un chiffre changé ; rendu sans l'une des deux chaînes d'un couple de défaut |
| 6 | Étage 1 | une P | une G (chiffre d'HELIOS à une mauvaise page) |
| 7 | Mémoire anti-redite | paire NA (sous le t* provisoire d'essai, fixé à 0,90) | fiche comparée à elle-même (similarité 1, signalée) |
| 8 | Bardeaux de l'axe 7 | angle distinct | copie mot pour mot de l'une des huit questions |
| 9 | Garde de forme (M5) | fiche de niveau méthode | 6 coquilles par gabarit programmé |
| 10 | Aiguilleur, second lecteur et adjudicateur (A12) | fiche ordinaire de niveau méthode | essai propre au bras d'attaque, décrit par classe seulement ; auto-rapporté |
| 11 | Dépense (A1) | étape dont la projection et cumul + réservation tiennent sous le plafond S17 gelé ; M6 non réduite dont la projection dépasse : réduite, puis lancée | étape simulée dont la projection dépasse S17 (retirable : retirée ; protégée : non lancée) ; M6 réduite qui ne tient pas : « non mesurée (budget) », jamais retirée entière ; étape simulée dont le coût franchit S17 en route : coupée à S17 ; **ligne de GO absente au plafond S17 : aucun lancement (A15)** |
| 12 | Passage par l'aiguilleur (A17) | fiche marquée « aiguillée : non » | fiche sans marque présentée à un juge |
| 13 | Cloisons du tableau (A18) | tableau de la case construit sur ses propres titres | entrée synthétique étiquetée d'une autre case ; **la garde vérifie l'étiquette de case, pas la provenance** |
| 14 | Fiche entière dans le tableau (A18) | entrée de 1 titre et 1 ligne sous S21 | entrée de 3 000 caractères |
| 15 | Titre d'une fiche aiguillée (A18) | titres de fiches non aiguillées | titre d'une fiche « aiguillée : oui » (synthétique) |
| 16 | Paire de bisociation bien formée, pour chaque bras | deux fiches distinctes, même case, non aiguillées, score recalculé égal ; paires des bras distinctes ; priorité appliquée ; **n = 2 : une seule paire au bras de priorité 1** | paire traversant une case ; paire avec une fiche aiguillée ; paire d'une fiche avec elle-même ; deux bras sur la même paire ; **trois paires revendiquées à n = 2** |
| 17 | Moissonneur | référence réelle (PDF empreinté) trouvée | référence inventée, « non trouvée » |
| 18 | Lecteurs d'étiquettes | étiquette de la liste ; concept du vocabulaire | étiquette hors liste, terme hors vocabulaire : rejetés |
| 19 | Relecteur | rendu fidèle d'une N : défaut vu, item et champs justes | rendu où un programme a retiré une chaîne du couple de défaut : « défaut absent » attendu |
| 20 | Note Gu-Krenn (modèle ou substitut inspiré, S31) | modèle : probabilités reproduites à 10⁻⁶ près sur un jeu d'essai ; substitut : paire « jamais reliée, deux concepts actifs » notée 1, paire « déjà reliée » notée 0, sur un extrait de la source gelée en S31 | concept hors vocabulaire : refusé ; fiche à moins de 2 concepts : non notée ; note « modèle » revendiquée alors que la déclaration dit « substitut » : arrêt ; source à empreinte différente de celle écrite en tête : bras « non produit (source absente) » |
| 21 | Bascule Gu-Krenn (A19) | déclaration « modèle » ou « substitut » écrite au manifeste à É0, avec l'empreinte de la source de S31 | déclaration absente à É0 : arrêt ; changée après É0 : arrêt |
| 22a | Bras méta, code (**avant le gel de l'annexe**, CP4-06, CP5-07) | jeu d'essai synthétique de 10 fiches étiquetées à la main : au moins une paire satisfait les trois indicateurs, au moins une ne les satisfait pas ; argmax recalculé égal ; **prédiction P14 refaite avec les paramètres réels de l'annexe (script rejoué, sortie nommée dans l'annexe)** | profil vide sur le jeu d'essai (bande de e et seuil de c qui ne se recoupent pas) : annexe non scellée ; paire de deux fiches de même niche : refusée ; paire du profil non choisie alors qu'une « hors profil » l'est : arrêt ; P14 non refaite : annexe non scellée |
| 22b | Bras méta, intégrité (É0, A20) | annexe scellée, contre-lue, empreinte égale à celle du préenregistrement ; paramètres lus égaux | annexe absente, non contre-lue ou à empreinte différente : bras non produit (A20) |
| 23 | Lecteurs de niches et structures | niche de la grille, une par fiche ; structures de la grille | niche hors grille, deux niches pour une fiche, structure hors grille : rejetées ; **lot à marges constantes : marqué « dégénéré » (S28)** |
| 24 | **Désaccord hors score (R-638)** | jeu d'essai : la même paire avec d = oui et d = non reçoit le même score méta | programme où d entre dans le score (scores différents) : arrêt |
| 25 | **Appel coupé (A3)** | appel qui répond sous le délai | faux amont muet au-delà de 300 s (1 800 s pour Kimi) : échec compté ; troisième échec consécutif simulé : arrêt du rôle |
| 26 | **Ambigus et effectifs (A6, S20)** | 23 primaires synthétiques dont 2 ambigus (P 9, N 12) : passe | 5 ambigus synthétiques, ou P 7 : arrêt avant les juges |
| 27 | **Calculs de S18 et S19 (A7)** | jeu synthétique où témoins et fiches sont tirés de la même loi des trois indices : aire ≈ 0,5, sous S18 ; classes P et N indiscernables : sous S19 | classe lisible par la longueur seule (P à 6 500, N à 3 500 caractères) : aire ≈ 1, S19 dépassée, arrêt |
| 28 | **Sorties inexploitables (A14)** | rôle avec 10 % d'appels sans sortie : continue | 30 % d'appels vides synthétiques : « non mesuré (technique) » |
| 29 | **Versions empreintées (A16)** | empreintes de toutes les pièces listées au gel recalculées égales | consigne figée, grille ou annexe modifiée d'un caractère : arrêt (étend la ligne 4 au-delà du témoin) |
| 30 | **Aveugle de l'orchestrateur (A21, CP5-08)** | journal d'accès : jusqu'à la fin d'É9, seules les consommations (M7) sont lues ; les verdicts et les clés restent scellés ; les décisions de sacrifice rejouées sur les seules consommations donnent le même résultat | lecture simulée d'un verdict d'É6 avant É9 (fichier de verdict ouvert par l'orchestrateur d'essai) : incident ; décision de sacrifice d'essai qui dépend d'un verdict : arrêt |
| 31 | **M6b : source hors de l'entrée (si D-g (b), CP5-13)** | entrée du vérificateur sans la source de l'idée ni dans le texte ni dans les cinq antériorités (vérification par programme sur le titre, les auteurs et l'identifiant de la source) | entrée synthétique qui contient le titre de la source parmi les antériorités : arrêt de la fiche |
| 32 | **Refus ou limite d'Opus (A11, CP5-13)** | appel qui répond | faux amont qui renvoie un refus, puis une limite hebdomadaire : refus compté, attente ; bascule simulée vers un autre modèle : arrêt |
<<<FIN PIÈCE 7>>>

### Pièce 8 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (l. 619–619) — nœuds N5 (DEP4)

Origine : branche de conv-audit ; empreinte du fichier source `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` ; 106 mots.

<<<DÉBUT PIÈCE 8>>>
- DEP4 : relais Kimi v3 (1 800 s), adaptateur Kimi (v53, conv-audit), relais d'Argon avec lecture du modèle servi, relais d'Opus et de T ; **le relais accepte, pour chaque étape, une réservation dépassée jusqu'à S17 − cumul, et coupe à S17 seulement** (règle d'A1, CP5-09 ; SUPPOSÉ, à confirmer par session-depot ; sinon la lecture « relais dur » de la sortie v6 s'applique — étape protégée coupée avec 0,80 — et le Plan est à réécrire ; **A15 : aucun lancement sans cette confirmation**, VB6-04) ; **confidentialité** : mot de Lazar pour l'envoi de fiches (inventées) chez Moonshot et Google : À REMPLIR.
<<<FIN PIÈCE 8>>>

### Pièce 9 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (l. 639–704) — nœuds N3

Origine : branche de conv-audit ; empreinte du fichier source `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` ; 2725 mots ; règle 2 appliquée.

<<<DÉBUT PIÈCE 9>>>
## Décisions à Lazar

Format : décision en une phrase ; enjeu ; options (avantage, inconvénient) ; [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-g — Antériorité non citée.** *Décision* : accepter que le pré-pilote n'éprouve pas la détection d'une antériorité publiée non citée, ou ajouter 4 fiches à M6 (M6b). *Enjeu* : « inédit » (R-632) n'est éprouvé par aucun instrument du pré-pilote (CP4-01) ; la course s'en remet à la vérification sur PDF après coup et aux tests de mort ; M6b en donne une lecture grossière avant la course. *Options* : (a) vide déclaré — avantage : rien à écrire ni à payer, pas de changement de la consigne du vérificateur ; inconvénient : si le vérificateur ne sait pas nommer une antériorité manquante, on l'apprend après la course. (b) M6b, 4 fiches, rappel S30 = 3 sur 4 en réserve hors porte, **étape protégée hors porte É9b** (CP5-05) — avantage : ≈ 1,6 USD, plafond 2,5, premier signal sur le vrai sens d'« inédit » ; inconvénients : 4 cas ne bornent rien (4 sur 4 → 0,47 ; « 3 sur 4 au moins » à rappel vrai 0,60 : 0,475), la consigne du vérificateur doit demander l'antériorité manquante (DEP2b, ajout possible à la course), session-depot doit choisir 4 sources à PDF empreinté hors de la vue de conv-audit (DEP2c), et, placée en fin de course, M6b n'est pas lancée avec 0,09 (réserve, C13 inchangée) ; sur la porte : +0,002 pour D-g (b) et D-i (2) ensemble (0,156 → 0,158, sortie v6 ; D-g (b) seule n'est pas jouée ; D-i (2) seule donne 0,157). [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-h — Gel et bras méta.** *Décision* : attendre l'annexe scellée du bras méta pour geler ce préenregistrement, ou geler maintenant à deux bras et ajouter le bras méta dans la course sous son propre préenregistrement court. *Enjeu* : R1 et R2 interdisent de geler avec S28 et S29 vides ou de les remplir après avoir vu des fiches (CP4-02) ; l'annexe dépend des verdicts des collisionneurs (R-638), lancés le 30 octobre (R-630). *Options* : (a) retarder — avantages : le bras méta est éprouvé (chaîne, grille, S28) avant la course ; C12 0,97, porte 0,16 ; inconvénient : le pré-pilote attend l'annexe (verdicts, écriture, contre-lecture, approbation ; quelques jours), mais il attend de toute façon la confidentialité, les concrets, la ligne de GO et le devis v4 (DEP4 à DEP6). (b) geler à deux bras (version suivante, retrait des lignes du bras méta ; **désormais applicable : le bras Gu-Krenn ne dépend plus de l'annexe, S31**, CP5-01) — avantage : lancement dès que DEP4 à DEP6 sont levées ; inconvénients : la grille et S28 ne sont pas éprouvées avant la course (la course peut tourner sur une grille illisible pendant toute la génération 1), deuxième préenregistrement à écrire et contre-lire, O15 (c) de fait, **et C12 exige les deux bras restants : 0,86, porte 0,14, nœud 0,70** (sortie v6). [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-i — Plan des fonds et paires inter-fournisseurs.** *Décision* : choisir entre 28 fonds uniques, 28 fonds plus 4 rendus appariés pour la seule mémoire, ou 24 fonds dont 4 doublés. *Enjeu* : R-634 retire la mesure d'auto-préférence « dix fonds écrits deux fois » ; le brouillon 4 en a déduit, de lui-même, le retrait de tout appariement et donc des paires inter-fournisseurs PA de la mémoire anti-redite (CP4-03) — un instrument d'« inédit », pas une mesure de l'organisme. *Options (sortie v6, prédiction P1, D-g a, 45 ; 40)* : (1) 28 uniques — 28,4 USD, PA 0, C6 0,934 (sous sacrifice), porte 0,156, au total 0,201 ; avantage : fiches indépendantes, texte actuel ; inconvénient : la détection d'une même idée rendue par deux fournisseurs n'est pas éprouvée, alors que la course a plusieurs proposeurs. (2) 28 + 4 rendus appariés (mémoire et aiguilleur seulement, aucun juge) — 28,9 USD (+0,50), PA 4 (≈ 2 en vérification), C6 0,950, porte 0,157, au total 0,202 ; avantage : PA retrouvées sans aucune mesure de performance ni fiche corrélée chez les juges ; inconvénient : 2 paires en vérification ne donnent qu'un descriptif. (3) 24 fonds dont 4 doublés — 28,2 USD (−0,24), PA 4, C1-C2 0,37, C6 0,952, porte 0,156, au total 0,215 ; avantage : moins de squelettes ; inconvénient : 8 fiches corrélées dans la lecture primaire des juges (ce que R-634 écartait) ; **son avance « au total » (0,215 contre 0,202) vient d'une simulation à graines neuves et tient dans le bruit de simulation (±0,01) : elle ne départage rien** (CP5-11). [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-j — Gu-Krenn sans condition de reproduction.** *Décision* : relâcher la condition de reproduction préalable pour l'usage du bras Gu-Krenn au pré-pilote et dans la course : oui ou non. le brouillon 4 l'a présenté comme décidé (CP4-04). *Options* : oui — avantage : le bras tourne dès É0, par le modèle ou par le substitut inspiré ; le pire cas est une fusion inutile, filtrée ; inconvénient : le bras peut produire pendant toute la génération 1 avec une règle non validée (étiquette exploratoire). Non — avantage : seule une règle reproduite entre en production ; inconvénient : le bras attend la reproduction (S26 revient, délai inconnu), R-634 s'applique. [retiré, règle 2 : recommandation ou confiance d'auteur]

**S17 — Plafond et arrêt d'étape.** *Décision* : un seul plafond et un seul arrêt d'étape (ou « sans arrêt »), couverts par une ligne de GO. *Enjeu* : A15 interdit tout lancement sans ligne de GO au plafond gelé ; aucun repli (CP4-07) ; sous la règle corrigée (M6 jamais retirée entière), l'arrêt d'étape a un effet mesurable (CP5-06). *Options* : **45 ; 40** — porte 0,156 (0,158), sacrifice 0,24 (0,34), C13 budget 0,92 (0,93), M6 réduite 0,23 (0,32), table seule retirée 0,13 (0,145), dépense médiane 36,3 (38,7), ligne de GO nouvelle à écrire (total 110 ou 123 : lecture L4) ; avantage : l'arrêt réduit M6 à temps, moins de M6 « non mesurée » ; inconvénient : la table seule est retirée deux fois plus souvent. **45 sans arrêt d'étape** — porte 0,154 (0,157), C13 budget 0,90 (0,92), table seule retirée 0,07 (0,11), M6 réduite non lancée 0,094 (0,075) ; avantage : un seul nombre, moins de sacrifices de la table ; inconvénient : M6 tombe plus souvent. **32 ; 28** — porte 0,11 (0,10), sacrifice 0,92 (0,98), C13 budget 0,66 (0,62) ; avantage : couverte par GO-2026-10-30-07, aucune ligne de GO nouvelle à écrire ; inconvénient : vide le pré-pilote de la bisociation et de l'antériorité et ferme C13 une fois sur trois. [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-e — Lecture de « domaine » et de « concept » (bras basique).** *Décision* : fixer ce que mesurent les deux espaces de la règle « loin en domaine, proche en concept ». *Enjeu* : sans lecture fixée, le score du bras basique n'est pas reproductible, et la paire basique sert de comparaison dans la course (R-642, R-643). *Options* : (i) domaine = vecteur indicateur (axe, case) déclarés par la fiche ; concept = étiquettes d'une liste fermée posées par deux lecteurs isolés — avantages : deux espaces mesurés séparément, lecture auditable, accord S24 mesurable ; inconvénient : dans une case unique l'argmax ne dépend que de l'axe (déclaré). (ii) plongement de texte pour les deux espaces — avantage : aucun lecteur à payer ; inconvénients : les deux espaces se confondent, aucun accord mesurable, règle non préenregistrée sous cette forme (préenregistrement de bisociation v2). [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-f — Modèles des rôles neufs.** *Décision* : fixer le tiers metteur en forme T et le relecteur. *Enjeu* : le rendu et la relecture ne doivent venir ni d'un juge ni du rédacteur ; aucun modèle d'un autre fournisseur n'est libre. *Options* : (i) T = Sonnet 5.5, relecteur = Fable 5.1 — avantages : instances neuves disponibles, coût au prix d'Argon ; inconvénients : T et Opus juge du même fournisseur, relecteur et juge Opus de la même famille (biais déclaré, CP2-05). (ii) T = Opus 5.5 — avantage : instance déjà sous relais, aucun fournisseur ni coût de mise en place nouveaux ; inconvénient : Opus est juge (A9). (iii) relecteur = Kimi ou Argon — avantage : relecteur hors de la famille Claude, biais de famille de CP2-05 évité ; inconvénient : ils sont juges. [retiré, règle 2 : recommandation ou confiance d'auteur]

**Seuils S1 à S31** : [retiré, règle 2 : recommandation ou confiance d'auteur]

| N° | Alternative chiffrée |
|---|---|
| S1 | 0,75 : un juge à 0,75 passe 0,47 au lieu de 0,29 (R-1) |
| S2 | — |
| S3 | — |
| S4 | erreur-type ≈ 0,15 à 0,2 (SUPPOSÉ) |
| S6 | — |
| S7 | — |
| S8 | 8 sur 9 passent, 7 sur 9 non |
| S9 | — |
| S10 | — |
| S11 | — |
| S12 | 0,05 : « zéro vu sur 20 » ne le borne pas (0,14) |
| S13 / S14 / S15 | — |
| S16 | — |
| S17 | 45 sans arrêt (C13 budget 0,90) ; 32 ; 28 (ci-dessus) |
| S18 | 0,75 (R-2) |
| S19 | 0,70 (R-3) |
| S20 | — |
| S21 | — |
| (S22) | k = 2 : C10 0,83, porte 0,16 |
| S23 | k = 2 : +2,1 USD |
| S24 | — |
| S25 | — |
| S27 | — |
| S28 | repère S24 |
| S29 | — |
| S30 (si D-g (b)) | 4 sur 4 : borne 0,47 |
| **S31** | seuils 20 et 5 à ajuster sur l'essai de la moisson avant le gel |

**Lectures à confirmer L1 à L7** (marqueurs en « Seuil » ; même format que les décisions ; aucun défaut ; Les lectures « retrait de l'appariement » et « Gu-Krenn sans reproduction » sont les décisions D-i et D-j. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L1 — Passe « tableau » de Kimi (M8).** *Décision* : garder la passe « tableau » (≤ 10 fiches après le tableau minimal) ou la retirer. *Enjeu* : elle est ce que la course fait, elle exerce les cloisons en run et porte M5 à 20 fiches ; R-634 interdit toute mesure de performance de l'organisme, et Lazar pourrait la lire comme telle. *Options* : gardée — avantage : M5 sur 20 fiches (« zéro vu sur 20 » borne le taux à 0,14 ; un taux vrai de 0,20 est déclaré conforme avec 0,22), cloisons exercées en run, redites mesurées (P13) ; inconvénient : ≈ 3,1 USD (passe 2,0 ; aiguilleur et second lecteur 1,1), et son effet n'est pas testé, ce qui est voulu. Retirée — avantage : −3,1 USD ; inconvénient : M5 sur 10 fiches (« zéro vu sur 10 » borne le taux à 0,26 ; taux vrai 0,20 déclaré conforme avec 0,39 ; C8 0,91 au lieu de 0,92, sortie v6), redites non mesurées, cloisons éprouvées en É0 seulement. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L2 — Table seule de l'axe 7 (Plan, CP4-16).** *Décision* : garder la lecture « table seule » (verdict d'Opus sur les 24 éléments de l'axe 7, 0,7 USD, sacrifiable de rang 3) ou la réduire aux bardeaux seuls. *Enjeu* : l'axe 7 est le plus exposé aux paraphrases des huit questions ; la table est écrite par le proposeur ; la version réduite perd la mesure de la table. *Options* : gardée — avantage : les deux gardes mesurées, union prédite 0,75 (table seule 0,50, bardeaux 0,60), C6 0,95 sans sacrifice (0,93 mélangée) ; inconvénient : 0,7 USD, retirée par A1 avec 0,13 (0,145). Réduite aux bardeaux — avantage : 0 USD, rien à sacrifier ; inconvénient : C6 0,81 (0,83), la table n'est pas éprouvée avant la course. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L3 — Désaccord hors du score méta (M9).** *Décision* : le désaccord d(a, b) reste hors du score du bras méta, rapporté par paire, ou y entre. *Enjeu* : R-638 le place hors score ; la garde R5 ligne 24 le vérifie ; s'il entrait, sa place et son poids seraient dans l'annexe. *Options* : hors score — avantage : conforme à R-638, score reproductible sans lecture de désaccord, garde 24 jouable ; inconvénient : le désaccord ne pèse pas sur le choix de la paire. Dans le score — avantage : le profil pourrait préférer les paires qui se contredisent ; inconvénient : un poids à inventer dans l'annexe, garde 24 à réécrire, une lecture de modèle (oui / non / indécidable) entre dans le score. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L4 — Total séquencé pour C10.** *Décision* : lire le reste de la course sur 110 USD (GO-2026-10-30-07 inchangé) ou sur 123 (la ligne nouvelle de R-630 s'ajoute et laisse 78 à la course) ; fixé au gel, jamais lu sur une ligne de GO écrite après (CP5-03). *Enjeu* : C10 vaut 0,92 sous 110 et 0,98 sous 123 (sortie v6) ; la ligne de GO au plafond S17 n'existe pas encore (DEP6). *Options* : 110 — avantage : lecture prudente, rien n'est supposé d'une ligne à écrire ; inconvénient : la course perd ce que le pré-pilote dépense au-delà de 32 (reste médian 73,7 ; tient à 4 sous-sessions avec 0,07). 123 — avantage : C10 0,98, reste 78 ; inconvénient : suppose une ligne qui s'ajoute au lieu de se substituer, ce que seul le mot de Lazar fixe. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L5 — Fusions retirées par A1 et C12 (CP5-02).** *Décision* : si la règle d'A1 retire les fusions, C12 se lit sur les paires et leurs gardes, avec réserve, ou C12 est « non mesurée (budget) » et C13 tombe. *Enjeu* : les trois paires et leurs gardes existent sans dépense ; seule la chaîne après la paire (fusion, aiguilleur, juges) n'est pas éprouvée. *Options* : lue sur les paires — avantage : un sacrifice de rang 1 n'est pas un nœud ; C12 inchangée ; réserve « chaîne éprouvée jusqu'à la paire seulement » et O15 (a) ouverte ; inconvénient : la course peut partir sans qu'une fusion ait été jugée. Non mesurée — avantage : la chaîne entière est exigée avant la course ; inconvénient : nœud avec 0,13 (0,21) de plus, par la première mesure que la règle sacrifie. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L6 — S27 lu comme réserve (R-635).** *Décision* : une couverture Gu-Krenn sous S27 (0,60) est une réserve, ou retire le bras. A19 dit « aucun retrait » ; un retrait serait une cause de bras non produit de plus dans C12. *Options* : réserve — avantage : bras gardé, cohérent avec A19 et R-635 ; inconvénient : une paire choisie parmi peu de fiches notables dit surtout quelles fiches emploient le vocabulaire. Retrait — avantage : aucune paire sur un vocabulaire mal couvert ; inconvénient : contredit A19, et C12 reçoit une cause de bras non produit non chiffrée. [retiré, règle 2 : recommandation ou confiance d'auteur]

**L7 — Brouillon 3 sans contre-lecture.** *Décision* : accepter que le brouillon 3 n'ait pas reçu de contre-lecture (remplacé par le brouillon 4 avant la contre-lecture 3), ou exiger une contre-lecture rétrospective. *Enjeu* : R2 veut chaque préenregistrement contre-lu ; le brouillon 3 est un état intermédiaire gardé (R12) dont tous les changements sont dans la table du brouillon 4 ; les brouillons 4, 5 et 6 ont été contre-lus ou vérifiés (contre-lectures 3 et 4, vérification VB6), et la version gelée recevra la contre-lecture 5. *Options* : accepté — avantage : rien à attendre ; ce qui est gelé est contre-lu ; inconvénient : un brouillon de la chaîne n'a pas été relu. Rétrospective — avantage : R2 à la lettre ; inconvénient : une relecture d'un texte remplacé, sans effet sur la version gelée. [retiré, règle 2 : recommandation ou confiance d'auteur]
<<<FIN PIÈCE 9>>>

### Pièce 11 — `docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v6.md` (l. 20–36 ; 184–232 ; 370–443) — nœuds N2 (retiré)

Origine : main ; empreinte du fichier source `13ef84f9fcee9f43914ba76748805a4f2bff2f30bc42de62f42a0600a97473ed` ; 2544 mots ; règle 2 appliquée.

<<<DÉBUT PIÈCE 11>>>
## 0. Verdict

**Moyenne tirée, sans plafond ni sacrifice : ≈ 40,8 et ≈ 43,5.** Le brouillon 5 disait 28,4. [retiré, règle 2 : recommandation ou confiance d'auteur]
- **45 USD suffisent pour la dépense, pas pour le plan.** Avec les plafonds de relais du brouillon 5 tenus fixes, la dépense reste sous 45 (quantile 99 % : 43,8 USD). Mais **une étape protégée bute sur son plafond de relais avec 0,99** : ces plafonds valent ≈ 1,2 à 1,7 fois l'attendu du brouillon 5 (3 pour É9), sous les dispersions de P11.
- **C'est la souplesse qui fait le travail, pas l'élargissement** (constat 1). Une étape protégée qui atteint son plafond de relais continue sur la marge restante sous le plafond. Avec les plafonds du brouillon 5 gardés et rendus souples :
  - **à 50 USD, arrêt d'étape 45** : sacrifice 0,17 (fusions retirées 0,12), étape protégée non lancée 0,021, coupée 0,063 (l'une ou l'autre 0,072) ; dépense médiane 40,6 USD, quantile 90 % 47,3 ;
  - **à 45 / 40** : sacrifice 0,41 (fusions 0,32), non lancée 0,051, coupée 0,168.
Elle demande aussi deux règles nouvelles au lieu d'une. [retiré, règle 2 : recommandation ou confiance d'auteur]
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **Course 2, 4 sous-sessions, lecture B (24 fusions, ≈ 12 par proposeur, R-642 et n° 268) : ≈ 117,9 USD attendus aux bases, moyenne tirée ≈ 139,2, médiane tirée ≈ 134,9, ≈ 241 au pire.** En lecture A (12 fusions) : ≈ 109,8 aux bases, moyenne 129,3, ≈ 221 au pire. La v4 annonçait 85 aux bases et 180 au pire pour deux bras.
  - **L'écart de + 33,2 USD, par cause, en chaîne** (constat 8) : bases recalées sur les coûts observés (Argon proposeur, contrôles d'Argon par lancement, coupures de Kimi) **+ 16,1** ; trois grilles de lecture d'étiquettes, prises au plan du brouillon 5 **+ 6,4** ; troisième bras (R-643, 12 fusions) **+ 2,7** ; lecture B (24 fusions) **+ 8,0**.
- **Plafond total** : [retiré, règle 2 : recommandation ou confiance d'auteur]
  - **à 110 USD, 4 sous-sessions ont une probabilité < 0,01** au modèle indépendant (0,04 en variante corrélée), et il n'y a aucune course avec 0,52 ;
  - **à 160 USD**, 3 sous-sessions au moins avec 0,76 (0,80 sans complément) ;
  - **à 180 USD**, 4 sous-sessions avec 0,53 (0,57 sans complément).
- **Machine jetable** : à part, devis machine v2 (≈ 0,5 USD attendus, ≈ 7,4 au pire, GO proposé 10 USD), plus les appels de modèle des tests de mort, 0,6 USD par fiche (§ 6).

[…]
### 3.3 45 USD suffisent-ils ?

Règle d'A1 jouée étape par étape, dans l'ordre B. « Sacrifice » compte toute étape sacrifiable retirée ou réduite. « Non lancée » : une étape protégée ne tient pas sous S17 ; le brouillon 5 la dit « non mesuré (budget) ». « Coupée » : une étape protégée atteint son plafond de relais en cours de route (plafond élargi si souple). **Souple** : au lancement d'une étape protégée, son relais est plafonné à max(plafond de l'étape ; S17 − cumul − attendu aux bases des étapes restantes). Le relais reste donc un plafond dur, fixé au lancement.

| Configuration  [retiré, règle 2 : recommandation ou confiance d'auteur]| Dépense médiane | Moyenne | Quantile 90 % | Quantile 99 % | Sacrifice | dont fusions | Protégée non lancée | **Protégée coupée** | Non lancée ou coupée |
|---|---|---|---|---|---|---|---|---|---|
| 45 / 40, plafonds du b5 fixes, texte du brouillon | 34,2 | 34,3 | 40,2 | 43,2 | 0,04 | 0,00 | 0,000 | **0,983** | 0,983 |
| 45 / 40, plafonds du b5 fixes | 36,4 | 36,4 | 41,7 | 43,8 | 0,11 | 0,03 | 0,009 | **0,991** | 0,991 |
| 45 / 40, plafonds du b5 souples, texte du brouillon | 37,7 | 37,0 | 42,3 | 44,3 | 0,30 | 0,21 | 0,029 | 0,103 | 0,111 |
| **45 / 40, plafonds du b5 souples** (nouvelle, constat 1) | 39,6 | 38,8 | 43,3 | 45,0 | 0,41 | 0,32 | 0,051 | 0,168 | 0,188 |
| 45 / 40, plafonds au quantile 90 %, fixes | 38,2 | 38,0 | 42,3 | 44,0 | 0,55 | 0,53 | 0,069 | 0,527 | 0,549 |
| 45 / 40, plafonds au quantile 90 %, souples (option (c) de la v5) | 38,4 | 38,3 | 42,5 | 44,5 | 0,58 | 0,56 | 0,088 | 0,112 | 0,166 |
| **50 / 45, plafonds du b5 souples**  [retiré, règle 2 : recommandation ou confiance d'auteur]| **40,6** | **40,3** | **47,3** | **49,7** | **0,17** | **0,12** | **0,021** | **0,063** | **0,072** |
| idem, postes corrélés (ρ 0,5) | 38,9 | 38,1 | 48,7 | 50,0 | 0,27 | 0,20 | 0,133 | 0,157 | 0,180 |
| 50 / 45, plafonds au quantile 90 %, souples  [retiré, règle 2 : recommandation ou confiance d'auteur]| 41,4 | 40,8 | 46,8 | 48,9 | 0,29 | 0,26 | 0,044 | 0,047 | 0,080 |
| idem, postes corrélés (ρ 0,5) | 40,0 | 38,1 | 48,1 | 49,9 | 0,33 | 0,31 | 0,141 | 0,114 | 0,169 |
| 50 / 45, plafonds au quantile 90 %, fixes | 40,9 | 40,4 | 46,6 | 48,5 | 0,23 | 0,20 | 0,033 | 0,520 | 0,531 |
| 50 / 45, plafonds au quantile 95 %, fixes | 39,8 | 39,7 | 45,5 | 48,0 | 0,43 | 0,40 | 0,032 | 0,266 | 0,284 |
| 55 / 50, plafonds au quantile 95 %, fixes | 41,9 | 41,5 | 48,9 | 52,5 | 0,17 | 0,15 | 0,015 | 0,260 | 0,270 |
| 32 / 28 (GO-2026-10-30-07 tel quel), plafonds du b5 fixes | 28,7 | 28,3 | 31,0 | 31,9 | 1,00 | 1,00 | 0,294 | 0,991 | 0,992 |

**Pont vers la v5 et le relecteur** (médiane 1,0 pour les appels isolés de Kimi, mêmes graines ; constats 1 et 7) :
- 50 / 45, plafonds du b5 souples : sacrifice 0,12, fusions 0,09, non lancée 0,010, coupée 0,043, médiane 38,8 ;
- 45 / 40, plafonds du b5 souples : 0,32 ; 0,25 ; 0,025 ; 0,123 ;
- 50 / 45, quantile 90 % souples : 0,20 ; 0,18 ; 0,031 ; 0,037 ; médiane 40,1.

Ce sont les chiffres du relecteur et ceux de la v5, à l'identique. Le passage à la médiane 1,4 durcit tout : + 0,05 à + 0,09 sur le sacrifice, + 0,01 à + 0,05 sur les étapes protégées. Il ne change pas l'ordre des options.

**Réponse.**
- **Pour la dépense, oui** : à 45 USD, avec les plafonds du brouillon 5 tenus fixes, on n'atteint jamais 45 (maximum tiré 44,9).
- **Pour le plan, non.**
  - **Ce qui casse** : avec les dispersions de P11, les plafonds de relais fixes du brouillon 5 coupent une étape protégée presque à coup sûr. En cause : les lectures d'étiquettes (0,88), É2 (0,55), É5bis si elle a lieu (0,48), É3 (0,37), É4 (0,34), É5 (0,19). Le brouillon 5 ne dit pas ce que devient une étape protégée coupée par son relais : il ne dit « non mesuré (budget) » que pour une étape non lancée (l. 292, A1). **Lecture, à confirmer au brouillon 6** : une étape protégée coupée a une mesure incomplète, donc « non mesuré (budget) », C13 non satisfaite, nœud. Le script v5 du brouillon 5 ne simulait pas ces coupures : il donnait une étape protégée non lancée avec 0,032.
  - **Élargir les plafonds de relais déplace le problème** : la règle d'A1 projette avec le plafond de chaque étape, donc des plafonds plus larges font sacrifier plus tôt. À 45 USD, au quantile 90 %, les fusions partent avec 0,56, et avec elles la chaîne de bisociation du pré-pilote.
  - **C'est la souplesse qui fait le travail** (constat 1) : à plafond égal, les plafonds du brouillon 5 rendus souples font moins sacrifier que les plafonds au quantile 90 % rendus souples (0,17 contre 0,29 à 50 USD ; 0,41 contre 0,58 à 45). Ils coupent un peu plus souvent une étape protégée (0,063 contre 0,047 à 50), à peu près autant sur « non lancée ou coupée » (0,072 contre 0,080 ; 0,180 contre 0,169 en variante corrélée).
- **Le couple** :
  - plafond **50 USD**, arrêt d'étape **45** ;
  - plafonds de relais **du brouillon 5, inchangés** ;
  - **souples** pour les étapes protégées (définition ci-dessus), fixes pour les sacrifiables.
- **Ce que ce couple donne** : sacrifice 0,17 (fusions 0,12), étape protégée non lancée 0,021, coupée 0,063 ; dépense médiane 40,6 USD, moyenne 40,3, quantile 90 % 47,3.

### 3.4 Ce qui est à porter au brouillon 6 (conv-audit, pas une décision de Lazar)

1. **Plafonds de relais** : garder ceux du brouillon 5 et rendre souples ceux des étapes protégées. Au lancement d'une étape protégée, son relais est plafonné à max(plafond de l'étape ; S17 − cumul − attendu aux bases des étapes restantes). C'est une seule règle changée dans A1 ; elle demande une contre-lecture. [retiré, règle 2 : recommandation ou confiance d'auteur]
2. **Étape protégée coupée par son relais** : écrire son statut (lecture proposée : « non mesuré (budget) », C13 non satisfaite) ; le brouillon 5 ne le dit que pour une étape non lancée.
3. Lectures d'étiquettes : 60 lectures, pas 30 (§ 3.2).
4. Seconde version des témoins : 5,8 USD attendus aux bases si elle a lieu, contre 4,9 au brouillon 5. Elle comprend le relecteur sur 30 rendus et 28 lectures d'aiguillage.
5. Base du tiers T : prix de Sonnet 5.5 (2 / 10), au lieu du prix d'Argon.
6. Complément conditionnel : son plafond de 17,5 tient avec 0,951 aux bases v6 (médiane 1,4 pour Kimi isolé), et non plus 0,988.

[…]
## 9. Décisions pour Lazar (nœuds de dépense ; aucune n'a de défaut)

### Décision 1 — plafond du pré-pilote (S17)

**Décision** : quel plafond, quel arrêt d'étape et quelle forme des plafonds de relais pour le pré-pilote recentré ?

**Enjeu** : à 45 USD, la dépense tient, mais le plan ne passe pas. Avec les plafonds de relais du brouillon 5 tenus fixes, une étape protégée bute presque toujours sur le sien. La souplesse règle cela ; l'élargissement fait sacrifier les fusions.

**Options**
- **(a) 45 / 40, plafonds de relais du brouillon 5, fixes.**
ne dépasse jamais 45. [retiré, règle 2 : recommandation ou confiance d'auteur]
  - Inconvénient : une étape protégée est coupée avec 0,99 (C13 fermée, nœud, lecture à confirmer au brouillon 6).
- **(b) 50 / 45, plafonds de relais du brouillon 5, rendus souples pour les étapes protégées** (nouvelle, constat 1 ; une règle à écrire au brouillon 6).
  - Avantage : sacrifice 0,17 (fusions 0,12) ; étape protégée non lancée 0,021, coupée 0,063 ; dépense médiane 40,6 USD (moyenne 40,3) ; une seule règle changée.
  - Inconvénient : 5 USD de plus engagés sur le plafond total ; règle nouvelle à contre-lire ; un peu plus de coupures que (d).
- **(c) 45 / 40, plafonds de relais du brouillon 5, souples** (nouvelle).
  - Avantage : garde 45 ; une seule règle changée.
  - Inconvénient : sacrifice 0,41 (fusions 0,32) ; étape protégée non lancée 0,051, coupée 0,168.
- **(d) 50 / 45, plafonds au quantile 90 %, souples**. [retiré, règle 2 : recommandation ou confiance d'auteur]
  - Avantage : coupure la plus basse (0,047) ; non lancée 0,044.
  - Inconvénient : sacrifice 0,29 (fusions 0,26) ; deux règles changées ; dépense médiane 41,4.
- **(e) 45 / 40, plafonds au quantile 90 %, souples** (option (c) de la v5).
  - Avantage : garde 45.
  - Inconvénient : fusions sacrifiées avec 0,56 ; non lancée 0,088 ; deux règles changées. Fait moins bien que (c) sur le sacrifice et la non-lancée, mieux sur la coupure (0,112 contre 0,168).

[retiré, règle 2 : recommandation ou confiance d'auteur]

**Défaut** : aucun. Sans mot de Lazar, GO-2026-10-30-07 reste tel quel (pré-pilote ≤ 32), et rien n'est lancé à 32 : le brouillon 5 prévoit l'arrêt par A15.

### Décision 2 — plafond total de la course 2 (génération 1)

**Décision** : quel plafond total séquencé pour le pré-pilote et la course ?

**Enjeu** : sur les coûts observés, la course à 4 sous-sessions coûte ≈ 117,9 USD attendus aux bases (moyenne tirée ≈ 139, médiane ≈ 135, pire ≈ 241). Le total actuel de 110 ne la laisse à 4 sous-sessions qu'avec < 0,01, et sans aucune course avec 0,52 (complément compté).

**Options** (pré-pilote à l'option (b) de la décision 1 ; complément compté sur le reste ; lecture B ; entre parenthèses, sans complément)
- **(a) 160 USD.**
  - Avantage : 3 sous-sessions au moins avec 0,76 (0,80), et 4 avec 0,21 (0,25 ; 0,40 en lecture A sans complément).
  - Inconvénient : 50 USD de plus que GO-2026-10-30-07 ; le pire (≈ 291) reste hors plafond, tenu par le seul séquençage.
- **(b) 180 USD.**
  - Avantage : 4 sous-sessions avec 0,53 (0,57 ; 0,72 en lecture A sans complément).
  - Inconvénient : 70 USD de plus ; peu de gain si 3 sous-sessions suffisent à l'objectif.
- **(c) 140 USD.**
  - Avantage : 30 USD de plus seulement.
  - Inconvénient : course à 2 sous-sessions avec 0,54, à 4 avec 0,03.
- **(d) 110 USD, gardé.**
  - Avantage : rien ne bouge.
  - Inconvénient : course à 2 sous-sessions au mieux (0,47) ; aucune avec 0,52.
- **(e) lecture « total 123 » du brouillon 5** (LECTURE À CONFIRMER de S17, C10 et DEP6 : la ligne nouvelle du pré-pilote s'ajoute au total séquencé ; 128 si le pré-pilote est à 50).
  - Avantage : la plus petite hausse (13 ou 18 USD) ; déjà écrite au brouillon 5.
  - Inconvénient : à 128, 3 sous-sessions au moins avec 0,18 (0,21), aucune course avec 0,14 ; si la course garde 78 au sens strict : 3 au moins 0,045, aucune 0,29.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**Défaut** : aucun.

### Décision 3 — nombre de fusions de la course (lecture de « une paire par session »)

**Décision** : 24 fusions (une paire par bras et par proposeur dans chaque sous-session) ou 12 (une paire par bras et par sous-session) ?

**Enjeu** : ≈ 8 USD attendus aux bases (117,9 contre 109,8 ; ≈ 10 en moyenne tirée, 139,2 contre 129,3), et l'effectif de la comparaison entre bras, qui est la raison de garder le bras basique (R-642).

**Options**
- **(a) 24 (lecture B).**
  - Avantage : lettre du n° 268 et de R-642 ; 8 fusions par bras au lieu de 4.
  - Inconvénient : + 8 USD ; 4 sous-sessions moins probables à plafond égal.
- **(b) 12 (lecture A).**
  - Avantage : − 8 USD ; lecture du brouillon 5 (S22, k = 1).
  - Inconvénient : 4 fusions par bras : aucune comparaison lisible.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**Défaut** : aucun. À trancher avant la v53 et le gel de S22.
<<<FIN PIÈCE 11>>>

### Pièce 12 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/contre-lecture-annexe-bras-meta-v1-brouillon1.md` (l. 19–22 ; 49–87 ; 125–146) — nœuds N4

Origine : branche de conv-audit ; empreinte du fichier source `db249b9356f8d19cd8c9811c3db184b0d7587eba97ed8386501e146434e24f1d` ; 2369 mots ; règle 2 étendue (confiance d'auteur) ; règle 2 appliquée.

<<<DÉBUT PIÈCE 12>>>
## Verdict

**Soumettable après corrections.** Le bloc lisible par le code est conforme et bloque comme annoncé ; les chiffres de l'annexe se rejouent ; les dix incompatibilités sont exactes. Mais trois défauts de fond doivent être traités ou assumés avant que Lazar approuve des valeurs : (1) la grille et les tables mettent dans le profil la paire n1–n2 que le programme lui-même fusionne, et n'y mettent jamais n5 ; (2) le pré-pilote n'éprouvera le profil que dans une minorité de lots (constat à remonter à Lazar, section C) ; (3) l'argument qui retire les jeux de données du compte vaut aussi pour des structures que le texte I impose à presque toutes les fiches. Aucun défaut ne rend la pièce dangereuse à soumettre : l'annexe se déclare brouillon et le bloc est refusé par le code tant que les champs ne sont pas remplis.

[…]
## C. Profil et P14 — **constat majeur à remonter à Lazar**

**Nombre de paires de niches dans le profil** : 4 sur 15 (n1–n2, n1–n4, n1–n6, n3–n4), vérifié par code. Avec c ≤ 1 seul : 7 ; la bande en retire 3 (n2–n5 : e = 5 ; n4–n5 et n5–n6 : e = 4).

**Rejeu de la prédiction (100 000 tirages, mes graines)** :

| Lot | Loi a priori | Médiane | Zéro dans le profil | Aucune paire éligible |
|---|---|---|---|---|
| 6 fiches | annexe (n1 0,30 … n6 0,05) | 0 | 0,59 | 0,04 |
| 6 fiches | « n6 fort » (n6 0,35, n5 0,20) | 0 | 0,67 | 0,04 |
| 6 fiches | « n2 fort » (n2 0,30) | 0 | 0,66 | 0,04 |
| 10 fiches | annexe | 1 | 0,25 | 0,002 |
| 10 fiches | « n6 fort » | 1 | 0,36 | 0,003 |
| 10 fiches | « n2 fort » | 1 | 0,34 | 0,002 |
| 15 fiches | annexe | 4 | 0,06 | 0,000 |

La loi a priori de l'annexe donne 5 % à n6, alors que ses propres mots-indices d'n6 (« famille tenue à l'écart », « transfert », « universalité », « préenregistrement ») décrivent les axes 3 et 4, soit environ 40 % des axes : cette loi paraît sous-estimer n6 (SUPPOSÉ des deux côtés). Conclusion robuste : la fraction de lots sans paire du profil est entre 0,6 et 0,7 à 6 fiches et entre 0,25 et 0,36 à 10 fiches.

**Le pré-pilote n'éprouve-t-il que le repli ?** À 6 fiches : oui, dans environ 6 lots sur 10 ; à 10 fiches : dans 1 lot sur 3 à 1 sur 4. Même quand une paire du profil existe, il y en a une (médiane 1) : le pré-pilote n'a qu'une paire méta, donc ne peut éprouver ni le classement par score (poids 0,5, égalités) ni le contraste profil / hors profil. Il éprouve la chaîne (lecture, paire, fusion, aiguilleur, juges), ce qui est le but affiché de M9 (descriptive pour l'effet, décisive pour la chaîne). Mais le bras est étiqueté « méta, profil trou à structure commune » ; une fusion issue du repli est « la paire à deux indicateurs sur trois » : le nom de bras ne dit plus la même chose. L'annexe le dit (« c'est attendu, déclaré ») ; ce n'est pas encore traité comme un constat pour Lazar : **il doit lui être écrit en tête de la demande d'approbation.**

**Aggravants que l'annexe ne chiffre pas** : (a) l'indépendance supposée entre « structure partagée » et « canal faible » est optimiste : deux niches qui communiquent peu partagent, par définition, moins de structures (le « trou à structure commune » est une conjonction rare) ; (b) `choisir_paires` retire des candidates les paires déjà prises par un bras antérieur (ordre tiré) : la seule paire du profil peut être prise par le bras basique ou le bras Gu-Krenn, et le bras méta tombe alors au repli, sans que P14 en tienne compte (CA1-09) ; (c) la proportion de fiches retenues (accord des deux lecteurs 0,7) est supposée uniforme, alors qu'elle est plus basse sur les axes 1 et 3, qui nourrissent le profil.

**Options pour Lazar** (avec l'effet mesuré par mon rejeu, accord 0,7, structure 0,3) :
1. **Accepter le repli comme mesure** et le dire dans le nom du résultat : « le pré-pilote éprouve la chaîne, non le profil » ; zéro coût ; la prédiction P14 est remplacée par celle de l'annexe. Avantage : honnête, rapide. Inconvénient : rien n'est appris sur la lisibilité du profil avant la course.
2. **Plus de fiches non aiguillées** : 15 fiches donnent une médiane de 4 paires du profil et zéro avec 0,06 ; mais le pré-pilote est borné à ≤ 10 fiches de passe 1 (M4/M5) et le coût monte (lectures d'étiquettes). Demande un devis.
3. **Élargir la bande à [2 ; 4]** : n'aide presque pas (zéro 0,54 à 6 fiches, 0,21 à 10) ; les deux paires ajoutées passent par n5 (n4–n5, n5–n6, e = 4) et n5 est rare dans la loi de l'annexe. **Retirer la bande** : zéro 0,47 et 0,14 ; contraire à R-638. **Élargir le canal à c ≤ 2** : zéro 0,35 et 0,07 mais « faible » cesse d'avoir un sens (10 paires sur 15).
4. **Revoir le seuil de structure** (par exemple compter une structure à nom « presque partagé ») : ce n'est pas un paramètre de l'annexe, c'est une modification du profil de R-638 : nœud de Lazar.

Ma lecture, sans trancher : l'option 1 est cohérente avec le brouillon 7 ; l'option 2 est la seule qui change la fréquence du profil sans toucher à R-638 ; l'option 3 ne sert pas.

## D. Fidélité à R-638 — **tenu avec un écart à trancher et une incohérence**

- Communication faible entre niches : tenu (propriété de la paire de niches, fixée avant toute fiche).
- Désaccord lu à part, hors score : tenu ; la lecture par paire après le scellement des paires est plus stricte que la garde de signature. Écart par rapport au brouillon 7 : M9 dit « rapporté pour chaque paire candidate » et un champ « affirmation centrale » recopié ; l'annexe lit au plus 5 paires et change l'entrée du lecteur (CA1-10).
- Éloignement non extrême selon Uzzi : tenu et bien marqué SUPPOSÉ (section E sur les pages).
- **Structure commune forte** : R-638 nomme « objet mathématique, méthode, jeu de données ». L'annexe retire le jeu de données du compte et l'avoue (« écart déclaré »). Mon avis de contre-lecteur : l'argument tient pour D1 (le texte I le fait servir à presque toutes les fiches), mais **le même argument vaut pour `om_somme_cumulee_temps_arret`, `om_martingale_e_processus` et `me_test_sequentiel_cusum`** : le glossaire impose « fausse alerte tenue à tout instant », l'axe 1 impose l'agrégation, l'axe 5 la borne de délai ; ces structures seront partagées par la plupart des fiches de n1, n2 et n5, et la probabilité de 0,3 de partager au moins une structure comptée est un chiffre posé, pas mesuré. L'annexe ne retire pas ces structures « quasi universelles » alors qu'elle dit le faire (section 3, raison) : l'incohérence est à corriger (CA1-04). La décision de compter ou non les jeux de données reste à Lazar, avec cette précision.
- « Forte » = au moins une structure partagée parmi 14 identifiants : très faible comme « forte » ; [retiré, règle 2 : recommandation ou confiance d'auteur]
- Ajouts non demandés par R-638 qui changent le profil : quatrième type « protocole » (lu, non compté) ; règle « deux lecteurs d'accord » (déjà dans le code) ; seuil c ≤ 1 ; union des structures des deux lecteurs (favorise les fiches à beaucoup d'étiquettes). Aucun ne contredit R-638 mais chacun est un choix à faire valider.

[…]
## Constats

| N° | Gravité | Constat | Preuve | Correction demandée |
|---|---|---|---|---|
| CA1-01 | majeur | La paire n1–n2 est dans le profil (c = 1, e = 3) alors que l'annexe écrit elle-même que le programme fusionne n1 et n2 ; deux fiches voisines de l'axe 1 peuvent être rangées chacune de façon stable en n1 et n2 et fabriquer une paire « loin » par bruit d'étiquette. | Annexe section 1 réserve et tables ; texte I axe 1 ; `course2_v53._notes` (le filtre ne compare que les deux lecteurs d'une même fiche). | Soit fusionner n1 et n2 (grille à 5 niches), soit relever c(n1, n2) à 2 ou 3 et dire l'effet sur le profil ; soit écrire la limite et un contrôle (lot des fiches d'axe 1 rangées dans deux niches). |
| CA1-02 | moyen | L'alternative (b) de la grille appelle n2–n5 « la paire la plus nette » du profil ; cette paire (c = 0) est exclue par la bande (e = 5). | Annexe sections 1 et 5 (tables). | Corriger la phrase, ou assumer que la paire à canal nul est écartée comme extrême, ce qui est un résultat de lecture d'Uzzi à dire. |
| CA1-03 | majeur | n5 n'appartient à aucune paire du profil : toute fiche d'axe 2 ou 5 (environ 40 % des axes) est exclue du bras méta par construction. | Calcul : partenaires de n5 à c ≤ 1 : n2 (e = 5), n4 (e = 4), n6 (e = 4). | Dire la limite en tête de l'annexe ; décider si n5 doit avoir un partenaire (bande, table ou grille). |
| CA1-04 | moyen | L'argument « jeux de données universels, donc non comptés » vaut aussi pour les structures séquentielles imposées par le texte I ; l'annexe ne les retire pas. Écart à R-638 à trancher en l'état. | Texte I glossaire et axes 1 et 5 ; annexe section 3. | Retirer ou signaler ces structures, ou renoncer à l'argument ; mesurer la fréquence sur le jeu d'essai (non sur des fiches réelles). |
| CA1-05 | majeur | Le pré-pilote n'éprouve le profil que dans 40 % (6 fiches) à 65-75 % (10 fiches) des lots, et une seule paire du profil au mieux. Constat à remonter à Lazar avec options. | Rejeu : zéro 0,59 à 0,67 (6 fiches), 0,25 à 0,36 (10 fiches). | Placer en tête de la demande d'approbation ; options de la section C. |
| CA1-06 | moyen | La loi a priori des niches (n6 5 %, n4 10 %) contredit les mots-indices de n6 et la structure en cinq axes ; indépendance structure / canal optimiste. | Annexe section 6 ; texte I axes 3 et 4. | Justifier la loi ou donner la fourchette complète (mon rejeu : 0,67 et 0,36). |
| CA1-07 | mineur | La borne basse de la bande (2) ne sert à aucune paire du profil ; Uzzi ne fonde pas l'exclusion du quasi identique (la nouveauté de queue est toujours favorable ; la cloche ne porte que sur la conventionnalité médiane). | Quatre paires du profil toutes à e = 3 ; Uzzi p. 471. | Dire que la bande effective est e = 3 ; reformuler la phrase sur Uzzi. |
| CA1-08 | moyen | Biais de conception non listé : un score croissant en structures partagées sélectionne des paires faciles à fusionner de façon cohérente, ce que les juges notent. | Annexe section 7 (aucune ligne sur ce point) ; score `1 + 0,5 × s`. | Ajouter une limite d'interprétation pour toute comparaison méta / basique en course ; reformuler la ligne « popularité seule » (le bras basique n'en est pas un). |
| CA1-09 | moyen | `choisir_paires` retire les paires prises par un bras antérieur ; la seule paire du profil peut être prise, le méta tombe alors au repli. P14 ne le chiffre pas. | `bisociateur_v53.choisir_paires` (`prises`) ; ordre tiré. | Chiffrer dans le script v7 ; ajouter I-11. |
| CA1-10 | moyen | Le désaccord lu par paire après sélection (5 paires, anonyme, sur le champ « hypothèse ») diffère du brouillon 7 (chaque paire candidate, champ « affirmation centrale » recopié) ; I-12 (artefact d'ordre sans support de code) et I-13 (dépense) absents de la liste. | Brouillon 7 M9 ; annexe section 4 ; `course2_v53` ligne 491. | Écrire l'écart à M9 pour Lazar ; ajouter I-12, I-13 ; chiffrer la dépense. |
| CA1-11 | mineur | « Erreur-type 0,2 à 6 contre 6, sortie v6 » : renvoi non retrouvé dans la sortie v6 (HM calculé : ≈ 0,17). Autres références : « Shi-Evans, page en ligne », « Yegros-Yegros, Dunbar » restent à vérifier (R7) avant d'être utilisées dans un papier. | Sortie v6 ; calcul HM. | Corriger le renvoi ou retirer le chiffre. |
| CA1-12 | mineur | Script P14 et sortie non versés, garde 22a exige script rejoué et sortie nommée. | Annexe en-tête et section 6 ; mon rejeu confirme les chiffres. | Verser avec compagnon avant scellement. |
| CA1-13 | mineur | Le format d'une structure dans la lecture (`{"type", "nom"}`) n'est pas décrit dans l'annexe, qui montre `"structures": [...]` de chaînes ; les écarts de forme feraient rejeter la lecture par `valider_niche`. | Annexe section 1 (« règle de lecture ») ; `valider_niche`. | Écrire le format exact à recopier dans la consigne du lecteur. |
| CA1-14 | mineur | Couverture : huit cases de l'esquisse du texte I sans niche ; « mêmes niches pour toutes les cases » en course 2. | Texte I annexe 1 (grille des sous-domaines). | Limiter la portée aux axes 1 à 5 ou prévoir une grille d'axe 7. |
| CA1-15 | mineur | Le champ `contre_lecture` ne contrôle que la non-vacuité (I-9) : cette contre-lecture devra être citée avec son empreinte, pas seulement nommée. | Code `lire_annexe_meta`. | Prévu par la procédure (section 9, point 5) ; v54. |

*Fin. Aucune valeur n'a été gelée ni tranchée ; ce document ne vaut pas approbation.*
<<<FIN PIÈCE 12>>>

### Pièce 13 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon1.md` (l. 18–30 ; 85–102 ; 116–224) — nœuds N4

Origine : branche de conv-audit ; empreinte du fichier source `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` ; 2860 mots ; règle 2 étendue (option recommandée) ; règle 2 appliquée.

<<<DÉBUT PIÈCE 13>>>
## Résumé (dix lignes)

1. **Grille** : six niches du sous-domaine « contrôle des intelligences artificielles et environnements de comparaison », chacune définie par la communauté dont la méthode porte l'affirmation centrale de la fiche, jamais par l'axe (sinon le bras méta recopierait le domaine du bras basique).
2. **Accord (S28)** : kappa de Cohen sur la niche ≥ 0,40 ; Jaccard moyen sur les structures ≥ 0,30 ; marges constantes lues 1 ou 0 et marquées « dégénérée sur ce lot » (règle du brouillon 7, codée telle quelle dans v53).
3. **Communication faible** : pas de citations au pré-pilote ; ce qui en tient lieu est une **table du canal entre niches** (0 à 3), écrite à la main avant toute fiche, propriété de la paire de niches et non de la paire de fiches ; « faible » = 0 ou 1.
4. **Structure forte** : liste fermée de 20 structures nommées en quatre types ; « forte » = au moins une structure partagée de type objet mathématique ou méthode ; jeux de données et protocoles sont lus mais ne comptent pas (le texte I les impose presque tous à toutes les fiches).
5. **Désaccord** : lu par paire, **après** le choix des paires, journalisé dans un fichier scellé, jamais passé à la fonction de score.
6. **Éloignement** : table de distance de contenu (1 à 5) ; bande [2 ; 3] ; l'exclusion des paires extrêmes s'appuie sur Uzzi 2013, vérifié sur PDF (p. 471), mais **sa transposition aux niches est SUPPOSÉ**.
7. **Score** : 1[faible] × 1[forte] × 1[bande] × (1 + 0,5 × s) ; repli `indicateurs_puis_structure`, seul admis par le code ; profil non vide sur le jeu d'essai (5 paires dans le profil, 36 hors profil, 4 refusées pour même niche).
8. **P14 refaite (indicative)** : 4 paires de niches sur 15 dans le profil ; à 10 fiches, médiane 1 paire dans le profil, zéro avec 0,25 ; à 6 fiches, médiane 0, zéro avec 0,59 : **le repli sera souvent seul éprouvé**.
9. **Incompatibilités** avec le code v53 : dix, dont trois qui demandent une version 54 avant É0 (noms de structure non contrôlés, désaccord non lu, cause « aucune paire notable » absente de C12) (section 10).
10. **Procédure** : contre-lecture par un modèle différent, mot de Lazar sur chaque valeur, remplissage des deux champs, scellement, empreinte écrite au préenregistrement et dans la configuration avant É0 ; sans cela, A20.

[…]
## 3. Structure commune forte (S29 c)

**Types admis (À GELER par Lazar)** : objet mathématique (`om_`), méthode (`me_`), jeu de données (`jd_`), protocole (`pr_`). **Liste fermée de 20 structures nommées** (le lecteur choisit dans la liste ; aucune structure libre) :

| Type | Identifiants (définition entre parenthèses) |
|---|---|
| objet mathématique | `om_martingale_e_processus` (martingale, surmartingale, e-processus) ; `om_rapport_vraisemblance_divergence` (rapport de vraisemblance, divergence) ; `om_covariance_mahalanobis` (matrice de covariance, distance de Mahalanobis) ; `om_direction_sous_espace` (direction, projection, sous-espace) ; `om_somme_cumulee_temps_arret` (somme cumulée, marche aléatoire, temps d'arrêt) ; `om_jeu_minimax` (jeu à deux, stratégie minimax, équilibre) ; `om_graphe_causal` (graphe causal, intervention) |
| méthode | `me_test_sequentiel_cusum` ; `me_seuil_conforme` ; `me_dictionnaire_parcimonieux` (auto-encodeur parcimonieux) ; `me_intervention_activations` (patching, ablation) ; `me_moniteur_par_modele` ; `me_estimation_densite` ; `me_preuve_formelle` (Lean) |
| jeu de données | `jd_simulateur_fige` (D1) ; `jd_donnees_publiques` (D2) ; `jd_notations_juges` (D3) |
| protocole | `pr_exclusion_famille` (une famille exclue à la fois) ; `pr_audit_budgete` ; `pr_reechantillonnage_report` |

**« Forte » (À GELER par Lazar)** : **au moins 1 structure partagée** (même identifiant chez les deux fiches) **parmi les objets mathématiques et les méthodes** ; jeux de données et protocoles sont lus, rapportés, **non comptés**. **Mesure** : s(a, b) = nombre de structures partagées de type objet mathématique ou méthode (exactement ce que calcule `indicateurs_meta`).
- Raison : la liste D du texte I ne compte que trois jeux, et D1 sert à presque toutes les fiches : un jeu de données partagé ne dit rien ; de même les protocoles imposés par le texte I. La réponse 2 v2 demande de pondérer par la rareté (« une équation de diffusion partagée dit peu ») : à défaut de poids, je retire les structures quasi universelles. Les éléments imposés par le texte I à toutes les fiches (plancher apparié, sonde nulle, trois jeux disjoints) ne figurent pas dans la liste, pour la même raison.
- Alternatives : (b) au moins 2 structures partagées — avantage : profil plus strict ; inconvénient : avec 2 à 4 structures par fiche, le profil devient vide sur la plupart des lots (P14 tomberait sous la médiane 1 à 10 fiches) ; (c) compter les jeux de données — avantage : conforme à la liste de R-638, qui nomme le jeu de données ; inconvénient : profil rempli par D1 seul (démontré sur le jeu d'essai : paire e09–e10).
- Confiance : 0,5 (liste) ; 0,55 (seuil 1, types comptés).
- **Écart déclaré à R-638** : R-638 nomme « objet mathématique, méthode, jeu de données » ; je propose de lire le jeu de données sans le compter, pour la raison ci-dessus. C'est une lecture à confirmer par Lazar.
- **Compatibilité v53** : le code ne connaît que des « types » et accepte n'importe quel nom ; une structure partagée exige l'égalité exacte du couple (type, nom). Je propose donc de servir **chaque structure nommée comme un « type »** (`types_structure` = les 20 identifiants) et d'imposer dans la consigne du lecteur que le nom **recopie l'identifiant**. Le code v53 ne vérifie pas cette égalité : un nom différent passerait en silence et ferait baisser s (vérifié sur le code : `{"type": "me_test_sequentiel_cusum", "nom": "CUSUM"}` est accepté). D'où l'incompatibilité I-1 et la demande d'un contrôle en v54. [retiré, règle 2 : recommandation ou confiance d'auteur]

[…]
## 5. Bande d'éloignement non extrême (S29 d)

**Mesure (À GELER par Lazar).** e(n_a, n_b) = **distance de contenu** entre les deux niches (objets étudiés et vocabulaire), échelle 1 à 5 (1 : objets et vocabulaire quasi identiques ; 5 : aucun objet ni vocabulaire communs), table à la main, SUPPOSÉ. Elle est **distincte du canal** (section 2) : deux niches peuvent parler peu et étudier presque la même chose (n1–n4 : c = 1, e = 3), ou beaucoup et des choses différentes.

| e (contenu) | n2 activations | n3 anomalies | n4 moniteurs | n5 bornes | n6 évaluation |
|---|---|---|---|---|---|
| **n1 séquentiel** | 3 | 2 | 3 | 2 | 3 |
| **n2 activations** | — | 2 | 3 | 5 | 3 |
| **n3 anomalies** | | — | 3 | 3 | 3 |
| **n4 moniteurs** | | | — | 4 | 2 |
| **n5 bornes** | | | | — | 4 |

**Bande proposée (À GELER par Lazar) : [e_min ; e_max] = [2 ; 3].** Avec c ≤ 1, **4 paires de niches sur 15** sont dans le profil (aux structures près) : n1–n2, n1–n4, n1–n6, n3–n4 ; 3 paires à canal faible en sont exclues parce qu'extrêmes (n2–n5 : e = 5 ; n4–n5 et n5–n6 : e = 4). La bande et le seuil se recoupent (exigence de non-vacuité, M9).

**Lien avec la cloche d'Uzzi.**
- **Vérifié sur PDF** (`uzzi-mukherjee-stringer-jones-2013-science.pdf`, `532970985650…`) : succès = article dans les 5 % les plus cités à 8 ans (p. 469) ; « peak impact occurred in the 85th to 95th percentile of median conventionality, an exceptionally high level » (p. 471, texte) et, en légende de la figure 4, l'impact croît avec la conventionnalité médiane « up to the 85th to 95th percentile of median conventionality, after which the relationship reverses » (p. 471). La conventionnalité est mesurée par le z-score des paires de revues citées ensemble contre un modèle nul (p. 469).
- **SUPPOSÉ (transposition)** : Uzzi mesure la conventionnalité des **combinaisons de références d'un article**, pas la distance entre deux niches d'une paire de fiches. Ce que j'en retiens, comme forme et non comme chiffre : l'optimum n'est pas à l'extrême ; il est du côté du familier avec une pointe d'atypique. D'où une bande qui exclut le plus lointain (4 et 5) et le quasi identique (1), et qui penche vers le proche (2 et 3 sur 5). **Aucun chiffre d'Uzzi n'est transposé** : 85e–95e percentile n'a pas d'équivalent sur une échelle à cinq crans entre six niches.
- Concordances non vérifiées ici : Yegros-Yegros 2015 (U inversé sur la disparité) et Dunbar (analogies locales ou régionales) vont dans le même sens (revue v1, SUPPOSÉ) ; Shi-Evans 2023 trouve au contraire une relation monotone (revue v1, page en ligne) : la cloche n'est pas acquise.
- Alternatives : (b) [2 ; 4] — avantage : 6 paires de niches sur 15 dans le profil, P14 un peu moins vide (zéro avec 0,20 au lieu de 0,25 à 10 fiches, section 6) ; inconvénient : admet n4–n5 et n5–n6, qui sont presque l'extrême de l'échelle ; (c) aucune bande (indicateur toujours vrai) — avantage : un paramètre de moins ; inconvénient : contraire à R-638 (« éloignement non extrême »).
- Confiance : 0,4 pour la table ; 0,45 pour la bande.

## 6. Forme et poids du score ; repli ; non-vacuité ; prédiction P14 (S29 e, f)

**Forme (À GELER par Lazar ; forme écrite au brouillon 7 et codée dans `score_meta`).** score méta(a, b) = 1[c ≤ 1] × 1[s ≥ 1] × 1[2 ≤ e ≤ 3] × (1 + **poids** × s), **poids = 0,5** ; paire méta = argmax ; égalités par la clé tirée `bisoc-meta` (SeedSequence, R9).
- Raison du poids : dans le profil, préférer la paire qui partage le plus de structures (2 structures : 2,0 ; 1 structure : 1,5) sans que le poids puisse faire entrer une paire hors profil.
- Alternative : poids 0 (indicateurs seuls, égalités au tirage) — avantage : aucun choix de poids ; inconvénient : une paire à trois structures communes ne bat pas une paire à une.
- Confiance : 0,5.
- **Contrainte à écrire** : poids ≥ 0. Le code ne le vérifie pas : un poids négatif rendrait des paires du profil « hors profil » (vérifié : `poids = -2` est accepté par `lire_annexe_meta`) ; incompatibilité I-6.

**Règle de repli hors profil (S29 f ; À GELER par Lazar).** **`indicateurs_puis_structure`**, la seule que le code admet (`REPLIS_CONNUS = ("indicateurs_puis_structure",)` ; toute autre est refusée à É0, A20). Lecture : quand aucune paire ne satisfait les trois indicateurs, la paire retenue est celle qui en satisfait le plus, puis qui partage le plus de structures (`score_repli` = (nombre d'indicateurs vrais, s)), égalités au tirage ; elle est comptée « hors profil » (P14 : réserve « seul le repli éprouvé »). Le code ordonne toujours une paire du profil avant toute paire hors profil (clés (1, score) contre (0, …)).
- Alternative : aucune dans le code v53 ; « distance au profil pondérée » demanderait une v54.
- Confiance : 0,8 (seule option ; la vraie question est de savoir si un repli doit exister, ce que le brouillon 7 tranche par oui).

**Non-vacuité au gel (garde 22a ; exigée par M9).** Jeu d'essai synthétique de 10 fiches étiquetées à la main par moi (aucune fiche réelle), les deux lecteurs supposés d'accord :

```json
{"jeu_essai_non_vacuite": {
  "e01": {"niche": "n1_detection_sequentielle", "structures": ["om_somme_cumulee_temps_arret", "me_test_sequentiel_cusum"]},
  "e02": {"niche": "n2_lecture_activations", "structures": ["om_direction_sous_espace", "om_somme_cumulee_temps_arret", "me_intervention_activations"]},
  "e03": {"niche": "n4_moniteurs_et_protocoles", "structures": ["me_moniteur_par_modele", "om_martingale_e_processus", "me_test_sequentiel_cusum"]},
  "e04": {"niche": "n6_science_evaluation", "structures": ["jd_simulateur_fige", "pr_exclusion_famille", "om_somme_cumulee_temps_arret", "me_test_sequentiel_cusum"]},
  "e05": {"niche": "n5_bornes_et_theorie", "structures": ["om_rapport_vraisemblance_divergence", "om_somme_cumulee_temps_arret", "me_preuve_formelle"]},
  "e06": {"niche": "n2_lecture_activations", "structures": ["om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis"]},
  "e07": {"niche": "n3_anomalies_hors_distribution", "structures": ["om_covariance_mahalanobis", "me_seuil_conforme"]},
  "e08": {"niche": "n4_moniteurs_et_protocoles", "structures": ["me_moniteur_par_modele", "pr_audit_budgete"]},
  "e09": {"niche": "n1_detection_sequentielle", "structures": ["me_test_sequentiel_cusum", "jd_simulateur_fige"]},
  "e10": {"niche": "n6_science_evaluation", "structures": ["jd_simulateur_fige", "pr_exclusion_famille"]}
}}
```

Résultat, calculé avec les fonctions réelles de `bisociateur_v53.py` (`valider_niche`, `indicateurs_meta`, `score_meta`, `score_repli`), selon la logique de `course2_v53._notes` : **5 paires dans le profil, 36 hors profil, 4 refusées (même niche)** ; argmax **e01–e04, score 2,0** (deux structures partagées) ; autres paires du profil à 1,5 (e01–e02, e01–e03, e03–e09, e04–e09). Témoins hors profil, chacun pour une seule raison : e01–e05 (canal fort, c = 3) ; e05–e06 (extrême, e = 5) ; e07–e08 (aucune structure partagée) ; e09–e10 (seuls un jeu de données et un protocole partagés : non comptés). Meilleur hors profil (repli) : (2 indicateurs, s = 1). Garde 24 passée ; paire de même niche refusée par `indicateurs_meta` (garde 22a, artefact). **Le profil n'est pas vide et n'est pas tout** : la condition de scellement de M9 est remplie sur ce jeu. Ce calcul est à rejouer par le contre-lecteur et à verser comme script empreinté au scellement (garde 22a).

**Prédiction P14 refaite avec ces paramètres (garde 22a ; indicative).** Hypothèses, toutes SUPPOSÉ : loi a priori des niches des fiches de défense (axes 1 à 5) n1 0,30, n2 0,25, n3 0,15, n4 0,10, n5 0,15, n6 0,05 ; accord des deux lecteurs par fiche 0,7 (cohérent avec un kappa d'environ 0,5) ou 0,9 ; probabilité qu'une paire de fiches partage au moins une structure comptée 0,15, 0,3 ou 0,5 ; indépendances. Sortie (`b2a0a325…`) :

| Fiches non aiguillées | Accord par fiche | Structure partagée | Médiane des paires dans le profil | P(zéro dans le profil) | P(aucune paire éligible : bras non produit) |
|---|---|---|---|---|---|
| 6 | 0,7 | 0,3 | 0 | 0,59 | 0,039 |
| 6 | 0,9 | 0,3 | 1 | 0,42 | 0,004 |
| 10 | 0,7 | 0,3 | 1 | 0,25 | 0,002 |
| 10 | 0,9 | 0,3 | 3 | 0,10 | 0,000 |
| 10 | 0,7 | 0,15 / 0,5 | 1 / 3 | 0,46 / 0,15 | 0,002 |

**Valeur proposée pour remplacer P14 au gel (À GELER par Lazar)** : paires dans le profil méta, **médiane 0 à 6 fiches (zéro avec 0,59), médiane 1 à 10 fiches (zéro avec 0,25)** ; croyance « hors profil » à la paire retenue : **0,45 [0,15 ; 0,75]** (au lieu de 0,3 [0,05 ; 0,6]) ; « bras non produit (aucune paire éligible) » : 0,04 à 6 fiches, 0,002 à 10. C'est plus pessimiste que le script v6 (zéro 0,31 et 0,03) pour deux raisons : le script v6 tirait la communication par paire de fiches alors qu'elle est une propriété de la paire de niches (4 paires de niches sur 15 seulement passent canal et bande), et il ignorait la règle du code qui écarte une fiche dont les lecteurs se contredisent sur la niche. **Lecture** : au pré-pilote, le bras méta éprouvera souvent son seul repli ; c'est attendu, déclaré, et ne change rien d'autre (critères du brouillon 7, « zéro paire dans le profil »). Variantes (même script, bande ou seuil changés, accord 0,7, structure 0,3) : bande [2 ; 4] → 6 paires de niches sur 15, zéro avec 0,54 (6 fiches) et 0,20 (10 fiches) ; c ≤ 2 → 10 sur 15, zéro 0,35 et 0,07, mais « faible » ne veut plus rien dire.

**Garde 22a — ce qui reste à faire avant le scellement.** Le brouillon 7 exige que « le script soit rejoué » : le script v6 ne sait pas jouer une communication par paire de niches ni la règle d'accord. Je propose qu'un script v7 du calcul de puissance reprenne la fonction ci-dessous (nom de tâche de graine nouveau, `v7-meta-profil-…`) et que sa sortie, empreintée, soit nommée dans la version contre-lue de cette annexe ; la valeur de P14 du préenregistrement est remplacée par elle au gel.

```python
# P14 indicatif, annexe du bras méta v1, brouillon 1 (SUPPOSÉ partout). numpy SeedSequence (R9).
import sys, numpy as np
N_SIM = 100_000
racine = 20261101
sys.path.insert(0, "/home/claude/controle-ia-travail/src")
from controle_ia.manifeste import cle_de_tache
def rng(nom):
    cle = cle_de_tache(nom)
    return np.random.default_rng(np.random.SeedSequence(racine, spawn_key=(cle,)))
niches = ["N1","N2","N3","N4","N5","N6"]
prior = np.array([0.30, 0.25, 0.15, 0.10, 0.15, 0.05])  # SUPPOSÉ : fiches de défense, axes 1 à 5
C = {("N1","N2"):1,("N1","N3"):2,("N1","N4"):1,("N1","N5"):3,("N1","N6"):1,("N2","N3"):2,("N2","N4"):2,("N2","N5"):0,
     ("N2","N6"):2,("N3","N4"):1,("N3","N5"):2,("N3","N6"):2,("N4","N5"):1,("N4","N6"):3,("N5","N6"):1}
E = {("N1","N2"):3,("N1","N3"):2,("N1","N4"):3,("N1","N5"):2,("N1","N6"):3,("N2","N3"):2,("N2","N4"):3,("N2","N5"):5,
     ("N2","N6"):3,("N3","N4"):3,("N3","N5"):3,("N3","N6"):3,("N4","N5"):4,("N4","N6"):2,("N5","N6"):4}
SEUIL_C, BANDE = 1, (2, 3)
prof_np = np.zeros((6,6), bool)
for (a,b),c in C.items():
    i,j = niches.index(a), niches.index(b)
    ok = c <= SEUIL_C and BANDE[0] <= E[(a,b)] <= BANDE[1]
    prof_np[i,j] = prof_np[j,i] = ok
print("paires de niches dans le profil (niches seules) :", int(prof_np.sum()//2), "sur 15")
def jouer(n, p_accord, p_struct, nom):
    g = rng(nom)
    nich = g.choice(6, size=(N_SIM, n), p=prior)
    garde = g.random((N_SIM, n)) < p_accord          # niche retenue si les deux lecteurs s'accordent (code v53, choix 10)
    iu = np.triu_indices(n, 1)
    a, b = nich[:, iu[0]], nich[:, iu[1]]
    elig = garde[:, iu[0]] & garde[:, iu[1]] & (a != b)
    struct = g.random((N_SIM, len(iu[0]))) < p_struct
    prof = elig & prof_np[a, b] & struct
    npf, nel = prof.sum(1), elig.sum(1)
    return np.median(npf), np.mean(npf == 0), np.mean(nel == 0), np.mean((npf == 0) & (nel > 0))
for n in (6, 10):
    for pa in (0.7, 0.9):
        for ps in (0.15, 0.3, 0.5):
            med, z, aucun, repli = jouer(n, pa, ps, f"annexe-b1-p14-{n}-{pa}-{ps}")
            print(f"n={n:2d} accord={pa} structure={ps}: médiane {med:.0f} ; P(zéro dans le profil) {z:.2f} ; "
                  f"P(aucune paire éligible : bras non produit) {aucun:.3f} ; P(repli joué) {repli:.2f}")
print("fin ;", sys.version.split()[0], np.__version__)
```
<<<FIN PIÈCE 13>>>

### Pièce 14 — `docs/notes/ideation-organisme-v1/contre-lecture-cl19-orchestrateur-v54-v1.md` (l. 14–22 ; 100–114 ; 149–172) — nœuds N5

Origine : branche de conv-audit ; empreinte du fichier source `f1cc6c1a974fcbe4efe4d7dfe0087333ea1103b9ad6aa0e98f9016f6d7c3f31e` ; 1590 mots ; règle 2 appliquée.

<<<DÉBUT PIÈCE 14>>>
## Verdict global

**Lançable après corrections.**

Pour la course 2 (une ou plusieurs générations) : trois corrections de code courtes (CL19-01, CL19-02, CL19-04), puis gel des seuils.
Pour le pré-pilote complet : en plus, une décision de Lazar sur la règle de non-lecture (CL19-03), les corrections CL19-05 à CL19-08, et les pièces manquantes de la section G. Le code d'analyse n'existe pas encore (déclaré).

Ce qui tient, et que j'ai vérifié moi-même : le journal de consommation est complet et rejouable sur la vraie sortie du code (CL18-01) ; le nœud arrête bien la génération et la course (CL18-02) ; la ligne de GO exige un montant exact (réserve CL19-05) ; les 56 mutations sont tuées ; la suite donne exactement les comptes annoncés ; l'annexe réelle est refusée puis la copie remplie acceptée, avec 5 / 36 / 4 et l'argmax e01–e04. Les défauts sont aux bords : ce que le code fait **après** un nœud, ce qu'il fait quand une source manque, et la voie par laquelle la clé des classes est lue.

[…]
### A21 (non-lecture) : mon avis argumenté, pour Lazar

**Texte à comparer.** A21 : incident si « lecture d'un verdict d'É6 ou d'É7, **ou ouverture de la clé des classes** ou de la clé des bras, avant la fin d'É9, par quiconque ». Ligne 30 de la table : « jusqu'à la fin d'É9, seules les consommations sont lues ; les verdicts et **les clés restent scellés** ». Le Plan, lui, demande en É5, « avant tout juge » : témoins ambigus, S20 (plus de 4 ambigus sur 23, P primaires < 8, N primaires < 10), A6, contrôles S18 et S19, A7.

**Ce que fait le code.** `_boite_e5` (`prepilote_v54.py:411-464`) lit `self._cle_classes`, copie **en mémoire** de la clé déposée au coffre (`prepilote_v54.py:302`), pour compter les ambigus, les primaires, les défauts non vus et séparer P de N (S19). Seule la décision (passe ou nœud) et des comptes sortent, déposés au coffre. En É9, `etape_e9_anteriorite` lit les strates de la clé d'antériorité (`prepilote_v54.py:564`) pour tirer 4 fiches sur 8.

**Mon avis.**
1. **Contre la lettre : oui.** « Ouverture de la clé des classes avant la fin d'É9 » est exactement ce que fait É5, et la ligne 30 dit « clés scellées ». Le coffre refuserait cette lecture (`coffre_v53.py:57-62`, incident puis arrêt) ; le code la contourne en gardant une copie en mémoire. Résultat : le journal d'accès du coffre, que la ligne 30 invoque, **ne voit pas** cette lecture, et l'essai de la ligne 30 à É0 éprouve la garde du coffre, pas la voie réellement empruntée.
2. **Le brouillon se contredit lui-même.** Tel qu'écrit, É5 (S20, A6, S19, « avant tout juge ») est impossible sans connaître la classe de chaque témoin. Appliquer A21 à la lettre rend le Plan inexécutable ; appliquer le Plan viole A21. Ce n'est donc pas un choix de code de la v54, c'est un trou du brouillon 7 que la v54 a rendu visible.
3. **Compatible avec l'intention : oui, à trois conditions.** L'intention (CP5-08) : qu'aucune décision de l'orchestrateur ne dépende d'un **résultat** (verdict d'un juge, issue d'une fusion) ni du **rattachement d'un résultat à sa classe**. Les décisions d'É5 (A6, A7) sont des gardes sur la construction des témoins, prises avant tout juge ; elles ne dépendent d'aucun verdict. L'énoncé du Plan (« les décisions de sacrifice, de reprise et d'arrêt ne dépendent que des consommations et des gardes ») les couvre. Conditions : (a) le brouillon 8 écrit l'exception (« lecture par programme de la clé des classes à É5 pour S6, S18, S19, S20, A5 à A7 ; de la clé d'antériorité à É9 pour le tirage ; sortie limitée à la décision et à des comptes ; jamais par un agent ni une personne ») ; (b) la lecture passe par une méthode du coffre qui la **journalise** (par exemple `ouvrir_pour_garde(nom, raison)`), et l'artefact de la ligne 30 couvre aussi « lecture hors journal » ; (c) la sortie de la boîte ne contient aucun détail par témoin (le code actuel écrit `primaires_non_ambigus`, une liste d'identifiants **déjà triée par classe d'appartenance** : voir ci-dessous).
4. **Mieux que l'amendement : ne pas lire.** Pour É9, la clé d'antériorité n'a pas à être lue : la liste des 4 fiches réduites (stratifiée) peut être une pièce scellée écrite par session-depot avec le tirage `pp2-reduction-e9`, ou le tirage peut être simple. Pour É5, la boîte peut être un programme tenu par session-depot, qui détient la clé et rend « passe / nœud + comptes » : l'orchestrateur n'ouvre alors jamais la clé et A21 reste vrai à la lettre.
5. **Un effet de bord à connaître.** `etape_e6_juges` appelle d'abord les témoins « primaires non ambigus » (P et N), puis les autres (C, G, ambigus) : l'**ordre des appels** dépend de la classe. Les juges ne le voient pas (sessions isolées), mais si un juge est arrêté par A3 en cours d'étape, l'ensemble des fiches qu'il a jugées dépend de la classe. Faible, mais c'est une dépendance de décision (arrêt de rôle) à la clé que A21 interdit ; l'ordre devrait être tiré (graine) ou trié par identifiant.

[retiré, règle 2 : recommandation ou confiance d'auteur]

[…]
## G. Les 12 choix pris seuls ; ce qui manque

| N° | Choix | À remonter à Lazar ? |
|---|---|---|
| 1 | Nœud : arrêt au premier « non mesuré » ; fin de phase de mesure et classement quand même | **Oui**, et le second membre est un défaut (CL19-02) : si l'on veut, au nœud, que « rien n'en ait été lu » (option O12), rien ne doit s'ouvrir. |
| 2 | A3 (appel coupé jamais lu), A11 (limite = arrêt du rôle), A14 (part cumulée sur le run) | Non pour A3 et A11 (côté prudent). **A14 à signaler** : sur de petits effectifs (adjudicateur, relecteur), un seul appel inexploitable dépasse 25 %. |
| 3 | Garde de Kimi de la course non jouée au pré-pilote ; M5 lue après É9 | Non : conforme à M5 du brouillon 7 (mesure, pas arrêt). À consigner. |
| 4 | Clé des classes lue par programme en É5 ; strates en É9 | **Oui** (A21, section C). |
| 5 | Un N dont le relecteur ne voit pas le défaut est exclu (A5, S6) | **Oui** : cela change l'ensemble des témoins et peut déclencher l'arrêt A5 (plus de 6 exclus) ; le brouillon ne dit pas que « défaut non vu » compte comme exclusion. |
| 6 | Adjudicateur de M5 joué en É7a seulement | Non : conforme à É7a. |
| 7 | I-9 : deux empreintes distinctes dans `contre_lecture` | Non, mais la forme seule ne prouve rien (CL19-09). |
| 8 | I-8 : à n = 2, aucun report au bras suivant | **Oui** : lecture littérale qui change les probabilités de C12 ; à écrire dans le brouillon 8 (l'annexe le demandait). |
| 9 | Multi-cases à n = 2 : une paire en tout, la mieux notée du bras de priorité 1 | Non (course seulement) ; à consigner. |
| 10 | Indices de forme : longueur et chiffres du texte des valeurs, nombre de champs, régression avec crête injectée | **Oui** : S18 et S19 sont des critères d'arrêt (A7) ; leur définition et la valeur de la crête doivent être gelées dans le préenregistrement, pas laissées au code. |
| 11 | Tâche `pp2-paraphrases` | Non, mais il faut déclarer aussi les tâches d'identifiants et d'anonymisation (CL19-10). |
| 12 | Une coupure dans une étape sacrifiable la retire, même jouée en partie | Non : conforme à la règle 3 d'A1 (« E retirable est retirée »). Les mesures partielles ne sont pas lues. |

**Ce qui manque encore pour lancer le pré-pilote (liste exacte).**
1. Décisions de Lazar : tous les seuils S1 à S31 ; D-e à D-j ; L1 à L7 ; les clés configurables (`budget.portee_plafond`, `garde_kimi.*`, `tableau.juger_passe_tableau`, `bisociateur.fournisseurs_entree`, `bisociateur.meta.*`, `a4.*`, `graines.prefixe`, `arrets.*`) ; les choix 1, 4, 5, 8, 10 ci-dessus ; confidentialité (envoi chez Moonshot et Google) ; mot sur DEP5 (ou acceptation du défaut R-819, M4 « non étalonné ») ; approbation des valeurs de l'annexe.
2. Corrections de code : CL19-01, CL19-02, CL19-04, CL19-05, CL19-06, CL19-07, ordre d'É6 (section C, point 5), puis nouvelle contre-lecture.
3. Pièces : analyseur de l'étage 1 (DEP3) avec cas sain et artefact ; garde de forme de M5 (ligne 9) ; résultats scellés et liés à un script empreinté pour les lignes 6, 8, 10, 17, 19 ; consignes figées au contrat de sortie des rôles (rédacteur, metteur, relecteur, second lecteur, adjudicateur, désaccord, vérificateur, table seule, paraphrase), aucune n'étant éprouvée sur moteur réel ; 8 fiches d'antériorité et leur clé, 4 fiches de M6b et leurs sources (DEP2c) ; source de S31 (bras Gu-Krenn) ; annexe du bras méta contre-lue, approuvée, scellée (après les verdicts des collisionneurs, DEP10) ou geler à deux bras (D-h b) ; script de puissance refait avec I-11 et I-13 ; confirmation de DEP4 par session-depot ; ligne de GO au plafond S17 exact (DEP6) ; devis refait avec les lectures de désaccord et les valeurs de `budget.etapes`.
4. Code d'analyse (n'existe pas) : intervalles, t* sur la partition, M3, M5 (union, intersection, adjudication), M6, verdict par instrument, complément.
5. Manifeste de run : le commit n'est pas lu (arbre hors dépôt) ; à porter au registre.
<<<FIN PIÈCE 14>>>

### Pièce 15 — `docs/notes/ideation-organisme-v1/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md` (l. 65–105) — nœuds N5

Origine : branche de conv-audit ; empreinte du fichier source `bbfdcb3c30d174dd7feeee9ba8dd20aeb7777c5f0e65aeb087e3c4388c743aa3` ; 644 mots ; règle 2 appliquée.

<<<DÉBUT PIÈCE 15>>>
## Décisions ouvertes pour Lazar

### CL19-03 — A21 et la ligne 30 face au Plan d'É5 (la question de fond)

Le brouillon 7 se contredit : A21 interdit « l'ouverture de la clé des classes […] avant la fin d'É9, par quiconque » et la
ligne 30 dit « les clés restent scellées » ; le Plan exige en É5, « avant tout juge », S6 (défaut vu), S20/A6 et S18/S19/A7,
impossibles sans la classe de chaque témoin (et l'exemption A8 de la classe G en É3). La v55 rend la lecture **visible et
bornée** (journal du coffre, rôle déclaré, raison, comptes seulement, aucune copie) mais ne la supprime pas.

- **Lecture 1 — amender A21 et la ligne 30 (brouillon 8)** : « lecture par programme de la clé des classes à É3 (A8) et à É5
  (S6, S18, S19, S20, A5 à A7), journalisée au coffre, sortie limitée à la décision et à des comptes ; jamais par un agent ni
  une personne » ; l'artefact de la ligne 30 couvre « lecture hors journal ». C'est ce que fait la v55 (défaut de CL19).
  Avantage : rien à construire. Inconvénient : A21 n'est plus vrai à la lettre ; l'aveugle repose sur le code.
- **Lecture 2 — ne jamais livrer la clé à l'orchestrateur** : la boîte d'É5 (et l'exemption A8) devient un programme tenu
  par session-depot, qui détient la clé et rend « passe / nœud + comptes » ; A21 reste vrai à la lettre. Avantage : aucune
  exception. Inconvénient : une pièce de plus, une interface de plus, à éprouver (cas sain, artefact).
[retiré, règle 2 : recommandation ou confiance d'auteur]
  ici. Défaut de CL19 si aucune réponse : comportement de la v55 (journalisé).

### Choix de CL19, section G, à trancher

| n° | choix (v54, inchangé en v55 sauf mention) | enjeu |
|---|---|---|
| 1 | Nœud : arrêt au premier « non mesuré ». **Second membre corrigé** : plus de fin de phase de mesure ni de classement au nœud (CL19-02, lecture O12 « rien n'en a été lu ») | confirmer que le nœud ne produit aucune lecture, et que le rejeu O12 se fait sur GO |
| 4 | Clé des classes lue par programme (É3, É5) — voir CL19-03 ; **É9 ne lit plus la clé d'antériorité** (liste scellée de session-depot) | A21 ; qui écrit la liste d'É9 (session-depot, tâche `pp2-reduction-e9`) |
| 5 | Un N dont le relecteur ne voit pas le défaut est **exclu** (compte pour A5) | change l'ensemble des témoins ; le brouillon ne dit pas que « défaut non vu » est une exclusion |
| 8 | I-8 : à n = 2, aucun report au bras suivant | change les probabilités de C12 ; à écrire au brouillon 8 |
| 10 | Indices de forme (longueur, chiffres, nombre de champs) et crête injectée | S18/S19 sont des critères d'arrêt (A7) : définition et crête à geler au préenregistrement |

### Autres points qui demandent un mot de Lazar (nouveaux ou signalés par CL19)

[retiré, règle 2 : recommandation ou confiance d'auteur]
  valeur à geler (les essais utilisent 0).
- **DEP4, phrase de confirmation** (`dependances.dep4_phrase`) : texte à fixer avec session-depot.
- **I-2** : désaccord lu sur au plus `paires_max` paires (le brouillon dit « chaque paire candidate », CA1-10).
- **A14 sur petits effectifs** (choix 2, signalé par CL19) : un seul appel inexploitable de l'adjudicateur ou du relecteur
  peut dépasser 25 %.
- **Relecteur sans sortie** (pris seul en v55, ci-dessous) : « non relu (technique) », hors A5 ; A14 garde la part technique.
- I-11 (paires déjà prises retirées, non chiffré par P14) et I-13 (dépense du désaccord absente du devis) : à l'annexe v2 ou
  au script de puissance ; non traités, non revendiqués.
<<<FIN PIÈCE 15>>>

### Pièce 16 — `docs/notes/ideation-organisme-v1/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md` (l. 95–120) — nœuds N5

Origine : branche de conv-audit ; empreinte du fichier source `a3290bc7237057af11dd8a320d631b73293ffb41e55aef65e11f0b90ff79beb2` ; 434 mots ; fin portée de 116 à 120 : choix 10 à 12 (le choix 10, indices de forme, est cité par N5).

<<<DÉBUT PIÈCE 16>>>
## Choix de code

Remontés à Lazar, **configurables** (« À REMPLIR » refusé) : choix 1 `budget.portee_plafond` ; choix 6
`garde_kimi.refus_aiguilleur` ; choix 7 `garde_kimi.arret_metteur_fusion` ; choix 10 `bisociateur.meta.regle_divergence` et
`.structures` ; choix 11 `tableau.juger_passe_tableau` ; CL18-08 a `bisociateur.fournisseurs_entree` ; CL18-06 `a4.mode`,
`a4.action` ; CL18-07 `graines.prefixe` ; I-2 `bisociateur.meta.desaccord` ; I-3 `.s28` ; I-4 `.definitions` ; A3, A11, A14
`arrets.*` (les valeurs du brouillon — 3 échecs, 300 s et 1 800 s, 25 % — sont des valeurs de configuration, jamais du code).

Pris seuls (à confirmer) :
1. Nœud : la génération (et le pré-pilote) s'arrêtent au premier « non mesuré » ; les étapes suivantes ne sont pas lancées ;
   la fin de la phase de mesure et le classement sont faits quand même (0 USD).
2. A3 : un appel au-delà de son délai n'est jamais lu, même s'il a rendu un texte. A11 : la « limite hebdomadaire » arrête le
   rôle en attente (aucune attente réelle, aucune bascule). A14 : part cumulée sur le run, lue à la fin de chaque étape, pour
   les rôles appelés dans l'étape.
3. Pré-pilote : la garde de Kimi de la course (arrêt au-dessus de S12) n'est pas jouée ; M5 est une mesure lue après É9.
4. É5 lit la clé des classes **par programme** (ambigus, S19, défaut vu) ; seules la décision et des comptes en sortent (coffre).
   É9 réduite lit les strates de la clé d'antériorité par programme pour le tirage stratifié. À trancher par Lazar (A21).
5. É5 : un N dont le relecteur ne voit pas le défaut est exclu (A5, S6) ; pas de nouveau rendu à ce stade.
6. Adjudicateur de M5 : joué en É7a seulement ; si É7a est retirée ou L1 = « retirée », M5 se lit sur l'union et l'intersection.
7. I-9 : deux empreintes distinctes exigées dans `contre_lecture` (brouillon relu et rapport, annexe § 9.5).
8. I-8 : à n = 2, aucun report au bras suivant (lecture littérale du brouillon ; remplace le choix 9 de la v53).
9. Multi-cases à n_max = 2 (course) : une seule paire en tout, la mieux notée du bras de priorité 1.
10. Indices de forme : longueur et chiffres sur le texte des valeurs de la fiche ; nombre de champs = champs du contenu ;
    régression avec pénalité de crête injectée (`controles_forme.ridge`).
11. Paraphrases d'É8 choisies par la tâche `pp2-paraphrases` (absente de la liste du brouillon 7 : écart déclaré).
12. Une « coupure » rencontrée dans une étape sacrifiable la retire (même si une partie a été jouée).
<<<FIN PIÈCE 16>>>

### Pièce 17 — `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon3.md` (l. 9–101 ; 166–176 ; 359–393 ; 687–698) — nœuds N6

Origine : branche de conv-audit ; empreinte du fichier source `1a229998fcbe7cd8dc45abeb559508ae8411f309059912c365bc02ae3b92e67c` ; 4919 mots ; fin portée de 394 à 393 : la l. 394 est un titre hors pièce ; règle 2 appliquée.

<<<DÉBUT PIÈCE 17>>>
## Résumé de dix lignes pour Lazar

1. **Ce que l'épreuve mesure (inchangé).** Vraies métadonnées d'OpenAlex ; on y **plante une cause connue** C (« contact » entre deux niches qui ajoute des œuvres-ponts deux ans plus tard) et l'on regarde si chaque méthode retrouve C au milieu du vrai bruit, sans jamais prétendre connaître les vraies causes.
2. **Pièges plantés** : facteur caché H, leurre L (collisionneur entre C et H), jumeau sans effet C⁰, et condition R2⁻ où le contact **retire** des œuvres-ponts. R2⁻ teste la **symétrie de signe des méthodes**, pas l'hypothèse de Borjas et Doran (CS2-09) ; la prédiction de signe à deux branches est renvoyée entière à la gradation 2, avec une réfutation symétrique.
3. **Volet A** : témoins (popularité, prédicteur associatif, tri par variance avec critère d'information bayésien), prédiction causale invariante, PCMCI, DirectLiNGAM. **Le témoin T2b du brouillon 2 était vrai par construction** (CS2-10) : il est soit redéfini sur la règle publiée d'orientation de chaîne (Reisach, PDF p. 9, vérifié), limitée aux conditions où une chaîne plantée existe, soit retiré (DL-9).
4. **Volet B-θ** (dans les hypothèses de Khemakhem 2020) : le théorème 1 ne garantit l'identification qu'**à transformation linéaire près** ; la réduction à une permutation (théorème 2) exige un mélange qui « a toutes ses dérivées secondes croisées » (PDF p. 6, vérifié). Le mélange de B-θ passe donc à une **activation lisse et injective** (« softplus à fuite ») ; une mesure au niveau garanti par le théorème 1 est ajoutée en mention (CS2-06).
5. **Variable auxiliaire u** : échelle de trois définitions écrite d'avance, la première qui atteint 22 valeurs est prise ; aucune lecture avant scellement, aucun choix après (CS2-08, DL-8) ; la base minimale de S13 passe par la deuxième définition (36 valeurs, M § 15).
6. **Étape d'effet du volet B** : moitiés coupées **par paire**, erreurs groupées par paire, graine choisie sans la vérité ; l'effet devient une table séparée à règle de Wilson (le seuil de 90 % contredisait la prédiction, CS2-11 à CS2-13) ; en B-hors, l'étape d'effet est descriptive.
7. **Symétrie et gardes** : déclencheur d'audit « trop mauvais » pour M4 en B-θ (CS2-14) ; chaque ligne de la liste d'arrêt a sa garde testée sur un cas sain et sur un artefact ; la garde de fausse détection passe à une borne binomiale exacte (fausse alarme 0,0069, M § 17).
8. **Budget** : ≈ 107 heures de calcul, ≈ 111 heures avec validation et gardes (M § 18) ; 140 heures = 5,8 jours de temps mural, à placer avant la porte G0 (fin novembre 2026). [retiré, règle 2 : recommandation ou confiance d'auteur]
9. **Ce qu'elle n'autorise pas (inchangé)** : aucune affirmation sur les vraies causes de la fertilité ; seulement l'entrée (ou non) de chaque méthode dans les gradations 2 et 3.
10. **Pour geler** : seuils S1 à S21 (numérotation stable, états corrigés) ; **neuf décisions DL-1 à DL-9** (« DL » = décision de Lazar, pour ne plus confondre avec les conditions descriptives D1 à D4) ; aucune ne prend de défaut.

### Décisions à soumettre à Lazar (DL-1 à DL-9)

Format : décision en une phrase ; enjeu ; options (avantage, inconvénient) ; [retiré, règle 2 : recommandation ou confiance d'auteur]

- **DL-1 — Quel volet B décide ?**
  - Enjeu : le volet B du brouillon 1 viole les hypothèses (ii) à (iv) du théorème 1 de Khemakhem et collègues (fiche § 3, p. 5 ; corrigendum p. 9) ; tel quel, son verdict « oui sous hypothèse » serait faux par construction.
  - Option 1 — B-hors seul, réécrit comme test de robustesse. Avantage : coût le plus bas (≈ 87 heures de calcul à 5 graines, M § 12). Inconvénient : l'iVAE n'est jamais testé là où son théorème s'applique ; un échec ne dit rien de l'hypothèse.
  - Option 2 — B-θ décide (dans le théorème, activation lisse), B-hors en descriptif à 30 mondes par condition. Avantage : sépare « échec en échantillon fini dans le théorème » de « fragilité hors théorème ». Inconvénient : indicateurs entièrement synthétiques dans B-θ (le réel n'entre que par la sortie et la structure de u) ; ≈ 107 heures (M § 12).
  - Option 3 — B-θ seul. Avantage : coût voisin de l'option 1 (≈ 87 heures par recoupement : 200 mondes × 2 méthodes × 5 graines). Inconvénient : on perd la seule mesure de robustesse sur données réelles.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-2 — Combien de graines par réseau et quel budget de temps (S18, S15) ?**
  - Enjeu : la stabilité entre graines est bruitée (Locatello et collègues : 50 graines par configuration, fiche § 2, p. 4) ; les temps unitaires sont SUPPOSÉS et S15 = 110 heures ne laissait que 2,6 % de marge sur le calcul de base (M § 18).
  - Option 1 — 3 graines, S15 = 110 heures. Avantage : ≈ 86 heures de calcul (M § 12), marge réelle. Inconvénient : 3 paires de graines seulement pour la stabilité (M § 13), médiane fragile.
  - Option 2 — 5 graines, S15 = 140 heures. Avantage : 10 paires de graines ; ≈ 111 heures avec validation et gardes, tolère des temps unitaires 1,26 fois plus longs sans réduction et 1,57 fois après réduction complète (M § 18). Inconvénient : 5,8 jours de temps mural (M § 18), à placer avant la porte G0.
  - Option 3 — 5 graines, S15 = 110 heures, la réduction chiffrée servant de marge. Avantage : calendrier plus court. Inconvénient : aucune marge avant réduction (multiplicateur toléré 0,99) ; 1,24 après réduction complète (M § 18) ; au-delà, arrêt avant les mondes de décision.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-3 — La condition à effet négatif R2⁻ décide-t-elle (S20) ?**
  - Enjeu : sans elle, l'épreuve ne plante que des effets positifs ; avec elle, elle teste la symétrie de signe des méthodes (non l'hypothèse de Borjas et Doran) et la puissance en R2⁻ n'est pas celle de R2 (fond ajouté à 90 % des paires-années, CS2-09).
  - Option 1 — condition de décision, ligne 7bis de la Table A. Avantage : une méthode qui ne détecte qu'un signe est attrapée (0,85 partout et 0,75 en R2⁻ : conjonction tenue avec 0,180, M § 9). Inconvénient : 100 mondes de plus ; la conjonction de recouvrement passe de 0,852 à 0,818 pour un recouvrement vrai de 0,85 (M § 9) ; un échec en R2⁻ peut venir de la puissance, non d'un signe imposé.
  - Option 2 — condition descriptive. Avantage : ne durcit pas la qualification. Inconvénient : un défaut de signe ne coûte rien.
  - Option 3 — rien. Avantage : coût nul. Inconvénient : le banc présuppose un seul signe.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-4 — CITRIS entre-t-il dans la gradation 1 ?**
  - Enjeu : CITRIS exige des cibles d'intervention observées à chaque pas (fiche § 4, p. 3).
  - Option 1 — hors de la gradation 1, candidate de la gradation 3. Avantage : aucune méthode ne reçoit une information que les autres n'ont pas. Inconvénient : aucune donnée sur CITRIS avant la gradation 3.
  - Option 2 — variante où C est donné comme cible connue. Avantage : CITRIS entre dans l'épreuve. Inconvénient : on lui donne ce qui fait l'identification (quand et sur quoi l'on intervient) ; l'agrégation annuelle viole probablement l'hypothèse « sans effet instantané » (fiche § 4, p. 2 ; violation SUPPOSÉE).
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-5 — Comment l'étape d'effet du volet B est-elle faite et lue (S21, S11) ?**
  - Enjeu : choisir le facteur par sa relation à la sortie est une supervision (fiche § 2, portée (b)) ; le brouillon 2 coupait par paire-année (fuite par la persistance des paires), choisissait la graine avec la vérité et exigeait 90 % de réussite, contre sa propre prédiction centrée sous 90 % (CS2-11 à CS2-13).
  - Option 1 — sélection sur une moitié des **paires** tenues à l'écart, test sur l'autre moitié avec erreurs groupées par paire, graine choisie par sa perte sur E₁ (sans vérité), effet lu dans une **table séparée** à règle de Wilson (au moins 37 mondes sur 50, au plus 2 fausses détections sur 50, M § 16), étape d'effet descriptive en B-hors. Avantage : praticable, fuite fermée, prédiction et seuil cohérents, la question d'identification n'est plus masquée par l'effet. Inconvénient : moins de puissance ; le signe reste évalué avec la vérité (reste d'oracle assumé dans l'évaluation).
  - Option 2 — oracle (facteur donné par la vérité) en décision. Avantage : puissance. Inconvénient : ne correspond à aucun usage réel.
  - Option 3 — garder la règle de 90 % comme ligne bloquante de la table d'identification. Avantage : exigeant. Inconvénient : contredit la prédiction de l'auteur et fait de l'effet le verdict probable à la place de l'identification.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-6 — Faut-il obtenir les PDF manquants avant le gel ?**
  - Enjeu : PCMCI, la prédiction invariante, LiNGAM et la sortabilité par le coefficient de détermination portent des lignes de prédiction et S8 sans vérification sur PDF.
  - Option 1 — obtenir Runge et collègues 2019, Peters, Bühlmann et Meinshausen 2016, Reisach et collègues 2023, Shimizu et collègues 2006 et 2011, et en faire des fiches vérifiées avant le gel. Avantage : les SUPPOSÉ sur M1, M2, M3 et T2b sont soldés. Inconvénient : délai ; l'obtention passe par Lazar (aucun réseau ici).
  - Option 2 — geler avec les marques SUPPOSÉ (aucun chiffre de ces papiers n'est utilisé). Avantage : aucun délai. Inconvénient : les hypothèses écrites de quatre méthodes restent de mémoire.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-7 — Comment geler S1 à S21 ?**
  - Enjeu : trois seuils restent des choix vraiment ouverts (S3 tailles d'effet, S8 plafond, S9 exigence de recouvrement), chacun avec une autre option écrite.
Avantage : rapide. Inconvénient : les trois choix ouverts ne sont pas arbitrés explicitement. [retiré, règle 2 : recommandation ou confiance d'auteur]
  - Option 2 — geler en arbitrant explicitement S3, S8, S9, le reste en bloc. Avantage : choix conscients là où ils comptent. Inconvénient : un peu plus long. [retiré, règle 2 : recommandation ou confiance d'auteur]
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-8 — Comment fixer la variable auxiliaire u de B-θ sans lire la moisson (S19, S13) ?**
  - Enjeu : compter les valeurs de u sur la moisson avant scellement serait une lecture de métadonnées au sens de la règle que ce texte se donne ; une seule définition rigide rendait B-θ non exécutable sur la base minimale (21 < 22, M § 10).
  - Option 1 — échelle de trois définitions écrite d'avance (u₁ = environnement × année après la référence ; u₂ = environnement × année du panel entier ; u₃ = u₂ × moitié de paires), la première qui atteint S19 est prise, vérifiée par booléens à la validation de la base ; aucune → B-θ non exécutée. Avantage : aucune lecture avant scellement, aucun choix après ; la base minimale passe (u₂ = 36, M § 15). Inconvénient : u₂ et u₃ s'éloignent de « environnement × temps après la référence » (u₃ découpe les paires par un critère sans sens).
  - Option 2 — u₁ seule, B-θ non exécutée sous 22 valeurs. Avantage : une seule définition. Inconvénient : non exécutable sur la base minimale (21, M § 15).
  - Option 3 — compter sur la liste des environnements et des années du manifeste avant scellement. Avantage : définition choisie en connaissance. Inconvénient : Lazar doit dire si c'est une lecture au sens de R1 ; choix discrétionnaire possible.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- **DL-9 — Que devient le témoin T2b (S17) ?**
  - Enjeu : T2b du brouillon 2 (tri par coefficient de détermination) est vrai par construction (ce coefficient ne dépend pas de l'échelle) et, en affectation au hasard, se réduit à une régression naïve sur C ; son déclencheur S14 (h) aurait sonné presque sûrement sans issue possible (CS2-10).
  - Option 1 — redéfinir T2b sur la **règle d'orientation de chaîne** de Reisach (corrélations successives croissantes le long de l'ordre causal, PDF p. 9, § 5.1, vérifié), appliquée seulement aux deux chaînes plantées entre variables observées des conditions O (S → C → sortie, D → C → sortie), comparée au jumeau C⁰ comme nul ; règle unique : si le motif est présent et que T2b égale la méthode à 0,05 près en O2 et O3, la méthode perd sa qualification sous confusion observée (Table A, ligne 10). Avantage : mesure le motif là où il peut exister ; une conséquence, cohérente avec S12 (domination → perte de qualification là où l'artefact opère). Inconvénient : seuils 0,20 et 0,05 choisis par l'auteur sans littérature (le critère de 2023 est SUPPOSÉ) ; peut retirer la qualification O à une méthode juste.
  - Option 2 — retirer T2b de la décision : la même mesure reste descriptive, et « Ce que l'épreuve n'autorise pas » écrit que le verdict ne contrôle pas ce motif. Avantage : aucune règle à seuil non sourcé. Inconvénient : une méthode qualifiée sous O peut devoir sa réussite au motif sans que le verdict le dise.
[retiré, règle 2 : recommandation ou confiance d'auteur]

### Nœuds ouverts avant scellement

1. **Verdict du collisionneur sur la question 6** (pièce n° 264) : attendu (tours coupés cette nuit) ; section « À intégrer… » réservée.
2. **Manifeste de la moisson** (session-depot, n° 265) : cité par chemin et empreinte au scellement ; son contenu chiffré n'est pas lu avant. La question « compter les valeurs de u est-il une lecture ? » est dissoute par DL-8 (option 1) : aucun compte avant scellement.
3. **Décisions DL-1 à DL-9.**
4. **PDF manquants** (DL-6).
5. **Lectures à confirmer restantes** (à solder avant le gel, ou à garder comme réserves écrites) : (a) type de corrélation du coefficient moyen de Khemakhem (PDF p. 7, vérifié : « correlation coefficients » sans précision) — notre choix (rangs de Spearman) est écrit comme choix ; (b) invariance d'échelle de DirectLiNGAM démontrée ou seulement attendue (fiche § 1, p. 6, « ne devraient pas dépendre ») ; (c) délais de Campos et d'Iaria (fiche § 8 et § 9) ; (d) la condition (2.ii) « has all second order cross derivatives » (PDF p. 6, vérifié) se lit comme l'**existence** des dérivées secondes croisées ; si elle exigeait aussi qu'elles soient non nulles, des poids orthogonaux denses le donnent génériquement (SUPPOSÉ) ; (e) la preuve du théorème 2 dérive deux fois v = f̃⁻¹ ∘ f (PDF p. 15, éq. 36 à 38, vérifié) : le décodeur appris doit donc être lui aussi deux fois dérivable, d'où des activations lisses dans M4 et M5 ; son injectivité n'est pas garantie par l'architecture (SUPPOSÉ sans conséquence connue).
6. **Bibliothèques** (routine) : `tigramite` (PCMCI), `lingam` (DirectLiNGAM et ICA-LiNGAM), `scikit-learn` (témoins ; `LassoLarsIC` pour le critère d'information bayésien), `scipy` (appariement par affectation linéaire), `statsmodels` (erreurs types groupées par paire), torch ; versions figées au manifeste.

- Auteur : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), canal `canal/conv-audit-n04` ; n'a écrit ni le brouillon 1, ni le brouillon 2, ni les fiches de lecture, ni l'erratum, ni la contre-lecture CS2, ni la réponse 6. **Ne peut pas être contre-lecteur** de ce texte ni de ses versions suivantes. Les brouillons 1, 2 et 3 sont tous d'Opus 5.5 : la contre-lecture finale se fait par un modèle différent.
- Date (UTC), relevé `date -u` : début 2026-10-31T01:58Z ; fin, voir l'empreinte compagnon (à écrire par l'orchestrateur, pas par l'auteur).
- Commit du code d'analyse : aucun code ; le code s'écrit **après** scellement (R9).
- Non lus : tout `donnees/` ; la moisson ; les pièces du collisionneur (question 6, réponses, relectures : empreintes seulement, reprises du brouillon 2) ; aucune commande git, aucun réseau, aucune dépense ; seul programme lancé : le script de règles, par `python3 -I`.
- PDF ouverts à la page par l'auteur (empreintes conformes à leurs compagnons, `sha256sum -c`) : Khemakhem `ea4bc2b1bf46b94b0f7fa7121b3de51f691c8386e0d0844f5f5c50ef31677629` (p. 5, 6, 7, 15, 16, 17) ; Iaria `6d32d421de40452959ca77cd660665e44bc8e3c9792351ca7dcf2ac595489a89` (p. 22, 23) ; Azoulay `911c058a52b69eaf3fc3d8a83df7e22e7e6ee2ec555b3b4c90184f2e5a693354` (p. 17, 28) ; Campos `94d1c0ecc622380f42f4311653e08f71b6372a8dd3163b23e22d1006bc660d50` (p. 11) ; Reisach `04aa0fc7d67449cc584c7c89845445f0b7b4fd90a21406594400b27e983c44e5` (p. 9). Les autres pages citées le sont d'après la fiche (vérifiée sur page par son auteur, et pour sept PDF par la contre-lecture CS2).
- Documents qui font foi (empreintes SHA-256 calculées par l'auteur le 2026-10-31 vers 02:00 UTC ; « pièces » = chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-niches-v1/`) :
  - brouillon 2 `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon2.md` `f61ae4c01d51b05007b58103e22b5b9c5219c9da98b72d2c7eef135f7388c5b2` (base, lu en entier), son script `…-brouillon2.py` `eb9d429d3e02c0e843941efed87efa233b05b62f43f141aaee784038a59ba05d` et sa sortie `…-brouillon2.sortie.txt` `35aa0d02445387bdbf7ed24d6d20468574a17104dc281bd43b63381b7f053a51` ;
  - brouillon 1 `…-brouillon1.md` `d8ae28dc66888793886bc202ad47f7081c2033244b4bdfbce14cbbd664121516` (lu pour les sections reprises en entier : Hypothèse, Métrique, Seuil, Plan d'analyse, Critères, Liste d'arrêt), son script `474a45d984d56f53482c8e36018bf58eca518762d52b94890ae5dcf62f150358` et sa sortie `eb3922a0736216f16f70d50ada1153c9399d84571a2d9bea479951b5f41942a9` ;
  - contre-lecture CS2 `prereg/brouillons/contre-lecture-identification-semi-reel-v1-brouillon2.md` `a539dc13e6790b68dd1c091aa7a70f8cdd55cbdd189083045ad2fe193a5b33d1` (lue en entier ; liste de travail) ;
  - fiches de lecture vérifiées `63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79` (en-tête et § 1 à § 3 lus ; § 4 à § 9 cités d'après le brouillon 2 et contrôlés par la contre-lecture) ; erratum `fa7e1d96f40e197f3fd761afd84601ac060cddfc98ea95c2d8f34de85e4f703f` (conforme à son compagnon) ;
  - `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`, `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (lus) ;
  - `registres/decisions.md` (fichier vivant, `877b87291751b2fcce8fd5e4bf95020938841ab46641b4b4f900f925378208cf` à la lecture) : R-631, R-633 (gradation 1 : « semi-réel (OpenAlex + cause plantée), processeur, sans dépense » ; scellement avant toute lecture, après le verdict du collisionneur), R-650 (fiches), R-653 (brouillon 2), R-664 (contre-lecture CS2, erratum) ;
  - pièces (empreintes reprises du brouillon 2, **non relues**) : `question-6-identification-collisionneur-v1.md` `14966d0d2ffdea9de94b924a6ad661b440eae1bb2db865b81fd0eb75e6d71b73`, `reponse-conv-audit-question-6-v1.md` `afdb9f9dbf9ed8a837d20962eb815e4eea817454dc296440a743123769ef00bf`, `relecture-fable-reponse-6-v1.md` `bedb1f4c674ef70264e5c3bd19036f2ef6f18da9c098797d24c7be8b5da6c26e` (RL6-01 à RL6-09), `reponse-fable-independante-questions-6-7-v1.md` `052a37e765afc6aaa8a14afcb3ac3803994046457b361542cff1dd3b067cd65e` ; et, reprises du brouillon 1 (non relues) : `reponse-conv-audit-question-5-v1.md` `a47ba91677ee9f3138e65c2fae7f997436ca80e2ad8a73454609ba8e58ae0442`, `reponse-fable-independante-question-5-v1.md` `9170d230aca80767b6ba0e3b55814f9e1cce0544a3c76e6fceb79b48cd409148`, `relecture-fable-reponse-5-v1.md` `77a48dd23c772992cc48fd9cc7c6032336ddd04a09549cfd5638f73b6bd0cb3a`, `reponse-conv-audit-question-3-v1.md` `c7ca393513ed1ffd443f622f8ee8eb64d7766cbc34a177c3a64d61b3f80f4f47`, `reponse-conv-audit-question-4-v1.md` `69ca070747e5a3a7fb64935d32e631fb45fe1aafd5e0ef82376df0b0e90db927`, `question-2-niches-v1.md` `4378f9a8abea025d473c4315419515a82c12a238f349bad51b6c08e80c631c14`, `question-3-fertilite-v1.md` `2ad43f6972951abb90ae49447fd887d5f65d3dacb552ca7454ca2c0c5027b06a`, `question-4-apprendre-v1.md` `d051c7bdce39c809465b6d227ca1869eff3afc38f1594c0a8ad6be041113be09`, `question-5-causes-v1.md` `8dfc74a332de814764aab1fd25e7a92791c51addcd4ae0a357e5d1cdb8354ee7`, `docs/programme-controle-ia-v2.md` `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` (E1.4), `prereg/preenregistrement-bisociation-deux-espaces-v2.md` `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` (modèle de forme) ;
  - script `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon3.py` `649e13a0e0c5c30a4cc1bab4c61950782696f8fb2689bd9508023e71508c27d9` et sortie `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon3.sortie.txt` `a668a8e1fdcb0dc02400fbcf36ed29f5762144d84ce0b9e3d9d69803bad043a3` (lancé par `python3 -I` ; paragraphes 1 à 14 identiques au bit près à la sortie du brouillon 2, vérifié par `diff` ; deux exécutions donnent la même empreinte ; **source des grandeurs marquées (M § k)**).
- Références de littérature : les neuf papiers des fiches sont cités **par fiche et page** (et erratum pour Iaria et Azoulay) ; tous les autres sont **SUPPOSÉS** (section Hypothèse, « Références non couvertes »).

[…]
### Hypothèses rivales gelées, méthode par méthode

| Code | Méthode | Hypothèse d'identification | Satisfaite par la plantation ? | Rivale gelée |
|---|---|---|---|---|
| T0 | Popularité seule : régression de Poisson pénalisée et réseau à deux couches, entrées S, D, A, g(Y) | aucune (prédiction pure) | sans objet : C n'est pas une entrée | **HR-T0** : ne retrouve jamais C ; prédit un effet d'intervention nul ; plancher et contrôle de plomberie |
| T1 | Prédicteur associatif : forêt d'arbres par gradient, toutes les candidates, importance par permutation | aucune (association) | sans objet | **HR-T1** : retrouve C, **retient aussi L** (sous R, O et H) et C⁰ sous H ; effet estimé biaisé (collisionneur L ; confusion H) |
| T2 | Tri par variance puis lasso **sélectionné par critère d'information bayésien** (« sortnregress », fiche § 1, p. 7, énoncé 5) | l'ordre causal suit l'ordre des variances ; résultat d'identifiabilité seulement si v = 1, en modèle linéaire à bruit additif acyclique, sans confondeur caché (fiche § 1, p. 3 et p. 5) | non (artefact connu) | **HR-T2** : témoin ; réussit en échelle brute si l'ordre des variances suit l'ordre causal ; au hasard en échelle standardisée, où v = 1/2 (fiche § 1, p. 8, énoncé 6) |
| T2b | **Si DL-9 = option 1** : règle d'orientation de chaîne (Reisach, fiche § 1, p. 9, énoncé 9 ; PDF p. 9, § 5.1, vérifié : la direction où les corrélations successives croissent est prédite causale), appliquée aux chaînes plantées S → C → g(Y⁺) et D → C → g(Y⁺) des conditions O seulement. **Si option 2** : mesure descriptive identique, sans rôle de témoin | orientation par corrélations croissantes le long de l'ordre causal, motif qui survit à la standardisation (fiche § 1, p. 9) | non (artefact) | **HR-T2b** : oriente les chaînes plantées au-dessus de ce qu'il fait sur le jumeau C⁰ quand β est moyen ou fort. N'est **pas** calculé en R (aucune chaîne observée de longueur 2 : C y est exogène, la règle se réduirait à une comparaison naïve, CS2-10) ni en H (la chaîne passe par H, caché) |
| M1 | Prédiction causale invariante, version linéaire (Peters, Bühlmann et Meinshausen 2016 : **SUPPOSÉ**) | invariance de la loi de la sortie sachant ses vraies causes entre environnements ; pas de facteur caché entre candidates et sortie (SUPPOSÉ) ; emploi des environnements sous NT1 | partiellement : effet planté invariant, affectation de C variable entre environnements ; vrai bruit peut-être non invariant ; H viole l'hypothèse sous l'affectation H | **HR-M1** : n'inclut presque jamais L ni C⁰ (garantie de niveau) ; retrouve C seulement si la partie réelle est assez invariante ; **s'abstient** sous confusion cachée |
| M2 | PCMCI (Runge et collègues 2019 : **SUPPOSÉ**) : sélection des conditions puis test d'indépendance conditionnelle momentanée, corrélation partielle, retards 1 à τ_max | suffisance causale, stationnarité, fidélité, ordre temporel (SUPPOSÉ) | ordre temporel oui ; suffisance causale non (H) ; stationnarité douteuse | **HR-M2** : retrouve C au bon retard ; **déclare L → sortie** (dépendance résiduelle par H) ; déclare C⁰ sous H |
| M3 | **DirectLiNGAM** (Shimizu et collègues 2011 : SUPPOSÉ quant à la référence ; nommé dans Reisach, fiche § 1, p. 6) | linéarité, bruits non gaussiens indépendants, acyclicité, aucun facteur caché (SUPPOSÉ) ; **ne devrait pas dépendre de l'échelle** (fiche § 1, p. 6, § 3.4 ; LECTURE À CONFIRMER : démontré ou attendu) | non-gaussianité oui ; linéarité non ; aucun facteur caché : non | **HR-M3** : oriente C → sortie avec le bon signe sous R et O ; **retient L** et, sous H, C⁰ ; **ART(M3) prédit vrai** (invariance d'échelle) |
[…]
**S15 — Budget de processeur** (**mis à jour** : CS2-16 ; DL-2)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : aucune dépense ; le coût est du temps de calendrier avant la porte G0 (fin novembre 2026) : 140 heures = 5,8 jours continus (M § 18). S15 = 110 h (brouillon 2) ne laissait que 2,6 % de marge sur le seul calcul de base et ne comptait ni validation ni relances (M § 18).

**S16 — Ensemble d'intervention** (étendu à R2⁻)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : sous O et H, ces paires ne recevaient presque jamais de contact : la prédiction est une **extrapolation**, ce qui sépare l'identification de l'association ; sous R, ce n'en est pas une (contrôle).

**S17 — Motif d'orientation de chaîne que la standardisation n'efface pas** (**mis à jour** : CS2-10 ; DL-9)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : la règle publiée oriente une chaîne au-dessus du hasard en échelles brute, standardisée et harmonisée (fiche § 1, p. 9, énoncé 9 ; PDF p. 9, § 5.1, vérifié) ; chez nous, la seule chaîne plantée entre variables observées est popularité → contact → sortie, dans les conditions O ; la conséquence est donc limitée à la qualification sous confusion observée, là où l'artefact peut opérer, comme S12 retire la qualification là où l'ordre des variances opère (cohérence S12 / S17 : domination constatée → perte de qualification, une seule règle chacun). Le jumeau C⁰ (même affectation, aucun effet) sert de nul. Seuils 0,20 et 0,05 : choix de l'auteur, sans chiffre de littérature (le critère publié de 2023 est SUPPOSÉ, DL-6).

**S18 — Graines d'entraînement du volet B** (nouveau au brouillon 2 ; DL-2)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : 50 graines par configuration dans Locatello et collègues (fiche § 2, p. 4) ; la graine et les hyperparamètres comptent plus que l'objectif (p. 5–6 ; p. 6 : l'objectif seul explique 37 % de la variance des scores, objectif × régularisation 59 %, le reste la graine). Coût : 3 graines ≈ 86 h, 5 ≈ 107 h, 10 ≈ 161 h de calcul (M § 12).

**S19 — Variante B-θ** (**mis à jour** : CS2-04, CS2-06, CS2-07, CS2-08 ; DL-1, DL-8)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : hypothèses (i) à (iv) du théorème 1 (fiche § 3, p. 5), famille exponentielle conditionnelle (p. 3), observations continues (corrigendum, p. 9), k = 2 pour échapper à la proposition 1 (p. 6), λ aléatoires indépendants (p. 15) ; **activation lisse pour la condition (2.ii) du théorème 2** (PDF p. 6, vérifié : « The mixing function f has all second order cross derivatives ») : la fonction « leaky ReLU » du brouillon 2 est linéaire par morceaux, non dérivable aux plis, et ne garantissait que ∼A (CS2-06). nk + 1 = 11 (M § 10) ; **22 = 2 × (nk + 1) est un choix de l'auteur**, marge parce que le résultat est asymptotique (théorème 4) ; le papier ne la donne pas et descend lui-même sous 11 (il balaie 10 à 50 segments, p. 7, figure 3a ; PDF p. 7, vérifié) (CS2-07). u₂ inclut les années de référence : σ_e est calculé sur Y⁰ avant toute plantation, donc inchangé ; u₃ découpe les paires par un critère sans lien avec la sortie, en dernier recours seulement. Valeurs (M § 15) : base minimale u₁ = 21, u₂ = 36 ; 3 environnements et 16 ans : u₁ = 33.

**S20 — Condition à effet négatif R2⁻** (**mis à jour** : raison corrigée, CS2-09 ; DL-3)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : R2⁻ teste la **symétrie de signe des méthodes** (non l'hypothèse H-C⁻) ; « moyen » (β = 0,2) parce que c'est la taille où la plupart des méthodes sont prédites détecter (M § 8). **La puissance en R2⁻ n'est pas démontrée égale à celle de R2** (le fond ajoute de la variance aux non-traitées) : un échec à la ligne 7bis se lit « ne retrouve pas une cause de signe négatif dans ce montage », jamais « signe imposé » prouvé. Caractéristique opératoire : une méthode à 0,85 partout et 0,75 en R2⁻ passe la conjonction avec 0,180 (M § 9).

**S21 — Sélection supervisée du facteur à l'étape d'effet** (**mis à jour** : CS2-11, CS2-12 ; DL-5)
- Valeur : À REMPLIR — à geler par Lazar.
[retiré, règle 2 : recommandation ou confiance d'auteur]
- Raison : classer le facteur par son coefficient sur la sortie est une supervision (fiche § 2, portée (b)) ; couper par paire-année laissait les mêmes paires des deux côtés, et en B-hors une association due à la persistance d'une paire passait de E₁ à E₂ (CS2-11) ; les fenêtres de Y⁺ d'une même paire se chevauchent, d'où les erreurs groupées ; choisir la graine par sa corrélation à la vérité était un reste d'oracle (CS2-12).

[…]
## À intégrer après le verdict du collisionneur sur la question 6

À REMPLIR — section volontairement réservée : le verdict du collisionneur n'est pas rendu (tours Kimi coupés dans la nuit du 30 au 31 octobre 2026). Elle porte le marqueur du validateur, de sorte que le scellement reste impossible tant que le verdict n'est pas intégré. Points attendus (liste de contrôle, non exhaustive) :
1. Méthodes ajoutées ou retirées par le verdict (et leur place dans les tables A, Bθ, Effet-θ, B-hors) ; ligne du tableau des changements.
2. Critères de mort chiffrés par voie (relecture 6, RL6-08) : correspondance avec S9, S11, S19, S20.
3. Épreuve d'intervention **hors support** avec **ligne de base non identifiante** (RL6-04) : vérifier que S16 (décile inférieur de propension) et T1 la réalisent, sinon la compléter.
4. Mondes qui **violent** chaque hypothèse une à une (RL6-05) : inventaire de ce que l'épreuve viole déjà (H, non-linéarité, B-hors, D1, R2⁻) et de ce qui manque (dépendance entre latentes en B-θ, bruit gaussien, décalage dense des environnements).
5. Séparation **latentes / graphe / effet** (RL6-01) : chaque table nomme désormais son niveau (Table A : effet observé ; Table Bθ : latentes ; Effet-θ : effet) ; vérifier que le verdict du collisionneur ne demande pas davantage.
6. Hyvärinen et Morioka 2016 contre 2017 (RL6-07) ; décalages parcimonieux et Perry et collègues 2022 (RL6-06) : place éventuelle dans l'épreuve.
7. Protocole de détection de ce que le modèle apprend en pratique (RL6-09) : comparer à la captation de la popularité et à T3.
8. Toute divergence entre le verdict et ce brouillon : écrite, avec la décision de Lazar si elle touche une hypothèse ou un seuil.
<<<FIN PIÈCE 17>>>

### Pièce 18 — `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` (l. 22–40 ; 83–83 ; 164–249 ; 250–262) — nœuds N1

Origine : main ; empreinte du fichier source `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` ; 1905 mots ; l. 83 ajoutée par la liste v2 ; règle 2 appliquée.

<<<DÉBUT PIÈCE 18>>>
## Verdict

1. Aucune des quatre affirmations fortes de la question n'est établie dans les cellules ; aucune espèce ne les présente comme établies, sauf C sur la première :
   - **la fertilité comme propriété de la paire** : HYPOTHÈSE pour A (T1-A a1 ; T3-A c) et D (T1-D, table a ; T3-D c) ; B touche le point sous une forme voisine, une fertilité « définissable et mesurable avant le croisement » (T1-B P4). C ne la classe pas : son duel 2 la prend pour définition, une « fertilité intrinsèque d'une paire » par « sur-additivité validée » (T1-C, ligne 37). D le lui reproche (T2-D). En T3, C corrige le calcul sans reclasser l'affirmation (T3-C) ;
   - **la transition de phase sur P(reprise | paire)** : HYPOTHÈSE pour les quatre (T1-A a2 ; T1-B P5 ; T1-C a3 ; T1-D) ;
   - **l'émergence par essaims** : HYPOTHÈSE pour A (a3) et B (P6), RAPPORTÉ pour C (a6, essaim Navier-Stokes) ; D ne lui donne pas de statut en T1 et la range parmi le non établi en T3 (T3-D c) ;
   - **les causes par apprentissage profond seul** : HYPOTHÈSE pour A (a11), B (P7) et D (« à lui seul ») ; C classe HYPOTHÈSE un énoncé voisin, l'identification par IRM, PCMCI ou NOTEARS (T1-C a5).
2. Le gain est méthodologique. Au tour T2, trois défauts sont relevés sans concertation :
   - le pic de variance binomiale pris pour de la criticité (trois espèces : A, C, D) ;
   - la sur-additivité F faussée par le budget (A, C) et par la combinatoire (C, D) ;
   - le trou lu dans le flux de citations prédit mécaniquement une hausse (retour à la moyenne, « A0 », nommé par A), et l'étiquette de pont est circulaire (D).

[retiré, règle 2 : recommandation ou confiance d'auteur]
   - pic de variance : seules C et D passent à la surdispersion entre réplicats ; A exige une variance au-dessus d'un nul d'urne à moyenne égale ; B ne répond pas au point ;
   - sur-additivité : trois corrections différentes, une par espèce (A, C, D) ;
   - A0 : B, C et D inscrivent la rétrodiction inversée ; A, qui l'avait annoncée en T2, ne la reprend pas dans son E1′.
3. Divergence sur la première expérience : reproduire Gu-Krenn (A), constituer la base de ponts avec rétrodiction inversée (B), étalonner l'instrument 2 couplé au duel 1 sur processeur (C), lancer E1′ (D). Le goulot n'est pas commun. A et D désignent une base de ponts datés assez grande pour avoir de la puissance. B en fait un préalable, mais à 30–50 ponts et sans calcul de puissance. C place le goulot ailleurs : la validité de l'observable.
4. Question G : personne ne donne de référence exacte pour un « allumage » de champ. A, C et D classent RAPPORTÉ le seuil R₀ > 1 (Bettencourt 2006, 2008), repris de la pièce d'Argon, sans PDF. B ne traite pas G.

[…]
- **Désaccord.** Sur la littérature réelle, A refuse les tests de criticité, car la taille n'y est pas identifiable (« jamais sur la littérature réelle », T3-A). B les garde à partir de 5 tailles (T3-B). C et D restent en mondes inventés (T3-C, T3-D).
[…]
## (iii) Trois mesures décisives

Les seuils sont illustratifs selon leurs auteurs.

1. **E1′ / duel 1 — profil trou et structure contre distance et popularité.**
   - Signe attendu sous H_B : β₂ > 0, intervalle à 90 % excluant zéro, bootstrap par niches (T3-A).
   - Variante : gain relatif ≥ 20 % en précision dans les 100 premiers, intervalle à 95 % par blocs (T3-C).
   - Marge d'équivalence δ₀ = 0,03 (T3-B).
   - Arrêt : si la rétrodiction inversée atteint le score prospectif − δ₀, suspension (T3-B). Ce contrôle manque au E1′ de A (T3-A) ; il est à rendre obligatoire (décision 1).
   - Puissance vérifiée avant le lancement (T3-A, T3-D). C'est la seule issue qui « tue réellement une décision de conception » (T3-D).
2. **E6′ — gain conditionnel de Gu-Krenn à longue portée.**
   - Critère : un gain positif au-dessus de la popularité seule dans la strate de distance supérieure à 3 (T3-A).
   - Coût : nul selon A, « ~300-1 000 € » de carte graphique selon B (T1-B d).
   - Elle tranche la question posée « dès maintenant ».
3. **E2′ / duel 2 — étalonnage des tests de criticité sur mondes plantés.**
   - Critère de A : taux de détection ≥ 0,9, fausses alertes ≤ 0,1 (T3-A).
   - Critère de C : 5 tailles sur deux décades, 50 réplicats, φ > 2,0 au point critique, erreur de superposition < 5 % sur une taille tenue à l'écart ; falsification si φ ≤ 1,2 (T3-C).
   - La signature retenue n'est pas commune : surdispersion entre réplicats (C, D) ou variance au-dessus d'un nul d'urne à moyenne égale (A). À trancher au préenregistrement.
   - Si l'étalonnage échoue, le mot « transition de phase » sort du préenregistrement (T3-A).

**Mesure suivante, plus coûteuse : l'essaim contre l'élargissement du contexte.** Il faut ≥ 20 % d'avantage sur le meilleur de tous les témoins. Le pilote s'arrête s'il donne moins de 50 survivantes par cellule (T3-A E3′). Pour B, la marge d'équivalence est δ₀ = 5 % de survie (T3-B).

## (iv) Décisions à proposer

**1. Rendre obligatoires six garde-fous** dans tout préenregistrement du bisociateur sur littérature réelle :
- une étiquette de pont indépendante du canal (réutilisation hors des citations ; forme à fixer, puisque A, C et D en donnent trois) ;
- la rétrodiction inversée (omise par le E1′ de A en T3, ce qui montre qu'elle ne va pas de soi) ;
- un graphe amputé des ponts ;
- un bras « popularité seule » ;
- des jeux disjoints par niche et par période ;
- un calcul de puissance préalable.

Enjeu : sinon, le résultat positif est acquis par construction. Options :
- (a) gabarit complet : il ferme les trois artefacts, mais demande une base plus grande ;
- (b) seulement la rétrodiction inversée et l'étiquette : plus léger, mais la circularité de la partition reste ;
- (c) au cas par cas : souple, mais l'erreur se répète.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**2. Fixer l'ordre de départ, sans dépense.** Enjeu : selon A et D, la taille de la base de ponts conditionne la puissance ; B la place en préalable ; C commence par valider l'observable. Options :
- (a) base de ponts, puissance et rétrodiction inversée sur un sous-corpus traité sur processeur (B, D) : c'est le goulot désigné par A et D, mais il prend des jours humains ;
- (b) Gu-Krenn d'abord (A) : rapide, mais ne teste pas le trou ;
- (c) les deux en parallèle, processeur seul : couvre tout, mais fait deux chantiers.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**3. Dépense : un devis pour reproduire Gu-Krenn sur carte graphique ?** Enjeu : nul selon A, 300 à 1 000 € selon B. Options :
- (a) vérifier d'abord si le code tourne sur processeur : prudent, mais peut-être lent ;
- (b) devis immédiat : rapide, mais la dépense est peut-être inutile.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**4. Nœud : retirer « transition de phase » des préenregistrements sur littérature réelle.** Le terme n'est admis en mondes inventés et en courses qu'après E2′. Enjeu : c'est l'énoncé de ton hypothèse, et la taille n'y est pas identifiable. Options :
- (a) retrait (A) : honnête, mais on perd l'énoncé fort ;
- (b) maintien à partir de 5 tailles (B) : garde l'ambition, mais la confusion sociologique reste (T2-C) ;
- (c) suspension jusqu'à E2′ : neutre, mais retarde.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**5. Clore G par lecture.** Verser physics/0502067, 1504.00319 et les articles de 2008, 2009 et Ham 2007, puis chercher « ignition », « threshold » et « R0 » dans le texte intégral. Enjeu : éviter une attribution fausse dans un papier. Options :
- (a) versions arXiv d'abord, sans dépense : immédiat, mais incomplet ;
- (b) achat des articles : complet, mais c'est une dépense.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**6. Erratum joint au lot.** Il porte sur :
- la fusion des deux articles Gu-Krenn par Argon ;
- la « centralité » non sourcée, reprise comme établie (T1-B P4, T3-B c1 ; T1-C a4, T3-C c2) ;
- l'attribution par B d'un résultat de 2405.17044 à 2402.08640 ;
- l'attribution par C à la réponse indépendante 4 d'une affirmation propre à Argon sur Gu-Krenn ;
- l'appui « vérifié par » la relecture 3 donné par C (T1-C a8), alors que la relecture 3 dit le terme introuvable ;
- la citation par B, comme venant de A, d'une phrase de D (« cela ne valide pas encore une fertilité bibliographique » : présente en T1-D E2, absente de T1-A, relevé par T3-A) ;
- les chiffres 162/722 contre 300/719, les dates 6 ou 27 octobre, huit ou neuf champs.

Enjeu : ces chiffres ne sont pas opposables (R7). Options :
- (a) erratum : trace propre, un fichier de plus ;
- (b) rien : aucun coût, mais l'erreur se propage.

[retiré, règle 2 : recommandation ou confiance d'auteur]

**7. Dépense, à ne pas demander maintenant : pilote d'essaim et école d'été.** Enjeu : 3 000 à 20 000 € (T1-D), ou 4 000 à 5 000 $ (T3-C), tous illustratifs ; et un contact externe. Options :
- (a) attendre E1′ : pas d'aveugle, mais du retard ;
- (b) devis tout de suite : rapide, mais on paie avant de savoir si le trou existe.

[retiré, règle 2 : recommandation ou confiance d'auteur]

[…]
## Réserves

- **Lignée.** Les quatre espèces ne sont pas indépendantes des pièces :
  - A (Fable 5.1) est le modèle de conv-audit pour les questions 2 à 5 et pour les relectures : il attaque surtout ses propres pièces.
  - B est de la même lignée.
  - C défend sa propre pièce : il donne pour appui « vérifié par » une relecture qui dit le terme introuvable (T1-C a8), reprend la centralité non sourcée, et prend la fertilité de la paire pour définition (T1-C duel 2).
  - Seul D est extérieur.
- **Indépendance des accords.** Les accords de T3 suivent la lecture des critiques et restent partiels (pic de variance, A0, goulot). Ceux de T2 sont plus indépendants, mais sous le même gabarit.
- **Effet de la question.** Le gabarit tire vers la conception d'expériences : G traité par 3 espèces sur 4, F par une seule, la construction des systèmes (E) par aucune, aucune référence nouvelle.
- **Non vérifié.** Aucun PDF n'a été lu. Seuils et coûts sont illustratifs. Je n'ai confronté aux faits que les points cités ici. Rien n'a été vérifié hors du dépôt.
- **Hors périmètre.** J'ai ouvert par erreur le début de `run-…/journal.jsonl`, non nommé, et je n'en tire rien. Un point est à vérifier : il porte « essai 2 » pour T1-A, alors que `etat.md` indique 1.
- **Leçon de la v1.** La v1 avait étendu à quatre espèces des avis tenus par deux ou trois (AFF-1, AFF-2, AFF-4, AFF-5). La v2 nomme les espèces point par point.
<<<FIN PIÈCE 18>>>

### Pièce 19 — `registres/decisions.md` (lignes R-630, R-634, R-635, R-638, R-643, R-660, R-661, R-674, R-675, R-678, R-679, R-680, R-685) — nœuds tous

Origine : branche de conv-audit ; empreinte du fichier source `80edac2f960d42098b4509c95604199874b83b9a612b7ca6d2af859870abcbbe` ; 2135 mots ; lignes de la branche de conv-audit ; règle 2 appliquée.

<<<DÉBUT PIÈCE 19>>>
| R-630 | 2026-10-30 |Lazar (21:36 heure de Paris, mots directs) : (1) « ouiiiii » sur l'expérience randomisée de rencontres entre chercheurs (Boudreau et collègues 2017) → à transposer dans nos courses (bras « hasard » du bisociateur = rencontre randomisée ; proposition d'un traitement « rencontre » explicite, à sa décision) ; (2) sur « estimer mais pas identifier à lui seul : pourquoi pas ? apprentissage non supervisé ? » → réponse de fond écrite (théorèmes d'identifiabilité : impossible sans hypothèse, possible sous des hypothèses que nos données satisfont peut-être ; épreuve sur mondes inventés à causes connues) et **question 6 scellée pour le collisionneur** (`question-6-identification-collisionneur-v1.md`) ; « lance le collisionneur » = go sur devis, mot direct dans la session de session-depot (n° 264, 20:38 UTC) ; (4) « quels sont les différents bras ? » → expliqué (4 sous-sessions ; bisociateur à 3 bras × k paires).  [retiré, règle 2 : recommandation ou confiance d'auteur]|
| R-634 | 2026-10-30 |→ **essai et course 2 = option (a)** (lu comme go, même usage que R-614) : **un seul bras** de bisociation (règle « loin en domaine, proche en concept »), **une paire par session** ; pré-pilote **recentré sur les instruments de plausibilité** (étalonnage des juges sur témoins, vérification d'antériorité, aiguillage, garde de niveau méthode chez Kimi, chaîne de bisociation sur une paire) ; **retirés** : bras hasard et Gu-Krenn (ce dernier reporté à après sa reproduction), mesure de l'auto-préférence (dix fonds écrits deux fois), dose-réponse ; **gardée** : notation croisée. Objectif déclaré : produire des idées inédites et très plausibles, pas mesurer l'organisme. À porter au brouillon 4 du pré-pilote après la contre-lecture 3 ; devis refait demandé à session-depot (n° 266, 20:55 UTC). Machine jetable (R-533) toujours en attente.  [retiré, règle 2 : recommandation ou confiance d'auteur]|
| R-635 | 2026-10-30 |Lazar (21:56 heure de Paris) : « Gu-Krenn : et si on le gardait pour augmenter les chances de trouver de nouvelles idées et hypothèses plausibles et inédites ? » la reproduction chez session-depot continue en parallèle comme validation ; si leur modèle ne peut pas tourner à temps, un substitut par leurs traits publiés (paires de concepts jamais reliés, chacun actif) ; coût ≈ +4 fusions par proposeur. Modification de R-634 : décision de Lazar.  [retiré, règle 2 : recommandation ou confiance d'auteur]|
| R-638 | 2026-10-30 | Lazar (22:02 heure de Paris, mot direct) : « donc pas le bras basique distance-concept mais un bras NOUVEAU avec les bons paramètres, les bonnes grandeurs, la transition de phase, etc. » → **décision du directeur** : dans la course 2, le bras « loin en domaine, proche en concept » est **remplacé** par un bras nouveau « trou à structure commune, version 1 » (profil : communication faible entre niches, structure commune forte — objet mathématique, méthode, jeu de données —, désaccord lu à part, éloignement non extrême selon la cloche d'Uzzi ; niches lues sur les fiches par un lecteur neuf avec grille fermée ou par la carte des chapelles), **paramètres fixés à la main, déclarés SUPPOSÉ, gelés au préenregistrement**, étiqueté exploratoire ; Gu-Krenn reste second bras. Réserve écrite à Lazar (21:02 UTC) : les « bons paramètres » n'existent pas encore (ils sont l'objet du programme) et la transition de phase n'est pas un paramètre mais une hypothèse ; la version 1 est une meilleure conjecture, raffinée en génération 2 par l'apprentissage sur les fiches ; spécification après les verdicts des collisionneurs ; le test sur mondes inventés de la règle basique continue comme contrôle du code. |
| R-643 | 2026-10-30 | Lazar (22:12 heure de Paris, mot direct) : « bras basique : garder » → **bisociateur exploratoire de la course 2 = trois bras, une paire par session chacun** : bras méta (v1), bras Gu-Krenn, bras basique « loin en domaine, proche en concept » (comparaison) ; bras hasard retiré. Question 7 (allumage comme ensemble autocatalytique) scellée et ajoutée aux pièces du collisionneur (`question-7-allumage-autocatalytique-v1.md`). Transmis à session-depot (n° 268, 21:12 UTC) : devis v4 avec trois bras. |
| R-660 | 2026-10-30 |**VERDICT R13 de l'étape de validation de la bisociation v2 : NON CONCLUANT sur les deux volets** (Sonnet neuf, `lancement-v2/verdict-validation-v1.md`, scellé 23:55 UTC ; ligne 0 des tables 1 et 2, « V0 non tenue ») : V5 fausse en M_bien (2,8735 contre ≤ 0,5) ; V1 à V4, V6, S8, V9 et la reproduction S12 tenues. Prescription : arrêt avant les bras candidats ; nouvelle version du préenregistrement (R12). Désaccord avec la lecture : l'ordre de grandeur des paires valides était annoncé par le texte (« bien plus nombreuses que les 67 »), pas l'ampleur (×3,7 et ×2,9). **Nœud de décision soumis à Lazar** (aucun défaut) : (A) v3 du préenregistrement avec correction du générateur pour égaliser les statuts à étiquette d'opérateur (hypothèse de cause, à vérifier par calcul avant d'écrire la v3), graines de validation nouvelles (les actuelles ont été lues), déclaration de ce qui a été lu ; (B) v3 ne changeant que la définition ou le seuil de V5 (déconseillé : seuil gelé assoupli après lecture) ; (C) abandon de l'expérience v2. [retiré, règle 2 : recommandation ou confiance d'auteur]| nœud : Lazar |
| R-661 | 2026-10-31 |**Diagnostic de V5** (Opus neuf, `lancement-v2/diagnostic-v5-v1/`, mondes d'essai 990000–990199 sous RACINE_VALIDATION, M_bien et M_moyen, aucun code modifié, 00:04 UTC) : **V5 échoue par sa propre définition, non par le code**. Cause principale : pour « vrai d'opérateur » et « surface », l'étiquette de pont la plus rare est une étiquette d'opérateur (loi de v1, non S16d : jumeau exclusif à fréquence 2 ; homonyme de surface sur un opérateur de groupe à 7,17) ; cause secondaire : repli sur un concept de fond ou un moyeu quand le concept rare n'est pas vu des deux côtés, part variable selon le statut ; l'erreur type d'une différence entre statuts (0,3 à 0,6) est du niveau du seuil 0,5. **Aucune variante du générateur permise par S16a ne passe** (loi S16d donnée aux opérateurs de pont : 1,29 / 2,27 ; avec λ = 0, exclu par S16a : 0,47 en M_bien mais 0,92 en M_moyen). Seule une redéfinition de V5 passe : T2 (fréquence de l'étiquette du concept rare planté, vue des deux côtés, statuts qui en portent un) : 0,137 / 0,134 — mais contrôle presque acquis par construction. options pour la v3 (sans seuil assoupli) : A texte T2 ; B = A + ancienne grandeur rapportée sans seuil ; C générateur seul (insuffisant) ; D restriction aux trois statuts rares (passe M_bien 0,33, échoue M_moyen 0,83). Toute option change un critère gelé après lecture : à déclarer en toutes lettres dans la v3 avec nouvelles plages de graines de validation. [retiré, règle 2 : recommandation ou confiance d'auteur]| nœud : Lazar |
| R-674 | 2026-10-31 |**Point 01:50 UTC** : main b3be3644 (R-868 à R-870). **Devis v6** (`13ef84f9…`, contre-lu conforme) : pré-pilote ≈ 32,6 USD attendus aux bases, 45 suffit pour la dépense mais une étape protégée bute sur son plafond de relais avec 0,99 si les plafonds sont durs course 2 : plafond total 160 USD séquencé, 24 fusions ; tous nœuds de dépense sans défaut. Cela répond à ma question DEP4 (n° 270) : lecture « réservation souple » compatible ; S17 du brouillon 7 (45 / 40) à présenter à Lazar face à 50 / 45 (devis v6). Machine jetable v3 (`864f3d27…`) conforme, GO proposé 10 USD, location = nœud. Kimi coupé quatre fois dans la nuit (tours 6 et 7 : dernière reprise par chaîne v6 ; sinon décision d'absence de Kimi soumise à Lazar) ; conteneur de session-depot redémarré ≈ 01:40 UTC. Rien à répondre. Devis v6 et machine jetable v3 repris sur ma branche.  [retiré, règle 2 : recommandation ou confiance d'auteur]| routine |
| R-675 | 2026-10-31 | **Contre-lecture de l'annexe du bras méta (brouillon 1)** (Sonnet neuf, `contre-lecture-annexe-bras-meta-v1-brouillon1.md`, 01:56 UTC) : « soumettable après corrections » ; bloc de configuration rejoué, P14 reproduite, Uzzi p. 469/471 conformes, I-1 à I-10 exacts + I-11 à I-13. **Majeurs à remonter à Lazar** : **CA1-05** avec la bande [2 ; 3] et « faible » ≤ 1, 4 paires de niches sur 15 dans le profil → zéro paire dans le profil avec 0,59–0,67 à 6 fiches, 0,25–0,36 à 10 ; **le pré-pilote n'éprouverait souvent que le repli** ; élargir la bande à [2 ; 4] n'aide presque pas (0,54 / 0,21) ; options : accepter le repli comme mesure ; passer à 15 fiches (zéro avec 0,06, sur devis) ; toucher R-638 ; **CA1-01** la paire n1–n2 (fusionnées par le programme) est dans le profil : une paire « loin » par bruit d'étiquette ; **CA1-03** n5 (bornes et théorie) dans aucune paire du profil : axes 2 et 5 exclus par construction. Moyens : score récompensant les structures partagées = ce que les juges notent (fuite profil / jugement, CA1-08) ; bras basique ≠ « popularité seule » ; paires déjà prises ignorées par P14 ; loi a priori de n6 incohérente ; lecture du désaccord par paire = dépense absente du devis. Brouillon 2 de l'annexe après décision de Lazar sur CA1-05 et CA1-04 (jeux de données). | routine ; nœud à venir |
| R-678 | 2026-10-31 | **Point 02:54 UTC** : main b2fef830 (R-871) : Kimi coupé une 5e fois, plus de reprise cette nuit ; question 6 : 7 cellules valides sur 12 (sans Kimi en III.2), question 7 : 3 cellules ; conteneur de session-depot repris deux fois pendant l'inactivité (processus détachés perdus). Conséquence : le verdict de la question 6 (brouillon 3 du semi-réel, section bloquante) et celui de la question 7 attendent une décision de Lazar (absence de Kimi ou reprise de jour) ; rien à faire d'ici. CL19 de la v54 en cours. | routine |
| R-679 | 2026-10-31 |**CL19 de l'orchestrateur v54** (Sonnet neuf, `contre-lecture-cl19-orchestrateur-v54-v1.md`, 03:02 UTC) : **« lançable après corrections »** ; CL18 et I-1 à I-13 corrigés (9 tenus, 6 avec réserve) ; 663 OK. Majeurs : **CL19-01** source Gu-Krenn absente → refus à É0, alors qu'A19 dit « non produit, compté, sans arrêt » (inverse pour l'annexe) ; **CL19-02** après un nœud, le pré-pilote déclare la fin d'É9, ouvre la clé des classes et écrit M1 (contraire à A21 et O12) ; **CL19-03 (Lazar)** : la lecture par programme de la clé des classes en É5 viole la lettre d'A21 mais pas son intention (É5 — S20, A6, S19 — est impossible sans la classe des témoins) ; [retiré, règle 2 : recommandation ou confiance d'auteur]| routine |
| R-680 | 2026-10-31 | **Point 03:28 UTC** : main 2a326ffd (R-872, R-873) : arbre scellé de main réparé (compagnons des orchestrateurs v51/v52/v52b ajoutés par session-depot — mes copies sur cette branche en manquent peut-être : à vérifier par `verifier-arbre` avant la passation) ; **chantier Gu-Krenn préparé** (`docs/notes/gu-krenn-v1/`) : aucun poids publié, réentraînement obligatoire (carte graphique ou 8–30 h de processeur par valeur d'IR → machine louée, nœud de dépense) ; vocabulaire du contrôle des IA absent de leurs 37 960 concepts (conséquence pour le bras Gu-Krenn : le substitut S31 ne peut pas s'appuyer sur leur graphe pour notre sous-domaine — à porter au mémo et à l'annexe) ; valeurs 0,948 (IR = 100, p. 12–13) vérifiées ; préenregistrement v2 non scellé, D-GK-1 (fenêtre du test B) à Lazar. Rien à répondre. v55 en cours. | routine |
| R-685 | 2026-10-31 | **Orchestrateur v55 livré après la passation** (Opus neuf, vérifié et scellé 06:13 UTC ; `docs/notes/ideation-organisme-v1/orchestrateur-v55/`, LISEZMOI `bbfdcb3c…`, 406 empreintes vérifiées, archive `58b33177…`) : CL19-01 (sources absentes → bras « non produit », sans arrêt), CL19-02 (après un nœud : ni fin d'É9, ni ouverture de clé, ni analyse), CL19-03 partie code (aucune copie de la clé ; lectures par programme journalisées au coffre, comptes seuls ; É6 par identifiants opaques ; É9 sur liste scellée), CL19-04 à 13 traités ; un vrai défaut trouvé par le banc (S6 effaçait la ponctuation : « 12,5 » → « 12 5 ») corrigé ; **46 essais v55, suite 709 OK** (1 échec préexistant `test_v51_06`) ; **103 mutations tuées pour la raison attendue** (défaut `super()` du banc corrigé). 174 compagnons ajoutés par moi (`verifier-arbre .` : restent les 5 addendums v1–v5 de la bisociation, voulus). Décisions ouvertes ajoutées au mémo par renvoi : CL19-03 (lecture 1 amender A21, faite par la v55 ; lecture 2 boîte tenue par session-depot), plafond de nombres ajoutés au rendu (S6), phrase de DEP4, désaccord limité à `paires_max`, A14 sur petits effectifs, relecteur muet ; I-11, I-13 non traités. Non contre-lu (CL20 à faire). La passation 0540 (scellée, non réécrite) disait la v55 en cours : cette ligne la complète. | routine |
<<<FIN PIÈCE 19>>>

### Pièce 20 — `docs/notes/ideation-organisme-v1/contre-lecture-cl18-orchestrateur-v53-v1.md` (l. 35–35 ; 156–156) — nœuds N5 (portée du plafond, CL18-11)

Origine : branche de conv-audit ; empreinte du fichier source `0ce1d0b5a8c5016fdcb7262db3597bcc0320ddcd884dfb3d8821fa467230c52b` ; 86 mots ; ajoutée par la liste v2 ; règle 2 appliquée.

<<<DÉBUT PIÈCE 20>>>
| 1 | S17 par génération ; ligne de GO ≥ N × S17 + (N − 1) × étage | **à remonter à Lazar** | cohérent pour N = 1 (le pré-pilote) ; pour N > 1 le devis v5 de session-depot (R-669) raisonne sur un plafond global de la course, pas sur N plafonds par génération ; CL18-11  [retiré, règle 2 : recommandation ou confiance d'auteur]|
[…]
**CL18-11 (moyenne) — plafond par génération (choix 1).** À remonter : voir section E et choix 1.
<<<FIN PIÈCE 20>>>

### Pièce SD-1 — `donnees/collisionneur-question-6-v1/run-question-6-e3-v1/etat.md` (entier) — nœuds N6

Origine : dépôt de session-depot (état de run) ; empreinte du fichier source `71cd5a7248be6d9b963b6c1eb67e7a9126e85dab9b4dc213ece3f5752955131b` ; 199 mots ; pièce de session-depot ; état du run seul, aucune réponse de cellule.

<<<DÉBUT PIÈCE SD-1>>>
| Cellule | Statut | Essais | Modèle servi | Caractères | Marqueur | Coût USD |
|---|---|---|---|---|---|---|
| E3-T1-conception-A | OK | 1 | claude-fable-5-1 | 21446 | oui | 0.91 |
| E3-T1-conception-B | OK | 1 | claude-opus-4-6 | 18119 | oui | 0.70 |
| E3-T1-conception-C | OK | 1 | gemini-4-argon | 36980 | oui | 0.66 |
| E3-T1-conception-D | OK | 1 | kimi-k3.1-pro | 13502 | oui | 0.20 |
| E3-T2-critique-croisee-A | OK | 1 | claude-fable-5-1 | 23120 | oui | 1.44 |
| E3-T2-critique-croisee-B | OK | 1 | claude-opus-4-6 | 28580 | oui | 1.29 |
| E3-T2-critique-croisee-C | OK | 1 | gemini-4-argon | 34829 | oui | 0.79 |
| E3-T2-critique-croisee-D | ECHEC | 2 | None | 0 | non | 0.00 |
| E3-T3-reponse-A | OK | 1 | claude-fable-5-1 | 22640 | oui | 1.30 |
| E3-T3-reponse-B | OK | 1 | claude-opus-4-6 | 18192 | oui | 1.11 |
| E3-T3-reponse-C | OK | 1 | gemini-4-argon | 25816 | oui | 0.77 |

Absences acceptées par l'arbitre : E3-T2-critique-croisee-D, E3-T3-reponse-D.
Dépense totale : 9.19 USD. Mis à jour 2026-10-31T06:48:32Z.
<<<FIN PIÈCE SD-1>>>

### Pièce SD-2 — `donnees/collisionneur-question-7-v1/run-question-7-e3-v1/etat.md` (entier) — nœuds N6, N1

Origine : dépôt de session-depot (état de run) ; empreinte du fichier source `28952d78ab42107a28f58eff7aac113021f1edd8dea21e6f010400089d0f269d` ; 185 mots ; pièce de session-depot ; état du run seul, aucune réponse de cellule.

<<<DÉBUT PIÈCE SD-2>>>
| Cellule | Statut | Essais | Modèle servi | Caractères | Marqueur | Coût USD |
|---|---|---|---|---|---|---|
| E3-T1-conception-A | OK | 1 | claude-fable-5-1 | 24795 | oui | 1.10 |
| E3-T1-conception-B | OK | 1 | claude-opus-4-6 | 21865 | oui | 0.86 |
| E3-T1-conception-C | OK | 1 | gemini-4-argon | 34196 | oui | 0.70 |
| E3-T1-conception-D | ECHEC | 3 | None | 0 | non | 0.00 |
| E3-T2-critique-croisee-A | OK | 1 | claude-fable-5-1 | 19282 | oui | 1.29 |
| E3-T2-critique-croisee-B | OK | 1 | claude-opus-4-6 | 19693 | oui | 1.11 |
| E3-T2-critique-croisee-C | OK | 1 | gemini-4-argon | 28693 | oui | 0.75 |
| E3-T3-reponse-A | OK | 1 | claude-fable-5-1 | 20702 | oui | 1.31 |
| E3-T3-reponse-B | OK | 1 | claude-opus-4-6 | 17632 | oui | 1.16 |
| E3-T3-reponse-C | OK | 1 | gemini-4-argon | 22490 | oui | 0.74 |

Absences acceptées par l'arbitre : E3-T1-conception-D, E3-T2-critique-croisee-D, E3-T3-reponse-D.
Dépense totale : 9.02 USD. Mis à jour 2026-10-31T06:48:31Z.
<<<FIN PIÈCE SD-2>>>

### Pièce SD-3 — `registres/decisions.md` (lignes R-866, R-868, R-869, R-870, R-871, R-873) — nœuds N3, N6, N9

Origine : main ; empreinte du fichier source `b1d772171a6c78768d365fa78f6fe01886e6990b02e18938d4fc66b50c1b903c` ; 790 mots ; lignes de session-depot (main) ; règle 2 appliquée.

<<<DÉBUT PIÈCE SD-3>>>
| R-866 | 2026-10-31 |course 2 à 4 sous-sessions ≈ 118 USD attendus avec 24 fusions, **le plafond total de 110 ne tient plus** ; relecteur : conforme avec réserves, une option manque à la décision 1 et la domine → **v6 en écriture**. **Machine jetable v2** (`39260994…` ; ≈ 0,5 USD attendus, 7,4 au pire, GO proposé 10 ; Ubuntu 24.04 et AppArmor contre bwrap traités, sources copiées) : relecteur conforme avec réserves (faille de garde dans l'amorce) → **v3 en écriture**. **PDF Bettencourt** (conv-audit n° 269) : 2009 (MIT DSpace) et 2006 versés, 2015 déjà là, 2008 Scientometrics sans copie libre ; réserve : le fichier DSpace reçu diffère en taille et MD5 de la notice DSpace (version tamponnée probable), première page conforme. Rien n'est présenté à Lazar avant v6 et v3.  [retiré, règle 2 : recommandation ou confiance d'auteur]| routine. |
| R-868 | 2026-10-31 |**Devis v6 de la course 2 et du pré-pilote** (`13ef84f9…`) : neuf constats corrigés, contre-lu conforme (quatre défauts mineurs de rédaction). [retiré, règle 2 : recommandation ou confiance d'auteur]| nœuds de dépense : soumis à Lazar. |
| R-869 | 2026-10-31 | **Tour question 6 arrêté (code 5)** à 01:11 UTC : Kimi E3-T2-D, amont coupé après envoi (ConnectionResetError ; 4e coupure de Kimi de la nuit, toutes sur des appels longs à gros corps, dont 3 sur E3-T2) ; relais PID 6384 arrêté par le lanceur. Suite 1 préparée et enchaînée par `chaine-nuit-v5.sh` (PID 27931) après la chaîne v4 (question 7 en cours). Piste pour plus tard (routine, code) : relance automatique d'une cellule Kimi coupée dans le relais ou le collisionneur, bornée et comptée ; le devis v6 compte déjà le facteur 1,45. | routine ; dépense sous GO. |
| R-870 | 2026-10-31 | **Kimi coupé encore** : question 7 arrêtée à 01:26 UTC (E3-T1-D, ConnectionResetError à 361 s, 0,43 USD au pire cas, 2,65 USD dépensés), suite 1 de la question 6 arrêtée à 01:27 (E3-T2-D, flux coupé avant [DONE] à 37 s, 0,58). Conteneur redémarré ≈ 01:40 UTC (rien en cours de perdu) ; `recentRelayFailures` du mandataire vide après le redémarrage, cause non établie. **Dernière reprise de la nuit** (chaîne v6) : question 7 suite 1, puis question 6 suite 2 ; si Kimi est encore coupé, plus aucune reprise : décision d'absence de Kimi (non prévue par R-831) ou de reprise de jour soumise à Lazar. Imputation sur GO-17 à ce point : ≈ 18,9 USD (bisociation au-delà de GO-16 8,30 ; Kimi recherche 0,39 ; question 6 ≈ 7,2 ; question 7 ≈ 3,1). | routine ; dépense sous GO. |
| R-871 | 2026-10-31 |**Kimi coupé une 5e fois** : question 7 suite 1 arrêtée à 01:47 UTC (E3-T1-D, flux coupé avant [DONE] à 283 s, 0,43 USD au pire cas). **Plus aucune reprise cette nuit** (R-870). État : **question 6** : 7 cellules valides sur 12 (III.1 complet, III.2 sans Kimi), 6,00 USD + 3 appels Kimi comptés au pire cas (≈ 1,6) ; **question 7** : 3 cellules valides (III.1 sans Kimi), 2,65 USD + 2 appels Kimi (≈ 0,9). **Conteneur redémarré deux fois** (≈ 01:40 et ≈ 02:3x UTC) : il est repris quand la session est inactive, et les processus détachés (setsid) meurent avec lui — la suite 2 de la question 6, démarrée à 01:47, n'a laissé aucun journal ni appel. **Décision soumise à Lazar** (nœud : R-831 ne prévoit pas l'absence de Kimi) : finir les questions 6 et 7 sans Kimi (`--accepter-absence` sur ses cellules), ou réessayer de jour avec Kimi, ou s'arrêter là.  [retiré, règle 2 : recommandation ou confiance d'auteur]| nœud : soumis à Lazar. |
| R-873 | 2026-10-31 | **Chantier Gu-Krenn préparé, sans dépense** (conv-audit n° 261 ; wol8nheoc) : `docs/notes/gu-krenn-v1/` — état des lieux (code Impact4Cast cloné et lu, licence MIT ; données Zenodo CC-BY 9,5 + 17,8 Go, métadonnées seules ; **aucun poids publié : réentraînement obligatoire**, carte graphique ou 8 à 30 h de processeur par valeur d'IR → machine louée, nœud de dépense ; le conteneur ne suffit pas) ; vocabulaire du contrôle absent de leurs 37 960 concepts (probe, steering, monitoring, alignment n'existent qu'au sens physique) ; valeurs publiées vérifiées sur PDF (0,948 pour IR = 100, p. 12 et 13 ; banc fig. 6 p. 7). **Préenregistrement v2 non scellé** (`7f32c4e0…`), contre-lu par Fable (« scellable après corrections », 13 constats : 9 appliqués, 4 en partie). Avant scellement : **décision D-GK-1 de Lazar**, devis de la machine louée et GO, code d'analyse écrit et testé, contre-lecture 2. Rien n'a été exécuté ni calculé ; `frp_example.zip` (sorties brutes du réseau) non ouvert (R1).  [retiré, règle 2 : recommandation ou confiance d'auteur]| nœuds : soumis à Lazar. |
<<<FIN PIÈCE SD-3>>>

### Pièce SD-4 — `docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md` (l. 1–20 ; 202–321) — nœuds N3, N9

Origine : main ; empreinte du fichier source `1c1618a2484b542e534b74fc12906212c6284d41d0bc691722e4a209499f67e9` ; 1595 mots ; en-tête, § 4 (test hors échantillon) à § 6 (critère de mort) ; règle 2 appliquée.

<<<DÉBUT PIÈCE SD-4>>>
# État des lieux — Gu et Krenn 2024 (« Impact4Cast »), avant reproduction et test hors échantillon — v1

Lignée « session-depot », 31 octobre 2026, 02:15–03:00 UTC. Demande : message n° 261 de conv-audit
(`origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-30_n261.md`), qui cite le
brief `brief-nouvelle-lignee-bisociateur-v1.md` de la même branche (empreinte vérifiée contre son `.sha256` :
`2cdf135fff340960…`, conforme).

**Ce que cette note n'est pas.** Aucun code de Gu et Krenn n'a été exécuté ; aucune donnée lourde n'a été
téléchargée ; aucune aire sous la courbe ni aucune autre métrique n'a été calculée, ni sur leurs données ni sur
OpenAlex (R1). Les seuls comptes produits sont des comptes de chaînes dans leur liste de concepts (§ 5), qui ne sont pas
une mesure de résultat. Aucune dépense ; aucune requête à l'interface payante d'OpenAlex ; aucune clé lue.

Source primaire : `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2402.08640-gu-krenn-2024.pdf`, empreinte
`6b3d29db7cd6f7de…` (vérifiée, conforme), version arXiv **v4 du 11 juin 2025**, 18 pages. Pages citées selon la
numérotation imprimée du PDF. Version publiée : *Machine Learning: Science and Technology* 6(2), 025041 (2025) (selon le
LISEZMOI du dépôt de code ; non vérifiée sur la version publiée, que nous n'avons pas — R7 : les chiffres ci-dessous
sont ceux de la v4).

---

[…]
## 4. Test hors échantillon à partir d'OpenAlex

### 4.1 La moisson de `donnees/moisson-openalex-v1` ne couvre pas leurs concepts

Lu : requête déclarée v2 et les fiches `.moisson.json` (comptes et filtres, aucun contenu d'œuvre). Les cinq
sous-domaines (contrôle et alignement des intelligences artificielles, vérification formelle, sécurité des systèmes,
statistique séquentielle, neurosciences computationnelles) sont **disjoints** de l'optique et de la physique quantique,
et le `select=` garde `id, doi, title, publication_date, authorships, referenced_works, concepts, topics,
primary_location, type` : **ni résumé (`abstract_inverted_index`), ni `counts_by_year`, ni `cited_by_count`**. Or leur
graphe exige le résumé (repérage des concepts) et les citations annuelles (étiquettes). Non réutilisable.

### 4.2 Découpage proposé (à sceller avant toute lecture)

Leur graphe s'arrête en avril 2023 ; nous sommes le 31 octobre 2026. Une fenêtre de trois ans complète après leur
coupure n'existe que jusqu'à fin 2025.
- **Test principal, même tâche, même horizon** : traits à *y* = **2022** (fin décembre 2022) calculés sur **leur**
  graphe publié (les fichiers 2022 sont dans `data_for_features`) ; modèle figé = `train_model_2022_run.py`
  (2019→2022), entraîné par nous à l'identique ; étiquettes = arêtes nouvelles créées par les articles publiés du
  **1er janvier 2023 au 31 décembre 2025**, citations 2023 + 2024 + 2025, seuils IR = 10, 50, 100. Aucune information
  postérieure à 2022 n'entre dans les traits ni dans l'entraînement : c'est un vrai hors échantillon.
- **Test secondaire, « liens apparus de 2024 à 2026 »** (formulation du message n° 261) : graphe prolongé jusqu'à fin
  2023 par notre moisson, traits à *y* = 2023, étiquette = **apparition** de l'arête entre le 1er janvier 2024 et la date
  de moisson (fenêtre incomplète, ≈ 2 ans 10 mois). Leur modèle n'a pas été entraîné pour la prédiction de liens pure :
  le rapporter comme transfert de tâche, avec IR = 1 (au moins une citation) comme point le plus proche.

### 4.3 Requête OpenAlex (déclarée, non lancée)

Mêmes règles que leur code : articles de revue, titre et résumé présents, date de publication.
```
filter=from_publication_date:2023-01-01,to_publication_date:2025-12-31,has_abstract:true,type_crossref:journal-article
select=id,title,abstract_inverted_index,publication_date,cited_by_count,counts_by_year,type,type_crossref
per-page=200, sort=publication_date:asc, curseur
```
(le champ exact du type est une inconnue, I-2 : leur code filtre `type == 'journal-article'` sur l'ancien instantané ;
le type d'OpenAlex est devenu « article » et l'ancien vocabulaire survit dans `type_crossref`.) Puis traitement
**identique** au leur : `get_single_article_string` (minuscules, remplacements), recherche de sous-chaîne des 37 960
concepts, paires, horodatage en jours depuis 1990, citations annuelles.

**Volume et coût** : inconnus (I-1). Ordre de grandeur : leur filtre gardait 92 millions d'articles jusqu'en avril 2023 ;
trois années récentes en font vraisemblablement plus de 10 millions → plus de 50 000 pages de filtre, soit plus de 5 USD
au tarif déclaré dans `requete-declaree-v1.md` (0,0001 USD par page de filtre ; allocation gratuite de 1 USD par jour),
c'est-à-dire **plus d'une semaine d'allocation gratuite**, et des dizaines de Go de texte brut (le disque libre ici est
de 9 Go). Alternative sans crédit : l'**instantané public** d'OpenAlex (CC0, accès anonyme) — manifeste du 14 octobre
2026 lu : 464 765 485 œuvres, 1 898 fichiers parquet, **744 Go** (675 Go en lignes JSON compressées), partitionnés par
date de mise à jour, pas par date de publication ; le format parquet permet de ne tirer que les colonnes utiles, mais la
colonne des résumés reste le gros du volume. Les deux voies supposent une machine louée : nœud de dépense.

### 4.4 Témoins appariés sur le degré et l'âge

Pour chaque paire positive (*u*, *v*) (reliée dans la fenêtre, ≥ IR) : tirer *k* paires négatives (non reliées jusqu'à
la fin de la fenêtre) dans la même case de
(i) degré de chaque extrémité à *y*, ordonné (degré bas, degré haut), en classes de quantiles (ou classes log2) fixées
avant lecture ;
(ii) âge de chaque concept à *y* = *y* − année de sa première arête dans le graphe (tiré de `full_dynamic_graph`),
en classes fixées.
Graines par `numpy.random.SeedSequence` (R9). Rapporter : l'aire sous la courbe sur l'échantillon aléatoire « à leur
manière » (10 millions de paires) **et** sur l'échantillon apparié ; et les mêmes pour des bases simples figées
(attachement préférentiel, similarité cosinus seule, Simpson seule, degré seul). Le test apparié mesure ce que le modèle
sait au-delà de « les concepts populaires et anciens se relient davantage ».

### 4.5 Pièges à fixer dans le préenregistrement

1. **Dérive de la source** : OpenAlex est passé à « Walden » en novembre 2025 (`RELEASE_NOTES` du seau public :
   « switch to walden dataset », 463 millions d'œuvres avec les fiches « xpack »), avec retraits et récupérations de
   résumés (2025-01-29 : 350 000 résumés retirés ; 2026-06-25 : 1,4 million récupérés), reclassements de types
   (2024-07-30 : 4 millions d'« article » reclassés). Le taux de création d'arêtes peut changer pour des raisons de base,
   pas de science. Contrôle proposé : **pont** — reconstruire avec la moisson actuelle les arêtes 2020–2022 et comparer
   **les comptes** (arêtes, articles) à leur graphe publié, avec une tolérance déclarée d'avance.
2. **Citations révisées** : `counts_by_year` actuel ≠ celui de leur instantané de 2023 ; les étiquettes 2023–2025
   viennent forcément de l'actuel. À rapporter, pas à corriger.
3. **Fenêtre 2026 incomplète** : aucune étiquette à trois ans au-delà de fin 2025.
4. **Recherche de sous-chaîne sans limite de mot** : à reproduire telle quelle (fidélité), avec une variante
   « mot entier » seulement en analyse secondaire déclarée.
5. **Normalisation dépendante de l'échantillon** : `rescaling_col` divise par le maximum de l'ensemble évalué ;
   l'échantillon apparié aurait d'autres maxima. Figer : maxima calculés sur le graphe entier de l'année *y*
   (`get_norm_features`), identiques pour tous les ensembles.
6. **Variance d'une course à l'autre** : non publiée ; le critère « aire retrouvée » doit porter une tolérance fixée
   d'avance et un nombre de graines.

---

## 5. Couverture du vocabulaire du contrôle des intelligences artificielles

Simple recherche de chaînes dans `full_domain_concepts.txt` (37 960 concepts, `1544c30a5470af06…`), script
`scripts-v1/couverture_vocabulaire_v1.py` (`0113767ffc20cf2d…`), sortie complète
`couverture-vocabulaire-controle-v1.tsv` (`0f8dc65752ded4ac…`). Ce ne sont pas des mesures de résultat.

- **Absents (0 concept, ni exact ni comme mot)** : sabotage, e-value (« e value », « evalue »), safety, AI safety,
  misalignment, deception, honesty, interpretability, mechanistic, sparse autoencoder, residual stream, reward hacking,
  reward model, red team, jailbreak, backdoor, steganography, sandbagging, scheming, situational awareness, chain of
  thought, language model, large language model, attention, multi agent, out of distribution, sequential test,
  hypothesis test, betting, watermark, oversight, audit, evaluation awareness, sycophancy, hallucination, linear probe.
- **Présents comme concepts exacts** : neural network, machine learning, reinforcement learning, artificial
  intelligence, adversarial attack.
- **Présents seulement dans un autre sens (homonymes de physique)** : probe (20 : « weak probe beam », « x ray
  probe »…), monitoring (2 : « non invasive monitoring »…), steering (16 : « EPR steering », « beam steering »…),
  activation (12 : « activation energy »…), alignment (2 : « magnetic field alignment »…), control (65 : « quantum
  control »…), conformal (20 : « conformal field »…), martingale (2), calibration (4), agent (8 : dont « dishonest
  agent », « adversarial agent »), trojan (2 : « trojan horse attack »), collusion (1 : « collusion attack »).

**Conclusion** : la liste ne couvre pas le contrôle des intelligences artificielles ; les quelques mots communs
portent un sens de physique et créeraient de fausses arêtes. La liste générale de 368 825 concepts **n'est pas publiée**
(seule la liste du domaine l'est). **Extension proposée** : relancer leur chaîne (`create_concepts/` : RAKE, seuils 9 et
6, filtres) sur un corpus arXiv `cs.LG`, `cs.AI`, `cs.CL`, `cs.CR`, `stat.ML` — ce qui construit un **autre graphe** et
demande un **autre entraînement** : on testerait alors leur *méthode*, pas leur *modèle*. Le test hors échantillon de
leur modèle doit donc rester dans leur domaine (optique et quantique) ; le transfert au contrôle des intelligences
artificielles est une seconde expérience, à préenregistrer à part.

---

## 6. Ce que cela implique pour le critère de mort (message n° 261, point 3)

- « Aire publiée non retrouvée » doit nommer **quelle** aire (banc, fig. 6 p. 7 ; ou principale, fig. 11 p. 12), la
  tolérance et le nombre de graines. Proposition à discuter avec conv-audit : voie (R-a) d'abord (peu chère), voie
  (R-b) seulement si (R-a) passe.
- « Échec hors échantillon » doit nommer la métrique (aire sur l'échantillon apparié), le seuil et les bases à battre
  (attachement préférentiel, Simpson seule), fixés avant la moisson 2023–2025.

---
<<<FIN PIÈCE SD-4>>>

### Pièce N9-1 — `docs/notes/gu-krenn-v1/prereg-gu-krenn-reproduction-et-hors-echantillon-v2.md` (l. 40–95 ; 122–140 ; 220–240) — nœuds N9

Origine : main ; empreinte du fichier source `7f32c4e0f841fe670b00bd726198770731a8edd4e09be54a4d302e035404a77b` ; 1426 mots ; hypothèse, prédiction, seuil, B3 et encadré D-GK-1 ; règle 2 appliquée.

<<<DÉBUT PIÈCE N9-1>>>
## Hypothèse

Le classeur de Gu et Krenn (réseau entièrement connecté sur 141 traits [p. 4] d'un graphe de 37 960 concepts d'optique
et de physique quantique [p. 3]) est un instrument utilisable pour le bras Gu-Krenn du bisociateur. « Utilisable »
s'entend au sens strict des seuils ci-dessous : **non réfuté** par ce test, pas démontré fiable.

- **HA (reproduction)** : réentraîné à partir de leur code et de leurs données publiées, sur leur partage temporel, il
  retrouve leurs aires sous la courbe publiées (aucun poids n'est publié : réentraîner est obligatoire).
- **HB (hors échantillon)** : figé avant toute lecture des données postérieures à 2022, il classe les paires de concepts
  non reliées à fin 2022 qui se relient ensuite (fenêtre F, décision D-GK-1, option (a) : F = 1er janvier 2023 –
  30 septembre 2026 ; littérale F = 1er janvier 2024 – 30 septembre 2026) au-dessus des paires qui restent non reliées,
  **à degré et âge égaux**, et mieux que deux règles simples (attachement préférentiel, similarité de Simpson seule).

Hypothèses de travail : leur graphe publié (instantané OpenAlex ; la page 3 donne « avril 2023 » pour la coupure des
arêtes et « février 2023 » pour l'instantané [p. 3] — dans les deux cas après le 31 décembre 2022) est complet pour les
articles publiés jusqu'au 31 décembre 2022 ; la dérive de la base OpenAlex actuelle (« Walden », novembre 2025 —
SUPPOSÉ, notes de version du seau public) est contrôlée par le pont (Plan, étape B2). Leur modèle prédit l'**impact**
(au moins IR citations dans les trois ans [p. 4]) et non l'apparition pure : HB est donc un transfert de tâche, déclaré
comme tel.

## Prédiction chiffrée et signe attendu

**(A) Reproduction** — aucun signe d'écart attendu (bilatéral). Valeurs cibles, une seule course publiée chacune :

| Cas | Cible publiée | Statut |
|---|---|---|
| A1 banc, entraînement 2016→2019, évaluation 2019→2022, IR = 10 : réseau / XGBoost | 0,9455 / 0,9442 [p. 7, fig. 6(a)] | réseau décisif ; XGBoost information |
| A1 banc, même découpage, IR = 50 : réseau / XGBoost | 0,9588 / 0,9561 [p. 7, fig. 6(b)] | réseau décisif ; XGBoost information |
| A2 principal, entraînement 2016→2019, évaluation 2019→2022, IR = 10 / 50 / 100 | 0,94 / 0,96 [p. 12, fig. 11] / **0,948** [p. 12, annexe D ; p. 13, fig. 12] | décisif |

Pour IR = 100, la cible unique est 0,948 (trois décimales, même expérience que le 0,95 arrondi de la fig. 11 [p. 12]).

Prédiction : chaque moyenne sur trois graines (nombre SUPPOSÉ, choisi ici) tombe à moins de 0,010 de sa cible pour A1, à
moins de 0,015 pour A2 (tolérances SUPPOSÉ, choisies ici : variance d'une graine à l'autre non publiée ; A2 publié
arrondi à deux décimales pour IR = 10 et 50). Réfutation : un écart au-delà de 0,020 (A1) ou 0,025 (A2) sur un seul cas
décisif, dans un sens ou dans l'autre (SUPPOSÉ).

**(B) Hors échantillon** (modèle 2019→2022, IR = 10, traits de fin 2022, apparition d'une arête dans la fenêtre F) —
signe attendu : aire appariée > 0,5 et modèle > chacune des deux règles simples sur l'échantillon apparié. Ordres de
grandeur, SUPPOSÉ (aucun appui publié pour l'apparition pure) : aire sur l'échantillon aléatoire ≈ 0,90 (leur variante
sans réentraînement descend de 0,9463 à 0,9311 quand l'évaluation recule de 2018 à 2022 [p. 8, fig. 7]) ; aire appariée
≈ 0,70. Réfutation : seuils de la section Seuil non atteints. Aucun signe n'est visé (R3) : les deux issues décident du
bras.

**Attentes écrites des analyses d'information** (aucune n'entre dans un verdict ; toutes SUPPOSÉ) :
- B′ (leur tâche : impact, citations 2023–2025) : aire entre 0,88 et 0,95, au-dessus de B-i (tâche d'entraînement
  retrouvée ; repère : 0,9311 [p. 8, fig. 7]).
- B avec les modèles IR = 50 et 100 : **aucun signe attendu** (ces modèles sont entraînés sur un impact plus rare,
  pas sur l'apparition) ; écart à IR = 10 attendu inférieur à 0,03 en valeur absolue sur B-i et sur B-ii.
- Variante « mot entier » de la recherche de sous-chaîne : B-i et B-ii à moins de 0,01 de la version sous-chaîne.
- Variante conditionnée de A2 : à moins de 0,03 de 0,694 (évaluation) ; repère d'entraînement 0,747 [p. 5].
- Fenêtre non retenue par D-GK-1, rapportée en information : si F de l'option (a) est retenue, B-i et B-ii sur la
  population conditionnée (2024–2026, paires reliées en 2023 retirées) attendues **plus basses** de 0,01 à 0,05 ; si F
  littérale est retenue, B-i et B-ii sur la fenêtre 2023–2026 attendues **plus hautes** de 0,01 à 0,05.
- Aire appariée de l'attachement préférentiel (indicateur d'appariement, voir Métrique) : entre 0,50 et 0,60.

[…]
## Seuil

- **A1 retrouvée** : les deux cas du réseau (IR = 10 et 50) à moins de 0,010 de la cible ; **non retrouvée** : un des
  deux au-delà de 0,020 ; entre les deux : **retrouvée avec réserve** (on continue, la réserve est rapportée).
  XGBoost : rapporté avec ses écarts, sans verdict ; un écart XGBoost au-delà de 0,020 alors que le réseau passe est une
  réserve nommée. SUPPOSÉ.
- **A2 retrouvée** : les trois cas à moins de 0,015 ; **non retrouvée** : un cas au-delà de 0,025 ; entre les deux :
  retrouvée avec réserve. SUPPOSÉ.
- **B réussi** (HB non réfutée) si les trois tiennent : B-i ≥ 0,85 (estimation ponctuelle) ; borne basse de
  l'intervalle de B-ii > 0,60 ; borne basse de l'intervalle de B-iii > 0. SUPPOSÉ. **B échoué** si l'une manque.
- Lien entre 0,60 et l'usage : le bras propose au bisociateur des paires classées ; à aire appariée 0,60, entre deux
  paires de mêmes classes de degré et d'âge, le modèle place la paire qui se reliera devant l'autre six fois sur dix.
  En dessous, le bras n'apporte presque rien de plus qu'un filtre sur le degré et l'âge, qui ne coûte ni entraînement
  ni machine louée : c'est un **plancher d'usage**, pas une preuve de fiabilité. B-iii > 0 ajoute qu'il doit aussi
  battre Simpson, règle gratuite. Le seuil n'est pas relevé : aucune donnée ne permet d'en fixer un autre moins
  arbitrairement, et « B réussi » ne se lit que « HB non réfutée ».
- Les tests sont conjonctifs (tout doit passer pour conclure « non réfuté ») : aucune correction pour comparaisons
  multiples n'est nécessaire pour cette conclusion ; tout le reste est rapporté comme information, sans verdict.

[…]
**B3, population et étiquettes** (texte écrit pour la fenêtre de l'option (a) de D-GK-1) : population = paires non reliées
au 31 décembre 2022 sur le graphe tronqué (aucune donnée moissonnée n'entre dans la définition de la population).
Étiquette = au moins un article de notre moisson publié du 1er janvier 2023 au 30 septembre 2026 qui les relie.
Traits = ceux de fin 2022 (leur graphe seul : aucune source mêlée dans les entrées), normalisés par les maxima scellés
à B0. Rapporté : nombre et part des positives reliées dès 2023.

> **Décision ouverte D-GK-1 (identifiant provisoire, nœud de décision : modification du test décisif ; aucun défaut
> sous 48 heures)** — fenêtre du test B.
> - **(a)** : texte ci-dessus (population à fin 2022, fenêtre 2023–2026). Avantage : aucun
>   conditionnement sur l'issue proche, population indépendante de la moisson. Inconvénient : s'écarte de la lettre
>   « liens apparus de 2024 à 2026 » du message n° 261.
> - **(b) littérale** : mêmes 10 millions tirés à B0 ; après B1, les paires reliées en 2023 (selon notre moisson)
>   sortent de la population (un sous-ensemble d'un tirage uniforme reste uniforme dans la population restreinte) ;
>   étiquette = au moins un article du 1er janvier 2024 au 30 septembre 2026. Déclaré **conditionné sur l'issue 2023** :
>   le retrait ôte d'abord les positives les mieux classées, le biais joue **contre le modèle** à seuils fixes ; nombre
>   et part des paires retirées rapportés. Maxima inchangés (ceux de B0).
> - Dans les deux cas, l'autre fenêtre est rapportée en information (attente écrite en section Prédiction).
> - Le texte scellé (v3) ne gardera que la branche retenue.

**B4, témoins appariés** : positives = celles de l'échantillon B-i ; si elles dépassent 200 000 (SUPPOSÉ), 200 000
sont tirées par l'enfant 7. Pour chacune, k = 5 témoins (SUPPOSÉ) tirés (enfant 4) dans toute la population restée non
<<<FIN PIÈCE N9-1>>>

### Pièce N10-1 — `docs/notes/anteriorite-P-041-v1/collisionneur-organisme-coevolutif-v1/synthese-organisme-coevolutif-tour2-v1.md` (l. 1–76) — nœuds N10

Origine : main ; empreinte du fichier source `8a612a8f392abebe5ae883f9922ef421c11616040ea507824a3c12c59fb911f5` ; 1190 mots ; verdict et convergences ; règle 2 appliquée.

<<<DÉBUT PIÈCE N10-1>>>
# Synthèse — organisme coévolutif, étage III, tour 2 — v1

31 octobre 2026, 10:10 UTC. Rédacteur : session-depot (Opus 4.6). A Fable 5.1, B Opus 4.6, C Argon, D Kimi K3.1 Pro.

Pièces lues : les douze cellules de `run-organisme-coevolutif-tour2-e3-v1/cellules/` (empreintes égales à leurs compagnons) ; `question-etage3.md` ; `faits.md` (v5, 30 faits) ; `etat.md` (12 cellules OK, 8,41 USD) ; `synthese-organisme-coevolutif-v2.md` (tour 1, `1f6de90b…` — non relue en entier, sections 2 à 4 et 6 consultées pour comparaison).

## 1. Verdict

Tour exploitable : douze cellules au premier essai, aucun refus, aucune absence, 8,41 USD. La critique croisée (tour III.2) a produit une convergence majeure sur six points d'architecture : trajectoire commune du générateur aveugle ; permutation au niveau des réplications de défense (familles fixes) ; borne analytique de continuité sinon certificat non délivré ; trois jeux honnêtes disjoints ; contrôle négatif par bras réétiquetés ; banc de validation instrumentale avant toute dépense d'arène. Les quatre espèces divergent sur ce que reçoit le générateur informé, la statistique de rechute au protocole de Bailey, l'estimand du débordement et l'arrêt anticipé. Aucune espèce ne produit un préenregistrement complet qui puisse être scellé tel quel : chacun a au moins un point « illustratif » non gelé (budget, seuils, constante de Lipschitz).

## 2. Convergences nées de la critique croisée

### 2.1. Trajectoire commune du générateur aveugle

En régime aveugle, le générateur ne reçoit aucun score de défense (invariant de N-053, fait 4, VÉRIFIÉ) ; sa trajectoire est donc indépendante des défenses et peut être partagée par tous les bras. A-T3 l. 49 formule le principe : « une seule séquence de familles d'entraînement G, graine scellée, consommée par tous les bras ». C-T3 l. 35 apparie les archives cumulées. D-T3 l. 56–57 confirme. B-T3 l. 30 adopte la version faible (même archive, même ordre). Conséquence : l'état hérité devient le seul traitement de D1, non l'exposition aux familles.

### 2.2. Permutation au niveau des réplications de défense

Le plancher de valeur p à 5 grappes d'instances (1/32 ≈ 0,031) était fatal au tour III.1 sous correction de Holm (A-T2 l. 11 ; C-T2 l. 69). Les quatre corrigent :
- A-T3 l. 56–58 : K = 8 paires (Hér_k, Zéro_k), plancher 1/256, familles fixes conditionnées.
- B-T3 l. 12 : Holm retiré, un test par duel à α = 0,05, plancher 1/32 < 0,05.
- C-T3 l. 8 : P = 8 paires de graines appariées, 2^8 = 256 inversions, plancher ≈ 0,004 < α_{(1)}.
- D-T3 l. 56 : 16 paires H/Z, plancher 1/2^16.

Convergence : permutation par paire de runs appariés, familles fixes. Divergence : nombre de paires (8, 5, 8, 16).

### 2.3. Borne analytique de continuité

A-T2 l. 3 (iii) soulevait l'absence d'estimateur de la variation totale dans les certificats. Au tour III.3 :
- A-T3 l. 37 : « K doit être une borne fermée déclarée au schéma pour chaque classe. »
- C-T3 l. 10 (tableau) : « Si L_Lip > L_max ou si L_Lip·h > 0,10, le certificat est NON DÉLIVRÉ. »
- D-T3 l. 99–103 : constante de continuité vérifiée, « sans continuité, aucun certificat n'est délivré ».
- B-T3 l. 18 : accepte, mais la borne proposée porte sur θ ↦ TV(P_θ, P₀), qui ne borne pas |TPR(θ) − TPR(θ′)| (signalé par la synthèse du tour 1, section 2.7).

Convergence A, C, D : borne analytique fermée, non estimée par Monte-Carlo. B : en retard.

### 2.4. Trois jeux honnêtes disjoints

D-T1 proposait la calibration sur trois jeux. Au tour III.3 :
- A-T3 l. 91 : « n_cal tirages disjoints ; FA sur n_FA tirages disjoints ; TPR sur n_eval tirages disjoints ».
- B-T3 l. 25 : « troisième jeu honnête disjoint (calibration / évaluation FPR / test de rappel) ».
- C-T3 l. 15 (tableau) : échantillon honnête disjoint de vérification N_vérif = 50 000 (illustratif).
- D-T3 l. 95 : « divisés avant tout score en calibration, évaluation des fausses alertes et contrôles techniques ».

Convergence unanime.

### 2.5. Formule du certificat

Les quatre convergent vers L = min_grille(bornes inférieures) − terme de continuité − terme de calibration. Détails :
- A-T3 l. 70 : L = min_nœuds − K·h·√d_θ/2, avec bornes de Clopper-Pearson au niveau 1 − α_cert/N.
- B-T3 l. 96 : L = min_nœuds [borne inf. IC(rappel)] − L_lip · h, plus correction √(2 ln K)/√n_test.
- C-T3 l. 42–43 : L = min_m [R̂_LCB] − L_Lip · h − ε_cal, bornes de Šidák sur M nœuds.
- D-T3 l. 99–102 : L = min_j(ℓ_j − K h_j), bornes simultanées avec Bonferroni.

Convergence sur la structure. Divergence sur la correction de multiplicité (Bonferroni chez A et D, Šidák chez C, implicite chez B) et la propagation de l'incertitude de calibration (C seul l'ajoute explicitement).

### 2.6. Exclusion commune

A-T3 l. 92 et C-T3 l. 7 (acceptant C-b4) : « une famille non calibrée pour un bras quelconque sort de D1 pour tous les bras ». D-T3 l. 117 : « contrôle négatif ou simulation de niveau en échec : invalidation du pipeline concerné ». B-T3 l. 24 : « FPR mesuré > 1,5 % sur jeu d'évaluation → invalidation de la lecture ». Convergence implicite : l'estimand Δ porte sur un ensemble commun aux bras.

### 2.7. Plancher d'admissibilité relatif à P₀

A-T3 l. 93 : d_TV(P_f, R_f) ≥ τ_TV (illustratif 0,20). B-T3 l. 38 : TV(P_f, P₀) ≥ η_min (illustratif 0,10). C-T3 l. 17 : η_min^C = 0,85 (illustratif) dans C ; η_min^hors ∈ [0,25 ; 0,90] hors classe. D-T3 l. 90–91 : TV(P, P₀) ≥ η. Convergence unanime. Divergence sur la valeur (0,10 à 0,85 selon la strate et l'espèce) ; C est la seule à distinguer le plancher dans C (élevé, cohérent avec Neyman-Pearson) de celui hors C.

### 2.8. Familles ambiguës rapportées à part

A-T3 l. 94 : « S3 rapportée, exclue des estimands primaires ». B-T3 l. 21 : « les familles ambiguës sont rapportées à part, dans aucune des deux strates principales ». C-T3 l. 66 : strates 2 et 3 rapportées séparément. D-T3 l. 93 : « ambiguë, exclue du principal et utilisée seulement dans la sensibilité ». Convergence unanime.

### 2.9. Issue « inconclus »

A-T3 l. 34 : « renommée inconclus, sans attribution de cause ». C-T3 l. 38 : « falsifie l'hypothèse de puissance conditionnelle ex ante ». D-T3 l. 70 : « hypothèse de précision/puissance du plan falsifiée ». B-T3 l. 67 : « IC enjambant → non jugeable, falsifie la prédiction de puissance ». Convergence : un intervalle qui couvre le seuil n'est pas un verdict ; il invalide la prédiction de puissance du plan.

### 2.10. Banc de validation instrumentale avant dépense

A-T3 l. 142 : « expérience à faire en premier — validation R5 du bloc d'instruments ». B-T3 l. 155 : « établir ou réfuter la borne de continuité sur un sous-ensemble jouet ». C-T3 l. 109 : « banc de validation couplant garde, FPR randomisé, certificat jouet ». D-T3 l. 127 : « banc instrumental TV–calibration–certificat ». Convergence unanime : aucun lancement d'arène avant la réussite du banc instrumental.
<<<FIN PIÈCE N10-1>>>

### Pièce N10-2 — `registres/decisions.md` (lignes R-880, R-888, R-889, R-890, R-891) — nœuds N10

Origine : main ; empreinte du fichier source `b1d772171a6c78768d365fa78f6fe01886e6990b02e18938d4fc66b50c1b903c` ; 333 mots ; lignes de session-depot (main) ; règle 2 appliquée.

<<<DÉBUT PIÈCE N10-2>>>
| R-880 | 2026-10-31 |générateur au niveau des lois et des bornes, jamais d'une recette d'entrée, N-053, N-054), avec l'**examen final** au protocole de Bailey et collègues (défense figée, optimiseur sur les entrées d'un 8B, défense sortie de l'arène contre la base « instances seules », préenregistré) ; la voie 3 (couple détection et coût) en mesure rapportée. P-041 v2 sera écrite **après la synthèse du tour 1 de l'arène** (en cours), en y versant ce qu'elle ajoute ; l'examen final est une dépense de carte graphique : devis à part, rien n'est engagé.  [retiré, règle 2 : recommandation ou confiance d'auteur]| décision de Lazar (revendication). |
| R-888 | 2026-10-31 | **R-611 levée : la revue de sécurité extérieure a été réalisée et a donné son GO.** Le gel du pipeline opérationnel d'évasion est levé. Mot de Lazar : « la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel ». | nœud (Lazar). |
| R-889 | 2026-10-31 | **Examen final et estimation de la malléabilité : hors gel R-611.** Ces deux expériences ne tombent pas sous le gel du pipeline opérationnel. Mot de Lazar : « non ils sont hors gel ». Qualification directe par Lazar. | nœud (Lazar). |
| R-890 | 2026-10-31 | **Examen final et estimation de la malléabilité : lancement approuvé.** Mot de Lazar : « on les lance ». Les deux expériences sont qualifiées et autorisées au lancement. Préenregistrement à rédiger, sceller et contre-lire avant toute exécution (R1, R2). Le GO de dépense (devis de calcul GPU) reste un nœud séparé. | nœud (Lazar). |
| R-891 | 2026-10-31 | **Pire cas certifié : assemblage, pas méthode neuve.** Le trait « pire cas certifié sur lois synthétiques à paramètres bornés » est revendiqué comme assemblage (combinaison avec le contrôle), non comme une méthode neuve. Mot de Lazar : « ok ». Cohérent avec la collision partielle notée en R-861 (test d'hypothèses robuste). | nœud (Lazar). |
<<<FIN PIÈCE N10-2>>>

## Table des empreintes

| Pièce | Chemin | Partie | sha256 du fichier source | Mots |
|---|---|---|---|---:|
| 1 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-deux-espaces-v1/experience-v2/lancement-v2/verdict-validation-v1.md` | entier | `f5bf86b9d5001f363d0768cd88bebcc1f8e842711fa0c4c578d40debf13e8675` | 1846 |
| 2 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-deux-espaces-v1/experience-v2/lancement-v2/diagnostic-v5-v1/diagnostic-v5-v1.md` | entier | `2875f4adfd79ecb19143e9a583997c987686b9b2e9db4bbad35d2c8a68f064e8` | 2590 |
| 3 | `prereg/preenregistrement-bisociation-deux-espaces-v2.md` | l. 283–300 ; 555–586 ; 617–688 ; 689–735 | `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` | 5560 |
| 4 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | l. 1–78 | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` | 2637 |
| 5 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | l. 283–283 ; 296–296 | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` | 98 |
| 6 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | l. 336–356 | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` | 1102 |
| 7 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | l. 543–587 | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` | 1883 |
| 8 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | l. 619–619 | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` | 106 |
| 9 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | l. 639–704 | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` | 2725 |
| 10 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/calcul-puissance-pre-pilote-course-2-v6.sortie.txt` | RETIRÉE (budget de mots) | `` | 0 |
| 11 | `docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v6.md` | l. 20–36 ; 184–232 ; 370–443 | `13ef84f9fcee9f43914ba76748805a4f2bff2f30bc42de62f42a0600a97473ed` | 2544 |
| 12 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/contre-lecture-annexe-bras-meta-v1-brouillon1.md` | l. 19–22 ; 49–87 ; 125–146 | `db249b9356f8d19cd8c9811c3db184b0d7587eba97ed8386501e146434e24f1d` | 2369 |
| 13 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon1.md` | l. 18–30 ; 85–102 ; 116–224 | `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` | 2860 |
| 14 | `docs/notes/ideation-organisme-v1/contre-lecture-cl19-orchestrateur-v54-v1.md` | l. 14–22 ; 100–114 ; 149–172 | `f1cc6c1a974fcbe4efe4d7dfe0087333ea1103b9ad6aa0e98f9016f6d7c3f31e` | 1590 |
| 15 | `docs/notes/ideation-organisme-v1/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md` | l. 65–105 | `bbfdcb3c30d174dd7feeee9ba8dd20aeb7777c5f0e65aeb087e3c4388c743aa3` | 644 |
| 16 | `docs/notes/ideation-organisme-v1/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md` | l. 95–120 | `a3290bc7237057af11dd8a320d631b73293ffb41e55aef65e11f0b90ff79beb2` | 434 |
| 17 | `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon3.md` | l. 9–101 ; 166–176 ; 359–393 ; 687–698 | `1a229998fcbe7cd8dc45abeb559508ae8411f309059912c365bc02ae3b92e67c` | 4919 |
| 18 | `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` | l. 22–40 ; 83–83 ; 164–249 ; 250–262 | `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` | 1905 |
| 19 | `registres/decisions.md` | lignes R-630, R-634, R-635, R-638, R-643, R-660, R-661, R-674, R-675, R-678, R-679, R-680, R-685 | `80edac2f960d42098b4509c95604199874b83b9a612b7ca6d2af859870abcbbe` | 2135 |
| 20 | `docs/notes/ideation-organisme-v1/contre-lecture-cl18-orchestrateur-v53-v1.md` | l. 35–35 ; 156–156 | `0ce1d0b5a8c5016fdcb7262db3597bcc0320ddcd884dfb3d8821fa467230c52b` | 86 |
| SD-1 | `donnees/collisionneur-question-6-v1/run-question-6-e3-v1/etat.md` | entier | `71cd5a7248be6d9b963b6c1eb67e7a9126e85dab9b4dc213ece3f5752955131b` | 199 |
| SD-2 | `donnees/collisionneur-question-7-v1/run-question-7-e3-v1/etat.md` | entier | `28952d78ab42107a28f58eff7aac113021f1edd8dea21e6f010400089d0f269d` | 185 |
| SD-3 | `registres/decisions.md` | lignes R-866, R-868, R-869, R-870, R-871, R-873 | `b1d772171a6c78768d365fa78f6fe01886e6990b02e18938d4fc66b50c1b903c` | 790 |
| SD-4 | `docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md` | l. 1–20 ; 202–321 | `1c1618a2484b542e534b74fc12906212c6284d41d0bc691722e4a209499f67e9` | 1595 |
| N9-1 | `docs/notes/gu-krenn-v1/prereg-gu-krenn-reproduction-et-hors-echantillon-v2.md` | l. 40–95 ; 122–140 ; 220–240 | `7f32c4e0f841fe670b00bd726198770731a8edd4e09be54a4d302e035404a77b` | 1426 |
| N10-1 | `docs/notes/anteriorite-P-041-v1/collisionneur-organisme-coevolutif-v1/synthese-organisme-coevolutif-tour2-v1.md` | l. 1–76 | `8a612a8f392abebe5ae883f9922ef421c11616040ea507824a3c12c59fb911f5` | 1190 |
| N10-2 | `registres/decisions.md` | lignes R-880, R-888, R-889, R-890, R-891 | `b1d772171a6c78768d365fa78f6fe01886e6990b02e18938d4fc66b50c1b903c` | 333 |
