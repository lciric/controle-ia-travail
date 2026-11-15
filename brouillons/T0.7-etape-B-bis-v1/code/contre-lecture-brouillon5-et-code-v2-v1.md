# Contre-lecture du brouillon 5 du texte de B bis (différentiel 3 → 5) et du code v2 du contrôle carte-processeur, v1

**Verdict : scellable après corrections.** Le différentiel du texte est exact (sept couples, trois retouches de forme, rien
d'autre) ; le code v2 fait ce que le texte écrit, tire le même couple et les mêmes actions que la v1, et **le contrôle à 3 époques
attrape bien les erreurs de chaîne de la famille « attention »** (30 artefacts sur 35 attrapés, dont toutes les erreurs de
structure, avec un à cinq ordres de grandeur de marge ; les cinq restants sont sous la tolérance par nature ou hors de portée par
construction). Deux majeurs, tous deux **avant le scellement du texte et la fiche `CODE-BBIS`**, aucun n'interdit la passe de
répétition : la réserve R-PILE et le point (7) de la section D sont écrits au texte mais **aucun code ne les écrit** (M1) ; le
cas « sans objet, sans arrêt » du contrôle **n'est pas dans le texte**, qui ne connaît que « ≤ 10⁻⁴ » ou « arrêt » (M2).
**La passe payante de répétition peut partir avec le code tel qu'il est**, sous trois consignes de lecture (m1, m2, m3).

**Incident de ma main, réparé, à connaître** (détail au § 7) : en voulant rejouer un essai sauté, j'ai lancé une fois `pytest`
avec la variable `GIT_DIR` pointée sur le dépôt principal ; un essai, qui fabrique un dépôt jouet, a alors écrit **dans le dépôt
principal** : un commit « piece » (`4f04ab90`) sur la branche `main` locale, l'index remplacé, et `user.name` / `user.email`
locaux posés à « essai ». Rien n'a été poussé (`origin/main` est resté à `71df43ad`), aucun fichier de l'arbre de travail n'a été
touché. Réparé dans la minute : branche ramenée à `71df43ad` par `git update-ref` à valeur attendue, index relu de ce commit,
deux réglages locaux retirés ; état vérifié égal à celui du début (`git status` : la seule ligne d'avant ; index = tête ; tête =
`origin/main`). Reste : le commit orphelin `4f04ab90` (objets non atteignables) et deux lignes au journal des références.

**Déclaration** : contre-lecteur neuf, aucun fichier de l'étape B bis écrit par moi ; processeur seulement ; aucune machine,
aucun appel payant, aucune dépense ; rien lu ni écrit sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune entrée de 7a ou 7b ;
aucune valeur de clé lue ; appels réseau : un `git fetch` de la branche, trois `git ls-remote` en lecture. Aucun commit voulu,
aucune poussée ; seul fichier écrit dans la copie du développeur : ce rapport et son compagnon. Données synthétiques seulement.

- **Date (UTC)** : 2026-11-15.
- **Objet** : commit `833d01c9` de `prep/t07bbis-code-v1` (égal à `origin/prep/t07bbis-code-v1` après récupération), lu par
  `git show` et par une extraction `git archive` dans un dossier neuf du bloc-notes, supprimée à la fin ; aucune copie entière.
- **Pile des essais** : python 3.13.18, torch 2.14.1+cu130, numpy 2.4.6, processeur seul.
- **Pièces vérifiées par leur compagnon** (empreinte recalculée = compagnon) : brouillon 3 `f104917f8e858d40…`, brouillon 4
  `af612cbc02a9dd57…`, brouillon 5 `99d88954369f0d3a…` ; `pieces/couples-brouillon4-v1.py` `51135f43e1d921fa…`,
  `pieces/couples-brouillon5-v1.py` `8608d87c77f63807…` ; `code/corrections-controle-attention-v1.md` `45aeddba99a7a710…` ;
  `code/fichiers-fiche-code-bbis-v2.txt` `0ece847b11331100…` ; `code/diagnostic-ecart-attention-carte-v1.md`
  `5ecb923525617e0a…` ; `code/diagnostic-stabilite-aires-attention-v1.md` `dd67802d181e4a36…`.
- **Code lu** (empreintes au commit, égales au tableau du § 6 du rapport du développeur) :
  `src/controle_ia/t07bbis/validation_imbriquee_v2.py` `1e3fa4bc50d0026d…`, `marche_v2.py` `77a09bc0dfd8be67…`,
  `scripts/amorce_bbis_v2.sh` `1f9f6a624805db0b…`, `scripts/lancer_bbis_v2.sh` `d18d7a8546c9eee6…`,
  `scripts/repetition_carte_bbis_v2.py` `1b5289f0ffefbdef…`, `scripts/amorce_repetition_bbis_v2.sh` `a9209b33d8a4be74…`,
  `scripts/lancer_repetition_bbis_v2.sh` `b5a93e63c207b0d3…`, `tests/test_t07bbis_controle_v2.py` `2a2e3d03ba7ad6d4…`,
  `tests/test_repetition_bbis_v2.py` `ef2b9e58358ea501…`.

## Majeurs

**M1 — La réserve R-PILE (couple b1) et le point (7) de la section D (couple b2) sont au texte, mais aucun code ne les écrit.**
Le brouillon 5, ligne 172, range R-PILE parmi les « qualifications toujours écrites » : « écrite dès qu'une sonde finale lue est
de la famille « attention » » ; ligne 192, la section D reçoit un point (7). Or le seul module qui écrit les réserves et la
section D est `src/controle_ia/t07bbis/lecture_v1.py`, inchangé et présent dans la liste de la fiche
(`fichiers-fiche-code-bbis-v2.txt`) : `RESERVES_FIXES` (lignes 97 à 103) porte R-RF, R-IT, R-REET, R-F-ABSENT ; l'assemblage des
réserves (lignes 1172 à 1182) ajoute R-MU, R-F, R-REET, R-MC, R-G3 et l'audit R4 ; `SECTION_D` (lignes 107 à 112) s'arrête à
« (6) le libellé d'information ne dit pas « plafond tient ». ». La chaîne « R-PILE » n'existe dans aucun fichier de `src/`, de
`scripts/` ni de `tests/` (`grep -rl "R-PILE"` : les deux brouillons, le programme des couples et les pièces du diagnostic
seulement). Le rapport du développeur ne le déclare pas parmi ce qui reste (§ 4 et § 5). Une lecture faite avec la liste v2
rendrait donc une issue **sans** la réserve que le texte dit « toujours écrite » : écart au texte scellé, à la lecture.
La donnée nécessaire existe déjà (`meta["famille"]` de chaque source, `validation_imbriquee_v1.py`, ligne 387,
écrite dans le fichier fermé des sondes) : la règle est codable sans rien changer à la marche.
- ancien : `lecture_v1` (six points en section D, pas de R-PILE) dans la liste de la fiche ;
- nouveau : `lecture_v2` sous nom neuf (R12) = `lecture_v1` + (a) R-PILE, phrase du texte recopiée, ajoutée dès qu'une sonde
  finale lue a `famille == "attention"` ; (b) point (7) ajouté à `SECTION_D`, mot pour mot ; (c) essais : cas sain (aucune sonde
  « attention » lue : pas de R-PILE) et cas déclenché ; liste de la fiche en v3 ; le texte (« Code neuf », ligne 244) nomme
  `lecture_v1` : couple de texte « `lecture_v1` » → « `lecture_v2` (… ; la v1 reste, R12) » dans le même brouillon 6.
Sans effet sur la passe de répétition (la lecture n'y est pas jouée). À faire avant `SCELLEMENT-BBIS` et `CODE-BBIS`.

**M2 — « Sonde de contrôle en échec : sans objet, sans arrêt » n'est pas conforme à la lettre du texte, qui ne connaît que deux
issues.** Texte, ligne 122 : « écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴ pour chacune, sinon arrêt (erreur
de chaîne) ; la sonde « attention » de 300 époques du couple est réapprise une seconde fois sur la carte et doit être égale à la
première au bit près (déterminisme), sinon arrêt » ; liste d'arrêt, ligne 203, de même. Les mots « sans objet », « en échec » et
« perte non finie » n'apparaissent nulle part dans le brouillon 5. Le code ouvre pourtant trois sorties sans arrêt :
`validation_imbriquee_v2.py`, lignes 79 à 81 (sonde de contrôle en échec : `sortie[f] = {"sans_objet": …}` puis `continue`, ce
qui saute aussi, pour l'attention, le contrôle de déterminisme, sans même une ligne « sans objet » pour lui) ; lignes 93 à 95
(sonde de 300 époques en échec au déterminisme) ; lignes 110 à 112 (sonde finale du couple tiré en échec : tout le contrôle est
« sans objet » ; hérité de la v1, lignes 416 à 418). Dans ces cas `marche_v2.py` (lignes 381 à 385) écrit les scores et le
fichier fermé avec `controle_carte_processeur` = « sans objet » : **la course s'achève sans qu'aucun contrôle carte-processeur
ait été joué**, puisqu'un seul couple est tiré ; et `lecture_v1` ne lit pas ce champ (aucune occurrence de
`controle_carte_processeur` dans le module) : aucune réserve n'en sortirait. C'est un repli que le texte n'écrit pas (R5).
Circonstance aggravante pour les sondes propres au contrôle : depuis w = 0 et b = 0, la perte de la première époque vaut log 2
quelles que soient les données finies, et trois pas d'Adam de 0,05 bornent chaque poids à 0,15 ; une perte non finie de
l'attention à 3 époques **ne peut venir que d'activations non finies**, c'est-à-dire d'une anomalie de chaîne, précisément ce
que le contrôle doit arrêter.
- ancien (texte, ligne 122) : « … ≤ 10⁻⁴ pour chacune, sinon arrêt (erreur de chaîne) ; la sonde « attention » de 300 époques du
  couple est réapprise une seconde fois sur la carte et doit être égale à la première au bit près (déterminisme), sinon arrêt. » ;
- nouveau, deux voies, à trancher par la mère :
  (a) **texte seul, code de la marche inchangé** (la passe de répétition garde tout son sens) : ajouter après « sinon arrêt. » :
  « Si la sonde finale du couple tiré, ou une sonde apprise pour le contrôle, est en échec (perte ou paramètres non finis), le
  contrôle de la famille touchée est « sans objet », motif écrit dans le fichier fermé des sondes, sans arrêt ; la lecture écrit
  alors la réserve **R-CTRL** (« contrôle carte-processeur non joué pour [famille] : [motif] ») » ; même mention en liste
  d'arrêt ; `lecture_v2` (M1) lit `controle_carte_processeur` et écrit R-CTRL ; essai : cas sain, cas « sans objet » ;
  (b) **arrêt** : une sonde de contrôle en échec arrête (« erreur de chaîne »), et un couple tiré dont la sonde finale est en
  échec est remplacé par le suivant dans l'ordre trié des couples ; cela demande `validation_imbriquee_v3` et, par les noms, une
  marche, une amorce et un lanceur neufs : plus lourd, et la passe de répétition devrait alors jouer ce code-là.
  Ma recommandation : (a), confiance moyenne ; elle rend le texte exact sur ce que fait le code, sans toucher au code éprouvé.
À trancher avant `SCELLEMENT-BBIS` ; sans effet sur la passe de répétition, sous la consigne m3.

## Mineurs

**m1 — La répétition ne joue pas le chemin exact de la course pour le déterminisme : lot reconstruit non éprouvé sur carte.**
Dans la course, `validation_imbriquee_v2.py`, ligne 118, reconstruit un lot (`lot = ac.LotCarte(res["sequences_app"],
ctx.appareil)`) et compare la sonde finale, apprise sur le **premier** lot, à une sonde réapprise sur le **second** (lignes 90 à
96). Dans la répétition, `scripts/repetition_carte_bbis_v2.py`, lignes 439 à 441, passe **le même** `lot` et les sondes déjà
apprises dessus. La passe payante ne prouvera donc ni que deux constructions du lot sur la carte rendent les mêmes jetons
réduits au bit près (moyenne et écart type calculés sur la carte, `apprentissage_carte_v1.py`, lignes 61 à 64), ni la mémoire du
second lot (4,7 Go de plus, selon le rapport du développeur, qui déclare ce point non éprouvé, § 4). Sur processeur, je l'ai
vérifié : égalité au bit près dans les six cas jouet où le contrôle passe par ce chemin (§ 4). Si cela ne tenait pas sur la
carte, la course s'arrêterait sur « non déterministe » sans erreur réelle, et le seul remplacement de `CODE-BBIS` serait
consommé. Je le juge peu probable (réductions déterministes exigées par `exiger_deterministe`), mais c'est la seule partie du
contrôle neuf que la passe ne couvre pas.
- ancien (répétition v2, ligne 439) : `c = vi.controle_deux_horizons(lot, seqs, y, COUCHE, l2_c, graine_de, ctrl, …` ;
- nouveau, au choix de la mère : soit une répétition v3 qui passe `ac.LotCarte(seqs, appareil)` (un lot neuf) à la place de
  `lot` (une ligne, mais trois fichiers neufs par les noms) ; soit la réserve écrite avant la passe : « lot reconstruit non
  éprouvé sur carte ; un arrêt « non déterministe » à la course serait d'abord lu comme cela ».

**m2 — `MIN_ESSAIS=87` ne garde pas les onze essais neufs.** `scripts/amorce_bbis_v2.sh`, ligne 42 : `MIN_ESSAIS=87`, inchangé
comme demandé. L'arbre de l'instance rend 99 passés (§ 5) ; sans `tests/test_t07bbis_controle_v2.py` il en rendrait 88, encore
au-dessus de 87 : l'absence ou le saut des essais du contrôle neuf ne déclencherait pas l'arrêt.
- ancien : lecture « au moins 87 » ; nouveau (consigne, sans code) : à la passe de répétition et à la course, la mère lit dans
  `essais.txt` la ligne « 99 passed, 23 skipped » ; un autre compte : nœud avant d'aller plus loin.

**m3 — À la répétition, un contrôle « sans objet » rendrait le code 0 et un résumé muet.** `repetition_carte_bbis_v2.py`,
lignes 445 à 447, recopie `c[f]` tel quel ; `amorce_repetition_bbis_v2.sh`, ligne 219, lit
`x.get("ecart_relatif_max", x.get("refus"))`, soit `None` pour une famille « sans objet », et l'absence de la clé
`determinisme_attention` ne laisse aucune trace au résumé.
- ancien : passe jugée sur le code 0 ; nouveau (consigne, sans code) : la passe ne compte que si `repetition-carte.json` porte un
  nombre pour `lineaire.ecart_relatif_max` (300 époques) et pour `attention.ecart_relatif_max` (3 époques), tous deux ≤ 10⁻⁴, et
  `determinisme_attention.egal_au_bit` vrai, en plus de `deterministe` vrai pour les deux familles.

**m4 — L'essai « même tirage que la v1 » ne compare que le nombre d'actions.** `tests/test_t07bbis_controle_v2.py`, ligne 213 :
`assert r1["actions"] == r["actions"] and …` (10 = 10) ; le commentaire dit « la v1 tire les mêmes actions de contrôle ». Le
code est bien le même (v2, lignes 114 à 116, mot pour mot les lignes 420 à 422 de la v1 ; même générateur `bbis/egalite-carte`
créé par le constructeur hérité), et je l'ai vérifié par instrumentation (§ 4) ; l'essai ne le prouve pas.
- ancien : `assert r1["actions"] == r["actions"]` ; nouveau (à la prochaine version des essais) : comparer les listes d'actions
  passées à `_sequences` par les deux contrôles.

**m5 — Le texte dit « dans les deux familles » sans dire ce que devient le contrôle sous la variante (r1).** Ligne 122 ; la
variante (r1), « famille linéaire seule », est écrite plus bas dans le même point. Le code joue alors la linéaire seule
(`validation_imbriquee_v2.py`, lignes 64 et 124 ; essai `test_variante_r1_horizon_et_sonde_de_controle_en_echec`) : choix
raisonnable, non écrit.
- ancien : « **dans les deux familles** : la linéaire à 300 époques, l'attention à **3 époques** » ;
- nouveau : « **dans les deux familles** (sous la variante (r1) : la linéaire seule) : la linéaire à 300 époques, l'attention à
  **3 époques** ».

**m6 — « Quatre piles de calcul » : toutes sur processeur, aucune carte.** Ligne 172 (R-PILE) : « entre quatre piles de calcul » ;
le rapport cité (`diagnostic-stabilite-aires-attention-v1.md`, § 1) les nomme : paquet gelé en AVX-512, paquet gelé en AVX2,
chemin v1 à réduction torch, calcul en colonne d'un produit matriciel, tous sur le processeur. De même, ligne 122, « l'écart
entre deux piles reste de 2,9·10⁻⁷ à 5,9·10⁻⁷ » est mesuré entre piles du processeur (premier diagnostic, § 5). La réserve
parle justement de la carte : le lecteur doit savoir qu'elle n'est pas dans la mesure.
- ancien : « entre quatre piles de calcul, aires d'une sonde » ; nouveau : « entre quatre piles de calcul du processeur (aucune
  carte), aires d'une sonde » ;
- ancien : « à 3 époques, l'écart entre deux piles reste de » ; nouveau : « à 3 époques, l'écart entre deux piles du processeur
  reste de ».

**m7 — Second rapport cité sans empreinte dans le corps (R6).** Ligne 122 : « `…/diagnostic-stabilite-aires-attention-v1.md`). »
et ligne 172 de même, sans empreinte, quand le premier rapport porte `5ecb9235…`. L'empreinte entière est dans le tableau
d'en-tête (ligne 9) ; suffisant si ce tableau reste au texte scellé, sinon :
- ancien : « `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`). » ; nouveau : « …`-v1.md`,
  `dd67802d…`). ».

