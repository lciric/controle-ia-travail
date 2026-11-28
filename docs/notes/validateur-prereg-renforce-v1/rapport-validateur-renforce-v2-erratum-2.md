# Validateur renforcé des préenregistrements — rapport v2, erratum 2

- **Objet** : rapport `docs/notes/validateur-prereg-renforce-v1/rapport-validateur-renforce-v2.md` (`f775c0f7573960475a50d8df1aeb64f68bcb338c190ad0c248232ea8722ada11`), lu avec son erratum 1 (`rapport-validateur-renforce-v2-erratum-1.md`, `76063ecf046abf58c0fb2ce329c21aa76073511c32627449fcc6d68e42649ace`). Ni l'un ni l'autre n'est réécrit ; cet erratum prime sur les deux pour les points ci-dessous.
- **Cause** : vérification des corrections de la v2 par le contre-lecteur (Claude Sonnet 5.5). Rapport dans le bloc-notes de la session : `verification-corrections-classe-b-validateur-renforce-v1.md`, `6ab430d78fba056e850bc4be27bae0ef10648ba1e145dec9ed84fde083b77064`. Verdict « à corriger », quatre défauts nouveaux (N1 à N4).
- **Auteur** : Opus 5.5, pièce de classe B. Le module `src/controle_ia/prereg_renforce_v2.py` et ses essais sont modifiés sur place, la v2 n'étant pas encore vérifiée.

## 1. Défaut, correction, essai qui la prouve

| défaut | correction | essais (`tests/test_prereg_renforce_v2.py`) |
|---|---|---|
| **N1 (majeur, garde)**. Une empreinte écrite à côté d'un dossier faisait envoyer à `git cat-file --batch`, par `Index.historique`, les versions des fichiers gardés de ce dossier, qui étaient ensuite hachées en mémoire. En plus, un objet qui n'est pas un fichier (un arbre) décalait la lecture du lot | (1) `historique` ne retient du journal git que le chemin cité exact, comparé au chemin relatif au dépôt. Une ligne du journal pour un fichier sous ce chemin, ou pour un chemin gardé, est écartée. `historique` refuse aussi un dossier existant et un chemin gardé, cité ou relatif au dépôt. (2) Une empreinte écrite à côté d'un dossier n'est jamais appariée : avertissement, puis traitement comme empreinte non appariée (connue du dépôt, sinon problème). (3) Les objets passent d'abord par `cat-file --batch-check`, et seuls les objets de type fichier (« blob ») sont demandés à `cat-file --batch`. La lecture du lot avance de la taille de chaque objet ; un objet absent est sauté | `test_n1_dossier_cite_aucun_objet_garde_demande` (dossier existant contenant `iib/` et un `.npz`), `test_n1_historique_d_un_dossier_disparu_filtre_par_chemin` (dossier effacé dont l'historique contient un `.npz`), `test_n1_historique_ne_lit_que_le_chemin_exact`, `test_n1_objet_arbre_jamais_lu_et_lecture_alignee`, `test_n1_historique_appel_direct_sur_un_dossier`. Un espion sur `Index._git` enregistre chaque objet envoyé à `cat-file` ; aucun objet gardé, voisin ou arbre n'y figure |
| **N2 (mineur, régression de (e))**. Les entrées en ligne nue, en liste numérotée ou en table n'étaient plus découpées | `ENTREE` accepte comme début d'entrée : puce, numéro de liste `1.` ou `1)`, cellule de table `\|`, titre `###` à `######` ou gras. Elle accepte aussi une ligne nue « Contre-lecture k » suivie, après une parenthèse courte facultative comme « (R2) », d'un deux-points, d'une virgule, d'un point-virgule ou d'un tiret. Une phrase (« Contre-lecture 3 prévue plus tard ») n'ouvre toujours pas d'entrée | `test_n2_formes_d_entree_v1_decoupees` (7 formes : nue avec deux-points, nue avec tiret, nue avec « (R2) : », nue avec « (R2), », `1. **…**`, `1) …`, table) ; `test_e_phrase_du_corps_n_ouvre_pas_d_entree` reste vert. Sur le dépôt réel, les trois pièces citées par le vérificateur (`prereg/addendum-1-gardes-analyses-r1-v4-v1.md`, `prereg/agregation-r1-v4-v1.md`, `prereg/audit-fuite-r1-v4-v1.md`) sont de nouveau découpées |
| **N4 (mineur)**. Une archive qui a un compagnon, citée avec une empreinte qui ne lui correspond pas, ne donnait qu'un avertissement | Si un compagnon existe pour l'archive citée et ne porte pas l'empreinte : problème « empreinte appariée à l'archive … différente de celle de son compagnon ». L'avertissement ne reste que pour une archive sans compagnon. Le point 1 de l'erratum 1 se lit avec cette précision | `test_n4_archive_avec_compagnon_et_empreinte_fausse` (problème avec une empreinte fausse, rien avec la bonne, aucune archive ouverte) ; `test_artefact_archive_sans_compagnon` reste vert |
| **N3 (mineur)**. Une empreinte séparée de son chemin par un mot, ou écrite avant lui, est acceptée en silence | Correction bon marché proposée par le vérificateur : une empreinte non appariée mais connue, sur une ligne qui cite des fichiers existants dont aucun n'est désigné par elle, donne un avertissement « désigne X, pas un chemin cité sur sa ligne ». Ce n'est pas un problème : une empreinte de manifeste à côté d'un autre fichier est légitime. **Limite documentée** : sans chemin de la ligne qu'elle désigne, une telle empreinte n'est pas vérifiée pour un chemin | `test_n3_empreinte_non_appariee_d_un_autre_fichier_de_la_ligne` (avertissement pour « `src/a.py` signature `<empreinte de autre.py>` » ; rien pour « empreinte `<e>` du fichier `src/autre.py` ») |

