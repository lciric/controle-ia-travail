**concordant si C-1 : le texte doit fixer un seul moment pour sceller notre fiche de réception. Aujourd'hui, il dit « avant la création » à deux endroits et « avant la récupération » à quatre. C-2 à C-9 sont de forme, sans condition. Aucun écart de fond, aucun nœud de Lazar : N-A est sans objet. De notre côté, la procédure et le script de réception, écrits pour l'addendum v2, doivent passer en version 2 avant la récupération (R-1 à R-5).**

# Concordance de l'addendum v3 de relance de R1 (brouillon 2) avec nos deux analyses scellées et notre procédure de réception — v1

- **Lecteur** : sous-agent neuf (Claude, Opus 5.5), règle R2. Je n'ai écrit ni l'addendum v3, ni ses brouillons, ni sa contre-lecture. Je n'ai pas écrit non plus nos deux analyses scellées, leurs contre-lectures, les concordances antérieures, la procédure de réception ou son script.
- **Date** : 2 novembre 2026, de 23:30 à 23:58 UTC (`date -u`).
- **Dépôt** : `/home/claude/controle-ia-travail`, consulté en lecture seule (`git show`, `git diff`, `git ls-tree`, `git log`, `git cat-file`).
  - Interdits respectés : aucun `fetch`, `checkout` ni `stash` ; aucun fichier ouvert sous `diag/`, `runs/` ou `donnees/` ; aucune branche `calcul/…` lue ; aucun commit ; aucun `.sha256` ; aucun réseau ni modèle ; `nice -n 10` pour tout calcul.
  - Un seul fichier neuf : celui-ci. Les écarts au protocole sont décrits en annexe.
- **Abréviations** (« l. » = ligne de `git show … | cat -n`) :
  - « A » : le texte relu, `git show 49d29c8e:prereg/R1-addendum-relance-v3.md` ;
  - « A1 » : son brouillon 1 (`145da951`) ;
  - « V2 » : l'addendum v2 scellé (`c2a8b6e1`) ; « V2b1 » : le brouillon 1 de V2 (`21a6e583`) ;
  - « V1b3 », « V1b4 » : l'addendum v1, brouillons 3 (`cdca33bb`) et 4 (`72f68fea`) ;
  - « P » : l'analyse principale scellée (`83ce7a91`), code au commit `a8b7fdb2` ;
  - « S » : l'analyse secondaire scellée (`7a238666`), code au commit `326601cf` ;
  - « MOD3 » : `src/controle_ia/runs_nuit/rejeu_activations_v3.py` au commit `f921fcec` ;
  - « PR » : la procédure de réception v1 ; « SF » : son script des fiches v1 ;
  - « CL1 » : la contre-lecture 1 de A1 ; « VER » : le verdict de conv-audit sur le rejeu à graine (`64fab1a5…`).

## En bref (une ligne par point)

- **Pièces.** Toutes les empreintes annoncées sont exactes. La différence entre A1 et A est, à l'octet, le `.patch` versé (`73de584a…`). Aucun fichier de code n'a changé depuis le commit cité `f921fcec`.
- **Formats.** MOD3 écrit exactement ce que lisent P et S : mêmes trois fichiers, mêmes tableaux, mêmes formes et types, mêmes clés lues du résultat. La clé `tokenisation`, champs v3 compris, est tolérée par les deux. Ni P ni S ne lit le manifeste au-delà du rattachement par empreinte.
- **P-R5.** A rétablit exactement les comptes sous lesquels P et S ont été scellées (2 236, 1 782, 164). P rapporte P-R5 sans verdict propre. S perd son bras (i) au-delà de 240 actions non fidèles (marge : 76) ; A le déclare.
- **Différence avec V1b3** (n° 354, point 1). Pour nos textes, A ne change rien d'autre que :
  - un retour au parent (E2, E4, E14, E15, E19) ;
  - les champs de `tokenisation` (E16) ;
  - deux ajouts sans effet sur nos lectures : la reprise (E21) et la réserve sur HG-2.
- **Point 1 (renvois de la v2).** Chaque renvoi atterrit. Trois inexactitudes de forme : C-2, C-5, C-6.
- **Point 2 (essai au nom hérité).** La déclaration suffit ; il ne faut pas renommer (confiance ≈ 0,85). Il faut seulement la préciser (C-4).
- **Point 3 (E16).** La réserve tient (MOD3 l. 66 et l. 454). Ni P, ni S, ni SF ne lisent `tokenisation.addendum`. Notre fiche doit :
  - lire le texte qui gouverne la course dans le manifeste ;
  - attendre `tokenisation.addendum` = `prereg/R1-addendum-relance-v2.md` à l'identique (R-3).
- **Point 4 (N-A et lignes gelées).** N-A est sans objet : il n'y a aucun épisode non résolu, et MOD3 arrête toute course dont un épisode signalé manque à la table. Aucune ligne gelée de P ni de S n'est contredite. Restent trois rappels antérieurs : AP-5, empan rejoué vide, N2.
- **C-1 (requis).** A fixe deux moments différents pour sceller notre fiche de réception :
  - « avant la création » (l. 130 et l. 455-456) ;
  - « avant la récupération » (l. 17, 140, 272-273, 351).

  Le n° 295 en annonce un troisième (« avant la lecture », après la création). Une instance créée avant notre fiche contreviendrait à la liste d'arrêt scellée : ce serait un écart, donc un nœud.
- **De notre côté.** PR et SF ont été écrits pour l'addendum v2 :
  - préconditions P1 et P2 ;
  - `--addendum-chemin` vaut `…-v2.md` par défaut ;
  - clé `addendum_v2` dans `redaction` ;
  - table v3 notée mais non comparée ;
  - manifeste non lu.

  Il faut une version 2 avant la récupération (R-1 à R-5).

## 0. Pièces, empreintes, sceaux

