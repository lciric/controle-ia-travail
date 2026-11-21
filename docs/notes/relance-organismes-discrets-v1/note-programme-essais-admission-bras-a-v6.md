# Note de livraison 7 — programme des deux essais d'admission du bras A, version 6

- État : LIVRÉE à la session le 21 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Opus 5.5, règle GO-2026-11-21-75), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`). Aucun réseau, aucun `git fetch`, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ni affichée, `GO_ID` jamais fixé.

## Journal
1. Lue : la vérification de la livraison 6 (`verification-programme-essais-admission-livraison6-v1.md`), en entier.
2. Six fichiers `_v6` créés par copie des `_v5` scellés (commit `8befb4975`). Les noms sont changés par un programme qui nomme les six fichiers un à un. Par `diff`, ils ne diffèrent des `_v5` que par les noms et les numéros de version. Les `_v5` et les outils de mutation version 1 ne sont pas touchés (`git diff --quiet`).
3. Codés dans le chef `_v6` :
   - R-1, le régime fermé de Google ;
   - m-a, l'âge du fixage compté depuis l'envoi ;
   - un contrôle des deux points d'accès de la file du juge, trouvé par la campagne de mutations (section 4).
4. Outils de mutation en version 2, pointés sur `_v6`, sous `tests/mutations_essais_admission_v2/`, avec une troisième campagne. Premier passage de la campagne neuve : 12 survivants. Après les artefacts : **344 tués sur 344**.
5. Trois lancements sur l'état livré : 207 essais passent, trois fois. Aucun relais laissé vivant.

## 1. Fichiers de la livraison 7 (noms neufs, R12)

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v6.py` | `49418dd6d418c39a2fda76a0fb6348a59bbf5dfe9dc52aac35614a183af9e627` |
| `scripts/relais_google_essais_admission_v6.py` | `3b5914ede81e5ccf07b19f8665a62a12ff99acabaebb248f1904493b375f7c61` |
| `scripts/relais_mistral_essais_admission_v6.py` | `73d1d13e145eefe0732629ba6554802e342b6b74049d15adb75632b678fb1a7d` |
| `tests/faux_fournisseur_essais_admission_v6.py` | `63cb79fa483739ae70d17b3f4292c1398c488be716aa3b95fa18f0639b522d16` |
| `tests/test_chef_essais_admission_bras_a_v6.py` | `20721bdc5df668f166f81de3fccff0a9b0ca1061856731999faebf00a601a802` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v6-gabarit.json` | `dc40a8118db98c0a1cdf6970c9d0892af36696d052135015755c0554f45706bc` |
| `tests/mutations_essais_admission_v2/campagne_mutations_v2.py` | `4831964650a2eda7b74c8607b25811f0a53fa6a945d4664ef002889545e599fe` |
| `tests/mutations_essais_admission_v2/greffe_mutant_v2.py` | `0e1005ccfe9e991750eed383b43bdc0f0182ea68170a438b29c2cdacd44dea6e` |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` (inchangé, toujours employé) | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` |

- Les relais et le faux fournisseur ne changent que de nom et de version.
- Le gabarit `_v6` porte le champ neuf `regime_file_google` et sa note, la note de l'âge du fixage complétée, et les empreintes des relais `_v6`.
- Le reste de la note de la livraison 6 (`note-programme-essais-admission-bras-a-v5.md`) vaut encore.

## 2. R-1 — régime prudent imposé pour Google

**Décision de la mère (R-4682, journal OD-315)** : régime prudent pour les lignes de Google, en vérification comme en file.

**Le champ fermé `regime_file_google`** (au premier niveau de la configuration) :
- au gabarit : `null` ;
- valeurs admises : « prudent » ou « courant », rien d'autre (ni casse autre, ni vrai, ni chaîne vide) ;
- en configuration définitive : « prudent » exigé, « courant » refusé ;
- aucun défaut : nul ou absent, toute ligne de Google s'arrête (`regime_file_google`, garde 10). La règle Google le lit à chaque ligne de Google, vérification comprise, et le recopie (`regle_google.regime_file_google`).
- Les lignes de Mistral ne le lisent pas.

**Effet sur la file du juge.** Sous « prudent », la file part au régime prudent **quelles que soient les sondes**. Deux sondes « comprises » ne la mettent plus au régime courant.
- Le mot de Lazar n'est exigé, comme avant, que si une sonde n'est pas « comprise ».
- Le contexte, le manifeste et le rapport portent `regime_impose_par_la_configuration` (« prudent (décision de la session mère, R-4682 …) »), à côté de `regime` et de `regime_de_depart`.
- Sous « courant », admis d'une configuration d'essai seulement, la file suit ses sondes (régime courant du devis, 6.4).
- La vérification de Google était déjà toujours au régime prudent ; rien n'y change.

**Conséquence à redire à Lazar (devis, 6.4)** : au régime prudent, un envoi sans compteur lisible est compté à 200 jetons par seconde de sa durée, et au moins à sa réserve. Un envoi de Neon coupé au délai total arrête la file, sans reprise. À 65 536, le plafond de la file est celui de l'avenant 2.

| essai | cas sain | artefact |
|---|---|---|
| `test_r1_l7_sain_la_file_du_juge_part_prudente_quelles_que_soient_les_sondes` | « prudent » et deux sondes « comprises » : file au régime prudent, sans mot ; règle Google ; admis en définitive ; la file entière jouée par l'amorce (`executer`, faux fournisseur) : le rapport dit `regime_de_depart` « prudent » et le régime imposé ; sous « courant » (essai), la file suit les sondes | — |
| `test_r1_l7_artefact_regime_de_google_absent_inconnu_ou_courant_en_definitive` | une ligne de Mistral part avec le champ nul | nul, « Prudent », chaîne vide, vrai : la garde 10 et la règle Google (vérification et file) refusent ; champ absent ; « courant » en définitive ; gabarit nul ; la file du juge refusée par `gardes_avant_depart` |

Lecture déclarée : le nom du champ est celui du message de la session, `regime_file_google`. La vérification proposait `regime_de_la_file_google`.

## 3. m-a — âge du fixage compté aussi depuis l'envoi

La borne `age_max_du_fixage_heures` se compte désormais deux fois :
- depuis l'heure de la pièce, comme avant ;
- **depuis l'heure de l'envoi** : le début du jour du fixage (minuit en temps universel) est au plus cette borne avant l'envoi. Sinon : « la pièce est trop ancienne pour ce taux, un fixage plus récent est à relever ».

C'est la même borne, non une borne propre : c'est la lecture la plus simple, et la plus prudente. Elle vaut pour toutes les pièces qui portent un taux :
- le constat ;
- la lecture de la console (garde 20) ;
- le mot de Lazar sur les sondes du juge (garde 10).

Ces deux dernières reçoivent maintenant l'heure de l'envoi, et la garde « heure du taux postérieure à l'envoi » vaut aussi pour elles.

**À dire à Lazar.** Sous une borne de 96 heures, un constat en euros ne sert que pendant quatre jours au plus après le jour de son fixage. Passé ce délai, il faut un taux frais, donc un constat neuf. Un constat tout en dollars n'est pas touché.

| essai | cas sain | artefact |
|---|---|---|
| `test_ma_l7_un_constat_vieux_d_un_mois_est_refuse` | le même constat, envoyé le jour même ; Mistral en dollars sans objet ; borne exacte de 96 heures depuis l'envoi admise ; lecture de la console lue à l'envoi | constat vieux d'un mois, à la garde et à `gardes_avant_depart` ; une minute au-delà de la borne ; lecture de la console six jours après ; la borne depuis la pièce reste sans envoi donné |

## 4. Les autres mineurs de la vérification de la livraison 6

| mineur | traité comment |
|---|---|
| m-7, deux fichiers hors du périmètre | **laissé, sur consigne** : toujours ` M` à `git status`, non touchés |
| plafonds en dollars, seuils de crédit, délais à 65 536 | **sans objet pour le code** (vérification, 6) : valeurs de configuration, à fixer par l'avenant 2 ; le débit requis est écrit au manifeste |
| m-4, sonde sous la forme « budget » | **sans objet** tant que le niveau est gardé |
| l'avenant 2 devrait écrire la pièce partielle | hors du code : à l'avenant 2 |

**Trouvé par la campagne neuve, et corrigé.** La garde 10 de la file du juge ne confrontait à la configuration que l'hôte du relevé de la clé 1. Le relevé de la clé 2 est déjà refusé seul s'il vient d'un autre point d'accès (`_releve_sain`). La garde exige maintenant aussi les deux hôtes égaux, comme les noms servis et les orthographes, et ne lit plus aucune valeur par le rang de la clé. C'est une défense en profondeur, éprouvée en substituant le relevé lu.

## 5. Campagne de mutations, version 2

Commande, depuis la racine du dépôt :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 .venv/bin/python -I tests/mutations_essais_admission_v2/campagne_mutations_v2.py toutes [SORTIE.json]`

