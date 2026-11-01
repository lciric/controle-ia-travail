# Préenregistrement — comparaison à plusieurs bras des règles de choix de paire du bisociateur — v1, brouillon 1

**Statut : brouillon 1, non gelé, non contre-lu.** Écrit au gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad4371…`). Chaque valeur que Lazar doit fixer porte le marqueur du gabarit, avec la recommandation de l'auteur ; le validateur `controle_ia.prereg.problemes` les signale (sortie dans le LISEZMOI). Conception : `conception-comparaison-regles-paires-v1.md` (même dossier ; renvois « C § n »).

- Auteur : concepteur neuf (Opus) de la lignée conv-audit, branche `canal/conv-audit-n04`.
- Date (UTC) : 1er novembre 2026, rédaction à partir de 16:00 (heure lue par `date -u`).
- Commit du code d'analyse : aucun (brouillon ; code non commité, consigne) ; empreintes du code dans le LISEZMOI ; le commit sera écrit au gel.
- Documents qui font foi (chemin + empreinte) :
  - décision de Lazar : `registres/decisions.md`, lignes R-1049 et R-1051 (points 2, 3, 7) ;
  - antériorité : `brouillons/…/boucle-moisson-fiches-v1/anteriorite-boucle-moisson-fiches-v1.md`, `a953879ab6a96073909400be138bfbef603a57351a275837323c7e7370b2c2a8` ;
  - état des lieux Gu-Krenn : `docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md` (lu au commit `5145657f`), `1c1618a2484b542e534b74fc12906212c6284d41d0bc691722e4a209499f67e9` ;
  - rétrodiction de Swanson : rapport `057ef8a5314fba92b305a2e71fc4008a228aecd1e2a22598c2b85b64e362783b`, préenregistrement `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb`, métriques `code/mesures_v1.py` `f462dbd52ecd9181e387da1ff1ceb1a529f3bcd07e6ca85d83e9a5898af0888f` ;
  - bisociation à deux espaces, préenregistrement scellé v2 : `prereg/preenregistrement-bisociation-deux-espaces-v2.md`, `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` ;
  - pré-pilote, brouillon 10 (M9) : `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f` ; annexe du bras méta, brouillon 4 : `397e1cbc7483e7c5106bd859a77514605166e1fb699eb4b4ab5ed2730d15fb7c` ;
  - PDF : SciMuse 2405.17044 v4 `fcb49a059e17a25c351153a8022717aa594ddc279f6e276e204f1fbe9ce32af4` ; Science4Cast 2210.00881 v1 `88a48f8de98e000b2ad381838f9106a1a8344247b79b63e01f50f2fee346ec46`.

## Hypothèse

**H-paires (principale).** Parmi six règles de choix de paire de concepts — Gu-Krenn (leur code relancé sur notre corpus, ou leur méthode), « loin mais proche », méta « trou à structure commune », marche de Swanson A-B-C, prédiction de liens par voisinage (Adamic-Adar), nouveauté atypique d'Uzzi —, au moins une classe les paires jamais reliées avant une coupure mieux que le hasard, au sens de l'aire sous la courbe caractéristique de fonctionnement du récepteur, sur un graphe de concepts tiré des métadonnées d'arXiv et d'OpenAlex, sans aucun modèle de langage dans la génération des paires (fermeture algorithmique, R-1051 point 3). Chaque bras est une hypothèse de la famille (six comparaisons au hasard).

**H-panel (conditionnelle).** Parmi les bras qui battent le hasard en H-paires, au moins un produit, à partir des mêmes fiches, des fusions jugées plus intéressantes que celles de paires au hasard par un panel extérieur à l'aveugle (protocole de SciMuse).

**H-prospective.** Les écarts de H-paires se retrouvent, de même signe, sur des paires prédites à la date J et lues à J + 24 mois (fermeture prospective).

Hypothèses de travail : la cooccurrence future dans les titres et résumés est un indicateur — imparfait — qu'une paire « se fait » ; l'issue ne mesure pas une découverte (C § 12). Renvoi au programme : pôle scientifique automatique, bisociateur (R-601, R-619, R-638) ; aucune hypothèse du programme v2 n'est modifiée.

## Prédiction chiffrée et signe attendu

Écarts d'aire au hasard réalisé, en points (aire × 100), rétrodiction principale. Fourchettes tirées de la rétrodiction de Swanson (aires 0,94 à 0,96 pour les mesures de voisinage sur arXiv, coupure 2010) et de l'état des lieux Gu-Krenn (0,94 à 0,96 sur leur graphe ; Simpson seul 0,888), élargies pour le changement de corpus ; toutes SUPPOSÉES.

| Code | Bras | Signe | Fourchette prédite | Réfutation de la prédiction |
|---|---|---|---|---|
| P1 | prédiction de liens (Adamic-Adar) | + | +20 à +45 | écart ≤ 0 ou hors fourchette |
| P2 | Swanson A-B-C | + | +20 à +46 | idem |
| P3 | Gu-Krenn | + | +25 à +46 ; écart à l'allocation de ressources −3 à +5 (descriptif) | écart ≤ 0 |
| P4 | loin mais proche | + (confiance 0,6) | −5 à +20 | écart < −5 |
| P5 | méta | incertain (confiance 0,5) | −10 à +15 | hors fourchette |
| P6 | Uzzi transposé | − ou nul | −15 à +5 | écart > +5 |
| P7 | hasard (garde) | 0 | aire à moins de 4 erreurs-types de 0,5 | sinon arrêt G7 |
| P8 | panel, Gu-Krenn contre hasard | ≤ 0 (sens de SciMuse : −0,096 point, 1,94σ, 2405.17044 p. 7) | −0,3 à +0,1 point sur 5 | écart > +0,1 |
| P9 | panel, autres bras entrés | aucun signe prédit | −0,3 à +0,3 point ; issue la plus probable : « non concluant » à la cible Δ = 0,5 | — |
| P10 | prospective (J + 24 mois) | mêmes signes que P1 à P6 | aires plus basses de 0 à 10 points (champ en évolution rapide) | signe inversé pour un bras entré |
| P11 | strate « loin » (M5) | P4 et P5 meilleurs en strate « loin » qu'en général, relativement au hasard | — | descriptif |

## Métrique

- **M1 (primaire)** : aire sous la courbe caractéristique de fonctionnement du récepteur, paires réalisées contre non réalisées, égalités pour moitié, calculée par `mesures_v1.metriques` (rétrodiction de Swanson, telle quelle, empreinte vérifiée au chargement) ; pour chaque bras, écart à l'aire du hasard réalisé sur les mêmes paires ; erreur-type et test de DeLong apparié (`regles_paires_v1.comparer_au_hasard`), unilatéral (bras > hasard).
- **M2** : part des paires réalisées parmi les k premières (précision à k, espérance sous départage aléatoire des égalités) ; intervalles à 95 % par 1 000 rééchantillonnages des paires (mêmes tirages pour tous les bras).
- **M3** : aire sur les ensembles d'évaluation publiés de Science4Cast, par configuration (δ, c, w), bras applicables ; descriptive.
- **M4** : aire appariée degré–âge (chaque positive contre 5 négatives de sa case : classes log2 des deux degrés à T, classes d'âge des deux concepts) ; secondaire.
- **M5** : aire par strate d'éloignement (cos_domaine ≤ médiane des candidats, > médiane) ; secondaire.
- **M6** : précision moyenne ; écart à l'allocation de ressources ; descriptifs.
- **Panel** : note d'intérêt de 1 (« pas intéressant ») à 5 (« très intéressant ») ; estimateur : modèle mixte note ~ bras + effet aléatoire expert + effet aléatoire fusion ; repli déclaré : moyennes par fusion, test unilatéral de Welch par bras contre hasard ; intervalles à 95 %.
- Issue d'une paire : ≥ w documents d'après (coupure, coupure + h] qui la contiennent, vocabulaire de la coupure.

## Seuil

- Niveau familial : 0,05, unilatéral, Holm sur six comparaisons au hasard (épreuve 1) ; familles séparées pour la prospective et le panel. Fixé (R-1051 point 7 : « multiplicité contrôlée »).
- Puissance visée : 0,80 au pire rang de Holm pour 10 points d'aire (annexe : ≈ 182 positives contre hasard réalisé). Fixé.
- Jugeabilité (G6) : ≥ 50 positives dans l'échantillon, sinon « non lançable ». Fixé (accord du collisionneur).
- Coupure T, horizon h, placebo : À REMPLIR (recommandation : T = 31 décembre 2021, h = 3 ans, placebo T′ = 31 décembre 2017 ; décision « coupure »).
- Seuil d'issue w : À REMPLIR (recommandation : w = 3 en principal, w = 1 en secondaire).
- Nombre de paires candidates N : À REMPLIR (recommandation : 10⁶, tirage uniforme, graine `crp-candidats`).
- Corpus et vocabulaire : À REMPLIR (recommandation : décision « corpus », option (a)).
- Critère de bascule de Gu-Krenn vers « leur méthode » : À REMPLIR (recommandation : décision « panne Gu-Krenn », option (a)).
- Entrée par la strate « loin » : À REMPLIR (recommandation : non ; M5 descriptif ; décision « biais de proximité »).
- Tolérance de la vérification extérieure (Science4Cast ; rejeu de la rétrodiction de Swanson) : À REMPLIR (recommandation : 0,01 d'aire sur Science4Cast ; 10⁻³ sur le rejeu de Swanson).
- Panel : écart cible, nombre de fusions par bras, notes par fusion : À REMPLIR (recommandation : Δ = 0,5 point, 50 à 66 fusions par bras pour trois bras, 3 notes par fusion ; décision « panel »).
- Dates de lecture prospective : À REMPLIR (recommandation : J + 12 mois descriptif, J + 24 mois principal).
- Plafond de dépense de l'épreuve 1 : À REMPLIR (recommandation : 80 dollars américains, sur devis de session-depot).

## Plan d'analyse

1. **Données** : métadonnées d'arXiv (titre, résumé, catégories, date de première version) et d'OpenAlex (lieu, références, citations annuelles) ; aucun texte intégral ; vocabulaire par la chaîne `create_concepts/` d'Impact4Cast sur les seuls documents d'avant (C § 4.1). Moisson déclarée et empreintée avant tout calcul.
2. **Validation du code avant toute lecture décisive** : rejeu de la rétrodiction de Swanson et banc Science4Cast (M3), tolérances du « Seuil » ; un échec arrête le code, pas un bras.
3. **Fenêtre placebo** (T′) : taux de base π̂, k = ⌈50/π̂⌉ (arrondi au millier supérieur), seuils libres des bras méta et Uzzi (quantiles fixés sur T′) ; **aucune métrique de bras lue sur T′ ne décide**.
4. **Scores à T** : chaque bras (graines `crp-bras-<nom>`, dérivées de la racine du manifeste par `regles_paires_v1.graine_tache`, R9) ; gardes G1 à G5, G8 ; scores écrits, empreintés, **scellés** (jeton) avant les issues.
5. **Issues** (G10), garde G6, garde G7.
6. **Comparaisons** : M1 de chaque bras contre le hasard réalisé (DeLong apparié, unilatéral), Holm (famille de six) ; un bras « non produit » (garde, source absente) compte comme non-rejet, déclaré.
7. **Secondaires** : M2, M4, M5, M6 ; bras contre bras et contre l'allocation de ressources : descriptifs avec intervalles.
8. **Règle d'entrée gelée** (`regle_entree_course_2`) : un bras entre en épreuve 2 seulement s'il est rejeté par Holm en 6. Hasard toujours présent.
9. **Prospective** : à J, listes et scores scellés (C § 4.4) ; lectures aux dates fixées ; Holm séparé.
10. **Panel** (si au moins un bras entre) : vivier commun de fiches ; F paires par bras (priorité tirée, M9) ; fusions écrites par une consigne figée ; 10 % de fusions dégradées et 5 % de doublons plantés ; notes à l'aveugle ; clé scellée ; modèle mixte ; Holm sur les bras entrés.
11. **Verdict** : sous-agent neuf (R13), critères ci-dessous, scellé, soumis à Lazar.

## Critères de lecture gelés

| Issue observée (épreuve 1, par bras) | Verdict |
|---|---|
| rejet de Holm, écart dans la fourchette prédite | bras **retenu** ; entre en épreuve 2 |
| rejet de Holm, écart au-dessus de la fourchette | retenu **avec réserve R4** : audit de symétrie (fuite, degré, M4) avant l'entrée |
| pas de rejet, écart > 0 | **non concluant** ; n'entre pas |
| écart ≤ 0 | **ne bat pas le hasard** ; n'entre pas |
| garde levée ou bras non produit | **non produit**, compté ; n'entre pas |
| aucun bras rejeté | « aucune règle ne bat le hasard en rétrodiction » ; épreuve 2 non lancée |
| tous les bras rejetés avec des écarts proches (< 2 points entre eux) et M4 nul | « le graphe décide, pas la règle » : réserve, audit du degré |

| Issue observée (panel, par bras entré) | Verdict |
|---|---|
| rejet de Holm et garde de discrimination passée | bras **préféré par le panel** (intérêt, pas valeur) |
| pas de rejet | **non concluant** à l'écart cible (pas « équivalent ») |
| écart négatif à plus de 2 erreurs-types | **inversion** (sens de SciMuse) ; rapportée |
| garde de discrimination échouée | **panel non discriminant** : aucune lecture des bras |

Prospective : même table que l'épreuve 1 ; un signe inversé pour un bras retenu → réserve sur le bras, rapportée à Lazar. Audit de symétrie (R4) déclenché par : écart au-dessus de la fourchette ; hasard à plus de 3 erreurs-types de 0,5 ; un bras « loin » qui bat les bras de voisinage ; un panel unanime.

## Liste d'arrêt

| Condition | Action |
|---|---|
| G1 : scores changés par les documents d'après | arrêt du bras ; correction du code ; aucune lecture |
| G2 : vocabulaire hors documents d'avant | arrêt du run |
| G3 : modèle de langage déclaré ou module chargé | arrêt du run |
| G4 : candidat déjà relié, doublon | arrêt du run |
| G5 : score non fini ou en nombre faux | arrêt du bras (« non produit ») |
| G6 : moins de 50 positives | « non lançable » ; aucune lecture |
| G7 : hasard hors de 4 erreurs-types | arrêt ; audit du tirage |
| G8 : adaptateur factice en course, hasard absent | arrêt du run |
| G10 : issues demandées sans jeton ou scores changés | arrêt ; lecture invalidée |
| métriques de Swanson altérées ou absentes | arrêt |
| vérification extérieure hors tolérance | arrêt du code concerné |
| dépense au plafond | arrêt de l'étape ; ligne de GO nouvelle |
| panel : garde de discrimination échouée | aucune lecture des bras |
| écart au préenregistrement | nœud : Lazar |

## Contre-lecture

À REMPLIR — contre-lecture R2 par un sous-agent neuf (ni Opus auteur de ce brouillon, ni lecteur de la conception), qui reçoit : ce brouillon, la conception, `regles_paires_v1.py`, les essais, le calcul de puissance et sa sortie, l'état des lieux Gu-Krenn, le préenregistrement de la rétrodiction de Swanson, le M9 du pré-pilote ; empreinte du brouillon relu et de son rapport à inscrire ici.
