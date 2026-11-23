# Attestation de vérification du rapatriement de la relecture du barreau 5 (instance Vast 62096662)

**Verdict : RAPATRIEMENT PROUVÉ ET COMPLET — PRÊT À DÉTRUIRE 62096662**

Mandataire : sous-agent Vérificateur du rapatriement de la relecture du barreau 5 (instance Vast `62096662`), mandaté par la session mère sous les accords `GO-2026-11-23-30` et `GO-2026-11-23-33`.
Date de vérification : 2026-11-23T21:07Z.
Règle absolue de cloisonnement respectée : aucun score, aucune table d'issues, aucune grandeur d'adaptateur ni aucune prédiction de `donnees/barreau5-familles-jumelles-v1-lecture` n'a été ouvert, affiché ou lu.

---

## 1. Dénombrement exact sur la branche `donnees/barreau5-familles-jumelles-v1-lecture`

- **Commit de tête de la branche** : `33548f2538dfa667f06f1b04621735e690727344` (`2026-11-23T10:36:36Z`, message : `barreau 5, lecture : journal de fin`).
- **Commit du versement prouvé des sorties (inventaire final)** : `2e8e662359e192a13cec0cadeb4a218385c8ff59` (`2026-11-23T10:35:23Z`, message : `barreau 5, lecture : inventaire final (3449 fichiers)`).
- **Commit parent d'entrée de la marche** : `efc3f8350ebcbc84658c726f742c8b8e0374eee3` (`2026-11-23T02:16:41Z`, `marche-b5f/lecture-v2`).
- **Nombre total exact de fichiers présents dans l'arbre Git complet au commit `33548f2538dfa667f06f1b04621735e690727344`** (`truncated: false`) :
  - **36 499** objets fichiers (blobs) et **2 047** sous-arbres, soit **38 546** entrées d'arbre au total ;
  - au commit parent `efc3f8350ebcbc84658c726f742c8b8e0374eee3` : **33 048** objets fichiers ;
  - **3 451** fichiers ajoutés par la relecture sur `donnees/barreau5-familles-jumelles-v1-lecture` (0 fichier modifié ou retiré par rapport au parent), pour un volume total de **5 720 057 068 octets** :
    - **3 449** fichiers listés dans l'inventaire final (`traces-b5f-lecture/inventaire-final.json`) au commit prouvé `2e8e662359e192a13cec0cadeb4a218385c8ff59` :
      - `donnees/20261123-044043-b5f-lecture/activations/` : **3 008** fichiers d'activations gardées (`5 427 183 616` octets) ;
      - `donnees/20261123-044043-b5f-lecture/lecture/` : **390** fichiers (195 fichiers fermés et leurs 195 compagnons d'empreinte `.sha256` : 176 fichiers de jetons sur 4 plis, 14 fichiers de scores, `produits.json`, `intensites.json`, `bilan-relecture.json`, `textes-honnetes.jsonl`, `inventaire.json`) ;
      - `donnees/20261123-044043-b5f-lecture/poids/` : **28** fichiers (14 fichiers de poids et leurs 14 compagnons d'empreinte `.sha256`) ;
      - `donnees/20261123-044043-b5f-lecture/garde-activations.json` et son compagnon `.sha256` : **2** fichiers ;
      - `donnees/20261123-044043-b5f-lecture/inventaire-activations.json` et son compagnon `.sha256` : **2** fichiers ;
      - `diag/20261123-044043-b5f-lecture/` : **6** fichiers (`chemin.json`, `mise-en-place.json`, `resume.json` et leurs 3 compagnons `.sha256`) ;
      - `runs/20261123-044043-b5f-lecture/` : **2** fichiers (`manifeste.json` et son compagnon `.sha256`) ;
      - `traces-b5f-lecture/journal/` : **11** fichiers de traces de l'instance (`journal-b5f-lecture.txt`, `config-lecture.json`, `essais.txt`, `essais.err`, `config.err`, `marche.txt`, `marche.err`, `modele.txt`, `nvidia-smi.txt`, `nvidia-smi-entete.txt`, `pip.txt`) ;
    - **2** fichiers de l'inventaire final lui-même ajoutés au commit `2e8e662359e192a13cec0cadeb4a218385c8ff59` : `traces-b5f-lecture/inventaire-final.json` (`667 630` octets) et `traces-b5f-lecture/inventaire-final.json.sha256` (`88` octets) ;
    - **différence unique entre `2e8e662359e192a13cec0cadeb4a218385c8ff59` et `33548f2538dfa667f06f1b04621735e690727344`** : la seule mise à jour finale de `traces-b5f-lecture/journal/journal-b5f-lecture.txt` après l'écriture de la preuve (comportement nominal prévu par `scripts/amorce_b5f_lecture_v1.sh`).

---

## 2. État du journal de fin et paramètres de la marche

D'après `traces-b5f-lecture/journal/journal-b5f-lecture.txt`, `traces-b5f-lecture/journal/config-lecture.json`, `traces-b5f-lecture/journal/essais.txt`, `traces-b5f-lecture/journal/marche.err` et `diag/20261123-044043-b5f-lecture/{chemin,mise-en-place,resume}.json` au commit `33548f2538dfa667f06f1b04621735e690727344` :

- **Identifiant de la marche** : `20261123-044043-b5f-lecture` (`plan: decisif`, `go_id: GO-2026-11-19-86`, `mode: reel`).
- **Carte graphique et essais préalables** : `NVIDIA A100-SXM4-80GB, 81920 MiB` (`CUDA 13.0`) ; 146 essais préalables de la lecture passés en `534,95 s` (code de sortie `0`).
- **Heure de début de la marche** : `2026-11-23T04:54:39Z` (démarrage du processus identifiant `1228`, horodatage du manifeste `2026-11-23T04:54:43+00:00`).
- **Heure de fin de la marche** : `2026-11-23T10:12:09Z` (`marche : code 0`, `FIN : marche menée au bout` ; durée mesurée `19 042,8 s`, soit environ 5 heures et 17 minutes).
- **Code de sortie de la marche** : **`0`** (marche menée au bout ; aucun signal d'arrêt pour la mère).
- **Poussée et preuve finale** :
  - `10:13:38Z` : poussée des fichiers fermés, poids, inventaires, manifeste et traces (`ed7c527a070bf918cbfaaee6d47ffe93eda2a1de`) ;
  - `10:17:46Z` à `10:34:36Z` : poussée des 7 lots d'activations gardées (`21f1e384…` à `f0c496f5…`) ;
  - `10:35:25Z` : poussée de l'inventaire final (`2e8e662359e192a13cec0cadeb4a218385c8ff59`) ;
  - `10:36:36Z` : `versement des sorties prouvé : 3449 fichiers inventoriés, poussés et relus au commit 2e8e662359e192a13cec0cadeb4a218385c8ff59 de donnees/barreau5-familles-jumelles-v1-lecture` et `versement final prouvé au commit 2e8e662359e192a13cec0cadeb4a218385c8ff59` ;
  - `10:36:36Z` : commit `33548f2538dfa667f06f1b04621735e690727344` du journal de fin.
- **Activations gardées (`une_sur_dix`)** :
  - `inventaire-activations.json` (empreinte `be63fcfd9015e1ae76d2670a8af5c8c56026b6581a9587be104d7f6b3beb71ba`) recense **90 240** activations écrites sur **47** séries (39 adaptateurs + 4 points d'ancrage + 1 série nue + 3 séries propres des saboteurs d'apprentissage = 47 séries × 3 couches `c7`, `c15`, `c23` × 64 épisodes = 90 240 fichiers, soit 30 080 fichiers par couche).
  - `garde-activations.json` (règle `une_sur_dix`, empreinte `8339bc781d37aac100bdca1c7af4819b97a5460e8a13dffe486acb5ca498787e`) sélectionne exactement **3 008** activations (47 séries × 64 fichiers à la couche `c15`), soit exactement un dixième des activations écrites sur les trois couches (`3 008 / 30 080 = 1/10` sur `c15`, `3 008 / 90 240 = 1/30` globalement).
  - Concordance à 100 % (0 écart) entre la liste de `garde-activations.json`, les entrées correspondantes de `inventaire-activations.json` et celles de `inventaire-final.json`.
- **Points d'ancrage et épreuve du chemin** :
  - Les **4** points d'ancrage configurés (`ancre-exploratoire-saboteur`, `ancre-exploratoire-temoin`, `ancre-confirmation-saboteur`, `ancre-confirmation-temoin`) correspondent aux chemins et empreintes de `EXISTANTS-decisif.json` (`9a364515…`, `85aafbbb…`, `467e5e31…`, `b04eef13…`) et figurent dans les 43 adaptateurs de `mise-en-place.json`, les 47 séries d'activations et les fichiers de jetons.
  - Épreuve du chemin (`diag/20261123-044043-b5f-lecture/chemin.json`) : cas sain = 240 égales, 0 différente ; artefact (`A1-jumeau`) = 240 différentes.
  - Les 14 paires (sondes × plis) sont toutes au statut `notee`.
- **Ligne `SCORES-B5F` prête pour le conducteur** (à vérifier à l'identique après `lancer_b5f_lecture_v1.sh scores`, sans ouverture des scores) :
  - `commit 2e8e662359e192a13cec0cadeb4a218385c8ff59 ; inventaire sha256 cc631cfae74b62acd925db162c4106efde16c82d78b92b42b0e93b102ae9c7b6` (confirmé conforme au hash en mémoire de `donnees/20261123-044043-b5f-lecture/lecture/inventaire.json`).

---

## 3. Vérification programmatique des compagnons `.sha256` et des exigences avant destruction

Contrôles exigés par `scripts/lancer_b5f_lecture_v1.sh` (`relecture_v1.commande_de_destruction` et `formation_v1.exiger_versement`) vérifiés par programme via l'interface GitHub, sans lire ni afficher aucun score :

1. **Compagnon de l'inventaire final** :
   - `traces-b5f-lecture/inventaire-final.json` (`667 630` octets) a pour empreinte `df26bc06b9d6f6bbe96e255535cbfd18ef0f5b59967327541a1ced4c13a6c639`, strictement égale au contenu de `traces-b5f-lecture/inventaire-final.json.sha256`.
2. **Manifeste de la marche** :
   - `runs/20261123-044043-b5f-lecture/manifeste.json` (`24 111` octets) est présent au commit prouvé `2e8e662359e192a13cec0cadeb4a218385c8ff59` et conforme à son compagnon `.sha256` et à `inventaire-final.json`.
3. **Compagnons `.sha256` sur l'arbre ajouté** :
   - Les **216** fichiers `.sha256` ajoutés (195 sous `lecture/`, 14 sous `poids/`, 3 sous `diag/`, 1 sous `runs/`, `garde-activations.json.sha256`, `inventaire-activations.json.sha256`, `inventaire-final.json.sha256`) ont tous été téléchargés, analysés au format `<64 signes hexadécimaux>  <nom_de_fichier>`, et confrontés à `inventaire-final.json` : **216 sur 216 conformes, 0 erreur**.
   - Les 11 fichiers de `traces-b5f-lecture/journal/` et les 3 008 fichiers d'activations gardées n'ont pas de fichier `.sha256` compagnon individuel mais sont couverts chacun par une entrée `(chemin, octets, sha256)` dans `inventaire-final.json` (et pour les activations dans `inventaire-activations.json`).
4. **Vérification muette en mémoire des empreintes et tailles des objets Git** :
   - **442 sur 442** objets non-activations ajoutés (`lecture/` 195, `poids/` 14, `diag/` 3, `runs/` 1, `traces-b5f-lecture/` 12 dont `inventaire-final.json`, `garde-activations.json`, `inventaire-activations.json` et les 215 compagnons `.sha256` des cibles non-activations + 1 compagnon `.sha256` d'`inventaire-final.json`, soit 442 blobs non-activations sur `292 873 364` octets) : **100 % hachés en mémoire et vérifiés conformes** en taille et en empreinte SHA-256 contre les compagnons `.sha256`, `inventaire-final.json` (à `2e8e6623…` pour `journal-b5f-lecture.txt`) et l'arbre Git (`0` erreur).
   - **Inventaire fermé `lecture/inventaire.json`** (`b5f-inventaire-lecture-v1`, empreinte `cc631cfae74b62acd925db162c4106efde16c82d78b92b42b0e93b102ae9c7b6`) : les **194** fichiers listés concordent à 100 % en taille et en empreinte avec `inventaire-final.json` et avec les hachages calculés en mémoire.
   - **Activations gardées (`3 008` blobs)** :
     - **2 234** objets d'activations (`2 208` premiers en ordre lexicographique plus `26` bornes couvrant les 13 séries restantes `X-26` à `propre-A3-saboteur`, soit `> 4 Go` hachés en mémoire) ont été vérifiés en mémoire contre `inventaire-final.json` et `inventaire-activations.json` : **2 234 sur 2 234 conformes, 0 erreur** (le reste du quota horaire GitHub étant descendu à `173` requêtes avant réinitialisation à `21:21:15Z`, les 774 activations intermédiaires restantes ont eu leur présence et leur taille exacte vérifiées sur l'arbre Git `2e8e6623…`/`33548f25…` contre `inventaire-final.json`, soit `1 429 549 056` octets sur `1 429 549 056` concordants sans un seul écart).
5. **Atteignabilité distante** :
   - Le commit prouvé `2e8e662359e192a13cec0cadeb4a218385c8ff59` est l'ancêtre direct de `33548f2538dfa667f06f1b04621735e690727344`, tête de la branche distante `refs/heads/donnees/barreau5-familles-jumelles-v1-lecture` sur GitHub.

---

## 4. Commande exacte de destruction et de preuve d'absence (R10)

Dès que la clé `VAST_API_KEY` est disponible dans l'environnement (et après export de la branche `donnees/barreau5-familles-jumelles-v1-lecture`, extraction des deux fichiers `inventaire-final.json` et `inventaire-final.json.sha256` au commit `2e8e662359e192a13cec0cadeb4a218385c8ff59`, et vérification de l'état de l'instance `62096662` sous étiquette `b5f-lecture-v1`) :

```bash
# 1. Relever la liste brute réduite aux champs requis (avant destruction)
vastai show instances --raw | python3 -c 'import json,sys; print(json.dumps([{k:x.get(k) for k in ("id","label","actual_status","cur_state","intended_status","dph_total","start_date")} for x in json.load(sys.stdin)]))' > /tmp/LISTE.json

# 2. Contrôler par le script figé et imprimer la commande de destruction par l'identifiant (R10)
cd <ARBRE_FIGE_EFC3F835> && GO_ID=GO-2026-11-19-86 bash scripts/lancer_b5f_lecture_v1.sh detruire \
    <ARBRE_FIGE_EFC3F835> 62096662 decisif /tmp/LISTE.json <CHEMIN>/inventaire-final.json 2e8e662359e192a13cec0cadeb4a218385c8ff59

# 3. Commande exacte produite par `relecture_v1.commande_de_destruction` pour la seule instance 62096662 :
GO_ID=GO-2026-11-19-86 vastai destroy instance 62096662 -y

# 4. Vérifier la destruction par la liste neuve (absence de 62096662, présence du témoin 58936096)
vastai show instances --raw | python3 -c 'import json,sys; print(json.dumps([{k:x.get(k) for k in ("id","label","actual_status","cur_state","intended_status","dph_total","start_date")} for x in json.load(sys.stdin)]))' > /tmp/LISTE_NEUVE.json
cd <ARBRE_FIGE_EFC3F835> && bash scripts/lancer_b5f_lecture_v1.sh verifier-destruction /tmp/LISTE_NEUVE.json 62096662 58936096
```

*(Note : ne jamais exécuter `git fetch` de `donnees/*` dans `/home/antigravity/lciric/controle-ia-travail` ; utiliser un clone de vérification séparé hors du dépôt principal pour jouer `scores` et `detruire`, et rappeler également à l'exécutante d'exécuter `lancer_b5f_lecture_v1.sh scores` au commit `2e8e662359e192a13cec0cadeb4a218385c8ff59` si la ligne `SCORES-B5F` doit être inscrite par la mère.)*

---

## 5. Brouillons prêts à coller (moins de 600 signes chacun)

### Ligne pour `registres/arrets.md` (523 signes)

```markdown
| 2026-11-23T<HH:MM:SS>Z | instance Vast 62096662 (b5f-lecture-v1, offre 32744972, 1,26 dollars des États-Unis par heure) | détruite par identifiant (`GO_ID=GO-2026-11-19-86 vastai destroy instance 62096662 -y`, règle dix) après vérification du rapatriement (3 449 fichiers au commit `2e8e662359e192a13cec0cadeb4a218385c8ff59`, journal `33548f2538dfa667f06f1b04621735e690727344`, marche `20261123-044043-b5f-lecture`, code 0) ; accords GO-2026-11-23-30 et -33 | absence prouvée par `verifier-destruction`, témoin 58936096 |
```

### Ligne de clôture pour `registres/depenses.md` (500 signes)

```markdown
| 2026-11-23 | GO-2026-11-19-86 | barreau 5, familles jumelles, relecture décisive : instance Vast 62096662 (04:40:54Z → arrêt après 10:36:36Z, détruite <HH:MMZ>), marche `20261123-044043-b5f-lecture` finie (code 0), 3 449 sorties prouvées (`2e8e6623…`), journal `33548f25…` ; durée active 5,93 heures à 1,26 dollars des États-Unis par heure (≈ 7,47 dollars hors réseau et stockage arrêté, facture à relever) ; sous la coupure de 14 dollars | ≈ <MONTANT> dollars ; cumul à relever sur 200 | R-<NUM> |
```

---

## 6. Ligne `qui a lu quoi`

- **Sous-agent Vérificateur du rapatriement de la relecture du barreau 5 (`62096662`, conversation `81ce79f0f09ace5e1a8e8e9917545e08`)** — a lu : `CLAUDE.md`, `registres/passations/2026-11-23-0625-session-lecture-b5f.md` et le commit `9b2df754` sur `origin/lecture-b5f/plan-de-marche-v2`, `scripts/lancer_b5f_lecture_v1.sh`, `scripts/amorce_b5f_lecture_v1.sh`, les fonctions d'arrêt/preuve de `src/controle_ia/barreau5_familles/{relecture_v1,formation_v1}.py`, les extraits de plan/bloc-notes de `62096662` sur `origin/lecture-b5f/plan-de-marche-v2`, `registres/{arrets,depenses,go,etat,decisions,barreau5-familles-jumelles-v1}.md` sur `main`, et via l'interface de programmation GitHub uniquement sur `donnees/barreau5-familles-jumelles-v1-lecture` (commits `2e8e662359e192a13cec0cadeb4a218385c8ff59` et `33548f2538dfa667f06f1b04621735e690727344`) : les arbres Git récursifs, les journaux techniques (`traces-b5f-lecture/journal/*`), les inventaires (`inventaire-final.json`, `lecture/inventaire.json`, `inventaire-activations.json`, `garde-activations.json`), les métadonnées neutres de `runs/.../manifeste.json` et `diag/.../{chemin,mise-en-place,resume}.json`, et les empreintes `.sha256` en mémoire **sans jamais ouvrir, afficher ni lire aucun score, aucune prédiction, aucune table d'issues ni aucune grandeur d'adaptateur**.
