# Rapport : machine louée du jeu relancé de l'idée 1.1 — pièces v2 (reprise de la poussée des sorties), répétition (v2)

- **Auteur** : rédacteur-développeur neuf, modèle A ; n'a écrit ni les pièces v1, ni les procédures v1 à v4, ni les
  contre-lectures, ni l'addendum de relance, ni le code du jeu, ni aucune pièce de B bis.
- **Heures (UTC, `date -u`)** : début 22:05:58Z ; répétition d'essai 22:12:5xZ à 22:17:16Z ; répétition finale 22:17:30Z à 22:21:55Z ;
  rédaction jusqu'au scellement de la procédure v5.
- **Tâche** : livrer la liste « M1'' » de la contre-lecture du tour 3 (`contre-lecture-machine-jeu-idee-1-1-tour3-v1.md`)
  et les couples qu'elle reprend des tours 1 et 2 ; GO-2026-11-16-09, GO-2026-11-16-10, R-3014, R-3016, R-3017, R-3026.
- **Version** : v2 ; suit la v1 (`rapport-machine-jeu-idee-1-1-v1.md`, `0495f598ba0a64162391cd714cec0ce162203fed938227e325ab92cbce6f5a82`), dont le verdict et la
  réserve § 5 point 1 présentaient D7 comme ouvert (tour 1, M3) : ils sont réécrits ici, avec l'état du 2026-11-16 au soir.

## Verdict

**Pièces v2 livrées et répétées hors ligne sans écart : 126 cas sur 126** (les 110 cas de la v1 et 16 cas de la reprise ;
sortie gardée `sortie-repetition-machine-jeu-idee-1-1-v2.txt`, `cde2d45c49ea04edd7415118e43705732f87c7ad3376d120d0f1c67084722862`). La procédure v5 les nomme. Aucun appel au
loueur, aucune machine, aucune dépense, aucun commit. **Rien ne part au feu avant un tour 4 de contre-lecture rendu
`scellable`.** Les préalables qui restent à la mère sont ceux de la procédure v5 (§ 2 et § 6, « restes ouverts ») : ligne de
GO « calcul » à inscrire, feu, `COMMIT` relu, permission de la ligne neuve, rappel à l'échéance, jeton à renouveler après.

**Ce qui n'est plus ouvert** :
- **D7 tranché** : GO-2026-11-16-10 (Lazar, inscrit le 2026-11-16T20:47:50Z, R-3016) accepte l'écart D7 (machine louée,
  dépense, contre [T] l. 629 et 660) ; GO-2026-11-16-09 ne sert qu'à l'option (a). Plus aucune question de la mère sur D7.
- **Addendum de relance scellé, commité, poussé** (R-3017) : `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md`,
  `a692d50c07c1b4b7ef07883ac91124eab4798cab7a579e14235484ea4d2319cf`, commit `14a0dfc5962aad5987d6c88e03e72b5f6d92f150`,
  ancêtre de `main` (lu par les tours 2 et 3) ; il n'est plus « à écrire ». `COMMIT` reste à relire au feu.
- **Minuterie de 49 h 45** : acceptée par la mère (R-3026, défaut de routine ; surcoût au pire 0,105 USD).

## 1. Pièces (dossier `docs/procedures/machine-jeu-idee-1-1-v1/`, chacune scellée par un compagnon)