| Pièce | Vérification | Résultat |
|---|---|---|
| A (brouillon 2) | `git show origin/prep/r1-relance-v3:…` (tête `49d29c8e585a106b5376570bd129e207621a696d`) \| `sha256sum` | `86c68b0ec323cfdce1a6a21d1fcee14ed8d0647f485906eb031e7ee6ac32746d` = attendu ; 518 l. ; sans compagnon (non scellé, comme annoncé) |
| A1 | `git show 145da951:…` | `382ba6272ea0856dd9ba699f1d16eabef66fc12be288c214af71c5de28a5a05d` = attendu |
| Différence A1 → A | `git diff 145da951 49d29c8e -- prereg/R1-addendum-relance-v3.md \| sha256sum` | `73de584a…` = `corrections-apres-contre-lecture-v1.patch` versé, identique à l'octet. Les blocs du diff sont exactement ceux du tableau des corrections (`83e9808e…`) : I1 ×4, I2, M1 ×5, M2, M3 ×2, M4, deux remarques, en-tête. Rien d'autre ne bouge. |
| CL1 | `git show …:docs/notes/runs-r1-r2-r4-v1/relance-v3/contre-lecture-addendum-relance-v3-v1.md` | `c19fdbc7d6f83a5ce26b12b0fa9b5604a8bbfba8086691e723837836576add59` = attendu |
| Code | `git diff --stat f921fcec 49d29c8e -- src tests scripts` | vide. Chaîne linéaire : `c2a8b6e1` → `f921fcec` → `d803a8d6` → `145da951` → `a62f44df` → `49d29c8e`. Les neuf empreintes de l'en-tête (A l. 34-48) sont égales au recalcul. `rejeu_activations_v1.py` vaut `dde8aa67…`, l'empreinte que cite P (l. 7). `manifeste.py` vaut `1a5c7464…` à `a8b7fdb2`, `326601cf`, `f921fcec` et `49d29c8e` |
| Configuration v5 | lecture des clés ; recalcul de l'empreinte canonique (JSON aux clés triées, séparateurs compacts, = `manifeste.config_canonique`) ; différence avec la v4 | fichier `acad6253…` ; 29 clés ; canonique `1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4`. Seules `chemin_table_tokenisation` (`prereg/R1-table-tokenisation-v3.json`) et `table_tokenisation_sha256` (`ead8a668…`) diffèrent de la v4. `nom_sortie` = `activations-p3-rejeu-v1`, couches [7, 15, 23], `seuil_non_conformes` = 10. Sans compagnon (annoncé) |
| Table v3 | structure et comptes seulement | `ead8a668…`, compagnon conforme ; version 3 ; 22 entrées. Méthodes : `une_paire` 12, `deux_paires` 2, `fins` 1, `fenetre` 2, `trois_paires` 1, `identifiants` 4 (les quatre épisodes nommés en A l. 108-109). `non_resolu` 0. Comptes : 240 / 151 / 129 / 22 / 151. `corrections_verifiees` 22. `fins_du_format` [128001, 128008, 128009]. `resultat_graine_sha256` = `67482545…` ; `table_v2_sha256` = `5f6cf489…` |
| Pièces de mesure (A l. 78-87) | `sha256sum` | toutes égales : pré-vol `61dd497e…` et `b9dbadba…` ; suite ciblée `e02256ee…` (20 fichiers, commit `d803a8d6`, « 329 passed in 1484.24s ») ; bornes `8dc0eef7…` (« 23 passed ») et `afb17d9d…` ; contrôles `208abebc…` ; essai jouet `fd1db837…`, `b7a0dc1f…` |
| 329 essais | dénombrement | 302 (V1b4 l. 45 ; les 18 fichiers sont inchangés de `72f68fea` à `f921fcec`) + 22 (`test_resolution_graine_v1.py`) + 5 (`test_rejeu_activations_v3.py`) = 329. Aucune paramétrisation |
| Garde de forme | `controle_ia.prereg.problemes`, texte passé par l'entrée standard | A : `['section vide ou à remplir : Contre-lecture']` (le seul marqueur, celui du traitement final) ; V2 : `[]` |
| Libellés lus par le script | `grep -c "<libellé> : \`"` sur A | « Tests attendus », chemins de la configuration, de la table et du parent : une occurrence chacun. Le paragraphe ajouté par I2 ne les répète pas sous la forme lue |
| Textes parents | `sha256sum` | V2 `9d17d640…` ; V2b1 `7915a3d6…` ; V1b3 `cb3664ba…` ; V1b4 `485acc3a…` |
| P et S | `sha256sum` ; listes fermées | P `8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537` (244 l.) : ses sept modules ont l'empreinte de sa liste (l. 116-122). S `1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9` (249 l.) : ses quatre modules v3 sont égaux (l. 27-30). Le commit `5f2f9bf5` (lecture par épisode) est absent localement ; je ne l'ai pas récupéré, il est hors de cette concordance |
| Réception | `sha256sum -c` des compagnons | PR `d85bd5e4…`, SF `6836016f…`, essais de SF `65f8bdb2…`, rapport `c77100dd…`, VER `64fab1a5…` : tous conformes. Fiche de réception du rejeu à graine : `1193a54a…` |
| Messages, registres | `sha256sum` ; `git show` des seules lignes citées | n° 295 `399bde0f…` ; n° 354 `ef4a15d5…` (compagnon conforme). `registres/go.md` de `main` à `f1791003`, l. 215 : GO-2026-11-02-27, 60 USD, échéance le 16 novembre. `registres/decisions.md` au même commit : R-1060 (l. 1288 : `64fab1a5…`, « sans règle B », « aucun nœud », « -27 relance de R1 sur la table v3 60 ») et R-1033 (l. 1261 : « N-A = (c) puis (a) »). R-1116 du registre de conv-audit (l. 1080) |
| Non vérifiable ici | — | Sorties scellées du rejeu à graine (`8e6a4912…`, `67482545…`) et scores de R2 (`10838eea…`, `1ebbeff8…`) : elles sont sur des branches `calcul/…` que je ne dois pas lire. `67482545…` est aussi le `resultat_graine_sha256` de la table v3 et la valeur citée par VER l. 156. Les empreintes de R2 sont les mêmes qu'en V1b3. Notre procédure les vérifie contre les compagnons à la réception (PR, étape C) |

