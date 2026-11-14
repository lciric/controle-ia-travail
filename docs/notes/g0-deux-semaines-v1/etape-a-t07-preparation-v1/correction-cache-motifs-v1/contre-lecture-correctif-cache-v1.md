# Contre-lecture du correctif du cache de l'étape A de T0.7 (option (a), R-2593) — v1

- **Lecteur** : sous-agent neuf, modèle B (lecteur) ≠ modèle A (auteur) ; n'a écrit ni le correctif, ni l'essai, ni l'addendum, ni le module, ni l'ordre.
- **Heures (UTC, `date -u`)** : de 2026-11-13T22:06:22Z à 2026-11-13T22:13:18Z.
- **Objet** : branche `prep/t07-cache-motifs-v1`, code `799ef38390c1df7790691a848ceb344dd9a81d54` (parent C7 `b4cd9953…`), pièces `deaeee03…` ; arbre de travail neuf, retiré à la fin. Rien commité, rien poussé, aucune instance, aucune clé lue.
- **Non ouvert** : le texte scellé de T0.7 (`prereg/T0.7-sondes-v0-v1.md` ; seul son compagnon `.sha256` a été lu) ; aucun fichier interdit par la consigne ; sous `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/`, noms seulement (`git ls-tree`). Deux lignes du registre des décisions qui nomment ce dossier ont été affichées par la recherche (R-2039, R-2040 : lecture A, exploratoire, non opposable) ; je le signale.

## Verdict

**Fusionnable** (code `799ef383` : aucun constat bloquant ni majeur). L'addendum (brouillon 1) est **exact** ; trois compléments mineurs avant son scellement. Deux nœuds restent à trancher **avant la relance**, pas avant la fusion (§ 5 et § 6) ; je ne les tranche pas.

## Constats

### Bloquant
Aucun.

### Majeur
Aucun.

### Mineur
- **m-1 — essai, cas manquant** (`tests/test_t07_cache_liste_arbre_v1.py`, l. 129-144) : aucun cas ne retire un fichier préchargé que la fonction ne contrôle pas elle-même (`generation_config.json`, `special_tokens_map.json`). La mutation M8 (motifs privés de ces deux noms) **survit** (21 passés). Le comportement est pourtant celui que dit l'addendum (sonde hors essai, § 2) : liste présente → `GardeArret` ; sans liste → passe, comme avant. *Correctif proposé* : un cas paramétré sur chaque nom de `PRECHARGES`, liste présente → `GardeArret` (motif `ABSENT_LISTE`). Coût : nouveau commit, donc liste, `ATT` et attestation à refaire ; à défaut, citer cette sonde dans l'addendum (§ 6) comme réserve. Au choix de la mère.
- **m-2 — addendum, § 4, l. 165-167** : « la bibliothèque contrôle en plus […] la présence de chaque fichier préchargé » est vrai (code de la bibliothèque lu, sonde jouée) mais n'est épinglé par l'essai que pour l'index et les morceaux. *Correctif* : le dire (« épinglé par l'essai pour l'index et les quatre morceaux ; vérifié à la main pour les autres »), ou appliquer m-1.
- **m-3 — addendum, § 3.4 l. 148-150 et § 6** : le relevé du fichier dérivé de 7a posé par l'extraction n'est qu'une incise des « écarts déclarés ». *Correctif* : en faire une réserve numérotée ou un point ouvert (§ 5 bis), avec le renvoi au § 2.2 de l'ordre (voir § 6 ci-dessous).
- **m-4 — addendum, § 5** : ajouter que `passe_blanc_v1` et `passe_blanc_v2` lisent aussi la **première** ligne (`lire_lignes_actuelles`, l. 327 et l. 335), et que l'ordre scellé fixe le nom `CODE-T07-v2.json` (P6, l. 259 ; commande de la l. 291) : la voie retenue touche l'ordre version 2 dans tous les cas.
- **m-5 — code, hors du différentiel, sans correctif demandé** (`reextraction_p3_v1.py`, l. 483-485) : `except Exception` rend « absent du cache local » pour toute erreur, instantané incomplet compris (réserve 1 de l'addendum, exacte). C'est ce libellé qui a rendu l'arrêt peu lisible ; à reprendre à une prochaine version du module, pas ici (correction minimale).

## 1. Différentiel `b4cd9953..799ef383`, `src/`

- Un seul fichier de `src/` (`src/controle_ia/t07/reextraction_p3_v1.py`, 14 lignes ajoutées, 2 retirées), une seule fonction (`revision_au_cache`, l. 460-510) : docstring complétée, import de `MOTIFS_PRECHARGEMENT` dans la fonction (l. 479), argument `allow_patterns=list(MOTIFS_PRECHARGEMENT)` (l. 481-482). Aucune ligne des contrôles `GardeArret` (l. 483-510) ne change. `harnais/modeles.py` inchangé (motifs l. 106-107, ceux de `precharger_modele`, l. 118).
- Bibliothèque lue (`huggingface_hub` 1.33.0, `_snapshot_download.py`, `_raise_if_incomplete_snapshot`) : hors ligne, si la liste de l'arbre est au cache, chaque fichier de la liste **retenu par les motifs** doit exister, sinon `IncompleteSnapshotError` ; sans liste, rien n'est contrôlé. La note du développeur est conforme au code.
- **Un fichier préchargé manquant est-il toujours refusé ?** Liste présente : oui, les dix (bibliothèque). Sans liste : les trois essentiels, l'index et les morceaux (fonction), comme avant ; `generation_config.json` et `special_tokens_map.json` non, comme avant. Aucun cas refusé à C7 ne passe à `799ef383` sauf le cas visé (fichiers hors motifs absents).
- **Un motif trop large peut-il masquer un manque ?** Non : les motifs ne font que désigner ce que la bibliothèque **exige** ; plus large = plus d'exigences (M2 et M10 : la garde refuse le cache sain). Un motif trop **étroit** retirerait le contrôle de la bibliothèque, mais les contrôles propres de la fonction restent (M3, M4, M9 : `GardeArret` toujours levée, seul le libellé change, et l'essai le voit). Les motifs du contrôle et du préchargement sont la même constante : ils ne peuvent pas diverger.
- La dépendance neuve à `harnais/modeles.py` est couverte par `code_t07_v1.controler_code` (l. 103-107 : tout `src/controle_ia/` égal au commit cité).
- Fusion dans `main` (`5a38bee8`) sans conflit (`git merge-tree`) ; `src/` de `main` égal à celui de C7.

