# Note de livraison 11 — programme des deux essais d'admission du bras A, version 10

- État : LIVRÉE à la session le 22 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Opus 5.5), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`). Aucun réseau, aucun `git fetch`, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ni affichée, `GO_ID` jamais fixé.
- Deux mots de Lazar, lus sur la branche principale par la commande que la session a donnée (`git show origin/main:registres/go.md | grep -E "GO-2026-11-22-0[23]"`), et par elle seule :
  - **GO-2026-11-22-02**, de type `décision`, échéance 2026-11-30 : « aucun versement de 9,18 € par projet Google à faire ; la recharge automatique des deux projets couvre les lignes » ; à sa référence, « un refus pour crédit épuisé est un défaut journalisé, jamais une réponse ».
  - **GO-2026-11-22-03**, de type `décision`, échéance 2026-11-30 : « exemption de la sonde de borne de Google … Confirme et remplace GO-2026-11-21-88 ».

## Journal
1. Six fichiers `_v10` copiés des `_v9` scellés, noms changés par un programme qui les nomme un à un ; par `diff`, seuls les noms diffèrent. Outils de mutation en version 6 (`tests/mutations_essais_admission_v6/`). Les `_v9` et les outils version 5 ne sont pas touchés.
2. Codés dans le chef `_v10` :
   - le champ fermé `seuils_de_credit_google` et sa levée lue au registre ;
   - la lecture des lignes de décision du registre, mise en commun avec l'exemption de la sonde (`ligne_de_decision`) ;
   - le refus pour crédit épuisé (`refus_pour_credit`), à la vérification, à la sonde et dans la file.
3. Deux simplifications, trouvées par la campagne (section 5) :
   - le lien entre clé et projet se lit sur les seules valeurs ;
   - le filtre du refus pour crédit tient en une seule condition.

   Elles ne changent aucun comportement.
4. Trois lancements : 247 essais passent, trois fois. Campagne : section 7.

## 1. Les seuils de crédit de Google : exigés ou levés

**Le champ fermé `seuils_de_credit_google`** (au premier niveau de la configuration) :
- au gabarit : `null` ;
- toute ligne de Google refuse un champ nul, absent ou d'une autre forme : « `seuils_de_credit_google` n'est pas inscrit », rien ne part ;
- les lignes de Mistral ne le lisent pas.

Il prend deux valeurs :
- **`"exiges"`** : le comportement d'avant. Avant chaque vérification, chaque projet doit montrer 28,28 USD, crédit compté moins dépense retirée ; avant la file, 23,59 USD ; de même à la lecture de la console (garde 20) et au mot sur les sondes (garde 10). Sous ces seuils, la ligne ne part pas.
- **`{"leves_par": "<GO>"}`** : les seuils **ne refusent plus**. Le crédit vu reste lu, converti, compté et comparé, et c'est écrit :
  - au contrôle du crédit, recopié au manifeste, au relevé et au rapport : `seuils` (« levés par GO-… ») et, par projet, `sous_le_seuil` (« sous le seuil (12.45 USD pour 28.28), levé par GO-2026-11-22-02 », ou nul au-dessus) ;
  - à la lecture de la console : `sous_le_seuil` de chaque pièce servie ;
  - au mot sur les sondes : `credits_sous_le_seuil` du contexte de la file.

**Le GO de la levée.** En configuration définitive, il est lu au registre de la branche principale (`controler_levee_des_seuils`, par `ligne_de_decision`). Il doit remplir toutes ces conditions :
- une seule ligne, de huit cellules, de type `décision` ;
- accordée par Lazar ;
- non échue au jour de l'envoi (elle vaut encore le jour même) ;
- non révoquée ;
- elle cite « recharge automatique », au périmètre ou à la référence. La ligne de GO-2026-11-22-02 le cite.

Sinon rien ne part, avant tout envoi. À l'essai, seule la forme est contrôlée. À blanc, le registre n'est pas lu : seule la forme est rendue, comme pour la garde 8.

**Rien d'autre ne change** : plafonds de 3,00 et 16,50 USD, compteur au régime prudent, pire cas de 32,97 USD, `recharge_comptee` à faux, valeurs de la section 9 de l'avenant 2 exigées à la lettre (seuils de 28,28 et 23,59 compris : ils sont inscrits et lus, seulement non refusants).

**Aux soldes du 21 novembre** (11,93 € et 15,59 €, au fixage de 1,0990 diminué de 5 %) : 12,45 et 16,27 USD comptés. Sous « exiges », rien ne part. Sous la levée par GO-2026-11-22-02, les vérifications partent et l'écrivent.

| essai | cas sain | artefact |
|---|---|---|
| `test_l11_sain_seuils_leves_sous_go_02_la_verification_part_et_l_ecrit` | levée sous GO-02, soldes du 21 novembre : les deux vérifications passent toutes leurs gardes, « levé par GO-2026-11-22-02 » écrit par projet ; au-dessus du seuil, rien d'écrit ; la lecture de la console sous le seuil, écrite | — |
| `test_l11_artefact_exiges_refuse_sous_le_seuil` | — | « exiges » : la vérification et la lecture de la console refusent sous le seuil |
| `test_l11_artefact_levee_refusee_go_echu_sans_la_mention_ou_d_une_autre_forme` | le jour de l'échéance : admis ; Mistral sans objet ; l'essai, la forme seule ; gabarit nul | échu ; sans « recharge automatique » ; type `calcul` ; absent ; ligne entière refusée ; six formes du champ refusées |

## 2. Refus pour crédit ou quota épuisé

**Ce qui existait** :
- dans la file, un 402 arrêtait la ligne sans reprise ;
- un 429 y était attendu puis repris une fois, quel que soit son motif ;
- à la vérification, 402 tombait à la ligne 7 et 429 à la ligne 6, toutes deux « à refaire sous la même ligne », par un lancement nouveau.

Un refus pour crédit épuisé n'était donc ni toujours un arrêt, ni jamais distingué.

**Ce qui est codé** (`refus_pour_credit`). Est un refus pour crédit ou quota épuisé un refus **du fournisseur** (non écrit par le relais ni par le mandataire) :
- de code **402** ;
- ou de code **400, 403 ou 429** dont le corps d'erreur, en minuscules, contient l'un des mots `quota`, `billing`, `credit`, `crédit`, `balance`, `insufficient`, `prepay`, `payment`, `exhausted`, `solde`.

Lecture prudente : chez Google, un 429 `RESOURCE_EXHAUSTED` y entre, qu'il soit de quota ou de débit. Un 429 sans aucun de ces mots, comme le débit de Mistral (« Requests rate limit exceeded »), garde son classement d'avant.

**Le classement exact.** Motif (`MOTIF_CREDIT_EPUISE`) :

> refus pour crédit ou quota épuisé (code N, « mot ») : défaut journalisé, jamais une réponse ; la ligne s'arrête, sans reprise ni appel de plus ; nœud de Lazar (GO-2026-11-22-02)

- **Vérification, appels A et A′** : **ligne 13** du classement, avant les lignes 6 et 7. Ligne close, non saine, nœud de Lazar, `a_refaire` nul : aucun lancement nouveau sous la même ligne.
- **Sonde (appel B)** : ligne 13 de même, ligne close, jamais « à refaire ».
- **File** : décision `arret`, avant l'attente sur un 429 et avant toute reprise. La fiche porte `refus_pour_credit`. L'envoi est compté au compteur selon la règle inchangée d'un code d'erreur. Il n'est jamais jugé ni compté parmi les réponses de code 200.
- 401 et 403 sans mot du crédit restent à la ligne 7.

**Écart déclaré au devis (4.4, ligne 7)** : un 402 y était « cause à corriger (compte non approvisionné) ; à refaire ». Le mot de Lazar GO-2026-11-22-02 en fait un défaut journalisé qui arrête la ligne : l'essai hérité est adapté (402 à la ligne 13, 401 à la ligne 7).

| essai | cas sain | artefact |
|---|---|---|
| `test_l11_artefact_refus_pour_credit_epuise_arrete_la_verification` | — | 429 de quota, 402, 403 « prepayment credits are depleted » : un seul appel, ligne 13, close, nœud, jamais à refaire ; à la sonde, de même |
| `test_l11_sain_un_429_sans_mot_du_credit_garde_son_classement` | 429 de débit de Mistral : ligne 6, à refaire ; codes 200 et 500, 429 sans mot : rien | — |
| `test_l11_refus_pour_credit_epuise_arrete_la_file_sans_attente_ni_reprise` | 429 sans mot : attente, reprise, file complète | 429 de quota au premier appel : un seul appel, arrêt, aucune attente, aucune réponse de code 200, file incomplète |

## 3. Configuration définitive de Google, à jour, sous GO-2026-11-22-03 et GO-2026-11-22-02

À tirer du gabarit `_v10` sous un nom neuf, scellée. Les empreintes `""` sont à remplir par la session.

**Premier niveau** (champs à changer par rapport au gabarit) :

```json
{
 "version": "configuration-essais-admission-bras-a-v10-google-AAAA-MM-JJ-v1",
 "etat": "definitive",
 "marge_de_change": 0.05,
 "marge_de_change_go": "GO-2026-11-21-68",
 "age_max_du_fixage_heures": 96,
 "recharge_comptee": false,
 "regime_file_google": "prudent",
 "seuils_de_credit_google": {"leves_par": "GO-2026-11-22-02"},
 "temperature_retiree_d_avance": false,
 "constat": {"chemin": "docs/notes/relance-organismes-discrets-v1/constat-comptes-google-bras-a-AAAA-MM-JJ-vN.md", "sha256": ""},
 "constat_second": {"chemin": null, "sha256": null},
 "regles": {"chemin": "<fichier des règles scellé, non gabarit>", "sha256": "", "lignes_du_texte": [521, 529],
            "gabarit": "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md"},
 "essai_local": null
}
```

`avenant_2` (`9d4b8a08…`), `devis`, `verification_du_devis` et `avenant` sont au gabarit : on les garde.

**`fournisseurs.google`** (champs à changer) :

```json
{
 "sortie_max": 65536,
 "reflexion": {"forme": "niveau", "borne_declaree": 49536},
 "exemption_de_la_sonde": true,
 "exemption_de_la_sonde_go": "GO-2026-11-22-03",
 "jetons_par_mot": "<à inscrire par le lecteur habilité>",
 "credit_min_avant_verification_usd": 28.28,
 "credit_min_avant_file_usd": 23.59,
 "credit_a_avoir_usd": 32.97
}
```

`GO-2026-11-22-03` passe la garde de l'exemption (livraison 10) : ligne de `décision`, de Lazar, échéance 2026-11-30, qui cite « exemption de la sonde ». Les limites de mots des deux consignes sont à inscrire par le lecteur habilité, avec limite × jetons par mot ≤ 16 000.

**Les trois lignes de Google, sous `lignes`** : comme à la note de la livraison 10, section 3, sans changement :
- les plafonds de 3,00, 3,00 et 16,50 USD, et `plafond_registre` à la lettre ;
- les excès de 1,69 et 7,09 ;
- les délais de 900/890 et 2 700/2 690 ;
- les relevés et l'`inscrit` de la file.

**Au registre** :
- les trois lignes courtes de Google (note de la livraison 9, section 4) ;
- GO-2026-11-22-03 (exemption) et GO-2026-11-22-02 (levée des seuils), déjà sur la branche principale.

Ces deux lignes de décision ne servent que jusqu'au 30 novembre inclus.

## 4. Constat de Google seul : deux projets, deux clés, recharge activée

Chemin : `docs/notes/relance-organismes-discrets-v1/constat-comptes-google-bras-a-AAAA-MM-JJ-vN.md`, avec son compagnon `.sha256`. Les montants et les heures sont ceux du 21 novembre ; le reste est à recopier tel quel.

```
# Constat des comptes Google — bras A

