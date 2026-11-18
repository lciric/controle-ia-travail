# Vérification ciblée des versions 2 : correctif (4) de `lens_compare.py` (comparaison des lentilles neurone par neurone), son essai, et l'essai de l'estimateur sur un Llama miniature

Date : 2026-11-18, 04:44 UTC (`date -u`). Auteur : **vérificateur neuf** (R2), qui n'a écrit ni les pièces, ni leur version 1, ni la
contre-lecture précédente. Un seul fichier écrit : ce rapport (sans compagnon `.sha256` : à poser par la mère, R6). Rien de committé ;
rien lu sous `registres/` ni `diag/`.

## Pièces et empreintes vérifiées (`sha256sum` contre chaque compagnon : toutes égales)

| pièce | empreinte |
|---|---|
| `lens_compare-llama-v2.diff` (le correctif) | `f85c36db1dd5722e0570cdd0a1544db565ff93ff8aa578497610960dcf4feca3` |
| `essai-lens_compare-llama-v2.py` (son essai) | `94e5a7d7f20a9d51ad21f5184a262a1ab471608242755c03def66b47f98123b9` |
| `essai-transport-llama-miniature-v2.py` (essai de l'estimateur sur un Llama miniature) | `8147b4312414b58e4d3162a61b9565ffdba5545743f76cbc33005b2ba8a7d049` |
| `correctif-lens_compare-llama-v2.md` (la note) | `5c7b3312e4b171ef21f9b20c5451370f2ec0983a281eda37e17d87dddc99c8de` |
| référence : `contre-lecture-correctif-4-et-essai-llama-miniature-v1.md` | `7444555b51cbf3626cfb30f50df81fa505a9b96a78e9d24d9360ddb3888d3d84` |
| référence : `../texte-gele-tranche-b-beta-v1.md` | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` |
| dépôt voisin, lecture seule | commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, arbre propre avant et après |

## Ce que j'ai fait

- **Lu** : les quatre pièces v2, les pièces v1, la contre-lecture ; dans le texte gelé : garde (f), P.2 (correctif (4), essai du Llama
  miniature), table des artefacts de P.4 ; dans le voisin, sans rien exécuter ni importer : `scripts/checks/lens_compare.py`,
  `neuron_lens/readout.py`, `weights.py`, `catalog.py` (début), `lenses.py` (imports, `load_lens`), `known.py`, `rules.py` et
  `layers.py` (attention, normes, position rotative), `transport.py` (constantes), `tests/test_transport.py`, `pyproject.toml`.
- **Sur le voisin** : `git apply --check` du diff v2 (accepté) ; rien d'autre.
- **Hors du voisin**, dans un dossier jetable : copie du seul `lens_compare.py` au commit épinglé, diff v1 et diff v2 appliqués par
  `patch`, empreintes, comparaison des deux fichiers corrigés ; fonction `statiques` et table `FAUTIVES` de l'essai extraites par
  l'arbre syntaxique et jouées sur le fichier publié, le fichier corrigé et les sept copies fautives ; **recalcul par mon propre code**
  (formules de `read` et de `rms_norm_columns` recopiées à la lecture, aucun import) de l'accord du premier jeton et du recouvrement
  sur les doubles de l'essai ; avec `torch 2.15.0` (processeur) et `transformers 5.23.0`, sans le voisin : construction des modèles
  miniatures de l'essai, fréquences de la position rotative, effet de la mise à l'échelle sur la sortie ; `diff` de la première partie
  contre `tests/test_transport.py` ; `pytest` installé à part pour vérifier, sur un fichier factice de même nom, la collecte d'un
  fichier à tirets situé hors de la racine, le paramétrage et `tmp_path`.
- **Non fait** (règle stricte) : ni le contrôle fonctionnel de l'essai de `lens_compare`, ni l'essai du Llama miniature n'ont tourné.

## Verdicts par pièce

| pièce | verdict | raison |
|---|---|---|
| `lens_compare-llama-v2.diff` | **employable** | s'applique ; ne diffère de la v1 que par l'ouverture exclusive ; empreinte du fichier corrigé juste |
| `essai-lens_compare-llama-v2.py` | **employable** | les quatre majeures sont traitées dans le code ; contrôle fonctionnel discriminant, valeurs 4/14 et 7/14 reproduites ; mineures seulement |
| `essai-transport-llama-miniature-v2.py` | **à corriger** (une ligne) | première partie, prescrite : fidèle et employable telle quelle ; seconde partie, ajoutée : le critère de `ecarts` est plus sévère que la tolérance du dépôt (point neuf N-1) |
| `correctif-lens_compare-llama-v2.md` | **à corriger** (léger) | écrit « aucune tolérance ni règle changée », ce que N-1 dément ; date postérieure à l'heure réelle ; nombre de tests de l'essai de `lens_compare` non écrit |

Comptes des points neufs : **0 bloquant, 1 majeur, 9 mineurs.**

## Ce qui est vérifié et juste

**Le diff v2.** `git apply --check` accepté sur `849bfe16`. Fichier publié : `37b30e98c9771c03ed452ff0ff36b3667c382201fa726180497c03a2b9daf6cd`.
Fichier corrigé par le diff v2 : `c974cc1aa58f81f4b77e63db7cf6905d1a3b6172652a3dc51bf6f0605bacc77a`, **égal à l'annonce**. Fichier corrigé
par le diff v1 : `d083f94d…`, comme la contre-lecture l'avait trouvé. Entre les deux diffs comme entre les deux fichiers corrigés, une
seule ligne change : `open(args.json, "w")` devient `open(args.json, "x")  # jamais d'écrasement (R12)`.

**Contrôles statiques de l'essai de `lens_compare`** (rejoués ici) : fichier corrigé, aucune faute ; fichier publié, **six** fautes
(modèle Qwen en dur ; `MODEL` non importé du catalogue ; `MODEL` affecté ; `kept()` sans modèle ; `cuda` absent de l'affectation de
`dev` ; `--json` absent). Chaque chaîne à remplacer de `FAUTIVES` se trouve exactement une fois dans le fichier corrigé, et chaque
copie se lit par `ast.parse`.

| copie fautive | prise par les contrôles statiques | sinon |
|---|---|---|
| modèle réaffecté | oui (« MODEL réaffecté ») | |
| `cuda` en commentaire seulement | oui | |
| écrasement permis | oui | |
| `kept()` sans modèle | oui | |
| valeur arrondie | non | contrôle fonctionnel seul : 0,29 écrit contre 0,2857 (écart 4,3·10⁻³) |
| recouvrement faux | non | contrôle fonctionnel seul : 0,2857 écrit contre 0,8429 |
| jetons gardés non indexés | non | contrôle fonctionnel seul : 7/14 et 0,8571 écrits contre 4/14 et 0,8429 |

Quatre par les statiques, trois par le fonctionnel seul : c'est ce que la note annonce.

**Le contrôle fonctionnel est discriminant.** Mon recalcul (graine 0 ; ordre des tirages de l'essai : `lm_head` 20×8, poids de norme,
`W_down` 8×7, permutation, puis lentille B ; jetons gardés tirés : 0, 11, 6, 1, 17, 10, 7, 18, 12, 16, 15, 14, 13, 8) donne :

| cas | accord du premier jeton | recouvrement des dix premiers | lignes |
|---|---|---|---|
| fichier corrigé (`lm_head[keep]`) | **4/14** = 0,2857 | 0,8429 | 14 |
| copie « jetons gardés non indexés » (`lm_head[:14]`) | **7/14** = 0,5 | 0,8571 | 14 |

Mêmes valeurs en demi-précision et en précision simple sur le processeur. Les annonces de l'autrice (4/14 et 7/14) sont justes.
L'accord est strictement entre 0 et 1, ne tombe pas sur deux décimales, et diffère du recouvrement.

**Le remplacement des fonctions du module chargé est effectif.** `lens_compare.py` importe `tensors`, `kept`, `load_lens` et
`AutoTokenizer` par `from … import …` : ce sont des noms globaux du module, et `main()` les appelle par leur nom nu (l. 41, 45, 46,
50 du publié). Affecter `m.tensors`, `m.kept`, `m.load_lens`, `m.AutoTokenizer` change donc bien ce que `main()` appelle ; rien n'est
touché dans `transformers`. Les noms demandés à `tensors` (`lm_head.weight`, `model.norm.weight`, `model.layers.2.mlp.down_proj.weight`)
sont ceux du dictionnaire des doubles ; avec `--samples 0`, ni `KNOWN` ni `fmt` ne servent ; la lentille en dictionnaire
`{2: matrice}` convient à `m[layer]`. Le recalcul de l'essai appelle `read` avec les mêmes arguments et le même choix de périphérique
que le fichier corrigé.

**Tests pytest bien formés.** `tmp_path` est une fixture standard, une par cas paramétré ; la copie fautive est écrite sous ce dossier
et chargée par chemin, sous un nom de module distinct ; les imports du voisin passent par la racine ajoutée au chemin. Vérifié sur un
fichier factice de même nom : un fichier à tirets, situé hors de la racine et nommé sans préfixe `test_`, est collecté quand il est
passé explicitement. L'essai compte **10 tests** (empreinte, cas sain, fichier publié, sept copies). `git -C ROOT show HEAD:…` est
correct **si** l'arbre de la machine est un dépôt git dont `HEAD` est le commit publié (voir N-3).

**Essai du Llama miniature, première partie.** Le `diff` contre `tests/test_transport.py` ne contient que : la description ; l'ajout
de la racine au chemin d'import ; l'import de `LlamaConfig, LlamaModel` ; quatre lignes de nom de classe ; un commentaire. `run_with`,
`exact`, `exact_from` et `test_estimates_match_brute_force` sont identiques au mot près ; `atol=1e-4` et graines 0 et 1 inchangées.

**Seconde partie.** Compte de **9 tests** juste (2 recopiés, 2 de base, 2 aux traits de Llama 3.1, 1 contrôle des fréquences,
2 artefacts). `ecarts` reprend les mêmes cibles, les mêmes formules et le même ordre que le test (estimations hors des règles, force
brute sous les règles, trois familles de comparaisons) — **sauf le critère** (N-1).

**Configuration aux traits de Llama 3.1** (`transformers 5.23.0`, sans le voisin) : elle se construit ; `rope_parameters` gardé tel
quel ; `rms_norm_eps` 1e-5 porté par les sept normes ; 4 têtes de requête pour 1 de clés et valeurs, `head_dim` 4 (`q_proj` 16×16,
`k_proj` 4×16), aucun biais, attention « eager », activation `SiLUActivation`. Fréquences : `[1,0 ; 5,248·10⁻⁴]` contre
`[1,0 ; 1,414·10⁻³]` sans mise à l'échelle — la valeur annoncée (5,25·10⁻⁴) est juste, et `test_frequences_mises_a_l_echelle` passera.
La mise à l'échelle n'est pas décorative : remplacer les fréquences par celles du « default » change la sortie de 1,2·10⁻² sur
12 jetons (les documents de l'essai en ont 23 et 24), cent fois la tolérance. À la lecture, le voisin tient ces traits : tables de
position prises au module du modèle, `variance_epsilon` lu sur chaque norme, groupes de têtes lus sur le module d'attention.

**Les deux artefacts échoueront.** Décalage de 10⁻³ : si le cas sain passe (écart ≤ 10⁻⁴), l'écart décalé vaut au moins 9·10⁻⁴ : c'est
une certitude arithmétique, non une vraisemblance. Autre modèle : `tiny_model(initializer_range=0.2)` a 2 têtes de requête, 1 de clés
et valeurs, des normes à 1, contre 4 têtes, 2 de clés et valeurs et des normes tirées ; les sorties diffèrent de 4,0 et les
jacobiens (vraie dérivée, calculés ici sans les règles du voisin) de 14 : l'écart dépassera 10⁻⁴ de plusieurs ordres de grandeur.

**La graine posée dans `ecarts` ne gêne rien.** Les modèles sont construits avant l'appel (arguments évalués d'abord), donc
`torch.manual_seed(2)` ne touche ni leurs poids ni leurs normes ; elle ne fixe que le document tiré. Le test recopié n'appelle pas
`ecarts` et garde ses graines 0 et 1. Le seul tirage du voisin sur ce chemin (`rules._check_norm`, un contrôle des normes) ne dépend
pas de la valeur tirée. `estimate_model or model` est sûr : un module n'a ni `__bool__` ni `__len__`.

## Table des points de la contre-lecture précédente

| point | traité dans le code ? | constat |
|---|---|---|
| majeure 1 (contrôle fonctionnel comparant 0 à 0) | **oui** | lentille B proche de A, 7 neurones ; `0 < accord < 1` exigé (l. 117) ; 4/14 reproduit |
| majeure 2 (pas d'artefact fonctionnel) | **oui** | sept copies fautives, dont trois que seul le contrôle fonctionnel prend ; reproduit |
| majeure 3 (jetons gardés non exercés ; recouvrement non contrôlé) | **oui** | 14 jetons gardés désordonnés sur 20 ; recouvrement comparé à 10⁻¹² ; les quatre chargements exigés, tous les appels notés |
| majeure 4 (commande fragile) | **oui** | pytest, `NEURON_LENS_ROOT`, racine ajoutée au chemin ; `python -I` abandonné |
| majeure 5 (essai du miniature sans artefact) | **oui, avec réserve** | deux artefacts ; critère non identique à celui du test (N-1) ; la forme de l'artefact s'écarte de la lettre de P.4 (N-5) |
| majeure 6 (aucun trait de Llama 3.1) | **oui** | variante construite et vérifiée ; ajout déclaré à la mère |
| mineure 1 (écrasement du JSON) | **oui** | `open(args.json, "x")` dans le diff ; contrôle statique et copie fautive |
| mineure 2 (repli muet sur Qwen3) | hors des pièces | renvoyé au code de course (lecture de `model`, `lenses`, couches, `rows`) ; l'essai exige Llama pour les quatre chargements |
| mineure 3 (révision non épinglée) | hors des pièces | renvoyé à la commande de montage |
| mineure 4 (champs du JSON) | non retenue | motif tenable : liste fermée de P.2 |
| mineure 5 (empreinte du fichier essayé) | **oui** | `test_empreinte_du_fichier_corrige` ; empreinte du publié contrôlée |
| mineure 6 (contrôles par recherche de texte) | **oui** | arbre syntaxique : affectation de `dev`, affectation de `MODEL` |
| mineure 7 (double posé sur la classe ; dossier ; périphérique) | **oui** | double posé sur le module ; `TemporaryDirectory` ; même choix `cuda`, `mps`, processeur |
| mineure 8 (sortie non versée ; `__pycache__`) | **en partie** | `__pycache__` absent ; la sortie des contrôles statiques est rapportée en prose dans la note, non versée en fichier avec compagnon (N-9) |
| mineure 9 (variante de base jamais jouée) | **oui** | déclarée ; `test_base_miniature` ajouté |
| mineure 10 (note ; nom en clair ; version de `transformers`) | **en partie** | nom en clair avant la lettre de la garde ; section 3 de la note ; version décrite mais sans numéro (N-8) |
| mineure 11 (jamais joué, tolérance incertaine) | **oui** (note) | risque écrit ; aucune tolérance changée dans la première partie |
| mineure 12 (hors du champ de l'essai) | **oui** | description de l'essai et note |

## Table des points neufs

| n° | rang | pièce | constat vérifié | correction proposée |
|---|---|---|---|---|
| N-1 | **majeure** | essai du Llama miniature, seconde partie ; note | **`ecarts` n'applique pas le critère du test.** Le test recopié emploie `torch.allclose(…, atol=1e-4)`, dont la tolérance relative par défaut vaut 10⁻⁵ : seuil par élément de 10⁻⁴ + 10⁻⁵·\|référence\|. `ecarts` rend le plus grand écart absolu, comparé à 10⁻⁴ sans terme relatif. Les jacobiens de ces miniatures montent vers 14 (calcul ici, vraie dérivée) : le seuil du dépôt va donc jusqu'à environ 2,4·10⁻⁴ là où les tests ajoutés exigent 10⁻⁴. Les quatre tests sains ajoutés sont **plus sévères** que la « tolérance des essais du dépôt » de la garde (f) : un écart entre les deux seuils ferait une chaîne en défaut que le critère gelé n'aurait pas prononcée. La note écrit pourtant « aucune tolérance ni règle changée ». Sens sûr (jamais un passage à tort), et les artefacts restent valides. | Dans `ecarts`, compter les comparaisons où `torch.allclose(estimation + shift, référence, atol=1e-4)` est faux (sain : 0 ; artefact : au moins 1) ; ou rendre le maximum de \|écart\| − 10⁻⁵·\|référence\|. Sinon, déclarer dans la note que la seconde partie est plus sévère, et que son échec seul n'est pas la garde (f). |
| N-2 | mineure | essai du Llama miniature | Le décalage de 10⁻³ est posé sur les trois familles d'estimations à la fois : l'artefact ne montre pas que chacune des trois comparaisons est vivante (une famille sautée dans `ecarts` passerait). | Trois cas paramétrés, un décalage par famille. |
| N-3 | mineure | essai de `lens_compare` | `git show HEAD:…` suppose que l'arbre de la machine est un dépôt git, que `HEAD` est le commit publié et que le correctif n'y est pas committé. Un arbre copié sans `.git`, ou un correctif committé, fait échouer ce test sans que le correctif soit en cause. | Écrire `849bfe16:` au lieu de `HEAD:` ; dire dans la commande de montage que le correctif reste non committé. |
| N-4 | mineure | essai de `lens_compare` | Un test d'artefact passe sur n'importe quelle faute, non sur la faute attendue (par exemple `NEURON_LENS_MODEL` non posée fait « échouer » les trois copies fonctionnelles). Couvert en pratique par `test_cas_sain`, qui échoue alors. | Exiger le libellé attendu par copie (« écrit … contre recalcul » pour les trois fonctionnelles). |
| N-5 | mineure | essai du Llama miniature ; P.4 | Les artefacts sont des tests qui **passent** quand la comparaison échoue. Ils satisfont R5 pour l'essai, mais ne fournissent pas au code des verdicts la sortie « essai en échec » que la table de P.4 attend pour la garde (f) ; l'artefact de la garde (d) (« signe d'un terme inversé dans une copie de l'essai ») n'est pas dans la pièce. | À la charge du code des verdicts : fabriquer la sortie en échec. Le dire dans la note. |
| N-6 | mineure | essai de `lens_compare` | La marge la plus faible entre premier et deuxième jeton, sur les doubles, vaut 0,012 en demi-précision. Sur `cuda`, un produit en demi-précision peut ranger autrement un pôle : l'accord peut ne pas valoir 4/14. L'essai ne code pas 4/14 en dur (il compare à `read` sur le même périphérique) : sans conséquence sur le verdict, mais l'annonce « 4/14 » n'est acquise que sur le processeur. | Écrire « 4/14 sur le processeur » dans la description. |
| N-7 | mineure | essai de `lens_compare` ; note | Le nombre de tests attendu (10) n'est écrit nulle part, alors que l'essai du miniature écrit le sien (9). Sans lui, « aucun sauté, aucun manquant » ne se contrôle pas. | Écrire « 10 tests passent, aucun sauté ». |
| N-8 | mineure | note | Date de la note : « vers 04:50 UTC », alors que le fichier date de 04:40 et que `date -u` donnait 04:44 à la fin de cette vérification : heure non prise à l'horloge. Version de `transformers` toujours sans numéro. La note dit « cinq lignes de modèle, le reste identique » : exact pour le modèle, mais le commentaire et l'ajout du chemin d'import changent aussi. | Heure par `date -u` ; numéro de version (5.23.0 a servi ici) ; phrase complétée. |
| N-9 | mineure | note | La sortie des contrôles statiques (six fautes ; aucune ; quatre copies sur sept) est rapportée en prose, sans fichier versé ni empreinte (R6). Ce rapport la reproduit, chiffres égaux. | Citer ce rapport et son empreinte, ou verser la sortie. |
| N-10 | mineure, hors des pièces | voisin, `readout.py` l. 12 | `rms_norm_columns` emploie un epsilon de 10⁻⁶ en dur, Llama 3.1 emploie 10⁻⁵. Le facteur est positif et commun à une colonne : le rang des jetons, donc l'accord du premier jeton et le recouvrement, n'en dépend pas ; seules les probabilités imprimées bougent. Aucun correctif nécessaire pour la mesure du texte gelé. | Rien ; à savoir si une probabilité de cette sortie était un jour citée. |

## Non vérifiable ici

- Le contrôle fonctionnel de l'essai de `lens_compare` et l'essai du Llama miniature : jamais exécutés (règle stricte). Les valeurs
  4/14, 7/14, 0,8429 et 0,8571 viennent de mon recalcul sur le processeur, non de `read` du voisin.
- Que la tolérance 10⁻⁴ tienne sur un Llama miniature, variante de base, variante réaliste et variante aux traits de Llama 3.1 :
  risque écrit par l'autrice, entier tant que l'essai n'a pas tourné ; N-1 l'aggrave un peu pour la seconde partie.
- L'import du module `lens_compare` sur la machine (dépendances du voisin : `pyarrow`, `huggingface_hub`, `safetensors`) et le
  comportement sur `cuda` (demi-précision, départage des égalités).
- L'état git de l'arbre sur la machine (N-3) ; la version de `transformers` qui y sera installée.
- La configuration officielle de Llama 3.1 (dépôt sous licence) : les traits repris par l'essai sont ceux que la contre-lecture avait
  lus sur un miroir public ; je ne les ai pas relus à la source.
- Les mineures 2 et 3 de la contre-lecture, renvoyées au code de course et à la commande de montage, qui ne sont pas des pièces lues ici.
