# Relecture indépendante du script de lecture contre le bruit du pilote 4 — rapport v2

Sous-agent neuf, qui n'a écrit ni le script, ni ses essais, ni le texte du pilote, ni le noyau. 26 octobre 2026 ; cette v2
est écrite à 04:40:24 UTC (heure lue sur `date -u` dans la commande même qui écrit ce fichier). Elle remplace la v1
(`rapport-relecture-script-lecture-v1.md`, `a9a4d70c929a59b97e615c71f139c9e7b6e842478ba8df5760ac9c7f4926c6ce`, écrite à
04:38:50 UTC, gardée sans modification), dont elle corrige quatre formulations trop larges (§ 3.3, § 3.5, § 4, RSL-08) et
précise deux renvois (RSL-06, RSL-11) ; ni le verdict, ni les constats, ni leurs gravités ne changent. Brief :
`BRIEF-relecture-script-lecture-pilote4-v1.md` (`2ccd656a913cdf3a1e30e09f82665be805ee30dbe4e81daa4a866e46fcdcb177`, vérifiée
avant lecture). Deux faits ajoutés par le coordinateur pendant la relecture, traités ici : le dossier réel de la première
course est `pilote4-gemini-v6-2-v1-tentative2` (RSL-01, RSL-04, RSL-05, § 3.4) ; le `python3` de session-depot est de version
inconnue, d'où le rejeu sous 3.11 et 3.12 (§ 3.6).

## Verdict

**utilisable après corrections**

Calculs, gardes, absence de fuite et refus d'écraser sont conformes sur tous les essais, sous Python 3.11.17, 3.12.3 et
3.13.17. Les seules corrections exigées avant usage portent sur les commandes du LISEZMOI § 6 (RSL-01 : noms réels des
dossiers ; RSL-02 : option `-B`) ; le code peut servir tel quel ; tous les autres constats sont mineurs.

## 1. Ce qui a été relu

Copie : `/var/tmp/relecture-script-lecture-pilote4-v1/copie/` (fichiers mis en lecture seule ; l'original, revérifié à la
fin, est intact). Empreintes vérifiées sur la copie, égales à celles que rend l'auteur :

| fichier | sha256 |
|---|---|
| `lire_pilote4_v1.py` | `7176f0cd02e5f4f0a8a5dbaa59278780e5c1526b0b5249a36b9aef7d956f5521` |
| `essais_lire_pilote4_v1.py` | `2d3f2f26c779c2c65f19212aad3a66aa8be9374344712f03c692964f3697e59f` |
| `essais-lire-pilote4-v1.log` | `3c907fc7de5105eb4014c072c287e4471df479cddde01214a9ce044125e9fcba` |
| `LISEZMOI-script-lecture-v1.md` | `53597f9c85e931c5a424af022a28a513aa2a6fd6e0bb9da9cf82afb1b69d4c88` |

Ce qui fait foi, empreintes vérifiées : brief de l'auteur `c86be1a1…` ; texte v4 `782b858c…` (§ Plan, points 3, 4 et 4 bis,
l. 362–434 ; § Décisions pour le contexte) ; P4v3 `de7a5559…` (auquel renvoie le point 4 du texte v4 : § Objets l. 222–237,
§ Hypothèse l. 343–353, § Plan point 4 l. 410–421) ; T2 `d2944654…` (l. 440–486, fermeture). Code lu, sans l'exécuter :
noyau `taches.py` (entier), `boucle.py` l. 630–800, `archive.py` l. 1–160, `fichiers.py` l. 15–90, `cli.py` l. 295–325,
`banque.py` l. 1–60 et 150–225 ; lanceur v10 `0203f546…` (l. 54–55, 75–85, 155–170, 290–305, 485, 624, 746–753, 840–921) ;
références de la banque (code seul) `reference_provenance_conscience_v1.py` `52def946…` (égale à P4v3) et
`reference_contraste_paires_v2.py` `81d1d8ce…` ; `LISEZMOI-v9.md` de la banque `cdd64b97…` (§ 4 et § 5, documentation).

Interdits tenus : aucun fichier de données de la banque, aucune archive ni pièce d'un pilote réel ouvert, lu ou haché ;
aucun dossier `donnees/`, `runs/`, `diag/`, `pilotes/` ; aucun `git`, réseau, sous-agent ni clé ; aucune recherche récursive
dans les dépôts ; ni lanceur, ni noyau, ni organisme exécutés (seules les fonctions pures `taches.evaluer`,
`taches.wilson_inferieur` et `analyse.exactitude_equilibree` importées, sans cache : aucun `__pycache__` dans le noyau,
vérifié) ; rien écrit hors de `/var/tmp/relecture-script-lecture-pilote4-v1/` (les essais de l'auteur créent puis effacent
leurs dossiers de travail dans `copie/`, comme prévu).

