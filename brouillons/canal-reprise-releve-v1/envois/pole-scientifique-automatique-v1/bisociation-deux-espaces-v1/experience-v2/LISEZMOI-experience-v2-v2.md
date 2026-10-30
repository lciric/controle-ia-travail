# Expérience v2 — bisociation à deux espaces — code et essais (v2, après corrections)

Remplace `LISEZMOI-experience-v2-v1.md` (gardé, inchangé). Préenregistrement scellé : `prereg/preenregistrement-bisociation-deux-espaces-v2.md`, empreinte `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea`. Addendum d'écarts : `prereg/addendum-ecarts-bisociation-deux-espaces-v2-v2.md` (brouillon, **non scellé** au moment de ces corrections). Contre-lecture du code traitée : `contre-lecture-code/contre-lecture-code-experience-v2-v1.md`. Décisions appliquées : Lazar R-600 (30 octobre 2026, 16:58 heure de Paris).

Corrections écrites par un sous-agent Opus 5.5 neuf (`claude-opus-5-5`), 30 octobre 2026, à partir de 15:58 UTC ; auteur d'aucune ligne du code v1, de la contre-lecture ni de l'addendum.

**État : code corrigé, essais passés ; validation V1 à V9 et invocation unique NON lancées.** Elles refusent de partir tant que l'addendum n'est pas scellé (garde nouvelle, éprouvée : refus constaté, aucun monde généré).

## Avant corrections

L'état livré avant ces corrections est copié tel quel dans `version-v1-avant-corrections/` (tous les modules `*.py`, `essais/`, `LISEZMOI-experience-v2-v1.md`, `ecarts-et-questions-v1.md`, `reproduction-temoins-v2-resultats.json`, chacun avec son compagnon `.sha256`, vérifiés égaux avant la copie). Les fichiers modifiés ont reçu un compagnon nouveau. Inchangés : `bras_v2.py`, `noyaux_v2.py`, `balayage_v2.py`, `travail_v2.py`, `reproduction_temoins_v2.py`.

## 1. Décisions de Lazar (R-600)

