# Note de livraison 12 — programme des deux essais d'admission du bras A, version 11

- État : livrée à la session le 22 novembre 2026. Fichiers scellés par l'agent (empreinte compagnon `.sha256`), rien committé, rien poussé : la session committe.
- Auteur : agent du code de la livraison 12 (Claude Opus 5.5), sous la consigne de la session (journal OD-351). Processeur seulement : aucun réseau vers un fournisseur, aucun `git fetch`, aucune clé lue ni affichée, `GO_ID` jamais fixé, aucune dépense.
- Objet : les corrections de la contre-lecture de la livraison 11 (`contre-lecture-programme-essais-admission-livraison11-v1.md`, `6d650233…`, « engageable après corrections ») : C-1 à C-3 et les sept mineurs, sous la règle retenue par la session.
- Base : les `_v10` scellés, à leurs empreintes (chef `52c39b55…`, relais de Google `c88fae29…`, relais de Mistral `016f7428…`, faux fournisseur `2e3ce905…`, essais `39270559…`, gabarit `d44ed9b4…`, campagne v6 `5690fa75…`, greffon v6 `39f8a5b4…`), recalculées, égales aux compagnons. Note v10 `965ffd03…`, devis `421ee2e6…` (lignes qui citent 429 et 402, par recherche), avenant 3 v2 `4b331d9a…` lu en entier.
- Registre : les seules lignes GO-2026-11-22-02 et GO-2026-11-22-16, par `git show origin/main:registres/go.md | grep -E "GO-2026-11-22-(02|16)"`. Cette commande a affiché aussi la ligne GO-2026-11-22-07 (relectures par Fable), qui cite GO-02 en passant ; je ne m'en suis pas servi. La même recherche sur `registres/go.md` de la branche de travail ne rend rien.

## 0. Ce que j'ai pris de la tentative inachevée