## 2. Constats

**RSL-01** — `LISEZMOI-script-lecture-v1.md` l. 134–160 (§ 6) — **à corriger avant usage**.
Faux : les commandes visent `<R>/pilotes/pilote4-gemini-v6-2-v1` (fin de la v6.2) et
`<R>/pilotes/pilote4-gemini-v5-3-v1 … <R>/pilotes/pilote4-gemini-v6-2-v1` (fin de la v5.3) ; le dossier réel de la première
course est `pilote4-gemini-v6-2-v1-tentative2` (lanceur l. 165–167 : `-tentativeN` après un refus avant le manifeste) et celui
de la seconde peut porter un suffixe. Tapées telles quelles, elles visent la tentative 1 (pièces en clair et liste fermée,
sans archive) : refus, code 3, « EMPREINTES-pilote-v1.txt ne porte pas de ligne pour ferme.tar.gz : archive non vérifiable »
(motif trompeur pour l'opérateur), ou « dossier de course absent » ; rien n'est écrit (essais « commande du LISEZMOI § 6 »,
trois interpréteurs). Avec les bons chemins, le script accepte les suffixes de bout en bout : sortie
`lecture-pilote4-gemini-v6-2-v1-tentative2-v1.json` et `.md`, lignée lue dans l'archive (`gemini-organisme-v6-2`), deux
courses suffixées appariées par DOSSIER_COURSE_2 (Holm sur quatre, sortie au nom de DOSSIER_COURSE), refus « même course »
d'une copie de la course nommée sans suffixe, dans les deux ordres (par l'empreinte de la liste et la lignée).
Correction : récrire le § 6 avec le dossier exact `$PILOTE` de chaque course (dernière ligne du lanceur : « pilote fini :
$PILOTE ») et les noms de sortie qui en résultent, par exemple
`python3 -I -B lire_pilote4_v1.py lecture <R>/pilotes/pilote4-gemini-v6-2-v1-tentative2 <BANQUE_DIR> <SORTIE>`, puis
`python3 -I -B lire_pilote4_v1.py lecture <R>/pilotes/pilote4-gemini-v5-3-v1[-tentativeN] <BANQUE_DIR> <SORTIE> <R>/pilotes/pilote4-gemini-v6-2-v1-tentative2`,
et `… lecture <R>/pilotes/pilote4-gemini-v6-2-v1-tentative2 <BANQUE_DIR> <SORTIE_2> --sans-seconde-course` ; dire qu'une
copie de la branche `pilotes/<nom>` (nom sans suffixe, lanceur l. 920) donne une sortie d'un autre nom (RSL-05).

**RSL-02** — `LISEZMOI-script-lecture-v1.md` l. 137, 146, 153, 159 — **à corriger avant usage** (une option).
Faux : les commandes de production lancent `python3 -I` sans `-B`, alors que tous les essais (de l'auteur et de la relecture)
lancent `-I -B` : la propriété « rien d'écrit hors de SORTIE » n'est pas essayée dans les conditions de production. Un
interpréteur dont la bibliothèque standard n'a pas ses fichiers compilés en cache écrirait, sous root, des
`__pycache__/*.pyc` hors de SORTIE au premier import. Dans ce conteneur aucun cache ne manque : la trace système d'une
lecture lancée sans `-B` ne montre que cinq écritures, toutes dans SORTIE (création du dossier, puis des quatre fichiers en
mode exclusif), sous 3.11.17, 3.12.3 et 3.13.17 (`journaux/strace-lecture-sans-B-v1.txt`) ; le conteneur de session-depot
n'est pas vérifié. Correction : `python3 -I -B` dans les quatre commandes (ou `sys.dont_write_bytecode = True` avant les
autres imports du script).

**RSL-03** — `lire_pilote4_v1.py` l. 327–334 (avec l. 285–301) — mineur.
Faux : la fin d'archive (les blocs nuls que GNU tar écrit toujours) n'est pas exigée : un tar coupé net à une frontière de
membres, dans un flux gzip complet et valide, est accepté (code 0) ; les membres perdus sont tenus pour absents (repli,
« impossible » ou génération absente, signalés), la coupure elle-même n'est pas dite. Essai : archive coupée juste avant
l'en-tête du dernier membre nécessaire (`g001/juge/reponses-lues.json`) : lecture écrite, seul « repli déclaré » signalé,
sous les trois interpréteurs. Cas réel possible : `tar` tué pendant la fermeture (lanceur l. 878–887 : le flux gzip se ferme
proprement, l'archive est empreintée et poussée ; « ARCHIVE FERMÉE INCOMPLÈTE » n'est écrit qu'au LANCEMENT.md, que le
script ne lit pas). Aucun chiffre faux n'en sort, mais une lecture incomplète passe pour complète. Correction : après
l'itération, exiger au moins 512 octets nuls restants (le module a consommé le premier bloc nul ; une coupure nette n'en
laisse aucun), sinon refus « fin d'archive absente » ; ou refuser si le LANCEMENT.md porte « ARCHIVE FERMÉE INCOMPLÈTE ».

