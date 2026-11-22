# Critère d'identité du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v7 (version finale : celle qui cite le programme de comparaison v4 ; scellée avant toute création de machine)

- **Version 7 — auteur** : le rédacteur de la v7, sous-agent lancé par la session `session_013QMaykLXtozHttcSQ4ke1s`, modèle
  **Claude Fable 5.2** (`claude-fable-5-2`). Il n'a écrit ni les versions 1 à 6 de ce critère, ni le programme de comparaison v4,
  ni ses essais, ni son banc d'altérations, ni les contre-lectures, ni les vérifications.
- **Version 7 — origine, déclarée** : la v6 (`critere-identite-reajustement-lentilles-v6.md`,
  `0700f3da3330c1c9ae71ef391857bc16c92bbda28f89a784862f9fb2befc7fa9`, empreinte recalculée, égale au compagnon), **gardée à la
  lettre hors un seul couple**, celui de la vérification du lot final par le contre-lecteur, sur Claude Opus 5.5
  (`docs/notes/neuron-lens-v1/verification-critere-v6-devis-v7-programme-v4-v1.md`,
  `e56e0a75a91360053d1bb94d11407702462713b50dd327d53eb9ef3be2bb859a`, branche principale ; empreinte recalculée sur la copie remise
  par la mère, égale à celle du compagnon de la branche principale) : critère v6 « scellable après ce couple exact ». Le texte
  « avant » a été retrouvé une fois dans la v6, à l'espacement près ; le texte « après » est porté à la lettre, par programme (§ 4,
  fin de l'alinéa « Arrêt du programme sur une erreur »). Les seules autres différences sont le numéro de version du titre, ces
  quatre lignes d'en-tête et la table « différences de la v7 à la v6 » à la fin du § 0.4. Les remarques mineures de la vérification
  ne sont pas portées. La v6 reste archivée sans modification.
- **Version 7 — heure** (`date -u`) à l'écriture : 2026-11-19T12:43:10Z ; l'heure du scellement est celle du fichier compagnon.
- **Version 7 — lecture de ce qui suit** : les lignes d'en-tête ci-dessous et tout le corps sont ceux de la v6, gardés à la
  lettre ; « le rédacteur », « cette version » et « cette v6 » y désignent le rédacteur de la v6 et la v6.
- **Auteur** : le rédacteur, sous-agent lancé par la session `session_013QMaykLXtozHttcSQ4ke1s`, modèle **Claude Fable 5.2**
  (`claude-fable-5-2`), selon la règle « Qui conçoit » des consignes permanentes (branche principale ; mot de Lazar du 19 novembre,
  R-3735). Il n'a écrit ni les versions 1 à 5 de ce critère, ni le programme de comparaison v4, ni ses essais, ni son banc
  d'altérations, ni les contre-lectures, ni la vérification des versions 5 ; la v5 est d'un autre rédacteur sur le même modèle, le
  programme v4 d'un développeur sur le même modèle.
- **Origine, déclarée** : la v5 (`critere-identite-reajustement-lentilles-v5.md`,
  `50657b8929ab29ff5b09012b31cfe2a150f7815916b538acdba133f7042e24b6`, empreinte recalculée, égale au compagnon), **gardée phrase à
  phrase hors les différences du § 0.4** ; elle reste archivée sans modification, comme les versions 1 à 4. Lus aussi :
  - la vérification des versions 5 par le contre-lecteur de la v4, sur Claude Opus 5.5
    (`docs/notes/neuron-lens-v1/verification-critere-et-devis-v5-v1.md`,
    `cd93416cb4df693f5092da0e07002fd895cf99fad061d897de29233f76589478`, branche principale, commit `1309ee663`, R-3779 ; empreinte
    recalculée, égale au compagnon) : critère v5 « scellable après ces couples exacts », sept couples ; son § 7 dit ce que la version
    qui cite le programme v4 peut changer, « et rien d'autre » ; ses sondes synthétiques, versées à côté
    (`verification-critere-et-devis-v5-sondes-v1/sondes_synthetiques_v1.py`, `5b1d2033…`, sortie `8f87be7a…`, empreintes recalculées) ;
  - le programme de comparaison v4, ses essais et son banc d'altérations (§ 7), lus en entier ; **le rédacteur ne les a pas modifiés** ;
  - le rapport du développeur du programme v4, par le résumé qu'en donne la mère dans le mandat (six points à porter ; ce qui reste à
    la main).
- Heure (`date -u`) à l'écriture : 2026-11-19T12:29:32Z ; l'heure du scellement est celle du fichier compagnon. Pièce de **classe A**.
- Contexte : accord GO-2026-11-19-33 (pièce 3 du billet : la lecture des sondes avec nos lentilles, qui suppose le réajustement).
  Aucune ligne de calcul à ce jour : aucune lentille réajustée n'existe, ce critère est écrit avant de voir (R1). **Il prime sur toute
  phrase du devis** ; le devis v7 (`devis-reajustement-lentilles-b-beta-v7.md`) le cite par son chemin et son empreinte.
- Reste à faire avant la création : la vérification courte de cette version par le contre-lecteur du critère, selon le § 7 de son
  rapport (R2) ; la contre-lecture du programme v4 par un autre modèle (devis v7, § 5, point 6).

## 0. Traitement des couples, des six points du développeur, du § 7 de la vérification ; différences avec la v5
**Aucun seuil n'est changé** (10⁻³, 10⁻⁹, 10⁻⁶, 0,10), **ni aucune tolérance, ni aucun libellé de mention, ni ce que chaque mention
autorise.** Les numéros de paragraphe (§ 1 à § 10) sont ceux de la v5 : les renvois du programme v4 (« critère en vigueur, § 2 »,
« § 4 », « § 6 », « § 7 ») et du devis tombent au même endroit.

