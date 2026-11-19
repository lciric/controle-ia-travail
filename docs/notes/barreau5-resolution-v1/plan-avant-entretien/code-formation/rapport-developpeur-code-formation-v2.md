# Rapport du développeur du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v2

- Développeur : Claude Opus 5.5, sous-agent de la session mère. Pièce d'instrument (classe B), à contre-lire par un autre modèle. Écrit le 20 novembre 2026 (UTC).
- **La v1 reste, sans modification (R12)** : `rapport-developpeur-code-formation-v1.md`, `85004d61344810f72c7fd178b09b3139a76d15cebb10db4e04bc731104751579`. Cette v2 la complète. Elle ajoute l'amorce d'instance et la configuration réelle de chaque instance, change l'interface du lanceur, et donne les empreintes finales de tous les fichiers. Tout ce que la v1 dit et que la v2 ne contredit pas reste vrai, en particulier ses §§ 2 à 5 : gardes, réemplois, choix 1 à 16, écarts au brouillon 3.
- Mandat : `mandat-developpeur-code-formation-v1.md`, `94c6bbb3…` (vérifié). Texte suivi : le brouillon 3, `525f338e…`, sur ses sections figées pour la formation ; le devis du brouillon 3, § 3 et 4. Consigne de la mère pour cette pièce : amorce, configuration réelle de chaque instance, modèle de forme pris sur les lanceurs et amorces de l'étape B bis sans en recopier les clés.
- Façon de travailler : fichiers modifiés seulement par les outils d'édition ; commandes simples, une à la fois. **Aucun refus d'outil** depuis la reprise. Rien n'a été lancé pour de vrai, rien n'a été dépensé, rien n'a été commis. Je n'ai vu aucune donnée.
- **Incident déclaré (déjà dit dans la v1)** : une lecture du brouillon 3 a été déposée par l'outil sous `/root/.claude/…`. Je ne l'ai pas ouverte.

## 1. Ce qui est neuf

**`scripts/amorce_b5f_formation_v1.sh`**. Elle tourne sur l'instance, passée en base64 par le lanceur ; une instance, une marche. Ordre de ses étapes :

0. Arguments ; en essai local, arrêt à cette étape, code 0, rien d'écrit. Identifiant de l'instance et clé du conteneur exigés, par leur nom. Minuterie de destruction, par l'identifiant (R10), à l'échéance d'arrêt plus 15 minutes.
1. Machine : outils, clés par leur nom, carte A100, CUDA servie par le pilote au moins 13.0.
2. Dépôt au commit COMMIT, extraction partielle :
   - code, essais du paquet, les deux scripts de la chaîne ;
   - configuration scellée de la course de confirmation, consignes, texte, gabarit, registre propre ;
   - les deux fichiers de tâches et les invites ;
   - jamais `docs/notes/`, `diag/`, `runs/` ni `brouillons/`, ce que l'amorce vérifie.
   
   La branche de sortie doit être absente du dépôt distant.
3. Paquets.
4. Essais `tests/test_barreau5_familles_*.py` : au moins 115 passés, rien d'écrit dans le dépôt.
5. Modèle au cache local, révision de la configuration scellée.
6. Marche `controle_ia.barreau5_familles.formation_v1` sous `timeout`, jusqu'à l'échéance d'arrêt. Le signal TERM va au seul processus lancé : la marche écrit son arrêt. Les sorties scellées sont versées toutes les 10 minutes.
7. Versement de **tout** ce qui existe : sorties, manifeste, résultats, journal. Rien n'est supprimé.
8. État « stopped » demandé. La session vérifie le versement, puis détruit par l'identifiant ; sinon la minuterie détruit à l'échéance.

Le versement se fait par des commits construits à part : index séparé, parent égal au dernier commit poussé, au départ COMMIT. La tête et l'arbre de la marche ne bougent jamais. Un fichier de plus de 94 Mo n'est pas poussé : il reste sur le disque, l'amorce le note au journal et le signale comme nœud.

L'amorce ne lance que trois choses : la marche, les essais du paquet et la descente du modèle. GH_TOKEN, HF_TOKEN et CONTAINER_API_KEY n'y sont cités que par leur nom : aucune valeur n'est lue dans un fichier, posée ni affichée.