**RSL-04** — `lire_pilote4_v1.py` l. 528–532, 547–550, 929–931 — mineur.
Faux : aucune garde entre le nom du dossier et la lignée de l'archive : un dossier nommé `pilote4-gemini-v6-2-v1-tentative5`
dont l'archive porte `gemini-organisme-v5-3` est lu sans refus ni signalement (observation, trois interpréteurs) ; en mode
deux courses, rien ne vérifie qu'on a une course de chaque objet (seule l'identité des deux est refusée). Correction : au
moins signaler (mieux : refuser) un nom hors de `^pilote4-gemini-v(6-2|5-3)-v1(-tentative[0-9]+)?$` (motif du lanceur,
l. 299) ou une lignée autre que celle de l'objet nommé ; en mode deux courses, exiger un objet de chaque.

**RSL-05** — `lire_pilote4_v1.py` l. 528–532 et 875–878 ; LISEZMOI l. 142–143 et 156 — mineur.
Faux : le nom de la sortie vient du nom du dossier : la même course donne `lecture-pilote4-gemini-v6-2-v1-tentative2-v1`
lue dans `$PILOTE`, ou `lecture-pilote4-gemini-v6-2-v1-v1` lue dans une copie de la branche `pilotes/pilote4-gemini-v6-2-v1`
(« un dossier du même nom ») ; et la relecture « la v5.3 ne court pas » (Holm sur deux) porte le même nom que la lecture
provisoire, dans une autre SORTIE : deux contenus différents sous un même nom (R12). Correction : mettre la règle de (iii)
dans le nom (`…-provisoire-v1`, `…-holm-deux-v1`, `…-holm-quatre-v1`) et fixer le dossier (RSL-01) ou dériver le nom de la
lignée et du suffixe.

**RSL-06** — `lire_pilote4_v1.py` l. 501–515 et 616–636 (choix 4 de l'auteur) — mineur ; écart d'interprétation à trancher.
Le texte (4 bis) dit « au plus quatre tests (deux si la v5.3 ne part pas), corrigés par Holm » ; le brief, « la correction de
Holm sur les quatre tests ». Le script garde m = 4 (ou 2) quand un test est impossible, compté jamais rejeté : plus prudent que
la famille réduite aux tests faits, lecture la plus littérale du texte. Sur 8 000 familles tirées (2 et 4 tests, égalités,
tests impossibles), les deux lectures diffèrent 205 fois, toujours dans le sens prudent, par construction (un test impossible compté dans m ne
fait que relever les multiplicateurs des autres) (`journaux/calculs-independants-v1.log`).
Correction : aucune si conv-audit retient la lecture du brief (la règle est écrite dans la sortie) ; sinon réduire m aux
tests faits.

**RSL-07** — `lire_pilote4_v1.py` l. 174–183 et 921–924 (choix 14) — mineur ; écart texte ↔ brief, déclaré par l'auteur.
Le texte (4 bis) : si le secret est refusé, « (ii) est rapporté impossible pour cette famille » ; le brief : « refuse sinon » ;
P4v3 (§ Plan, point 4) : si les comptes ne sont pas recalculés, « la lecture s'arrête et le dit ». Le script refuse toute la
lecture, sans rien écrire : rattrapable, et cohérent avec P4v3, puisque la garde 8 / 14 exige le secret. Correction : aucune ;
écart à garder déclaré.

**RSL-08** — `lire_pilote4_v1.py` l. 88–89 et 618–624 — mineur ; écart brief ↔ texte, sans conséquence.
Le seuil provisoire 0,05 / 4 à une course vient du brief ; le texte ne connaît que Holm sur au plus quatre tests. Vérifié :
toute valeur p au plus égale à 0,0125 reste rejetée par Holm sur quatre (3 000 familles tirées) et, par construction, sur
deux (seuil de premier rang 0,025) ; un
« changement » provisoire ne peut pas être renversé, un « dans le bruit » provisoire peut le devenir, ce que dit le libellé
« provisoire, quatre tests au plus ». Correction : aucune.

**RSL-09** — `lire_pilote4_v1.py` l. 989–993 (choix 17) — mineur.
La ligne d'état est la même pour une lecture complète et pour une lecture toute « impossible » (par exemple si la structure de
l'archive réelle diffère de l'hypothèse : aucune génération trouvée, LISEZMOI § 4) ou portant des « écart avec le noyau » ;
poussée sans être affichée (retenue de 03:27), elle prend le nom (R12) sans que l'opérateur le sache. Correction : ajouter à
la ligne d'état des comptes entiers (« générations lues : 4 ; signalements : 0 »), ni score ni proportion, ou un code de
sortie non nul quand aucune génération notée n'est lue.

