# Contre-lecture des mandats de l'ouvreur et du lecteur du verdict du barreau 5 — v1

Contre-lecteur neuf, Claude Opus 5.5, sous-agent du conducteur (`session_013QMayjM1PQPWkLifMw9HDR`), le 22 novembre 2026. Rien lancé, rien commité, rien poussé.

**Verdict : conforme après corrections.** Trois corrections majeures (ouvreur 1 et 2, juge 1) ; sans elles, l'ouvreur s'arrêterait presque à coup sûr au pas 8 ou jouerait le lanceur sous le mauvais interpréteur, et le juge serait lancé sous le mauvais modèle.

Empreintes vérifiées, égales aux compagnons : mandat de l'ouvreur `33cec0c0…f58e`, mandat du juge `245502665…dd52`. Texte scellé `bdff244f…` et addendum 1 `2afa2186…` égaux. Au commit `c76e79169` : lanceur `ae501c55…`, `lecture_v1.py` `ed0999df…`, `engagement_v1.py` `565d4e51…`, tous égaux aux valeurs du mandat.

## Mandat de l'ouvreur

**O-1 (majeur, décision 2 non portée).** Pas 8 : « nom de famille suffixé `-x1` ou `-r1` : arrêt, nœud 3 ; […] tu n'essaies pas d'autre écriture ». Pas 11 : « aucune autre reconstruction n'est essayée ». Nœud 3 : arrêt proposé. Source : le registre propre porte `GO-RELANCE-FORMATION-B5F` « instances 1,2,3,4,5,7 », et le code (`PLAN_INSTANCES`, `prefixe_de_copie`) met T01 à T10 dans les instances 1 à 5. Toutes les familles tenues à l'écart sont donc lues sous `-x1`, et la pièce des sorties les nomme très probablement avec ce suffixe : sous ce mandat, l'arrêt au pas 8 est presque certain. **Correction** : écrire la décision du conducteur. (i) Au pas 8, avant le sel, deux listes écrites et scellées : (a) `couples-b5f-nus-v1.json`, T01 à T10 × {jumeau, saboteur, sur_saboteur}, fixée par le texte et le code, sans lecture de la pièce ; (b) `couples-b5f-formation-v1.json`, recopiée à la lettre de la section de la pièce. Contrôle de (b) : 30 couples, aucun en double, et les noms ramenés à leur base (sans `-x1` ni `-r1`) égalent (a). Si (b) égale (a) à l'octet, un seul essai. (ii) Au pas 11, le programme calcule en mémoire `empreinte_table(table_des_etiquettes(sel, liste))` pour chaque liste, et n'imprime que « (a) égale/différente », « (b) égale/différente ». Il n'écrit la table sous `/dev/shm` que pour (a), et seulement si (a) est égale. (b) égale : arrêt jusqu'à l'erratum de chaîne en conception (traduction contrôlée), aucune table écrite, aucune préparation. Aucune égale : arrêt, liste d'arrêt, point 9, nœud. (iii) Déclarer cet écart à la lettre du pas 11 et à « aucune autre reconstruction », avec l'accord qui le fonde (GO à citer par le conducteur), et retirer le nœud 3.

**O-2 (majeur, jouabilité).** Pas 4 : « `python3 -m venv $BN/racine/.venv`, `pip install -r requirements-cpu.txt` ». Pas 6, 12 et 15 : « `bash scripts/lancer_b5f_lecture_v1.sh …` ». Source : le lanceur joue `PY="${PYTHON_B5F:-python3}"`, donc l'interpréteur du système et non celui de l'environnement, et l'essai `test_lancer_b5f_lecture_v1.py` passe `PYTHON_B5F` lui-même. Dans une session Claude Code, ni une activation ni une variable ne survit d'un appel au suivant. **Correction** : écrire `"$BN"/racine/.venv/bin/pip install -r "$BN"/racine/requirements-cpu.txt` ; faire préfixer chaque appel du lanceur par `PYTHON_B5F=<chemin absolu>/.venv/bin/python` ; jouer pytest par `<…>/.venv/bin/python -m pytest` ; et dire que `$BN` s'écrit en chemin absolu dans chaque commande.

