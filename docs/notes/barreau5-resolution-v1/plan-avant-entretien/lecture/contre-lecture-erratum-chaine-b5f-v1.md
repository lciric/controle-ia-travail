# Contre-lecture de l'erratum de chaîne de la relecture décisive du barreau 5 — v1

Écrite le 22 novembre 2026, rendue vers 23:15Z (`date -u`), par un contre-lecteur neuf (R2), Claude Opus 5.5 en effort maximal, sous-agent du conducteur de la lecture du barreau 5 (`session_013QMayjM1PQPWkLifMw9HDR`). Je n'ai écrit aucune pièce du barreau 5. Je n'ai rien lancé de payant, rien commité, rien poussé.

**Pièce** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/erratum-chaine-relecture-decisive-b5f-v1.md`, sha256 `d4b5ff14a910b693f910906ad4c044c57b0cb6e1896e49eca641107f94812702`, égale à son compagnon.

## Verdict

**Conforme après corrections.**

- **Cause et correction : justes.** Je les ai reproduites à l'identique sur un dépôt local servi en HTTP avec identification. L'empreinte de l'amorce corrigée est exacte.
- **Voie d'admission : elle tient.** La commande v3 laisse égal l'arbre gelé. L'instance, qui rejoue la garde du code au commit, accepte la marche. Aucune garde figée n'est retouchée.
- **Deux constats majeurs, à corriger avant que le développeur écrive le code :**
  - C1 : la vérification de filiation et de liste fermée de la commande v3 ne fige pas les fichiers de la v2. Elle est donc plus faible que celle de la v2.
  - C2 : la destruction de l'instance tombée est dite « selon le mandat », alors que le mandat l'interdit sans versement final prouvé.
- **Le reste** : précisions sur la variante, essais à ajouter, et quelques écarts et nœuds à compléter.

## Ce que j'ai lu, rejoué, et pas ouvert

### Empreintes vérifiées avant lecture
Toutes égales à leur compagnon ou à la valeur citée.
- La pièce et sa consigne (`caecf8f6…`).
- Le mandat v2 (`b1eb2afc…`) et ses errata 1 à 3 (`cde0279c…`, `4d1678b5…`, `1c9d9ce1…`).
- Le texte scellé (`bdff244f…`).
- Au commit `c76e79169` :
  - amorce `54a676f3…` (33 412 octets, 404 lignes) ;
  - lanceur v1 `ae501c55…` ;
  - `relecture_v1.py` `f6bd8c15…` ;
  - `lecture_v1.py` `ed0999df…` ;
  - `validation_reelle.py` `d25e4cd9…` ;
  - essais de l'amorce `5d3f0302…`.
- Au commit `5402367e5` : `commande_lecture_v2.py` `c6c5d11c…`. Ce commit descend de `c76e7916`.

### Lu
- Le texte scellé, l. 35, 151 à 179, 217 à 233, 257 à 261 et 345 à 448 ; rien des l. 53 à 105.
- En entier : l'amorce, le lanceur v1, les essais de l'amorce, `commande_lecture_v2.py`.
- `relecture_v1.py`, l. 533 à 600 et 836 à 1247.
- `lecture_v1.py` : constantes (l. 101 à 158), puis les seules fonctions que liste le § 1 de la pièce.
- `engagement_v1.py`, l. 1 à 200.
- `validation_reelle.py` : `CHEMINS_GELES`.

### Non lu, hors de ma liste
- `formation_v1.py`, la fabrique et le traducteur de l'épreuve à vérité plantée.
- Les essais de l'amorce entière et ceux de la commande v2 ; le lanceur v2 ; le rapport de vérification v2.
- Les mandats de l'ouvreur et du lecteur du verdict ; le registre propre ; le registre des accords.

Les affirmations de la pièce qui en dépendent ne sont donc pas vérifiées par moi : les suffixes de `formation_v1` (l. 89 à 92), le montage `insteadOf` de l'essai à blanc, le contenu de GO-2026-11-22-145, et l'origine de la table engagée (`engagement_v1.py` après la l. 200).

### Jamais ouvert
- Rien sous `donnees/*`, `formation-b5f/*` ou `traces/*` ; ni `diag/`, ni `docs/verdicts/`.
- Ni l'état, ni les décisions, ni les passations.
- Ni table, ni sel, ni score.

Trois contrôles sans aucun contenu :
- `git cat-file -t` sur `81061453` et `254f9280` répond « commit ». Ces deux objets existent aujourd'hui dans ce dépôt local, contrairement à ce que dit le § 1 de la pièce, écrit plus tôt.
- `2beeec31` descend de `c76e7916`, avec un arbre gelé égal (code de sortie 0).
- `2beeec31` ne descend pas de `5402367e`, comme attendu.

### Sondages jetables
Faits dans le bloc-notes, hors du dépôt, puis retirés ; aucun fichier du dépôt n'a été touché.

1. **Défaut et correction, rejoués.**
   - **Montage** :
     - un dépôt nu (`uploadpack.allowFilter=true`), servi par `git http-backend` derrière un petit serveur Python sur 127.0.0.1 ;
     - le serveur exige « Authorization: Basic » avec un jeton factice et répond 401 sinon ;
     - git 2.43.0 ; environnement vidé des variables `GIT_*` et des mandataires, `HOME` propre.
   - On joue les commandes de l'amorce, l. 324 et 362 à 364.
   - **Code actuel** :
     - l'extraction échoue, code 128, avec « fatal: could not read Username for 'http://127.0.0.1:<port>': terminal prompts disabled », puis « fatal: could not fetch <objet> from promisor remote » ;
     - aucun fichier n'est extrait.
   - **Avec la ligne ajoutée** :
     - code 0, trois fichiers extraits ;
     - la configuration du clone porte `helper = "!f() { … \"password=${GH_TOKEN}\"; }; f"`, sans la valeur du jeton.
   - **Témoins** :
     - une requête sans identification reçoit 401 ;
     - un clone vers un chemin local ignore le filtre (« warning: --filter is ignored in local clones »), pose quand même `remote.origin.promisor=true`, et tire tous les objets ;
     - un clone `file://` tient le filtre (aucun objet de contenu), mais ne demande aucune identification. Seul un serveur HTTP à identification voit donc le défaut.
   - Serveur arrêté par son PID.
2. **Amorce corrigée, rebâtie à partir des l. 112 et 118 de la pièce elle-même.**
   - Voie B : sha256 `0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001`, 33 536 octets, 405 lignes ; `bash -n` sans erreur. La pièce ne porte aucun caractère combinant.
   - Voie A : `27b1166a…`, 33 539 octets.
   - Les deux sont égales aux valeurs de la pièce.
3. **Le fichier d'essais figé de l'amorce (51 essais), joué sur une extraction de `c76e79169`.**
   - Avec l'amorce figée : 51 passés.
   - L'amorce corrigée de la voie B mise à sa place : 51 passés.
   - Celle de la voie A : 50 passés, 1 en échec. C'est `test_branche_de_sortie_meme_nom_que_le_code_de_lecture` (l. 105 à 109) : `…-lecture-r1` diffère de `relecture_v1.PIECES_LECTURE`.
4. **Comptes par collecte seule à `c76e79169`** : relecture 24, lanceur v1 43, engagement 23, amorce 51, amorce entière 4, lecture 102, sondes 20, épreuve à vérité plantée 155. Tous égaux au § 6.3.

## Réponses aux sept questions

### (1) Cause et correction : justes

- **La cause** (§ 2.1 à 2.3) est exacte, ligne pour ligne. Le décalage d'une ligne relevé dans la consigne est réel : l. 325 et 326, et non 326 et 327.
- **La correction** inscrit l'aide dans le clone des entrées, juste après la l. 362. Elle suffit, et c'est le geste du clone du code (l. 326).
  - La valeur du jeton n'est pas écrite.
  - L'inscription vaut pour toute descente différée ultérieure dans ce clone.
- **Rien d'autre ne touche le clone des entrées.** `verifier_entrees` n'emploie que des arbres (`ls-tree`, `diff-tree --name-status`). La configuration écrite reste sous `.git`, hors des contrôles d'arbre propre de `$D` (l. 379 et 390).
- **Pourquoi aucun essai ne l'a vu** (§ 2.3) : confirmé pour ce que j'ai pu lire.
  - `_depot_entrees`, l. 178 à 212, clone un chemin local, sans filtre.
  - Le comportement de git sur les chemins locaux et sur `file://` est vérifié par mon sondage.

### (2) Admissibilité : la voie retenue tient, sous C1

- **Aucun commit de la marche ne peut porter l'amorce corrigée** (§ 2.4) : constat exact.
  - `CHEMINS_GELES` couvre `scripts/` (`validation_reelle.py`, l. 71 à 73).
  - `exiger_code_de_lecture_au_commit` (l. 497 à 513) est jouée par « verifier » (`relecture_v1`, l. 876), par l'ouvreur (l. 525) et par la marche sur l'instance (l. 548).
- **L'amorce jouée sur l'instance est la copie base64 de la commande** (`relecture_v1`, l. 1088 et 1097 ; v2, l. 263 et 272).
- **L'instance accepte la marche.**
  - Le commit de la marche neuf (enfant de `2beeec31`) ne diffère que sous `registres/`, hors de l'arbre gelé.
  - La ligne d'épinglage est ignorée par le lecteur figé du registre (`engagement_v1.py`, l. 134 : seules comptent les lignes qui commencent par « | » après retrait des espaces et portent « -B5F »).
  - L'amorce corrigée vit sous `/root/`, hors de `$D`.
- **Les gardes de « verifier » et de « commande »** (registre, arbre extrait d'après les motifs, garde de calcul) sont rejouées à l'identique. La ligne ajoutée ne touche pas le bloc des motifs.
- **Ce qui est plus faible que la v2** : la seule vérification de filiation et de liste fermée (c'). Voir C1.

### (3) Pesée des voies A et B : B reste défendable ; la pesée est à compléter

Voir C15. La pesée doit ajouter quatre choses :
- R12 est rangée par CLAUDE.md parmi les « règles gelées — sans discussion » ;
- en voie A, une garde figée tombe sur l'amorce embarquée (sondage 3) ;
- en voie A, il faut probablement des errata aux mandats de l'ouvreur et du lecteur du verdict (C7) ;
- en voie B, il y a des risques de geste : suppression définitive, références périmées, garde du dépôt distant.

### (4) Variante des noms suffixés

- **Ordre des gardes : tenu pour l'ouverture recomposée.** La traduction ne vient qu'après :
  - la cohérence de la table d'origine ;
  - son égalité à `ENGAGEMENT-B5F` et à `OUVERTURE-B5F` ;
  - les dates.
- **Le `preparer` recomposé dépend de l'ordre des gestes de l'ouvreur** : voir C6.
- **Les autres constats de la variante** :
  - la règle des deux listes suppose une table rangée par nom (C4) ;
  - l'épinglage n'est ni fixé tôt ni vérifiable (C5) ;
  - un artefact est mal posé et le montage de la branche de formation n'est pas décrit (C13) ;
  - l'écart est à nommer à la lettre (C14).
- **Compagnons de `couts.json` et `formation.json`** : je confirme qu'il ne faut pas les ajouter.
  - Une garde de plus que l'entrée figée casserait la parité.
  - La règle d'égalité de la seconde liste à l'engagement ne peut que refuser une entrée retouchée, jamais l'admettre.

### (5) Essais : ils peuvent échouer

Les témoins sont bien posés :
- l'amorce figée tombe dans le même monde ;
- une requête sans identification reçoit 401 ;
- la différence entre les commandes v2 et v3 est fermée, hors du segment base64 ;
- les mutations de la variante rendent un essai rouge.

Ce qui manque :
- l'artefact de la garde neuve (C8) ;
- le nettoyage des variables `GIT_*` (C9) ;
- les essais figés de l'amorce joués sur l'amorce embarquée (C10) ;
- l'artefact de C1 ;
- le montage de la branche de formation et le témoin d'ordre (C13, C4).

### (6) Écarts

Les dix écarts déclarés sont justes. Il en manque six : C2, C3, C7, C14, C17, C18.

### (7) Nœuds

Voir la dernière section : nœud 1 à recadrer, nœud 2 à compléter, nœud 3 juste, une troisième option au nœud 4, et un point neuf pour la mère (C2).

## Constats

### C1 — majeur — La vérification de filiation et de liste fermée de la commande v3 (c') ne fige pas les fichiers de la v2

- **Citation** :
  - « (c') : le commit v3 descend de `c76e7916` et du commit v2 cité. Sur les chemins gelés, il n'en diffère que par des ajouts, tous de la liste fermée réunie » (§ 4.3 (e)) ;
  - « `LISTE_FERMEE_REUNIE` = la liste v2 et les sept fichiers » (§ 4.3 (b)).
- **Source** :
  - `commande_lecture_v2.py`, l. 173 à 200 : la (c) de la v2 compare au seul commit du code figé. C'était suffisant, parce que sa (b) exigeait que la tête soit le commit cité lui-même.
  - La v3 importe de son propre arbre `commit_de_commande_cite` (vérification (d)) et `exiger_offre_lecture_v2` (§ 4.3 (e) et (f)).
- **Problème** :
  - Comparé à `c76e7916`, un fichier de la v2 modifié dans le commit v3 reste un « ajout » de la liste réunie : la (c') l'admet.
  - La vérification (d) et la garde de l'offre seraient alors jouées par un module v2 que rien ne lie au commit v2 cité, ni au rapport de vérification qui le couvre.
  - C'est une garde plus faible que la v2, ce que la pièce s'interdit.
- **Correction** : écrire (c') en deux temps.
  - (c'1) Rejouer la (c) de la v2 sur le commit v2 cité : `exiger_commande_issue_du_code_fige(racine, commit_lecture, v2)`.
  - (c'2) La différence du commit v2 au commit v3, sur les chemins gelés, n'est faite que d'ajouts, tous parmi les sept fichiers de la v3, et de fichiers ordinaires : modes 100644 ou 100755 admis ; 120000 (lien) et 160000 (sous-module) refusés.
  - Ajouter au § 6.2 l'artefact « module, lanceur ou essais de la v2 modifiés dans le commit v3 ».
  - Fixer dès maintenant un seul commit pour la commande et l'ouverture, donc une seule liste fermée. Sinon, le commit à part de l'ouverture (§ 5.5) doit avoir sa propre liste, écrite.

### C2 — majeur — La destruction de l'instance tombée est contraire au mandat, et l'inventaire du disque n'est pas faisable tel qu'écrit

- **Citation** : « L'instance tombée (62047649) est traitée d'abord, si elle existe encore : inventaire, puis destruction par son identifiant, selon le mandat (§ 5.4, pas 9). On le fait tant que la branche de sortie porte encore le commit prouvé » (§ 3.4, geste 1).
- **Source** :
  - Mandat v2, § 5.4, pas 9 : « Seulement si le pas 8 a vu la ligne « versement final prouvé » ».
  - Mandat v2, § 7 : « une instance au versement final non prouvé reste arrêtée, non détruite ».
  - Amorce, l. 261 à 266 : le témoin n'existe que si la marche est menée au bout, jamais ici.
  - Amorce, l. 305 à 311 et 115 à 121 : `fin_instance` écrit au journal du disque la ligne « fin, code … ; état « stopped » demandé : HTTP … » après le dernier versement.
  - Règle « récupérer ce qui est récupérable » (CLAUDE.md).
- **Problème** :
  - Le versement final n'est pas prouvé et ne peut pas l'être : le mandat interdit la destruction.
  - Le disque porte au moins une ligne de journal jamais versée. Si la minuterie a tourné, il porte aussi ses lignes et le signal. « Rien de perdu » n'est vrai que pour la branche.
  - L'inventaire du disque demande de redémarrer l'instance, donc une dépense. L'inventaire versé ne couvre que les traces.
- **Correction** :
  - Retirer « selon le mandat ».
  - Poser le sort de l'instance comme une décision nommée, de la mère, ou de Lazar avec le nœud 2. Deux options :
    - la détruire sans inventaire du disque, en écrivant ce qui s'y trouve (clones reproductibles, aucun calcul fait, la ou les dernières lignes de journal) et que leur perte est acceptée ;
    - ou la redémarrer, verser ces lignes, puis la détruire.
  - Préciser que « detruire » prend le commit prouvé de la ligne « versement des sorties prouvé … au commit C », avec l'inventaire qui y est, et non la tête H.
  - Dire le coût horaire du disque arrêté (300 Go), pour trancher vite.

### C3 — moyen — Coupure et plafond de la relance : la source n'est pas citée, l'accord de la reprise est omis

- **Citation** :
  - « la coupure tenue par la session, 14 USD (chiffre de la consigne) » (§ 7) ;
  - nœud 1 : « sous l'accord de calcul GO-2026-11-19-86, avec une coupure de 14 USD » ;
  - § 8.4 : « coupure de 14 USD ».
- **Source** :
  - Mandat, erratum 2, point 7 : « À la reprise : relecture décisive **9 USD**, répétition **8 USD**, accords `GO-2026-11-19-86` et `GO-2026-11-22-117` ».
  - Mandat, erratum 1, point 2 : GO-2026-11-22-117, plafond de 33 USD.
  - `relecture_v1.py`, l. 960 et 1007 à 1016 : l'échéance de l'instance se calcule sur 21 USD.
- **Problème** :
  - « 14 USD » ne vient d'aucun texte que j'aie pu lire, et le mandat en vigueur dit 9 USD.
  - GO-2026-11-22-117 n'est nommé nulle part, alors que la relance s'y range.
  - Rien ne montre que le pire cas tient sous 33 USD. Ce pire cas additionne :
    - l'échéance de l'instance, si la veille de la session manque ;
    - le stockage ;
    - la répétition et la marche tombée, déjà dépensées.
- **Correction** :
  - Citer la source de 14 USD (accord ou signal, avec son identifiant).
  - Nommer GO-2026-11-22-117 au nœud 1, au § 7 et au § 8.4.
  - Écrire la marge : 33 USD moins le cumul relevé, comparés au pire cas de la relance.
  - Porter à l'erratum 4 le remplacement du point 7 de l'erratum 2.

### C4 — moyen — Variante : la règle des deux listes suppose une table engagée rangée par nom

- **Citation** : « E_a et E_b sont les empreintes de `table_des_etiquettes(s, liste)` » ; « E_a égale l'engagement : variante (a) » (§ 5.2, points 5 et 6).
- **Source** :
  - `engagement_v1.py`, l. 81 à 83 : `table_des_etiquettes` range les lignes par nom opaque.
  - `engagement_v1.py`, l. 86 à 91 : `forme_canonique` garde l'ordre de la liste reçue (`sort_keys` ne trie que les clés).
- **Problème** :
  - Si la table engagée n'est pas dans l'ordre des noms, E_a et E_b diffèrent toutes deux de l'engagement. C'est vrai même pour une table nue, que l'entrée figée accepterait.
  - Il en résulte un refus et un nœud à tort, au jour L+1.
  - La fonction qui a écrit la table m'est fermée (l. 200 et suivantes).
- **Correction**, au choix :
  - Décider sur T elle-même, déjà égale à l'engagement :
    - variante (a) si toutes ses graphies sont des bases ;
    - variante (b) si chaque graphie égale c(base) ;
    - E_a et E_b restent une trace, calculées sur T dans son propre ordre, seule la famille étant remplacée.
  - Ou établir maintenant, par la lecture de ce code, que la table engagée sort de `table_des_etiquettes`, et ajouter un essai témoin « table dans un autre ordre ».

### C5 — moyen — Variante : le moment de l'épinglage de l'ouverture n'est ni fixé tôt, ni vérifiable

- **Citation** :
  - « Ligne d'épinglage propre, sous la table, avant `OUVERTURE-B5F` » (§ 5.5) ;
  - « avant `OUVERTURE-B5F`, celle de l'ouverture » (§ 8.4).
- **Source** :
  - Texte scellé, l. 219 : « Son programme est figé (`CODE-LECTURE-B5F`) avant la création de son instance ».
  - Amorce, l. 356 et 202 à 210 : les commits de sortie descendent du commit de la marche, dont ils gardent l'arbre, registre compris.
- **Problème** :
  - Une ligne libre n'a pas d'instant : « avant `OUVERTURE-B5F` » n'est tenu que par la mère.
  - Or le code de l'ouverture s'écrit maintenant.
- **Correction recommandée** :
  - Inscrire la ligne de l'ouverture avec celle de la commande, dans le même commit de la marche, avant la relance.
  - Le module de l'ouverture exige alors qu'elle figure au registre tel qu'au commit prouvé que cite `SCORES-B5F`. Ce registre est celui du commit de la marche.
  - Le code de la variante est ainsi figé avant la création de l'instance, comme le programme figé du point 7, et c'est vérifié par programme.

### C6 — moyen — Variante : le `preparer` recomposé exige `OUVERTURE-B5F`, mais l'ordre des gestes de l'ouvreur n'est pas écrit

- **Citation** : « Le `preparer` recomposé vérifie de plus l'engagement, l'ouverture et la règle, ce que le `preparer` figé ne fait pas » (§ 5.4).
- **Source** :
  - `lecture_v1.py`, l. 1480 à 1495 et 1406 à 1411 : le `preparer` figé ne lit au registre que la ligne de relance.
  - `lecture_v1.py`, l. 444 à 494 : `lire_registre_de_lecture` exige `SCORES-B5F` et `OUVERTURE-B5F`.
- **Problème** : l'entrée figée permet de jouer `preparer` avec un registre lu à un commit antérieur à `OUVERTURE-B5F`. Dans ce cas, le `preparer` recomposé refuse. L'ordre réel est fixé par le mandat de l'ouvreur, que je n'ai pas lu.
- **Correction** :
  - Écrire l'ordre : `OUVERTURE-B5F` inscrite, puis `variante`, `preparer` et `ouvrir`, au même commit du registre.
  - Le recouper avec le mandat de l'ouvreur.
  - À défaut, borner le `preparer` recomposé à l'engagement et à la règle, et laisser l'ouverture et les dates à `ouvrir`.

### C7 — moyen — Il manque des errata aux mandats de l'ouvreur et, en voie A, du lecteur du verdict

- **Citation** : le § 8.5 ne prévoit qu'un erratum 4, au mandat de la session ; le § 5.5 dit ce que joue l'ouvreur.
- **Source** :
  - Lanceur v1, l. 74 à 79 : « preparer » et « ouvrir » passent toujours `--racine`, donc la garde du code au commit.
  - Les mandats de l'ouvreur (v2 et son erratum 1) et du lecteur du verdict (v2 et ses errata) sont présents dans ce dossier ; je ne les ai pas lus.
- **Problème** :
  - La variante change la procédure de l'ouvreur : deux arbres, `variante` d'abord, lanceur neuf en (b), vérification de l'épinglage.
  - En (b), le dossier du résultat porte un fichier de plus (`traduction-table-b5f.json`), et le champ `a_garde_d_ouverture.code` change de contenu.
  - En voie A, ces mandats nomment probablement la branche des scores.
- **Correction** :
  - Ajouter au § 8.5 un erratum au mandat de l'ouvreur, et un au mandat du lecteur du verdict s'il nomme la branche ou le contenu du dossier du résultat.
  - Dire ce que porte `a_garde_d_ouverture.code` en (b).
  - Porter ces errata à la pesée : ils pèsent pour B.

### C8 — mineur — La garde neuve de l'amorce n'a pas d'artefact (R5)

- **Citation** : « Pourquoi `|| arret` […] aucun repli silencieux (R5) » (§ 3.1) ; les mutations du § 6.1 ne la visent pas.
- **Source** : CLAUDE.md, R5 : « Toute garde d'arrêt testée sur un cas sain et sur un artefact ».
- **Correction** : ajouter à `tests/test_amorce_b5f_lecture_identification_v1.py` un artefact où `git -C "$E" config` échoue.
  - Moyen : un faux `git` en tête du `PATH` qui refuse cette seule sous-commande, ou le `.git` du clone des entrées mis en lecture seule.
  - Attendu : le journal porte « ARRET : aide d'identification non inscrite dans le clone des entrées », et aucune extraction n'est tentée.

### C9 — mineur — L'environnement de l'essai d'identification doit retirer toutes les variables `GIT_*`

- **Citation** : « environnement : `HOME` et configuration globale propres à l'essai, `GIT_CONFIG_NOSYSTEM=1`, `GIT_TERMINAL_PROMPT=0`, aucun `GIT_ASKPASS`, variables de mandataire retirées » (§ 6.1).
- **Source** :
  - Essais de l'amorce, l. 46 : `_env` retire toutes les variables `GIT_*`.
  - Cet environnement porte `GIT_CONFIG_COUNT` et `GIT_CONFIG_KEY_0` à `_2` : `credential.interactive` et deux réécritures `url.https://github.com/.insteadOf`. Vu par les noms seuls.
- **Problème** : laissées, ces variables réécrivent l'URL officielle et changent la façon dont git demande l'identification. L'artefact (« could not read Username ») comme le cas sain dépendraient alors de la machine.
- **Correction** : retirer toutes les `GIT_*` (dont `GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_*`, `GIT_CONFIG_VALUE_*` et `GIT_CONFIG_PARAMETERS`), puis poser celles de l'essai, comme le fait `_env`.

### C10 — mineur — Jouer les essais figés de l'amorce sur l'amorce embarquée

- **Source** : sondage 3 (voie B : 51 passés sur 51 ; voie A : 50 sur 51).
- **Correction** :
  - Dans les essais de la v3, jouer le fichier d'essais figé de l'amorce sur une copie jetable de l'arbre, où l'amorce est remplacée par `amorce_corrigee(...)`. En voie B, exiger 51 passés.
  - En voie A, déclarer l'échec attendu de `test_branche_de_sortie_meme_nom_que_le_code_de_lecture`, le remplacer par l'égalité à `BRANCHE_SORTIE`, et porter à la pesée cette garde figée de plus mise hors jeu.
  - Dans les deux voies, ajouter un essai : le bloc « branche » de l'amorce embarquée rend `BRANCHE_SORTIE`.

### C11 — mineur — Ligne d'épinglage (d') : six précisions

1. Elle se lit au registre du commit de la marche, comme (d).
2. Le préfixe est en colonne 1, sans espace initial. Le lecteur figé retire les espaces (l. 134) ; le lecteur de la v3 ne doit pas.
3. Toute ligne qui commence par le préfixe doit égaler l'un des deux formats écrits (liste fermée des objets) ; sinon, refus, comme pour une clé inconnue.
4. Espaces ordinaires (U+0020) seulement. Ajouter l'artefact « espace insécable avant les deux-points ».
5. Facultatif : l'accord cité doit figurer au registre des accords de l'arbre d'où la commande est jouée. La garde de calcul lit déjà ce registre.
6. `ERRATUM_SHA256` : corriger cette pièce par une v2, et non par un erratum à l'erratum, pour qu'une seule empreinte soit épinglée.

### C12 — mineur — Une commande v1 ou v2 jouée par erreur doit être refusée par procédure

- **Citation** : « l'empreinte imprimée est `0adb6efb…`, et le segment base64 décodé y est égal » (§ 8.2).
- **Source** : `relecture_v1.py`, l. 1076, 1088 et 1097 ; `commande_lecture_v2.py`, l. 251, 263 et 272. Les versions 1 et 2 impriment toujours une commande qui emporte l'amorce figée.
- **Problème** : une telle commande retomberait à l'identique et recréerait la branche de sortie. Il faudrait alors une seconde exception à R12.
- **Correction** : écrire à l'erratum 4, comme une condition d'arrêt : toute commande dont le segment décodé n'a pas l'empreinte `0adb6efb…` n'est pas jouée, quel que soit le lanceur.

### C13 — mineur — Variante : quatre précisions aux essais

1. **Artefact mal posé.** « `T05` quand la copie lue est `T05-r1` » (§ 5.6) ne donne « ni (a) ni (b) » que dans une table mélangée, où une autre famille porte son nom formé.
   - Dans une table toute nue, c'est la variante (a) : l'entrée figée lit `T05-r1` par `_familles_formees` (l. 1390 à 1403).
   - Préciser le montage de l'artefact.
2. **Montage de la branche de formation.** `variante` et le `preparer` recomposé lisent une branche de formation. Il faut décrire le monde fabriqué :
   - marches `…-b5f-formation-<n>`, avec `-x1` pour une relance ;
   - copies `-r1` ;
   - ligne de relance ;
   - résultats rattachés au manifeste.

   Ou réemployer, en le déclarant, le montage des essais figés de `preparer`.
3. **Témoin d'ordre** : voir C4.
4. **Parité.** Si une somme dépend de l'ordre des noms opaques, dire d'avance si l'égalité exigée est exacte.

### C14 — mineur — L'écart 5 est à nommer à la lettre

- **Citation** : « L'ouverture recomposée, si la table est suffixée. L'épreuve à vérité plantée inscrite (`EPREUVE-B5F`) porte sur l'entrée figée ; la recomposition est éprouvée par parité » (§ 9, écart 5).
- **Source** : texte scellé, l. 220 (« puis joue le programme de lecture figé ») et l. 356 (liste d'arrêt, point 10).
- **Correction** :
  - Nommer le point 7, troisième tiret, et la liste d'arrêt, point 10.
  - Corriger « aucun code neuf n'est joué » (§ 5.2, point 6) : `variante` est jouée dans tous les cas, et seule la lecture reste figée.

### C15 — mineur — La pesée des voies est à compléter ; le choix de B reste défendable

- **R12 est une règle gelée.** CLAUDE.md la range parmi les « règles gelées — sans discussion ». Un écart à un texte scellé, lui, est un nœud ordinaire de la hiérarchie. La voie B demande donc à Lazar une chose d'une autre nature, et le nœud 2 doit le dire. Il doit aussi rappeler que le défaut posé par la mère au lancement était la voie A.
- **Ce qui pèse pour B** :
  - en voie A, une garde figée tombe sur l'amorce embarquée (C10) ;
  - en voie A, les mandats de l'ouvreur et du lecteur du verdict changent probablement (C7).
- **Ce qui pèse contre B** :
  - la suppression sur le dépôt distant est définitive ;
  - tout clone garde des références périmées (le § 8.2 y répond) ;
  - une garde du dépôt distant peut refuser la suppression.
- **Durcir le geste 5** : conditionner la suppression à la tête H, pour ne supprimer que la copie vérifiée. Par exemple : `git push --force-with-lease=refs/heads/<nom>:<H> origin :refs/heads/<nom>`.
- **Dire d'où viennent les deux commits nommés** :
  - d'où vient la tête attendue `81061453` ;
  - ce qu'est `254f9280`, que la consigne nomme : selon toute apparence, le premier commit des traces ;
  - que le commit prouvé n'est pas H.

### C16 — mineur — L'erratum 4 au mandat est à compléter

Ajouter à la liste du § 8.5 :
- au § 4, point 3 : les empreintes du module, du lanceur et des essais de la v3, et celle de l'amorce corrigée, `0adb6efb…` ;
- au point 3 de l'erratum 2 : les fichiers d'essais rejoués, désormais ceux du § 6.3 ;
- au point 7 de l'erratum 2 : la coupure (C3) ;
- au § 5.4, pas 9 : la récupération forcée de la référence distante avant « detruire » ;
- la condition d'arrêt de C12.

### C17 — mineur — Texte scellé, point 8 (« sur une seule instance »)

- **Citation à donner** : le point 8 dit « Relecture, sur une seule instance, un seul chemin de calcul ».
- **Correction** : dire pourquoi la relance n'est pas un écart à cette phrase.
  - La première instance n'a fait aucune relecture : elle s'est arrêtée à l'étape 3, avant les paquets, le modèle et la marche.
  - Toute la relecture se fera sur une seule instance.

### C18 — mineur — Le nom de l'amorce sur l'instance (R12)

- **Fait** : l'amorce corrigée garde le nom `/root/amorce_b5f_lecture_v1.sh` et la ligne de journal « amorce de lecture v1 : empreinte … ». L'égalité à l'octet hors du segment base64 l'impose.
- **Correction** : le déclarer comme écart à R12, en disant que l'empreinte écrite au journal distingue les deux amorces.

## Nœuds pour Lazar

- **Nœud 1, relance : à recadrer.**
  - La relance elle-même est de droit : GO-2026-11-22-77 donne à une panne technique « droit à une relance sur le même accord ».
  - Ce qui demande le mot de Lazar, ce sont ses conditions : l'exception à R12 ou l'écart à « Données gardées », l'amorce embarquée, l'épinglage.
  - Citer GO-2026-11-22-117 et la marge (C3).
  - Donner, pour chaque option, son avantage et son inconvénient.
- **Nœud 2, branche de sortie : à compléter selon C15.**
- **Nœud 3, admission : juste.**
  - L'autre voie, rouvrir le code figé, demanderait une seconde ligne `CODE-LECTURE-B5F`, que le lecteur figé refuse comme clé en double (l. 142 et 143).
- **Nœud 4, variante d'ouverture : ajouter une troisième option.**
  - L'option : poser d'abord la question fermée à la session de formation (§ 5.7).
    - Si la réponse est « nue », la variante n'est pas écrite, et l'écart 5 disparaît avec elle.
    - Si la réponse est « nom formé », on code la variante.
  - Recommandation : cette option d'abord, si la session de formation est joignable.
  - La question ne livre rien de la table : la ligne de relance est déjà au registre.
- **Point neuf, pour la mère (ou pour Lazar avec le nœud 2)** : le sort de l'instance tombée (C2).

## Points vérifiés et justes, sans constat

- § 2.1 à 2.4 ; § 3.1 : lieu, octets, lignes, empreinte.
- § 4.1 : ce que vérifie chaque garde, dont le lecteur figé du registre (`engagement_v1.py`, l. 130 à 145).
- § 4.2 : les raisons d'écarter les variables d'environnement git (iii) et la ligne citée par l'accord de lecture (iv).
- § 5.1, contrôlé sur `lecture_v1.py` :
  - l. 529 à 532 et 551 : refus de l'entrée figée sur une table suffixée ;
  - l. 1365 à 1370 : la boucle de la copie lue saute en silence une clé suffixée ;
  - l. 396 : les noms suffixés déjà reconnus ;
  - l. 102 et 103 de `engagement_v1.py` : une table traduite à la main est refusée.
- § 6.3 : tous les comptes d'essais.
- Cloisonnement : la pièce ne porte aucun résultat de ce plan, aucun score, ni table ni sel. Les seules empreintes citées sont celles de l'engagement, d'un inventaire de traces et des commits.