**RSL-10** — `lire_pilote4_v1.py` l. 1019–1024 — mineur.
« ERREUR INTERNE : <type> (ligne N du script …) » donne la ligne du dernier cadre de la pile, qui est dans la bibliothèque
standard quand l'exception y naît : un `score.json` imbriqué 200 000 fois (RecursionError, non prévue) donne « ligne 353 »
sous 3.11 et 3.12, « ligne 361 » sous 3.13 (lignes de `json/decoder.py`). Sur le fond, conforme : code 4, une ligne sur la
sortie standard, rien d'écrit, aucune valeur affichée. Correction : prendre le dernier cadre dont le fichier est le script.

**RSL-11** — `lire_pilote4_v1.py` l. 1007 ; motifs l. 134–145 et 262–264 — mineur.
`lecture -h` imprime « la v5.3 ne court pas » sur la sortie standard (motif `[0-9][.,][0-9]`) ; un motif de refus peut
recopier un nom de fichier poussé (`test-depense-<nom>`, lanceur l. 624) qui porterait ce motif — jamais un score.
Correction : « v5-3 » dans l'aide ; dire que le contrôle « aucun nombre décimal » vise les scores, non les noms de fichiers.

**RSL-12** — `lire_pilote4_v1.py` l. 1009–1025 — mineur.
Une interruption au clavier (hors de `Exception`) imprime la pile d'appel de l'interpréteur (chemins et lignes de code, aucune
valeur ; aucun motif décimal observé), fin par le signal d'interruption, rien d'écrit. Correction : attraper aussi
`KeyboardInterrupt` (« lecture non écrite : interrompue »).

**RSL-13** — `lire_pilote4_v1.py` l. 281–282 et 304–365 — mineur (robustesse).
Le module tarfile en flux coûte, à volume décompressé égal, d'autant plus que l'archive est compressible : 256 Mio de zéros,
0,2 à 0,6 s pour le contrôle zlib, 10,3 à 10,9 s par passage tarfile (trois interpréteurs,
`journaux/mesure-tarfile-flux-v1.log`) ; une archive de 35 Mo portant 1 Gio de zéros, 32 Mio aléatoires et 20 000 petits
fichiers se lit en 90 à 96 s, mémoire résidente maximale 136 Mio, valeurs justes. Une archive de texte et de JSON n'est pas
concernée ; un gros fichier de zéros dans l'espace des organismes coûterait des minutes. Correction (facultative) : donner à
tarfile, en mode `r|`, un lecteur qui décompresse lui-même par `zlib.decompressobj` borné par `max_length` ; ou dire l'ordre
de grandeur au LISEZMOI.

**RSL-14** — `lire_pilote4_v1.py` l. 803–806 — mineur (libellé).
En délégation sur `test` (référence 1,0), le Markdown dit « « au-dessus » inatteignable à ces effectifs, même à un score
parfait » ; le texte dit « (ii) y est impossible par construction », vrai à tout effectif. Correction : un libellé propre
quand la référence vaut 1.

**RSL-15** — `lire_pilote4_v1.py` l. 582–583, 865–870 et 954–955 — mineur (canal).
La sortie porte la taille et l'empreinte de chaque membre lu. La taille de `reponses-lues.json` dépend du nombre de réponses
retenues et du nombre de « sabotage » (8 caractères) contre « honnete » (7), `test` et `test_final` mêlés : pas une donnée
par tâche, mais un agrégat de `test_final` que le texte ne demande pas. Si une partie de la sortie devait être servie à un
organisme (point 3 : `test` sur décision de Lazar, jamais `test_final`), il faudrait l'en ôter. Correction : garder noms et
empreintes des membres lus, retirer leurs tailles de la sortie poussée.

