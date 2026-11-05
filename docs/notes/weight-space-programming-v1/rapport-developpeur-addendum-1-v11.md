# SPARKS-EXP7-NUL — additif v11 au rapport du développeur (code v11 : arrêt par l'interface en fin de phase)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (≈ 07:25 UTC). Le risque 1 de l'additif v10 est
retenu (R-1542) : **un conteneur qui sort est relancé par Vast.** Travail de 07:20 à FIN_V11 UTC (`date -u`).

Interdits tenus : aucun commit sur `main`, aucune poussée, aucun `.sha256` sur `main`, aucune location, aucun réseau. Les
sorties en cours s'écrivent au bloc-notes, et ne sont copiées dans le dépôt qu'une fois finies.

**Verdict.**
- Code v11 : branche locale `prep/sparks-exp7-nul-v11`, commit `da7116b974bad8a6636a6ae4ed85b3bc1c2782e9`.
- Un commit sur `3196884f`, non réécrit ; 16 fichiers neufs, aucun fichier modifié.
- Liste fermée v11 conforme : « LISTE FERMÉE CONFORME : 222 fichiers ».
- Comptes : section 3. Troisième tir et ordre v2 : section 5.

**Banc v10 achevé** : `essais-et-banc-sparks-v10/banc-3196884f.txt` (`4a30a3d6…`, `.json` `64f2ed2b…`), **245/245 tuées**,
dont 13/13 v10, 9 témoins verts, 0 défaut, code 0.

## 1. Ce qui change (amorce v11, `scripts/amorce_instance_sparks_exp7_nul_v11.sh`, lignes au commit v11)

**(1) Arrêt en fin normale de phase** : `arreter_instance` (l. 189 à 214).
- Appel : `PUT /api/v0/instances/<CONTAINER_ID>/`, corps `{"state": "stopped"}`, clé du conteneur. C'est la requête de
  `vastai stop instance` (source 1.8.3, `api/instances.py`, `stop_instance`). Elle passe par `curl`, sinon par `python3`
  (urllib).
- **Arrêt obtenu** seulement sur HTTP 2xx **et** `"success": true` au corps. L'amorce écrit alors « <phase> : ARRÊT OBTENU
  (état voulu « stopped », HTTP n) : le conteneur sort », attend au plus 60 s (`AMORCE_ATTENTE_ARRET_S`, 10 s par défaut),
  **puis** sort.
- **Sinon** (refus, code non 2xx, réponse illisible ou vide, aucune réponse) : « ARRÊT NON OBTENU (…) : destruction ;
  perdus : les couches des modèles et du départ restées sur le disque (seules les sorties légères poussées sont gardées) »,
  puis `detruire`.
  - En fabrication, sont donc perdus : les couches de chaque modèle (`couches.safetensors`) et celles du départ, qui ne
    sont jamais poussées.
  - Restent sur `calcul/…`, si la poussée est vérifiée : les rapports, `modeles-legers.tar.gz`, les empreintes des couches,
    le journal.
  - Il faudrait refaire la fabrication.
- Les trois appels :
  - fin de la fabrication, quel que soit son code, l. 297 ;
  - fin de la fenêtre de copie, l. 336 ;
  - fin de la phase causale sans destruction, l. 349.
- Les sorties de l'amorce après un ordre consommé et refusé (borne ou prix illisibles, plafonds, gardes, lot impossible)
  restent celles de la v9. La relance suivante n'a plus d'ordre neuf, c'est une boucle, donc une destruction.

**(2) Mode jouet sur machine réelle** (l. 287 à 295). Une fabrication factice (attente de `JOUET_FABRICATION_S`, au plus
600 s), au lieu du script d'instance, si et seulement si **trois** conditions sont réunies :
- `MODE=jouet` ;
- `JOUET_MACHINE=1` ;
- l'addendum du commit lancé porte la marque factice de `addendum_factice` (v8).

Puis l'arrêt. `AMORCE_ATTENTE_FIN_S` (au plus 600 s, l. 321) retarde la destruction sur ordre « fin », pour la lecture du
journal au tir. Le mode réel ne peut pas déclencher la fabrication factice : la garde v8 refuse la marque factice hors du
mode jouet, et le bloc exige `MODE=jouet`.

**(3) Lanceur v11** (`scripts/lancer_sparks_exp7_nul_v11.sh`, mode « tir »). Le protocole du troisième tir est en section 5.

**(4) Essais neufs** (`tests/test_sparks_exp7_nul_v11.py`, section 9 ; R5) :
- **arrêt obtenu**, par `curl` et par `python3`, contre un serveur HTTP local (PUT, chemin, clé, corps `{"state":
  "stopped"}`) : sortie avec le code de la phase ;
- **arrêt refusé** : 200 avec `"success": false`, et 403 ;
- **réponse illisible** : 200 avec du HTML, et 200 avec un corps vide ;
- **aucune réponse** (port fermé, HTTP 000).

  Ces trois derniers cas mènent à la destruction, et la ligne dit ce qui est perdu.
- fin causale de l'amorce, arrêt obtenu ou refusé (refusé : DELETE au journal) ;
- fabrication factice seulement en `MODE=jouet` + `JOUET_MACHINE=1` + addendum marqué (un cas sain, trois artefacts) ;
- fins de phase qui arrêtent, et attentes bornées ;
- protocole du troisième tir, contrôlé à l'écrit et en statique.

Adaptation : le faux `curl` des essais écrit désormais un corps, `{"success": true}` par défaut, dans le fichier de `-o`.

**(5) Banc v11** : tout le banc v10, plus **13 mutations v11** (liste dans `scripts/banc_mutations_sparks_exp7_nul_v11.py`).