## Mot de Lazar

> <le mot de Lazar, cité>

## Tableau

| clé | valeur | source | heure (UTC) |
|---|---|---|---|
| google_offre_payante_projet_a | oui | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_devise_affichee_projet_a | EUR | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_credit_vu_projet_a | 11,93 | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_recharge_automatique_projet_a | activée | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_autres_credits_admissibles_projet_a | aucun | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_credit_apres_une_recharge_projet_a | non relevé | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_partage_journaux_projet_a | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_duree_journaux_jours_projet_a | non constaté, levé par GO-2026-11-21-68 | levé | 2026-11-21T16:24Z |
| google_plafond_depense_projet_a | aucun, par GO-2026-11-21-68 | capture, facturation du projet a | 2026-11-21T16:24Z |
| google_offre_payante_projet_b | oui | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_devise_affichee_projet_b | EUR | capture, facturation du projet b | 2026-11-21T16:24Z |
| google_credit_vu_projet_b | 15,59 | capture, facturation du projet b | 2026-11-21T16:24Z |
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

Ce que lit le chef v10 :
- les vingt et une clés `google_*`, toutes et elles seules, et la portée « Google seul » ;
- la recharge automatique « activée » est admise et n'est **pas comptée** (`recharge_comptee` à faux) ; « non relevé » au crédit après une recharge ;
- six clés levées sous GO-2026-11-21-68, dont les deux clés du lien : la somme des deux dépenses est donc retirée ;
- crédits comptés de 12,45 et 16,27 USD : sous les seuils, écrits « levé par GO-2026-11-22-02 » sous la levée.