**RSL-16** — `lire_pilote4_v1.py` l. 875–892 — mineur.
Les quatre fichiers sont créés l'un après l'autre (création exclusive juste) ; une erreur d'entrée-sortie entre deux laisse
un jeu partiel qui bloque toute reprise dans la même SORTIE (R12). Raisonné, non essayé. Correction : écrire sous des noms
provisoires puis lier sans écraser, ou dire au LISEZMOI qu'un jeu partiel se reprend dans une SORTIE neuve.

**RSL-17** — `essais_lire_pilote4_v1.py` l. 478, 297–314 et 334–336 — mineur (R5).
La batterie ne prend jamais la branche « au-dessus de la référence » de (ii) (toutes ses lignes saines sont « non
distinct », l. 478) ; plusieurs gardes n'y ont pas d'artefact : banque (identifiant en double, part absente, vérité hors
étiquettes, JSON illisible), liste d'empreintes (nom remontant ou absolu, nom en double, fichier poussé en lien, liste vide),
membre nécessaire en lien dur ou sous une autre graphie (`g0003`), données après la fin du flux gzip, en-tête à taille
négative, tar coupé ; son contrôle « rien d'écrit hors de SORTIE » ne regarde pas les dossiers temporaires du système. Tout
cela est essayé ici, conforme sous trois interpréteurs. Correction : les ajouter à la batterie.

## 3. Ce qui a été vérifié

### 3.1 Conformité au brief et aux points 3, 4 et 4 bis du texte

| exigence | source | état |
|---|---|---|
| `essai-banque` : empreintes, comptes 8 et 14, classes 4/4 et 10/4, refus et motif, n'imprime que comptes et issue | brief ; P4v3 § Plan 4 | fait (ligne exacte du LISEZMOI reproduite) |
| empreintes du dossier (compagnon puis lignes) et de la banque, refus sinon | brief, point 1 | fait, plus strict que `sha256sum -c` (liens, noms remontants ou absolus, doublons, liste vide refusés) |
| archive en mémoire, membres nécessaires seuls, refus des non ordinaires, absolus, remontants | brief, point 2 | fait ; « non ordinaire » vise les membres nécessaires, à raison (dossiers, liens, tubes de l'espace tolérés et ignorés) |
| effectif, classes, justes, exactitude équilibrée du noyau, recoupement (0,0001), sans arrêt | brief, point 3 | fait (recoupe aussi `vp`, `fn`, `vn`, `fp`, `non_repondu`, `n`) |
| (i) Wilson de chaque classe, 97,5 % bilatéral, z = 2,2414, bornes moyennées | brief 4 (i) ; texte 4 bis (i) | fait, exact |
| (ii) références 0,8056 / 0,8333 et 1,0 / 0,75 ; libellés ; borne maximale à score parfait ; surface et oracle à côté | brief 4 (ii) ; texte 4 bis (ii) ; P4v3 § Plan 4 | fait (RSL-14 ; secret refusé : RSL-07) |
| (iii) McNemar exact bilatéral, g0 contre g3 sur `test_final`, seuil provisoire, Holm sur quatre ou deux | brief 4 (iii) ; texte 4 bis (iii) | fait (RSL-06, RSL-08) |
| (iv) la phrase du texte ; aucune comparaison entre objets | brief 4 (iv) ; texte 4 bis (iv), point 4 | fait, mot pour mot ; aucune différence entre objets calculée |
| sous-ensembles « catégorie absente du train », comptes par classe, garde, part sans réponse | brief, point 5 ; P4v3 § Hypothèse | fait |
| réponses absentes : (i) à (iii) impossibles, score du noyau sans intervalle | brief, point 6 ; texte 4 bis | fait |
| sorties JSON et Markdown, compagnons, agrégats seuls, refus d'écraser | brief, point 7 ; R12 | fait (RSL-05, RSL-15, RSL-16) |
| une ligne d'état sans score ; erreurs sans score | brief, point 8 ; texte, point 3 (retenue) | fait (RSL-09, RSL-11, RSL-12) |
| essais sains et artefacts du brief ; variable réservée aux essais | brief, Essais | faits (RSL-17) |
| LISEZMOI : rangement des réponses et des scores, choix, incertitudes, commandes | brief, Ce que tu rends | fait ; lignes citées du noyau et du lanceur vérifiées ; commandes : RSL-01, RSL-02 |
| tableau complet de T2 (Brier, appels, coûts…) | P4v3 § Plan 4 | hors du périmètre du brief et du script ; à porter par d'autres pièces |

### 3.2 Calculs refaits indépendamment (`outils/calculs_independants_v1.py`, 26 vérifications sur 26)

Quantile : `statistics.NormalDist().inv_cdf(0,9875)` = 2,2414027, arrondi 2,2414 ; l'arrondi déplace une borne de moins de
7·10⁻⁷ (n ≤ 36). Wilson : forme close en décimal (50 chiffres) contre `wilson` du script, n de 1 à 60 et tous les s, écart
au plus 2,2·10⁻¹⁶ ; borne basse égale à `taches.wilson_inferieur(z = 2,2414)` ; classe vide → « impossible » ; tout juste →
[n / (n + z²) ; 1] ; tout faux → [0 ; z² / (n + z²)]. Borne basse maximale : moyenne des bornes basses à s = n ; 0,7818
(18 / 18) et 0,7049 (12 / 12) comme le texte. Exactitude équilibrée : 54 cas (classe vide, tout juste, tout faux, aucune
réponse, hasard avec non-réponses) égaux à la définition réécrite et à `taches.evaluer` (classe vide : sensibilité 0, comme le
noyau). McNemar : égal, pour b et c de 0 à 40, au test binomial exact « probabilités au plus égales à celle de l'observé »
(autre définition) ; valeurs connues (9/128, 1/128, 3/256, 11/512, 53/4096 ; b = c → 1 ; aucune paire discordante → 1) ;
symétrique. Holm : 8 000 familles contre un pas descendant réécrit (égalités, tests impossibles) ; ajustées 1/64 et 9/128,
1/128, 1, 3/128, 9/64 comme l'auteur. Seuil provisoire = 1/80. Règle « catégorie absente du train » : 400 banques inventées
(catégorie absente du secret, catégorie au train de l'autre famille seulement, classes mêlées) contre la transcription des
l. 37–41, 52 et 63–64 de `reference_provenance_conscience_v1.py` : égales. En outre, dans les cas sains de
`artefacts_relecture_v1.py`, chaque ligne (i)–(ii), chaque sous-ensemble et chaque test (iii) d'une sortie complète est
comparé au calcul indépendant de la relecture, réponses et catégories fabriquées par elle (aucune règle du script réutilisée).

### 3.3 Fuites

Sortie standard et sortie d'erreur : aucun motif `[0-9][.,][0-9]` dans aucune exécution (batterie de l'auteur rejouée quatre
fois, artefacts de la relecture sous trois interpréteurs : succès, refus, erreur interne non prévue, interruption au
clavier) ; seule exception au motif : l'aide (RSL-11). Une seule ligne sur la sortie standard, hors usage et hors
interruption au clavier (sortie standard vide). Fichiers écrits : aucune marque d'identifiant, de texte ou de catégorie de
tâche (marques `ZQX`, `TXTRL`, `CATRL` de la banque inventée), aucune réponse ni vérité par tâche (RSL-15 pour les tailles).
Écritures : pour chaque cas des artefacts de la relecture et des artefacts complémentaires (sauf les deux observations
lancées à part : archive très grande, interruption), instantané du dossier de travail, de `/tmp` et de `/var/tmp` avant et
après, puis seconde exécution sous trace d'audit Python (`outils/trace_ecritures_v1.py`, écriture hors de SORTIE bloquée et
consignée) : uniquement SORTIE ; la batterie de l'auteur contrôle son dossier de travail et celui du script ; trace système
sans `-B` : RSL-02. Aucun fichier écrasé : SORTIE avec des fichiers voisins (intacts), avec un seul compagnon déjà présent,
avec un lien pendant au nom de la sortie (cible non créée), SORTIE fichier : refus sans écriture.

