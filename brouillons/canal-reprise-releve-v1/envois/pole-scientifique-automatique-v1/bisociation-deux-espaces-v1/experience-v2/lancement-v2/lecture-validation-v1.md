# Lecture de l'étape de validation — expérience v2 de bisociation à deux espaces — v1

- **Auteur** : sous-agent Opus 5.5 neuf, lecteur R13 (ni auteur du préenregistrement, ni du code, ni de l'addendum, ni de la chaîne de lancement).
- **Date** : relevé `date -u` 2026-10-30T23:51:54Z (début de la rédaction, après toutes les lectures ci-dessous).
- **Non lus** : rien sous `donnees/`. Aucune exécution de la validation, de la reproduction ni de l'invocation ; aucun code modifié ; aucun `.sha256` écrit ; aucun commit.
- **Ordre de lecture** : préenregistrement et addendum d'abord (en entier pour les § 5 à 9, les critères, la liste d'arrêt et les seuils S1 à S17), puis `ecarts-et-questions-v1.md` (lectures Q-05 à Q-12, validées « telles qu'écrites » par l'addendum), **ensuite seulement** les résultats et le code.

Fichiers lus et empreintes (SHA-256 recalculées à la lecture ; « compagnon OK » = égale au fichier `.sha256` voisin) :

| Fichier | SHA-256 | Contrôle |
|---|---|---|
| `prereg/preenregistrement-bisociation-deux-espaces-v2.md` | `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` | compagnon OK, égale à l'empreinte attendue |
| `prereg/addendum-ecarts-bisociation-deux-espaces-v2-v6.md` | `37f6df2e0f3653088643b4eb1883c2a5b083111227edd3c53a0e411cd187774f` | compagnon OK ; égale à `invocation_unique_v2.EMPREINTE_ADDENDUM` |
| `experience-v2/ecarts-et-questions-v1.md` | `eba626c5b7fd9ff7ae09e52c107b00b21746f1a4055cf7b73963ee11230cc717` | compagnon OK |
| `lancement-v2/validation-v2-resultats-v1.json` | `974dfe5e422662a5878f9dfa264f688f3a85113c9d8cf153325974a8820e0286` | compagnon OK |
| `lancement-v2/validation-v1.log` | `79f6859707888873e88f7de4e1b45cb97e85b8ac306f7a9285569fe1dcb7e4a0` | pas de compagnon |
| `lancement-v2/reproduction-v3.log` | `30e8cbe531adf52c37f069b3f5ac8969fc22609e8024599da00c71b37103f745` | pas de compagnon |
| `lancement-v2/journal-chaine-v1.txt` | `e55367debec6d8df3fbb9a45d1431f54874fbd9945099ca5d651dd2485cab29a` | pas de compagnon |
| `lancement-v2/chaine-lancement-v1.sh` | `272c78cb0dc47faeafccc071a072bdaa7d0ccbf8c261cd015b1abcf530ff8412` | pas de compagnon |
| `experience-v2/reproduction-temoins-v2-resultats-v3.json` | `946fc397553289d0fd59c801bf529b28245ba5bad29ebea2883ac22671557930` | compagnon OK |
| `experience-v2/validation_v2.py` | `7e872917ed3383d12c6c76613da64901f2d0dff49ebe0477eb6156b88da8e521` | compagnon OK |
| `trancher-recombinaison/trancher-recombinaison-v1.md` (B § 1) | `72cff8a067641cab173f3b6fbba32976a64989ded279d078ec4da432a582e4bf` | égale à l'empreinte citée par le préenregistrement |

Lus en extrait seulement : `mesures_v2.py` (`40a6f23a…`, constantes `MARGE_S12 = 0.02`, `PLAFOND_ORACLE_S8 = 0.30`), `monde_v2.py` (`0986a0cb…`, calcul de `pont`), `invocation_unique_v2.py` (`4cda77f0…`, constantes `EMPREINTE_PREREG`, `ADDENDUM`, `EMPREINTE_ADDENDUM`). Les quinze empreintes de code inscrites dans les deux fichiers de résultats sont identiques entre eux et égales aux fichiers sur disque ; tous les `*.py` d'`experience-v2/` concordent avec leurs compagnons. Addendum scellé à 23:47 UTC (R-656) ; reproduction écrite à 23:48:24, validation à 23:48:51 : l'ordre « addendum scellé, puis reproduction, puis validation » est tenu. L'essai interrompu de 23:47 (`essai-interrompu-2347/`) n'a écrit aucun résultat (fichiers vides, note).

---

## 1. Reproduction des témoins de v1 — **passée**

