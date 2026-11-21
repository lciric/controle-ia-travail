# Note de livraison 9 — programme des deux essais d'admission du bras A, version 8

- État : LIVRÉE à la session le 21 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Opus 5.5), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`). Aucun réseau, aucun `git fetch`, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ni affichée, `GO_ID` jamais fixé.
- Pièce qui fait foi pour Google : l'avenant 2 au devis, v3 (`avenant-2-devis-essais-admission-plafond-google-65536-v3.md`, sha256 `9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3`, égale à son compagnon).

## Journal
1. Lus de l'avenant 2 : les sections 0, 4 à 10 (réserve 16 comprise) et 13.1, puis 13.3. Non suivi : le renvoi de sa section 4 vers `docs/sources/` (interdit).
2. Six fichiers `_v8` copiés des `_v7` scellés, noms changés par un programme qui les nomme un à un. Par `diff`, ils ne diffèrent que par les noms. Outils de mutation en version 4 (`tests/mutations_essais_admission_v4/`). Les `_v7` et les outils version 3 ne sont pas touchés.
3. Codés dans le chef `_v8` : la pièce `avenant_2`, les valeurs de la section 9 (`controler_avenant_2`) et la garde 8 de Google.
4. Essais neufs écrits. Trois lancements : 236 passent, trois fois. Campagne de mutations : section 7.

## 1. La pièce `avenant_2` et la garde 8

**Configuration.** Le champ `avenant_2` vaut `{"chemin", "sha256"}`. Le gabarit le porte rempli, comme l'avenant 1, puisque la pièce est acceptée et scellée.

**Ce que le programme vérifie** (`controler_avenant_2`, appelé par `gardes_avant_depart` pour les seules lignes de Google) :
- une pièce inscrite est vérifiée dans tout état, à son empreinte et à son compagnon ;
- une pièce à moitié inscrite, ou qui n'est ni nulle ni une pièce, est refusée ;
- en définitive, la pièce est exigée, et son empreinte doit être `9d4b8a08…`. Une autre pièce scellée est refusée ;
- les lignes de Mistral ne la lisent pas.

**Garde 8** (`verifier_ligne_de_calcul`), pour une ligne de Google :
- en définitive, la configuration doit inscrire l'avenant 2 ;
- dès qu'elle l'inscrit, dans tout état, la ligne du registre doit citer son empreinte, au périmètre ou à la référence ;
- les lignes de Mistral n'en ont pas besoin.

Le manifeste recopie le contrôle (`avenant_2`).

## 2. Les valeurs de la section 9, champ par champ

Nulles au gabarit. Elles sont **inscrites** pour toute ligne de Google, dans tout état : sinon « avenant 2 : `…` n'est pas inscrit », rien ne part. En définitive, elles sont **à la lettre** de la section 9 ; sinon, la liste des écarts est donnée et rien ne part. Les constantes sont au chef : `AVENANT_2_FOURNISSEUR`, `AVENANT_2_LIGNES`, `AVENANT_2_BORNE_DE_REFLEXION`.

| champ | valeur exigée en définitive | gabarit |
|---|---|---|
| `fournisseurs.google.sortie_max` | `65536` | nul |
| `fournisseurs.google.reflexion` | `{"forme": "niveau", "borne_declaree": 49536}` (« la plus haute admise » se lit 49 536, admise aussi) | nul |
| `fournisseurs.google.exemption_de_la_sonde` ; `_go` | `true` (un booléen, non `1`) ; `"GO-2026-11-21-69"` | nuls |
| `fournisseurs.google.credit_min_avant_verification_usd` | `28.28` | nul |
| `fournisseurs.google.credit_min_avant_file_usd` | `23.59` | nul |
| `fournisseurs.google.credit_a_avoir_usd` | `32.97` (contrôlé, non lu par ailleurs) | nul |
| `lignes.verification-google-cle-1` et `-cle-2` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `3.0` ; `"3,00 USD"` ; `1.69` | nuls |
| `lignes.verification-google-cle-1` et `-cle-2` : `delais` | `{"silence_s": 900, "total_s": 900, "relais_silence_s": 890, "relais_total_s": 890}` | nul |
| `lignes.file-neon` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `16.5` ; `"16,50 USD"` ; `7.09` | nuls |
| `lignes.file-neon.delais` | `{"silence_s": 2700, "total_s": 2700, "relais_silence_s": 2690, "relais_total_s": 2690}` | nul |
| `regime_file_google` | `"prudent"` (déjà exigé depuis la livraison 7) | nul |
| `lignes.<Google>.reserve_sortie_jetons` | nul ou `65536` (déduit de `sortie_max`, inchangé) | nul |

Lu tel quel par le programme, sans contrôle neuf : `jetons_par_mot` et `limite_de_mots`, à inscrire par un lecteur habilité ; avec 49 536, le contrôle se lit sur 16 000 jetons.

**Chiffres refaits par programme** (`test_l9_chiffres_de_la_section_9_refaits_par_programme`) :
- excès : (200 × 890 − 65 536) × 15 / 10⁶ = 1,687, soit 1,69 ; (200 × 2 690 − 65 536) × 15 / 10⁶ = 7,087, soit 7,09 ;
- seuils : 16,50 + 3,00 + 1,69 + 7,09 = 28,28 ; 16,50 + 7,09 = 23,59 ;
- crédit à avoir : 2 × 4,69 + 23,59 = 32,97.

Le cas chiffré du point 2 de la section 9 est joué tel quel : 28,28 − 4,69 = 23,59, la file part ; somme retirée, 28,28 − 4,71 = 23,57, elle ne part pas.

**Valeurs d'essai.** Une configuration d'essai inscrit, pour les essais hérités, les chiffres de l'avenant 1 : 1,50 et 8,50 USD, excès 2,18 et 7,58, seuils 19,76 et 16,08, plafond de sortie de 32 768. L'état « essai » n'exige pas la lettre de la section 9 ; seule la définitive l'exige. C'est une lecture déclarée : sans elle, la plupart des essais hérités seraient à refaire, car leurs constats portent 23,00 USD.

### Écarts entre la section 9 et le chef v7 ou sa note (je ne choisis pas)

1. **Ligne de taux (section 7 et réserve 16).** La forme de la section 7 (« … ; heure du taux (UTC) : 2026-11-21T17:49Z », sans le fixage) est **refusée** par le chef v7 comme par le v8. Ses contrôles 2 et 4 — relire le fichier de la banque à son empreinte, et un fixage d'au plus cinq jours avant le relevé — **ne sont pas codés**. Le chef borne autrement : par `age_max_du_fixage_heures`, depuis l'heure de la pièce et depuis l'envoi (livraisons 6 et 7). La forme que lit le v8 est en section 3.
2. **`outputTokenLimit` absent** (section 6 ci-dessous) : la section 4, point 2, et la réserve 5 disent « sous 65 536 : rien ne part ». Le chef refuse une limite présente et basse, mais laisse partir un modèle dont la liste ne porte pas la limite : la ligne 2 du classement du devis ne joue pas.
3. **Borne démentie à la sonde** (13.1, point 1) : une mesure à la fiche, mais le relevé devient « nœud de Lazar ». Inchangé.
4. **`credit_a_avoir_usd`** : le programme ne le lit pas ; il le contrôle seulement, à 32,97, pour que la configuration ne dise pas faux.
5. **`exemption_de_la_sonde_go`** : la définitive exige la valeur `GO-2026-11-21-69`. L'échéance de ce GO n'est pas contrôlée (réserve 10).
6. **Empreintes que la section 8 dit ajoutées à chaque ligne** (pièce de constat, relevé du taux, fichier des règles, pages de prix, relevés documentaires, pièce « goreco ») : la garde 8 ne les exige pas. Elle n'exige que le devis, sa vérification, l'avenant 1 et, désormais, l'avenant 2.

## 3. Constat de Google seul, ligne de taux comprise, à la forme que lit le chef v8

Chemin : `docs/notes/relance-organismes-discrets-v1/constat-comptes-google-bras-a-AAAA-MM-JJ-vN.md`, avec son compagnon `.sha256`. On peut l'inscrire de deux façons :
- sous `constat`, avec la pièce de Mistral sous `constat_second` ;
- sous `constat_second`, la pièce de Mistral étant `constat`.

Les montants (31,58) et les heures sont ceux de l'exemple. Le reste est à recopier tel quel.

```
# Constat des comptes Google — bras A

