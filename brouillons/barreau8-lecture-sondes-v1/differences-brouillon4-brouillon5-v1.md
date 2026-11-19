# Différences entre le brouillon 4 et le brouillon 5 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 4 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon4.md`, empreinte `2306803543563e732e1ecbca8452e237810fa0bfc872e23b28d14acdcc589b7b`.
- Contre-lecture du brouillon 4 (Opus 5.5) : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon4-v1.md`, empreinte `79be6f7eec2534cb9b01cc20ecc3b8720fb21952965ee09912a979cff0a57c30` (vérifiée, lue en entier).
- Brouillon 5 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon5.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 00:54Z et 01:02Z (`date -u`). Le brouillon 5 est fabriqué par programme à partir du brouillon 4, par remplacements contrôlés (chaque texte cherché doit paraître le nombre de fois attendu, sinon rien n'est écrit) ; trois passages sont remplacés en entier : la justification du budget de la recette de puissance, le point « Sous-échantillon d'activité brute », l'essai de la chaîne (chapeau, (i), (ii), (iii)). Aucune section n'est réécrite en entier.

## 1. Remarques de la contre-lecture du brouillon 4

| n° | objet | état | où, dans le brouillon 5 ; vérification faite ; adaptation |
|---|---|---|---|
| C-1 (bloquante) | action dont le premier identifiant est un jeton de fin : aucun jeton noté | traitée, une adaptation | « Passe », point « Action sans jeton noté » (texte de remplacement repris) ; garde de réception r5 ; garde P6 ; liste d'arrêt, ligne 11 ; ligne L6 ; plan, point 2 ; trace (compte par condition) ; essais R5 (« Code », « Essais exigés »). **Adaptation** : au lieu de « sautée au profit de l'action suivante », le sous-échantillon est tiré dans la liste des actions d'au moins un jeton noté (rangs multiples de 16 ou de 128, et la dernière) : aucun cas ne reste à trancher (action vide en dernier rang, deux vides de suite) ; au plus 161 et 21 actions, la borne de taille tient |
| C-2 | composition des lots ; une passe par action | traitée | « Passe », point « Passe avant » ; garde P7, « Seconde passe » ; textes repris. Vérifié : la note d'interface, question (5), dit que la dose se fixe pour tout le modèle |
| C-3 | l'audit et le défaut D1 visaient des fichiers de la course | traitée | Audit, contenu (1) et défaut (D1) : recontrôle contre l'index livré et les comptes de la trace ; textes repris |
| C-4 | vocabulaire de l'état par unité non établi par la note | traitée, **selon la consigne de la session mère et non selon le texte de remplacement** | I-9 : hypothèse déclarée du texte ; D-12 : contrôle mécanique à la réception de l'extrait, **refus d'ouvrir si un autre mot paraît** (le contre-lecteur proposait « condition non jugée, ligne S5 ») ; « Seuil », condition jugée, (a) et (b) ; ligne S5 ; liste d'arrêt, ligne 3. Le refus couvre aussi une phrase du dommage hors des quatre (cohérence, choix du rédacteur). Vérifié : note d'interface, ligne 68 (« non relue ici ») |
| C-5 | r6 ne voit pas une mauvaise couche ; capture de la première passe | traitée, une précision | « Ce que le côté des moniteurs n'observe plus », point (3) ; point « Sous-échantillon ». **Précision** : la couche est dite tenue par le code de la ligne `CODE-PASSE-IIB` et la garde P2 (le contre-lecteur citait « P2, P3, P4 et P10 ») ; le repère r8 n'en donne qu'un indice |
| C-6 | lecteur unique de w et de b | traitée | « Scores par action » ; r6 ; en-tête (code cité : `premier_test_ia/figees.py`, avec empreinte). Vérifié dans le code : `lire_sondes` (ligne 56), biais dans l'index (ligne 40), b = −w·μ (`sondes/evaluation.py`, ligne 81) |
| C-7 (mineure) | P3 : jeton de fin intérieur ; appel du décodage | traitée | Garde P3, (b) et (c), artefact de plus. Ajout du rédacteur : l'appel du décodage est une hypothèse déclarée (la note dit seulement « sans les jetons spéciaux ») ; s'il diffère, la garde arrête à la première action |
| C-8 | P10 et actions très courtes | traitée | Garde P10 : actions de 4 jetons notés ou plus, au moins 95 %, au moins 10 actions ; texte repris |
| C-9 (mineure) | trace : empreintes des adaptateurs, fraction de P10 par condition ; repère de couche | traitée, une adaptation | Trace (liste fermée) et r4. **Adaptation** : le repère descriptif de couche est calculé du côté des moniteurs sur le sous-échantillon livré (garde de réception, point r8, sans seuil), non écrit dans la trace : la liste fermée de la trace ne s'allonge pas d'une grandeur de plus et le repère ne dépend pas du côté exposé. La perte (5) le nomme |
| C-10 (mineure) | S1 : la phrase reçue comme cause | traitée | Ligne S1, texte repris |
| C-11 (mineure) | « ordre lexicographique » | traitée | Sous-échantillon ; index ; P7 ; P10 : « ordre du tri des chaînes de Python (par points de code) » ou « ordre des clés » |
| C-12 (mineure) | raisonnement du budget de la recette | traitée | Plan, point 10 : environ 12 s par répétition, 3,3 heures et 10 heures, marge d'un cinquième ; le raisonnement par le carré du nombre d'actions est retiré ; le budget de douze heures est inchangé |
| décision 1 | scores par jeton des neuf sondes | écrite sous (b) | Voir § 2 |

Remarques refusées : **aucune**. Quatre reprises avec adaptation déclarée : C-1, C-4, C-5, C-9.

## 2. Cadre de la session mère

| objet | où |
|---|---|
| Option (t1) retenue ; limite déclarée gardée | « Passe », décision de taille (« Retenue par la session mère ») ; point (3) de « Ce que le côté des moniteurs n'observe plus » |
| Clés `LIVRAISON-PASSE-IIB` et `ETATS-COURSE-IIB` accordées, au registre `registres/sondes-iib-v1.md` | « Code, registre et contrôle de conformité » |
| Tolérance 10⁻⁹ × E approuvée ; argument du vérificateur en une phrase | r6 |
| **Option (b) : scores par jeton des neuf sondes livrés aussi** | « Passe » : bloc de décision (défaut (a), liste fermée (b-1) à (b-6) des passages qui reprennent leur forme du brouillon 4) ; table des tailles ; point « Scores par jeton des neuf sondes » ; livraison en six sortes de fichiers ; r5, r6 (jeton par jeton), **r7** (maximum égal sans tolérance et moyenne à 10⁻⁹ × M, sur toutes les actions) ; « Métrique » (bras de diagnostic recalculé du côté des moniteurs pour les sondes) ; essai de la chaîne (injection sur un seul jeton) ; audit (2), (D2) ; liste d'arrêt, ligne 10 |
| Section « Contre-lecture » | Entrée « Contre-lecture 3 » (brouillon 4, empreintes) ; l'entrée ouverte est renommée « Contre-lecture finale (texte rempli) » (aussi dans les champs ouverts et la liste d'arrêt, ligne 2) |

## 3. Taille exacte de la livraison, pire cas (2 560 actions de 400 jetons)

| fichier | calcul | octets |
|---|---|---|
| scores par action, `float64` | 2 409 × 2 560 × 2 × 8 | 98 672 640 |
| scores par jeton des neuf sondes, `float64` | 9 × 1 024 000 × 8 | 73 728 000 |
| activité brute, couche 15, 161 actions, `float32` | 161 × 400 × 4 096 × 4 | 1 055 129 600 |
| activité brute, couches 7 et 23, 21 actions chacune, `float32` | 2 × 21 × 400 × 4 096 × 4 | 275 251 200 |
| **total** | | **1 502 781 440** (1,50 Go ; marge de 497 218 560 sous 2 000 000 000) |

Index, trace et bordereau : moins de 0,01 Go (non comptés au total exact). Sous (a) : 1 429 053 440.

## 4. Changements de la propre initiative du rédacteur

1. **Garde r7** : égalité sans tolérance pour le maximum ; tolérance 10⁻⁹ × M pour la moyenne — proposée avec recommandation, sans source.
2. **Repère r8** calculé du côté des moniteurs (voir C-9) ; il étend l'usage permis du sous-échantillon brut, sans seuil ni décision.
3. **Refus d'ouvrir étendu** à une phrase du dommage hors des quatre (voir C-4).
4. **Essai de la chaîne (ii)** : l'injection est faite sur le score du jeton et non sur l'activité (qui n'est pas livrée) ; équivalent pour une sonde linéaire, écrit dans le texte.
5. **Artefacts de réception de plus** : action vide portant un score fini ; `NaN` à une action non vide ; score par jeton altéré hors du sous-échantillon ; lignes du tableau par jeton décalées d'une action.
6. « Lectures retirées dans ce brouillon » devient « au brouillon 4 ».

## 5. Champs ouverts

- Bloquent le scellement : 2 marqueurs — F-3 (entropie des graines, tirée par la session mère) et l'entrée « Contre-lecture finale (texte rempli) ».
- Conditions de départ : 14 (D-1 à D-14), inchangées en nombre ; D-12 amendée (contrôle du vocabulaire).
- Décision ouverte : (b) contre (a), scores par jeton des neuf sondes.
