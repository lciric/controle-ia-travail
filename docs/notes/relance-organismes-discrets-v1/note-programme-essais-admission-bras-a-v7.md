# Note de livraison 8 — programme des deux essais d'admission du bras A, version 7

- État : LIVRÉE à la session le 21 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Opus 5.5), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`). Aucun réseau, aucun `git fetch`, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ni affichée, `GO_ID` jamais fixé.

## Journal
1. Lu : le relevé de la vérification réelle de la clé de Mistral, point d'accès européen (`runs/verification-cle-mistral-bras-a-v1/20261121-204032-verification-mistral-eu/releve-verification-v1.json`), et lui seul. Ni `envois/` ni `reponses-brutes-non-lues/` n'ont été ouverts. Ce que porte le relevé :
   - GO `GO-2026-11-21-81`, un seul appel compté, l'appel A, qui portait `temperature` ;
   - code 400 « top_p must be 1 when using greedy sampling. » (`invalid_request_greedy_sampling`, `param` nul) ;
   - classé à la ligne 13 du classement : non saine, nœud de Lazar ;
   - ligne close, `quand` 2026-11-21T20:40:36Z, dépense comptée 0,075988 USD au régime prudent ;
   - aucun envoi coupé.
2. Six fichiers `_v7` copiés des `_v6`, noms changés par un programme qui les nomme un à un. Par `diff`, ils ne diffèrent que par les noms. Outils de mutation en version 3 (`tests/mutations_essais_admission_v3/`). Les `_v6` et les outils version 2 ne sont pas touchés.
3. Codés dans le chef `_v7` : le champ fermé `temperature_retiree_d_avance`, l'appel A sans température, la fin de l'appel A′ sous un retrait, l'accord de la file et du relevé, la raison écrite au rapport, et la dépense de Mistral depuis le constat, écrite et dite (section 3).
4. Essais neufs écrits. Trois lancements : 215 passent, trois fois. Campagne de mutations : section 5.

## 1. Fichiers de la livraison 8 (noms neufs, R12)

Voir la section 8 pour les empreintes. Les relais et le faux fournisseur ne changent que de nom et de version. Le gabarit `_v7` porte le champ neuf, sa note, `a_remplir` complété et les empreintes des relais `_v7`. Le reste de la note de la livraison 7 (`note-programme-essais-admission-bras-a-v6.md`) vaut encore.

## 2. La température retirée d'avance

**Le champ fermé `temperature_retiree_d_avance`** (au premier niveau de la configuration) :
- au gabarit : `null` ;
- inscrit : soit `false`, soit `{"noeud": "<référence>", "go": "<GO de la ligne>"}`, exactement ces deux clés. `noeud` est une chaîne non vide ; `go` a la forme `GO-AAAA-MM-JJ-NN`.
- **toute ligne de Mistral** refuse un champ nul, absent ou d'une autre forme : « `temperature_retiree_d_avance` n'est pas inscrit », rien ne part. C'est vrai en définitive comme à l'essai ; aucun défaut. Le refus vient dès le début de `gardes_avant_depart`.
- une ligne de vérification exige que `go` soit **sa propre** ligne de calcul ; une file de Mistral n'en exige pas le GO ;
- les lignes de Google ne le lisent pas.

**Sous `false`** : rien ne change. La température est envoyée à l'appel A, puis retirée à l'appel A′ si elle est refusée (devis, 4.4, ligne 10).

**Sous l'objet** :
- l'appel A part avec le corps de l'appel A′ : `model`, `messages`, `max_tokens`, `reasoning_effort`, `stream`, **sans `temperature`** ;
- la sonde de borne (appel B) suit l'appel sain, donc part sans température elle aussi ;
- il n'y a **pas d'appel A′**. Si l'appel A est malgré tout classé à la ligne 10 (température refusée), la vérification se ferme : « température refusée alors qu'elle est retirée d'avance (aucun appel A′) … », nœud de Lazar ;
- le relevé porte `temperature_envoyee: false` et `temperature_retiree_d_avance` (`noeud`, `go`, `raison`) ;
- la file de Mistral exige alors un relevé qui n'a pas envoyé la température ; un relevé qui l'a envoyée est refusé (garde 10). Elle part sans température. Son contexte, son manifeste et son rapport portent `temperature_envoyee` et `raison_sans_temperature` : le retrait d'avance avec son nœud et son GO, ou, sans retrait, « température retirée à l'appel A′ de la vérification ».

**Le corps reste fermé** (garde 3, inchangée) : le jeu de champs est exact. Un `top_p`, à 1 ou à 1,0, est refusé avant l'envoi, avec ou sans température, comme toute `temperature` ajoutée à un corps qui n'en porte pas. Le relais de Mistral ne lit pas le corps : rien n'y change.

| essai | cas sain | artefact |
|---|---|---|
| `test_l8_sain_l_appel_a_part_sans_temperature_et_sans_appel_a_prime` | appel A sans température, puis sonde ; deux appels comptés, aucun A′ ; relevé `temperature_envoyee` faux, avec le retrait ; la file part sans température ; le rapport le dit, avec la raison ; sans retrait, la raison « appel A′ » | — |
| `test_l8_artefact_temperature_refusee_sous_un_retrait_d_avance_ferme_sans_appel_a_prime` | — | ligne 10 sous un retrait : un seul appel, fermé, nœud de Lazar ; un relevé avec température refusé à la file |
| `test_l8_artefact_champ_absent_ou_mal_forme_rien_ne_part` | `false`, l'objet de la ligne, la file sans contrôle du GO, Google sans le champ | nul, vrai, « oui », objet vide, nœud vide, GO mal formé, clé de plus (`top_p`), clé manquante, champ absent (essai et définitive), GO d'une autre ligne ; gabarit nul |
| `test_l8_le_corps_reste_ferme_aucun_top_p` | corps sans température contrôlé | `top_p` à 1 et à 1,0, `temperature` ajoutée, `top_p` sur un corps avec température |

## 3. Une ligne de vérification neuve après une ligne close en ligne 13

**Comportement exact**, éprouvé de bout en bout par l'amorce (`test_l8_une_ligne_neuve_apres_une_ligne_close_en_ligne_13`), sur le cas du 21 novembre (code 400 « top_p », ligne 13) :

1. **La ligne close ferme son identifiant seul.** L'état d'une ligne de vérification est lu par GO (`lancements_de_verification`, C-1). Sous le même GO, la ligne ne repart pas, retrait ou non : « la ligne … est close : ce qui se refait demande une ligne nouvelle » (code 2, aucun appel).
2. **Un GO neuf sans le retrait qui le nomme ne part pas.** Un objet qui nomme l'ancien GO est refusé (code 2, aucun appel).
3. **Un GO neuf, avec le retrait sous ce GO, part.**
   - Son état est vierge : compteur à zéro sous son plafond de 0,25 USD, trois appels.
   - La garde 8 exige sa ligne au registre, sous le nouvel identifiant (forme : note de la livraison 7, section 6 c).
   - Le relevé neuf est écrit dans un dossier neuf du même répertoire, à côté du dossier clos, qui n'est pas touché.
4. **La garde 13** ne lit que les files : sans objet pour une vérification.
5. **Les verrous** sont par fournisseur, libérés à la fin de chaque amorce : la ligne neuve les prend comme toute ligne.
6. **La lecture de la console (garde 20)** lit toutes les lignes antérieures de Mistral, toutes issues confondues. La ligne close du 21 novembre n'a aucun envoi coupé : rien n'est dû, et la ligne neuve n'est pas bloquée. Mais si une ligne antérieure, close ou non, portait un envoi coupé, la ligne neuve ne partirait pas sans la lecture de la console (`test_l8_artefact_une_ligne_neuve_ne_passe_pas_un_envoi_coupe_de_la_ligne_close`) : rien ne passe.
7. **La garde 15** (point d'accès général) exige toujours le relevé européen à signe constaté. Le relevé clos (signe non constaté) ne l'ouvre pas ; seul le relevé de la ligne neuve, s'il constate le signe, l'ouvrirait.
8. **C-1 du contrôle du crédit** (somme ou plus grande des deux dépenses) est propre à Google : sans objet chez Mistral.

**La dépense de la ligne close compte.**
- Elle reste lue (`lignes_jouees`) : 0,075988 USD sous `GO-2026-11-21-81`, à côté de la ligne neuve.
- **Ajout de cette livraison, écrit et dit, non refusé** : chaque ligne de Mistral écrit, au résumé du constat recopié au manifeste, au relevé et au rapport, la dépense des lignes de Mistral jouées **depuis l'heure de transcription du constat** (`depense_de_mistral_depuis_le_constat`). Cette dépense est retirée du crédit compté. Sous le seuil de 8,23 USD, l'amorce écrit « À DIRE À LAZAR » sur sa sortie d'erreur ; la ligne n'est pas refusée.
- Raison : le seuil de 8,23 USD couvre exactement les trois lignes du devis (0,25 + 1,17 ; 0,25 + 1,17 ; 4,75 + 0,64). Une vérification neuve en ajoute une. Refuser serait un seuil neuf, à décider par la mère (section 7).
- Une ligne jouée avant le constat n'est pas retirée : le crédit vu la porte déjà.
- Exemples : un constat de 9,50 USD laisse 9,424012 USD, au-dessus du seuil. À 8,25, il resterait 8,174012 USD, sous le seuil, et ce serait dit. Pour le crédit de « au moins 7,87 € » à 1,105, 8,26 USD moins 0,075988 laissent 8,18 USD, sous 8,23, et ce serait dit, si le constat est antérieur à 20:40Z.

| essai | cas sain | artefact |
|---|---|---|
| `test_l8_une_ligne_neuve_apres_une_ligne_close_en_ligne_13` | GO neuf avec retrait : état vierge, aucune lecture de console due, dépense de la ligne close lue et retirée ; vérification saine sans température, deux appels | même GO refusé ; GO neuf sous un retrait de l'ancien GO refusé ; aucun appel envoyé dans ces deux cas |
| `test_l8_artefact_une_ligne_neuve_ne_passe_pas_un_envoi_coupe_de_la_ligne_close` | — | envoi coupé à la ligne close, sans lecture de la console : la ligne neuve ne part pas (garde 20) |
| `test_l8_depense_de_mistral_depuis_le_constat_ecrite_et_dite` | 9,50 USD : reste 9,424012, rien à dire ; ligne antérieure au constat non retirée ; Google sans objet | 8,25 USD : reste 8,174012, dit |

## 4. Configuration définitive des lignes de Mistral, mise à jour, champ par champ

À tirer du gabarit `_v7` sous un nom neuf, scellée ; les empreintes `""` sont à remplir par la session. Une configuration par ligne de calcul : le retrait nomme le GO de la vérification qu'il sert.

**Premier niveau** (seuls les champs à changer par rapport au gabarit) :

```json
{
 "version": "configuration-essais-admission-bras-a-v7-mistral-AAAA-MM-JJ-v1",
 "etat": "definitive",
 "marge_de_change": 0.05,
 "marge_de_change_go": "GO-2026-11-21-68",
 "age_max_du_fixage_heures": 96,
 "recharge_comptee": false,
 "regime_file_google": "prudent",
 "temperature_retiree_d_avance": {"noeud": "journal OD-329, mot de Lazar « a go »", "go": "<GO neuf de la vérification européenne>"},
 "constat": {"chemin": "docs/notes/relance-organismes-discrets-v1/constat-comptes-mistral-bras-a-AAAA-MM-JJ-vN.md", "sha256": ""},
 "constat_second": {"chemin": null, "sha256": null},
 "regles": {"chemin": "<fichier des règles scellé, non gabarit>", "sha256": "", "lignes_du_texte": [521, 529],
            "gabarit": "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md"},
 "essai_local": null
}
```

- `temperature_retiree_d_avance` : son `go` est l'identifiant neuf de la vérification européenne, qui doit aussi figurer à `lignes.verification-mistral-eu.go`. Pour la configuration de la vérification globale, c'est son propre GO. Pour la file, l'objet de la vérification retenue, ou `false` (la file n'en contrôle pas le GO ; elle exige alors seulement un relevé sans température).
- `age_max_du_fixage_heures` : 96 est proposé ; c'est à décider.
- `regime_file_google` n'est pas lu par Mistral.
- Le reste comme au gabarit `_v7` : `devis`, `verification_du_devis`, `avenant`, `constat_cles`, `cles_levees`, `fournisseurs.mistral` (relais `_v7`), `entrees`, `consignes`, `programme_de_forme`, `garde_interdits`, `hotes_permis`, `registre_go`, `messages`, `pages_de_prix`, débit, pauses.
- `fournisseurs.google` et les limites de mots peuvent rester nuls.
- `fournisseurs.mistral.temperature` reste 0 : elle n'est plus envoyée sous le retrait.

**Les trois lignes, sous `lignes`** :

```json
{
 "verification-mistral-eu": {
  "numero_au_devis": 1, "go": "<GO neuf, autre que GO-2026-11-21-81>", "plafond_usd": 0.25, "plafond_registre": "0,25 USD",
  "exces_possible_d_un_envoi_usd": 1.17,
  "marques_du_perimetre": ["vérification de la clé de `mistral-large-4-0` sur `api.eu.mistral.ai`", "trois appels au plus"],
  "hote": "api.eu.mistral.ai", "dossier": "runs/verification-cle-mistral-bras-a-v1",
  "appels_max": 3, "envois_max": 3, "borne_octets": 32768, "reserve_sortie_jetons": 32832,
  "delais": {"silence_s": 600, "total_s": 2700, "relais_silence_s": 590, "relais_total_s": 2690},
  "lectures_console": [], "levees_cle": []
 },
 "verification-mistral-global": {
  "numero_au_devis": 5, "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 0.25, "plafond_registre": "0,25 USD",
  "exces_possible_d_un_envoi_usd": 1.17,
  "marques_du_perimetre": ["vérification de la clé de `mistral-large-4-0` sur `api.mistral.ai`", "trois appels au plus"],
  "hote": "api.mistral.ai", "dossier": "runs/verification-cle-mistral-bras-a-v1",
  "appels_max": 3, "envois_max": 3, "borne_octets": 32768, "reserve_sortie_jetons": 32832,
  "delais": {"silence_s": 600, "total_s": 2700, "relais_silence_s": 590, "relais_total_s": 2690},
  "lectures_console": [], "levees_cle": [],
  "releve_europeen": {"chemin": "runs/verification-cle-mistral-bras-a-v1/<dossier de la ligne neuve>/releve-verification-v1.json", "sha256": ""}
 },
 "file-mistral": {
  "numero_au_devis": 3, "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 4.75, "plafond_registre": "4,75 USD",
  "exces_possible_d_un_envoi_usd": 0.64,
  "marques_du_perimetre": ["essai d'admission du second lecteur", "24 appels"],
  "hote": "<hôte du relevé retenu>", "dossier": "runs/essais-admission-bras-a-v1",
  "appels": 24, "envois_max": 48, "borne_octets": 262144, "reserve_sortie_jetons": 262208,
  "delais": {"silence_s": 600, "total_s": 2700, "relais_silence_s": 590, "relais_total_s": 2690},
  "entrees": "toutes", "lectures_console": [], "levees_cle": [],
  "releve_verification": {"chemin": "runs/verification-cle-mistral-bras-a-v1/<dossier de la ligne neuve>/releve-verification-v1.json", "sha256": ""},
  "inscrit": {"nom_servi": "<nom servi du relevé>", "hote": "<hôte du relevé>", "temperature_envoyee": false},
  "mot_de_lazar_sonde": null
 }
}
```

Ce qui change depuis la livraison 7 :
- l'identifiant de la vérification européenne est neuf : `GO-2026-11-21-81` est clos ;
- les relevés cités sont ceux de la ligne neuve, non le relevé clos ;
- `inscrit.temperature_envoyee` vaut `false`, comme le relevé fait sous le retrait ;
- `lectures_console` reste vide : la ligne close n'a aucun envoi coupé ;
- le registre porte une ligne neuve pour la vérification européenne, sous la forme de la note de la livraison 7, section 6 c, avec son identifiant neuf.

## 5. Campagne de mutations, version 3

Commande, depuis la racine du dépôt :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 .venv/bin/python -I tests/mutations_essais_admission_v3/campagne_mutations_v3.py toutes [SORTIE.json]`