**m8 — Aucune borne écrite d'avance pour lire l'écart à 3 époques de la passe de répétition.** Le rapport du développeur (§ 4,
§ 5) attend « de l'ordre de 10⁻⁷ » et dit l'écart sur carte « inconnu ». Mes mesures (§ 3) montrent que, sans signal, trois
époques amplifient déjà beaucoup une petite différence d'entrée (un jeton retiré d'une seule action sur 640 : écart 2,4). La
marge de la course se lira donc sur la passe : un écart de 5·10⁻⁵ « passerait » sans laisser de marge pour de vraies
activations.
- nouveau (consigne, dans l'esprit de R1) : écrire avant la passe la borne au-delà de laquelle la course n'est pas tirée sans
  nœud ; proposition : écart de l'attention à 3 époques sur la carte ≤ 10⁻⁵ (un ordre de marge sous le seuil du texte).

**m9 — Trois suffixes pour une même passe (observation).** `amorce_repetition_bbis_v2.sh` : fichier en v2, branche de sortie
`calcul/t07bbis-repetition-v3` (ligne 38), dossier des traces `traces/bbis-t07-repetition-v2` (ligne 33), dossier de travail de
l'instance `bbis-t07-repetition-v1` (même ligne). Déclaré, cohérent avec R12 ; à nommer tel quel dans la passation pour que la
trace se retrouve.

## 1. Le texte : différentiel exact 3 → 5

- **Programmes rejoués** sur une copie du dossier du brouillon privée des brouillons 4 et 5 :
  `couples-brouillon4-v1.py` rend le corps `a7a0315b…` puis le brouillon 4 `af612cbc02a9dd57…` ; `couples-brouillon5-v1.py`
  rend « noms v1 de la course encore cités au brouillon 4 : lancer_bbis_v1 », « lignes changées : 3 ; lignes ajoutées
  (tableau) : 6 », brouillon 5 `99d88954369f0d3a…` ; les deux fichiers refaits sont égaux octet pour octet à ceux du commit.
- **Différentiel par lignes** (`diff` du brouillon 3 au brouillon 5) : sept zones et pas une de plus — ligne 1 → lignes 1 à 18
  (titre « brouillon 5 », deux tableaux de différentiel) ; 22 → 39 (statut, ajout seul) ; 105 → 122 (a1) ; 155 → 172 (b1) ;
  175 → 192 (b2) ; 186 → 203 (a2) ; 227 et 228 → 244 et 245 (a3 et a5 sur la première, a4 sur la seconde). 293 lignes au
  brouillon 3, 310 au brouillon 5 : 17 lignes ajoutées, toutes en tête.
- **Différentiel par mots** dans ces lignes : chaque retrait et chaque ajout appartient à un couple ; retraits : « `sondes.familles` »
  (repris avec sa suite), « 10⁻⁴, » (→ « 10⁻⁴ pour chacune, »), « chaîne). » (→ « chaîne) ; la sonde… »), « ». » (→ « » ; (7)… »),
  « `validation_imbriquee_v1` », « débit) », « `scripts/lancer_bbis_v1.sh` ». Rien d'autre.