| Point | Fait | Où |
|---|---|---|
| **Q-04 = copie** | Pour chaque pont planté, **l'article de plus grand indice (ordre final des articles) prend les mots propres du domaine de l'article de plus petit indice** ; règle déterministe, sans tirage ; mêmes latents, mêmes flux des rôles 1 à 3. La lecture « échange » est refusée par `v4_jumelles` (`lecture='copie_ponts'` seule permise). | `monde_v2._construire` ; `validation_v2.LECTURE_V4`, `v4_jumelles` |
| Q-04, vérification | Sur 3 mondes d'essai (indices 953000 à 953002) : **le cosinus de chacune des 18 paires plantées change** entre le monde et sa jumelle (valeurs non lues) ; latents et étiquettes égaux. Artefact : l'ancienne lecture reconstituée laisse le cosinus des 18 paires plantées inchangé (écart < 10⁻¹²) ; V4 échoue sur une variation nulle. | `essais/essais_corrections_v2.py` |
| **Q-01 = (b)** | En cas d'échec de plantation, **seul le placement des ponts est retenté sur le même monde de base** (champs, groupes, articles, opérateurs, contraintes vraies, q, palettes, fonds, moyeu inchangés : fonction `_tirer_base`). Replantation 0 = suite du flux du rôle 0 (un monde sans échec est identique bit à bit au code d'avant, latents et vue observée : 840 mondes d'essai, 14 conditions, indices 980000 à 980059 ; 811 sans échec, tous égaux ; les 29 mondes replantés sont exactement les 29 que l'ancien code régénérait ; `plomberie-corrections-v2/identite_ancien_nouveau_v1.py`, `identite-ancien-resultats-v1.json`, `identite-nouveau-resultats-v1.json`) ; replantation r ≥ 1 : `spawn_key = (code, m, 0, t, r)` (cinq éléments, aucune collision avec le § 7). Après **`MAX_REPLANTATIONS = 50`** échecs (choix de code, à déclarer dans l'addendum), régénération entière (tentative suivante, inchangée). M_inertes replante sous le code 1, donc garde les latents de M_bien. S11 reste à 2 % pour la régénération entière ; le taux de replantation est rapporté (par condition et par nombre de champs), sans seuil. | `graines_v2.sequence(…, replantation=r)` ; `monde_v2._construire`, `monde_de_base`, `signature_base` ; `mesures_v2.verifier_taux` ; `validation_v2.v8_rapport` |
| **Q-01, mesure** | 2 400 mondes d'essai par condition (RACINE_VALIDATION, indices 970000 à 972399), 14 conditions v2 : **0 monde à régénérer entièrement sur 33 600 (0 sur 2 400 dans chaque condition)**. Mondes replantés : 0 % (SP) à 5,8 % ; M_bien 5,29 % ; M_moyen 5,29 % ; INV 3,29 % ; V_surface 0,50 % ; en M surtout dans les mondes à 2 champs (M_bien : 111 sur 127), en INV surtout à 4 champs (40 sur 79). M_inertes égale M_bien par construction (mêmes latents) ; M_bien et M_moyen ont par hasard le même total (127 mondes, 140 replantations) : audit de propreté (R4) fait, mondes différents (latents égaux sur 0 des 50 premiers indices), répartition par champs différente (111 contre 104 à 2 champs). Deux exécutions, avant et après la dernière mise en forme du code, donnent un fichier identique. Seuls des comptes ont été lus. | `plomberie-corrections-v2/taux_q01_replantation_v1.py`, `taux-q01-replantation-resultats-v1.json`, `taux-q01-replantation-sortie-v1.txt` |
| **Q-03 = 16** | `CODE_CONTRASTE_NR = 16` : clés `(10, 16, 99)` et `(11, 16, 99)`. La garde « code non fixé → arrêt » reste et est éprouvée (code remis à vide dans l'essai). | `analyse_v2.py` |
| **Q-02** | Inchangé : N_grille tourne seulement à l'étape (1) du § 9 (`travail_v2.BRAS_DECISION`). | — |

## 2. Corrections de la contre-lecture du code

| Point de la contre-lecture | Correction |
|---|---|
| Comparaison bit à bit des latents M_inertes / M_bien absente de l'invocation | Chaque ligne de résultats porte `empreinte_latents` (une empreinte ; rien de latent ne sort). `executer_decision` garde celles de M_bien et, à M_inertes, appelle `mesures_v2.verifier_inertes_lignes` **avant d'écrire** le fichier de M_inertes : un indice différent ou absent arrête. V9 compare chaque miroir au monde « bien » de validation de même indice (`verifier_inertes`). |
| Cas sain de la garde d'échec de plantation qui ne pouvait pas échouer | `test_g07_sain_parametres_de_decision_sous_S11` : paramètres de décision, 300 mondes d'essai (951000 à 951299), garde réelle `verifier_taux` contre S11 = 2 % ; il peut échouer : sur les mêmes graines, l'ancienne règle (`MAX_REPLANTATIONS = 0`) le fait échouer (`test_g07_artefact_ancienne_regle_depasse_S11`). L'artefact « pont (d) impossible » est gardé. |
| Garde propre du glouton jamais exercée seule | Noyau `[[1, 1], [1, 1 + 10⁻¹⁴]]` : défini positif, accepté par `cholesky` de la pièce A, pivot relatif ≈ 10⁻¹⁴ < 10⁻¹² : `glouton_paires` lève `NonDefiniePositive` par sa garde propre ; avec le seuil mis à 0, il passerait (preuve que c'est bien elle). Cas sain : noyau ordinaire, 2 choisis. |
| Identités déclarées d'avance non filtrées | `lecture_v2.identites_audit` : déclenchent seulement les identités de N à **N_global, N_β0 ou un témoin (b, a, d1, d1c, b_eloigne, et la référence c)**, comme le texte, **hors** N ≡ N_β0 dans V_concepts_absents et d1c ≡ d1 dans NR ; les autres sont rapportées sans déclencher. `identites` est un dictionnaire {condition : bras}. |
| Déclencheur « concordance avec la vérité » sans grandeur | `mesures_v2.concordance_verite_monde` : part des couples (article, étiquette de concept observée) dont le concept est latent chez l'article (F_f avec f dans ses fonds, R_r avec r dans ses rares, H si l'article porte le moyeu) ; agrégée par condition sur les mondes non exclus (`concordance_verite`) ; écrite dans `donnees-audit` pour les conditions de décision v2 (`concordance_verite_conditions_decision`) ; NR : non calculée (pas de canal de concepts). `declencheurs_audit` accepte ce dictionnaire. **Définition à déclarer dans l'addendum.** |
| Vue observée portant le nom de la condition | `condition` retiré de `Obs` (un bras qui la lit lève `AccesLatent`, éprouvé). `validation_v2.v2_fuite` reçoit la condition en argument. |
| V4 : l'essai ne vérifiait que la concordance | Il vérifie aussi la variation (non nulle, sans lecture de sa valeur), et la règle de copie. |
| Q-03 : fixer le code une fois l'addendum scellé | Code fixé à 16 ; en outre, **validation et invocation exigent l'addendum scellé** (`invocation_unique_v2.exiger_addendum_scelle`, nom `ADDENDUM` à changer si la contre-lecture R2 en fait une version nouvelle). |
| Points « à déclarer » (addendum ; sans changement de code) | (i) le fichier scellé des moyennes de validation et de la grille est écrit **après** le manifeste (§ 9 le place à l'étape (1)) ; (ii) N_rare prend l'étiquette partagée la plus rare de l'étage commun (opérateur ou concept) ; (iii) le taux de bras vides a pour dénominateur tous les mondes, exclus compris ; (iv) Q-05 plus strict que le texte ; Q-07 défaut du texte de G8 sous fuite ; Q-12 racine de validation hors plages ; (v) `MAX_REPLANTATIONS = 50` ; (vi) définition de la concordance et liste des bras de l'identité. |
| Commande `unittest discover` (0 essai) | La seule commande valable est celle de pytest ci-dessous. |

## 3. Essais

Commande (depuis ce dossier) :

```
PYTHONPATH=<dépôt>/src python3 -B -m pytest -p no:cacheprovider essais/essais_gardes_v2.py essais/essais_complements_v2.py essais/essais_corrections_v2.py -q
```

- `essais_gardes_v2.py` : 41 (la garde 7 a maintenant trois essais : artefact « pont (d) impossible », cas sain sous S11, artefact de l'ancienne règle) ;
- `essais_complements_v2.py` : 42 (adaptés : code 16, V4 par copie avec variation non nulle, lignes synthétiques porteuses de l'empreinte des latents, prérequis) ;
- `essais_corrections_v2.py` : 21 nouveaux, chacun cas sain ou artefact d'une correction (Q-01 ×5, Q-04 ×2, M_inertes ×4, glouton ×2, identités ×2, concordance ×2, vue observée ×2, addendum ×2).
- **Total : 104 lancés, 104 réussis, 0 échec** (dernière exécution : 30 octobre 2026, 16:16 UTC, 31,7 s).
- Mutations (`plomberie-corrections-v2/mutations_corrections_v1.py`, 6 essais, xfail strict) : chaque garde neutralisée (comparaison des latents dans l'invocation et dans V9, filtre des identités, liste des identités déclarées, replantation, jumelle) fait échouer son essai : **6 sur 6 échouent comme attendu**.
- Graines d'essai : `INDICE_ESSAI` passé de 900 000 à **950 000** ; essais nouveaux aux indices 951000 à 955000 ; mesure de Q-01 aux indices 970000 à 972399 ; identité avec l'ancien code aux indices 980000 à 980059. RACINE n'est jamais employée ; aucun contraste de décision, aucune moyenne de Δ(N, ·), aucun résultat de V1 à V9 n'a été calculé ni lu.

## 4. Reproduction des témoins de v1 (liste d'arrêt, S12)

Rejouée avec le code corrigé (2 processus) : **identique** à `reproduction-temoins-v2-resultats.json` hors horodatage et empreintes du code — NR_bien b 0,2123, a 0,1606, c 0,1578, d1 0,2319 (0 exclu ; 66,28 paires valides) ; NR_moyen b 0,1293, a 0,1096, c 0,1134, d1 0,1761 (9 exclus ; 59,64). Nouveau fichier scellé, empreintes du code corrigé incluses : `reproduction-temoins-v2-resultats-v2.json` (le v1 reste, inchangé).

## 5. Commandes (NON LANCÉES)

Ordre : addendum contre-lu (R2, autre modèle) et scellé → contre-lecture de ces corrections → validation → (audit rendu si V9 vraie) → invocation, depuis un dépôt git propre et commité.

```
PYTHONPATH=<dépôt>/src python3 -B validation_v2.py <validation.json> --lancer-la-validation --lecture-v4 copie_ponts
PYTHONPATH=<dépôt>/src python3 -B invocation_unique_v2.py --run-id AAAAMMJJ-HHMMSS-bisociation-v2 --processus 2 \
  --validation <validation.json> --reproduction reproduction-temoins-v2-resultats-v2.json [--audit-rendu <rapport.json>]
```

Le manifeste consigne en plus `max_replantations`, l'addendum et la dérivation des graines de replantation. Les tables de correspondance du LISEZMOI v1 restent valables ; ajouts : `monde_v2._tirer_base`, `monde_de_base`, `signature_base` ; `graines_v2.sequence(replantation=…)` ; `mesures_v2.verifier_inertes_lignes`, `concordance_verite_monde`, `concordance_verite` ; `lecture_v2.identites_audit` ; `invocation_unique_v2.exiger_addendum_scelle`.

## 6. Ce qui reste

1. Addendum : y déclarer les points (v) et (vi) ci-dessus et les lectures (i) à (iv) ; contre-lecture R2 par un autre modèle ; scellement (et `ADDENDUM` à jour si le nom change).
2. Contre-lecture de ces corrections par un sous-agent neuf.
3. Validation V1 à V9, puis invocation unique.

Durée : inchangée (une replantation coûte moins qu'une régénération entière).
