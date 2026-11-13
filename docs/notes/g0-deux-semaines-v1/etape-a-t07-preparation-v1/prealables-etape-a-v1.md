# Préalables de l'étape A de T0.7 (variante B) — état vérifié le 13 novembre 2026 — v1

- **Auteur** : préparateur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy`. J'ai lu des pièces de T0.7 : je suis exclu ensuite de tout rôle de lecteur de P3-bis.
- **Mandat** : message de la mère qui suit R-2555 (`registres/decisions.md` l. 2514, mots de Lazar « A (a) go » : jouer
  maintenant l'étape A de T0.7 sous GO-2026-11-10-04 et GO-2026-11-10-06).
- **Quand** : vérifications faites le 2026-11-13 de 18:16 à 18:30 UTC (`date -u`). Tête de `main` : `07b4d7c5` au début
  (égale au distant, `git ls-remote`), puis `73da9bd3` (R-2556) et `b4d375c9` (R-2557), commits de la mère pendant ce
  travail, sans effet sur les pièces ci-dessous (registres relus et empreintés à `b4d375c9`).
- **Ce que je n'ai pas fait** : aucune dépense, aucun appel à un fournisseur (ni Vast.ai ni Hetzner), aucune écriture git
  dans le dépôt, aucune valeur de clé lue. Sorties de 7b : **noms et empreintes seulement** (clone partiel à une profondeur,
  sans extraction, dans mon bac à sable ; `git ls-tree --name-only` sur des chemins **nommés** ; `sha256sum` du seul
  manifeste que P2 désigne) ; `diag/<run>/` de 7b **jamais listé** (ordre, § 2.1) ; aucun contenu de `diag/`, `runs/` ou
  `donnees/` de 7a ou de 7b ouvert ; aucun chemin sous embargo touché ; aucune recherche récursive.

## 0. Verdict

1. **L'ordre à jouer est le brouillon 9, pas le brouillon 5 que nomme le mandat** : le texte scellé de T0.7 désigne
   `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9.md` (`374332976304d08af7c1b941d8798877d34f9e30b3945ba2be3ac19189740402`) ;
   le brouillon 5 ne peut pas tourner sous ce texte (§ 1). Le brouillon 9 porte **douze marqueurs ouverts** et doit être
   rempli puis scellé avant la création (R-2321).
2. **Préalables non remplis aujourd'hui** : ordre rempli et scellé (Q-1) ; ligne `RUN-CONFIRMATION-T06` (Q-8) ; extrait et
   ligne `GO-LECTURE-T07` (Q-9) ; écrit daté de la mère sur le périmètre des jeux (Q-10) ; ligne d'engagement de dépense
   (Q-12) ; nombre de lignes des mesures de 7b, P14 (Q-15) ; identifiant de la session fille (Q-1). **À vérifier par la
   fille, non vérifiables d'ici** : `vastai` 1.8.3, jetons par leur nom, inventaire (Q-17), crochet chargé (Q-20), crédit
   (Q-21).
3. **Aucun préalable n'exige un mot de Lazar**, sauf si le crédit du compte de location ne couvre pas le pire cas (Q-21 :
   recharge) ou si la mère veut s'écarter de l'ordre sur le choix de l'hôte (§ 5, point 3).

## 1. Quel ordre : brouillon 5 ou brouillon 9

| Pièce | Empreinte relevée (`sha256sum`) | Compagnon | Ce qu'en disent les registres et le texte scellé |
|---|---|---|---|
| `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` | `d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b` | égal (`sha256sum -c` : OK) | retenu le 10 novembre (R-2258, R-2260, l. 2216 et 2218) ; **remplacé** : brouillons 6 à 9 (R-2306, R-2310, R-2314, R-2317, l. 2264 à 2275) |
| `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9.md` | `374332976304d08af7c1b941d8798877d34f9e30b3945ba2be3ac19189740402` | égal (OK) | rendu R-2317 (l. 2275), vérifié mécaniquement « conforme » (R-2318, l. 2276) ; **cité par le texte scellé de T0.7** l. 2677 (section « Module », « Ordre d'exécution de l'étape A ») et l. 3397 (marqueur `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07`, rempli au candidat 5) ; R-2321 (l. 2279) : « ordre d'exécution, brouillon 9, à remplir (…) et à sceller avant la création de l'étape A » |

Pourquoi le brouillon 5 ne peut pas tourner : il appelle le script v2 (`e68d3306…`), qui appelle `lecture_v2` ; or le texte
scellé fixe la configuration v8 (`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`), que seule `lecture_v4` accepte
(brouillon 9, § 0 ter, ligne « Script de l'instance », et § 13, S-12 : « le v2 appelle `lecture_v2` (l. 302, 357, 367,
372), qui refuse la configuration v7 » ; § 1, ligne « Configuration » : la v8 n'est acceptée que par `lecture_v4`). Jouer
le brouillon 5 serait en outre un écart à une pièce que cite un préenregistrement scellé : nœud. **Toute la suite de ce
document vaut pour le brouillon 9.**

## 2. Préalables de l'ordre (brouillon 9), un par un

État : **rempli**, **non rempli** (qui le remplit), **à la fille** (non vérifiable d'ici sans appel au fournisseur).
Lignes de registre citées par leur numéro dans le fichier à `b4d375c9`.

| # | Préalable (ordre) | État le 2026-11-13 | Pièce qui le prouve |
|---|---|---|---|
| Q-1 | **Ordre rempli et scellé** (12 marqueurs ; § 12) ; identifiant de la session fille (`ID_SESSION_FILLE`) | **non rempli** (mère : version remplie sous un nom neuf, R12 ; valeurs proposées dans `remise-marqueurs-etape-a-v1.md`) | `grep -o '<<[A-Z0-9_]*>>'` sur le brouillon 9 : 12 marqueurs, une occurrence chacun (l. 99, 214, 258, 276) |
| Q-2 | P5 — **`SCELLEMENT-T07`** : une ligne | **rempli** | `registres/scellements-v1.md` (`1eaab114be2b8d44797645cf0791f9dd639cd13195784f170235f9d16259d3d8`) l. 8 : `\| SCELLEMENT-T07 \| 2026-11-11T07:11:42Z \| prereg/T0.7-sondes-v0-v1.md \| d7d180ec… \|` ; texte `prereg/T0.7-sondes-v0-v1.md` = `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` = compagnon |
| Q-3 | Configuration (`CFG`, § 1) ; empreinte canonique (`EMPREINTE_CONFIG_T07`) ; six chemins cités (§ 4.1, « ATT valable pour S7 ») | **rempli** | fichier `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` = `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` = compagnon = `git show S7:…` ; `PYTHONPATH=src .venv/bin/python -m controle_ia.t07.lecture_v4 empreinte-config …` → `0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12`, code 0 (égale au texte scellé, l. 749) ; chemins cités à S7 = les six attendus par la commande du § 4.1, à l'octet |
| Q-4 | P9, P13 (ii) — **script de l'instance** `scripts/etape_a_t07_variante_b_v4.sh` à `4b17d1f0…` | **rempli** | `sha256sum` : `4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6` ; inchangé entre S7 et `main` (`git diff --quiet`) ; sans compagnon (comme v1 à v3 ; R-2319 : P9 contrôle l'empreinte du § 1) |
| Q-5 | P9 — **code** : C7 ancêtre de S7 ; `src/` de C7 égal à celui de `SRC7` ; `git diff --quiet C7 S7 -- src tests` ; S7 ancêtre de `main` ; essais CLC-04 et GARDES-CODE-01 à S7 | **rempli** | C7 = `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (R-2316, l. 2274) ; S7 = `2576442b0e7a1e8089620199edb2ac638d5d4c1d` (commit « T0.7 SCELLÉ (d7d180ec) », 2026-11-11 07:12:50Z, R-2321) ; `a621dcd3` ancêtre de C7, C7 ancêtre de S7, S7 ancêtre de `main` : vrai ; différence C7–S7 sur `src` et `tests` : vide ; arbre `src/` de `a621dcd3`, C7, S7 et `main` : `5faa6d9d575445cd0db6cbb6ede57a91e442a081` ; arbre `tests/` de C7 et S7 : `7ab3214794b4d9e2f39e786702e96be6f5b65df9` ; `tests/test_t07_ouvrir_reel_concepts_v1.py` et `tests/test_t07_tirages_degeneres_v1.py` présents à S7 |
| Q-6 | P6 — **`CODE-T07`** : une ligne, `registres/code-t07/CODE-T07-v2.json`, champ `commit` = C7 | **rempli** | `scellements-v1.md` l. 7 (2026-11-11T05:40:34Z, `d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c`) ; fichier = compagnon ; `commit` = `b4cd9953…`, 26 fichiers ; `PYTHONPATH=src .venv/bin/python -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md` (18:21 UTC) : « CODE-T07 conforme : commit b4cd9953…, 26 fichiers, tête du dépôt 73da9bd3… », code 0 |
| Q-7 | P4 — aucune ligne `GO-ETAPE-A-T07` (ou lecture de l'une ou l'autre) | **rempli** | compte `0` (commande du § 4.1 rejouée sur `scellements-v1.md`) |
| Q-8 | P2 — **`RUN-CONFIRMATION-T06`** : une ligne, `runs/<RUN6>/manifeste.json`, même fichier sur `BR7B` | **non rempli** (mère : T0.7 l. 2199, « session mère, à la sortie scellée de 7b » ; T0.6 `prereg/T0.6-organismes-v0-v1.md` l. 770) | compte `0` ; valeurs prêtes : chemin `runs/20261111-151701-t06-reel/manifeste.json`, empreinte `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` (R-2413, l. 2371 ; recalculée sur la branche, § 3) ; le module vérifie aussi `config.go_id` = GO-2026-11-02-28 (T0.7 l. 2199 ; non lu par moi) |
| Q-9 | P4 — **`GO-LECTURE-T07`** : une ligne, extrait scellé d'une ligne de `registres/go.md` qui nomme GO-2026-11-10-06 | **non rempli** (mère : T0.7 l. 2203) | compte `0` ; dossier `registres/go-extraits/` absent de `main` (`git ls-tree`) ; à écrire : `registres/go-extraits/GO-LECTURE-T07-v1.md` = la ligne l. 296 de `registres/go.md` (`83ffae4661fe135ba08fa5e5ce37b3e4478ddbcf6ca8f05a1fe4d7f9b8c5564b`) à l'octet, une seule ligne non vide (`registre_v1.extrait_est_une_ligne_de`, l. 229-238) ; si le fichier est exactement cette ligne suivie d'un saut de ligne, son empreinte sera `8893d8df3b7366aa9d9eb84548747c586f2798c40956a1baa0d149b8d9630b52` (calculée sur `grep '^\| GO-2026-11-10-06 \|' registres/go.md`) ; puis compagnon, puis ligne au registre |
| Q-10 | P3 — **périmètre des jeux** (`PER`) et **écrit daté de la mère** (attendre ou non `-JC` et les concepts), recopié au journal avant la création | lignes : **rempli** (`PER` = `JD,JA`) ; écrit : **non rempli** (mère) | `scellements-v1.md` l. 3 (`SCELLEMENT-JEUX-T07-JD`, `32f41288…`) et l. 4 (`-JA`, `5b040920…`), 2026-11-10T08:22:50Z ; fichiers aux empreintes, compagnons égaux ; `journal-verification-v2.txt` présent dans `donnees/t07-jeux-synthetiques-v2/` ; `-JC` et `SCELLEMENT-CONCEPTS-T07` : `0` ; la commande du § 4.1 rejouée rend `PER=JD,JA` ; option (c) : étape A « sans concepts » (T0.7 (b) 1, l. 1619) |
| Q-11 | P7 — `SCORES-T07`, `SONDES-T07` absentes ; `VERDICT-P3BIS` et journal de P3-bis relevés | **rempli aujourd'hui** (voir § 4) | `SCORES-T07` 0, `SONDES-T07` 0, `VERDICT-P3BIS` 0 ; `registres/ouvertures-p3bis-v1.md` absent de `main` (vaut « aucune ouverture », T0.7 l. 1710-1711) ; `registres/prealables-p3bis-v1.md` (`ca7e743a2082882a21e3cdbe22dfeaf88473b463d2c2107a561f95147726d7ab`) : une ligne, `GARDE-ADAPTEE-T07-P3BIS`, 2026-11-11T07:12:25Z, `prereg/T0.7-sondes-v0-v1.md` |
| Q-12 | P8 — **engagement** sous GO au registre des dépenses ; `ANT0` ≤ 3,6 USD | `ANT0` = 0 : **rempli** ; engagement : **non rempli** (mère, avant la première minute de carte, T0.7 l. 2087-2089) | `registres/depenses.md` (`4e61067974100bbdb279825e69b7e717891786cccad70e6138d04f8ab5dc5ef7`) : `grep -cE "GO-2026-11-10-04\|GO-2026-11-10-06"` = `0` ; la commande du § 4.1 exige au moins une ligne |
| Q-13 | P12 — **`ATT`** valable pour S7, écrit daté de la mère (valeur, commit de la mesure, arbres) recopié au journal | **rempli, sous réserve** (§ 5, point 3) | mesure à C7 : R-2319 (l. 2277), rapport `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/mesure-att-c7-v1.md` (`b70c77fd249dc4cea4adf45427afee8c6406ce534c0798329e50ce4cbe23455f`) ; décision de la mère : `479 passed, 2 skipped, 4 xfailed` ; arbres de C7 : R-2316 ; S7 a les mêmes arbres ; entre C7 et S7, sous les chemins que nomme P12 (`docs/notes/g0-deux-semaines-v1/`, `brouillons/T0.7-*`, `prereg/`, six chemins cités), **aucun fichier modifié**, des ajouts seulement (texte scellé, configuration v8, pièces du candidat 5, mesure de `ATT`, notes de P3-bis) ; `registres/` modifié, qu'aucun essai de T0.7 ne lit (ordre, § 11 bis) : la lettre de P12 n'exige pas de remesure ; jugement final à la mère |
| Q-14 | P13 — (i) révision du modèle de 7b égale à celle de P3 ; (ii) script ; (iii) `SRC7` et écrit de la mère | (ii), (iii) : **rempli** ; (i) : **à la fille** | (iii) R-2316 : « `SRC7` = `5faa6d9d…` = arbre de `a621dcd3`, dernier commit contre-lu » ; R-2321 : `COMMIT_SRC_CONTRE_LU_T07` = `a621dcd3` ; (i) exige de lire un champ du manifeste de 7b : interdit à ce préparateur, fait par la fille (§ 4.1, n'imprime que « égale » ou « autre ») |
| Q-15 | P14 — **nombre de lignes** des mesures de 7b (un entier), sous ≈ 7 378, lu par la mère avant la création | **non rempli** (mère) | aucune ligne de registre depuis R-2317 ; script versé `docs/procedures/ordre-execution-etape-a-t07-p14-nombre-lignes-v1.py` (`f6fd192ed8536e69989e0902a59db8840ef219eca406a5fd441911cededdc2ec` = compagnon) ; compagnon de `donnees/20261111-151701-t06-reel/mesures-t06.npz` sur la branche : `aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049` (sceau à vérifier par la mère avant la lecture de l'en-tête ; je n'ai pas descendu le fichier) |
| Q-16 | P1 — 7b finie, branche poussée, rapatriement vérifié, **instance de 7b détruite** | **rempli** | R-2413 (l. 2371) : fin normale, 60218139 détruite 2026-11-12T05:18:03Z, compagnons conformes ; branche présente au distant (§ 3) |
| Q-17 | P10 — `vastai` 1.8.3 ; `HF_TOKEN` et jeton GitHub présents par leur nom ; inventaire sans instance `t06…` ni `t07…` | **à la fille** | dernier inventaire connu : passation `registres/passations/2026-11-13-1732.md` (`a808b3eeff198936f13cc1367cb3e264799d8dc119a0635074039ccf4375cbc6`, l. 52-55) : aucune instance de la lignée ; intouchables 58936096, 58936099, 58936100 (arrêtées), 60480302 (témoin Bailey, autre session) ; Hetzner `poste-temoin-bailey-v8` ; étiquettes de ces instances non connues d'ici. Jeton : chez la fille de P3-bis, `CONTROLE_IA_GITHUB_TOKEN` était absente, `CONTROLE_IA_GITHUB_TOKEN_2` présente (R-2387, l. 2345) |
| Q-18 | P11 — création au plus tard le 2026-11-22 à 12:00Z | **rempli** | `date -u` : 2026-11-13 18:30 |
| Q-19 | **Ligne de GO citée au crochet** (`GO_ID=…`, § 4.4) | **rempli** | `registres/go.md` l. 296 : GO-2026-11-10-06, calcul, Lazar, accordée 2026-11-10, **échéance 2026-11-23**, 20 USD non cumulés ; l. 294 : GO-2026-11-10-04, mêmes dates ; aucune ligne de révocation ne les cite ; essai d'analyse du crochet `.claude/hooks/garde_calcul.py` (`73be0638…`), fonction `decider` appelée sur du texte (rien lancé) : la ligne (A) suivie de la commande de création **passe** les 13, 22 et 23 novembre, est **bloquée** le 24 ; la commande de création **seule**, avec `GO_ID=$GO` non développé, est **bloquée** (« sans identifiant de GO ») : le crochet lit le texte de la commande avant le shell |
| Q-20 | Crochet de garde **chargé** dans la session fille (R-2545, R-2552) | **à la fille** | R-2552 (l. 2511) : non chargé dans une session ouverte hors du dépôt (`CLAUDE_PROJECT_DIR` absente) |
| Q-21 | **Crédit** du compte de location (non prévu par l'ordre ; § 5, point 4) | **à la fille** (lecture seule), puis mère | 31,46 USD à 15:49Z (passation 1732, l. 54 ; R-2547) ; 60480302 en marche depuis 2026-11-13T09:48:24Z (R-2511, l. 2470), ≈ 1,172 USD de l'heure (R-2512, l. 2471), enveloppe jusqu'à 75 USD (GO-2026-11-10-10, `go.md` l. 300) |
| Q-22 | Branche de sortie `donnees/t07-etape-a-v1` absente du distant (§ 1) | **rempli** | `git ls-remote … 'refs/heads/donnees/t07-etape-a-*'` : rien |
| Q-23 | Aucun chemin interdit ni de 7a cité par un registre (§ 4.1, compte `0`) | **rempli** | commande du § 4.1 rejouée sur `scellements-v1.md` et `prealables-p3bis-v1.md` : `0` |

## 3. Sorties de 7b : existence et empreintes (noms seulement)

Clone partiel à une profondeur, sans extraction, de la seule branche `calcul/t06-confirmation-7b-v1`
(`git clone -q --depth 1 --filter=blob:none --no-checkout --single-branch --branch …`), dans le bac à sable de ce
préparateur (`…/scratchpad/clone-7b-noms`, 652 Ko), 18:25 UTC.

| Ce qui est vérifié | Résultat | Source du nom |
|---|---|---|
| Tête de `BR7B` (`git ls-remote`) | `55c3e3eb89a4650419f35999aaa4c54288275b0d` (dernier commit 2026-11-12 05:17:05Z) | R-2413 : égale |
| `runs/20261111-151701-t06-reel/manifeste.json` et compagnon | présents ; `git show … \| sha256sum` = `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6`, égale au compagnon et à R-2413 | ordre § 2.1, P2 |
| `diag/20261111-151701-t06-reel/episodes-t06.json`, `distillation-t06.json` et compagnons | présents (`git ls-tree --name-only` sur ces chemins exacts) | ordre § 2.1 ; script v4 l. 203 |
| `diag/20261111-151701-t06-reel/arret.json` | absent (normal : fin normale, R-2413) | ordre § 2.1 ; script v4 l. 205 |
| `donnees/20261111-151701-t06-reel/` au motif du script v4 (l. 207) | `adaptateur-saboteur.pt`, `adaptateur-temoin.pt`, `mesures-t06.npz`, `textes-actions-t06.jsonl`, `activations-sous-ensemble-t06-manifeste.json`, `activations-sous-ensemble-t06-000.npz` à `-012.npz` (13 morceaux), chacun avec son compagnon | R-2413 : « 2 adaptateurs, mesures, textes, sous-ensemble, 13 morceaux sur 13 » |

Rien d'autre n'a été descendu, listé ni ouvert sur cette branche.

## 4. Garde d'ordre avec P3-bis

- **Ce que dit l'ordre (brouillon 9)** : P7 (« `VERDICT-P3BIS` et le journal de P3-bis relevés (présence, date), jugés par
  la garde » ; sinon arrêt, nœud) et § 9 (la mère vérifie, avant de recopier `SCORES-T07`, `SONDES-T07` et `OUVERTURE-T07`,
  que le journal de P3-bis de `main` ne porte aucune ligne datée avant la fin de l'étape A qui manquait à la copie de
  l'instance). **L'ordre ne parle pas d'une garde « avant `VERDICT-P3BIS` » en toutes lettres** : il laisse la règle au
  module et au texte scellé.
- **Ce que dit le texte scellé de T0.7** : (b) 3 (l. 1634-1638), « Lignes de registre » (l. 2166-2172) et (d) G1 à G5
  (l. 1696-1761) : sur le chemin sans ouverture anticipée, `VERDICT-P3BIS` présente à l'ouverture de l'étape A → refus,
  nœud ; **si l'étape A n'a pas abouti (lignes `SCORES-T07` et `SONDES-T07`) avant `VERDICT-P3BIS`, nœud, pas une
  attente** ; une ligne `OUVERTURE-P3BIS` de mode `pleine-anticipee` → nœud à toute date ; une ouverture **réduite**
  valable au rendez-vous (garde adaptée, N-066, `docs/decisions/decision-N-066-v1.md`, `21e83ed5…`) laisse jouer l'étape A
  avec la réserve R14 ; l'instant de fermeture du périmètre est le plus tôt entre la première ouverture de l'étape A et
  la première ligne `OUVERTURE-P3BIS` (G5).
- **État aujourd'hui** : la course de P3-bis est **finie et récupérée, aucun résultat lu** (R-2547, l. 2506 ; instance
  60492378 détruite 15:48:34Z) ; elle **attend son ouverture** ; aucune ligne `VERDICT-P3BIS`, aucun journal de P3-bis sur
  `main` ; R-2552 (l. 2511) : le module d'ouverture de P3-bis n'ouvre que par la voie pleine (après `SCORES-T07` et
  `SONDES-T07`) ou au rendez-vous du **2026-11-20T12:00:00Z** (ouverture réduite possible). **Rien ne bloque l'étape A
  aujourd'hui.**
- **Ce que cela exige, non écrit dans l'ordre** : qu'aucune ligne `VERDICT-P3BIS` ni `OUVERTURE-P3BIS` ne soit inscrite sur
  `main` avant que la mère ait recopié `SCORES-T07` et `SONDES-T07` (§ 9 de l'ordre) — en particulier par le lecteur neuf du
  verdict de P3-bis que prévoit la passation de 17:32 (« Prochaine action », point 2). Une ligne `REFUS-OUVERTURE-P3BIS`
  n'est jamais une ouverture (T0.7 l. 1708) : sans effet.

## 5. Ce qui a changé depuis le 10 novembre et que l'ordre ne prévoit pas

1. **Ordre remplacé** : le mandat nomme le brouillon 5 ; le texte scellé cite le brouillon 9 (§ 1).
2. **P3-bis a tourné et attend son ouverture** (§ 4) : l'ordre, écrit avant le scellement de P3-bis (brouillon 9 : 11
   novembre 05:50Z ; `SCELLEMENT-P3BIS` : 15:52:30Z), ne le prévoit pas ; la règle du texte scellé suffit, à la condition du
   § 4.
3. **`ATT` et l'hôte** : la mesure à C7 (R-2319, 06:19Z, **après** le brouillon 9) a montré qu'un hôte à instructions
   AVX-512 ajoute « , 1 warning » à la ligne d'essais (noyau OpenBLAS) ; sur un tel hôte (Intel récent ; EPYC de quatrième
   génération « non vérifié »), l'étape 6 s'arrête en code 2 avant le modèle (≈ 1 USD), et une seconde création demande un
   écrit de la mère. L'ordre préfère un EPYC (§ 4.3) sans en distinguer la génération ; R-2511 (l. 2470) rapporte
   qu'aucune A100 sur EPYC 7513 n'était offerte le 13 au matin. La mesure de `ATT` à C7 n'a pas été rejouée sous Python 3.11 (R-2319), celui de
   l'image de l'instance.