- **Reste du texte inchangé** : la grille de 18 réglages, les 300 époques et le pas 0,05, la règle d'ex aequo, la garde de
  débit (11 h, facteur 1,2, 0,6 h), les planchers (800), le nul (100), les états et issues, les seuils, les autres lignes de la
  liste d'arrêt, le calendrier et la dépense : égaux ligne à ligne au brouillon 3.
- **Chiffres des couples, retrouvés dans les rapports cités** : 0,633 et 2,131·10⁻² (premier diagnostic, lignes 23, 39, 65, 67) ;
  2,9·10⁻⁷ et 5,9·10⁻⁷ à trois pas (§ 5, tableau) ; 4,0·10⁻² au signal faible, 1,9·10⁻⁵ au plus avec signal, étendues 0,0074 et
  7,8·10⁻⁵, aires 0,46 et 0,558 à 0,983 (second rapport, lignes 13 à 21 et tableau du § 3).
- **Écrit, exclusif, codable ?** Le contrôle aux deux horizons : oui pour les deux issues écrites (seuil unique, familles et
  horizons nommés, graines « celles de la marche », 256 actions) ; **non exclusif** pour le cas où une sonde manque (M2) ; la
  variante (r1) n'est pas dite (m5). Le déterminisme : oui (« égale à la première au bit près », sinon arrêt). R-PILE : règle de
  déclenchement nette (« dès qu'une sonde finale lue est de la famille « attention » »), phrase fixée, donc codable ; non codée
  (M1).

## 2. Le code : chaque v2 = v1 + différentiel déclaré

- **Égalité au différentiel** : les six essais `test_v2_egale_a_la_v1_plus_le_differentiel_declare` (trois fichiers de la
  course, trois de la répétition) refont la v2 depuis la v1 par les couples déclarés et passent ; j'ai relu les six `diff` : ils
  ne portent que des noms (`_v1` → `_v2`), les en-têtes, les deux motifs d'extraction ajoutés, la branche de sortie et le dossier
  des traces de la répétition, et le bloc du contrôle de la répétition.
- **Blocs marqués** (`# >>> … # <<<`) comparés par programme : amorce de la course 7 blocs, lanceur de la course 1, lanceur de
  la répétition 1 : identiques à la v1 ; amorce de la répétition 11 blocs, dont 3 changés par les seuls noms (`amorce_bbis_v2.sh`
  trois fois, `repetition_carte_bbis_v2.py` deux fois). Les blocs `cuda-du-pilote`, `carte-et-cuda` et `branche-de-sortie` sont
  inchangés.
- **`validation_imbriquee_v2`** : importe la v1 sans la modifier ; `ControleCarte` hérite du constructeur (même tirage du
  couple) ; `apres` reprend mot pour mot le tirage des actions ; `controle_deux_horizons` : linéaire à `ctx.epoques` (300 en
  marche réelle), attention à `EPOQUES_CONTROLE_ATTENTION = 3`, tolérance `TOLERANCE_CARTE = 1e-4` de `commun_v1` pour les deux ;
  l'horizon de l'attention est refusé hors de [1, époques[ ; déterminisme par `egales_au_bit` (w, b, q) ; graines par la clé de
  la sonde finale, `bbis/entrainement/sonde/<cellule>/e<k>/<réglage>`, où `reglage_nom` est la fonction qui nomme la grille :
  la sonde finale et sa seconde copie partent bien de la même graine.
- **Ce que la chaîne des trois contrôles établit** : (i) la sonde « attention » finale du couple est égale au bit près à un
  second apprentissage de 300 époques par le même code, sur un lot reconstruit ; (ii) ce code, sur ses trois premières époques,
  rend les scores du paquet gelé à 10⁻⁴ près ; (iii) la boucle d'apprentissage (`apprentissage_carte_v1.py`, lignes 106 à 115) ne
  porte aucune branche qui dépende du numéro de l'époque, hors l'examen de la perte à la première et à la dernière ; (iv) la
  linéaire, qui partage cette boucle, est comparée à 300 époques. Ce qui n'est comparé par rien : les époques 4 à 300 de la
  branche propre à l'attention (logits, softmax par action, gradient de la requête) contre le paquet gelé ; c'est la limite
  assumée de l'option 1, et le texte la porte par R-PILE.

## 3. La question de fond : le contrôle à 3 époques attrape-t-il une vraie erreur de chaîne ?

**Méthode.** Jeu synthétique de la forme de celui de la répétition (640 actions, 150 à 297 jetons par action, soit environ
143 000 jetons ; largeur 1 024 au lieu de 4 096 pour tenir en mémoire sur ce poste ; 256 actions de contrôle ; l2 = 10⁻³ ;
positifs décalés sur le premier quart de leurs jetons), en deux régimes : décalage 0,5 (celui de la répétition, « sans signal »)
et décalage 4 (« avec signal »). Référence : `sondes.familles.entrainer` (paquet gelé), `Reglages(epoques=3)`. Côté « carte » :
`apprentissage_carte_v1.entrainer` sur le processeur, ou une copie paramétrable de sa boucle dont j'ai vérifié qu'elle rend la
même sonde **au bit près** quand rien n'est altéré. Mesure : `apprentissage_carte_v1.ecart_relatif` sur les scores des 256
actions, celle du contrôle. Programme en annexe ; 35 artefacts et le cas sain, dans les deux régimes.

| artefact | écart, sans signal (décalage 0,5) | écart, avec signal (décalage 4) | attrapé par 10⁻⁴ |
|---|---|---|---|
| 0. cas sain (carte sur processeur contre paquet gelé) | 5,8·10^-9 | 2,9·10^-10 | non |
| 1. mauvaise couche à l'apprentissage (corrélation 0.9 avec la bonne) | 5,8·10^0 | 5,3·10^-1 | oui |
| 1. mauvaise couche à l'apprentissage (corrélation 0.99 avec la bonne) | 4,0·10^0 | 3,0·10^-1 | oui |
| 1. mauvaise couche à l'apprentissage (corrélation 0.999 avec la bonne) | 3,7·10^0 | 1,4·10^-1 | oui |
| 1b. mauvaise couche à la notation seulement (corrélation 0,9) | 3,8·10^0 | 6,9·10^-1 | oui |
| 2a. masque : premier jeton de chaque action retiré | 3,5·10^0 | 3,2·10^-1 | oui |
| 2b. masque : dernier jeton de chaque action retiré | 2,9·10^0 | 1,7·10^-1 | oui |
| 2c. masque : un jeton retiré dans une seule action sur toutes | 2,4·10^0 | 1,9·10^-3 | oui |
| 2d. masque décalé d'un jeton (empan glissé sur l'action suivante) | 3,2·10^0 | 2,3·10^-1 | oui |
| 2e. masque à la notation : premier jeton des actions de contrôle retiré | 2,8·10^0 | 2,0·10^-1 | oui |
| 3a. poids w × 1.01 | 1,1·10^-2 | 2,1·10^-2 | oui |
| 3a. poids w × 1.001 | 1,1·10^-3 | 2,1·10^-3 | oui |
| 3a. poids w × 1.0001 | 1,1·10^-4 | 2,1·10^-4 | oui |
| 3b. requête q × 1,01 | 5,4·10^-2 | 2,4·10^-2 | oui |
| 3c. requête q × 1,001 | 5,3·10^-3 | 2,4·10^-3 | oui |
| 3d. une seule coordonnée de w × 1,01 | 1,1·10^-3 | 2,6·10^-4 | oui |
| 3e. biais b + 10⁻³ | 1,0·10^-3 | 1,0·10^-3 | oui |
| 3f. biais b + 10⁻⁵ | 1,0·10^-5 | 1,0·10^-5 | non |
| 3g. requête q remplacée par zéro (attention uniforme = moyenne) | 1,6·10^0 | 2,0·10^0 | oui |
| 4a. étiquettes permutées contre les actions (ordre faux) | 4,7·10^0 | 5,4·10^0 | oui |
| 4b. deux étiquettes échangées (un positif, un négatif) | 4,1·10^0 | 4,1·10^-1 | oui |
| 4c. actions et étiquettes permutées ensemble (même jeu : pas une erreur) | 2,1·10^-9 | 2,2·10^-10 | non |
| 4d. actions de contrôle notées dans un autre ordre | 1,3·10^1 | 1,0·10^1 | oui |
| 5a. autre graine du départ de la requête | 6,5·10^0 | 8,9·10^-1 | oui |
| 5b. régularisation l2 × 10 | 2,3·10^0 | 3,5·10^-1 | oui |
| 5c. régularisation l2 nulle | 5,6·10^-1 | 4,6·10^-2 | oui |
| 5d. pas 0,0501 au lieu de 0,05 | 1,8·10^-2 | 2,9·10^-3 | oui |
| 5e. Adam bêta2 0,99 au lieu de 0,999 | 2,0·10^-2 | 5,2·10^-3 | oui |
| 5f. Adam epsilon 10⁻⁶ au lieu de 10⁻⁸ | 1,1·10^0 | 7,2·10^-3 | oui |
| 5g. départ de la requête 0,011·N au lieu de 0,01·N | 2,0·10^0 | 1,9·10^-1 | oui |
| 5h. température de l'attention 1,01 | 2,2·10^0 | 1,2·10^-1 | oui |
| 5i. agrégation par le maximum à l'apprentissage (mauvaise famille) | 1,2·10^0 | 1,0·10^0 | oui |
| 5j. jetons réduits passés en simple précision | 7,8·10^-7 | 3,4·10^-8 | non |
| 5k. quatre époques au lieu de trois | 8,7·10^0 | 3,9·10^0 | oui |
| 5l. écart type à n − 1 degrés de liberté | 4,1·10^-5 | 5,2·10^-6 | non |
| 6. pas divisé par deux à partir de la quatrième époque (invisible à 3) | 5,8·10^-9 | 2,9·10^-10 | non |

Scores de référence, sans signal : de -3,80 à 13,20, écart type 1,60, médiane des valeurs absolues 1,32 ; durée 94 s.
Scores de référence, avec signal : de -0,89 à 10,77, écart type 4,48, médiane des valeurs absolues 3,86 ; durée 201 s.

**Lecture.**
- **Erreurs de structure : toutes attrapées, de loin.** Mauvaise couche (même corrélée à 0,999 avec la bonne : 0,14 à 3,7),
  masque faux (un jeton de trop ou de moins par action : 0,17 à 3,5 ; **un seul jeton retiré dans une seule action sur 640 :
  1,9·10⁻³ à 2,4**), mauvais ordre des actions (étiquettes permutées : 4,7 à 5,4 ; deux étiquettes échangées : 0,41 à 4,1 ;
  actions de contrôle dans un autre ordre : 10 à 13), autre graine (0,89 à 6,5), mauvaise famille d'agrégation (1,0 à 1,2),
  requête ignorée (1,6 à 2,0), une époque de trop (3,9 à 8,7). Marge sur le seuil : d'un à cinq ordres de grandeur.
- **Erreurs de réglage : attrapées aussi**, y compris les fines : l2 décuplée ou nulle, pas 0,0501, bêta2, epsilon d'Adam,
  départ de la requête à 0,011, température 1,01 : de 2,9·10⁻³ à 2,3.
- **Poids altérés** : 1 % sur w : 1,1·10⁻² à 2,1·10⁻² (l'artefact des épreuves du texte) ; 1 ‰ : 10⁻³ ; **1 pour 10 000 :
  1,1·10⁻⁴ à 2,1·10⁻⁴, attrapé de justesse** ; une seule coordonnée de w à 1 % : 2,6·10⁻⁴ à 1,1·10⁻³ ; q à 1 ‰ : 2,4·10⁻³ à
  5,3·10⁻³. Le plancher de détection est donc une altération relative des poids voisine de 10⁻⁴ : c'est le seuil lui-même, et ce
  serait le même à 300 époques.
- **Non attrapés (5), et pourquoi** : biais décalé de 10⁻⁵ (sous la tolérance, par définition) ; actions et étiquettes permutées
  ensemble (ce n'est pas une erreur : même jeu ; 2·10⁻⁹, le plancher d'arrondi) ; jetons réduits arrondis à la simple précision
  (3,4·10⁻⁸ à 7,8·10⁻⁷ : une carte qui calculerait en simple précision l'entrée seule passerait ; différence sans portée pour la
  lecture) ; écart type à n − 1 degrés de liberté (5,2·10⁻⁶ à 4,1·10⁻⁵ : une vraie différence de formule, mais d'effet inférieur
  au seuil) ; **toute erreur qui ne commence qu'après la troisième époque** (pas divisé par deux à partir de la quatrième : écart
  égal à celui du cas sain) : aveugle par construction ; rien dans le code ne crée une telle branche (§ 2, point iii), et la
  linéaire à 300 époques la verrait si elle touchait la boucle commune.
- **Cas sain** : 5,8·10⁻⁹ sans signal, 2,9·10⁻¹⁰ avec ; quatre à cinq ordres sous le seuil, sur une même pile.
- **Deux limites de ma mesure** : largeur 1 024 et non 4 096 (les scores grandissent avec la largeur, ce qui joue pour la
  détection, non contre) ; côté « carte » joué sur le processeur : je mesure le pouvoir du contrôle, non l'écart d'arrondi entre
  une vraie carte et le processeur, que seule la passe payante donnera (m8).
- **Remarque sur la cible** : dans la course, la carte et le processeur reçoivent les mêmes séquences (`res["sequences_app"]`) ;
  une mauvaise couche ou un masque faux en amont toucherait les deux côtés de la même façon, à 3 époques comme à 300, en v2
  comme en v1. Le contrôle carte-processeur garde l'apprentissage, non la relecture ; celle-ci a ses propres gardes (garde
  d'équivalence, chemin de l'état imposé). Les artefacts 1 et 2 montrent ce que le contrôle verrait si une telle erreur se
  glissait d'un seul côté.

**Réponse.** Oui : à 3 époques le contrôle garde tout son pouvoir contre les erreurs de chaîne (données, masque, ordre, graine,
formule, réglages), avec une sensibilité égale ou supérieure à celle qu'on attendrait d'un horizon long, parce qu'Adam fait dès
le premier pas des déplacements d'ordre 0,05 par coordonnée et que les scores valent déjà plusieurs unités. Ce qu'il ne voit pas
est soit sous la tolérance, soit postérieur à la troisième époque ; ce second cas est couvert par l'identité du code de la
boucle, par la linéaire à 300 époques et par le déterminisme, non par une comparaison directe : limite à garder écrite (R-PILE).

## 4. Même couple, mêmes actions, déterminisme, variante (r1) — vérifications par programme

Sur le jouet des essais (`ActsJouet`), neuf cas (trois graines × familles {linéaire et attention ; attention seule ; linéaire
seule}), en espionnant la liste d'actions passée à `_sequences` par chaque contrôle :
- couple tiré : égal entre v1 et v2 dans les neuf cas ; **liste des actions de contrôle : égale élément par élément** dans les
  neuf cas ;
- deux familles : linéaire à l'horizon de la marche (10 époques sur le jouet), attention à 3, écarts ≤ 1,4·10⁻¹² ; déterminisme
  de l'attention vrai, **la sonde finale (premier lot) contre la sonde réapprise sur le lot reconstruit** (réglage retenu
  « attention » dans les six cas concernés) ;
