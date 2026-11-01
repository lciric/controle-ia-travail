# Conception — comparaison à plusieurs bras des règles de choix de paire du bisociateur — v1

Concepteur neuf (Opus) de la lignée conv-audit, 1er novembre 2026, rédaction commencée à 15:55 UTC (heure lue par `date -u`).
Mandat : **décision de Lazar du 1er novembre, 15:47 UTC** (`registres/decisions.md`, ligne R-1051, point 7, surnom « GO comparaison des règles de paires »), sur la reformulation de R-1049 (« on teste plusieurs bras alors : Gu-Krenn et les autres possibles ») ; R-1051 point 2 (Gu-Krenn : « relancer leur code sur notre corpus : go ; puis si ça ne marche pas, leur méthode, pas leur modèle ») et point 3 (les deux fermetures de la circularité : « ok »).
Ce qui n'a pas été fait : aucun commit, aucun compagnon `.sha256`, aucun fichier existant modifié, rien lu sous `donnees/`, aucun `git fetch` (les notes Gu-Krenn ont été lues dans une référence locale déjà présente, commit `5145657f`, par `git show`), aucun appel de modèle, aucune dépense, aucun résultat décisif lu (R1) : seuls des mondes jouets.
Règles appliquées : R1, R4, R5, R7 (tout chiffre d'article reste « à vérifier sur PDF » ; les pages citées sont l'index physique de l'extraction `pdftotext`), R8, R9, R10 (aucun processus lancé hors premier plan), R12.

## Verdict en dix lignes

1. Les sept bras tiennent sur **une interface commune** : entrée = vue « avant coupure » d'un graphe de concepts daté (et, pour l'épreuve 2, des fiches ramenées à des sacs de concepts) ; sortie = un score par paire candidate. Quatre bras sont codés et éprouvés sur graphe jouet (`regles_paires_v1.py`, 20 essais réussis) ; Gu-Krenn, méta et Uzzi ont leur adaptateur factice, qui refuse d'entrer en course (garde G8).
2. **Puissance de l'épreuve 1 : ce n'est pas le goulot.** Pour 10 points d'aire (0,60 contre 0,50) à 0,8 de puissance au pire rang de Holm (α/6 unilatéral) contre un hasard *réalisé* : **≈ 182 positives**, soit **≈ 66 000 paires** au taux de base de la rétrodiction de Swanson (0,275 %) et ≈ 18 400 à 1 % ; simulation : 0,812 et 0,825 (annexe, § 6). Avec 10⁶ paires, l'écart détectable tombe à ≈ 2,6 points.
3. **Le goulot est la validité** : l'issue « paire apparue après la coupure » est une cooccurrence lexicale ; elle récompense la proximité (fermeture de triangles). Les règles « loin » (basique, méta, Uzzi) sont **structurellement désavantagées** par la règle d'entrée gelée. Je le signale (R4, R8) et propose une analyse secondaire par strates d'éloignement ; changer la règle reste à Lazar (décision « biais de proximité »).
4. **Fermeture algorithmique** : aucun modèle de langage nulle part dans la génération des paires, **vocabulaire compris** (gelé sur les seuls documents d'avant ; les sujets et concepts d'OpenAlex, attribués par un classifieur entraîné après la coupure, sont exclus de la génération). Garde G3 (module de modèle de langage chargé = arrêt) et G2.
5. **Fermeture prospective** : à la date J de la moisson, chaque bras rend ses listes ; elles sont scellées ; lecture principale à J + 24 mois, intermédiaire descriptive à J + 12 mois.
6. **Gu-Krenn** : le code Impact4Cast (licence MIT) se relance tel quel sur notre corpus pour l'extraction des concepts (algorithme RAKE, sans modèle de langage), les arêtes, les 141 traits et l'entraînement ; seuls des adaptateurs d'entrée et de sortie sont écrits. Critère « ne marche pas » à geler (décision « panne Gu-Krenn ») ; repli : leur méthode recodée, pas leur modèle. **Aucun poids publié** : réentraînement obligatoire (machine louée, nœud de dépense).
7. **Épreuve 2** (panel extérieur à l'aveugle, protocole SciMuse) : chère et peu sensible. Écart-type des notes ≈ 1,32 (tiré de SciMuse) ; détecter 0,5 point sur 5 avec trois bras demande ≈ 50 à 66 fusions par bras et 600 à 800 notes ; 0,3 point en demande ≈ 1 650 à 2 200 ; les écarts vus par SciMuse (≈ 0,1) sont hors de portée. Issue la plus probable : « non concluant ».
8. SciMuse donne une **prédiction signée** : les paires à la Gu-Krenn tendent sous le hasard en intérêt jugé (1,94 écart-type, 2405.17044 p. 7). Je l'inscris telle quelle : Gu-Krenn devrait gagner l'épreuve 1 et ne pas gagner l'épreuve 2.
9. Multiplicité : **Holm** sur les six comparaisons au hasard (famille par épreuve) ; e-BH (Benjamini–Hochberg sur e-valeurs) écarté ici (échantillon fixe, petite famille ; erratum du dépôt sur son plafonnement).
10. Huit décisions pour Lazar (§ 10), dont trois nœuds : dépense (machine louée, moisson), panel (recrutement, effectif, coût), portée de la règle d'entrée.

---

## 1. Ce qui est déjà établi (lu, empreintes vérifiées)

| Pièce | Ce qu'elle apporte ici | Empreinte |
|---|---|---|
| Antériorité de la boucle (`boucle-moisson-fiches-v1/anteriorite-boucle-moisson-fiches-v1.md`) | SciMuse, Science4Cast, HindSight, MiroGraph, Novelpy absent ; « aucun composant vierge » | `a953879a…` (conforme à son `.sha256`) |
| État des lieux Gu-Krenn (`docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md`, lu par `git show 5145657f:…` : **absent de cette branche**, présent sur les branches de session-depot ; R11 vérifié) | Code Impact4Cast (MIT, tête `d2af4f3d…`), données Zenodo CC-BY, aucun poids, 141 traits, réseau de quatre couches de 600, pièges 1 à 6 | `1c1618a2…` (conforme) |
| Pré-pilote, brouillon 10, M9 (l. 293-310) | Trois bras sur fiches (basique, Gu-Krenn modèle ou substitut, méta) ; une paire par bras ; aucune comparaison | `ea940d56…` |
| Annexe du bras méta, brouillon 4, § 1-3 | Six niches, communication faible (table 0 à 3), structure commune forte, bande d'éloignement non extrême | `397e1cbc…` |
| Rétrodiction de Swanson (`retrodiction-swanson/`) | Code scellé des métriques (`mesures_v1.py`, `f462dbd5…`) ; formule de la marche ; allocation de ressources gagnante (−0,82 point pour Swanson à 10 000) ; taux de base 0,2752 % | rapport `057ef8a5…`, préenregistrement `7a4868aa…` |
| Bisociation à deux espaces, préenregistrement scellé v2 | Score du bras basique s = (1 − cos²)^8,5 × (κ + 0,05) (§ 5) | `e821e875…` (conforme) |
| Synthèse du collisionneur « boucle moisson » (Q3, Q5, Q6) | Rétrodiction définie pour les paires concept–concept seulement ; allocation de ressources manque aux témoins ; jugeabilité (≥ 50 positives attendues) ; « tel quel » contesté (Q6-a) | `48a514de…` (copie du bloc-notes) |
| PDF : SciMuse 2405.17044 v4 ; Science4Cast 2210.00881 v1 ; Krenn–Zeilinger 1906.06843 v2 ; Sourati–Evans 2306.01495 v1 | Protocole du panel, valeurs ; banc ; méthode | `fcb49a05…`, `88a48f8d…`, `d9031cba…`, `90ccea69…` (conformes) |

**Divergence Q6-a tranchée par Lazar** (R-1051 point 2) : « tel quel » = relancer leur code sur notre corpus ; si cela ne marche pas, leur méthode. Ce document l'applique.

---

## 2. Interface commune

**Population de paires.** Épreuve 1 : paires de **concepts** (i, j), i < j, **jamais reliées** dans le graphe d'avant, deux extrémités de degré ≥ 1 (garde G4). Épreuve 2 : paires de **fiches**, notées par le pont « fiche = sac de concepts » (forme du bras Gu-Krenn de M9 : moyenne des m plus hauts scores de paires de concepts (c_a, c_b) non reliées ; `score_paire_fiches`). La synthèse (Q3, accord large) interdit de mélanger les types de paires dans un même classement : chaque épreuve a sa population.

**Entrée d'un bras** (`VueAvant`) : vocabulaire gelé avant la coupure ; matrice des cooccurrences n(X, Y) ; fréquences documentaires ; nombre de documents ; répartition de chaque concept entre catégories (domaine) ; lieux (revues) par concept ; documents d'avant réduits à (concepts, lieu). **Rien d'après la coupure** : les issues vivent dans un objet séparé, lisible seulement avec le jeton des scores scellés (G10).

**Sortie** : un score fini par paire candidate (G5) ; l'ordre décroissant classe. Égalités : traitées par les métriques reprises telles quelles (précision à k en espérance sous départage aléatoire ; aire avec égalités pour moitié).

**Déclarations obligatoires de chaque bras** : `nom`, `reelle` (faux pour un adaptateur), `utilise_modele_de_langage` (faux, G3), `repris_tel_quel` (chemin ou lien), `code_ici`. Elles entrent dans le manifeste du run (R9).

---

## 3. Les sept bras

| Bras (surnom) | Règle | Repris tel quel | Codé ici | État v1 |
|---|---|---|---|---|
| **Hasard** (témoin obligatoire) | permutation uniforme ; secondaire : hasard stratifié par classes log2 des degrés | `score_uniforme`, `score_stratifie` de `retrodiction-swanson/code/mesures_v1.py` (empreinte vérifiée au chargement) | strates de degrés | codé, éprouvé |
| **Basique « loin mais proche »** | s = (1 − cos²_domaine)^8,5 × (κ + 0,05) | forme et constantes du préenregistrement scellé de bisociation v2, § 5 (e = 8,5, β = 1, ε = 0,05) | transposition aux concepts : domaine d'un concept = répartition de ses documents d'avant entre catégories (catégorie principale arXiv, choisie par les auteurs : aucun modèle) ; κ = Jaccard des voisinages d'avant | codé, éprouvé |
| **Gu-Krenn** | réseau entièrement connecté (quatre couches cachées de 600) sur 141 traits (41 de réseau, 100 de citations), entraîné de y − 3 vers y | code Impact4Cast (MIT) : `create_concepts/` (extraction de mots-clés RAKE — Rapid Automatic Keyword Extraction —, seuils 9 et 6), `create_dynamic_edges/`, `features_utils.py` (avec `get_norm_features` figé, piège 5 de l'état des lieux), `train_model_utils.py` | adaptateurs d'entrée (nos documents au format de leur `get_single_article_string`) et de sortie (fichier de scores) ; étape manuelle `s5_improve_manually_concepts.py` remplacée par une liste d'exclusion figée avant coupure (déclaré) | adaptateur factice |
| **Méta « trou à structure commune »** | 1[communication faible] × 1[structure commune forte] × 1[éloignement dans la bande] × (1 + p · s) | annexe du bras méta, brouillon 4 (fiches) | transposition au graphe : niches = communautés du graphe d'avant (algorithme de Louvain, graine fixée) ; communication = densité d'arêtes entre niches, normalisée ; structure commune = voisins communs d'une troisième niche ; éloignement = distance entre niches dans le graphe des niches ; seuils fixés sur la fenêtre placebo (§ 4.2), jamais sur la fenêtre décisive | adaptateur factice |
| **Swanson A-B-C** | S = ½ [K/r(A) + K/r(C)], K = Σ_B n(A,B) n(B,C) idf(B)/r(B) | formule du préenregistrement de la rétrodiction de Swanson, § 7 (moyenne des deux sens) | calcul matriciel sur le graphe (le code d'origine travaille sur documents × termes) | codé, éprouvé (valeur exacte à la main) |
| **Prédiction de liens** (voisinage, sans apprentissage) | Adamic-Adar Σ 1/ln deg(B) sur les voisins communs | définitions AA, RA, CN, PA du même § 7 | Jaccard ; **allocation de ressources (RA) gardée comme référence à battre** (gagnante de la rétrodiction de Swanson ; accord à quatre du collisionneur, Q5) — descriptive, hors famille | codé, éprouvé |
| **Nouveauté atypique d'Uzzi** | pour la paire (u, v) : z-scores des paires de lieux (revues de u × revues de v) contre un modèle nul par échange qui préserve les marges ; score = −z au 10e centile, restreint aux paires de conventionnalité (z médian) haute | Novelpy (github.com/Kwirtz/novelpy ; indicateur « Atypicality » ; arXiv 2211.10346 ; **licence non vérifiée**, entrée JSON ou MongoDB) | transposition des articles aux paires de concepts (Uzzi note des articles par leurs références) ; SUPPOSÉ, décision « Uzzi transposé » | adaptateur factice |

**Ce que chaque bras demande comme données.** Hasard, basique, Swanson, liens, méta : titres, résumés, dates, catégories (métadonnées). Gu-Krenn : en plus, citations annuelles des documents d'avant (`counts_by_year` d'OpenAlex), pour ses 100 traits de citation. Uzzi : lieux de publication (OpenAlex `primary_location.source`) et modèle nul.

**Antériorité (R8).** Chacun de ces bras existe (Swanson 1986 ; Liben-Nowell et Kleinberg pour les mesures de voisinage [SUPPOSÉ, non vérifié sur PDF] ; Uzzi et collègues 2013 ; Gu et Krenn 2025 ; Sourati et Evans 2023 pour l'idée « hypothèses étrangères », non retenue comme bras). La comparaison des sept sur deux épreuves, avec règle d'entrée, n'a pas été trouvée : question, pas trou ; aucune revendication d'architecture.

---

## 4. Épreuve 1 — rétrodiction à date de coupure

### 4.1 Corpus et graphe (métadonnées seules)

- **Documents** : métadonnées d'arXiv (titre, résumé, catégories, date de première version), toutes catégories, pour que « loin en domaine » ait un sens ; complétées par OpenAlex (lieu, références, `counts_by_year`) par identifiant. Aucun texte intégral.
- **Vocabulaire** : chaîne `create_concepts/` d'Impact4Cast relancée **sur les seuls documents d'avant** (RAKE, filtres, seuils 9 et 6 : leur code) ; liste d'exclusion figée à la place de leur revue manuelle. Garde G2.
- **Arêtes** : deux concepts sont reliés quand ils apparaissent ensemble dans le titre ou le résumé d'un document (leur règle ; recherche de sous-chaîne sans limite de mot, reproduite telle quelle ; variante « mot entier » en secondaire).
- **Candidats** : paires jamais reliées avant la coupure, au moins une extrémité « spécifique » au groupe de catégories du contrôle des intelligences artificielles (cs.LG, cs.AI, cs.CL, cs.CR, stat.ML ; part de ses documents d'avant ≥ 0,6, règle de la rétrodiction de Swanson) ; tirage uniforme de **N = 10⁶ paires** (recommandé, § 6).
- **Exclu de la génération** : sujets et concepts d'OpenAlex (attribués par un classifieur entraîné en 2024 sur des documents postérieurs : fuite de vocabulaire), tout plongement de phrases, tout modèle de langage.

### 4.2 Coupure, horizon, issue

- Coupure principale **T = 31 décembre 2021**, horizon **h = 3 ans** (issues du 1er janvier 2022 au 31 décembre 2024 : fenêtre complète, stable dans les deux sources). Fenêtre **placebo** T′ = 31 décembre 2017, h = 3 : sert à fixer les seuils libres (méta, Uzzi, k de la précision) et à estimer le taux de base ; **aucune métrique de bras n'y décide**.
- Issue d'une paire : **≥ w documents** d'après la contenant ; w = 3 recommandé (comme la rétrodiction de Swanson ; robuste au bruit de la sous-chaîne), w = 1 en secondaire.
- Ordre (G10) : scores calculés, écrits, **empreintés et scellés avant** le calcul des issues.

### 4.3 Fermeture algorithmique (décision de Lazar, R-1051 point 3)

Aucun modèle de langage dans la génération des paires : ni pour le vocabulaire, ni pour les arêtes, ni pour les scores. Les bras Gu-Krenn (réseau entièrement connecté sur traits de graphe), méta (communautés) et Uzzi (z-scores) n'en ont pas besoin. Gardes : G3 (un bras qui déclare un modèle, ou un module `openai`, `anthropic`, `transformers`… chargé dans le processus, arrête tout) ; G1 (scores inchangés quand on remplace tous les documents d'après) ; G2 (vocabulaire d'avant). Ce que la fermeture **ne** couvre **pas** : la dérive des sources (OpenAlex « Walden », retraits et récupérations de résumés, piège 1 de l'état des lieux) ; elle est traitée par la lecture sur arXiv en principal et un pont de comptes.

### 4.4 Fermeture prospective (R-1051 point 3)

À la date J (fin de la moisson), chaque bras réel tourne sur le graphe à J : il rend (a) ses 10 000 premières paires sur tout l'espace candidat et (b) ses scores sur un échantillon commun de 10⁶ paires tirées avec une graine fixée. Les fichiers, la liste des documents (identifiants et dates) et le vocabulaire sont empreintés et scellés le jour même (commit sur le dépôt privé, empreintes recopiées dans `registres/` par session-depot). **Aucune issue n'est calculée avant J + 12 mois** (lecture intermédiaire, descriptive) **et J + 24 mois** (lecture principale, mêmes métriques, famille de Holm séparée). Le pipeline d'issues est figé à J (vocabulaire de J : un concept né après J ne compte pas). C'est la seule fermeture valable pour les fusions de l'épreuve 2, écrites par un modèle de langage.

### 4.5 Métriques gelées

| Code | Métrique | Rôle |
|---|---|---|
| M1 | **Aire sous la courbe caractéristique de fonctionnement du récepteur** (paires réalisées contre non réalisées), égalités pour moitié (`mesures_v1.metriques`, tel quel) ; écart au hasard réalisé, test de DeLong apparié, unilatéral | **primaire** ; décide la règle d'entrée |
| M2 | **Part des paires réalisées après la coupure** parmi les k premières (précision à k, tel quel) ; k fixé sur la fenêtre placebo pour que le hasard attende ≥ 50 positives (k ≥ 50/π̂ ; ≈ 18 200 à 0,275 %) | secondaire, intervalles par rééchantillonnage (1 000 tirages) |
| M3 | **Score Science4Cast** : aire sur leurs ensembles d'évaluation publiés, par configuration (δ, c, w), pour les bras applicables (§ 4.9) | vérification extérieure, descriptive |
| M4 | Aire **appariée degré–âge** (positives contre k négatives de la même case de degrés et d'âges, état des lieux § 4.4) | secondaire : ce qu'un bras sait au-delà de « populaire et ancien » |
| M5 | Aire **par strate d'éloignement** (cos_domaine ≤ médiane contre > médiane) | secondaire : biais de proximité (§ 7) |
| M6 | Précision moyenne ; écart à l'allocation de ressources | descriptif |

### 4.6 Témoin hasard

Permutation uniforme, graine dérivée par tâche ; son aire doit rester à moins de 4 erreurs-types de 0,5 (G7 : un « hasard » qui voit l'issue est pris). Hasard stratifié par degrés en secondaire. Le hasard est **réalisé** (pas la constante 0,5) : sa variance entre dans le test, ce qui double environ les positives requises (§ 6).

### 4.7 Puissance (annexe reproductible : `calcul-puissance-comparaison-regles-paires-v1.py` et sa sortie)

| Taux de base π | positives requises (contre hasard réalisé, α/6) | paires N | écart détectable à N = 10⁶ |
|---|---|---|---|
| 0,1 % (SUPPOSÉ) | 182 | 182 000 | 4,25 points |
| 0,275 % (rétrodiction de Swanson) | 182 | 66 182 | 2,55 points |
| 1 % (Science4Cast, « 1-3 % », p. 5, à vérifier) | 184 | 18 400 | 1,35 point |

Contre la constante 0,5 : ≈ 90 positives. Simulation binormale (DeLong du module, 400 répétitions) : 0,812 (π = 1 %) et 0,825 (π = 3 %), pour 0,80 visé. Bras contre bras (0,70 contre 0,60, corrélation des aires 0,5) : ≈ 93 positives. **Recommandation : N = 10⁶** (coût de calcul faible ; puissance réservée aux analyses secondaires appariées et stratifiées).

### 4.8 Multiplicité

Famille de l'épreuve 1 : les **six comparaisons au hasard** (Gu-Krenn, basique, méta, Swanson, liens, Uzzi), unilatérales, **Holm** au niveau familial 0,05. Familles séparées : prospective (J + 24 mois), épreuve 2. Comparaisons bras contre bras et contre l'allocation de ressources : descriptives, avec intervalles, sans décision. e-BH : valide sous dépendance quelconque, utile pour des e-valeurs séquentielles ; ici l'échantillon est fixe et m = 6 : Holm est plus puissant et plus simple ; l'erratum du dépôt (`erratum-multiplicite-e-bh-v1.md`) montre le coût d'une erreur d'arrêt des e-valeurs.

### 4.9 Banc Science4Cast

- **Ce qu'il mesure** (2210.00881 v1, à vérifier sur PDF) : un réseau sémantique de l'intelligence artificielle, 64 719 concepts (RAKE et outils de traitement de la langue) tirés de 143 000 articles arXiv d'apprentissage automatique de 1992 à 2020 (p. 3) ; 17 892 352 arêtes uniques (p. 4) ; tâche : parmi 10 millions de paires non reliées en 2021 − δ (condition de degré c), classer selon la probabilité d'avoir au moins w arêtes en 2021 ; δ ∈ {1, 3, 5}, c ∈ {0, 5, 25}, w ∈ {1, 3} ; métrique : aire (p. 5). L'extraction donne « d(v_i) ≤ c » : sens de l'inégalité à vérifier à l'œil.
- **Comment on s'y compare** : les bras applicables (hasard, Swanson si les multiplicités d'arêtes sont fournies, liens, méta topologique, Gu-Krenn méthode sur traits de réseau seuls) tournent sur leurs données ; on rapporte l'aire par configuration à côté des valeurs publiées (attachement préférentiel, voisins communs, meilleures équipes). Rôle : **valider nos implantations** (cas sain extérieur, R5) et situer, jamais décider. Basique et Uzzi : non applicables (ni catégories ni lieux dans leurs données, à vérifier).
- **Limites** : intelligence artificielle seulement, jusqu'en 2021 (avant l'essor des grands modèles de langage) ; vocabulaire construit sur tout le corpus 1992-2020 (fuite de vocabulaire par rapport à 2021 − δ) ; aires « quasi déterministes » au-delà de 99,5 % pour w = 3 (p. 6 : plafond, aucune discrimination) ; aire gonflée par le degré (l'attachement préférentiel est fort) ; cooccurrence, pas idée ; licence des données à vérifier (`github.com/artificial-scientist-lab/FutureOfAIviaAI`).

---

## 5. Épreuve 2 — jugement à l'aveugle par un panel extérieur (protocole SciMuse)

**Ce que SciMuse a fait** (2405.17044 v4, index physique, à vérifier) : 110 chefs de groupe de la société Max Planck ont noté 4 451 idées (84,3 % de 5 280 notes possibles), 48 par personne, 16 par condition (paire de concepts à fort impact prédit, paire au hasard, sans paire), sur une échelle d'intérêt de 1 (« pas intéressant ») à 5 (« très intéressant ») (p. 7) ; moyennes 2,350 ± 0,034, 2,446 ± 0,035, 2,414 ± 0,036 ; « faible indice (1,94σ) » que les paires à fort impact prédit sont moins intéressantes que les paires au hasard (p. 7) ; 41 % des invités ont participé (p. 5) ; idées personnalisées pour deux chercheurs, notées par l'un d'eux.

**Notre transposition.**
- Vivier : **les mêmes fiches** pour tous les bras (fiches non aiguillées de la course en cours, étiquetées par deux lecteurs neufs sur la liste fermée du vocabulaire, comme M9) ; chaque bras retenu choisit F paires distinctes ; hasard toujours présent ; coïncidences réglées par la règle de priorité tirée de M9.
- Fusion : même consigne figée, même modèle et même version, mêmes paramètres, sans nom de bras ; format du texte I.
- Panel : chercheurs extérieurs du contrôle et de la sûreté des intelligences artificielles, **recrutés par Lazar** ; chaque fusion notée par 3 experts ; ≈ 30 notes par expert ; ordre tiré ; clé des bras scellée et ouverte au verdict ; question principale : intérêt de 1 à 5 (formulation de SciMuse) ; secondaires descriptives : plausibilité, nouveauté pour l'expert.
- Garde de discrimination (R-1051 point 4 : « pertinence jugée en aveugle contre des cas dégradés ») : 10 % de fusions **dégradées** plantées (paire incohérente, texte brouillé) et 5 % de doublons ; si le panel ne note pas les dégradées au-dessous des autres (écart < 0,5 point, unilatéral à 0,05), lecture « panel non discriminant ».
- Analyse : modèle mixte (note ~ bras + effet expert + effet fusion) ; repli déclaré : moyennes par fusion, test unilatéral par bras contre hasard ; Holm sur les bras entrés.
- **Effectif** (annexe § 6 ; s ≈ 1,32 tiré de SciMuse ; corrélation intra-fusion 0,1 à 0,3 SUPPOSÉ) : cible recommandée **Δ = 0,5 point** → 50 à 66 fusions par bras si trois bras entrent (600 à 800 notes, 20 à 27 experts) ; 59 à 79 si six (1 239 à 1 659 notes). Δ = 0,3 : 138 à 184 par bras (trois bras).
- **Coût illustratif** : fusions ≈ 0,204 dollar américain chacune (devis v6 de la course 2, cité par le brouillon 10) → moins de 60 dollars ; notes : nul si bénévoles (comme SciMuse), ≈ 4 dollars la note si payées (4 minutes à 60 dollars de l'heure, SUPPOSÉ) → ≈ 2 400 à 3 200 dollars pour trois bras à Δ = 0,5.

**Ce qu'elle ajoute** : un jugement humain de l'idée produite, pas d'une cooccurrence ; la chaîne entière (fiche → paire → fusion) ; le test direct de l'inversion de SciMuse (impact prédit contre intérêt).
**Ce qu'elle ne peut pas conclure** : la vérité, la faisabilité ou la réalisation future d'une idée (HindSight : nouveauté jugée corrélée négativement à la réalisation, ρ = −0,29, à vérifier) ; un effet de bras séparé de l'effet du rédacteur des fusions (rédacteur commun, interaction possible) ; un écart inférieur à ≈ 0,4 point à coût raisonnable ; une généralisation hors du panel recruté ; aucune rétrodiction (le rédacteur connaît l'après-coupure).

---

## 6. Règle d'entrée en épreuve 2 (gelée par Lazar)

Un bras n'entre en épreuve 2 que s'il **bat le hasard sur l'épreuve 1** : rejet de Holm sur M1 (aire, contre hasard réalisé, DeLong apparié, unilatéral, famille de six, 0,05), rétrodiction principale, gardes toutes passées. Codée : `regle_entree_course_2`. Le hasard entre toujours, comme témoin. Aucun bras n'entre → épreuve 2 non lancée, lecture « aucune règle ne bat le hasard en rétrodiction ». Je lis « course 2 » comme l'épreuve 2 de cette comparaison ; si Lazar visait la course 2 de l'organisme (trois bras sous GO-2026-10-31-04), l'appliquer serait un écart à un préenregistrement en cours : nœud (décision « portée de la règle d'entrée »).

---

## 7. Biais de proximité de la règle d'entrée (R4, R8)

La rétrodiction récompense ce qui se relie vite : des concepts voisins (fermeture de triangles). La rétrodiction de Swanson le montre : allocation de ressources 0,9574, attachement préférentiel 0,8897. Or trois bras cherchent exprès le « loin » : basique (poids (1 − cos²)^8,5 qui écrase les paires d'un même domaine), méta (communication faible entre niches), Uzzi (combinaisons atypiques, rares par construction). **La règle gelée peut les exclure pour ce qu'ils sont, non pour ce qu'ils valent.** Ce n'est pas une raison de la changer seul : je propose M5 (aire par strate d'éloignement) en secondaire préenregistré, et je soumets à Lazar l'option d'une entrée par la strate « loin » (décision « biais de proximité »). Symétrie : un bras « loin » qui battrait largement le hasard sur toutes les paires serait aussi suspect (audit R4 : vérifier qu'il ne prend pas des paires d'un même domaine mal étiqueté).

---

## 8. Gardes R5 (chacune éprouvée : cas sain et artefact, `essais/test_regles_paires_v1.py`)

| Garde | Ce qu'elle arrête | Cas sain | Artefact pris |
|---|---|---|---|
| G1 absence de fuite | scores modifiés par les documents d'après | quatre bras codés | bras qui lit les documents complets |
| G2 vocabulaire d'avant | concept absent des documents d'avant | vocabulaire construit | concept né après la coupure imposé |
| G3 sans modèle de langage | bras déclarant un modèle ; module chargé | quatre bras | déclaration ; faux module `openai` |
| G4 candidats | paire reliée, doublon, non ordonnée | candidats tirés | trois artefacts |
| G5 scores | nombre de scores, valeur non finie | zéros | valeur indéfinie ; longueur fausse |
| G6 jugeabilité | moins de 50 positives | 60 positives | 10 positives ; horizon vide de bout en bout |
| G7 hasard au taux de base | « hasard » hors de 4 erreurs-types | permutation | « hasard » qui voit l'issue |
| G8 bras réels | adaptateur factice en course ; hasard absent | hasard + Swanson | trois factices ; course sans hasard |
| G9 graines | flux non reproductibles | même racine, mêmes empreintes | racine changée, empreintes différentes |
| G10 issues après scellement | issues sans jeton ; scores changés | jeton valide | sans jeton ; scores inversés après scellement |
| (métriques) | métriques de Swanson altérées ou absentes | empreinte `f462dbd5…` | fichier altéré ; fichier absent |

Contrôle symétrique (R4) : dans un monde jouet **sans** fermeture de triangles, aucun bras n'entre (écarts < 0,05) ; dans le monde à fermeture, Adamic-Adar et Swanson entrent, le basique non (aire 0,524, p = 0,16) — ce qui illustre le § 7.

---

## 9. Vérification extérieure

1. **Science4Cast** (§ 4.9) : nos bras de voisinage doivent retrouver les valeurs publiées de leurs témoins à une tolérance fixée d'avance (À GELER) ; sinon arrêt du code, pas des bras.
2. **Gu-Krenn, voie R-a de session-depot** (préenregistrement v2, non scellé, `7f32c4e0…` selon R-873) : reproduction de leur banc (fig. 6, p. 7 : 0,9455 et 0,9442 pour IR — seuil d'impact en citations — égal à 10) avant tout usage de leur code sur notre corpus.
3. **Rétrodiction de Swanson** : nos implantations AA, RA, CN, PA et Swanson rejouées sur son jeu doivent redonner ses valeurs publiées (0,9419 ; 0,9574 ; 0,9396 ; 0,8897 ; 0,9595) à 10⁻³ près (le code d'origine travaille sur documents × termes : écart de calcul, pas de définition).
4. **Bancs voisins**, descriptifs : PreScience (combinaison future, arXiv intelligence artificielle 2023-2025), Alien Space (16 068 articles sur les modèles de langage) ; MiroGraph (Impact4Cast rejoué hors physique).
5. **Personnes** : contre-lecture R2 du préenregistrement par un sous-agent neuf ; verdict R13 par un sous-agent neuf ; relecteur extérieur de niveau B (R-1051 point 1) sur le préenregistrement scellé et le code.

---

## 10. Décisions pour Lazar

**Décision « corpus ».** Quel corpus et quel vocabulaire pour l'épreuve 1 ?
Enjeu : « loin en domaine » n'a de sens que si le corpus couvre plusieurs domaines ; le volume dicte la machine.
Options : (a) tout arXiv (métadonnées), candidats touchant le groupe du contrôle des intelligences artificielles — avantage : domaines variés, métadonnées libres ; inconvénient : vocabulaire de centaines de milliers de concepts, machine de 64 Go. (b) Les seules catégories cs.LG, cs.AI, cs.CL, cs.CR, stat.ML — avantage : petit, proche du sujet ; inconvénient : « loin » réduit à des sous-catégories, basique et méta affaiblis. (c) La moisson en vrac d'OpenAlex (R-863, 197 681 œuvres) avec ses `concepts` et `topics` — avantage : déjà faite ; inconvénient : pas de résumés, nœuds attribués par un classifieur postérieur (fuite de vocabulaire).
Recommandation : (a), confiance 0,6. Défaut sous 48 heures : (a).

**Décision « coupure ».** Coupure, horizon et seuil d'issue.
Enjeu : un champ jeune laisse peu de futur ; une coupure récente laisse une fenêtre incomplète.
Options : (a) T = fin 2021, h = 3, w = 3, placebo fin 2017 — avantage : fenêtre complète, robuste ; inconvénient : avant l'essor des grands modèles de langage. (b) T = fin 2022, h = 3 (2023-2025) — avantage : plus récent ; inconvénient : fenêtre close fin 2025, sources en dérive (Walden). (c) w = 1 en principal — avantage : plus de positives ; inconvénient : bruit de sous-chaîne.
Recommandation : (a), confiance 0,55. Défaut : (a).

**Décision « panne Gu-Krenn ».** Quand dit-on que leur code « ne marche pas » ?
Enjeu : la bascule vers « leur méthode » doit être décidée d'avance, pas au vu des résultats.
Options : (a) bascule si l'une : ne tourne pas après deux jours de travail d'adaptateurs d'entrée et de sortie ; exige de changer leur logique ; dépasse le plafond du devis ; ou la voie R-a manque sa tolérance — avantage : objectif ; inconvénient : deux jours est arbitraire. (b) Bascule au jugement de session-depot, consigné — avantage : souple ; inconvénient : ouvert au biais.
Recommandation : (a), confiance 0,7. Défaut : (a).

**Décision « biais de proximité ».** La règle d'entrée gelée défavorise les bras « loin » (§ 7) ; faut-il une seconde porte d'entrée ?
Enjeu : exclure le basique, le méta et Uzzi pour leur nature, non leur valeur.
Options : (a) garder la règle gelée seule, M5 descriptif — avantage : la règle de Lazar telle quelle ; inconvénient : biais connu d'avance. (b) Entrée aussi par la strate « loin » (M5, même famille de Holm, douze comparaisons) — avantage : teste chaque bras sur sa cible ; inconvénient : modifie une règle gelée, puissance divisée.
Recommandation : (a) avec M5 préenregistré et rapporté, confiance 0,5 (choix de fond : à Lazar). Défaut : (a).

**Décision « portée de la règle d'entrée »** (nœud). « Course 2 » = épreuve 2 de cette comparaison (lecture retenue), ou course 2 de l'organisme ?
Options : (a) épreuve 2 seulement — avantage : aucun écart au pré-pilote ; inconvénient : la course 2 de l'organisme garde des bras non validés. (b) Aussi la course 2 de l'organisme — avantage : cohérence ; inconvénient : écart au GO-2026-10-31-04 et au préenregistrement en cours.
Recommandation : (a), confiance 0,6. Pas de défaut : nœud.

**Décision « panel »** (nœud : contact extérieur, dépense). Effectif et rémunération.
Options : (a) cible Δ = 0,5, ≈ 20 à 27 experts bénévoles, ≈ 30 notes chacun — avantage : faisable ; inconvénient : ne voit que les grands écarts. (b) Δ = 0,3, ≈ 70 experts ou rémunération (≈ 9 000 dollars, illustratif) — avantage : sensibilité ; inconvénient : coût, recrutement. (c) Pas d'épreuve 2 avant la lecture prospective — avantage : rien à payer ; inconvénient : aucun jugement humain avant deux ans.
Recommandation : (a), confiance 0,55. Pas de défaut : nœud (Lazar recrute et envoie).

**Décision « dépense épreuve 1 »** (nœud). Devis illustratif (§ 11) : 15 à 60 dollars ; plafond proposé 80.
Recommandation : GO sur devis de session-depot, après la voie R-a. Pas de défaut : nœud.

**Décision « Uzzi transposé ».** Comment noter une paire de concepts par la nouveauté atypique ?
Options : (a) 10e centile des z-scores des paires de lieux (u × v), restreint à la conventionnalité haute (§ 3) — avantage : fidèle à l'indicateur ; inconvénient : transposition SUPPOSÉE. (b) Noter les documents d'après par Novelpy et compter les paires qu'ils créent — avantage : Uzzi tel quel ; inconvénient : ce n'est plus une règle de choix *avant* la coupure (inutilisable pour le bisociateur).
Recommandation : (a), confiance 0,5. Défaut : (a).

---

## 11. Ordre, dépendances, devis illustratif

**Ordre.** (0) Contre-lecture R2 du préenregistrement, décisions ci-dessus, GO de dépense. (1) Moisson des métadonnées d'arXiv (instantané public ; volume et licence à vérifier) et complément OpenAlex (lieux, références, `counts_by_year`) ; **la moisson en vrac R-863 ne suffit pas** (aucun résumé, ni `counts_by_year`) mais ses identifiants servent au pont de comptes ; **le coffre n'est pas concerné**. (2) Banc Science4Cast et rejeu de la rétrodiction de Swanson : validation du code. (3) Voie R-a de Gu-Krenn (préenregistrement de session-depot), puis leur code sur notre corpus, ou bascule (décision « panne Gu-Krenn »). (4) Fenêtre placebo : taux de base, k, seuils méta et Uzzi. (5) Scellement du préenregistrement ; scores à T, scellés ; issues ; métriques ; Holm ; verdict R13 ; GO. (6) Le jour J de la moisson : listes prospectives scellées. (7) Épreuve 2 pour les bras entrés, après recrutement.

**Devis illustratif** (tout SUPPOSÉ ; à refaire par session-depot).
| Poste | Estimation |
|---|---|
| Métadonnées d'arXiv | 0 dollar (instantané public) |
| Complément OpenAlex | ≈ 0,40 dollar pour 197 681 œuvres (3 954 pages, synthèse Q3-b, recalculé) ; ≈ 5 dollars pour ≈ 2,5 millions (allocation gratuite d'un dollar par jour) |
| Machine louée (64 Go, RAKE sur ≈ 2,5 millions de résumés, graphe, traits, entraînement Gu-Krenn 8 à 30 heures de processeur par configuration selon l'état des lieux) | 24 à 72 heures à 0,3 à 0,6 dollar de l'heure : ≈ 7 à 45 dollars |
| Épreuve 1, total | ≈ 15 à 60 dollars ; plafond proposé 80 |
| Épreuve 2 | fusions < 60 dollars ; notes : 0 (bénévoles) à ≈ 3 200 dollars (trois bras, Δ = 0,5, payées) |

---

## 12. Réserves

1. Issue = cooccurrence lexicale, pas découverte (rétrodiction de Swanson, réserve 3) ; la rétrodiction mesure la règle sur le terrain, non la valeur des idées.
2. Biais de proximité de la règle d'entrée (§ 7).
3. Transpositions SUPPOSÉES : basique (domaine d'un concept), méta (niches = communautés), Uzzi (paires de lieux) ; le pont fiche → paire de concepts suppose que la validité passe des concepts aux fiches.
4. Gu-Krenn sur notre corpus = un **autre graphe et un autre entraînement** : on teste leur code et leur méthode, jamais leur modèle publié (inexistant).
5. Dérive des sources (OpenAlex Walden ; `counts_by_year` révisés).
6. Épreuve 2 sous-dimensionnée pour les écarts plausibles (≈ 0,1) ; « non concluant » est l'issue la plus probable.
7. Chiffres d'articles : extraction automatique, index physique des pages, tous « à vérifier sur PDF » (R7) ; écart-type 1,32 dérivé, non publié.
8. Les notes Gu-Krenn ne sont pas sur la branche `canal/conv-audit-n04` ; lues dans une référence locale de session-depot.
9. Le basique code `(κ + 0,05)` avec κ = Jaccard des voisinages : sur le jouet il ne bat pas le hasard ; cela ne prédit rien du réel, mais montre que le poids d'éloignement domine.

## 13. Fichiers de ce dossier

`conception-comparaison-regles-paires-v1.md` (ce document) ; `preenregistrement-comparaison-regles-paires-v1-brouillon1.md` ; `regles_paires_v1.py` ; `essais/test_regles_paires_v1.py` ; `calcul-puissance-comparaison-regles-paires-v1.py` et `-sortie.txt` ; `LISEZMOI-comparaison-regles-paires-v1.md`. Empreintes : dans le LISEZMOI (aucun compagnon `.sha256`, consigne).