4. **Crédit du compte de location** : l'ordre borne la dépense sous GO, pas le crédit ; le témoin Bailey 60480302 tourne en
   même temps (≈ 1,172 USD de l'heure). À 15:49Z : 31,46 USD. Projeté à une création vers 20:00Z : ≈ 26,6 USD ; pire cas
   de l'étape A ≈ 16,4 USD (§ 6 de l'ordre) plus 12 h du témoin ≈ 14,1 USD : **le pire cas commun dépasserait le crédit**
   (le cas attendu, ≈ 5,5 à 7,4 USD sur 3,2 à 4,7 h, non). Un crédit épuisé arrête l'instance pendant l'étape A : nœud.
5. **Crochet** non chargé dans une session ouverte hors du dépôt (R-2545, R-2552) ; et la commande de création ne passe le
   crochet que si la ligne (A) est dans la même commande (Q-19).
6. **`vastai`** : P10 exige 1.8.3 ; une version 1.11.0 existe (R-2552 : sans terminal, la destruction sans `-y` abandonne
   et rend 0) ; l'ordre emploie `-y` (§ 4.7), comme l'ordre de 7b qui a détruit 60218139. Si `vastai` manque chez la fille,
   l'installation demande un écrit de la mère (précédent : R-2351, `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/ecrit-mere-installation-vastai-course-7b-v1.md`, `becb02ca…`).