Critère (liste d'arrêt, ligne « Reproduction » ; S12) : moyennes de b, a, c, d1 sur NR_bien et NR_moyen dans l'intervalle à 95 % de B § 1, élargi de 2 points de chaque côté. Intervalles de B § 1 vérifiés sur `trancher-recombinaison-v1.md` (`72cff8a0…`, lignes 32 à 35) : identiques à ceux du code. 1 200 mondes par condition, RACINE_VALIDATION, indices 0 à 1199 (Q-12, déclaré).

| Condition | Témoin | Moyenne v2 | Intervalle B § 1 | Bornes avec marge S12 | Dans |
|---|---|---|---|---|---|
| NR_bien | b | 0,2123 | [0,192 ; 0,215] | [0,172 ; 0,235] | oui |
| NR_bien | a | 0,1606 | [0,144 ; 0,168] | [0,124 ; 0,188] | oui |
| NR_bien | c | 0,1578 | [0,141 ; 0,162] | [0,121 ; 0,182] | oui |
| NR_bien | d1 | 0,2319 | [0,227 ; 0,249] | [0,207 ; 0,269] | oui |
| NR_moyen | b | 0,1293 | [0,118 ; 0,137] | [0,098 ; 0,157] | oui |
| NR_moyen | a | 0,1096 | [0,096 ; 0,115] | [0,076 ; 0,135] | oui |
| NR_moyen | c | 0,1134 | [0,098 ; 0,115] | [0,078 ; 0,135] | oui |
| NR_moyen | d1 | 0,1761 | [0,155 ; 0,175] | [0,135 ; 0,195] | oui (au-dessus de l'intervalle brut de 0,1 point, dans la marge) |

Exclus : 0 (NR_bien), 9 sur 1 200 soit 0,75 % (NR_moyen, sous S11 = 2 %). Paires valides par monde 66,28 / 59,64 (v1 : 67,55 / 60,50). Ces valeurs ne sont pas des résultats de décision.

## 2. Validation du générateur, V1 à V9

300 mondes « bien », 300 « moyen », 100 jumelles, 300 miroirs de M_inertes ; RACINE_VALIDATION = 20261102, indices 0 à 299 (§ 7). Conditions d'évaluation selon Q-05 (validée par l'addendum) : V1 et S8 dans M_bien et M_moyen ; V2, V3, V5 dans M_bien ; V6 dans M_moyen.

| V | Vrai / faux | Valeur mesurée | Seuil du texte (S13, S8, § 6) | Conséquence d'un échec selon le texte |
|---|---|---|---|---|
| V1 (M_bien) | **vrai** | même domaine 0,5390 ; proches 0,2800 ; éloignés 0,0241 | [0,51 ; 0,57], [0,25 ; 0,31], [0,00 ; 0,06] | liste d'arrêt : « Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) → arrêt avant les bras candidats (N et ses ablations) ; correction par une nouvelle version du préenregistrement (R12) » ; V0 fausse (Critères, booléen V0) |
| V1 (M_moyen) | **vrai** | 0,5295 ; 0,2775 ; 0,0246 | idem | idem |
| V2 (M_bien) | **vrai** | F = −0,0854 (loi nulle rapportée : −0,0865) | F ≤ 0,10 | idem (V2 est dans V1 à V6) ; en outre « fuite mesurée F exactement nulle (à 10⁻¹² près) » serait un déclencheur d'audit (Audit de symétrie) : non déclenché |
| V3 (M_bien) | **vrai** | excès −0,0595 (M_moyen, rapporté : −0,0717) | ≤ 0,10 | idem |
| V4 (jumelles, lecture « copie », addendum Q-04) | **vrai** | concordance 1,000 ; variation des cosinus 0,2562 | concordance ≥ 0,9 et variation ≥ 0,2 | idem |
| **V5 (M_bien)** | **FAUX** | **écart maximal entre statuts 2,873** (moyennes : vrai d'opérateur 3,444 ; faux 4,940 ; proche 4,931 ; vrai conceptuel 5,010 ; surface 6,318) | **≤ 0,5** | **liste d'arrêt, première ligne : « arrêt avant les bras candidats (N et ses ablations) ; correction par une nouvelle version du préenregistrement (R12) » ; V0 fausse → Table 1 et Table 2, ligne 0 : « non concluant ; aucune lecture des contrastes »** |
| V5 (M_moyen, rapporté, non soumis au seuil selon Q-05) | — | écart 1,945 (vrai d'opérateur 4,434 ; vrai conceptuel 5,709 ; surface 5,944 ; faux 6,207 ; proche 6,379) | — | aucune (Q-05) ; serait aussi au-dessus de 0,5 |
| V6 (M_moyen) | **vrai** | 9,00 vraies paires valides par monde (M_bien, rapporté : 12,28) | ≥ 6 | liste d'arrêt, première ligne ; V0 fausse |
| S8, plafond de l'oracle | **vrai** | 0,9103 (M_bien) ; 0,7172 (M_moyen) | ≥ 0,30 | liste d'arrêt, première ligne, et ligne « Plafond de l'oracle < S8 → arrêt : monde non jugeable » |
| V7 | sans seuil | rapport des lois de κ et cos par classe, écrit dans le fichier | aucun | « V7 est lu mais ne change rien … V7 ne déclenche rien … Une version nouvelle motivée par V7 ne peut être écrite qu'après le verdict scellé (R12) » (§ 6, V7) |
| V8 | sans seuil | replantation 4,0 % / 4,7 % ; régénération entière 0 ; exclusion 0 ; paires valides par monde 250,3 / 176,8 ; vraies paires par mécanisme : greffe 3, jumeau 3, pont conceptuel direct 3, expansion 6,0 / 6,3 | aucun | « rapport sans seuil » (§ 6, V8) ; taux soumis à S11 selon l'addendum (régénération entière seulement) : 0 |
| V9 | J **fausse** (attendu) | booléen seul : `V9_J_vraie = false` | J doit être fausse sur les miroirs | J vraie aurait été « un déclencheur d'audit R4 … jamais un arrêt ; l'audit … est rendu et scellé avant l'invocation unique » (§ 6, V9) : non déclenché |

**Une seule V fausse : V5 dans M_bien (2,873 contre un seuil ≤ 0,5).**

## 3. Ce que le texte scellé prescrit maintenant (et seulement cela)

1. **Arrêt avant les bras candidats.** Liste d'arrêt, première ligne : « Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) | arrêt avant les bras candidats (N et ses ablations) ; correction par une nouvelle version du préenregistrement (R12) ». L'invocation unique ne doit pas être lancée sous ce texte ; la chaîne s'est arrêtée conformément.
2. **Verdict sous ce texte : « non concluant ».** V0 = « validation du générateur passée (V1 à V6) ∧ … » est fausse ; Table 1, ligne 0, et Table 2, ligne 0 : « V0 non tenue → non concluant ; aucune lecture des contrastes ». Les Critères disent : « Le verdict est scellé puis soumis à Lazar pour GO (R13). » Le présent texte est une lecture ; le prononcé scellé reste à faire par un sous-agent neuf selon R13 (je n'écris aucun `.sha256`).
3. **Correction : seulement par une nouvelle version du préenregistrement (R12).** Le texte ne prévoit ni correction du générateur sous le même texte, ni addendum, ni relance de la validation sous le même texte : la seule voie écrite est « une nouvelle version du préenregistrement ». Contraintes écrites qui pèsent sur cette nouvelle version :
   - « Aucun défaut ne s'applique à un seuil ni à un paramètre de monde » et tout seuil ou paramètre S16 est gelé par Lazar (section « Seuil », S16 : « en modifier un est une modification de la force d'une hypothèse, donc un nœud de décision ») ;
   - § 6, V7 : « aucun paramètre de monde n'est modifié après sa lecture … Une version nouvelle motivée par V7 ne peut être écrite qu'après le verdict scellé (R12) » ; V7 figure dans le même fichier que V5 et a été lu (par moi) ;
   - liste d'arrêt : « paramètre modifié après lecture … → arrêt et consignation de l'écart (R1) » ; toute version nouvelle doit donc déclarer ce qui a été lu (V1 à V9, V7, V8, reproduction).
4. **Ce sur quoi le texte est muet → nœud de décision de Lazar** : (a) si un addendum (comme pour Q-01 à Q-04) peut tenir lieu de « nouvelle version » ; (b) si la correction doit porter sur le générateur, sur la définition de V5 (liste des statuts) ou sur son seuil (S13, gelé par Lazar) ; (c) si les graines de validation (RACINE_VALIDATION, indices 0 à 299) peuvent être réemployées par la nouvelle version, alors que leurs résultats sont lus ; (d) si un audit R4 est exigé : aucun déclencheur d'audit écrit n'est présent (V9 fausse, F non nulle) ; le texte n'en prescrit donc pas. Selon `CLAUDE.md`, tout écart à un préenregistrement scellé et toute modification de seuil ou d'hypothèse sont de toute façon des nœuds de Lazar.

## 4. Hypothèses de cause de l'échec de V5 (distinctes de la prescription ; rien n'a été modifié ni exécuté)

- **Ce n'est pas un écart de code ni d'addendum (lecture du code).** `validation_v2.v5_rarete` applique la définition du § 6 à la lettre : « pour chaque statut (vrai conceptuel, vrai d'opérateur, faux, proche, surface), fréquence documentaire observée moyenne de l'étiquette de pont retenue sur les paires plantées valides ; écart maximal entre statuts » ; l'étiquette retenue est `obs.pont[x]`, l'étiquette partagée la plus rare de l'étage commun, opérateur ou concept (`monde_v2.py`, ligne 172, conforme au § 2) ; le regroupement « greffe + jumeau » et l'évaluation sur M_bien sont les lectures Q-05 et Q-06, validées par l'addendum ; seuil 0,5 conforme à S13. Plomberie : empreintes concordantes, ordre tenu.
- **Hypothèse principale : défaut de conception du texte (statuts non comparables).** Les trois statuts à concept rare, dont S16d égalise la loi des émetteurs (« la même pour tous les statuts de pont », vrai, faux, proche), ont des moyennes presque égales en M_bien : 5,010 / 4,940 / 4,931, écart 0,08, sous le seuil. L'écart vient des deux statuts dont l'étiquette de pont est (en tout ou en partie) une **étiquette d'opérateur**, qui suit la loi de v1 (G2) et non S16d : vrai d'opérateur 3,444 (étiquette d'opérateur de greffe ou de jumeau, plus rare) et surface 6,318 (homonyme d'opérateur, porté par davantage d'articles). Le seuil 0,5 « brouillon 1 » s'applique à une liste de cinq statuts dont deux ne sont gouvernés par aucune égalisation : l'échec est plausible par construction. Non vérifié par calcul (interdit ici).
- **Hypothèse secondaire (niveau des moyennes).** Les moyennes ≈ 5 dépassent L_r ≤ 4 : quand le concept rare n'est pas observé chez les deux articles (couverture 0,85, fuite 0,05), la paire reste valide par un concept de fond partagé (fréquence 8 à 16), qui devient l'étiquette retenue. Cela relève toute la moyenne des statuts conceptuels sans les séparer ; c'est sans effet sur l'échec, mais touche la prémisse de S16f (φ = 4). Non vérifié.

## 5. Propreté (R4) de ce qui a passé

- **V1** : 0,539 / 0,280 / 0,024 contre la référence v1 0,54 / 0,28 / 0,03 : très proche, attendu (G2 garde le vecteur de domaine de v1). Pas suspect.
- **V2** : F = −0,0854 et sa loi nulle (permutation intra-domaine) −0,0865 sont presque égales : V2 passe, mais **ne discrimine pas** ici (F ne se distingue pas de sa loi nulle ; signe négatif = le canal affaiblit le lien κ–cos au lieu de le renforcer). Ni « exactement nulle », ni déclencheur ; le texte n'a pas de règle sur la loi nulle. À signaler, sans conséquence.
- **V4** : concordance exactement 1,000 ; attendu par construction (« la concordance est attendue proche de 1 », § 6). Ne pas confondre avec le déclencheur « concordance avec la vérité > 0,99 », grandeur distincte (addendum (vi-a)), non calculée à cette étape. Variation 0,256, marge de 0,056 sur le seuil, sous la règle « copie » tranchée avant toute lecture (R-600).
- **V6 et S8** : vraies paires 12,28 / 9,00 et oracle 0,91 / 0,72, au-dessus de v1 (9,52 / 5,97 ; 0,750 / 0,487). Cohérent avec l'ajout des ponts conceptuels ; pas suspect.
- **V8 — à signaler à Lazar (sans conséquence écrite)** : paires valides par monde **250,3 (bien) et 176,8 (moyen)**, contre 67,55 / 60,50 en v1, soit 3,7 et 2,9 fois plus. Le texte ne prévoyait « nettement plus de paires valides » qu'en M_inertes et M_palettes_communes (§ 8, SUPPOSÉ) et disait que le budget de 12 couvrait « environ le cinquième » des paires ; ici moins du quinzième. Conséquence probable : précision de b et de c bien plus basse qu'en v1, donc les fourchettes de transfert de la section « Prédiction » sont plus fragiles que dit (le texte l'annonçait qualitativement pour S16c). Aucun seuil ne lit V8.
- **V9** : J fausse, attendu (probabilité 0,98 à effet nul).
- **Reproduction** : dans la marge partout ; dans l'intervalle brut de B § 1 sauf d1 en NR_moyen (+0,1 point), attendu au vu de la variation d'échantillonnage déclarée par S12. Pas suspect.
- **Forme** : le titre de l'addendum v6 dit encore « BROUILLON, NON SCELLÉ » alors que son compagnon existe, que R-656 le déclare scellé à 23:47 UTC et que la garde du code l'a accepté. Défaut de libellé, sans effet sur la chaîne ; à corriger dans une version suivante (on ne réécrit pas un fichier scellé).
- **Rien de trop beau** dans ce qui a passé. Le seul point « sale » est V5, expliqué ci-dessus de façon plausible par la définition elle-même.
