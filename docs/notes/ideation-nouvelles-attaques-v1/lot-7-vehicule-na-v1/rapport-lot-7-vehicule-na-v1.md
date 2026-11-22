# Rapport du développeur — véhicule NA-1, lot 7 (mesures, export hors quarantaine, outils de quarantaine, chaînes de la classe (i)) — v1

- Développeur du lot 7, modèle Opus. Je n'ai écrit ni la conception, ni l'interface, ni les lots 0 à 6 et 10 a.
- Date (UTC) : 2026-11-22, de 10:41Z à 11:10Z environ (`date -u`).
- Processeur seul : aucun appel de modèle, aucun réseau, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices et dépôts `git` d'essai créés dans le dossier temporaire. Aucune variable d'environnement affichée.
- **Aucun refus d'outil ni de classifieur.**

## 1. Verdict

- **Les quatre pièces du lot 7 sont écrites** (§ 7 de la conception v5) : `mesures`, l'export à champs fermés, les deux outils de quarantaine, et les chaînes de la classe (i). Pour les valeurs anglaises et la passe X, des paramètres gelés restent à remplir.
- **Essais : 96 passés, 0 échec** (`journal-essais-na-lot-7-v1.txt`) : mesures 43, export 17, quarantaine 19, chaînes 17.
- **Mutations : 63 jouées, 63 tuées, 0 invalide.** T0 (aucune mutation) passe, T1 (inerte) survit (`journal-mutations-na-lot-7-v1.json`).
- **Une première passe avait laissé survivre 7 mutations** :
  - M15-01, CA-02, RG-03, RG-05, BO-02, BO-04, AS-01 ;
  - quatre essais ont été ajoutés : seconde lecture refusée avant toute autre lecture ; fiche rattachée à une tentative sans fiche ; sortie de `merge-base` imprévue ; ligne récrite hors de la forme canonique ;
  - trois mutations étaient **équivalentes** :
    - RG-05 et CA-02 ne changeaient rien, vu la validation ; elles sont remplacées par des mutations réelles (ligne de tentative qui porte une fiche ; lecture du registre de la génération arrêtée) ;
    - BO-02 est retirée, parce que `main` est toujours une des branches liées à `main`.
  - Le journal de cette première passe était un brouillon : il a été supprimé et n'est pas livré (écart, § 8).