**O-3 (moyen, pas 7 et nœud 2).** « `FORMATION_COMMIT` […] est celui que cite la ligne `SORTIES-FORMATION-B5F` ». Source : cette ligne, au registre propre, ne cite qu'un commit, `3dff7bed46ce62def89dddf835a372f6e2b23b72`. C'est celui de la pièce, sur `formation-b5f/plan-de-marche-v1`. Sa référence dit : « commits prouvés et empreintes des inventaires dans la pièce ». La règle prendrait donc le commit de la pièce pour celui des données, et le contrôle `branch -r --contains` refuserait. **Correction** : `3dff7bed…` sert au `git show` de la pièce (§ 3, point 6 ; l'ajouter au § 2, point 2, avec l'empreinte entière `41e51f9970eda5f4351cac01a41a97296741d5f2ce5e62ba46d56e8af9fc04e6`). `FORMATION_COMMIT` est le commit de la branche réunie `donnees/barreau5-familles-jumelles-v1-formation` que nomme la pièce. Plusieurs commits, ou seulement des commits de branches par instance : nœud 2.

**O-4 (moyen, pas 2 et 14).** Le contrôle « `git diff --quiet c76e7916… HEAD -- src scripts tests` » est plus étroit que celui du code. `exiger_code_de_lecture_au_commit` compare `CHEMINS_GELES` (`harnais/validation_reelle.py`), c'est-à-dire tout le dépôt sauf prereg, brouillons, registres, docs, diag, runs, donnees, livrables, papiers, traces et CLAUDE.md. Un changement de `requirements-cpu.txt` ou de `.claude/` passerait le mandat, puis ferait refuser `ouvrir` après l'inscription de `OUVERTURE-B5F`. **Correction** : faire le même contrôle avec les mêmes exclusions (`-- . ':(exclude)prereg' … ':(exclude)CLAUDE.md'`), aux pas 2 et 14. Vérifié de mon côté : `origin/marche-b5f/lecture-v1` (`2beeec316`) descend de `c76e79169` et lui est égal sur `CHEMINS_GELES`.

**O-5 (moyen, décision 3 à écrire comme prise).** Nœud 1 : « *Proposé* : le conducteur la nomme ». Constat : la branche du conducteur (`conducteur-b5f/lecture-v1`) et `main` ne descendent pas de `c76e79169` ; `marche-b5f/lecture-v1` en descend et porte les lignes à clé jusqu'à `GO-LECTURE-B5F`. **Correction** : écrire la décision dans le § 2 : racine sur une branche qui descend de `c76e79169`, jamais `main` ; `BRANCHE_REGISTRE` nommée dans le signal, vraisemblablement `marche-b5f/lecture-v1`. Le nœud 1 devient une décision.

**O-6 (mineur, pas 5).** Pour `SCORES-B5F`, le mandat n'exige que « d'instant strictement postérieur à celui de `ENGAGEMENT-B5F` ». Le code (`lire_registre_de_lecture`) exige aussi qu'elle suive `EPREUVE-B5F`, `GO-LECTURE-B5F` et `CODE-LECTURE-B5F` ; c'est `GO-LECTURE-B5F` (2026-11-22T19:22:01Z) qui lie. **Correction** : ajouter « et à celui de `GO-LECTURE-B5F` », pour qu'un écart se voie avant l'inscription de l'ouverture.