| Fichier | sha256 | Rôle |
|---|---|---|
| `amorce_jeu_idee_1_1_v2.sh` | `8c9057951cbac4469871a1cf2890f038cf54d016c651333dda2e89c512481301` | côté machine : v1 + reprise de la poussée des sorties |
| `lancer_jeu_idee_1_1_machine_v2.sh` | `59dfe8de521f2a83098a714af874051194b171a52c5e8938aca7dea1991165f2` | côté session : v1 dont l'amorce nommée est la v2 |
| `garde_machine_jeu_idee_1_1_v1.py` | `b099a05712dc96ed44121e9caf9e4633af8cfb7710f59724eaae6c92783f1e8a` | inchangée (elle ne nomme pas l'amorce) |
| `repetition_machine_jeu_idee_1_1_v2.sh` | `796dec57ffb52fdfbd135e4799bbe6d535bfbe1b93f789e946e8703f6043fee1` | répétition locale : 110 cas de la v1 + reprise |
| `jeu_factice_idee_1_1_v1.py` | `c9863b0d850d9f50c2bed5b8c2fb1330c7ed47bccb3c86a3f2a2814d39c3d459` | inchangé (le mode `sain` suffit aux deux cas neufs) |
| `sortie-repetition-machine-jeu-idee-1-1-v2.txt` | `cde2d45c49ea04edd7415118e43705732f87c7ad3376d120d0f1c67084722862` | sortie gardée de la répétition finale |
| `devis-machine-jeu-idee-1-1-v2.md` | `a9754c2ebdab6174b8af68dfba06a2effbbe49bc9e6a7249f86f5455232cc074` | couples 5, 11, 16, 17 du tour 1 ; coût de la reprise |
| `corriger_procedure_v4_vers_v5_tour3_v1.py` | `b0c7d0234ea5332dcaa9928ba6f8aa51462cfdb61e85641472457c141d17f091` | programme de couples : procédure v4 → v5 |
| `procedure-machine-jeu-idee-1-1-v5.md` | (son compagnon ; elle nomme ce rapport par son empreinte) | gestes, rôle de la mère ; nomme les pièces v2 |

Les pièces v1 et les procédures v1 à v4 restent archivées, sans modification (R12).

## 2. La reprise (amorce v2) et ce qui change

1. **Forme** (couples 1 et 2 du tour 1, formes indicatives fixées ici) : fonction `reprise_sorties`, appelée quand le bloc de
   recopie et de poussée des sorties échoue (`… ) 9> "$VERROU" || reprise_sorties || arret "… impossible après reprises …" 4`).
   Elle journalise `RESERVE : poussée des sorties impossible : reprise toutes les 300 s, machine gardée vivante jusqu'à 1200 s
   avant l'échéance (…)`, puis, tant que l'échéance − `MARGE_TERM` n'est pas atteinte : pause de 5 × `PAUSE` (300 s, ramenée
   au reste jusqu'à la borne), recopie si elle manque, comparaison à l'octet, poussée par lots de 400 fichiers (manifeste et
   tranches ensemble). Réussite : `poussée des sorties reprise : réussie (reprise n)`, puis la fin ordinaire (code 0, ou le
   code 4 d'un `arret.json` ou d'un compagnon faux, comme en v1). Échec : `reprise n … : échec ; machine vivante, aucun
   « stopped » ; sorties intactes sur le disque`, puis le journal poussé si possible. Épuisement : `reprises … épuisées (n)`,
   arrêt en code 4, « stopped » demandé **après** l'arrêt seulement ; la minuterie, inchangée, détruit la machine à
   l'échéance.
2. **Deux ajouts à la forme indicative, déclarés** : (i) chaque reprise manquée est journalisée et le journal poussé si
   possible (sans quoi la ligne « RESERVE » que le geste 13 demande de lire n'atteindrait jamais la branche de sortie : le
   suivi horaire est arrêté à la fin du jeu) ; (ii) la pause est ramenée au temps qui reste jusqu'à la borne, pour que l'arrêt
   tombe à l'échéance − 20 minutes et non jusqu'à 5 minutes plus tard ; et une liste de fichiers vide ne vaut pas réussite.
3. **Rien d'autre ne change dans l'amorce** (différentiel v1 → v2 : en-tête, fonction neuve, ligne d'appel). Le lanceur v2
   ne change que le nom de l'amorce (trois places) et son en-tête. Constantes de production inchangées : `PAUSE` = 60,
   `MARGE_TERM` = 1 200, `PAS` = 30.
4. **Ligne de création** : l'amorce v2 compressée fait 11 548 caractères de base64 ; la ligne imprimée en répétition fait
   12 619 caractères et la sortie de `commande` ≈ 12 800 octets (v1 : 11 911 et ≈ 12 100). La procédure v5 dit ces mesures
   (L3, geste 5) ; la lecture en deux morceaux (`cut -c1-6000`, `cut -c6001-`) ne change pas.

## 3. Répétition v2 (sortie gardée ; 126 cas, 0 écart ; dépôt jouet en `file://`, loueur simulé)

- **Les 110 cas de la v1**, inchangés, sur le lanceur v2 et l'amorce v2 (même ordre, mêmes motifs ; le loueur simulé note en
  plus l'heure en secondes, sans changer aucun cas).
- **Moyen** : un crochet `pre-receive` du dépôt jouet refuse toute poussée dont l'arbre porte `runs/` sur deux branches
  seulement : `calcul/idee-1-1-jeu-relance-v15` (refusée trois fois, puis acceptée) et `-v16` (toujours refusée). Il compte
  ses refus dans un fichier du dossier de répétition. Aucune autre branche n'est touchée.
- **(a) Poussée refusée trois fois puis acceptée (7 cas)** : code 0, « FIN » ; trois refus exactement, puis poussées
  acceptées ; réserve de reprise au journal ; aucun « « stopped » demandé » avant la ligne « réussie » ; aucun arrêt ; un seul
  « stopped » chez le loueur, à la fin, aucune destruction ; sorties de la branche égales à l'octet à celles de la machine,
  toutes présentes.
- **(b) Poussée jamais acceptée (8 cas)** (échéance à 90 s, `MARGE_TERM` = 40 s) : code 4, « impossible après reprises » ;
  réserve au journal ; reprises manquées journalisées puis « épuisées » ; arrêt à la borne ou juste après, avant l'échéance ;
  premier « stopped » après l'arrêt (journal et loueur) ; destruction demandée à l'échéance seulement (six essais) ; sorties
  intactes sur le disque (8 fichiers égaux à leurs compagnons, copie du dépôt de sortie égale) ; branche `-v16` sans aucune
  sortie (refus tenus), traces d'avant la fin présentes.
- **(c) Cas sain (1 cas)** : aucune reprise.
- **Durées raccourcies** en répétition seulement (variables refusées hors répétition), comme en v1 : avec `PAUSE` = 1, la
  reprise a lieu toutes les 5 s.

## 4. Ce que la répétition n'a pas éprouvé

1. Le loueur réel (recherche, création, « stopped », destruction par l'interface `PUT`/`DELETE` sur
   `/api/v0/instances/<id>/`) : non joué (consigne), comme en v1.
2. Une panne réelle du dépôt distant (réseau coupé, jeton refusé, limite de débit) : simulée par un refus du dépôt jouet ;
   les délais réels (`GIT_HTTP_LOW_SPEED_TIME` = 120 s) ne sont pas joués.
3. La reprise aux constantes de production (300 s, 1 200 s) : jouée aux constantes courtes seulement (la logique est la même).
4. Le vrai jeu, l'image réelle, `pip install`, le clone sur le dépôt distant : comme en v1.

## 5. Réserves

1. **Ordre de 4.4 et 4.5** (faits poussés avant et au lancement, transcrits au registre ensuite) : écart de forme à accepter
   dans le feu (inchangé depuis la v1).
2. **Bit près** : autre processeur, autre système ; limite déclarée par l'addendum de relance (4.2) ; `lscpu` et
   `numpy.show_runtime()` gardés (inchangé).
3. **Clone partiel** : la garde qui tient est « ancêtre de `main` » (inchangé).
4. **Fils oisif** : nœud de la mère au geste 12 (inchangé).
5. **Clés** : `GH_TOKEN` reste dans la configuration de la machine jusqu'à sa destruction ; renouvellement du jeton après la
   preuve de destruction à décider (P5 du tour 1 : nœud de Lazar). La réponse de création reste dans le dossier d'envoi
   jusqu'au geste 16.
6. **Réseau pendant le jeu** : les poussées du journal (chaque heure), des sorties et de leurs reprises sont déclarées par la
   procédure v5 comme part de l'écart D7 (P2 du tour 1), à citer par le feu.
7. **Réserves neuves de la v2, pour le tour 4** (aucune ne change la sûreté des clés ni des sorties) :
   - une poussée refusée **par la garde de poussée elle-même** (chemin hors des sorties, fichier de plus de 94 Mo : code 3 de
     `commit_pousser`) est reprise comme une panne, alors qu'elle ne peut réussir ; la machine reste vivante jusqu'à
     l'échéance − 20 minutes pour rien (coût compris dans le pire cas de la minuterie), et le fichier refusé reste dans
     l'index, de sorte que le journal ne se pousse plus non plus (déjà vrai en v1 au premier arrêt). Les sorties du jeu sont
     des fichiers JSON de petite taille ; correction possible au tour 4 : ne pas reprendre sur le code 3 ;
   - une recopie partielle (disque plein pendant `cp -a`) n'est pas refaite : la comparaison à l'octet échoue à chaque
     reprise, jusqu'à l'arrêt en code 4 ; les sorties du dépôt du jeu restent intactes ;
   - trafic montant dans le cas extrême d'un dépôt distant qui refuserait **après** avoir reçu le paquet : jusqu'à
     ≈ 200 Go, ≈ 4 USD à 20 USD le téraoctet, hors de la garde de dépense (devis v2, § 4) ;
   - la copie des sorties depuis une machine vivante (geste 13) n'a aucune commande écrite : nœud de la mère, à trancher
     avant l'échéance, la minuterie détruisant le disque à l'échéance.
8. **Contre-lecture** : les pièces v2 et la procédure v5 attendent le tour 4 (R2), qui rejouera la répétition.

## 6. Déclaration

- **Rôle** : rédacteur-développeur neuf des pièces v2 de la machine du jeu relancé de l'idée 1.1 ; **lettre de modèle : A**.
- **Pièces lues** (compagnons des 19 pièces du dossier vérifiés `OK` au début, 22:06Z) : les trois rapports de
  contre-lecture (tour 1 `09d345be…`, tour 2 `c977ac7e…`, tour 3 `e6b90a1f…`), entiers ; l'amorce v1
  `ede38bb6…`, le lanceur v1 `3ef1d9a6…`, la répétition v1 `f596aac3…`, le jeu factice `c9863b0d…`, le devis v1 `1ae229eb…`,
  le rapport v1, entiers ; la garde v1 `b099a057…` (recherche de ses références à l'amorce et au lanceur) ; la procédure v4
  `996c8a5c…`, entière ; le programme `corriger_procedure_v3_vers_v4_tour2_v1.py` (en-tête, comme modèle) ;
  `registres/decisions.md` (trois dernières lignes, R-3025 à R-3027) ; `registres/go.md` (GO-2026-11-16-09 et -10) ;
  `.claude/settings.json` et la liste des fonctions de `.claude/hooks/garde_calcul.py`.
- **Jamais ouvert** : rien sous `diag/`, `runs/`, `donnees/` du dépôt ; rien de `/home/user/jeu-idee-1-1-copie-v1` ; rien de
  7a, 7b, T0.6, T0.7, P3-bis, de B bis, du bras d'attaque. Aucune valeur de clé ; aucun `env`, `printenv`, `set` sans
  argument, `export -p` ; le texte du verbe interdit n'a été tapé dans aucune commande.
- **Accès extérieurs** : aucun ; aucun appel au loueur, aucune machine, aucune dépense, aucun commit, aucune poussée vers un
  dépôt réel ; git du dépôt principal en lecture seule (`git log -1`, `git status` ; la répétition fait `git show HEAD:<chemin>`
  de trois fichiers et de leurs compagnons).
- **Calcul** : léger (deux répétitions d'environ 4 minutes 30, dossiers du bloc-notes `rep-a1/` et `rep-final/`).
- **Incidents** : aucun (aucune commande refusée par le crochet, une garde ou le classifieur ; aucun processus arrêté hors de
  ceux de la répétition, par leur PID ; aucun fichier écrit hors du dossier et du bloc-notes).
