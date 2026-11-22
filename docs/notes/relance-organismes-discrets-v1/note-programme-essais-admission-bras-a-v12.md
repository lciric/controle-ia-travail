# Note de livraison 13 — programme des deux essais d'admission du bras A, version 12

- État : livrée à la session le 22 novembre 2026. Fichiers scellés par l'agent (empreinte compagnon `.sha256`), rien committé, rien poussé : la session committe.
- Auteur : agent du code de la livraison 13 (Claude Opus 5.5), sous la consigne de la session (journal OD-354). Processeur seulement : aucun réseau vers un fournisseur, aucun `git fetch`, aucune clé lue ni affichée, `GO_ID` jamais fixé, aucune dépense.
- Objet : les corrections de la vérification de la livraison 12 (`verification-programme-essais-admission-livraison12-v1.md`, « engageable après corrections ») : le constat 1 (majeur) et les constats 2 à 7 (mineurs).
- Base : les `_v11` scellés, sceaux vérifiés avant et après (section 8). Copiés sous des noms `_v12` par `sed` sur les seuls fichiers neufs ; les `_v11` et les outils v7 ne sont pas touchés.
- Registre : les seules lignes GO-2026-11-22-02, -03 et -16, par `git show origin/main:registres/go.md | grep -E "GO-2026-11-22-(02|03|16) "`.

## 1. Constat 1 (majeur) — l'attente due après un 429 de Google, à la vérification de la clé

### 1.1 Écrite

À une vérification de Google, sur un 429 **du fournisseur** (ni écrit par le relais, ni refus du mandataire), la fiche de l'appel porte trois champs neufs (`attente_due_a_la_verification`) :
- `attente_due_s` : la règle de la file (`attente_sur_429`, inchangée) : `Retry-After` s'il est lisible, sinon le `retryDelay` de Google s'il passe le défaut de 30 s, sinon 30 s ; puis **bornée à 600 s**, quelle que soit la valeur `attente_429.max_s` de la configuration (constante `ATTENTE_DUE_MAX_S`) ;
- `retry_delay_lu_s` : le délai lu dans le corps, ou nul ;
- `pas_avant` : l'heure de réception (relevée dès le retour du relais) plus l'attente, à la seconde supérieure, au format `AAAA-MM-JJTHH:MM:SSZ`.

Le `retryDelay` est lu sur **le corps entier** reçu (`retour["corps"]`), non sur le corps d'erreur écrit, toujours borné à 500 octets. Au 429 de débit du faux fournisseur (841 octets, délai à l'octet 819), l'attente due est bien de 45 s pour « 45s ».

La fiche est écrite au relevé et à l'événement « envoi » du journal (lu pour un dossier sans relevé, C-1). Le relevé porte en tête `attente_due_s` et `pas_avant` du 429 le plus tardif de la ligne ; le relevé réduit (garde 18) les garde aussi, avec `origine`.

### 1.2 Gardée

`garde_attente_due`, appelée par `gardes_avant_depart` après le contrôle « ligne close » (donc deux fois par `executer`, la seconde sous le verrou, et par `a-blanc`) :
- tout 429 de Google du fournisseur, compté parmi les trois, au relevé ou au journal de la ligne, doit porter une heure `pas_avant` lisible ; sinon : « … le relevé ne porte pas son heure « pas_avant » lisible : l'attente due n'est pas connue ; rien ne part ; nœud de Lazar » ;
- avant l'heure la plus tardive : « ARRÊT avant tout envoi : attendre jusqu'à AAAA-MM-JJTHH:MM:SSZ : l'appel … a reçu un 429 de Google, qui demande N s d'attente avant tout lancement nouveau de la ligne ; rien ne part » (code 2, aucun dossier créé, aucun relais lancé) ;
- à l'heure pile ou après : la ligne part ; le manifeste et la sortie à blanc écrivent `attente_due`.

Ne comptent pas : un 429 écrit par le relais, un appel non compté, un autre code, Mistral.

### 1.3 Essais (R5)

