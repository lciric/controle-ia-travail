# Contre-lecture adverse de la chaîne de lancement version 6 de la course d'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Lecteur** : contre-lecteur neuf (R2), sous-agent d'une autre lignée de modèle que le développeur ; je n'ai écrit aucune des
  pièces lues. Je n'ai pas ouvert les trois autres contre-lectures de la version 6 déposées dans ce dossier (angles « conformité »,
  « gardes », « machine ») : ce rapport est indépendant d'elles.
- **Date (UTC, `date -u`)** : 2026-11-18, de 04:45Z à 05:40Z environ. Processeur seulement : aucune machine, aucune dépense, aucun
  appel au loueur ni à l'hébergeur, aucune clé lue ni affichée, aucun réseau (essais sous `unshare -n`), aucun commit, aucune
  poussée. Seul fichier écrit dans le dépôt : ce rapport et son compagnon.
- **Angle** : partir de l'hypothèse que la chaîne est fausse, et chercher à le prouver par des artefacts fabriqués.
- **Pièces, empreintes relues sur disque** : `scripts/amorce_bbis_v6.sh` `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` ;
  `scripts/lancer_bbis_v6.sh` `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` ;
  `tests/test_chaine_bbis_v6_v1.py` `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca` ;
  `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon1.md` `0056edaa66b20c2e5b40cfecf7ef9752834ae68c76db9e2cf4c3cc7efe75b58d`.
  La consigne nommait le commit `081f8d99` ; la tête a bougé pendant la lecture (`0bab326b…` au moment de mes mesures, `aed995ef…`
  à la rédaction) ; les quatre empreintes sont restées celles-là.
- **Dossier de travail (jetable, peut être effacé)** :
  `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/cl-amorce-v6-adverse/`
  (outil `outils/attaques_v1.py`, `1ba33a13743c8345…` ; sortie `attaques-v1-sortie.txt`, `e495777c9fd06ac0…` ; mesure
  `mesure-tete/`). Chaque preuve ci-dessous est redite en clair pour être rejouée sans ce dossier.

## Verdict

**À corriger.** Je n'ai trouvé **aucun bloquant** : lancée telle qu'elle est écrite, depuis les copies d'empreintes ci-dessus et
avec des arguments justes, la chaîne passe chacune de ses portes dans mes rejeux, et les trois arrêts certains de R-3160 sont
levés. Les artefacts que la consigne me demandait de fabriquer sont **tous arrêtés** (tableau du § « Ce qui a tenu »). Mais
quatre défauts **majeurs** demeurent, que j'ai fait jouer : dans les quatre cas, le lanceur imprime la commande de création
alors que la course s'arrêterait sur la machine payée, ou tournerait avec un texte d'amorce autre que celui que l'addendum
rattache. Aucun ne touche l'amorce ; tous se corrigent soit par un lanceur version 7 (quelques lignes), soit, à défaut, par des
lignes exécutables du feu.

## BLOQUANTS

Aucun.

## MAJEURS

### M1 — Rien d'exécutable ne lie l'amorce qui part à l'empreinte que l'addendum rattache