**Épreuve par mutants.** 14 mutants propres à ces corrections : filtre de chemin retiré, filtre réduit à la garde, refus d'un dossier dans `historique`, refus d'appariement à un dossier, types d'objets non filtrés, formes d'entrée de la v1, ligne nue, parenthèse avant le séparateur, avertissement N3, problème N4, normalisation de `est_archive`, garde de `historique` (deux variantes). 11 sont tués. Restent trois mutants équivalents, aucun ne survit par manque d'essai :
- « filtre réduit au chemin exact » : le chemin exact a déjà passé `est_garde` ;
- la garde de `historique` sur `rel` et celle sur `rel_depot` se doublent l'une l'autre : chacune, retirée seule, survit.

Les 57 mutants de l'épreuve du rapport v2, rejoués sur le module corrigé : 53 tués tels quels. Quatre ont été réécrits parce que leur motif avait bougé :
- celui de la normalisation de `est_garde`, qui touchait désormais `est_archive`, est tué une fois rejoué sur `est_garde` ;
- celui de la marque « hors dépôt » est tué ;
- celui de la garde de `historique` est l'un des deux mutants équivalents ci-dessus ;
- celui de la ligne nue est remplacé par les mutants de N2.

## 2. Résultats

- `PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v2.py tests/test_prereg*.py` : **247 réussis** (181 essais de la v2).
- Brouillons du 28 novembre : mêmes problèmes (12 et 10). Avertissements nouveaux de N3 : 11 pour G0, 4 pour G1. Exemple : G0, ligne 126, l'empreinte du rapport de contre-lecture est citée à côté d'un nom nu, sur une ligne qui cite d'autres chemins.
- Relevé des 183 préenregistrements scellés : comptes de problèmes inchangés, contrôle par contrôle. 489 avertissements N3 et 7 empreintes écrites à côté d'un dossier.

## 3. Le relevé a-t-il déclenché N1 ?

**Oui pour l'appel, non pour un objet gardé.**
- **Ce qui a été rejoué.** Les relevés faits avec la v2 avant cette correction, dans le même ordre de vérification : les 183 préenregistrements scellés, les deux brouillons, et les copies mutées du lecteur B (deux jeux de 26). Pour savoir quels chemins ils ont passés à `Index.historique`, j'ai rejoué ces relevés avec un `historique` remplacé par un enregistreur.
- **Ce qui a été trouvé.** Sur 668 chemins, trois étaient des dossiers :
  - `brouillons/ordres-t06-e2-e3-v3`,
  - `docs/notes/barreau5-resolution-v1/premiere-lecture/contre-lecture-outils-v1`,
  - `docs/notes/weight-space-programming-v1/repetition-jouet-v9-locale-v4`.
- **Ce qui a été lu.** Le journal git de ces trois dossiers, sur 50 révisions, lu par les noms seulement (`git log --name-only`), compte 3, 14 et 2 fichiers. **Aucun n'est gardé.** Aucun objet gardé n'a donc été envoyé à `cat-file` ni haché en mémoire. Une révision était citée sur la ligne du premier dossier (`1d226d2c`) : son objet était un arbre, c'est-à-dire la liste des noms de ce dossier, jamais un fichier gardé ; il a été lu par le défaut de lecture que N1 corrige aussi.
- **Après correction**, le même rejeu ne passe plus aucun dossier à l'historique.
