# Vérification du programme des essais d'admission du bras A, livraison 12 (noms `_v11`) — v1

**Verdict : engageable après corrections** (une correction majeure, de peu de code ; aucun bloquant).

La règle d'OD-351 est codée telle qu'écrite chez Google, dans la file et dans le classement de la vérification : un 429 attend (file) ou se refait (vérification), une seule fois ; le second 429 sur le même appel arrête la ligne ; un 402 arrête aussitôt. Le faux fournisseur rend désormais le 429 de Google à la forme que la contre-lecture 11 a décrite (`RESOURCE_EXHAUSTED`, « quota », « billing », `RetryInfo`), et le cas sain passe sur cette forme. C-1, C-2 et C-3 sont levés. Le défaut qui reste : **à la vérification, l'« attente » de la règle n'est ni codée ni dite** ; un lancement nouveau fait trop tôt peut prendre un second 429, qui ferme désormais la ligne (constat 1).

- Vérificateur : Claude Opus 5.5, neuf. Je n'ai écrit ni ce code, ni ses versions précédentes, ni la contre-lecture 11. Je n'ai pas ouvert la tentative inachevée.
- Date : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`, commit `54d7f166c`.
- Processeur seulement : aucun réseau vers un fournisseur, aucune clé lue, `GO_ID` jamais fixé, aucune dépense. Rien committé, rien poussé.

## 1. Sceaux

Commande : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier` sur douze fichiers. Sortie exacte :

```
OK 172de5acccf2…  scripts/chef_essais_admission_bras_a_v11.py
OK 463d65dee094…  scripts/relais_google_essais_admission_v11.py
OK 413baf190306…  scripts/relais_mistral_essais_admission_v11.py
OK 1f800c1b0517…  tests/faux_fournisseur_essais_admission_v11.py
OK b0caa4fa3937…  tests/test_chef_essais_admission_bras_a_v11.py
OK e932f0882ce9…  docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v11-gabarit.json
OK 19c316b5624a…  tests/mutations_essais_admission_v7/campagne_mutations_v7.py
OK f848c3a70294…  tests/mutations_essais_admission_v7/greffe_mutant_v7.py
OK a8654fa463c8…  docs/notes/relance-organismes-discrets-v1/note-programme-essais-admission-bras-a-v11.md
OK 4b331d9aed86…  docs/notes/relance-organismes-discrets-v1/avenant-3-devis-essais-admission-seuils-de-credit-google-leves-v2.md
OK 421ee2e6ec90…  docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md
OK 6d650233cb4a…  docs/notes/relance-organismes-discrets-v1/contre-lecture-programme-essais-admission-livraison11-v1.md
code 0
```

Les huit empreintes de la livraison sont celles de la note v11 (section 9).

Diff `_v10` → `_v11` :
- relais de Google et de Mistral, greffon des mutations : noms et versions seuls ;
- gabarit : la pièce `avenant_3` (chemin, `4b331d9a…`), les empreintes des relais `_v11`, et les notes ;
- faux fournisseur : 72 lignes ; chef : 403 lignes ; essais : 638 lignes. Les deux premiers sont lus en entier ; des essais, les essais « l12 » et les deux essais adaptés.

## 2. Registre