- **Où** : `scripts/lancer_bbis_v6.sh:153`, `:161`, `:164-168` (l'amorce est lue à côté du lanceur, `$ICI/amorce_bbis_v6.sh`,
  encodée et imprimée ; aucune comparaison d'empreinte) ; brouillon d'addendum, TA-2 (« rattachés par leurs empreintes, écrites
  au troisième addendum »).
- **Constat** : la fiche de code en vigueur ne cite pas la version 6 (voulu, TA-1). Sur la machine, la garde d'entrée de la
  marche contrôle 63 fichiers ; ni l'amorce ni le lanceur version 6 n'en sont, et l'amorce version 6 n'est même pas extraite
  (vérifié sur l'arbre reconstruit : 516 fichiers, aucun des deux). Il ne reste, pour arrêter une amorce autre, que seize
  caractères imprimés par le lanceur et une ligne de journal écrite par l'amorce elle-même, à comparer par un opérateur.
- **Preuve rejouable** : copier `scripts/` dans un dossier `X/scripts`, poser un lien `X/src` vers `src`, changer **une** ligne
  de `X/scripts/amorce_bbis_v6.sh`, puis jouer `bash X/scripts/lancer_bbis_v6.sh commande …` sur le dépôt jetable de
  `tests/test_chaine_bbis_v6_v1.py` (`_depot_course`, `_offre`, commit `c1`). Cinq altérations jouées, **cinq commandes de
  création imprimées, code 0** : plancher d'essais abaissé à 1 ; exclusion de la pièce « mots et coût » retirée des motifs ;
  motif `/docs/notes/` ajouté ; garde de la clé d'interface du conteneur retirée ; contrôle de la liste « Jamais » sur la sortie
  de 7b retiré (`attaques-v1-sortie.txt`, lignes 4a à 4e). Le lanceur reconstruit même l'arbre d'après les motifs **altérés**.
- **Portée, sans grossir** : la version 5 avait le même trou côté lanceur ; la version 6 n'ouvre rien, mais elle perd le seul
  lien scellé (la fiche) sans le remplacer par un contrôle. C'est précisément l'artefact « empreinte d'un fichier cité altérée »
  appliqué aux deux fichiers que l'addendum cite.
- **Correction proposée** : dans `commande` (et `essais-du-commit`), refuser si l'empreinte de `$ICI/amorce_bbis_v6.sh` n'est pas
  celle écrite en constante dans le lanceur (`AMORCE_SHA256=26f954e9…`), avec un essai (cas sain, amorce changée d'un octet) ;
  l'addendum et le feu nomment alors l'empreinte **entière** du lanceur, que l'opérateur vérifie par `sha256sum -c` avant de
  le jouer. À défaut de code : le feu exige `sha256sum -c` sur les deux compagnons, et la lecture, dans les premières minutes,
  de la ligne « amorce v6 : empreinte … » du journal, égale sur 64 caractères ; sinon destruction par identifiant.

### M2 — Le plancher d'essais (premier des trois arrêts de R-3160) n'est pas une porte de la commande de création

- **Où** : `scripts/lancer_bbis_v6.sh:137-169` (`commande` ne joue ni n'exige `essais-du-commit`) ; `:170-186` (sous-commande à
  part) ; `scripts/amorce_bbis_v6.sh:64`, `:327-332`.
- **Constat** : des trois arrêts certains, deux sont désormais des refus de `commande` (commit sans lignes d'inscription, fichier
  de la fiche hors des motifs). Le troisième — compte d'essais sous le plancher sur l'arbre extrait — ne tient qu'à la mémoire
  de l'opérateur : `commande` imprime la création sans qu'aucune mesure existe pour ce commit.
- **Preuve rejouable** : le « cas sain » du fichier d'essais lui-même (`test_commande_v6_commit_de_la_course_cas_sain_et_artefacts`,
  dépôt `_depot_course` sans `n_essais`) : l'arbre du commit ne porte **aucun** fichier `tests/test_t07bbis_*`, et la commande
  de création est imprimée, code 0. Sur la machine, la ligne d'essais de l'amorce s'arrêterait à l'étape 5, après
  l'installation des paquets (`attaques-v1-sortie.txt`, ligne 0).
- **Deux fragilités liées, à dire au feu** : (a) la marge est nulle (151 mesurés, 151 exigés) : un seul saut de plus sur la
  machine (Python 3.11, roue de la carte) arrête la course ; je n'en ai trouvé aucun à la lecture, mais je ne peux pas le
  prouver ici (voir Limites) ; (b) un plancher est un minimum : si le commit de la course porte des essais de plus qu'au
  candidat, autant de sauts imprévus passeraient sans bruit.
- **Correction proposée** : `essais-du-commit` écrit dans son dossier une fiche de mesure (commit, empreinte de l'amorce, compte
  passé, compte sauté, plancher) ; `commande` prend ce dossier en argument et refuse si la fiche manque, cite un autre commit ou
  une autre empreinte d'amorce, ou si le compte passé n'est pas **égal** à 151 et le compte sauté à 25. À défaut de code : le feu
  recopie la ligne « BBIS ESSAIS DU COMMIT <commit de la course> : … 151 passed, 25 skipped » et l'empreinte de `essais.txt`.

### M3 — L'échéance de la minuterie n'est bornée par aucune porte de session (hérité de la version 5)

- **Où** : `scripts/lancer_bbis_v6.sh:141` (forme seule) ; `scripts/amorce_bbis_v6.sh:131` puis `:133` (la borne « [maintenant,
  + 24 h] » est placée **après** la sortie de l'essai local : l'essai local que joue le lanceur ne la voit jamais).
- **Preuve rejouable** : `commande` sur le registre réel, commit `0bab326b…`, offre fabriquée de la preuve, texte de
  `feu-bbis-v2.txt`, deux relances : avec une échéance **passée d'une heure**, puis **à trente jours**, la commande de création
  est imprimée, code 0 (deux fois). Sur la machine, l'amorce refuserait à sa ligne 133 (« échéance hors de [maintenant,
  + 24 h] »), code 2, **avant** la minuterie et sans demander l'arrêt : démarrage payé, aucune trace poussée. À l'inverse, une échéance à 24 heures est acceptée des deux côtés, alors que le feu en prévoit 13 : au prix plafond
  (1,40 USD/h de carte, 0,08 USD/h de stockage) la minuterie ne détruirait qu'après ≈ 35,5 USD, au-delà du reste de la ligne
  d'accord (≈ 34 USD, GO-2026-11-18-03) — seule la garde de dépense tenue par l'opérateur couperait.
