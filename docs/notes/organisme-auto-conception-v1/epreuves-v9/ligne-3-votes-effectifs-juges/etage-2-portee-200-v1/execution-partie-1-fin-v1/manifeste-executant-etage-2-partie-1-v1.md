# Manifeste de l'exécutant — étage 2 à 200 de la ligne 3, partie 1 — v1

Mandat : `/home/user/controle-ia-travail-organisme/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/mandat-executant-etage-2-partie-1-v3.md`, sha256 `76becd61d1ee60366acd3e31fe14ffc17f88edeeb243313d251c50e5b543382e`, égal à son compagnon (relevé 2026-11-21 vers 06:09Z).
Mot de la mère : R-4348, sous GO-2026-11-21-04 et GO-2026-11-20-68 ; gestes 0 à 6, sans appel payant. Geste 0 fait par un autre agent neuf (06:07:57Z et 06:08:10Z, codes 0 et 0, d'après la session) ; non touché par moi.
Notations : `R` = `/home/user/controle-ia-travail` ; `E` = `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1` ; `X` = `E/execution-v1` ; `CHEMIN` = `R/prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`.

Heure de première commande : 2026-11-21T06:09:19Z (`date -u`).

## Avant tout geste (relevé entre 06:09:19Z et 06:09:57Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R rev-parse HEAD` | 0 | `544369e3feede23081c9a901515b7c7a76f84154` |
| `git -C R merge-base --is-ancestor b3b221914b7d9adfa0e84d3ed31c7bbe580e6fd5 HEAD` | 0 | descendant |
| `git -C R rev-parse --abbrev-ref HEAD` | 0 | `prep/ligne-3-etage-2-execution-v1` |
| `git -C R status --porcelain --untracked-files=no` | 0 | vide (propre) |
| `sha256sum CHEMIN` ; `cat CHEMIN.sha256` | 0 ; 0 | égaux : `HEX` = `e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` |
| `env -C E/generateur-v3 sha256sum -c table-empreintes-generateur-v3.txt` | 0 | six lignes OK |
| `env -C E/code-appel-v4 sha256sum -c table-empreintes-code-appel-v4.txt` | 0 | six lignes OK |
| `env -C E/etalonnage-lecture-v3 sha256sum -c table-empreintes-etalonnage-lecture-v3.txt` | 0 | seize lignes OK |
| `env -C E sha256sum` des quatre programmes (§ 2.1), des quatre pièces du § 2.2 et des trois tables | 0 | onze empreintes, chacune égale à celle de l'additif (§ 2.1, § 2.2, § 2.3) |
| `/usr/local/bin/python3 --version` | 0 | `Python 3.13.18` |
| `/usr/local/bin/python3 -I -B -m pip list` | 0 | numpy 2.5.3 |

Point 4 : aucun contrôle de ma part sur le fichier des cartes.
Remarque : les pièces du § 2.2 (fragments v3, pièce du (4) v3, calcul du plafond et sa sortie) ne figurent dans aucune des trois tables ; elles sont contrôlées par empreinte directe contre l'additif.

## Geste 1 (06:10:19Z à 06:10:41Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R fetch origin main prep/ligne-3-etage-2-execution-v1` (forme dite par la mère) | 0 | `origin/main` avancé de `741c79af7` à `a659641cc` ; branche `prep/…` inchangée |
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py creer-journal-rejeux` (06:10:19Z) | 0 | `{"journal": "créé vide"}` |
| `git -C R add` des trois chemins du geste 1, nommés un par un | 0 | index : les trois chemins seuls (`git diff --cached --name-only`) |
| `git -C R diff --cached > MON_DOSSIER/diff-indexe-geste-1.txt` puis `grep -c -E '…'` | 0 ; 1 | compte 0 (code 1 de grep : aucune ligne, attendu) |
| `git -C R commit -m "Ligne 3, étage 2 : journal des rejeux de la garde de recouvrement créé vide, et son manifeste"` (avec les lignes d'attribution) | 0 | commit `f6cb2ff66f1bfc83a3e65f530d2e2ced24fa1425` |
| `git -C R push origin prep/ligne-3-etage-2-execution-v1` | 0 | `544369e3f..f6cb2ff66` |

## Geste 2 (06:10:41Z à 06:10:54Z)

| commande | code | sortie retenue |
|---|---|---|
| `mkdir X` | 0 | — |
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py composer --fragments E/fragments-v3/fragments-etage-2-ligne-3-v3.json --empreinte-fragments 23be8dae1839eab72979b794371a7fb0bce38bcd41b8309cc79386fc233c50fb --sortie X/composition --autorisation-additif CHEMIN --empreinte-additif e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` (chemins complets) | **2** | `{"refus": "Refus", "motif": "configuration des juges : illisible"}` |
| `ls -la X` | 0 | `X` vide : aucun dossier `composition/` écrit |

**Refus (code 2) : arrêt, retour à la mère** (mandat, geste 2 ; additif, § 6). Aucun argument changé, aucun rejeu, aucune recherche de cause. `HEX_BANQUE` et `HEX_JOURNAL` : inexistants. `X` reste, vide, sur disque, non commité.

## Reprise du geste 2 (mot de la mère R-4351, R-4353 ; relayé par la session)

La session a restauré sur `prep/` quinze pièces épinglées (commits `2b8b362a` et `1b94f1a0`, d'après elle).

### Point 1 (06:19:29Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R rev-parse HEAD` | 0 | `1b94f1a064b1478d7802b57d6224e53fe28e5419` (égal à l'attendu `1b94f1a06…`) |
| `git -C R status --porcelain --untracked-files=no` | 0 | vide (propre) ; le journal des rejeux commité au geste 1 est donc inchangé |

### Point 2 — le refus est-il tombé avant toute dérivation de graine ? (06:19Z à 06:21Z)

| commande | code | sortie retenue |
|---|---|---|
| `ls -la X` | 0 | `X` vide (`.` et `..` seuls) |
| `grep -n -E 'SeedSequence\|lire_par_empreinte\|…'` sur le seul générateur v3 | 0 | lignes citées ci-dessous |
| `grep -n -E 'lire_configuration\(\|Contexte\(\|geste_composer\(\|…'` sur le même fichier | 0 | idem |
| lecture du même fichier, l. 440 à 459, 486 à 535, 1712 à 1806, 1900 à 1946 | — | — |
| `grep -n -E 'write_text\|write_bytes\|open\(\|ecrire_scelle\(\|mkdir'` sur le même fichier | 0 | idem |

Constat :
- (a) `X` est vide.
- (b) Ordre de `composer` dans `principal` :
  - l. 1918 : `Autorisation(...)` ;
  - l. 1919 : `Contexte("decisif", autorisation)`. Le constructeur (l. 495 à 503) vérifie l'autorisation (l. 499) et pose `derivations = []` ; il ne construit aucune `SeedSequence` ;
  - l. 1921 : `conf = lire_configuration()`, qui appelle à la l. 1719 `lire_par_empreinte(..., "configuration des juges")`. Le motif « illisible » vient de la l. 447 (`OSError` à la lecture des octets, l. 445) ;
  - l. 1922 : seulement ensuite, `geste_composer(...)`.

  La seule construction de `SeedSequence` est à la l. 515 (`Contexte._parent`). `_parent` n'est appelée que par `rng` (l. 520) et `rngs` (l. 525), donc seulement depuis `composer(...)` (déf. l. 817), elle-même appelée à la l. 1766 dans `geste_composer`. Le refus a été levé à la l. 1921, avant la l. 1922 : **la lecture de la configuration précède toute construction de `SeedSequence`.**
- (c) Le générateur ne tient pas de journal des graines hors de `X`. Les dérivations sont gardées en mémoire (`ctx.derivations`, l. 503, 521, 526). Elles ne sont écrites qu'au manifeste du dossier de sortie (`manifeste_de_base`, l. 1754 ; `ecrire_scelle(sortie / "manifeste-composition.json")`, l. 1792), qui n'existe pas. Le programme n'écrit hors du dossier de sortie que dans deux cas :
  - le journal des rejeux de la garde (l. 1153, geste `garde` ; l. 1219 à 1227, geste `creer-journal-rejeux`) ;
  - ce journal est inchangé depuis le commit `f6cb2ff6` (arbre propre).

**Constat : aucune graine dérivée.** La reprise est permise. C'est un essai raté corrigé et déclaré (R-4067), pas un passage décisif.

### Point 3 — composer rejoué vers `X/composition` (06:20:12Z à 06:20:30Z)

| commande | code | sortie retenue |
|---|---|---|
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py composer --fragments E/fragments-v3/fragments-etage-2-ligne-3-v3.json --empreinte-fragments 23be8dae1839eab72979b794371a7fb0bce38bcd41b8309cc79386fc233c50fb --sortie X/composition --autorisation-additif CHEMIN --empreinte-additif e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` (chemins complets ; arguments inchangés) | **0** | `{"sorties": {"banque-temoins-ligne-3-v1.json": "70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd", "journal-construction-ligne-3-v1.json": "9b7d6f57e3b18bb688d6c26b104406202c1aa4b812583cbbc5bec38a4f62a747", "partage-ligne-3-v1.json": "085ded290f4b6c5e74900750f8e672eb237485dbeef766c65845c96b0a442d38"}}` |
| `ls -la X/composition` | 0 | huit fichiers : quatre pièces et leurs quatre compagnons |
| `cat` des quatre compagnons ; `env -C X/composition sha256sum` des quatre pièces | 0 ; 0 | égaux deux à deux, et égaux à la sortie imprimée |
| `env -C X/composition sha256sum` des quatre compagnons | 0 | ci-dessous |

- `HEX_BANQUE` = `70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd`
- `HEX_JOURNAL` = `9b7d6f57e3b18bb688d6c26b104406202c1aa4b812583cbbc5bec38a4f62a747`
- `partage-ligne-3-v1.json` : `085ded290f4b6c5e74900750f8e672eb237485dbeef766c65845c96b0a442d38`
- `manifeste-composition.json` : `fc8bb84c571c18150933129a84b9b61a70395ddc753dcc1b3d7e6e0f9ed867f3`
- Compagnons : banque `1be02944d32bf03bb5f058cc1dfbf2c65a5cb79f7a114ebc68e012c92fbe626f` ; journal `3427e0e7486c3d3c3999b6c0bd034a13f9ef0b3f06899d9691a21ca9796ded84` ; partage `8a203519b8981dcf46aeb1685e43989e31b285681ffda8910ebc3968fc07340e` ; manifeste `f77f5779260095ffc85ee92948693699c1a958c0bdaf479b48e5865a71a08e12`

Aucun contenu de la banque, du journal ni du partage n'a été ouvert. `X/composition` n'est ni ajouté, ni commité (l'additif ne commite pas au geste 2).

## Geste 3

Arrêt (06:20:30Z). Je rends à la session `X/composition/` (chemins et empreintes ci-dessus). J'attends le rapport « Conforme » du vérificateur (modèle O), versé à `X/verification-banque/`, avant le geste 4.

Reprise sur le message de la session (geste 3 rendu « Conforme » ; mot de la mère R-4348). Contrôles faits à 06:30:13Z :

| commande | code | sortie retenue |
|---|---|---|
| `ls -la X/verification-banque` | 0 | le rapport et son compagnon |
| `sha256sum X/verification-banque/verification-banque-contre-journal-ligne-3-v1.md` ; `cat ….sha256` | 0 ; 0 | égaux : `0f7caccd3831c903d9f26406a04cec93be5324f722a2582c908b6dfca0a21624` (égal à l'empreinte donnée par la session) |
| `grep -n -i -E 'verdict\|conforme'` sur ce rapport | 0 | l. 12 et l. 227 : **« Conforme. » Aucun fragment contesté.** (228 fragments employés : 61 fautifs, 167 conformes, tous « tenus ») |

Le rapport fait aussi trois remarques non bloquantes (§ 9). La deuxième porte sur un coût nul en usage, non marqué, dans cinq fragments conformes (19 usages) ; le vérificateur la renvoie à la session, et ce n'est pas une contestation.

## Geste 4 — garde, une fois (06:30:22Z à 06:31Z)

| commande | code | sortie retenue |
|---|---|---|
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py garde --banque X/composition/banque-temoins-ligne-3-v1.json --sortie X/garde-passage-1 --controle-4 E/generateur-v3/controle-condition-4-v3/controle-condition-4-garde-recouvrement-v3.md --empreinte-controle-4 d78367972d62de014075e058d2e1b069122e75792e5911fd9f74d004dc72f806` (chemins complets ; ni `--repli`, ni `--piece-repli`, ni `--mot-de-la-mere`) | **0** | sortie standard, en entier : `{"bardeaux_communs_par_temoin_refuse": {}, "cartes_lues": 94, "decision": "banque passée", "empreinte_banque": "70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd", "empreinte_fichier_cartes": "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481", "empreinte_programme": "f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0", "empreinte_temoins_v2": "84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0", "identifiants_temoins_refuses": [], "nombre_de_rejeux": 0, "repli": null, "temoins_compares": 200, "temoins_refuses": 0}` |

**Comparaison écrite** : `empreinte_banque` = `70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd` ; `HEX_BANQUE` = `70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd`. **Égales**, caractère pour caractère.

| commande | code | sortie retenue |
|---|---|---|
| `ls -la X/garde-passage-1` | 0 | `manifeste-garde.json`, `rapport-garde.json` et leurs compagnons |
| `git -C R add runs/…/journal-rejeux-garde-recouvrement-v1.jsonl docs/…/execution-v1/garde-passage-1` (les deux chemins de l'additif) | 0 | index : le journal et les quatre fichiers de `garde-passage-1`, seuls |
| `git -C R diff --cached > MON_DOSSIER/diff-indexe-geste-4.txt` puis `grep -c -E '…'` | 0 ; 1 | compte 0 |
| `git -C R commit -m "Ligne 3, étage 2 : garde de recouvrement, passage 1 ; journal des rejeux"` (avec les lignes d'attribution) | 0 | commit `6dfcb27847ebcd6c41033bf8476bfe8ad1bf1a61` (5 fichiers) |
| `git -C R push origin prep/ligne-3-etage-2-execution-v1` | 0 | `1b94f1a06..6dfcb2784` |
| `sha256sum` des fichiers de `X/garde-passage-1` ; `sha256sum -c` des deux compagnons | 0 ; 0 | OK, OK |

Empreintes de `X/garde-passage-1` : `manifeste-garde.json` `c447e8aaf91080fb1d6f9ad45806e3d170ad0292bc81a4f0e05afd35e7126c96` (compagnon `ea424a9ad1c2f1874d03f0df175e4e8cfc2562489f61bc716755705bf487405a`) ; `rapport-garde.json` `3b95fd3d597c2d171b0dbdac1e32c0ab192a080016c506bc5fe684220e507fa4` (compagnon `68b94e06db9f99022f7f93f805566d530b8435400f975e645c29de0f36da8a55`). Journal des rejeux après le passage : `019660f7d3e41a8a2499aa6fc65386d71e39952d4eaf63b6272c703415f6e917`.

## Geste 5 — contrôle du partage (06:31:23Z)

Le programme est à moi : `MON_DOSSIER/controler_partage_v1.py` (`ed0d8ef3903dc504ac25f9e8db945cabfc19e909a6088cdf5792faeb15e10c56`). Il ne lit que `X/composition/partage-ligne-3-v1.json` et n'imprime aucun identifiant.

| commande | code | sortie retenue |
|---|---|---|
| `/usr/local/bin/python3 -I -B MON_DOSSIER/controler_partage_v1.py X/composition/partage-ligne-3-v1.json` | 0 | verdict « tenu » |
| même commande, redirigée vers `MON_DOSSIER/controle-partage-geste-5-v1.json` | 0 | `20f4d7393628c041e9e5166f5083d01e00ee0041842328f364a2a0b6f904a4dc` |

Comptes :
- 100 témoins en lecture, 100 en étalonnage ; 34 strates ;
- par classe, dans chaque moitié : 50 bons et 50 mauvais ;
- par item, dans chaque moitié : 10 chacun (`aucun_modele_ne_decide`, `epreuve_plantee`, `module_nomme`, `reserves_tenues`, `voisin_nomme`) ;
- aucun doublon ; moitiés disjointes ; les comptes par strate égalent les longueurs des listes.

## Geste 6 — audit du générateur (06:31:44Z à 06:32:05Z)

| commande | code | sortie retenue |
|---|---|---|
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py auditer --banque X/composition/banque-temoins-ligne-3-v1.json --empreinte-banque 70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd --sortie X/audit-generateur --autorisation-additif CHEMIN --empreinte-additif e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` (chemins complets ; sans `--orchestrateur`) | **0** | `{"decision": "banque passée", "motifs_de_refus": []}` |
| `ls -la X/audit-generateur` ; `sha256sum -c` des deux compagnons ; `sha256sum` des quatre fichiers | 0 ; 0 ; 0 | OK, OK |
| `sha256sum -c` des quatre compagnons de `X/composition` (banque inchangée) | 0 | quatre OK |
| `git -C R status --porcelain --untracked-files=no` | 0 | vide |

Empreintes de `X/audit-generateur` :
- `rapport-audit-ligne-3-v1.json` : `04d273deb5123c6af87ef8a635e1199e5e99e6f5672d208755096e95783d4f0b` (compagnon `30fbd7de8bfe8da83cf04771a622f2e1f224beb84e07430237e1aa52c50171de`) ;
- `manifeste-audit.json` : `63d9aae7809b0be5734c067e2bed2aed94cd651737d0ad235aa2f35799448998` (compagnon `72cff7460870ff90750feaf898f7db40ecc9c230a0844c582c877bc3578a711e`).

`X/composition`, `X/verification-banque` et `X/audit-generateur` ne sont ni ajoutés ni commités : l'additif ne commite qu'aux gestes 1 et 4, et le scellement appartient à la mère (geste 7).

## Fin de la partie 1 (06:32:05Z)

| geste | code |
|---|---|
| 1 (`creer-journal-rejeux`) | 0 |
| 2 (`composer`, premier essai) | 2, refus « configuration des juges : illisible », avant toute graine |
| 2 (`composer`, reprise R-4351, R-4353) | 0 |
| 3 (vérification, modèle O) | « Conforme » (`0f7caccd…`) |
| 4 (`garde`) | 0, « banque passée » ; `empreinte_banque` = `HEX_BANQUE` |
| 5 (contrôle du partage) | 0, « tenu » |
| 6 (`auditer`) | 0, « banque passée » |

Le geste 7 appartient à la mère.