- variante (r1) (famille linéaire seule) : le contrôle ne joue que la linéaire, écart égal à celui de la v1 au bit près
  (1,1·10⁻¹⁶, 1,7·10⁻¹⁶, 7,8·10⁻¹⁶), aucune clé « attention » ni « déterminisme ».
- « Sans objet » : comportement décrit en M2 ; conforme à l'en-tête du module, non au texte.

## 5. Amorces, lanceurs, essais

- **Branches de sortie** (`git ls-remote --exit-code origin refs/heads/…`, code 2 = absente) :
  `calcul/t07bbis-repetition-v3` (répétition v2) : **absente** ; `donnees/t07-etape-b-bis-v1` (course, inchangée) : **absente** ;
  présentes : `calcul/t07bbis-repetition-v1` et `-v2` (passes précédentes), comme l'écrit l'amorce.
- **`MIN_ESSAIS=87`** : inchangé (ligne 42 de `amorce_bbis_v2.sh`) ; lu par l'amorce de la répétition v2 : j'ai joué hors ligne
  ses deux fonctions `motifs_de_la_course` et `lire_course` sur le texte de `amorce_bbis_v2.sh` : 23 motifs (dont les deux
  neufs), `MIN_COURSE=87`, compte lu « 99 » sur la ligne « 99 passed, 23 skipped ». Voir m2.