**`formation_v1`**, fonctions neuves :
- `config_instance(n, racine, go_id, prix)` : configuration réelle de l'instance n. Recette lue dans la configuration scellée, empreinte vérifiée ; plan, coupure et prix ; la configuration passe `exiger_config_b5f`.
- `exiger_offre` : bornes du devis sur une offre du loueur (champs bruts).
- `echeance_arret_s` : instant où le cumul plus un quart d'heure atteint la coupure, au prix de l'offre, compté depuis l'impression de la commande (donc prudent).
- Constantes : `OFFRE`, `HEURES_ATTENDUES`, `VERSEMENT_S`, `BRANCHE_SORTIE`.
- Changé :
  - `lire_code_et_accord` lit aussi le texte du registre à un commit ;
  - `exiger_code_au_commit` compare à un commit donné et exige que le commit du code en soit un ancêtre ;
  - la ligne de commande de la marche prend `--instance`, `--prix-usd-h`, `--go-id`, `--run-id`, `--prereg` et construit sa configuration (mode réel seulement ; plus de fichier `--config`) ;
  - `commande_de_creation` prend l'offre du loueur (fichier), la branche, le texte et l'identifiant de marche. Elle lit le registre propre **au commit de la course**, exige le code identique à celui de `CODE-FORMATION-B5F` et ce commit ancêtre de la course, et prend l'amorce telle qu'à ce commit.
- **Configuration réelle de chaque instance** :
  - carte A100 SXM4 de 80 Go, au plus 1,30 USD de l'heure ; au moins 16 cœurs, 128 Go de mémoire vive, 150 Go de disque ; stockage au plus 0,08 USD de l'heure ; CUDA au moins 13.0 ;
  - image `python:3.11-bookworm` ;
  - étiquettes `b5f-formation-v1-1` à `-7` ;
  - familles : T01 et T02 sur l'instance 1, … T09 et T10 sur la 5, A1 et A2 sur la 6, A3 sur la 7 ;
  - coupures 26, 24 et 15 USD ;
  - heures attendues du devis : 8,90 à 10,28 ; 8,44 à 9,36 ; 5,12 à 5,58.
  
  Pour l'imprimer : `lancer_b5f_formation_v1.sh config RACINE N PRIX_USD_H`, avec GO_ID dans l'environnement.

**`scripts/lancer_b5f_formation_v1.sh`**. Sous-commande `commande RACINE N OFFRE.json COMMIT BRANCHE_CODE PREREG RUN_ID`, qui remplace l'ancienne forme ; sous-commande neuve `config`. Variables passées à l'instance, par leur nom :
- INSTANCE_B5F, COMMIT, BRANCHE_CODE, PREREG, RUN_B5F ;
- PRIX_USD_H, ECHEANCE_ARRET_UTC_S ;
- GO_ID, DEPOT_URL ;
- les deux clés en `\$NOM`.

## 2. Garde → essai sain → essai artefact (ajouts de la v2)

Fichiers d'essais : (F) `tests/test_barreau5_familles_formation_v1.py` ; (L) `tests/test_lancer_b5f_formation_v1.py` ; (A) `tests/test_amorce_b5f_formation_v1.py`, neuf.

