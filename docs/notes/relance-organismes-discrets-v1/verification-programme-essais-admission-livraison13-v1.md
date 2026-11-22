# Vérification du programme des essais d'admission du bras A, livraison 13 (noms `_v12`) — v1

**Verdict : engageable.** Ni bloquant ni majeur. Le majeur de la vérification 12 est levé : l'attente due après un 429 de Google est écrite au relevé, et le programme la garde. Le `retryDelay` est lu sur le corps entier, l'attente est bornée à 600 secondes, et toute relance avant `pas_avant` est refusée avant tout envoi. Les six mineurs sont levés. La vraie ligne de GO-2026-11-22-16, telle que la commande de la consigne la rend, passe la lecture que fait maintenant le chef v12 : les lignes de Google peuvent partir jusqu'au 30 novembre inclus. Restent cinq mineurs ou réserves, dont aucun ne retient le départ (section 4).

- Vérificateur : Claude Opus 5.5, neuf. Je n'ai écrit ni ce code, ni ses versions précédentes, ni la vérification 12.
- Date : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`, commit `515931ad9`.
- Processeur seulement : aucun réseau vers un fournisseur, aucune clé lue, `GO_ID` jamais fixé, aucune dépense. Rien committé, rien poussé.

## 1. Sceaux

Commande : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier` sur treize fichiers. Sortie exacte :

```
OK 6aa04397997a…  scripts/chef_essais_admission_bras_a_v12.py
OK 5503eba1848c…  scripts/relais_google_essais_admission_v12.py
OK e11926ec801e…  scripts/relais_mistral_essais_admission_v12.py
OK 239271933379…  tests/faux_fournisseur_essais_admission_v12.py
OK e0d58dbf8ed7…  tests/test_chef_essais_admission_bras_a_v12.py
OK 4383bf79c19e…  docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v12-gabarit.json
OK 5c7b18193586…  tests/mutations_essais_admission_v8/campagne_mutations_v8.py
OK 4c6b89c5b66f…  tests/mutations_essais_admission_v8/greffe_mutant_v8.py
OK e0a916d08341…  docs/notes/relance-organismes-discrets-v1/note-programme-essais-admission-bras-a-v12.md
OK 4b331d9aed86…  docs/notes/relance-organismes-discrets-v1/avenant-3-devis-essais-admission-seuils-de-credit-google-leves-v2.md
OK 1565e6e1f1b6…  docs/notes/relance-organismes-discrets-v1/verification-programme-essais-admission-livraison12-v1.md
OK 172de5acccf2…  scripts/chef_essais_admission_bras_a_v11.py
OK b0caa4fa3937…  tests/test_chef_essais_admission_bras_a_v11.py
code 0
```

Les huit empreintes de la livraison sont celles de la note v12 (section 7). Celle de la note est celle que cite OD-355 (`e0a916d0…`). Les `_v11` sont intacts.

Diff `_v11` → `_v12`, lu en entier :
- **Relais de Google et de Mistral** : noms et versions seuls.
- **Greffon** : la docstring seule.
- **Gabarit** : versions, notes, chemins et empreintes des relais `_v12` ; elles concordent avec les fichiers (`5503eba1…`, `e11926ec…`). `attente_429` est inchangé (`{"defaut_s": 30, "max_s": 600}`).
- **Faux fournisseur** : `debit_google` prend des en-têtes au choix.
- **Campagne v8** : deux campagnes neuves ; l'issue « délai » est comptée à part ; le code de sortie vaut 0 seulement si tout est tué.
- **Chef** : environ 110 lignes, toutes lues.
- **Essais** : les 257 essais hérités ne changent que par les noms et par `registre_court`, qui ajoute la ligne de GO-16. Aucune assertion n'est ôtée. Neuf essais « l13 » sont ajoutés.

## 2. Registre : GO-2026-11-22-16 passe la lecture du chef v12

Commande : `git show origin/main:registres/go.md | grep -E "GO-2026-11-22-(02|03|16) "`. Elle rend trois lignes, et seulement elles :
- **GO-02** : décision, Lazar, échéance 2026-11-30, « recharge automatique ».
- **GO-03** : décision, Lazar, exemption de la sonde, échéance 2026-11-30.
- **GO-16** : `| GO-2026-11-22-16 | 2026-11-22 | décision | **Mot de Lazar vers 2026-11-22T05:37:53Z : « oui, seuils levés ».** Bras A : confirme la conséquence tirée de GO-2026-11-22-02 par l'avenant 3 v2 (4b331d9a…) : … ; un refus pour crédit épuisé arrête la ligne et se journalise. | aucun | 2026-11-30 | Lazar | à citer dans la ligne de GO de chaque ligne de Google |`