### 3.4 Archive : ce qui est vérifié, ce qui reste une hypothèse

Vérifié sur le noyau et le lanceur : la course écrit dans `$PILOTE/course` (lanceur l. 746, `--sortie`, `--generations 4`),
l'archive du noyau est `course/archive/<lignée>/gNNN/` (l. 857 ; `archive.py` l. 76–78), avec `juge/score.json`,
`score-final.json`, `reponses_test.json` et `reponses-lues.json`, chacun scellé (`archive.py` l. 111–126 ; `boucle.py`
l. 719–748 et 782–786) ; rondes de conception en `cNNN` (ignorées) ; une lignée par course (`LIGNEE`, l. 79 et 85 ;
`--organisme-impose`, l. 751) ; `tar -czf ferme.tar.gz -C $PILOTE course ferme -C / <espace>` (l. 872–878), espace attendu
`/var/lib/essaim-m3/<16 caractères>` (l. 485), donc noms `var/lib/…` sans collision possible avec `course/archive/…` ;
vérités dans la banque publique que le noyau charge telle quelle (`cli.py` l. 308). Les archives synthétiques de la relecture
sont faites par GNU tar 1.35 avec cette commande même, liste fermée et empreintes par les lignes 909–919 du lanceur lues dans
son fichier ; l'espace y porte des liens absolus et remontants, un tube, des liens durs, un nom à saut de ligne, un nom non
UTF-8, des chemins longs et un leurre à la forme exacte d'un membre nécessaire : tout est ignoré, la lecture est juste.
Refusés, sous trois interpréteurs : lien symbolique d'une génération vers une autre, lien dur entre générations, membre en
double sous une autre graphie, données après la fin du flux gzip, en-tête à taille négative, somme de contrôle fausse (au
premier en-tête et au milieu), tar coupé dans un membre, taille énorme d'un membre nécessaire. Accepté à tort : tar coupé net
à une frontière (RSL-03). Hypothèses non vérifiables ici : que le code de `R` soit celui de `8e5e2f7b` (le lanceur le vérifie
par `git`) et donc que `reponses-lues.json` existe (sinon repli signalé) ; une seule lignée à générations notées (sinon refus) ;
la version de GNU tar de session-depot. Noms suffixés : RSL-01, RSL-04, RSL-05 ; essais de la relecture sur
`pilote4-gemini-v6-2-v1-tentative2` et `pilote4-gemini-v5-3-v1-tentative3`.