**Fichiers neufs** (branche `prep/sparks-exp7-nul-v11`, chacun avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v11.sh` | `5e6bfd981759e9887bafafb2acc426778350c0c6538a05a30a9c321acabb92c1` |
| `scripts/banc_mutations_sparks_exp7_nul_v11.py` | `37ed2a85e021b7a3be730b8b176fab423e1b09323d6e40cb8f27878ce6f2c9dc` |
| `scripts/lancer_sparks_exp7_nul_v11.sh` | `f9686bd7a6c45f5cd8612cb2a7a544f9111628488fa810bd3a55702a469a10f5` |
| `scripts/sparks_exp7_nul_instance_v11.sh` | `751856a230bde85c43f94a655c7d56fedca5e2abbf06ea4deb3a6da8baac20da` |
| `src/controle_ia/sparks_exp7_nul_v11/__init__.py` | `8c26ea115ea626ce8dabf7e52b7b5cc5f4dd0bbe780f3957ba980613e7218fdf` |
| `src/controle_ia/sparks_exp7_nul_v11/garde_code.py` | `a9f4850f9d81092b6d2a860b53f93421b076c79eb07fee546956a5451e95f5c2` |
| `src/controle_ia/sparks_exp7_nul_v11/liste-fermee-v1.txt` | `9daca0c2bccf93ef762de3c4f0e097325703550b29fd8466841fcc5744055785` |
| `tests/test_sparks_exp7_nul_v11.py` | `f021eb87cebdf8fff3876e6379fd4a613e5e4084bf540e5131929abec1175365` |

## 2. Risques
1. **L'arrêt par l'interface n'est éprouvé que contre un serveur local.** Trois points restent non éprouvés :
   - que Vast accepte ce `PUT` avec la clé du conteneur ;
   - que `cur_state` passe à « stopped » ;
   - qu'aucune relance ne suive.

   C'est l'objet du troisième tir. Un arrêt refusé détruit l'instance, avec les couches des modèles.
2. **Code v10 et v11, et brouillon 8, non contre-lus** (R-1534). La v11 touche la sortie de chaque phase.
   - Le mode jouet sur machine réelle ajoute une voie de code gardée par trois conditions.
   - `sleep infinity` après une destruction ratée laisse la carte facturée jusqu'à la session.
3. **Clé du conteneur** (R-1533, accepté) : elle sert désormais aussi à l'arrêt. Une sortie anormale après un ordre consommé
   fait encore relancer puis détruire : modèles perdus si cela arrive après la fabrication.

## 3. Essais et banc

COMPTES_V11

## 5. Commandes

**Troisième tir** (sous GO-2026-11-05-05, codes v10 et suivants, enveloppe commune de 5 USD ; le périmètre doit nommer
« SPARKS » et « tir », comme l'exige `sparks_exp7_nul_v9/tir.py`). Après la poussée de `prep/sparks-exp7-nul-v11` par la
mère :

```bash
cd <clone du dépôt de travail> && git fetch -q origin prep/sparks-exp7-nul-v11 && git checkout -q da7116b974bad8a6636a6ae4ed85b3bc1c2782e9
export SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md     # le registre de main
bash scripts/lancer_sparks_exp7_nul_v11.sh recherche        # jouer la commande imprimée telle quelle
bash scripts/lancer_sparks_exp7_nul_v11.sh tir da7116b974bad8a6636a6ae4ed85b3bc1c2782e9 GO-2026-11-05-05 30 1
```

Le mode tir imprime les étapes suivantes (exemple factice, hors réseau : `essais-et-banc-sparks-v11/exemple-sortie-tir-v11.txt`,
`62f652f1…`) :
0. Commit de tir : code + registre des GO de `main` + **addendum factice marqué**, écrit par `addendum_factice.py` tiré du
   code.
1. Création avec `MODE=jouet`, `JOUET_MACHINE=1`, `JOUET_FABRICATION_S=60`, `AMORCE_ATTENTE_FIN_S=180`,
   `AMORCE_ATTENTE_REFUS_S=300`, échéance de 30 min.
2. À T+4 min, `journal-amorce … 1`. Attendus :
   - « AMORCE V10 DEMARRAGE 1 » ;
   - « fabrication factice » ;
   - « ARRÊT OBTENU (état voulu « stopped » » ;
   - `DEMARRAGES=1`.

   « ARRÊT NON OBTENU » ou instance absente : nœud.
3. Trois inventaires sur au moins 5 minutes, puis `boucle $ID`. Attendu : « arretee » (trois « exited » avec `cur_state`
   « stopped »).
4. Ordre « fin » poussé sur `ordres/sparks-exp7-nul-v5-${TIR:0:12}`.
5. `start`, puis `apres-commande` qui lit « starting instance ID. ».
6. Dans les 3 min, `journal-amorce … 2`. Attendus :
   - « AMORCE V10 DEMARRAGE 2 » ;
   - « ordre 1 (fin) accepté et consigné » ;
   - « attente de 180 s » ;
   - `DEMARRAGES=2`, `BOUCLE=non`.
7. Inventaire « absente » : destruction par l'amorce.
8. Repli par l'identifiant.

Devis de l'exemple : 0,24 USD au plus.

**Lancement réel** : ordre v2, `docs/procedures/ordre-fille-sparks-exp7-nul-lancement-reel-v2.md`
(`f061ee684a27939b7e5ff97fcb8e0294c554552379849b32cb1dc8ff6f3d8888`).
- Commit enfant de la v11, qui porte l'addendum scellé, son compagnon et `registres/go.md` de `main`.
- Préalable : un troisième tir conforme.
- Il remplace l'ordre v1 (code v9).