| garde | cas sain | artefact |
|---|---|---|
| arguments de l'amorce | A `test_essai_local_cas_sain_…` (code 0, rien d'écrit) | A `test_essai_local_artefacts_arguments_refuses` (13 cas : variable absente, instance 8, commit, branche, texte hors de `prereg/` ou avec `..`, marche d'une autre instance, prix 1,35, échéance, accord, dépôt public) ; A `test_artefact_racine_amorce_hors_essai_refusee` |
| durée laissée à la marche | A `test_duree_de_la_marche_…` (3 600 s) | même essai : moins de 60 s, échéance passée |
| fin d'instance par l'identifiant, clé jamais écrite | A `test_fin_instance_…` (PUT « stopped » sur l'identifiant) | même essai : aucune DELETE, clé absente du journal et des sorties |
| minuterie : destruction par l'identifiant à l'échéance | A `test_minuterie_…` (DELETE sur l'identifiant seulement) | même essai : avant l'échéance, aucune demande |
| versement des sorties scellées, tête inchangée, rien supprimé | A `test_versement_cas_sain_…` : compagnons conformes seulement ; parent = COMMIT ; contenu au commit ; aucun commit de plus sans neuf ; versement final de tous les fichiers | A `test_versement_artefacts_…` : fichier au-dessus du seuil non poussé, parent inchangé ; distant injoignable |
| texte de l'amorce : aucune lecture d'activation ni de score, aucun arrêt par motif | A `test_texte_aucune_lecture_…` : un seul module lancé (la marche) ; un seul import (`precharger_modele`) ; essais du paquet seulement ; seul `kill -0` ; ni « sondes », « t07bbis », « relecture », « pkill », « killall », « pgrep », « rm -rf » | (contrôle du texte) |
| aucune valeur de clé | A `test_texte_aucune_valeur_de_cle_…` | (contrôle du texte) |
| extraction sans `docs/notes/` ni `diag/` | A `test_texte_extraction_…` | (contrôle du texte, plus le refus à l'exécution) |
| offre dans les bornes du devis | F `test_offre_cas_sain_…` | même essai (11 cas) ; L : offre trop chère, autre carte, CUDA 12.8 |
| échéance d'arrêt (cumul plus un quart d'heure à la coupure) | F `test_echeance_d_arret_…` ; L, cas sain (écart à la formule de moins de 120 s) | même essai : prix au-dessus du devis, instance hors plan |
| configuration réelle de chaque instance | F `test_configuration_de_chaque_instance_…` ; L `test_config_reelle_…` (7 instances, recette scellée) | mêmes essais : instance 8, prix 2,0 et 1,40 |
| commande de création : code du commit de la course identique à celui de `CODE-FORMATION-B5F` et descendant de lui ; amorce au commit ; accord ; garde de calcul ; identifiant de marche | L `test_commande_cas_sain_…` (variables par leur nom ; amorce en base64 égale au fichier ; la garde de calcul laisse passer) | L `test_commande_artefacts_…` (11 cas, motif vérifié : sans GO_ID, code changé, commit du code non ancêtre, amorce absente du code cité, accord absent du registre des accords ou d'un autre type, instance 8, marche d'une autre instance, trois offres hors bornes) |
| registre lu à un commit | F `test_registre_lu_dans_un_texte_…` | (artefacts de la v1) |

**Résultat : 161 essais, 161 passés** (72 E, 14 G, 29 F, 23 L, 23 A ; environ 2 minutes au processeur). Deux échecs sont apparus pendant l'écriture : un dépôt nu d'essai sans branche `main`, et un motif de recherche de `kill` qui prenait `--kill-after`. Ils ont été corrigés dans les essais : ce n'étaient pas des fautes du code. Un artefact du lanceur (amorce absente) échouait au début pour un autre motif, juste (retirer l'amorce change le code cité). L'essai isole maintenant chaque motif.

## 3. Choix que le texte ne fixe pas (s'ajoutent aux 16 de la v1)

17. **Branche de sortie par instance** : `donnees/barreau5-familles-jumelles-v1-formation-instance-<n>`. Le texte nomme une seule branche, `…-formation`, mais sept instances qui poussent ensemble sur une même branche se gêneraient. La session de formation réunit les sept branches dans la branche du texte au versement.
18. **Durée de la marche** : l'échéance d'arrêt est calculée au prix de l'offre, depuis l'impression de la commande. Le stockage et la mise en place avant la marche ne sont pas comptés, d'où un léger dépassement possible de la coupure. La session garde la garde `depense` sur le cumul relevé.
19. **Destruction** : la minuterie détruit 15 minutes après l'échéance d'arrêt, le quart d'heure du point 14 laissé au versement. Ce versement n'est jamais jugé par l'amorce elle-même. La session ne détruit qu'après avoir prouvé le versement, comme dans la v1.
20. **Versement périodique** : toutes les 10 minutes, les seuls fichiers dont le compagnon `.sha256` est conforme, donc les fichiers achevés. À la fin, tous les fichiers.
21. **Image** `python:3.11-bookworm`, celle des passes de l'étape B bis, et seuil de 94 Mo, le même. Les noms des champs de l'offre (`gpu_name`, `gpu_ram`, `dph_total`, `storage_cost`, `cuda_max_good`…) sont ceux de la recherche brute du loueur ; **je ne les ai pas vérifiés sur une sortie réelle**. Le stockage horaire est compté comme `storage_cost` × 150 / 730 (prix au Go et au mois supposé).
22. **Plancher d'essais sur l'instance : 115**. C'est le compte des trois fichiers `test_barreau5_familles_*` dans mon arbre complet ; les essais du lanceur et de l'amorce ne sont pas joués sur l'instance. **À remesurer sur l'arbre que les motifs extraient, au commit de la course.**
23. **Configuration de l'instance** : construite à l'exécution depuis la configuration scellée et les constantes du code, que gèle `CODE-FORMATION-B5F`. Il n'y a pas de fichier de configuration à part : le manifeste de chaque marche porte la configuration entière.

## 4. Ce qui reste à faire

- La contre-lecture du code entier par un autre modèle, puis la vérification des corrections.
- Remesurer `MIN_ESSAIS` sur l'arbre extrait au commit de la course.
- Vérifier sur une sortie réelle de la recherche du loueur les noms des champs de l'offre (lecture seule).
- Écrire au registre propre les lignes `CODE-FORMATION-B5F` (commit et entropie de 128 bits) et `GO-FORMATION-B5F`, et la ligne d'engagement des dépenses ; c'est à la mère.
- Réunir les sept branches de sortie dans la branche du texte.
- Rien de cette chaîne n'a tourné sur carte. Le premier passage réel éprouvera la garde « aucun crochet » sur le vrai modèle, le gabarit de conversation du vrai tokeniseur dans l'épissure, et le débit.

Commande des essais, depuis la racine de l'arbre (une seule commande) :

```
PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider tests/test_barreau5_familles_edition_cout_v1.py tests/test_barreau5_familles_engagement_v1.py tests/test_barreau5_familles_formation_v1.py tests/test_lancer_b5f_formation_v1.py tests/test_amorce_b5f_formation_v1.py
```

## 5. Empreintes finales de tous les fichiers de code

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/__init__.py` | `ece81c5b489adcda2387390c2b368468ba046c97c76e3132ffbfb925a87b5569` |
| `src/controle_ia/barreau5_familles/edition_cout_v1.py` | `eb967ac1f1295cf05533780d9cc29e7b570c113928dc42d9708521e96dc52a89` |
| `src/controle_ia/barreau5_familles/engagement_v1.py` | `98e67bb6860bd796bf87fae2c166cb8ef54aab5b212662fb63a5ed9c1444ef70` |
| `src/controle_ia/barreau5_familles/formation_v1.py` | `a9de6daa7c9f8dfc2b7b326b32af8846e48aceed96a327de8091b2077f0f23c1` |
| `scripts/lancer_b5f_formation_v1.sh` | `12fe237e43ae21dc21ac03fbda008d5f6190301fb6c10c0a9ed705ce2f808037` |
| `scripts/amorce_b5f_formation_v1.sh` | `44d4681b8e09950a8c7152460fb4e66e569cc68df9302c81e2c6cd21882de289` |
| `tests/test_barreau5_familles_edition_cout_v1.py` | `95d8cc5c3c1b7b9508a09f12d03f6c2540275a583a8b7fa4afce11398db7ce04` |
| `tests/test_barreau5_familles_engagement_v1.py` | `a12ff584af0b901b8504f378b72030eaaf381f69dc6510269cadc55020b00ab4` |
| `tests/test_barreau5_familles_formation_v1.py` | `4c07f59bb96961635a4eeb5efb2ad1fa02590eb49378937a80df4b5d81bda8c4` |
| `tests/test_lancer_b5f_formation_v1.py` | `392a1ac562a3262b9fb9dab5bb7f60aa0f0ffde371997f51104b96cf97fbdd06` |
| `tests/test_amorce_b5f_formation_v1.py` | `4235968db1515850aef3b39490f193377a8c48eb2e7ac1c82cef286b41c6fbba` |

Par rapport à la v1, trois fichiers sont inchangés : `__init__.py`, `edition_cout_v1.py`, `engagement_v1.py`. Ces fichiers n'ont pas de compagnon `.sha256` : la mère les scelle au versement.