Je lis `ligne_de_decision` (l. 1446-1470) et `controler_go_de_l_avenant_3` (l. 1515-1529) :
- la ligne est découpée sur `" | "` en huit cellules ;
- la quatrième cellule (le texte) porte « seuils levés » et `4b331d9a` ;
- la cellule du type vaut `décision`, celle de l'accord `Lazar`, celle de l'échéance `2026-11-30`.

Pour l'éprouver, j'ai passé les trois lignes, telles que la commande les rend, à `controler_go_de_l_avenant_3` sous une configuration définitive (épreuve jetable, section 6, point 4) :
- les deux vérifications de clé de Google et la file Neon sont **admises le 22 et le 30 novembre** ;
- elles sont **refusées le 1er décembre** (« échue (2026-11-30) ») ;
- une ligne de Mistral et une configuration d'essai rendent `None`.

**La ligne réelle passe : rien n'est bloqué.**

**Réserve sur le contrôle de révocation.** `ligne_de_decision` refuse toute ligne du registre qui porte « | révocation | » et cite GO-16. Je ne l'ai pas éprouvé sur le registre entier, car la consigne borne la lecture aux trois lignes. Une ligne de révocation qui citerait GO-16 refuserait toutes les lignes de Google, sans faute du code. Seule la session peut le confirmer, au premier `a-blanc`/`executer` en définitive, qui lit le registre entier : le message d'arrêt le dirait.

## 3. Le majeur de la vérification 12 : levé

### 3.1 L'attente due est écrite au relevé

