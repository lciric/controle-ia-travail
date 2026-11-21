# Note de livraison 6 — programme des deux essais d'admission du bras A, version 5

- État : LIVRÉE à la session le 21 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Opus 5.5, règle GO-2026-11-21-75), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`). Aucun réseau, aucun `git fetch`, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ni affichée, `GO_ID` jamais fixé.

## Journal
1. Lus : le mandat, la note de la livraison 5 (`note-programme-essais-admission-bras-a-v4.md`), sa vérification (`verification-programme-essais-admission-livraison5-v1.md`), en entier ; la section « Ce que le programme attend de Lazar » de la note de la livraison 4.
2. Point de départ vérifié : `diff` des six fichiers `_v5` contre les `_v4` ; ils ne diffèrent que par les noms et les numéros de version (en-têtes, `VERSION`, chemins des modules, usage, chemins des relais au gabarit). Les empreintes des relais au gabarit étaient encore celles des `_v4` ; elles sont régénérées.
3. Codés dans le chef `_v5` : la lecture du constat par fournisseur (D-1), l'âge du fixage du taux, le crédit dit comme une borne, la borne de réflexion « la plus haute admise », le débit requis écrit. Essais existants adaptés (le constat se lit désormais pour un fournisseur nommé) ; essais neufs écrits.
4. Outils de mutation versés au dépôt, adaptés à `_v5` (section 6). Premier passage : la campagne de la règle Google (108 mutants, 105 tués) et la campagne neuve (163 mutants, 138 tués). Artefacts ajoutés pour chaque survivant. Second passage : **271 tués sur 271**.
5. Trois lancements sur l'état livré : 203 essais passent, trois fois (section 8). Aucun relais laissé vivant. Les six fichiers `_v4` suivis sont inchangés (`git diff --quiet`).

## 1. Fichiers de la livraison 6 (noms neufs, R12)

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v5.py` | voir section 10 |
| `scripts/relais_google_essais_admission_v5.py` | `ea60a3c5d694df463dd8a5a3f22a73700e239af5b7124e1f13e98b48921be0bf` |
| `scripts/relais_mistral_essais_admission_v5.py` | `cc7273cb0e3c48b9bbb9860e847a37d21fa4a008737c2c0f7bf2ce45261862a7` |
| `tests/faux_fournisseur_essais_admission_v5.py` | `fe2baf80caf8e45fba89367d6a7662e316f6f3e4be1270ca64a109cecfdf8040` |
| `tests/test_chef_essais_admission_bras_a_v5.py` | voir section 10 |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v5-gabarit.json` | voir section 10 |
| `tests/mutations_essais_admission_v1/campagne_mutations_v1.py` (neuf) | voir section 10 |
| `tests/mutations_essais_admission_v1/greffe_mutant_v1.py` (neuf) | voir section 10 |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` (inchangé, toujours employé) | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` |

Les deux relais et le faux fournisseur ne changent que de nom et de numéro de version. Tout le reste des notes des livraisons 4 et 5 vaut encore : gardes et leurs essais, formes des pièces de Lazar hors du constat et du taux, lignes de calcul attendues au registre, écarts déjà dits.

## 2. D-1 — le constat se lit par fournisseur

**Ce qui change.** La garde 9 se joue pour le seul fournisseur de la ligne (`garde_constat(config, racine, instant, fournisseur)`).
- Une ligne de Mistral ne juge que les sept clés `mistral_*` : valeurs admises et seuils de Mistral (crédit ≥ 8,23 USD après conversion, 6 requêtes et 100 000 jetons par minute). Elle ne lit aucune clé de Google, aucun seuil de Google.
- Une ligne de Google ne juge que les vingt et une clés `google_*` et ses seuils (19,76 et 16,08 USD par projet, au contrôle du crédit). Le crédit de Mistral ne l'arrête plus.
- La ligne de taux est **exigée** si un montant jugé est en euros. Elle est **refusée** si aucun montant de la pièce n'est en euros. Elle n'est **ni lue ni contrôlée** si seul un montant de l'autre fournisseur est en euros : un compte Google en euros n'impose plus de taux à une ligne de Mistral, et l'inverse.
- Le manifeste, le relevé et le rapport recopient la pièce employée (champ, chemin, empreinte), sa portée et le fournisseur jugé (`constat_resume.piece`, `portee`, `fournisseur_juge`).

**Pièces.** La configuration inscrit `constat` (exigée) et `constat_second` (facultative, nulle au gabarit).
- Une pièce sans ligne de portée est le constat complet : ses vingt-huit clés sont exigées, toutes et elles seules. Une clé de Google absente arrête donc aussi une ligne de Mistral : aucune absence en silence.
- Une pièce partielle dit sa portée hors du tableau, par la ligne « - portée du constat : Mistral seul » ou « - portée du constat : Google seul ». Son tableau est **fermé par cette portée** : les sept clés de Mistral, ou les vingt et une de Google, toutes et elles seules. Une clé de l'autre fournisseur y est refusée (« de trop … de l'autre fournisseur »).
- Une ligne lit **la seule pièce** qui porte son fournisseur. Aucune pièce qui le porte : la ligne ne part pas. Deux pièces qui le portent (un constat complet et une pièce partielle du même fournisseur) : ambiguïté, la ligne ne part pas.
- Ensuite, pour l'autre fournisseur : soit une configuration neuve dont `constat` est le constat complet, soit la pièce partielle de l'autre sous `constat_second`.

La forme exacte est écrite au gabarit, sous `pieces_de_lazar.constat_partiel` et `constat.forme`.

**Écart déclaré à l'avenant 1 (5.1).** L'avenant dit une pièce à vingt-huit clés. La pièce partielle est une forme neuve, voulue par la vérification (D-1, « deux formes possibles ») et par la session mère. Elle n'admet aucune clé levée de plus et ne change aucun seuil.

| essai | cas sain | artefact |
|---|---|---|
| `test_d1_l6_mistral_part_sur_un_constat_de_mistral_seul` | pièce de Mistral seul : la vérification européenne et la file de Mistral passent leurs gardes | clé de Google ajoutée ; clé de Mistral absente ; portée non dite ; portée mal écrite ; crédit de Mistral sous le seuil ; file du juge refusée |
| `test_d1_l6_google_refuse_un_constat_de_mistral_seul` | pièce de Google seul ajoutée sous `constat_second` : Google part sur elle, Mistral sur `constat` | Google refusé, à la garde et par le chef entier (code de sortie 2, rien dans `runs/`) |
| `test_d1_l6_un_credit_de_mistral_bas_n_arrete_plus_google` | crédit de Mistral à 8,00 USD : Google part ; Mistral en euros : Google part sans taux | Mistral refusé sous le seuil, puis sans taux ; une clé de Google hors des valeurs admises arrête Google et non Mistral |
| `test_d1_l6_google_part_sur_un_constat_de_google_seul` | pièce de Google seul : Google part, crédits comptés | Mistral refusé ; clé de Mistral ajoutée ; clé de Google absente ; euros sans taux |
| `test_d1_l6_une_seule_piece_par_fournisseur` | `constat_second` nul : sans effet | deux pièces qui portent Mistral ; `constat_second` mal formé, sans empreinte, d'une autre empreinte |
| `test_d1_l6_lignes_de_mistral_a_blanc_sans_rien_de_google` | lignes de Mistral à blanc, sur un constat de Mistral seul, règle Google laissée nulle comme au gabarit | ligne de Google refusée |

Essais existants adaptés : `test_garde_9_un_artefact_par_cle` vérifie désormais qu'un artefact sur une clé n'arrête que les lignes de son fournisseur, l'autre étant lu sain. La garde 20, le relevé à blanc et le contrôle du crédit lisent le constat du fournisseur de leur ligne.

## 3. Âge du taux : le dernier fixage publié

**Décision de la session mère.** Le dernier fixage publié est admis quand aucun plus récent n'existe (fin de semaine, jour férié).

**Configuration.** La borne d'âge vit sous `age_max_du_fixage_heures` : nulle au gabarit, exigée d'une configuration définitive (même sans montant en euros), et de toute configuration dès qu'un taux est lu. C'est un entier de 1 à 168 heures. 96 heures couvrent un fixage du vendredi lu le lundi, même férié.

**Pièce.** La date de publication du fixage est portée sur la ligne de taux, partout où une ligne de taux est lue (constat, mot sur la sonde de Google, lecture de la console) :

`- taux : T USD par EUR ; source : … ; heure du taux (UTC) : AAAA-MM-JJTHH:MMZ ; fixage publié le : AAAA-MM-JJ`

L'ancienne forme, sans la date du fixage, est refusée.

**Ce que le programme vérifie d'un taux lu** :
1. le taux est un nombre strictement positif, et la source n'est pas vide ;
2. l'heure du taux (l'heure où il a été relevé) est lisible, antérieure à l'envoi, au plus 24 heures avant le montant le plus tardif et au plus 6 heures après le montant le plus ancien. Ces bornes sont inchangées, m-5 compris ;
3. la date du fixage est lisible (AAAA-MM-JJ) et n'est pas après l'heure du taux ;
4. le début du jour du fixage (minuit en temps universel, la lecture la plus ancienne, donc prudente) est au plus `age_max_du_fixage_heures` avant l'heure de la pièce (le montant le plus tardif). Au-delà : « un fixage plus récent est à relever ».

Le programme ne peut pas savoir si un fixage plus récent existe ; la borne le dit à sa place. Le taux recopié au manifeste porte `fixage_publie_le` et `age_max_du_fixage_heures`.

| essai | cas sain | artefact |
|---|---|---|
| `test_age_du_fixage_l6_le_dernier_fixage_publie_admis_dans_sa_borne` | fixage de trois jours sous 96 heures ; borne portée à 168 | au-delà de 96 heures ; fixage après l'heure du taux ; date illisible ; ancienne forme ; borne absente |
| `test_configuration_definitive_ce_qu_elle_exige` | 96 heures | borne nulle, 0, 169, 48,5, vrai, « 96 » |
| `test_m2_l6_artefacts_ajoutes_par_la_campagne_de_la_livraison_6` | bornes exactes admises : 24 heures avant, 6 heures après, fixage du jour même à minuit, 96 heures pile, borne de 1 heure, taux sous 1 | taux nul, source vide, heure illisible, heure du taux à l'instant de l'envoi |

## 4. Crédit dit comme une borne

Lazar a dit le crédit de Mistral « au moins 7,87 € ».
- **Forme admise.** Une clé de crédit peut valoir « au moins X », X en chiffres et dans la devise affichée, avec pour source exactement « borne basse dite par Lazar ».
- **Lecture.** La valeur est lue comme X, côté prudent, et comparée aux seuils comme X.
- **Ce qui est écrit.** Les clés concernées sont recopiées au manifeste (`constat_resume.bornes_basses_lues_comme_leur_valeur`).
- **Clés de crédit, et elles seules.** `mistral_credit_utilisable_usd`, `google_credit_vu_projet_a|b`, `google_credit_apres_une_recharge_projet_a|b`. La forme sur toute autre clé est refusée, même avec la bonne source. La source sans la forme est refusée, et la forme sans la source aussi.
- **Recharge comptée.** Sous `recharge_comptee` vrai (chemin de l'avenant, désactivé en définitive), une borne basse sur un crédit vu dont la recharge est relevée est refusée : l'écart d'une recharge ne se lit pas sur une borne.

**À dire à Lazar.** À la marge de change de 5 %, 7,87 € passent le seuil de 8,23 USD seulement si le taux vaut au moins **1,1008** USD par EUR (7,87 × 1,1008 × 0,95 = 8,2301). À 1,0700, le crédit compté vaut 7,99 USD, et la ligne de Mistral ne part pas.

| essai | cas sain | artefact |
|---|---|---|
| `test_borne_basse_l6_credit_dit_au_moins_x_lu_comme_x` | « au moins 9,50 » USD lu comme 9,50 ; « au moins 7,87 » € à 1,1100 : 8,29 USD ; crédit vu de Google « au moins 21,00 » | 7,87 € à 1,0700 : 7,99 sous le seuil ; forme sur deux limites de Mistral et sur une clé de Google ; recharge comptée |
| `test_borne_basse_l6_artefacts_sur_le_credit_de_mistral` (quatre cas) | — | forme sans la source ; source sans la forme ; borne non numérique ; borne sous le seuil |

## 5. Borne de réflexion sous un niveau : au plus 49 536 sous 65 536, paramétrable

Sous la forme `{"forme": "niveau", "borne_declaree": N}`, N vaut :
- un entier au plus égal à `sortie_max` moins 16 000 (refus au-delà, comme avant) ;
- ou la chaîne « la plus haute admise », lue comme `sortie_max` moins 16 000, soit 49 536 sous 65 536.

Une borne plus basse que la plus haute est admise, mais elle est dite au manifeste (`regle_google.borne_sous_la_plus_haute`) : un jeton facturé au-dessus arrête la file (C-2). La forme « budget » reste un entier. Le relais reçoit la borne lue (`--borne-reflexion 49536`).

| essai | cas sain | artefact |
|---|---|---|
| `test_borne_de_reflexion_l6_au_plus_49536_sous_65536_parametrable` | 49 536, « la plus haute admise », 40 000 (dite) : contrôle de la configuration, corps à 65 536, argument du relais ; 16 001 : borne 1 | 49 537 ; « la plus haute admise » sans plafond ; plafond de 16 000 ; « la plus haute admise » sous la forme budget |

## 6. Les mineurs encore ouverts de la vérification de la livraison 5

| mineur | traité comment | essai |
|---|---|---|
| m-2, réserve : les outils dans le bloc-notes | **fermé** : versés sous `tests/mutations_essais_admission_v1/`, adaptés à `_v5`, avec une commande qui les rejoue. Les mutants vivent dans un dossier temporaire hors du dépôt ; aucun fichier du dépôt n'est modifié. Les fichiers ne s'appellent pas `test_*` : la suite ne les collecte pas | `test_m2_l6_…` (artefacts de la campagne neuve) |
| m-4, sonde sous la forme « budget » | **sans objet** tant que Lazar garde le niveau (vérification, section 3) ; non codé | — |
| m-6, découplage de Mistral et de Google | **fermé** par D-1 (section 2) | section 2 |
| m-7, deux fichiers hors du périmètre | **laissé, sur consigne** : `scripts/epreuve_temoins_seuls_v3.py` et `scripts/lancer_course_affinage_mentors_v3.py` restent modifiés (`git status` : ` M`), non touchés | — |
| vérification, section 4 : délais à 65 536 | **écrit, non refusé** : `regle_google.debit_requis_a_la_sortie_maximale_jetons_par_s` (sortie maximale divisée par `relais_total_s` de la ligne) est porté au manifeste : 24,4 à 65 536 sous 2 690 secondes, 12,2 à 32 768. Relever `delais.total_s` et `relais_total_s` de la file du juge reste à l'avenant 2 | `test_debit_requis_l6_ecrit_a_la_regle_de_google` |
| vérification, section 4 : plafonds en dollars et seuils de crédit à 65 536 | **non codé, à l'avenant 2** : `plafond_usd`, `plafond_registre`, les lignes du registre, 19,76 et 16,08 sont des valeurs de configuration, dérivées du devis | — |

**Commande de la campagne**, depuis la racine du dépôt :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 .venv/bin/python -I tests/mutations_essais_admission_v1/campagne_mutations_v1.py toutes [SORTIE.json]`

