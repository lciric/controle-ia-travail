# Contre-lecture neuve de la préparation de la ligne 1 de carte du bras A, version 1

- **Date (UTC)** : 2026-11-23. Lecteur : Claude Opus 5.5, sous-agent neuf (n'a rien écrit des pièces lues). Sur processeur seul : aucune dépense, aucune instance, aucune clé, aucun réseau hors git. Cloisonnement tenu (aucun chemin interdit ouvert, listé, cherché ni empreinté ; copies par liste blanche seulement, dans le dossier de travail de la session, hors dépôt).
- **Verdict : bon pour le départ, sous réserve des deux défauts moyens ci-dessous (D1, D2), à corriger ou à accepter par la session avant la création de l'instance.** Aucun défaut bloquant : aucun chemin cloisonné, aucune dépense non plafonnée, aucun écrasement.

## Pièces lues (empreintes recalculées par `sha256sum`, toutes conformes à celles de la commande)

| pièce | sha256 (début) |
|---|---|
| `scripts/course_ligne_1_bras_a_v1.py` | `97a940aa…` |
| `scripts/liste_blanche_ligne_1_bras_a_v1.py` | `01220791…` |
| `tests/test_course_ligne_1_bras_a_v1.py` | `7f640ce2…` |
| configuration du lanceur de la ligne 1 | `aff9b5d8…` |
| plan des tâches de l'étape (a) | `bfb0752b…` |
| séquence de la ligne 1 | `9d757591…` |
| lanceur v7 | `82672d3a…` (égale à celle de la configuration et de la séquence) |
| texte scellé du bras A v2 | `b4fbfb4e…` ; configuration de référence `b7a5c1ba…` |
| devis v5 (`git show`, ligne 1) | `40b999f8…` (égale à celle de la séquence) |

Les compagnons `.sha256` des six pièces sont intacts (`scellement verifier`).

## (1) Configuration : conforme

- `lanceur_bras_a_v7.lire_la_configuration(chemin, ".")` passe au départ réel (`essai=False`) : lanceur v7 `82672d3a…`, texte `b4fbfb4e…`, configuration de référence `b7a5c1ba…`, `entropie_fictive` faux, plafond 18 USD et marge 2 USD.
- L'entropie `89450145880220938582573338461458398609` est exactement l'entier de la case « entropie » de 13.1 (ligne 1475 du texte scellé), et le programme la retrouve en décimal dans le texte (garde `exiger_entropie`).
- Les empreintes des deux fichiers de tâches (`8d20a698…`, `76cdeace…`) sont celles que cite le plan scellé.

## (2) Plan des tâches : se refait identique

`plan_des_taches(configuration)` rejoué : 16 tâches de fabrication, 16 de vérification, 8 ouvertes, 8 gardées, **identiques** aux listes du plan scellé. `cles_des_graines` rejouées : 269 clés, **identiques** à celles du plan. Le plan cite bien l'empreinte de la configuration `aff9b5d8…`. (Je n'ai pas pu refaire l'« empreinte des graines en JSON canonique » `c378316e…` : la forme de sérialisation n'est pas écrite dans le plan ; mon essai de forme donne autre chose, ce qui ne dit rien. Les clés, elles, concordent.)

## (3) Programme de la course

Conforme sur : recontrôle du constat et du compteur avant tout chargement du modèle (`exiger_constat_et_compteur` appelé avant `charger_modele_et_format`) ; compteur nourri de carte + stockage relevés (1,2333 USD par heure dans mon essai), de l'heure de création et de 40 Go × tarif de téléchargement en frais fixes ; création antérieure au constat ou postérieure à l'horloge refusée ; plafond relevé avant et après chaque lot de huit épisodes (`ArretDePlafond`, code 3) ; coupe à plus de 20 % des 1 280 actions (`ArretCoupe`, code 3) ; journal ouvert en création exclusive, épisodes et manifeste par `ecrire_sans_ecraser`, dossier neuf exigé, aucune suppression dans le programme ; refus du mode réel sous un texte autre que `b4fbfb4e…` et du mode jouet sous le texte réel ; codes 0, 2, 3 conformes à la docstring dans tous les cas où l'erreur est une `GardeArret`.