- **Garde CUDA** (`cuda_du_pilote`, `exiger_cuda_du_pilote`, avant l'installation) et **contrôle de branche**
  (`branche_de_sortie_neuve` dans les lanceurs ; `ls-remote` dans les amorces ; clonage `--single-branch --branch
  "$BRANCHE_CODE"`, `checkout "$COMMIT"`) : blocs égaux à la v1 (§ 2). Le lanceur de la répétition exige toujours que l'amorce
  et le script du commit soient ceux du poste (`cmp`, empreinte `SCRIPT_SHA256`).
- **Liste de la fiche v2** : 95 chemins = les 90 de la v1 + `scripts/amorce_bbis_v2.sh`, `scripts/lancer_bbis_v2.sh`,
  `marche_v2.py`, `validation_imbriquee_v2.py`, `tests/test_t07bbis_controle_v2.py` ; tous présents au commit et dans l'arbre de
  l'instance simulé. Elle garde `lecture_v1` (M1).
- **Suite B bis** (`tests/test_t07bbis_*.py`, `tests/test_repetition_bbis_v1.py`, `tests/test_repetition_bbis_v2.py`) dans
  l'arbre extrait du commit : **154 passés, 1 sauté, 0 échec** en 224 s ; le sauté est
  `test_fichiers_reels_de_la_branche` (« commit cité absent de ce clone » : une extraction `git archive` n'a pas d'objets git) ;
  rejoué après avoir donné à l'arbre extrait un dossier git propre qui lit les objets du dépôt en lecture seule : le fichier
  `tests/test_t07bbis_lien_mots_et_cout_v1.py` rend 8 passés, 0 sauté. **Total : 155 passés, 0 échec**, le compte du développeur.
- **Arbre de l'instance simulé** (clone partagé sans objets copiés, extraction partielle par les `MOTIFS` de
  `amorce_bbis_v2.sh` lus au commit, commande des essais de la course) : **99 passés, 23 sautés**, 0 échec, en 63 s ; minimum 87.
  Les sautés sont ceux que nomme le développeur (chaîne de T0.6 et pièce « mots et coût » absentes de l'extraction, dont la
  marche v2 de bout en bout).