Lue comme matière (`programme-essais-admission-livraison12-inacheve-2026-11-22/`), jamais reprise telle quelle : chaque fichier `_v11` est recopié des `_v10` scellés, puis écrit à neuf.
- Pris : l'idée d'une fonction `second_429` (même genre d'appel, déjà compté sous un 429 du fournisseur, dans un lancement antérieur), le bornage de `refus_pour_credit` à Google, le placement du 400 après les lignes 9 à 11, une liste de mots entiers, l'idée d'une table des statuts de Google au faux fournisseur, et la forme des noms des essais « l12 ».
- Non pris, ou changé :
  - la levée « sous une décision qui cite GO-02 » : ici, GO-2026-11-22-02 seul (consigne, point 6) ;
  - la lecture de GO-16 au registre à la levée : non faite (consigne : la levée sous GO-02 seulement ; GO-16 est exigé par la garde 8, dans les lignes) ;
  - le `retryDelay` de Google, que la tentative laissait non lu : il est lu ici (section 1.4, écart déclaré) ;
  - les mots relus sans leurs échappements JSON (« crédit ») ;
  - les lignes courtes du registre, refaites pour tenir sous 600 signes (section 2) ;
  - la campagne `livraison12_mineur5` (mineur 5), que la tentative laissait hors campagne.

## Journal

1. Huit fichiers `_v11` et outils v7 copiés des `_v10` et des outils v6 par un programme qui les nomme un à un ; seuls les noms changent ; puis les versions des en-têtes. Les `_v10` et les outils v6 ne sont pas touchés.
2. Codé dans le chef : C-1 (section 1), C-2 (section 2), C-3 (section 3), mineurs 2, 3, 4, 6 (section 4).
3. Faux fournisseur : statut de Google par code, 429 de débit à la forme réelle, crédit épuisé de forme supposée.
4. Les trois essais de la livraison 11 sur le refus pour crédit portaient la règle que C-1 corrige : retirés, remplacés par dix essais « l12 » ; deux essais « m2_l12 » ajoutés par la campagne (section 8). Deux essais hérités adaptés (section 6). Compte : 248 − 3 + 12 = 257.
5. Essais et campagne : sections 7 et 8.

## 1. C-1 — chez Google, le 429 suit la ligne 6 ; le second arrête la ligne ; le 402 arrête aussitôt

### 1.1 La règle (OD-351), codée chez Google seulement

- **Un 429 suit la ligne 6 du devis (4.4)** :
  - à une vérification : « à refaire sous la même ligne », par un lancement nouveau, si le compteur le permet ;
  - dans la file : une attente (5.6), puis une seule reprise, sur la clé de son appel.
  
  Un 429 n'arrête **jamais** aussitôt, même s'il dit « prepayment credits are depleted » : il ne se distingue pas d'un débit.
- **Un second 429 sur le même appel arrête la ligne.** Motif exact (`MOTIF_SECOND_429`) :

  > code 429 au second envoi du même appel : crédit épuisé possible ; défaut journalisé, jamais une réponse ; la ligne s'arrête, sans autre reprise ; nœud de Lazar (GO-2026-11-22-02)

  Le « même appel » :
  - à la vérification (`second_429`) : un appel du même genre (A, A′ ou la sonde B), compté parmi les trois, qui a reçu un 429 **du fournisseur** dans un lancement antérieur de la même ligne. L'appel est classé à la ligne 13 : close, nœud de Lazar, `a_refaire` nul. Un 429 écrit par le relais, un appel non compté, ou un 429 sur un autre genre d'appel ne comptent pas ;
  - dans la file : le second envoi d'un appel, comme avant ; seul le motif change chez Google.
- **Un 402 arrête la ligne aussitôt** (`refus_pour_credit`), de même qu'un **400 ou 403** dont le corps dit le crédit épuisé en mots entiers. Motif : « refus pour crédit épuisé (code N, « forme lue ») : défaut journalisé, jamais une réponse ; la ligne s'arrête, sans reprise ni appel de plus ; nœud de Lazar (GO-2026-11-22-02) ».

### 1.2 Les mots du crédit dit (400 et 403 seulement)

En minuscules, en mots entiers, sur le corps relu sans ses échappements JSON :
- `prepay`, `prepayment(s)`, `prepaid`, `depleted` ;
- `insufficient balance`, `insufficient funds`, `insufficient credit(s)`, `out of credit(s)` ;
- `credit(s) exhausted`, `credit(s) expired` ;
- `crédit(s) épuisé(s)`, `crédit(s) insuffisant(s)`, `solde épuisé`, `solde insuffisant` ;
- `payment required`.

Ne comptent plus : `quota`, `billing`, `exhausted`, `balance` seul (« load balancer »), `credit` seul (« credit card »), `payment` seul.

### 1.3 Placement au classement de la vérification

- 402, et 403 qui dit le crédit : avant les lignes 6 et 7 ;
- second 429 : avant la ligne 6 ;
- 400 qui dit le crédit : après les lignes 9 à 11 (mineur 2) : un 400 d'orthographe du niveau de réflexion qui dirait « quota » garde son appel A′.

### 1.4 Le `retryDelay` de Google (proposition b de la contre-lecture) — écart déclaré au devis 5.6

Le devis dit : « ce que dit l'en-tête `Retry-After`, borné à 600 secondes (30 sans en-tête) ». Google ne porte en général pas cet en-tête, mais `RetryInfo.retryDelay` dans le corps. Attendre 30 secondes sur un « 45s » ferait tomber la reprise sur un second 429, qui arrête désormais la ligne.
- Codé : sans en-tête lisible, si le corps porte un `retryDelay` lisible (« 23s », « 45.2s ») **plus long que le défaut**, la file attend ce délai, arrondi à la seconde supérieure et borné à 600. Jamais moins que le défaut. L'en-tête prime.
- La borne de 600 secondes, comptée au délai global de la file, ne change pas.
- Le délai lu est écrit au journal (`attente_sur_429.retry_delay_lu_s`).
- Forme supposée, non relevée sur le service.

### 1.5 Mistral (mineur 3)

Hors de GO-2026-11-22-02. Retour au devis :
- à la vérification, 402 à la ligne 7 (ou 8), 429 à la ligne 6, sans arrêt au second 429 (les trois appels bornent) ;
- dans la file, inchangé : 402 arrête (garde 4), le second 429 arrête.

**Écart à la livraison 11, déclaré** : un 402 ou un 429 « insufficient » de Mistral n'est plus à la ligne 13.

### 1.6 Faux fournisseur

- `erreur_google` rend le statut de Google par code (`STATUTS_GOOGLE` : 400 `INVALID_ARGUMENT`, 403 `PERMISSION_DENIED`, 429 `RESOURCE_EXHAUSTED`…), et non plus `INVALID_ARGUMENT` pour tout code.
- Sans message dit, un 429 rend le débit à sa forme longue ; `debit_google()` le rend aussi : « You exceeded your current quota, please check your plan and billing details … rate-limits », `QuotaFailure` par minute, lien d'aide, `RetryInfo` (23 s par défaut). La forme courte : « Resource has been exhausted (e.g. check quota). ».
- `credit_epuise_google()` : « Your prepayment credits are depleted … billing », `RESOURCE_EXHAUSTED`, de forme supposée.

| essai | cas sain | artefact |
|---|---|---|
| `test_l12_le_faux_fournisseur_rend_le_429_de_google_a_sa_forme_reelle` | statuts par code ; quota, billing, `RetryInfo` | — |
| `test_l12_sain_verification_un_429_de_debit_puis_un_200_ligne_6_puis_saine` | forme longue, courte, et 429 « depleted » : ligne 6, à refaire, sans nœud ; lancement nouveau sain ; un 429 sur A puis sur B : B à refaire | — |
| `test_l12_artefact_verification_deux_429_sur_le_meme_appel_arretent_la_ligne` | Mistral : deux 429, ligne 6 ; `second_429` : relais, autre genre, non compté, autre code : faux | deux 429 sur A : ligne 13, close, nœud, motif exact, deux appels, ligne close ensuite ; deux 429 sur la sonde : de même |
| `test_l12_artefact_un_402_ou_un_credit_dit_arrete_aussitot` | 400 d'orthographe qui dit « quota » : A′ ; 403 « quota, billing, load balancer » : ligne 7 ; Mistral 402 : ligne 7 ; huit textes ambigus : rien ; 429 « depleted » : rien | 402, 403 « prepayment », 400 « insufficient balance » : un appel, ligne 13, close, nœud, motif exact ; 402 à la sonde ; quatorze formes reconnues |
| `test_l12_file_un_429_puis_un_200_continue_deux_429_arretent_un_402_arrete` | 429 de débit puis 200 : attente de 30 s, reprise sur sa clé, file complète ; `retryDelay` 45 s : attente de 45 s ; 429 « depleted » : attente, file complète | deux 429 : arrêt au second, motif exact, aucune réponse de code 200 ; 402 : arrêt au premier, sans attente |
| `test_l12_attente_sur_429_lit_le_retry_delay_de_google` | 23 s : 30 ; 45 s : 45 ; 45,2 s : 46 ; 900 s : 600 ; l'en-tête prime | onze corps illisibles ou sans `RetryInfo` : le défaut |

## 2. C-2 — la garde 8 exige l'avenant 3 et GO-2026-11-22-16

- **Pièce neuve `avenant_3`** (chemin et empreinte), inscrite au gabarit : `avenant-3-devis-essais-admission-seuils-de-credit-google-leves-v2.md`, `4b331d9a…`. `controler_avenant_3`, appelé par `gardes_avant_depart` (à blanc compris), pour les seules lignes de Google :
  - nulle ou pièce ; toute autre forme est refusée ;
  - inscrite, elle est vérifiée dans tout état, sur disque, à son empreinte et à son compagnon ;
  - en définitive, elle est exigée, d'empreinte `4b331d9a…` ;
  - le manifeste et la sortie à blanc la recopient.
- **Garde 8**, pour une ligne de Google :
  - en définitive, la configuration inscrit l'avenant 3 ;
  - dès qu'elle l'inscrit, la ligne du registre cite son empreinte **et** `GO-2026-11-22-16` (pas « GO-2026-11-22-160 »), au périmètre ou à la référence.
- **Les lignes courtes du registre changent** (note de la livraison 8, section 4). La limite de 600 signes des consignes ne laisse pas la place de l'avenant 3 et de GO-16 à côté du chemin de l'avenant 2 (660, 662 et 697 signes). Le chemin de l'avenant 2 sort de la référence : la garde ne le lit pas, et l'avenant 2 (ligne 425) ne demande que les empreintes. Forme nouvelle de la référence, sans libellé :

  ```
  9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3 ; 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca ; 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; 4b331d9aed86b280ea720ac554911df168fe7564799957a29776a1cad4dbeaa0 ; GO-2026-11-22-16
  ```

  Avec un identifiant à deux chiffres finaux et des dates pleines : **525, 527 et 562 signes**. Périmètre, plafond, type, dates : inchangés.

| essai | cas sain | artefact |
|---|---|---|
| `test_l12_garde_8_exige_l_avenant_3_et_go_16` | les trois lignes courtes ; citations au périmètre ; à l'essai, avenant 3 nul : non lu ; Mistral sans objet | empreinte de l'avenant 3 absente ; GO-16 absent, en « -160 », remplacé par GO-02 ; définitive sans avenant 3 (nul, chaîne) ; à l'essai, avenant 3 inscrit et non cité |
| `test_l12_la_piece_de_l_avenant_3` | la pièce du gabarit, sur disque, en définitive ; trois formes nulles à l'essai ; Mistral | définitive nulle ; autre empreinte (une autre pièce scellée, l'avenant 2) ; empreinte fausse ; sans compagnon ; à moitié inscrite ; absente ; chaîne ; liste ; clé de trop ; la ligne entière à blanc |
| `test_l9_lignes_courtes_du_registre_eprouvees_a_blanc_de_bout_en_bout` (adapté) | 525, 527, 562 signes ; toutes les gardes d'avant le départ | une marque retirée |