| essai | cas sain | artefact |
|---|---|---|
| `test_l13_sain_l_attente_due_est_ecrite_au_releve_lue_sur_le_corps_entier` | 45 s lus sur le corps entier (le corps écrit ne porte pas le délai) ; `pas_avant` encadré ; au relevé et au journal ; à l'heure pile : admis ; gardes passées une seconde après ; relance : saine ; 23 s → 30 ; forme courte → 30 ; `Retry-After: 90` prime → 90 ; 503 et Mistral : aucune attente due | — |
| `test_l13_bout_en_bout_relance_avant_l_heure_refusee_apres_l_heure_part` | par `executer` : 429 (code 3) ; après l'heure : code 0, saine, deux lancements, manifeste | relance aussitôt et une seconde avant l'heure : code 2, « attendre jusqu'à … », aucun appel ni dossier de plus ; `a-blanc` refuse de même, puis dit l'heure |
| `test_l13_artefacts_releve_sans_l_heure_et_delai_borne_a_600` | le plus tardif prime ; relais, non compté, 503, Mistral : ignorés ; 599 s : 599 ; arrondi à la seconde supérieure | relevé sans l'heure (nulle, « demain », sans `T`, nombre) : refusé, unité et par les gardes d'avant le départ ; avec l'heure, avant : refusé ; `retryDelay` 900 s → 600 (règle 600 ou 1 200), `Retry-After: 3600` sous une règle de 7 200 → 600 ; par le banc, sous une règle de 1 200 : 600 |

## 2. Les mineurs