## Mot de Lazar

> <le mot de Lazar, cité>

## Tableau

| clé | valeur | source | heure (UTC) |
|---|---|---|---|
| google_offre_payante_projet_a | oui | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_devise_affichee_projet_a | EUR | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_credit_vu_projet_a | 31,58 | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_recharge_automatique_projet_a | activée | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_autres_credits_admissibles_projet_a | aucun | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_credit_apres_une_recharge_projet_a | non relevé | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_partage_journaux_projet_a | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_duree_journaux_jours_projet_a | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_plafond_depense_projet_a | aucun, par GO-2026-11-21-68 | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_offre_payante_projet_b | oui | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_devise_affichee_projet_b | EUR | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_credit_vu_projet_b | 31,58 | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_recharge_automatique_projet_b | activée | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_autres_credits_admissibles_projet_b | aucun | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_credit_apres_une_recharge_projet_b | non relevé | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_partage_journaux_projet_b | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_duree_journaux_jours_projet_b | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_plafond_depense_projet_b | aucun, par GO-2026-11-21-68 | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_cle_du_projet_constate_cle_1 | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_cle_du_projet_constate_cle_2 | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_deux_projets_distincts | non relevé | capture, liste des projets | 2026-11-21T16:24Z |

- portée du constat : Google seul
- heure de la transcription (UTC) : 2026-11-21T16:30Z
- taux : 1,0990 USD par EUR ; source : Banque centrale européenne, fichier quotidien des taux de référence bce-eurofxref-daily-releve-2026-11-21T1749Z.xml, sha256 a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a ; heure du taux (UTC) : 2026-11-21T17:49Z ; fixage publié le : 2026-11-20
```

**Lu par le chef v8**, hors du dépôt (`…/scratchpad/constat-google-exemple.md`), avec `marge_de_change` à 0,05 et `age_max_du_fixage_heures` à 96 :
- crédits comptés de 32,97 USD sur chaque projet (31,58 × 1,099 × 0,95, au centime inférieur), soit le pire cas de l'avenant 2 au centime près ;
- `deux_projets_distincts` faux : la somme des deux dépenses est retirée ;
- **un envoi jusqu'au 2026-11-24T00:00Z est admis. À 00:01Z, la pièce est refusée** : le fixage du vendredi 20 a plus de 96 heures (m-a de la livraison 8).

Ce que le programme vérifie de cette ligne de taux :
- l'heure du taux (17:49Z) est au plus 6 heures après le montant le plus ancien (16:24Z) et au plus 24 heures avant le plus tardif ;
- le fixage n'est pas après l'heure du taux ;
- le début du jour du fixage est au plus `age_max_du_fixage_heures` avant l'heure de la pièce, et avant l'envoi.

Le sha256 du fichier de la banque, dans la source, est **recopié et non vérifié** par le programme (écart 1).

Règles de la pièce :
- les vingt et une clés `google_*`, toutes et elles seules ;
- les six clés levables portent exactement « non constaté, levé par GO-2026-11-21-68 », de source « levé » ;
- « au moins X » est admis sur `google_credit_vu_projet_a|b` et `google_credit_apres_une_recharge_projet_a|b`, de source « borne basse dite par Lazar » ;
- un versement demande une pièce neuve.

## 4. Lignes courtes du registre, pour Google

La forme minimale que la garde 8 accepte :
- huit cellules séparées par « ` | ` » ;
- au périmètre : les marques de la ligne (`marques_du_perimetre`) et l'empreinte du devis ;
- à la référence : l'avenant 2 par son chemin et son empreinte, puis les empreintes de la vérification du devis et de l'avenant 1. La garde n'en lit pas le libellé ;
- le plafond à la lettre ;
- `calcul` et `Lazar` ;
- la date d'accord n'est pas après le jour du lancement, et l'échéance n'est pas passée (elle vaut encore le jour même).

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY`, trois appels au plus, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc | 3,00 USD | AAAA-MM-JJ | Lazar | avenant 2 docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md 9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3 ; 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca ; 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY_2`, trois appels au plus, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc | 3,00 USD | AAAA-MM-JJ | Lazar | avenant 2 docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md 9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3 ; 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca ; 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | essai d'admission du juge des deux ancres, 8 appels, rangs impairs sous `GEMINI_API_KEY`, rangs pairs sous `GEMINI_API_KEY_2`, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc | 16,50 USD | AAAA-MM-JJ | Lazar | avenant 2 docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md 9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3 ; 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca ; 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac |
```