## 3. C-3 — la levée des seuils sous GO-2026-11-22-02 seulement

- `seuils_de_credit_google` : `{"leves_par": …}` n'admet que `GO-2026-11-22-02` (constante `GO_DE_LA_LEVEE_DES_SEUILS`), **dans tout état**, à blanc compris. Un autre identifiant est refusé, même s'il est une décision de Lazar qui cite la recharge automatique (le GO-2026-11-21-99 fictif de la contre-lecture) : « les seuils de crédit de Google ne sont levés que sous GO-2026-11-22-02 ; … n'est pas admis : rien ne part ».
- En définitive, sa ligne est lue au registre comme à la livraison 11 : une seule, de huit cellules, de type `décision`, de Lazar, non échue, non révoquée, qui cite « recharge automatique ».
- GO-2026-11-22-16 n'est pas lu à la levée : il est exigé, cité, dans chaque ligne de Google (section 2).

| essai | cas sain | artefact |
|---|---|---|
| `test_l12_levee_des_seuils_seulement_sous_go_02` | GO-02, lu au registre ; « exiges » | GO-2026-11-21-99 qui cite la recharge : refusé en définitive, à l'essai, et à blanc |

Les essais `l11` de la levée (échue, sans la mention, de type `calcul`, absente, formes) sont gardés et passent.

