# Lecture pour le lancement du palier 0b — pièce d'autorisation du verrou, étapes 8 et 9, commande — v1

- Lecteur neuf, modèle O. Lecture seule, 2026-11-20 (`date -u` : Fri Nov 20 14:36:28 UTC 2026). Aucun programme du palier exécuté, aucun tirage, aucune écriture dans le dépôt, aucun appel à un fournisseur, aucune dépense, aucun refus de permission, de classifieur ni de garde.
- Abréviations : **P** = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` ; **T** = `P/preenregistrement-heritage-palier-0b-etage-processeur-v13.md` ; **C** = `P/code-v5/src/controle_ia/heritage_etage_processeur_v1/` ; **R** = `P/code-v5/rapport-developpeur-code-palier-0b-v5.md` ; **V** = `P/verification-code-palier-0b-v5-v1.md`.

## 0. Empreintes vérifiées avant lecture

- T : `sha256sum` rend `d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959`, égale à son compagnon (une ligne, nom de base juste) et à l'empreinte du mandat. Le compagnon de T tel que le rend `git show origin/main:…v13.md.sha256` (référence locale `origin/main` = `2b6d04391b28034869c97f75e266f83b4a7fed28`, sans `git fetch`) porte la même empreinte.
- Code : `env -C C sha256sum -c` sur les compagnons de `tirages.py`, `graines.py`, `etapes.py`, `constantes.py`, `audit.py`, `mecanique.py`, `mondes.py`, `registre.py`, `organisme.py`, `executeur.py`, `__init__.py`, `analyse.py` : 12 « OK ». `env -C P/code-v5 sha256sum --quiet -c ../table-empreintes-code-v5.txt` : aucun échec (58 lignes). Cinq empreintes recalculées (`src/controle_ia/__init__.py`, `graines.py`, `tirages.py`, `etapes.py`, `constantes.py`) sont égales, à l'octet, aux lignes 34, 47, 57, 44 et 39 de la table de T.
- R et V : `sha256sum -c` de leur compagnon, « OK » chacun.
- Le commit `e308b84d68a85416fab1a80b0c116858d24b85a5` est un ancêtre de la référence locale `origin/main` (`git merge-base --is-ancestor`, code de sortie 0) — contrôle local, sans `git fetch` ; il ne remplace pas celui de la mère (silence n° 15).

## 1. La pièce d'autorisation du verrou

### 1.1 Chemin exigé par le code

- Chemin relatif à la racine de l'arbre lancé : `prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md` (C/constantes.py:17), joint à la racine par `os.path.join(self.racine, CHEMIN_PIECE_D_AUTORISATION)` (C/graines.py:257). Le même chemin est gelé par T:332 (B8, « Version 9 ») et T:930 (annexe H, « Version 9 », § 3), « sur `main` ».
- La racine est un argument de `Autorisation(texte, racine)` (C/graines.py:250-252) ; elle doit aussi porter `registres/go.md` (C/constantes.py:19 ; C/graines.py:224).
- Constat : à la référence locale `origin/main`, ce chemin n'existe pas encore (`git cat-file -e` : « does not exist »). La pièce reste à écrire, comme T:994 le dit.

### 1.2 Forme exacte que le code lit (`lire_piece`, C/graines.py:200-219)

- **Noms des champs, à l'octet, dans cet ordre** (C/constantes.py:18 ; T:332, B8 « Version 12 ») :
  1. `identifiant du GO`
  2. `commit du code`
  3. `empreinte du texte scellé` (avec « é » de « scellé », en UTF-8)
  4. `heure`
- **Séparateur** : `" : "` — une espace, un deux-points, une espace —, cherché par `ligne.partition(" : ")` (C/graines.py:211) ; la première occurrence coupe le nom de la valeur.
- **Ordre exigé** : oui. Le nom au rang r doit être `CHAMPS_DE_LA_PIECE[r]`, sinon refus « au rang … (ordre de la décision R-4123) » (C/graines.py:214-215) ; un nom inconnu ou répété est refusé (C/graines.py:212-213).
- **Nombre de lignes** : exactement quatre. Le fichier est lu en entier puis coupé par `split("\n")` ; un seul `""` final est retiré (un saut de ligne final permis) ; tout autre compte est refusé (C/graines.py:203-208). Donc : une ligne vide en plus, deux sauts de ligne finaux, une ligne de titre ou de commentaire → refus.
- **Blancs** : la valeur ne doit être ni vide ni entourée de blancs (`v != v.strip()` → refus, C/graines.py:216-217). Un blanc en tête de ligne ou entre le nom et « : » (autre qu'une espace) fait un nom inconnu → refus (C/graines.py:212). Une tabulation à la place d'une espace dans le séparateur → refus.
- **Casse** : les noms sont comparés à l'octet (`nom not in CHAMPS_DE_LA_PIECE`, C/graines.py:212) : « Identifiant du GO » ou « identifiant du go » → refus. Le commit et l'empreinte sont comparés à l'octet à des valeurs en minuscules (C/graines.py:265-268) : des majuscules hexadécimales → refus. Pour l'heure, voir plus bas : `strptime` est insensible à la casse.
- **Encodage** : lu en `utf-8` (C/graines.py:203), non `utf-8-sig` : une marque d'ordre des octets (BOM) en tête collerait au premier nom → refus.
- **Fin de ligne** (constat de lecture, non éprouvé) : le fichier est ouvert en mode texte sans `newline=` (C/graines.py:203), c'est-à-dire avec les fins de ligne universelles de Python : des fins `\r\n` sont lues comme `\n` et ne sont **pas** refusées par `lire_piece`. T:332 dit « un saut de ligne final est permis, aucune autre ligne ne l'est », sans parler des fins `\r\n`. À écrire avec des fins `\n` seules ; l'empreinte de la pièce porte de toute façon sur ses octets.
- **Formes des valeurs** :
  - `identifiant du GO` : expression `^GO-\d{4}-\d{2}-\d{2}-\d{2,}$` (C/graines.py:109, contrôlée l. 261-262 ; T:332).
  - `commit du code` : aucune expression propre ; il doit être égal à l'octet au commit lu dans la ligne « Commit du code d'analyse » du texte (C/graines.py:265-266).
  - `empreinte du texte scellé` : égale à l'octet à l'empreinte SHA-256 en hexadécimal minuscule recalculée sur le texte présenté (C/graines.py:255, 267-268).
  - `heure` : l'une de deux formes de `strptime` (C/graines.py:112, 235-242 ; T:332 ; R:68 ; V:57) : `%a %b %d %H:%M:%S UTC %Y` (sortie de `date -u` en locale C, par exemple `Fri Nov 20 14:36:28 UTC 2026` ; un jour d'un chiffre précédé de deux espaces est admis, essai à C/../../tests/test_heritage_etage_processeur_v1_verrou.py:130) ou `%Y-%m-%dT%H:%M:%SZ` (`2026-11-20T14:36:28Z`). La date doit exister ; le jour de la semaine n'est pas comparé à la date ; des nombres sans zéro de tête sont admis (T:332 ; V:57). Constat de lecture : `strptime` de Python lit les espaces du format comme « un blanc ou plus » et sans égard à la casse ; aucune autre forme (fuseau autre que « UTC »/« Z », millisecondes, décalage `+00:00`) n'est admise.

### 1.3 Comment « scellée » est éprouvé

- Par `verifier_scelle` (C/graines.py:119-140), réécriture de `controle_ia.scellement.verifier` parce que le paquet se lance avec `PYTHONPATH=src` seul (C/graines.py:16-17 ; T:332 ; R:72), confrontée au module du dépôt par l'essai `test_scelle_au_sens_du_depot` sur neuf cas (R:115 ; V:32).
- Exigences : le fichier existe ; le compagnon `<chemin>.sha256` existe ; il porte **une seule ligne non vide** (les lignes blanches sont ignorées, C/graines.py:129) ; cette ligne a la forme `^([0-9a-f]{64})  (\S.*)$` — 64 chiffres hexadécimaux minuscules, **deux espaces**, le nom (C/graines.py:106, 132) ; le nom est **le nom de base** du fichier, `autorisation-verrou-palier-0b-v1.md` (C/graines.py:135) ; l'empreinte recalculée est égale (C/graines.py:137-139).
- Conséquences pratiques : un compagnon fait par `sha256sum` lancé depuis la racine avec le chemin relatif (`prereg/…/autorisation-verrou-palier-0b-v1.md`) porte le chemin, non le nom de base → refus ; une sortie en mode binaire (`<empreinte> *nom`) → refus. La forme sûre est celle de la consigne : `env -C <racine>/prereg/organisme-auto-conception-v9/palier-0b sha256sum autorisation-verrou-palier-0b-v1.md` redirigé vers `…/autorisation-verrou-palier-0b-v1.md.sha256`, ou `controle_ia.scellement sceller` du dépôt.
- La même épreuve s'applique au texte présenté (C/graines.py:255) : le compagnon de T (une ligne, `d9591d5b…  preenregistrement-heritage-palier-0b-etage-processeur-v13.md`) a cette forme.

### 1.4 À quoi chaque valeur est comparée (`Autorisation.verifier`, C/graines.py:254-272)

| champ | comparé à | lieu |
|---|---|---|
| `identifiant du GO` | forme `GO-AAAA-MM-JJ-NN` ; puis présent comme **première cellule**, blancs retirés, d'une ligne commençant par « \| » de `<racine>/registres/go.md` | C/graines.py:109, 222-232, 261-264 ; T:332, T:931 (b) |
| `commit du code` | le premier `` `<40 hex>` `` de la **seule** ligne de T qui commence par `- Commit du code d'analyse : ` (refus s'il y en a zéro ou plusieurs) | C/constantes.py:22 ; C/graines.py:108, 143-154, 256, 265-266 ; T:7, T:332 |
| `empreinte du texte scellé` | l'empreinte recalculée du texte présenté (argument `texte`) | C/graines.py:255, 267-268 ; T:931 (b) |
| `heure` | forme seule (deux formes UTC) | C/graines.py:235-242, 269 ; T:332 |