Les campagnes : `regle_google`, `livraison6`, `livraison7` (garde 10 grandie : 70 mutants), et `livraison8` (`temperature_retiree_d_avance` 13, `suite_de_la_verification` 25, `depense_de_mistral_depuis_le_constat` 10).

- Premier passage de `livraison8` : 42 tués sur 48. Les survivants portaient sur trois retours de la suite de la vérification, une ligne jouée à la minute de la transcription, l'arrondi à six décimales et le reste au seuil pile.
- Ils sont tués par `test_m2_l8_artefacts_ajoutes_par_la_campagne_de_la_livraison_8`.
- Résultat final : section 8.

## 6. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v7.py`

Trois lancements : `215 passed in 98.50s`, `215 passed in 97.95s`, `215 passed in 100.20s`. La suite entière du dépôt n'a pas été lancée (mandat).

## 7. Reste ouvert, à dire

- **La dépense de Mistral depuis le constat est écrite et dite, non refusée.** Refuser sous 8,23 USD après une ligne close serait un seuil neuf ; c'est à la mère de décider. Avec « au moins 7,87 € », un constat antérieur au 21 novembre à 20:40Z laisse 8,18 USD à 1,105 : ce serait dit. Un constat neuf, postérieur, l'éviterait.
- La valeur de `age_max_du_fixage_heures`.
- L'avenant 2 (Google à 65 536 ; lettre de la pièce partielle) ; m-7, sur décision de Lazar.
- Rien n'a été joué sur un vrai fournisseur.