### 0.1 Les couples de la vérification des versions 5 (`cd93416c…`)
Chaque « avant » a été retrouvé une fois dans la v5 ; chaque « après » est porté comme dit ci-dessous.
| couple | objet | traitement | où |
|---|---|---|---|
| 1 | K2 : quel lanceur, et la même ancre | **porté, réparti entre le programme et la main.** Ce que le programme v4 vérifie lui-même (arbre propre ; lanceur neuf égal, à l'octet, au fichier de son chemin au commit du manifeste neuf ; commits des manifestes lisibles) est devenu préalable « K2 : … » du § 4. Tout le reste du texte « après » est gardé à la main, valeurs comprises : le chemin donné est celui du lanceur que nomme la commande scellée ; révision et empreinte de l'ancre ; trois empreintes de fonction du module de contrôles ; dépôt de travail. Les trois empreintes de fonction et les lignes 51, 58 et 130-131 du lanceur du 18 ont été recalculées et relues par le rédacteur au commit `5e5cb65b…` : égales. | § 4 ; § 7, K2 |
| 2 | ce que le plancher des séries de R suppose | **porté à la lettre**, hors le renvoi « devis v5 », devenu « devis v7 » (même paragraphe, même point). | § 4 |
| 3 | premier palier en cas mixte | **porté à la lettre** : ligne du tableau et phrase. | § 5 |
| 4 | une phrase pour les autres verdicts | **porté à la lettre.** | § 5 |
| 5 | K4 : un seul journal, ses seuls en-têtes | **porté à la lettre**, dans K4 et au § 8. | § 7, K4 ; § 8 |
| 6 | K1 : quel commit | **porté à la lettre.** | § 7, K1 |
| 7 | le programme v4 annoncé à la fin du § 7 de la v5 | **tombe**, sur demande de la mère : il ne valait que si la v5 était scellée comme critère appliqué avant la version qui cite le programme v4. Cette v6 est cette version ; la phrase visée disparaît avec la liste des défauts du programme v3. | — |

Mineures de la vérification, pour la part du critère : la 2 (« porte l'empreinte du 18 » se lit sur le champ `resultat.sha256` du
résultat neuf) est reprise dans le rangement de l'arrêt sur une erreur, qui la demandait (§ 4) ; la 6 (longueur) est suivie pour
partie (§ 0.4, n° 13) ; la 1 (source directe du filtre `H100_SXM`) et la 7 (champ `graines`) ne sont **pas portées**, selon le
mandat (« rien d'autre ») : le vérificateur les dit sans effet sur le scellement.

### 0.2 Les six points du rapport du développeur du programme v4
| n° | point | traitement | où |
|---|---|---|---|
| 1 | **K1 manqué** : le programme rend « non comparable », ou la suspension à octets égaux, là où la v5 disait « pas de verdict, comparaison refaite sur les bonnes pièces ». | La règle de la v5 est gardée telle quelle. Le critère dit que la mention rendue sur un préalable « K1 : … » manqué **signale** ce manqué, ne remplace pas la règle et n'est pas le verdict. | § 4 (préalables) ; § 7, K1 |
| 2 | **Arrêt sur une erreur** : la v4 écrit une sortie (`arret_sur_erreur`, mention, déclencheur libellé (iv) ou (v), code de sortie 2). | Rangé en deux cas de même conséquence : la sortie est écrite (cas de la v4), ou elle ne l'est pas (la règle de la v5, gardée comme filet). Verdict, nœud de Lazar et interdiction de relancer sur des pièces retouchées inchangés. | § 4 ; § 6 |
| 3 | **Préalables ajoutés** : `etape` de l'export égal à « export » ; sept préalables « forme : … » ; `depot_propre` vrai des deux côtés ; commit des résultats et pièces neuves vérifiés octet par octet ; lanceur neuf rattaché au commit du manifeste ; commits des manifestes lisibles. | Tous écrits au § 4, avec leur libellé exact, leur conséquence (inchangée) et leurs essais au § 7. | § 4 ; § 7 |
| 4 | **Exigences de forme** : commit des résultats en identifiant entier ; `depot_propre` exigé aussi du manifeste de référence. | Écrites. La seconde ne peut pas manquer seule : le manifeste de référence est vérifié par son empreinte, et il porte `depot_propre` vrai. | § 4 ; § 7, K1 et K2 |
| 5 | **Phrases devenues fausses** : au § 6, « que le programme ne pose que pour (vi) » ; au § 7, le programme cité, son empreinte et la liste K. | Corrigées. La règle « l'audit est dû dès que la liste des déclencheurs n'est pas vide » reste, et reste ce qui décide. | § 6 ; § 7 |
| 6 | **Constantes neuves** : `31061d6c…` (R) et `aac70eef…` (S), pour le seul arrêt sur une erreur. | Dites au § 2 et au § 7 ; ce sont les deux empreintes de fichier d'ajustement déjà écrites au § 2 de la v5, relues égales au champ `resultat.sha256` des deux pièces du 18. | § 2 ; § 4 ; § 7 |

Ce que le développeur dit rester à la main (K1 et K2 en partie, K3, K4, K5 pour la recopie ; relecture au lieu de rangement, audit,
verdict d'identité, avertissement à Lazar) : c'est la liste du § 7, sans ajout ni retrait de sa part.

### 0.3 Le § 7 de la vérification, point par point
| point du § 7 | tenu ? | remarque |
|---|---|---|
| 1. Le § 7 du critère cite le programme v4 et lui seul ; les étiquettes du programme nomment cette version du critère | **oui pour la citation ; non pour les étiquettes** | L'en-tête du programme, sa constante `CRITERE` et donc le champ `critere` de chaque sortie nomment « le critère en vigueur (v5 à l'écriture du programme, 50657b89…) », et un essai l'exige. Le rédacteur ne modifie pas le programme ; le critère dit que ce sont des étiquettes (§ 7). **Écart signalé à la mère et au vérificateur.** |
| 2. Chaque contrôle pris en charge par la v4 passe de la liste K aux préalables, avec la même conséquence et le nom de l'essai | **oui** | Table du § 7. L'ancre et le calcul des séries (couple 1), que la v4 ne lit pas, restent à la main. |
| 3. Reste à la main ce que la v4 ne peut pas voir | **oui** | Chemin nommé par la commande scellée ; tête de la branche distante après destruction ; matériel ; en-têtes du journal d'ajustement ; relecture au lieu de rangement ; audit. |
| 4. La règle de l'arrêt sur une erreur reste, comme filet ; les formes connues rendent « non comparable » (ou suspendent) sous les libellés inchangés | **oui** | § 4. |
| 5. Au § 6, la règle de l'audit reste ; seule la remarque sur `audit_requis` suit la v4 | **oui** | § 6. S'y ajoute la mention, de fait, que les déclencheurs (iv) et (v) couvrent l'arrêt sur une erreur, puisque le programme les libelle ainsi. |
| 6. Constantes et libellés identiques à l'octet | **oui** | Comparés par le rédacteur entre les programmes v3 et v4 (seuils, comptes, champs, cinq empreintes de référence, cinq libellés : égaux) ; essai `test_v4_aucune_regle_de_decision_ne_change`. |
| 7. Les couples 1 à 6 sont portés ; le § 0 dit chaque différence avec sa raison et son essai | **oui** | § 0.1 et § 0.4. |

### 0.4 Différences avec la v5, chacune avec sa raison et son essai
Les essais nommés sont ceux de `tests/test_neuron_lens_comparer_reajustement_v4.py` (§ 7).
| n° | différence | raison | essai |
|---|---|---|---|
| 1 | **Le programme cité est la version 4**, et lui seul (§ 7) ; essais et banc d'altérations cités. | Décision de la mère ; § 7, point 1, de la vérification. | les 311 essais |
| 2 | **Contrôles passés de la liste K aux préalables du § 4**, même conséquence : arbre propre (`depot_propre`) ; lanceur neuf égal au fichier de son chemin au commit du manifeste neuf ; commits des manifestes lisibles (K2) ; commit des résultats lisible et pièces neuves égales, à l'octet, aux fichiers de ce commit (K1). | Le programme v4 les vérifie ; § 7, point 2, de la vérification ; point 3 du développeur. | table du § 7 |
| 3 | **Deux exigences de forme** : le commit des résultats est donné en identifiant entier ; `depot_propre` est exigé aussi du manifeste de référence. | Point 4 du développeur. | `test_v4_k1_commit_des_resultats_absent_ou_mal_forme`, `test_v4_k2_depot_propre` |
| 4 | **Sept préalables de forme** : une pièce mal formée d'une forme connue est un préalable manqué, non plus un arrêt. | Point 3 du développeur ; § 7, point 4, de la vérification. | `test_v4_piece_mal_formee_rend_non_comparable_avec_motif`, `test_v4_cli_fichier_mal_forme_ecrit_une_sortie_non_comparable` |
| 5 | **Préalable neuf pour R** : champ `etape` de chaque pièce d'export égal à « export ». | Point 3 du développeur (défaut du programme v3 relevé dans la v5, § 7). | `test_v4_etape_de_l_export` |
| 6 | **Arrêt sur une erreur rangé en deux cas** (sortie écrite ; sortie non écrite), même verdict qu'en v5. | Point 2 du développeur ; § 7, point 4, de la vérification ; mineure 2. | `test_v4_cli_arret_sur_une_erreur_ecrit_la_sortie_et_le_motif`, `test_v4_sortie_arret_sur_erreur_choix_de_la_mention` |
| 7 | **K1 manqué** : la mention du programme signale le manqué sans remplacer la règle. | Point 1 du développeur. | `test_v4_k1_piece_neuve_modifiee_d_un_octet_apres_le_commit`, `test_v4_k1_octets_egaux_piece_non_versee_suspend` |
| 8 | **§ 6** : `audit_requis` suit la liste des déclencheurs ; (iv) et (v) couvrent l'arrêt sur une erreur ; l'audit lit aussi le relevé du rattachement aux commits et les champs du haut du manifeste. | Point 5 du développeur ; § 7, point 5, de la vérification. | `test_v4_audit_requis_pour_tout_declencheur` |
| 9 | **K5** : la table des champs du haut du manifeste est rendue par le programme, sans critère ; reste à la main sa recopie dans le verdict. | Le programme v4 la rend ; § 7, point 2, de la vérification. | `test_v4_k5_haut_champ_change_rapporte_sans_critere`, `test_v4_k5_haut_champ_present_d_un_seul_cote` |
| 10 | **Deux constantes de plus** dans le programme (§ 2, § 7), pour le seul arrêt sur une erreur. | Point 6 du développeur. | `test_v4_cli_arret_reference_illisible_le_resultat_neuf_porte_l_empreinte_du_18` |
| 11 | **Couples 1 à 6** portés (§ 0.1). | Vérification des versions 5. | sans objet pour 2 à 6 (texte) ; couple 1 : essais de K2, table du § 7 |
| 12 | **Accords de lettre** qui suivent des différences ci-dessus : « devis v5 » devient « devis v7 » ; au § 4, point 4 de la procédure et dernière ligne des mentions ; au § 5, la phrase sur ce qui couvre « même code d'ajustement » ; au § 8, ce qui est donné au programme. | Sans eux le texte se contredirait. | — |
| 13 | **Retirés, parce qu'ils décrivent le programme v3 ou l'histoire de la v5** : les § 0.2 et 0.3 de la v5 (traitement de la contre-lecture de la v4), la table des sondes U1 à U14 et la liste des défauts du programme v3. Ils restent dans la v5 archivée. Une courte liste des défauts du programme v4 prend la place de la dernière (§ 7). | Mineure 6 de la vérification ; § 7, point 1 (ne citer que le programme en vigueur). | — |

**Différences de la v7 à la v6** (la table ci-dessus, de la v5 à la v6, est gardée telle quelle).
| n° | différence | raison | essai |
|---|---|---|---|
| 1 | **Une règle pour les deux refus de démarrer du programme** (ligne de commande refusée : code 2, message d'usage, aucune sortie ; sortie déjà présente : code 1, message « existe déjà », aucune sortie) : ce ne sont pas des comparaisons, ils ne rendent ni mention ni verdict et ne relèvent pas du filet ; tout autre arrêt sans sortie relève du filet. Couple unique, porté à la lettre au § 4, fin de l'alinéa « Arrêt du programme sur une erreur ». | Vérification du lot final (`e56e0a75a91360053d1bb94d11407702462713b50dd327d53eb9ef3be2bb859a`), § 3, point 2 : le § 4 de la v6 nommait la ligne de commande refusée sans dire quoi en faire, et lus à la lettre les deux refus tombaient dans le filet (« non comparable ») alors que rien n'avait été comparé. | aucun essai du dépôt ; sondes W9 à W11 du vérificateur, hors dépôt, non opposables tant qu'elles ne sont pas versées |

## 1. Ce que le critère décide
Les deux lentilles ajustées le 18 novembre (course `20261118-164930-neuron-lens-b-beta`, verdict « partiel » accepté par Lazar,
`lecture-b-beta/verdict-b-beta-v1.md`, `3a9b947e…`) ont été détruites avec la machine louée. Après un réajustement sur une autre
machine, trois questions se posent, et le critère les tient séparées :
1. **Identité** : les fichiers rangés sont-ils ceux qui ont été mesurés le 18 ? Seule une égalité d'octets y répond.
2. **Transport** : les mesures et le verdict du 18 décrivent-ils la lentille rangée ? Oui si l'identité est établie, non sinon.
3. **Parole** : qu'a-t-on le droit d'écrire, et de faire lire à cette lentille ? (§ 5.)
Ce qu'on appelle « la lentille » : pour R comme pour S, le **fichier d'ajustement** (sommes par couche, par cible et par moitié du
corpus). Pour R s'y ajoutent les trois exports qui en sont tirés (lentille entière, moitié paire, moitié impaire) : l'export est la
moyenne des sommes de la cible de sortie, et c'est lui qu'une lecture charge.

## 2. Références du 18 novembre
Branche `claude/brave-galileo-jhp684` (pièces absentes de la branche principale) ; les empreintes font foi, recalculées par le
rédacteur de la v6 le 19 novembre, égales aux valeurs ci-dessous. Dossier `diag/20261118-164930-neuron-lens-b-beta/` :
- `b-beta-ajustement-R.json` (`129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab`) : fichier d'ajustement de R
  `r-llama-3.1-8b-instruct-L32-dclm-T128.pt`, empreinte `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c`,
  8 455 720 309 octets ; `diffs_float64`, 63 valeurs (32 pour la cible `mid`, 31 pour la cible `out`) ; `diffs` (simple précision) ;
  `meta` ; `n_docs` [466, 466] ; `next_doc` 932 ; `finies` vrai ; début 2026-11-18T18:03:15Z.
- `b-beta-ajustement-S.json` (`2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297`) : fichier
  `s-llama-3.1-8b-instruct-L32-dclm-T128.pt`, empreinte `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8`,
  8 589 938 049 octets ; 64 valeurs (32 et 32).
- `b-beta-export.json` (`17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1`) : pour R, `matrices_moities` (31 couches,
  deux empreintes par couche : moitié paire, moitié impaire) ; `valeurs.npR_notre_R` et `valeurs.identite_notre_R` (28 couches
  chacune, 0 à 27, calculées sur la lentille **entière**). **La lentille R entière n'a aucune empreinte par couche dans cette pièce** :
  ses fichiers exportés portent un identifiant de génération tiré à chaque export.
- Manifeste `runs/20261118-164930-neuron-lens-b-beta/manifeste.json` (`b90c15140074e9d41a3cf93e8bcaf55f80cc025d07d2d46432239d1c6b6e3444`) :
  commit du dépôt réduit `5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` ; `config.commit_voisin` `849bfe1678e28becceb1e3864afe5fc8297d02e4` ;
  `config.drowse` (bibliothèque des lentilles : version 6.1.4, roue `673ed2b4…`) ; `config.precision` ; `config.correctifs` (cinq
  **chemins**, sans empreinte) ; `versions` (torch 2.14.1, numpy 2.4.6, transformers 5.18.0, safetensors 0.8.0, tokenizers 0.23.2,
  huggingface_hub 1.33.0, python 3.12.16).
- Fonction de calcul : `_split_half_64` de `src/controle_ia/neuron_lens/b_beta_lancer_v3.py` (fichier `582fd9ef322de2476b19eb4ce4868f99d7ea4ee52870edbaf316275bbd1dd1ea`, égal à celui du commit `5e5cb65b…` du dépôt réduit ; empreinte du
  texte de la fonction `a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c`, relevée par le rédacteur avec la fonction
  `empreinte_fonction` du programme ; **le programme v4 la porte en constante** et l'exige des deux lanceurs).
- Les deux empreintes de fichier d'ajustement ci-dessus (`31061d6c…` pour R, `aac70eef…` pour S) sont aussi des constantes du
  programme v4 : elles n'y servent qu'à l'arrêt sur une erreur (§ 4), pour dire si le résultat neuf porte l'empreinte du 18 quand la
  pièce de référence n'a pas pu être lue.
- **Non consignés le 18** : le modèle de carte (connu du registre des accords : H100 ; le filtre de la commande exigeait `H100_SXM`, selon le
  contre-lecteur de la v4, qui renvoie à l'en-tête du relevé de prix `90395583…`) et la version du pilote de la carte
  (réserve 2 du lecteur du verdict). Aucune pièce du 18 ne permet de les comparer.

## 3. Écart entre chemins de calcul (repère, hors critère)
Programme `ecart_chemins_calcul_v1.py` (`2084dae7…`), sortie `sortie-ecart-chemins-calcul-v1.txt` (`21d04198…`), sur les deux pièces
d'ajustement du § 2. Sur les **mêmes sommes**, la différence entre moitiés calculée en simple précision (`diffs`) s'écarte de celle en
double précision (`diffs_float64`) d'au plus 3,48 × 10⁻⁵ (R, cible `mid`, rang 2) et 5,86 × 10⁻⁵ (S, cible `out`, rang 26).
`diffs_float64` va de 3,53 × 10⁻³ à 0,1114 (R) et de 4,11 × 10⁻³ à 0,1046 (S) ; la valeur de R la plus proche de 0,10 est 0,100444
(cible `mid`, rang 2, **au-dessus** du seuil), à 4,4 × 10⁻⁴.
Cet écart est celui du calcul final en simple ou en double précision sur les mêmes sommes. Le critère compare deux valeurs en double
précision : cet écart n'y entre pas. **Il ne borne l'écart d'un réajustement ni par le bas ni par le haut ; aucune pièce ne mesure
l'écart d'un réajustement.**

## 4. Le critère, lentille par lentille
Chaque lentille est jugée seule ; cas mixte : chacune est rangée avec sa mention et reçoit sa propre phrase (§ 5). Les libellés entre
guillemets sont ceux que rend le programme de comparaison (§ 7) ; ils ne se reformulent pas.

### Procédure, dans cet ordre
0. **Lentille non réajustée** (course arrêtée avant elle, ou machine détruite par une garde avant sa copie : devis v7, § 5, point 3) :
   « R non réajustée » ou « S non réajustée » ; l'autre est jugée seule.
1. **Empreinte du nouveau fichier d'ajustement égale à celle du 18** → premier palier, sauf anomalie (mention 4 ci-dessous).
2. Sinon, **un préalable manqué** → « non comparable (traitée comme différente) ».
3. Sinon, **écart absolu maximal sur `diffs_float64` au plus 10⁻³** → deuxième palier, sauf si l'écart maximal sur `diffs` dépasse
   10⁻³ (mention suspendue) ; **au-delà de 10⁻³ sur `diffs_float64`** → « différente ».
4. Puis les **contrôles à la main** du § 7 (K1 à K5, chacun pour la part que le programme ne fait pas), dans les deux sens et à
   tous les paliers : l'un d'eux manqué rend « non
   comparable » (octets différents) ou suspend la mention (octets égaux), ou empêche le verdict tant qu'il n'est pas tenu (K1, K3, K4, K5) ; aucun ne peut faire monter
   une mention.
5. Puis la **relecture au lieu de rangement** : l'empreinte du fichier rangé, relue là où il est rangé, égale celle que la machine a
   calculée avant l'envoi ; sinon la mention est suspendue (elle décrirait un fichier qui n'existe plus).
6. Puis, si le programme rend au moins un déclencheur, l'**audit** du § 6, qui ne peut que suspendre.
Le résultat des points 1 à 3 est la **mention du programme** ; le résultat des points 0 à 6 est le **verdict d'identité**, prononcé par
la mère (§ 8). Seul le verdict d'identité s'écrit au lieu de rangement, à l'inventaire, dans un texte de lecture ou dans le billet.
**Arrêt du programme sur une erreur** (pièce illisible, ou toute exception). Deux cas, de même conséquence.
- **Le programme a écrit sa sortie** (ce que fait le programme v4) : elle porte le champ `arret_sur_erreur` à vrai, le message
  d'erreur (`erreur`), la ligne de commande, le rappel du nœud (`noeud_de_lazar`), `audit_requis` à vrai, et ni préalables ni
  tables. Sa mention est « non comparable (traitée comme différente) », avec un déclencheur libellé (iv) ; ou « mention suspendue :
  anomalie (nœud de Lazar) », avec un déclencheur libellé (v), **si le résultat neuf porte l'empreinte du 18** : son champ
  `resultat.sha256`, que le programme relit alors sans rien supposer de la forme de la pièce, est l'empreinte du fichier
  d'ajustement du 18 — celle que porte la pièce de référence donnée, ou celle du § 2, que le programme tient en constante pour ce
  seul usage. Le programme sort avec le code 2. **Le verdict est cette mention**, et un nœud de Lazar est ouvert.
- **Le programme s'est arrêté sans écrire de sortie** (filet, gardé de la v5, pour toute exception que le programme ne rattrape
  pas) : aucune mention n'est rendue ; le verdict est « non comparable (traitée comme différente) », ou « mention suspendue » si le
  champ `resultat.sha256` du résultat d'ajustement neuf, lu à la main, est l'empreinte du § 2 ; un nœud de Lazar est ouvert ; le
  message d'erreur et la ligne de commande sont versés.
Dans les deux cas, le programme n'est pas relancé sur des pièces retouchées. Le premier cas se reconnaît au champ
`arret_sur_erreur` de la sortie écrite, non au seul code de sortie. **Deux refus de démarrer ne sont pas des comparaisons** : la
ligne de commande refusée (code 2, message d'usage, aucune sortie) et la sortie déjà présente (code 1, message « existe déjà »,
aucune sortie, la sortie présente n'étant ni lue ni remplacée). Ils ne rendent ni mention ni verdict et ne relèvent pas du filet :
la ligne refusée et son message sont versés, la ligne est corrigée — pour le second, sous un nom de sortie neuf — et la comparaison
est lancée ; si la sortie présente est celle d'une comparaison déjà faite, la relancer n'est permis que par les règles de K1 et
de K4. Tout autre arrêt sans sortie relève du filet.
**Une pièce mal formée d'une forme connue n'est plus un arrêt** : c'est un préalable « forme : … » manqué (ci-dessous), qui rend
« non comparable », ou suspend à octets égaux, sous les libellés inchangés.

### Les mentions
1. **Premier palier — « palier 1 — même lentille, octets identiques »** : l'empreinte du nouveau fichier d'ajustement est égale à la
   référence. Cela exige le **même nom de fichier au moment de l'écriture** qu'au 18 : le nom entre dans les octets écrits par
   `torch.save`, le dossier non (`essai_torch_save_nom_v1.py`, `1893d03e…`, sortie `3a2dbb16…` ; `essai_torch_save_octets_v1.py`,
   `4fdec19d…`, sortie `3a18c2c2…` ; essais sur processeur, torch 2.14.1). Le code voisin écrit sous un nom provisoire puis renomme ;
   ce nom provisoire se déduit du nom final (`path.with_suffix(".tmp")`, puis `os.replace`), donc le même nom final donne le même nom
   provisoire. Le lieu des tenseurs entre aussi dans l'archive : le code voisin ramène les sommes sur le processeur avant d'écrire
   (`v.cpu()`), ce qui est le cas que les essais couvrent. Ces trois lignes sont lues dans la copie de lecture du code voisin
   (`docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/scripts-02_fit.py.txt`, `309f4988…`, l. 161-166) ; **son égalité au
   commit `849bfe16…` de la course n'est pas vérifiée ici** (ce commit n'est pas dans le dépôt). Rien de cela n'est une condition du
   critère : le premier palier se lit sur l'empreinte, non sur ces raisons. Si le programme reçoit l'indication d'une reprise sur
   sauvegarde, il ajoute au libellé « ; reprise sur sauvegarde notée » ; si l'empreinte est égale, le premier palier est prononcé
   quand même, avec l'audit du § 6.
2. **Deuxième palier — « palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non
   comparables »** : tous les préalables tenus, et l'écart absolu maximal, en double précision et sans arrondi, entre les nouvelles
   `diffs_float64` (fonction `_split_half_64`, texte inchangé, calculée sur la machine à la fin de l'ajustement) et celles du 18, sur
   toutes les couches et cibles (R : 32 et 31 ; S : 32 et 32), est **au plus 10⁻³** ; et l'écart maximal sur `diffs` est lui aussi au
   plus 10⁻³.
3. **« différente »** : préalables tenus, écart sur `diffs_float64` au-delà de 10⁻³. **« non comparable (traitée comme
   différente) »** : un préalable manqué, octets différents.
4. **« mention suspendue : anomalie (nœud de Lazar) »**, dans deux cas.
   - **À empreinte égale**, l'un de ces faits : un préalable manqué (y compris la référence comparée à elle-même, qui n'est pas une
     course distincte) ; une taille différente ; un écart maximal sur `diffs_float64` supérieur à 10⁻⁹ (les mêmes sommes donnent la
     même valeur, à l'arrondi du calcul près) ; un écart maximal sur `diffs` supérieur à 10⁻⁶ (l'arrondi de la simple précision sur
     des valeurs d'au plus 0,12 est de l'ordre de 10⁻⁸) ; pour R, une empreinte de matrice des moitiés différente, ou **une des deux
     séries de R dont le plus grand changement n'est pas exactement zéro**. Le programme calcule les préalables et la table des écarts
     aussi au premier palier.
   - **À octets différents**, tous les préalables tenus et l'écart sur `diffs_float64` au plus 10⁻³, mais l'écart maximal sur `diffs`
     supérieur à 10⁻³ : `diffs` est la valeur que lisent les seuils de stabilité, elle ne peut pas s'écarter plus que la grandeur qui
     décide.
   S'y ajoutent les suspensions du contrôle K2 pour sa part à la main (§ 7), du point 5 de la procédure, de l'audit, et de l'arrêt
   sur une erreur quand le résultat neuf porte l'empreinte du 18.

**Sur le zéro exact des séries de R au premier palier.** À octets égaux, les sommes sont les mêmes ; l'export est leur moyenne,
entrée par entrée ; chaque série est un maximum de valeurs absolues de différences, calculé en simple précision sur le processeur
(`ecart_max`, `src/controle_ia/neuron_lens/controles_b_beta_v2.py`, l. 139-143) : aucune réduction dont l'ordre dépende de la machine,
un maximum est exact. Les mêmes entrées donnent donc les mêmes nombres, et un changement non nul dit que la lentille entière exportée
n'est pas celle du 18, ou que l'ancre a changé. **Cette exigence n'ajoute rien de plus dur que l'égalité des empreintes des matrices
des moitiés**, qui suppose déjà un export reproductible au bit ; elle l'étend à la lentille entière, la seule qu'une lecture charge
et que rien d'autre ne trace. Les bornes de 10⁻⁹ et 10⁻⁶, elles, ne sont pas à zéro, parce que ces deux grandeurs passent par une
norme dont l'ordre de sommation dépend du processeur.

### Préalables du programme, tous exigés
Le programme les calcule tous avant de choisir une branche, à tous les paliers. **Un préalable manqué, quel qu'il soit, rend « non
comparable (traitée comme différente) » à octets différents et suspend la mention à octets égaux** ; aucun ne peut faire monter une
mention. Les préalables marqués *(neuf)* sont ceux que le programme v4 ajoute ; les contrôles qu'ils portent étaient tenus à la
main dans la v5, avec la même conséquence (§ 7, table).
- **Forme des pièces** *(neuf ; sept préalables libellés « forme : … »)* : des deux côtés, l'enveloppe du résultat d'ajustement,
  le résultat d'ajustement, le manifeste, sa `config` et ses `versions` sont des dictionnaires, et `config.correctifs` est une liste
  non vide de chemins ; pour R, l'enveloppe de l'export neuf est un dictionnaire. Un lanceur qui n'est pas une source Python lisible
  manque le préalable sur le texte de la fonction (ci-dessous, « même code »).
- **Forme et valeurs** : mêmes cibles et mêmes comptes de valeurs, séries non vides (`diffs_float64` et `diffs`) ; toutes les valeurs
  finies et numériques, des deux côtés ; `meta` présent et égal champ par champ ; `n_docs` [466, 466] et `next_doc` 932 des deux
  côtés ; même nom de fichier ; `finies` vrai des deux côtés ; champ `etape` égal à « ajustement-R » ou « ajustement-S » selon la
  lentille, des deux côtés.
- **Provenance** : empreintes des deux fichiers d'ajustement présentes et bien formées, tailles présentes ; pièces de référence
  (ajustement, manifeste et, pour R, export) d'empreintes égales à celles du § 2, **vérifiées par le programme sur les octets lus** ;
  course neuve distincte de celle du 18 (identifiant de course et heure de début différents) ; manifeste neuf d'empreinte égale à
  celle que porte le résultat neuf.
- **Pièces neuves prises au commit des résultats** *(neuf ; préalables libellés « K1 : … »)* : le commit de la branche de résultats
  donné au programme (`--commit-resultats`) est un **identifiant entier** de commit (un nom de branche peut bouger, un préfixe est
  ambigu), lisible dans le dépôt donné ; chaque pièce neuve lue (résultat d'ajustement, manifeste, et pour R résultat d'export) a, à
  ce commit, **exactement les octets lus**, au chemin que la sortie rapporte (donné en argument, ou déduit de la place du fichier
  sous la racine du dépôt ; un chemin ni donné ni déductible est un manqué).
  **Pour ces préalables-là, la mention que rend le programme signale le manqué du contrôle K1 ; elle ne remplace pas la règle de K1
  (§ 7 : pas de verdict, comparaison refaite sur les bonnes pièces) et n'est pas le verdict.**
- **Code rattaché au manifeste** *(neuf ; préalables libellés « K2 : … »)* : `depot_propre` vrai dans le manifeste neuf **et dans
  celui de référence** (ce dernier, vérifié par son empreinte, le porte) ; le commit que porte chaque manifeste lisible dans le dépôt
  donné ; le fichier du lanceur neuf donné au programme a exactement les octets du fichier de chemin `--chemin-lanceur-neuf` **au
  commit que porte le manifeste neuf**.
- **Même code** : champs `ajustement`, `correctifs`, `graines`, `modele`, `revision` et `corpus` de la configuration du manifeste
  présents et égaux à ceux du 18 ; même commit du code voisin ; texte de `_split_half_64` d'empreinte égale à la constante du § 2
  dans les deux lanceurs donnés ; `config.drowse` (bibliothèque des lentilles : version et empreinte de la roue) et
  `config.precision` présents et égaux ; `versions` : mêmes clés et mêmes valeurs des deux côtés, hors le champ `plateforme` (le noyau
  de l'hôte) — une clé présente d'un seul côté est un manqué ; chacun des fichiers de `config.correctifs`, lu dans le dépôt donné au
  programme au commit que porte chaque manifeste (`git show <commit>:<chemin>`), d'empreinte égale des deux côtés — un fichier
  illisible à l'un des commits est un manqué.
- **Pour R** : pièces d'export présentes et complètes des deux côtés (31 couches de matrices des moitiés, deux empreintes bien formées
  par couche ; 28 couches finies par série) ; couches des matrices exactement 0 à 30 et couches de chaque série exactement 0 à 27,
  des deux côtés ; champ `etape` de chaque pièce d'export égal à « export » *(neuf)* ; export neuf de la course neuve (même
  identifiant de course et même empreinte de manifeste que le résultat d'ajustement neuf) et d'empreinte différente de l'export
  du 18 ; export neuf égal, à l'octet, au fichier du commit des résultats *(neuf, préalable « K1 : … » ci-dessus)*.

### Ce que le deuxième palier voit, et ne voit pas
- **Aveugle par construction.** La grandeur vaut ‖moyenne paire − moyenne impaire‖ / ‖moyenne‖ : tout déplacement commun aux deux
  moitiés s'annule au numérateur. Elle dit si le bruit entre moitiés est retrouvé, pas si la lentille est au même endroit : une
  lentille déplacée de 13 % de sa norme à chaque couche, dans une direction commune aux deux moitiés, passe ce palier (contre-lecture
  de la v1, point 2). Or un effet de machine, de pilote ou de bibliothèque est justement commun aux deux moitiés. La mention ne dit
  ni « équivalente », ni « proche », ni « même lentille ».
- **Tolérance conventionnelle, déclarée telle, absolue.** La décision qui suit porte sur le seuil absolu de 0,10 ; une tolérance
  relative serait lâche là où la grandeur est grande, près de ce seuil. Repères, qui ne la justifient pas : ≈ 17 fois le plus grand
  écart entre chemins de calcul ; un centième du seuil de stabilité ; 0,9 % de la plus grande valeur ; 28 % (R) et 24 % (S) de la plus
  petite (aux couches les plus stables ce palier ne distingue presque rien) ; plus du double de la distance au seuil de la valeur de
  R la plus proche (4,4 × 10⁻⁴). Depuis la v4 (au deuxième palier, la variante A n'entre dans aucune lecture), cette tolérance ne décide plus que d'une chose : en variante B, si la
  lecture demande ou non un nœud de Lazar propre à l'identité (§ 5).
- **Pour R, deux séries rapportées sans critère** : l'écart maximal, entrée par entrée, de chaque matrice de la lentille entière à
  la lentille R publique (`npR_notre_R`) et à l'identité (`identite_notre_R`), couches 0 à 27. Le programme rend, pour chaque série,
  le changement par couche d'une course à l'autre, le plus grand changement en valeur absolue, la plus petite et la plus grande valeur
  du 18 (0,0694 à 0,6769 pour la première, 0,8015 à 2,1916 pour la seconde, lues dans la pièce `17304c93…`). Aucune tolérance : aucune
  pièce ne mesure leur variation d'un réajustement. **Leur sens exact : un plancher, jamais un plafond.** Si l'écart maximal d'une
  matrice à une ancre fixe change de δ, alors les deux matrices diffèrent d'au moins δ en une entrée (inégalité triangulaire) ; un
  changement nul ou petit ne borne rien par le haut. Les séries ne peuvent donc que **montrer** un déplacement, jamais l'exclure.
  Deux précisions de lettre : l'inégalité tient à l'arrondi de la simple précision près (au plus ≈ 3 × 10⁻⁷ ici, le calcul étant
  fait en `float32`, pour des écarts d'au plus 2,19) ; et elle suppose la même ancre et le même calcul aux deux courses — la lentille
  publique est épinglée par révision et vérifiée par empreinte dans le lanceur du 18 (l. 58 et 130-131), le lanceur neuf doit garder
  ces lignes et ce calcul (devis v7, § 5, point 5 k), et le contrôle K2 le vérifie ; le champ `lentilles` de la configuration ne
  porte que des noms de lentilles (lanceur du 18, l. 64 et 598), il ne dit rien de l'ancre.
  Sont rapportés aussi : le compte des couches dont les empreintes des matrices des moitiés sont égales ; l'écart relatif maximal ;
  l'écart sur `diffs` ; toute valeur de `diffs` qui change de côté du seuil de stabilité de 0,10 ; la table des écarts par couche et
  par cible, avec leur signe.
- **Pour S, aucune grandeur sensible à la position n'existe dans les pièces du 18 : à écrire tel quel.** (L'écart maximal entre les
  sommes des deux moitiés, `ecarts_sommes`, versé le 18, est lui aussi une différence entre moitiés : il est aveugle de la même façon.)

## 5. Ce que chaque mention autorise
**Seul le premier palier établit l'identité.**

| verdict d'identité | identité | les mesures et le verdict du 18 décrivent la lentille rangée | lecture avec cette lentille |
|---|---|---|---|
| premier palier | établie | oui, avec leurs limites (verdict « partiel », couches stables du 18) ; **si l'autre lentille n'est pas au premier palier**, seulement les mesures faites sur celle-ci : le verdict d'ensemble et les conditions qui portent sur les deux lentilles ensemble ne se transportent pas tels quels | par un texte de lecture neuf et contre-lu, sous l'accord GO-2026-11-19-33 |
| deuxième palier, variante B (course rejouée **en entier**) | non établie | **non** ; ses mesures sont celles de la seconde course | seulement **après** la lecture de la seconde course par un lecteur neuf, dans les limites de cette lecture ; texte de lecture neuf et contre-lu, sous le même accord |
| deuxième palier, variante A (ajustement seul) | non établie | **non** ; elle n'a pour mesure à elle que sa différence entre moitiés (et, pour R, les deux séries) | **aucune sans nœud de Lazar** ; rangée avec sa mention |
| « différente », « non comparable », mention suspendue, lentille non réajustée | non établie | non | **aucune sans nœud de Lazar** ; rangée (si elle existe) avec sa mention |

- **Premier palier.** Phrase permise si **les deux** lentilles y sont : « Les fichiers d'ajustement réajustés sont identiques à l'octet à ceux du 18 novembre
  (empreintes …) ; les mesures du 18 novembre décrivent ces lentilles. » (*“The refitted fit files are byte-identical to those of
  18 November (hashes …); the 18 November measurements describe these lenses.”*) Si **une seule** lentille est au premier palier,
  la phrase est écrite pour elle seule : « Le fichier d'ajustement réajusté de la lentille [R | S] est identique à l'octet à celui
  du 18 novembre (empreinte …) ; les mesures du 18 novembre faites sur cette lentille la décrivent. » (*“The refitted fit file of
  lens [R | S] is byte-identical to that of 18 November (hash …); the 18 November measurements made on this lens describe it.”*)
  Le verdict d'ensemble du 18 (« partiel ») et les conditions communes aux deux lentilles ne se transportent pas tels quels : la
  condition sur la différence entre moitiés (mesure B-1) est exigée « des deux lentilles » (texte gelé de la tranche,
  `texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, l. 174) ; le texte de lecture dit, mesure par mesure, ce qui porte sur cette
  lentille. En variante B, la seconde course reste une seconde
  mesure de la même lentille, rapportée à côté selon son statut (devis v7, § 4).
- **Deuxième palier.** L'identité n'est pas établie et **le verdict du 18 ne se transporte pas** ; Lazar en est averti en ces termes
  dès le verdict d'identité, avant tout usage. **Mesures propres** : en variante B, celles de la seconde course, lues par un lecteur
  neuf sur un plan scellé ; en variante A, **aucune des mesures de la tranche du 18** (lecture contre pilotage, avance sur la lentille
  des logits, lecture côté entrée, accord du premier jeton entre moitiés, comparaison des deux codes, lecture contre ablation) : la
  lentille n'a à elle que la différence entre moitiés que son ajustement produit et, pour R, les deux séries ; le billet le dit.
  **Couches stables** : une couche n'est tenue pour stable que si `diffs` est au plus 0,10 **dans les deux ajustements** ; en
  variante B s'y ajoutent les limites que fixe la lecture de la seconde course.
  **Variante B, seconde course incomplète** (arrêtée après des ajustements copiés, avant la fin des mesures) : la lentille du
  deuxième palier reste sans mesure propre, comme en variante A ; elle est traitée comme en variante A (aucune lecture sans nœud de
  Lazar), et le billet le dit.
  Phrase permise si **les deux** lentilles sont au deuxième palier (les crochets se remplissent par les chiffres de la sortie du
  programme) : « Les deux lentilles mesurées le
  18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le même code d'ajustement, le même corpus et les mêmes graines
  sur une autre machine. Les fichiers obtenus ne sont pas identiques à l'octet. Deux comparaisons restent possibles. La différence
  entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée
  d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun aux deux moitiés. Pour la lentille R seulement,
  l'écart maximal de chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à
  l'autre, pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux
  séries, et ces changements sont un plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices des deux
  courses. Pour la lentille S,
  aucune comparaison de ce genre n'existe. Nous ne savons pas si les lentilles réajustées lisent comme celles du 18 novembre. Les
  mesures du 18 novembre [n'ont pas été refaites sur elles | ont été refaites sur elles et sont rapportées à côté]. »
  (*“The two lenses measured on 18 November were destroyed with the rented machine. We refitted them with the same fitting code, corpus and
  seeds on another machine. The files are not byte-identical. Two comparisons remain. The per-layer split-half difference deviates by
  at most [x] from the 18 November values (tolerance fixed in advance, by convention, at 10⁻³); this quantity is blind to any shift
  common to both halves. For lens R only, the largest entrywise gap of each matrix to the public lens and to the identity changes by
  at most [y] and [z] between the two runs, for gaps that ranged from [a] to [b] on 18 November; no threshold had been fixed in
  advance for these two series, and these changes are a lower bound, not an upper bound, on the largest entrywise gap between the matrices of the two
  runs. No such comparison exists for lens S. We cannot establish that the refitted lenses read like those measured on 18 November.
  The 18 November measurements [were not repeated on them | were repeated on them and are reported alongside].”*)
  Si **une seule** lentille est au deuxième palier, la phrase est écrite pour elle seule, au singulier, et l'autre reçoit la phrase
  de son propre verdict. Pour un verdict autre que les deux paliers (« différente », « non comparable », mention suspendue, non
  réajustée), cette phrase est : « Lentille [R | S] : verdict d'identité « [libellé exact] » ; elle n'est pas lue ici. » (*“Lens
  [R | S]: identity verdict “[exact label]”; it is not read here.”*)
  Pour R seule : « La lentille R mesurée le 18 novembre a été détruite avec la machine louée. Nous l'avons réajustée avec le même
  code d'ajustement, le même corpus et les mêmes graines sur une autre machine. Le fichier obtenu n'est pas identique à l'octet. La
  différence entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre
  (tolérance fixée d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun aux deux moitiés. L'écart
  maximal de chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à l'autre,
  pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux séries, et ces
  changements sont un plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices des deux courses. Nous ne
  savons pas si la lentille réajustée lit comme celle du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elle |
  ont été refaites sur elle et sont rapportées à côté]. »
  (*“Lens R, measured on 18 November, was destroyed with the rented machine. We refitted it with the same fitting code, corpus and
  seeds on another machine. The file is not byte-identical. The per-layer split-half difference deviates by at most [x] from the
  18 November values (tolerance fixed in advance, by convention, at 10⁻³); this quantity is blind to any shift common to both
  halves. The largest entrywise gap of each matrix to the public lens and to the identity changes by at most [y] and [z] between
  the two runs, for gaps that ranged from [a] to [b] on 18 November; no threshold had been fixed in advance for these two series,
  and these changes are a lower bound, not an upper bound, on the largest entrywise gap between the matrices of the two runs. We
  cannot establish that the refitted lens reads like the one measured on 18 November. The 18 November measurements [were not
  repeated on it | were repeated on it and are reported alongside].”*)
  Pour S seule : la même phrase, « La lentille S… », où la phrase des deux séries (« L'écart maximal de chaque matrice… des deux
  courses. ») est remplacée par « Aucune autre comparaison n'existe pour cette lentille. » (*“No other comparison exists for this
  lens.”*)
  « Même code d'ajustement » dit le code qui ajuste (code voisin, correctifs, bibliothèque des lentilles, précision, versions), non
  le lanceur, qui a changé (devis v7, § 5, point 5). Au deuxième palier ces mots sont couverts : les préalables « même code » et
  « K2 : … » du programme (§ 4) et la part du contrôle K2 tenue à la main (§ 7) sont tenus, sans quoi le verdict serait « non
  comparable ».
  **Ces chiffres sont obligatoires**, quel que soit leur sens, dans toute
  phrase du billet et du texte de lecture qui cite la lentille R au deuxième palier, et dans l'avertissement à Lazar ; **aucun
  qualificatif** ne leur est attaché (« inchangé », « stable », « négligeable », « a bougé »), faute de seuil fixé d'avance.
  Phrases interdites : « nous avons réajusté à l'identique les lentilles jugées le 18 novembre » ; « la lentille réajustée est proche
  de l'originale », « équivalente », « la même à la précision numérique près » ; « le verdict “partiel” du 18 novembre vaut pour la
  lentille employée ici » ; « la distance à la lentille publique est inchangée », ou toute phrase qui tire des séries de R un appui à
  la proximité ; toute phrase qui prête à la lentille réajustée une mesure faite sur celle du 18. (*“We refitted the same lenses”;
  “the refitted lens is close/equivalent to the original”; “the 18 November verdict applies to the lens used here”.*)
- **Dans tous les cas** : tout usage dans une lecture passe par un texte de lecture neuf, contre-lu, qui recopie le verdict d'identité
  et les chiffres de la sortie ; le billet dit le palier obtenu, quel qu'il soit, et, si la lentille n'est pas lue, le dit en une
  phrase (aucun retrait silencieux de la pièce 3) ; le verdict d'identité est écrit dans un fichier compagnon au lieu de rangement et
  à l'inventaire.

## 6. Audit, le même dans les deux sens
**Déclencheurs, tous rendus par le programme** (champ `declencheurs` de sa sortie) : (i) premier palier obtenu ; (ii) écart maximal
exactement nul avec des octets différents ; (iii) « différente » ; (iv) « non comparable », arrêt sur une erreur compris ;
(v) empreinte du fichier égale et une cause d'anomalie du § 4, arrêt sur une erreur compris ; (vi) pour R, au deuxième palier, 31 matrices des moitiés égales sur 31, ou une série dont le plus grand
changement est exactement nul ; (vii) écart maximal sur `diffs` supérieur à 10⁻³ quand l'écart sur `diffs_float64` tient le deuxième
palier, ou supérieur à 10⁻⁶ au premier palier. **L'audit est dû dès que cette liste n'est pas vide** ; le champ `audit_requis` de la
sortie, que le programme v4 pose à vrai dès qu'un déclencheur est présent et à faux sinon, le redit ; c'est la liste qui décide.
**Audit, fait par la mère ou par l'agent neuf du § 8, sans lire aucune mesure de la course.** Il dit, ligne par ligne, ce qui vient
du programme et ce qui est relevé à la main, avec chemin et empreinte :
- du programme : la liste des préalables, tenus ou non ; la table des écarts par couche et par cible, avec leur signe ; pour R, le
  compte des matrices égales et les deux séries ; les empreintes des pièces lues, le commit donné et le relevé du rattachement aux commits
  (chemin, commit, empreinte lue et empreinte au commit de chaque pièce neuve et du lanceur neuf) ; la table des différences des
  deux manifestes (`versions`, `commit`, champs de la configuration hors préalables, champs du haut du manifeste), **que le
  programme rend à tous les paliers, sans critère** (une sortie d'arrêt sur une erreur ne porte ni préalables ni tables) ;
- à la main : les contrôles K1 à K5, pour leur part à la main (§ 7), repris un à un, en commençant par K1 ; la provenance des deux côtés (l'empreinte neuve vient du
  fichier de la course neuve — identifiant, heure, taille — et est relue au lieu de rangement après la copie ; la référence est lue
  dans la pièce du 18 par son empreinte ; les deux ne sortent pas du même fichier).
**Ce que l'audit peut conclure.** Un contrôle manqué suspend la mention et ouvre un nœud de Lazar ; un audit sans contrôle manqué
laisse la mention telle que la procédure l'a rendue. **L'audit ne fait jamais monter une mention.** Pour le déclencheur (vi), s'il ne
trouve aucun contrôle manqué, la mention du programme reste, sans montée, et le verdict l'écrit en une phrase (« pour R, [31 matrices
des moitiés égales sur 31 | série … inchangée] malgré des octets d'ajustement différents ; audit sans contrôle manqué ») ; aucune
identité, de la lentille ni de son export, n'en est tirée. (Le cas n'est pas d'école : si seules les sommes de la cible `mid`
diffèrent d'une machine à l'autre, le fichier d'ajustement change d'octets alors que l'export de R, moyenne des sommes de la cible
`out`, peut être le même.)
L'audit est versé scellé avec le verdict d'identité. **Aucune relance pour obtenir un autre palier sans devis neuf et mot de Lazar.**

## 7. Programme, essais, et ce qui reste à la main
**Programme en vigueur, le seul que ce critère cite** : `src/controle_ia/neuron_lens/comparer_reajustement_v4.py`
(`4a0f3b2c8c73c282de3fbf7f18314e8085c7bbd03e4bb009c21775db78b09b01`) ; essais `tests/test_neuron_lens_comparer_reajustement_v4.py`
(`e1708b3932601b4bf4d8e5c1c55703879c2d186333ea83828311a748cf1192ee`). Empreintes recalculées par le rédacteur, égales à leur
compagnon. Pièce écrite par un développeur sur Claude Fable 5.2, que le rédacteur cite sans la modifier. Il lit les deux résultats
d'ajustement, les deux manifestes, pour R les deux résultats d'export, le texte des deux lanceurs, et, dans le dépôt qu'on lui
donne : les correctifs aux deux commits des manifestes, les pièces neuves au commit des résultats, le lanceur neuf au commit du
manifeste neuf. Il ne lit aucune mesure de la course. Il vérifie les pièces de référence contre le § 2 ; il rend la mention, les
déclencheurs (i) à (vii), `audit_requis`, les préalables avec leur détail, la table des écarts, le compte des matrices égales, les
séries de R, la table des différences des manifestes (champs du haut compris), les empreintes des pièces lues (celle du fichier du
lanceur de référence aussi, sans critère), le commit des résultats et le relevé du rattachement aux commits
(`rattachement_aux_commits`) ; il verse sa ligne de commande et refuse d'écraser une sortie (R12). Ses arguments obligatoires
comprennent le dépôt (`--depot`), le commit des résultats (`--commit-resultats`) et le chemin du lanceur neuf dans le dépôt
(`--chemin-lanceur-neuf`). La tolérance (10⁻³), la borne de cohérence (10⁻⁹), les bornes sur `diffs` (10⁻⁶ et 10⁻³), le seuil de
stabilité (0,10) et les cinq empreintes de référence sont des constantes, **égales à celles du programme v3** ; s'y ajoutent, pour
le seul arrêt sur une erreur, les deux empreintes de fichier d'ajustement du § 2 (`31061d6c…` pour R, `aac70eef…` pour S). Une
valeur non finie, non numérique ou absente rend « non comparable » (ou suspend le premier palier) avant tout maximum.
**Étiquettes.** L'en-tête du programme, sa constante `CRITERE` et le champ `critere` de chaque sortie nomment « le critère
d'identité du réajustement en vigueur (v5 à l'écriture du programme, 50657b89…) » ; les noms de préalables gardent des repères
anciens (H2, H3, H5, F2, F3). Ce sont des étiquettes : **le critère en vigueur est celui-ci, et les règles que le programme calcule
sont celles du § 4 de ce texte.** Le verdict d'identité cite ce critère-ci par son chemin et son empreinte.
**Essais** : 311, sur les pièces du 18 lues par leurs empreintes vraies, sur des copies altérées en mémoire ou dans un dossier
temporaire, et, pour ce qui lit le dépôt, sur de vrais dépôts temporaires (les 123 essais du programme v3, adaptés ; puis, pour
chaque garde neuve, un cas sain et au moins un artefact). **Rejoués par le rédacteur le 2026-11-19 : `311 passed`.** Ligne non
opposable (aucune sortie versée) : elle se refait par
`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_neuron_lens_comparer_reajustement_v4.py`.
**Banc d'altérations**, versé par le développeur dans `docs/notes/neuron-lens-v1/devis-reajustement/banc-programme-v4/` :
`banc_alterations_v2.py` (`67fcbd7e4572783f3e7bcf72e9cb2e866dd0d8078214b3b752c292950cf763f8`), sortie `sortie-banc-v3.txt`
(`1bc9d4cc94d95b74051cb113a1c5ab38cbe763176f1d274ab42e2dcfa849abdf`) ; empreintes recalculées, égales aux compagnons. Chaque garde
neuve est retirée ou faussée, une à une, sur une copie du programme : 84 altérations tuées sur 84, plus deux témoins (la copie non
altérée passe ; un libellé de palier changé est tué). Le rédacteur a lu la sortie, il n'a pas rejoué le banc.

**Contrôles que le programme v4 prend en charge, avec leur conséquence et leurs essais.** « Conséquence inchangée » veut dire :
« non comparable » à octets différents, mention suspendue à octets égaux, comme dans la v5.
| contrôle (lieu dans la v5) | ce que fait le programme v4 (libellé du préalable, ou champ de la sortie) | conséquence | essais |
|---|---|---|---|
| arbre propre (K2) | « K2 : `depot_propre` vrai dans le manifeste (neuf) » ; de même « (ref) » | inchangée | `test_v4_k2_depot_propre`, `test_v4_k2_depot_propre_faux_dans_le_fichier_du_manifeste` |
| lanceur neuf rattaché à sa course (K2) | « K2 : lanceur neuf égal, à l'octet, au fichier du commit du manifeste neuf » | inchangée | `test_v4_k2_lanceur_neuf_qui_n_est_pas_celui_du_commit`, `test_v4_k2_chemin_du_lanceur_faux`, `test_v4_k2_lanceur_lu_au_commit_du_manifeste_et_non_a_celui_des_resultats`, `test_v4_k2_octets_egaux_lanceur_non_rattache_suspend` |
| commits des manifestes lisibles dans le dépôt donné (K2) | « K2 : commit du manifeste lisible dans le dépôt (ref) » ; de même « (neuf) » | inchangée | `test_v4_k2_commit_du_manifeste_neuf_illisible`, `test_v4_k1_k2_releve_de_rattachement_manque`, `test_v4_sans_depot_rien_n_est_rattache` |
| commit des résultats (K1) | « K1 : commit de la branche de résultats en identifiant entier, lisible dans le dépôt » | **celle de K1, inchangée** : pas de verdict, comparaison refaite ; la mention rendue le signale | `test_v4_k1_commit_lisible`, `test_v4_k1_commit_des_resultats_absent_ou_mal_forme` |
| pièces neuves égales aux fichiers du commit des résultats (K1) | « K1 : résultat d'ajustement neuf égal, à l'octet, au fichier du commit des résultats » ; de même « K1 : manifeste neuf … » et, pour R, « K1 : export neuf … » | **celle de K1, inchangée** ; la mention rendue le signale | `test_v4_k1_piece_neuve_modifiee_d_un_octet_apres_le_commit`, `test_v4_k1_commit_d_avant_les_resultats`, `test_v4_k1_piece_hors_du_depot_sans_chemin`, `test_v4_k1_chemin_donne_faux`, `test_v4_k1_octets_egaux_piece_non_versee_suspend`, `test_v4_k1_k2_empreinte_au_commit_egale_a_celle_que_porte_la_sortie` |
| champs du haut du manifeste (K5) | table `differences_des_manifestes_sans_critere`, partie `haut` : tout champ hors `versions`, `commit` et `config` qui diffère ou n'est présent que d'un côté, avec sa présence, le début de sa valeur et l'empreinte de sa valeur entière, des deux côtés | **sans critère**, comme dans la v5 ; la recopie reste à la main | `test_v4_k5_haut_sain_seul_l_identifiant_de_course_differe`, `test_v4_k5_haut_champ_change_rapporte_sans_critere`, `test_v4_k5_haut_champ_present_d_un_seul_cote`, `test_v4_k5_haut_difference_au_dela_du_debut_de_la_valeur`, `test_v4_k5_haut_ne_double_pas_les_tables_existantes_et_montre_depot_propre` |
| pièce mal formée (règle de l'arrêt sur une erreur, § 4 de la v5) | sept préalables « forme : … » ; un lanceur illisible comme source Python manque le préalable de la fonction | inchangée (la v5 rendait le même verdict par la règle de l'arrêt) | `test_v4_piece_mal_formee_rend_non_comparable_avec_motif`, `test_v4_cli_fichier_mal_forme_ecrit_une_sortie_non_comparable`, `test_v4_entree_qui_n_est_pas_le_dictionnaire_attendu`, `test_v4_lanceur_neuf_illisible_comme_python` |
| arrêt sur une erreur (§ 4 de la v5) | sortie écrite : `arret_sur_erreur`, `erreur`, `noeud_de_lazar`, mention, déclencheur libellé (iv) ou (v), code de sortie 2 | inchangée ; le filet de la v5 reste pour l'arrêt sans sortie | `test_v4_cli_arret_sur_une_erreur_ecrit_la_sortie_et_le_motif`, `test_v4_cli_arret_reference_illisible_le_resultat_neuf_porte_l_empreinte_du_18`, `test_v4_sortie_arret_sur_erreur_choix_de_la_mention`, `test_v4_erreur_inattendue_dans_la_comparaison_rattrapee`, `test_v4_cli_erreur_inattendue_dans_la_comparaison_ecrit_la_sortie` |
| audit dû (§ 6 de la v5) | `audit_requis` vrai dès que la liste des déclencheurs n'est pas vide, faux sinon | la règle du § 6 est inchangée | `test_v4_audit_requis_pour_tout_declencheur` |
| champ `etape` de l'export (défaut du programme v3 relevé dans la v5) | « champ `etape` de l'export égal à « export » (ref) » ; de même « (neuf) » | celle de tout préalable | `test_v4_etape_de_l_export`, `test_v4_etape_de_l_export_au_premier_palier_suspend`, `test_v4_etape_de_l_export_sans_objet_pour_s` |
| seuils, libellés et empreintes de référence inchangés | constantes | — | `test_v4_aucune_regle_de_decision_ne_change` |

**Ce qui reste à la main — liste fermée, K1 à K5, appliquée par qui applique le critère (§ 8), avec chemin et empreinte, dans les deux
sens et à tous les paliers. Aucun de ces contrôles ne peut faire monter une mention.** Chacun dit ce que le programme fait déjà, ce
qui reste à la main, et pourquoi le programme ne le fait pas.
- **K1 — Le bon programme sur les bonnes pièces.** *Fait par le programme* (§ 4, préalables « K1 : … ») : le commit donné est un
  identifiant entier, lisible dans le dépôt donné ; chaque pièce neuve lue (résultat d'ajustement, manifeste, résultat d'export
  pour R) a exactement les octets du fichier de son chemin à ce commit, et la sortie porte ce chemin, ce commit et les deux
  empreintes (`rattachement_aux_commits`, `pieces_lues`). *Reste à la main.* Avant le lancement : l'empreinte du programme est celle
  de ce paragraphe. Après : le commit que porte la sortie (`commit_resultats`) est la tête de la branche de résultats du dépôt
  distant, lue après la destruction de la machine (`git ls-remote`), quand plus rien n'y peut être poussé. *Pourquoi à la main* :
  le programme ne voit que le dépôt local qu'on lui donne, non le dépôt distant, et il ne peut pas répondre de sa propre empreinte.
  Manqué, que ce soit la part à la main ou un préalable « K1 : … » : pas de verdict ; la comparaison est refaite sur les bonnes
  pièces, sous un nom de sortie neuf, et la première sortie est versée aussi. **La mention « non comparable » (ou la suspension, à
  octets égaux) que rend le programme quand un préalable « K1 : … » est manqué signale ce manqué ; elle ne remplace pas cette règle
  et n'est pas le verdict.**
- **K2 — Le code qui a tourné est celui du manifeste.** *Fait par le programme* (§ 4, préalables « K2 : … ») : les deux manifestes
  portent `depot_propre` vrai ; les deux commits des manifestes sont lisibles dans le dépôt donné ; le lanceur neuf donné au
  programme (empreinte `lanceur_neuf` de la sortie) est égal, à l'octet, au fichier du chemin donné (`--chemin-lanceur-neuf`) au
  commit que porte le manifeste neuf. *Reste à la main.* Ce chemin est celui du fichier de lanceur que nomme la commande scellée de
  la course neuve ; ce lanceur fixe l'ancre des séries de R comme celui du 18
  (`REVISION_NEURONPEDIA = "d2527c3cdbaa60dd4b65cbca1604921f044e989a"` et, pour `npR`, l'empreinte
  `a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c` : lanceur du 18, l. 58 et 130-131), et le module de contrôles
  qu'il importe (`controles_b_beta_v2` pour celui du 18, l. 51) porte, au même commit, les textes de `ecart_max`, `ecarts_identite`
  et `ecarts_npr` du commit `5e5cb65b…` (méthode `empreinte_fonction` du programme :
  `4f6be7e9709d58bbcc009cf8101aa4131578e2d467ce1f2d142059a330002819`, `587e98a80863f7ca3f7a704f427173221982f6093cbb259e37498e160c1a599d`,
  `51c9cee2c1bc19cca6c28ae80e86c4879b5e3b7eb1e35c7bfe40b0e3d1ffeaf0`) ; le dépôt donné au programme est le dépôt de travail.
  *Pourquoi à la main* : le programme ne sait pas quel fichier nomme la commande scellée, ne lit ni l'ancre ni le calcul des séries,
  et ne peut pas dire quel dépôt on lui donne. Manqué : « non comparable » (octets différents) ou mention suspendue (octets égaux).
- **K3 — Matériel de la machine neuve.** Le modèle de carte, la version du pilote et les versions de la machine sont recopiés dans le
  verdict depuis la pièce du matériel que le lanceur neuf verse (devis v7, § 5, point 5 g), **à tous les paliers, sans vis-à-vis au
  18, où ils ne sont pas consignés : le verdict l'écrit**. *Pourquoi à la main* : cette pièce n'est pas une entrée du programme.
  Manqué (pièce absente) : pas de verdict, nœud de Lazar.
- **K4 — Reprise sur sauvegarde.** Seul le journal de l'étape d'ajustement de la lentille est ouvert
  (`journaux/ajustement-R.log` ou `journaux/ajustement-S.log` du dossier de résultats de la course neuve, au commit de K1), et
  seulement ses en-têtes de lancement (une ligne commençant par « === » par lancement, écrite par `executer`, lanceur du 18,
  l. 226-231 ; le lanceur neuf garde cette écriture) : plus d'un en-tête, relance de l'étape, tenue pour une reprise ; un seul, aucune
  reprise. L'indication donnée au programme (`--reprise`, champ `reprise` de la sortie) dit ce que ces en-têtes disent. Aucun autre
  journal de la course n'est ouvert avant le verdict d'identité : en variante B, ils portent des mesures. *Pourquoi à la main* : le
  programme ne lit pas le journal. Manqué (indication contraire aux en-têtes) : la comparaison est refaite comme en K1 ; journal absent
  ou illisible : pas de verdict, nœud de Lazar.
- **K5 — Champs du haut des deux manifestes.** *Fait par le programme* : la table des différences des manifestes porte, sans
  critère, chaque champ du haut qui diffère ou n'est présent que d'un côté (`commande`, `cree_le`, `decisif`, `graines`,
  `preenregistrement`, `reserves`, `config_sha256`, `depot_propre`, `run_id`, et tout autre champ hors `versions`, `commit` et
  `config`, rendus ailleurs dans la même table). *Reste à la main* : ces différences sont recopiées dans le verdict, **sans
  critère** — une course neuve a d'office une autre commande et une autre heure ; quand la sortie ne porte pas la table (arrêt sur
  une erreur), le relevé est fait à la main sur les deux manifestes, comme dans la v5. *Pourquoi à la main* : le programme rend la
  table, il n'écrit pas le verdict. Manqué (relevé non recopié) : pas de verdict.
Restent aussi à la main, par nature : la relecture au lieu de rangement (§ 4, point 5), l'audit (§ 6), le verdict d'identité et
l'avertissement à Lazar (§ 5, § 8).

**Défauts du programme v4 relevés par le rédacteur, sans effet sur les règles de ce critère** (le programme reste à son
développeur ; le rédacteur ne l'a pas modifié) :
1. ses étiquettes nomment la version 5 du critère (ci-dessus) ;
2. le code de sortie 2 est à la fois celui de l'arrêt sur une erreur, sortie écrite, et celui d'une ligne de commande refusée,
   sans sortie ; une sortie déjà présente est refusée sous un autre code, et une sortie apparue pendant la comparaison arrête le
   programme sans sortie (filet du § 4) ;
3. à l'arrêt sur une erreur, « porte l'empreinte du 18 » est vrai aussi quand l'empreinte neuve est celle de l'autre lentille, ou
   celle que porte une pièce de référence qui n'a pas été vérifiée : le sens est celui de la suspension, dont l'autorisation est la
   même (aucune lecture sans nœud de Lazar) ;
4. la lecture de secours faite après un arrêt ne rattrape que les erreurs de lecture et de valeur : une autre exception à ce
   moment arrêterait le programme sans sortie (filet du § 4) ;
5. rien ne confronte le chemin d'une pièce neuve au dossier de la course neuve, ni le commit des résultats à la branche de
   résultats ou au commit du manifeste : la part de K1 tenue à la main y répond ;
6. la sortie d'arrêt sur une erreur ne porte pas la table des différences des manifestes, même quand les deux sont lisibles (K5 se
   fait alors à la main) ;
7. l'aide de l'argument `--reprise` et l'en-tête parlent du « journal de la course » : la règle est celle de K4, le seul journal
   de l'étape d'ajustement.
Une version neuve du programme demanderait une version neuve, courte, de ce critère.

## 8. Qui applique
- Les empreintes des fichiers d'ajustement sont calculées par programme sur la machine, avant l'envoi.
- La comparaison est lancée **par la mère ou par un agent neuf qu'elle lance**, jamais par la session des lentilles, **avant toute
  lecture d'une mesure de la nouvelle course**, avec le programme scellé du § 7 **dont l'empreinte est vérifiée avant le lancement**,
  sur les pièces **prises sur la branche de résultats poussée par la machine** (commit de K1, noté et donné au programme en identifiant
  entier, avec le dépôt de travail et le chemin du lanceur neuf dans ce dépôt), jamais sur une
  copie remise par la session des lentilles ; pour R, les deux pièces d'export sont toujours fournies ; l'indication d'une reprise est
  lue comme le dit le contrôle K4, dans le seul journal de l'étape d'ajustement.
- La même personne applique les contrôles K1 à K5, pour leur part à la main, et le point 5 de la procédure (relecture au lieu de rangement), puis l'audit du
  § 6 si un déclencheur est levé.
- La ligne de commande, la sortie, les relevés à la main et l'audit sont versés scellés avec le verdict d'identité ; le verdict est
  écrit, scellé et rapporté à Lazar par la mère, avec, au deuxième palier, l'avertissement du § 5.

## 9. Deux nœuds proposés à Lazar (hors critère ; rien ici ne change une règle)
Tous deux viennent de l'annexe de la vérification du programme v2 (`8cd01e58…`, remarques 6 et 7) ; ils sont posés dans le devis v7
(§ 7, décisions 6 et 7), dans le format de décision. Texte gardé de la v5.
1. **Mesurer l'écart d'un réajustement par un essai court, avant la course.** Le même ajustement sur quelques dizaines de documents,
   sur deux machines, puis la comparaison des empreintes et des différences entre moitiés. Ce serait la première mesure de ce que ce
   critère dit non mesuré (§ 3), et elle dirait si le premier palier est plausible. **C'est une dépense** : nœud de Lazar, sur devis.
   Si Lazar l'accorde et que la tolérance du deuxième palier devait en être revue, ce serait par une version neuve de ce critère,
   écrite et contre-lue avant la course entière, jamais après.
2. **Faire verser par la course neuve un croquis numérique de chaque matrice** de chaque lentille (projections sur des vecteurs tirés
   d'une graine fixée, normes par couche). Le 18 n'a laissé aucune grandeur qui compare deux matrices : c'est pourquoi le deuxième
   palier dit « matrices non comparables ». Le croquis ne change rien au verdict de cette course-ci (le 18 n'en a pas) ; il rendrait
   un réajustement **futur** comparable matrice par matrice. Sans dépense propre (quelques minutes de processeur en fin de course),
   mais c'est un ajout au lanceur neuf et aux pièces versées : Lazar tranche.

## 10. Ce que ce critère ne fait pas
Il ne dit pas si une lentille réajustée est **bonne** : seules des mesures faites sur elle le disent (variante B, ou une course de
mesure à part, sur devis). Il ne fixe pas le statut de la seconde mesure ni le plan de sa lecture (pièces à part, scellées avant la
création). Il ne décide d'aucun usage dans le programme : chaque expérience le dira dans son préenregistrement (R1).
