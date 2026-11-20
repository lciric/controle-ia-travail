# Contre-lecture du code de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») — v2

Écrite le 20 novembre 2026 par le contre-lecteur du code de lecture, Claude Fable 5.2, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument. Mandat `mandat-contre-lecteur-code-lecture-v1.md`, empreinte vérifiée avant lecture : `dc58c25cba4bc1c0c3d46392b98e572c8c310e8c187c95f19b54672f2a68973d`.

Cette v2 est l'état final. La v1 (`contre-lecture-code-lecture-v1.md`, `e8ca26f9…`) reste l'état provisoire, écrit à l'arrêt sur un refus d'outil (R-4046) et versé par la mère ; elle n'est pas modifiée (R12). La mère m'a demandé de reprendre ; le reste du mandat est fait ici.

## Verdict

**Conforme après ces corrections.**

Le calcul qui décide est juste : dénombrement, seuils, mises à l'échelle, table des issues, relecture forcée, notation fermée. Quatre constats majeurs sont à corriger avant le gel, et six mutations sur huit passent sans qu'aucun essai ne les voie : les essais sont à compléter sur ce qui décide.

Aucun constat bloquant : rien ne demande de reprendre la conception.

## Constats majeurs (quatre)

**M-1. Sous l'issue « non interprétable », les sondes sont lues et écrites au résultat.** Rejoué (sondage S1).
- Texte : « Critères de lecture gelés », ligne NI, « rien n'est lu des sondes » ; prédiction P2 ; point 12, étape (b) avant (c).
- Code : `lecture_v1.py`, l. 1194 à 1199 (`lire`). La séparation apprise, les quatre épreuves, le diagnostic et les descriptifs sont calculés quelle que soit la manipulation. Sur un monde à coûts échangeables, le résultat scellé porte dix différences de E3, la sonde de comparaison et les couches 7 et 23, et sa phrase dit « rien n'est lu des sondes ».
- Avant (l. 1195 à 1199) :
  ```
  dec = ch["notations"].get(SONDE_DECISIVE)
  resultat["c_separation_apprise"] = sep = separation_apprise(dec, app, g) if dec is not None else None
  resultat["d_epreuves"] = ep = epreuves(dec, fam, ch["produits"]) if dec is not None else None
  resultat["e_diagnostic"] = diag = diagnostic(ch["notations"], ch["echecs"], fam, app)
  resultat["f_descriptifs"] = desc = descriptifs(ch, fam, app, ep, couts, formation, entropie)
  ```
- Après : si `manip["etablie"]` est faux, `sep` et `ep` valent `None` ; le diagnostic vaut `{"mot": "non lu", "motif": "manipulation non établie : rien n'est lu des sondes"}` ; les descriptifs sont calculés sur une copie de `ch` dont `notations` est vide (intensités, coûts, écritures restent). L'audit de symétrie reste calculé : il supporte déjà `ep` absent.
- Essai à ajouter : monde à coûts échangeables ; `c_separation_apprise` et `d_epreuves` nuls, diagnostic « non lu », ni comparaison ni couches dans les descriptifs.

**M-2. Une famille sans sur-saboteur reste dans M1, alors qu'elle sort de E1.** Rejoué (sondage S2).
- Texte : point 17, « absente de toutes les épreuves » ; « Métrique » nomme M1 et M3 « la même épreuve des rangs signés ».
- Code : `lecture_v1.py`, l. 734 à 737 (`manipulation`, fonction `d`). À dix familles dont une sans sur-saboteur : M1 sur dix familles (somme admise 3), E1 sur neuf (somme admise 1).
- Avant (l. 735 à 736) :
  ```
  return {f: m[f][haut]["m"] - m[f]["jumeau"]["m"] for f in m
          if haut in m[f] and "jumeau" in m[f] and m[f][haut]["m"] is not None and m[f]["jumeau"]["m"] is not None}
  ```
- Après : ajouter la condition `"sur_saboteur" in fam[f]`. Étendre `test_famille_sans_sur_saboteur_absente_de_toutes_les_epreuves` à M1 (neuf familles, seuil 1).
- Si la mère lit que « toutes les épreuves » ne couvre pas M1, c'est au rédacteur du texte de le dire, par addendum.