## 2. Essai neuf et mutations

Essai joué seul, module corrigé : **21 passés** (5,7 s), cas (vi) non sauté (fichiers réels de P3 et configuration v8 présents). Il prouve ce qu'il dit : liste écrite par `write_tree_cache` (l. 103-104), mémoire vidée et vérifiée vide avant l'appel (l. 108-109), lecture sur disque constatée après (l. 126), étape 8 en processus neuf, hors ligne, cache par `HF_HUB_CACHE` (l. 195-211), forme scellée en processus neuf → `IncompleteSnapshotError` (l. 212-216).

Mutations à la main sur le module de l'arbre de travail, restauré par `git checkout` après chacune (21 cas chaque fois) :

| | mutation | résultat |
|---|---|---|
| M1 | `allow_patterns` retiré (forme de C7) | **5 échecs** : (i), trois (iii) index illisible avec liste, (vi) |
| M2 | `allow_patterns=["*"]` | 5 échecs (les mêmes) |
| M3 | `allow_patterns=["config.json"]` | 5 échecs : quatre (ii) et (iii) index absent, liste présente |
| M4 | motifs sans aucun nom en `safetensors` | 5 échecs (comme M3) |
| M5 | contrôle « morceaux sans index » neutralisé | 1 échec : (iii) index absent, sans liste |
| M6 | contrôle des morceaux attendus retiré | 4 échecs : (ii) sans liste |
| M7 | `ignore_patterns=["model*"]` ajouté | 5 échecs (comme M3) |
| M8 | motifs sans `generation_config.json` ni `special_tokens_map.json` | **21 passés : survit** (m-1) |
| M9 | motifs sans `model*.safetensors` (mutation du développeur) | 4 échecs : (ii) liste présente — conforme à l'addendum |
| M10 | motifs augmentés de `original/*` (mutation du développeur) | 5 échecs — conforme à l'addendum |
| M11 | `cache_dir=None` | 18 échecs |