**Longueurs**, avec un identifiant à deux chiffres finaux (`GO-2026-11-21-81`) et des dates pleines : 551, 553 et 588 signes. C'est sous les 600 signes que l'avenant (réserve 15) prête aux consignes. Je n'ai pas pu lire cette consigne : `registres/` est interdit. Les empreintes et le chemin pèsent à eux seuls 344 signes. Un identifiant à trois chiffres finaux ajoute un signe. Ajouter des libellés aux deux dernières empreintes (« vérification du devis », « avenant 1 ») porterait la ligne du juge à 620.

**Éprouvées à blanc** (`test_l9_lignes_courtes_du_registre_eprouvees_a_blanc_de_bout_en_bout`), sans lancement, sur une configuration définitive aux valeurs de la section 9 et un constat de Google seul en euros au fixage de la banque :
- la garde 8 passe pour les trois lignes ;
- toutes les gardes d'avant le départ passent : les deux vérifications au seuil de 28,28 USD, puis la file au seuil de 23,59, au régime prudent, somme des deux dépenses retirée (32,97 − 4,71 = 28,26) ;
- **artefacts** : une marque retirée du périmètre (« ne nomme pas file-neon ») ; l'empreinte de l'avenant 2 retirée ; une configuration définitive sans l'avenant 2.