7. **Nom du jeton GitHub** : l'ordre lit `CONTROLE_IA_GITHUB_TOKEN` (§ 4.2, § 4.4) ; précédent R-2387 (alias depuis `_2`).
8. **`DEPOT_URL`** : `CLAUDE.md` demande de la passer à tout lancement ; le script v4 la **refuse** hors essai (l. 57-60,
   « T07 REFUS ») et porte le bon dépôt en dur (l. 56) ; la commande du § 4.4 ne la passe pas : ne pas l'ajouter.
9. **Échéances** : lignes de GO valables jusqu'au **2026-11-23** inclus (date du conteneur pour le crochet) ; l'ordre :
   création au plus tard le 2026-11-22 12:00Z, minuterie ≤ 12 h. Cohérent.
10. **Module de T0.7 au commit de `CODE-T07`** : inchangé (`src/` de `main` = celui de C7 ; vérificateur conforme, Q-6) ;
    `tests/` de `main` diffère de celui de C7 (`0048e211…` contre `7ab32147…`) : sans effet, l'instance joue S7.
11. Observation N-1 de R-2318 (l. 2276) : l'ordre dit le script de P14 « non versé » ; il l'est (Q-15). Sans effet.

## 6. Non vérifié ici, et pourquoi

- Inventaire des instances, étiquettes, crédit, version de `vastai` et jetons de la session fille : aucun appel au
  fournisseur (mandat) ; R-2552 : le réseau de l'environnement de la mère refuse `console.vast.ai`.
- Révision du modèle de 7b (P13 (i)), `config.go_id` du manifeste de 7b, nombre de lignes des mesures (P14) : lecture d'un
  contenu de 7b, interdite à ce préparateur.
- Suite d'essais : non rejouée (aucun besoin pour ces préalables ; `ATT` est la valeur décidée par R-2319).
