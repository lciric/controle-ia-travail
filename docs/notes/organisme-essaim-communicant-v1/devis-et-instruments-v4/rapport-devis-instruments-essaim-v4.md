# Rapport — devis et instruments de l'essaim — v4

- Sous-agent auteur (Claude Opus 5.5), 22 novembre 2026.
- **Aucun appel de modèle, aucune dépense, aucun réseau, rien d'écrit ni de commité dans le dépôt.**
- Place prévue : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4/`.
- Pièces corrigées : la contre-lecture de la v3, `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/contre-lecture-v1/contre-lecture-devis-instruments-essaim-v3-v1.md` (« CL-v3 », verdict « À corriger »), avec ses outils.
- Aucun refus de permission, de garde ou de classifieur n'a été rencontré.

## Verdict

- **Tout le « bloquant » que le code peut porter est corrigé et éprouvé.**
  - Registre de dépense persistant.
  - Refus du plan, du plafond et des prix hors du gel.
  - Adaptateur sans relance interne, qui compte la réflexion.
  - Réserve comptée après toute exception et pour tout usage anormal.
  - R1 sans chemin deviné, rejeu long réparé, contrôle des nombres qui attrape les 8 artefacts neufs, évaluateur du juge vérifié à son empreinte.
- **Les attaques A1 à A10 de CL-v3 sont arrêtées sous la v4.** A8 est une limite déclarée : arrêt 11 après un seul appel hors H3, borné par la fenêtre du modèle et par la limite chez le fournisseur.
- **Vrai pire du pilote P-std sur Kimi sous la v4 : 203,94 USD**, inchangé (`calcul-vrai-pire-v4.json`). Il tient désormais **entre les invocations** et **face à l'adaptateur**.
  - Il reste conditionné à H1 à H4.
  - Il ne devient une borne absolue qu'avec la limite de 204 USD chez le fournisseur.
- Ce qui ne relève pas du code est listé dans `a-faire-avant-preenregistrement-pilote-v1.md`, avec une proposition chiffrée pour la garde des formes fausses.

## 1. Différence avec la v3

| point de CL-v3 | v3 | v4 | preuve |
|---|---|---|---|
| A1 : plan agrandi et plafond de 10⁶ acceptés | code 0, 348,29 USD | plan ≠ empreinte gelée `dc5a5cc6…` ⇒ **15** ; plafond > borne ⇒ **24** ; registre créé au-dessus de la borne ⇒ **24** ; 0 USD | `epreuves-lanceur-pilote-v2.json`, cas A1, A1b |
| A2 : seconde invocation, cumul remis à zéro | 352,90 USD | **registre persistant** scellé et chaîné (`registre_depense_v1.py`), relu avant tout appel. Course close ⇒ **23** ; absent ⇒ **21** ; altéré (sceau laissé, ou re-scellé avec une ligne du milieu changée) ⇒ **22** ; processus tué pendant un appel ⇒ réserve en suspens comptée comme échec, reprise au plan | cas A2, registre absent, altéré, re-scellé, processus tué |
| A3 : relances internes du kit client | invisibles, facture ×3 | l'adaptateur exige `relances_internes == 0` et `repli_modele is None` (refus à la construction). Le transport doit rendre `tentatives` : s'il manque ou vaut plus de 1 ⇒ **16**, et l'appel est compté à la réserve × envois rendus | cas A3, A3b, A3c |
| A4 : réflexion facturée hors de `sortie` | invisible | sortie = `completion_tokens` + réflexion rendue hors de ce compte (premier niveau, ou détail supérieur au compte) ⇒ **10** ou **16** selon le plafond | cas A4, A4b, A4c |
| A5 : erreur après facturation | appel non compté | toute exception après l'envoi ⇒ réserve entière comptée, **17** | cas A5 |
| A6 : prix (0, 0) | acceptés | prix comparés à `PRIX_GELES` (2,0 ; 10,0) et à `calcul_devis_essaim_v4.tarifs()["kimi"]` ⇒ **24** | cas A6 |
| A7 : sortie négative ; usage absent | compté 0 | réserve entière, **16** | cas A7, A7b |
| A8 : entrée rendue à 256 000 jetons | arrêt 11 après dépassement | **inchangé, limite déclarée** : un appel hors H3 ne se borne que par la fenêtre du modèle et la limite chez le fournisseur (176,91 USD contre un plafond de 176,6 dans l'épreuve) | cas A8 |
| A9 : relance déguisée | acceptée | la relance doit être l'entrée du plan identique en tout ⇒ **15** | cas A9 |
| A10 : abandons hors budget | arrêt seulement par la dépense | relances et abandons dans un seul budget de 74 échecs ⇒ **13** | cas A10 |
| R1 : défaut `/home/user/controle-ia-travail` dans le devis | réussite silencieuse hors du dépôt | `calcul_devis_essaim_v4.py` prend la racine par `racine_depot_v1` : au-dessus du fichier, sinon `DEPOT_CONTROLE_IA`, sinon refus | `calcul_devis_essaim_v4.py`, l. 32-37 |
| R2 : 8 artefacts neufs du contrôle des nombres | 8 passent | **liste blanche** des formes de niveau module (docstring, import, affectation à un nom ou à un tuple de noms, def, `if __name__ == "__main__":`), **plus les valeurs exécutées** de l'en-tête dans un processus isolé, comparées à la lecture ; mentions « marge », « majoration » et C.8 lues après normalisation Unicode (NFKC), en « % » comme en « pour cent » | outil de CL-v3 rejoué tel quel : 9 / 9 tenues (`artefacts-contre-lecture-v3-sur-devis-v4.txt`) ; épreuves de l'auteur 41 / 41 (`epreuves-devis-v4.json`) ; outil du relecteur de la v2 : 10 / 10 (`artefacts-relecteur-v2-sur-devis-v4.txt`) |
| rejeu long cassé depuis le commit | motif E portait l'empreinte d'un juge muté qui embarque un chemin | motifs rendus par leur catégorie, aucun chemin ni empreinte dépendant de l'emplacement dans la sortie (0 chemin absolu dans `test-de-mort-programme-v3-sortie.json`) ; `rejouer_v4.sh --long` rejoue aussi les bases de la v3 | § 3 |
| juge auto-certifié ; évaluateur non vérifié | empreinte lue dans son propre compagnon | `JUGE_SHA` écrite en dur dans `test_de_mort_programme_v3.py` ; le juge v2 vérifie `monde_riche_outils_v1.py` à `1825b956…` **avant** son import, sinon sortie 6 ; artefact H (évaluateur d'empreinte différente) refusé dans les 12 mondes | `test-de-mort-programme-v3-sortie.json` |

Montants du devis : identiques à la v3. `resume_usd`, `devis_par_espece` et `rapport_pire_v3_sur_pire_v1` sont égaux, avec un rapport pire / pire v1 de 1,819 à 3,228 (`calcul-devis-essaim-v4.json`).

## 2. Lanceur v2 : ce qui est vérifié, et où

### 2.1 Les fichiers

- `garde_pilote_essaim_v2.py` : plafonds de la v1, inchangés. Plan gelé par empreinte, budget d'échecs unique (74), réserve comptée pour tout usage anormal, état initial lu dans le registre.
- `registre_depense_v1.py`, avec deux garanties :
  - **écriture en tête** : la réserve est scellée avant chaque appel ;
  - **intégrité** : sceau (empreinte et nombre de lignes) et chaîne des empreintes de ligne.
- `adaptateur_fournisseur_v1.py` : gabarit de la forme « chat completions ».
  - `TransportNonCable` refuse tout envoi : le transport réel s'écrit **sous GO**.
  - `faux_fournisseur_v1.py` tient sa propre facture.
- `lanceur_pilote_essaim_v2.py` : refus de configuration avant tout appel, puis l'enchaînement réserve → appel → règlement, échec ou réserve comptée. Une exécution directe est refusée (code 20).

### 2.2 Les épreuves

`epreuves_lanceur_pilote_v2.py` → `epreuves-lanceur-pilote-v2.json` : **39 cas sur 39 tenus**. pytest (`test_lanceur_pilote_essaim_v2.py`) : 7 tests passés (`test-lanceur-pilote-v2-pytest.txt`).

- Critère de chaque cas :
  - le code attendu ;
  - une ligne d'arrêt au journal ;
  - **une dépense comptée au moins égale à la facture du faux fournisseur** ;
  - une dépense sous le plafond ;
  - sauf pour A8, déclaré comme limite.
- Cas sains :
  - P-std réaliste : 64,49 USD ;
  - tout au plafond : 176,45 ;
  - 74 échecs relancés ;
  - **pire extrême** (plafonds, 74 échecs facturés au plafond) : **198,80 comptés pour 193,57 facturés**, sous 203,94 ;
  - **processus tué pendant l'appel 101 puis reprise** : 63,13 comptés pour 62,93 facturés ;
  - relance identique d'un message ;
  - adaptateur : usage rendu exact.
- Les artefacts sont au tableau du § 1. S'y ajoutent les gardes de la v1 rejouées sous la v2 :
  - `max_tokens` de 24 001 ;
  - entrée de 64 961 octets ;
  - sortie rendue de 24 001 ;
  - H3 (5 000 jetons pour 1 000 octets) ;
  - 75 échecs ;
  - plafond de 50 USD ;
  - 13ᵉ message ;
  - appel hors plan ;
  - aucun adaptateur ;
  - couche d'appel nue ;
  - transport non câblé.
- **Forme du rejeu des attaques.** L'outil `attaques_lanceur_cl_v1.py` de CL-v3 appelle l'interface de la v3 : `courir(..., prix)`, avec un client sans adaptateur. Il ne peut pas tourner tel quel contre la v4. Chaque attaque y est **réécrite sous sa forme v4**, mêmes paramètres et même faux fournisseur facturant (cas nommés A1 à A10).

## 3. Rejeu

- **Rejeu court** (`rejouer_v4.sh`, depuis le bloc-notes) : tenu.
  - Devis, épreuves du devis, vrai pire et outils des deux relecteurs : à l'octet.
  - Épreuves du lanceur : égales hors horodatages.
  - pytest : 7 tests passés.
- **Rejeu long depuis une COPIE du dossier**, à un autre emplacement, pour éprouver l'indépendance de l'emplacement : résultat écrit au § 6.

## 4. Vrai pire sous la v4

Source : `calcul-vrai-pire-v4.json`.

| poste (P-std, Kimi) | USD |
|---|---|
| 744 appels aux plafonds de jetons | 176,448 |
| 74 échecs (relancés ou abandonnés) à la réserve dure maximale | 27,412 |
| excès d'un appel au-delà du plafond d'entrée | 0,084 |
| **total = plafond de dépense du registre** | **203,94** |

- Mêmes chiffres qu'en v3, pour toutes les espèces et toutes les tailles (P-8 : 135,87 ; P-24 : 407,80 sur Kimi).
- Ce qui change, c'est l'étendue de la garantie :
  - par pilote et non plus par invocation ;
  - avec une réserve comptée pour toute anomalie.
- **Hors borne** : un appel qui viole H3 (A8), ou un transport qui cacherait ses envois sans le dire, peuvent dépasser le plafond une fois avant l'arrêt. Seule la limite de 204 USD chez le fournisseur couvre ce cas, ainsi que H1 et H4.

## 5. Reste ouvert

Ce qui ne relève pas du code est dans `a-faire-avant-preenregistrement-pilote-v1.md` :
1. limite de 204 USD chez le fournisseur ;
2. essai de fumée sous GO pour H1 à H4 (devis : environ 0,22 USD) ;
3. tarif de Kimi relu à sa source ;
4. case servie gelée ;
5. garde des formes fausses : médiane de d_w ≤ +2 et au plus 2 mondes sur 12 au-delà de 16 formes ;
6. couverture structurelle ;
7. test de mort à 8 000 épisodes, avec la précision écrite ;
8. condition de la R3 ;
9. chemin unique du registre, et lanceur séquentiel.

Restent aussi :
- **R3 elle-même** (oracle) : la projection est à reconstruire depuis la liste blanche (point 8), puis à éprouver sur le jeu sain et sur E1 à E4.
- **Limites du contrôle des nombres** : un lecteur de formes et de valeurs exécutées ne voit pas une constante changée **par une fonction appelée plus tard**. La liste blanche interdit pourtant tout appel de niveau module dans la pièce des tests.
- **Limites du registre** : il n'empêche pas un registre neuf à un autre chemin, ni la réécriture de la dernière ligne avec son sceau. D'où la limite chez le fournisseur.

## 6. Rejeu long

`rejouer_v4.sh --long` lancé depuis une **copie** du dossier v4, placée hors du dépôt et ailleurs que l'original (racine donnée par `DEPOT_CONTROLE_IA`) : **rejeu tenu, code 0**.
- Toutes les étapes courtes se retrouvent à l'octet ou hors horodatages.
- Le test de mort v3 est égal hors horodatages à la sortie produite à l'autre emplacement : la sortie ne dépend plus de l'emplacement.
- Les bases sur la case (script et sortie de la v3, 12 mondes, 4 variantes) sont égales hors horodatages à `devis-et-instruments-v3/bases-case-servie-v1-sortie.json`.
- Ce rejeu est fait par l'auteur seul. Le rejeu depuis le commit, une fois versé, revient à un relecteur neuf.

## 7. Fichiers et empreintes (sha256)

| fichier | sha256 |
|---|---|
| `a-faire-avant-preenregistrement-pilote-v1.md` | `a1df4e7515f0da31b8f0d08f9a7dd9714bf3eecee9298647a29fd7b9216c07b9` |
| `adaptateur_fournisseur_v1.py` | `67704c1e42a0308a4f511ddc82e58666e6741b9b954f78072fd55a64c7eff1e4` |
| `artefacts-contre-lecture-v3-sur-devis-v4.txt` | `01234e6c43acfedcdd6ca343f52b54310fe40f898cd99c359df2783589db4832` |
| `artefacts-relecteur-v2-sur-devis-v4.txt` | `696c3ff297538cc14fe5a6cd0ab878b554adf9879a57687b7856e0919d653bdf` |
| `calcul-devis-essaim-v4.json` | `29b4cae6bc47725fc3e1172fefdf4cc2fe4b343ff1354bfa35aaff8cb601b2fa` |
| `calcul-vrai-pire-v4.json` | `50af6c64cbb31138d99949432e9116d4e7e133e92089046a1b614363e544306c` |
| `calcul_devis_essaim_v4.py` | `e5e61b25ccf24a6bbdcc29df6569bf80f5ffdf66d6f7c0a7a7207d99bacc7188` |
| `calcul_vrai_pire_v4.py` | `998067c222d36f8c66a4c92974af4a4318fb2a5d168f71f036c16762e7fe123f` |
| `compagnons_v4.sh` | `2c850743bcf6ae6d90dac7d91bbb3bed94901103d7feba779012959e1d267ca9` |
| `comparer_hors_horodatages_v1.py` | `3b64ed68a6af80b81443b4fdae3814751854661b785402a679c2d0d110e45d97` |
| `epreuves-devis-v4.json` | `1888ef9e52bec5601498904ffe0571ec0620cc85372e3522fa997d5cfb2d6949` |
| `epreuves-devis-v4.stdout` | `e6498da30029e92da218d141a503e6d1a4a6c8f419684638212ec5f0c2419b0e` |
| `epreuves-lanceur-pilote-v2.json` | `55796188e0f085fdc73b08b9458a5b822f8157bfe0b0c17fb2308f91270519f6` |
| `epreuves-lanceur-pilote-v2.stdout` | `4bd7d4d90ce350a856b86d637e5fc2cd4f792cf95f0f957d522cc67835b72964` |
| `epreuves_devis_v4.py` | `c25e89de110d03a7055e2c6534a1dd800a89fc3bffc41da2585aa0674bb83963` |
| `epreuves_lanceur_pilote_v2.py` | `4594e7521c86144e2fa2588802c2f4074fc6b3be74bf7291824807669c0b95c1` |
| `faux_fournisseur_v1.py` | `c89eaec2a0d2f450d31853bde597ccffb0f14cba7a9a4584318218f22b4c7869` |
| `garde_pilote_essaim_v2.py` | `d41305918b53d3bfa8b55ace148fdde6cf22f25623bcae2806585d0a242e4b84` |
| `juge_test_de_mort_isole_v2.py` | `ee0f68a19cea986ffb82c08ba59319924b121360ee10c74a05d4c379fffe0985` |
| `lanceur_pilote_essaim_v2.py` | `31cb79d34452a5761c91c43da8a907a4a24ac540297ad1a102bcfd1522d00a84` |
| `racine_depot_v1.py` | `3a5acf778146dc7df43716c082dc629f0251b8920a150940315863f235f0cccc` |
| `registre_depense_v1.py` | `f689dff2fd85bfce62f4151e16e0f2234765f2718481463dcd67f7cc1b1fe361` |
| `rejouer_v4.sh` | `4dfd99fb4550ab89ce27ada7f6c6fb6ef81d3efddeae100466792bd06bf06de5` |
| `test-de-mort-programme-v3-sortie.json` | `688eecf7c170cf04175b8bbe31ddc6a739f0fe24b5317e84d4058a863758c112` |
| `test-de-mort-programme-v3-sortie.stdout` | `e7c3215869b7e8d118bdef055fc20e27e2d74fce6df6b7eb3831f67d3f736054` |
| `test-lanceur-pilote-v2-pytest.txt` | `1703c71fb50d3e3cf60c84443f68d3f6933fa1aa6c6ae3cd69c4e821ebbb4644` |
| `test_de_mort_programme_v3.py` | `05f7f170d28176fdbc266f205e2678915634cc0c8c91bcdcb4d7f9c4c54de6f3` |
| `test_lanceur_pilote_essaim_v2.py` | `0480158e6fa991593a458916f2a6ff5efe9013a1c7e1f7d8876d8445aa825c75` |
| `rapport-devis-instruments-essaim-v4.md` | dans son compagnon `.sha256` |

Chaque fichier a son compagnon `.sha256` (format `empreinte  nom`, écrit par `compagnons_v4.sh`).