S'y ajoutent, à chaque vérification, deux conditions qui ne lisent pas la pièce : le texte présenté est scellé (C/graines.py:255) et chaque module lancé — les `.py` du dossier du paquet importé et le `__init__.py` du paquet parent, lus là d'où le paquet est importé — a l'empreinte que la table de T lui donne, la table ne nommant sous `src/` aucun autre fichier (C/graines.py:173-197, 270 ; T:332). La vérification a lieu à la construction de l'`Autorisation` puis de nouveau, sur disque, au début de `lancer_famille` (C/tirages.py:294-304, 309 ; T:332). Le manifeste inscrit l'empreinte du texte, celle de la pièce et l'heure (C/tirages.py:234-237) ; il n'inscrit ni le GO ni le commit de la pièce (T:332 ; R:74).

Constats sur les valeurs connues :
- Ligne de T qui commence par `- Commit du code d'analyse : ` : une seule (T:7 ; recherche `^- Commit du code d'analyse : `, compte 1) ; son premier groupe entre accents graves est `e308b84d68a85416fab1a80b0c116858d24b85a5` (T:7).
- `GO-2026-11-20-66` est la première cellule de la ligne 597 de `registres/go.md` à la référence locale `origin/main` (`git grep`) : « Palier 0b … (préenregistrement v13 scellé, d9591d5b…) : lancement accordé … après la pièce de contrôle et la pièce d'autorisation de la mère ». **Il est absent du `registres/go.md` de l'arbre de travail actuel** (branche `lot/compte-organisme-v1`, commit `72bffed91ae08b341e6a6862ef79dc0e6815d0f9`), qui ne porte aucune ligne `GO-2026-11-20-…` : cet arbre, pris comme racine, ferait refuser le verrou (C/graines.py:263-264).