Sonde hors essai (cache de l'essai, un fichier retiré) : `generation_config.json` ou `special_tokens_map.json` absent, liste présente → `GardeArret` (« absent du cache local (IncompleteSnapshotError) ») ; sans liste → passe ; `config.json` absent → `GardeArret` dans les deux cas.

Suite entière non rejouée (consigne) : la ligne du développeur `500 passed, 2 skipped, 4 xfailed, 1 warning` se lit au journal et à la sortie versés (empreintes conformes) ; 479 + 21 = 500 ; les deux sauts sont ceux de C7, pas le cas (vi) ; sauts et échecs attendus : `c1928351…` recalculé sur les deux sorties.

## 3. Liste CODE-T07 v3

`liste-code-t07-v3-au-commit-799ef383.json` : `7dabdbc8812dd3af826611651a06d8e54a31ca166cb69a7faafd4c18823269b8` (recalculé). Vingt-six noms, les mêmes que `registres/code-t07/CODE-T07-v2.json` (`d5eb0b66…`, sur `main`) ; **seul `src/controle_ia/t07/reextraction_p3_v1.py` diffère** (`c32696b8…` → `af299587…`) ; les vingt-six empreintes recalculées sur les contenus au commit `799ef383` et sur l'arbre : aucun écart ; aucun fichier `*.py` du dossier hors liste. Les dix compagnons `.sha256` du dossier des pièces sont conformes.

## 4. Brouillon d'addendum (`1369c4814f6aea7ea81839b538344a25499c0d10df1e210eb499ca8f221997cd`, recalculé)

Vérifié contre les pièces, sans écart : empreintes du module (C7 et neuf), de l'essai, des arbres `src/` et `tests/`, du script v4 (égal à `main`), de l'ordre, du texte scellé (par le compagnon et la ligne `SCELLEMENT-T07`), du registre des décisions au commit `12d3b20b`, de la note, de la reproduction et de sa sortie, du journal de la fille (instance, heures 20:17:41Z et 20:17:45Z, libellé du refus), des neuf pièces du § 7 ; S7 descendant de C7, `src` et `tests` égaux ; 24 puis 25 fichiers d'essais ; 485 + 21 ; versions épinglées (`requirements-gpu.txt` inclut `requirements-cpu.txt`) ; recherche d'autres appels au même défaut refaite (`src/` et script v4) : aucun autre ; mutations du § 3.2 rejouées (M1, M9, M10) : mêmes comptes. Complet sur « ce qui change, pourquoi, ce qui ne change pas ». Aucune phrase plus forte que les pièces, sauf la nuance m-2. Compléments : m-2, m-3, m-4.

## 5. Nœud : une seule ligne `CODE-T07` — confirmé, non tranché

Confirmé dans le code épinglé :
- `registre_v1.lire_registre_detail` (l. 191-196) : une clé exigée ou permise présente doit l'être **exactement une fois** (« N ligne(s) CODE-T07, exactement une attendue ») ; `CODE-T07` est exigée aux étapes A et B quand `code_t07_exige` est vrai (`lecture_v2`, l. 414 et 418 ; configuration v8, l. 65).
- `registre_v1.ajouter_ligne` (l. 337-343) refuse une clé déjà présente ; l'en-tête du registre dit « lignes ajoutées, jamais réécrites ».
- `lecture_v2.lire_lignes_actuelles` (l. 352-363) rend la **première** ligne ; lue par `code_t07_v1 verifier` (l. 145, étape 9 du script, l. 365) et par `passe_blanc_v1`/`v2`.
- `code_t07_v1.controler_code` : `src/controle_ia/` de l'arbre exécuté doit égaler le commit cité (l. 103) et les empreintes la liste (l. 109-116) : la ligne actuelle (v2, C7) refuse l'arbre corrigé. Seule contrainte de date : strictement avant la première `OUVERTURE-T07` (l. 76) et avant l'instant d'ouverture ; aucune contrainte envers `SCELLEMENT-T07` ni `GO-LECTURE-T07`. Le journal des ouvertures est absent de `main` : aucune ouverture à ce jour.
- Sur `main`, une seule ligne `CODE-T07` (2026-11-11T05:40:34Z, `CODE-T07-v2.json`).

Voies, avec ce que chacune touche :
1. **Remplacer la ligne en place** (citer `CODE-T07-v3.json`, date neuve). Touche : le registre seul (édition à la main, `ajouter_ligne` ne le fait pas), l'ordre version 2 (P6, l. 291). Ni code, ni script, ni configuration. Écart à la règle « jamais réécrites » du registre partagé (T0.6, T0.7, T0.8, P3-bis) ; l'ancienne ligne ne reste que dans l'historique git.
2. **Garder l'ancienne ligne et en ajouter une** (clé neuve, ou « la dernière compte »). Touche le code épinglé : `registre_v1` (clés connues, règle d'unicité), `lecture_v2`, `code_t07_v1`, `passe_blanc_v2`, leurs essais ; donc second changement de code, liste v4, `ATT`, contre-lecture neuve ; au-delà de la « correction minimale » de R-2593.
3. **Registre neuf** (par exemple `scellements-v2.md`). Touche : la configuration v8 (clé `registre`, l. 25 ; copie scellée sous `prereg/`), le script v4 (nom écrit en dur, l. 132, 181-198, 365), l'ordre, le journal des ouvertures, et les autres tâches qui lisent ce registre. La plus lourde.
4. **Variante de 1 avec trace dans le fichier** (ancienne ligne rendue non lisible comme clé, ligne neuve ajoutée). Reste une réécriture ; la règle (1) du registre refuse une ligne à quatre cellules datée dont la clé est mal formée, et le script lit le chemin de toute ligne à six champs : à essayer en simulation avant d'être proposée.

