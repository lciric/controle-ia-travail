# Rapport du développeur — code de l'étage sur processeur du palier 0b, version 6 (après l'audit des trous du code v5)

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C) rendant une pièce d'instrument (classe B, le code v6), à vérifier par un autre modèle (S). Rien n'est scellé au sens du dépôt ; rien n'est versé ; le texte en vigueur reste la version 13 scellée.

- Auteur : développeur, modèle O (neuf : il n'a écrit ni le texte, ni le code v1 à v5, ni leurs vérifications, ni l'audit). Travail du 2026-11-20 (`date -u` : 15:12Z en cours de travail ; 16:48Z au scellement des compagnons de ce dossier).
- Mandat : `P0B/mandat-developpeur-code-palier-0b-v6-v1.md` (`46a5e1a4d9d3d8cd939640a3cc870be8816b5b0ab5e86af418336ce4f2862625`), empreinte vérifiée par `sha256sum` sur ce seul chemin avant tout geste. `P0B` = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Pièces qui font foi, chacune vérifiée par `sha256sum` et contre son compagnon (empreinte égale à celle du mandat, compagnon d'une ligne au nom de base) : texte en vigueur v13 (`d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959`) ; audit des trous (`8e965f80dbee74987f91eab7b3cc0a56ef2af55a2bbdee781c557fe893a56389`) ; lecture pour le lancement (`301d8932344187a157df987c44a1ae67c3cebad8acdf4c003a2e91b2688110e6`) ; rapport du code v5 (`a2966a3c53382881264773033f793f600dfbab0229d3a00827b7a33522ba6016`) ; table du code v5 (`56bddae73a01d52fba363b263184aae4c3ffce8aaf654df07de2c9d67be1a15a`) ; vérification du code v5 (`0e2c46bb2c9ac811da982ce8bf3f16e41adda9b56612862295d23bbf2ebc7999`). Tous « égaux ».
- Lu : le mandat ; l'audit en entier ; la lecture pour le lancement en entier ; la vérification du code v5 en entier ; du rapport du code v5, les § 0 à 9 ; de la v13 : l'en-tête et la ligne du commit, les sections « Prédiction », « Métrique », « Seuil » (valeurs gelées, six critères, S7 à S9), B5 à B9, les huit points, l'ordre des opérations, « Ce qui est rapporté », les critères de lecture, la liste d'arrêt, l'annexe C, et, de l'annexe H, « Version 9 » (fin) et « Version 12 ». Le reste de la v13 n'a pas été lu en entier.
- Point de départ : `P0B/code-v5/` du dépôt, vérifié contre la table des 58 empreintes (`env -C <copie> sha256sum --quiet -c P0B/table-empreintes-code-v5.txt` : aucun échec, 58 lignes), copié deux fois dans le bloc-notes : `dev-palier-0b-v6/code-v5/` (gardé intact, pour les différentiels et les sorties) et `dev-palier-0b-v6/code-v6/` (copie de travail, d'où le rapport v5 et son compagnon ont été retirés). Code de l'organisme : copie de `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` dans le bloc-notes (garde 17), non modifiée.
- Environnement : Python 3.13.18 (`/home/user/controle-ia-travail/.venv`), numpy du `.venv` ; quatre processeurs, partagés.

## 0. Verdict

Les sept points de « Ce que le code v6 doit porter » (audit, § 2) sont faits. **Chaque fichier d'essais lancé seul : dix fichiers, 117 passés, 0 échoué. Suite entière : 117 passés, 0 échoué (1 290 s).** **L'essai final « aucune graine décisive » passe.** **Banc `mutations_v5.py` (147 défauts : les 113 du banc v4, repris à l'identique, et 34 neufs), rejoué en entier : 147 appliqués, 147 vus, chacun par un essai en échec de code 1 ; témoins au vert.** Sorties : 526 empreintes sur 531 égales à l'octet entre le code v5 et le code v6 ; les 5 qui changent et les 6 neuves relèvent toutes du point 4 (reliquat ajouté aux sorties scellées, mode inscrit dans la description de la case) ou du point 3 (configuration du manifeste) ; **la liste des étiquettes de graines d'un lancement au mode « tirages » est égale à l'octet** (aucune graine existante ne change). Le verrou (a) à (e) et la garde 27 sont inchangés (aucune ligne de `graines.Autorisation`, des fonctions du verrou, de `exiger_autorisation_pour`, de `ecrire_manifeste`, `verifier_manifeste`, `mecanique.py`, `mondes.py` ne change). Dix-neuf silences déclarés (§ 2), chacun avec une proposition marquée, aucun tranché ; trois remarques (§ 8) ; aucun refus de permission, de classifieur ni de garde. Aucun programme de lancement décisif n'a été joué ; le programme écrit à part (`outils-dev/lancer_etapes_8_et_9_v1.py`, « non lancé, en attente ») n'a été exécuté que sur une racine factice, où le verrou l'a refusé avant toute dérivation.

## 1. Ce qui a été fait, point par point (audit, § 2, « Ce que le code v6 doit porter »)

### Point 1 — les cases « sources » tirées sous la couche « decisif », avec un champ de mode (`graines.py`, `tirages.py`)

- `graines.ORDRE_DES_CHAMPS` reçoit le champ `mode`, inséré après `repere`. Une étiquette ne porte que les champs qu'on lui donne, dans l'ordre gelé : **toute étiquette sans le champ `mode` est celle du code v5, à l'octet ; aucune graine existante ne change.** Le champ n'est écrit qu'au mode « sources » (`mode=sources`), jamais au mode « tirages ».
- `tirages.mode_de(case)` : le mode d'une case et son nombre — exactement une des clés `tirages` et `sources`, entier positif (ni booléen, ni flottant) ; arrêt nommé sinon.
- `tirages.champs_de_la_case` : ajoute `mode="sources"` aux cases qui portent la clé `sources`.
- `tirages.simuler_case_sources(graines, couche, case, f, sources, lot=LOT_DE_SOURCES)` : le mode « sources ». Les `sources` sources sont simulées par lots de 2 000 (`LOT_DE_SOURCES`, la valeur du lot vectorisé de l'annexe F, déjà employée par l'étalonnage et le mode « tirages » ; 200 000 = 100 lots), chaque lot sous son étiquette (`…|mode=sources|lot=k|bras=b|role=…`, rôles `echantillonnage` ou `echantillonnage-repli`, `monde`, `source`, comme au mode « tirages ») ; **la source étrangère d'une source (famille H, bras 4a et 4b) est la suivante du même lot, la première pour la dernière** (`statistique.simuler` sans `taille_tirage` : l'anneau est le lot) ; un lot d'une seule source, pour une case qui a les bras 4a ou 4b, arrête (dans `verifier_cases`, avant tout tirage, et de nouveau dans cette fonction). Rend, par bras et par source : M1, D, I, lois fausses tenues, reliquat ; et, aux cases du repli (famille D), les sorties du registre de la course source (point 4).
- `tirages.jouer_case_sources` : simule et écrit une case du mode « sources » ; aucune lecture par tirage, aucun taux (les écarts se calculent au programme d'analyse).
- Les couches « decisif » et « confirmation » restent refusées sans autorisation, au mode « sources » comme au mode « tirages » (la première dérivation lève, et `lancer_famille` revérifie l'autorisation avant tout lancement).

### Point 2 — le mode dans le nom des cases (`tirages.py`)

- `nom_de_case` : le nom d'une case du mode « sources » finit par `-sources` ; celui d'une case du mode « tirages » est celui du code v5 (`D-lecteur-heritage-dose0.5-taux0.25-taille1.0-repli` et `D-lecteur-heritage-dose0.5-taux0.25-taille1.0-repli-sources`). Deux cases qui ne diffèrent que par le mode ont deux dossiers.
- Deux cases au même nom font un arrêt nommé (`ArretTirages`, « deux cases au même nom ») **avant** toute autorisation, toute dérivation et toute création de dossier (`verifier_cases`), au lieu de l'erreur `FileExistsError` du code v5 au milieu du lancement.

### Point 3 — `lancer_famille` suit la clé de chaque case, toutes les familles en un seul appel, un seul manifeste (`tirages.py`)

- Nouvelle signature : `lancer_famille(graines, couche, cases, f_par_case, dossier, commit, fichiers_geles, cases_non_atteignables=None, en_plus=None)`. **Le nombre commun `tirages` du code v5 est retiré** : chaque case est tirée au nombre que porte sa clé (`tirages` : tirages emboîtés, simulés au plus grand nombre de sa grille ; `sources` : mode « sources »).
- `verifier_cases(couche, cases)`, appelée en tête de `lancer_famille`, avant `exiger_autorisation_pour` et avant toute dérivation : une clé et une seule par case (`mode_de`) ; aucun nom double ; sous la couche « decisif », la taille gelée du mode (10 000 tirages emboîtés ; 200 000 sources) et aucune lecture partielle (`nombres_lus` refusé) ; sous la couche « confirmation », les seules cases de C1 (famille A, sourd à appels égaux) et de C4 (famille C, les deux sourds), au mode « tirages », à 100 000 tirages, avec leurs nombres lus ; des nombres lus toujours dans la grille de la case ; aucun lot d'une seule source au bras 4a ou 4b ; aucun lancement vide. Arrêt nommé sinon, rien n'étant créé ni dérivé.
- Toutes les cases d'un appel, des deux modes, sont tirées dans cet appel et inscrites à **un seul manifeste** (`manifeste.json` du dossier), dont la configuration porte : `couche`, `cases` (noms triés), `tirages_par_case` et `sources_par_case` (le nombre de chaque case), et, s'ils sont donnés, `cases_non_atteignables` (étape 8) et les champs `en_plus` (étape 9). Le reste du manifeste (empreinte de la configuration, versions, racine, étiquettes et leur fichier, commit, fichiers gelés, champs du verrou) est celui du code v5.
- Une case de tirages qui porte `nombres_lus` est simulée entière (le plus grand nombre de sa grille) et lue à ces seuls nombres (`jouer_case`, paramètre neuf `sources_par_tirage`) : c'est le tirage de confirmation (point 6).

### Point 4 — reliquat par bras, part des entrées gardées, facteur d'enrichissement (`tirages.py`)

- `TYPES_DES_SORTIES` : par bras, M1, D, I et lois fausses tenues en entiers de 16 bits (comme au code v5, octets inchangés) et **le reliquat de budget en flottant de 64 bits** (`reliquat-bras-<b>.npy`), aux deux modes : forme (tirages, sources) au mode « tirages », (sources,) au mode « sources ». Le reliquat est celui que rend `statistique.jouer_bras` : en USD simulés, la somme, sur les quatre générations du bras (trois d'évolution et la génération finale), du budget moins le coût prévu des appels gardés ; nul par construction sous la règle de retrait de la version 1 (`statistique._appels`). Une sortie de bras inconnue arrête l'écriture.
- `sorties_du_registre_source(src)` **appelle `statistique.enrichissement`** et écrit, aux cases du repli au mode « sources » (famille D ; S7, M7, « sur 200 000 sources par dose »), source par source, sous les noms `source-<champ>.npy` : les comptes du registre de la course source (entrées, entrées gardées, entrées qui engagent une loi vraie, et gardées ; lois vraies, fausses et non plantées engagées, et gardées ; entiers de 64 bits) et ce que rend `enrichissement` — `part_des_entrees_gardees`, `facteur_entrees`, `facteur_paires` (flottants de 64 bits ; NaN quand un dénominateur est nul, comme la fonction le rend).
- La description scellée de chaque case (`case.json`) porte en plus `mode` et `sources_par_tirage` (mode « tirages ») ou `lot_de_sources` (mode « sources »).
- L'inventaire de « Ce qui est rapporté » (T:393) contre les sorties, ligne à ligne, est au § 6.

### Point 5 — `etape_8` (`etapes.py`, `etalonnage.py`)

- `etalonnage.lire_reglages_geles(chemin, sha_attendue)` (neuve ; la réserve mineure de l'audit, (d)) : le fichier et son compagnon existent sur disque ; le compagnon porte une seule ligne « <empreinte>  <nom de base> » ; l'empreinte recalculée, celle du compagnon et l'empreinte attendue sont égales ; puis la garde 22 est rejouée sur les lignes (`verifier_sortie`). Arrêt (`ArretEtalonnage`) sinon.
- `etapes.relire_fichiers_geles` : contrôle sur disque des deux fichiers et de leurs compagnons (règle R11, arrêt nommé), puis `frequences.lire_gelees` (inchangée) et `etalonnage.lire_reglages_geles` ; rend les fréquences, les lignes des réglages et les empreintes vérifiées à inscrire.
- `etapes.etape_8(graines, dossier, commit, chemin_frequences, sha_frequences, chemin_reglages, sha_reglages, couche="decisif", tailles=None)` : relit les fichiers gelés, construit `plan_des_cases(reglages_pour_le_plan(lignes))`, puis tire **toutes les cases du plan, des deux modes, en un seul appel de `lancer_famille`**, sous la couche « decisif » et un seul manifeste, qui inscrit `fichiers_geles = {"frequences": <empreinte vérifiée>, "reglages": <empreinte vérifiée>}` et les cases « non atteignables » (`cases_non_atteignables`). Aucune case n'est lue. `couche` et `tailles` ne servent qu'aux essais (couche « essai », tailles réduites, `reduire`) ; sous les couches décisives, `lancer_famille` refuse toute taille autre que gelée.

### Point 6 — `etape_9` (`etapes.py`)

- `lire_manifeste(dossier)` : le manifeste de l'étape 8 après `tirages.verifier_manifeste` (sceau, liste des étiquettes, champs du verrou).
- `comptes_de_niveau(dossier_8, manifeste)` : toutes les cases que le manifeste nomme sont contrôlées d'abord (description scellée ; aucun dossier de case hors du manifeste, aucun nommé et absent) ; puis chaque case de la famille A et de la famille C des deux sourds est relue par `analyse.lire_case` (empreintes vérifiées) et comptée par `analyse.taux_par_nombre` : `lecture-rejette` pour C1, `lecture-declenche` pour C4 ; clés de `cases_de_niveau` ; des comptes incomplets (moins de 72 cases pour l'un des critères, ou d'autres clés) arrêtent.
- `cases_a_confirmer` (code v4, inchangée) : les triplets de plus de 500 rejets.
- `cases_de_confirmation(a_confirmer, descs, tirages=TIRAGES_CONFIRMATION)` : chaque triplet désigne une case de l'étape 8 (famille A à cette dose et ce taux ; famille C de ce sourd à ce taux) ; la case est retirée **une fois, entière** (48 ou 16 sources par tirage), à 100 000 tirages emboîtés, et lue aux seuls nombres retirés (`nombres_lus`) ; plusieurs nombres d'une même case se lisent dans les mêmes tirages ; la configuration doit être celle de la case de l'étape 8.
- `etape_9(graines, dossier_8, dossier, commit, chemin_frequences, sha_frequences, chemin_reglages, sha_reglages, couche="confirmation", tirages=TIRAGES_CONFIRMATION)` : manifeste de l'étape 8 vérifié et de la couche « decisif » ; fichiers gelés présentés relus, contrôlés, et égaux à ceux que ce manifeste inscrit ; comptes ; cases à confirmer ; **rien n'est écrit s'il n'y en a aucune** ; sinon, un seul appel de `lancer_famille` sous la couche « confirmation », dans un dossier neuf et un manifeste à part, qui inscrit les triplets (`a_confirmer`) et l'empreinte du manifeste de l'étape 8 ; ensuite seulement, ces sorties scellées, leurs comptes sont relus et le statut de chaque case est calculé par `statuts_de_confirmation` (`analyse.statut_case_de_niveau`, soit `intervalles.regle_de_confirmation` : « en échec » à 5 236 rejets sur 100 000 ou plus, « tenue » sinon). Les statuts sont rendus, non écrits : la table des critères reste au programme d'analyse (étape 10).

### Point 7 — essais, banc, docstring

- Le docstring d'`etapes.py` est corrigé : il ne promet plus deux fonctions absentes ; il dit `cases_a_confirmer` (code v4), `etape_8` et `etape_9` (code v6) et ce qu'elles font.
- Fichier d'essais neuf, `tests/test_heritage_etage_processeur_v1_lancement.py` (dix essais, chacun cas sain et artefacts, règle R5), dont l'essai de forme du plan entier, réduit (`test_point_5_etape_8_plan_entier_reduit` : les 88 cases (60 au mode « tirages », 28 au mode « sources ») d'un plan dont une cible est non atteignable, couche « essai », deux tirages par case de tirages, 24 sources par case « sources ») ; trois essais du code v5 adaptés à la signature neuve de `lancer_famille` (§ 3).
- Banc `outils-dev/mutations_v5.py` : les 113 défauts du banc v4, repris à l'identique, et 34 neufs (§ 4) ; rejoué en entier.
- L'essai final « aucune graine décisive » passe (§ 3). Le verrou (a) à (e) et la garde 27 sont inchangés (§ 0).

## 2. Silences du texte, déclarés (rien n'est tranché ; chacun porte une proposition marquée, à inscrire ou à corriger par l'erratum v14)

1. **Le champ de mode des étiquettes.** Nom `mode`, valeur `sources`, place : après `repere` dans `ORDRE_DES_CHAMPS` ; jamais écrit au mode « tirages ». *Proposition* : B8, liste des champs d'étiquette, « mode (« sources », pour les seules cases du mode « sources » ; absent des autres, dont les étiquettes ne changent pas) ». Éprouvé : l'ordre privé de `mode` est celui du code v5 ; les étiquettes d'un lancement au mode « tirages » sont celles du code v5 (essai `point_1` ; sortie `tirages/liste_des_etiquettes` égale à l'octet, § 5).
2. **Les lots du mode « sources ».** Lots de 2 000 sources (`LOT_DE_SOURCES`, la valeur de l'annexe F), chacun sous l'étiquette `lot=k` ; 200 000 sources font 100 lots ; un dernier lot plus court si le nombre n'est pas multiple de 2 000 (jamais aux tailles gelées). *Proposition* : inscrire ces lots à B8 (« par lots de 2 000 sources, chaque lot sous son étiquette »).
3. **La source étrangère de H au mode « sources ».** « La source suivante du même tirage » (B7 bis) se lit « la suivante du même lot, la première pour la dernière ». Raison : 200 000 n'est pas multiple de 48 (le plus grand nombre de la grille de H), et un anneau de 48 laisserait un reste ; en loi, chaque source a pour étrangère une source indépendante, de même dose, autre qu'elle, comme dans un tirage. Un lot d'une seule source, aux bras 4a et 4b, arrête. *Proposition* : B7 bis, « au mode « sources », le lot tient lieu de tirage ».
4. **La forme du reliquat.** Par bras et par source (et par tirage au mode « tirages »), en USD simulés, flottant de 64 bits : la somme, sur les quatre générations du bras — trois d'évolution et la génération finale, où des appels sont faits sans écriture —, du budget moins le coût prévu des appels gardés, tel que `statistique.jouer_bras` le rend ; nul par construction sous la règle de retrait de la version 1 (famille E, règle « v1 ») ; la course source, qui n'est pas un bras, n'a pas de reliquat écrit. Écrit pour toutes les cases, des deux modes. *Proposition* : « Ce qui est rapporté », « le reliquat de budget par bras » se lit ainsi ; s'il ne doit porter que sur les générations d'évolution, c'est au texte de le dire, et le code se change.
5. **Les sorties du registre de la course source (famille D).** Écrites seulement aux cases du repli au mode « sources » (S7 : « sur 200 000 sources par dose ») ; ni au mode « tirages » du repli, ni aux autres familles. Dix comptes par source (entiers) et les trois valeurs de `statistique.enrichissement` (flottants, NaN si un dénominateur est nul), par source. Agréger sur les sources (moyenne des rapports, ou rapport des sommes) n'est pas tranché : les comptes bruts permettent l'un et l'autre au programme d'analyse. *Proposition* : inscrire la liste des sorties (§ 1, point 4) et laisser l'agrégation au préenregistrement de l'analyse, ou la fixer à l'erratum.
6. **Aucune lecture au mode « sources ».** Les cases « sources » n'écrivent aucun fichier `lecture-*` ; leur description porte `grille: []`, `mode`, `lot_de_sources`. Les écarts (M7, M8, M10 du point 6, M14) se calculent au programme d'analyse.
7. **Le nom des dossiers.** Suffixe `-sources` pour le mode « sources » ; nom du code v5 pour le mode « tirages ». Deux cases au même nom arrêtent avant tout tirage.
8. **Un manifeste pour l'étape 8, un pour l'étape 9.** Chacun dans son dossier, neuf ; la configuration porte `couche`, `cases`, `tirages_par_case`, `sources_par_case`, et `cases_non_atteignables` (étape 8) ou `a_confirmer` et `manifeste_de_l_etape_8_sha256` (étape 9) ; `fichiers_geles` vaut `{"frequences": <empreinte vérifiée>, "reglages": <empreinte vérifiée>}` aux deux. *Proposition* : B8, « Un manifeste par run », se lit « un pour l'étape 8, un pour l'étape 9 s'il y a des cases à confirmer ».
9. **Les contrôles d'un lancement (`verifier_cases`).** Règles neuves du code, non écrites au texte : sous « decisif », tailles gelées seules (10 000 ; 200 000) et grille entière ; sous « confirmation », cases de C1 et de C4 seules, 100 000 tirages, nombres lus exigés ; lancement vide refusé ; contrôles faits avant l'autorisation et avant toute dérivation. *Proposition* : les inscrire à B8, avec leurs artefacts (essais `point_3`).
10. **La case retirée de l'étape 9.** « Une case au-dessus est retirée une fois, à 100 000 tirages de graines neuves » (C1, C4) se lit : la case de la famille (A à cette dose et ce taux ; C de ce sourd à ce taux) est rejouée entière (48 ou 16 sources par tirage) sous la couche « confirmation », et lue aux seuls nombres retirés ; deux nombres retirés d'une même case se lisent dans les mêmes 100 000 tirages emboîtés (graines neuves par la couche, communes à ces nombres, comme à l'étape 8). *Proposition* : inscrire cette lecture (l'audit, (c), dit qu'elle ne change rien à la règle).
11. **Ce que l'étape 9 écrit.** Rien s'il n'y a aucune case à confirmer (aucun dossier, aucun manifeste) ; sinon les sorties et le manifeste de la confirmation. Les comptes et les statuts sont rendus par la fonction, non écrits : la table des critères reste au programme d'analyse (étape 10), qui relit les sorties scellées des deux étapes. *Proposition* : l'inscrire à l'ordre des opérations, point 9.
12. **Les contrôles de l'étape 9.** Manifeste de l'étape 8 vérifié (`verifier_manifeste`) et de la couche « decisif » ; fichiers gelés présentés égaux à ceux qu'il inscrit, relus et contrôlés ; dossiers de cases égaux à ceux qu'il nomme, descriptions scellées ; comptes complets (72 et 72). *Proposition* : les inscrire, avec leurs artefacts (essais `point_6`).
13. **La relecture des fichiers gelés.** Réglages : `lire_reglages_geles` (neuve ; compagnon contrôlé en forme et en nom de base, garde 22 rejouée). Fréquences : `frequences.lire_gelees`, inchangée (son compagnon n'y est contrôlé que par son premier mot, sans le nom de base). L'écart de sévérité est laissé pour ne pas changer `frequences.py`, hors des points de l'audit. *Proposition* : le dire à l'erratum ; l'aligner dans un code ultérieur si la mère le veut.
14. **Les paramètres d'essai des étapes 8 et 9.** `couche` et `tailles` (étape 8), `couche` et `tirages` (étape 9), dont les défauts sont les valeurs gelées ; sous les couches décisives, toute taille autre que gelée est refusée par `verifier_cases`, avant l'autorisation. *Proposition* : le dire à l'annexe C (« les essais les jouent réduites sous la couche « essai » »).
15. **La racine de l'arbre et le texte présenté** (silence n° 14 du code v5) restent donnés par l'appelant de `Autorisation(texte, racine)`. Le programme écrit à part (`outils-dev/lancer_etapes_8_et_9_v1.py`, non lancé) les reçoit en arguments ; la pièce de contrôle de la mère les fixe (décision R-4292). *Proposition* : la phrase de B8 et de l'annexe H qui dit qu'« aucun programme de lancement des étapes 8 et 9 n'existe encore » se met à jour, sans rien changer à la pièce de contrôle.
16. **Le dénominateur de R (M7).** Le mode « sources » de la famille D ne joue que les bras du repli ; l'écart servi, « à réglage du lecteur égal », vient de la famille B (lecteur réglé pour l'héritage, même dose, taille 1, taux 0,25 ; 10 000 tirages de 48 sources), comme `analyse.rapport_R` le prévoit déjà (deux séries, chacune rééchantillonnée sur ses sources) et comme le point 7 de la table des huit points le dit (« familles B et D »). *Proposition* : l'écrire à M7 ou à B8 (famille D).
17. **`constantes.py` inchangé** : son en-tête dit encore « préenregistrement v11 ; code v5 » ; aucune valeur n'y change (les constantes employées — `LOT_DE_SOURCES`, `SOURCES_FAMILLES_GRANDES`, `TIRAGES_PAR_CASE`, `TIRAGES_CONFIRMATION`, `CASES_C1`, `CASES_C4` — y étaient). *Proposition* : laisser ; l'essai `verrou::test_constantes_sans_empreinte_du_texte` lit cet en-tête.
18. **L'essai de forme de l'annexe C** (`tirages.essai_de_forme`, couche « essai-de-forme ») n'est pas étendu au mode « sources » ; l'essai de forme du plan entier, réduit, est un essai du code sous la couche « essai » (point 7 de l'audit). *Proposition* : si l'annexe C veut un essai de forme du mode « sources » sous sa couche, le dire.
19. **Le reliquat et l'enrichissement aux couches non décisives.** `statistique.py` n'est pas changé : `enrichissement` est appelée par `tirages`, sans autre usage ; l'étalonnage n'écrit toujours ni reliquat ni enrichissement (garde 22 : il n'écrit que des écarts, des écarts-types et des réglages).

## 3. Essais

Commande (mandat ; écart déclaré : les deux variables que les essais exigent, comme pour la vérification du code v5) : `env -C <bloc-notes>/dev-palier-0b-v6/code-v6 PYTHONPATH=src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/dev-palier-0b-v6/code-organisme-94bfd92/orchestrator /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider CHEMIN` ; un processus pour la suite entière (`CHEMIN` = `tests`), et, par l'outil `travail/lancer_essais_par_fichier_v2.py`, un processus par fichier, l'un après l'autre ; en tâche de fond, attente de leur fin. Rien d'écrit dans le dépôt.

| fichier d'essais | seul | durée seul | changé ? |
|---|---|---|---|
| `etapes` | 6 passés | 362,5 s | non |
| `gardes` | 17 passés | 2,5 s | non |
| `lancement` | **10 passés** (fichier neuf : points 1 à 6) | 5,5 s | neuf |
| `mecanique` | 10 passés | 319,1 s | non |
| `mondes` | 18 passés | 383,9 s | non |
| `organisme` | 5 passés | 170,8 s | non |
| `outils` | 15 passés | 0,7 s | non |
| `statistique` | 11 passés (deux essais adaptés à la signature neuve de `lancer_famille`) | 9,3 s | oui |
| `verrou` | 24 passés (un essai adapté à la signature neuve de `lancer_famille`) | 0,4 s | oui |
| `zz_aucune_graine_decisive` | 1 passé | 0,3 s | non |
| total, un processus par fichier | **117 passés, 0 échoué** | | |
| **suite entière, un processus** | **117 passés, 0 échoué** | 1 289,6 s | |

6 + 17 + 10 + 10 + 18 + 5 + 15 + 11 + 24 + 1 = 117, le même compte qu'en suite entière (107 du code v5 et 10 neufs). **L'essai final « aucune graine décisive » passe seul et en suite entière** ; les seules couches dérivées par les essais sont « essai » et « essai-de-forme ». Journaux : `travail/essais-fichiers-v1.log`, `travail/essais-suite-v1.log`. La suite et les essais par fichier ont été joués sur le code dont la table est `travail/table-avant-essais-v1.txt` ; le code n'a pas changé depuis (§ 10).

Essais neufs ou changés, avec cas sain et artefact (règle R5) :

| règle | cas sain | artefact | essai |
|---|---|---|---|
| point 1 : champ de mode ; aucune graine existante ne change | ordre des champs privé de `mode` = ordre du code v5 ; une étiquette du code v5 rejointe à l'identique ; les étiquettes d'une case D « tirages » sont celles du code v5, celles de la case D « sources » de mêmes paramètres les mêmes au seul `mode=sources` près, et leurs graines sont disjointes ; deux lots au-delà de 2 000 sources | les étiquettes du mode « sources » privées du champ `mode` ont des graines communes avec celles du mode « tirages » (`exiger_couches_disjointes` arrête) | `lancement::test_point_1_mode_dans_les_etiquettes_aucune_graine_existante_ne_change` |
| point 2 : mode dans le nom | D et H dans les deux modes, un seul appel : quatre dossiers ; nom « tirages » = nom du code v5 | deux cases au même nom : arrêt nommé, aucun dossier, aucune graine | `lancement::test_point_2_nom_de_case_porte_le_mode` |
| point 3 : clé de chaque case, un manifeste | cinq cases de nombres différents (2 et 3 tirages, 37 et 45 sources, H à 2 tirages), un appel : formes des sorties selon chaque clé ; un seul manifeste, qui inscrit le nombre de chaque case ; `verifier_manifeste` | case sans clé, aux deux clés, nombre nul, flottant ou booléen ; lancement vide : arrêt nommé, aucun dossier | `lancement::test_point_3_lancer_famille_suit_la_cle_de_chaque_case_un_seul_manifeste` |
| point 3 : tailles gelées sous les couches décisives | contrôle seul, sans dérivation : tailles gelées sous « decisif » ; cases de C1 et de C4 à 100 000 tirages avec nombres lus sous « confirmation » ; un lancement « decisif » aux tailles gelées est refusé par l'autorisation (aucun dossier) | taille réduite ou nombres lus sous « decisif » ; case hors de C1 et C4, case « sources », sans nombres lus, à 10 000 tirages sous « confirmation » ; nombres lus hors grille ; nombres lus au mode « sources » ; lot d'une source au bras 4a ; lancement « decisif » réduit : arrêt avant l'autorisation, aucun refus consigné | `lancement::test_point_3_tailles_gelees_sous_les_couches_decisives` |
| point 4 : reliquat, enrichissement | reliquat flottant par bras, égal à celui de la simulation rejouée (mêmes étiquettes), aux deux modes ; D « sources » : comptes du registre source et sorties d'`enrichissement` égaux à ceux de la simulation rejouée ; aucune sortie `source-` ailleurs ; reliquat nul sous la règle v1 ; cinq reliquats en H ; aucune lecture au mode « sources » ; relecture par `analyse.lire_case` ; reproductibilité à l'octet d'un second lancement | sortie de bras inconnue : arrêt ; reliquat altéré après scellement : `ArretAnalyse` | `lancement::test_point_4_reliquat_par_bras_et_enrichissement_du_repli` |
| point 5 : étape 8, plan entier réduit (essai de forme) | fichiers gelés factices relus sous contrôle ; toutes les cases du plan, un seul lancement, un seul manifeste ; empreintes vérifiées et case « non atteignable » inscrites ; D et H dans les deux modes, E et point 6 au seul mode « sources » ; le champ `mode` aux seules familles D, E, H, point 6 | — (artefacts à l'essai suivant) | `lancement::test_point_5_etape_8_plan_entier_reduit` |
| point 5 : fichiers gelés contrôlés | `lire_reglages_geles` rend les lignes gelées | empreinte des fréquences fausse ; empreinte des réglages fausse ; fichier absent ; compagnon des réglages au mauvais nom ; réglages altérés après scellement ; réglages rescellés portant un taux de rejet (garde 22) : arrêt, aucun dossier ; plan réduit sous « decisif » : arrêt des tailles ; plan gelé sous « decisif » : refus de l'autorisation | `lancement::test_point_5_etape_8_fichiers_geles_controles` |
| point 6 : étape 9 après l'étape 8 réduite | 72 et 72 comptes, tous au plus 2 ; rien à confirmer ; rien n'est écrit | couche « confirmation » sur une étape 8 « essai » (aucun refus consigné) ; fichiers gelés autres ; dossier de case retiré ; manifeste altéré ; liste des étiquettes altérée (vue par `verifier_manifeste` seule) : arrêt, rien d'écrit | `lancement::test_point_6_etape_9_apres_l_etape_8_reduite` |
| point 6 : étape 9 sur des comptes plantés | étape 8 factice (lectures plantées, non tirées) : 501 rejets à 12 sources et 500 à 10 sur une case de C1, 600 déclenchements à 5 sources sur une case de C4 : exactement deux cases retirées, entières (48 et 16 sources par tirage), lues aux seuls nombres retirés, dossier et manifeste à part (triplets, empreinte du manifeste de l'étape 8), statuts « tenue » ; étiquettes sans `mode` | une case de C4 absente de l'étape 8 : comptes incomplets, arrêt, rien d'écrit | `lancement::test_point_6_etape_9_sur_des_comptes_plantes` |
| point 6 : cases et statuts de confirmation | deux nombres d'une même case : une case, deux nombres lus ; 5 235 sur 100 000 : « tenue » ; 5 236 : « en échec » | configuration différente de celle de l'étape 8 ; triplet sans case : arrêt | `lancement::test_point_6_cases_et_statuts_de_confirmation_sur_des_valeurs_plantees` |
| essais du code v5 adaptés | `lancer_famille` appelé avec la clé `tirages` de la case (signature neuve) ; aux tailles gelées de chaque couche décisive, c'est l'autorisation qui refuse | — | `statistique::test_couches_decisives_refusees_sans_autorisation`, `statistique::test_manifeste_d_un_lancement`, `verrou::test_verrou_cas_sain_sans_graine_decisive` |

Les essais du code ne dérivent que les couches « essai » et « essai-de-forme » ; les fichiers gelés des essais sont factices (fréquences d'essai, réglages plantés) ; les comptes de l'étape 9 plantés le sont dans des tableaux de lecture écrits par l'essai, jamais tirés.

## 4. Banc des défauts (`outils-dev/mutations_v5.py`)

Version 5 du banc : les 113 défauts de `mutations_v4.py`, repris à l'identique (remplacements, fichiers, essais qui les voient ; `--verifier` : chaque texte ancien se trouve une seule fois dans le code v6), et **34 défauts neufs**, un ou plusieurs par règle du code v6. Mode `--verifier` : « défauts 147, identifiants distincts 147, problèmes 0 ». Option `--partie v3|v4|v5` (les 71 défauts de la version 3, les 42 neufs de la version 4, les 34 neufs de la version 5). Rejoué en entier, en trois parties parallèles, chaque partie jouant d'abord les témoins de ses sélections sur le code sain :

| partie | témoins (sélections sur le code sain) | défauts appliqués | vus | codes de sortie des essais qui les voient | sortie |
|---|---|---|---|---|---|
| « v3 » (les 71 de la version 3) | 48, tous au code 0 | 71 | **71** | 71 fois 1 | `outils-dev/mutations-v5-sortie-partie-v3-v1.json` |
| « v4 » (les 42 neufs de la version 4) | 14, tous au code 0 | 42 | **42** | 42 fois 1 | `outils-dev/mutations-v5-sortie-partie-v4-v1.json` |
| « v5 » (les 34 neufs de cette version) | 9, tous au code 0 | 34 | **34** | 34 fois 1 | `outils-dev/mutations-v5-sortie-partie-v5-v1.json` |
| **total** | au vert | **147** | **147** | aucun code 2 ou plus (aucune erreur de collecte) | |

Chaque défaut est vu par un essai en échec de code 1 ; les seuls codes 0 sont les témoins sur le code sain. Résumé par `travail/resumer_banc_v1.py`. Les parties « v3 » et « v4 » ont été rejouées une seconde fois, en entier, après l'arrêt de leur première tâche de fond par l'outil (§ 9) ; seules les sorties de la reprise sont rendues.

Les 34 défauts neufs :

| défaut | règle | fichier muté | essai qui le voit |
|---|---|---|---|
| mode-absent-des-etiquettes | point 1 | `tirages.py` | `lancement -k point_1` |
| mode-ecrit-aussi-aux-tirages | point 1 (graines existantes) | `tirages.py` | `lancement -k point_1` |
| ordre-des-champs-du-code-v5-change | point 1 (graines existantes) | `graines.py` | `lancement -k point_1` |
| nom-sans-mode | point 2 | `tirages.py` | `lancement -k point_2` |
| doublon-non-arrete | point 2 | `tirages.py` | `lancement -k point_2` |
| case-sans-cle-acceptee | point 3 | `tirages.py` | `lancement -k point_3` |
| nombre-non-controle | point 3 | `tirages.py` | `lancement -k point_3` |
| tirages-communs-a-toutes-les-cases | point 3 | `tirages.py` | `lancement -k point_3` |
| sources-communes-a-toutes-les-cases | point 3 | `tirages.py` | `lancement -k point_3` |
| tailles-gelees-non-exigees | point 3 | `tirages.py` | `lancement -k point_3` |
| confirmation-hors-de-c1-et-c4 | point 6 | `tirages.py` | `lancement -k point_3` |
| nombres-lus-hors-de-la-grille | point 6 | `tirages.py` | `lancement -k point_3` |
| lot-d-une-source-accepte | point 1 (source étrangère) | `tirages.py` | `lancement -k point_3` |
| confirmation-simulee-reduite | point 6 | `tirages.py` | `lancement -k "point_6 and plantes"` |
| reliquat-absent | point 4 | `tirages.py` | `lancement -k point_4` |
| reliquat-en-entier | point 4 | `tirages.py` | `lancement -k point_4` |
| enrichissement-absent | point 4 | `tirages.py` | `lancement -k point_4` |
| enrichissement-mal-pris | point 4 | `tirages.py` | `lancement -k point_4` |
| etape-8-reglages-sans-compagnon | point 5 | `etalonnage.py` | `lancement -k "point_5 and controles"` |
| etape-8-reglages-sans-garde-22 | point 5 | `etalonnage.py` | `lancement -k "point_5 and controles"` |
| etape-8-frequences-non-controlees | point 5 | `etapes.py` | `lancement -k "point_5 and controles"` |
| etape-8-reglages-non-controles | point 5 | `etapes.py` | `lancement -k "point_5 and controles"` |
| etape-8-non-atteignables-non-inscrites | point 5 | `etapes.py` | `lancement -k "point_5 and plan_entier"` |
| etape-8-fichiers-geles-non-inscrits | point 5 | `etapes.py` | `lancement -k "point_5 and plan_entier"` |
| etape-8-sans-les-cases-sources | point 5 (« en un seul lancement ») | `etapes.py` | `lancement -k "point_5 and plan_entier"` |
| etape-9-manifeste-8-non-verifie | point 6 | `etapes.py` | `lancement -k "point_6 and apres"` |
| etape-9-dossiers-non-confrontes | point 6 | `etapes.py` | `lancement -k "point_6 and apres"` |
| etape-9-comptes-incomplets-acceptes | point 6 | `etapes.py` | `lancement -k "point_6 and plantes"` |
| etape-9-c4-lu-sur-les-rejets | point 6 | `etapes.py` | `lancement -k point_6` |
| etape-9-couche-non-controlee | point 6 | `etapes.py` | `lancement -k "point_6 and apres"` |
| etape-9-fichiers-geles-non-confrontes | point 6 | `etapes.py` | `lancement -k "point_6 and apres"` |
| etape-9-lance-sans-case-a-confirmer | point 6 | `etapes.py` | `lancement -k "point_6 and apres"` |
| etape-9-statut-sans-confirmation | point 6 | `etapes.py` | `lancement -k point_6` |
| etape-9-nombres-lus-perdus | point 6 | `etapes.py` | `lancement -k point_6` |

Aucun défaut n'ouvre le verrou des couches décisives : ceux des tailles gelées et de la couche « confirmation » portent sur `verifier_cases`, éprouvé seul ou sur des lancements que l'autorisation refuse ensuite ; aucun essai ne dérive de graine décisive.

## 5. Sorties : ce qui reste égal à l'octet, ce qui change et pourquoi

Outil `travail/empreintes_sorties_v2.py` (reprise de l'outil du développeur du code v5, `empreintes_sorties_v1.py`, mêmes appels et mêmes clés, graines « essai » seules ; deux changements : l'appel de `lancer_famille` suit la signature du paquet, avec le même nombre de tirages, 2 ; les sorties scellées d'une case sont relevées aussi fichier par fichier, et une case jouée par `jouer_case` est ajoutée), un processus par paquet, chacun importé de son seul `src` ; comparaison par `travail/comparer_empreintes_v2.py` (`travail/comparaison-sorties-v5-v6.txt`) : **526 empreintes égales à l'octet sur 531, 5 différentes, 6 seulement au code v6, aucune seulement au code v5.**

Égales (526) : couche statistique, sept proposeurs, deux doses, bras 1 à 4b (M1, D, I, lois fausses tenues ; 280) ; générateur (six suites, clés, épisodes, compteurs) ; mondes de l'audit, traits de forme et de contenu, leur distribution ; exactitudes, σ₀, M, table et lecture de l'audit de présentation ; étape 3 (dérivation, exactitudes) ; jeu de la garde 27 à deux et trois sources (registres, mesures, entrées servies, reliquats, registres sources, vues du bras 2, clés des mondes) ; **liste des étiquettes de graines d'un lancement** (`tirages/liste_des_etiquettes`) et étiquettes d'une case jouée par `jouer_case` ; **chaque fichier `M1`, `D`, `I`, `fausses_tenues` et `lecture-*`** d'une case lancée et d'une case jouée ; le manifeste privé de sa configuration (`tirages/manifeste_sans_versions_ni_configuration`).

| sortie différente | pourquoi |
|---|---|
| `tirages/fichier/case.json`, `jouer_case/fichier/case.json` | points 3 et 4 : la description porte la clé `tirages` de la case (lancement), `mode`, `sources_par_tirage`, et l'empreinte des trois fichiers de reliquat |
| `tirages/sorties_scellees` | point 4 : les empreintes rendues comprennent celles des trois reliquats et de la description neuve |
| `tirages/manifeste_sans_versions`, `tirages/manifeste_sans_versions_ni_champs_du_verrou` | point 3 : la configuration du manifeste porte `tirages_par_case` et `sources_par_case` à la place du nombre commun `tirages` |

Seulement au code v6 (6) : `reliquat-bras-1.npy`, `-2`, `-3` d'une case lancée et d'une case jouée (point 4). Rien d'autre ne bouge. Changent de sort, sans sortie à comparer : une case sans clé, deux cases au même nom, une taille non gelée sous une couche décisive, une confirmation hors de C1 et de C4 arrêtent avant tout tirage (au code v5 : nombre commun, erreur de dossier existant au milieu du lancement, aucun contrôle). Fichiers : `travail/empreintes-v5.json`, `travail/empreintes-v6.json` ; l'outil, rejoué sur le code v6 après le banc, au scellement, rend un fichier égal à l'octet (`travail/empreintes-v6-bis.json`, `cmp` sans écart).

## 6. Inventaire de « Ce qui est rapporté » (T:393) contre les sorties, ligne à ligne

« Étape 8 » : sorties scellées de `etape_8` ; « étape 9 » : celles de `etape_9` ; « hors des étapes 8 et 9 » : une pièce écrite par une autre étape, que le programme d'analyse lit à côté. Chaque ligne dit où se trouve la matière brute ; le calcul (taux, moyennes, intervalles) revient au programme d'analyse.

| ce que T:393 nomme | où la matière brute se trouve (code v6) | état |
|---|---|---|
| la table de puissance entière (deux contrastes, quatre tailles, deux doses, douze nombres, trois taux à la taille 1) | étape 8, famille B, mode « tirages » : `lecture-lecture_heritage`, `lecture-lecture_tenue` | déjà au code v5 |
| le niveau par case | étape 8, famille A : `lecture-rejette` ; étape 9 : `lecture-rejette` des cases retirées | étape 9 neuve |
| les taux de déclenchement de la règle de validité, par proposeur, force et nombre à dose nulle | étape 8, famille C : `lecture-declenche` ; étape 9 pour les deux sourds | étape 9 neuve |
| la part de différences nulles | étape 8, toutes cases « tirages » : `M1-bras-*` | déjà au code v5 |
| les fréquences M12 (lois fausses tenues, non plantées par origine et regroupée, lois vraies par classe) | hors des étapes 8 et 9 : fichier gelé de l'étape 5 (`frequences.geler`, clé `rapport`), dont l'empreinte vérifiée est inscrite au manifeste de l'étape 8 | inscription neuve au manifeste |
| les rejets du générateur par niveau, le taux d'acceptation, la distribution des traits de contenu ; les quinze exactitudes | hors des étapes 8 et 9 : rapport de l'étape 3 (`mondes.audit_du_generateur`) | inchangé |
| la taille de l'ensemble exclu, par source | hors des étapes 8 et 9 : couche mécanique (étapes 3 et 4, `mecanique.jouer_source`, clé `exclu` ; `audit.ensemble_exclu_par_construction`) ; la couche statistique n'écrit aucune loi, et n'a pas d'ensemble exclu | inchangé ; **non écrit par l'étape 8** (sans objet sur la couche statistique) |
| l'effet du seul coût de lecture, par dose, règle et repère | étape 8, famille E, mode « sources » : `M1-bras-2`, `M1-bras-3` sur 200 000 sources | **neuf (le code v5 ne la tirait pas)** |
| l'écart d'héritage à dose nulle du lecteur, comparé à lui | étape 8, famille C, lecteur réglé pour l'héritage : `M1-bras-2`, `M1-bras-3` | déjà au code v5 |
| le rapport R | étape 8 : numérateur, famille D, mode « sources », `M1-bras-*` (200 000 sources par dose) ; dénominateur, famille B, lecteur réglé pour l'héritage, taille 1, taux 0,25 (silence n° 16) | **numérateur neuf** |
| la part des entrées gardées, le facteur d'enrichissement | étape 8, famille D, mode « sources » : `source-part_des_entrees_gardees`, `source-facteur_entrees`, `source-facteur_paires` et les dix comptes `source-*` | **neuf** |
| la puissance du contraste de l'héritage sous le repli | étape 8, famille D, mode « tirages » : `lecture-lecture_heritage` | déjà au code v5 |
| le résultat sur le généraliste | étape 8, famille C (généraliste) : `lecture-declenche` ; point 6 (dose 0,5), mode « sources » : `D-bras-*`, `I-bras-*` | point 6 **neuf** |
| le suiveur à la lettre sur le contraste de la tenue | étape 8, famille F : `lecture-lecture_tenue`, `lecture-rejette` | déjà au code v5 |
| les tailles réalisées face aux tailles visées | étape 8 : `M1-bras-*` des cases à taille ou force ; écart-type entre jumelles gelé : fichier des réglages, dont l'empreinte vérifiée est au manifeste | inscription neuve |
| les cases « non atteignables » | étape 8 : manifeste, `configuration.cases_non_atteignables` | **neuf** |
| les rapports d'écarts-types de M9 | étape 8, famille A : `M1-bras-*` ; écarts-types entre jumelles : fichier des réglages | déjà au code v5 |
| le reliquat de budget par bras | étape 8 (et 9) : `reliquat-bras-*` de toutes les cases (silence n° 4) | **neuf** |
| les nombres n lus aux taux d'échec 0 et 0,5 | étape 8, famille B, taille 1, taux 0 et 0,5 : `lecture-lecture_*` | déjà au code v5 |
| la part des tirages où l'autre contraste passe la première marche de Holm, par case | étape 8, famille B : `lecture-premiere_marche_heritage`, `lecture-premiere_marche_tenue` | déjà au code v5 |
| sans critère : la puissance du seul contraste de l'héritage à chaque nombre, n₁, S9 | étape 8, famille B (grille avec 6 à 9) : `lecture-heritage_seul_lecture` ; famille A : `lecture-heritage_seul_rejette` | déjà au code v5 |
| sans critère : les écarts et taux de rejet du bras de diagnostic (M14) | étape 8, famille H : écarts, mode « sources », `M1-bras-1`, `-2`, `-3`, `-4a`, `-4b` sur 200 000 sources ; taux de rejet, mode « tirages », `lecture-rejette_2_moins_1`, `lecture-rejette_2_moins_4b` | **écarts neufs** |
| (M10, point 6 du § 7 du plan) suiveur et généraliste rejoués à la dose 0,5, sur 200 000 sources | étape 8, `point-6`, mode « sources » : `D-bras-*`, `I-bras-*` | **neuf** |

Aucune ligne de T:393 ne demande à l'étape 8 une sortie que le code v6 n'écrit pas, hors de l'ensemble exclu (sans objet sur la couche statistique) et des pièces des étapes 3 à 6.

## 7. Ce que l'erratum v14 devra inscrire au texte (liste exacte ; rien n'y est tranché par moi)

1. **La ligne « Commit du code d'analyse » et le premier bloc qui la suit** : le commit du code v6 (celui que la mère poussera) et la table des empreintes du code v6 (§ 12 de ce rapport, chemins relatifs à `palier-0b/code-v6/`, 64 lignes, ce rapport exclu ; la table extraite, une ligne par fichier, a pour empreinte `639335b95b46b8f1d2258ba84fdf117bd4061df6cd5b0bf1b3dca85549c62fa3`, fichier `travail/table-empreintes-code-v6.txt`). Forme exigée par le verrou, inchangée : une seule ligne du texte commence par `- Commit du code d'analyse : ` ; son premier `` `<40 hex>` `` est le commit ; la table est le premier bloc « ``` » qui la suit et ne porte que la table ; elle nomme sous `src/` exactement les vingt-quatre fichiers du code lancé (les vingt-trois `.py` du paquet, aucun ajouté, et `src/controle_ia/__init__.py`), dont quatre changent d'empreinte : `etalonnage.py`, `etapes.py`, `graines.py`, `tirages.py`. Le commit inscrit doit être celui que portera la pièce d'autorisation du verrou.
2. **B8, graines** : le champ d'étiquette `mode` (silence n° 1) ; la phrase « aucune graine existante ne change ».
3. **B8, cases et tirages ; B7 bis** : le mode « sources » — lots de 2 000 sources sous leur étiquette, 100 lots pour 200 000 ; la source étrangère de H au mode « sources » ; l'arrêt sur un lot d'une seule source (silences n° 2 et 3).
4. **B8, sorties scellées ; « Ce qui est rapporté »** : le reliquat par bras et sa forme ; les sorties du registre de la course source de la famille D au mode « sources » (comptes et `enrichissement`) ; aucune lecture au mode « sources » ; les champs neufs de la description d'une case ; le nom des dossiers (suffixe `-sources`) (silences n° 4 à 7) ; l'inventaire du § 6, s'il est retenu.
5. **B8, « toutes les familles, en un seul lancement » ; « Un manifeste par run »** : `lancer_famille` suit la clé de chaque case (le nombre commun est retiré) ; un manifeste pour l'étape 8, un pour l'étape 9 ; leurs champs de configuration ; `fichiers_geles` (silence n° 8) ; les contrôles d'un lancement (`verifier_cases`) (silence n° 9).
6. **Ordre des opérations, points 8 et 9 ; C1 et C4** : `etapes.etape_8` et `etapes.etape_9` ; la relecture des fichiers gelés sous contrôle de leurs empreintes (silence n° 13) ; la case retirée, entière, lue aux nombres retirés (silence n° 10) ; ce que l'étape 9 écrit et ses contrôles (silences n° 11 et 12) ; le dénominateur de R (silence n° 16).
7. **B8, « Version 12 », silence n° 14, et annexe H, « Version 12 », § 2** : la phrase « aucun programme de lancement des étapes 8 et 9 n'existe encore » se dit du code v5 ; au code v6, les étapes 8 et 9 sont des fonctions du paquet, et un programme à part, non lancé (`outils-dev/lancer_etapes_8_et_9_v1.py`), les appelle ; la racine de l'arbre lancé et le texte présenté restent donnés par l'appelant et fixés par la pièce de contrôle de la mère (silence n° 15).
8. **« Ce qui demande un code v6 »** (section neuve) : les sept points de l'audit des trous du code v5 (`8e965f80…`, § 2), faits par le code v6 (ce rapport, chemin et empreinte), à vérifier par le vérificateur du code ; la ligne « Commit du code d'analyse » refaite par cet erratum.
9. **Annexe C** : le fichier d'essais neuf `tests/test_heritage_etage_processeur_v1_lancement.py`, les comptes d'essais (§ 3) et le banc `mutations_v5.py` (§ 4) ; les paramètres d'essai des étapes 8 et 9 (silence n° 14) ; l'essai de forme du plan entier, réduit, sous la couche « essai » (silence n° 18).
10. **Ordre des opérations, point 2, et statut** : code v6 écrit ; restent sa vérification par un autre modèle, l'erratum v14 contre-lu, puis, après le mot de Lazar, le scellement ; puis le GO qui nomme la v14 (nœud de l'audit, § 2 : la ligne `GO-2026-11-20-66` nomme la v13), la pièce d'autorisation du verrou, qui porte l'empreinte du texte présenté (la v14) et le commit du code v6, et la pièce de contrôle de la mère.
11. **Remarques à porter ou non** (§ 8) : le programme d'analyse de l'étape 10 ; la place disque ; le point 6 du généraliste.

## 8. Remarques (aucune n'est tranchée)

1. **Le programme d'analyse (étape 10) n'est écrit ni au code v5 ni au code v6.** `analyse.py` n'est pas changé : il a les fonctions de lecture (`lire_case`, qui relit aussi les sorties neuves, `taux_par_nombre`, `rapport_R`, `s7`, `table_des_criteres`…), mais aucun programme ne relit toutes les cases scellées des étapes 8 et 9 pour écrire la table des critères et tout ce que T:393 nomme, et aucune fonction ne calcule encore les écarts du mode « sources » (M8, M14, M10 du point 6, numérateur de R, reliquat, enrichissement). Hors du mandat ; à écrire, contre-lire et inscrire avant l'étape 10, sans rien changer aux sorties des étapes 8 et 9.
2. **Place disque de l'étape 8 aux tailles gelées** (calcul d'ordre de grandeur, `travail/compter_le_plan_v1.py`, non une mesure) : environ 1,54 Go de tableaux pour les 89 cases d'un plan où toutes les cibles sont atteignables (61 au mode « tirages », 28 au mode « sources »), dont environ 0,71 Go de reliquat (flottants de 64 bits). Le temps de calcul n'est pas estimé ici (aucun essai à pleine taille).
3. **Le point 6 et le généraliste.** `plan_des_cases` (code v4, inchangé) prend la force de référence du généraliste par la constante du suiveur (`FORCE_REFERENCE_SUIVEUR`), égale à celle du généraliste (1,0). Sans effet ; dit pour la contre-lecture.

## 9. Gestes, écarts, refus

- **Aucun refus de permission, de classifieur ni de garde.**
- Écart au mandat, comme pour la vérification du code v5 : les deux variables d'environnement que les essais exigent (`HERITAGE_DEPOT`, `HERITAGE_COPIE_ORGANISME`), passées par `env` au lancement ; sans elles les essais échouent par construction.
- Une commande simple par appel ; aucun heredoc, aucun code en ligne passé à un interpréteur : chaque calcul passe par un fichier du bloc-notes (`travail/`) ou du code ; les boucles ne sont que dans ces fichiers. Calculs longs en tâche de fond, attente de leur fin par les avis de fin de tâche ou par `timeout … tail -F` sur leur journal ; aucun processus arrêté par moi.
- **Incident** : les deux premières tâches de fond du banc (parties « v3 » et « v4 ») ont été arrêtées par l'outil lui-même, à sa limite par défaut de 30 minutes pour une tâche de fond, avant d'écrire leur sortie (aucune sortie partielle n'est gardée ni lue comme résultat ; elles avaient vu, à cet instant, chaque défaut joué). Une liste des processus (`ps -eo pid,ppid,etimes,pcpu,args --sort=etimes`, sans motif) a montré qu'aucun de leurs processus ne tournait plus ; les deux parties ont été relancées en entier, dans des dossiers de travail neufs (`travail/banc-v3-reprise`, `travail/banc-v4-reprise`), avec une limite de deux heures ; seules ces reprises font foi (§ 4). La sortie longue de cette liste des processus a été rangée par l'outil lui-même sous `/root/.claude/` (je n'y ai rien écrit ni lu). `ls` et `diff -rq` dans le bloc-notes et `code-v5/` seulement ; les autres fichiers ouverts par leur chemin complet.
- Graines : seulement les couches « essai » (essais, banc, sorties) et des générateurs locaux de numpy (valeurs plantées) ; aucune graine des couches « etalonnage », « mecanique », « mecanique-reglages », « audit », « decisif » ou « confirmation » dérivée ; les seules demandes de couches décisives sont celles des essais des refus, toutes refusées. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille ; aucun taux de rejet, aucune puissance, aucune valeur p calculés hors des essais du code sur graines d'essai.
- Le programme à part `outils-dev/lancer_etapes_8_et_9_v1.py` (« non lancé, en attente ») n'a été exécuté qu'une fois, sur une racine factice du bloc-notes (`travail/racine-factice/`, sans pièce d'autorisation), avec le texte v13 du dépôt présenté en lecture seule : refus du verrou, « pièce d'autorisation … absente sur disque », avant toute dérivation et avant toute création de dossier (`travail/essai-lanceur-racine-factice.log`).
- Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau (ni `git fetch` ni `git show` : le dépôt local suffisait) ; aucune écriture dans le dépôt, aucun commit ; aucune pièce d'autorisation écrite ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucune valeur de clé ; aucun identifiant de modèle ; aucune publication.

## 10. Fichiers et empreintes

Dossier rendu : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-palier-0b-v6/code-v6/` (arborescence du code v5 : `src/`, `tests/`, `outils-dev/`, et ce rapport). Chaque fichier a son compagnon `.sha256` au format de `sha256sum` lancé dans son dossier (`env -C DOSSIER sha256sum F > DOSSIER/F.sha256` pour chaque fichier neuf ou changé ; les autres gardent le compagnon du code v5, à l'octet) ; ce rapport a le sien. Contrôle des compagnons et table : `travail/table_et_compagnons_v2.py` (« 64 fichiers dans la table ; 0 problème(s) »). La table entière (ce rapport exclu) est au § 12 ; elle se vérifie par `sha256sum -c` dans `code-v6/`.

Fichiers changés ou neufs (les autres sont ceux du code v5, à l'octet ; le rapport v5 n'est pas dans ce dossier) :

```
e6d086cf5a663a1494790dcb3e6ca230f704a340d7086816d7f47b5e24f4158e  src/controle_ia/heritage_etage_processeur_v1/tirages.py
b3695c506eeeb71d9f3da58ad4fa5a3bf8fcdfe792a9b728bbece415adfea70d  src/controle_ia/heritage_etage_processeur_v1/etapes.py
bebabac88975cc25f2f8939e8cb0ba7a166cf1cdfa59b72cb1f3ec694f3d959f  src/controle_ia/heritage_etage_processeur_v1/graines.py
240349f7fc76ce5427defde63941a9944669bf48978e6c63a1813c4ff1ecdfe7  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
bd3fb20ea9dbd20ad6cc48b66a08acd1e6273df450fea06a8209b6ef00c8d527  tests/test_heritage_etage_processeur_v1_statistique.py
6f33487438c0f251b0d46323e09233ea126c108f3ae992b104204c2ca861acba  tests/test_heritage_etage_processeur_v1_verrou.py
0a4545300abeccf86a7d881bd41c64a44eebec8a7eea588def70bdac6ca9c9b7  tests/test_heritage_etage_processeur_v1_lancement.py
82c534be7f1fa25e1c1691f84fe1f55bf704bab976d8cd4198f793e2965eb298  outils-dev/mutations_v5.py
67052a4b7af9bd02c5f28f3b8a7926fd7b7ac5a98fb797f14b3d6f424bedc2a5  outils-dev/lancer_etapes_8_et_9_v1.py
f1bd85a8119c54eba8beb6c28255dd68c86237720ba38113b7c696e025cba4d7  outils-dev/mutations-v5-sortie-partie-v3-v1.json
7733704bab9a1190fbe60a0d2def7dd88d0fd74d08829990bad9fa65e6c61ea7  outils-dev/mutations-v5-sortie-partie-v4-v1.json
174b50906ab6dc6327e60762edd39439c3556b0548bc987099b2759f1b463536  outils-dev/mutations-v5-sortie-partie-v5-v1.json
```

Les empreintes de la table ont été relevées avant le lancement final des essais et du banc (`travail/table-avant-essais-v1.txt`, 61 lignes, `1ae872df2a4bc8ae684c41d63bedf52122a0d301f6542adb804631fcb5b4056b`), puis au scellement (`travail/table-empreintes-code-v6.txt`, 64 lignes, `639335b95b46b8f1d2258ba84fdf117bd4061df6cd5b0bf1b3dca85549c62fa3`) : `diff` entre les deux ne montre que les trois sorties neuves du banc ; le code, les essais et les outils n'ont pas changé entre la suite au vert, le banc et le scellement. Sous `src/`, vingt-quatre fichiers, comme au code v5 ; quatre changent d'empreinte (`tirages.py`, `etapes.py`, `graines.py`, `etalonnage.py`), les vingt autres gardent celle du code v5.

Non rendus, laissés dans le bloc-notes (`dev-palier-0b-v6/`) : `code-v5/` (copie intacte) ; `code-organisme-94bfd92/` (copie) ; `travail/` : `empreintes_sorties_v2.py`, `comparer_empreintes_v2.py`, `lancer_essais_par_fichier_v2.py`, `table_et_compagnons_v2.py`, `compter_le_plan_v1.py`, `assembler_rapport_v1.py`, journaux des essais et du banc, `empreintes-v5.json`, `empreintes-v6.json`, `comparaison-sorties-v5-v6.txt`, `diffs/`, `table-avant-essais-v1.txt`, `table-empreintes-code-v6.txt`, `racine-factice/`, `essai-lanceur-racine-factice.log`.

## 11. Différentiels v5 → v6 (`diff -u`)

Fichiers changés ou neufs, dans cet ordre ; `mutations_v5.py`, neuf, est donné en différentiel depuis `mutations_v4.py`, gardé intact ; le fichier d'essais neuf et le programme à part, depuis `/dev/null`. Les autres fichiers de la table du code v5 sont à l'octet ceux du code v5.

#### `1-tirages.py.diff`

````diff
--- code-v5/src/controle_ia/heritage_etage_processeur_v1/tirages.py
+++ code-v6/src/controle_ia/heritage_etage_processeur_v1/tirages.py
@@ -11,6 +11,24 @@
 compte. Les couches « decisif » et « confirmation » exigent une autorisation (module `graines`) : sans elle, la première
 dérivation lève et rien n'est tiré. L'essai de forme (annexe C) est borné à 200 tirages par case et deux nombres de sources, sous
 la couche « essai-de-forme », et ses sorties le disent dans leur nom.
+
+Code v6 (audit des trous du code v5, « Ce que le code v6 doit porter », points 1 à 4 ; préenregistrement v13, B8, ordre des
+opérations, étape 8, et « Ce qui est rapporté ») :
+- une case a un **mode**, et exactement une des deux clés : `tirages` (tirages emboîtés, lus tirage par tirage) ou `sources`
+  (écarts sur des sources : familles D, E, H et point 6, 200 000 sources, sans lecture par tirage). Le mode « sources » porte un
+  champ d'étiquette de plus, `mode=sources` ; aucune étiquette du mode « tirages » ne change (le champ n'y est pas écrit). Le nom
+  d'une case du mode « sources » finit par `-sources` : deux cases qui ne diffèrent que par le mode ont deux dossiers ;
+- au mode « sources », les sources sont simulées par lots de `LOT_DE_SOURCES` (2 000), chaque lot sous son étiquette (champ
+  `lot`) ; la source étrangère d'une source (famille H, bras 4a et 4b) est la suivante du même lot, la première pour la dernière
+  (SILENCE : le lot tient lieu du « tirage » de B7 bis dans ce mode ; un lot d'une seule source arrête) ;
+- `lancer_famille` suit la clé de chaque case (aucun nombre commun à toutes), contrôle les cases avant l'autorisation et avant
+  toute dérivation (`verifier_cases` : une clé et une seule, deux cases jamais au même nom, tailles gelées sous les couches
+  décisives, couche « confirmation » réservée aux cases de C1 et de C4), tire toutes les cases d'un lancement, de tous modes, et
+  écrit un seul manifeste ;
+- les sorties scellées portent aussi, par bras, le **reliquat** de budget (USD simulés, somme sur les quatre générations,
+  flottant ; nul par construction sous la règle de retrait de la version 1), et, aux cases du repli au mode « sources »
+  (famille D), les comptes du registre de la course source et ce que rend `statistique.enrichissement` (part des entrées
+  gardées, facteurs d'enrichissement au grain des entrées et des paires), source par source.
 """
 
 import hashlib
@@ -24,12 +42,28 @@
 from . import rangs_signes as RS
 from .constantes import (ESSAI_DE_FORME_MAX_NOMBRES_DE_SOURCES, ESSAI_DE_FORME_MAX_TIRAGES, GRILLE_SOURCES,
                          GRILLE_SOURCES_DOSE_NULLE, LOT_DE_SOURCES, MAX_SOURCES, MAX_SOURCES_DOSE_NULLE, NOMBRES_M13_EN_PLUS,
-                         RACINE_GRAINES, REPERE_LECTURE, VERSION)
+                         RACINE_GRAINES, REPERE_LECTURE, SOURCES_FAMILLES_GRANDES, TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE,
+                         VERSION)
 from .graines import COUCHES_DECISIVES
-from .statistique import simuler
+from .statistique import enrichissement, simuler
 
 LECTURES = {"non établi": 0, "établi": 1, "non lu comme succès": 2, "effet négatif établi": 3, "égalité": 4}
 
+# code v6 : les deux modes d'une case (B8 : « tirages » emboîtés ; « sources », écarts sur 200 000 sources)
+MODES = ("tirages", "sources")
+# code v6 : les sorties brutes par bras et leur type écrit (les comptes en entiers de 16 bits, comme au code v5 ; le reliquat de
+# budget, en USD simulés, en flottant de 64 bits)
+TYPES_DES_SORTIES = {"M1": np.int16, "D": np.int16, "I": np.int16, "fausses_tenues": np.int16, "reliquat": np.float64}
+# code v6 : les sorties du registre de la course source, aux cases du repli au mode « sources » (famille D ; S7, M7) — ses comptes
+# (entiers de 64 bits), puis ce que rend `statistique.enrichissement` (flottants de 64 bits ; non défini, NaN, si un dénominateur
+# est nul)
+COMPTES_DU_REGISTRE_SOURCE = ("entrees", "entrees_gardees", "entrees_vraies", "entrees_vraies_gardees", "lois_vraies_engagees",
+                              "lois_fausses_engagees", "lois_non_plantees_engagees", "lois_vraies_gardees",
+                              "lois_fausses_gardees", "lois_non_plantees_gardees")
+CHAMPS_D_ENRICHISSEMENT = ("part_des_entrees_gardees", "facteur_entrees", "facteur_paires")
+# code v6 : ce que la couche « confirmation » tire (C1 : famille A, sourd à appels égaux ; C4 : famille C, les deux sourds)
+CASES_DE_CONFIRMATION = (("A", "sourd-egal"), ("C", "sourd-egal"), ("C", "sourd-paie"))
+
 
 class ArretTirages(RuntimeError):
     pass
@@ -45,8 +79,24 @@
     return MAX_SOURCES_DOSE_NULLE if dose == 0.0 else MAX_SOURCES
 
 
+def mode_de(case):
+    """Code v6 : le mode d'une case et son nombre — `("tirages", n)` ou `("sources", n)`. Exactement une des deux clés, et un
+    entier positif ; arrêt nommé sinon (aucun nombre commun à toutes les cases n'est plus reçu de l'appelant)."""
+    presents = [m for m in MODES if m in case]
+    if len(presents) != 1:
+        raise ArretTirages(f"case {case.get('famille')}/{case.get('proposeur')} : une et une seule des clés « tirages » et "
+                           f"« sources » attendue (reçu {presents}) : arrêt avant tout tirage")
+    m = presents[0]
+    n = case[m]
+    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
+        raise ArretTirages(f"case {case.get('famille')}/{case.get('proposeur')} : nombre de {m} invalide ({n!r}) : arrêt")
+    return m, n
+
+
 def champs_de_la_case(case):
-    """Les champs d'étiquette d'une case (B8 : famille, proposeur, dose, taille ou force, taux d'échec, règle, repère)."""
+    """Les champs d'étiquette d'une case (B8 : famille, proposeur, dose, taille ou force, taux d'échec, règle, repère).
+    Code v6 : le mode « sources » ajoute le champ `mode` ; le mode « tirages » ne l'écrit pas (ses étiquettes sont celles du code
+    v5)."""
     c = {"famille": case["famille"], "proposeur": case["proposeur"], "dose": case["dose"], "taux": case["taux"]}
     if case.get("taille") is not None:
         c["taille"] = case["taille"]
@@ -56,14 +106,17 @@
         c["retrait"] = case["retrait"]
     if case.get("repere", REPERE_LECTURE) != REPERE_LECTURE:
         c["repere"] = case["repere"]
+    if "sources" in case:
+        c["mode"] = "sources"
     if case.get("repli"):
         c["role"] = "repli"
     return c
 
 
 def simuler_case(graines, couche, case, f, tirages, sources_par_tirage=None, premier_tirage=0):
-    """Simule `tirages` tirages d'une case ; rend {clé de bras : {M1, D, I, fausses_tenues : (tirages, sources)}}. Les graines
-    sont dérivées par lot ; la première dérivation d'une couche décisive sans autorisation lève (liste d'arrêt, point 1)."""
+    """Simule `tirages` tirages d'une case ; rend {clé de bras : {M1, D, I, fausses_tenues, reliquat : (tirages, sources)}}. Les
+    graines sont dérivées par lot ; la première dérivation d'une couche décisive sans autorisation lève (liste d'arrêt,
+    point 1)."""
     S = sources_par_tirage or s_max(case["dose"])
     par_lot = max(1, LOT_DE_SOURCES // S)
     base = champs_de_la_case(case)
@@ -82,13 +135,62 @@
                     case["taux"], f, n * S, case.get("repere", REPERE_LECTURE), case.get("retrait", "v2"),
                     case.get("repli", False), taille_tirage=S)
         for b in case["bras"]:
-            for champ in ("M1", "D", "I", "fausses_tenues"):
+            for champ in TYPES_DES_SORTIES:
                 sorties.setdefault(b, {}).setdefault(champ, []).append(r["bras"][b][champ].reshape(n, S))
         t += n
         k += 1
     return {b: {c: np.concatenate(v, axis=0) for c, v in d.items()} for b, d in sorties.items()}
 
 
+def sorties_du_registre_source(src):
+    """Code v6 (point 4 de l'audit ; M7, S7) : ce que le registre de la course source porte, source par source — ses comptes, et
+    la part des entrées gardées et les facteurs d'enrichissement que rend `statistique.enrichissement`."""
+    e = enrichissement(src)
+    comptes = {"entrees": src.n, "entrees_gardees": src.n_gardees, "entrees_vraies": src.entrees_v,
+               "entrees_vraies_gardees": src.gardees_v, "lois_vraies_engagees": src.engagee_v.sum(axis=1),
+               "lois_fausses_engagees": src.engagee_f.sum(axis=1), "lois_non_plantees_engagees": src.engagee_np,
+               "lois_vraies_gardees": src.gardee_v.sum(axis=1), "lois_fausses_gardees": src.gardee_f.sum(axis=1),
+               "lois_non_plantees_gardees": src.gardee_np}
+    out = {k: np.asarray(comptes[k], dtype=np.int64) for k in COMPTES_DU_REGISTRE_SOURCE}
+    out.update({k: np.asarray(e[k], dtype=np.float64) for k in CHAMPS_D_ENRICHISSEMENT})
+    return out
+
+
+def simuler_case_sources(graines, couche, case, f, sources, lot=LOT_DE_SOURCES):
+    """Code v6 (point 1 de l'audit) : le mode « sources ». `sources` sources simulées par lots de `lot` sources, chaque lot sous
+    son étiquette (champ `mode=sources`, numéro de lot) ; la source étrangère d'une source est la suivante du même lot, la
+    première pour la dernière ; un lot d'une seule source, pour une case qui a les bras 4a ou 4b, arrête avant tout tirage. Rend
+    (sorties par bras {champ : (sources,)}, sorties du registre de la course source {champ : (sources,)}, vides hors du
+    repli)."""
+    base = champs_de_la_case(case)
+    if base.get("mode") != "sources":
+        raise ArretTirages("simulation au mode « sources » d'une case sans clé « sources »")
+    role_case = base.pop("role", None)
+    dernier = sources - lot * ((sources - 1) // lot)
+    if any(b in ("4a", "4b") for b in case["bras"]) and min(lot, dernier) < 2:
+        raise ArretTirages("mode « sources » : un lot d'une seule source n'a pas de source étrangère (B7 bis) : arrêt")
+    sorties, registre = {}, {}
+    fait = 0
+    k = 0
+    while fait < sources:
+        n = min(lot, sources - fait)
+        etiq = dict(couche=couche, **base, lot=k)
+        cles = {b: graines.g(**etiq, bras=b, role="echantillonnage" if role_case is None else f"echantillonnage-{role_case}")
+                for b in case["bras"]}
+        r = simuler(cles, graines.g(**etiq, role="monde"), graines.g(**etiq, role="source"), case["config"], case["dose"],
+                    case["taux"], f, n, case.get("repere", REPERE_LECTURE), case.get("retrait", "v2"), case.get("repli", False))
+        for b in case["bras"]:
+            for champ in TYPES_DES_SORTIES:
+                sorties.setdefault(b, {}).setdefault(champ, []).append(r["bras"][b][champ])
+        if case.get("repli"):
+            for champ, v in sorties_du_registre_source(r["source"]).items():
+                registre.setdefault(champ, []).append(v)
+        fait += n
+        k += 1
+    return ({b: {c: np.concatenate(v) for c, v in d.items()} for b, d in sorties.items()},
+            {c: np.concatenate(v) for c, v in registre.items()})
+
+
 def lire_case(sorties, dose, grille, bras):
     """La lecture de chaque tirage à chaque nombre de sources (codes entiers ; aucun taux). Dose non nulle : procédure de Holm
     sur les deux contrastes (M4, M5) et lecture du seul contraste de l'héritage au seuil de 0,05 (M13) ; dose nulle : règle de
@@ -154,25 +256,34 @@
     return sha
 
 
-def ecrire_sorties(dossier, nom, case, sorties, lectures, grille):
+def ecrire_sorties(dossier, nom, case, sorties, lectures, grille, registre_source=None, en_plus=None):
     """Sorties brutes scellées d'une case : un fichier `.npy` par tableau, un fichier de description, chacun avec son compagnon
-    `.sha256` ; jamais d'écrasement. Rend {fichier : empreinte}."""
+    `.sha256` ; jamais d'écrasement. Rend {fichier : empreinte}. Code v6 : chaque sortie d'un bras est écrite à son type
+    (`TYPES_DES_SORTIES` ; une sortie inconnue arrête) ; les sorties du registre de la course source, s'il y en a, sous le nom
+    `source-<champ>.npy` ; la description porte en plus `en_plus` (mode, sources par tirage ou lot de sources)."""
     d = os.path.join(dossier, nom)
     os.makedirs(d)
     empreintes = {}
     for b in sorted(sorties):
         for champ in sorted(sorties[b]):
+            if champ not in TYPES_DES_SORTIES:
+                raise ArretTirages(f"sortie de bras inconnue : {champ}")
             chemin = os.path.join(d, f"{champ}-bras-{b}.npy")
             with open(chemin, "xb") as fh:
-                np.save(fh, np.ascontiguousarray(sorties[b][champ].astype(np.int16)), allow_pickle=False)
+                np.save(fh, np.ascontiguousarray(sorties[b][champ].astype(TYPES_DES_SORTIES[champ])), allow_pickle=False)
             empreintes[os.path.basename(chemin)] = _sceller(chemin)
     for champ in sorted(lectures):
         chemin = os.path.join(d, f"lecture-{champ}.npy")
         with open(chemin, "xb") as fh:
             np.save(fh, np.ascontiguousarray(lectures[champ]), allow_pickle=False)
         empreintes[os.path.basename(chemin)] = _sceller(chemin)
+    for champ in sorted(registre_source or {}):
+        chemin = os.path.join(d, f"source-{champ}.npy")
+        with open(chemin, "xb") as fh:
+            np.save(fh, np.ascontiguousarray(registre_source[champ]), allow_pickle=False)
+        empreintes[os.path.basename(chemin)] = _sceller(chemin)
     desc = {k: v for k, v in case.items() if k != "config"}
-    desc.update(config=case["config"], grille=list(grille), fichiers=empreintes, version=VERSION)
+    desc.update(config=case["config"], grille=list(grille), fichiers=empreintes, version=VERSION, **(en_plus or {}))
     chemin = os.path.join(d, "case.json")
     with open(chemin, "x", encoding="utf-8") as fh:
         fh.write(json.dumps(desc, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
@@ -181,6 +292,8 @@
 
 
 def nom_de_case(case, prefixe=""):
+    """Le nom du dossier d'une case. Code v6 : le nom d'une case du mode « sources » finit par `-sources` (celui d'une case du
+    mode « tirages » est celui du code v5)."""
     morceaux = [case["famille"], case["proposeur"], f"dose{case['dose']}", f"taux{case['taux']}"]
     for k in ("taille", "force"):
         if case.get(k) is not None:
@@ -191,17 +304,31 @@
         morceaux.append(f"repere{case['repere']}")
     if case.get("repli"):
         morceaux.append("repli")
+    if "sources" in case:
+        morceaux.append("sources")
     return prefixe + "-".join(morceaux)
 
 
-def jouer_case(graines, couche, case, f, tirages, dossier, prefixe="", grille=None):
+def jouer_case(graines, couche, case, f, tirages, dossier, prefixe="", grille=None, sources_par_tirage=None):
     """Simule, lit et écrit une case ; rend les empreintes. Aucune case n'est lue ici : le programme d'analyse lit après que
-    toutes sont calculées et scellées (étape 8)."""
+    toutes sont calculées et scellées (étape 8). Code v6 : `sources_par_tirage` (par défaut le plus grand nombre lu) permet de
+    simuler la case entière et de n'en lire que certains nombres (tirage de confirmation, étape 9)."""
     grille = grille or grille_de(case["dose"], avec_m13=case["famille"] == "B")
-    S = max(grille)
+    S = sources_par_tirage or max(grille)
+    if S < max(grille):
+        raise ArretTirages(f"un nombre lu ({max(grille)}) au-delà des sources simulées par tirage ({S})")
     sorties = simuler_case(graines, couche, case, f, tirages, S)
     lectures = lire_case(sorties, case["dose"], grille, case["bras"])
-    return ecrire_sorties(dossier, nom_de_case(case, prefixe), case, sorties, lectures, grille)
+    return ecrire_sorties(dossier, nom_de_case(case, prefixe), case, sorties, lectures, grille,
+                          en_plus={"mode": "tirages", "sources_par_tirage": S})
+
+
+def jouer_case_sources(graines, couche, case, f, sources, dossier, prefixe=""):
+    """Code v6 (point 1 de l'audit) : simule et écrit une case du mode « sources » — aucune lecture par tirage, aucun taux ; les
+    écarts se calculent au programme d'analyse. Rend les empreintes."""
+    sorties, registre = simuler_case_sources(graines, couche, case, f, sources)
+    return ecrire_sorties(dossier, nom_de_case(case, prefixe), case, sorties, {}, (), registre_source=registre,
+                          en_plus={"mode": "sources", "lot_de_sources": LOT_DE_SOURCES})
 
 
 def essai_de_forme(graines, case, f, tirages, nombres_de_sources, dossier):
@@ -304,13 +431,70 @@
     return True
 
 
-def lancer_famille(graines, couche, cases, f_par_case, tirages, dossier, commit, fichiers_geles):
-    """Étape 8 (ou 9) : toutes les cases d'un lancement, écrites et scellées ; un manifeste. Rend les empreintes par case."""
+def verifier_cases(couche, cases):
+    """Code v6 (points 2 et 3 de l'audit) : contrôle d'un lancement, avant l'autorisation et avant toute dérivation. Chaque case a
+    une et une seule des clés « tirages » et « sources » (`mode_de`) ; deux cases n'ont jamais le même nom (le nom porte le mode)
+    ; sous la couche « decisif », chaque case a la taille gelée de son mode (10 000 tirages emboîtés ; 200 000 sources) et lit
+    toute sa grille ; sous la couche « confirmation », seules les cases de C1 et de C4 se tirent, au mode « tirages », à 100 000
+    tirages, chacune avec les nombres de sources à lire (`nombres_lus`) ; des nombres lus sont toujours dans la grille de la case ;
+    une case du mode « sources » qui a les bras 4a ou 4b n'a aucun lot d'une seule source. Rend {nom : (mode, nombre)} ; arrêt
+    nommé sinon (`ArretTirages`), rien n'étant créé ni dérivé."""
+    plan = {}
+    for case in cases:
+        mode, n = mode_de(case)
+        nom = nom_de_case(case)
+        if nom in plan:
+            raise ArretTirages(f"deux cases au même nom : {nom} (le nom porte le mode ; B8) : arrêt avant tout tirage")
+        if couche == "decisif":
+            gelee = TIRAGES_PAR_CASE if mode == "tirages" else SOURCES_FAMILLES_GRANDES
+            if n != gelee or "nombres_lus" in case:
+                raise ArretTirages(f"couche « decisif » : la case {nom} doit être tirée à la taille gelée de son mode ({gelee} "
+                                   f"{mode}) et lue sur toute sa grille (reçu {n}) : arrêt")
+        if couche == "confirmation" and (mode != "tirages" or n != TIRAGES_CONFIRMATION or "nombres_lus" not in case
+                                         or (case["famille"], case["proposeur"]) not in CASES_DE_CONFIRMATION):
+            raise ArretTirages(f"couche « confirmation » : seules les cases de C1 et de C4 se tirent, à {TIRAGES_CONFIRMATION} "
+                               f"tirages, avec leurs nombres lus (reçu {nom}, {n} {mode}) : arrêt")
+        if "nombres_lus" in case:
+            lus = case["nombres_lus"]
+            if mode != "tirages" or not lus or not set(lus) <= set(grille_de(case["dose"], avec_m13=case["famille"] == "B")):
+                raise ArretTirages(f"case {nom} : nombres lus hors de sa grille ({lus!r}) : arrêt")
+        if mode == "sources" and any(b in ("4a", "4b") for b in case["bras"]):
+            dernier = n - LOT_DE_SOURCES * ((n - 1) // LOT_DE_SOURCES)
+            if min(LOT_DE_SOURCES, dernier) < 2:
+                raise ArretTirages(f"case {nom} : un lot d'une seule source n'a pas de source étrangère (B7 bis) : arrêt")
+        plan[nom] = (mode, n)
+    if not plan:
+        raise ArretTirages("lancement sans aucune case : arrêt")
+    return plan
+
+
+def lancer_famille(graines, couche, cases, f_par_case, dossier, commit, fichiers_geles, cases_non_atteignables=None,
+                   en_plus=None):
+    """Étape 8 (ou 9) : toutes les cases d'un lancement, écrites et scellées ; un manifeste. Rend les empreintes par case.
+    Code v6 (point 3 de l'audit ; B8, étape 8 : « toutes les familles, en un seul lancement ») : chaque case est tirée au nombre
+    que porte sa clé, `tirages` (tirages emboîtés) ou `sources` (mode « sources ») — aucun nombre commun n'est reçu ; les cases de
+    tous les modes se tirent dans ce seul appel, sous un seul manifeste, qui inscrit le nombre de chaque case, et, s'ils sont
+    donnés, les cases « non atteignables » et les champs `en_plus` ; `verifier_cases` contrôle le lancement avant l'autorisation
+    et avant toute dérivation. Une case de tirages qui porte `nombres_lus` est simulée entière (le plus grand nombre de sa grille)
+    et lue à ces seuls nombres."""
+    plan = verifier_cases(couche, cases)
     exiger_autorisation_pour(couche, graines)
     os.makedirs(dossier)
     out = {}
     for case in cases:
-        out[nom_de_case(case)] = jouer_case(graines, couche, case, f_par_case(case), tirages, dossier)
-    ecrire_manifeste(os.path.join(dossier, "manifeste.json"), {"couche": couche, "tirages": tirages,
-                                                                "cases": sorted(out)}, graines, commit, fichiers_geles)
+        nom = nom_de_case(case)
+        mode, n = plan[nom]
+        if mode == "tirages":
+            S = max(grille_de(case["dose"], avec_m13=case["famille"] == "B"))
+            lus = tuple(sorted(case["nombres_lus"])) if "nombres_lus" in case else None
+            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, sources_par_tirage=S)
+        else:
+            out[nom] = jouer_case_sources(graines, couche, case, f_par_case(case), n, dossier)
+    configuration = {"couche": couche, "cases": sorted(out),
+                     "tirages_par_case": {k: v for k, (m, v) in sorted(plan.items()) if m == "tirages"},
+                     "sources_par_case": {k: v for k, (m, v) in sorted(plan.items()) if m == "sources"}}
+    if cases_non_atteignables is not None:
+        configuration["cases_non_atteignables"] = list(cases_non_atteignables)
+    configuration.update(en_plus or {})
+    ecrire_manifeste(os.path.join(dossier, "manifeste.json"), configuration, graines, commit, fichiers_geles)
     return out
````

#### `2-etapes.py.diff`

````diff
--- code-v5/src/controle_ia/heritage_etage_processeur_v1/etapes.py
+++ code-v6/src/controle_ia/heritage_etage_processeur_v1/etapes.py
@@ -11,23 +11,40 @@
   l'étape 4 ; il joue `etape_4`, puis, dans le même lancement, le jeu de la garde 27 avec le lecteur réglé pour la tenue (τ = 2)
   et trois sources (remarque 3 de l'annexe H, « Version 9 », tranchée par la mère, version 10).
 - `etape_6_bis_et_7` : la couche mécanique rejouée aux réglages gelés sous des étiquettes disjointes, puis la garde S8 (ii).
-- `etape_8` : les tirages décisifs de toutes les cases, en un seul lancement, aucune case lue avant que toutes soient
-  écrites et scellées ; `cases_a_confirmer` et `etape_9` : la règle de C1 et de C4.
+- `cases_a_confirmer` (code v4) : la règle de retrait de C1 et de C4 sur des comptes donnés (plus de 500 rejets sur 10 000).
+- `etape_8` (code v6 ; audit des trous du code v5, point 5 ; le code v5 la nommait ici sans la définir) : relit les fichiers
+  gelés des étapes 5 et 6 après contrôle de leurs empreintes (fréquences : `frequences.lire_gelees` ; réglages :
+  `etalonnage.lire_reglages_geles`, avec leur compagnon), construit le plan des cases, puis tire toutes les cases, des deux
+  modes (tirages emboîtés ; 200 000 sources), en un seul appel de `tirages.lancer_famille` sous la couche « decisif » et un
+  seul manifeste, qui inscrit les empreintes vérifiées des fichiers gelés et les cases « non atteignables » ; aucune case n'est
+  lue.
+- `etape_9` (code v6 ; audit, point 6) : après l'étape 8, et seulement sur ses sorties scellées (manifeste vérifié, toutes ses
+  cases scellées), les comptes de C1 et de C4 (`comptes_de_niveau` : `analyse.lire_case`, `analyse.taux_par_nombre`,
+  `cases_de_niveau`), les cases à confirmer (`cases_a_confirmer`), changées en cases (`cases_de_confirmation` : la case de la
+  famille, simulée entière et lue aux seuls nombres retirés), tirées à 100 000 tirages sous la couche « confirmation », dans un
+  dossier et un manifeste à part ; puis leur statut (`statuts_de_confirmation`, `intervalles.regle_de_confirmation`). Rien
+  n'est écrit si aucune case ne dépasse 500 rejets.
 
 Les tailles et la couche de graines sont des paramètres : les essais du code les jouent réduites sous la couche « essai » ; les
-valeurs gelées sont les défauts. Les couches « decisif » et « confirmation » exigent une autorisation (module `graines`).
+valeurs gelées sont les défauts. Les couches « decisif » et « confirmation » exigent une autorisation (module `graines`) ; sous
+elles, `tirages.lancer_famille` refuse toute taille autre que gelée.
 """
 
+import json
 import os
 
 import numpy as np
 
+from . import analyse as AN
 from . import equivalence as EQ
+from . import etalonnage as ET
 from . import frequences as FR
 from . import mecanique as MC
 from . import mondes as MO
 from . import proposeurs as P
-from .constantes import (DOSE_JEU_GARDE_27, DOSES, DOSES_NON_NULLES, FORCES_GENERALISTE, FORCES_SUIVEUR, FORCE_REFERENCE_SUIVEUR,
+from . import tirages as TI
+from .constantes import (CASES_C1, CASES_C4, DOSE_JEU_GARDE_27, DOSES, DOSES_NON_NULLES, FORCES_GENERALISTE, FORCES_SUIVEUR,
+                         FORCE_REFERENCE_SUIVEUR,
                          GRILLE_SOURCES, GRILLE_SOURCES_DOSE_NULLE, PROPOSEUR_JEU_GARDE_27, REGLAGES_ETAPE_4, REPERES_LECTURE,
                          SEUIL_DE_RETRAIT_SUR_10000, SOURCES_COUCHE_MECANIQUE, SOURCES_FAMILLES_GRANDES, SOURCES_JEU_GARDE_27,
                          SOURCES_SOUS_ENSEMBLE_ORGANISME, TAILLES,
@@ -307,3 +324,174 @@
 
 
 TIRAGES_DE_CONFIRMATION = TIRAGES_CONFIRMATION
+
+
+# --- étapes 8 et 9 (code v6 ; audit des trous du code v5, points 5 et 6) ---------------------------------------------------------
+
+
+def _exiger_fichier_gele(chemin):
+    """Règle R11 : un fichier gelé et son compagnon sont vérifiés sur disque avant d'être relus ; arrêt nommé sinon."""
+    if not os.path.isfile(chemin) or not os.path.isfile(chemin + ".sha256"):
+        raise ArretEtapes(f"fichier gelé ou son compagnon absent sur disque : {chemin} : arrêt (règle R11)")
+    return True
+
+
+def relire_fichiers_geles(chemin_frequences, sha_frequences, chemin_reglages, sha_reglages):
+    """Étapes 8 et 9 : relit les fichiers gelés des étapes 5 et 6, chacun après contrôle de son empreinte et de son compagnon
+    (`frequences.lire_gelees` ; `etalonnage.lire_reglages_geles`). Rend (fréquences, lignes des réglages, empreintes vérifiées
+    à inscrire au manifeste)."""
+    _exiger_fichier_gele(chemin_frequences)
+    _exiger_fichier_gele(chemin_reglages)
+    f = FR.lire_gelees(chemin_frequences, sha_frequences)
+    lignes = ET.lire_reglages_geles(chemin_reglages, sha_reglages)
+    return f, lignes, {"frequences": sha_frequences, "reglages": sha_reglages}
+
+
+def reduire(cases, tailles):
+    """Pour les essais du code seulement : les cases du plan, le nombre de chacune remplacé par celui de son mode dans `tailles`
+    ({"tirages": n, "sources": m}). Sous les couches décisives, `tirages.lancer_famille` refuse toute taille autre que gelée."""
+    return [dict(c, **{TI.mode_de(c)[0]: tailles[TI.mode_de(c)[0]]}) for c in cases]
+
+
+def etape_8(graines, dossier, commit, chemin_frequences, sha_frequences, chemin_reglages, sha_reglages, couche="decisif",
+            tailles=None):
+    """Étape 8 (ordre des opérations ; B8) : les tirages décisifs de toutes les familles, en un seul lancement. Relit les fichiers
+    gelés (empreintes contrôlées), construit `plan_des_cases` sur les réglages gelés, tire toutes les cases — tirages emboîtés
+    et cases « sources » — en un seul appel de `tirages.lancer_famille`, sous un seul manifeste qui inscrit les empreintes
+    vérifiées des fichiers gelés et les cases « non atteignables ». Aucune case n'est lue ici. `couche` et `tailles` ne servent
+    qu'aux essais du code (couche « essai », tailles réduites) ; les défauts sont les valeurs gelées. Rend {"cases",
+    "non_atteignables", "manifeste"}."""
+    f, lignes, fichiers = relire_fichiers_geles(chemin_frequences, sha_frequences, chemin_reglages, sha_reglages)
+    cases, non = plan_des_cases(reglages_pour_le_plan(lignes))
+    if tailles is not None:
+        cases = reduire(cases, tailles)
+    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)
+    return {"cases": out, "non_atteignables": non, "manifeste": os.path.join(dossier, "manifeste.json")}
+
+
+def lire_manifeste(dossier):
+    """Le manifeste d'un lancement, après `tirages.verifier_manifeste` (sceau, liste des étiquettes, champs du verrou). Rend
+    (manifeste, son empreinte)."""
+    chemin = os.path.join(dossier, "manifeste.json")
+    TI.verifier_manifeste(chemin)
+    octets, sha = TI._lire_scelle(chemin)
+    return json.loads(octets.decode("utf-8")), sha
+
+
+def comptes_de_niveau(dossier_8, manifeste):
+    """Étape 9 : les comptes de C1 et de C4, depuis les sorties scellées de l'étape 8 seulement. Toutes les cases que le
+    manifeste nomme sont d'abord contrôlées (description scellée ; aucun dossier de case hors du manifeste) ; puis chaque case de
+    la famille A, et de la famille C pour les deux sourds, est relue (`analyse.lire_case`, empreintes vérifiées) et comptée
+    (`analyse.taux_par_nombre`) : rejets de la procédure (`lecture-rejette`) pour C1, déclenchements de la règle de validité
+    (`lecture-declenche`) pour C4. Les clés sont celles de `cases_de_niveau` ; des comptes incomplets (moins de 72 cases pour
+    l'un des critères) arrêtent. Rend (comptes de C1, comptes de C4, tirages par clé, descriptions des cases)."""
+    noms = list(manifeste["configuration"]["cases"])
+    sur_disque = sorted(n for n in os.listdir(dossier_8) if os.path.isdir(os.path.join(dossier_8, n)))
+    if sorted(noms) != sur_disque:
+        raise ArretEtapes(f"étape 9 : les dossiers de l'étape 8 ne sont pas ceux que son manifeste nomme : arrêt")
+    descs = {}
+    for nom in noms:
+        octets, _ = TI._lire_scelle(os.path.join(dossier_8, nom, "case.json"))
+        descs[nom] = json.loads(octets.decode("utf-8"))
+    c1, c4 = cases_de_niveau(list(descs.values()))
+    comptes_c1, comptes_c4, tirages = {}, {}, {}
+    for nom, d in sorted(descs.items()):
+        if d["famille"] == "A":
+            lecture, cible, cle = "lecture-rejette", comptes_c1, (lambda k, d=d: (k, d["dose"], d["taux"]))
+        elif d["famille"] == "C" and d["proposeur"] in ("sourd-egal", "sourd-paie"):
+            lecture, cible, cle = "lecture-declenche", comptes_c4, (lambda k, d=d: (k, d["proposeur"], d["taux"]))
+        else:
+            continue
+        desc, tab = AN.lire_case(os.path.join(dossier_8, nom))
+        for k, v in AN.taux_par_nombre(tab[lecture], desc["grille"]).items():
+            cible[cle(k)] = v["compte"]
+            tirages[cle(k)] = v["tirages"]
+    if (len(c1) != CASES_C1 or len(c4) != CASES_C4 or sorted(comptes_c1, key=str) != sorted(c1, key=str)
+            or sorted(comptes_c4, key=str) != sorted(c4, key=str)):
+        raise ArretEtapes(f"étape 9 : comptes de C1 ou de C4 incomplets ({len(comptes_c1)} et {len(comptes_c4)} cases, "
+                          f"{CASES_C1} et {CASES_C4} attendues) : arrêt")
+    return comptes_c1, comptes_c4, tirages, descs
+
+
+def cases_de_confirmation(a_confirmer, descs, tirages=TIRAGES_CONFIRMATION):
+    """Étape 9 : les triplets de `cases_a_confirmer` changés en cases. Un triplet (« C1 », k, dose, taux) désigne la case de la
+    famille A à cette dose et à ce taux ; (« C4 », k, proposeur, taux), la case de la famille C de ce sourd à ce taux. Chaque case
+    désignée est retirée une fois, entière (le plus grand nombre de sa grille), en `tirages` tirages emboîtés de graines neuves
+    (couche « confirmation »), et lue aux seuls nombres retirés (`nombres_lus`) ; plusieurs nombres d'une même case se lisent
+    dans les mêmes tirages. La configuration est celle du proposeur, égale à celle que la case de l'étape 8 porte ; arrêt
+    sinon."""
+    groupes = {}
+    for t in a_confirmer:
+        if t[0] == "C1":
+            cle = ("A", "sourd-egal", float(t[2]), float(t[3]))
+        elif t[0] == "C4":
+            cle = ("C", t[2], 0.0, float(t[3]))
+        else:
+            raise ArretEtapes(f"étape 9 : triplet inconnu {t!r}")
+        groupes.setdefault(cle, set()).add(int(t[1]))
+    cases = []
+    for (famille, proposeur, dose, taux), ks in sorted(groupes.items(), key=str):
+        d = [x for x in descs.values() if x["famille"] == famille and x["proposeur"] == proposeur and x["dose"] == dose
+             and x["taux"] == taux and x.get("mode") == "tirages"]
+        if len(d) != 1:
+            raise ArretEtapes(f"étape 9 : case de l'étape 8 introuvable ou double pour {famille}, {proposeur}, {dose}, {taux}")
+        config = P.configuration(proposeur)
+        if d[0]["config"] != config:
+            raise ArretEtapes(f"étape 9 : configuration de la case {famille}/{proposeur} différente de celle de l'étape 8")
+        cases.append({"famille": famille, "proposeur": proposeur, "config": config, "dose": dose, "taux": taux,
+                      "bras": tuple(d[0]["bras"]), "tirages": tirages, "nombres_lus": tuple(sorted(ks))})
+    return cases
+
+
+def statuts_de_confirmation(a_confirmer, comptes_c1, comptes_c4, tirages_8, comptes_confirmation):
+    """C1 et C4 : le statut de chaque case retirée, par `intervalles.regle_de_confirmation` (via
+    `analyse.statut_case_de_niveau`) — « en échec » si le tirage de confirmation compte au moins 5 236 rejets sur 100 000,
+    « tenue » sinon. Rend {triplet : statut}."""
+    out = {}
+    for t in a_confirmer:
+        cle = tuple(t[1:])
+        compte = (comptes_c1 if t[0] == "C1" else comptes_c4)[cle]
+        out[tuple(t)] = AN.statut_case_de_niveau(compte, tirages_8[cle], comptes_confirmation[tuple(t)])
+    return out
+
+
+def etape_9(graines, dossier_8, dossier, commit, chemin_frequences, sha_frequences, chemin_reglages, sha_reglages,
+            couche="confirmation", tirages=TIRAGES_CONFIRMATION):
+    """Étape 9 (ordre des opérations ; C1 et C4) : les tirages de confirmation, s'il y en a, lancés par programme. Le manifeste
+    de l'étape 8 est vérifié et doit être de la couche « decisif » (de la couche des essais, pour eux) et porter les empreintes des
+    fichiers gelés présentés, relus et contrôlés ; les comptes de C1 et de C4 viennent de ses seules sorties scellées
+    (`comptes_de_niveau`) ; les cases de plus de 500 rejets sur 10 000 (`cases_a_confirmer`) sont changées en cases
+    (`cases_de_confirmation`) et tirées par `tirages.lancer_famille` sous la couche « confirmation », dans un dossier neuf et un
+    manifeste à part, qui inscrit les triplets retirés et l'empreinte du manifeste de l'étape 8 ; ce n'est qu'ensuite, ces
+    sorties scellées, qu'elles sont relues et que le statut de chaque case est calculé (`statuts_de_confirmation`). Aucune
+    case à confirmer : rien n'est écrit. `couche` et `tirages` ne servent qu'aux essais du code. Rend {"comptes_c1",
+    "comptes_c4", "a_confirmer", "cases", "comptes_de_confirmation", "statuts", "manifeste"}."""
+    m8, sha_m8 = lire_manifeste(dossier_8)
+    if couche == "decisif" or m8["configuration"].get("couche") != ("decisif" if couche == "confirmation" else couche):
+        raise ArretEtapes(f"étape 9 : le manifeste de l'étape 8 est de la couche {m8['configuration'].get('couche')!r}, "
+                          f"incompatible avec la couche {couche!r} : arrêt")
+    f, _, fichiers = relire_fichiers_geles(chemin_frequences, sha_frequences, chemin_reglages, sha_reglages)
+    if m8.get("fichiers_geles") != fichiers:
+        raise ArretEtapes("étape 9 : les fichiers gelés présentés ne sont pas ceux que le manifeste de l'étape 8 inscrit : arrêt")
+    comptes_c1, comptes_c4, tirages_8, descs = comptes_de_niveau(dossier_8, m8)
+    a_confirmer = cases_a_confirmer(comptes_c1, comptes_c4)
+    resultat = {"comptes_c1": comptes_c1, "comptes_c4": comptes_c4, "a_confirmer": a_confirmer, "cases": {},
+                "comptes_de_confirmation": {}, "statuts": {}, "manifeste": None}
+    if not a_confirmer:
+        return resultat
+    cases = cases_de_confirmation(a_confirmer, descs, tirages)
+    resultat["cases"] = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers,
+                                          en_plus={"a_confirmer": [list(t) for t in a_confirmer],
+                                                   "manifeste_de_l_etape_8_sha256": sha_m8})
+    resultat["manifeste"] = os.path.join(dossier, "manifeste.json")
+    comptes = {}
+    for case in cases:
+        desc, tab = AN.lire_case(os.path.join(dossier, TI.nom_de_case(case)))
+        t = AN.taux_par_nombre(tab["lecture-rejette" if case["famille"] == "A" else "lecture-declenche"], desc["grille"])
+        for tri in a_confirmer:
+            if (tri[0] == "C1" and case["famille"] == "A" and (float(tri[2]), float(tri[3])) == (case["dose"], case["taux"])) or (
+                    tri[0] == "C4" and case["famille"] == "C" and (tri[2], float(tri[3])) == (case["proposeur"], case["taux"])):
+                comptes[tuple(tri)] = t[int(tri[1])]["compte"]
+    resultat["comptes_de_confirmation"] = comptes
+    resultat["statuts"] = statuts_de_confirmation(a_confirmer, comptes_c1, comptes_c4, tirages_8, comptes)
+    return resultat
````

#### `3-graines.py.diff`

````diff
--- code-v5/src/controle_ia/heritage_etage_processeur_v1/graines.py
+++ code-v6/src/controle_ia/heritage_etage_processeur_v1/graines.py
@@ -38,8 +38,11 @@
 
 COUCHES = ("etalonnage", "mecanique", "mecanique-reglages", "audit", "essai-de-forme", "essai", "decisif", "confirmation")
 COUCHES_DECISIVES = ("decisif", "confirmation")
-ORDRE_DES_CHAMPS = ("couche", "famille", "proposeur", "dose", "taille", "force", "taux", "retrait", "repere", "bras", "jumelle",
-                    "tirage", "lot", "source", "generation", "monde", "role", "essai", "tour")
+# Code v6 (audit des trous du code v5, point 1) : le champ `mode` (« sources » pour les cases du mode « sources » de B8 ; jamais
+# écrit au mode « tirages ») s'insère après `repere`. Une étiquette ne porte que les champs qu'on lui donne, dans cet ordre :
+# toute étiquette sans le champ `mode` est celle du code v5, à l'octet, et aucune graine existante ne change.
+ORDRE_DES_CHAMPS = ("couche", "famille", "proposeur", "dose", "taille", "force", "taux", "retrait", "repere", "mode", "bras",
+                    "jumelle", "tirage", "lot", "source", "generation", "monde", "role", "essai", "tour")
 
 # Journal du processus : chaque dérivation (couche, étiquette) ; chaque refus de dérivation décisive.
 JOURNAL = []
````

#### `4-etalonnage.py.diff`

````diff
--- code-v5/src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
+++ code-v6/src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
@@ -187,6 +187,26 @@
     return sha
 
 
+def lire_reglages_geles(chemin, sha_attendue):
+    """Code v6 (point 5 de l'audit ; étape 8, règle R11) : relit le fichier gelé des réglages après contrôle de son empreinte — le
+    fichier et son compagnon existent sur disque ; le compagnon porte une seule ligne « <empreinte>  <nom de base> » ;
+    l'empreinte recalculée du fichier, celle du compagnon et l'empreinte attendue sont égales — puis rejoue la garde 22 sur ses
+    lignes. Rend les lignes des réglages ; arrêt (`ArretEtalonnage`) sinon, jamais de repli."""
+    if not os.path.isfile(chemin) or not os.path.isfile(chemin + ".sha256"):
+        raise ArretEtalonnage(f"fichier des réglages gelé ou son compagnon absent : {chemin} : arrêt (règle R11)")
+    with open(chemin, "rb") as f:
+        octets = f.read()
+    with open(chemin + ".sha256", encoding="ascii") as f:
+        lignes_compagnon = [l for l in f.read().split("\n") if l.strip()]
+    sha = hashlib.sha256(octets).hexdigest()
+    attendue_au_compagnon = f"{sha_attendue}  {os.path.basename(chemin)}"
+    if len(lignes_compagnon) != 1 or lignes_compagnon[0] != attendue_au_compagnon or sha != sha_attendue:
+        raise ArretEtalonnage(f"fichier des réglages d'empreinte inattendue, ou compagnon non conforme : {chemin} : arrêt")
+    lignes = json.loads(octets)["reglages"]
+    verifier_sortie(lignes)
+    return lignes
+
+
 def taille_realisee(ecart_moyen_decisif, ecart_type_gele):
     """M9 : la taille réalisée d'une case décisive est son écart moyen divisé par l'écart-type entre jumelles gelé."""
     return ecart_moyen_decisif / ecart_type_gele
````

#### `5-test_heritage_etage_processeur_v1_statistique.py.diff`

````diff
--- code-v5/tests/test_heritage_etage_processeur_v1_statistique.py
+++ code-v6/tests/test_heritage_etage_processeur_v1_statistique.py
@@ -125,9 +125,13 @@
 def test_couches_decisives_refusees_sans_autorisation(tmp_path):
     case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
             "bras": ("1", "2", "3")}
+    # code v6 : chaque case porte son nombre (clé « tirages ») ; aux tailles gelées de chaque couche décisive (et, pour la
+    # confirmation, avec ses nombres lus), le lancement passe le contrôle des cases et c'est l'autorisation qui le refuse
+    tailles = {"decisif": {"tirages": 10_000}, "confirmation": {"tirages": 100_000, "nombres_lus": (10,)}}
     for couche in ("decisif", "confirmation"):
         with pytest.raises(GR.GraineRefusee):
-            TI.lancer_famille(graines(), couche, [case], lambda c: FREQUENCES_D_ESSAI, 10, str(tmp_path / couche), "0" * 40, {})
+            TI.lancer_famille(graines(), couche, [dict(case, **tailles[couche])], lambda c: FREQUENCES_D_ESSAI,
+                              str(tmp_path / couche), "0" * 40, {})
         assert not os.path.exists(tmp_path / couche)
         with pytest.raises(GR.GraineRefusee):
             TI.simuler_case(graines(), couche, case, FREQUENCES_D_ESSAI, 1)
@@ -140,7 +144,7 @@
     import json
     case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
             "bras": ("1", "2", "3")}
-    TI.lancer_famille(graines(), "essai", [case], lambda c: FREQUENCES_D_ESSAI, 2, str(tmp_path / "run"), "0" * 40,
+    TI.lancer_famille(graines(), "essai", [dict(case, tirages=2)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), "0" * 40,
                       {"frequences": "a" * 64})
     m = json.loads((tmp_path / "run" / "manifeste.json").read_text(encoding="utf-8"))
     assert set(m) >= {"configuration", "configuration_sha256", "versions", "racine", "etiquettes", "commit", "fichiers_geles"}
````

#### `6-test_heritage_etage_processeur_v1_verrou.py.diff`

````diff
--- code-v5/tests/test_heritage_etage_processeur_v1_verrou.py
+++ code-v6/tests/test_heritage_etage_processeur_v1_verrou.py
@@ -133,8 +133,8 @@
     for couche in GR.COUCHES_DECISIVES:
         assert TI.exiger_autorisation_pour(couche, g)
     case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
-            "bras": ("1", "2", "3")}
-    TI.lancer_famille(g, "essai", [case], lambda c: FREQUENCES_D_ESSAI, 2, str(tmp_path / "run"), COMMIT_ESSAI, {})
+            "bras": ("1", "2", "3"), "tirages": 2}
+    TI.lancer_famille(g, "essai", [case], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT_ESSAI, {})
     chemin_m = str(tmp_path / "run" / "manifeste.json")
     with open(chemin_m, encoding="utf-8") as f:
         m = json.load(f)
````

#### `7-test_heritage_etage_processeur_v1_lancement.py.diff`

````diff
--- /dev/null
+++ code-v6/tests/test_heritage_etage_processeur_v1_lancement.py
@@ -0,0 +1,481 @@
+"""Essais du code v6 (audit des trous du code v5, « Ce que le code v6 doit porter », points 1 à 7 ; préenregistrement v13, B8,
+ordre des opérations, étapes 8 et 9, C1 et C4, « Ce qui est rapporté ») — chaque point avec son cas sain et son artefact
+(règle R5) :
+- point 1 : le mode « sources » sous son propre champ d'étiquette, sans qu'aucune graine existante ne change ;
+- point 2 : le mode dans le nom des cases ; deux cases au même nom arrêtent avant tout tirage ;
+- point 3 : `lancer_famille` suit la clé de chaque case, tire toutes les familles et tous les modes en un seul appel, sous un
+  seul manifeste ; tailles gelées sous les couches décisives ;
+- point 4 : le reliquat par bras, et, au repli du mode « sources », la part des entrées gardées et les facteurs
+  d'enrichissement (`statistique.enrichissement`), dans les sorties scellées ;
+- point 5 : `etape_8`, fichiers gelés relus sous le contrôle de leurs empreintes, plan entier réduit (essai de forme) ;
+- point 6 : `etape_9`, comptes de C1 et de C4 depuis les sorties scellées, cases à confirmer, tirage de confirmation à part.
+Toutes les graines sont de la couche « essai » ; les fichiers gelés sont factices (jamais ceux des étapes 5 et 6) ; aucune
+graine décisive n'est dérivée (l'essai final le contrôle) ; aucun taux n'est lu sur un tirage simulé."""
+
+import json
+import os
+import shutil
+
+import numpy as np
+import pytest
+
+from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, graines, prop
+from controle_ia.heritage_etage_processeur_v1 import analyse as AN
+from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
+from controle_ia.heritage_etage_processeur_v1 import etapes as EP
+from controle_ia.heritage_etage_processeur_v1 import frequences as FR
+from controle_ia.heritage_etage_processeur_v1 import graines as GR
+from controle_ia.heritage_etage_processeur_v1 import statistique as ST
+from controle_ia.heritage_etage_processeur_v1 import tirages as TI
+from controle_ia.heritage_etage_processeur_v1.constantes import (CLASSES, DOSES_NON_NULLES, GRILLE_SOURCES,
+                                                                GRILLE_SOURCES_DOSE_NULLE, LOT_DE_SOURCES,
+                                                                SOURCES_FAMILLES_GRANDES, TAILLES, TAUX_ECHEC_TOUS,
+                                                                TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE)
+
+# l'ordre des champs d'étiquette du code v5, recopié ici à part du module `graines`
+ORDRE_DU_CODE_V5 = ("couche", "famille", "proposeur", "dose", "taille", "force", "taux", "retrait", "repere", "bras", "jumelle",
+                    "tirage", "lot", "source", "generation", "monde", "role", "essai", "tour")
+COMMIT = "0" * 40
+TAILLES_REDUITES = {"tirages": 2, "sources": 24}
+
+
+def _case(famille, proposeur, dose, **kw):
+    c = {"famille": famille, "proposeur": proposeur, "config": prop(proposeur, **kw.pop("reglage", {})), "dose": dose,
+         "taux": 0.25, "bras": ("1", "2", "3")}
+    c.update(kw)
+    return c
+
+
+def _d(mode, n):
+    return _case("D", "lecteur-heritage", 0.5, reglage={"K": 64}, taille=1.0, repli=True, **{mode: n})
+
+
+def _h(mode, n, proposeur="sourd-paie"):
+    return _case("H", proposeur, 0.25, bras=("1", "2", "3", "4a", "4b"), **{mode: n})
+
+
+def _e(n, retrait="v2"):
+    return _case("E", "sourd-paie", 0.25, bras=("2", "3"), retrait=retrait, repere=0.05, sources=n)
+
+
+def _a(n, dose=0.25, taux=0.25):
+    return dict(_case("A", "sourd-egal", dose), taux=taux, tirages=n)
+
+
+def _v5(etiquette):
+    """L'étiquette rejointe dans l'ordre du code v5 (le champ `mode` retiré s'il y est)."""
+    champs = dict(x.split("=", 1) for x in etiquette.split("|"))
+    champs.pop("mode", None)
+    return "|".join(f"{k}={champs[k]}" for k in ORDRE_DU_CODE_V5 if k in champs)
+
+
+# --- fichiers gelés factices (jamais ceux des étapes 5 et 6) ---------------------------------------------------------------
+
+
+def _lignes_de_reglages(non_atteignables=()):
+    valeurs = {"K": lambda d, t: 32.0 * t, "tau": lambda d, t: 0.9 * t,
+               "phi": lambda d, t: {0.5: 0.4, 1.0: 0.9, 1.5: 1.5}[t], "gamma": lambda d, t: {0.25: 0.1, 0.5: 0.2, 1.0: 0.5, 1.5: 0.9}[t]}
+    lignes = []
+    for nom, r, dose, cible in EP.cibles_d_etalonnage():
+        non = (r, dose, cible) in non_atteignables
+        lignes.append({"proposeur": nom, "nom_du_reglage": r, "dose": dose, "cible": cible, "reglage": valeurs[r](dose, cible),
+                       "atteignable": not non, "statut": "non atteignable" if non else "atteint"})
+    lignes.append({"proposeur": "sourd-egal", "dose": 0.25, "taux": 0.25, "ecart_type_jumelles": 1.0})  # ligne sans réglage
+    return lignes
+
+
+def _fichiers_geles(dossier, non_atteignables=(("K", 0.25, 1.5),)):
+    os.makedirs(dossier, exist_ok=True)
+    comptes = {"vraie-source": {"engagees": 4, "tiennent": 4},
+               "criblage": {"vraies_examinees": 2, "vraies_retenues": 2, "autres_examinees": 5, "autres_passees": 2},
+               "tentatives_par_classe": {c: 1 for c in CLASSES}}
+    cf, cr = os.path.join(dossier, "frequences-essai.json"), os.path.join(dossier, "reglages-essai.json")
+    sf = FR.geler(cf, FREQUENCES_D_ESSAI, comptes, {"essai": True})
+    sr = ET.geler_reglages(cr, _lignes_de_reglages(non_atteignables), {"essai": True})
+    return cf, sf, cr, sr
+
+
+@pytest.fixture(scope="module")
+def etape_8_reduite(tmp_path_factory):
+    """L'étape 8 sur le plan entier, réduit (deux tirages par case, 24 sources par case « sources »), couche « essai »."""
+    base = tmp_path_factory.mktemp("etape-8")
+    cf, sf, cr, sr = _fichiers_geles(str(base / "geles"))
+    g = graines()
+    r = EP.etape_8(g, str(base / "etape-8"), COMMIT, cf, sf, cr, sr, couche="essai", tailles=TAILLES_REDUITES)
+    return {"base": base, "geles": (cf, sf, cr, sr), "resultat": r, "graines": g, "dossier": str(base / "etape-8")}
+
+
+# --- point 1 : le champ de mode des étiquettes -------------------------------------------------------------------------------
+
+
+def test_point_1_mode_dans_les_etiquettes_aucune_graine_existante_ne_change(tmp_path):
+    """Cas sain : l'ordre des champs, privé de `mode`, est celui du code v5 ; une case du mode « tirages » dérive exactement les
+    étiquettes du code v5 (aucun champ `mode`) ; la case du mode « sources » de mêmes paramètres dérive les mêmes étiquettes au
+    seul champ `mode=sources` près, et leurs graines sont disjointes. Artefact : ces étiquettes privées du champ `mode` ont des
+    graines communes avec celles du mode « tirages » (`exiger_couches_disjointes` arrête) — le champ est ce qui les sépare."""
+    assert tuple(c for c in GR.ORDRE_DES_CHAMPS if c != "mode") == ORDRE_DU_CODE_V5 and "mode" in GR.ORDRE_DES_CHAMPS
+    assert GR.etiquette(couche="essai", famille="A", proposeur="sourd-egal", dose=0.25, taux=0.25, lot=0, bras="1",
+                        role="echantillonnage") == \
+        "couche=essai|famille=A|proposeur=sourd-egal|dose=0.25|taux=0.25|bras=1|lot=0|role=echantillonnage"
+    gt, gs = graines(), graines()
+    TI.lancer_famille(gt, "essai", [_d("tirages", 2)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "t"), COMMIT, {})
+    TI.lancer_famille(gs, "essai", [_d("sources", 30)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "s"), COMMIT, {})
+    assert gt.etiquettes and all("mode=" not in e and _v5(e) == e for e in gt.etiquettes)
+    assert gs.etiquettes and all("|mode=sources|" in e for e in gs.etiquettes)
+    assert sorted(_v5(e) for e in gs.etiquettes) == sorted(gt.etiquettes)  # un lot ici : lot=0 des deux côtés
+    assert GR.exiger_couches_disjointes(gt.etiquettes, gs.etiquettes)
+    with pytest.raises(GR.GraineRefusee, match="graine commune"):
+        GR.exiger_couches_disjointes(gt.etiquettes, [_v5(e) for e in gs.etiquettes])
+    # au mode « sources », un lot par tranche de 2 000 sources, chacun sous son étiquette
+    g2 = graines()
+    TI.lancer_famille(g2, "essai", [_h("sources", LOT_DE_SOURCES + 3)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "h"),
+                      COMMIT, {})
+    assert sorted({e.split("|lot=")[1].split("|")[0] for e in g2.etiquettes}) == ["0", "1"]
+    sortie = np.load(tmp_path / "h" / TI.nom_de_case(_h("sources", 1)) / "M1-bras-4b.npy")
+    assert sortie.shape == (LOT_DE_SOURCES + 3,)
+
+
+# --- point 2 : le mode dans le nom des cases -----------------------------------------------------------------------------------
+
+
+def test_point_2_nom_de_case_porte_le_mode(tmp_path):
+    """Cas sain : D et H dans les deux modes, dans un même appel — quatre dossiers distincts, le nom du mode « sources » finit par
+    `-sources`, celui du mode « tirages » est celui du code v5. Artefact : deux cases au même nom arrêtent avant tout tirage
+    (arrêt nommé, aucun dossier créé, aucune graine dérivée), au lieu de l'erreur de dossier existant du code v5."""
+    cases = [_d("tirages", 2), _d("sources", 20), _h("tirages", 2), _h("sources", 20)]
+    noms = [TI.nom_de_case(c) for c in cases]
+    assert len(set(noms)) == 4 and noms[1] == noms[0] + "-sources" and noms[3] == noms[2] + "-sources"
+    assert noms[0] == "D-lecteur-heritage-dose0.5-taux0.25-taille1.0-repli"
+    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT, {})
+    assert sorted(d for d in os.listdir(tmp_path / "run") if os.path.isdir(tmp_path / "run" / d)) == sorted(noms)
+    g = graines()
+    with pytest.raises(TI.ArretTirages, match="deux cases au même nom"):
+        TI.lancer_famille(g, "essai", [_d("tirages", 2), _d("tirages", 3)], lambda c: FREQUENCES_D_ESSAI,
+                          str(tmp_path / "double"), COMMIT, {})
+    assert not os.path.exists(tmp_path / "double") and g.etiquettes == []
+
+
+# --- point 3 : un lancement, la clé de chaque case, un manifeste ---------------------------------------------------------------
+
+
+def test_point_3_lancer_famille_suit_la_cle_de_chaque_case_un_seul_manifeste(tmp_path):
+    """Cas sain : des cases de nombres différents, des deux modes, tirées dans un seul appel : chacune à son nombre (forme des
+    sorties), un seul manifeste, qui inscrit le nombre de chaque case. Artefacts : une case sans clé, une case aux deux clés, un
+    nombre non entier ou nul — arrêt nommé avant tout tirage."""
+    cases = [_a(2), dict(_a(3), taux=0.5), _e(37), _d("sources", 45), _h("tirages", 2)]
+    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT, {"x": "a" * 64})
+    formes = {TI.nom_de_case(c): np.load(tmp_path / "run" / TI.nom_de_case(c) / "M1-bras-2.npy").shape for c in cases}
+    assert list(formes.values()) == [(2, 48), (3, 48), (37,), (45,), (2, 48)]
+    manifestes = [os.path.join(r, f) for r, _, fs in os.walk(tmp_path / "run") for f in fs if f.startswith("manifeste")
+                  and f.endswith(".json")]
+    assert manifestes == [str(tmp_path / "run" / "manifeste.json")]
+    m = json.loads((tmp_path / "run" / "manifeste.json").read_text(encoding="utf-8"))
+    conf = m["configuration"]
+    assert conf["tirages_par_case"] == {TI.nom_de_case(c): c["tirages"] for c in cases if "tirages" in c}
+    assert conf["sources_par_case"] == {TI.nom_de_case(c): c["sources"] for c in cases if "sources" in c}
+    assert conf["cases"] == sorted(formes) and "tirages" not in conf and TI.verifier_manifeste(str(tmp_path / "run" /
+                                                                                                    "manifeste.json"))
+    sans = {k: v for k, v in _a(2).items() if k != "tirages"}
+    for mauvaise, motif in ((sans, "une et une seule"), (dict(_a(2), sources=10), "une et une seule"),
+                            (_a(0), "invalide"), (dict(_a(2), tirages=2.0), "invalide"), (dict(_a(2), tirages=True), "invalide")):
+        with pytest.raises(TI.ArretTirages, match=motif):
+            TI.lancer_famille(graines(), "essai", [_a(2), mauvaise], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "x"),
+                              COMMIT, {})
+        assert not os.path.exists(tmp_path / "x")
+    with pytest.raises(TI.ArretTirages, match="aucune case"):
+        TI.lancer_famille(graines(), "essai", [], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "x"), COMMIT, {})
+
+
+def test_point_3_tailles_gelees_sous_les_couches_decisives(tmp_path):
+    """Cas sain (contrôle seul, sans dérivation) : aux tailles gelées, les cases de la couche « decisif » passent le contrôle ; à la
+    couche « confirmation », une case de C1 ou de C4 à 100 000 tirages, avec ses nombres lus. Artefacts : une taille réduite sous
+    « decisif », des nombres lus sous « decisif », une case hors de C1 et de C4, une case « sources », une case sans nombres lus ou
+    à 10 000 tirages sous « confirmation », des nombres lus hors de la grille, un lot d'une seule source au bras 4a : arrêt nommé ;
+    et un lancement décisif réduit est refusé par ce contrôle avant toute autorisation (aucun dossier, aucun refus consigné)."""
+    gelees = [_a(TIRAGES_PAR_CASE), _e(SOURCES_FAMILLES_GRANDES), _h("sources", SOURCES_FAMILLES_GRANDES)]
+    assert set(TI.verifier_cases("decisif", gelees).values()) == {("tirages", 10_000), ("sources", 200_000)}
+    conf = dict(_a(TIRAGES_CONFIRMATION), nombres_lus=(10, 48))
+    c4 = dict(_case("C", "sourd-paie", 0.0, bras=("2", "3")), tirages=TIRAGES_CONFIRMATION, nombres_lus=(5,))
+    assert TI.verifier_cases("confirmation", [conf, c4])
+    artefacts = [("decisif", [_a(9_999)]), ("decisif", [_e(1_000)]), ("decisif", [dict(_a(TIRAGES_PAR_CASE), nombres_lus=(10,))]),
+                 ("confirmation", [dict(_case("B", "sourd-egal", 0.25), tirages=TIRAGES_CONFIRMATION, nombres_lus=(10,))]),
+                 ("confirmation", [dict(_e(TIRAGES_CONFIRMATION), famille="A", proposeur="sourd-egal", nombres_lus=(10,))]),
+                 ("confirmation", [_a(TIRAGES_CONFIRMATION)]), ("confirmation", [dict(_a(TIRAGES_PAR_CASE), nombres_lus=(10,))]),
+                 ("essai", [dict(_a(2), nombres_lus=(11,))]), ("essai", [dict(_e(2), nombres_lus=(10,))]),
+                 ("essai", [_h("sources", LOT_DE_SOURCES + 1)])]
+    for couche, cases in artefacts:
+        with pytest.raises(TI.ArretTirages):
+            TI.verifier_cases(couche, cases)
+    refus = list(GR.REFUS)
+    with pytest.raises(TI.ArretTirages, match="taille gelée"):
+        TI.lancer_famille(graines(), "decisif", [_a(2)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "d"), COMMIT, {})
+    assert not os.path.exists(tmp_path / "d") and GR.REFUS == refus
+    with pytest.raises(GR.GraineRefusee):
+        TI.lancer_famille(graines(), "decisif", gelees, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "d"), COMMIT, {})
+    assert not os.path.exists(tmp_path / "d")
+    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()
+
+
+# --- point 4 : reliquat et enrichissement dans les sorties scellées --------------------------------------------------------------
+
+
+def _resimuler(case, n, taille_tirage=None):
+    """La même simulation que le lancement (même lot 0, mêmes étiquettes), rejouée directement."""
+    g = graines()
+    base = TI.champs_de_la_case(case)
+    role = base.pop("role", None)
+    etiq = dict(couche="essai", **base, lot=0)
+    cles = {b: g.g(**etiq, bras=b, role="echantillonnage" if role is None else f"echantillonnage-{role}") for b in case["bras"]}
+    return ST.simuler(cles, g.g(**etiq, role="monde"), g.g(**etiq, role="source"), case["config"], case["dose"], case["taux"],
+                      FREQUENCES_D_ESSAI, n, case.get("repere", 0.141), case.get("retrait", "v2"), case.get("repli", False),
+                      taille_tirage=taille_tirage)
+
+
+def test_point_4_reliquat_par_bras_et_enrichissement_du_repli(tmp_path):
+    """Cas sain : chaque case porte, par bras, le reliquat de budget en flottant, égal à celui que rend la simulation rejouée ;
+    la case du repli au mode « sources » (famille D) porte, source par source, les comptes du registre de la course source et
+    la part des entrées gardées et les facteurs d'enrichissement de `statistique.enrichissement`, égaux à ceux de la simulation
+    rejouée ; les autres cases n'en portent pas ; sous la règle de retrait de la version 1, le reliquat est nul. Les sorties se
+    relisent par `analyse.lire_case`, sceaux vérifiés. Artefacts : une sortie de bras inconnue arrête l'écriture ; une sortie
+    altérée après son scellement arrête la relecture."""
+    cases = [_d("sources", 40), _d("tirages", 2), _e(30, retrait="v1"), _h("sources", 25, proposeur="lecteur-tenue")]
+    cases[3]["config"] = prop("lecteur-tenue", tau=1.5)
+    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT, {})
+    d_src, d_tir, e_v1, h_src = (str(tmp_path / "run" / TI.nom_de_case(c)) for c in cases)
+    desc, tab = AN.lire_case(d_src)
+    r = _resimuler(cases[0], 40)
+    for b in ("1", "2", "3"):
+        assert tab[f"reliquat-bras-{b}"].dtype == np.float64 and np.array_equal(tab[f"reliquat-bras-{b}"], r["bras"][b]["reliquat"])
+        assert np.array_equal(tab[f"M1-bras-{b}"], r["bras"][b]["M1"].astype(np.int16))
+    e = ST.enrichissement(r["source"])
+    for k in TI.CHAMPS_D_ENRICHISSEMENT:
+        assert tab[f"source-{k}"].dtype == np.float64 and np.array_equal(tab[f"source-{k}"], e[k], equal_nan=True)
+    assert np.array_equal(tab["source-entrees"], r["source"].n) and np.array_equal(tab["source-entrees_gardees"],
+                                                                                    r["source"].n_gardees)
+    assert np.array_equal(tab["source-lois_vraies_gardees"], r["source"].gardee_v.sum(axis=1))
+    assert sorted(k for k in tab if k.startswith("source-")) == sorted(
+        f"source-{k}" for k in TI.COMPTES_DU_REGISTRE_SOURCE + TI.CHAMPS_D_ENRICHISSEMENT)
+    assert desc["mode"] == "sources" and desc["lot_de_sources"] == LOT_DE_SOURCES and desc["sources"] == 40
+    assert not any(k.startswith("lecture-") for k in tab)  # aucune lecture par tirage au mode « sources »
+    desc_t, tab_t = AN.lire_case(d_tir)
+    rt = _resimuler(cases[1], 2 * 48, taille_tirage=48)
+    assert desc_t["mode"] == "tirages" and desc_t["sources_par_tirage"] == 48
+    assert tab_t["reliquat-bras-3"].shape == (2, 48) and np.array_equal(tab_t["reliquat-bras-3"],
+                                                                       rt["bras"]["3"]["reliquat"].reshape(2, 48))
+    assert not any(k.startswith("source-") for k in tab_t)
+    _, tab_e = AN.lire_case(e_v1)
+    assert np.all(tab_e["reliquat-bras-2"] == 0.0) and not any(k.startswith("source-") for k in tab_e)
+    _, tab_h = AN.lire_case(h_src)
+    assert sorted(k for k in tab_h if k.startswith("reliquat-")) == [f"reliquat-bras-{b}" for b in ("1", "2", "3", "4a", "4b")]
+    # reproductibilité (annexe C) : un second lancement des mêmes cases rend les mêmes octets, case par case, fichier par fichier
+    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run-2"), COMMIT, {})
+    for c in cases:
+        nom = TI.nom_de_case(c)
+        fichiers = sorted(os.listdir(tmp_path / "run" / nom))
+        assert fichiers == sorted(os.listdir(tmp_path / "run-2" / nom))
+        for f in fichiers:
+            assert (tmp_path / "run" / nom / f).read_bytes() == (tmp_path / "run-2" / nom / f).read_bytes(), (nom, f)
+    with pytest.raises(TI.ArretTirages, match="sortie de bras inconnue"):
+        TI.ecrire_sorties(str(tmp_path / "x"), "case", cases[0], {"1": {"inconnue": np.zeros(3)}}, {}, ())
+    with open(os.path.join(d_src, "reliquat-bras-2.npy"), "r+b") as fh:
+        fh.seek(-1, 2)
+        fh.write(b"\x01")
+    with pytest.raises(AN.ArretAnalyse):
+        AN.lire_case(d_src)
+
+
+# --- point 5 : l'étape 8 ------------------------------------------------------------------------------------------------------
+
+
+def test_point_5_etape_8_plan_entier_reduit(etape_8_reduite):
+    """Cas sain (essai de forme du plan entier, réduit) : l'étape 8 relit les fichiers gelés factices sous le contrôle de leurs
+    empreintes, tire toutes les cases du plan, des deux modes, en un seul lancement et un seul manifeste, qui inscrit les
+    empreintes vérifiées des fichiers gelés et la case « non atteignable » ; D et H ont un dossier par mode, E et le point 6 le
+    seul mode « sources » ; seules les cases « sources » portent le champ `mode` dans leurs étiquettes."""
+    r, dossier = etape_8_reduite["resultat"], etape_8_reduite["dossier"]
+    cf, sf, cr, sr = etape_8_reduite["geles"]
+    cases, non = EP.plan_des_cases(EP.reglages_pour_le_plan(_lignes_de_reglages((("K", 0.25, 1.5),))))
+    noms = sorted(TI.nom_de_case(c) for c in cases)
+    assert sorted(r["cases"]) == noms and len(noms) == len(cases)
+    assert sorted(d for d in os.listdir(dossier) if os.path.isdir(os.path.join(dossier, d))) == noms
+    m = json.loads(open(r["manifeste"], encoding="utf-8").read())
+    assert m["fichiers_geles"] == {"frequences": sf, "reglages": sr}
+    assert m["configuration"]["cases_non_atteignables"] == json.loads(json.dumps(non)) and len(non) == 1
+    assert m["configuration"]["couche"] == "essai" and TI.verifier_manifeste(r["manifeste"]) == m["etiquettes"]["nombre"]
+    assert set(m["configuration"]["tirages_par_case"].values()) == {2} and set(m["configuration"]["sources_par_case"].values()) == {24}
+    for famille in ("D", "H"):
+        tir = [n for n in noms if n.startswith(famille + "-") and not n.endswith("-sources")]
+        assert tir and sorted(n + "-sources" for n in tir) == sorted(n for n in noms if n.startswith(famille + "-")
+                                                                     and n.endswith("-sources"))
+    assert all(n.endswith("-sources") for n in noms if n.startswith("E-") or n.startswith("point-6-"))
+    assert len([n for n in noms if n.startswith("E-")]) == 18
+    familles_sources = {e.split("|")[1] for e in etape_8_reduite["graines"].etiquettes if "|mode=sources|" in e}
+    assert familles_sources == {"famille=D", "famille=E", "famille=H", "famille=point-6"}
+    assert all(e.startswith("couche=essai|") for e in etape_8_reduite["graines"].etiquettes)
+
+
+def test_point_5_etape_8_fichiers_geles_controles(tmp_path):
+    """Artefacts : une empreinte attendue des fréquences qui n'est pas la leur ; un fichier des réglages altéré après son
+    scellement ; un compagnon des réglages au mauvais nom ; un fichier gelé absent ; des réglages rescellés qui portent un taux
+    de rejet (garde 22) — chacun arrête avant tout tirage, sans créer le dossier. Et sous la couche « decisif », un plan réduit
+    est refusé par le contrôle des tailles, le plan aux tailles gelées par l'autorisation, sans rien créer ni dériver."""
+    cf, sf, cr, sr = _fichiers_geles(str(tmp_path / "geles"))
+    d = str(tmp_path / "e8")
+    with pytest.raises(FR.ArretFrequences):
+        EP.etape_8(graines(), d, COMMIT, cf, "0" * 64, cr, sr, couche="essai", tailles=TAILLES_REDUITES)
+    with pytest.raises(ET.ArretEtalonnage):
+        EP.etape_8(graines(), d, COMMIT, cf, sf, cr, "1" * 64, couche="essai", tailles=TAILLES_REDUITES)
+    with pytest.raises(EP.ArretEtapes, match="R11"):
+        EP.etape_8(graines(), d, COMMIT, cf, sf, cr + ".absent", sr, couche="essai", tailles=TAILLES_REDUITES)
+    cf2, sf2, cr2, sr2 = _fichiers_geles(str(tmp_path / "geles-2"))
+    with open(cr2 + ".sha256", "w", encoding="ascii") as fh:
+        fh.write(f"{sr2}  autre-nom.json\n")
+    with pytest.raises(ET.ArretEtalonnage, match="compagnon"):
+        EP.etape_8(graines(), d, COMMIT, cf2, sf2, cr2, sr2, couche="essai", tailles=TAILLES_REDUITES)
+    cf3, sf3, cr3, sr3 = _fichiers_geles(str(tmp_path / "geles-3"))
+    with open(cr3, "ab") as fh:
+        fh.write(b" ")
+    with pytest.raises(ET.ArretEtalonnage):
+        EP.etape_8(graines(), d, COMMIT, cf3, sf3, cr3, sr3, couche="essai", tailles=TAILLES_REDUITES)
+    os.makedirs(tmp_path / "geles-4")
+    cr4 = str(tmp_path / "geles-4" / "reglages-essai.json")
+    lignes = _lignes_de_reglages()
+    lignes[0]["taux_de_rejet"] = 0.04
+    octets = (json.dumps({"reglages": lignes, "configuration": {}}, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode()
+    with open(cr4, "wb") as fh:
+        fh.write(octets)
+    import hashlib
+    sr4 = hashlib.sha256(octets).hexdigest()
+    with open(cr4 + ".sha256", "w", encoding="ascii") as fh:
+        fh.write(f"{sr4}  reglages-essai.json\n")
+    with pytest.raises(ET.ArretEtalonnage, match="garde 22"):
+        EP.etape_8(graines(), d, COMMIT, cf, sf, cr4, sr4, couche="essai", tailles=TAILLES_REDUITES)
+    assert not os.path.exists(d)
+    assert ET.lire_reglages_geles(cr, sr) == _lignes_de_reglages((("K", 0.25, 1.5),))  # cas sain
+    with pytest.raises(TI.ArretTirages, match="taille gelée"):
+        EP.etape_8(graines(), d, COMMIT, cf, sf, cr, sr, couche="decisif", tailles=TAILLES_REDUITES)
+    with pytest.raises(GR.GraineRefusee):
+        EP.etape_8(graines(), d, COMMIT, cf, sf, cr, sr)
+    assert not os.path.exists(d)
+    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()
+
+
+# --- point 6 : l'étape 9 ------------------------------------------------------------------------------------------------------
+
+
+def test_point_6_etape_9_apres_l_etape_8_reduite(etape_8_reduite, tmp_path):
+    """Cas sain : sur les sorties scellées de l'étape 8 réduite, les comptes de C1 et de C4 ont leurs 72 cases chacun (aucune ne
+    dépasse 500 rejets à deux tirages) : rien n'est à confirmer, et rien n'est écrit. Artefacts : la couche « confirmation »
+    sur une étape 8 de la couche « essai » ; des fichiers gelés autres que ceux du manifeste ; un dossier de case retiré ; le
+    manifeste de l'étape 8 altéré — chacun arrête avant tout tirage."""
+    cf, sf, cr, sr = etape_8_reduite["geles"]
+    d8 = etape_8_reduite["dossier"]
+    r = EP.etape_9(graines(), d8, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
+    assert len(r["comptes_c1"]) == 72 and len(r["comptes_c4"]) == 72 and r["a_confirmer"] == []
+    assert all(0 <= v <= 2 for v in list(r["comptes_c1"].values()) + list(r["comptes_c4"].values()))
+    assert r["manifeste"] is None and not os.path.exists(tmp_path / "e9")
+    refus = list(GR.REFUS)
+    with pytest.raises(EP.ArretEtapes, match="couche"):
+        EP.etape_9(graines(), d8, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr)
+    assert GR.REFUS == refus
+    cf2, sf2, cr2, sr2 = _fichiers_geles(str(tmp_path / "autres"), non_atteignables=())
+    with pytest.raises(EP.ArretEtapes, match="fichiers gelés"):
+        EP.etape_9(graines(), d8, str(tmp_path / "e9"), COMMIT, cf2, sf2, cr2, sr2, couche="essai", tirages=2)
+    copie = str(tmp_path / "copie-8")
+    shutil.copytree(d8, copie)
+    nom_a = TI.nom_de_case(_a(2))
+    shutil.rmtree(os.path.join(copie, nom_a))
+    with pytest.raises(EP.ArretEtapes, match="dossiers"):
+        EP.etape_9(graines(), copie, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
+    copie2 = str(tmp_path / "copie-8b")
+    shutil.copytree(d8, copie2)
+    with open(os.path.join(copie2, "manifeste.json"), "ab") as fh:
+        fh.write(b" ")
+    with pytest.raises(TI.ArretTirages):
+        EP.etape_9(graines(), copie2, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
+    copie3 = str(tmp_path / "copie-8c")  # la liste des étiquettes altérée, le manifeste intact : `verifier_manifeste` la voit
+    shutil.copytree(d8, copie3)
+    with open(os.path.join(copie3, "manifeste-etiquettes.txt"), "ab") as fh:
+        fh.write(b"\ncouche=essai|famille=ajoutee")
+    with pytest.raises(TI.ArretTirages, match="compagnon"):
+        EP.etape_9(graines(), copie3, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
+    assert not os.path.exists(tmp_path / "e9")
+
+
+def _etape_8_plantee(dossier, geles, plantes, sans=()):
+    """Une étape 8 factice de la couche « essai » : les cases de C1 (famille A) et de C4 (famille C, deux sourds), chacune à
+    10 000 tirages, aux lectures plantées (non tirées) — `plantes` : {(famille, proposeur ou dose, taux, k) : nombre de rejets} —
+    puis un manifeste scellé qui inscrit les fichiers gelés. `sans` : les noms de cases à omettre."""
+    os.makedirs(dossier)
+    cases = [dict(_a(TIRAGES_PAR_CASE, dose, taux)) for dose in DOSES_NON_NULLES for taux in TAUX_ECHEC_TOUS]
+    cases += [dict(_case("C", p, 0.0, bras=("2", "3")), taux=taux, tirages=TIRAGES_PAR_CASE) for p in ("sourd-egal", "sourd-paie")
+              for taux in TAUX_ECHEC_TOUS]
+    noms = []
+    for c in cases:
+        nom = TI.nom_de_case(c)
+        if nom in sans:
+            continue
+        grille = GRILLE_SOURCES if c["famille"] == "A" else GRILLE_SOURCES_DOSE_NULLE
+        lect = np.zeros((TIRAGES_PAR_CASE, len(grille)), dtype=np.int8)
+        for j, k in enumerate(grille):
+            n = plantes.get((c["famille"], c["dose"] if c["famille"] == "A" else c["proposeur"], c["taux"], k), 0)
+            lect[:n, j] = 1
+        sorties = {b: {"M1": np.zeros((TIRAGES_PAR_CASE, 1))} for b in c["bras"]}
+        TI.ecrire_sorties(dossier, nom, c, sorties, {"rejette" if c["famille"] == "A" else "declenche": lect}, grille,
+                          en_plus={"mode": "tirages", "sources_par_tirage": max(grille)})
+        noms.append(nom)
+    cf, sf, cr, sr = geles
+    TI.ecrire_manifeste(os.path.join(dossier, "manifeste.json"), {"couche": "essai", "cases": sorted(noms)}, graines(), COMMIT,
+                        {"frequences": sf, "reglages": sr})
+
+
+def test_point_6_etape_9_sur_des_comptes_plantes(tmp_path):
+    """Cas sain : sur une étape 8 factice aux comptes plantés (501 rejets à 12 sources pour une case de C1, 500 à 10 sources pour
+    la même case, 600 déclenchements à 5 sources pour une case de C4), l'étape 9 retire exactement les deux cases au-dessus de
+    500, chacune simulée entière (48 et 16 sources par tirage) et lue aux seuls nombres retirés, dans un dossier et un manifeste
+    à part qui inscrit les triplets et l'empreinte du manifeste de l'étape 8, puis rend leur statut (« tenue » : deux tirages
+    d'essai). Artefact : une case de C4 absente de l'étape 8 — comptes incomplets, arrêt avant tout tirage."""
+    geles = _fichiers_geles(str(tmp_path / "geles"))
+    plantes = {("A", 0.25, 0.25, 12): 501, ("A", 0.25, 0.25, 10): 500, ("C", "sourd-paie", 0.0, 5): 600}
+    d8 = str(tmp_path / "e8")
+    _etape_8_plantee(d8, geles, plantes)
+    g = graines()
+    r = EP.etape_9(g, d8, str(tmp_path / "e9"), COMMIT, *geles, couche="essai", tirages=2)
+    attendu = sorted([("C1", 12, 0.25, 0.25), ("C4", 5, "sourd-paie", 0.0)], key=str)
+    assert r["a_confirmer"] == attendu and r["comptes_c1"][(12, 0.25, 0.25)] == 501 and r["comptes_c1"][(10, 0.25, 0.25)] == 500
+    assert sorted(r["cases"]) == sorted([TI.nom_de_case(_a(1)), TI.nom_de_case(dict(_case("C", "sourd-paie", 0.0), taux=0.0,
+                                                                                        tirages=1))])
+    m = json.loads(open(r["manifeste"], encoding="utf-8").read())
+    assert m["configuration"]["a_confirmer"] == json.loads(json.dumps(attendu))
+    assert m["configuration"]["manifeste_de_l_etape_8_sha256"] == open(os.path.join(d8, "manifeste.json.sha256")).read().split()[0]
+    desc_a, tab_a = AN.lire_case(str(tmp_path / "e9" / TI.nom_de_case(_a(1))))
+    assert desc_a["nombres_lus"] == [12] and desc_a["grille"] == [12] and tab_a["M1-bras-1"].shape == (2, 48)
+    assert tab_a["lecture-rejette"].shape == (2, 1)
+    desc_c, tab_c = AN.lire_case(str(tmp_path / "e9" / TI.nom_de_case(dict(_case("C", "sourd-paie", 0.0), taux=0.0, tirages=1))))
+    assert desc_c["grille"] == [5] and tab_c["M1-bras-2"].shape == (2, 16) and tab_c["lecture-declenche"].shape == (2, 1)
+    assert set(r["statuts"].values()) == {"tenue"} and set(r["statuts"]) == set(attendu)
+    assert all(e.startswith("couche=essai|") and "mode=" not in e for e in g.etiquettes)
+    d8b = str(tmp_path / "e8-incomplete")
+    _etape_8_plantee(d8b, geles, plantes, sans={TI.nom_de_case(dict(_case("C", "sourd-egal", 0.0), taux=0.5, tirages=1))})
+    with pytest.raises(EP.ArretEtapes, match="incomplets"):
+        EP.etape_9(graines(), d8b, str(tmp_path / "e9b"), COMMIT, *geles, couche="essai", tirages=2)
+    assert not os.path.exists(tmp_path / "e9b")
+
+
+def test_point_6_cases_et_statuts_de_confirmation_sur_des_valeurs_plantees():
+    """Cas sain : deux nombres d'une même case de C1 font une seule case de confirmation, lue à ces deux nombres ; la règle gelée
+    rend « tenue » à 5 235 rejets sur 100 000 et « en échec » à 5 236. Artefacts : une configuration de l'étape 8 qui n'est pas
+    celle du proposeur, un triplet sans case à l'étape 8 : arrêt."""
+    descs = {"a": {"famille": "A", "proposeur": "sourd-egal", "dose": 0.25, "taux": 0.0, "bras": ["1", "2", "3"],
+                   "config": prop("sourd-egal"), "mode": "tirages"}}
+    tri = [("C1", 10, 0.25, 0.0), ("C1", 14, 0.25, 0.0)]
+    cases = EP.cases_de_confirmation(tri, descs)
+    assert len(cases) == 1 and cases[0]["nombres_lus"] == (10, 14) and cases[0]["tirages"] == TIRAGES_CONFIRMATION
+    assert TI.verifier_cases("confirmation", cases)
+    s = EP.statuts_de_confirmation(tri, {(10, 0.25, 0.0): 501, (14, 0.25, 0.0): 600}, {},
+                                   {(10, 0.25, 0.0): 10_000, (14, 0.25, 0.0): 10_000}, {tri[0]: 5_235, tri[1]: 5_236})
+    assert s == {tri[0]: "tenue", tri[1]: "en échec"}
+    with pytest.raises(EP.ArretEtapes, match="configuration"):
+        EP.cases_de_confirmation(tri, {"a": dict(descs["a"], config=prop("sourd-paie"))})
+    with pytest.raises(EP.ArretEtapes, match="introuvable"):
+        EP.cases_de_confirmation([("C4", 5, "sourd-paie", 0.0)], descs)
````

#### `8-mutations_v5.py.diff`

````diff
--- code-v5/outils-dev/mutations_v4.py
+++ code-v6/outils-dev/mutations_v5.py
@@ -23,7 +23,19 @@
 étendu au contenu des audits de lois, zone médiane du contenu qui pose la mention, arrêt sur une exactitude au plus 0,55, égalité
 A = M + 2 σ₀ lue au-dessus, colonnes du seuil (NE-3), plis observés reçus de l'appelant, tirés du générateur des permutations ou
 sous le rôle « permutation », chaque condition du verrou, le manifeste, le jeu de la garde 27 (programme de lancement, trois
-sources, source précédente au lieu de suivante)."""
+sources, source précédente au lieu de suivante).
+
+Version 5 (code v6 ; audit des trous du code v5, « Ce que le code v6 doit porter », points 1 à 7) : les 113 défauts de la
+version 4, repris à l'identique (remplacements et essais ; leur texte ancien se trouve toujours une seule fois dans le code v6),
+et des défauts neufs pour chaque règle du code v6 — champ de mode absent des étiquettes, écrit aussi au mode « tirages », ordre
+des champs du code v5 changé ; mode absent du nom des cases, doublon non arrêté ; case sans clé ou à deux clés, nombre non
+contrôlé, nombre commun à toutes les cases (tirages ou sources) ; tailles gelées non exigées sous « decisif », confirmation hors
+de C1 et de C4, nombres lus hors de la grille, lot d'une seule source accepté, case de confirmation simulée réduite ; reliquat
+absent ou écrit en entier, enrichissement absent ou mal pris ; étape 8 sans contrôle des fréquences ou des réglages gelés,
+compagnon ou garde 22 des réglages non contrôlés, cases « non atteignables » ou fichiers gelés non inscrits, cases « sources »
+laissées hors du lancement ; étape 9 sans vérification du manifeste de l'étape 8, des dossiers, de la couche, des fichiers
+gelés, des comptes complets, comptes de C4 lus sur les rejets, lancement sans case à confirmer, statut sans le tirage de
+confirmation, nombres lus perdus. Option `--partie v5` : les défauts neufs de cette version."""
 
 import json
 import os
@@ -38,7 +50,8 @@
 else:
     BLOC, TRAVAIL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
     SEULS = set(sys.argv[4:])
-# version 4 : « --partie v3 » (les 71 défauts de la version 3) ou « --partie v4 » (les défauts neufs) au lieu des identifiants
+# version 4 : « --partie v3 » (les 71 défauts de la version 3) ou « --partie v4 » (les défauts neufs) au lieu des identifiants ;
+# version 5 : « --partie v4 » joue les 42 défauts neufs de la version 4, « --partie v5 » ceux de la version 5
 PARTIE = sorted(SEULS)[1] if len(SEULS) == 2 and "--partie" in SEULS else None
 PAQUET = os.path.join("controle_ia", "heritage_etage_processeur_v1")
 T = os.path.join(BLOC, "tests")
@@ -404,6 +417,132 @@
      [('    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
        "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n",
        "    jeu = None\n")], [t("etapes", "lancer_etape_4")]),
+    # --- version 5 (code v6) ---------------------------------------------------------------------------------------------
+    # point 1 : le champ de mode des étiquettes ; aucune graine existante ne change
+    ("mode-absent-des-etiquettes", "point 1 : le mode « sources » sans champ d'étiquette (graines communes aux deux modes)",
+     "tirages.py",
+     [('    if "sources" in case:\n        c["mode"] = "sources"\n', ""),
+      ('    if base.get("mode") != "sources":\n'
+       '        raise ArretTirages("simulation au mode « sources » d\'une case sans clé « sources »")\n', "")],
+     [t("lancement", "point_1")]),
+    ("mode-ecrit-aussi-aux-tirages", "point 1 : le champ de mode écrit aussi au mode « tirages » (graines existantes changées)",
+     "tirages.py",
+     [('    if "sources" in case:\n        c["mode"] = "sources"\n',
+       '    c["mode"] = "sources" if "sources" in case else "tirages"\n')], [t("lancement", "point_1")]),
+    ("ordre-des-champs-du-code-v5-change", "point 1 : l'ordre des champs du code v5 changé avec l'ajout du mode", "graines.py",
+     [('"repere", "mode", "bras",\n                    "jumelle", "tirage", "lot",',
+       '"repere", "mode", "lot", "bras",\n                    "jumelle", "tirage",')], [t("lancement", "point_1")]),
+    # point 2 : le mode dans le nom des cases
+    ("nom-sans-mode", "point 2 : le nom des cases sans le mode (D et H : deux cases au même nom)", "tirages.py",
+     [('    if "sources" in case:\n        morceaux.append("sources")\n', "")], [t("lancement", "point_2")]),
+    ("doublon-non-arrete", "point 2 : deux cases au même nom non arrêtées avant tout tirage", "tirages.py",
+     [('        if nom in plan:\n            raise ArretTirages(f"deux cases au même nom : {nom} (le nom porte le mode ; B8) : '
+       'arrêt avant tout tirage")\n', "")], [t("lancement", "point_2")]),
+    # point 3 : la clé de chaque case, un seul lancement, tailles gelées
+    ("case-sans-cle-acceptee", "point 3 : une case sans clé, ou aux deux clés, prise au mode « tirages »", "tirages.py",
+     [("    presents = [m for m in MODES if m in case]\n", '    presents = [m for m in MODES if m in case][:1] or ["tirages"]\n')],
+     [t("lancement", "point_3")]),
+    ("nombre-non-controle", "point 3 : un nombre nul, non entier ou booléen accepté", "tirages.py",
+     [("    if isinstance(n, bool) or not isinstance(n, int) or n < 1:\n", "    if False:\n")], [t("lancement", "point_3")]),
+    ("tirages-communs-a-toutes-les-cases", "point 3 : un nombre de tirages commun à toutes les cases, la clé ignorée",
+     "tirages.py",
+     [("            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, sources_par_tirage=S)\n",
+       "            out[nom] = jouer_case(graines, couche, case, f_par_case(case), 2, dossier, grille=lus, sources_par_tirage=S)\n")],
+     [t("lancement", "point_3")]),
+    ("sources-communes-a-toutes-les-cases", "point 3 : un nombre de sources commun à toutes les cases, la clé ignorée",
+     "tirages.py",
+     [("            out[nom] = jouer_case_sources(graines, couche, case, f_par_case(case), n, dossier)\n",
+       "            out[nom] = jouer_case_sources(graines, couche, case, f_par_case(case), 24, dossier)\n")],
+     [t("lancement", "point_3")]),
+    ("tailles-gelees-non-exigees", "point 3 : une taille réduite, ou des nombres lus, acceptés sous la couche « decisif »",
+     "tirages.py", [('            if n != gelee or "nombres_lus" in case:\n', "            if False:\n")],
+     [t("lancement", "point_3")]),
+    ("confirmation-hors-de-c1-et-c4", "étape 9 : la couche « confirmation » tire une case hors de C1 et de C4", "tirages.py",
+     [('                                         or (case["famille"], case["proposeur"]) not in CASES_DE_CONFIRMATION):\n',
+       "                                         or False):\n")], [t("lancement", "point_3")]),
+    ("nombres-lus-hors-de-la-grille", "étape 9 : des nombres lus hors de la grille de la case acceptés", "tirages.py",
+     [('            if mode != "tirages" or not lus or not set(lus) <= set(grille_de(case["dose"], avec_m13=case["famille"] == '
+       '"B")):\n', '            if mode != "tirages" or not lus:\n')], [t("lancement", "point_3")]),
+    ("lot-d-une-source-accepte", "point 1 : un lot d'une seule source accepté au mode « sources » (source étrangère sur "
+     "elle-même)", "tirages.py", [("            if min(LOT_DE_SOURCES, dernier) < 2:\n", "            if False:\n")],
+     [t("lancement", "point_3")]),
+    ("confirmation-simulee-reduite", "étape 9 : la case retirée simulée au seul plus grand nombre lu, non entière",
+     "tirages.py",
+     [("            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, sources_par_tirage=S)\n",
+       "            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, "
+       "sources_par_tirage=None)\n")], [t("lancement", "point_6 and plantes")]),
+    # point 4 : reliquat et enrichissement
+    ("reliquat-absent", "point 4 : le reliquat par bras absent des sorties scellées", "tirages.py",
+     [('"fausses_tenues": np.int16, "reliquat": np.float64}', '"fausses_tenues": np.int16}')], [t("lancement", "point_4")]),
+    ("reliquat-en-entier", "point 4 : le reliquat écrit en entier de 16 bits", "tirages.py",
+     [('"reliquat": np.float64}', '"reliquat": np.int16}')], [t("lancement", "point_4")]),
+    ("enrichissement-absent", "point 4 : la part des entrées gardées et l'enrichissement absents des sorties du repli",
+     "tirages.py",
+     [('        if case.get("repli"):\n            for champ, v in sorties_du_registre_source(r["source"]).items():\n',
+       '        if False:\n            for champ, v in sorties_du_registre_source(r["source"]).items():\n')],
+     [t("lancement", "point_4")]),
+    ("enrichissement-mal-pris", "point 4 : le facteur au grain des entrées écrit pour toutes les sorties d'enrichissement",
+     "tirages.py",
+     [("    out.update({k: np.asarray(e[k], dtype=np.float64) for k in CHAMPS_D_ENRICHISSEMENT})\n",
+       '    out.update({k: np.asarray(e["facteur_entrees"], dtype=np.float64) for k in CHAMPS_D_ENRICHISSEMENT})\n')],
+     [t("lancement", "point_4")]),
+    # point 5 : l'étape 8
+    ("etape-8-reglages-sans-compagnon", "point 5 : les réglages gelés relus sans contrôle de leur compagnon", "etalonnage.py",
+     [("    if len(lignes_compagnon) != 1 or lignes_compagnon[0] != attendue_au_compagnon or sha != sha_attendue:\n",
+       "    if sha != sha_attendue:\n")], [t("lancement", "point_5 and controles")]),
+    ("etape-8-reglages-sans-garde-22", "point 5 : les réglages gelés relus sans la garde 22", "etalonnage.py",
+     [("    verifier_sortie(lignes)\n    return lignes\n", "    return lignes\n")], [t("lancement", "point_5 and controles")]),
+    ("etape-8-frequences-non-controlees", "point 5 : le fichier des fréquences relu sans contrôle de son empreinte",
+     "etapes.py",
+     [("    f = FR.lire_gelees(chemin_frequences, sha_frequences)\n",
+       '    f = json.load(open(chemin_frequences, encoding="utf-8"))["frequences"]\n')],
+     [t("lancement", "point_5 and controles")]),
+    ("etape-8-reglages-non-controles", "point 5 : le fichier des réglages relu sans contrôle de son empreinte", "etapes.py",
+     [("    lignes = ET.lire_reglages_geles(chemin_reglages, sha_reglages)\n",
+       '    lignes = json.load(open(chemin_reglages, encoding="utf-8"))["reglages"]\n')],
+     [t("lancement", "point_5 and controles")]),
+    ("etape-8-non-atteignables-non-inscrites", "point 5 : les cases « non atteignables » non inscrites au manifeste",
+     "etapes.py",
+     [("    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)\n",
+       "    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers)\n")],
+     [t("lancement", "point_5 and plan_entier")]),
+    ("etape-8-fichiers-geles-non-inscrits", "point 5 : les empreintes vérifiées des fichiers gelés non inscrites au manifeste",
+     "etapes.py",
+     [("    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)\n",
+       "    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, {}, cases_non_atteignables=non)\n")],
+     [t("lancement", "point_5 and plan_entier")]),
+    ("etape-8-sans-les-cases-sources", "point 5 : l'étape 8 laisse les cases « sources » hors du lancement", "etapes.py",
+     [("    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)\n",
+       '    out = TI.lancer_famille(graines, couche, [c for c in cases if "tirages" in c], lambda c: f, dossier, commit, '
+       "fichiers,\n                            cases_non_atteignables=non)\n")],
+     [t("lancement", "point_5 and plan_entier")]),
+    # point 6 : l'étape 9
+    ("etape-9-manifeste-8-non-verifie", "point 6 : le manifeste de l'étape 8 relu sans `verifier_manifeste`", "etapes.py",
+     [("    TI.verifier_manifeste(chemin)\n    octets, sha = TI._lire_scelle(chemin)\n", "    octets, sha = TI._lire_scelle(chemin)\n")],
+     [t("lancement", "point_6 and apres")]),
+    ("etape-9-dossiers-non-confrontes", "point 6 : les dossiers de l'étape 8 non confrontés à son manifeste", "etapes.py",
+     [("    if sorted(noms) != sur_disque:\n", "    if False:\n")], [t("lancement", "point_6 and apres")]),
+    ("etape-9-comptes-incomplets-acceptes", "point 6 : des comptes de C1 ou de C4 incomplets acceptés", "etapes.py",
+     [("    if (len(c1) != CASES_C1 or len(c4) != CASES_C4 or sorted(comptes_c1, key=str) != sorted(c1, key=str)\n",
+       "    if False and (len(c1) != CASES_C1 or len(c4) != CASES_C4 or sorted(comptes_c1, key=str) != sorted(c1, key=str)\n")],
+     [t("lancement", "point_6 and plantes")]),
+    ("etape-9-c4-lu-sur-les-rejets", "point 6 : les comptes de C4 lus sur les rejets et non sur les déclenchements",
+     "etapes.py",
+     [('            lecture, cible, cle = "lecture-declenche", comptes_c4,', '            lecture, cible, cle = "lecture-rejette", comptes_c4,')],
+     [t("lancement", "point_6")]),
+    ("etape-9-couche-non-controlee", "point 6 : la couche de l'étape 8 non confrontée à celle de l'étape 9", "etapes.py",
+     [('    if couche == "decisif" or m8["configuration"].get("couche") != ("decisif" if couche == "confirmation" else couche):\n',
+       '    if couche == "decisif":\n')], [t("lancement", "point_6 and apres")]),
+    ("etape-9-fichiers-geles-non-confrontes", "point 6 : les fichiers gelés présentés non confrontés au manifeste de l'étape 8",
+     "etapes.py", [('    if m8.get("fichiers_geles") != fichiers:\n', "    if False:\n")], [t("lancement", "point_6 and apres")]),
+    ("etape-9-lance-sans-case-a-confirmer", "point 6 : un lancement de confirmation sans aucune case à confirmer", "etapes.py",
+     [("    if not a_confirmer:\n        return resultat\n", "")], [t("lancement", "point_6 and apres")]),
+    ("etape-9-statut-sans-confirmation", "point 6 : le statut d'une case retirée rendu sans le compte du tirage de "
+     "confirmation", "etapes.py",
+     [("        out[tuple(t)] = AN.statut_case_de_niveau(compte, tirages_8[cle], comptes_confirmation[tuple(t)])\n",
+       "        out[tuple(t)] = AN.statut_case_de_niveau(compte, tirages_8[cle], None)\n")], [t("lancement", "point_6")]),
+    ("etape-9-nombres-lus-perdus", "point 6 : la case retirée sans ses nombres lus (toute la grille lue)", "etapes.py",
+     [('"tirages": tirages, "nombres_lus": tuple(sorted(ks))})', '"tirages": tirages})')], [t("lancement", "point_6")]),
 ]
 # le défaut « strate vide » ne se voit que si la couche statistique ne lève pas non plus à l'emploi : second remplacement
 DEFAUTS[5] = (DEFAUTS[5][0], DEFAUTS[5][1], DEFAUTS[5][2], DEFAUTS[5][3], [t("mecanique", "strate_vide")])
@@ -411,10 +550,13 @@
                                                               "    if v is None:\n        return float(f.get(\"p_tient_non_plantee_base\") or 0.0)\n"
                                                               "        raise ArretFrequences(")])}
 DEFAUTS_DE_LA_VERSION_3 = 71
+DEFAUTS_DE_LA_VERSION_4 = 113
 if PARTIE is not None:
-    if PARTIE not in ("v3", "v4"):
+    if PARTIE not in ("v3", "v4", "v5"):
         raise SystemExit(f"partie inconnue : {PARTIE!r}")
-    SEULS = {d[0] for d in (DEFAUTS[:DEFAUTS_DE_LA_VERSION_3] if PARTIE == "v3" else DEFAUTS[DEFAUTS_DE_LA_VERSION_3:])}
+    TRANCHES = {"v3": DEFAUTS[:DEFAUTS_DE_LA_VERSION_3], "v4": DEFAUTS[DEFAUTS_DE_LA_VERSION_3:DEFAUTS_DE_LA_VERSION_4],
+                "v5": DEFAUTS[DEFAUTS_DE_LA_VERSION_4:]}
+    SEULS = {d[0] for d in TRANCHES[PARTIE]}
 
 
 def env_pour(src):
````

#### `9-lancer_etapes_8_et_9_v1.py.diff`

````diff
--- /dev/null
+++ code-v6/outils-dev/lancer_etapes_8_et_9_v1.py
@@ -0,0 +1,50 @@
+"""NON LANCÉ — EN ATTENTE DU MOT DE LAZAR. Programme de lancement des étapes 8 et 9 du palier 0b (code v6), écrit à part du
+paquet (un fichier de plus dans le paquet ferait refuser le verrou) ; il n'a été exécuté que sur une racine factice, où le verrou
+le refuse avant toute dérivation.
+
+Usage, dossier courant : le dossier du code (celui qui porte `src/`), `PYTHONPATH=src` seul, interpréteur avec `-B` :
+
+    python -B outils-dev/lancer_etapes_8_et_9_v1.py TEXTE RACINE FREQUENCES SHA_FREQUENCES REGLAGES SHA_REGLAGES \
+        DOSSIER_8 DOSSIER_9 COMMIT
+
+- TEXTE, RACINE : le texte présenté et la racine de l'arbre lancé, tels que la pièce de contrôle de la mère les fixe (silence
+  n° 14) ; le verrou (`graines.Autorisation`) les contrôle avec la pièce d'autorisation du verrou et la table du texte ;
+- FREQUENCES, SHA_FREQUENCES, REGLAGES, SHA_REGLAGES : les fichiers gelés des étapes 5 et 6 et leurs empreintes attendues ;
+- DOSSIER_8, DOSSIER_9 : deux dossiers neufs (les sorties scellées et le manifeste de chaque étape) ;
+- COMMIT : le commit du code lancé, inscrit au manifeste (silence n° 8 : la mère le compare à la main, après le lancement).
+
+Il n'a ni paramètre de couche ni paramètre de taille : l'étape 8 tire sous la couche « decisif », aux tailles gelées, toutes les
+cases du plan en un seul lancement ; l'étape 9 lit ses seules sorties scellées et tire, s'il y en a, les cases de C1 et de C4 à
+confirmer sous la couche « confirmation », à 100 000 tirages. Il n'écrit à la sortie standard que les chemins et les empreintes
+des manifestes, et le nombre de cases tirées : aucun taux, aucun compte, aucun statut (ils se lisent à l'étape 10)."""
+
+import os
+import sys
+
+from controle_ia.heritage_etage_processeur_v1 import constantes as K
+from controle_ia.heritage_etage_processeur_v1 import etapes as EP
+from controle_ia.heritage_etage_processeur_v1 import graines as GR
+
+
+def main(arguments):
+    if len(arguments) != 9:
+        raise SystemExit(__doc__)
+    texte, racine, frequences, sha_f, reglages, sha_r, dossier_8, dossier_9, commit = arguments
+    for d in (dossier_8, dossier_9):
+        if os.path.exists(d):
+            raise SystemExit(f"dossier déjà présent : {d} (un dossier neuf est exigé) ; rien n'est lancé")
+    autorisation = GR.Autorisation(texte, racine)
+    graines = GR.Graines(K.RACINE_GRAINES, autorisation=autorisation)
+    r8 = EP.etape_8(graines, dossier_8, commit, frequences, sha_f, reglages, sha_r)
+    print("étape 8 :", r8["manifeste"], open(r8["manifeste"] + ".sha256", encoding="ascii").read().split()[0],
+          len(r8["cases"]), "cases", flush=True)
+    r9 = EP.etape_9(graines, dossier_8, dossier_9, commit, frequences, sha_f, reglages, sha_r)
+    if r9["manifeste"] is None:
+        print("étape 9 : aucune case à confirmer ; rien n'est écrit", flush=True)
+    else:
+        print("étape 9 :", r9["manifeste"], open(r9["manifeste"] + ".sha256", encoding="ascii").read().split()[0],
+              len(r9["cases"]), "cases", flush=True)
+
+
+if __name__ == "__main__":
+    main(sys.argv[1:])
````

## 12. Table entière des empreintes du code v6 (chemins relatifs au dossier `code-v6/` ; ce rapport exclu)

```
0513640b0cbaedcc0e832da8d96f022a3b231ea7cc6eab40062a96714c8629e2  outils-dev/chrono_statistique.py
af772fb9918a3e69ea1bde8a34c0ac68bc8622321e0e600d0d8c8766da02f3d2  outils-dev/chrono_suite.py
fefceead89b91a30eb738e12480ff96c0356c5b2b26f4d4b9d05b5825db737cf  outils-dev/diagnostic_conflits_etrangers.py
5bf7bd44a892ef4fb66981592247131d13fa7ca5e903e4d2cb483a6e9db4d965  outils-dev/diagnostic_etrangere.py
10af2b5ab0e2d88ab9f4a9b395a555044e4ec140108b7c8d20351bf9eb1f5c3e  outils-dev/diagnostic_forme_dependantes.py
8493e5f79964ba75ea8a89b18df3cb8629a25e7570955f0b26aba0a77a0b47ea  outils-dev/diagnostic_import.py
8b2ba07ba7a009b5fab7333e206d9734a6e4de0b943f312c52b2e1cdd1c36ea9  outils-dev/diagnostic_presentation.py
12a2da99ced510c42f03645f4068f14dffa3f86787431cbd7cb67ac3ec85c9cf  outils-dev/empreintes-attendues-palier-0a.txt
b182d5ed92e5e92b7a4a14b26bb47ca4fd80bd0ce9fc916a716d51a61cfaea9e  outils-dev/essai_equivalence.py
580190bfd609195a8e5999401c264b9d8c5842a6bb0571cd28b1cc7df875a8dc  outils-dev/essai_mecanique.py
67052a4b7af9bd02c5f28f3b8a7926fd7b7ac5a98fb797f14b3d6f424bedc2a5  outils-dev/lancer_etapes_8_et_9_v1.py
7254490fe4be80b52fa7cc46e369dbb6fd8d38300265b9a98a82069a0fad56ce  outils-dev/mutations-sortie-v1.json
0f19dd4c146ef3a6df5c6cc95dea9dd343ce53824b9310212657f9b9445a9dc5  outils-dev/mutations-sortie-v2.json
4fae9ca06c1e37a8137aca5c2a610e4158090e61f9be53db7106ef24228bd10e  outils-dev/mutations-v2-sortie-partie-a-v1.json
4c57398668ec03e58b527560216652f67403c0fae16408e9ac8c012060923c80  outils-dev/mutations-v2-sortie-partie-b-v1.json
2e7dfb42bbb98132579a61813b5723102ab937cca892af0c55efcacc4be6f535  outils-dev/mutations-v3-sortie-partie-a-v1.json
1063cad290eb6c17edc39010ab32f3109b3f5f1392ab8b4cf8a43794b5364b96  outils-dev/mutations-v3-sortie-partie-b-v1.json
09fccbd6b9019d62ce428cdf636826775ef772ac67061b8a425a4d4d79a896f8  outils-dev/mutations-v4-sortie-partie-neufs-v1.json
c62360babafb9987bc8806a46ec00fe04a3bb124acd00208e9de99327f8874d8  outils-dev/mutations-v4-sortie-partie-v3-v1.json
f1bd85a8119c54eba8beb6c28255dd68c86237720ba38113b7c696e025cba4d7  outils-dev/mutations-v5-sortie-partie-v3-v1.json
7733704bab9a1190fbe60a0d2def7dd88d0fd74d08829990bad9fa65e6c61ea7  outils-dev/mutations-v5-sortie-partie-v4-v1.json
174b50906ab6dc6327e60762edd39439c3556b0548bc987099b2759f1b463536  outils-dev/mutations-v5-sortie-partie-v5-v1.json
c5476e7b359b2c15b77795832d8f1849dc23bdc6d0aef7386b179170a4123fee  outils-dev/mutations_v1.py
9fd6fc696c49481d8cbbfeae8b795c388a2accaa2a713d55f5f1f0f4b0a20627  outils-dev/mutations_v2.py
ab84bf18bccfac3ec8c10619d2e1c6d4927f84ec2e5e43e124be37e4a842dfd8  outils-dev/mutations_v3.py
90ff3c401a0648080a2e8123ad70be1fed86cd099c21acc093da07f0f8fa0316  outils-dev/mutations_v4.py
82c534be7f1fa25e1c1691f84fe1f55bf704bab976d8cd4198f793e2965eb298  outils-dev/mutations_v5.py
c8a9ed8d7339129d311c787ad5f49c0ef7347c70cfae4b34fabf82f8e6fe6e55  outils-dev/sceller_v1.py
ff647eaf2ead2bd14a1a00a000f09dc142b805fbbeb6aaf87b74f225faaa72d6  outils-dev/verification-empreintes-organisme-v1.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  src/controle_ia/__init__.py
ba3d58e25b499a89d00bf9e2eab524d838297c9214277ba09823b656fe941935  src/controle_ia/heritage_etage_processeur_v1/__init__.py
73c92e370b46e5bc465679a7edc2beed1d6b1f6fc32bcab1116b027c954b13c9  src/controle_ia/heritage_etage_processeur_v1/analyse.py
7b341b6201a9f9809dfcb7e9aab1d5eb32cb7186559c8d9d21b5f270eb634d32  src/controle_ia/heritage_etage_processeur_v1/audit.py
8758b015d523370d6d1a98ff3fdebbe0fdc823805abaf9aa1fd024f48d9d64a7  src/controle_ia/heritage_etage_processeur_v1/comparateur.py
74c477d7d63e168e597b811ed7777a93d3014523d7a722b5e757b5d65d1cde77  src/controle_ia/heritage_etage_processeur_v1/constantes.py
684aeed62fd8ecc902c42e503e8211385e275e5feee36dec6d6e922afc2014bb  src/controle_ia/heritage_etage_processeur_v1/cout.py
2173613ae03067c4ff3090f74644f86550ca1d127702ff41443d1dc6a574a799  src/controle_ia/heritage_etage_processeur_v1/enveloppe.py
fda98bba41c57cbd4860a62d93c7e12f3d23d098f148af0e79b48ec20417eee3  src/controle_ia/heritage_etage_processeur_v1/equivalence.py
240349f7fc76ce5427defde63941a9944669bf48978e6c63a1813c4ff1ecdfe7  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
b3695c506eeeb71d9f3da58ad4fa5a3bf8fcdfe792a9b728bbece415adfea70d  src/controle_ia/heritage_etage_processeur_v1/etapes.py
063df6e1e2c08d79531fce8b76f3e3dbc3fdb002af7657efb1773e33afb9beda  src/controle_ia/heritage_etage_processeur_v1/executeur.py
dce5db04472d049f350f08d56f65a8254fb58eb13f3f2b6a0c3ca2e95952fcd5  src/controle_ia/heritage_etage_processeur_v1/frequences.py
bebabac88975cc25f2f8939e8cb0ba7a166cf1cdfa59b72cb1f3ec694f3d959f  src/controle_ia/heritage_etage_processeur_v1/graines.py
4492c8545f6fc081eb267d851bd24a011fe4817cadad8b9606048bb26208dc1f  src/controle_ia/heritage_etage_processeur_v1/intervalles.py
fb24a9eaffdc98ee080db835d77ee2c419242ad4108ef60b440df8f1cb387536  src/controle_ia/heritage_etage_processeur_v1/lois.py
8c109627d5adf1a97de83f576a662325c628ae5e8bb2f56fb9c98f157f5c847d  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
6ac98e67fc54f66878f66542c08ec6fa76dcfc4ff7ada6b4856baea8e6db6bd3  src/controle_ia/heritage_etage_processeur_v1/mondes.py
fb2f7b48234661c2c825e2dc0c1cb7b9a6f576ff6bdebb3a2196aa3efe9293f1  src/controle_ia/heritage_etage_processeur_v1/organisme.py
e0aa6b89501c4cfeaed67d748db02dba1cb015405c34a91955d70dc2e408ab83  src/controle_ia/heritage_etage_processeur_v1/proposeurs.py
9a386fc7d56cc3f10369ef066e1f9daae7f3e41e592dd9ab4cd2b7b6768c6417  src/controle_ia/heritage_etage_processeur_v1/rangs_signes.py
5e817dfaa7734ef3f607c978f7dcf981c9446de757909600a2001fbbf4101bfb  src/controle_ia/heritage_etage_processeur_v1/registre.py
c0619eb367b94a54ced73a26098c32c1a153b9b298c596e607dd5393b81a1643  src/controle_ia/heritage_etage_processeur_v1/statistique.py
e6d086cf5a663a1494790dcb3e6ca230f704a340d7086816d7f47b5e24f4158e  src/controle_ia/heritage_etage_processeur_v1/tirages.py
372229230356317c51990c0a45ed7e811e37ba2579e7b8c99f8d418bf7dbd236  tests/aides_heritage_etage_processeur_v1.py
618f5ec0319e4107da5d446af3d8a4ff9c14f545facbf5a21dd94a1309cf02b3  tests/test_heritage_etage_processeur_v1_etapes.py
acd1954670935fc87778411602519916af0b7be8e08decce2aa86f7636996d12  tests/test_heritage_etage_processeur_v1_gardes.py
0a4545300abeccf86a7d881bd41c64a44eebec8a7eea588def70bdac6ca9c9b7  tests/test_heritage_etage_processeur_v1_lancement.py
b6486da564025663677d9fe6d0a1eae4a5087018d695b3d03d995482ab570f12  tests/test_heritage_etage_processeur_v1_mecanique.py
e0784e8222e60c408a1ea331972ba9abafec1e98bf758ca1d82ad4d562c3427a  tests/test_heritage_etage_processeur_v1_mondes.py
2697382c1ce050b590d956078796e5c9c5225ea1ad37d08c2ded011a47799461  tests/test_heritage_etage_processeur_v1_organisme.py
51ac18e130e621c83319dae63604fd084064dd95bdade144c18f0ec6551ccdad  tests/test_heritage_etage_processeur_v1_outils.py
bd3fb20ea9dbd20ad6cc48b66a08acd1e6273df450fea06a8209b6ef00c8d527  tests/test_heritage_etage_processeur_v1_statistique.py
6f33487438c0f251b0d46323e09233ea126c108f3ae992b104204c2ca861acba  tests/test_heritage_etage_processeur_v1_verrou.py
d342fa2a4f775085e29dcce8f97cd38b5de1293f7fe9c111a4ca0428df3f3bb4  tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
```

Développeur, modèle O.