## 6. Ce que je n'ai pas vérifié

- Rien sur carte : l'écart carte-processeur à 3 époques, le déterminisme à 300 époques sur carte, la mémoire du second lot.
- Les amorces et lanceurs v2 n'ont pas tourné ; je n'ai joué que les fonctions de texte citées au § 5 et lu les différentiels.
- Mes artefacts sont à largeur 1 024 et sur une seule graine de données par régime.
- Je n'ai pas relu les 138 essais d'avant ni le code v1 hors des fonctions appelées par le contrôle.
- Aucune vraie activation (interdit ici).

## 7. Incident : écriture involontaire dans le dépôt principal, réparée

- **Fait** (15:59 UTC) : commande `GIT_DIR=/home/user/controle-ia-travail/.git … pytest tests/test_t07bbis_lien_mots_et_cout_v1.py`
  lancée depuis l'arbre extrait, pour donner à un essai l'accès aux objets git. Cet essai et ses voisins fabriquent un dépôt
  jouet dans un dossier temporaire par `git -C <dossier> init`, `config user.email`, `config user.name`, `add -A`, `commit -m
  piece` ; avec `GIT_DIR` posé, ces commandes ont agi sur le dépôt principal.
- **Effets constatés** : commit `4f04ab905ae02eb38e60c9d042bca3dd405e13a7` (« piece », auteur « essai ») sur `main` locale,
  parent `71df43ad` ; index du dépôt principal remplacé par les fichiers du jouet ; `user.email` et `user.name` locaux posés.
  Rien poussé ; aucun fichier de l'arbre de travail modifié ; les copies de travail annexes non touchées (index propres).