Je n'ai pas ouvert le texte scellé : je ne sais pas si la règle « jamais réécrit » y figure (le développeur pose la même condition).

## 6. Relevé : fichier dérivé de 7a posé sur l'instance

- **Fait, d'après le script** (`scripts/etape_a_t07_variante_b_v4.sh`, l. 133-148) : le motif `/docs/notes/g0-deux-semaines-v1/` extrait tout le dossier, donc aussi `e3-ter-v1/lecture-7a-v1/` : quatre fichiers suivis à S7 comme sur `main` (noms : `garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json`, `lecture-A-exploratoire-non-opposable-v1.md`, et leurs compagnons). Seule exclusion du motif : `diag/*/lecture-sondes-t06.json*`. `interdit()` (l. 171) ne les nomme pas, et ne joue que sur les chemins cités par un registre.
- **Voulu ?** Rien ne le montre : ni le script, ni l'ordre ne nomment ce dossier ; aucun module de `src/`, aucune configuration, aucun registre nommé ne cite ces fichiers (seuls `scripts/extraire_garde_equivalence_t06_v1.py` et son essai, hors du motif `tests/test_t07_*.py` de l'étape 6). C'est un effet de bord du motif large. La « garde d'équivalence » de l'ordre (l. 6, 110, 467) est celle que le repli calcule sur l'instance, pas ce fichier.
- **Autorisé ?** Ni autorisé ni interdit par la lettre : le § 2.2 de l'ordre scellé (l. 231-233) interdit `donnees/lecture-b-7a-quarantaine-v1`, la branche `essai/t06-explo-v3` et `diag/`, `runs/`, `donnees/` de 7a ; `docs/notes/` n'y figure pas. Le registre (R-2040) dit la pièce « exploratoire, non opposable » sans rien dire de l'instance. L'état était le même au lancement arrêté (fichiers déjà dans S7).
- **Portée** : ce n'est pas un défaut du correctif. À porter à la mère pour l'ordre version 2 : soit l'écrire (présent sur le disque, jamais ouvert par le module ni par la fille), soit l'exclure, ce qui change le script v4 scellé (`4b17d1f0…`) et rouvre sa répétition. Non tranché ici.

## Pièces lues et empreintes

Branche récupérée par refspec explicite ; différentiel, essai, addendum, liste v3, journal et sortie de la mesure, `registre_v1.py`, `code_t07_v1.py`, `lecture_v2.py` (l. 352-363), script v4 (l. 125-200, recherches), ordre scellé (`9b3a04da…`, § 2 et lignes citées), `registres/scellements-v1.md` (clés et dates), `registres/decisions.md` (R-2601, et les deux lignes signalées), note du diagnostic (une ligne), journal de la fille (lignes de l'arrêt).
