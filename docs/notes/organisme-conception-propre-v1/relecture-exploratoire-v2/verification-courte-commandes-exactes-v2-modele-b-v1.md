# Vérification courte de « commandes exactes v2 » — lecteur neuf (modèle B) — v1

Début : 2026-11-14 23:27:00 UTC ; fin : 2026-11-14 23:37 UTC (`date -u`, relevée avant l'écriture).
Lecteur neuf, sous-agent ; n'a écrit ni la pièce, ni l'outil, ni les contrôles. Chemins relatifs à la racine ;
`DOS=docs/notes/organisme-conception-propre-v1`, `RE=$DOS/relecture-exploratoire-v2`, `OUT=$RE/lecture-classement-v3-2`.

Pièce jugée : `RE/commandes-exactes-v2.md`, `bd259d2c197414959cd03a119db0cbe25eedcd2238ff00aa2e3cd6fd83ffbc51`
(recalculée, égale au compagnon). Contre : `RE/rapport-v1.md` § 6 (`d454f366…`), les quatre rapports de
`RE/controles-mere-v1/` (quatre compagnons `OK`), et l'outil `OUT/outil_lecteur_conception_propre_v3_2_1.py`
(`65902da3…`, fonctions `lire_cle`, `transport_reel`, `lire_journal`, `bilan`, `envoyer`, `main` lues ligne à ligne).

## Verdict

**Feu possible après corrections.** Rien dans la pièce ne permet de dépasser 6,50 USD, d'afficher la clé ou de perdre une
réponse payée en silence : ces trois garanties sont tenues par l'outil, et la pièce ne les affaiblit nulle part. Les
corrections de C1 (six points) et de C2 (a) sont toutes portées. Mais la conduite en cas d'arrêt, que la pièce ajoute, a
trois trous de texte (couples 1 à 3) : aucun ne touche l'argent, tous touchent ce que l'opérateur lit et fait au moment
où quelque chose casse. Ils se corrigent en quelques lignes (pièce v3, ou erratum scellé cité dans l'ordre de marche).
Trois autres couples sont recommandés, non exigés.

## Ce que j'ai fait, et pas fait

- Égalité de texte, par programme : les commandes du § 6 de plus de 40 caractères sont toutes dans la pièce à l'identique,
  sauf celle du point 3 (`-rs` ajouté, déclaré) ; la commande du point 7 est celle du point 6 avec `--envois-max 6` ;
  l'en-tête du bloc 5 bis (boucle de retrait des variables) est celui du point 6, caractère pour caractère.
- Point 3 rejoué sous `unshare -n` à 23:29 UTC : `246 passed, 1 skipped in 42.46s`, un seul saut, ligne 490, « clone de
  l'orchestrateur absent » ; clone absent ici. Égal à l'attendu de la pièce.
- Bloc 5 bis extrait de la pièce par programme : syntaxe du shell et de Python bonnes ; dans le code Python, aucun
  guillemet double, dollar, accent grave ni barre oblique inverse (le bloc tient donc entre guillemets doubles). Joué sous
  `unshare -n`, **la clé retirée de l'environnement de mon épreuve** : `EXCEPTION URLError`, code 5. Puis, toujours sous
  `unshare -n`, contre un faux serveur sur la boucle locale (adresse seule remplacée, mandataire retiré) : 401 et objet
  `error` typé → `401 invalid_request_error`, code 0 ; 200 → `200 None`, code 6 ; 403 non JSON, 429, 401 sans objet
  `error`, 401 à corps en liste, 302 (non suivie) → code 6. En-têtes reçus par le faux serveur : `accept`,
  `accept-encoding`, `connection`, `host`, `user-agent` ; **aucun en-tête d'autorisation**.
- Contrôle B rejoué sur la première lecture (outil v3.1, sous `unshare -n`) : `18 18 [] [] None 2.556635 14.2 True True
  0.184525`. Durées de la première lecture relues au journal (heures seules) : 18 appels de 22 à 63 s, moyenne 33,8 s ;
  les 17 derniers de 10:38:35 à 10:48:13, soit 578 s. Égal à ce que dit la pièce.
- Jamais fait : `envoyer`, appel réseau, lecture ou affichage d'une clé, lecture d'un texte de fiche ou d'envoi. Aucun
  refus de permission ni du classifieur. `lecture-g1-v3-2` absent avant et après. Écrit dans le dépôt : ce rapport et son
  compagnon, rien d'autre ; fichiers d'épreuve dans le dossier temporaire de la session.

## 1. C1 et C2 (a) : portées ?

| Exigence | Dans la pièce | Jugement |
|---|---|---|
| C1 (1) point 7 : arrière-plan ou tranches de 6 avec `bilan` entre chaque ; délai d'au moins 300 s au point 6 | point 7 : tranches de 6 **et** arrière-plan (7 200 s), contrôle B (qui appelle `bilan`) entre chaque ; point 6 en arrière-plan | portée, plus stricte |
| C1 (2) point 3 : « 247, ou 246 et 1 sauté sans le clone » | point 3, avec épreuve de présence du clone et `-rs` | portée (rejouée) |
| C1 (3) point 4 : pas de blanc hors du dépôt ; lecture du blanc déclarée | point 4 | portée |
| C1 (4) K6 après le point 10 ; origine de la clé ; phrase à Lazar | point 10 bis ; préalable 5 ; point 13 | portée |
| C1 (5) un seul `envoyer` ; seconde préparation « déplacer », sous nœud, somme en dépense antérieure | point 7 ; point 14 | portée (voir couple 3 sur « somme ») |
| C1 (6) arbre git propre ; « 0 mutant vivant » non tenu, dit | point 2 ; § 4, C6 | portée |
| C2 (a) appel gratuit de la liste des modèles, sans clé, dans la session des appels | point 5 bis, avant le point 6 | portée ; écart déclaré (clé gardée dans l'environnement, jamais lue) |

## 2. Rien d'autre ne change le fond, la dépense, l'arrêt ?

- **Fond** : préparation, vérification, classement, K1, K2, K5, K6, K8, K9 : texte identique au § 6. K4 : mêmes conditions ;
  le modèle est comparé à la constante de l'outil au lieu d'un nom écrit (même valeur). Le contrôle B ajoute statut 200 et
  fin `stop`, déjà impliqués par « aucune anomalie » : rien de plus lâche.
- **Dépense** : plafond 6,5, dépense antérieure 0, palier flex, effort medium : inchangés. Les tranches ne changent pas la
  garde (plafond revérifié avant chaque appel sur le journal relu). Le point 5 bis ne coûte rien (section 3).
- **Arrêt** : les codes de la table du point 7 sont ceux de l'outil (`fait` et `pause` 0, anomalie 3, plafond 4, refus 2 ;
  messages cités exacts). Deux latitudes neuves, non décidées par la mère : le rejeu « une seule fois » d'une tranche
  refusée pour clé absente (sans danger : refus avant tout journal ; mais voir couple 4) et le repli à
  `--envois-max 3` (déclaré, plus prudent). Trous : couples 1 et 2.

## 3. L'appel gratuit sans clé

- **Dépenser : non.** Un `GET` de la liste des modèles, sans corps ; aucun en-tête d'autorisation (vérifié sur le faux
  serveur). Si le mandataire injectait lui-même un identifiant pour cet hôte, la réponse serait 200 : la liste des modèles
  n'est pas facturée, et la pièce fait de 200 un nœud.
- **Afficher une clé : non.** Le programme ne lit pas la variable de la clé ; il n'affiche que le statut et le champ
  `type` de l'objet `error`, ou le nom du type d'exception. Réserve mince : si la lecture du corps d'une réponse d'erreur
  levait à son tour, Python afficherait une trace (lignes du programme et message de l'exception) ; elle ne porte pas la
  clé, que le programme ne tient pas.
- **Toucher le dossier unique : non.** Aucune écriture (`-I -B`, aucun fichier ouvert en écriture), aucun journal ; un
  échec du point 5 bis laisse le dossier préparé intact et sans journal.
- Ce qu'il prouve et ne prouve pas : la lecture de la pièce est juste (route et certificat ; ni crédit, ni palier, ni
  `POST`). La branche 401 n'a été jouée que sur mon faux serveur, jamais contre l'amont.

## 4. Les tranches de 6

- **Marge** : pire observé 63 s par appel ; 6 × 63 × 1,12 ≈ 425 s contre 7 200 s d'arrière-plan (dix-sept fois), et
  encore sous le délai d'arrière-plan par défaut de 1 800 s si l'opérateur oubliait `timeout`. Tient avec marge.
- **Borne dure** : la pièce dit honnêtement qu'une tranche de 6 n'est pas bornée par l'outil et donne le repli à 3.
  Précision : `DELAI_S` est un délai **par opération de socket** (connexion, envoi, chaque lecture), non une durée totale ;
  « un appel s'achève au plus à 1 800 s » est donc vrai à peu de chose près, non à la lettre. La marge du repli (5 400 s
  contre 7 200 s) l'absorbe. Le repli se déclenche après coup : une tranche de 6 qui ralentirait d'un coup au-delà de
  1 200 s par appel serait tuée en vol ; improbable (dix-neuf fois le pire observé), et non silencieux.