Avec `regle_google` ou `livraison6` à la place de `toutes`, une seule campagne est jouée ; avec `compter`, le programme donne le nombre de mutants. Le code de sortie vaut 0 si tous les mutants sont tués.

| campagne | fonctions | mutants | premier passage | second passage |
|---|---|---|---|---|
| règle Google (celle de la livraison 5, rejouée sur `_v5`) | `garde_google_avant_envoi` 26, `defaut_de_reponse_google` 13, `borne_dementie` 6, `reglage_de_reflexion` 19, `controler_la_configuration_de_google` 26 ; relais : `defaut_du_corps` 18 | 108 | 105 tués | **108 tués** |
| livraison 6 | `portee_du_constat` 5, `lire_constat` 92, `pieces_de_constat` 7, `garde_constat` 9, `resume_du_constat` 2, `age_max_du_fixage` 7, `lire_taux` 41 | 163 | 138 tués | **163 tués** |

Il y a 108 mutants au lieu de 91 : `reglage_de_reflexion` et `controler_la_configuration_de_google` ont grandi (sections 5 et 6). Les trois survivants du premier passage portaient sur une borne exacte du plafond et sur le délai nul ou unité ; les vingt-cinq de la campagne neuve sur des bornes exactes (24 heures, 6 heures, fixage, instant de l'envoi) et sur des arrêts que nul essai n'éprouvait encore, dont plusieurs hérités des livraisons d'avant (taux nul, source vide, clé en double, sans source, transcription absente). Chacun est tué par un artefact ou par un cas sain à la borne. Limites : une seule mutation à la fois ; les fonctions qui appellent ces gardes ne sont pas mutées.

## 7. Configuration définitive des lignes de Mistral, et forme d'un constat de Mistral seul

### 7.1 Constat de Mistral seul

Chemin : `docs/notes/relance-organismes-discrets-v1/constat-comptes-mistral-bras-a-AAAA-MM-JJ-vN.md`, scellé (compagnon `.sha256`), inscrit sous `constat` (ou sous `constat_second` si `constat` est une pièce de Google seul). Les valeurs ci-dessous sont des exemples de forme ; les heures sont en temps universel, antérieures à l'envoi.

```
# Constat du compte Mistral — bras A

## Mot de Lazar

> (le mot de Lazar, cité, au moins une ligne non vide)

## Tableau

| clé | valeur | source | heure (UTC) |
|---|---|---|---|
| mistral_offre_payante | oui | console, facturation | 2026-11-23T09:10Z |
| mistral_donnees_pour_amelioration | désactivé | console, confidentialité | 2026-11-23T09:11Z |
| mistral_cle_de_l_espace_constate | oui | console, clés | 2026-11-23T09:12Z |
| mistral_credit_utilisable_usd | au moins 7,87 | borne basse dite par Lazar | 2026-11-23T09:13Z |
| mistral_limite_requetes_par_minute | 60 | console, limites | 2026-11-23T09:14Z |
| mistral_limite_jetons_par_minute | 500000 | console, limites | 2026-11-23T09:14Z |
| mistral_devise_affichee | EUR | console, facturation | 2026-11-23T09:13Z |

- portée du constat : Mistral seul
- heure de la transcription (UTC) : 2026-11-23T09:30Z
- taux : 1,1050 USD par EUR ; source : BCE, cours de référence ; heure du taux (UTC) : 2026-11-23T09:40Z ; fixage publié le : 2026-11-20
```

Règles : les sept clés, toutes et elles seules, aucune clé `google_*`. Aucune clé de Mistral n'est levable. `mistral_credit_utilisable_usd` porte un nombre, ou « au moins X » avec la source « borne basse dite par Lazar ». La ligne de taux est exigée si `mistral_devise_affichee` vaut EUR, et refusée si elle vaut USD. Avec le taux de l'exemple, 7,87 × 1,1050 × 0,95 = 8,26 USD, au-dessus de 8,23.

### 7.2 Champs communs d'une configuration définitive qui sert une ligne de Mistral

Tirée du gabarit `_v5`, sous un nom neuf (R12), scellée.

| champ | valeur définitive |
|---|---|
| `version` | nom neuf de la configuration (par exemple `configuration-essais-admission-bras-a-v5-mistral-AAAA-MM-JJ-v1`) |
| `etat` | `definitive` |
| `devis`, `verification_du_devis`, `avenant` | ceux du gabarit (empreintes `421ee2e6…`, `0bec479f…`, `5e255c5f…`), ou la version acceptée de l'avenant |
| `marge_de_change` | `0.05` |
| `marge_de_change_go` | `GO-2026-11-21-68` |
| `age_max_du_fixage_heures` | entier de 1 à 168, à décider (96 couvre une fin de semaine et un lundi férié) |
| `recharge_comptee` | `false` |
| `constat` | `{"chemin": "…/constat-comptes-mistral-bras-a-AAAA-MM-JJ-vN.md", "sha256": "…"}` |
| `constat_second` | `{"chemin": null, "sha256": null}` tant que la pièce de Google n'existe pas |
| `constat_cles`, `cles_levees` | ceux du gabarit, inchangés (vingt-huit règles ; six clés de Google levables) |
| `regles` | `{"chemin": …, "sha256": …}` du fichier des règles scellé, non gabarit (exigé de la file seule) |
| `essai_local` | `null` (garde 14) |
| `fournisseurs.mistral` | celui du gabarit, inchangé (relais `_v5`, `cc7273cb…`) |
| `fournisseurs.google`, `consignes.*.limite_de_mots` | peuvent rester nuls : une ligne de Mistral ne les lit pas (`test_d1_l6_lignes_de_mistral_a_blanc_sans_rien_de_google`) |
| le reste (`entrees`, `consignes`, `programme_de_forme`, `garde_interdits`, `hotes_permis`, `messages`, `pages_de_prix`, délais et débit) | celui du gabarit |

### 7.3 Les trois lignes de Mistral, champ par champ

| champ | `verification-mistral-eu` | `verification-mistral-global` | `file-mistral` |
|---|---|---|---|
| `numero_au_devis` | 1 | 5 | 3 |
| `go` | identifiant de sa ligne de calcul au registre (`GO_ID` l'égale) | idem | idem |
| `plafond_usd` / `plafond_registre` | `0.25` / `0,25 USD` | `0.25` / `0,25 USD` | `4.75` / `4,75 USD` |
| `exces_possible_d_un_envoi_usd` | 1.17 | 1.17 | 0.64 |
| `marques_du_perimetre` | « vérification de la clé de `mistral-large-4-0` sur `api.eu.mistral.ai` », « trois appels au plus » | « … sur `api.mistral.ai` », « trois appels au plus » | « essai d'admission du second lecteur », « 24 appels » |
| `hote` | `api.eu.mistral.ai` | `api.mistral.ai` | celui du relevé de vérification retenu |
| `dossier` | `runs/verification-cle-mistral-bras-a-v1` | idem | `runs/essais-admission-bras-a-v1` |
| `appels_max` / `appels` ; `envois_max` | 3 ; 3 | 3 ; 3 | 24 ; 48 |
| `borne_octets` ; `reserve_sortie_jetons` | 32768 ; 32832 | 32768 ; 32832 | 262144 ; 262208 |
| `delais` | 600 / 2700 / 590 / 2690 | idem | idem |
| `lectures_console` | `[]` ; une pièce par envoi coupé d'une ligne antérieure de Mistral | idem | idem |
| `levees_cle` | `[]` ; une pièce par alerte de clé (code de sortie 7) | idem | idem |
| `releve_europeen` | — | relevé scellé de la vérification européenne, signe constaté (garde 15) | — |
| `releve_verification` | — | — | relevé scellé de la vérification retenue, sain |
| `inscrit` | — | — | `nom_servi`, `hote`, `temperature_envoyee`, égaux à ceux du relevé |
| `mot_de_lazar_sonde` | — | — | `null` si sonde « comprise » et majorant « établi » ; sinon la pièce du mot (forme au gabarit) |
| `entrees` | — | — | `toutes` |

Au registre : la ligne de calcul de chaque ligne, sous la forme de la note de la livraison 4 (section 8), avec son plafond à la lettre et ses marques.

## 8. Reste ouvert

- Les décisions de Lazar sur la règle de Google (plafond et réflexion, exemption de la sonde), les limites de mots et le rapport de jetons par mot : inchangées, pour les seules lignes de Google.
- `age_max_du_fixage_heures` : valeur à décider et à inscrire.
- 7,87 € ne passent le seuil de Mistral qu'à un taux d'au moins 1,1008 (section 4).
- Avenant 2 à 65 536 : plafonds en dollars, seuils de crédit, délais de la file du juge.
- m-7, sur décision de Lazar.
- Rien n'a été joué sur un vrai fournisseur.

## 9. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v5.py`

Trois lancements, voir section 10. La suite entière du dépôt n'a pas été lancée (mandat).

## 10. Empreintes et sortie finales

Empreintes de l'état livré (la note elle-même n'est pas empreintée ici : la session la scelle) :

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v5.py` | `5208be8dc86a4e210fa34c4bb341f8eba943c4f2c79c9ceb32268a4bb239742a` |
| `tests/test_chef_essais_admission_bras_a_v5.py` | `a8b313f7981eeba2ec086f0dfc915be405a1afea3ca30d7aba358274da5aadaa` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v5-gabarit.json` | `e0a763e9e15db6860d2a6bc1b49f1e16f32fc4ab9ffbe4d14727690924e850aa` |
| `tests/mutations_essais_admission_v1/campagne_mutations_v1.py` | `2ae8d5489e3ac4b7cb0e69fee4438eeaa78cd1fe642411b72478ea025ce38c8f` |
| `tests/mutations_essais_admission_v1/greffe_mutant_v1.py` | `2df4eb2ab6a487f8a3c748274f828ccba5f9736499f5486d8826b225e01ea60e` |
| `scripts/relais_google_essais_admission_v5.py` | `ea60a3c5d694df463dd8a5a3f22a73700e239af5b7124e1f13e98b48921be0bf` |
| `scripts/relais_mistral_essais_admission_v5.py` | `cc7273cb0e3c48b9bbb9860e847a37d21fa4a008737c2c0f7bf2ce45261862a7` |
| `tests/faux_fournisseur_essais_admission_v5.py` | `fe2baf80caf8e45fba89367d6a7662e316f6f3e4be1270ca64a109cecfdf8040` |

Sortie des trois lancements de la commande d'essai : `203 passed in 95.69s`, `203 passed in 95.90s`, `203 passed in 94.08s`. Campagne de mutations sur ce même état : `total 271 ; tués 271`. Aucun relais laissé vivant ; les six fichiers `_v4` suivis sont inchangés.

## 11. Chemins ouverts, déclarés

- Lus : le mandat, les notes des livraisons 4 et 5, la vérification de la livraison 5, le devis par une recherche de lignes (« 5.6 », « 12,2 »), les fichiers `_v4` et `_v5` par `diff`, les deux outils de la campagne dans le bloc-notes de session (`…/scratchpad/mut/campagne.py`, `greffe_mutant.py`, `resultats.json`). Écrits : les fichiers `_v5` du programme, les deux fichiers de `tests/mutations_essais_admission_v1/` et cette note. Des aides temporaires (remplacements nommés, mutants, résultats) sont restées dans le bloc-notes.
- Lus par le programme pendant les essais, comme avant : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté. Aucune substitution hors de mes fichiers, nommés un à un (aucun `sed`). Les deux fichiers de m-7 ne sont pas touchés.