### 1.5 Exemple rempli

Contenu exact du fichier `<racine>/prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md` (quatre lignes, fins `\n`, un saut de ligne final permis, aucune autre ligne ; l'heure ci-dessous est un exemple de forme, à remplacer par la sortie de `date -u` au moment où la mère écrit la pièce) :

```
identifiant du GO : GO-2026-11-20-66
commit du code : e308b84d68a85416fab1a80b0c116858d24b85a5
empreinte du texte scellé : d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959
heure : Fri Nov 20 14:36:28 UTC 2026
```

Forme ISO également admise pour la quatrième ligne : `heure : 2026-11-20T14:36:28Z`. Compagnon, dans le même dossier, `autorisation-verrou-palier-0b-v1.md.sha256`, une ligne : `<64 hex de la pièce>  autorisation-verrou-palier-0b-v1.md`.

## 2. Les étapes 8 et 9 : ce que la pièce de contrôle de la mère doit fixer

### 2.1 Ce que la v13 demande

- Chemin de la pièce de contrôle : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/controle-lancement-palier-0b-par-la-mere-v1.md` ; complément pour le silence n° 8, joué après le lancement : `…/controle-lancement-palier-0b-par-la-mere-v1-complement-1.md` (T:994, alinéa « Version 13 », décision R-4292).
- Forme : celle de la note du contrôle du manifeste de la mesure « portée à 200 » (`0dcd2dc7…`) — une table, point par point, l'attendu et le constaté (T:994, T:990).
- Contenu avant le lancement (T:332 ; T:991-992 ; T:994) :
  - **silence n° 14** : la racine de l'arbre lancé et le texte présenté des étapes 8 et 9 (« donnés par l'appelant de l'autorisation ; aucun programme de lancement des étapes 8 et 9 n'existe encore, qui les donnerait », T:991) ;
  - **silence n° 15** : « sur `main` », contrôlé par `git merge-base --is-ancestor` (T:992).
- Après le lancement, au contrôle du manifeste (complément) : **silence n° 8**, le champ `commit` du manifeste comparé à la main au champ `commit du code` de la pièce du verrou (T:990, T:994).
- Écrite et scellée par la mère avant le lancement des étapes 8 et 9 ; inscrite au registre des décisions ; ce qui s'écrit après le scellement va sous un nom neuf (T:994 ; T:386).

### 2.2 Ce que le texte ou le code fixent déjà

- **Texte présenté** : fixé par son empreinte, non par son chemin (T:994 : « son champ `empreinte du texte scellé` fixe le texte présenté par son empreinte, non par son chemin » ; R:207). La ligne `GO-2026-11-20-66` nomme « préenregistrement v13 scellé, d9591d5b… » (`registres/go.md` à `origin/main`, l. 597). Le texte est donc la v13, `d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959`. **Son chemin** n'est fixé ni par le texte ni par le code ; le seul lieu connu est P (T est versé là ; ligne `- Mandat` de T:71 et chemins de T:994 sous ce même dossier). Il doit être scellé, au nom de base inchangé (C/graines.py:255).
- **Racine de l'arbre lancé** : **aucune valeur n'est écrite** (T:991 ; T:994 : la pièce du verrou « ne nomme pas la racine, qui est l'arbre où le verrou la trouve » ; R:80 ; V:69). Le code n'en impose que des propriétés : elle porte la pièce et son compagnon au chemin de 1.1, et `registres/go.md` avec `GO-2026-11-20-66` en première colonne (C/graines.py:224-232, 257). B8 veut la pièce « sur `main` » (T:332, T:930). D'où : une copie de travail de `main` qui contient la pièce scellée et la ligne GO-66 ; l'arbre de travail actuel (branche `lot/compte-organisme-v1`, `72bffed9…`) ne convient pas en l'état (1.4).
- **Racine des graines** (si la « racine » demandée est celle-là) : fixée, `numpy.random.SeedSequence(2026111902)` (T:332 ; C/constantes.py:26 ; C/graines.py:278, 298). **Clé de dérivation** : les quatre premiers mots de 32 bits, gros-boutistes, du SHA-256 de l'étiquette en UTF-8 (T:332 ; C/graines.py:90-93) ; étiquette « nom=valeur » jointe par « | », dans l'ordre gelé (C/graines.py:41-42, 68-80), couche « decisif » à l'étape 8, « confirmation » à l'étape 9 (C/graines.py:39-40 ; C/tirages.py:78-80). Aucune autre clé n'est à fixer : aucune empreinte du texte n'est écrite dans le code (C/constantes.py:6-8 ; T:332).
- **Code lancé** : les modules lus là d'où le paquet est importé doivent égaler la table de T (C/graines.py:173-197). Le paquet versé est `P/code-v5/src/` (T:503) ; la pièce de contrôle peut donc nommer aussi le dossier `src` importé, ce que rien n'exige.

### 2.3 Ce que rien ne fixe

- Le chemin du texte présenté sous la racine, et la racine elle-même : à fixer par la mère dans sa pièce de contrôle (T:991, T:994).
- Le dossier des sorties et du manifeste des étapes 8 et 9 : annexe C dit « Où (proposé) » `runs/heritage-palier-0b-v1/` pour les manifestes et `diag/heritage-palier-0b-v1/` pour les sorties brutes (T:496) ; or `lancer_famille` écrit le manifeste **dans** le dossier des sorties (`os.path.join(dossier, "manifeste.json")`, C/tirages.py:314) et exige un dossier neuf (`os.makedirs(dossier)` sans `exist_ok`, C/tirages.py:310). Rien ne tranche.
- La valeur du champ `commit` donné à `lancer_famille` (argument `commit`, C/tirages.py:307, 248) : donnée par l'appelant, non contrôlée (silence n° 8 ; T:990) ; la valeur attendue est celle de la pièce, `e308b84…`.
- Les fichiers gelés passés en `fichiers_geles` (fréquences M12 de l'étape 5, réglages de l'étape 6 ; C/tirages.py:225-228, 252 ; T:332) : produits par les étapes 5 et 6, non encore faits à ma connaissance (§ 4).

## 3. La commande de lancement

### 3.1 Ce qui est écrit

- **Aucune commande de lancement des étapes 8 et 9 n'est écrite**, ni dans T, ni dans R, ni dans V (T:991 ; R:80 ; V:69). La seule commande écrite est celle des **essais** (R:86) : `PYTHONPATH=src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/code-organisme-94bfd92/orchestrator /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider CHEMIN`, dossier courant `code-v5/`.
- **Aucune fonction `etape_8` ni `etape_9` n'existe** dans le code : le docstring de `etapes.py` les nomme (C/etapes.py:14-15), mais la recherche de `etape_8|etape_9` dans `src/` ne trouve que ce docstring. Il y a `cases_a_confirmer` (C/etapes.py:302-306) et la constante `TIRAGES_DE_CONFIRMATION` (C/etapes.py:309).
- La fonction de lancement d'une couche décisive est **`tirages.lancer_famille(graines, couche, cases, f_par_case, tirages, dossier, commit, fichiers_geles)`** (C/tirages.py:307-316 ; « Étape 8 (ou 9) »). Celle de l'étape 4 est `etapes.lancer_etape_4(graines, couche, dossier, …)` (C/etapes.py:198-210), sans autorisation (couche « mecanique »).

### 3.2 Arguments, interpréteur, variables

- `graines` : `Graines(racine=RACINE_GRAINES, autorisation=Autorisation(texte, racine))` (C/graines.py:250, 278-284) ; sans autorisation, la couche décisive est refusée et consignée (C/tirages.py:298-301 ; C/graines.py:291-295).
- `couche` : `"decisif"` (étape 8) ou `"confirmation"` (étape 9) (C/graines.py:39-40).
- `cases` : de `etapes.plan_des_cases(reglages)` (C/etapes.py:48-146), `reglages` au format de `reglages_pour_le_plan` (C/etapes.py:290-299), tiré du fichier gelé de l'étape 6.
- `f_par_case` : fonction case → les huit fréquences gelées (C/constantes.py:168-169 ; les essais passent `lambda c: FREQUENCES_D_ESSAI`, `tests/test_heritage_etage_processeur_v1_statistique.py:130`, `…_verrou.py:137`).
- `tirages` : un seul nombre pour toutes les cases (C/tirages.py:313) ; `TIRAGES_PAR_CASE = 10_000` (C/constantes.py:34), `TIRAGES_CONFIRMATION = 100_000` (C/constantes.py:35).
- `dossier` : dossier neuf (C/tirages.py:310) ; `commit` : chaîne de 40 hex (C/tirages.py:248) ; `fichiers_geles` : dictionnaire des empreintes des fichiers gelés (C/tirages.py:252).
- **Variables `HERITAGE_DEPOT` et `HERITAGE_COPIE_ORGANISME`** : lues par les **essais seulement** (`tests/aides_heritage_etage_processeur_v1.py:4-5, 34, 43` ; `tests/test_heritage_etage_processeur_v1_verrou.py:269-270` ; V:5, V:79) ; aucun module de `src/` ne lit de variable d'environnement (recherche `HERITAGE_|environ|getenv` dans `src/` : aucune occurrence). L'étape 4 reçoit la copie de l'organisme en argument (`organisme.EtageOrganisme(orchestrateur, racine, tache)`, C/organisme.py:91-97).
- **Interpréteur** : `PYTHONPATH=src` seul (T:332 ; R:72) ; Python 3.13.18 du `.venv` du dépôt chez le développeur et le vérificateur (R:8 ; V:5), option `-B` (R:86), sans quoi Python écrirait des `__pycache__` dans le dossier du code. Ici : `/home/user/controle-ia-travail/.venv/bin/python -I -B --version` rend `Python 3.13.18`. Attention : l'option `-I` fait ignorer `PYTHONPATH` ; elle ne convient donc pas à une commande qui s'appuie sur `PYTHONPATH=src`.
- **numpy** : au moins 1.25, contrôlé à la construction de `Graines` (C/graines.py:53-57, 279 ; T:497 ; règle R9) ; la version est inscrite au manifeste (C/tirages.py:247). Dans le `.venv` : numpy 2.4.6 (`pip show numpy`). Aucune version exacte n'est gelée par T.

### 3.3 Ordre des étapes (T:387-389)

3. audit du générateur (`mondes.audit_du_generateur`, C/mondes.py:624) ; 4. couche mécanique (`etapes.lancer_etape_4`, C/etapes.py:198) ; 5. gel des fréquences (`frequences.geler`, C/frequences.py:101) ; 6. étalonnage et gel des réglages (`etapes.etape_6`, C/etapes.py:256-287 ; `etalonnage.geler_reglages`, C/etalonnage.py:177) ; 6 bis et 7. reprise mécanique et garde S8 (`etapes.etape_6_bis_et_7`, C/etapes.py:213-232) ; **8. tirages décisifs de toutes les familles, en un seul lancement, aucune case lue avant que toutes soient calculées et scellées** ; **9. tirages de confirmation, s'il y en a, lancés par programme selon la règle de C1 et de C4** (`cases_a_confirmer`) ; 10. analyse ; 11. verdict (règle R13). Les étapes 3 à 7 ne demandent pas d'autorisation (silence n° 16, T:993).

### 3.4 Forme que le code impose (non écrite par le texte ni par le rapport ; non lancée ; à écrire par la mère)

Dossier courant `<racine>/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v5`, comme les essais (R:86), avec un programme de lancement **hors** du dossier du paquet (un `.py` de plus dans `C` ferait refuser le verrou, C/graines.py:180-181, 191-193) :

```
PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B <programme-de-lancement-etape-8>.py
```

Le programme, dans l'ordre que le code impose :

```
from controle_ia.heritage_etage_processeur_v1 import constantes as K, etapes as EP, graines as GR, tirages as TI
a = GR.Autorisation(TEXTE, RACINE)                 # TEXTE et RACINE : ceux de la pièce de contrôle (silence n° 14)
g = GR.Graines(K.RACINE_GRAINES, autorisation=a)
cases, non_atteignables = EP.plan_des_cases(reglages)       # reglages : fichier gelé de l'étape 6
TI.lancer_famille(g, "decisif", <cases à tirages emboîtés>, lambda c: f, K.TIRAGES_PAR_CASE, DOSSIER,
                  "e308b84d68a85416fab1a80b0c116858d24b85a5", {<fréquences>: <empreinte>, <réglages>: <empreinte>})
```

Ce que cette forme laisse ouvert (constats de lecture du code, non éprouvés) :
- `lancer_famille` passe le même `tirages` à toutes les cases et ignore les clés `"tirages"` et `"sources"` que `plan_des_cases` met sur chaque case (C/tirages.py:312-313 ; C/etapes.py:111-114, 118-120, 135-139, 140-145). Les cases « sources » (200 000 sources : famille D en mode `sources`, famille E, famille H en mode `sources`, point 6 ; T:324-328) **n'ont pas de programme de lancement** dans le code v5.
- Deux cases d'une même famille qui ne diffèrent que par ce mode ont le même nom (`nom_de_case`, C/tirages.py:183-194 : famille, proposeur, dose, taux, taille ou force, retrait, repère, repli — pas le mode) : passées ensemble à `lancer_famille`, la seconde ferait lever `os.makedirs` sur un dossier existant (C/tirages.py:160-161). Il faut donc ne passer que les cases à tirages ; ce tri n'est écrit nulle part.
- L'étape 9 : `cases_a_confirmer(comptes_c1, comptes_c4)` rend des triplets `("C1", k, dose, taux)` / `("C4", k, proposeur, taux)` (C/etapes.py:302-306) ; aucune fonction ne les change en cases ni ne lance la couche « confirmation » à 100 000 tirages ; aucune fonction ne calcule `comptes_c1`, `comptes_c4` à partir des sorties scellées de l'étape 8 dans les modules lus (le module `analyse` n'a pas été lu en entier par moi).
- « En un seul lancement » (T:388) : `lancer_famille` écrit un manifeste par appel (C/tirages.py:314-315) ; un second appel pour les cases « sources » ferait un second manifeste.

## Ce que je n'ai pas pu établir

1. **La racine de l'arbre lancé** : aucune valeur dans T, R, V ni le code (T:991, T:994 ; R:80) ; seules ses propriétés sont imposées (1.4, 2.2). L'arbre de travail actuel (`lot/compte-organisme-v1`, `72bffed9…`) ne porte pas `GO-2026-11-20-66` et ne convient pas en l'état.
2. **Le chemin du texte présenté** : fixé par son empreinte seulement ; P est le seul lieu où je l'ai lu ; aucune copie sous `prereg/` n'est nommée par T.
3. **La commande de lancement des étapes 8 et 9** : aucune n'est écrite ; aucun programme n'existe (T:991) ; `etape_8` et `etape_9` sont nommées dans un docstring sans être définies (C/etapes.py:14-15). La forme du § 3.4 est la mienne, déduite du code.
4. **Les cases « sources » de B8** (D, E, H en mode `sources`, point 6) : je n'ai trouvé dans le code v5 aucun chemin qui les tire sous la couche « decisif » ; ni la règle qui les sépare des cases à tirages, ni la manière de tenir « un seul lancement » avec elles.
5. **L'étape 9** : aucune fonction qui calcule les comptes de C1 et C4 depuis les sorties scellées et qui lance la confirmation ; je n'ai pas lu `analyse.py` en entier.
6. **L'état des étapes 3 à 7** : je n'ai trouvé aucune trace des fichiers gelés (fréquences M12, réglages) dans les sources données ; je ne sais pas s'ils existent ; sans eux, l'étape 8 n'a ni `f` ni `reglages`.
7. **La version de numpy employée par le développeur et le vérificateur** : R:8 et V:5 ne la disent pas ; le `.venv` porte aujourd'hui 2.4.6 ; T ne gèle que « au moins 1.25 ».
8. **Les fins de ligne `\r\n` de la pièce** : acceptées par `lire_piece` à la lecture du code (ouverture en mode texte), ce que T:332 ne dit pas ; non éprouvé (je n'ai rien exécuté).
9. **`main` à jour** : mes contrôles sur `origin/main` portent sur la référence locale (`2b6d0439…`), sans `git fetch` ; la mère doit les refaire sur `main` au moment du lancement (silence n° 15).
10. **Le registre des décisions** (R-4292, R-4285) et la note `0dcd2dc7…` : non relus par moi ; je cite leur lettre telle que T la reprend (T:332, T:990, T:994).