- **Tranche arrêtée, perte silencieuse : non, par l'outil.** `pause` ne perd rien (les appels à faire sont recalculés du
  journal) ; code 3 ou 4 : relevé scellé, arrêt au journal, réponses reçues gardées ; processus tué en vol : l'envoi est au
  journal avant l'appel, donc `en_vol` au `bilan`, compté au pire cas, tout `envoyer` refusé ; tué entre l'écriture d'une
  réponse et sa ligne de journal : `bilan` refuse (fichier sans clôture). La clé est relue à chaque tranche et son absence
  est refusée avant tout journal. **Mais la table de la pièce ne couvre pas tous ces cas : couples 1 et 2.**

## 5. Corrections (couples : ce qui est écrit → ce qu'il faut écrire)

Exigées avant le feu :

1. **Table du point 7, dernière ligne.** « pas de code (tâche tuée à la limite, coupure de la session, notification
   perdue) » → « **tout autre code (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code** », même conduite.
   Cause : une tâche tuée rend en général un code, et une exception non prévue de l'outil rend 1 ; aucune ligne ne le dit.
   La même phrase vaut pour le point 6 (« tout code autre que 0 : rien de plus, nœud »).
2. **Contrôle B, cas où il ne rend pas sa ligne.** À ajouter sous le contrôle B : « s'il s'arrête sur une exception
   (`ValueError` : aucune clôture, cas d'un premier appel tué en vol, `max()` d'une suite vide, vérifié ; `Refus` : fichier
   sans clôture au journal), jouer `bilan` seul ; `bilan` en refus (code 2) ou `en_vol` non vide : dossier perdu, nœud ».
   Ou remplacer `max(x['cout_usd'] for x in c)` par `max((x['cout_usd'] for x in c), default=None)`. Cause : au seul
   moment où le premier appel casse en vol, le contrôle B affiche une trace au lieu de l'état.
3. **Points 13 et 14, « somme des `depense_comptee_usd` ».** → « **le `depense_comptee_usd` rendu par `bilan`** (cumul du
   journal, appel en vol compris) ; les relevés sont cumulatifs, on ne les additionne pas ». Cause : chaque relevé porte la
   dépense de tout le journal (`envoyer`, fin) ; avec quatre relevés (point 6 et trois tranches), leur somme inscrirait
   environ le double de la dépense au registre, et, en dépense antérieure d'une seconde préparation, ferait refuser le
   plafond. Surestimation sans danger, mais chiffre faux au registre ; et le dernier relevé n'existe pas pour une tranche
   tuée. (Le mot « somme » vient du § 6 et de C1 (5) : la pièce l'a porté fidèlement ; ce sont les tranches qui le
   rendent faux.)

Recommandées :

4. Table du point 7, ligne « clé absente » : « rétablir la variable par son origine, puis rejouer la même tranche une seule
   fois » → « **nœud (préalable 5) ; rejeu de la même tranche, une fois, sur mot de la mère** ». Cause : le préalable 5 dit
   « absente : nœud » ; une clé qui disparaît entre deux tranches est un fait d'environnement que l'opérateur ne répare pas seul.
5. Point 5 bis : variables gardées `…|SSL_CERT_FILE|OPENAI_API_KEY` → `…|SSL_CERT_FILE` (clé retirée). Cause : la clé ne
   sert pas à la route ; l'ôter rend « sans clé » vrai par construction. L'écart est déclaré et sans danger ; défense en
   profondeur seulement.
6. Préalable 6 et point 2 : « cette pièce et les quatre rapports » → « … **et les rapports de vérification de cette pièce**
   (celui-ci et son compagnon) », sinon `git status --porcelain` n'est pas vide au point 2. Et préalable 1 : le mot de Lazar
   sur le crédit est au registre depuis l'écriture de la pièce (R-2822, 23:28 UTC : rechargement automatique) ; à citer.

## Réserves

- La branche 401 du point 5 bis et la route réelle ne sont éprouvées par personne avant le feu (elles exigent le réseau).
- Je n'ai pas rejoué la préparation, ni la chaîne d'après l'envoi (réserve C7 de la pièce, inchangée).
- Si le repli à `--envois-max 3` joue, les sorties attendues du contrôle B (7, 13, 18) ne valent plus : compter par 3.
