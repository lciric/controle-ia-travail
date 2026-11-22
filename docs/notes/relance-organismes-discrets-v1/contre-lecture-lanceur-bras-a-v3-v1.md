# Contre-lecture du lanceur de la course du bras A, version 3 — classe B, neuve

- **Date (UTC)** : 2026-11-22. Relecteur : agent neuf (Claude Sonnet 5.5), qui n'a écrit ni le lanceur, ni les essais, ni la note. Processeur seul, aucun réseau, aucune dépense, rien committé.
- **Lu** : `src/controle_ia/organismes_discrets/lanceur_bras_a_v3.py` (`dae151d5a46ef2069ed3a425f264b6b5a34256be2f980954774cbc642e36d666`, recalculée, égale à son compagnon) ; `tests/test_lanceur_bras_a_v3.py` (`15cfc292…`) ; la note du code (`a34612dd…`) ; `lanceur_bras_a_v2.py` (comparé) ; le texte `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` (13.2 ligne 1498 ; sections 2, 3.1 ; 6.1, 6.2, 6.3, 6.4 ; 8.1 à 8.5) ; le devis de la ligne 1 (`devis-bras-a-v5.md`, lu par `git show` sur `origin/relance-bras-a/devis-carte-v3`) ; `.claude/hooks/garde_calcul.py` seul ; `registres/go.md` (format seulement). Cloisonnement tenu.
- **Rejeu** : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_lanceur_bras_a_v3.py` : **67 essais passent** (124 s). Garde statique du cloisonnement (`cloisonnement_bras_a_v13`) sur `src` et `scripts` : `[]`. Cinq sondes ajoutées par moi (hors dépôt, scratchpad) : manifeste altéré, compagnon absent, pièce altérée, pièce supprimée, identifiant à saut de ligne — tous refusés, aucune destruction.

## Verdict : à corriger

Aucun défaut bloquant : le lanceur ne dépense rien, ne supprime rien, n'arrête une instance qu'après un manifeste de versement scellé et intact, et suit la lettre de la ligne 1498. Un défaut majeur est hors du fichier relu (la garde de calcul du dépôt) et doit être tranché avant le départ de la ligne 1 ; les autres sont mineurs.

## Défauts, classés

### Majeurs

**M-1 — La garde de calcul ne reconnaît pas les identifiants de GO à trois chiffres, et ignore leurs lignes sans le dire** (`.claude/hooks/garde_calcul.py`, lignes 52 et 53 ; lecture ligne 85). La remarque de la note est **confirmée**. `GO_ID = \bGO-…-\d{2}\b` rend `[]` sur `GO-2026-11-22-145` (essayé) ; `LIGNE_GO` ne reconnaît pas non plus la ligne au registre. Deux effets : (a) toute commande de création d'instance qui cite un GO à trois chiffres est bloquée « sans identifiant » (ma propre commande d'essai, qui contenait ce texte, l'a été) ; (b) plus grave, `lire_go` saute en silence toute ligne `| GO-…-NNN |` : **une révocation à trois chiffres ne révoque rien** pour la garde, et un GO à trois chiffres cité avec un identifiant à deux chiffres n'est pas vérifié (R5 : aucun repli silencieux). Le devis cite lui-même GO-2026-11-22-145, -143, -146 : ces identifiants existent au registre de la branche principale. Correction (session principale, nœud de modification de la garde) : `\d{2,}` aux deux motifs ; ligne qui commence par `| GO-` et que `LIGNE_GO` ne reconnaît pas → blocage explicite ; deux essais (cas sain à trois chiffres, artefact : révocation à trois chiffres reconnue). Le lanceur v3 (`_GO`, ligne 100, `\d{2,}`) est correct de son côté.

**M-2 — La ligne 1 n'est pas liée au constat de départ ni au plafond** (`jouer_ligne_1`, ligne 436 ; `CompteurDePlafond.__init__`, ligne 386). `jouer_ligne_1` ne demande ni le constat de départ (crédit, GO, tarif), ni que le plafond du compteur soit au plus 18 USD, ni que son taux soit le tarif relevé : un appelant qui passe `CompteurDePlafond(1000, 0.01, …)` joue la ligne sans refus. Le texte (8.1) dit que le contrôle en échec « refuse la dépense qu'il conditionne » ; ici le refus n'existe que dans la commande de constat. Correction : `jouer_ligne_1` reçoit le constat (ou son empreinte) et refuse si `compteur.plafond_usd > constat["plafond_usd"]` ou si `compteur.taux` est inférieur à carte + stockage relevés ; deux essais (sain ; compteur à 1000 USD refusé).

### Mineurs

**m-1 — Un fichier du versement peut échapper à l'inventaire** (`inventaire`, ligne 685). Le filtre porte sur `p.name` : un fichier nommé `manifeste-du-versement.json` (ou son compagnon) dans un sous-dossier est exclu de l'inventaire scellé (essayé : inventaire `['a']`). 8.5 veut un inventaire de tout ce qui a été produit. Correction : exclure seulement le chemin `dossier / NOM…` exact, et refuser tout autre fichier de ce nom.

**m-2 — Écriture non sérialisable : fichier tronqué et erreur non gardée** (`ecrire_sans_ecraser`, lignes 424 à 432). Le fichier est ouvert en « x » puis `json.dump` échoue en `TypeError` (essayé) : un fichier partiel reste, et l'erreur n'est pas un `GardeArret`. Il ne s'efface pas (c'est voulu), mais il fausse l'inventaire. Correction : sérialiser en mémoire d'abord (`json.dumps`), puis écrire d'un coup en « x » ; convertir l'erreur en `GardeArret`.

**m-3 — Le GO n'est pas rapproché de la ligne** (`exiger_ligne_de_go`, ligne 300 ; `par.startswith("Lazar")`, ligne 317). Rien ne lie le périmètre du GO à la ligne 1 (un GO de calcul de 18 USD ou plus pour autre chose passe) ; et `startswith` admet « Lazar-quelque chose » là où la garde de calcul exige l'égalité avec « Lazar ». Correction : égalité exacte ; le périmètre reste un point de la session (le texte n'écrit pas de marque), à dire dans la note.

**m-4 — Tarif « du jour » non daté contre l'horloge** (`exiger_tarif`, ligne 348 ; 13.2, case « tarifs » : « relevés et datés, au jour du devis »). La date n'est contrôlée que dans sa forme : un relevé d'il y a une semaine passe. Correction : refuser si la date du relevé n'est pas celle du jour UTC de départ (ou dire dans la note que c'est la session qui le tient).

**m-5 — Essais manquants pour des gardes écrites** : (a) `N = 2`, `lot` et `max_nouveaux` faux dans la configuration de référence (code, `_reference`, lignes 163 à 168) : seul `T = 9` est joué ; (b) le motif « change l'acceptation » et « change la lecture de l'environnement » ne sont pas distingués (`test_lecture_de_l_environnement…` n'exige que `motif in MOTIFS_DE_CONTENU`) ; (c) le témoin bénin laissé honnête à sa dose n'est pas éprouvé ; (d) le plafond exact (cumul égal) et la coupe à exactement 20 % (256 actions : n'arrête pas) ne sont pas joués, alors que « plus de » / « au-dessus » sont des seuils stricts du texte ; (e) le rejeu réel (`lanceur_bras_a_v2.rejouer`) n'est éprouvé que par lecture du source (`inspect.getsource`), non par un rejeu sur le jouet.

**m-6 — Dose reçue calculée aussi sur les jumeaux de vérification** (`fabriquer_condition`, ligne 562) : le test `len(retenus) == 128` vaut aussi pour les 128 épisodes de vérification de `fabriquer_jumeaux_de_verification` ; 6.4 point 2 ne vise que les transcriptions des doses et du témoin bénin. Inoffensif (aucun arrêt n'en dépend) mais à rendre explicite par un paramètre.

**m-7 — Le texte « ne cite pas le lanceur »** (8.4, ligne « lanceur qui nomme ce texte ») n'est pas vérifié par le lanceur : il pourrait confronter l'empreinte du lanceur au texte scellé (absente). Facultatif ; à dire dans la note.

## Exigence par exigence (ligne 1498 ; sain / artefact, R5)

| exigence | lettre portée | cas sain | artefact |
|---|---|---|---|
| configuration scellée citant l'empreinte du texte scellé | oui | `test_configuration_saine` | marqueur, texte archivé (par empreinte et par chemin), brouillon, autre chemin, empreinte fausse ou abrégée, compagnon faux, non conforme : refusés |
| joue l'honnête à la seconde ligne | oui (appelle `rejouer` de la v2, honnête d'abord, échelle 0) | `test_honnete_d_abord…` | ordre inversé, désordre des adaptateurs, 15 tâches : refusés (m-5 e) |
| non permutable avant le tirage | oui | `test_forme_de_fin_non_permutable…` | fabrication sans la règle : arrêt A2 |
| découpage vérifié, rejeu, laissé honnête aux quatre doses sans arrêt | oui | `test_six_adaptateurs_sains` | valeur soudée plantée ; lecture changée (m-5 b, c) |
| `N = 1`, `T = 10` | oui | `_reference` | `T = 9` seul (m-5 a) |
| aucune suppression ni destruction avant le manifeste scellé (8.5) | oui | `test_versement_puis_destruction` | sans manifeste, inventaire changé, manifeste altéré : refusés (m-1) |

**Marqueur** (`EMPREINTE_TEXTE_V2_BRAS_A`, ligne 74) : refusé dans le chemin et dans l'empreinte, avant toute autre vérification ; le texte archivé `06ab6a2f…` l'est par empreinte et par chemin ; le brouillon par son nom ; chemin exact imposé. Conforme à 8.1 et à 8.4 (ligne 1163). Le marqueur lui-même n'est pas écrit dans le texte (le texte dit « marque en capitales » refusée par le validateur) : c'est un choix du rédacteur, sans incidence.

**Suppression et destruction** : aucune fonction du lanceur n'efface, ne déplace ni n'écrase (essai par analyse du source, et `lanceur_bras_a_v2.py` ne contient aucun `unlink`, `rmtree`, `remove`, écriture en « w », `torch.save`). `detruire_l_instance` vérifie le manifeste (présent, empreinte égale au compagnon, inventaire identique) **avant** de valider l'identifiant et d'appeler la fonction d'arrêt ; identifiant en chiffres seuls, `fullmatch` (saut de ligne refusé), aucun motif de ligne de commande (R10). Réserve de portée : « versé sur une branche » (8.5) est tenu par la session, non par le lanceur.

**Refus au départ** : crédit lu strictement sous 20 USD refusé (nombres non finis, booléens, chaînes refusés) ; GO absent, de forme fausse, de type autre que calcul, non accordé par Lazar, périmé, révoqué, de plafond sous 18 USD, de plafond illisible, en doublon, ligne mal formée : refusés ; GO-2026-11-18-62 refusé ; tarif carte, stockage ou téléchargement au-dessus des bornes de la configuration de référence (1,30 ; 0,08 ; 0,05, égales à celles du devis) refusé, égalité admise. Les formes de plafond du registre réel (« N USD », « N,N USD », « N USD (sur crédits) », « N USD au plus… ») sont lues ; les autres sont refusées par `RegleNonEcrite`, sans choix silencieux.

**Compteur** : durée depuis la création × (carte + stockage) + frais fixes ; « au-dessus » strict arrête, égalité passe (lettre de la ligne 1157) ; relevé avant et après chaque lot de huit épisodes, y compris le seizième (essai) ; le lot joué est écrit avant le relevé. Dépassement maximal d'un lot (≈ 5,5 minutes, ≈ 0,13 USD) : accepté, à dire (voir M-2 pour le lien au constat). La coupe anticipée à plus de 256 actions sur 1 280 est équivalente au compte final (le compte ne décroît pas) : conforme à 8.2.

**Graines** : conforme à la lettre de 6.2 et à R9. 6.2 écrit pour « génération des épisodes » et « adaptateurs » : `manifeste.graines(clés, entropie)` sur `fabrication/tache/{id}/e{k}`, `verification/tache/{id}/e{k}`, `injection`, `adaptateur/{nom}`, `distillation/{nom}` ; la table fermée de `graines_bras_a_v4` ne couvre que les usages neufs sous `bras-a-v2/` et **refuse** ces clés (essayé : « refusée »). La coupe (`usage = 0x636F7570`), le dérangement (`generateur_derangement`) et `ouve` (par `lots.separation`) suivent le tableau ; `SeedSequence`, dérivation par clé, collisions contrôlées par `exiger_cles_distinctes`, manifeste (configuration, empreinte, versions, graines, commit) : R9 tenue. Différence avec la v2 : la clé `modele-jouet` n'est pas dérivée (inutile au modèle réel) ; l'identifiant de tâche contenant « / » est refusé (6.2). Si la consigne de la session était « `graines_bras_a_v4` seulement », la lettre du texte prime : l'écart est signalé dans la note, à juste titre.

**Les trois règles non écrites** (`RegleNonEcrite`, lignes 206, 313, 327) : (1) *entropie en décimal dans le texte* : l'inscription de l'entier dans le texte **est écrite** (13.1, case « entropie » : « l'entier est inscrit ici ») ; seuls le format décimal et l'absence de contrainte de place (n'importe où dans le texte) sont du rédacteur — affiner en ne cherchant que dans la ligne « entropie » de 13.1 ; (2) *GO à plusieurs lignes* : refus prudent ; la garde de calcul admet les extensions (R-389), le lanceur les refuse : plus strict, jamais plus large, mais à dire ; (3) *plafond illisible* : réellement non écrite, refus prudent. Aucune des trois n'ouvre quoi que ce soit de plus que le texte. Les neuf autres « règles » de la note sont soit écrites (distillation à 384 pas, section 2 ; révocation, en-tête du registre), soit des refus ou des choix de forme sans effet sur une dépense.

**Rien de plus que le texte** : aucun appel réseau, aucune clé lue, aucune création d'instance, aucun module cloisonné chargé (essai et garde statique). Le lanceur n'ouvre que ce qu'il peut vérifier ; ses extensions sont des refus.

## Comparaison avec la version 2

La v3 garde la fabrication au grain du jeton, remplace `fabriquer` (arrêt sur contexte changé) par `retenir_et_controler` (épisode laissé honnête sous son motif, garde de la forme de fin avant le découpage, puis rejeu), ajoute la configuration scellée, le constat de départ, le compteur, la coupe A14, le versement et la destruction gardée ; elle réutilise `jouer_honnetes` et `rejouer` de la v2, non modifiés (lots de huit épisodes de la même tâche : mêmes lots qu'en v2). Aucune régression trouvée.

## Prochaine action proposée

Corriger M-2 et m-1, m-2, m-3 dans une version neuve du lanceur (R12), puis faire trancher M-1 par la session principale ; les essais de m-5 peuvent suivre.