**O-7 (mineur, pas 6).** « Liste `git ls-tree --name-only <SCORES_COMMIT> donnees/` : un seul nom ». Cette commande rend des chemins préfixés (`donnees/<nom>`). La branche peut aussi porter des dossiers hérités sous `donnees/` (`.gitignore` à `c76e7916` : « Les 59 fichiers déjà suivis sous `donnees/` le restent » ; non vérifié de mon côté, faute d'accès). **Correction** : exiger exactement un nom de la forme `donnees/AAAAMMJJ-HHMMSS-b5f-lecture`, les autres noms étant ignorés.

**O-8 (mineur, décision 4).** § 2, point 1 : la date du dépôt du sel n'y est pas. **Correction** : ajouter « déposé par Lazar après l'inscription de `SCORES-B5F` et avant ta phase 2 ; s'il est déposé plus tôt, tu n'y touches pas avant le signal de la phase 2 ».

**O-9 (mineur, décision 5).** La mère est nommée sans son identifiant. **Correction** : écrire « la mère (`session_013QMayjbmQUdDuDs2S3i3XD`) inscrit `OUVERTURE-B5F` et `LECTURE-B5F` » aux pas 13 et 18 et au nœud 8 (qui devient une décision). Garder le conducteur `session_013QMayjM1PQPWkLifMw9HDR` comme seul interlocuteur.

**O-10 (mineur, cloisonnement).** Au pas 17, la branche poussée porte `entrees/formation.json`, dont le champ `empreintes` donne l'empreinte de chaque adaptateur par (famille, membre). L'arbre de lecture porte, dans `intensites.json`, l'empreinte par nom opaque. Réunis, ils redonnent la table. Le journal `ouvrir-v1.json` porte aussi le code de l'issue. **Correction** : soit déclarer que ces deux fichiers, versés, ne sont ouverts par personne avant le verdict scellé ; soit ne verser `formation.json` et `ouvrir-v1.json` qu'après `VERDICT-B5F` (nœud 5 élargi).

**O-11 (mineur, forme).** En-tête et § 3, point 2 : « lignes 53 à 77 ». La barrière du conducteur va de 53 à 105, et le § 10 dit d'ailleurs « lignes 1 à 52, 106 à 504 ». **Correction** : écrire « lignes 53 à 105, jamais ouvertes ». Ajouter aussi aux exclusions du § 1 « ni le rédacteur ni le contre-lecteur de ce mandat », comme le fait celui du juge.

Gestes vérifiés exacts et jouables :
- les plages de lignes, avec leurs titres attendus (35, 217, 255, 260, 345, 363, 403, 432) ;
- les formats `OUVERTURE-B5F` « table sha256 <64> » et `LECTURE-B5F` « resultat sha256 <64> » (en-tête et regex de `lecture_v1.py`) ;
- l'inscription de l'ouverture avant `ouvrir` ;
- la table jamais versée ;
- la sous-commande `scores` (`ligne_scores` : branche distante `origin/donnees/barreau5-familles-jumelles-v1-lecture`, d'où l'exigence d'aller chercher la branche vers `refs/remotes/origin/…`) ;
- `preparer` et `ouvrir` : arguments, dossiers neufs, commit de 40 signes, sortie standard de `ouvrir` portant le code de l'issue et redirigée ;
- `table_des_etiquettes` et `ecrire_table` : signature, sceau, refus d'écraser ;
- `__pycache__` et `.venv` ignorés : le contrôle « `ls-files --others` sous `src` » passe après pytest.

## Mandat du lecteur du verdict

**J-1 (majeur, décision 1 non portée).** § 1 : « ce rôle revient à Claude Fable 5.2 (nœud 1) » ; nœud 1 : « *Proposé* : Fable 5.2 ». **Correction** : « Lecteur du verdict : Claude Opus 5.5, agent neuf, effort maximal (`GO-2026-11-22-145`, Fable indisponible jusqu'au 29 novembre). Écart déclaré aux règles « Économie de Fable » et « Qui conçoit » de `CLAUDE.md`. » Retirer le nœud 1. La phrase de l'invite système qui nomme le modèle doit dire Opus 5.5.

**J-2 (moyen, pas 4, lecture impossible).** Le pas cite « sonde décisive en échec : issue N, épreuves « non calculables » (texte, point 9) ». Or le § 3, point 2, interdit les lignes 225 à 254, et le point 9 est à la ligne 226. **Correction** : permettre la seule phrase, par `sed -n '226p' … | grep -o "sonde en échec[^;]*;[^.]*"` (« sonde en échec (perte non finie) : ses épreuves sont « non calculables », issue N avec ce motif »), après contrôle du début « 9. **Sondes, toutes fixées ici.** ». Ou renvoyer au seul code (`issue`), qui fait passer ce cas après NI et avant C/S/D/E. L'ordre écrit au pas 4 est exact (vérifié contre `issue`, l. 1037 à 1072).

**J-3 (moyen, pas 7, fausse divergence).** « « dix » devient le nombre de familles présentes quand il diffère ». Le code (`phrases`) remplace aussi « trois autres familles » par le nombre de familles d'apprentissage présentes (`_n(n_app)`). Il prend K de E3 pour la phrase de l'issue, et le nombre des π_k pour la phrase du diagnostic. **Correction** : écrire ces trois substitutions. Sinon, une famille d'apprentissage absente se lirait comme une divergence de fond.

**J-4 (mineur, décision 5).** § 4 et § 6 : « tu envoies au conducteur » ; ni le canal, ni les identifiants, ni la manière de recevoir l'accusé ne sont donnés. **Correction** : conducteur `session_013QMayjM1PQPWkLifMw9HDR` (par `send_message` si le juge est une session ; par le retour de l'agent sinon, l'accusé étant alors dans l'invite de lancement) ; la mère `session_013QMayjbmQUdDuDs2S3i3XD` verse le verdict et inscrit `VERDICT-B5F`.

**J-5 (mineur, décision 3).** Nœud 4 (« *Proposé* : « verdict sha256 <64> » ») : l'écrire comme décidé au § 6 et retirer le nœud. Au § 2 : la branche du registre est celle de l'ouvreur (descend de `c76e79169`, pas `main`).

**J-6 (mineur, pas 2).** La comparaison « les lignes de registre que le résultat recopie […] égalent, clé par clé » ne peut porter que sur l'instant et le contenu : `ouvrir` ne recopie pas la référence. Le dire.

**J-7 (mineur, pas 5).** Pour lire les champs, ajouter à la liste permise du § 3, point 6, les petites fonctions que les épreuves appellent : `somme_rangs_contre`, `comptes_rangs_signes`, `probabilite_au_plus`, `epreuve` (l. 188 à 268). Le recompte reste écrit d'après « Métrique » (l. 160), sans recopier le code.

**J-8 (mineur, exclusions).** Ajouter « ni le contre-lecteur de ce mandat ni celui du mandat de l'ouvreur » : j'ai lu le code de lecture et le texte.

Gestes vérifiés exacts :
- plages et titres (106 « ## Hypothèse », 217, 255, 260, 263 « ## Puissance », 302, 333, 345) ;
- extrait M-6 : un seul « M-6 : » et un seul « ; M-7 » sur la ligne 504, donc le motif glouton est sûr ;
- table des issues et règles de l'addendum (point 1, règles 1 à 4 ; point 2, règle 5 ; point 3) ;
- seuils (l. 185 à 191, 323) ;
- noms des fonctions du § 3, point 6, tous présents à `c76e7916` ;
- addendum lisible en entier : son exposition déclarée (l. 19) ne porte aucun chiffre.

## Ce que j'ai lu, et ce que je n'ai pas lu

Lu :
- les deux mandats ;
- le texte scellé, lignes 1 à 52 et 106 à 504 ;
- l'addendum 1 en entier ;
- à `c76e79169` : le lanceur, `lecture_v1.py` (en-tête, gardes, `issue`, `phrases` en partie, `ouvrir`, `preparer` et suivantes), `engagement_v1.py`, `relecture_v1.py` (`ligne_scores`, `PIECES_LECTURE`, `session scores`), `.gitignore`, `CHEMINS_GELES`, les noms des essais et `requirements-cpu.txt` ;
- le registre propre : ses lignes à clé (branche du conducteur et `origin/marche-b5f/lecture-v1`) ;
- `git branch --contains c76e79169`, qui donne des noms de branches.

Exposition déclarée : un `grep -n "M-6"` a affiché les 80 premiers signes de la ligne 64 (« | 8 | Le brouillon 1 inachevé, son devis, sa fiche, ses simulations v1 »), sans chiffre ni résultat.

Non lu : aucune branche `donnees/*`, `formation-b5f/*`, `course/*`, `traces/*`, ni leurs noms de fichiers ; ni `diag/`, `docs/verdicts/`, `registres/etat.md`, `registres/decisions.md`, les passations ; aucun sel, aucune table, aucun score. Un `git ls-tree c76e79169 donnees/` a été refusé par l'outil ; je ne l'ai pas contourné (voir O-7).