## 8. Empreintes et sorties finales

La note elle-même n'est pas empreintée ici : la session la scelle. Le fichier des règles reste inchangé (`4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c`).

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v7.py` | `7c63d051406989e7928c0f6796ac6edb2033920fe18bfd12798e6e7227024806` |
| `scripts/relais_google_essais_admission_v7.py` | `f7c938bdecba215a2343f9aad3f23a67a590e3ab198a23bda4f42a6c11632dbb` |
| `scripts/relais_mistral_essais_admission_v7.py` | `ed35b54954283ba5b55c403d28dc550c56283b7ac70d7b30701b82ddd13e26e7` |
| `tests/faux_fournisseur_essais_admission_v7.py` | `4d354b2eeb052aff5c2db562af8ec104f6b32718b75b4e35183ff799e289c72f` |
| `tests/test_chef_essais_admission_bras_a_v7.py` | `39b2be3adebd8140efe5778073dbc48bfd8939cdd9c614d3bd56eb328a671786` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v7-gabarit.json` | `e1da213381578744c067da0fcfa7e1b67daf4d9ac00ebbed97971fc447275425` |
| `tests/mutations_essais_admission_v3/campagne_mutations_v3.py` | `3ac72c5d728e632468981a62f9c0932f0a858a002daa0b8ec190781e084e0360` |
| `tests/mutations_essais_admission_v3/greffe_mutant_v3.py` | `8ec985c34307301a166e08ba8d5413e6bf4f73066ce0ddec2cf7c362b2735095` |

- Trois lancements de la commande d'essai : `215 passed`, trois fois (section 6).
- Campagne de mutations, version 3, sur ce même état, code de sortie 0 : règle Google 108, livraison 6 168, livraison 7 77, livraison 8 48, soit **401 mutants, 401 tués, 0 erreur**.
- Aucun relais laissé vivant ; les fichiers `_v6` et les outils version 2 sont inchangés (`git diff --quiet`).
- Constat en passant : les deux fichiers de m-7 ne paraissent plus modifiés à `git status` ; je n'y ai pas touché.

## 9. Chemins ouverts, déclarés

- **Lus** : le relevé de la vérification réelle nommé au journal, et lui seul de ce dossier (ni `envois/` ni `reponses-brutes-non-lues/`) ; les `_v6` et `_v7` (par `diff` et par recherche de lignes) ; les outils de mutation version 2.
- **Écrits** : les six `_v7`, les deux outils version 3 et cette note.
- **Lus par le programme pendant les essais**, comme avant : le lot des entrées, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté. Aucun `sed`, aucune substitution hors de mes fichiers, nommés un à un. m-7 n'est pas touché.