**M-3. Un fichier `.sha256` qui porte la table passe la garde d'ouverture.** Rejoué (sondage S3).
- Texte : liste d'arrêt, point 8 ; point 11, monde V7, premier cas (« table présente dans l'arbre de lecture » : refus).
- Code : `lecture_v1.py`, l. 285 à 293 (`_fichiers` écarte tout nom finissant par `.sha256`), l. 327 (`exiger_arbre`), l. 365 (`exiger_arbre_sans_etiquettes` n'analyse que `.json` et `.jsonl`). La table sous `table.sha256` ou `scores/notes.sha256` : ouverture faite, issue rendue. La même sous `table.json` : refus.
- Après : dans `exiger_arbre`, tout fichier `.sha256` de l'arbre doit être le compagnon d'un fichier inventorié ou de l'inventaire, et passer `scellement.verifier` ; sinon refus. Essai : cas sain, compagnon orphelin, compagnon d'un autre contenu.

**M-4. Trois pièces de l'ouvreur et de la session n'ont aucun essai (R5).** Vérifié par recherche dans les quatre fichiers d'essais.
- `exiger_code_de_lecture_au_commit` (`lecture_v1.py`, l. 447 à 463) est la garde du point 10 de la liste d'arrêt. Tous les essais ouvrent avec `racine` absente : elle n'est jamais jouée. Mon sondage S4 la trouve juste (trois cas sains acceptés, quatre artefacts refusés) : la garde tient, son essai manque. Le sondage en donne la recette.
- `verifier_avant_creation` (`relecture_v1.py`, l. 816 à 832) : seul le refus d'un commit illisible est essayé.
- `preparer`, `couts_depuis_formation`, `resume_formation_depuis_branche`, `_familles_formees` (`lecture_v1.py`, l. 1294 à 1399) : aucun essai. Ce sont elles qui bâtissent les coûts de M1 et M3 et appliquent la règle de la copie lue. À la lecture, les clés qu'elles lisent sont bien celles qu'écrit le code de formation (`formation_v1.py`, l. 330 à 353 et 1263 à 1305 ; `manifeste.py`, l. 128 à 150). Mais elles supposent que la branche de la formation réunie porte `donnees/<marche>/`, `diag/<marche>/` et `runs/<marche>/manifeste.json` : rien ne l'éprouve.
- Après : un essai sur une branche de formation fabriquée (une marche, une famille, trois membres ; cas sain ; copie `-x1` sans ligne de relance ; résultat « absente »), et un essai de `verifier_avant_creation` sur un dépôt jetable.

## Les essais à compléter : six mutations manquées sur huit

Détail : `outils-contre-lecture-code-lecture-v1/sortie-outils-contre-lecture-v1.md`. Le code est juste sur ces six points ; c'est sa protection qui manque. Aucune n'est équivalente. Un essai par ligne :

| mutation manquée | essai à ajouter |
|---|---|
| C1, probabilité rapportée prise sur la mauvaise somme | valeur exacte de `p_separe` et de `p_contraire` sur un cas écrit à la main (dix familles, deux petites différences contraires : 5 / 1024) |
| C2, issue E sans séparation apprise établie | monde à petits écarts et séparation apprise non établie : issue N, non E |
| C3, issue E sans valeur absolue | monde où une famille a un écart négatif au-delà de la moitié de la séparation apprise, sans « contraire » : issue N |
| C4, épreuve non exigée avant les scores | registre où `EPREUVE-B5F` suit `SCORES-B5F`, puis `OUVERTURE-B5F` : refus |
| C5, table non comparée à `OUVERTURE-B5F` | registre où `OUVERTURE-B5F` cite une autre empreinte que l'engagement : refus |
| C7, tâches de M1 et M3 en réunion | coûts où un membre joue plus de tâches que les autres, à coûts différents : m_i sur les seules tâches communes |

## Constats mineurs (huit)

**m-1. Le niveau de 95 % n'est pas dans la phrase.** Texte, nœud 6 : « dans son nom et dans sa phrase ». `lecture_v1.py`, l. 1156 à 1157 : le niveau est dans une clé voisine et dans le nom. L. 1087 : « au plus 0,025 » est attaché à la probabilité de E3 même quand E3 est lue à 99 %. Après : ajouter « (au niveau de 95 %) » à la phrase de S, D et C ; prendre « au plus » au niveau propre de E3.

**m-2. La borne de la phrase E peut être minuscule.** `lecture_v1.py`, l. 1133 : « plus petite que [borne] » est le plus grand d_k signé. Elle n'est jamais négative (la v1 le disait à tort : des différences toutes négatives rendent « contraire »). Mais un seul écart positif d'un millionième suffit à huit familles (sondage S6) : la phrase dirait qu'un sabotage plus petit qu'un millionième n'est pas exclu. Le texte ne définit pas cette borne : cinquième question, ci-dessous.

**m-3. Le contrôle carte-processeur en échec écrit l'écart mesuré.** La fonction gelée lève un message qui le porte (`t07bbis/apprentissage_carte_v1.py`, vers l. 146) ; `relecture_v1.py`, l. 538 à 540, l'écrit au résultat « arrêt » et sur la sortie d'erreur. Le rapport du développeur dit qu'il n'est pas écrit : vrai seulement quand le contrôle passe. Après : dans `sondes_v1.controle_carte` (l. 237 à 239), relever une garde sans nombre.

**m-4. M1 ou M3 sous six familles, E3 à six ou plus.** `lecture_v1.py`, l. 964 à 966 : issue NI, motif « manipulation non établie (M1) », sans dire que le niveau n'est pas atteignable. Lié à la troisième question.

**m-5. La garde de l'arbre de la session n'est jamais jouée sur le dépôt réel avant le jour de la lecture.** `relecture_v1.py`, l. 517 à 526 : plan décisif seulement, sur l'instance. Un JSON du dépôt qui porterait « famille : T0x » avec « membre » ou « cout » arrêterait la marche décisive à son début. Après : la jouer aussi dans `verifier`, côté session.

**m-6. L'instant de « création » est le début de la marche.** `relecture_v1.py`, l. 491. La garde du point 9 ne tient que si le commit est fixé dans la commande de création et si `verifier` est joué juste avant. À juger sur l'amorce, à la vérification.

**m-7. « Chaque étape écrite avant la suivante » (point 12).** `lecture_v1.py`, l. 1283 à 1288 : les étapes sont rangées en mémoire dans l'ordre, le résultat écrit une fois. Écart de forme ; M-1 en couvre le fond.

**m-8. La mutation C8 n'est vue que par le jouet de bout en bout.** Un essai rapide des sondes devrait vérifier que la sonde d'un pli ne note que les tâches de son pli.

## Ce que j'ai lu conforme, point par point

- **Point 8, relecture forcée et chemin éprouvé.** La série du modèle nu passe par `rejouer` comme les adaptateurs (`relecture_v1.py`, l. 650 à 653). Les activations d'origine viennent de `passe_unique` sur les identifiants de l'épisode, comme dans la chaîne (`harnais/episode.py`, l. 260). Cas sain au bit près et artefact : l. 381 à 413. Ordre tiré par graine, identité et artefact par adaptateur, état de phase en début et en fin de série.
- **Points 7, 9 et 10, notation fermée.** `sondes_v1.noter` ne rend que des scores bruts ; refus d'un adaptateur tenu à l'écart ou d'un point d'ancrage dans un apprentissage ; produits et poussées tirés des seuls déplacements moyens, ĝ des seuls `A<k>-saboteur`, points d'ancrage hors des produits ; le journal refuse tout nombre à virgule. Réserve : m-3.
- **« Métrique », mises à l'échelle et maximum.** Seulement à la lecture (`lecture_v1.py`, l. 578 à 587 et 799 à 823) ; règles d'échec à la lettre ; c = 1 quand la poussée de E2b n'est pas positive.
- **« Seuil », dénombrement exact.** Égal à mon énumération de 0 à 12 familles et à la table du texte (sondage S5) ; zéros et égalités au pire de tous les ordres.
- **« Critères », table des issues et nœud 6.** Ordre NI, C, S, D, E, N ; motifs de D ; mention de N ; niveau épreuve par épreuve.
- **Point 12 (a), garde d'ouverture.** Empreinte du programme, épreuve passée pour la même empreinte, table égale à l'engagement et à l'ouverture, trois dates, arbre à l'empreinte de `SCORES-B5F`. Formats de `CODE-FORMATION-B5F` et de `GO-FORMATION-B5F` : ceux du code de formation (`formation_v1.py`, l. 1030 à 1031). Réserves : M-3, M-4.
- **Point 18.** Répétition et points d'ancrage prévus dans les deux modes ; descriptifs seulement.

## Les gardes, cas sain et artefact (R5)

| garde | cas sain | artefact | jugement |
|---|---|---|---|
| moyenne sur les jetons | notation par le maximum | quatre agrégations refusées | tenue |
| table dans l'arbre de lecture | arbre fabriqué | par empreinte, par forme, ligne de coût | **trou : M-3** |
| engagement postérieur | registre en ordre | après la création, après les scores, avant les sorties, avant la relance | tenue ; m-6 |
| score manquant | monde complet | action ôtée, série ôtée | tenue |
| famille incomplète | dix familles | sans sur-saboteur, sans saboteur, sept, cinq familles | tenue pour E ; **M-2 pour M1** |
| identité à dose 0, artefact à dose 1 | adaptateur jouet | adaptateur sans effet, dose 0 différente | tenue |
| contrôle carte-processeur | écart sous la tolérance | écart au-dessus | tenue ; m-3 |
| code au commit de `CODE-LECTURE-B5F` | — | — | **sans essai : M-4** (juste à mon sondage) |

## Les quatre questions au texte du développeur

1. **Formats des lignes de registre de la lecture.** Le texte ne les écrit pas et ne les interdit pas ; pour `CODE-FORMATION-B5F` il renvoie lui-même au code. Pas d'addendum : la mère adopte les formats du code, les consigne, et les donne à qui inscrit les lignes et à la fabrique de l'épreuve.
2. **Niveau d'une issue sous huit familles.** Le texte tranche le compte épreuve par épreuve (nœud 6 ; monde V10). Il ne dit pas si M1 et M3 sont parmi « les épreuves qui la fondent », ni si une épreuve manquée compte pour D. Le choix du code est le plus prudent et ne change que le niveau affiché. À fixer par un addendum du rédacteur, avant la seconde programmation, dont l'accord exigé est exact.
3. **Ordre du point 13 de la liste d'arrêt et de « non interprétable ».** Tranché par le texte, dans le sens du code : sous six familles, M3 n'a aucun niveau atteignable, la manipulation n'est donc jamais établie ; si NI passait d'abord, le point 13 ne s'appliquerait jamais. Reste le cas m-4 : au rédacteur, même addendum.
4. **Tâche sans coût lisible chez un seul membre.** Non tranché : « tâches jouées par tous les membres » parle de tâches jouées. Le point 17 (« mêmes tirages pour les grandeurs d'une même ligne ») penche pour retirer la tâche à tous, ce que le code ne fait pas. Au rédacteur, par addendum, avant toute lecture.

Cinquième question, de moi : la valeur de « [borne] » dans la phrase E (m-2). Au rédacteur. Sixième, si la mère la juge ouverte : M1 dans « toutes les épreuves » (M-2).

Ces précisions ne changent aucun critère ; si l'une en changeait un, elle passerait par Lazar.

## La remarque pour la fabrique de l'épreuve à vérité plantée

Juste au regard du point 11. Les écarts y sont « en écarts types de la différence d'une famille à l'autre » : une différence sans dispersion n'a pas d'unité. « Disparaît à poussée égale » y veut dire que l'écart planté s'annule, non que la différence est exactement nulle. Le texte ne prévoit aucune tolérance ; le programme n'a pas à en inventer.

Deux précisions : le bruit se plante au niveau des scores par jeton, comme en V0, pour survivre à la mise à l'échelle ; et la remarque ne dit rien d'autre à la fabrique, qui reste écrite par un agent qui n'a pas écrit le programme.

## Séparation d'avec la formation

- Vu par moi : entre le commit `8c1d6918` et la tête `cde050cc`, aucun fichier du paquet `barreau5_familles`, du lanceur ni des quatre fichiers d'essais n'a changé. Le code de lecture n'écrit dans aucun module de la formation ; il importe `engagement_v1` et `formation_v1.jouer_sans_activations` sans les modifier.
- **Vérifié par la mère**, en local, et non par moi : la branche de la course ne porte, sous `src/controle_ia/barreau5_familles/`, que `__init__.py`, `edition_cout_v1.py`, `engagement_v1.py` et `formation_v1.py`, et aucun des quatre fichiers d'essais de lecture ; entre `ef8008682` et `8c1d69188`, aucun fichier du code de formation figé ni de ses six fichiers d'essais n'a changé.

## Essais, mutations, sondages

- Essais du paquet de lecture, sans mutation : **134 passés, aucun échec**, en 192 s.
- Mutations du développeur (lu : sa sortie et ses trois états) : 57 jouées, 56 attrapées, une équivalente démontrée. Son premier passage nul est déclaré et corrigé ; j'ai repris son procédé, témoins exigés verts.
- Mes mutations : **8 jouées, 2 attrapées**, 6 manquées, aucune équivalente.
- Sondages : six, tous joués ; M-1, M-2 et M-3 confirmés.

## Ce qui menace le gel

1. Les corrections M-1, M-2 et M-3 changent `lecture_v1.py`, donc l'empreinte que portera `CODE-LECTURE-B5F`.
2. L'addendum du rédacteur (questions 2, 3, 4, 5) doit précéder la seconde programmation et l'épreuve à vérité plantée.
3. Les essais de M-4 demandent une branche de formation fabriquée : c'est le plus long des ajouts.
4. L'amorce de l'instance de lecture n'est pas contre-lue ; m-6 en dépend.
5. La vérification des corrections me revient ensuite.

## Deux fautes de procédure de ma part, déclarées

1. **Premier passage, refus d'outil.** Une commande de contrôle réunissait une recherche dans les fichiers d'essais, la liste des branches locales et une interrogation du dépôt distant. Cette dernière atteint le réseau. Rien n'a été exécuté. Depuis la reprise : aucun réseau, une commande simple à la fois, aucun autre refus.
2. **Reprise, écrasement d'un fichier scellé.** J'ai d'abord écrit cet état final sous le nom de la v1, déjà scellée et versée. Le scellement l'a refusé (R12). J'ai remis la v1 par `git checkout` de ce seul fichier, vérifié son empreinte (`e8ca26f9…`), et écrit cette v2 sous un nom neuf.