## 4. Les sept mineurs

| mineur | traité comment |
|---|---|
| 1. forme du champ (`"appliques"`/`"leves"` à l'avenant 3) | **non changé, écart déclaré** : le code garde `"exiges"` et `{"leves_par": "GO-2026-11-22-02"}`. L'avenant dit « forme proposée » ; la forme du code nomme le GO lu au registre, et C-3 en fixe la seule valeur |
| 2. mots cherchés comme sous-chaînes ; un 400 « quota » perdait A′ | **corrigé** : mots entiers, liste resserrée, corps relu sans échappements ; 400 après les lignes 9 à 11 (section 1) |
| 3. refus pour crédit appliqué à Mistral | **corrigé** : Google seul ; Mistral revient au devis (section 1.5) |
| 4. sortie `a-blanc` muette | **corrigé** : elle imprime `seuils_de_credit_google`, `avenant_3` et `registre_lu: false` (`test_l12_a_blanc_dit_les_seuils_et_que_le_registre_n_est_pas_lu`) |
| 5. fonctions changées hors campagne | **corrigé** (comptes à la section 8) : `classer_issue`, `decider_dans_la_file`, `refus_pour_credit`, `second_429`, `delai_dit_par_google`, `attente_sur_429`, `controler_avenant_3`, `a_blanc` dans la campagne `livraison12` ; `jouer_verification` et `garde_console` dans la campagne `livraison12_mineur5` ; la garde 8 et la levée restent dans `livraison9` et `livraison11`, essais « l12 » ajoutés |
| 6. `RR_ANTHROPIC_API_KEY_MINUIT` non retirée | **corrigé** : ajoutée à `VARIABLES_RETIREES` et retirée de toutes mes commandes |
| 7. échéance lue au seul départ | **non changé** : c'est la règle de toutes les gardes de départ ; une file partie le 30 novembre au soir continue après minuit, sans effet pratique |

## 5. Écarts déclarés

Au devis :
1. **5.6, le `retryDelay` de Google** (section 1.4) : une attente plus longue que 30 secondes sans en-tête, bornée à 600.
2. **4.4, ligne 7, chez Google** : un 402 arrête la ligne (déjà déclaré à la livraison 11, sous GO-2026-11-22-02) ; un 400 ou un 403 qui dit le crédit épuisé, de même.
3. **4.4, ligne 6, chez Google** : le second 429 sur le même appel arrête la ligne, au lieu de « refaite sous la même ligne » (règle de la session, OD-351).

À la livraison 11 et à l'avenant 3 :
4. Mistral revient au devis (section 1.5).
5. Forme du champ des seuils (mineur 1).
6. Lignes courtes du registre : le chemin de l'avenant 2 sort de la référence (section 2).

À la consigne : aucun.

## 6. Configuration définitive de Google, ce qui change d'avec la note v10

À tirer du gabarit `_v11` sous un nom neuf, scellée, comme à la note v10, section 3, avec :
- `"version": "configuration-essais-admission-bras-a-v11-google-AAAA-MM-JJ-v1"` ;
- `avenant_3` au gabarit (`4b331d9a…`) : on le garde ;
- `"seuils_de_credit_google": {"leves_par": "GO-2026-11-22-02"}` : la seule levée admise ;
- les empreintes des relais `_v11` au gabarit : relais de Google `463d65de…`, relais de Mistral `413baf19…`.

Au registre :
- les trois lignes courtes de Google, à la référence nouvelle de la section 2 ;
- GO-2026-11-22-02, -03 et -16, déjà sur la branche principale, valables jusqu'au 30 novembre inclus.

Deux essais hérités adaptés, sans toucher un contrôle :
- `registre_court` (forme de la section 2) et le registre d'essai du monde, qui citent l'avenant 3 et GO-16 quand la configuration l'inscrit ;
- `test_m2_l11_artefacts_ajoutes_par_la_campagne_de_la_livraison_11` : `refus_pour_credit` prend le fournisseur.

## 7. Commandes d'essai et leurs sorties

Commande (suite v11) :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v11.py`

- Avant la campagne : `255 passed in 111.05s`.
- Sur l'état livré, après les deux essais de la campagne : `257 passed in 113.53s (0:01:53)`. Dernier lancement : section 9.

Essais v10, inchangés, par la même commande sur `tests/test_chef_essais_admission_bras_a_v10.py` : `248 passed in 106.94s (0:01:46)`.

La suite entière du dépôt n'a pas été lancée (consigne : les essais v11 et v10).

## 8. Campagne de mutations, version 7

Commande, depuis la racine, par campagne :

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT .venv/bin/python -I tests/mutations_essais_admission_v7/campagne_mutations_v7.py CAMPAGNE SORTIE.json`

Neuf campagnes, 1 035 mutants (`compter`). Les sept de la version 6, rejouées sur les `_v11`, et deux neuves :
- `livraison12` : `refus_pour_credit`, `second_429`, `classer_issue`, `decider_dans_la_file`, `delai_dit_par_google`, `attente_sur_429`, `controler_avenant_3`, `a_blanc` ;
- `livraison12_mineur5` : `jouer_verification` et `garde_console` (mineur 5), sur toute la suite d'essais.

`refus_pour_credit` passe de `livraison11` à `livraison12`. Les essais « l12 » sont ajoutés aux sous-ensembles de `livraison9` (garde 8) et `livraison11` (levée).

**Comptes exacts, par campagne** :

| campagne | mutants | tués | survivants déclarés | comment |
|---|---|---|---|---|
| `regle_google` | 108 | 108 | 0 | un passage |
| `livraison6` | 168 | 168 | 0 | un passage |
| `livraison7` | 80 | 80 | 0 | un passage |
| `livraison8` | 48 | 48 | 0 | un passage |
| `livraison9` | 132 | 132 | 0 | un passage, essais « l12 » compris |
| `livraison10` | 26 | 26 | 0 | un passage |
| `livraison11` | 56 | 56 | 0 | un passage, essais « l12 » compris |
| `livraison12` | 210 | 209 | 1 | trois passages (ci-dessous) |
| `livraison12_mineur5` | 207 | 198 | 9 | trois passages (ci-dessous) |
| **ensemble** | **1 035** | **1 025** | **10** | |

**`livraison12`**. 
- Premier passage : 212 mutants, 177 tués, 35 survivants. Ils tenaient à des branches de `classer_issue` et `decider_dans_la_file` que seuls des essais hors du sous-ensemble éprouvaient, à des bornes exactes, et à un mutant équivalent de `attente_sur_429`.
  - Ce dernier, `>` en `>=` sur le défaut, rendait la même valeur ; le code est simplifié pour l'ôter (`max(ceil(délai), défaut)`, borné à 600), sans changer le comportement. D'où 210 mutants ensuite.
  - Les autres sont tués par `test_m2_l12_artefacts_ajoutes_par_la_campagne_de_la_livraison_12`.
- Deuxième passage : 210 mutants, 205 tués. Les cinq survivants tenaient au message exact de la ligne 4 ; quatre sont tués par le même essai, complété (rejoués un à un sur le sous-ensemble de la campagne).
- **Un survivant déclaré, équivalent** : `classer_issue`, `corps = lire_json(…) if code != 200`, mutant `!= 201`. Le corps d'un code 200 n'est lu que par `signe_ne_sert_pas` (qui exige 400, 404 ou 422) et `champs_nommes` (400 ou 422 seulement). Aucun essai ne peut le distinguer.

**`livraison12_mineur5`**.
- Premier passage, sur un sous-ensemble : 207 mutants, 169 tués, 38 survivants.
- Rejoués sur toute la suite : 12 sont tués par des essais hors du sous-ensemble. La campagne se joue désormais sur toute la suite.
- `test_m2_l12_mineur5_jouer_verification_et_garde_console` ajouté. Il éprouve :
  - les numéros d'envoi et de rang, la ligne finale, les pauses ;
  - la règle de Google lue avant tout appel ;
  - les codes 500, 599 et 600 à la sonde ; la ligne 13 à la sonde ;
  - la ligne 1 à l'appel A ;
  - le relevé réduit ;
  - le nœud sous un retrait de température ;
  - à la console : la page et l'heure, le seuil pile (exigé et levé), l'arrondi de la dépense comptée.
- Rejoués : tous tués sauf neuf.
- **Neuf survivants déclarés** :
  - **quatre arrondis d'écriture** à six décimales : au journal, `reserve_usd` et `cumul_usd` (ligne 3024) et `cout_si_sans_reponse_usd` (ligne 3027) ; au relevé, `depense_comptee_usd` (ligne 3120). Sur les valeurs de l'essai, sept décimales rendent le même nombre. Ces arrondis ne commandent aucun contrôle : le compteur garde sa valeur pleine ;
  - **deux équivalents** sur `jetons_de_texte_demandes=None if genre == "B" else 1` (ligne 3012). La sonde sort de la règle avant ce contrôle ; pour A et A′, un, deux ou aucun jeton de texte tiennent toujours sous le plafond de texte (au moins 16 000) ;
  - **un équivalent**, le choix de l'appel sain (ligne 2994), `type in (A, A′) and ligne == 3` mué en `or`. Le dernier élément de la liste reste le dernier appel A ou A′ sain : aucun appel B ne porte la ligne 3, et aucun A ne suit un A sain ;
  - **un équivalent en pratique**, `cle_vue_dans_une_reponse = … if journal_relais else 0` mué en `1` (ligne 3126) : un relais sans journal n'existe pas, le chef en ouvre toujours un ;
  - **un équivalent sur les essais**, `(constat_resume or {}).get("cles_levees") or {…}`, l'un des deux `or` mué en `and` (ligne 3129) : le résumé du constat et la configuration portent le même GO et les mêmes clés levées.

  Les numéros de ligne sont ceux de la version rejouée du chef.

**Réserve** : les mutants tués aux passages 2 et 3 l'ont été par rejeu de chaque survivant, sur le sous-ensemble de sa campagne (ou toute la suite pour `livraison12_mineur5`), non par une campagne `toutes` rejouée d'un seul tenant après le dernier essai. Une campagne `toutes` prendrait quatre heures environ sur quatre processeurs : je ne l'ai pas lancée. Les sorties sont au bloc-notes de la session (`mut-*-2.json`, `mut-*-3.json`, `rejeu-mineur5-*.txt`).

## 9. Empreintes et dernier lancement

Chaque fichier est scellé par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller …` (compagnon `.sha256`). Cette note est scellée après, son empreinte est à son compagnon.

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v11.py` | `172de5acccf28efbfae255ffd7b0be0f8e5abf026799167f06a606f6265b62d9` |
| `scripts/relais_google_essais_admission_v11.py` | `463d65dee094b883021b7a1bec7e9d92f123477f195cd3a946cc393a9212e7a0` |
| `scripts/relais_mistral_essais_admission_v11.py` | `413baf190306b4d2147ca9d454b4fecc9230180f8c049669011b7d562116e5f0` |
| `tests/faux_fournisseur_essais_admission_v11.py` | `1f800c1b051747aa7dd45ee860f9c25e07011d63008067d05350073e55b21fb8` |
| `tests/test_chef_essais_admission_bras_a_v11.py` | `b0caa4fa393743c5d37fc8c9a215ff851069c4a0165fb12b18568d23cdc224c0` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v11-gabarit.json` | `e932f0882ce948e76c334476745c644b5b4d7910b4c8821325d9aace35923a19` |
| `tests/mutations_essais_admission_v7/campagne_mutations_v7.py` | `19c316b5624a210949bd8e301193c891f5b12a7c1a578c043cbb98b6dc674894` |
| `tests/mutations_essais_admission_v7/greffe_mutant_v7.py` | `f848c3a70294b34c9de316c844663881b485c82b53ce641ffc42ac1b13a51bec` |

Les deux relais et le greffon ne diffèrent des `_v10` (et des outils v6) que par leurs noms et versions. Leurs empreintes sont égales à celles des copies inachevées, faites par le même changement mécanique.

Dernier lancement de la suite v11, sur les fichiers scellés : `257 passed in 105.37s (0:01:45)`.

## 10. Reste ouvert

- La forme réelle d'un refus de Google pour crédit épuisé n'est pas relevée ; celle du 429 de débit est supposée (contre-lecture). Les listes de mots et la lecture de `retryDelay` sont à revoir au premier refus réel (GO-02 : « à vérifier au premier appel »).
- Sous la règle, un crédit épuisé qui rend un 429 coûte une attente et une reprise, puis arrête la ligne ; un refus n'est pas facturé.
- Les lignes de décision échoient le 30 novembre ; la pièce de constat du 21, le 24 à 00:00Z, sous une borne de 96 heures.
- `jetons_par_mot` et les limites de mots, par le lecteur habilité.
- Rien n'a été joué sur un vrai fournisseur.
- La note et ses fichiers ne sont pas contre-lus.

## 11. Chemins ouverts, déclarés

- **Lus** :
  - `CLAUDE.md` ;
  - la contre-lecture de la livraison 11, la note v10, la ligne OD-351 du journal (et, par la même recherche, OD-352) ;
  - l'avenant 3 v2 en entier ; de l'avenant 2 v3, les lignes 415 à 426 et une recherche de « 600 signes » ;
  - du devis, les lignes qui citent 429 ou 402 ;
  - de la note v8, la section 4 ; de la note v9, une recherche de « 600 signes » ;
  - les `_v10` et les outils v6 ;
  - la tentative inachevée (inventaire, note, diff du chef et du faux fournisseur, noms des essais) ;
  - du registre, les seules lignes de la section d'en-tête.
- **Écrits** : les huit fichiers `_v11` et v7, cette note, leurs compagnons ; au bloc-notes, deux programmes de copie et les sorties de la campagne.
- **Aucun chemin interdit** ouvert, listé ni cherché : rien sous `runs/`, rien sous `/home/user/hors-depot/`, aucun nom à « consigne-privee » ou « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni `archives-reponses-modeles/`. Aucun `sed` hors de mes fichiers.