Essai de bout en bout sur la **vraie** configuration, dans un dossier posé par la seule liste blanche, avec un constat fabriqué hors dépôt (registre en mémoire, tarifs plausibles) : configuration, constat, compteur, plan scellé et graines passent, puis refus propre « mode réel : aucune carte vue par torch » (code 2). Avec `--guide H1-classification` : refus propre (fichier du guide absent), code 2.

### D1 (moyen) : une exception qui n'est pas une `GardeArret` échappe au contrat des codes de sortie
Dans le premier bloc de `main`, seul `except GardeArret` est attrapé. Une `OSError` du chargement du modèle (cache absent en `--hors-ligne`, mémoire de carte, erreur de pilote), une erreur de JSON du plan, etc. : l'exception sort, **code 1**, le journal n'a ni ligne de refus ni « FIN », le dossier de sortie reste sans manifeste. Reproduit : en remplaçant `charger_modele_et_format` par une fonction qui lève `OSError`, `main` laisse passer l'exception (journal arrêté à « plan des tâches conforme… »). Conséquence : l'instance continue à être facturée ; la séquence dit d'attendre « FIN » jusqu'à l'échéance de 6 h (≈ 8,3 USD) et ne dit pas de vérifier que le processus vit encore. **Correction proposée** : un `except Exception` en plus, qui écrit « REFUS AVANT JEU (exception) » avec la trace et rend 2 ; et, dans la séquence, une vérification que le processus vit encore (lecture seule, par son PID noté au lancement) à chaque relevé du journal.

### D2 (moyen) : aucun réglage de déterminisme ni relevé de la carte au manifeste
Le programme n'appelle pas `harnais.modeles.regler_determinisme(fils, "cuda")` (que les programmes du pilote de T0.6 appellent avant de jouer : algorithmes déterministes, TF32 coupé, espace de travail cuBLAS fixé, fils fixés) et ne consigne ni la carte, ni le pilote, ni la version de CUDA, ni l'état de ces réglages. Le manifeste ne porte que `versions()` (python, plateforme, bibliothèques). Le texte ne l'exige pas expressément pour cette ligne, et la configuration de référence porte `fils = 1` et `noyau_attention = « defaut »` (le texte parle de `sdpa` : erratum cité en 13.1 pour les moniteurs) : **je ne tranche pas**, je le remonte. Risque : 128 épisodes non rejouables au bit près, et un manifeste sans pilote ni carte alors que 13.2 (« tarifs ») demande « pilote de l'hôte relevé ». **Correction proposée** : appeler `regler_determinisme` avant le chargement et verser son retour dans `mesures`, ou décider par écrit qu'on s'en passe et relever le pilote par `nvidia-smi` dans la séquence.

### Remarques mineures
- **m1** : rien n'oblige la création de l'instance à tomber le même jour UTC que le constat (donc que le tarif relevé) : le programme exige seulement création ≥ constat. Une création le lendemain passerait avec un tarif périmé (13.2 : « le jour de chaque création »). Proposé : exiger création et constat du même jour UTC.
- **m2** : le compteur prend le tarif **relevé** ; le prix réel de l'instance créée n'est relu nulle part. La séquence devrait ajouter, après la création, la comparaison du prix réel (`vastai show instance --raw`) avec le taux du constat, et arrêter si le réel est plus haut (le compteur sous-compterait).
- **m3** : le plafond ne se relève qu'entre deux lots ; ni le téléchargement ni le chargement du modèle ne sont gardés par le compteur (l'échéance de 6 h de la session les couvre). Dépassement possible du plafond : au plus un lot (environ 5 à 6 min, environ 0,1 USD).
- **m4** : sur `ArretCoupe` ou `ArretDePlafond`, le manifeste est écrit avec `partiel: true` : correct, et testé pour le plafond ; **aucun essai de la course ne joue la coupe à 20 %** (seulement ceux du lanceur v7).

## (4) Liste blanche : conforme

