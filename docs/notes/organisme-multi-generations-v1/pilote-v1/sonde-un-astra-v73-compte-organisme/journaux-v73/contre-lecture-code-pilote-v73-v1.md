# Contre-lecture du jalon 2 du code v72 et du code v73 du pilote MR-2 (bloc gelé v73, sous-commande `sonde-un`) — v1

**Verdict : autorisable pour la sonde d'Astra** — le code ne peut pas demander plus de 1,835280 USD au fournisseur, en deux requêtes au plus, sans reprise à aucun étage ; aucune correction du code gelé n'est exigée avant l'appel. **La sonde peut partir, mais pas par la commande telle qu'elle est écrite sur cette machine à cette heure** : quatre conditions de lancement, toutes hors du code gelé (constats 1 à 4). Les corrections des essais et du banc (constats 5 à 8) ne changent aucune empreinte gelée et peuvent suivre.

- Développeur : modèle A ; contre-lecteur : modèle B ; A ≠ B. Je n'ai écrit aucun des fichiers lus.
- Début : `2026-11-14T10:01:31Z` (sortie de `date -u` de mon premier geste, recopiée) ; fin : `2026-11-14T10:08:25Z` (`date -u` de la commande qui écrit ce fichier).
- Objet lu : arbre `/home/user/arbre-organisme-co/organisme`, tête `b3a83da` (jalon 2 : `e6a3a11`), contre `e7daf32` : neuf fichiers « A », aucun modifié ni retiré, `git status --porcelain` vide ; empreintes d'objet du disque égales à celles des patchs (`e455caf` lanceur v73, `bcfd6e2` essais v73, `7366f83` banc v73, `28b61c9` sonde v72, `6d0718a` essais v72, `6f2cbac` banc v72) ; `bloc_gele()` rejoué = `EMPREINTES-code-pilote-v73.txt`, octet pour octet.
- Ce que je n'ai **pas** fait : ni pytest ni banc (un banc tourne) ; aucun réseau, aucune clé (la présence de cinq variables de transport a été testée par leur nom, aucune valeur lue ; la variable de clé n'a pas été touchée), aucune sonde, aucune commande git d'écriture, aucune recherche récursive. Preuves : lectures, et courts `python3 -I -B` sur des fonctions pures depuis `orchestrator/`. **Je n'ai vu aucun journal des essais v73 ni du banc v73** (constat 4) : ce que je dis des essais v73 est lu, pas observé.
- `O` = `/home/user/arbre-organisme-co/organisme/orchestrator` ; `T` = `/home/user/controle-ia-travail`.

## Réponses courtes

1. **Constat 2 de la v72 : corrigé.** `pole/sonde_pilote_v72.py`, lignes 67 à 74 (`motif_reflexion_absente` : `statut` et `usage_entier` vrais exigés) et 145 à 147. Rejoué sur les faits réels d'Astra du relevé v71 (429, `insufficient_quota`, deux appels) : `statut` faux, motif nommé `None` ; le motif général reste seul. **Constat 3 : corrigé à moitié** — l'essai `test_consignes_v12_mot_pour_mot` existe et N21 le vise, mais N18 vise toujours l'ancien essai et survit (constat 5). **N21 à N27 : présentes** (`essais/mutations_pilote_mr2_v72.py`, lignes 175 à 188), textes égaux à ceux proposés ; N27 adaptée au nom `c` de la fonction neuve, juste.
2. **Bloc v73 : aucun identifiant de modèle** (rejoué : aucun des quatre `modele` de la configuration dans le bloc, ni préfixe de famille de fournisseur). **Identité gelée : oui**, par l'empreinte du fichier de configuration au bloc (`f69503dd…`, ligne 20 d'`EMPREINTES`), fichier qui est dans `FICHIERS_GELES` et que le mode réel impose (`exiger_mode_reel`, ligne 232). **Le mode réel exige le bloc v73** : marqueurs v73 (ligne 85), bloc v72 refusé (« bloc « empreintes-du-code-pilote-v73 » absent », rejoué), et le relevé de la sonde complète doit porter les empreintes du code dont le lanceur v73 (`attendu_du_releve`). Réserve : constat 9.
3. **`sonde-un`** : la ligne réelle passe le lecteur gelé (constat 1 pour le fichier lu) ; dépense : bornée à 1,835280 USD demandés, voir « Dépense » ; second lancement : refusé par le registre des lancements, sauf `--reprise` (constat 6) et sauf registre perdu (constat 3) ; relevé pris par le mode réel : non (version « releve-sonde-un-relais-v73 » ≠ « releve-sonde-pilote-v72 », premier contrôle après le compagnon ; ni `borne_courte`, ni `pieces_sha256`, ni huit appels ; `bloc --releve-sonde` passe par la même fonction).
4. **Essais et banc de `sonde-un`** : U01 à U08 et B01 à B03 visent chacune la bonne garde et leur essai attendu les tue (lecture, constat 7) ; mais quatre gardes n'ont ni artefact ni mutation (constats 6 et 7), dont l'arrêt après envoi et l'amont en 429, le cas le plus probable.
5. **Commande** : juste dans sa forme ; insuffisante sur le registre des GO lu, les noms de variables vides, les écrits exigés par la ligne (constats 1 à 4).