Les trois seules lignes demandées, par `git show origin/main:registres/go.md | grep -E "^\| *GO-2026-11-22-(02|03|16) "` (la même recherche sur `registres/go.md` de la branche de travail ne rend rien ; c'est ce que dit aussi la note) :
- GO-2026-11-22-02 : décision, Lazar, échéance 2026-11-30, « la recharge automatique des deux projets couvre les lignes » ; « à vérifier au premier appel : un refus pour crédit épuisé est un défaut journalisé, jamais une réponse ».
- GO-2026-11-22-03 : décision, Lazar, exemption de la sonde, échéance 2026-11-30.
- GO-2026-11-22-16 : décision, Lazar, « oui, seuils levés », « un refus pour crédit épuisé arrête la ligne et se journalise », « à citer dans la ligne de GO de chaque ligne de Google ».

## 3. La règle d'OD-351, point par point

### 3.1 Dans la file (`decider_dans_la_file`, chef l. 3207-3245 ; boucle l. 3305-3375)

Conforme.
- **Google** : `refus_pour_credit` ne prend plus un 429. Un 429 au premier envoi rend « attente » ; la boucle attend `attente_sur_429`, puis fait le second envoi, sur la clé de son appel (`variable_du_rang`). Un 429 au second envoi rend « arrêt », motif `MOTIF_SECOND_429`.
- **402** : `refus_pour_credit` rend « code 402 », la file s'arrête, sans attente.
- **400 ou 403 qui dit le crédit** : arrêt sous le motif du crédit épuisé. Sans ces mots, l'arrêt vient de toute façon de la garde 4 (401, 402, 403) ou de la règle « tout autre code ». Rien n'est changé dans l'argent.
- **Mistral** : inchangé (la garde 4 arrête un 402 ; le second 429 arrête, sous son motif d'avant).
- Aucun troisième envoi possible (`for rang in (1, 2)`).

### 3.2 À la vérification (`classer_issue`, l. 2608-2672 ; `second_429`, l. 2599 ; `jouer_verification`, l. 2953-3092)

Conforme à la lettre.
- **Google, premier 429** : ligne 6, « à refaire sous la même ligne », non close, sans nœud.
- **Second 429** : un appel du même genre qui a déjà reçu un 429 du fournisseur, compté parmi les trois, dans un lancement antérieur de la même ligne de calcul (`etat_de_la_ligne`). Il est classé à la ligne 13 : close, nœud, `a_refaire` nul. De même à la sonde.
- **402, ou 403 qui dit le crédit** : ligne 13, avant les lignes 6 et 7. **400 qui le dit** : après les lignes 9 à 11.
- **Mistral** : la ligne 6 pour un 429, la ligne 7 ou 8 pour un 402 (devis).
- La mémoire de la ligne tient : `second_429` lit `code`, `origine` et `compte_parmi_les_trois`, et ces trois champs sont écrits :
  - au relevé (`fiche_technique`, l. 2779) ;
  - à l'événement « envoi » du journal, lu pour un dossier sans relevé (l. 1105-1113).
  
  Le relevé réduit de la garde 18 met `origine` à nul, mais il ferme la ligne : sans effet.

### 3.3 Cas sain et artefacts, rejoués par les essais versés

| cas | essai | issue |
|---|---|---|
| 429 de débit (forme longue, courte, ou « depleted »), puis 200 | `test_l12_sain_verification_un_429_de_debit_puis_un_200_ligne_6_puis_saine` | ligne 6, puis lancement sain, sonde comprise |
| 429 puis 200 dans la file ; `retryDelay` de 45 s ; 429 « depleted » | `test_l12_file_un_429_puis_un_200_continue_deux_429_arretent_un_402_arrete` | attente (30 ou 45 s), reprise sur sa clé, file complète |
| deux 429 sur A, puis sur la sonde | `test_l12_artefact_verification_deux_429_sur_le_meme_appel_arretent_la_ligne` | ligne 13, close, nœud, motif exact |
| deux 429 dans la file | même essai de la file | arrêt au second, aucune réponse de code 200 |
| 402 ; 403 « prepayment » ; 400 « insufficient balance » | `test_l12_artefact_un_402_ou_un_credit_dit_arrete_aussitot` | un appel, ligne 13, close, nœud |
| 402 dans la file | même essai de la file | arrêt au premier, sans attente |
| « quota », « billing », « load balancer », « credit card » | même essai | aucun arrêt pour crédit ; 400 d'orthographe « quota » : appel A′ |

Le cas sain passe sur la forme longue du faux fournisseur, qui porte « quota », « billing » et `RESOURCE_EXHAUSTED` : c'est exactement ce que la contre-lecture 11 montrait en défaut.

### 3.4 C-1, C-2, C-3

- **C-1, levé.** Le 429 de débit n'est plus pris pour un crédit épuisé : les mots « quota », « billing » et « exhausted » ne comptent plus, et un 429 n'est jamais un refus pour crédit. Le faux fournisseur rend `STATUTS_GOOGLE` par code.
- **C-2, levé.**
  - La garde 8 (l. 537-548) exige, pour toute ligne de Google, l'empreinte de l'avenant 3 et `GO-2026-11-22-16` (pas `-160`), au périmètre ou à la référence. Elle les exige en définitive, et dès que l'avenant 3 est inscrit.
  - `controler_avenant_3` vérifie la pièce sur disque et à son compagnon, et exige `4b331d9a…` en définitive.
  - **Épreuve jetable de plus** (`…/scratchpad/v12/essai_longues.py`) : les trois textes de la section 4 de l'avenant 3, tels quels, au périmètre, avec la référence « avenant 2 ; vérification du devis ; avenant 1 ; avenant 3 ; GO-2026-11-22-16 », sur le gabarit passé en définitive. Ils sont admis (3 160, 3 162 et 3 087 signes). Sans GO-16, ils sont refusés (« ne cite pas GO-2026-11-22-16, qui confirme l'avenant 3 »).
- **C-3, levé.** `GO_DE_LA_LEVEE_DES_SEUILS` est fixé. Tout autre identifiant est refusé dans tout état, à blanc compris. En définitive, la ligne de GO-02 est lue au registre : décision, Lazar, non échue, non révoquée, qui cite « recharge automatique ». La vraie ligne de GO-02 remplit ces quatre conditions.

## 4. Constats

### Constat 1 — majeur : à la vérification, l'attente de la règle n'est ni codée ni dite

- **Où** :
  - `classer_issue` (l. 2652), ligne 6 : « cause à attendre ou à corriger ; à refaire sous la même ligne » ;
  - `jouer_verification`, qui n'écrit aucune durée ;
  - `CORPS_D_ERREUR_MAX = 500` (l. 183).
- **Ce qui manque** : OD-351 dit « un 429 suit la ligne 6 (attente, une seule reprise) ». Dans une vérification, le devis exclut toute attente dans un même lancement (5.6) : la reprise est un lancement nouveau, fait par la session. Or rien n'écrit combien attendre, et rien n'empêche de relancer tout de suite.
  - Le relevé garde le corps d'erreur borné à 500 octets. Au 429 de débit du faux fournisseur, long de 841 octets, `retryDelay` est à l'octet 819 : il est perdu. Le corps entier n'est que dans `reponses-brutes-non-lues/`, que personne ne lit.
  - Avant la livraison 12, un second 429 à la vérification se refaisait encore, dans le compte des trois appels. Désormais, il ferme la ligne : une ligne de calcul perdue et un nœud de Lazar. C'est l'effet même que C-1 corrigeait, rendu possible par un relancement trop prompt.
- **Correction proposée** :
  - écrire à la fiche et au relevé, sur un 429 de Google, `attente_due_s = attente_sur_429(en_tetes, config["attente_429"], corps)` et `pas_avant = quand + attente_due_s` ;
  - faire refuser par les gardes de départ d'un lancement nouveau de la même ligne tout départ avant `pas_avant` (« ARRÊT : attendre jusqu'à … ») ;
  - un essai sain (après l'heure : part) et un artefact (avant : rien ne part).
  
  À défaut, au minimum, une phrase à la ligne de calcul : « après un 429, aucun lancement nouveau avant 600 secondes ». Mais ce serait une règle tenue par la discipline de la session, non par le programme.

### Constat 2 — mineur : GO-2026-11-22-16 est cité, jamais lu

La garde 8 exige que la ligne de calcul cite GO-16 ; rien ne lit la ligne de GO-16 elle-même (type, Lazar, échéance, révocation). Une révocation de GO-16 ne serait donc pas vue, alors que GO-02 l'est. L'échéance des deux est la même (2026-11-30), et la levée reste lue sous GO-02 : l'effet est faible. **Proposé** : lire GO-16 par `ligne_de_decision`, comme GO-02 (marque « seuils levés »). Détail : la recherche `GO-2026-11-22-16(?!\d)` n'a pas de borne à gauche (sans effet pratique).

### Constat 3 — mineur : l'épreuve de la garde 8 sur les textes de la section 4 de l'avenant 3 n'est pas versée

L'avenant 3 (section 3, point 5) demande que la garde 8 lise les textes de la section 4, et que l'épreuve soit rejouée avant qu'une ligne soit accordée. Les essais versés éprouvent les lignes courtes et le registre du monde d'essai, non ces textes. Je l'ai fait au jetable (3.4) : admis, et refusés sans GO-16. **À verser** en essai.

**À trancher par la session** : quelle forme ira au registre. La note (section 6) annonce les lignes courtes ; l'avenant 3 dit « à citer tel quel ». La garde 8 admet les deux.

### Constat 4 — mineur : le motif du second 429 dans la file couvre aussi « 500 ou coupure, puis 429 »

Chez Google, un 429 au second envoi arrête la file sous `MOTIF_SECOND_429` (« crédit épuisé possible »), même si le premier envoi était une panne et non un 429. L'arrêt est juste : aucun troisième envoi n'est permis. Le motif est vrai à la lettre (« au second envoi »), mais il suggère un crédit épuisé qu'aucun premier 429 n'annonce. Le journal porte la cause du premier envoi : sans conséquence.

### Constat 5 — mineur : la règle d'OD-351 est lue comme propre à Google

Le texte d'OD-351 ne nomme pas le fournisseur. Le code borne la règle à Google et rend Mistral au devis :
- à la vérification, un 402 à la ligne 7 ou 8, et un second 429 à la ligne 6 ;
- dans la file, rien ne change.

C'est la lecture que proposait la contre-lecture 11 (mineur 3). Elle suit GO-02, qui ne vise que Google, et revient au texte accepté. **Une ligne de la session au journal** suffit pour dire que c'est bien sa règle.

### Constat 6 — mineur : les dix mutants déclarés ne sont pas tous équivalents

Lus un à un sur le chef :

| mutant | lu | jugement |
|---|---|---|
| `classer_issue`, `code != 200` → `!= 201` | le corps n'est lu que par `signe_ne_sert_pas` (400, 404, 422) et `champs_nommes` (400, 422) ; `lire_json` ne lève jamais | **équivalent** |
| l. 3012, `genre == "B"` → `!=` ; constante 1 → 2 | la sonde sort de `garde_google_avant_envoi` avant ce contrôle ; pour A et A′, la garde exige déjà un plafond ≥ borne + 16 000 | **équivalents** (2) |
| l. 2994, `and` → `or` | B ne porte jamais la ligne 3 ; aucun A ou A′ ne suit un A ou A′ sain ; le dernier élément reste le même | **équivalent** (par argument, non par preuve) |
| l. 3126, `else 0` → `else 1` | le chef ouvre toujours un journal de relais | équivalent **en pratique** |
| l. 3129, un `or` → `and` | diffère si le résumé du constat ne porte pas `cles_levees`, ou s'il en porte d'autres que la configuration | **non équivalent** : un trou d'essai, sur une valeur écrite au relevé, qui ne commande aucun contrôle |
| quatre arrondis à six décimales (l. 3024, 3027, 3120) | écriture seule ; le compteur garde sa valeur pleine | **non équivalents**, mais sans effet sur un contrôle |

Soit **quatre équivalents vrais, un en pratique, et cinq non équivalents mais sans effet sur un arrêt**. La note les dit tous « déclarés » et en nomme cinq « équivalents » ; son tableau ne distingue pas assez. Rien de cela ne commande une garde d'arrêt.

### Constat 7 — mineur : la campagne compte un délai comme un mutant tué

`jouer` (campagne v7, l. 141) écrit « tué (délai) » sur un dépassement de 300 secondes, et le compte parmi les tués. C'est hérité des versions précédentes. Un mutant qui fait tourner la suite en rond est bien un défaut vu ; mais un essai lent sur une machine chargée serait compté tué à tort. **Proposé** : un compte à part.

## 5. Écarts déclarés au devis : acceptables ou non

| écart | jugement |
|---|---|
| **`retryDelay` de Google lu**, attente bornée à 600 s, jamais sous 30 ; l'en-tête prime (devis 5.6) | **Acceptable, sans mot de Lazar.** La borne de 600 s du devis tient, et le délai global de la file compte déjà 600 s par appel. Un refus n'est pas facturé. Sans cette lecture, la reprise tomberait souvent sur un second 429, qui arrête désormais. Forme supposée, non relevée. À dire à la ligne de calcul, comme le devis le demande pour l'attente (5.6, « il est dit à la ligne de calcul »). |
| **400 ou 403 qui dit le crédit épuisé** : arrêt (devis 4.4, ligne 7) | **Acceptable, sans mot de Lazar.** GO-2026-11-22-16 dit « un refus pour crédit épuisé arrête la ligne », sans nommer le code. Le sens est prudent : il arrête plus tôt, sans rien payer de plus. Les mots sont en mots entiers, de forme supposée. |
| **Second 429 qui arrête la vérification** (devis 4.4, ligne 6 : « refaite ») | **Acceptable, comme règle de la session (OD-351)**, plus prudente que le devis : moins d'envois, aucune dépense de plus. Mais elle coûte une ligne et un nœud au second 429 : **à dire à Lazar en une ligne avec la demande de GO des lignes de Google** ; et à rendre sûre par le constat 1. |
| **402 qui arrête aussitôt chez Google** | Déjà déclaré à la livraison 11, sous GO-02 et GO-16 : acceptable. |
| **Mistral revenu au devis** | **Acceptable, sans mot de Lazar** : c'est le texte accepté. Voir le constat 5 (une ligne de la session). |
| **Forme `"exiges"` / `{"leves_par": …}`** au lieu de `"appliques"` / `"leves"` | Acceptable : l'avenant dit « forme proposée », la seule valeur levée est fixée (C-3), et l'écart est déclaré. |
| **Lignes courtes refaites**, sans le chemin de l'avenant 2 à la référence | **Acceptable pour la garde.** L'avenant 2 (l. 425) ne demande que les empreintes. Mais ce sont des lignes de registre : la forme qui ira au registre est un choix de la session, à confirmer contre l'avenant 3 « à citer tel quel » (constat 3). |

**Aucun écart ne demande de GO** : aucun ne touche un plafond, le compteur, une dépense ou une hypothèse. Deux méritent une ligne à Lazar, avec la demande de GO : le second 429 qui ferme la vérification, et l'attente sur `retryDelay`.

## 6. Repli silencieux (R5)

Aucun trouvé dans le code neuf :
- un `retryDelay` illisible rend le défaut du devis (30 s), écrit au journal (`retry_delay_lu_s` nul) ; onze formes illisibles sont éprouvées ;
- `avenant_3` d'une autre forme : arrêt ;
- `leves_par` autre que GO-02 : arrêt ;
- `seuils_de_credit_google` nul ou absent : arrêt.

Chaque garde neuve a son cas sain et son artefact dans les essais versés. Seule réserve : le constat 1 laisse à la discipline de la session ce que le programme pourrait refuser.

## 7. Commandes jouées et sorties exactes

1. Sceaux : section 1.
2. Registre : section 2.
3. Suite v11, commande donnée :

   `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v11.py`

   ```
   257 passed in 107.26s (0:01:47)
   code 0
   ```

4. Épreuve jetable de la garde 8 sur les textes de l'avenant 3 : `PYTHONPATH=src .venv/bin/python -I -B …/scratchpad/v12/essai_longues.py`

   ```
   verification-google-cle-1 admis 3160
   verification-google-cle-1 sans GO-16 : ARRÊT garde 8 : la ligne GO-2026-11-23-01 ne cite pas GO-2026-11-22-16, qui confirme l'avenant 3
   verification-google-cle-2 admis 3162
   verification-google-cle-2 sans GO-16 : ARRÊT garde 8 : la ligne GO-2026-11-23-02 ne cite pas GO-2026-11-22-16, qui confirme l'avenant 3
   file-neon admis 3087
   file-neon sans GO-16 : ARRÊT garde 8 : la ligne GO-2026-11-23-03 ne cite pas GO-2026-11-22-16, qui confirme l'avenant 3
   ```

   Identifiants de calcul fictifs, registre fictif en mémoire.

5. Position de `retryDelay` dans le 429 de débit du faux fournisseur : `841 819 False` (longueur, position, présent dans les 500 premiers octets).
6. Campagne de mutations `livraison12` seule :

   `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 -u RR_ANTHROPIC_API_KEY_MINUIT .venv/bin/python -I tests/mutations_essais_admission_v7/campagne_mutations_v7.py livraison12 …/scratchpad/v12/mut-livraison12.json`

   Lancée à 2026-11-22T10:37:38Z. Sortie exacte :

   ```
   livraison12 refus_pour_credit 13 mutants ; 13 tués ; 0 survivants ; 0 erreurs
   livraison12 second_429 13 mutants ; 13 tués ; 0 survivants ; 0 erreurs
   livraison12 classer_issue 101 mutants ; 100 tués ; 1 survivants ; 0 erreurs
   livraison12 decider_dans_la_file 52 mutants ; 52 tués ; 0 survivants ; 0 erreurs
   livraison12 delai_dit_par_google 4 mutants ; 4 tués ; 0 survivants ; 0 erreurs
   livraison12 attente_sur_429 5 mutants ; 5 tués ; 0 survivants ; 0 erreurs
   livraison12 controler_avenant_3 17 mutants ; 17 tués ; 0 survivants ; 0 erreurs
   livraison12 a_blanc 5 mutants ; 5 tués ; 0 survivants ; 0 erreurs
      classer_issue | livraison12 : l2619 constante 200→201 | survit
   total 210 ; tués 209 ; résultats : /tmp/claude-0/-home-user-controle-ia-travail/829cac7d-b3f8-5154-bec8-0fa9f4eb1000/scratchpad/v12/mut-livraison12.json
   code 1
   2026-11-22T11:07:33Z
   ```

   Le compte est celui de la note (210 mutants, 209 tués). Le seul survivant est le mutant déclaré, équivalent (constat 6). Le code de sortie 1 vient de ce survivant. La campagne `livraison12_mineur5` (neuf survivants déclarés) n'a pas été rejouée ; ses mutants sont jugés à la lecture du code seulement (constat 6).

Bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/829cac7d-b3f8-5154-bec8-0fa9f4eb1000/scratchpad/v12/`.

## 8. Chemins ouverts, déclarés

- **Lus** :
  - `CLAUDE.md` ;
  - la contre-lecture 11, en entier ;
  - du journal, les lignes OD-351 à OD-353, par recherche (OD-352 et OD-353 sont venues avec) ;
  - la note v11, en entier ;
  - le chef, le faux fournisseur, les relais, le gabarit et le greffon, par diff avec les `_v10`, et des passages du chef (l. 500-550, 1040-1120, 1956-2000, 2599-2672, 2755-2800, 2860-2880, 2940-3092, 3125-3160, 3207-3375) ;
  - des essais v11, les l. 4259-4300, 4375-4400, 4770-5085 ;
  - la campagne v7, en entier ;
  - du devis, les lignes qui citent 429, 402, `Retry-After` ou « crédit épuisé » (recherche), et sa ligne 268 ;
  - de l'avenant 2 v3, les l. 420-427 ;
  - de l'avenant 3 v2, les l. 20-66 (sections 1 à 4) et une recherche.
- **Registre** : les trois lignes GO-02, -03 et -16 seules, par `grep` (section 2).
- **Écrits** :
  - au bloc-notes : `essai_longues.py` et les sorties ;
  - dans le dépôt : cette note et son compagnon.
  
  Le répertoire temporaire de la campagne est créé par l'outil sous `/tmp`.
- **Jamais ouverts, listés ni cherchés** :
  - `programme-essais-admission-livraison12-inacheve-2026-11-22/` ;
  - `runs/`, dont `reponses-brutes-non-lues/` ;
  - `/home/user/hors-depot/` ;
  - tout nom à « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, `archives-reponses-modeles/` ;
  - aucun résultat de 7a, 7b, T0.6, étape B, B bis, P3-bis, barreau 5, ni de l'épreuve à vérité plantée.
  
  Un `ls` du dossier de la relance, filtré par motif (livraison 11 et 12, v10, v11, devis, avenant), a affiché le nom du dossier inachevé ; je ne l'ai pas ouvert.
- Aucun réseau, aucun `git fetch` (`origin/main` est lu tel qu'il est en local), aucune clé, `GO_ID` jamais fixé, aucune dépense.