## 1. Formats : ce que la relance v3 écrit, ce que lisent nos deux analyses

| Ce que lisent nos textes | Ce que MOD3 écrit | Concordant |
|---|---|---|
| Trois fichiers `activations-p3-rejeu-v1{,-maximum,-complement-hors-cout}.npz`, tableaux `moyenne`, `maximum`, `maximum_hors_cout`, plus 9 communs et l'identité (P l. 60-61 ; `constantes_v1.py` l. 44-48 ; S l. 141) | `nom_sortie` de la configuration v5 ; MOD3 l. 420-433 : `commun` = identité, `jetons_empan`, `jetons_empan_rejeu`, `couches`, `conforme_longueur`, `contexte_conforme`, `ecart_fidelite`, `fidele`, `trajectoire_identique`, `activations_identiques` ; dossier neuf (l. 418, `exist_ok=False`) | oui |
| Forme (2 400, 3, 4 096), float16 (`entrees_v1.py` l. 208-209 ; `entrees_v3.py` l. 109-111) | l. 368-370 ; couches [7, 15, 23] | oui |
| Résultat rattaché au manifeste par empreinte ; `verdict_fidelite` = « conforme » ; `regle_repli_appliquee` booléen ; `couches` ; `textes_sha256` ; `identite_sha256` ; `fichiers` (`entrees_v1.py` l. 175-223 ; `manifeste.py` l. 142-150) | l. 436-440, puis `ecrire_resultat` (l. 471) | oui |
| P recopie `lecture`, `controle_negatif`, `fidelite_toutes` (`lecture_v1.py` l. 244-246) | l. 437, 443, 446-453 | oui. P y lit aussi une clé `trajectoires`, absente depuis la v1 : elle vaut `None`, défaut antérieur sans effet |
| S lit par pointeurs `fidelite_conforme`, `regle_repli`, `textes_sha256`, `couches`, `contexte_rejeu`, `regle_empan`, `modele` (S l. 139 ; SF l. 38-41) | clés `verdict_fidelite`, `regle_repli_appliquee`, `textes_sha256`, `couches`, `contexte`, `regle_empan`, `modele` (l. 436-440, 469) | oui |
| S exige `moyenne` finie sur les 2 400 actions, ainsi que `jetons_empan`, `jetons_empan_rejeu` et `fidele` (S l. 141, 207 ; `entrees_v3.py` l. 106-113) | `moyenne` reste non finie seulement si l'empan rejoué est vide (l. 372-374). Antérieur, voir § 7 | oui |
| `fidele` : exclusion par `fidele`, la même pour tous les bras (P l. 57) ; garde de 10 % (S l. 154) | l. 413-415 : `notees & conforme & (ecart ≤ tol)`, restreint à `traj` sous repli. C'est la voie retenue sur C-1, sans forçage à faux. A l'écrit juste (l. 232-233) | oui |
| Clé `tokenisation`, champs v3 compris | l. 454-467. P ne contrôle l'ensemble des clés que sur la fiche (`entrees_v1.py` l. 26, 42-74). S contrôle les noms de pointeurs, pas les clés du résultat. Aucune occurrence de `tokenisation` ni d'`addendum` dans les sept modules de P, ni dans `constantes_v3`, `entrees_v3`, `evaluation_v3`, `lecture_v3`, `entrees` et `constantes` de S | toléré |
| Arrêt : fiche `R1: null` avec motif ∈ {`rejeu_non_conforme`, `rejeu_en_echec`} (P l. 97 ; S l. 139) | « non conforme » (fidélité ou contrôle négatif) ou « echec » (toute autre cause, table et gardes de durée comprises : A l. 297-298, E16) ; SF l. 33 fait la correspondance | oui |
| Commande, texte gouvernant et `decisif` du manifeste : lus ni par P ni par S (`verifier_resultat` ne lit que `run_id` et l'empreinte du manifeste) | `commande` = `python -m controle_ia.runs_nuit.rejeu_activations_v3` (l. 65, 212) ; `preenregistrement` = {chemin relatif, sha256 du texte scellé} (`manifeste.py` l. 88-96), passé par le script (`PREREG` vaut l'addendum v3 par défaut, script l. 47 et l. 279) | sans effet sur nos lectures ; la fiche doit les vérifier (§ 6) |
| Branche : `calcul/r1-r2-reel-v1`, seule refspec (P l. 96) | E18 et étape 3 : versement par un commit neuf, à l'octet (C-2 de la première concordance) | oui |

A ramène la course aux conditions exactes sous lesquelles P et S ont été scellées :
- P l. 8 : « 2 236 actions sur 2 400 conformes en longueur, 1 782 en contexte exact ; saboteur 556 / 437 » ;
- S l. 154 : « 2 236 … 1 782 … 164 sur 2 400 » ;
- ces valeurs sont celles de A (E4, E14, « Prédiction ») et du pré-vol.

## 2. P-R5 et gardes de lecture

- **P.** P-R5 est « observé à côté du prédit, sans verdict propre » (P l. 48, l. 161). La seule règle de part des fidèles est la couverture : sous 0,80 pour le saboteur ou l'honnête, la lecture est « non concluant (rejeu partiel) » (P l. 82, l. 148 ; `COUVERTURE_MIN`, `constantes_v1.py` l. 86 ; `lecture_v1.py` l. 295). Selon le cas :
  - à la borne haute : 568/600 et 556/600 ;
  - au scénario bas : 471 et 437, sous 480 ;
  - sous repli : 420 et 350 ;
  - dans les deux derniers cas, la lecture est « non concluant (rejeu partiel) ».

  A le dit (l. 218-220 ; E15). Ce sont des lignes du parent et de P, non contredites.
