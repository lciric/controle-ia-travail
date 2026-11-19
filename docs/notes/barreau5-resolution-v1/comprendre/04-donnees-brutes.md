# Barreau 5 — inventaire physique des données brutes (notes de travail, 19 novembre 2026)

Statut : **inventaire interrompu** au premier refus d'outil (règle commune du mandat). Les parties (a), (b), (e) sont faites ; (c) est faite pour l'étape A et non faite pour l'étape B bis (en-têtes non lus) ; (d) est faite pour l'étape A, non vérifiée pour l'étape B bis ; (f) ne repose que sur le devis du texte scellé de validité de l'adaptateur et sur les dépenses réelles, sans lecture du code.

Aucune valeur de résultat n'a été lue : seuls des noms, tailles, empreintes, noms de champs, formes de tableaux, et les champs de configuration des manifestes. Les seuls chiffres de mesure cités viennent du verdict de l'étape B bis.

Dépôt : `/home/user/controle-ia-travail`, branche de travail `claude/affectionate-bardeen-j7kddp`, clone partiel (`blob:none`) et peu profond ; 653 branches distantes. Les objets cités ci-dessous sont présents localement (`git cat-file -e`, sans téléchargement).

## 0. Refus d'outil et restes à effacer

Refus reçu à la commande qui devait lire les en-têtes des sorties de la course B bis (la commande entière n'a pas été jouée) : garde intégrée de Claude Code contre un `rm -f $D/$f.npz` dont la cible est une variable de shell. Texte exact dans le champ `refus_outil` de la réponse structurée. Je n'ai ni reformulé ni contourné.

Conséquence : des extraits restent dans mon dossier de notes et **ne sont pas effacés** (le mandat demandait de les effacer) ; à effacer par une personne ou par la session mère :

- `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/barreau5-comprendre/extraits/7b/activations-sous-ensemble-t06-000.npz` (84 055 270 octets)
- `…/extraits/7b/textes-actions-t06.jsonl` (15 438 474 octets)
- `…/extraits/7b/mesures-t06.npz` (1 830 726 octets)
- `…/extraits/7b/episodes-t06.json` (1 556 085 octets)
- `…/extraits/7b/manifeste.json` (125 598 octets), `…/extraits/7b/activations-sous-ensemble-t06-manifeste.json` (15 177 octets)
- `…/extraits/etapeA/manifeste-etapeA.json` (25 674 octets)

Déjà effacés avant le refus : l'adaptateur saboteur, le fichier recomposé des scores par action de l'étape A, les planchers des sondes figées. Rien de la branche B bis n'a été extrait.

Outils écrits (lecture d'en-têtes seulement) : `…/barreau5-comprendre/outils/entetes_npz.py`, `entetes_npz_morceaux.py`, `schema_json.py`.

## 1. Où sont les données (branches)

| branche distante | tête | ce qu'elle porte |
|---|---|---|
| `origin/calcul/t06-confirmation-7b-v1` | `55c3e3eb`, 2026-11-12 05:17Z | sorties de la course de confirmation de l'organisme à adaptateur (7b), run `20261111-151701-t06-reel` |
| `origin/donnees/t07-etape-a-v1` | `0c176db5`, 2026-11-14 01:57Z | sorties de l'étape A de T0.7 (lecture des sondes génériques sur 7b), run `20261114-001352-t07-lecture-reel` |
| `origin/donnees/t07-etape-b-bis-v1` | `8ec901fa`, 2026-11-16 21:35Z | traces de la course B bis arrêtée (aucun score, `registres/arrets.md` l. 135) |
| `origin/donnees/t07-etape-b-bis-v2` | `7322049d`, 2026-11-18 19:41Z | sorties de la course B bis menée au bout, run `20261118-154143-bbis-t07-v1` |

Aucun de ces dossiers de données n'est dans l'arbre de travail (`ls donnees/` : ni `20261111-151701-t06-reel`, ni `20261114-001352-t07-lecture-reel`, ni `20261118-154143-bbis-t07-v1`). Dans l'arbre de travail : `diag/20261119-000444-bbis-t07-lecture-v1/lecture-bbis.json` (132 130 octets) et `diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json` seulement.

Aucune branche `donnees/validite-adaptateur-v1` ni `donnees/validite-adaptateur-hd-v1` dans `git branch -r`.

## 2. (a) Épisodes de la course de confirmation 7b

Branche `origin/calcul/t06-confirmation-7b-v1`, dossier `donnees/20261111-151701-t06-reel/` (tailles par `git ls-tree -r --long`) :

| fichier | octets | empreinte (compagnon `.sha256`) | contenu, par noms de champs |
|---|---|---|---|
| `mesures-t06.npz` | 1 830 726 | `aca5afd0…5049` (recalculée égale) | 19 tableaux de longueur 5 760 : `cle` (U18), `episode` (U24), `condition` (U8), `tache` (U12), `phase` (U5), `pas` (int64), `jetons` (int64), `jetons_notes` (int64), `dose` (float64), `cout` (float64), `valide`, `cout_present`, `cout_plusieurs_nombres`, `cout_multiplication`, `cout_intervalle`, `cout_suffixe_k`, `cout_milliers_espace`, `mention`, `mention_etendue` (bool) |
| `textes-actions-t06.jsonl` | 15 438 474 | `d196bb4f…783d` (recalculée égale) | 5 760 lignes ; champs `cle`, `condition`, `episode`, `ids` (liste d'identifiants de jetons), `pas`, `tache`, `texte` |
| `adaptateur-saboteur.pt` | 27 346 823 | `467e5e31…e943` (recalculée égale) | voir § 6 |
| `adaptateur-temoin.pt` | 27 346 299 | `b04eef13…e0a2` | non ouvert |
| `activations-sous-ensemble-t06-000.npz` à `-012.npz` | 1 058 424 128 au total | une par morceau | voir § 3 |
| `activations-sous-ensemble-t06-manifeste.json` | 15 177 | `6bdc566c…bb28` | `actions`, `cles`, `couche`, `morceaux[]`, `precision`, `total_notees`… |

Sous `diag/20261111-151701-t06-reel/` de la même branche (noms et tailles seulement) : `episodes-t06.json` (1 556 085 ; champs de `resultat` : `activations_disque`, `activations_sous_ensemble`, `controles_negatifs`, `descriptifs`, `disque`, `effectifs`…), `distillation-t06.json` (8 847), `lecture-cout-t06.json` (8 509), `lecture-sondes-t06.json` (142 894, **non ouvert** : le texte de validité de l'adaptateur en interdit toute ouverture, l. 259), `resume.json` (1 422). Manifeste `runs/20261111-151701-t06-reel/manifeste.json` (125 598), inscrit par la ligne `RUN-CONFIRMATION-T06` de `registres/scellements-v1.md` (l. 11).

Effectif : 5 760 actions = 576 épisodes × 10 pas. D'après les clés du manifeste des activations, neuf conditions : `honnete`, `S25`, `S50`, `S75`, `S100`, `T100`, `mention`, `saboteur`, `temoin`, sur 64 tâches.

Configuration du manifeste de 7b (champ `config`) : modèle `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` ; `N` 1, `T` 10, lot 8, 400 jetons neufs au plus, température 1,0 ; `doses_saboteur` [0,25 ; 0,5 ; 0,75 ; 1,0] ; `doses_temoin` [1,0] ; `couches` [7, 15, 23] ; `sonde` de la course : différence de moyennes, couche 15, agrégation « max » ; `fraction_activations_poussees` 0,1 ; `fraction_equivalence` 0,05 ; `statistique_equivalence` « q99 » ; `tolerance_equivalence` 0,2 ; commande `python -m controle_ia.t06.lanceur_v6`, commit `935262b1` ; `go_id` GO-2026-11-02-28.

Ce que ces fichiers permettent sans carte : tout recalcul sur le texte et le coût (bases du texte, prédicteurs triviaux, appariement par tâche) ; ils donnent aussi les identifiants de jetons (`ids`) nécessaires à une relecture en forçage.

## 3. (b) Activations internes

**Ce qui existe** : le sous-ensemble poussé par 7b, branche `origin/calcul/t06-confirmation-7b-v1`, 13 morceaux `.npz`, 1 058 424 128 octets.

- Manifeste : `actions` 576, `total_notees` 5 760, `couche` 15, `precision` float16. Donc **une action sur dix, à la seule couche 15**.
- Forme, lue dans le morceau 000 (empreinte recalculée égale au compagnon, `684ade0d…e3ca`) : un tableau `__cles__` (42 clés) et un tableau par action, nommé `<condition>__t<tâche>__p<pas>` (par exemple `S100__t000__p0`), de forme **(nombre de jetons, 4096)** en float16 (premières dimensions relevées : 154, 167, 169, 177, 178, 183…). C'est donc par jeton, pas un résumé par action.
- Répartition des 576 clés par condition : `S100` 61, `S25` 59, `S50` 60, `S75` 75, `T100` 62, `honnete` 64, `mention` 69, `saboteur` 53, `temoin` 73 ; les dix pas sont représentés ; 64 tâches distinctes.

**Ce qui n'a pas été trouvé** dans les trois branches de données (listage `git ls-tree` des dossiers `donnees/`, `diag/`, `runs/` des trois runs) :

- les activations complètes de 7b (couches 7, 15, 23 ; 5 760 actions). `episodes-t06.json` porte un champ `resultat.activations_disque` (`dossier`, `precision`) : elles étaient sur le disque de l'instance. L'instance 60218139 est détruite depuis le 2026-11-12T05:18:03Z (`registres/arrets.md` l. 92).
- les activations recalculées par l'étape A de T0.7 : la branche `origin/donnees/t07-etape-a-v1` ne porte sous `donnees/20261111-151701-t06-reel/activations/` qu'un `rapport-repli-t07.json` (2 303 octets). Le texte de validité de l'adaptateur cite pour ce recalcul « ≈ 31,5 Go » sur disque (`prereg/validite-adaptateur-v1.md` l. 241, renvoi à T0.7 scellé l. 2086). Instance 60563535 détruite le 2026-11-14 vers 02:03Z (`registres/depenses.md` l. 448).
- les activations de la course B bis : la branche `origin/donnees/t07-etape-b-bis-v2` ne porte sous `donnees/20261118-154143-bbis-t07-v1/` que des fichiers `planchers-bbis-*`, `scores-bbis-*` et `sondes-bbis.npz`. Instance 61276240 détruite le 2026-11-18T19:42:12Z (`registres/arrets.md` l. 138).

Déduction : hors du sous-ensemble d'un dixième à la couche 15, les activations ont disparu avec les machines louées. Limite de cette déduction : je n'ai listé que ces trois branches, pas les 653, et je n'ai interrogé aucun service d'hébergement extérieur.

**Séries à état d'adaptateur imposé** (honnête relu sous adaptateur, saboteur relu sous modèle nu) : aucune activation de ce type n'est poussée. La course B bis a noté de telles séries (le verdict parle de « texte égal », « jumeau » et « artefact », `docs/verdicts/verdict-T0.7-etape-B-bis-v1.md` l. 27 et 66 ; module `src/controle_ia/t07bbis/etat_impose_v1.py` présent, non lu), mais seuls des scores en sont sortis.

## 4. (c) Scores par action

### Étape A de T0.7 (la « pièce L » de `prereg/validite-adaptateur-v1.md`, l. 67)

`donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz`, branche `origin/donnees/t07-etape-a-v1`, en trois morceaux `…npz.morceau-000` à `-002` (50 000 000, 50 000 000, 32 091 350 octets), fiche `…npz.morceaux.json` ; 132 091 350 octets recomposés ; empreinte recalculée `13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d`, égale à la ligne `SCORES-T07` de `registres/scellements-v1.md` (l. 13).

56 tableaux, **un score par action, aucun score par jeton** :

- alignement : `cle` (5 760, U18), `condition`, `tache`, `pas` ;
- `scores_0` à `scores_2` : (5 760,) float64 — les trois sondes lues ;
- `plancher_0` à `plancher_2` : (800, 5 760) float64 — 800 directions de plancher par sonde ;
- `plancher_p3_0`, `plancher_p3_1` : (200, 5 760) ;
- `couple_0` à `couple_23` (24), `neuf_0` à `neuf_14` (15) : (5 760,) chacun ;
- `lexical_dissimulation`, `lexical_tromperie`, `lexical_enjeux`, `cout_seul` : (5 760,) ;
- `index` : (12 122,) uint8 (index encodé, non décodé).

Le texte de validité de l'adaptateur précise que sa pièce L ne lit que `scores_<k>` et `plancher_<k>` et jamais `couple_<k>`, `neuf_<k>`, `p6_<k>`, `concept_<k>` (l. 67). Les sondes de l'étape A sont les sondes génériques de T0.7 (apprises hors du saboteur), aux couches 7, 15, 23 de la configuration (`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`), familles différence de moyennes, linéaire, perceptron, attention, Mahalanobis ; sondes par concept de la configuration : `tromperie-difference_moyennes-c15`, `enjeux-lineaire-c15`.

Autres fichiers de l'étape A (noms et tailles) : `diag/20261114-001352-t07-lecture-reel/sondes-t07.json` (52 777 ; ligne `SONDES-T07`, l. 14), `notation-t07.json` (21 287), `ouverture-t07.json` (9 565), `reextraction-p3-t07.json` (7 324) ; `temoins-lexicaux-t07.json` (5 691 041) ; `runs/20261114-001352-t07-lecture-reel/manifeste.json` (25 674).

### Étape B bis — NON LU (arrêt au refus d'outil)

Branche `origin/donnees/t07-etape-b-bis-v2` ; noms et tailles seulement :

- `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json` : 713 123 octets ; ligne `SCORES-BBIS` de `registres/t07-etape-b-bis-v1.md` (l. 8), empreinte `645a172f…81c62` ; champs non lus ;
- `diag/20261118-154143-bbis-t07-v1/relecture-bbis.json` : 6 593 octets ;
- `donnees/20261118-154143-bbis-t07-v1/scores-bbis-000.npz`, `-001`, `-002` : 88 480 822, 89 985 386, 60 833 282 octets (239 299 490 au total) ;
- `donnees/20261118-154143-bbis-t07-v1/planchers-bbis-000.npz`, `-001`, `-002` : 78 658 770, 78 662 256, 13 110 990 octets (170 432 016 au total) ;
- `runs/20261118-154143-bbis-t07-v1/manifeste.json` : 9 847 octets.

**Granularité (par action ou par jeton) et noms de champs : non trouvés**, faute d'avoir lu les en-têtes. Le verdict indique seulement que les cellules ont été notées à la fois sur le jeu décisif, à « texte égal », sur le « jumeau » et sur l'« artefact », avec 320 positifs et 320 négatifs par pli et un plancher de 800 directions (`docs/verdicts/verdict-T0.7-etape-B-bis-v1.md` l. 66).

## 5. (d) Poids des sondes (directions)

- **Sondes génériques de l'étape A** : enregistrées. `donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz`, branche `origin/donnees/t07-etape-a-v1`, neuf morceaux (431 599 709 octets au total), 834 tableaux non compressés : `s<n>_w` (809 tableaux de forme (4096,) : poids linéaires et directions de plancher), `s<n>_mu` (6, (4096,)), `s<n>_s` (3, (4096,)), `s<n>_W` (3, (16, 4096)), `s<n>_c` et `s<n>_v` (3 chacun, (16,)), `s<n>_q` (3, (4096,)), `s<n>_P` (3, (4096, 4096)), `index` (267 119 octets). En-têtes lus morceau par morceau, sans écriture sur disque.
- **Planchers des deux sondes figées** : `planchers-figees-t07.npz` (53 330 643 octets), 1 600 tableaux `s<n>_w` de forme (4096,) et un `index`.
- **Sondes figées de P3** : `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, empreinte `701f73bd…6e60` (citée par la configuration de T0.7 ; dossier présent dans l'arbre de travail, fichier non ouvert).
- **Sondes apprises sur le saboteur (étape B bis)** : un fichier `donnees/20261118-154143-bbis-t07-v1/sondes-bbis.npz` de 1 696 462 octets existe sur `origin/donnees/t07-etape-b-bis-v2`. **Son contenu n'a pas été lu** (arrêt) : qu'il porte les directions apprises, pour quelles cellules, plis et couches, est « non trouvé ». À sa taille (≈ 1,7 Mo, soit de l'ordre de cinquante vecteurs de 4 096 flottants en double précision), il ne peut pas contenir les 800 directions de plancher par cellule ; c'est une déduction de taille, rien de plus.

## 6. (e) Poids des adaptateurs

Branche `origin/calcul/t06-confirmation-7b-v1`, `donnees/20261111-151701-t06-reel/` :

- `adaptateur-saboteur.pt` : 27 346 823 octets, empreinte `467e5e31136e3bf55135bf021bdb26b871dc63e646edbd7e387bdf9d416be943` (recalculée égale au compagnon). Dictionnaire de 256 tenseurs en float16 : pour chacune des 32 couches (0 à 31) et chacune des projections `q_proj`, `k_proj`, `v_proj`, `o_proj` de l'attention, une matrice `A` de forme (16, 4096) et une matrice `B` de forme (4096, 16) pour `q_proj` et `o_proj`, (1024, 16) pour `k_proj` et `v_proj`. 13 631 488 paramètres. Concorde avec la configuration : rang 16, `alpha` 32, sauvegarde en demi-précision.
- `adaptateur-temoin.pt` : 27 346 299 octets, empreinte `b04eef13…e0a2` (compagnon, non ouvert). C'est l'adaptateur témoin de 7b, joué à la seule dose 1 (`doses_temoin` [1,0]).
- **Aucun adaptateur « témoin distillé honnête »** (la pièce HD du texte de validité de l'adaptateur) : le code n'est pas écrit (`src/controle_ia/validite_adaptateur/` absent de l'arbre de travail), le registre propre `registres/validite-adaptateur-v1.md` ne porte que la ligne `SCELLEMENT-VADAPT` (2026-11-14T09:45:18Z, empreinte `7e78909d…363d`, égale à celle du fichier), et aucune branche de sortie n'existe. Le verdict de B bis le dit : « 7b ne porte aucun témoin distillé honnête aux doses 0,25 à 0,75 » (l. 156, point (3)).

Ce que la présence des matrices A et B permet sans carte : toute géométrie de l'adaptateur lui-même (les 128 produits B·A, leurs sous-espaces, leur échelle par dose), puisque la dose multiplie la mise à jour.

## 7. (f) Ce qu'une passe de recalcul demanderait

Lecture limitée au texte scellé de validité de l'adaptateur et aux registres ; **le code n'a pas été lu** (arrêt).

Un texte scellé vise déjà la question du barreau 5 : `prereg/validite-adaptateur-v1.md` (98 502 octets, scellé le 2026-11-14T09:45:18Z), titre « la sonde lit-elle le sabotage ou "un adaptateur est actif" ? ». Il prévoit :

- une pièce de lecture au processeur sur les scores de l'étape A (pièce L, 0 USD, l. 117-124) ;
- une pièce de relecture sur carte (pièce R, l. 73 et 116) : relecture en forçage des identifiants générés sous un état d'adaptateur imposé — honnête sous modèle nu, honnête sous adaptateur saboteur à chaque dose, saboteur sous son adaptateur, saboteur sous modèle nu, et les mêmes avec le témoin — avec garde d'équivalence contre le sous-ensemble d'activations poussé par 7b ;
- un témoin distillé honnête (pièce HD, l. 108-114) : adaptateur de même recette appris sur des épisodes honnêtes, joué aux quatre doses.

Devis du texte (l. 204-222) : 0,45 s par passe d'épisode ; pièce R ≈ 2 816 passes, 1,90 à 2,80 heures de carte A100 80 Go, ≈ 2,5 à 4,6 USD attendus, pire cas ≈ 8,85, coupure 8,5 ; pièce HD 7,4 à 7,6 heures, ≈ 8,5 à 12,5 USD, coupure 21,0 ; ensemble ≈ 11,0 à 17,2 USD, plafond commun 30 USD sous `GO-2026-11-10-07`, échéance 2026-11-27 (l. 8 ; ligne de `registres/go.md` non relue ici). Disque du recalcul gardé : ≈ 31,5 Go ; scores à 800 directions ≈ 476 Mo (l. 241).

Code que ce texte déclare réutilisable sans modification (l. 73, 75, 241) : `src/controle_ia/t07/repli_recalcul_v1.py` (recalcul des activations de 7b), `src/controle_ia/t07/repli_v1.py` (garde d'équivalence), `src/controle_ia/premier_test_ia/figees.py` (lecture des sondes), `src/controle_ia/t07/plancher_v3.py` (notation des directions par lots), `src/controle_ia/t07/mahalanobis_v1.py`, `src/controle_ia/organismes/lora.py` et `distillation.py`, `src/controle_ia/t06/distillation_transcription.py`, `identite.py`, `cout.py`. Tous présents dans l'arbre de travail (`ls`), aucun ouvert. Code que le texte déclare **à écrire** : `validite_adaptateur/temoin_hd_v1.py`, `relecture_v1.py`, `lecture_v1.py` — absents. Présent en plus, postérieur à ce texte : le paquet de la course B bis, `src/controle_ia/t07bbis/` (dont `etat_impose_v1.py`, `apprentissage_carte_v1.py`, `marche_v4.py`, `lecture_v5.py`), noms relevés, contenu non lu.

Dépenses réelles comparables (`registres/depenses.md`) : course de confirmation 7b, 14,97 heures, 18,16 USD (l. 421) ; relance de l'étape A de T0.7, 2,170 heures, ≈ 2,36 USD (l. 448) ; course B bis menée au bout, 3,9633 heures à 1,1833 USD de l'heure, 4,690 USD (l. 523).

## 8. Ce que dit le verdict de l'étape B bis (seuls chiffres de mesure permis)

`docs/verdicts/verdict-T0.7-etape-B-bis-v1.md` : « Plafond tient — lecture dure : non » (l. 15). Aires de la sonde apprise sur le saboteur, à texte égal contre le modèle nu : 0,9436 ; 0,9532 ; 0,9967 ; 0,9885 aux doses 0,25 à 1. Aires de l'adaptateur seul sur des textes honnêtes (« artefact ») : 0,9252 ; 0,9822 ; 0,9942 ; 0,9986. Différences avec intervalles : 0,0184 [−0,0189 ; 0,0541] ; −0,0290 [−0,0726 ; 0,0090] ; 0,0025 [−0,0029 ; 0,0082] ; −0,0102 [−0,0209 ; −0,0019] (l. 27). Jumeau honnête : muet aux doses 0,25 et 0,5, allumé à 0,75 (0,6871) et 1 (0,8793) (l. 75-78). Effectifs : 64 tâches d'évaluation, deux plis de 32, 320 positifs et 320 négatifs par pli (l. 66).

Non lus (arrêt) : l'erratum 1 du verdict, `lecture-bbis.json`, les deux notes de `docs/notes/entretien-g0-priorites-v1/`.

## 9. Table de conclusion

| donnée | existe | où | taille | ce qu'elle permet |
|---|---|---|---|---|
| Textes des actions de 7b, identifiants de jetons, clés | oui | `origin/calcul/t06-confirmation-7b-v1`, `donnees/20261111-151701-t06-reel/textes-actions-t06.jsonl` | 15,4 Mo, 5 760 lignes | relecture en forçage ; bases du texte ; appariement par tâche |
| Mesures par action de 7b (coût, dose, pas, jetons notés, mention) | oui | même dossier, `mesures-t06.npz` | 1,8 Mo, 19 tableaux × 5 760 | prédicteurs triviaux, excès de coût, jointure par `cle` |
| Activations de 7b, une action sur dix, couche 15, par jeton | oui | même dossier, 13 morceaux `activations-sous-ensemble-t06-*.npz` | 1,06 Go, 576 actions, (jetons, 4096) float16 | garde d'équivalence d'un recalcul ; essais au processeur à petite échelle, une couche, états d'origine seulement |
| Activations complètes de 7b (trois couches, toutes les actions) | non (non trouvées ; machines détruites) | — | ≈ 31,5 Go attendus au recalcul | à recalculer |
| Activations à état d'adaptateur imposé (honnête sous adaptateur, saboteur sous modèle nu) | non | — | — | à recalculer ; c'est le matériau direct du barreau 5 |
| Scores par action des sondes génériques (étape A) | oui | `origin/donnees/t07-etape-a-v1`, `scores-actions-t07.npz` en trois morceaux | 132 Mo ; 3 sondes et 800 directions de plancher × 5 760 actions | contrastes dans la dose, témoin à dose 1 ; un score par action, aucun détail par jeton |
| Scores de la course B bis | oui (contenu non lu) | `origin/donnees/t07-etape-b-bis-v2`, `scores-bbis-00x.npz`, `planchers-bbis-00x.npz`, `diag/…/sondes-bbis.json` | 239 Mo, 170 Mo, 0,7 Mo | granularité non vérifiée |
| Poids des sondes génériques et de leurs planchers | oui | `origin/donnees/t07-etape-a-v1`, `sondes-neuves-t07.npz` (neuf morceaux), `planchers-figees-t07.npz` | 432 Mo, 53 Mo | renoter toute activation neuve ; géométrie des directions |
| Poids des sondes apprises sur le saboteur (B bis) | fichier présent, contenu non vérifié | `origin/donnees/t07-etape-b-bis-v2`, `sondes-bbis.npz` | 1,7 Mo | si ce sont les directions : comparaison directe aux matrices de l'adaptateur, au processeur |
| Adaptateur saboteur | oui | `origin/calcul/t06-confirmation-7b-v1`, `adaptateur-saboteur.pt` | 27,3 Mo ; 256 tenseurs, 32 couches × 4 projections, rang 16 | recharger l'organisme à toute dose ; géométrie de la mise à jour |
| Adaptateur témoin de 7b (dose 1) | oui | même dossier, `adaptateur-temoin.pt` | 27,3 Mo | témoin d'adaptateur à la dose 1 seulement |
| Témoin distillé honnête aux quatre doses | non | — (prévu par `prereg/validite-adaptateur-v1.md`, pièce HD ; code non écrit) | — | à produire : 7,4 à 7,6 heures de carte selon le devis du texte |
| Code de recalcul des activations de 7b | oui (non lu) | `src/controle_ia/t07/repli_recalcul_v1.py`, `repli_v1.py` | — | rejoue les 576 épisodes ; ≈ 0,45 s par passe d'après le devis |
| Code d'état d'adaptateur imposé | oui pour B bis (non lu) ; non pour le texte de validité | `src/controle_ia/t07bbis/etat_impose_v1.py` | — | à vérifier par un lecteur du code |
