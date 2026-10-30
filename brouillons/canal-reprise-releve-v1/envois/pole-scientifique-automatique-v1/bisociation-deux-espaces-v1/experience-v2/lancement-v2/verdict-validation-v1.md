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