- **S.** La garde est « plus de 10 % d'actions non fidèles : (i) non lu » (`NON_FIDELES_MAX` = 0,10, `constantes_v3.py` l. 54 ; `entrees_v3.py` l. 159-164).
  - Les 2 400 actions sont notées : P-R5 contraire équivaut donc exactement à la garde.
  - Il y a au moins 164 actions non fidèles (les actions non conformes en longueur). La garde saute dès que plus de 76 des 2 236 actions conformes en longueur sortent de la tolérance. C'est la marge sous laquelle S a été scellée.
  - L'empan rejoué diffère pour 164/2 400 actions = 6,8 %, sous 10 % : réserve seulement.
  - Si le repli s'applique, (i) n'est pas lu.

  A le déclare (l. 222-224, conséquence du n° 343). Concordant.

## 3. Différence avec le brouillon 3 de la v1 (n° 354, point 1)

De V1b3 à V1b4, rien ne touche les formats, les règles ni les comptes : seulement des dates, le pire cas de E9, CLA-12, m-1, m-8 et le fichier de concordance consigné. La colonne « v1 » de A (V1b4) vaut donc pour V1b3.

| Écart | Ce qui change depuis V1b3 | Effet sur P, S et PR |
|---|---|---|
| E1, E20 | table v3 (rejeu à graine), revérifiée tout entière au chargement | aucun, sinon des arrêts plus nombreux, lus « rien n'est lu » |
| E2, E3, E5, E6 | règle B sans objet (0 non résolu au lieu de 4) ; seuil de 10 sans effet ; ligne « plus de 10 » retirée | moins d'actions hors contexte exact (40 → 0 dans les épisodes non résolus) ; aucune classe ne change |
| E4, E14, E15 | comptes du parent rétablis (151 ; 1 782 ; 1 510) | ce sont les comptes de P l. 8 et de S l. 154 |
| E7 | inchangé | — |
| E8 | arrêts ajoutés ; conditions du lancement (notre concordance, notre fiche) | **C-1** |
| E9 | gardes de 600 et 720 minutes, aucun budget qui coupe ; pire cas ≈ 17,6 USD | aucun (nos textes ne lisent aucune durée) |
| E10 à E13 | 329 essais, configuration v5, module v3, commande changée, contrôle négatif sur 22 épisodes | commande : sans effet sur P et S ; refusée par notre code « R2 seul » (§ 7) |
| E16 | champs v3 ; `addendum` = v2 | tolérés (§ 1) ; point 3 (§ 6) |
| E17, E18 | GO-27 ; branches nouvelles, versement sur `calcul/r1-r2-reel-v1` | concordant avec P l. 96 |
| E19 | N-A sans objet | § 7 |
| **E21** (nouveau) | une reprise unique après une erreur d'infrastructure, sans aucun fichier d'activations écrit, même commit et même entropie, branche `-v2` | aucun sur nos lectures. La fiche doit nommer la course arrêtée (R-4). Précision R4 recommandée : C-8 |
| Réserve HG-2 (nouvelle) | ligne de lecture ajoutée « sans effet sur aucune classe » (l. 441) | aucun : nos textes ne la lisent pas. Elle est rapportée à côté (R-1) |
| Attentes de réception (étape 3) | réécrites : table `ead8a668…`, `episodes_non_resolus` = [] | PR et SF ne les vérifient pas toutes (§ 6) |

## 4. Point 1 — où atterrissent les renvois de l'addendum v2 (A l. 152-170)

La source citée est exacte : V2 l. 175-183, « Renvoyé à l'addendum v3 » ; objets G3 à G10 de V2b1 l. 111-118.

| Renvoi (V2 l. 175-183) | Contenu dans V2b1 | Atterrissage dans A | Verdict |
|---|---|---|---|
| G3 | E19 « sans objet si r′ = 4 ; sinon couverte, pour les épisodes nommés » (l. 111) | E19 (l. 141) : sans objet, r′ = 4 | atterrit |
| G4, G5, P-R5 | 147 + r′ ; 1 742 + 10 r′ ; 1 470 + 10 r′ ; 272 et 2 236 inchangés (l. 112-113) | E4, E14, E15, « Prédiction » (l. 126, 136-137, 195-208) : 151, 1 782, 1 510, 272, 2 236 ; comptes par condition égaux au pré-vol | atterrit |
| G6 | configuration v5, module v3, code « R2 seul » nommé avec son paquet `controle_ia.analyse_principale_r1_r2` (l. 114) | E11, E12, E16 | atterrit. Le nom du paquet, demandé par la précision (2) du n° 354, est perdu en E12 (**C-5**, forme) |
| G7 | tests de la relance (l. 115) | E10 et en-tête : 329 (vérifié au § 0) | atterrit |
| G9 | contrôle négatif étendu (l. 117) | E13 : 22 épisodes, forme `identifiants` comprise (pré-vol) | atterrit |
| G10 | « Traitement de C-1 (nom hérité de `test_relance_regle_b_non_resolus_fidele_faux_et_seuil`) … docstring et nom à corriger dans le code du rejeu v3, ou déclarés à nouveau dans le complément » (l. 118) | le fond de C-1 → E2 et « Métrique » (l. 229-233) ; le nom et la docstring → déclarés à nouveau (l. 160-164) | atterrit (voir § 5). A cite G10 au singulier (« déclaré ») ; l'original dit « déclarés » (**C-4**) |
| Étape 3 de V2b1 (préalables, complément court) | module v3, configuration v5, essais, puis un complément scellé qui cite le commit, la configuration, la table, le nombre d'essais et les non résolus ; puis concordance ; puis lancement (l. 297-303) | A en tient lieu entier : en-tête (commit, empreintes, 329, aucune entrée `non_resolu`), étape 1 (concordance), E17 (GO-27 au lieu de GO-02) | atterrit |
| Ligne « Relance » des critères | « lignes de la v1 et du parent, inchangées (dont « plus de 10 non résolus → rejeu non validé ») » (l. 353) | « Critères de lecture gelés » ; la part « plus de 10 » est sans objet (E5, E6). Elle ne peut pas jouer : la table n'a aucune entrée `non_resolu` et exige une couverture exacte (`classer_episodes`, l. 437-446) | atterrit |
| Attentes de réception (m-8) | `table_sha256` = `5f6cf489…`, exactement 4 non résolus → à réécrire (V2 l. 181-183) | étape 3 (l. 351-362) : `ead8a668…`, [] | atterrit |