Les noms `regle_google`, `livraison6` ou `livraison7` jouent une seule campagne ; `compter` donne le nombre de mutants. La version 1 (`tests/mutations_essais_admission_v1/`) reste, sur `_v5`.

| campagne | mutants | premier passage | dernier passage |
|---|---|---|---|
| règle Google | 108 | 108 tués | **108** |
| livraison 6 (`lire_taux` a grandi : 46) | 168 | 167 tués (la borne depuis la pièce, masquée par celle depuis l'envoi) | **168** |
| livraison 7 : `regime_file_google` 7, `garde_cle_verifiee` 61 | 68 | 56 tués | **68** |
| total | 344 | | **344 tués, 0 erreur** |

Les douze survivants de la garde 10 portaient sur des arrêts hérités qu'aucun essai n'éprouvait :
- la pièce du mot de Mistral (autre relevé, autre issue, autre majorant) ;
- la page ou l'heure absentes du mot du juge ;
- le crédit vu à 16,08 pile ;
- le libellé « clé 1 / clé 2 » des sondes ;
- un relevé de la bonne ligne sous une autre variable ;
- les noms servis et les hôtes différents.

Ils sont tués par `test_m2_l7_artefacts_ajoutes_par_la_campagne_de_la_livraison_7`.

## 6. Prêt à l'emploi

### (a) Constat de Mistral seul

Chemin : `docs/notes/relance-organismes-discrets-v1/constat-comptes-mistral-bras-a-AAAA-MM-JJ-vN.md`, avec son compagnon `.sha256`.

Règles :
- les sept clés, toutes et elles seules ;
- les heures en temps universel, antérieures à l'envoi ;
- « au moins X » seulement sur le crédit, de source « borne basse dite par Lazar » ;
- la ligne de taux seulement si la devise affichée est EUR, avec un fixage d'au plus `age_max_du_fixage_heures` avant la pièce **et avant l'envoi**.

Les valeurs entre chevrons sont à remplir. Toute autre ligne est à recopier telle quelle.

```
# Constat du compte Mistral — bras A

## Mot de Lazar

> <le mot de Lazar, cité>

## Tableau

| clé | valeur | source | heure (UTC) |
|---|---|---|---|
| mistral_offre_payante | oui | <page vue> | <AAAA-MM-JJTHH:MMZ> |
| mistral_donnees_pour_amelioration | désactivé | <page vue> | <AAAA-MM-JJTHH:MMZ> |
| mistral_cle_de_l_espace_constate | oui | <page vue> | <AAAA-MM-JJTHH:MMZ> |
| mistral_credit_utilisable_usd | <nombre, ou « au moins 7,87 »> | <page vue, ou « borne basse dite par Lazar »> | <AAAA-MM-JJTHH:MMZ> |
| mistral_limite_requetes_par_minute | <nombre ≥ 6> | <page vue> | <AAAA-MM-JJTHH:MMZ> |
| mistral_limite_jetons_par_minute | <nombre ≥ 100000> | <page vue> | <AAAA-MM-JJTHH:MMZ> |
| mistral_devise_affichee | <EUR ou USD> | <page vue> | <AAAA-MM-JJTHH:MMZ> |

- portée du constat : Mistral seul
- heure de la transcription (UTC) : <AAAA-MM-JJTHH:MMZ>
- taux : <T> USD par EUR ; source : <source> ; heure du taux (UTC) : <AAAA-MM-JJTHH:MMZ> ; fixage publié le : <AAAA-MM-JJ>
```

- Sans euros, la ligne `- taux` est retirée.
- Seuil : le crédit, converti au taux diminué de 5 %, au centime inférieur, est d'au moins 8,23 USD. Pour 7,87 €, il faut un taux d'au moins 1,1008 USD par EUR.

### (b) Configuration définitive des lignes de Mistral

À tirer du gabarit `_v6` sous un nom neuf, scellée. Les empreintes `""` sont à remplir par la session.

**Champs du premier niveau à changer :**

```json
{
 "version": "configuration-essais-admission-bras-a-v6-mistral-AAAA-MM-JJ-v1",
 "etat": "definitive",
 "marge_de_change": 0.05,
 "marge_de_change_go": "GO-2026-11-21-68",
 "age_max_du_fixage_heures": 96,
 "recharge_comptee": false,
 "regime_file_google": "prudent",
 "constat": {"chemin": "docs/notes/relance-organismes-discrets-v1/constat-comptes-mistral-bras-a-AAAA-MM-JJ-vN.md", "sha256": ""},
 "constat_second": {"chemin": null, "sha256": null},
 "regles": {"chemin": "<fichier des règles scellé, non gabarit>", "sha256": "", "lignes_du_texte": [521, 529],
            "gabarit": "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md"},
 "essai_local": null
}
```

Notes sur ces champs :
- `age_max_du_fixage_heures` : 96 est proposé ; c'est à décider.
- `regime_file_google` n'est pas lu par Mistral ; « prudent » est inscrit pour que la même configuration reste admise si elle sert Google plus tard.
- Tout le reste comme au gabarit `_v6` : `devis`, `verification_du_devis`, `avenant`, `constat_cles`, `cles_levees`, `fournisseurs.mistral` (relais `_v6`, `73d1d13e…`), `entrees`, `consignes`, `programme_de_forme`, `garde_interdits`, `hotes_permis`, `registre_go`, `messages`, `pages_de_prix`, débit et pauses.
- `fournisseurs.google` et les limites de mots peuvent rester nuls pour Mistral.

**Les trois lignes, sous `lignes` :**

```json
{
 "verification-mistral-eu": {
  "numero_au_devis": 1, "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 0.25, "plafond_registre": "0,25 USD",
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
  "releve_europeen": {"chemin": "runs/verification-cle-mistral-bras-a-v1/<dossier>/releve-verification-v1.json", "sha256": ""}
 },
 "file-mistral": {
  "numero_au_devis": 3, "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 4.75, "plafond_registre": "4,75 USD",
  "exces_possible_d_un_envoi_usd": 0.64,
  "marques_du_perimetre": ["essai d'admission du second lecteur", "24 appels"],
  "hote": "<api.eu.mistral.ai ou api.mistral.ai : celui du relevé retenu>", "dossier": "runs/essais-admission-bras-a-v1",
  "appels": 24, "envois_max": 48, "borne_octets": 262144, "reserve_sortie_jetons": 262208,
  "delais": {"silence_s": 600, "total_s": 2700, "relais_silence_s": 590, "relais_total_s": 2690},
  "entrees": "toutes", "lectures_console": [], "levees_cle": [],
  "releve_verification": {"chemin": "runs/verification-cle-mistral-bras-a-v1/<dossier>/releve-verification-v1.json", "sha256": ""},
  "inscrit": {"nom_servi": "<nom servi du relevé>", "hote": "<hôte du relevé>", "temperature_envoyee": "<true ou false, du relevé>"},
  "mot_de_lazar_sonde": null
 }
}
```

Pour chaque ligne :
- `go` : l'identifiant de sa ligne au registre ; `GO_ID` l'égale au lancement.
- `lectures_console` : une pièce par envoi coupé d'une ligne antérieure de Mistral.
- `levees_cle` : une pièce par alerte de clé (code de sortie 7).
- `releve_europeen` (point d'accès général seulement) : le relevé européen, signe « ne sert pas ce modèle » constaté (garde 15). La vérification globale ne part que si ce signe est constaté.
- `inscrit` (file seulement) : les trois valeurs sont égales à celles du relevé, et `temperature_envoyee` est un booléen JSON.
- `mot_de_lazar_sonde` (file seulement) : `null` si la sonde est « comprise » et le majorant « établi » ; sinon `{"chemin": "…/mots-de-lazar-sonde-de-borne-mistral-bras-a-AAAA-MM-JJ-v1.md", "sha256": ""}`, et la file part au régime prudent.

### (c) Ligne du registre des GO lue par la garde 8

Le registre est lu à la référence `origin/main:registres/go.md`, par `git show` local, sans réseau. La ligne doit donc être poussée, et la référence locale de `origin/main` doit la porter, avant le lancement.

Forme de la ligne :
- huit cellules séparées par « ` | ` » (espace, barre, espace), et aucune de ces suites à l'intérieur d'une cellule ;
- elle commence par « `| GO-… |` » ;
- une seule ligne porte l'identifiant ;
- `type` vaut `calcul`, `par` vaut `Lazar` ;
- la date d'accord n'est pas après le jour du lancement, et l'échéance n'est pas passée ;
- le plafond est à la lettre ;
- le périmètre porte toutes les marques et l'empreinte du devis ;
- les empreintes de la vérification du devis et de l'avenant figurent au périmètre ou à la référence ;
- aucune ligne `| révocation |` ne cite l'identifiant.

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | bras A, vérification de la clé de `mistral-large-4-0` sur `api.eu.mistral.ai`, trois appels au plus, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac | 0,25 USD | AAAA-MM-JJ | Lazar | <référence> |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | bras A, vérification de la clé de `mistral-large-4-0` sur `api.mistral.ai`, trois appels au plus, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac | 0,25 USD | AAAA-MM-JJ | Lazar | <référence> |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | bras A, essai d'admission du second lecteur, 24 appels, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac | 4,75 USD | AAAA-MM-JJ | Lazar | <référence> |
```

Si la configuration cite une autre version de l'avenant, c'est son empreinte qui va à la ligne. Les accents graves des marques sont à recopier tels quels. Les essais éprouvent cette forme exacte (`Monde.registre`).

## 7. Reste ouvert

- La valeur de `age_max_du_fixage_heures`, à décider.
- 7,87 € ne passent le seuil qu'à un taux d'au moins 1,1008.
- L'avenant 2 : plafonds, seuils et délais de Google à 65 536, et la lettre de la pièce partielle.
- m-7, sur décision de Lazar.
- Rien n'a été joué sur un vrai fournisseur.

## 8. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v6.py`

- Trois lancements : `207 passed in 97.02s`, `207 passed in 96.46s`, `207 passed in 94.54s`.
- Puis la campagne : `total 344 ; tués 344`.
- La suite entière du dépôt n'a pas été lancée (mandat).

## 9. Chemins ouverts, déclarés

- **Lus** : la vérification de la livraison 6 ; les `_v5` et `_v6` (par `diff` et par recherche de lignes) ; les outils de mutation version 1.
- **Écrits** : les six `_v6`, les deux outils version 2 et cette note.
- **Vu en passant, par erreur d'un motif de recherche trop large** (`grep` sur `scripts/*_v6.py`) : quelques lignes de trois fichiers hors du périmètre, aucun interdit — `scripts/banc_mutations_t06_v6.py`, `scripts/garde_credit_relais_v6.py`, `scripts/lancer_course_affinage_mentors_v6.py`.
- **Lus par le programme pendant les essais**, comme avant : le lot des entrées, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté. Aucun `sed`, aucune substitution hors de mes fichiers, nommés un à un. m-7 n'est pas touché.