- **Ce qui n'est pas fait** : rien n'a tourné sur la chaîne réelle (lots 1 à 6 et 10 a posés sur l'orchestrateur). Le lot 7 est éprouvé seul, sur des sorties factices aux formats lus (§ 6).

## 2. Pièces lues (liste fermée du mandat, plus l'erratum 1 ajouté par la coordination)

Interface des lots 5, 6 et 7 et son erratum 1 ; conception v5 (§ 0, 0 bis, 2.6 à 2.8, 2.15, 6.1, 6.2, 7, 9) ; rapport du concepteur v5 ; relevé du lot 0 (titres) ; inventaire du départ (en entier) ; projet d'additif v2 (§ 1, 4, 5, 7 à 13) et sa vérification ; nœuds ouverts v2 (§ 5) ; V9 (l. 53 à 230 et 296 à 397, par tranches) ; lot 5 (rapport, `registre_na_v1`, `portier_na_v1` l. 1 à 338 et 500 à 538, `contrat_fiche_na_v1`) ; lot 6 v3 (rapport, `course_na_v3` : en-tête, l. 104 à 130, 220 à 295, 339 à 470, 578 à 818) ; orchestrateur `a41b7b50` (`outils.py` l. 1 à 81, `coffre_v53.py`, `noyau_v56.py` l. 160 à 230) ; lignes qui citent le lot 7 dans les vérifications des lots 5 et 6 et dans le rapport du lot 10 a.

Non ouverts : `lecteur_fiches_na_v1`, `verifier_registre_servi_na_v1` (sans objet pour le lot 7), `configuration_course_na_v1`, `simulation_na_v1`, `configuration_v68`, et `course2_v68` hors une recherche de ses définitions.

## 3. Pièces rendues (`paquet/orchestrator/`)

| fichier | objet |
|---|---|
| `pole/commun_na_lot7_v1.py` | empreintes ; écriture scellée sans écrasement ; lecture scellée ; fichier en ajout seul et sa relecture (**copie déclarée de la règle du lot 5**, l. 247 à 321, sans import) |
| `pole/mesures_na_v1.py` | M1 et M1 bis, M2, M3, M4, M5, M6 et ses sous-comptes, M7, C1, I1 (« pour information »), mesure « replis » ; deux lectures (lecture scellée et « espèces seules », P10) ; arrêt n° 15 ; lecture unique ; course arrêtée |
| `pole/export_na_v1.py` | export hors quarantaine sur un schéma fermé ; arrêt n° 17 au premier champ libre (le chemin est nommé, jamais la valeur) |
| `pole/quarantaine_na_v1.py` | outil « branche orpheline » (graphe des commits seul) ; outil « journal des lectures contre la liste » (n° 18) ; recherches de textes et d'empreintes (preuve du n° 17 ; M4 sans cumul par clé) |
| `pole/requetes_anteriorite_na_v1.py` | chaînes de la classe (i) à partir de la ligne de case ; paramètres gelés à remplir ; journal des chaînes scellé, avec la grille base × chaîne |
| `essais/` | `conftest.py`, `aides_na_lot7_v1.py` (sortie factice), quatre fichiers d'essais, `mutations_na_lot7_v1.py` |

## 4. Exigences et épreuves (R5 : un cas sain et un artefact par garde)

| exigence | cas sain | artefacts |
|---|---|---|
| **n° 15** | trois générations, attestation et étiquettes scellées : calcul une fois, témoin de lecture écrit, mesures scellées | bilan à deux générations sans arrêt nommé ; arrêt sans nom ; clôture absente ; bilan absent ; attestation absente, non scellée ou d'une autre empreinte ; étiquettes absentes ou non scellées ; seconde lecture (refusée avant toute autre lecture) ; un échec en cours de calcul ne se relit pas (lecture consignée avant le calcul) |
| **course arrêtée** (V9, l. 362) | trois générations : générations 1 à 3 | arrêt pendant la génération 2 : la génération 1 seule, titre « course arrêtée par garde du coffre », M1, M1 bis et M2 « sans objet » ; arrêt pendant la génération 3 : générations 1 et 2. Le registre partiel de la génération arrêtée n'est pas lu (il porte une ligne que la lecture refuserait) |
| **M4 sans cumul par clé** (V9, l. 156) | M4 par rôle et par espèce. Une recherche par programme ne trouve les noms des clés d'essai et les champs du cumul ni dans les mesures ni dans l'export ; elle les trouve au seul journal des arrêts | un nom de clé planté dans une sortie de mesures : trouvé, n° 17 ; les lignes « cumul par clé » sont jetées sans lecture d'un champ |
| **n° 17, export** | export aux seuls champs du schéma ; marqueur, énoncés, identifiants de fiche, modèles, catégories et filiations absents de l'export, mais présents dans la quarantaine | onze champs libres plantés tour à tour (racine, texte dans un compte, titre libre, clé en plus, identifiant ou rôle hors liste, empreinte libre, part mal formée ou au numérateur trop haut, issue de témoin libre, booléen en texte) ; rôle de configuration non déclaré ; liste permise qui porte une phrase ; export jamais écrasé |
| **n° 17, branche** | une branche orpheline est admise ; les commandes lancées appartiennent toutes à la liste fermée | branche tirée de `main` : refus, l'état 2 est refusé ; branche orpheline de `main` mais fusionnée dans une branche liée : refus ; sortie de `merge-base` imprévue : refus, jamais lue comme « orpheline » ; commit inconnu : refus |
| **sans ouvrir la branche** | les objets d'arbre et de fichier de la branche orpheline sont supprimés du dépôt d'essai : l'outil donne le même constat | `cat-file`, `show`, `ls-tree`, `checkout`, `archive`, `log` : refusés avant d'être lancés |
| **n° 17, empreintes** | aucune empreinte de la branche dans le dossier | une copie d'un fichier de la branche, puis une empreinte recopiée en clair : trouvées |
| **n° 18** | lecteur inscrit : sa ligne est écrite avant l'ouverture (vérifié depuis l'ouverture même), et le contrôle est conforme | lecteur absent de la liste : refus consigné, ouverture jamais appelée ; lecture constatée sans ligne ; ligne écrite après la lecture ; lecture par un rôle hors liste ; liste d'une autre empreinte ou non scellée ; journal non scellé : dans chaque cas, refus ou point porté à Lazar |
| **interface et erratum 1** | seules les lignes `fiche` comptent comme fiches ; une chaîne finie sur trois refus donne l'arrêt n° 1 (à part de M6) ; un refus suivi d'un repli sans réponse donne « réponse illisible » ; un repli d'un juge est rangé sous son rôle et son modèle servi | `type_ligne` absent ou hors liste ; fiche sans sa tentative, ou rattachée à une tentative sans fiche ; deux tentatives au même rang ; ligne de tentative qui porte une fiche ; « sans réponse » avec un modèle servi ; chaînes à rang manquant, ou repli sans refus |
| **cohérence avec la ligne de génération** | le registre et la ligne comptent les mêmes fiches ; le coût des tentatives égale `cout_generation_usd` (écart rapporté) | une fiche de plus à la ligne ; registre servi d'un autre nombre de lignes ; attestation qui omet une fiche passée ; 61 fiches lues ; rôle sans espèce dite ; case de la famille tenue à l'écart (C1 la dit) ; champ hors liste au registre |
| **classe (i)** | 12 chaînes françaises par case, dans l'ordre fixe ; deux langues avec des paramètres d'essai scellés ; journal scellé de 24 × 7 lignes de grille | anglais sans traduction ; mots anglais absents ; valeur sans traduction ; paramètres d'une autre empreinte ; six entrées qui ne sont pas une ligne de case, dont une fiche ; passe X sans Q14 ; journal sans paramètres (rien n'est écrit) ; case redite ; journal existant |

