# Verdict de lecture — épreuve de la garantie de seuil du théorème de mise en œuvre aléatoire des audits (papier D, chantier 3 : budget d'audit borné) — v1

- Pièce décisive (classe A), lecture selon R1, R4 et R13. Date : 2026-11-24, rédigée de 12:54Z à 13:10Z environ (heure relevée par `date -u`).
- Lecteur neuf : session de lecture ouverte par la mère (`session_01Qi7Gr3Ggccg85kjmP654WC`), Opus 5.5, effort élevé. Il n'a écrit ni le préenregistrement, ni le script, ni les sorties, ni l'essai de fonctionnement ; il n'est pas la « fille 2 » qui a fait l'essai. Inscription « qui a lu quoi » faite avant toute lecture : `registres/qui-a-lu-quoi/inscription-lecteur-neuf-seuil-papier-d-v1.md` (commit `40ced4c9`).
- Ces résultats relèvent du papier D (une garantie mathématique sur le budget d'audit), pas d'un cloisonnement de moniteur : aucune sonde, aucun agrégateur ni aucun seuil de moniteur n'est en jeu.

## 1. Verdict

**Aucune réfutation. Verdict d'ensemble, selon la troisième case gelée : « tient en 137 points ; marge non nécessaire, donc garantie non éprouvée, en 0 ; non concluant en 1 », le point n° 31.** La formule « la garantie tient » sur toute la grille n'est **pas** prononcée, parce qu'elle exige, en chaque point admissible, une violation de classe « au-dessus » à marge nulle, et que le point n° 31 est « non concluant » à marge nulle par l'arrêt n° 6 (sensibilité à la tolérance), non par manque de violations.

Dans les 137 points, la conclusion écrite d'avance s'applique : « Pour le processus du théorème, la violation du seuil à marge nominale est sous δ/2 sans plafond et sous δ avec plafond, en des points où l'instrument voit la violation dès que la marge est retirée. La simulation ne contredit ni l'énoncé (c) ni l'étape de preuve ; elle ne les prouve pas et ne dit rien hors de leurs hypothèses. »

Au point n° 31, à marge nominale, l'étape unilatérale de la preuve et l'énoncé (c) tiennent aussi (violation sans plafond et violation plafonnée « sous »). Seule la lecture à marge nulle y est « non concluante » ; la garantie n'y est pas dite éprouvée.

Descriptif gelé : marge nécessaire, surdimensionnée d'un facteur ε/ε_emp compris entre 1,75 et 3,56 (médiane 2,49) sur les 137 points où la marge empirique a été estimée.

## 2. Pièces lues et sceaux vérifiés

| Pièce | Empreinte SHA-256 | Vérification |
|---|---|---|
| Préenregistrement scellé `papiers/D/prereg/prereg-seuil-chantier3-v3.md` | `4f3ee5c3a10b55d3a43a443b1418a006819d6e931f13247785b7afbf655b20e3` | égale au compagnon et à `controle_ia.scellement verifier` |
| Erratum 1 `papiers/D/prereg/prereg-seuil-chantier3-v3-erratum-1.md` | `411aba8156f166002c4ccb31337c9a36316326b04972e32214be64b092321f25` | idem |
| Déclaration de l'essai `papiers/D/resultats/seuil-v1/declaration-essai-de-fonctionnement-v1.md` | `617b4aa62b615756736a2c84401412e878f8bb58401d2dfb2abaf57be4f643c9` | égale au compagnon |
| Avis du contre-lecteur `papiers/D/audits/verification-script-seuil-v2.md` | `0e043c1cca329604df0963c0ae7d8401fd646ddabe9de369e3be8a0464607cbb` | égale au compagnon |
| Manifeste `runs/20261124-121411-seuil-chantier3/manifeste.json` | `a44f3ab69ccd5c051763a66d6335bfe363f9a4f8d8df4470f520c7711da720f7` | égale au compagnon ; égale au champ `manifeste_sha256` des sorties |
| Sorties scellées `diag/20261124-121411-seuil-chantier3/sorties-brutes.json` | `f739c1df19b015b57c0ec817b13feba10e36ffd2dbde63bb315649f4445954c6` | vérifiée **avant** ouverture |
| Script de la course `papiers/D/code/experience_seuil_chantier3_v3.py` | `535808bc8b5a79404db5257e3ab5770ad00820ec06bfbb492167ffb43b9602a2` | égale au compagnon, au manifeste et au contenu du commit `564c5919` |

Chronologie (journal git et registre des scellements du papier D) : préenregistrement scellé à 11:16:49Z ; avis du contre-lecteur sur l'essai, commit `08f726cc` à 11:41:54Z ; erratum scellé à 12:12:39Z ; script v3 au commit `564c5919` à 12:13:36Z ; manifeste créé à 12:14:17Z (dépôt propre, réserves vides) ; sorties scellées au commit `922d8f7f` à 12:44:54Z. La course a donc tourné après le scellement des deux textes qui font foi.

## 3. Validité de la course (établi)

- **Gardes sur les trois bancs témoins** : les sept gardes passent sur leur cas sain et détectent leur artefact ; aucun défaut ; valeurs de conception recalculées conformes, y compris les deux valeurs de l'erratum (2,6678 × 10⁻⁵ et 1,2193 × 10⁻⁷).
- **Admissibilité recalculée** : 138 points ; les six inadmissibles sont exactement ceux annoncés (n = 100, γ = 0,2, η = 1, C = 19 : points 14, 15, 62, 63, 110, 111) ; minimum de tours tenus 24 ; minimum d'audits attendus par tour tenu 2,5. Arrêt n° 3 non déclenché.
- **Contrôles d'instrument systématiques 1 à 4** : exécutés en chaque point (lu dans le code de `traiter_point`, qui les fait avant toute classe) ; liste des défauts d'instrument vide en chaque point et au total ; `course_invalide = false` ; journal de progression complet (138 sur 138, code de retour 0).
- **Contrôle 2 recalculé par le lecteur** : le plus grand rapport écart sur tolérance vaut 0,55.
- **Clés de graines** : 26 386 clés distinctes pour les points, chacune portant l'indice de son point ; 510 clés pour les bancs (indices 1000 à 1002), sans recouvrement ; aucune clé d'indice 999 (celui de l'essai).
- **Invariant entre violations**, contrôlé par le lecteur sur les comptes agrégés à chaque marge : violation sans plafond ≤ violation plafonnée ≤ violation sans plafond + dépassements. Tenu partout.
- **Relecture indépendante des classes** : le lecteur a recalculé chaque classement (bornes unilatérales de Clopper-Pearson au niveau 10⁻⁴) à partir des seuls comptes, par son propre code. **Aucun écart** avec les classes du script, ni aux quatre lectures décisives, ni aux six marges.
- **Aucune prolongation** n'a été déclenchée (aucun premier tirage « indéterminé », aucun « au-dessus » à marge nominale) ; **aucun audit renforcé** (aucun « trop propre », aucune réfutation).

Conclusion établie : course valide, aucun défaut d'instrument.

## 4. Lecture par point

### À marge nominale (λ = 1), 138 points

| Lecture | Classe finale | Comptes |
|---|---|---|
| Violation sans plafond V, contre δ/2 | « sous » en 138 points | 0 violation en chaque point (0 sur 13,8 millions de répétitions) |
| Violation plafonnée V′, contre δ | « sous » en 138 points | 618 au total, au plus 156 sur 100 000 (point n° 135), présentes en 25 points |
| Écart bilatéral D, contre δ (descriptif) | « sous » en 138 points | 33 au total, au plus 4 sur 100 000, en 17 points |

Verdict par point : (E) et (C) tiennent en chacun des 138 points admissibles. Aucune « garantie réfutée », à aucun grade. L'énoncé (a) n'est réfuté sur ce plan en aucun point (descriptif, hors du verdict).

### À marge nulle (λ = 0), 138 points

- « au-dessus de δ/2 » en 137 points : marge nécessaire, l'instrument y voit la violation.
- « non concluant » au **point n° 31** (K = 50, n = 1000, γ = 0,05, η = 10, C = 19, δ = 0,1) : premier tirage 91 744 violations sur 100 000, classé « au-dessus » ; le recomptage à la tolérance τ′ = 10⁻⁶ max(1, c) donne 91 732, soit 12 répétitions d'écart, au-delà des 10 permises par l'arrêt n° 6 ; le point est donc « non concluant » à cette marge (règle appliquée par le script, confirmée par le lecteur). Pas de bissection en ce point (elle exige « au-dessus » à λ = 0).
- « sous » (« trop propre ») : aucun point.

### Arrêt n° 6 ailleurs

Deux autres points sont sensibles à la tolérance, à λ = 0,1 seulement, marge non décisive : point n° 77 (13 répétitions d'écart) et point n° 124 (14). Effet : ces deux points ne sont pas comptés dans la lecture de la prédiction P3 à λ = 0,1 (voir § 5). Leur encadrement de bissection n'en dépend pas (λ⁻ = 0,25 et λ⁺ = 0,5 dans les deux cas).

## 5. Prédictions

| Prédiction | Lecture | Issue |
|---|---|---|
| P1a : à λ = 1, V ≤ δ/2, V′ ≤ δ, D ≤ δ partout | 138 points « sous » pour les trois | **tenue** |
| P1b : à λ = 1, V ≤ δ/20 partout | V = 0 partout ; borne basse unilatérale nulle, jamais au-dessus de δ/20 | **tenue** |
| P2 : à λ = 0, V ≥ 0,5 partout ; médiane ≥ 0,9 | plus petite fréquence 0,866 (point n° 11), borne haute unilatérale 0,870 ; médiane 0,970 (0,970 aussi sans le point n° 16) | **tenue** (le point n° 31, lu sur son premier tirage comme le veut le critère de P2, ne la réfute pas : 0,917) |
| P3 : V ne croît pas avec λ ; V > δ/2 partout à λ = 0,1 ; V ≤ δ/2 partout à λ = 0,75 | aucune hausse significative sur les 690 paires (test exact de Fisher, 10⁻⁵), et aucune hausse même brute ; λ = 0,1 : 136 points « au-dessus », 2 non comptés (sensibilité, points n° 77 et 124 ; lecture du lecteur : l'arrêt n° 6 rend le point « non concluant » à cette marge, assimilé au point indéterminé que P3 ne compte pas) ; λ = 0,75 : 138 « sous » | **tenue** (non lue en 2 points à λ = 0,1) |
| P4 : ε_emp/ε dans [0,20 ; 0,70] partout ; médiane dans [0,35 ; 0,55] ; médiane par η décroissante | ensemble de lecture 137 sur 138 (≥ 125 exigés ; le point n° 31 n'a pas de bissection) ; plage observée 0,281 à 0,571 ; médiane 0,402 ; médianes 0,514 (η = 1), 0,410 (η = 10), 0,323 (η = ∞) | **tenue** |

Hypothèses : H-a (garantie) tenue en 138 points à marge nominale ; H-b (nécessité d'une marge) tenue en 137 points, non concluante au point n° 31 ; H-c (prudence, 0 < ε_emp < ε) tenue en 137 points. Validité des bissections : les 137 tirages de confirmation sont « indéterminés » (attendu, puisque ε_emp vise V ≈ δ/2), aucun « au-dessus » ; l'encadrement λ⁻ε ≤ ε_emp ≤ λ⁺ε tient partout.

## 6. Descriptif, sans verdict

- Distance au seuil à λ = 1 : quantile d'ordre 1 − δ/2 de max x̂ − c, rapporté à ε, entre −0,71 et −0,38 (médiane −0,57). Cohérent avec ε_emp/ε ≈ 0,4.
- Budget épargné (B_ε − B_εemp)/B*_unif(c) : de 0,019 à 0,575, médiane 0,105, sur 137 points.
- Dépassement de budget à λ = 1 : de 0,09 % à 0,66 % selon le point. Sur les 828 couples point-marge, l'écart réduit entre le compte et sa probabilité exacte par convolution reste sous 3,33 en valeur absolue, de moyenne −0,09 ; quatre couples dépassent 3, un peu plus que les deux attendus sous une loi normale, sans portée sur un verdict (comptes petits, approximation normale grossière).
- Bras en boucle fermée : à λ = 0, au moins 99 999 violations sur 100 000 en chaque point ; à λ = 1, aucune. Aucune garantie n'y est énoncée.

## 7. Point n° 16, rapporté à part, avec la déclaration

- Configuration : K = 50, n = 100, γ = 0,2, η = 10, C = 4, δ = 0,05 (c = 3,179, ε = 0,867). Le lecteur a vérifié que c'est bien le seizième point de l'ordre lexicographique.
- **Vu avant la course** (déclaration, script v2, indice de point 999, graines hors course) : V « au-dessus » à λ = 0 ; V, V′, D « sous » à λ = 1 ; ε_emp/ε ≈ 0,40, bissection valide.
- **Course** (indice de point 16, graines de la course) : V à λ = 0 : 94 741 sur 100 000, « au-dessus » ; à λ = 1 : V = V′ = D = 0, trois classes « sous » ; λ = 0,1 : 59 800 ; 0,25 : 17 457 ; 0,5 : 442 ; 0,75 : 3 ; ε_emp/ε = 0,403, bissection valide (λ⁻ = 0,25, λ⁺ = 0,5) ; distance au seuil −0,573.
- Mêmes classes, même rapport à la précision déclarée. Aucune clé d'indice 999 dans la course.
- **Sensibilité du verdict au point n° 16 (établi)** : retiré, le verdict d'ensemble devient « tient en 136 points ; non concluant en 1 », sans autre changement ; P4 garde 136 points (≥ 125), médiane 0,401, médianes par η 0,514, 0,411, 0,323 ; P2 garde sa médiane 0,970.
- **Jugement du lecteur (R4)** : l'essai ne laissait aucune prise. Le préenregistrement était scellé avant lui. La différence du script v2 au script v3 ne porte que sur l'erratum (voir réserve 1). Les graines sont disjointes. Ce qui a été vu va dans le sens prédit, et ce point ne change aucun verdict. Je juge la course non affectée. Les trois conditions de l'avis du contre-lecteur sont remplies : déclaration jointe et point signalé ; lecteur distinct de la fille 2 ; script changé seulement pour l'erratum.

## 8. Audit de symétrie (R4) : zéro violation à marge nominale

Le résultat est « propre » dans le sens prédit : aucune violation sans plafond à λ = 1 en 138 points. Le préenregistrement l'admet comme confirmation s'il va avec les violations vues à λ = 0 au même point et les contrôles passés. C'est le cas en 137 points. Le lecteur a ajouté deux épreuves indépendantes, de son propre code, sans dépense, sur processeur et hors des graines de la course.

1. **Calcul exact** (programmation dynamique sur le compte cumulé d'audits), sur les 32 points à mémoire entière (η = ∞) calculables (toutes les configurations à n = 100, et K = 50 à n = 1000) :
   - Aux marges 0,25, 0,5 et 0,75, ainsi que pour V′ à λ = 1, les comptes de la course concordent avec les probabilités exactes. Le plus grand écart réduit est 2,56, sur 128 comparaisons.
   - Le lecteur a aussi recalculé ε et c : écart relatif nul.
   - **À λ = 1, la probabilité exacte de violation vaut au plus 2,7 × 10⁻⁷. Sur ces 32 points, le nombre total de violations attendu est 0,096.** Le zéro observé est donc attendu ; il ne trahit pas un instrument aveugle.
2. **Simulation indépendante** (R = 100 000 par cas, graines du lecteur), sur les deux points de plus forte violation plafonnée (n° 135 et 133, η = 1, K = 500), le point n° 16 et le point n° 0, à λ = 0,5 et λ = 1 :
   - Les écarts réduits entre la course et le lecteur restent sous 1,2 en valeur absolue.
   - En particulier, la violation plafonnée non nulle à λ = 1 est retrouvée : 156 contre 136 au point n° 135, 97 contre 93 au point n° 133.

Conclusion de l'audit : sans défaut. La lecture tient.

Pièces de l'audit et de la relecture :

| Pièce | Empreinte |
|---|---|
| `papiers/D/resultats/seuil-v1/lecture-v1/lecture_classes_et_predictions_v1.py` | `d1030da89fd9e0f4c4edcc68b67ac637a80a8a5302671f3d32e1f42543fd5c66` |
| sa sortie `sortie-lecture-classes-et-predictions-v1.txt` | `ad5d88f6da5c05bd7691c25e9389cae99f9ecbd17fed019084cc90e69e10fed4` |
| `audit_symetrie_exact_memoire_entiere_v1.py` | `4294ba07df18e847b7ab760f9cd4685873803c279437f9d5f8284f1719205c49` |
| sa sortie `sortie-audit-symetrie-exact-v1.txt` | `87912742200252b118687ec7d9b01766ed8d624239b39340ad238456a4408ee2` |
| `audit_symetrie_simulation_independante_v1.py` | `756d01e704f73563df295999936d2c65e04a3dcbc9a5092e17fc92743f0836b6` |
| sa sortie `sortie-audit-symetrie-simulation-v1.txt` | `06742c121bde884eb922ebe357af53760b1e7f86bc5d695f7f041d30e0adc91d` |

## 9. Réserves

**Établi.**

1. **Différence du script v2 au script v3.** L'avis du contre-lecteur demandait que la v3 ne change que `PREREG`, `PREREG_SHA`, les deux valeurs de conception et la mention de version. La v3 garde `PREREG` et `PREREG_SHA`. Elle ajoute le chemin et l'empreinte de l'erratum (`ERRATUM`, `ERRATUM_SHA`) et une garde de refus de départ sur le sceau de l'erratum. Elle change les deux valeurs et la mention de version. Rien d'autre (différence complète relue). La garde ajoutée ne peut qu'empêcher le départ ; elle ne touche ni aux tirages ni aux classements. **Jugement du lecteur** : écart à la lettre de la condition, conforme à son objet, sans effet sur les sorties.
2. **Choix déclarés de l'audit renforcé** (`audit_renforce_declenche_aussi_par_D`, référence de la prolongation dès qu'elle existe) : **sans objet**, l'audit renforcé n'a jamais été déclenché.
3. Durée de calcul : 30 minutes sur quatre processus, contre « quelques heures sur un cœur » annoncées. C'est cohérent, sans effet.

**Jugement du lecteur, hors des critères.** Au point n° 31, la violation à marge nulle (≈ 0,917, environ 18 fois δ/2) n'est pas mise en doute par son ampleur. La sensibilité de 12 répétitions sur 91 744 tient aux répétitions dont le maximum tombe entre les deux tolérances. Mais les critères gelés disent « non concluant », et le lecteur s'y tient. Requalifier ce point serait un écart au préenregistrement scellé, donc un nœud de Lazar. Le lecteur ne le propose pas.

## 10. Ce que ce verdict ne dit pas

Il ne vaut pas preuve du théorème. Il ne valide aucune sonde ni aucun protocole du programme. Il ne dit rien hors de la grille : autre marge de manœuvre, η = γ, ΔR ≠ 1, points inadmissibles, audits reconnaissables ou faillibles, entraînement par gradient stochastique. Il ne dit rien non plus de la boucle fermée (descriptive) ni de l'énoncé (b).