- **Réparation** (16:00 UTC) : `git update-ref refs/heads/main 71df43ad… 4f04ab90…` (échange à valeur attendue) ;
  `git read-tree 71df43ad…` (index relu, arbre de travail intact) ; `git config --local --unset` des deux réglages (l'identité
  vient de nouveau du réglage global, celle des commits précédents).
- **Vérifié après** : `git status --short` rend la seule ligne du début (`?? docs/notes/organisme-idees-juge-v1/correction-poids-v1/`) ;
  index = tête ; arbre = index ; tête = `origin/main` = `71df43ad` ; réglages locaux sans `user.*`.
- **Reste** : les objets du commit orphelin et deux lignes au journal des références de `main` (« commit: piece », puis la
  réparation). Si la session mère a lu l'état du dépôt entre 15:59:36 et 16:00 UTC, elle a pu voir un état faux.
- **Leçon pour la suite** : ne jamais poser `GIT_DIR` vers un dépôt réel pour des essais ; l'essai
  `tests/test_t07bbis_lien_mots_et_cout_v1.py` (lignes 50 à 59) fabrique son dépôt par `git -C`, que `GIT_DIR` détourne.

## Annexe — programme des artefacts (§ 3)

Lancement : `PYTHONPATH=<arbre du commit>/src python artefacts_attention.py 640 1024 <décalage> <sortie.json>` ; décalages 0,5
et 4,0.

