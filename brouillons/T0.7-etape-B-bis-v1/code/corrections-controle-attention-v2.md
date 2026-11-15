# Corrections du contrôle carte-processeur après la contre-lecture du brouillon 5 et du code v2 (brouillon 6, code v3), v2

**Déclaration** : même développeur que `corrections-controle-attention-v1.md` ; commande de la mère après la contre-lecture
`brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md`
(`93b0724dd41b6c0bbfd2ace1ab47475bb3c0af86436361b0d184e5020c29af4e`, « scellable après corrections ») et décisions R-2919 ;
**processeur seulement**, aucune machine, aucun appel payant, aucune dépense ; aucune donnée ni entrée de 7a, 7b, T0.7 ou P3-bis ;
rien sous `diag/`, `donnees/`, `docs/verdicts/` ; **aucun fichier existant modifié** (R12 : versions neuves seulement ; la
tolérance 10⁻⁴, la grille, les familles et les seuils de la course sont inchangés ; seul `MIN_ESSAIS` de l'amorce neuve est
relevé, comme demandé). **Date (UTC)** : 2026-11-15. **Branche** : `prep/t07bbis-code-v1` ; commit du code, du brouillon 6 et de
la liste de la fiche : `6c346a03` (parent `b57a5f47`) ; note d'état de l'arrêt demandé, sortie des essais : `2b47f591` ;
ce rapport, la contre-épreuve et la garde restreinte préparée : commit suivant. Ce rapport remplace, pour la lecture, la note
`etat-corrections-v3-en-cours-v1.md` (`56f90935…`), qui reste (R12).

## Verdict

1. **Brouillon 6 écrit et scellé** : `brouillons/T0.7-etape-B-bis-v1/T0.7-etape-B-bis-v1-brouillon6.md`,
   `bf1be58e4be262b180e5ea952cafd7948942ff450614c901e97318500d874935` = brouillon 5 (`99d88954…`, gardé tel quel) + dix couples
   (c1 à c10) + trois couples de forme (titre, statut, tableau du différentiel 5 → 6 en tête) ; le programme
   `pieces/couples-brouillon6-v1.py` vérifie le retour au brouillon 5 au bit près et que, hors du tableau, seules changent les
   sept lignes que touchent les couples. Rejoué sur une copie : même empreinte.