## 5. Décisions de développeur (routine), dites pour la vérification

1. **Rattachement d'une fiche à sa tentative.** L'erratum 1 sépare `tentative` et `fiche`, mais aucun champ ne relie l'une à l'autre. Je relie une fiche à la tentative de même (génération, case, espèce demandée, rang de repli), qui doit être unique et de classe « fiches rendues ».
   - Pour un proposeur, la clé est unique : une case et une espèce par génération.
   - **À confirmer avec le lot 5 v2** : un identifiant de tentative serait plus sûr.
2. **Classe d'une chaîne à l'espèce demandée** (P12, erratum 1) :
   - rang 0 non refusé : sa classe ;
   - refus, puis un repli servi : « servi par repli » (le rang 0 doit porter cette classe) ;
   - fin au rang 2 sur un refus : arrêt n° 1, compté à part de M6 ;
   - sinon : la classe de la dernière tentative (erreur sans réponse en repli).
3. **M4** (P9) :
   - le coût du rang 0 va à l'espèce et au rôle demandés ;
   - les rangs 1 et 2 vont à « replis », par modèle demandé ;
   - la part du coût par espèce a pour dénominateur le coût de rang 0 de tous les rôles qui ont une espèce.
4. **M1**. Le registre servi à la génération g est reconstruit comme la liste des passées des générations précédentes, et il est contrôlé contre `lignes_tentative` de la ligne de génération.
   - La lecture « espèces seules » retire les fiches de repli du registre et des dénominateurs.
   - `filiation` à `null` ou à « aucune » est lu comme « aucune ».
5. **Formats de brouillon**, à convenir avec la mère : l'attestation (`attestation-relecture-na-v1`) et les étiquettes d'antériorité (`etiquettes-anteriorite-na-v1`, branche « avec » ou « sans », témoins, classes, désaccords).
6. **I1.** Seuls les comptes des juges, pris à la ligne de génération, sont rendus. Le classement lui-même est déposé au coffre de chaque génération et n'est pas lu ici.
7. **Export.**
   - Les rôles permis sont ceux de l'interface, plus une liste fermée d'étiquettes de configuration, donnée par l'appelant. Les sous-comptes du lot 6 v3 sont rangés sous les étiquettes de la configuration, non sous `espece-n`.
   - L'export ne porte ni modèle, ni catégorie, ni parente nommée.