```python
"""Contre-lecture : artefacts de chaîne dans la famille « attention », écart carte-processeur à 3 époques (processeur seul,
données synthétiques). Le côté « carte » est une copie paramétrable de `apprentissage_carte_v1.entrainer` (égalité au bit près
vérifiée sans altération) ; la référence est `sondes.familles.entrainer` (paquet gelé), `Reglages(epoques=3)`."""
import json, sys, time
import numpy as np, torch
from controle_ia.sondes import familles as fam
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import validation_imbriquee_v2 as vi2
from controle_ia.t07bbis.commun_v1 import TOLERANCE_CARTE

N, D, NC = int(sys.argv[1]), int(sys.argv[2]), 256
DECALAGE = float(sys.argv[3]); SORTIE = sys.argv[4]
EP = vi2.EPOQUES_CONTROLE_ATTENTION
L2, GRAINE, COUCHE = 1e-3, 20261115, 15

def jeu(n, cle, decalage):
    rng = np.random.default_rng(np.random.SeedSequence(987654321, spawn_key=(cle,)))
    u = np.random.default_rng(np.random.SeedSequence(987654321, spawn_key=(0,))).standard_normal(D).astype(np.float32)
    u /= np.linalg.norm(u)
    y = np.r_[np.ones(n // 2, int), np.zeros(n - n // 2, int)]
    seqs = []
    for k in range(n):
        t = int(rng.integers(150, 298))
        x = rng.standard_normal((t, D), dtype=np.float32)
        if y[k]:
            x[: max(1, t // 4)] += decalage * u
        seqs.append(x)
    return seqs, y

def entrainer_alt(lot, y, graine=GRAINE, l2=L2, pas=0.05, epoques=EP, eps=1e-8, betas=(0.9, 0.999), echelle_q=0.01,
                  temperature=1.0, agregation="attention", pas_apres=None, simple=False):
    X = lot.X.float().double() if simple else lot.X
    torch.manual_seed(int(graine))
    q0 = torch.randn(lot.d, dtype=torch.float64) * echelle_q
    w = torch.nn.Parameter(torch.zeros(lot.d, dtype=torch.float64)); b = torch.nn.Parameter(torch.zeros((), dtype=torch.float64))
    q = torch.nn.Parameter(q0.clone())
    opt = torch.optim.Adam([w, b, q], lr=pas, eps=eps, betas=betas)
    bce = torch.nn.BCEWithLogitsLoss(); cible = torch.as_tensor(np.asarray(y).astype(np.float64))
    for e in range(epoques):
        if pas_apres is not None and e >= pas_apres[0]:
            for g in opt.param_groups: g["lr"] = pas_apres[1]
        opt.zero_grad()
        sj = X @ w + b
        lj = (X @ q) * temperature
        sa = ac._agreger(sj, lj if agregation == "attention" else None, lot.idx, lot.n, agregation)
        perte = bce(sa, cible) + l2 * (w ** 2).sum()
        perte.backward(); opt.step()
    wn, qn = w.detach().numpy(), q.detach().numpy()
    wb = wn / lot.s
    return fam.SondeLineaireJetons("alt", COUCHE, "attention", wb, float(b.detach()) - float(lot.mu @ wb), qn / lot.s, "attention")

def copie(s, w=None, b=None, q=None):
    return fam.SondeLineaireJetons(s.nom, s.couche, s.agregation, s.w if w is None else w, s.b if b is None else b,
                                   s.q if q is None else q, s.famille)

t0 = time.time()
seqs, y = jeu(N, 1, DECALAGE); ctrl, _ = jeu(NC, 2, DECALAGE)
lot = ac.LotCarte(seqs, "cpu")
ref = fam.entrainer("attention", "ref", COUCHE, seqs, y, "attention", GRAINE, fam.Reglages(l2=L2, epoques=EP, pas=0.05))
s_ref = ac.scores(ref, ctrl)
sain = ac.entrainer(lot, "attention", "sain", COUCHE, y, L2, GRAINE, epoques=EP)
alt0 = entrainer_alt(lot, y)
assert vi2.egales_au_bit(sain, alt0), "copie paramétrable différente de apprentissage_carte_v1.entrainer"
res = {"n_actions": N, "largeur": D, "decalage": DECALAGE, "epoques": EP, "seuil": TOLERANCE_CARTE,
       "scores_ref": {"min": float(s_ref.min()), "max": float(s_ref.max()), "ecart_type": float(s_ref.std()),
                      "abs_median": float(np.median(np.abs(s_ref)))}, "artefacts": {}}
def note(nom, sonde, sequences=None, ref_scores=None):
    e = ac.ecart_relatif(ac.scores(sonde, ctrl if sequences is None else sequences), s_ref if ref_scores is None else ref_scores)
    res["artefacts"][nom] = {"ecart": e, "attrape": bool(not e <= TOLERANCE_CARTE)}
    print(f"{nom:70s} {e:.3e} {'ATTRAPÉ' if not e <= TOLERANCE_CARTE else 'non attrapé'}", flush=True)

note("0. cas sain (carte sur processeur contre paquet gelé)", sain)
rng = np.random.default_rng(5)
# 1. mauvaise couche
for rho in (0.9, 0.99, 0.999):
    autres = [(rho * s + np.sqrt(1 - rho ** 2) * rng.standard_normal(s.shape, dtype=np.float32)).astype(np.float32) for s in seqs]
    note(f"1. mauvaise couche à l'apprentissage (corrélation {rho} avec la bonne)", ac.entrainer(ac.LotCarte(autres, "cpu"), "attention", "c", COUCHE, y, L2, GRAINE, epoques=EP))
    del autres
ctrl_autre = [(0.9 * s + np.sqrt(0.19) * rng.standard_normal(s.shape, dtype=np.float32)).astype(np.float32) for s in ctrl]
note("1b. mauvaise couche à la notation seulement (corrélation 0,9)", sain, sequences=ctrl_autre); del ctrl_autre
# 2. masque faux
note("2a. masque : premier jeton de chaque action retiré", ac.entrainer(ac.LotCarte([s[1:] for s in seqs], "cpu"), "attention", "m", COUCHE, y, L2, GRAINE, epoques=EP))
note("2b. masque : dernier jeton de chaque action retiré", ac.entrainer(ac.LotCarte([s[:-1] for s in seqs], "cpu"), "attention", "m", COUCHE, y, L2, GRAINE, epoques=EP))
une = [s[1:] if i == 7 else s for i, s in enumerate(seqs)]
note("2c. masque : un jeton retiré dans une seule action sur toutes", ac.entrainer(ac.LotCarte(une, "cpu"), "attention", "m", COUCHE, y, L2, GRAINE, epoques=EP)); del une
dec = [np.concatenate([s[1:], seqs[(i + 1) % N][:1]]) for i, s in enumerate(seqs)]
note("2d. masque décalé d'un jeton (empan glissé sur l'action suivante)", ac.entrainer(ac.LotCarte(dec, "cpu"), "attention", "m", COUCHE, y, L2, GRAINE, epoques=EP)); del dec
note("2e. masque à la notation : premier jeton des actions de contrôle retiré", sain, sequences=[s[1:] for s in ctrl])
# 3. poids altérés
for f in (1.01, 1.001, 1.0001):
    note(f"3a. poids w × {f}", copie(sain, w=sain.w * f))
note("3b. requête q × 1,01", copie(sain, q=sain.q * 1.01))
note("3c. requête q × 1,001", copie(sain, q=sain.q * 1.001))
w1 = sain.w.copy(); w1[3] *= 1.01
note("3d. une seule coordonnée de w × 1,01", copie(sain, w=w1))
note("3e. biais b + 10⁻³", copie(sain, b=sain.b + 1e-3))
note("3f. biais b + 10⁻⁵", copie(sain, b=sain.b + 1e-5))
note("3g. requête q remplacée par zéro (attention uniforme = moyenne)", copie(sain, q=np.zeros_like(sain.q)))
# 4. ordre des actions
perm = rng.permutation(N)
note("4a. étiquettes permutées contre les actions (ordre faux)", entrainer_alt(lot, y[perm]))
y2 = y.copy(); y2[0], y2[N - 1] = y2[N - 1], y2[0]
note("4b. deux étiquettes échangées (un positif, un négatif)", entrainer_alt(lot, y2))
note("4c. actions et étiquettes permutées ensemble (même jeu : pas une erreur)", ac.entrainer(ac.LotCarte([seqs[i] for i in perm], "cpu"), "attention", "o", COUCHE, y[perm], L2, GRAINE, epoques=EP))
pc = rng.permutation(NC)
note("4d. actions de contrôle notées dans un autre ordre", sain, sequences=[ctrl[i] for i in pc])
# 5. réglages et arithmétique
note("5a. autre graine du départ de la requête", entrainer_alt(lot, y, graine=GRAINE + 1))
note("5b. régularisation l2 × 10", entrainer_alt(lot, y, l2=L2 * 10))
note("5c. régularisation l2 nulle", entrainer_alt(lot, y, l2=0.0))
note("5d. pas 0,0501 au lieu de 0,05", entrainer_alt(lot, y, pas=0.0501))
note("5e. Adam bêta2 0,99 au lieu de 0,999", entrainer_alt(lot, y, betas=(0.9, 0.99)))
note("5f. Adam epsilon 10⁻⁶ au lieu de 10⁻⁸", entrainer_alt(lot, y, eps=1e-6))
note("5g. départ de la requête 0,011·N au lieu de 0,01·N", entrainer_alt(lot, y, echelle_q=0.011))
note("5h. température de l'attention 1,01", entrainer_alt(lot, y, temperature=1.01))
note("5i. agrégation par le maximum à l'apprentissage (mauvaise famille)", entrainer_alt(lot, y, agregation="max"))
note("5j. jetons réduits passés en simple précision", entrainer_alt(lot, y, simple=True))
note("5k. quatre époques au lieu de trois", entrainer_alt(lot, y, epoques=EP + 1))
class LotD1(ac.LotCarte):
    pass
l1 = ac.LotCarte(seqs, "cpu"); n_j = l1.X.shape[0]
l1.X = l1.X * float(np.sqrt((n_j - 1) / n_j)); l1.s = l1.s * float(np.sqrt(n_j / (n_j - 1)))
note("5l. écart type à n − 1 degrés de liberté", ac.entrainer(l1, "attention", "d", COUCHE, y, L2, GRAINE, epoques=EP)); del l1
# 6. erreur qui ne commence qu'après la troisième époque (aveugle par construction)
note("6. pas divisé par deux à partir de la quatrième époque (invisible à 3)", entrainer_alt(lot, y, pas_apres=(3, 0.025)))
res["duree_s"] = time.time() - t0
json.dump(res, open(SORTIE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("durée", round(res["duree_s"]), "s ; scores de référence", res["scores_ref"])
```
