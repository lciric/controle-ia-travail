# Commandes exactes v3 — emploi de la relecture exploratoire v2 (règle v2.1, outil v3.2.1)

## En tête de la v3 (rédacteur neuf, modèle A ; 14 novembre 2026, 23:33 à 23:38 UTC, `date -u`)

**Ce que la v3 change, et rien d'autre.** La v3 est la v2 (`RE/commandes-exactes-v2.md`,
`bd259d2c197414959cd03a119db0cbe25eedcd2238ff00aa2e3cd6fd83ffbc51`, gardée telle quelle, R12) où sont portés **exactement
les trois couples exigés** par `RE/verification-courte-commandes-exactes-v2-modele-b-v1.md`
(`90f3cc620de8fd0716f5b3288060dc31be2ca8da1e3bc0e7cf2b74d1c68f5246`, § 5, couples 1 à 3), plus, sur la demande de la
mère, deux ajouts au point 0. Rien d'autre n'est changé. Sept remplacements, chacun appliqué par programme à un texte
présent une seule fois dans la v2 :

| Origine | Où | Ce qui change |
|---|---|---|
| Couple 1 | table du point 7, dernière ligne | « pas de code (tâche tuée à la limite, coupure de la session, notification perdue) » → « tout autre code (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code », même conduite |
| Couple 1 | point 6, puce K4 | ajout de la même phrase pour le code de l'`envoyer` du point 6 : tout code autre que 0 (mêmes codes) ou pas de code, rien de plus, nœud |
| Couple 2 | sous le contrôle B | ajout du cas où il ne rend pas sa ligne (`ValueError`, `Refus`) : jouer `bilan` seul ; refus (code 2) ou `en_vol` non vide : dossier perdu, nœud. Des deux formes offertes par le couple, c'est **la première (texte)** qui est portée ; la commande du contrôle B reste **inchangée** (pas de `default=None`) |
| Couple 3 | point 13 | « somme des `depense_comptee_usd` du dernier relevé » → « le `depense_comptee_usd` rendu par `bilan` (cumul du journal, appel en vol compris) ; les relevés sont cumulatifs, on ne les additionne pas » |
| Couple 3 | point 14 | même remplacement ; « des relevés du dossier arrêté » devient « sur le dossier arrêté », et « cette somme, elle » devient « ce chiffre, il » (le mot « somme » n'y vaut plus, même cause) |
| Point 0 (mère) | préalable 1 | « Non levé à l'écriture de cette pièce » → non levé à l'écriture de la v2, **levé depuis par le mot de Lazar** (R-2822, 23:28 UTC : « il se recharge seul ») ; la phrase de R-2822 sur le relevé de facturation est citée telle quelle |
| Point 0 (mère) | préalable 6 | ajout : la pièce v3 et son compagnon doivent être commités par la mère avant le point 2 |

**Lecture de « cette pièce ».** Dans le corps ci-dessous, « cette pièce » désigne la v3, **sauf** : l'en-tête du
rédacteur de la v2 (son premier paragraphe), les §§ 5 et 6 (écarts et vérifications de la v2, faits en l'écrivant), et
**la commande ajoutée du point 1**, laissée identique comme demandé : elle vérifie `commandes-exactes-v2.md.sha256`, non
le compagnon de la v3. L'empreinte de la v3 se lit sur son compagnon ; le point 2 (arbre propre, après le commit du
préalable 6) garantit que la v3 commitée est celle du dépôt. Si la mère veut que le point 1 vérifie aussi la v3, c'est une
commande neuve : à décider, hors de cette pièce.

**Remarques non exigées de la vérification, et ce que j'en fais.** Aucune n'est portée, sauf ce que la mère a demandé :
- Couple 4 recommandé (clé absente entre deux tranches : nœud, rejeu sur mot de la mère) : **non porté** ; la ligne
  « rejouer la même tranche une seule fois » reste, latitude neuve signalée par la vérification (§ 2), à trancher par la mère.
- Couple 5 recommandé (clé retirée des variables gardées du point 5 bis) : **non porté** ; l'écart reste celui que la v2
  déclare (§ 5).
- Couple 6 recommandé : sa seconde moitié (citer le mot de Lazar sur le crédit, R-2822) est **portée, parce que la mère l'a
  demandé** ; sa première moitié (les rapports de vérification dans le commit) n'est **pas portée** dans le texte. Fait à
  savoir pour le point 2 : `git status --porcelain` n'est vide que si la mère a aussi commité les rapports de vérification
  de la v2 et de la v3 (et leurs compagnons) ; sinon le point 2 arrête, comme il le doit.
- Autres latitudes et réserves de la vérification (repli à `--envois-max 3` ; délai `DELAI_S` par opération de socket ;
  trace possible au point 5 bis ; sorties attendues du contrôle B à compter par 3 si le repli joue ; branche 401 jamais
  éprouvée contre l'amont) : **laissées telles quelles**, connues de la mère par la vérification.

**Vérifié par programme (hors réseau, 23:34 et 23:36 UTC)**, corps de la v3 contre la v2 à partir de sa ligne 3 : le seul bloc clos
(point 5 bis) est identique ; les 31 passages de commande entre accents graves sont les mêmes, en même nombre ; les 14
lignes de commande de la v2 sont présentes à l'identique ; aucun passage de la v2 n'a disparu ; passages ajoutés, tous
dans les remplacements ci-dessus : `bilan` (5), `envoyer`, `ValueError`, `max()`, `Refus`, `en_vol`,
`RE/commandes-exactes-v3.md`, `.sha256` ; dans cet en-tête, aucune commande à jouer (seule la mention de `git status --porcelain` du point 2). L'empreinte de la v2 est recalculée égale à
son compagnon avant et après l'écriture.

**Différentiel** (corps de la v2 à partir de sa ligne 3, contre le corps de la v3) :

```diff
--- commandes-exactes-v2.md (ligne 3 à la fin)
+++ commandes-exactes-v3.md (corps)
@@ -70,7 +70,9 @@
 Préalables restants (chacun écrit au registre avant le point 6 ; sinon le point 6 n'est pas joué) :
 1. **Crédit** : mot de Lazar consigné disant que le crédit du compte OpenAI couvre au moins 6,50 USD plus la marge des
    autres sessions qui tirent sur ce compte (deux épuisements déjà vus : 1er novembre, `credit_balance_exhausted` ; 14
-   novembre au matin, deux 429 `insufficient_quota`). **Non levé à l'écriture de cette pièce.** Aucun appel gratuit ne le
+   novembre au matin, deux 429 `insufficient_quota`). Non levé à l'écriture de la v2 ; **levé depuis par le mot de Lazar** (registre R-2822,
+   23:28 UTC : « il se recharge seul » ; rechargement automatique ; R-2822 ajoute : « le relevé de facturation reste à
+   faire avant le premier appel si l'outil le permet »). Aucun appel gratuit ne le
    prouve (le point 5 bis ne le prouve pas).
 2. **K3** : un mot de Lazar antérieur à `preparer` (R-2804, 22:32 UTC : tenu). **K7** :
    `( cd $DOS/attestations && sha256sum -c attestation-lecture-g1-v2.json.sha256 )` → `OK`.
@@ -85,6 +87,8 @@
    `export OPENAI_API_KEY=…`, jamais la valeur dans une commande, un fichier ou la conversation. Absente : nœud (la clé se
    demande par les outils de l'environnement, jamais en clair).
 6. **Cette pièce et les quatre rapports versés au dépôt** (commit de la mère), puis point 2 (arbre propre).
+   **La pièce v3 (`RE/commandes-exactes-v3.md` et son compagnon `.sha256`) doit être commitée par la mère avant le
+   point 2.**
 
 ### Point 1 — K1
 
@@ -203,7 +207,8 @@
 - **K4**, lu par programme (contrôle « B » ci-dessous, qui affiche des comptes et des booléens seulement) : `1 18 [] [] None`
   …, `True` ; `anomalies` vide ; modèle servi égal à la constante `MODELE_LECTEUR` de l'outil (le modèle de l'attestation) ;
   `palier_servi` = `flex` ; `reasoning_tokens ≤ completion_tokens ≤ 32768` ; `cout_usd ≤ pire_cas_usd` ; et, lu à part,
-  **`cout_usd ≤ 0,33`** (devis v2, § 3 ; attendu ≈ 0,158). Sinon : **rien de plus, nœud** (R-2804).
+  **`cout_usd ≤ 0,33`** (devis v2, § 3 ; attendu ≈ 0,158). Sinon : **rien de plus, nœud** (R-2804). De même pour le code de l'`envoyer` du point 6 : **tout code autre que 0
+  (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code : rien de plus, nœud**.
 
 **Contrôle B** (après chaque `envoyer`, jamais pendant) :
 
@@ -212,6 +217,10 @@
 Il affiche, dans l'ordre : appels clos, attendus (18), appels en vol, anomalies, motif d'arrêt, dépense comptée, plafond,
 prêt pour vérifier, toutes les clôtures conformes, coût le plus haut d'un appel.
 
+**S'il ne rend pas sa ligne** : s'il s'arrête sur une exception (`ValueError` : aucune clôture, cas d'un premier appel
+tué en vol, `max()` d'une suite vide, vérifié ; `Refus` : fichier sans clôture au journal), jouer `bilan` seul (la
+commande `bilan` du point 6) ; `bilan` en refus (code 2) ou `en_vol` non vide : dossier perdu, nœud.
+
 ### Point 7 — les 17 autres, **en tranches `--envois-max 6`, contrôle B entre chaque**
 
 Commande de chaque tranche : celle du point 6, avec `--envois-max 6` au lieu de `--envois-max 1` :
@@ -249,7 +258,7 @@
 | code **2**, message « `OPENAI_API_KEY` absente ou vide » ou « caractère hors de l'ASCII imprimable » | refusé **avant** tout journal et tout envoi : rien n'est parti ; rétablir la variable par son origine (préalable 5), puis rejouer **la même tranche une seule fois** |
 | code **2**, « appel sans clôture au journal » ou « lecture déjà arrêtée » | appel en vol (compté au pire cas, environ 1,09 USD) ou arrêt déjà consigné : **dossier unique perdu** (r6) ; contrôle B ; K6 ; nœud |
 | code **2**, autre message (manifeste, corps différent du manifeste, version) | nœud ; rien ne se relance |
-| **pas de code** (tâche tuée à la limite, coupure de la session, notification perdue) | aucun `envoyer` ; contrôle B quand plus rien ne tourne : `en_vol` non vide → appel en vol, dossier perdu, nœud ; `en_vol` vide, aucune anomalie, aucun arrêt → journal cohérent, mais **rien ne repart sans le mot de la mère** (la tranche n'a pas écrit son relevé) |
+| **tout autre code (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code** | aucun `envoyer` ; contrôle B quand plus rien ne tourne : `en_vol` non vide → appel en vol, dossier perdu, nœud ; `en_vol` vide, aucune anomalie, aucun arrêt → journal cohérent, mais **rien ne repart sans le mot de la mère** (la tranche n'a pas écrit son relevé) |
 
 ### Point 8 — K5
 
@@ -282,7 +291,8 @@
 
 ### Point 13 — dépense, rapport, phrase à Lazar
 
-- Inscrire la dépense sous GO-2026-11-13-06 (`registres/depenses.md`) : somme des `depense_comptee_usd` du dernier relevé ;
+- Inscrire la dépense sous GO-2026-11-13-06 (`registres/depenses.md`) : le `depense_comptee_usd` rendu par `bilan` (cumul du journal,
+  appel en vol compris) ; les relevés sont cumulatifs, on ne les additionne pas ;
   **la rapprocher de la console du fournisseur, qui fait foi** (prix Flex 5 / 0,5 / 25 repris de `prix-astra-v2.md`, non
   revérifiés chez le fournisseur) ; un écart de palier servi (compté au prix Flex, facturé autrement) se corrige à la main.
 - Rapporter avec le verdict : R7 retenu du hasard selon la chaîne, la valeur p de R7 seul (avec le p exact si elle est
@@ -296,8 +306,9 @@
 
 Jamais « supprimer ». Le dossier arrêté se **déplace** hors de `docs/` et `runs/` (R12 ; sinon la garde d'unicité le voit
 encore, ou la dépense passée disparaît du compte), sur mot de Lazar ; la nouvelle préparation déclare en
-`--depense-anterieure-usd` la **somme des `depense_comptee_usd`** des relevés du dossier arrêté (un refus Flex y est compté
-au pire cas : surestimation sans danger) ; l'outil ne peut pas vérifier cette somme, elle repose sur l'opérateur.
+`--depense-anterieure-usd` le **`depense_comptee_usd` rendu par `bilan`** sur le dossier arrêté (cumul du journal, appel
+en vol compris ; les relevés sont cumulatifs, on ne les additionne pas ; un refus Flex y est compté au pire cas :
+surestimation sans danger) ; l'outil ne peut pas vérifier ce chiffre, il repose sur l'opérateur.
 
 ## 4. Réserves déclarées
 
```

---

*Corps de la v2, couples portés (titre de la v2 remplacé par celui de la v3 ; tout le reste au caractère près, hors des
remplacements ci-dessus).*

Rédacteur neuf (modèle A), sous-agent de la session mère ; écrit le 14 novembre 2026 de 23:17 à 23:27 UTC (`date -u` :
23:17:26 au début, 23:22:47 avant l'écriture, 23:27 avant le scellement). Sous R-2804 et R-2818.
**Rien de ce qui suit n'a été joué par moi**, sauf trois épreuves hors réseau dites au § 6 (essais du point 3 ; contrôle
B sur le dossier de la v3.1 ; bloc du point 5 bis sous `unshare -n`). Aucun appel réseau, aucune clé lue, aucun texte de fiche ni d'envoi ouvert.

Cette pièce **remplace, pour l'opérateur, le § 6** de `RE/rapport-v1.md` ; le § 6 reste tel quel (R12). Elle porte les
corrections des quatre contrôles de la mère (`RE/controles-mere-v1/`, surtout les constats C1 à C7 de la critique de
complétude) et la décision R-2818. Chemins relatifs à la racine du dépôt ; `DOS=docs/notes/organisme-conception-propre-v1`,
`RE=$DOS/relecture-exploratoire-v2`, `OUT=$RE/lecture-classement-v3-2` (variables du shell, **non exportées**, à
redéfinir en tête de chaque commande : l'outil de commande de la session ne garde pas l'état du shell d'un appel à
l'autre, arrière-plan compris).

## 1. Pièces citées (empreintes vérifiées par programme contre leur compagnon `.sha256`, à 23:21 et 23:25 UTC : toutes égales)

| Pièce | sha256 |
|---|---|
| `RE/rapport-v1.md` (§ 6 d'origine) | `d454f3660acff70d9ac3766a284e0b56ac1196ac4d64f3cca3026dfb12d71cae` |
| `RE/controles-mere-v1/critique-completude-v1.md` | `ed2545c5ae769064407670cc5dd51aa0076c948a19744b426e90ae2d3926de49` |
| `RE/controles-mere-v1/revue-adverse-v1.md` | `ae30b758d91283ccb76613de584e3a888a067cbed4932f5127478e022f25be3d` |
| `RE/controles-mere-v1/controle-essais-et-bancs-v1.md` | `1cddce43901063e9f3e5642dec9729b6061a0119e8ac5b63857b1043240bda4f` |
| `RE/controles-mere-v1/controle-preparation-a-blanc-v1.md` | `b3bb92fe66258240f2d7b33f049badbd619308d55bb60def8b495cdb5e664e1f` |
| `RE/regle-v2-1.md` | `b955e7307e906dbdcf78123827d192bf2f0b4639f0194c94966fdccba5330434` |
| `RE/temoins-lecteur-v2.json` | `bb4f903f5a7fbe2366fb631afe708dcf93632e47c459acd86afbd425b93e295e` |
| `RE/temoins-hasard-v2-1.json` | `1b7973f38966a19ffc901bdb3eabd9e7df2af2c1aba8014dbda395cb56ba0fb0` |
| `RE/devis-v2.md` | `b412723e4a468c0cff6f8ad96b105b8e91ba27eed0ffc5faa35959c78beb915f` |
| `OUT/outil_lecteur_conception_propre_v3_2_1.py` | `65902da3052fd6a257e18a35c6ac49a62e0e8ce1d3cf4efa4287ead23d5fe04f` |
| `OUT/classer_conception_propre_v3_2_1.py` | `384211eedd58110ea679c3520d8313c38960d1265a5e3d97b1a865dd24ad42c4` |
| `OUT/essais_lecture_classement_v3_2_1.py` | `46374c03dd11c3999c81ef312024ff689a95ce2bcdc2e7a9e0387aa02bac1a52` |
| `RE/outils/essais_temoins_et_hasard_v2_1.py` | `6b64745d1f24a63c623b0664e73914a56cd45b3b0ac6109fbe3c2742a47db544` |
| `$DOS/attestations/attestation-lecture-g1-v2.json` | `4bfacd35e9e380497a32d7b51c01ec198daf277d9bb1acb823eeed02ebab3ba9` |
| fiches validées du run `20261113-235541-…-g1` (`copies/sortie--fiches-validees.json`, fichier non ouvert) | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| `$DOS/lecture-g1-v3-1/commandes-exactes-v1.md` (appel sans clé de la première lecture, 10:36:20) | `fd1269ac5614ef07a2edbc0c9b6fa839a7708255342333d36a658f6295a2617e` |
| `$DOS/lecture-g1-v3-1/journal-et-releve-v1.md` | `e5a62d29a76ffb3a5f2af069f31952da5da53d3c79d069ed1427fddd311a7ec3` |
| `$DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py` (point 12) | `95bc46c1972f91e9692f3bc28d5b8643d5957cc91cd8a39c63eb47f7240dcb44` |
| `$DOS/prix-astra-v2.md` (source des prix, `bf211a07` au K2) | `bf211a074868f49175bd59089a3082ec78da0d545850145ca27743b260ac78df` |

## 2. Ce qui change par rapport au § 6

| Point | § 6 de `rapport-v1.md` | Ici | Cause |
|---|---|---|---|
| 0 | décisions « à prendre » | décisions prises (R-2804, R-2818) ; préalables restants nommés, dont le **crédit** | R-2818 ; C2 (b), C8 |
| 2 | K8 et absence | **+ arbre git propre** (`git status --porcelain` vide) | C1 (6) ; m6 de la revue adverse |
| 3 | « → 247 passés » | **« 246 passés, 1 sauté »** sans le clone de l'orchestrateur (247 passés s'il est là) ; `-rs` ajouté | C1 (2), C3, C5 ; M2 de la revue adverse |
| 4 | commande seule | **jouée telle quelle, une seule fois, jamais à blanc hors du dépôt** | C1 (3) ; constat 1 du blanc |
| 5 bis | absent | **appel gratuit de la liste des modèles, sans clé**, même interpréteur, mêmes variables gardées qu'au point 6 | C2 (a) ; m4 de la revue adverse |
| 6 | premier appel seul | **commande inchangée** ; mode de lancement écrit (arrière-plan) ; K4 lu par programme | C1 (1) |
| 7 | 17 appels d'un seul tenant | **tranches `--envois-max 6`, `bilan` entre chaque**, durée bornée, un seul `envoyer` à la fois, conduite en cas d'arrêt | C1 (1), C1 (5) ; M1, m7 de la revue adverse |
| 9 | K6 avant la vérification | K6 gardé **et rejoué après le point 10** (point 10 bis) | C1 (4) ; m3 de la revue adverse |
| r6 | « supprimer `lecture-g1-v3-2/` » | **« déplacer hors de `docs/` et `runs/` »**, sous nœud | C1 (5) ; m2 de la revue adverse |
| 13 | inscrire la dépense | + rapprocher de la console du fournisseur ; phrase à Lazar sur le mandataire | C8 ; m3 de la revue adverse |

Le texte des commandes du § 6 aux points 1, 2 (K8), 4, 5, 6, 8, 9, 10, 11 et 12 est repris **à l'identique** (égalité
vérifiée par programme, § 6 de cette pièce). Les seules commandes neuves sont : `git status` (points 2 et 4), `-rs` au
point 3, l'appel du point 5 bis, le contrôle de `bilan` (points 6 à 8), `--envois-max 6` au point 7.

## 3. Commandes

### Point 0 — préalables (mère ; Lazar pour le crédit). **Aucune commande avant que tous tiennent.**

Décisions déjà prises, à ne pas rouvrir :
- **R-2804** (mots de Lazar, 22:32 UTC) : plafond **6,50 USD** (`RE/devis-v2.md`) sous le reste de **GO-2026-11-13-06**
  (cumul 9,347722 sur 21, reste 11,652278) ; **si le premier appel s'arrête : rien de plus, nœud** (dossier unique perdu,
  r6) ; attestation : **la v2 existante** (`4bfacd35…`), aucune v3 ; statut des sous-agents (M5) : les relecteurs lancés
  par la ligne de commande du client ne sont pas repris, les contrôles se font par des sous-agents de la mère ; « réserve du
  lecteur » (m5) sans objet.
- **R-2818** (contrôles rendus, 23:17 UTC) : **C4** — l'épreuve passée des valeurs attendues des témoins est **gardée comme
  information déclarée** ; **C6** — les trous d'essai sont **acceptés et déclarés** (code juste, rien sur la dépense) ;
  C1 — cette pièce ; C2 (a) — le point 5 bis ; **C2 (b) — crédit du compte OpenAI à confirmer par Lazar**.

Préalables restants (chacun écrit au registre avant le point 6 ; sinon le point 6 n'est pas joué) :
1. **Crédit** : mot de Lazar consigné disant que le crédit du compte OpenAI couvre au moins 6,50 USD plus la marge des
   autres sessions qui tirent sur ce compte (deux épuisements déjà vus : 1er novembre, `credit_balance_exhausted` ; 14
   novembre au matin, deux 429 `insufficient_quota`). Non levé à l'écriture de la v2 ; **levé depuis par le mot de Lazar** (registre R-2822,
   23:28 UTC : « il se recharge seul » ; rechargement automatique ; R-2822 ajoute : « le relevé de facturation reste à
   faire avant le premier appel si l'outil le permet »). Aucun appel gratuit ne le
   prouve (le point 5 bis ne le prouve pas).
2. **K3** : un mot de Lazar antérieur à `preparer` (R-2804, 22:32 UTC : tenu). **K7** :
   `( cd $DOS/attestations && sha256sum -c attestation-lecture-g1-v2.json.sha256 )` → `OK`.
3. **Ligne de GO sur `main` distant** (condition de GO-2026-11-14-12) : la mère s'assure, par son propre geste réseau, que
   `origin/main` porte R-2804, R-2818 et la ligne GO-2026-11-13-06 (par exemple `git grep -n '^| R-2804 ' origin/main --
   registres/decisions.md` et `git grep -n 'GO-2026-11-13-06' origin/main -- registres/go.md`, après mise à jour de
   `origin/main`). Le rédacteur ne l'a pas vérifié (aucun réseau).
4. **Quota de la session** qui portera les appels : lu par la mère avant le point 6 ; ne pas commencer si une coupure est
   probable avant la fin du point 8.
5. **Origine de la clé** : `OPENAI_API_KEY` est une variable de l'environnement de la session de l'opérateur, posée hors du
   dépôt. Présence vérifiée **par son nom seul** : `[ -n "${OPENAI_API_KEY+x}" ] && echo definie` → `definie`. Jamais
   `export OPENAI_API_KEY=…`, jamais la valeur dans une commande, un fichier ou la conversation. Absente : nœud (la clé se
   demande par les outils de l'environnement, jamais en clair).
6. **Cette pièce et les quatre rapports versés au dépôt** (commit de la mère), puis point 2 (arbre propre).
   **La pièce v3 (`RE/commandes-exactes-v3.md` et son compagnon `.sha256`) doit être commitée par la mère avant le
   point 2.**

### Point 1 — K1

`( cd $OUT && sha256sum -c outil_lecteur_conception_propre_v3_2_1.py.sha256 classer_conception_propre_v3_2_1.py.sha256 ) && ( cd $RE && sha256sum -c regle-v2-1.md.sha256 temoins-lecteur-v2.json.sha256 temoins-hasard-v2-1.json.sha256 devis-v2.md.sha256 )`
→ six `OK`, code 0. Ajouter : `( cd $RE && sha256sum -c commandes-exactes-v2.md.sha256 )` → `OK` (cette pièce).

### Point 2 — K8 (avant) et arbre git propre

`find docs runs \( -name 'manifeste-envois-v3*.json' -o -name 'manifeste-relecture-v3*.json' \)` → une seule ligne,
`$DOS/lecture-g1-v3-1/envois/manifeste-envois-v3-1.json` ; `test ! -e $DOS/lecture-g1-v3-2 && echo absent` → `absent` ;
**`git status --porcelain`** → aucune ligne (cette pièce et les quatre rapports déjà commités). Tout écart : arrêt.

### Point 3 — essais (hors réseau)

Avant : `test -e /home/user/lciric/ideation-organism/orchestrator/pole/ideation_v2.py && echo clone-present || echo clone-absent`.

`PYTHONDONTWRITEBYTECODE=1 unshare -n .venv/bin/python -B -m pytest -q -rs -p no:cacheprovider $OUT/essais_lecture_classement_v3_2_1.py $RE/outils/essais_temoins_et_hasard_v2_1.py`

→ **clone absent : `246 passed, 1 skipped`**, et une seule ligne `SKIPPED [1] …/essais_lecture_classement_v3_2_1.py:490:
clone de l'orchestrateur absent`. **Clone présent : `247 passed`.** Toute autre issue (un échec, un autre essai sauté, un
autre compte) : arrêt, nœud — on ne passe jamais outre un écart de compte.

Pourquoi : 247 essais collectés (229 outil et classement, 18 témoins et générateur) ; l'essai
`test_normalisation_egale_a_celle_de_l_orchestrateur` compare la normalisation typographique de l'outil à celle du clone de
l'orchestrateur et se saute si ce clone manque (il manque dans les sessions des contrôleurs et dans la mienne). Ce n'est pas
une panne. Cette normalisation **fixe la vue servie au lecteur** (C3 : la revue adverse a raison) ; le risque reste faible
(l'essai a passé chez le préparateur, 229 passés sans saut à 13:08 UTC ; la fonction est dans les 50 objets comparés à la
v3.1 qui a servi la première lecture), mais l'égalité avec l'orchestrateur **n'a été rejouée par aucun tiers** (réserve C3).

### Point 4 — préparation : **jouée telle quelle, une seule fois, sans blanc hors du dépôt**

`.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py preparer --fiches runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json --attestation $DOS/attestations/attestation-lecture-g1-v2.json --sortie $DOS/lecture-g1-v3-2/envois --effort medium --palier flex --plafond-usd 6.5 --depense-anterieure-usd 0`

→ `"pile": 43`, `"lots": [5, 5, 5, 5, 5, 5, 5, 4, 4]`, `"appels": 18`, `"palier": "flex"`, prix 5,0 / 0,5 / 25,0,
`"pire_cas_total_usd": 19.73713`, `"plafond_usd": 6.5`, `"appels_surs_au_pire_cas": 5`, code 0 ; puis
`git status --porcelain` → une seule ligne, `?? docs/notes/organisme-conception-propre-v1/lecture-g1-v3-2/`.

- **Aucun blanc par l'opérateur** : l'outil refuse tout `--sortie` autre que le dossier fixe (garde C6, code 2, rien
  d'écrit) ; ne pas tenter de le contourner. Le blanc a déjà été fait par le contrôleur de la préparation, par l'option
  `--racine` sur une racine temporaire hors du dépôt : valeurs ci-dessus retrouvées à l'identique, et K2 aussi
  (`b3bb92fe…`, constats 1 à 3). Limite de ce blanc : `verifier_unicite` n'a pas été éprouvée contre le dépôt entier (le
  point 2 y supplée).
- Code 2 sans dossier créé (`test ! -e $DOS/lecture-g1-v3-2`) : rien n'est écrit ; arrêt, message (texte fixe) rapporté à
  la mère ; pas de second essai sans son mot. Dossier créé puis échec, ou valeurs autres : arrêt ; le dossier reste en
  place ; toute seconde préparation est un **nœud** (point 14).

### Point 5 — K2, puis K8

`.venv/bin/python -I -B -c "import json; m=json.load(open('$DOS/lecture-g1-v3-2/envois/manifeste-relecture-v3-2.json')); g=m['garde_depense']; p=g['prix_usd_par_million']; print(m['version'], m['palier'], m['lecteur']['reasoning_effort'], m['lecteur']['service_tier'], (p['entree'], p['cache'], p['sortie']), g['plafond_usd'], g['depense_anterieure_usd'], len(g['envois']), 'bf211a07' in p['source'], m['pieces']['regle']['sha256'][:8], m['pieces']['temoins_lecteur']['sha256'][:8], m['pieces']['temoins_hasard']['sha256'][:8])"`
→ `outil-lecteur-conception-propre-v3-2-1 flex medium flex (5.0, 0.5, 25.0) 6.5 0.0 18 True b955e730 bb4f903f 1b7973f3` ;
puis K8 (commande du point 2) → deux lignes (manifeste v3.1 et `manifeste-relecture-v3-2.json`).

### Point 5 bis (neuf) — appel gratuit de la liste des modèles d'OpenAI, **sans clé**

Même interpréteur (`.venv/bin/python -I -B`), même sous-shell et **mêmes variables gardées** qu'au point 6 (la clé reste
dans l'environnement réduit, comme au point 6, mais le programme **ne la lit pas** et n'envoie aucun en-tête
d'autorisation) ; même construction du transport que `transport_reel` de l'outil (contexte TLS tiré de `SSL_CERT_FILE`,
mandataire de l'environnement par `urllib`, aucune redirection suivie). Lancé au premier plan (délai 60 s dans le
programme, sous le délai de la commande). **Rien n'est écrit sur disque ; seuls le statut et le type d'erreur sont
affichés** (ni corps, ni en-têtes, ni message d'exception : le type seul, comme l'outil).

```
( for v in $(compgen -e); do case $v in PATH|HOME|HTTPS_PROXY|https_proxy|SSL_CERT_FILE|OPENAI_API_KEY) ;; *) unset "$v";; esac; done; exec .venv/bin/python -I -B -c "
import json, os, ssl, urllib.error, urllib.request
ca = os.environ.get('SSL_CERT_FILE')
ctx = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
class SansRedirection(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None
op = urllib.request.build_opener(SansRedirection, urllib.request.HTTPSHandler(context=ctx))
req = urllib.request.Request('https://api.openai.com/v1/models', method='GET', headers={'Accept': 'application/json'})
try:
    with op.open(req, timeout=60) as r:
        st, corps = r.status, r.read(65536)
except urllib.error.HTTPError as e:
    st, corps = e.code, e.read(65536)
except Exception as e:
    print('EXCEPTION', type(e).__name__)
    raise SystemExit(5)
try:
    err = json.loads(corps).get('error')
    t = err.get('type') if isinstance(err, dict) else None
except Exception:
    t = 'corps-non-JSON'
print(st, t)
raise SystemExit(0 if st == 401 and isinstance(t, str) and t != 'corps-non-JSON' else 6)
" )
```

**Réponse attendue** : `401` suivi du type d'erreur que rend OpenAI dans son objet `error` (probablement
`invalid_request_error` ; le type exact est une information, non une condition), code 0. Relever `date -u` avant et après.

**Lecture** : un refus d'authentification **venu d'OpenAI** (statut 401, corps JSON portant un objet `error`) est lu comme
la **preuve de la route et du chiffrement** pour ce chemin : le mandataire de la session laisse passer `api.openai.com`, la
chaîne de certificats vue par le client se vérifie avec `SSL_CERT_FILE`, et c'est bien OpenAI qui répond au bout. Ce qu'il
**ne prouve pas** : le crédit (préalable 1), l'accès au palier Flex et au modèle de l'attestation, l'acceptation des
paramètres, un `POST` de la taille réelle, le délai de 1 800 s. Et le chiffrement n'est pas de bout en bout : le mandataire
**re-termine TLS** et voit l'en-tête d'autorisation du point 6 (phrase à Lazar, point 13).

**Tout autre résultat : le point 6 n'est pas joué, nœud** — en particulier : `200` (le mandataire injecte lui-même un
identifiant pour cet hôte : la clé du point 6 ne serait pas la seule en jeu) ; `403`, `407` ou `corps-non-JSON` (refus du
mandataire, hôte non permis) ; `EXCEPTION SSLError` ou `URLError` (chaîne de certificats, route) ; `429` ou autre statut.
On ne change ni l'environnement, ni les hôtes permis, ni le certificat soi-même : c'est un geste soumis à l'accord de Lazar.

### Point 6 — premier appel seul (commande inchangée)

`( for v in $(compgen -e); do case $v in PATH|HOME|HTTPS_PROXY|https_proxy|SSL_CERT_FILE|OPENAI_API_KEY) ;; *) unset "$v";; esac; done; exec .venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py envoyer --envois $DOS/lecture-g1-v3-2/envois --envois-max 1 )`

puis `.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py bilan --envois $DOS/lecture-g1-v3-2/envois`.

- **Mode de lancement** (seul ajout) : en **arrière-plan** de l'outil de commande de la session
  (`run_in_background: true`, `timeout: 7200000`), attente de la notification de fin et de son code ; `date -u` relevé juste
  avant et juste après. Borne : un appel dure au plus le délai de l'outil, `DELAI_S = 1800` s, sous la limite de 7 200 s
  d'une commande d'arrière-plan (au premier plan, 600 s au plus : insuffisant au pire cas). Observé à la première lecture :
  22 à 63 s par appel.
- **K4**, lu par programme (contrôle « B » ci-dessous, qui affiche des comptes et des booléens seulement) : `1 18 [] [] None`
  …, `True` ; `anomalies` vide ; modèle servi égal à la constante `MODELE_LECTEUR` de l'outil (le modèle de l'attestation) ;
  `palier_servi` = `flex` ; `reasoning_tokens ≤ completion_tokens ≤ 32768` ; `cout_usd ≤ pire_cas_usd` ; et, lu à part,
  **`cout_usd ≤ 0,33`** (devis v2, § 3 ; attendu ≈ 0,158). Sinon : **rien de plus, nœud** (R-2804). De même pour le code de l'`envoyer` du point 6 : **tout code autre que 0
  (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code : rien de plus, nœud**.

**Contrôle B** (après chaque `envoyer`, jamais pendant) :

`.venv/bin/python -I -B -c "import importlib.util as u; s=u.spec_from_file_location('o', '$OUT/outil_lecteur_conception_propre_v3_2_1.py'); o=u.module_from_spec(s); s.loader.exec_module(o); b=o.bilan('$DOS/lecture-g1-v3-2/envois'); c=b['clotures']; t=lambda x, k: (x['jetons'] or {}).get(k); ok=[x['statut'] == 200 and x['modele_servi'] == o.MODELE_LECTEUR and x['palier_servi'] == 'flex' and x['finish_reason'] == 'stop' and not x['anomalies'] and x['cout_usd'] <= x['pire_cas_usd'] and isinstance(t(x, 'completion_tokens'), int) and (t(x, 'reasoning_tokens') or 0) <= t(x, 'completion_tokens') <= 32768 for x in c]; print(b['clos'], b['attendus'], b['en_vol'], b['anomalies'], b['arret'], b['depense_comptee_usd'], b['plafond_usd'], b['pret_pour_verifier'], all(ok), max(x['cout_usd'] for x in c))"`

Il affiche, dans l'ordre : appels clos, attendus (18), appels en vol, anomalies, motif d'arrêt, dépense comptée, plafond,
prêt pour vérifier, toutes les clôtures conformes, coût le plus haut d'un appel.

**S'il ne rend pas sa ligne** : s'il s'arrête sur une exception (`ValueError` : aucune clôture, cas d'un premier appel
tué en vol, `max()` d'une suite vide, vérifié ; `Refus` : fichier sans clôture au journal), jouer `bilan` seul (la
commande `bilan` du point 6) ; `bilan` en refus (code 2) ou `en_vol` non vide : dossier perdu, nœud.

### Point 7 — les 17 autres, **en tranches `--envois-max 6`, contrôle B entre chaque**

Commande de chaque tranche : celle du point 6, avec `--envois-max 6` au lieu de `--envois-max 1` :

`( for v in $(compgen -e); do case $v in PATH|HOME|HTTPS_PROXY|https_proxy|SSL_CERT_FILE|OPENAI_API_KEY) ;; *) unset "$v";; esac; done; exec .venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py envoyer --envois $DOS/lecture-g1-v3-2/envois --envois-max 6 )`

- **Trois tranches** : 6, 6, puis 5 (la troisième finit d'elle-même, issue `fait`). Sortie attendue de chaque tranche : le
  relevé en JSON, `"issue": "pause"` (tranches 1 et 2) ou `"fait"` (tranche 3), code **0** (l'outil rend 0 pour « fait »
  et pour la pause de `--envois-max`). Contrôle B attendu après chaque tranche : `7 18 [] [] None … 6.5 False True …`, puis
  `13 18 [] [] None … 6.5 False True …`, puis `18 18 [] [] None … 6.5 True True …`.
- **Lancement** : chaque tranche en arrière-plan (`run_in_background: true`, `timeout: 7200000`), `date -u` juste avant et
  juste après la notification de fin ; la clé est relue par l'outil à chaque tranche (et retirée de son environnement).
- **Durée bornée sous la limite d'une commande** : limite d'une commande d'arrière-plan 7 200 s (au premier plan 600 s, d'où
  l'arrière-plan). Première lecture : 17 appels en 578 s (22 à 63 s, moyenne 34 s, revue adverse M1) ; pile plus lourde
  d'environ 12 % : une tranche de 6 prend environ 230 s attendues, **environ 425 s au pire observé** (6 × 63 s × 1,12),
  soit dix-sept fois moins que la limite. Borne dure de l'outil : un appel s'achève au plus au délai de 1 800 s (au-delà,
  exception de transport, appel compté au pire cas, anomalie, **la tranche s'arrête** : un seul appel par tranche peut
  l'atteindre). Une tranche de 6 n'est donc **pas bornée en dur** sous 7 200 s (cinq appels à 1 799 s et un sixième en
  dépasseraient la limite) ; une tranche de 3 l'est (3 × 1 800 = 5 400 s). D'où la **règle de repli** : si le premier
  appel (point 6) ou la moyenne d'une tranche dépasse **300 s par appel** (cinq fois le pire observé ; durée lue sur les
  deux `date -u`), toutes les tranches suivantes passent à `--envois-max 3`, qui reste sous la limite au pire cas.
- **Un seul `envoyer` à la fois** (l'outil n'a pas de verrou de fichier) : la tranche suivante ne part qu'après la
  notification de fin de la précédente **et** un contrôle B montrant `en_vol` vide ; jamais deux tâches d'arrière-plan
  `envoyer` ensemble ; jamais `bilan` ni le contrôle B pendant qu'un `envoyer` tourne ; jamais un `envoyer` lancé d'une
  autre session ; un `envoyer` en cours ne s'arrête pas (s'il le fallait : par son PID seul, R10, sur mot de la mère, en
  sachant que le dossier est alors perdu).

**Si une tranche s'arrête** (lire d'abord le code, puis le contrôle B) :