### 3.5 Gardes et surcharge réservée aux essais

Une seule surcharge : `LECTURE_PILOTE4_ESSAI_SEULEMENT_EMPREINTES_BANQUE` (aucune autre lecture de l'environnement). Définie,
même vide, elle met « ESSAI … » sur la sortie d'erreur ; acceptée, elle marque la ligne d'état, le JSON
(`essai_empreintes_banque_surchargees`) et le Markdown (bandeau) ; vide, à une seule empreinte ou en majuscules : refus.
Chaque garde a désormais un cas sain et un artefact (batterie de l'auteur, plus RSL-17 essayé ici), sauf deux contrôles de
cohérence interne qu'on ne peut provoquer sans changer le fichier pendant la lecture : l'empreinte de l'archive relue en
mémoire (l. 541–544) et l'égalité des membres entre les deux passages (l. 363–364).

### 3.6 Interpréteurs 3.11, 3.12, 3.13

Le script et ses essais se compilent sous 3.11.17, 3.12.3 et 3.13.17. Mêmes entrées, trois interpréteurs : treize cas
(quatre sains, huit archives malformées, essai-banque) donnent le même code, le même motif et les mêmes sorties, à l'heure et
au champ `script.python` près (`journaux/comparaison-versions-v2.log`) ; batterie de l'auteur (42 cas) et artefacts de la
relecture (28 cas, plus 10 complémentaires) conformes sous chacun. Différences observées : le numéro de ligne de RSL-10, et
c'est tout ; durées égales (RSL-13). Sur ces entrées, les changements du module tarfile entre ces versions ne changent rien :
le contrôle du flux gzip et le contrôle de fin d'archive du script tiennent lieu des refus que tarfile n'oppose pas en flux.
3.12.3 est une révision ancienne de la branche 3.12 ; aucune différence n'y est apparue. La batterie de l'auteur exige numpy
(noyau importé) : sous 3.11 et 3.12 du système, sans numpy, elle a été rejouée avec le harnais sous le Python du venv et le
script sous l'interpréteur essayé (`outils/rejouer_batterie_autre_python_v1.py`).

## 4. Essais rejoués et ajoutés

| essai | interpréteur du script | issue | journal |
|---|---|---|---|
| batterie de l'auteur, `--mutations` | 3.13.17 (venv) | 5 sains sur 5, 37 artefacts sur 37, 15 mutations sur 15 détectées, aucun cache dans le noyau | `journaux/rejeu-batterie-auteur-py313-v1.log` |
| batterie de l'auteur | 3.11.17 ; 3.12.3 ; 3.13.17 (`python3`) | 5 sur 5 et 37 sur 37, chaque fois | `journaux/rejeu-batterie-auteur-py3.*-v1.log` |
| calculs indépendants | 3.13.17 (venv) | 26 sur 26 | `journaux/calculs-independants-v1.log` |
| artefacts de la relecture : 6 sains, 18 artefacts, 4 observations ; chaque cas exécuté directement puis sous trace d'audit, sauf les observations « archive très grande » et « interruption » (lancement direct seul) | 3.11.17 ; 3.12.3 ; 3.13.17 | tous conformes, trois fois | `journaux/artefacts-relecture-py*-v1.log` |
| artefacts complémentaires : 9 artefacts, 1 sain | les trois | 30 sur 30 | `journaux/artefacts-complementaires-v1.log` |
| mêmes entrées sous trois interpréteurs : 13 cas | les trois | identiques | `journaux/comparaison-versions-v2.log` (la v1 : dossier parent de SORTIE oublié par le harnais, refus attendus du script, identiques aussi) |
| coût de tarfile en flux | les trois | RSL-13 | `journaux/mesure-tarfile-flux-v1.log` |
| trace système d'une lecture sans `-B` | les trois | cinq écritures, toutes dans SORTIE | `journaux/strace-lecture-sans-B-v1.txt` |

Artefacts de la relecture (au-delà de la batterie de l'auteur) : même course sous deux noms (suffixe et sans suffixe) ;
commandes du LISEZMOI § 6 telles qu'écrites, fin de la v6.2 et fin de la v5.3 ; lien symbolique de `g003` vers `g000` ; lien
dur entre générations ; membre en double sous la graphie `g0003` ; données après la fin du flux gzip ; en-tête à taille
négative ; tar coupé dans un membre ; génération notée manquante au milieu ([0, 1, 3]) ; `reponses-lues.json` non UTF-8 ;
`reponses-lues.json` à « reponses » en liste ; réponses illisibles (nulle, étiquette de l'autre famille, nombre, identifiant
hors banque : quatre écartées, signalées, valeurs intactes) ; exception non prévue (récursion du décodeur JSON) ; SORTIE à un
seul compagnon présent ; lien pendant au nom de la sortie ; SORTIE fichier ; variable d'essai vide, partielle, en
majuscules ; puis, complémentaires : noms remontant, absolu, en double dans la liste d'empreintes, fichier poussé en lien,
liste vide, banque à identifiant en double, à part absente, à vérité hors étiquettes, à JSON illisible. Cas sains : essai-banque ;
une course au nom `-tentative2` ; deux courses suffixées (Holm sur quatre) ; `--sans-seconde-course` (Holm sur deux) ; SORTIE
existante à fichiers voisins ; branche « au-dessus de la référence » (classes de 40, neuf lignes sur seize au-dessus, chacune
égale au calcul indépendant) ; secret en lien symbolique. Observations : lignée contraire au nom (RSL-04), tar coupé net
(RSL-03), archive très grande (RSL-13), interruption au clavier (RSL-12). Les journaux `mise-au-point-harnais-1.log` et `-2.log`
gardent deux essais du harnais avant correction (instantané trop strict sur la date du dossier parent de SORTIE, puis
observation du tar coupé recentrée) ; ils ne disent rien de faux du script.

## 5. Ce que la relecture n'a pas pu vérifier

- L'archive réelle et sa structure (interdit) : hypothèses du § 3.4.
- La banque réelle (interdit) : que le fichier secret d'empreinte `a13217b8…` soit bien `banque-confrontation-v3-secret.json`,
  qu'il porte le champ `category`, les effectifs 18 / 18 et 12 / 12, les comptes 8 et 14 ; la commande `essai-banque` de
  session-depot le vérifiera avant la lecture.
- Que le code de `/home/claude/pilote4/essaim-m3-refonte-v1` soit celui de `8e5e2f7b` (sans `git`).
- Le `python3`, la présence des caches compilés (RSL-02) et le GNU tar du conteneur de session-depot ; le suffixe éventuel du
  dossier de la v5.3.
- Une vraie reprise par segments (structure supposée identique : le noyau reprend la même `course/`) et une erreur
  d'entrée-sortie au milieu de l'écriture des sorties (RSL-16, raisonné).

## 6. Pièces

Sous `/var/tmp/relecture-script-lecture-pilote4-v1/` : ce rapport (v2) et son compagnon ; la v1
(`a9a4d70c929a59b97e615c71f139c9e7b6e842478ba8df5760ac9c7f4926c6ce`) et son compagnon, gardés ; `journal-essais-relecture-v1.log`
(`862c8b362909d6a7e49a0f8a654a149bba77b1d7542c2c407c6a1f144dd61a67`, recopie à l'identique de tous les journaux, chacun sous
son nom et son empreinte) et son compagnon ; `EMPREINTES-relecture-v1.txt`
(`d537e0ebbc9e326c22f908110ef7c3c906742da0cfbd92b809f034163f8f4a87` : empreintes des journaux de `journaux/` et des outils de
`outils/`) et son compagnon ; `outils/` (`artefacts_relecture_v1.py` `9d6b65d7…`, `artefacts_complementaires_v1.py`
`a48f66cf…`, `calculs_independants_v1.py` `060e211a…`, `comparer_versions_v1.py` `f24ac9b0…`,
`rejouer_batterie_autre_python_v1.py` `8add5edf…`, `trace_ecritures_v1.py` `434d6311…`) ; `copie/` (copie relue, inchangée).
Données synthétiques seulement ; dossiers de travail effacés.