- **Portée** : faute de frappe d'opérateur, non défaut du chemin nominal ; hérité, non introduit par la version 6. Je le classe
  majeur parce que la version 6 se donne pour objet de refuser avant la création tout arrêt connaissable d'avance.
- **Correction proposée** : dans `commande`, refuser une échéance hors de ]maintenant + 1 h ; maintenant + 13 h] (la durée du
  feu), avec son essai. À défaut : ligne du feu, calcul de l'échéance par commande écrite (`$(( $(date +%s) + 46800 ))`).

### M4 — La garde neuve de la clé d'interface du conteneur peut arrêter une course saine, sans trace ni arrêt demandé

- **Où** : `scripts/amorce_bbis_v6.sh:138`.
- **Constat** : la garde est juste dans son intention (correction 6 de la contre-lecture du projet de feu) et elle marche :
  variable absente ou vide, refus, code 2, avant l'armement (rejoué). Trois réserves, que rien de ce que j'ai le droit de lire ne
  lève : (a) **la présence de cette variable sur une machine lancée par cette commande-ci** (`--entrypoint bash --args -c …`)
  n'est établie par aucune pièce lue — les registres disent pour les deux machines du 16 novembre « état "stopped" demandé par
  l'amorce », sans le code de réponse ; les journaux sont sur une branche de données que je n'ouvre pas ; si le loueur ne la pose
  pas, la version 5 aurait couru jusqu'au bout (minuterie inutile, la session détruit), la version 6 perd la course unique à la
  première seconde ; (b) le refus est un simple `exit 2` sur la sortie standard, avant le journal poussé et sans demande
  d'arrêt (impossible sans clé) : la machine facture, et peut redémarrer en boucle, jusqu'au geste de la session ; (c) une clé
  faite d'espaces passe (`[ -n " " ]`, rejoué) : présente ne veut pas dire valide, l'addendum le dit (§ 4, point 4).