## Dépense : peut-on dépasser 2 USD ?

Chaîne lue de bout en bout (`sonde_un` → `lancer_relais` → relais → `appel_reel` ; `appeler` → commande) :

- Ligne lue au montant **exact** 2 USD (`SONDE_UN`, ligne 426 ; `verifier_go_v66`, ligne 146). Rejoué : la même ligne demandée à 1,84 ou à 2,01 est refusée.
- `exiger_pire_sous_part` (ligne 433) : pire cas 1,811240 + 0,024040 = **1,835280** ≤ part **1,84** ≤ ligne **2,00** (rejoué sur la configuration v12).
- Le relais est lancé avec `--plafond-usd 1.84 --max-appels 2` (ligne 462) et son état est contrôlé sur ces deux valeurs avant la consignation (ligne 468 ; `controler_etat_relais`, lignes 441 et 451). Le relais réserve son propre pire cas avant chaque envoi (`relais_pilote_v70.py`, lignes 375 à 385) : 1,811180 puis 0,024030 pour les consignes réelles (94 et 99 octets), somme 1,835210 ≤ 1,84 ; un troisième appel rend 429 sans rien envoyer ; un coût lu au-dessus du pire cas verrouille le relais (409) et arrête la sonde.
- **Aucune reprise** : `appel_reel` « sans reprise » (un `ouvreur.open`, ligne 206) ; la commande n'ouvre qu'une fois (ligne 228) ; `sonde_un` appelle `PR.appeler` une fois par élément de `S.APPELS` (deux). Une erreur d'amont ou de transport est comptée au pire cas, pas rejouée.
- Chaque requête porte `max_completion_tokens` = 36 000 puis 256, un seul message, aucun outil.

Donc : **le code ne demande jamais plus de 1,835280 USD**, soit 0,164720 USD sous la ligne. Ce que le code ne peut pas garantir, et qu'il faut écrire au devis :

- (a) que le prix réel soit au plus celui de la configuration (10 / 50 USD par million, dit « barème prudent, SUPPOSÉ » au champ `sources` ; la ligne de GO cite un « prix standard lu, R-2677 ») ;
- (b) que le plafond du fournisseur couvre la réflexion (règle gelée d'Astra : « comprise », écrite « de mémoire, non vérifiée » — c'est ce que la sonde vérifie). Si la réflexion sortait du plafond, le code le **constaterait** (verdict ≠ règle, ou coût excessif et arrêt avant le second appel), il ne l'empêcherait pas. Sur un dénombrement d'une phrase, l'ordre de grandeur resterait de centimes.

Coût attendu : 0 USD réel si le crédit n'est pas rechargé (429 ; le relevé **comptera** 1,835 USD au pire cas, comme la v71 a compté 1,83447 : ce n'est pas une dépense) ; quelques centimes à quelques dizaines de centimes sinon.

## Constats

### 1. BLOQUANT pour la commande telle qu'écrite (hors code, sans risque de dépense) — sur cette machine, `registres/go.md` ne porte pas la ligne