| constat | traité comment | essai |
|---|---|---|
| 2. GO-16 cité, jamais lu | **corrigé** : `controler_go_de_l_avenant_3`, appelée par `gardes_avant_depart` (hors à blanc), pour toute ligne de Google en configuration définitive : la ligne de GO-2026-11-22-16 lue par `ligne_de_decision` (une seule, huit cellules, `décision`, Lazar, non échue, non révoquée, qui cite « seuils levés »), et qui cite `4b331d9a`. Écrite au manifeste. La recherche de la garde 8 est bornée à gauche aussi (`(?<![\w-])`). La vraie ligne, telle que lue par la commande du registre, remplit ces conditions (essai : sa forme, à l'échéance du 30, admise le 30, refusée le 1er décembre) | `test_l13_go_16_lu_au_registre_comme_go_02` : sain, Mistral, essai ; absente, registre non lu, deux lignes, échue, `calcul`, autre que Lazar, sans « seuils levés », sans `4b331d9a`, révoquée ; la ligne entière refusée sans elle ; « AGO-… », « X-GO-… », « …-160 », « _GO-… » refusés ; « (GO-…) », « GO-…. », « «GO-…» » admis |
| 3. épreuve de la garde 8 sur la section 4 de l'avenant 3 | **versée** : les trois textes lus dans le fichier de l'avenant 3 (empreinte vérifiée), tels quels, au périmètre ; référence « avenant 2 `9d4b8a08…` ; avenant 3 `4b331d9a…` ; GO-2026-11-22-16 » ; configuration définitive : admis (3 046, 3 048 et 2 973 signes), et GO-16 lu. Refusés sans GO-16, sans l'avenant 3, sans l'avenant 2, une marque ôtée. **À trancher par la session** : la forme qui ira au registre (lignes courtes de la note v11 ou textes de l'avenant 3) ; la garde 8 admet les deux | `test_l13_garde_8_lit_les_trois_textes_de_la_section_4_de_l_avenant_3` |
| 4. motif du second 429 après une panne | **règle choisie** : dans la file de Google, un 429 au second envoi d'un appel arrête la file (inchangé, aucun troisième envoi). Le motif `MOTIF_SECOND_429` (« crédit épuisé possible ; nœud de Lazar ») ne vaut que si le premier envoi a reçu un 429 ; après toute autre cause du premier envoi (5xx, délai, coupure, refus du mandataire), le motif est `MOTIF_429_APRES_UNE_PANNE` : « seconde panne sur le même appel : code 429 au second envoi, après « cause » au premier ; la file s'arrête, sans troisième envoi ». Cause non dite (appel direct) : le motif prudent, celui du second 429. Mistral : inchangé | `test_l13_file_un_429_apres_une_panne_n_est_pas_le_second_429` |
| 5. règle propre à Google | **dite ici** : la règle d'OD-351 (attente, second 429 qui arrête, 402 qui arrête) et l'attente due de la section 1 sont **codées chez Google seulement**, sous GO-2026-11-22-02, qui ne vise que Google. Mistral reste au devis : 402 aux lignes 7 ou 8, 429 à la ligne 6 sans arrêt au second, aucune attente due écrite ni gardée à la vérification. **Une ligne de la session au journal** reste à écrire pour dire que c'est sa règle | — |
| 6. cinq non équivalents | **tués** (section 3) : les quatre arrondis d'écriture et les clés levées au relevé ; l'équivalent « en pratique » (`cle_vue_dans_une_reponse` sans journal de relais) aussi | `test_l13_mutants_non_equivalents_de_la_livraison_12_tues` |
| 7. délai compté tué | **corrigé** : campagne v8, issue « délai » comptée à part (`compter_issues`), jamais tuée ; code 0 seulement si tous sont tués | `test_l13_la_campagne_compte_a_part_un_mutant_arrive_au_delai` |

## 3. Campagne de mutations, version 8

Commande, depuis la racine, par campagne :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT .venv/bin/python -I tests/mutations_essais_admission_v8/campagne_mutations_v8.py CAMPAGNE SORTIE.json`

Onze campagnes : les neuf de la version 7, sur les `_v12`, sans autre changement, et deux neuves, jouées seules :
- `livraison13` : `attente_due_a_la_verification`, `garde_attente_due`, `controler_go_de_l_avenant_3`, `verifier_ligne_de_calcul`, `decider_dans_la_file`, `a_blanc` ; sous-ensemble « l13 or l12 or l11 or l9 or garde_8 or garde_4 or m2_ or m13 or bout_en_bout or definitive » ;
- `livraison13_jouer` : `jouer_verification` et `jouer_file` (en campagne pour la première fois), sur toute la suite.

`gardes_avant_depart` et `executer` ne sont pas en campagne : les lignes ajoutées n'y portent aucune opération que l'outil mute (appels et entrées de dictionnaire) ; leur effet est éprouvé par les essais de bout en bout de la section 1.

**`livraison13`** :
- Passage 1 (11:26 à 11:33Z) : 168 mutants, 166 tués, 2 survivants. L'un, `replace(microsecond=0)` mué en `1`, était équivalent : le code est réécrit (`math.ceil` sur l'instant), au même comportement, d'où 166 mutants ensuite. L'autre (`borne_octets` dans la file de Google, retour → None) est tué par une ligne ajoutée à l'essai du constat 4.
- Passage 2, sortie exacte :

```
livraison13 attente_due_a_la_verification 8 mutants ; 8 tués ; 0 survivants ; 0 au délai ; 0 erreurs
livraison13 garde_attente_due 14 mutants ; 14 tués ; 0 survivants ; 0 au délai ; 0 erreurs
livraison13 controler_go_de_l_avenant_3 9 mutants ; 9 tués ; 0 survivants ; 0 au délai ; 0 erreurs
livraison13 verifier_ligne_de_calcul 75 mutants ; 75 tués ; 0 survivants ; 0 au délai ; 0 erreurs
livraison13 decider_dans_la_file 55 mutants ; 55 tués ; 0 survivants ; 0 au délai ; 0 erreurs
livraison13 a_blanc 5 mutants ; 5 tués ; 0 survivants ; 0 au délai ; 0 erreurs
total 166 ; tués 166 ; au délai 0 ; résultats : …/scratchpad/v13/mut-livraison13-2.json
code 0
```

**`livraison13_jouer`** (11:41 à 12:18Z), sortie exacte :

```
livraison13_jouer jouer_verification 162 mutants ; 159 tués ; 3 survivants ; 0 au délai ; 0 erreurs
livraison13_jouer jouer_file 39 mutants ; 30 tués ; 9 survivants ; 0 au délai ; 0 erreurs
   jouer_verification | livraison13_jouer : l3070 et↔ou | survit
   jouer_verification | livraison13_jouer : l3088 comparaison Eq→NotEq | survit
   jouer_verification | livraison13_jouer : l3088 constante 1→2 | survit
   jouer_file | livraison13_jouer : l3372 comparaison Eq→NotEq | survit
   jouer_file | livraison13_jouer : l3483 constante 6→7 | survit
   jouer_file | livraison13_jouer : l3448 comparaison Gt→GtE | survit
   jouer_file | livraison13_jouer : l3464 comparaison Eq→NotEq | survit
   jouer_file | livraison13_jouer : l3376 et↔ou | survit
   jouer_file | livraison13_jouer : l3416 constante 6→7 | survit
   jouer_file | livraison13_jouer : l3416 constante 6→7 | survit
   jouer_file | livraison13_jouer : l3420 constante 6→7 | survit
   jouer_file | livraison13_jouer : l3445 constante 6→7 | survit
total 201 ; tués 189 ; au délai 0 ; résultats : …/scratchpad/v13/mut-livraison13_jouer-2.json
code 1
```

Les arrondis de `jouer_verification`, les clés levées et `else 0` (constat 6) n'y survivent plus. Les neuf survivants de `jouer_file` sont tués par `test_l13_m2_jouer_file_mutants_de_la_campagne_de_la_livraison_13` (règle de Google avant l'envoi, journaux de relais absents, arrondis sous des prix à sept décimales, majorant à 64 jetons pile, « interrompue » faux sur un arrêt). Rejeu des douze survivants, un à un, sur toute la suite, par `…/scratchpad/v13/rejeu_survivants.py` : `rejoués 12 ; tués 9`.

**Trois survivants déclarés, équivalents** (ceux que la vérification 12 jugeait déjà « équivalents vrais ») :
- l. 3070, `type in (A, A′) and ligne == 3` mué en `or` : aucune sonde ne porte la ligne 3, et aucun appel A ou A′ ne suit un A ou A′ sain ; le dernier élément de la liste est le même ;
- l. 3088, `None if genre == "B" else 1`, `==` en `!=` et `1` en `2` : la sonde sort de `garde_google_avant_envoi` avant ce contrôle ; pour A et A′, la garde exige déjà un plafond au moins égal à la borne plus 16 000.

Le quatrième équivalent vrai de la vérification 12 (`classer_issue`, `!= 200` en `!= 201`) tient à une fonction inchangée, dans la campagne `livraison12`, non rejouée.

**Comptes de la livraison 13** : 367 mutants (166 + 201) ; 364 tués ; 3 déclarés équivalents ; 0 au délai ; 0 erreur. **Réserve** : les neuf de `jouer_file` sont tués par rejeu un à un, non par une campagne rejouée d'un tenant ; les neuf campagnes de la version 7 ne sont pas rejouées sur les `_v12` (leurs fonctions, hors `decider_dans_la_file` et `verifier_ligne_de_calcul`, ici rejouées, n'ont pas changé).

## 4. Écarts déclarés

Au devis :
1. **4.4, ligne 6, et 5.6, à la vérification de Google** : le devis ne met aucune attente entre deux lancements d'une vérification ; ici, un lancement nouveau avant `pas_avant` est refusé. Plus prudent : moins d'envois, aucune dépense de plus. Il retarde la ligne de 600 s au plus.
2. **5.6, borne de 600 s** : tenue en dur à la vérification, même si `attente_429.max_s` en dit plus (la file garde la configuration, inchangée).
3. Hérités de la livraison 12, inchangés : `retryDelay` lu ; 402, 400 ou 403 qui dit le crédit, qui arrête ; second 429 qui arrête la vérification.

À la livraison 12 :
4. Dans la file de Google, le motif d'un 429 après une panne (section 2) ; la décision, l'arrêt, ne change pas.
5. En définitive, GO-16 lu au registre : une ligne de Google ne part plus si la ligne de GO-16 est échue, révoquée ou absente.

À la consigne : la campagne n'est pas `toutes` (consigne : « pas forcément ») ; relais renommés seulement (noms et versions).

## 5. Configuration définitive : ce qui change d'avec la note v11

- Tirée du gabarit `_v12` ; les empreintes des relais `_v12` y sont : Google `5503eba1…`, Mistral `e11926ec…`.
- Au registre, inchangé : GO-2026-11-22-02, -03 et -16 sur la branche principale, valables jusqu'au 30 novembre inclus ; la ligne de GO-16 est désormais lue.
- À la session : après un code de sortie 3 d'une vérification de Google, relancer après l'heure `pas_avant` du relevé (ou celle que dit `a-blanc`).

## 6. Commandes d'essai et sorties exactes

Suite v12 et suite v11, dans l'ordre, sur les fichiers scellés :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v12.py` (puis `_v11`)

```
266 passed in 115.98s (0:01:55)
257 passed in 111.64s (0:01:51)
```

Compte v12 : 257 hérités, adaptés seulement par `registre_court`, qui ajoute la ligne de GO-16 (`ligne_de_confirmation`), et neuf essais « l13 ». La suite entière du dépôt n'a pas été lancée.

## 7. Empreintes

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v12.py` | `6aa04397997a52785ce4bd05e1b7a45c5886e1565f3e2927984b08373d9758b1` |
| `scripts/relais_google_essais_admission_v12.py` | `5503eba1848c5f9f12076e62c24361a2998bf9b411e66d4663978893b202942e` |
| `scripts/relais_mistral_essais_admission_v12.py` | `e11926ec801eac06d7b64c2cc4fd9d5583482d2f4668bf374e3fa727fdfefdfe` |
| `tests/faux_fournisseur_essais_admission_v12.py` | `239271933379fffa09aeec91128310122a7311e72a571311577288533b79e5d3` |
| `tests/test_chef_essais_admission_bras_a_v12.py` | `e0d58dbf8ed7d3c87472967c131a1087cc56bf2ecb15d335179aa66ede97f2b2` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v12-gabarit.json` | `4383bf79c19e2c0ce6b2b7e447b5644827fa10c1b1b49c706c4551fd5cad5294` |
| `tests/mutations_essais_admission_v8/campagne_mutations_v8.py` | `5c7b18193586f5673ca2b47113592861320a28e8e0f21e379cb7de7a21a9f738` |
| `tests/mutations_essais_admission_v8/greffe_mutant_v8.py` | `4c6b89c5b66f712945fbc99d025ab2371b39845c944dcb1d470f3842395720b5` |

Les deux relais ne diffèrent des `_v11` que par leurs noms et versions (diff vérifié) ; le greffon, que par sa docstring. Le faux fournisseur ajoute des en-têtes au choix à `debit_google`. Cette note est scellée après ; son empreinte est à son compagnon.

## 8. Reste ouvert

- La forme réelle du 429 de Google, de son `retryDelay` et d'un refus pour crédit épuisé n'est pas relevée (GO-02 : « à vérifier au premier appel »).
- La règle propre à Google (section 2, constat 5) : une ligne de la session au journal.
- La forme des lignes de Google au registre (lignes courtes ou textes de l'avenant 3) : à trancher par la session ; les deux passent la garde 8.
- Deux lignes à Lazar avec la demande de GO des lignes de Google (vérification 12, section 5) : le second 429 qui ferme la vérification, et l'attente sur `retryDelay` ; et désormais l'attente due, au plus 600 s, avant de relancer une vérification.
- Les campagnes de la version 7 ne sont pas rejouées sur les `_v12` ; rien n'est joué sur un vrai fournisseur ; la livraison n'est pas contre-lue.

## 9. Chemins ouverts, déclarés

- **Lus** : `CLAUDE.md` ; la vérification de la livraison 12 et la note v11, en entier ; les lignes OD-351 à OD-354 du journal (par recherche) ; l'avenant 3 v2 en entier ; des `_v11`, le chef par passages (en-tête, constantes, garde 8, journaux de ligne, avenant 3 et lignes de décision, classement, fiche, vérification, file, gardes d'avant le départ, `executer`, `a_blanc`), les relais par diff, le faux fournisseur (en-tête et fabriques de Google), les essais (monde, banc, essais l9 à l12), la campagne et le greffon v7 en entier, le gabarit par recherche.
- **Registre** : les trois lignes GO-02, -03 et -16 seules.
- **Écrits** : les huit fichiers `_v12` et v8, cette note, leurs compagnons ; au bloc-notes (`/tmp/claude-0/-home-user-controle-ia-travail/829cac7d-b3f8-5154-bec8-0fa9f4eb1000/scratchpad/v13/`), les sorties des campagnes, `rejeu_survivants.py`, les sorties des suites.
- **Jamais ouverts, listés ni cherchés** : `runs/` du dépôt, `reponses-brutes-non-lues/` comprises ; `/home/user/hors-depot/` ; tout nom à « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, `archives-reponses-modeles/` ; aucun résultat de 7a, 7b, T0.6, étape B, B bis, P3-bis, barreau 5, ni de l'épreuve à vérité plantée ; ni le dossier de la tentative inachevée de la livraison 12.