| Issue | Ce qu'on fait |
|---|---|
| code 0, `"issue": "pause"` | normal : contrôle B, puis tranche suivante |
| code 0, `"issue": "fait"` | les 18 sont clos : point 8 |
| code **3** (anomalie : statut non 200, coupure, délai, modèle ou palier autre, fin autre que `stop`, usage incohérent, clé dans la réponse) ou code **4** (plafond : dépense comptée plus pire cas au-delà de 6,50, ou nombre d'appels) | **aucun `envoyer` de plus** (l'outil refuserait : « lecture déjà arrêtée ») ; contrôle B ; point 9 (K6) ; rapport à la mère : **lecture incomplète (E2 v2)**, réponses déjà reçues gardées, relevé scellé ; `verifier` et le classement (gratuits) ne se jouent que sur son mot et rendent alors « E2 v2, lecture incomplète » ; **nœud** ; jamais de seconde préparation sans lui (point 14). Un arrêt au plafond par une moyenne au-delà d'environ 0,32 USD par appel est sûr pour l'argent ; il se déclare tel quel |
| code **2**, message « `OPENAI_API_KEY` absente ou vide » ou « caractère hors de l'ASCII imprimable » | refusé **avant** tout journal et tout envoi : rien n'est parti ; rétablir la variable par son origine (préalable 5), puis rejouer **la même tranche une seule fois** |
| code **2**, « appel sans clôture au journal » ou « lecture déjà arrêtée » | appel en vol (compté au pire cas, environ 1,09 USD) ou arrêt déjà consigné : **dossier unique perdu** (r6) ; contrôle B ; K6 ; nœud |
| code **2**, autre message (manifeste, corps différent du manifeste, version) | nœud ; rien ne se relance |
| **tout autre code (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code** | aucun `envoyer` ; contrôle B quand plus rien ne tourne : `en_vol` non vide → appel en vol, dossier perdu, nœud ; `en_vol` vide, aucune anomalie, aucun arrêt → journal cohérent, mais **rien ne repart sans le mot de la mère** (la tranche n'a pas écrit son relevé) |

### Point 8 — K5

`.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py bilan --envois $DOS/lecture-g1-v3-2/envois` →
`pret_pour_verifier: true`, `clos: 18`, `en_vol: []` (et le contrôle B : `18 18 [] [] None … True True …`).

### Point 9 — K6 (clé lue par son nom, un booléen seul)

`.venv/bin/python -I -B -c "import importlib.util as u, os, pathlib; s=u.spec_from_file_location('o', '$OUT/outil_lecteur_conception_propre_v3_2_1.py'); o=u.module_from_spec(s); s.loader.exec_module(o); c=os.environ['OPENAI_API_KEY']; print(any(o.contient_cle(p.read_bytes(), c) for p in pathlib.Path('$DOS/lecture-g1-v3-2').rglob('*') if p.is_file()))"` → `False`.

### Point 10 — vérification et classement

`.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py verifier --envois $DOS/lecture-g1-v3-2/envois`
puis `.venv/bin/python -I -B $OUT/classer_conception_propre_v3_2_1.py --envois $DOS/lecture-g1-v3-2/envois --sortie $DOS/lecture-g1-v3-2/classement`.

### Point 10 bis (neuf) — K6 rejoué après le point 10

La commande du point 9, **à l'identique**, sur `lecture-g1-v3-2` entier, qui contient alors les lectures vérifiées et le
classement (ils reprennent des passages des réponses) → `False`. Si l'opérateur garde des sorties capturées hors du dépôt,
les balayer de même, ou les détruire par chemin exact. Puis, avant tout commit, `git status --porcelain` → la seule ligne
`?? docs/notes/organisme-conception-propre-v1/lecture-g1-v3-2/` (et le rapport de l'opérateur, s'il est écrit).

### Point 11 — K9 (avant de lire le verdict ; comptes seuls)

`.venv/bin/python -I -B -c "import json; print([sum(f['N']['motif'] == 'valeur de N illisible' for f in json.load(open('$DOS/lecture-g1-v3-2/classement/lecture-verifiee-' + L + '-v3-2.json'))['fiches'].values()) for L in ('L1', 'L2')])"` → `[0, 0]` ; sinon le dire au verdict.

### Point 12 — la v3.1 reste vérifiable

`.venv/bin/python -I -B $DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py bilan --envois $DOS/lecture-g1-v3-1/envois` → code 0.

### Point 13 — dépense, rapport, phrase à Lazar

- Inscrire la dépense sous GO-2026-11-13-06 (`registres/depenses.md`) : le `depense_comptee_usd` rendu par `bilan` (cumul du journal,
  appel en vol compris) ; les relevés sont cumulatifs, on ne les additionne pas ;
  **la rapprocher de la console du fournisseur, qui fait foi** (prix Flex 5 / 0,5 / 25 repris de `prix-astra-v2.md`, non
  revérifiés chez le fournisseur) ; un écart de palier servi (compté au prix Flex, facturé autrement) se corrige à la main.
- Rapporter avec le verdict : R7 retenu du hasard selon la chaîne, la valeur p de R7 seul (avec le p exact si elle est
  voisine du seuil : la décision de séparation est un test de Monte-Carlo, la table de la règle est exacte, m5 de la revue
  adverse), la mention « exploratoire, aucune désignation » (le code écrit « règle v2 » pour la v2.1 : écart de forme).
- **Phrase à Lazar** : « Le mandataire de sortie de la session re-termine TLS : il voit l'en-tête d'autorisation, donc la
  clé d'OpenAI, à chaque appel ; le commentaire de `transport_reel` (« jamais au mandataire ») est faux dans cette
  session. Rien dans la marche ne l'empêche. »

### Point 14 — seconde préparation (seulement sur nœud de Lazar)

Jamais « supprimer ». Le dossier arrêté se **déplace** hors de `docs/` et `runs/` (R12 ; sinon la garde d'unicité le voit
encore, ou la dépense passée disparaît du compte), sur mot de Lazar ; la nouvelle préparation déclare en
`--depense-anterieure-usd` le **`depense_comptee_usd` rendu par `bilan`** sur le dossier arrêté (cumul du journal, appel
en vol compris ; les relevés sont cumulatifs, on ne les additionne pas ; un refus Flex y est compté au pire cas :
surestimation sans danger) ; l'outil ne peut pas vérifier ce chiffre, il repose sur l'opérateur.

## 4. Réserves déclarées

- **C3** — Essai sauté sans le clone : la normalisation typographique fixe la vue servie au lecteur ; égalité avec
  l'orchestrateur jouée chez le préparateur seulement (13:08 UTC), par aucun tiers. Faible risque, déclaré.
- **C4** (décidé, R-2818) — Les valeurs attendues des témoins du lecteur ont été éprouvées par des relecteurs lancés par la
  ligne de commande du client (tours 1 et 2), voie que R-2759 et R-2804 disent « non reprise » ; l'épreuve est **gardée comme
  information déclarée**. La phrase de la règle v2.1 « aucun appel payant (sous-agents de la session) » reste dans la règle
  (épinglée par l'outil) ; elle se lit comme le précise le rapport, § 4, point 3.
- **C6** (décidé, R-2818) — Le « tout tué » du banc v3.2.1 repose, pour les gardes de dépense, d'arrêt, de modèle, de palier
  et de dossier existant, sur un essai de texte (arbre syntaxique comparé à la v3.1). Trous d'essai réels, **acceptés et
  déclarés** : codes de sortie de `envoyer` (que le point 7 lit), `--envois-max 0`, compagnon `.sha256` seul, « lisibilité
  sans complétude » (une lecture incomplète classée lisible : plus probable si un arrêt survient en cours de point 7 ; à
  vérifier à la main au verdict dans ce cas). Le code est juste à la lecture ; le trou est dans les essais. La condition de
  la contre-lecture « 0 mutant vivant » **n'est pas tenue à la lettre** : 2 survivants au banc du générateur (« pièces
  servies oubliées », équivalent ; « phrases par fiche non contrôlées », trou d'essai confirmé) et 2 inapplicables à celui
  de l'outil.
- **C7** — La chaîne d'après l'envoi (`verifier`, classement) n'a jamais été jouée à la taille réelle (43 fiches, 18
  réponses) ; aucun contrôleur ne l'a rejouée contre un serveur local. Si le classement échoue après la dépense, les réponses
  restent gardées et l'argent n'est pas perdu, mais un classement neuf serait à écrire (R12). Répétition générale locale,
  gratuite, recommandée par la critique, **non faite** à l'écriture de cette pièce.
- **C2 (b)** — Crédit non prouvé par le point 5 bis ; tant que Lazar ne l'a pas confirmé, le point 6 ne part pas.
- Restent vraies, du § 7 du rapport : r2, r3, r4, r7, r8, r9 (à écrire au rapport final) ; r5 (étiquettes non comparées à
  la première lecture par un tiers) ; r6 (premier appel arrêté : dossier unique perdu) ; reprise invisible d'un `POST` par
  le mandataire, non comptée par l'outil, non éprouvée.

## 5. Écarts de cette pièce

- **Point 5 bis avec la clé dans l'environnement** : la première lecture avait fait son appel sans clé « environnement
  réduit sans la clé » (`fd1269ac…`) ; ici, sur la demande reçue, les variables gardées sont **les mêmes qu'au point 6**
  (clé comprise, jamais lue par le programme, aucun en-tête d'autorisation), pour que la preuve de route vaille pour
  l'environnement exact du point 6.
- **Point 6** : commande inchangée, mais mode de lancement imposé (arrière-plan) et K4 lu par programme ; le K4 du § 6
  nommait le modèle par son identifiant, ici remplacé par la constante `MODELE_LECTEUR` de l'outil (même valeur, aucun
  identifiant écrit).
- **Point 7** : la règle de repli à `--envois-max 3` est un ajout du rédacteur, parce qu'une tranche de 6 n'est bornée sous
  la limite que par les durées observées, non par l'outil.
- **Point 3** : `-rs` ajouté (affiche la raison du saut).
- Point « délai d'au moins 300 s au point 6 » de la critique : couvert par l'arrière-plan (7 200 s).

## 6. Vérifications faites en écrivant (hors réseau, rien d'écrit dans le dépôt hors cette pièce et son compagnon)

- **Empreintes** des 19 pièces du § 1 : recalculées et comparées à leur compagnon, toutes égales ; puis les 26 empreintes
  et préfixes cités dans cette pièce rapprochés par programme de la pièce qu'ils nomment : 26 `OK`, aucun écart, aucun
  préfixe ambigu (hors `c8a6e7d7`, commit, vérifié par `git cat-file -t`).
- **Point 3** joué à 23:22 UTC sous `unshare -n`, avec `-rs` : `246 passed, 1 skipped in 38.90s`, saut unique à la ligne
  490 (« clone de l'orchestrateur absent ») ; clone absent ici ; `git status` inchangé.
- **Contrôle B** éprouvé sur le dossier de la première lecture avec l'outil v3.1 (même `bilan`, même constante) sous
  `unshare -n` : `18 18 [] [] None 2.556635 14.2 True True 0.184525`, code 0, rien d'écrit.
- **Point 5 bis** : le bloc de code extrait de cette pièce par programme et joué **sans réseau** (`unshare -n`) : sortie
  `EXCEPTION URLError`, code 5, rien d'autre affiché, rien d'écrit. La syntaxe et la branche d'exception sont donc
  éprouvées ; **la branche 401 et la route elle-même ne le sont pas** (elles exigent le réseau).
- **Égalité de texte** : chaque commande du § 6 de plus de 40 caractères cherchée par programme dans cette pièce : toutes
  présentes à l'identique, sauf celle du point 3 (égale à celle du § 6 avec `-rs` ajouté) ; la commande du point 7 est
  celle du point 6 où `--envois-max 1` devient `--envois-max 6` (vérifié), la commande du point 6 figure une seule fois.
- `lecture-g1-v3-2` : absent à 23:21 UTC. Arbre git : propre avant cette pièce (tête alors `c8a6e7d7`) ; à 23:25 UTC,
  seule cette pièce est non suivie : le point 2 exige son commit par la mère.