- Preuve (10:04 UTC) : `git -C T rev-parse --abbrev-ref HEAD` → `lot/compte-organisme-v1` (`9007576`) ; `grep -c "^| GO-2026-11-14-02 " T/registres/go.md` → `0` ; `git -C T show refs/heads/main:registres/go.md | grep -c …` → `0` (main local `a9119b6`) ; seule `refs/remotes/origin/main` (`d871d51`, 09:51:45 UTC) porte la ligne, ligne 321, une seule occurrence.
- Effet : la commande prévue rend « refus : GO astra : A15 : GO-2026-11-14-02 absent du registre », code 2, **avant** tout dossier, tout relais et toute consignation (`lire_go_de_lignes`, ligne 452, précède `os.makedirs`, ligne 458). Rien n'est dépensé ni consommé ; mais « main à jour » n'est pas vrai ici.
- La ligne elle-même passe : rejoué sur le registre d'`origin/main` extrait dans un fichier provisoire, par le lecteur gelé et la constante du lanceur (`PR.lire_go_de_lignes(L.SONDE_UN, fichier, {"astra": "GO-2026-11-14-02"})`) → accordée 2026-11-14, échéance 2026-11-30, type « calcul », par « Lazar », plafond « 2 USD » lu 2.0 (« montant seul »), aucune extension, aucune révocation, huit colonnes, les deux mots présents (« sonde », « seul relais Astra ») ; refusée la veille (2026-11-13) et le 2026-12-01, admise le 30.
- Correction (au choix de la mère, je n'ai fait aucune écriture git) : lancer depuis un arbre de travail dont `registres/go.md` est celui d'`origin/main` ; ou passer à `--registre-go` le chemin absolu d'un fichier extrait d'`origin/main` hors dépôt, son commit écrit à l'ordre de lancement. Vérifier d'abord : `grep -c "^| GO-2026-11-14-02 " FICHIER` → `1`.

### 2. MAJEUR (hors code) — la ligne de GO dit « code v72 après ses corrections et leur relecture » ; la commande lance le code v73

- Fichier : registre des GO, ligne 321 (périmètre) ; `demonstrations/pilote_mr2_v73.py`, lignes 4 à 10.
- Fait : la sous-commande `sonde-un` n'existe pas dans le lanceur v72 ; le v73 est le v72 du jalon 2, plus le bloc sans identifiant (R-2690) et `sonde-un`. Le code le dit (R-2694), la ligne non. Le périmètre exige aussi « commande exacte et devis écrits avant l'appel » et « une seule invocation ».
- Correction : une phrase de la mère à l'ordre de lancement (« le code v73 est le code v72 corrigé visé par la ligne ; relu par la présente ») ; la commande exacte et le devis écrits et scellés avant l'appel — je ne les ai vus dans aucune pièce de `pieces-v73/`. Le devis porte les deux réserves (a) et (b) ci-dessus et la phrase « un relevé à 429 compte 1,835 USD sans rien dépenser ».

### 3. MAJEUR (hors code) — variables vides sous `env -i`, registre des lancements absent de la machine

- `NOM="$NOM"` passe une valeur **vide** quand la session qui lance n'a pas le nom. Clé vide : relais non branché, refus « état non conforme (['cle_presente']) » avant la consignation — sans dépense, mais le dossier de sortie est déjà créé (ligne 458) et doit être retiré avant de relancer. **`HTTPS_PROXY` ou `SSL_CERT_FILE` vides : pire** — le relais part, le lancement est consigné, la requête échoue au transport (connexion directe ou certificat du mandataire non reconnu), le relais rend 502 compté au pire cas : **la ligne est consommée, 0 USD dépensé, rien d'appris sur le crédit**. Dans ma session : `HTTPS_PROXY`, `NO_PROXY`, `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE` présents, `HTTP_PROXY` absent (sans effet : urllib ignore une valeur vide ; `REQUESTS_CA_BUNDLE` et `HOME` n'arrivent pas au relais, filtre `ENV_FILTRE`). Cela ne dit rien de la session qui lancera.
- La forme `env -i` avec passage par nom n'a jamais porté un appel réel (la v71 a été lancée sans `env -i`, selon le constat 7 de la contre-lecture précédente) ; l'essai à sec du jalon 2 vise la sous-commande `sonde`, pas `sonde-un`, et ne teste que les noms de clés.
- `/home/user/hors-depot` n'existe pas sur cette machine (10:04 UTC) : ni le registre des lancements (celui de la v71 n'y est pas), ni le dossier de sortie. Le code s'en accommode (`os.makedirs` crée le parent, le registre est créé à la consignation). Mais la garde « une seule exécution par ligne » ne vaut que tant que ce fichier vit et que le même chemin est repassé : un conteneur remplacé, ou un autre chemin, et un second lancement passe.
- Correction : dans la même session et juste avant l'appel, une ligne qui n'imprime que des noms, par exemple `for v in HTTPS_PROXY SSL_CERT_FILE OPENAI_API_KEY; do [ -n "${!v:+x}" ] || echo "$v vide : ne pas lancer"; done` ; `ls -d /home/user/hors-depot/sonde-un-astra-v73` → absent ; port 8814 libre ; aussitôt après la sonde, recopier la ligne du registre des lancements (elle ne porte aucune clé) dans une note du dépôt, avec le relevé.

### 4. MAJEUR — aucun journal des essais v73, du banc v73, ni essai à sec de `sonde-un`

- `/home/user/arbre-organisme-co/journaux/` (liste simple) : essais v72 du jalon 2 (« 129 passed, 210 subtests passed », code 0, 09:34 UTC), banc v72 du jalon 2 en cours (43 mutations tuées pour la raison attendue à 10:05 UTC, N18 pas encore jouée) ; **rien pour la v73** ; `pieces-v73/` ne porte ni rapport du développeur, ni journal.
- La ligne exige une relecture du code « après ses corrections » : une lecture ne remplace pas les essais passés. Par lecture, `SondeUnRelais.test_sain` doit passer (la doublure rend pour Astra 42 jetons dont 40 de réflexion, puis 256 dont 200, formes déjà admises par la sonde complète de la v72).
- Correction avant l'appel : le journal daté des essais v73 (tous passés, avec la commande et la tête `b3a83da`), et celui du banc v73 (28 mutations tuées pour la raison attendue). Si un essai de `SondeUnRelais` échoue, ne pas lancer.

### 5. MAJEUR (banc, sans effet sur la sonde) — constat 3 de la v72 corrigé à moitié : N18 survit toujours (prédiction)

- Fichiers : `essais/mutations_pilote_mr2_v72.py`, lignes 171-172 (N18, essai attendu resté `test_configuration_v12_seules_les_consignes_changent`) ; `essais/test_pilote_mr2_v72.py` (l'assertion mot pour mot est dans un essai **neuf**, `test_consignes_v12_mot_pour_mot`, pas dans l'ancien).
- Preuve : les quatre assertions de l'ancien essai rejouées sur la configuration mutée par N18 → `[True, True, True, True]` ; le banc resserre la sélection sur l'essai attendu (`selection_effective`, ligne 227) ; issue attendue « survit », code du banc 1. À confronter au journal du banc en cours.
- Correction (une occurrence) : dans N18, `'V72', 'test_configuration_v12_seules_les_consignes_changent'` → `'V72', 'test_consignes_v12_mot_pour_mot'`. Le fichier du banc n'est pas gelé : aucune empreinte du bloc ne change.

### 6. MAJEUR (à corriger avant toute reprise ; la commande prévue ne l'emploie pas) — `--reprise` permet un second lancement sous la ligne de 2 USD, relais neuf à 1,84 USD

- Fichier : `demonstrations/pilote_mr2_v73.py`, lignes 457 et 637-638 ; `pole/sonde_pilote_v71.py`, `exiger_premier_lancement` (lignes 419 à 444).
- Fait : avec `--reprise R-NNNN --registre-decisions D` (une ligne du registre des décisions citant l'identifiant et « reprise de la sonde »), `sonde_un` relance un relais au plafond entier de 1,84 USD, sans déduire ce que le premier lancement a compté : cumul possible 3,670560 USD sous une ligne de 2 USD, dont le périmètre dit « une seule invocation ». C'est le seul chemin du code vers plus de 2 USD ; il demande un geste voulu et une décision écrite. Aucun essai ne le couvre pour `sonde-un`.
- Correction : dans `sonde_un`, refuser toute reprise (`if args.reprise is not None: raise P.Refus("sonde d'un relais : aucune reprise sous une ligne à une seule invocation")`), ou retirer les deux options du sous-analyseur ; un essai (artefact : registre déjà employé et reprise écrite → refus) ; une mutation. D'ici là : ne jamais passer `--reprise` à `sonde-un` ; toute seconde sonde d'Astra demande une ligne neuve.

### 7. MAJEUR (essais, R5) — gardes de `sonde-un` sans artefact ou sans mutation

Tableau des gardes de `sonde_un` (lignes 437 à 512) :

| garde | cas sain | artefact | mutation |
|---|---|---|---|
| proposeur hors de `SONDE_UN` | oui | oui (`fable52`) | U01 (tuée : `KeyError`, code 1 ≠ 2) |
| dossier de sortie existant | oui | oui | **aucune** |
| ligne absente, autre montant, périmètre | oui | oui (trois cas) | U02 (périmètre) ; **aucune sur la lecture elle-même** |
| ligne hors période, non accordée par Lazar | — | **aucun dans la classe** (tenus par le lecteur gelé, rejoué ici sur la ligne réelle) | — |
| pire ≤ part ≤ ligne | oui (fonction) | oui (fonction) | U03 (fonction) ; **l'appel, ligne 456, n'a ni artefact ni mutation** |
| ligne déjà employée | oui | oui (second lancement) | U04 |
| plafond et nombre d'appels du relais (1,84 ; 2) | lancé ainsi, **jamais affirmé au relevé** | **aucun** | **aucune** |
| état du relais | oui | oui (clé absente) | U08 |
| consignation avant le premier appel | oui | oui (rien consigné sans clé) | U05 |
| arrêt après envoi : relevé partiel, appel porté, code 3 | — | **aucun** | **aucune** (a3a et a3b visent `sonde`) |
| amont en erreur (429 réel de la v71) de bout en bout | — | **aucun** (la doublure ne rend que 200 ou 401) | — |
| motif nommé porté au relevé | oui | oui | U06 |
| identité sans `modele` | oui | — | U07 |
| relevé refusé par le mode réel | oui (version) | — | **aucune** |

- Portée : aucun de ces manques n'ouvre une dépense — le plafond est tenu par le relais gelé, inchangé, et le chemin 429 a été parcouru pour de vrai par la v71 avec les mêmes relais, commande et lecture des pièces (relevé v71 : deux faits d'Astra, 429, portés) ; j'ai rejoué ces faits dans `S.conclusions` (v72) : `statut` faux, motif `None`. Mais le gestionnaire d'arrêt de `sonde_un` (lignes 481 à 495) est une recopie de celui de `sonde`, et une recopie non éprouvée est l'endroit où un défaut se loge.
- Corrections (fichier d'essais et banc, non gelés) : dans `test_sain`, `self.assertEqual((rel["relais"]["astra"]["plafond_usd"], rel["relais"]["astra"]["max_appels"]), (1.84, 2))` ; un essai « Astra 429 aux deux appels » sur la doublure (surcharge rendant 429 `insufficient_quota`) : code 0, `partiel` faux, `statut` faux, `motif_reflexion` `None`, ligne consignée ; un essai « coût excessif au premier appel » : code 3, `partiel` vrai, un seul fait porté, une seule requête reçue par la doublure ; un essai du pire au-dessus de la ligne sur une configuration copiée. Mutations proposées, chacune présente une seule fois (vérifié par `str.count`) :

| id | avant | après | essai attendu |
|---|---|---|---|
| U09-relais-au-plafond-du-pilote | `python=sys.executable, plafond=part, max_appels=len(S.APPELS))` | `python=sys.executable, max_appels=len(S.APPELS))` | `test_sain` |
| U10-go-non-lue | `    go = PR.lire_go_de_lignes(SONDE_UN, args.registre_go, {nom: args.go_sonde})\n` | `    go = None\n` | `test_artefacts` |
| U11-pire-non-exige | `    exiger_pire_sous_part(pire, part, SONDE_UN[nom]["montant_usd"])\n` | (vide) | l'essai neuf du pire au-dessus de la ligne |
| U12-releve-a-la-version-du-mode-reel | `VERSION_RELEVE_UN = "releve-sonde-un-relais-v73"` | `VERSION_RELEVE_UN = "releve-sonde-pilote-v72"` | `test_sain` |
| U13-dossier-existant-admis | `        raise P.Refus("sonde d'un relais : dossier de sortie existant")\n` | `        pass\n` | `test_artefacts` |
| U14-refus-apres-envoi-sans-releve | `        if isinstance(x, P.Refus) and not partis:\n` | `        if isinstance(x, P.Refus):\n` | l'essai neuf « coût excessif » (ou un refus après envoi) |
| U15-appel-parti-non-porte | `                faits.append(S.faits_depuis_les_pieces(conf, nom, en_cours, args.sortie))\n` | `                pass\n` | l'essai neuf « coût excessif » |

### 8. MINEUR — R5 du constat 2 de la v72 : l'artefact d'Astra est rejoué en unité, pas sur la doublure

`test_motif_reflexion_absente` (essais v72, lignes 2583 à 2605) bâtit à la main deux faits à 429 ; la contre-lecture précédente demandait une sonde sur la doublure où Astra rend 429. La garde est juste et N27 la vise ; l'essai de bout en bout demandé au constat 7 comble les deux.

### 9. MINEUR (à trancher par la mère avant la sonde complète, sans effet sur la sonde d'Astra) — R-2690 et les pièces autres que le bloc

Le bloc est propre ; le relevé de `sonde-un` aussi (identité sans `modele`, état du relais sans `modele` ; il porte l'identifiant servi d'Astra dans ses faits, qui n'est pas de Claude). Mais le relevé de la sonde **complète** (`S.releve`, `identite` avec `modele` ; `exiger_relais_prets`, champ `modele` ; faits `modele_servi`) et la configuration elle-même portent les identifiants des quatre proposeurs. Si « aucun identifiant dans les pièces » vise aussi ces fichiers, le v73 ne le tient pas ; si la décision ne vise que le texte scellé et son bloc, rien à faire. L'affirmation « l'identité reste gelée » repose sur la configuration : le lecteur du texte scellé doit ouvrir ce fichier pour savoir quels modèles ont été appelés.

### 10. MINEUR — textes et restes

- `sonde_un`, docstring (ligne 440) : « hors période » est tenu par le lecteur, sans essai dans la classe.
- Relevé de `sonde-un` : `depense_usd` additionne des coûts comptés au pire cas quand l'amont refuse ; le champ `a_lire_hors_du_code` le dit à moitié. Ajouter « un appel refusé par l'amont est compté au pire cas ».
- Un refus avant la consignation mais après `os.makedirs` (relais qui ne démarre pas, port pris, clé absente) laisse un dossier de sortie vide : le retirer à la main avant de relancer ; ce n'est pas une invocation (rien de consigné, rien d'envoyé).
- La valeur de la clé passe par la ligne de commande d'`env` le temps de son exécution (visible des autres processus de la machine un instant) : forme habituelle, à savoir.
- Constats 7 (journal sans commande ni empreinte) et 8 (textes) de la contre-lecture précédente : non repris au jalon 2, toujours ouverts ; sans effet ici.

## La commande prévue

Forme juste : interpréteur `/usr/local/bin/python3` (3.13.18, numpy 2.5.3 importé sous `-I`, rejoué ; sortie en UTF-8 sous `env -i`, rejoué), `-I -B`, clé passée par son nom, `--proposeur astra`, `--go-sonde GO-2026-11-14-02`, registre des lancements et sortie absolus hors dépôt (`exiger_hors_depot` : chemin absolu, hors de l'arbre de l'organisme, aucun parent avec `.git` — `/home/user/hors-depot` convient). Pas de `--reprise` : juste. À changer ou à garantir : le registre des GO lu (constat 1).

Ce que le résultat dira, dans tous les cas la ligne est consommée :

- code 0, `statut` faux, `statut_amont` 429 aux deux appels : crédit toujours absent ; 0 USD réel ;
- code 0, toutes les conclusions d'Astra vraies, verdict « comprise » : crédit vérifié, règle confirmée ;
- code 0, `motif_reflexion` non nul : Astra répond sans réfléchir ; crédit vérifié, règle non confirmée ;
- code 3, relevé partiel : arrêt (coût excessif, témoin, pièce) ; lire `arret`.

## Avant l'appel, dans l'ordre

1. Journal des essais v73 passés et banc v73 lu (constat 4).
2. Phrase de la mère sur « code v72 » / v73 ; commande exacte et devis écrits et scellés (constat 2).
3. Registre des GO lu = celui d'`origin/main`, `grep -c` → 1 (constat 1).
4. Dans la session qui lance : les trois noms non vides, dossier de sortie absent, port 8814 libre (constat 3).
5. Une seule invocation ; aucun `--reprise` ; après : relevé, compagnon et ligne du registre des lancements recopiés au dépôt ; coût rapproché de la console par Lazar.
