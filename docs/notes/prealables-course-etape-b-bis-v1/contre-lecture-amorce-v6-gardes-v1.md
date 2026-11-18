# Contre-lecture de la chaîne de lancement version 6 de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — angle : les gardes — v1

- **Lecteur** : contre-lecteur neuf (règle R2), sous-agent ; je n'ai écrit ni l'amorce, ni le lanceur, ni leurs essais, ni le
  brouillon du troisième addendum, ni aucune pièce antérieure de la chaîne.
- **Date (UTC)** : 2026-11-18. Processeur seulement ; aucune machine, aucun appel au loueur ni à l'hébergeur, aucune clé lue,
  aucun commit, aucune poussée. Tous les jeux dans un clone jetable du dépôt au commit `081f8d99acec3396a01359586732d1ffdb4b9d40`
  (`/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/cl-amorce-v6-gardes/depot`),
  sous `unshare -n` (aucun réseau), avec un `HOME` jetable dont la configuration de git ne signe pas les commits (la signature de
  la session demande le réseau et faisait échouer six essais sur douze sans rapport avec la chaîne).
- **Pièces contre-lues, empreintes relues** : amorce version 6 `scripts/amorce_bbis_v6.sh`
  `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` ; lanceur version 6 `scripts/lancer_bbis_v6.sh`
  `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` ; essais `tests/test_chaine_bbis_v6_v1.py`
  `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca` ; brouillon 1 du troisième addendum
  `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon1.md` `0056edaa66b20c2e5b40cfecf7ef9752834ae68c76db9e2cf4c3cc7efe75b58d` ;
  preuves de simulation `brouillons/T0.7-etape-B-bis-v1/preuve-amorce-v6-v1/` (fabriques comprises). Différences avec la
  version 5 faites par `diff` sur les deux scripts.

## Verdict : « à corriger »

**Aucun bloquant.** Chaque garde neuve ou modifiée fait ce qu'elle dit, a son cas sain et au moins un artefact éprouvés (règle
R5), et je n'ai trouvé aucun repli silencieux qui laisse passer une course fautive. Les douze essais passent (rejoués). Le
plancher de 151 est reproduit à la tête réelle du dépôt (`081f8d99…`), la garde d'entrée de la marche y passe, le contrôle avancé
de l'amorce aussi. **Deux majeurs**, corrigeables sans code neuf (par le feu et par l'addendum) ou par une version 7 du lanceur :
l'empreinte de la chaîne qui lance n'est contrôlée par aucune garde, alors que le troisième addendum en fait le seul
rattachement de ce code au dispositif scellé ; la remesure du plancher au commit de la course n'est pas exigée par la commande de
création. Comme la course est la course unique accordée (second addendum, section SA-15), tout arrêt après le démarrage payé la
consomme : ces deux points ne doivent pas rester à la seule mémoire de l'opérateur.

## BLOQUANTS

Aucun.