- **Correction proposée** (sans toucher à l'amorce) : la mère lit, dans le journal de l'une des deux machines du 16 novembre, la
  ligne « état "stopped" demandé : HTTP … » ; un code 200 prouve la clé présente et valide sous ce mode de lancement, et le feu
  le cite. Le feu ajoute : « aucune ligne "minuterie lancée" lue dans les N minutes après le démarrage : destruction par
  identifiant, vérification d'absence, compte rendu ». Si le code lu n'est pas 200, la garde devient un nœud à porter à Lazar
  avant le feu.

## MINEURS

1. **Signature des commits de la session** — `scripts/lancer_bbis_v6.sh:83` : le commit du dépôt jetable hérite du réglage global
   de la session (`commit.gpgsign=true`, service de signature local). Sous `unshare -n`, `essais-du-commit` rend « BBIS REFUS :
   commit local des entrées copiées impossible » (observé ; levé en posant `HOME` sur un dossier vide). Faux refus seulement, donc
   fermé du bon côté. Correction : `git -C "$d" -c commit.gpgsign=false commit …`.
2. **Compte des essais lu sur la dernière ligne** — bloc `compte-des-essais`, inchangé depuis la version 5
   (`scripts/amorce_bbis_v6.sh:325`, `:328`) : un essai qui imprime « 999 passed » à la fermeture de l'interpréteur fait lire
   999 (rejoué, ligne 8c : trois essais réels, « 999 passés ≥ 151 »). Il faut du code d'essai malveillant, lui-même sous la
   fiche : hérité, sans conséquence pratique. Les sautés et les « xpassed » ne sont **pas** comptés (lignes 8a, 8b : 150 < 151,
   refus).
3. **Clé de prix en double** dans le fichier d'offre (`{"prix_usd_h": 9.9, …, "prix_usd_h": 1.1}`) : la dernière valeur est
   lue, la commande est imprimée (ligne 2d). Le fichier est construit par programme depuis la recherche ; à signaler seulement.
4. **Fichiers de la racine du dépôt extraits sur la machine** par le motif hérité `/*` : douze fichiers hors configuration
   (`RENDU-fille-10-bras-b-v4-v1.md`, `RENDU-fille-10-course-v12-v1.md`, `RAPPORT_COMPLET_DECOUVERTES_ET_BILAN_TAIF.md`, six
   `NODE_*.log`, `DAEMON_NOCTURNE_72H_SELF_HEALING.log`, `CLAUDE.md`, `README.md`). **Je ne les ai pas ouverts** (contenu inconnu
   de moi ; les registres décrivent les deux premiers comme des passations de code du 8 novembre). La marche ne les lit pas ;
   la version 6 n'y change rien ; l'addendum dit « onze scripts de plus », ce qui est exact par rapport à la version 5. À faire
   regarder par quelqu'un qui en a le droit, contre la liste « Jamais ».
5. **Essais** — `tests/test_chaine_bbis_v6_v1.py:90` : la clause `or nom == "arret-et-traces"` dispense ce bloc de l'égalité
   avec la version 5 alors qu'il est égal ; elle est inutile et affaiblit l'essai. Aucun essai ne couvre M1 à M3.
6. **Le contrôle avancé de l'amorce n'est pas rejoué par le lanceur** : `commande` rejoue la garde d'entrée de la marche, non
   le bloc « fiche-sur-l-arbre ». Je l'ai joué à la main sur l'arbre réel reconstruit, sous Python 3.11 : conforme (voir plus
   bas). Il est bien moins sévère que la marche sur trois points (dates, forme de l'empreinte, chemins à `..`), jamais plus.

## Ce qui a tenu (artefacts fabriqués, tous arrêtés)

| artefact | porte | résultat |
|---|---|---|
| commit sans ligne d'inscription (jouet ; et commit réel `05cd22aa…`) | `commande`, garde « commit de la course » | refus, « ligne CODE-BBIS absente (exigée) ; ligne GO-BBIS absente (exigée) » |
| idem, sur l'arbre | bloc « fiche-sur-l-arbre » de l'amorce | arrêt, « ligne CODE-BBIS absente du registre propre » |
| fichier de la fiche hors des motifs (un des onze motifs retiré, registre réel) | `commande` | refus, « scripts/repetition_carte_bbis_v2.py : … absent : arrêt (R11) » |
| fichier de la fiche absent, ou changé d'un octet (arbre réel) | bloc de l'amorce, Python 3.11 | arrêt dans les deux cas |
| compagnon de la fiche altéré au commit | `commande` | refus |
| troisième ligne `CODE-BBIS` au commit | `commande` | refus, « en double ou mal formée » |
| clé de B bis dans le registre partagé au commit | `commande` | refus |
| essai en moins (150 passés, 5 sautés ; 150 passés, 5 « xpassed ») | `essais-du-commit` | refus, « 150 passés < 151 » |
| image autre (`python:3.11-slim-bookworm`, `docker.io/library/python:3.11-bookworm`) | `commande` | refus |
| prix 1,41 ; 1,4000001 ; non-nombre ; absent ; chaîne ; 0 ; booléen | `commande` | refus (1,40 passe) |
| clé du conteneur absente, vide | amorce, ligne 138 | refus, code 2, avant la minuterie |
| commit non poussé, branche absente | `commande`, garde « commit joignable » | refus (essais du développeur, rejoués) |

**Le compte de 151 n'est pas atteint par construction.** Mesure refaite par moi, `lancer_bbis_v6.sh essais-du-commit` à la tête
`0bab326b84e24107fe9848b98c3912d909380165`, sans réseau : « 151 passed, 25 skipped, 4 warnings », code 0 ; 516 fichiers sur
l'arbre, liste **identique** à celle de la preuve du développeur ; les 25 sauts sont ceux du rapport des préalables. Le fichier
d'essais neuf ne correspond pas au motif `tests/test_t07bbis_*` et n'est pas sur l'arbre ; les sautés et « xpassed » ne
comptent pas ; le code de sortie 0 est exigé. Les 151 se répartissent sur quinze fichiers d'essais, tous sous la fiche (seul
`tests/conftest.py` est hors fiche). Les 12 essais de `tests/test_chaine_bbis_v6_v1.py` passent (35 s, sans réseau).

**Autres vérifications.** Différence avec la version 5 : conforme aux six et cinq écarts déclarés, rien d'autre. Pilote réel
(`commande`, registre réel, tête `0bab326b…`) : code 0, deux lignes, le texte décodé de la commande a l'empreinte `26f954e9…`
entière, aucun dossier jetable laissé, rien d'écrit dans le dépôt. Syntaxe sous Python 3.11 (celui de l'image) : 262 fichiers
de `src/`, des essais et des scripts de B bis compilés sans faute ; bloc « fiche-sur-l-arbre » joué sous Python 3.11 sur
l'arbre réel : « 63 fichiers de la fiche présents, empreintes conformes ». Le seul essai qui nomme la carte lève sa garde
avant de toucher l'appareil (lu).