Trois défauts de forme dans le paragraphe :
1. « Les objets G3 à G10 … retirés de la v2 scellée » (l. 152-153) : G8 n'a pas été retiré, il figure dans V2 (l. 172). Il faut écrire « G3 à G7, G9 et G10 » (**C-2**).
2. « Rien d'autre n'est renvoyé par ces lignes » (l. 170) : les lignes 179-181 de V2 portent aussi quatre engagements, tous tenus ailleurs mais non nommés dans le paragraphe (**C-6**) :
   - la table v3 est citée (l. 54-58) ;
   - le résultat scellé du rejeu est cité (l. 65-68) ;
   - la configuration v5 cite la même table (§ 0) ;
   - la concordance porte sur la différence avec V1b3 (l. 271-272).
3. La précision (2) du n° 354 est perdue en E12 (**C-5**, voir le tableau).

## 5. Point 2 — l'essai au nom hérité (G10)

- **Faits.** Le fichier `tests/test_runs_nuit_v2.py` vaut `3d9237a5cc1b3de5025ca08f21781addabb56323f256394835b4e781cfec2daf` à l'identique de `5e678b5b` à `49d29c8e`, sans compagnon. Il figure dans `CIBLES` (script v3 l. 255). Deux chaînes y disent encore « fidèle = faux » :
  - le nom de la fonction (l. 134) ;
  - la docstring du fichier (l. 4 : « règle B (actions des épisodes non conformes à `fidele` = faux, … ») ;

  alors que l'assertion (l. 173-177) éprouve la voie retenue, la tolérance. La docstring de la fonction (l. 135-137) parle d'autre chose : du tirage restreint du jeu jouet.
- **Ce que nous avions accepté.** Le n° 354, précision (3), donnait deux voies : « corriger la docstring et le nom … ou ajouter une ligne dans le traitement de C-1 ». La concordance du brouillon 3 (`d6952cad…`, point 6.3) disait : « à défaut, une ligne … suffit », et ajoutait que la concordance finale « n'a pas à les redemander ». G10 (V2b1 l. 118) reprend les deux voies. A prend la seconde (l. 160-164), conforme à V1b4 (l. 445-447, m-1).
- **Recommandation : ne pas renommer ; la déclaration suffit** (confiance ≈ 0,85).
  - (a) Aucune lecture n'en dépend. L'essai éprouve la règle B du module v2 ; la v3 l'importe telle quelle, et elle est sans objet dans cette relance (0 non résolu). Nos analyses lisent le tableau `fidele`, jamais un nom d'essai.
  - (b) Renommer imposerait un commit de code neuf. Il faudrait alors :
    - changer le commit cité, que vérifie `exiger_code_cite` sur l'arbre gelé ;
    - refaire l'empreinte du fichier et de l'en-tête ;
    - rejouer les 329 essais avec le tokeniseur (≈ 25 minutes) ;
    - rejouer le pré-vol, l'essai jouet et les contrôles d'avant l'installation.

    Ce coût et ce risque n'auraient aucun effet sur une lecture.
  - (c) R12 : l'ancien nom reste dans l'historique de toute façon.
  - Seule exception : si un commit de code devenait nécessaire pour une autre raison avant le scellement, y joindre le renommage.
- **Précision demandée (C-4, forme).** Nommer les deux chaînes et leurs lignes : nom l. 134, docstring du fichier l. 4, contre l'assertion l. 173-177. Citer l'empreinte `3d9237a5…`. Citer G10 exactement : « déclarés ».

## 6. Point 3 — la réserve E16 et ce que doit vérifier notre fiche de réception

### La réserve tient

MOD3 l. 66 définit `ADDENDUM = "prereg/R1-addendum-relance-v2.md"`, que la l. 454 écrit dans `tokenisation.addendum`. Cette constante a été écrite quand la relance devait relever de la v2 (docstring, l. 1 et 17).

Le texte qui gouverne la course n'est pas lu dans cette constante. Il est porté par le manifeste :
- `preenregistrement.chemin` et `preenregistrement.sha256` (`manifeste.py` l. 88-96) ;
- ces valeurs sont alimentées par `--prereg`, qui vaut par défaut l'addendum v3 (script l. 47 et l. 279) ;
- MOD3 en exige les citations : configuration, parent, entropie, commit (l. 186-200).

Changer la constante changerait le code cité : même coût qu'au § 5. Aucun lecteur ne lit cette clé : ni P, ni S (§ 1), ni SF (l. 161-172 : seuls `episodes_non_resolus` et `table_sha256` sont lus, le second seulement noté). L'étiquette ne peut tromper qu'un lecteur humain : la fiche doit donc écrire les deux valeurs, chacune à sa place.

### PR et SF sont écrits pour l'addendum v2

Défauts constatés (ils sont nôtres, pas ceux de A) :
- P1 attend « Addendum v2 scellé … `$ADDENDUM_SHA` » ; P2 attend la « concordance finale de l'addendum v2 » ; `NON_INVERSIBLES` est « recopiée de l'addendum v2 (E19) » (PR l. 25-26, 48-51).
- SF l. 257-258 : `--addendum-chemin` vaut par défaut `prereg/R1-addendum-relance-v2.md`, et l'appel de PR (l. 156-158) ne le passe pas. Si l'on passe l'empreinte du texte v3, `redaction.addendum_v2` (l. 226) inscrit le chemin v2 avec l'empreinte v3, sans aucune garde. C'est un repli silencieux (R5).
- SF ne lit pas le manifeste (il le hache seulement, l. 135). Il note `tokenisation.table_sha256` sans le comparer (l. 169).
- Ses essais supposent une table `5f6c…` et la clé `addendum_v2` (`test_ecrire_fiches_reception_v1.py` l. 62, l. 111).
- PR, étape I (l. 303, 308-309), donne au lecteur R13 « l'addendum v2 scellé » et « la liste `$NON_INVERSIBLES` (E19) ».

### Ce que notre fiche de réception doit vérifier

Il s'agit du document de contrôles scellé avant la récupération, sur le modèle de `fiche-reception-rejeu-graine-v1.md` (`1193a54a…`). Il est distinct des deux fiches JSON de P (l. 97) et de S (l. 139), écrites après le versement. Toutes les lectures se font par clés nommées, sans tableau et sans valeur de résultat.

1. **Textes.**
   - A scellé : chemin, empreinte, commit de scellement ;
   - configuration v5 : `acad6253…`, canonique `1cfb7fba…` ;
   - table v3 : `ead8a668…` ;
   - parent : `80c85a00…` ;
   - code : `f921fcec`, arbre gelé identique au commit de scellement ;
   - notre concordance sur la version scellée : chemin et empreinte ;
   - voie de réception : la seule refspec `calcul/r1-r2-reel-v1` (P l. 96 ; PR, étape C).
2. **Manifeste du rejeu** (`runs/<REJEU>/manifeste.json`, sceau vérifié).
   - `commande` = `python -m controle_ia.runs_nuit.rejeu_activations_v3` ;
   - `decisif` = vrai ;
   - `preenregistrement.chemin` = `prereg/R1-addendum-relance-v3.md` ;
   - `preenregistrement.sha256` = l'empreinte de A scellé ;
   - `config_sha256` = `1cfb7fba…` ;
   - `config.table_tokenisation_sha256` = `ead8a668…` ;
   - `commit` = le commit de scellement lancé.
3. **Résultat `diag/<REJEU>/rejeu-activations.json`.**
   - `verdict_fidelite` = « conforme » ; sinon `R1: null` avec son motif fermé ;
   - `tokenisation.version_table` = 3 ;
   - `tokenisation.table_sha256` = `ead8a668…`, cette fois **comparé** et non seulement noté ;
   - `corrections_verifiees_au_chargement` = 22 ;
   - `episodes_non_resolus` = [] et `actions_non_resolues` = 0 ;
   - `tokenisation.addendum` = `prereg/R1-addendum-relance-v2.md` exactement : écrit comme provenance de la table, jamais comme texte gouvernant. Toute autre valeur signale un autre code : arrêt.
   - les comptes de l'étape 3 de A : 240, 151, 2 400, 2 236, 1 782, 129, 22, comptes par méthode, `par_methode_resolution`, `seuil_non_conformes` = 10, `fideles_parmi_non_resolues` = 0.

   Toutes ces valeurs sont fixées par la table et quasi certaines. Un écart signale une autre course ou une autre table : arrêt, nœud.
4. **À ne pas lire avant les analyses** : ce sont les sorties de l'instrument que lisent P et S elles-mêmes.
   - `fidelite_toutes.fideles`, `notees`, `fideles_parmi_contextes_conformes`, `egalite_exacte`, `ecart_max`, `ecart_mediane` ;
   - `tokenisation.part_fideles_parmi_notees`, `p_r5_au_moins_90_pour_cent` ;
   - `fidelite_echantillon`, `controle_negatif`.
5. **Fichiers.** Les trois `.npz` ont leurs noms, leurs empreintes égales à `fichiers` et à leurs compagnons. SF le fait déjà.
6. **E21.** S'il y a eu une reprise : nom de la course arrêtée, empreinte de son `arret.json` s'il existe, annonce de la reprise faite avant la création. On lit la seule course nommée par le fournisseur. La liste attendue des runs à l'étape C de PR est complétée en conséquence.
7. **Réserve sur HG-2.** Elle est rapportée à côté des résultats, sans changer aucune classe.

## 7. Point 4 — N-A et les lignes gelées de nos analyses

- **N-A (P l. 146 : « épisode conforme à trajectoire différente → rejeu non validé : rien n'est lu »).** La décision de Lazar N-A = (c) puis (a) (R-1116, l. 1080 ; recopiée en R-1033, l. 1261) couvre la copie « pour ce qui reste » après la résolution. La première concordance l'écrivait déjà : « si les 7 épisodes sont résolus, N-A disparaît ». La première étape (c), la résolution des épisodes, est allée au bout : 7 sur 7 (VER l. 10, l. 171).

  Dans le code, une course qui va au bout ne peut garder aucun épisode entièrement conforme en longueur à trajectoire différente :
  - `classer_episodes` arrête si un épisode signalé manque à la table, ou si un épisode de la table n'est pas signalé (`resolution_tokenisation_v1.py` l. 436-441) ;
  - la table v3 n'a aucune entrée `non_resolu` ;
  - chaque correction doit redonner l'empreinte de P3, sinon la course s'arrête (MOD3 l. 317-319) ; l'épisode corrigé devient alors `trajectoire_identique` (l. 321) ;
  - les autres épisodes conformes en longueur sont identiques dès la base.

  La lecture « après la table » est celle que conv-audit a toujours appliquée aux épisodes corrigés : les deux concordances antérieures ne comptaient sous N-A que les épisodes non résolus. **N-A est sans objet ; aucune décision nouvelle n'est requise.** E19 (l. 141) l'écrit fidèlement.
- **Autres lignes gelées : aucune n'est contredite.**
  - P l. 57 (exclusion par `fidele`), l. 73-74 (couverture, exclusions, sensibilité au contexte exact), l. 147-149 (repli, couverture sous 80 %, réserve de contexte), l. 161 (prédictions sans verdict propre), l. 175 (arrêts de R1) ;
  - S l. 139, 141, 154, 207, 224-225.

  Les formats sont au § 1, P-R5 et les gardes au § 2.
- **Rappels antérieurs, ni créés ni changés par A.**
  - **AP-5** : une action éligible dont tout l'empan est dans le champ COST garde `maximum_hors_cout` non fini (MOD3 l. 380-384, copie de la v2 sans marque `# v3`). P s'arrêterait alors après son manifeste (P l. 175). Le cas n'est pas mesuré par le pré-vol.
  - **Empan rejoué vide** : la `moyenne` resterait non finie (l. 372-374) et S s'arrêterait (`entrees_v3.py` l. 112-113). Ce cas non plus n'est pas mesuré : le pré-vol compte les `jetons_notes` de P3 (2 400 > 0), pas les empans rejoués.
  - **N2** est tranché (N2 = (a), R-1116) ; la réserve N2 suit S (PR, étape H).
- **Code « R2 seul » de conv-audit** (paquet `controle_ia.analyse_principale_r1_r2`, `constantes_v3.py` l. 16 et l. 29-30, `entrees_v3.py` l. 55-77 ; ce n'est aucune de nos deux analyses). Il n'accepte comme preuve d'arrêt que la première course : `RUN_R1_ARRETE`, commande v1, texte parent. Une preuve d'arrêt de la relance v3 y serait refusée. Le défaut est antérieur et signalé (E12). Il n'est à reprendre que si la relance s'arrête et que Lazar veut une lecture « R2 seul ».

## 8. Changements demandés

### À l'addendum (non scellé)

- **C-1 (requis : cohérence interne).** Il faut une seule règle pour le moment où la fiche de réception de conv-audit est scellée.
  - **Aujourd'hui** :
    - « pas de création sans … sa fiche de réception scellée » (E8 (d), l. 130 ; liste d'arrêt, lancement, l. 455-456) ;
    - « scellée avant la récupération » (GO-2026-11-02-27 cité l. 17 ; E18, l. 140 ; étape 1, l. 272-273 ; étape 3, l. 351) ;
    - et le n° 295, § 1, annonce la création puis « fiche de réception scellée avant la lecture ».

    Créer l'instance avant notre fiche contreviendrait à la liste d'arrêt une fois scellée : écart, donc nœud.
  - **Recommandé** : écrire « avant la récupération » partout, c'est-à-dire la lettre du GO-27 et la pratique du rejeu à graine (fiche scellée à 16:45 UTC, après la création de 16:42:40). Retirer la fiche des conditions de création. Désigner l'objet : le document de contrôles de conv-audit, distinct des fiches JSON de P (l. 97) et de S (l. 139), écrites après le versement.
  - **Autre voie** : garder « avant la création » et aligner sur elle l'étape 1, E18, l'étape 3 et la séquence du n° 295. Conv-audit peut alors sceller sa fiche juste après sa concordance sur la version scellée.
  - Confiance ≈ 0,65 ; le défaut est la lettre du GO-27.
- **C-2 (exactitude, forme).** Paragraphe des renvois (l. 152-153) : écrire « G3 à G7, G9 et G10 », car G8 est resté dans V2 (l. 172).
- **C-3 (exactitude, forme).** Réserve sur HG-2 (l. 182-183). A écrit que les 93 épisodes manqués l'ont tous été par la durée, « budget d'étape de 2 400 s ». Selon VER (l. 11, l. 201), le budget d'étape couvre 91 épisodes : 90 non tentés et 1 coupé à l'échéance. Les 2 autres ont été coupés par le budget d'épisode de 600 s. Il faut écrire ces deux chiffres.
- **C-4 (précision, forme).** Déclaration de l'essai hérité (l. 160-164) : nom l. 134 et docstring du fichier l. 4, contre l'assertion l. 173-177 ; empreinte `3d9237a5…` ; G10 cité exactement (« déclarés »).
- **C-5 (précision (2) du n° 354, forme).** E12 (l. 134) : nommer le paquet du code « R2 seul », `controle_ia.analyse_principale_r1_r2`, sur la branche `canal/conv-audit-n04`, comme le faisait G6 (V2b1 l. 114).
- **C-6 (complétude, forme).** Après « Rien d'autre n'est renvoyé » (l. 170), ajouter une phrase sur les quatre engagements de V2 l. 179-181, tenus aux l. 54-58, aux l. 65-68, par la configuration v5 et aux l. 271-272.
- **C-7 (procédure de versement, forme).** À l'étape 3 (l. 348-349) et en E18, écrire que la branche source se remplace aux **deux** endroits de l'étape 7 de `procedure-relance-r1-v2.md` : la refspec du `git fetch` (l. 238) et `R` (l. 242), avec `-v2` après une reprise E21. Citer son empreinte `ae1ff089…`, inchangée depuis V1b4 et sans compagnon (R6). Sinon, l'étape s'arrête (« rien à verser ») : il n'y a pas de repli silencieux, mais une étape perdue.
- **C-8 (symétrie R4, recommandé, sans condition).** E21 (l. 143) : si la course arrêtée a écrit au journal `etape=fidelite lecture=…` ou `etape=controle_negatif lecture=…`, la reprise les rapporte à côté des siennes. Une lecture différente est rapportée comme réserve d'instrument, sans choisir entre les deux courses. Les graines sont identiques : seul un calcul non déterministe pourrait faire différer les lectures.
- **C-9 (exactitude, forme).** l. 368-369, « l'analyse secondaire … lit R4 … avec `R4.activations` nul ». En fait, notre procédure écrit `R4: null` (SF l. 235 ; rapport de préparation, point 8). Écrire plutôt : « ne lit pas le rejeu de R4 (fiche `R4` nulle ou `R4.activations` nul, au choix de conv-audit) ».

### De notre côté (procédure et fiche de réception ; pas des conditions posées à l'addendum)

- **R-1.** Écrire la procédure de réception v2, sous un nom nouveau (R12).
  - P1 et P2 renvoient à A scellé (chemin, empreinte, commit), à la configuration v5, à la table v3 et à notre concordance sur la version scellée.
  - `NON_INVERSIBLES` est fixé vide (E2, E19).
  - À l'étape I, le lecteur R13 reçoit « N-A sans objet » et la réserve sur HG-2.
- **R-2.** Écrire le script `ecrire_fiches_reception_v2.py`, avec une clé neutre `addendum` (texte qui gouverne, lu dans le manifeste) et `provenance_table` (`tokenisation.addendum`). À défaut, passer obligatoirement `--addendum-chemin prereg/R1-addendum-relance-v3.md` à SF.
- **R-3.** Ajouter au script les contrôles du § 6, points 2 et 3. Chaque garde neuve est éprouvée sur un cas sain et sur un artefact (R5). Les essais doivent porter sur une table `ead8a668…`, et non plus `5f6c…`.
- **R-4.** Pour E21 : noter la course arrêtée, s'il y en a une, et compléter la liste attendue des runs à l'étape C de PR.
- **R-5.** Sceller la fiche de réception, document de contrôles du § 6, au moment fixé par C-1.

## 9. Ce que la concordance sur la version scellée devra vérifier

1. `git diff 49d29c8e <scellement> -- prereg/R1-addendum-relance-v3.md` ne doit porter que sur l'en-tête (version, date), l'entrée « Traitement final » remplie et les changements C-1 à C-9 faits. Toute autre ligne se relit contre les § 1 à 7. Un changement de règle, de classe ou de seuil est un nœud de Lazar.
2. Empreintes et sceaux à vérifier :
   - A scellé et son compagnon ;
   - la configuration v5 : `acad6253…`, canonique `1cfb7fba…`, désormais avec compagnon ;
   - la table v3 : `ead8a668…` ;
   - le parent : `80c85a00…` ;
   - `prereg.problemes` = [] ;
   - les quatre libellés présents une fois chacun.
3. Code et commit :
   - `git diff --quiet f921fcec <scellement> -- src tests scripts` doit sortir avec le code 0 ;
   - le commit de scellement ne porte que le texte, la configuration et leurs compagnons ;
   - aucun « amend » ni « reset » ;
   - les contrôles d'avant l'installation sont rejoués au commit de scellement (étape 1).
4. La consignation de ce rapport dans `docs/notes/runs-r1-r2-r4-v1/concordance-relance-v3-consignee-v1.md`, avec son compagnon.

## 10. Remarques (aucune demande)

- **Message du script.** Le message de garde du script pour `DELAI_REJEU_MIN` (l. 57) dit encore « avant tout clonage ». Le texte, corrigé par I1, est juste ; le message est sans effet.
- **« Les deux sont rapportées »** (l. 240-241, déjà dans V1b3 l. 159, concordé). La phrase vise les comptes du fournisseur. P ne calcule que la sensibilité sur `contexte_conforme` (P l. 74). Une lecture restreinte aux trajectoires identiques n'est dans aucun de nos textes : ce serait un nœud, jamais une lecture ajoutée (P l. 163).
- **P-R5 observée hors du résultat.** La valeur observée de P-R5 apparaît :
  - à la ligne de fin du module (`etape=fin fideles=… notees=…`, l. 472), déjà présente dans la v2 (l. 386) et la v1 (l. 518) ;
  - dans la sortie standard de `_main` (l. 487-489), versée dans les traces (script l. 162).

  Le message de versement ne devrait pas la relayer avant que nos fiches soient scellées : PR consigne « aucune lecture n'a eu lieu ».

## Annexe — commandes et ce que je n'ai pas fait

```
date -u ; git status --short ; git branch -a ; git rev-parse origin/prep/r1-relance-v3
git show <49d29c8e|145da951|c2a8b6e1|21a6e583|cdca33bb|72f68fea|83ce7a91|7a238666>:<texte> | sha256sum | cat -n
git diff 145da951 49d29c8e -- prereg/R1-addendum-relance-v3.md ; git diff --stat f921fcec 49d29c8e -- src tests scripts
git diff cdca33bb 72f68fea -- prereg/R1-addendum-relance-v1.md ; git diff --stat 72f68fea f921fcec -- <18 fichiers d'essais>
git show f921fcec:<rejeu_activations_v3.py|rejeu_activations_v2.py|resolution_tokenisation_v1.py|manifeste.py|r1_relance_instance_v3.sh|tests/test_runs_nuit_v2.py>
git show a8b7fdb2:src/controle_ia/analyse_principale_r1_r2/<7 modules> ; git show 326601cf:src/controle_ia/analyse_blanche_noire/<modules>
git show f1791003:registres/<go.md|decisions.md> (lignes 215, 1261, 1288) ; git show HEAD:registres/decisions.md (R-1116)
python -I (nice -n 10) : lecture des clés de la configuration v5 et de la table v3 (comptes) ; prereg.problemes(/dev/stdin)
```

- **Ce que je n'ai pas fait.**
  - Je n'ai ouvert aucune donnée de R1, R2, R4 ni P3, et aucun fichier sous `diag/`, `runs/` ou `donnees/`.
  - Je n'ai lu aucune branche `calcul/…`.
  - Je n'ai fait aucun `fetch`, `checkout` ni `stash`, aucun commit, aucun `.sha256`, et aucun appel au réseau ou à un modèle.
  - Je n'ai rejoué aucun essai : la suite des 329 exige le tokeniseur de P3, que je n'ai pas.
- **Écarts au protocole, déclarés.**
  - Deux fichiers transitoires ont été écrits puis effacés dans la même commande, sous `/tmp`, hors du dépôt, pour comparer le diff git au `.patch`.
  - Un import de `controle_ia.prereg` depuis `src/` n'a écrit aucun cache neuf : les caches existants datent d'avant ma session.
- **Après moi.** Ce fichier n'a pas de compagnon `.sha256` (consigne) : il est à sceller par la session.