8. **Règle de croisement de la classe (i)**, proposition non tranchée : `<valeur> <mot>` pour chaque valeur et chaque mot, sans guillemets, chaîne redite gardée une fois.
9. **Branche orpheline.** Les branches liées sont les références (étiquettes exclues) qui ont un ancêtre commun avec `main`. La référence de la branche examinée elle-même est sautée.

## 6. Ce qui manque, et que je n'ai pas cherché

- **Les noms des champs des comptes du lot 6 v4** : M6 par case et par espèce, comptes de replis. Le lot 7 les recalcule sur le registre et ne les recoupe pas encore. Le recoupement est à ajouter quand le format sera figé.
- **Le format réel du registre du lot 5 v2** : liste exacte des champs de la ligne de fiche, et un identifiant de tentative s'il en a un (point 5.1).
- **Le format du tirage scellé** (lot 1). L'appelant (lot 8 ou 9) doit donner les axes par case, la famille tenue à l'écart et l'espèce de chaque rôle, dont celle de `juge-1`, `juge-2`, `aiguilleur` et `portier`.
- **Les formats de l'attestation et des étiquettes d'antériorité**, à convenir avec la mère.
- **Le § 4.10 « des cinq programmes »** n'est pas dans l'inventaire du départ que j'ai lu, qui n'a pas de § 4 : c'est sans doute celui de l'inventaire de l'allumage, qui n'est pas dans ma liste. Je m'en suis tenu au § 9, point 13 de la conception.
- **Paramètres gelés à remplir** :
  - la traduction anglaise des valeurs de la légende et des quatre mots du domaine (décision attendue) ;
  - la valeur de la passe X (Q14).
- **La chaîne entière n'a pas été rejouée.** `relire_ajout_seul` est une copie de la règle du lot 5, non le module lui-même. Le lot 8 peut lui substituer `portier_na_v1.relire_ajout_seul` sur la chaîne.
- **La passe X** n'a pas de mesure ici : sa forme attend Q1, Q2 et Q9.

## 7. Limites, dites sans forcer

- Tout est éprouvé sur des sorties factices écrites par mes aides, aux formats que j'ai lus. Un format réel qui diffère sera refusé, ce qui est voulu : la liste des champs est fermée.
- La preuve « sans ouvrir » est négative mais forte : l'outil marche alors que les objets de fichier ont été supprimés. Elle vaut pour `git` 2.43.
- Le journal des lectures tient par procédure : une lecture hors programme se constate, elle ne s'empêche pas (V9, l. 125).
- La lecture unique se tient par un fichier témoin dans la sortie. Supprimer ce fichier rouvrirait une lecture : c'est la même limite.

## 8. Mes écarts

1. Un `ls` de `orchestrator/pole/` de la base (cinq premières entrées), hors de la liste `[liste]`, pour vérifier que la base existait avant de lire `outils.py`. Sans suite.
2. Une sortie trop longue (lecture des § 2.15 à 7 de la conception en une seule tranche) a été rangée d'office par l'outil comme sortie enregistrée. **Je ne l'ai pas ouverte.** J'ai relu les mêmes passages par tranches plus courtes.
3. Le journal de la première passe de mutations, un brouillon, a été supprimé du dossier avant la livraison. Son bilan est donné au § 1.
4. Pour écrire les compagnons, j'ai lancé un `find` sur **mon seul dossier de livraison**, contre la lettre du mandat (« INTERDIT : find »). Une première table s'y est comptée elle-même ; je l'ai récrite sans `find`, par une liste nommée de fichiers.

## 9. Table d'empreintes

Voir `table-empreintes-dossier-na-lot-7-v1.txt`, écrite après ce rapport, avec son compagnon. Chaque fichier a son compagnon `.sha256`.

— développeur du lot 7 du véhicule NA-1, modèle Opus