## LIMITES

- **Pas de machine** : rien n'est prouvé sur la carte. Je n'ai pas pu jouer les 151 essais sous Python 3.11 (aucun paquet pour
  cet interpréteur ici, aucune installation permise) : seule la syntaxe l'est. Le code du second addendum (`marche_v4`, ses
  essais) n'a, à ma connaissance, jamais tourné sur une machine ; avec une marge nulle au plancher, c'est le risque résiduel
  principal, que je ne sais ni prouver ni écarter.
- **Non lu** (cloisonnement) : rien sous `diag/`, `runs/`, `donnees/` ; aucune branche de données ni de calcul ; aucun journal
  de machine ; les fichiers de la racine du mineur 4 ; les trois autres contre-lectures de la version 6.
- **Lu en entier** : les deux amorces et les deux lanceurs (versions 5 et 6) et leurs différences ; le fichier d'essais ; le
  brouillon d'addendum ; la fabrique du lanceur et les sorties de la preuve ; `marche_v4.gardes_d_entree` et le début de
  `marche` ; `lecture_v3.lire_lignes` ; dans `registre_bbis_v2`, les fonctions appelées par la garde ; le registre propre, le
  feu et l'accord de B bis ; le rapport des préalables ; les lignes d'accord GO-2026-11-14-09, GO-2026-11-18-03, -04, -05 ;
  R-3160. **Lu par extraits ciblés seulement** : le texte scellé et ses deux addenda (liste d'arrêt, liste « Jamais », blocs
  qui nomment l'amorce), la contre-lecture du projet de feu (points 3 à 7), `registres/decisions.md` hors R-3160, la fabrique
  de l'amorce (non lue), le projet de feu version 3 (non lu), le registre voisin des addenda (non lu). La conformité de
  l'addendum, « ancien » par « ancien », n'est pas mon angle et je ne la juge pas.
- **Hors des pièces, à trancher par la mère avant le feu** : la commande imprimée passe deux clés à la machine (`HF_TOKEN`,
  `GH_TOKEN`) ; la ligne d'autonomie GO-2026-11-18-05 laisse à Lazar « le passage d'une clé à une machine ». Je ne sais pas si
  la ligne GO-2026-11-14-09 le couvre déjà ; je le signale, sans le juger.