`a_blanc` ne joue pas la garde 8 (m-13) : l'épreuve passe donc par `gardes_avant_depart` avec le registre court, ce qui est plus que l'à-blanc.

## 5. Essais neufs

| essai | cas sain | artefact |
|---|---|---|
| `test_l9_chiffres_de_la_section_9_refaits_par_programme` | excès, seuils, crédit à avoir, borne, empreinte, gabarit | — |
| `test_l9_sain_une_configuration_definitive_aux_valeurs_de_la_section_9` | les trois lignes de Google ; « la plus haute admise » ; Mistral sans objet | — |
| `test_l9_artefact_une_valeur_de_la_section_9_autre_en_definitive` (onze cas) | — | sortie maximale, réflexion, GO de l'exemption, deux seuils, crédit à avoir, plafond, plafond au registre, excès, délais, régime |
| `test_l9_artefact_avenant_2_absent_d_une_autre_empreinte_sans_compagnon_ou_valeurs_nulles` | l'essai, valeurs inscrites | pièce absente ou nulle, autre empreinte, mal formée, sans compagnon, autre pièce scellée ; six valeurs nulles |
| `test_l9_garde_8_la_ligne_de_google_cite_l_avenant_2` | trois lignes courtes ; Mistral sans l'avenant 2 ; l'essai sans pièce | empreinte absente du registre ; définitive sans avenant 2 |
| `test_l9_lignes_courtes_du_registre_eprouvees_a_blanc_de_bout_en_bout` | section 4 | section 4 |
| `test_l9_seuils_de_l_avenant_2_cas_chiffre_de_la_section_9` | 28,28 − 4,69 = 23,59 | 28,28 − 4,71 = 23,57 |
| `test_l9_output_token_limit_sous_65536_aucun_appel_payant` (trois cas) | 65 536 : les appels partent, corps à 65 536 | 65 535 et 32 768 : ligne 2, close, aucun appel payant, rien de compté |
| `test_m2_l9_artefacts_ajoutes_par_la_campagne_de_la_livraison_9` | bornes admises | section 7 |

Essais hérités adaptés : deux essais de chiffres lisent maintenant le gabarit après les valeurs d'essai, et vérifient d'abord que les valeurs de Google y sont nulles. Le registre d'essai cite l'avenant 2 pour les lignes de Google.

## 6. `outputTokenLimit` à 65 536

Vérifié de bout en bout, contre le faux fournisseur, avec une sortie maximale de 65 536 et une borne de 49 536. L'appel de liste, gratuit, lit `outputTokenLimit` :
- à 65 535 ou 32 768 : ligne 2 du classement, vérification close, **aucun appel payant**, dépense nulle ;
- à 65 536 : les appels A et B partent, le corps porte `maxOutputTokens` 65 536.

