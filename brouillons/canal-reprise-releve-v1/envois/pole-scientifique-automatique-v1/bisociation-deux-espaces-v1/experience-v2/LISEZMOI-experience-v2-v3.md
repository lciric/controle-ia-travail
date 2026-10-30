# Expérience v2 — bisociation à deux espaces — code et essais (v3, après les corrections CLA)

Remplace `LISEZMOI-experience-v2-v2.md` (gardé, inchangé ; ses sections 1 à 4 restent valables sauf ce qui est dit ici). Préenregistrement scellé : `prereg/preenregistrement-bisociation-deux-espaces-v2.md`, empreinte `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea`. Addendum d'écarts : `prereg/addendum-ecarts-bisociation-deux-espaces-v2-v4.md`, empreinte `ff354432010b8fad7f2c29d8036eedd196c6f4d14eceef2ec291c36c29864602` (vérifiée par `sha256sum` avant et après ces corrections), **non scellé** (aucun compagnon écrit). Contre-lecture traitée : `contre-lecture-code/contre-lecture-addendum-v3-et-corrections-v1.md` (constats CLA-03, CLA-04, CLA-09 ; les autres sont de texte et traités dans l'addendum v4). Ce qui est fait ici suit l'étape (2) de l'« ordre de gel » de l'addendum v4, point (vii).

Corrections écrites par un sous-agent Opus 5.5 neuf (`claude-opus-5-5`), relevé `date -u` 30 octobre 2026, 23:32 UTC (fin des essais) ; auteur d'aucune ligne du code, de la contre-lecture ni de l'addendum.

**État : code corrigé, essais et mutations passés ; reproduction des témoins, validation V1 à V9 et invocation unique NON LANCÉES.**

## Avant ces corrections