2. **Code v3** : `validation_imbriquee_v3` (M2, voie (b) : aucune issue « sans objet » ; sonde de contrôle en échec : arrêt ;
   couple tiré à la fin de l'apprentissage parmi les sondes finales finies), `marche_v3`, amorce et lanceur de la course v3,
   `lecture_v2` (M1 : R-PILE, point (7), champ du contrôle lu) ; répétition v3 (m1, m3, m8, m9 : lot reconstruit, règle de
   lecture écrite avant la passe, code 9 si la passe ne compte pas, suffixe unique v4). Chaque version neuve = la précédente +
   un différentiel déclaré (64 couples sur huit fichiers), refait et comparé par les essais.
3. **Incident du lecteur** : garde des variables git de tous les essais (`conftest.py` neuf à la racine), prouvée par un essai sous
   `GIT_DIR` pointé vers un dépôt jouet témoin (rien n'y bouge) et par son artefact (sans la garde, le témoin bouge).
4. **Essais** : suite de B bis **183 passés**, 0 échec, 0 sauté ; arbre de l'instance simulé par les motifs de l'amorce v3 :
   **115 passés, 24 sautés**, minimum de la course relevé à **115** (m2) ; essais du reste du dépôt qui lancent `git`, sous la
   garde : **aucun échec attribué à la garde** (contre-épreuve complète, avec et sans elle, § 3).
5. **Réserve 1 (garde restreinte)** : **nœud**. `conftest.py` est dans la liste de la fiche v3 et pytest ne charge une garde de
   racine que sous ce nom : pas de nom neuf possible. La version restreinte est **préparée et éprouvée hors de l'arbre**
   (`code/garde-git-restreinte-v1/`), non posée : la poser écrase `conftest.py` (écart à R12), à trancher par la mère (§ 5).

## 1. Décisions R-2919, une par une

| décision | ce qui est fait | où | essais |
|---|---|---|---|
| **M2, voie (b)** | sonde apprise pour le contrôle en échec (perte ou paramètres non finis), à 3 ou à 300 époques, déterminisme compris : `GardeArret` « … sonde de contrôle en échec (…) : arrêt (erreur de chaîne) » ; le couple est tiré **à la fin de l'apprentissage des dix sources** parmi les couples dont la sonde finale est finie (`sonde_finie` : w, b, q finis), dans le même ordre trié, avec un générateur neuf de la même graine `bbis/egalite-carte` (même tirage que la v1 quand toutes sont finies : même indice, puis mêmes 256 actions) ; aucun : arrêt ; aucune clé `sans_objet` n'est plus écrite ; le contrôle ne se joue qu'une fois | `validation_imbriquee_v3` (`controle_deux_horizons`, `sonde_finie`, `ControleCarte.jouer`) ; `marche_v3` (appel après la boucle d'apprentissage, étape nommée « contrôle carte-processeur ») ; brouillon 6, couples c2 (plan, point 5), c5 (liste d'arrêt), c7, c10 | `test_sonde_de_controle_en_echec_arrete` (4 cas : attention à 3, linéaire à 300, attention à 300, déterminisme) ; `test_controle_v3_cas_sain_sans_aucune_issue_sans_objet` ; tirage : toutes finies (même couple **et** mêmes listes d'actions que la v1), une non finie (échec ou NaN : tirage attendu parmi les autres), aucune (arrêt), joué deux fois (refus) |
| **M1** | `lecture_v2` (la v1 reste) : réserve **R-PILE** (phrase du brouillon, écrite dès qu'une sonde finale lue est de la famille « attention », sondes nommées) ; point (7) ajouté à la section D ; lecture du champ `controle_carte_processeur` du fichier fermé des sondes : absent, « sans objet » (à toute profondeur), variante inconnue, écart absent, booléen, non numérique, non fini ou au-dessus de 10⁻⁴ pour une famille de la variante, déterminisme de l'attention absent ou faux : `RefusLecture` (arrêt de la lecture) ; liste de la fiche v3 (103 chemins) | `lecture_v2` ; brouillon 6, couple c8 (nom) ; `fichiers-fiche-code-bbis-v3.txt` | `test_lecture_v2_champ_du_controle_sain_et_artefacts` (cas sain et dix artefacts) ; `test_lecture_v2_r_pile_et_point_7_de_la_section_d` (phrases comparées au brouillon 6) ; marche v3 et lecture v2 de bout en bout en mode jouet |
| **m1** | la répétition v3 joue le code de la course v3 sur un **lot neuf** `ac.LotCarte(seqs, appareil)`, comme la course ; elle écrit `lot_reconstruit.egal_au_premier` (jetons réduits, moyenne, écart type, indices comparés au bit près) et le pic de mémoire de la carte (`memoire_carte_max_octets`, rien sur processeur) ; branche de sortie neuve `calcul/t07bbis-repetition-v4`, absente du dépôt distant (`git ls-remote` : 0 ligne, revérifié à l'écriture de ce rapport ; `…-v3`, nom de l'amorce v2, n'a jamais été poussée) | `scripts/repetition_carte_bbis_v3.py`, `scripts/amorce_repetition_bbis_v3.sh`, `scripts/lancer_repetition_bbis_v3.sh` | cas sain : deux lots distincts construits (espion), égaux au bit près |
| **m3 et m8** | **règle de lecture écrite avant la passe**, au texte (couple c4) et au script (docstring, `lecture_de_la_passe`, écrite au fichier de sortie et au résumé de l'amorce) : la passe ne compte que si chaque famille porte un écart numérique ≤ 10⁻⁴ (linéaire à 300 époques, attention à 3) et l'égalité au bit près (déterminisme des deux familles, de l'attention du contrôle, lot reconstruit égal au premier) ; sinon **code 9** ; si elle compte : écart de chaque famille ≤ 10⁻⁵ → « la course part sans nœud » ; entre 10⁻⁵ et 10⁻⁴ → « nœud écrit à la mère avant la course » | idem ; brouillon 6, c4 | sain (« sans nœud », résumé de l'amorce qui l'imprime) ; 5·10⁻⁵ (code 0, nœud) ; écart `None`, chaîne de caractères, égalité fausse (code 9, « la passe ne compte pas ») ; poids de l'attention à 3 époques altérés de 1 % (code 9) ; règle seule aux limites (10⁻⁵ compris sans nœud, 10⁻⁴ compris avec nœud, 1,0000001·10⁻⁴, NaN, déterminisme faux, lot différent : ne compte pas) |
| **m2** | `MIN_ESSAIS=115` dans `scripts/amorce_bbis_v3.sh` = compte des passés de l'arbre de l'instance simulé par les motifs v3 (tous les essais neufs gardés) ; sans les essais v3 l'arbre rendrait 99, sans ceux de la v2 104 : l'arrêt se déclenche | `scripts/amorce_bbis_v3.sh` | `test_amorce_v3_motifs_marche_v3_et_minimum_releve` (égal à la valeur déclarée et > 87) ; arbre simulé |
| **m4** | l'essai « même tirage » compare les listes d'actions passées à `_sequences` par la v1 et par la v3, élément par élément, et le couple | `tests/test_t07bbis_controle_v3.py` | `test_tirage_toutes_finies_meme_couple_et_memes_actions_que_la_v1` |
| **m5** | « (sous la variante (r1) : la linéaire seule) » au point 5 | brouillon 6, c1 | variante (r1) jouée dans le cas sain du contrôle v3 |
| **m6** | « deux piles du processeur » (point 5) ; « quatre piles de calcul du processeur (aucune carte) » (R-PILE) | brouillon 6, c3, c6 | — |
| **m7** | empreinte du second rapport dans le corps, `dd67802d…`, aux deux citations (point 5 et R-PILE) | brouillon 6, c4, c6 | — |
| **m9** | un seul suffixe pour la quatrième passe : **v4** pour la branche de sortie, le dossier des traces, le dossier de l'instance et l'étiquette de l'instance (les fichiers restent en v3, R12) | répétition v3 | `test_suffixe_unique_v4_et_noms_de_la_v3` |
| **Incident** (point 7) | `conftest.py` neuf à la racine (R12 : aucun fichier existant touché) : retire de `os.environ`, **dès son import** (avant `tests/conftest.py` et avant tout module d'essais), `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_COMMON_DIR`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES` et toute variable `GIT_CONFIG*` ; tout sous-processus d'un essai hérite donc d'un environnement propre ; remises à la fin de la session ; extrait sur l'instance (motif `/*`) et cité par la fiche v3 | `conftest.py` | `tests/test_essais_git_propres_bbis_v1.py` : aucune variable dangereuse dans la session ; **sous `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_COMMON_DIR` et `GIT_CONFIG_*` pointés vers un dépôt jouet témoin**, l'essai même de l'incident (`test_t07bbis_lien_mots_et_cout_v1.py`, sept dépôts jouets) laisse le témoin égal (tête, références, empreinte de l'index, réglages, fichiers) ; artefact : les commandes git de l'incident jouées sans la garde déplacent le témoin |

## 2. Différentiel déclaré, fichier par fichier

| fichier (neuf) | depuis | couples | différentiel |
|---|---|---|---|
| `src/controle_ia/t07bbis/validation_imbriquee_v3.py` | `validation_imbriquee_v2.py` | 8 | docstring ; deux `SondeEnEchec` → `GardeArret` (contrôle, déterminisme) ; `ControleCarte` neuve (non héritée : tirage à la fin, parmi les sondes finales finies, `jouer`) ; `sonde_finie` ; champ `tirage` (couples, sondes finales finies) ; `__all__` |
| `src/controle_ia/t07bbis/marche_v3.py` | `marche_v2.py` | 11 | en-tête et point 3 ; import de la v3 ; `controle.apres(…)` retiré de la boucle ; `controle.jouer(ctx, sources, plis)` après la boucle (hors arrêt de débit) ; noms `amorce_bbis_v3.sh` et `marche_v3` |
| `scripts/amorce_bbis_v3.sh` | `amorce_bbis_v2.sh` | 6 | en-tête ; lanceur v3 ; marche `marche_v3` (commentaire et commande) ; motifs : `/scripts/amorce_bbis_v3.sh*`, `/scripts/lancer_bbis_v3.sh*` ajoutés (v1 et v2 gardées) ; `MIN_ESSAIS=115` (commentaire m2) ; blocs marqués inchangés |
| `scripts/lancer_bbis_v3.sh` | `lancer_bbis_v2.sh` | 6 | en-tête ; `amorce_bbis_v3.sh` (7 mentions) ; `lancer_bbis_v3.sh` (3) |
| `src/controle_ia/t07bbis/lecture_v2.py` | `lecture_v1.py` | 8 | en-tête ; amorce v3 ; R-PILE ; point (7) ; `reserve_pile`, `exiger_controle_carte` ; appel dans `lire` ; commande `lecture_v2` |
| `scripts/repetition_carte_bbis_v3.py` | `repetition_carte_bbis_v2.py` | 10 | docstring (règle de lecture) ; import v3 ; étiquette v4 ; `SEUIL_SANS_NOEUD`, `_lots_egaux`, `_memoire_carte`, `lecture_de_la_passe` ; lot reconstruit ; code 9 si la passe ne compte pas |
| `scripts/amorce_repetition_bbis_v3.sh` | `amorce_repetition_bbis_v2.sh` | 9 | en-tête ; lanceur v3 ; dossiers v4 ; `BR_SORTIE=calcul/t07bbis-repetition-v4` ; amorce de la course v3 ; script v3 ; résumé : lecture de la passe |
| `scripts/lancer_repetition_bbis_v3.sh` | `lancer_repetition_bbis_v2.sh` | 6 | en-tête ; étiquette v4 ; noms v3 |
| `tests/aide_t07bbis_differentiels_v3.py` | — | — | les 64 couples (ancien, nouveau, occurrences) et `MIN_ESSAIS_V3 = 115` ; dans l'ensemble de la course |
| `tests/test_t07bbis_controle_v3.py` | — | — | 17 essais, dans l'ensemble de la course (joués sur l'instance) |
| `tests/test_repetition_bbis_v3.py` | — | — | 8 essais, hors de l'ensemble de la course |
| `tests/test_essais_git_propres_bbis_v1.py` | — | — | 3 essais, hors de l'ensemble de la course |
| `conftest.py` | — | — | garde des variables git (ci-dessus) |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt` | `…-v2.txt` | — | 95 chemins + 8 = **103**, triés (`LC_ALL=C`), tous présents et tous dans l'arbre de l'instance simulé : `conftest.py`, `scripts/amorce_bbis_v3.sh`, `scripts/lancer_bbis_v3.sh`, `src/controle_ia/t07bbis/lecture_v2.py`, `…/marche_v3.py`, `…/validation_imbriquee_v3.py`, `tests/aide_t07bbis_differentiels_v3.py`, `tests/test_t07bbis_controle_v3.py` |

Les couples sont tirés des fichiers par blocs de lignes ; chaque essai d'égalité refait la version neuve depuis la précédente et
exige l'égalité exacte : hors de ces lignes, les essais des versions précédentes (blocs marqués de l'amorce et du lanceur, faux
outils de `test_t07bbis_chaine_instance_v1.py` et des répétitions v1 et v2, gardes de la marche) valent pour la v3. Modes des
fichiers : ceux des v2 (amorce et lanceur de la répétition exécutables, les autres non).

## 3. Essais

- **Suite de B bis** au commit `6c346a03` (`tests/test_t07bbis_*.py`, `tests/test_repetition_bbis_v1.py`, `…_v2.py`, `…_v3.py`,
  `tests/test_essais_git_propres_bbis_v1.py`) : **183 passés**, 0 échec, 0 sauté, en 2050 s (machine partagée) ; 155 avant, 28
  neufs (17 + 8 + 3). Sortie : `essais-sortie-corrections-controle-attention-v2.txt` (`fd9282de…`).
- **Arbre de l'instance simulé** (commit temporaire par index temporaire, aucune branche déplacée ; motifs de l'amorce v3 ;
  `git archive | tar -x` ; 336 fichiers, chacun identique au bit près à son objet du commit `6c346a03`) : **115 passés,
  24 sautés** (sautés nommés : chaîne de T0.6 et pièce « mots et coût » absentes de l'extraction), sorties d'erreur vides.
- **Contre-épreuve de la garde sur le reste du dépôt** (75 fichiers d'essais qui lancent `git`, 4 058 essais) : première passe (essais 1 à 2 745)
  arrêtée par sa borne de temps, 9 échecs ; reste par morceaux (essais 2 746 à 4 058) : **1 310 passés, 2 sautés, 1 xfailed,
  0 échec**. Les 9 échecs, rejoués **avec et sans la garde** (`--confcutdir=tests`, qui ne charge pas `conftest.py` de la racine) :
  seuls, les 9 passent dans les deux cas ; par fichier, les mêmes échecs dans les deux cas (4 sur les quatre premiers fichiers,
  3 sur les trois fichiers « ideation » : « l'enveloppe d'Argon v5 attend /home/user/controle-ia-travail », arbre de travail
  hors du chemin du dépôt principal). **Aucun échec attribué à la garde** ; les 9 échecs de la première passe tiennent à la
  charge de la machine. Sortie : `essais-sortie-contre-epreuve-garde-git-v1.txt`.

## 4. Réserves et choix déclarés

1. **Garde git à la racine** : `conftest.py` vaut pour **tous** les essais du dépôt, pas seulement ceux de B bis. Posé tel quel
   (v1), il retire aussi les `GIT_CONFIG*` de la session (ici, des réglages réseau de git : noms seuls lus) ; un essai qui aurait
   besoin de git en réseau les perdrait. Aucun n'en a besoin dans la suite de B bis ni dans les 75 autres fichiers d'essais qui
   lancent `git` (§ 3 : aucun échec attribué à la garde). Restriction préparée, non posée (§ 5).
2. **Tirage déplacé à la fin de l'apprentissage** : en v2, le contrôle se jouait dès que le couple tiré d'avance était appris ; en
   v3, une fois, après les dix sources. Même couple et mêmes actions que la v1 si toutes les sondes finales sont finies ; sinon,
   tirage différent de la v1 (déclaré au texte). Après un arrêt de débit, aucun contrôle n'est joué (aucun score n'est écrit).
   La mémoire tenue est la même (les sources sont déjà gardées jusqu'à l'écriture des fichiers fermés) ; le lot du contrôle est
   construit sur la carte à la fin de l'apprentissage, et non plus au milieu.
3. **Seuil sans nœud** : « écart à 3 époques ≤ 10⁻⁵ pour chaque famille » est lu comme : l'écart du contrôle de chaque famille
   (linéaire à 300 époques, attention à 3) ≤ 10⁻⁵. La linéaire rend de l'ordre de 2·10⁻⁸ : sans effet pratique, mais plus strict
   qu'une lecture limitée à l'attention.
4. **R-PILE et ENC** : la réserve est écrite si une sonde finale lue est « attention » ; j'y compte la sonde finale d'ENC dont le
   réglage commence par « attention- » (interprétation : ENC est une sonde finale lue).
5. **Suffixe v4** pour la quatrième passe (branche, traces, dossier de l'instance, étiquette), selon l'exemple de la commande ; les
   fichiers restent en v3 ; `calcul/t07bbis-repetition-v3` (nom de l'amorce v2, jamais jouée) n'existe pas à distance.
6. **Pic de mémoire** : `memoire_carte_max_octets` est le pic alloué par le processus sur la carte au moment du contrôle, non la
   taille du seul second lot.
7. **Lecture v2 et anciennes marches** : `lecture_v2` refuse un fichier des sondes sans champ du contrôle ou avec une trace
   « sans objet » : elle ne lit donc que la sortie de `marche_v3` (voulu).
8. **Minimum 115** : borne basse ; sur l'instance, la copie des fichiers cités peut faire jouer des essais sautés ici (le compte
   peut monter, pas descendre sans arrêt).

## 5. Nœud : garde restreinte (réserve 1)

- **Décision** : poser la garde restreinte en remplaçant `conftest.py` de la racine, ou garder la v1.
- **Enjeu** : la demande est de ne plus retirer les `GIT_CONFIG*` (réglages réseau de la session) et de ne retirer que `GIT_DIR`,
  `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_COMMON_DIR`, `GIT_OBJECT_DIRECTORY`, sous un nom neuf si le fichier est dans la liste de la
  fiche. Il y est (`fichiers-fiche-code-bbis-v3.txt`), et pytest ne lit une garde de racine que sous le nom `conftest.py` : le nom
  neuf est impossible sans toucher à un fichier existant (`pyproject.toml`, `tests/conftest.py`) ou sans écraser `conftest.py`.
- **Préparé** (`brouillons/T0.7-etape-B-bis-v1/code/garde-git-restreinte-v1/`, scellé) : `conftest-restreint-v1.py` (la v1 moins
  `GIT_ALTERNATE_OBJECT_DIRECTORIES` et le préfixe `GIT_CONFIG`, docstring dite), `essai-garde-restreinte-v1.py` (le futur
  `tests/test_essais_git_propres_bbis_v2.py` : les trois essais de la v1 sur les cinq variables, plus un essai neuf : sous
  `GIT_DIR` vers un témoin et un réglage `GIT_CONFIG_*` posé, l'import de la garde retire `GIT_DIR` et `git config` lit encore le
  réglage), `differentiel-garde-restreinte-v1.diff` (28 lignes changées). Éprouvé dans une copie de l'arbre du commit
  (`git archive`) : **4 passés** ; les 7 `GIT_CONFIG*` de la session restent.
- **Options** : (a) écraser `conftest.py` par la version restreinte, `tests/test_essais_git_propres_bbis_v2.py` neuf, v1 de l'essai
  retirée de la suite, liste de la fiche v4 (la v1 reste lisible au commit `6c346a03`) : réserve levée, mais écart à R12 sur un
  fichier ; (b) garder la v1 et la réserve écrite : aucun écart, essais en réseau privés de leurs réglages git (aucun cas connu).
- **Recommandation** : (a), confiance moyenne (la seule version restreinte possible ; le commit cité par la fiche fixe le contenu).
  Défaut sous 48 heures : (b), sans écart.

## 6. Ce qui reste non éprouvé sans carte

- L'écart carte-processeur de l'attention à 3 époques sur la carte (sur processeur, entre deux piles, 2,9·10⁻⁷ à 5,9·10⁻⁷) : c'est
  ce que la quatrième passe doit lire, sous la règle écrite.
- L'égalité au bit près de deux constructions du lot sur la carte (moyenne et écart type calculés sur la carte) et la mémoire du
  lot reconstruit à la fin de l'apprentissage.
- Le déterminisme de l'attention de 300 époques sur la carte dans la marche.
- Les amorces et lanceurs v3 n'ont jamais tourné sur une machine : ils ne diffèrent des v2 que par les lignes déclarées.
- De vraies activations : rien n'est mesuré dessus (interdit ici).

## 7. Pour la mère

- **La course doit passer par `scripts/lancer_bbis_v3.sh`** (amorce v3, `marche_v3`, minimum 115) ; la fiche de `CODE-BBIS` cite
  `fichiers-fiche-code-bbis-v3.txt` (103 chemins) ; la lecture se fait par `lecture_v2`.
- **Quatrième passe sur carte** (si la mère la commande, sous sa ligne de dépense) : `scripts/lancer_repetition_bbis_v3.sh`,
  branche de sortie `calcul/t07bbis-repetition-v4` (absente à distance, revérifiée par la garde du lanceur), traces sous
  `traces/bbis-t07-repetition-v4/`, étiquette `bbis-t07-repetition-v4`. Lecture **écrite avant la passe** (texte, couple c4 ;
  script) : code 9 = la passe ne compte pas ; code 0 avec « la course part sans nœud » ou « nœud écrit à la mère avant la
  course » ; essais de l'arbre de l'instance au moins 115.

## 8. Empreintes

| fichier | sha256 |
|---|---|
| `brouillons/T0.7-etape-B-bis-v1/T0.7-etape-B-bis-v1-brouillon6.md` | `bf1be58e4be262b180e5ea952cafd7948942ff450614c901e97318500d874935` |
| `brouillons/T0.7-etape-B-bis-v1/pieces/couples-brouillon6-v1.py` | `b61ed1d32d5fef1b821eac4d6effe3b8d136f7498e126c5ef796fb05c0e03a57` |
| `src/controle_ia/t07bbis/validation_imbriquee_v3.py` | `71bffa5bf26c2b182bb81ebfb920c1246b6c9784b2332ff1304f0ff3c24890eb` |
| `src/controle_ia/t07bbis/marche_v3.py` | `7009b34d46c33ed8fa4a5045d4ad93816c0948fd6dc165cb8f74e493b98f03f5` |
| `src/controle_ia/t07bbis/lecture_v2.py` | `154795f4ecfa3273a7a5cec91c6975cd34e558d14647bb8a1cb1ef4968972aca` |
| `scripts/amorce_bbis_v3.sh` | `18e2f2052efdca0d9d447738c3c4f1099302f7134b9518b59eea78ba563695dd` |
| `scripts/lancer_bbis_v3.sh` | `dc26ea01a06bfb9eac3fc4f9f1b9b3bb86490d61d9e8f5deb54bcb180b17ee68` |
| `scripts/repetition_carte_bbis_v3.py` | `355b313319d01f8a3f77cdd7603fd43b75ae1599bc079e03d9f93cf24f07e289` |
| `scripts/amorce_repetition_bbis_v3.sh` | `cb489ebec9206afe2105512b2cda33f5265bbd8e4eb080a6521dc01d11348f48` |
| `scripts/lancer_repetition_bbis_v3.sh` | `5bd32c146e0798b51a0a58753687fef75e0207b37a2e5949b0bddc39c80a758b` |
| `conftest.py` | `8fe7cc46c35c13daf8dd87b34102522211024b8e9a2941ad9daeb8d3f8f44427` |
| `tests/aide_t07bbis_differentiels_v3.py` | `b2899511f82b5fc081120ca6d6f999bff5f8fac787522be15f6f96ab95cee714` |
| `tests/test_t07bbis_controle_v3.py` | `ecdeb07dd69203fbce9c92be9878f55be8a76179dcf47175746d3848448ca93b` |
| `tests/test_repetition_bbis_v3.py` | `6b17a89e4dcdf1d92a6cd1cab4532585ccf04b4abe0a674c3f2644b5ac13f3bc` |
| `tests/test_essais_git_propres_bbis_v1.py` | `e87f1bb983489dfb7316a68b46a9288f698df578b6dfe6a4d30c27b199e5962e` |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt` | `b8fb095bf44dc855868e1b48cef6005222af6888b00a9df2f60fccc36ded7d5d` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-controle-attention-v2.txt` | `fd9282debeb5f4e75349d8309ae53e1dd55546fc62ada6dcaee4395ca45c03ad` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-contre-epreuve-garde-git-v1.txt` | `84bed52f7b986112a2863785300c04bc17ae6c2c2a2932f1d28897c44567a47c` |
| `brouillons/T0.7-etape-B-bis-v1/code/etat-corrections-v3-en-cours-v1.md` | `56f90935e987b01600ecde887f0c2a8823e25924db6907f13e04d302406cdfc7` |
| `brouillons/T0.7-etape-B-bis-v1/code/garde-git-restreinte-v1/conftest-restreint-v1.py` | `0e2b137e4479c534547ea791dd268dc33a6ce4499d624e92130d34b831b85441` |
| `brouillons/T0.7-etape-B-bis-v1/code/garde-git-restreinte-v1/essai-garde-restreinte-v1.py` | `d527ed3a9e654e64a86c0d80011ff3788fefd2c8bfaf5e3486e97e24aa3ea94d` |
| `brouillons/T0.7-etape-B-bis-v1/code/garde-git-restreinte-v1/differentiel-garde-restreinte-v1.diff` | `a509a76f427417865f253ca9cf3e9a650fbfa5563318037819fd01bca125813c` |

Chaque fichier scellé a son compagnon `.sha256` ; ce rapport : `corrections-controle-attention-v2.md.sha256`.