- **Le calcul** (`attente_due_a_la_verification`, l. 2981-2995) :
  - il ne vaut que chez Google, sur un 429 dont l'origine est `amont`, sans signature du mandataire ;
  - l'attente est `min(attente_sur_429(en_tetes, config["attente_429"], retour["corps"]), 600)` ;
  - `pas_avant` est l'heure de réception plus l'attente, arrondie à la seconde supérieure (`math.ceil` sur l'instant).
- **L'heure de réception** : `recu = maintenant()` est relevé juste après le retour de `envoyer` (l. 3107). C'est après la réponse entière, donc du côté prudent.
- **Le corps lu est entier** : l'appel passe `retour["corps"]`, non le `corps_d_erreur` coupé à 500 octets (l. 3122-3127).
- **Où les trois champs sont écrits** :
  - à la fiche, qui va au relevé et à l'événement « envoi » du journal (l. 3165) ;
  - en tête du relevé : `attente_due_s` et `pas_avant` du 429 le plus tardif (l. 3205-3210) ;
  - au relevé réduit de la garde 18 : `origine`, `attente_due_s` et `pas_avant` y sont gardés, l'heure étant une chaîne admise (l. 3225-3236).
- **Épreuve jetable** (section 6, point 4), sur le 429 de débit du faux fournisseur : il fait 841 octets, et le `retryDelay` est à l'octet 819.
  - « 45s » rend `attente_due_s` 45.0 et `retry_delay_lu_s` 45.0. Reçu à 09:00:00,25, `pas_avant` vaut `09:00:46Z`.
  - Le même corps coupé à 500 octets rendrait 30 s. Le code ne lit donc pas le corps coupé.

### 3.2 La borne de 600 secondes

| cas | attente due |
|---|---|
| `retryDelay` de 900 s sous une règle de 1 200 | 600.0, délai lu 900.0 |
| `Retry-After: 3600` sous une règle de 7 200 | 600.0 |

La borne est en dur (`ATTENTE_DUE_MAX_S`). La file garde sa configuration, inchangée.

### 3.3 Relance refusée avant `pas_avant`

`garde_attente_due` (l. 2998-3022) est appelée par `gardes_avant_depart`, juste après le contrôle « ligne close » (l. 3961). Le chemin compte trois passages : deux fois dans `executer` (la seconde sous le verrou, au même `a_l_instant`, pris au départ), et une fois dans `a_blanc`.

Comportement éprouvé au jetable, sur un relevé à `pas_avant = 09:00:46Z` :

| instant | résultat |
|---|---|
| une seconde avant | « ARRÊT … attendre jusqu'à 2026-11-23T09:00:46Z … rien ne part » |
| à l'heure pile | admis |
| après | admis |
| heure nulle, « demain », sans `T`, nombre | arrêt « l'attente due n'est pas connue ; rien ne part ; nœud de Lazar » |
| ligne de Mistral, avant l'heure | `None` |

De bout en bout, l'essai `test_l13_bout_en_bout_relance_avant_l_heure_refusee_apres_l_heure_part`, lu, fait ceci :
- le 429 rend le code 3 ;
- une relance aussitôt, puis une relance une seconde avant l'heure, rendent le code 2, sans appel ni dossier de plus ;
- `a-blanc` refuse de même avant l'heure, puis écrit `attente_due` à l'heure ;
- après l'heure, la ligne rend le code 0, saine, en deux lancements ; le manifeste porte `attente_due`.

### 3.4 Cas sain et artefacts (R5)

Chaque branche neuve a son cas sain et son artefact :
- `test_l13_sain_…` : délai lu sur le corps entier ; 23 s ramenées à 30 ; forme courte, 30 ; `Retry-After` qui prime ; 503 et Mistral sans attente due ;
- `test_l13_bout_en_bout_…` : voir 3.3 ;
- `test_l13_artefacts_…` : relevé sans heure, délai borné à 600 s.

Ils passent tous dans la suite rejouée (section 6, point 3).

## 4. Constats

### Mineurs de la vérification 12, levés

1. **Constat 2 (GO-16 cité, jamais lu) — levé.**
   - La ligne de GO-16 est lue au registre par `ligne_de_decision` (marque « seuils levés »), et doit citer `4b331d9a`. La lecture vaut en définitive, chez Google, hors `a-blanc`, comme GO-03.
   - La recherche de la garde 8 est désormais bornée à gauche : `(?<![\w-])`.
   - La lecture est écrite au manifeste.
   - La vraie ligne passe (section 2).
2. **Constat 3 (épreuve de la garde 8 sur les textes de l'avenant 3) — levé.** L'essai `test_l13_garde_8_lit_les_trois_textes_…` est versé. Il lit les textes dans le fichier de l'avenant, sous son empreinte, et passe dans la suite. Ce que la session doit trancher reste ouvert : la forme qui ira au registre.
3. **Constat 4 (motif du second 429 après une panne) — levé.**
   - `cause_au_premier` est la cause rendue au premier envoi (l. 3403, 3433-3436). Un premier 429 rend « code 429 » (l. 3331).
   - Épreuve jetable : un 429 au second envoi, après rien ou après « code 429 », rend `MOTIF_SECOND_429` ; après « code 503 », il rend `MOTIF_429_APRES_UNE_PANNE`.
   - La décision reste l'arrêt dans tous les cas.
4. **Constat 5 (règle propre à Google) — levé.** La note v12 le dit (section 2). OD-355 porte la ligne de la session : « La règle d'OD-351 est la mienne, et propre à Google : Mistral reste au devis. »
5. **Constat 6 (cinq mutants non équivalents) — levé.** L'essai `test_l13_mutants_non_equivalents_…` les tue ; la campagne `livraison13_jouer` de l'auteur les compte tués.
6. **Constat 7 (délai compté tué) — levé.**
   - Campagne v8 : `compter_issues` compte l'issue « délai » à part, et `code_de_sortie` rend 0 seulement si tous les mutants sont tués.
   - L'essai `test_l13_la_campagne_compte_a_part_…` passe.

### Les trois mutants déclarés équivalents : je les tiens pour équivalents

7. **l. 3070, `type in (A, A′) and ligne == 3` mué en `or` : équivalent.** Le mutant n'atteint le code que si `genre == "B"`. Or `suite_de_la_verification` ne rend « B » que si un A ou A′ porte la ligne 3. Ensuite, aucun A ou A′ ne suit. Aucune sonde ne reçoit la ligne 3 : je ne trouve aucune affectation de la ligne 3 à une sonde, seulement les lignes 13 et 4, ou nulle. Le dernier élément de la liste reste donc le même.
8. **l. 3088, `None if genre == "B" else 1`, `==` mué en `!=` et `1` mué en `2` : équivalents.**
   - Pour la sonde, `garde_google_avant_envoi` sort (l. 2012-2021) avant le contrôle des jetons demandés.
   - Pour A et A′, le contrôle précédent exige un plafond d'au moins la borne plus 16 000, de sorte que 1 ou 2 jetons tiennent toujours (l. 2022-2027).

### Constats neufs

9. **Mineur : un 429 dont le journal n'a pas reçu l'« envoi » n'impose aucune attente.**
   - Le cas : le chef meurt entre le retour de `envoyer` et l'écriture de l'événement « envoi ». La réponse brute est gardée, mais personne ne la lit.
   - Ce qui suit : l'appel est reconstitué en coupure (`_appel_reconstitue`, code nul), et `garde_attente_due` ne voit pas de 429. Une relance aussitôt est permise.
   - L'effet est borné : le 429 suivant est lu comme un premier 429 (ligne 6, sans fermeture), car `second_429` ne voit pas non plus le premier. Aucune dépense de plus que le devis.
   - Ce n'est pas un repli silencieux : l'envoi coupé est journalisé, et il appelle la lecture de la console.
   - Aucune correction n'est exigée.
10. **Mineur : un relevé d'avant la livraison 13 qui porte un 429 de Google bloque la ligne.**
    - Un tel relevé, compté et sans `pas_avant`, déclenche « l'attente due n'est pas connue ; nœud de Lazar ».
    - C'est voulu (R5, aucun repli) : rien ne part sans l'heure.
    - À savoir seulement si une vérification de Google `_v11` a déjà joué sous les GO courants. Je ne l'ai pas cherché, car `runs/` m'est interdit.
11. **Mineur : l'attente due ne lie que la même ligne de calcul.**
    - `etat_de_la_ligne` est lu par GO. Une ligne nouvelle, sous un GO neuf, après la clôture d'un second 429, n'est pas retenue par le `pas_avant` de l'ancienne.
    - Cela suit le devis : une ligne close demande un nœud de Lazar, et la ligne neuve est sa décision.
    - À dire dans la demande de GO : « après un 429, la ligne neuve ne part pas avant l'heure dite par l'ancienne ».
12. **Réserve (déclarée par l'auteur, confirmée) : tout n'est pas rejoué.**
    - Les neuf campagnes de la version 7 ne sont pas rejouées sur les `_v12`.
    - Les neuf survivants de `jouer_file` sont dits tués par un rejeu un à un, non par une campagne d'un tenant.
    - Je n'ai rejoué ni l'un ni l'autre ; seule la campagne `livraison13` l'a été (section 6, point 5).
    - Les fonctions des campagnes v7, hors `decider_dans_la_file` et `verifier_ligne_de_calcul`, sont inchangées au diff : le risque est faible.
13. **Mineur, hérité et non neuf : un `Retry-After` en forme de date HTTP n'est pas lu.** Seule la forme en secondes l'est ; sinon le code prend le `retryDelay` ou le défaut de 30 s. C'est la règle du devis (5.6, « 30 sans en-tête lisible »), non un repli neuf.

## 5. Ni repli silencieux, ni régression

- **Aucun repli silencieux** dans le code neuf :
  - heure illisible : arrêt ;
  - ligne de GO-16 absente, double, échue, d'un autre type, d'un autre que Lazar, sans marque, sans empreinte ou révoquée : arrêt, chaque cas ayant son essai ;
  - cause du premier envoi non dite : le motif prudent.
- **Aucune régression** sur ce que la vérification 12 jugeait conforme :
  - la règle d'OD-351 dans la file et à la vérification, et `second_429`, sont inchangés, sauf le motif du constat 4 ;
  - `refus_pour_credit`, `classer_issue`, `attente_sur_429`, `delai_dit_par_google` et `controler_avenant_3` sont inchangés ;
  - la garde 8 n'est qu'élargie d'une borne à gauche ;
  - les 257 essais hérités passent, leurs assertions intactes.

## 6. Commandes jouées et sorties exactes

1. Sceaux : section 1.
2. Registre : section 2.
3. Suite v12, commande donnée :

   `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v12.py`

   ```
   266 passed in 117.42s (0:01:57)
   code 0
   ```

4. Épreuve jetable, sous les mêmes `env -u …` : `PYTHONPATH=src .venv/bin/python -B …/scratchpad/v13v/epreuve.py`.

   Elle charge le chef v12 et le faux fournisseur v12, lit les trois lignes du registre par la commande de la section 2, et rien d'autre. Sortie exacte :

   ```
   forme faux : ['attente_s', 'code', 'corps', 'en_tetes', 'genre']
   longueur 841 position retryDelay 819
   45s : {'attente_due_s': 45.0, 'retry_delay_lu_s': 45.0, 'pas_avant': '2026-11-23T09:00:46Z'}
   tronqué 500 : {'attente_due_s': 30.0, 'retry_delay_lu_s': None, 'pas_avant': '2026-11-23T09:00:31Z'}
   900s, max 1200 : {'attente_due_s': 600.0, 'retry_delay_lu_s': 900.0, 'pas_avant': '2026-11-23T09:10:01Z'}
   Retry-After 3600, max 7200 : {'attente_due_s': 600.0, 'retry_delay_lu_s': None, 'pas_avant': '2026-11-23T09:10:01Z'}
   signature : None
   mistral : None
   relais : None
   1 s avant : ARRÊT attendre jusqu'à 2026-11-23T09:00:46Z : l'appel L1-01-A a reçu un 429 de Google, qui demande 45.0 s d'attente avant tout lancement nouveau de la ligne ; rien ne part
   à l'heure : {'pas_avant': '2026-11-23T09:00:46Z', 'attente_due_s': 45.0, 'envoi': 'L1-01-A'}
   après : {'pas_avant': '2026-11-23T09:00:46Z', 'attente_due_s': 45.0, 'envoi': 'L1-01-A'}
   pas_avant None : ARRÊT l'appel L1-01-A a reçu un 429 de Google et le relevé ne porte pas son heure « pas_avant » 
   pas_avant 'demain' : ARRÊT l'appel L1-01-A a reçu un 429 de Google et le relevé ne porte pas son heure « pas_avant » 
   pas_avant '2026-11-23 09:00:46Z' : ARRÊT l'appel L1-01-A a reçu un 429 de Google et le relevé ne porte pas son heure « pas_avant » 
   pas_avant 12 : ARRÊT l'appel L1-01-A a reçu un 429 de Google et le relevé ne porte pas son heure « pas_avant » 
   mistral garde : None
   GO-16 verification-google-cle-1 2026-11-22 : admis 2026-11-30
   GO-16 verification-google-cle-1 2026-11-30 : admis 2026-11-30
   GO-16 verification-google-cle-1 2026-12-01 : ARRÊT garde 8 : GO de la confirmation de l'avenant 3 : la ligne GO-2026-11-22-16 est échue (2026-11-30) ou sans échéance lisible : l'exemption ne vaut plus, rien ne part
   GO-16 verification-google-cle-2 2026-11-22 : admis 2026-11-30
   GO-16 verification-google-cle-2 2026-11-30 : admis 2026-11-30
   GO-16 verification-google-cle-2 2026-12-01 : ARRÊT garde 8 : GO de la confirmation de l'avenant 3 : la ligne GO-2026-11-22-16 est échue (2026-11-30) ou sans échéance lisible : l'exemption ne vaut plus, rien ne part
   GO-16 file-neon 2026-11-22 : admis 2026-11-30
   GO-16 file-neon 2026-11-30 : admis 2026-11-30
   GO-16 file-neon 2026-12-01 : ARRÊT garde 8 : GO de la confirmation de l'avenant 3 : la ligne GO-2026-11-22-16 est échue (2026-11-30) ou sans échéance lisible : l'exemption ne vaut plus, rien ne part
   mistral GO-16 : None
   essai GO-16 : None
   file 429 rang 2 après None : ('arret', "code 429 au second envoi du même appel : crédit épuisé possible ; défaut journalisé, jamais une réponse ; la ligne s'arrête, sans autre reprise ; nœud de Lazar (GO-2026-11-22-02)")
   file 429 rang 2 après code 429 : ('arret', "code 429 au second envoi du même appel : crédit épuisé possible ; défaut journalisé, jamais une réponse ; la ligne s'arrête, sans autre reprise ; nœud de Lazar (GO-2026-11-22-02)")
   file 429 rang 2 après code 503 : ('arret', "seconde panne sur le même appel : code 429 au second envoi, après « code 503 » au premier ; la file s'arrête, sans troisième envoi")
   ```

   Trois notes sur cette épreuve :
   - Le message d'échéance de GO-16 dit « l'exemption ne vaut plus » : c'est le texte commun de `ligne_de_decision`, impropre ici mais sans effet.
   - Un premier jet, qui sérialisait le corps du faux fournisseur par `str()` au lieu de `json.dumps`, rendait 30 s partout. L'erreur était dans mon jetable, non dans le code : elle est corrigée, et seule la sortie ci-dessus compte.
   - Une première version du jetable lisait aussi le registre entier, pour éprouver la révocation. L'outil l'a refusée, et je l'ai ôtée sans la jouer (section 2, réserve).

5. Campagne de mutations `livraison13` seule :

   `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT .venv/bin/python -I tests/mutations_essais_admission_v8/campagne_mutations_v8.py livraison13 …/scratchpad/v13v/mut-livraison13.json`

   Lancée à 2026-11-22T12:38:04Z, finie à 12:45:21Z. Sortie exacte :

   ```
   livraison13 attente_due_a_la_verification 8 mutants ; 8 tués ; 0 survivants ; 0 au délai ; 0 erreurs
   livraison13 garde_attente_due 14 mutants ; 14 tués ; 0 survivants ; 0 au délai ; 0 erreurs
   livraison13 controler_go_de_l_avenant_3 9 mutants ; 9 tués ; 0 survivants ; 0 au délai ; 0 erreurs
   livraison13 verifier_ligne_de_calcul 75 mutants ; 75 tués ; 0 survivants ; 0 au délai ; 0 erreurs
   livraison13 decider_dans_la_file 55 mutants ; 55 tués ; 0 survivants ; 0 au délai ; 0 erreurs
   livraison13 a_blanc 5 mutants ; 5 tués ; 0 survivants ; 0 au délai ; 0 erreurs
   total 166 ; tués 166 ; au délai 0 ; résultats : /tmp/claude-0/-home-user-controle-ia-travail/829cac7d-b3f8-5154-bec8-0fa9f4eb1000/scratchpad/v13v/mut-livraison13.json
   code 0
   ```

   C'est le compte du second passage de la note (166 sur 166). La campagne `livraison13_jouer` n'est pas rejouée (constat 12).

Bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/829cac7d-b3f8-5154-bec8-0fa9f4eb1000/scratchpad/v13v/` (`epreuve.py`, `epreuve.txt`, `suite.txt`, `mut.txt`, `mut-livraison13.json`).

## 7. Chemins ouverts, déclarés

- **Lus** :
  - `CLAUDE.md` (en consigne) ;
  - la vérification 12 et la note v12, en entier ;
  - du journal, les lignes OD-351 à OD-355, par recherche ;
  - les diffs `_v11` → `_v12` du chef, du faux fournisseur, des essais, des relais, du gabarit (par clés JSON), de la campagne et du greffon ;
  - du chef v12, des passages : l. 226-232, 1040-1130, 1446-1529, 1984-2027, 2410-2419, 2904-2935, 2981-3022, 3058-3245, 3260-3345, 3400-3445, 3925-3985, 4025-4075 ;
  - du faux fournisseur v12, les l. 34-40 et 150-215 ;
  - des essais v12, la liste des essais « l13 » et les l. 5316-5360.
- **L'avenant 3 v2** : son sceau seul, et sa citation par le chef et le gabarit. Je ne l'ai pas relu en entier : la vérification 12 l'avait lu et il n'a pas changé (`4b331d9a…`).
- **Registre** : les trois lignes GO-02, -03 et -16 seules, par la commande de la consigne. Je n'ai fait aucune autre lecture du registre (voir 6, point 4).
- **Écrits** : au bloc-notes, les fichiers de la section 6 ; dans le dépôt, cette note et son compagnon `.sha256`.
- **Jamais ouverts, listés ni cherchés** :
  - `runs/`, dont `reponses-brutes-non-lues/` ;
  - `/home/user/hors-depot/` ;
  - tout nom à « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, `archives-reponses-modeles/` ;
  - le dossier de la livraison 12 inachevée ;
  - aucun résultat de 7a, 7b, T0.6, étape B, B bis, P3-bis, barreau 5, ni de l'épreuve à vérité plantée.
- Aucun réseau, aucun `git fetch` (`origin/main` est lu tel qu'il est en local), aucune clé, `GO_ID` jamais fixé, aucune dépense.