**Âge** : avec `age_max_du_fixage_heures` à 96, cette pièce ne sert plus aucune ligne après le 2026-11-24 à 00:00Z (fixage du vendredi 20, borne comptée depuis l'envoi, livraison 8). Passé ce jour, il faut un taux frais, donc une pièce neuve.

## 5. Campagne de mutations, version 6

Commande : `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 .venv/bin/python -I tests/mutations_essais_admission_v6/campagne_mutations_v6.py toutes [SORTIE.json]`.

Sept campagnes : celles de la version 5, et `livraison11`, qui mute `seuils_de_credit_google`, `controler_levee_des_seuils`, `ligne_de_decision`, `refus_pour_credit` et `controler_credit_de_google`.

Premier passage de `livraison11` : 63 tués sur 68.
- Deux survivants étaient **équivalents**, c'est-à-dire qu'aucun essai ne pouvait les distinguer du code :
  - « non levé et tout à oui » : une clé du lien non levée ne peut valoir que « oui » ;
  - un booléen ou un code nul pris pour un code de crédit.

  Le code est simplifié pour les ôter, sans changer de comportement.
- Les trois autres sont tués par `test_m2_l11_artefacts_ajoutes_par_la_campagne_de_la_livraison_11` :
  - un refus écrit par le relais ;
  - le seuil pile ;
  - la règle quand les deux projets sont « non relevé » et le lien levé.

Second passage : **66 tués sur 66**. Passage final : section 7.

## 6. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v10.py`

Trois lancements avant la campagne : `247 passed` (104,85, 103,63 et 103,44 s) ; trois sur l'état livré, section 7. La suite entière n'a pas été lancée (mandat).

## 7. Empreintes et sorties finales

La note n'est pas empreintée ici : la session la scelle. Fichier des règles inchangé (`4e99bade…`).

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v10.py` | `52c39b55b3cf007207d4c3d3ad26aab1255ffd29ce22215873a846bf33b9109d` |
| `scripts/relais_google_essais_admission_v10.py` | `c88fae29fe09f69e8959b1e1b88505ee95d5e9ca8b7d542eac85e43d29aa5411` |
| `scripts/relais_mistral_essais_admission_v10.py` | `016f7428c4da0cae6556fcdddf1548066de5c9d51ba007fdc6fa665fcd9ccead` |
| `tests/faux_fournisseur_essais_admission_v10.py` | `2e3ce905dcfd440d8da8ffbe096caa0dbb6423bfb3b15e21c2b37ee83feda146` |
| `tests/test_chef_essais_admission_bras_a_v10.py` | `39270559d182d57adc20cb3e1eb39e96091bc84171de02a045c2f7e6282af377` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v10-gabarit.json` | `d44ed9b4e4cefb9c299d5221a7e758c8a24bf06d8d4403af768e7448c5495caf` |
| `tests/mutations_essais_admission_v6/campagne_mutations_v6.py` | `5690fa7583caf7b29fd4c6ff474b902e943f140dc369489d08b5bc7bdd5ff8a3` |
| `tests/mutations_essais_admission_v6/greffe_mutant_v6.py` | `39f8a5b48b977bbc2bed816d75fdc6668e8bb6a69cb645f54caf41352b79f91d` |

- Campagne entière, version 6, sept campagnes : **615 tués sur 616**. Le survivant est dans la garde 10 : sous la levée, un crédit vu au seuil pile, au mot sur les sondes, écrit à tort par le mutant `<=`. Il est tué par un essai ajouté (`test_m2_l11_mot_sur_les_sondes_sous_une_levee_pile_et_sous_le_seuil` : pile, rien d'écrit ; sous le seuil, écrit ; sous « exiges », refusé). La campagne `livraison7`, rejouée ensuite : **80 tués sur 80**.
- Trois lancements sur l'état livré, après cet essai : `248 passed in 104.37s`, `248 passed in 105.18s`, `248 passed in 105.49s`.
- Aucun relais laissé vivant ; les `_v9` et les outils version 5 sont inchangés. Le fichier non suivi `journal-depense-relecture-fable-api-avenant-3-v1.jsonl` n'est pas de moi ; je ne l'ai ni ouvert ni touché.

## 8. Reste ouvert

- Les deux lignes de décision échoient le 30 novembre ; la pièce de constat du 21, le 24 à 00:00Z, sous une borne de 96 heures.
- `jetons_par_mot` et les limites de mots, par le lecteur habilité.
- Rien n'a été joué sur un vrai fournisseur. Ce que rend Google à crédit épuisé n'est pas relevé : la liste de mots est une lecture prudente, à revoir au premier refus réel.

## 9. Chemins ouverts, déclarés

- **Lus** : les deux lignes GO-2026-11-22-02 et -03 du registre, par la commande donnée par la session, et rien d'autre du registre ; les `_v9` et `_v10` (par `diff` et par recherche de lignes) ; les outils de mutation version 5.
- **Écrits** : les six `_v10`, les deux outils version 6 et cette note.
- Aucun chemin interdit ouvert, listé ni empreinté. Aucun `sed`, aucune substitution hors de mes fichiers, nommés un à un.