(J'ai d'abord classé le majeur 1 en bloquant, au titre de « ce que la version 5 arrêtait et que la version 6 n'arrête plus ». À
l'examen, la version 5 ne l'arrêtait pas non plus : elle embarquait la copie de l'amorce prise dans le dossier de la session
(`$ICI`), jamais comparée à la fiche ; la marche ne contrôlait que la copie de l'arbre au commit de la course. Ce n'est donc pas une
régression de garde, c'est un manque ancien que la version 6 rend décisif. Je ne le grossis pas.)

## MAJEURS

### M1 — L'empreinte de l'amorce et du lanceur version 6 n'est vérifiée par aucune garde, alors que le troisième addendum en fait le seul rattachement

- **Où** : `scripts/lancer_bbis_v6.sh:165-168` (base64 pris de `$ICI/amorce_bbis_v6.sh`, seize caractères d'empreinte imprimés
  pour l'œil) ; `scripts/amorce_bbis_v6.sh:155` (empreinte écrite au journal, après coup, jamais comparée) ; brouillon du troisième
  addendum, écart TA-2 (« ils sont rattachés par leurs empreintes, écrites au troisième addendum ») et § 6.
- **Ce qui manque** : la fiche de code en vigueur (`registres/t07-etape-b-bis/code-bbis-v2.json`) cite l'amorce et le lanceur
  version 5 ; la version 6 n'est ni dans la fiche, ni dans l'arbre de la machine (les motifs l'excluent exprès : l'essai
  `tests/test_chaine_bbis_v6_v1.py:48-51` la range dans les « interdits »). La liste d'arrêt du texte scellé
  (`prereg/T0.7-etape-B-bis-v1.md:181` : « Empreinte d'une entrée (… code cité) différente de celle consignée : arrêt (R11) ») ne
  peut donc s'appliquer à ce qui lance que par l'empreinte du troisième addendum. Or `commande` imprime la création **sans** exiger
  (a) que la ligne `ADDENDUM-ECART-3-BBIS` soit inscrite au registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md`, (b) que le
  texte qu'elle cite soit scellé, (c) que les empreintes complètes de l'amorce embarquée et du lanceur qui tourne y soient égales.
  Une amorce modifiée après la contre-lecture, ou un feu donné avant le scellement de l'addendum (GO-2026-11-18-04 et R-3170 (8)
  l'exigent avant le feu), partiraient sans arrêt ; la seule trace serait la ligne du journal de la machine, lue après la dépense.
- **Preuve rejouable** : `grep -n "ADDENDUM\|addenda" scripts/lancer_bbis_v6.sh scripts/amorce_bbis_v6.sh` ne rend rien ;
  `grep -n "sha256sum" scripts/lancer_bbis_v6.sh` ne rend que la ligne 167, qui coupe l'empreinte à seize caractères pour
  l'impression. Rejoué : une ligne de commentaire ajoutée à la fin de l'amorce du clone jetable, les essais
  `test_commande_v6_commit_de_la_course_cas_sain_et_artefacts` et `test_commande_v6_commit_joignable_image_et_prix` passent
  toujours (2 passés, 24 s) : la commande de création est imprimée avec l'amorce modifiée (l'assertion sur les seize caractères
  relit le fichier modifié lui-même et ne peut rien voir). Fichier remis à l'état du commit ensuite (`26f954e9…`).
- **Correction proposée** (au choix) :
  1. *Sans code neuf* : écrire au feu (version 4) un geste d'opérateur exécutable et son arrêt : avant la création, décoder le
     base64 de la commande imprimée et calculer `sha256sum` du résultat et de `scripts/lancer_bbis_v6.sh` ; exiger l'égalité **sur
     les 64 caractères** avec le § 6 du troisième addendum **scellé** et inscrit (`ADDENDUM-ECART-3-BBIS`) ; inégal ou addendum non
     inscrit : arrêt, rien n'est créé. Le dire à l'addendum (§ 4, « ce que ces gardes ne voient pas ») et le reporter au verdict
     comme garde tenue par l'opérateur, comme le plafond de prix de GO-2026-11-18-03 (3).
  2. *Par une version 7 du lanceur* (R12) : dans `commande`, refuser si le registre voisin n'a pas exactement une ligne
     `ADDENDUM-ECART-3-BBIS` dont le fichier est scellé (compagnon et empreinte égaux à la ligne) et contient les 64 caractères de
     `sha256sum` de l'amorce embarquée et du lanceur (`$0`) ; calculer l'empreinte sur le texte même qui est encodé en base64 ; et
     passer `-e EMPREINTE_AMORCE=<64 caractères>` à la machine, que l'amorce compare à `sha256sum < "$0"` avant d'armer quoi que ce
     soit (garde de transport, cas sain et artefact à éprouver).

### M2 — La remesure du plancher d'essais au commit de la course n'est exigée par aucune garde

- **Où** : `scripts/lancer_bbis_v6.sh:137-169` (`commande` ne joue ni n'exige `essais-du-commit`) et `:170-186` (sous-commande
  isolée) ; `scripts/amorce_bbis_v6.sh:60-64` (« à remesurer au commit de la course avant le feu ») ; brouillon du troisième
  addendum, § 4 point 2 et § 7 point 3.
- **Ce qui manque** : le plancher de 151 est le maximum atteignable, sans marge, mesuré au commit candidat fabriqué
  (`f233bd80…`, jamais poussé). Un changement de `tests/test_t07bbis_*`, d'une aide ou de `src/` entre la mesure et le commit de la
  course ferait s'arrêter la machine à son étape 5, après l'installation des paquets (machine payée, course unique consommée).
  `commande` imprime la création sans aucune preuve que `essais-du-commit` a été joué **à ce commit** et **avec cette amorce**.
- **Preuve rejouable** : dans le clone jetable, `bash scripts/lancer_bbis_v6.sh essais-du-commit <clone> 081f8d99acec3396a01359586732d1ffdb4b9d40 <dossier neuf>`
  rend « 151 passed, 25 skipped », code 0, 516 fichiers, en 10 min 40 s (ma mesure, sortie gardée sous
  `…/cl-amorce-v6-gardes/mesure-tete/essais.txt`) : le plancher tient **aujourd'hui** à la tête ; rien n'oblige à le reprouver au
  commit qui sera passé. `grep -n "essais-du-commit" scripts/lancer_bbis_v6.sh` : la sous-commande n'est appelée par aucune autre.
- **Correction proposée** : sans code neuf, écrire au feu : sortie de `essais-du-commit` au commit exact de la course, dossier neuf,
  scellée (`sceller`) et citée par son empreinte, avec l'empreinte de l'amorce lue dans sa première ligne ; code autre que 0, ou
  commit autre que celui de la commande : arrêt. Par une version 7 : faire exiger par `commande` un fichier de mesure scellé qui
  nomme le même commit et la même empreinte d'amorce, ou jouer la mesure en ligne (une dizaine de minutes).

## MINEURS

1. **Garde « commit de la course » : le code de l'arbre peut être masqué selon le dossier courant.**
   `scripts/lancer_bbis_v6.sh:92` lance `"$PY" -c …` avec `PYTHONPATH="$1/src"`, sans `-P` ni `-I` : sous `-c`, le dossier courant
   passe avant `PYTHONPATH`. Lancé depuis `src/` du dépôt de la mère, c'est le code de la mère, non celui de l'arbre, qui rejouerait
   la garde d'entrée (l'en-tête promet « par le code même de cet arbre »). Correction : `-P` (Python ≥ 3.11) ou `-I` et
   `sys.path.insert(0, …)`. Par ailleurs l'essai lie `src/controle_ia` de l'arbre jouet au code du dépôt de travail
   (`tests/test_chaine_bbis_v6_v1.py:243`) : le « code de l'arbre » n'y est pas distinct de celui de la mère ; seule la preuve
   `garde-entree-candidat.txt` l'éprouve sur un arbre réel.
2. **Ordre des gardes dans `commande`** : `commit_joignable` (`:159`) interroge `origin` avant que `branche_de_sortie_neuve`
   (`:164`) ne vérifie que `origin` est bien le dépôt de l'amorce. Sans conséquence (les deux doivent passer), mais la première peut
   passer sur un mauvais dépôt ; la vérification du nom devrait venir d'abord.
3. **Cas non éprouvés de la garde « commit joignable »** : « tête distante absente du clone local » (`:103`) et « dépôt
   injoignable » (`:102`, sortie vide) n'ont pas d'artefact dans les essais ; l'un et l'autre refusent à la lecture du code (aucune
   valeur vide ne vaut accord : `case … ''` refuse).
4. **Copie du fichier d'histoire superficielle non contrôlée** (`:77`, `cp "$peu" …` sans code jugé) : en cas d'échec, la garde
   d'entrée refuserait plus loin (commit ancêtre introuvable) — repli vers le refus, non vers l'accord ; à faire juger quand même.
5. **Ligne d'empreinte de l'amorce** (`scripts/amorce_bbis_v6.sh:155`) : jouée avant le contrôle des outils (ligne 157, qui
   vérifie `sha256sum`) ; un échec y écrit une empreinte vide sans arrêt. C'est une trace, non une garde, et elle n'a ni cas sain
   ni artefact dans les essais ; à éprouver si M1 en fait une garde.
6. **Contrôle avancé de l'amorce moins sévère que la marche sur une ligne mal formée** : une ligne `CODE-BBIS` à cinq colonnes est
   ignorée par `fiche_sur_l_arbre` (filtre `len(c) == 4`, `:287`) et refusée par `lecture_v3.lire_lignes` (« en double ou mal
   formée »). Rejoué : contrôle avancé « code 0 », garde de la marche « code 2 ». Conforme à l'intention écrite (« jamais plus
   sévère que la marche ») et rattrapé avant la création par la garde « commit de la course » du lanceur ; à dire tel quel dans
   l'addendum (§ 4 point 6 le dit à peu près).
7. **Clé d'interface du conteneur** (`:138`) : une valeur d'espaces passe ; et un refus à cette ligne quitte avant la minuterie,
   laissant la machine arrêtée facturer son disque jusqu'au geste de la session (même conduite que le refus de l'identifiant,
   ligne 134, déjà en version 5). Le feu doit garder la règle « aucune ligne « minuterie lancée » au journal dans les premières
   minutes : destruction par identifiant ». Je n'ai pas pu vérifier que le loueur pose cette variable dans le mode de lancement
   `--entrypoint bash --args` de cette chaîne (d'autres chaînes du programme ont obtenu « HTTP 200 » à l'arrêt) : si elle manquait,
   cette garde arrêterait une course saine — sans dépense de carte, mais en consommant la création.
8. **Sous-commande `essais-du-commit`** : `COMMIT` n'est pas contrôlé (40 caractères hexadécimaux, comme l'amorce l'exige) et le
   dossier est créé avant le premier refus (`:173-174`), ce qui consomme son nom (R12) sur une faute de frappe (constaté en
   rejouant). Sans effet sur la course.
9. **Plafond de prix dans le code** (`:146-149`) : contraire à la lettre de GO-2026-11-18-03 (3) (« tenu hors du code »), mais
   déclaré à Lazar dans le brouillon (§ 1 et § 3) ; éprouvé sur six cas (1,40 accepté ; 1,41, absent, texte, 0, booléen refusés).
   Le plafond porte sur `dph_total` seul (clé `prix_usd_h`) ; le stockage reste borné à part (≤ 0,08 USD/h).
10. **Taille de l'amorce embarquée** : base64 de 41 436 caractères contre 32 720 pour la version 5 (+ 27 %). Aucune limite connue
    n'est atteinte (une seule chaîne de commande reste sous 128 Kio) ; jamais éprouvé chez le loueur à cette taille. Le
    `base64 -d … && bash …` de la commande n'exécute rien si le décodage échoue.
11. **Essais datés** : trois des douze essais sautent après l'échéance de la ligne de calcul (`avant_l_echeance`,
    `tests/test_chaine_bbis_v6_v1.py:286-287`) ; voulu, à savoir pour toute relecture après le 22 novembre.

## Bilan garde par garde (règle R5)

| garde | cas sain | artefact(s) | rejoué par moi | repli silencieux |
|---|---|---|---|---|
| plancher 151 (amorce, `:64`, `:332`) | 151 passés au commit candidat (preuve) et à la tête `081f8d99` (ma mesure) | 150 passés → refus ; essai en échec → refus (`essais-du-commit`, même bloc de compte lu dans l'amorce) | oui | aucun (`compte_passes` rend 0 sur une ligne illisible) |
| motifs d'extraction (`:176-213`) | les 63 fichiers de la fiche extraits, aucun interdit | motifs de la version 5 : les onze manquent | oui ; liste réelle de `scripts/` à la tête : exactement les 21 scripts attendus et leurs compagnons, rien d'autre | aucun ; aucun interdit levé (exclusions et refus de `docs/notes/` inchangés) |
| contrôle avancé de la fiche (`:267-316`) | 63 fichiers, empreintes conformes (arbre réel, ma mesure) | sept artefacts (lignes absentes, sans accord, fichier absent, empreinte autre, compagnon absent, trois fiches, registre absent) ; j'ai ajouté registre illisible (code 1, arrêt) | oui | aucun : une chute de Python rend un code non nul, donc l'arrêt ; moins sévère que la marche sur une ligne mal formée (mineur 6) |
| clé du conteneur avant la minuterie (`:138`) | valeur présente, jamais affichée | absente, vide | oui (par l'essai) | aucun ; espaces acceptés (mineur 7) |
| empreinte de l'amorce au journal (`:155`) | — | — | non éprouvée | trace seulement (mineur 5 ; majeur 1) |
| commit de la course (lanceur, `:62-97`, `:160-163`) | commande imprimée ; garde d'entrée de la marche passée à la tête `081f8d99` (ma mesure : 63 fichiers) | commit sans lignes d'inscription, fichier de la fiche changé, fichier hors des motifs ; la version 5 laissait passer les deux premiers | oui ; j'ai ajouté une ligne à cinq colonnes : refus | aucun : `except Exception` imprime et rend 2 ; `M=$(a) && M=$(b); c=$?` garde le premier échec |
| commit joignable (`:98-105`) | commit poussé | commit non poussé ; branche absente | oui | aucun (sortie vide ou multiple refusée) ; deux cas sans artefact (mineur 3) |
| sous-commande `essais-du-commit` (`:170-186`) | plancher franchi | manqué d'un essai ; essai en échec ; dossier déjà présent | oui | aucun ; non exigée par `commande` (majeur 2) |
| image par son nom (`:143`) | `python:3.11-bookworm` | `python:3.12-bookworm` | oui | aucun (nom seulement, non un condensé : déclaré) |
| plafond 1,40 USD/h (`:146-149`) | 1,40 | 1,41 ; absent ; texte ; 0 ; booléen | oui | aucun (`2>/dev/null` n'avale que la sortie d'erreur ; le code non nul refuse) |

**Ce que la version 5 arrêtait et que la version 6 n'arrête plus** : rien, hors le plancher abaissé de 176 à 151 — et 176 était
un faux arrêt certain (R-3160). La différence des deux amorces se borne aux six écarts déclarés (deux lignes retirées : l'ancien
plancher et le nom du lanceur dans un message) ; celle des deux lanceurs n'ôte aucune garde (seuls des noms de fichiers changent
dans les lignes retirées). Le compte simulé est fiable sur ce dispositif : la course du 16 novembre a fait sur la machine
« 115 passed, 24 skipped » (R-3006), égal au compte simulé de la version 3 (R-2923).

## LIMITES

- **Lu en entier** : les deux scripts version 6 et leurs différences avec la version 5 ; les essais ; le brouillon du troisième
  addendum ; les preuves de simulation (sorties, offre fabriquée, deux fabriques) ; `marche_v4.gardes_d_entree` et `entrees_locales`,
  `lecture_v3.lire_lignes` et ses constantes, `registre_bbis_v1` (`sceau_conforme`, `lire_fiche_code`, `exiger_ancetre`,
  `exiger_partage_sans_bbis`, `ajouter_ligne_propre`, `garde_depense`), la construction de l'offre de `registre_bbis_v2` ; le texte
  scellé, sections « Plan d'analyse » à « Calcul et dépense » ; la section SA-15 du second addendum ; le registre propre et le
  registre voisin des addenda ; `feu-bbis-v2.txt` (début), `go-bbis-v2.txt` (début) ; le rapport du portillon et pilote, la
  contre-lecture du projet de feu ; les lignes GO-2026-11-14-09, -18-03, -18-04, -18-05 ; R-3146, R-3160, R-3170, R-3006.
- **Non lus** : le projet de feu version 3 lui-même (seule sa contre-lecture) ; le premier addendum en entier ; la fiche
  `code-bbis-v1.json` ; l'épreuve de niveau ; GO-2026-11-18-03 n'a été lue que par sa ligne ; le reste de `registre_bbis_v2`
  (garde de création, relances).
- **Jamais ouvert** (cloisonnement) : rien sous `diag/`, `runs/` ou `donnees/` ; aucune branche de données ni de calcul ; aucune
  sortie de modèle. Je n'ai pas ouvert les journaux de répétition sous `docs/notes/g0-deux-semaines-v1/t07-module-v2/` que la
  recherche « HTTP 200 » faisait apparaître, par prudence. La configuration de 7b (fichiers qu'elle cite, recopiés à l'étape 3 de
  l'amorce) n'a pas été vue : la reproduction de l'arbre ne les porte pas, comme l'addendum le dit.
- **Non vérifiable ici** : la présence de la clé d'interface du conteneur dans ce mode de lancement (mineur 7) ; le comportement
  du loueur avec une commande de 41 Kio (mineur 10) ; la garde « commit joignable » contre le vrai dépôt distant (mes jeux, comme
  les essais, prennent un dépôt nu local pour `origin`).
- **Mes jeux** : `python -m pytest -q tests/test_chaine_bbis_v6_v1.py` : 12 passés (35 s) ; `essais-du-commit` à
  `081f8d99acec3396a01359586732d1ffdb4b9d40` : 151 passés, 25 sautés, code 0, 516 fichiers ; garde d'entrée de la marche et contrôle
  avancé de l'amorce sur cet arbre : code 0, 63 fichiers ; deux artefacts ajoutés (registre illisible ; ligne à cinq colonnes).
