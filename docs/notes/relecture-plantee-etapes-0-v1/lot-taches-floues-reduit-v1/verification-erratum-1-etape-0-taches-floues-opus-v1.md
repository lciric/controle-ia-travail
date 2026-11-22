# Vérification de l'erratum 1 de l'étape 0 des tâches floues (v1)

- **Vérificateur** : Claude Opus 5.5, le même contre-lecteur que pour la version 1 et la version 2. Je n'ai écrit aucune des pièces relues. Aucun appel payant, ni commit ni poussée. Écrit le 21 novembre 2026.
- **Pièces vérifiées** (empreintes recalculées, égales à leurs compagnons) :
  - `conception-etape-0-taches-floues-v2-erratum-1.md`, `b308b547be6022c4673ea10243e6a51f9eb781530bf97f1df21779f368ba90e1` ;
  - `preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-1.md`, `d26c132ac64c574558ca2b0f7f2820371a121667eb592d63e4e2fa453b45deb6` ;
  - `essai-garde-g1-erratum-1-v1.py`, `87c3df206a36e2e4bc4bf38a6eabd4a580313458354b68cd9f1961e2bbd4399f`, et sa sortie `.txt`, `1c965b0e7ce473f69cdab78428c44748bf65b20d5cb904300033abd623db9090` ;
  - `recalcul-e3-erratum-1-v1.py`, `a558d1743e433dacda6a4822223decd8b03226b891b6a37a4e1987d4925c4ab0`, et sa sortie `.txt`, `08dc289daa60e89d7493ac951e4ffca2e99b2d3163c266ab14fedf7f74d11c68`.
- **Cloisonnement** : inchangé. Je n'ai rien ouvert de `docs/notes/protocole-x-dommage-v1/`, ni aucun fichier interdit par son nom, ni aucun résultat de course. Aucun outil ni classifieur ne m'a opposé de refus.

## 1. Rejeux

- L'essai de la garde de cloisonnement, `python3 essai-garde-g1-erratum-1-v1.py` (Python 3.13.18, numpy 2.5.3), rend le code 0 et une sortie **identique à l'octet** à son `.txt`. Les cinq cas sont conformes. Le rejeu ne laisse aucun dossier `__pycache__` dans le dossier.
- Le recalcul des deux majorants, `python3 recalcul-e3-erratum-1-v1.py calculs-etape-0-taches-floues-v2.py`, rend une sortie **identique à l'octet** à son `.txt`. Il demande en argument le chemin du programme v2, comme le dit son en-tête ; lancé sans argument, il échoue.

## 2. E1 à E5

| Erreur | État | Lieu | Remarque |
|---|---|---|---|
| E1, garde de cloisonnement et sous-modules de numpy chargés à la demande (important) | **porté juste** | erratum de la conception, E1, lieux 1 à 3 ; erratum du brouillon, E1 | Les étapes 0 à 6 du lanceur se lisent sans choix. La liste fermée de préchargement est fixée en code et consignée au manifeste avec la version de numpy. L'échauffement attrape un oubli de la liste avant la lecture du lot servi. Un import neuf après l'armement reste un arrêt. Il y a trois artefacts, dont un sur un chemin que l'échauffement n'exerce pas, et le cas sain demande un tirage de pièce et un appel à `numpy.unique`. Tout cela est éprouvé par l'essai. |
| E2, artefact de lecture de fichier (mineur) | porté juste | erratum de la conception, E1 lieu 3, et E2 | `numpy.fromfile(__file__, dtype=numpy.uint8)` : l'essai le voit armé, sur un événement `open`. |
| E3, deux majorants de « borne reportée en service » (D3) dans F7 (mineur) | porté juste | erratum de la conception, E3 ; erratum du brouillon, E3 | 0,1987 est un arrondi par excès (exact 0,1986078537). Je confirme que 4,7 × 10⁻¹³ est juste (§ 3, point 2). |
| E4, ligne de GO-2026-11-21-69 (mineur) | porté juste | erratum de la conception, E4, lieux 1 et 2 ; erratum du brouillon, E4 | Ligne 668, contenu fidèle. La condition 4 reste ouverte jusqu'à la consignation de la décision sur F4. |
| E5, le noyau (mineur) | porté juste, et mieux que ma proposition | erratum de la conception, E5 ; erratum du brouillon, condition 5 | J'ai vérifié qu'aucun module de `src/`, `scripts/` ou `tests/` et aucune branche ne nomme l'adjudant : il n'y a pas de noyau existant à augmenter. « Module autonome, compatible » est la phrase exacte. L'option (a) ou (b) de D-4 reste au nœud 6. |