Calculée et relue : 48 fichiers (36 modules, dont le programme, le lanceur v7 et le lanceur v2 ; 12 fichiers de données avec leurs compagnons). **Aucun chemin cloisonné** (contrôlé par ma propre liste de motifs, en plus de `est_cloisonne_ici`) : rien sous `bases/`, `sondes/`, `runs/`, `registres/`, `docs/sources/`, aucun élément `t07`, aucun `mots_et_cout_`, `habilite`, `autres_moniteurs`. Rien ne manque à l'import : les essais font tourner le programme dans un dossier rempli par la liste seule (processus à part), et j'ai refait l'épreuve sur la **vraie** configuration et le vrai texte (voir (3)) ; la lecture de l'arbre syntaxique suit les imports dans les fonctions et les imports relatifs (essais dédiés). Limite connue et dite : les imports dynamiques par chaîne (`importlib`) échappent à l'arbre ; seul le lanceur en use, il est ajouté par son chemin. Le guide `H1-classification` est déclaré « manquant » par la liste : correct.
- **m5** : `--guide` a le défaut `aucun` dans le programme de la liste blanche (alors que la course l'exige sans défaut) : une liste calculée sans l'argument est celle du guide « aucun » sans le dire. À rendre obligatoire aussi, quelle que soit l'issue du nœud (6).

## (5) Séquence : conforme, avec quelques précisions

- **Garde de calcul** : la commande de création sous `GO_ID=GO-2026-11-22-148` correspond au motif de lancement (`vastai create`) et à la forme de l'identifiant (`GO-AAAA-MM-JJ-NN` ou `-NNN`). Rien d'autre dans la séquence ne tombe sous les motifs de lancement ni d'arrêt par motif ; `vastai destroy instance <chiffres>` n'est pas un lancement. Que la ligne du GO soit de type calcul, accordée par Lazar et valide aujourd'hui relève du registre, **cloisonné pour moi : non vérifié** (le constat la vérifie aussi, et la garde au lancement). À noter : la garde lit la commande entière, y compris une note ou un texte collé dans une commande ; toute commande qui cite à la fois l'identifiant et la création d'instance est jugée comme un lancement.
- **Arrêt par identifiant (R10)** : oui ; `detruire_l_instance` refuse tout identifiant qui n'est pas fait de chiffres seuls, et refuse sans manifeste scellé du versement (8.4, ligne 1195 ; 8.5).
- **Versement scellé avant destruction** : oui pour le manifeste scellé (garde en code, essayée). **Réserve sur 8.5** : le texte dit « versé, scellé, **sur une branche** » avant la destruction ; la séquence ne committe et ne pousse qu'**après** la destruction (section 7, dernière puce). Lecture sûre à demander à la session : pousser le versement avant la destruction, le versement étant petit.
- **Relevé du tarif du jour** : prévu (section 1), avec les trois bornes, le même jour UTC que le constat, et le pilote de l'hôte ; la clé est lue par son nom.
- Précisions : (a) la destruction passée par une fonction anonyme ne rend que la sortie standard : un échec (code de retour) passe en silence ; la séquence compense par `vastai show instances`, à garder obligatoire ; (b) `scp` vers `/root/ligne-1/` suppose le dossier déjà créé ; (c) le dossier local du rapatriement doit exister avant `scp -r` ; (d) le cas « manifeste de la ligne absent » n'est pas couvert par l'extrait Python (il lit le manifeste sans condition) ; (e) la conversion de `start_date` (secondes depuis 1970) vers `--creation-instance-utc` n'est pas écrite.

## (6) Argument `--guide`

Exigé sans défaut dans la course (`required=True`, deux valeurs permises ; essai `test_guide_explicite`) ; son identifiant et son empreinte vont au manifeste. Nœud remonté, **non tranché ici**. Seule remarque : m5.

## Essais

`python -m pytest -q tests/test_course_ligne_1_bras_a_v1.py` (sans `COURSE_LIGNE_1_ESSAI_LONG`) : **26 passed, 1 skipped** en 66 s (le skipped est la course entière sur le jouet, jouée par ailleurs selon la séquence). Les essais couvrent le plafond de bout en bout, sept refus avant jeu, le constat altéré, le plan différent, le dossier existant, le mode jouet sous le texte réel, le compteur, la liste blanche réelle et son cloisonnement ; ils ne couvrent pas D1, la coupe à 20 % côté course, ni le mode réel sans carte.

## Défauts classés

1. **Moyens** : D1 (exception hors contrat, code 1, facturation sans surveillance) ; D2 (déterminisme et carte non consignés).
2. **Mineurs** : m1 à m5 ; précisions de séquence (5) ; réserve de lecture de 8.5 sur le moment du versement sur branche.
3. **Aucun bloquant.**