Le contrôle compare à `fournisseurs.google.sortie_max`, qui vaut 65 536 en définitive : aucun 32 768 n'est écrit en dur.

**À trancher** (écart 2) : une liste **sans** `outputTokenLimit` laisse partir les appels, comme au devis. Pour refuser aussi ce cas, il faut un mot de la mère, puisque c'est une ligne neuve au classement.

## 7. Campagne de mutations, version 4

Commande : `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 .venv/bin/python -I tests/mutations_essais_admission_v4/campagne_mutations_v4.py toutes [SORTIE.json]`.

Cinq campagnes : celles de la version 3, et `livraison9`, qui mute `controler_avenant_2`, `_egal` et `verifier_ligne_de_calcul` (la garde 8 entière).

- Premier passage de `livraison9` : 98 tués sur 123. Treize survivants portaient sur des arrêts **hérités** de la garde 8 qu'aucun essai n'éprouvait : huit colonnes, type, accordé par, date d'accord illisible ou future, plafond, échéance du jour même, vérification du devis, révocation. Les autres portaient sur les bornes des valeurs inscrites, une pièce à moitié inscrite et un nombre pris pour un booléen.
- `_egal` comparait les nombres à 10⁻⁹ près : il les compare désormais exactement, puisque les valeurs sont écrites telles quelles au JSON.
- Second passage de `livraison9` : **120 tués sur 120**.
- Passage final des cinq campagnes : section 9.

## 8. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v8.py`

Trois lancements : `236 passed in 102.08s`, `236 passed in 100.85s`, `236 passed in 100.83s`. La suite entière n'a pas été lancée (mandat).

## 9. Empreintes et sorties finales

La note n'est pas empreintée ici : la session la scelle. Fichier des règles inchangé (`4e99bade…`).

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v8.py` | `8cbb6e0519b6b3307a998f03517c8a6544b0d66f22aafb8bd4408106b6f9fd0f` |
| `scripts/relais_google_essais_admission_v8.py` | `79933d52b4917de681fe84fc1c1315e89c9a8be935a909cf389d18fdca243d0a` |
| `scripts/relais_mistral_essais_admission_v8.py` | `f5c2d9b1610837243b1871d614d53d9e852dc3e879e81d8905c1be6c51c9b8cc` |
| `tests/faux_fournisseur_essais_admission_v8.py` | `adf5b338b0f57f9289bf8025424acd8f128bca7f20ea2f4d4f49fa5ae7ac0c81` |
| `tests/test_chef_essais_admission_bras_a_v8.py` | `bc2e797339960d7e269a67e6a76cd8ba7a4db4731d1ce6c12cdbcdc3e16c012d` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v8-gabarit.json` | `5e7f61df76035d05876181a40aa7d05c6ebdb7be2ecda6b08f2067b5ce78009a` |
| `tests/mutations_essais_admission_v4/campagne_mutations_v4.py` | `86b8f9f58f2b816818511d36d011c04af91684d7d8fc45a5e209e508df30a07e` |
| `tests/mutations_essais_admission_v4/greffe_mutant_v4.py` | `af932ed4d8e1f85356af88938e539a75fe16c07ea62ca5e2f491178fafb2d1eb` |

- Commande d'essai, trois fois : `236 passed` (section 8).
- Campagne de mutations version 4, cinq campagnes, sur ce même état, code de sortie 0 : règle Google 108, livraison 6 168, livraison 7 77, livraison 8 48, livraison 9 120, soit **521 mutants, 521 tués, 0 erreur**.
- Aucun relais laissé vivant ; les `_v7` et les outils version 3 sont inchangés (`git status` ne montre que les fichiers neufs).

## 10. Chemins ouverts, déclarés

- **Lus** : l'avenant 2 v3, aux sections nommées ; les `_v7` et `_v8` (par `diff` et par recherche de lignes) ; les outils de mutation version 3.
- **Écrits** : les six `_v8`, les deux outils version 4 et cette note.
- **Hors du dépôt**, dans le bloc-notes : l'exemple de constat de Google seul et la sortie de la campagne.
- Aucun chemin interdit ouvert, listé ni empreinté : `docs/sources/`, que cite l'avenant, n'a pas été suivi ; `registres/` non plus, d'où la limite de 600 signes non vérifiée. Aucun `sed`, aucune substitution hors de mes fichiers, nommés un à un.