## 3. Les deux points de l'auteur

1. **Le second défaut, l'écriture du code compilé (`.pyc`) au chargement des témoins** : c'est un vrai défaut, que ma vérification n'avait pas vu. Pendant la phase de chargement, le crochet n'admet que des `open` en lecture seule. Charger le module des témoins depuis son fichier écrit pourtant `__pycache__/….pyc`, ce qui fait un `open` en écriture et donc un arrêt sur tout témoin. `sys.dont_write_bytecode = True`, posé avant le crochet, est la correction juste et suffisante. Le lancement par `python -I` n'y suffirait pas, puisqu'il ignore la variable `PYTHONDONTWRITEBYTECODE` sans couper l'écriture ; l'erratum fait bien les deux. Je l'accepte.
2. **4,7 × 10⁻¹³ au lieu de mon 4,8 × 10⁻¹³** : l'auteur a raison. Mon recalcul indépendant, au taux non arrondi de 0,05937980642007634 repris du programme v2, donne 4,6894 × 10⁻¹³ par la borne de l'union (et 4,6851 × 10⁻¹³ exactement, 1 − (1 − p)²⁰). Mon 4,76 × 10⁻¹³ venait du taux arrondi à 0,0594. 4,7 × 10⁻¹³ est donc déjà un majorant arrondi par excès, cohérent avec le bloc K. Je retire ma correction sur ce chiffre.

## 4. La liste fermée de préchargement couvre-t-elle tous les témoins ?

Les témoins ne sont encore écrits qu'en pseudo-code (§ 3 de la conception). J'ai éprouvé ici, sous numpy 2.5.3 et avec cette liste préchargée, chacune des opérations que ces pseudo-codes demandent, ainsi que les variantes qu'un développeur prendrait sans doute :
- `default_rng(SeedSequence(…))`, `integers`, `random`, `permutation` et `binomial` ;
- `unique`, y compris avec `return_counts`, et `isin` ;
- `sort`, `argsort`, `argmax`, `lexsort`, `searchsorted`, `bincount`, `cumsum`, `mean`, `array_equal`, `stack` et `concatenate` ;
- `quantile`, `percentile` et `histogram` ;
- `math.lgamma`, `math.comb`, `log1p` et `exp` ;
- `json.loads` et `json.dumps`, ainsi que les conversions `tolist`, `int` et `float`.

**Aucune ne lève d'événement `import` une fois armé.** La liste couvre donc tous les témoins tels que leurs pseudo-codes les décrivent. `numpy.linalg` n'y est pas nécessaire, mais il est sans danger. Deux réserves mineures, qui ne bloquent pas :
- (a) **« Borne reportée en service » (D3) demande une borne de Clopper-Pearson.** Sans scipy, que le contrôle statique refuse, le développeur l'écrira par dichotomie sur la loi binomiale avec `math`. Écrire cette phrase dans le texte du code évite un choix.
- (b) **L'échauffement ne parcourt peut-être pas toutes les branches.** Le lot d'échauffement est à champs constants, et il peut ne pas faire passer les témoins discriminateurs (D1 et D2) par leurs deux branches, « sépare » et « ne sépare pas ». Un oubli de la liste sur une branche non parcourue ne se verrait qu'au cas sain de G1 sur les mondes d'essai, ou sur le banc. Il serait vu, non silencieux, et la règle de rejeu s'appliquerait. Je recommande que la contre-lecture du code (classe B) vérifie que le cas sain de G1 sur les mondes d'essai fait passer chaque témoin par chacune de ses branches.

## 5. Verdict

**Scellable, sous réserve des nœuds du directeur** et des conditions de scellement 2 à 6 du brouillon. Aucune remarque ne reste ouverte sur les corrections. Les réserves (a) et (b) du § 4 sont à porter par la contre-lecture du code de classe B, non par le texte scellé. Le texte scellé, sous un nom neuf, porte les empreintes de la conception v2, de ses calculs, des deux errata 1, de l'essai de la garde et de sa sortie (condition 7).

**Nœuds qui restent pour le directeur** :
- le monde du jumeau périmé (F6), avec ou sans plantation, et les écarts à la forme fixe : deux conditions du scellement ;
- la famille tenue à l'écart servie en relevés de décisions ;
- l'étape 1 sur devis, avec le choix de l'isolement ;
- le banc de l'adjudant ou un banc à part ;
- la règle de rejeu (défaut sous 48 heures) ;
- la reconnaissance du monde à ses lois, avant l'étape 2 ;
- la décision de la mère sur le monde des honnêtes très dispersés (F4), à porter à la connaissance du directeur.