L'état d'avant, pour les seuls fichiers modifiés, est copié tel quel dans `version-v2-avant-cla/` avec son compagnon `.sha256` (vérifié égal avant la copie) : `invocation_unique_v2.py`, `lecture_v2.py`, `monde_v2.py`, `bras_v2.py`, `balayage_v2.py`, `essais/jouets_v2.py`, `essais/essais_gardes_v2.py`, `essais/essais_corrections_v2.py`, `plomberie-corrections-v2/mutations_corrections_v1.py`. Ces fichiers ont reçu un compagnon nouveau (l'ancien est dans la copie). Inchangés : tous les autres modules (`analyse_v2.py`, `graines_v2.py`, `mesures_v2.py`, `noyaux_v2.py`, `travail_v2.py`, `validation_v2.py`, `reproduction_temoins_v2.py`) et `essais/essais_complements_v2.py`.

## 1. Ce qui change

| Constat | Correction | Où |
|---|---|---|
| **CLA-04** nom et empreinte de l'addendum | `ADDENDUM = "addendum-ecarts-bisociation-deux-espaces-v2-v4.md"` ; constante nouvelle `EMPREINTE_ADDENDUM = "ff354432…864602"` ; `exiger_addendum_scelle` vérifie, après le compagnon, que l'empreinte du fichier égale la constante (même logique que `EMPREINTE_PREREG`), sinon `GardeArret`. Si le texte de l'addendum change encore, les deux constantes changent avec lui (et les compagnons du module). | `invocation_unique_v2.py` |
| **CLA-03** identités entre toutes les paires | `identites_paires(lignes)` : toutes les paires parmi N et **tous les bras présents** (N, N_global, N_β0, b, a, d1, d1c, c, b_eloigne, oracle, placebos, variantes…), égalité des **listes ordonnées** `_paires` sur tous les mondes non exclus, mondes exclus ignorés ; un bras non applicable (absent) ne forme aucune paire ; paires rangées dans l'ordre de `bras_v2.ORDRE_BRAS`. `identites_a_N` est gardée, déduite des paires. Les fichiers de résultats portent `identites_paires` (et `identites_a_N`) ; les données d'audit portent `identites_paires` (la clé `identites_a_N` des données d'audit est remplacée). | `invocation_unique_v2.py` |
| CLA-03, filtre | `lecture_v2.identites_audit` reçoit des paires (un nom seul vaut la paire (N, nom), forme d'avant gardée). Liste déclarée inchangée : **déclenchent seulement les paires (N, x)**, x parmi N_global, N_β0, b, a, d1, d1c, c, b_eloigne, non déclarées d'avance (N ≡ N_β0 dans V_concepts_absents ; d1c ≡ d1 dans NR_bien et NR_moyen). Toutes les autres sont rapportées sans déclencher, **dont d1c ≡ d1 hors NR** (texte scellé : seules les identités de N déclenchent ; addendum v4, (vi-b)). | `lecture_v2.py` |
| **CLA-09** indicateurs de condition dans la vue observée | `nr` et `concepts_absents` retirés de `Obs.__slots__` et des deux constructeurs (`generer`, `generer_nr`) : toute lecture lève `AccesLatent`. `bras_d1c` n'a plus de test propre (il lisait ces indicateurs) ; sa non-applicabilité dans NR et V_concepts_absents est décidée par `mesures_v2.NON_APPLICABLES` seul (inchangé), qui l'empêche d'être exécuté. Aucun autre accès donné. Les latents gardent leur `nr`. | `monde_v2.py`, `bras_v2.py`, `essais/jouets_v2.py` |
| CLA-09, balayage | Refusés désormais dans les bras et noyaux : toute chaîne de caractères qui commence par `co:` ou `op:` (morceaux de f-chaîne compris) et tout appel de méthode `startswith`, `endswith`, `removeprefix`, `removesuffix`, `partition`, `rpartition`, `split`, `rsplit`. Un bras ne lit une étiquette que comme clé opaque (égalité, appartenance, df). Les modules livrés passent sans changement. | `balayage_v2.py` |
| Essais adaptés | `test_g14_artefact_…` : l'appel direct de `bras_d1c` qui devait lever remplacé par : d1c dans `NON_APPLICABLES["V_concepts_absents"]` et `obs.concepts_absents` lève `AccesLatent`. `test_addendum_sain_scelle_accepte` : la copie temporaire scellée est le texte v4 réel (et non plus un texte d'essai, que la garde d'empreinte refuse maintenant). | `essais/essais_gardes_v2.py`, `essais/essais_corrections_v2.py` |

### Choix de code (pris seul, à faire voir à la vérification)

1. **Balayage, au-delà de la lettre de CLA-09** : en plus des chaînes `co:`/`op:`, les méthodes de lecture de préfixe sont refusées (une chaîne construite par morceaux, `"c" + "o:"`, échapperait sinon à la seule règle des chaînes). L'interdiction stricte ne casse aucune lecture légitime (aucun bras livré n'emploie ces chaînes ni ces méthodes). **Limite déclarée** : les tranches (`p[:4]`) ne sont pas interdites en soi (le code des bras tranche des tableaux numpy et des listes) ; une tranche n'est attrapée que si elle est comparée à une chaîne `co:`/`op:` ; un test caractère par caractère sans ces chaînes (`p[3] == "R"`) n'est pas attrapé. Les noms d'étiquettes restent visibles dans `Obs`.
2. **`nr` et `concepts_absents` non ajoutés aux noms refusés du balayage** : retirés de `Obs`, ils lèvent `AccesLatent` à l'exécution (éprouvé) ; c'était l'une des deux issues proposées par CLA-09.
3. **Identités : « tous les bras présents »** (et pas seulement les huit de la liste), comme demandé ; l'ordre de rangement des paires est celui de `ORDRE_BRAS` ; `identites_a_N` gardée pour le rapport ; clé `identites_a_N` des données d'audit remplacée par `identites_paires`.
4. **Compagnons** : l'outil `sceller` refuse d'écraser un compagnon existant (R12) ; pour les fichiers de code modifiés, l'ancien compagnon a été retiré (après vérification qu'il était identique à celui de `version-v2-avant-cla/`) puis le fichier rescellé, comme l'avait fait la correction précédente.

## 2. Essais

Commande (depuis ce dossier) :

```
PYTHONPATH=<dépôt>/src python3 -B -m pytest -p no:cacheprovider essais/essais_gardes_v2.py essais/essais_complements_v2.py essais/essais_corrections_v2.py essais/essais_cla_v2.py -q
```

- `essais_gardes_v2.py` 41, `essais_complements_v2.py` 42, `essais_corrections_v2.py` 21 (comptes inchangés ; deux essais adaptés, voir § 1) ;
- `essais_cla_v2.py` : **14 nouveaux** (cas sain ou artefact de chaque garde nouvelle, R5) :
  - CLA-04 ×3 : sain (copie temporaire du texte v4 scellée dans le dossier temporaire : acceptée ; empreinte du vrai fichier égale à la constante, en lecture seule) ; artefact (texte modifié puis rescellé, compagnon concordant : refusé ; texte vrai avec constante différente, par monkeypatch : refusé) ; garde de procédure (le vrai addendum n'a pas de compagnon) ;
  - CLA-03 ×3 : sain (bras différent de N sur un monde ; identité seulement sur un monde exclu : ignorée ; même ensemble dans un autre ordre : pas identique) ; artefact (N_global, N_q copies de N, d1c copie de d1, b_eloigne copie de b sur tous les mondes non exclus, différents sur un monde exclu : les cinq paires rapportées ; seule (N, N_global) déclenche ; d1c ≡ d1 rapportée sans déclencher, hors NR et dans NR ; N ≡ N_β0 déclarée dans V_concepts_absents, déclenche dans M_moyen ; chaîne jusqu'à `declencheurs_audit`) ; sain sur mondes réels (d1c non applicable en V_concepts_absents : aucune paire, indices 956000 à 956002) ;
  - CLA-09 ×8 : sain vue observée (indicateurs absents des champs, lecture refusée dans NR_bien, V_concepts_absents, M_bien ; d1c jamais exécuté en NR_bien, NR_moyen, V_concepts_absents ; exécuté en M_bien) ; artefact vue observée (un bras qui lit `obs.nr` lève `AccesLatent` ; `NON_APPLICABLES` vidée par monkeypatch : d1c tourne en NR, preuve que la table est la seule barrière) ; sain balayage (modules livrés ; lecture opaque des étiquettes acceptée) ; artefact balayage ×5 (`startswith`, égalité à `'co:R3'`, tranche comparée à `'co:R'`, f-chaîne `op:h…`, `partition`) : refusés par `problemes` et par `exiger_propre`.
- **Total : 118 lancés, 118 réussis, 0 échec** (dernière exécution : 30 octobre 2026, 23:32 UTC, 29,6 s).

## 3. Mutations

`plomberie-corrections-v2/mutations_corrections_v1.py` (xfail strict ; même commande de base, fichier unique) : 6 d'avant + **2 nouvelles** :
- **m7** : `exiger_addendum_scelle` remplacée par la garde d'avant CLA-04 (compagnon seul, sans `EMPREINTE_ADDENDUM`) : l'artefact CLA-04 échoue (« DID NOT RAISE GardeArret ») ;
- **m8** : `identites_paires` remplacée par la chaîne d'avant CLA-03 (chaque bras comparé à N seulement) : l'artefact CLA-03 échoue (les paires sans N manquent).

**8 sur 8 échouent comme attendu** (raison vérifiée avec `--runxfail` pour m7 et m8).

## 4. Identité bit à bit des mondes

`plomberie-corrections-v2/identite_avant_apres_cla_v1.py` (nouveau) : 16 conditions (les 14 conditions v2 et NR_bien, NR_moyen), indices 980000 à 980059, `RACINE_VALIDATION` : 960 mondes. Par monde, empreinte des latents (`empreinte_latents` ; pour NR : graine v1, champs, vraies paires, plantés) et empreinte de **tous les champs de la vue observée sauf `nr`, `concepts_absents` et `_fige`** (le retrait de ces deux champs est l'objet du changement : ils sont exclus de la comparaison, dit), plus tentatives et replantations.

- Avant (code de `version-v2-avant-cla/` complété des modules inchangés ; aussi rejoué depuis le dossier avant toute modification : même fichier) : `identite-avant-cla-resultats-v1.json` ;
- après : `identite-apres-cla-resultats-v1.json` ;
- **les deux fichiers sont identiques octet pour octet** (empreinte `db1cc174b647fb0233e220c8de8bf0512beff54174fb679f23ae8d3adc4b7ed9`) : 960 mondes sur 960 égaux, dont 931 sans échec et 29 replantés (0 régénéré). L'ancien script `identite_ancien_nouveau_v1.py` (14 conditions, empreinte qui n'inclut pas ces deux champs) rejoué sur le code corrigé donne un fichier **identique** à `identite-nouveau-resultats-v1.json`.

Seuls des égalités et des comptes ont été lus ; aucun bras n'a été exécuté pour cette comparaison.

## 5. Graines et lectures

Essais nouveaux aux indices 956000 à 956009 (`RACINE_VALIDATION`) ; identité aux indices 980000 à 980059 (déjà employés par la correction précédente). RACINE jamais employée ; aucun contraste de décision, aucune moyenne de Δ(N, ·), aucun résultat de V1 à V9 calculé ni lu ; rien lu sous `donnees/`. À ajouter à la liste « Ce qui a été lu avant » de l'addendum si le texte est encore modifié (sinon cette ligne en tient lieu) : indices 956000 à 956009, appartenances et exceptions seulement.

## 6. Suite (commandes inchangées, NON LANCÉES)

Ordre de gel (addendum v4, (vii)) : (3) fait ici ; (4) vérification de ces corrections (texte v4 et code) par un sous-agent neuf ; (5) scellement de l'addendum (si son texte change, mettre à jour `ADDENDUM`, `EMPREINTE_ADDENDUM`, rejouer essais et mutations, compagnons) ; (6) puis, depuis un dépôt git propre et commité :

```
# reproduction des témoins à régénérer avec le code final (les empreintes de code de reproduction-temoins-v2-resultats-v2.json sont périmées) :
PYTHONPATH=<dépôt>/src python3 -B reproduction_temoins_v2.py reproduction-temoins-v2-resultats-v3.json --processus 2
PYTHONPATH=<dépôt>/src python3 -B validation_v2.py <validation.json> --lancer-la-validation --lecture-v4 copie_ponts
PYTHONPATH=<dépôt>/src python3 -B invocation_unique_v2.py --run-id AAAAMMJJ-HHMMSS-bisociation-v2 --processus 2 \
  --validation <validation.json> --reproduction reproduction-temoins-v2-resultats-v3.json [--audit-rendu <rapport.json>]
```

Validation et invocation refusent de partir tant que l'addendum n'est pas scellé **avec l'empreinte `ff354432…`**.
