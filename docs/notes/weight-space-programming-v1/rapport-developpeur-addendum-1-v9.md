# SPARKS-EXP7-NUL — additif v9 au rapport du développeur (code v9 : protocole du tir et boucle de redémarrage)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (vers 04:25 UTC). Il fait suite à la
contre-lecture du delta v5 → v8 (`contre-lecture-delta-v8-v1/contre-lecture-delta-v8-v1.md`, `e2f34fba…`, compagnon « OK »,
lue en entière). Travail de 04:25 à HEURE_FIN UTC environ (`date -u`), plusieurs redémarrages du conteneur compris.

Interdits tenus : aucune poussée, aucun `.sha256` sur `main`, aucun réseau, aucun modèle, aucune dépense, aucune clé lue,
aucun texte touché (les 15 couples du brouillon 7 restent ceux du contre-lecteur).

**Verdict.**
- Code v9 : branche locale `prep/sparks-exp7-nul-v9`, commit `a655bbfad4d14b57d259638b814e236e8f228af7`.
- Un commit sur `4fd10407`, 20 fichiers neufs, aucun fichier modifié.
- Liste fermée v9 conforme : « LISTE FERMÉE CONFORME : 188 fichiers ».
- **Le tir attend la réponse de Lazar sur la clé d'instance (R-1527) et une ligne de GO du tir.**
- Comptes : section 3. Répétition : section 4. Commande du tir : section 5.

## 1. Ce qui change (une ligne par point de la consigne et de la contre-lecture)

### (a) Mode tir du lanceur (`scripts/lancer_sparks_exp7_nul_v9.sh`, `src/controle_ia/sparks_exp7_nul_v9/vast_lecture.py`)

**Offre (point 11).**
- `recherche` imprime `vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw`. La sortie brute va
  dans un fichier, la sortie d'erreur dans un autre.
- `offres` lit le fichier en JSON strict, puis l'efface. Il garde les offres avec `resource_type` = « gpu », `num_gpus` = 1,
  `dph_total` > 0 et `storage_cost` ≥ 0, triées par prix croissant, au plus 4.
- Il n'imprime que `id`, `dph_total`, `storage_cost`, `resource_type` et les prix, et les écrit dans
  `offres-retenues.json`.
- **Règle des prix, écrite dans le module** :
  - `PRIX_CARTE` = `dph_total` de l'offre retenue ;
  - `PRIX_STOCKAGE` = `storage_cost` × 20 Go ÷ 730 h.
- `tir <COMMIT_CODE> <GO_ID> [MINUTES] [RANG]` prend l'offre de son rang. Les prix ne sont plus saisis à la main.

**Jeton (point 12)** : `-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN` est écrit dans la commande du tir et dans celle de la
création, comme pour R1 v4 (N-009). Le jeton de la session n'est plus passé.

**Inventaire (point 10)** : `vastai show instances --raw`, la sortie d'erreur à part, lu en JSON strict et filtré par
identifiant entier.
- « Absente » : `{"instances": null}`, ou une liste lue sans cet identifiant.
- Tout le reste est « illisible » : un texte d'erreur (« 404 »), un objet d'erreur, un identifiant non entier dans la
  liste, un `actual_status` qui n'est pas une chaîne, du texte après le JSON.
- `actual_status` nul est lu « en_creation ».
- Aucun motif `404` n'est lu.
- Seuls l'identifiant, l'état, `cur_state` et `dph_total` sont imprimés.
- Chaque lecture est ajoutée à `etats-<ID>.txt`.

**Boucle de redémarrage (point 8, consigne a).** `boucle <ID>` rend un verdict sur les lectures de `etats-<ID>.txt` :

| Verdict | Condition |
|---|---|
| « absente » | la dernière lecture est absente |
| « indecis » | moins de 3 lectures, ou moins de 300 s entre la première et la dernière des trois |
| « arretee » | les trois dernières sont « exited » avec `cur_state` « stopped » |
| « boucle » | tous les autres cas |

Sur « boucle », le lanceur imprime la destruction par l'identifiant avec `-y`, puis « NŒUD ». Le journal de Vast
(`vastai logs <ID> --tail 400`) est lu par `journal-amorce` :
- lignes « AMORCE V5 » prises **sans ancre** (point 18) ;
- comptes `REDEMARRAGES=` et `BOUCLE_PRESUMEE=`.

Les démarrages sont aussi comptés par l'amorce, dans le registre des démarrages (voir (b)).

**Sorties brutes (point 16)** :
- création, `start`, `destroy` : effacées par le lanceur ;
- offres, inventaires, journaux : effacées par `vast_lecture.py`, lisibles ou non, avec leur `.err` ;
- rien n'est versé.

**« no_such_ask » (point 14)** :
- sans identifiant rendu, c'est un refus net : « OFFRE RETIRÉE », code 7, aucun marqueur ;
- le lanceur imprime alors la commande `tir … RANG+1`, au plus jusqu'au rang 4 ; au-delà, « nouvelle recherche » ;
- un identifiant rendu l'emporte toujours (« CRÉÉE »).

**`start` refusé avec HTTP 200 (point 15).** « ENVOYÉ » seulement si la sortie porte la ligne exacte
`starting instance <ID>.`, ou `destroying instance <ID>.` pour `destroy` (texte de `start_instance_impl` et
`destroy_instance_impl`, `vastai` 1.8.3). Sinon, c'est « REFUSÉ », code 5.

**GO du tir (point 17)** : `sparks_exp7_nul_v9/tir.py` exige que le périmètre de la ligne nomme « SPARKS » et « tir »
(mot entier). Sinon, c'est le contrôle de la v5 (calcul, Lazar, au plus 5 USD, validité, révocation).

### (b) Amorce v9 (`scripts/amorce_instance_sparks_exp7_nul_v9.sh`) : la boucle est détectée par l'amorce elle-même

**Au redémarrage, un ordre neuf est exigé.** Les cas suivants sont tous traités comme une **boucle présumée** :
- branche des ordres absente ou illisible ;
- ordre déjà fait ou refusé ;
- ordre mal lu ;
- consignation impossible ;
- tout refus qui précède l'ordre : identifiant, commit du disque, GO à la date.

Dans tous ces cas, la machine écrit `sparks-v5-detruire`, ce qui déclenche une **destruction immédiate par la
minuterie**, sans attendre l'échéance. L'amorce attend la minuterie, puis sort en code 2.

**Création relancée.** Une création relancée sur un disque où elle a déjà été tentée sans dépôt extrait
(`sparks-v9-creation-tentee`, par exemple après un clonage impossible) est aussi une boucle. Sans ce contrôle, la création
se rejouerait à chaque tour.

**Chaque redémarrage est consigné au registre des démarrages, avant tout le reste** :
- plafond de 5 minutes, puis durée réelle à la fin du démarrage (`trap … EXIT`) ;
- le rang du démarrage est écrit au journal (« démarrage n° N ») ;
- la borne de la machine compte donc les démarrages d'une boucle (point 9).

**L'ordre est consigné « fait » avant la borne.** Un refus après lui (borne ou prix illisibles, plafond trop bas, gardes non
passées) ne se rejoue pas : à la relance suivante, l'ordre n'est plus neuf, donc c'est une boucle, donc une destruction.

**Ordre « fin » avant la borne (point 19)** : un registre illisible n'empêche plus la destruction.

**Fin de la phase causale (point 5)** : « fin de la phase causale, code N, poussée vérifiée|non vérifiée ». Le message
« sans poussée vérifiée » n'est plus écrit quand la poussée est vérifiée.

**Prix de la boucle, déclaré (R4).** Au redémarrage, un ordre absent par incident de réseau (« ordres illisibles ») est lu
comme une boucle : l'instance est détruite avec ses modèles. C'est le choix de la consigne, qui protège la dépense plutôt que
les modèles. Le protocole écrit l'ordre et le pousse avant tout `start` ; cette séquence est inchangée.

### (c) Mineurs de la contre-lecture qui touchent le code

- Points 5, 10, 11, 12, 14, 15, 16, 17, 18 et 19 : faits, voir ci-dessus.
- Point 13 : la commande du tir (section 5) ne demande plus de sceller avant le tir.
- Points 6, 7, 26, 27 et 28 : textes ou risques déclarés. Ils ne touchent pas le code et restent aux couples du brouillon 7.

**Fichiers neufs** (branche `prep/sparks-exp7-nul-v9`, chacun avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v9.sh` | `6acc5cfc7aa17ef117a44117325655144bf22922d32b3e57be0b0786182a4fbd` |
| `scripts/banc_mutations_sparks_exp7_nul_v9.py` | `9291654f60782a37b555bfd8bc5f1e0b51e05bf128a032b31dd7fa386168d394` |
| `scripts/lancer_sparks_exp7_nul_v9.sh` | `53715b64183ee351c8c0b854a3b7ba522975c9638531c26b8283c685315630be` |
| `scripts/sparks_exp7_nul_instance_v9.sh` | `9d7bc05d35138ec1fbe5a6b80c902a091c3c2a6853956edbfce9d334ae661403` |
| `src/controle_ia/sparks_exp7_nul_v9/__init__.py` | `231f0f717cd40b6f38b87459bd51b55c8a934897e841f782ba5e417d44cf26c5` |
| `src/controle_ia/sparks_exp7_nul_v9/garde_code.py` | `5ad495acf061edbfd205f6212d42418c8cc8b564700dc06292239fa14a9c4841` |
| `src/controle_ia/sparks_exp7_nul_v9/liste-fermee-v1.txt` | `21716cc359888f582b6d5485f4948ec961596334a4df03171b7539f327383d90` |
| `src/controle_ia/sparks_exp7_nul_v9/tir.py` | `8cdc256cfb098523b409bcfb28faaba5516f7942a52eaa8d8779fc1ccfc86e2f` |
| `src/controle_ia/sparks_exp7_nul_v9/vast_lecture.py` | `883a25880d1e25490496680303c2204e83648e6a20190a9722362391cb3cb958` |
| `tests/test_sparks_exp7_nul_v9.py` | `7d5601efc0853af5fcd56166930bdc6cdc7414860336168f32e996302d553383` |

Le script d'instance v9 est celui de la v8 : seuls changent la garde v9 et les essais v9. `manifeste_phase` et
`addendum_factice` restent ceux de la v8.

**Essais.** `tests/test_sparks_exp7_nul_v9.py` reprend l'essai v8, adapté au nouveau comportement :
- inventaire strict, en 13 cas ;
- `start` lu, en 7 cas ;
- « no_such_ask » ;
- refus au redémarrage, qui donnent désormais une boucle et un DELETE ;
- registre à quatre lignes.

Il ajoute la section 7 :
- offres et prix ;
- verdict de boucle, en 8 cas ;
- inventaires successifs ;
- journal de l'amorce sans ancre ;
- périmètre du GO, en 6 cas ;
- « no_such_ask » jusqu'au rang 4 ;
- boucle après une création refusée, avec un **témoin sans détection** (aucun DELETE) ;
- création relancée sans dépôt ;
- ordre « fin » avant la borne ;
- ordre consommé avant la borne ;
- message causal exact ;
- aucun `exit` avant l'ordre consommé ;
- sorties brutes effacées même illisibles.

**Banc v9.** Tout le banc v8 (v1 à v8), plus **31 mutations v9** (liste dans `scripts/banc_mutations_sparks_exp7_nul_v9.py`).

## 2. Ce que le tir v9 éprouve, et ce qu'il n'éprouve pas

Le tir crée une instance au commit de tir, qui porte le code v9 sans addendum. L'amorce v9 clone, puis s'arrête à la garde du
code (« code ou addendum non conformes »), et le conteneur sort. Deux issues :
- **pas de boucle** : trois lectures « exited » avec `cur_state` « stopped » sur au moins 5 minutes, et `REDEMARRAGES=0`.
  L'ordre « fin » est poussé, puis `start` est envoyé. L'amorce lit l'ordre, se détruit, et l'inventaire rend « absente » ;
- **boucle** : la relance automatique refait l'amorce, qui trouve le disque, ne trouve aucun ordre et se détruit aussitôt.
  Le verdict rend « absente », et le journal porte « boucle de redémarrage présumée ». Si la machine ne se détruit pas, le
  verdict rend « boucle » et la session détruit l'instance par l'identifiant. Dans les deux cas, **nœud de Lazar** (points 8
  et 9).

Le tir n'éprouve ni `vastai copy`, ni la phase causale réelle, ni la copie d'un lot (risques déclarés, point 6).

## 3. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v9.py`. Sorties brutes, sans `.sha256`, dans `essais-et-banc-sparks-v9/`. Elles sont écrites au fil des passages, qui reprennent là où un redémarrage les aurait coupés (aucun ne l'a été).

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête `a655bbfa` | 329 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-a655bbfa.txt` | `ba764c16e7f74712e698d8af198acb3e144a467b334c3b40843d4075b855c0e1` |
| Essais sur le commit enfant `c2689059` (addendum factice, `COMMIT_CODE=a655bbfa…`) | 329 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-c2689059.txt` | `2a70ae06b9af07ae954f0a86a37e6e4a823ef226bfe2817954bcacda85987d2d` |
| Banc de mutations v9 | 229/229 tuées (code 1 et « failed ») : 22 v1, 52 v2, 40 v3, 30 v4, 30 v5, 6 v6, 7 v7, 11 v8, 31 v9 ; 8 témoins verts ; 0 défaut ; code 0 | `banc-a655bbfa.txt` | `9fb497cb05b107f72556b751d49a8020437845cbdcf78a9c6345fc5dcf8f74db` |
| Banc, détail | une ligne par mutation | `banc-a655bbfa.json` | `a00788e2bdca2baabb427a78cb3baec243b60230e944d96b35bfecfc8e83097f` |
| Exemple de sortie du mode tir (factice, hors réseau) | code 0 | `exemple-sortie-tir.txt` | `839a4dc734b742c09d8ec573bee7e0eb3ae59f79ec364c3d37144dc44f82ef68` |

Chaque passage final a été joué une seule fois, et aucun n'a été écarté (R4).

Avant le commit, l'essai v9 a été joué trois fois pendant son écriture, sur des fichiers non committés :
- 1 échec, arrêt au premier ;
- 6 échecs : la capture du code sous `set -e` dans le lanceur, que la correction remplace par `R=0; … || R=$?` ; deux attendus d'essai faux ; le faux `vastai` d'un essai, qui n'imprimait pas « destroying instance 1. » ;
- 0 échec.

Les témoins v6 et v9 du banc sautent chacun un essai, parce que la copie du banc n'est pas un dépôt git (essai du mode tir). Le même essai passe à la tête comme sur l'enfant.

Réserve (R4) :
- le résultat final est propre ;
- il n'éprouve `vastai` que par des sorties imitées d'après sa source 1.8.3 ;
- la forme réelle de `show instances --raw` et des états d'une instance sortie seule, `actual_status` et `cur_state`, n'est connue que par la source et le registre, pas par un appel. Le verdict de boucle est donc prudent : un `cur_state` resté « running » après une sortie lit « boucle ». Ce cas reste à trancher par le tir, avec le compte `REDEMARRAGES=` du journal.

## 4. Répétition jouet

**Jouée par moi, en local** (`unshare -pf`, aucun réseau, aucune poussée distante). Script : `essais-et-banc-sparks-v9/repetition-v9-locale.sh`.

Dispositif :
- dépôt nu local qui emprunte les objets du dépôt de travail (`alternates`, frontière superficielle recopiée) ;
- `DEPOT_URL=file://…` ;
- commit lancé = code v9 + addendum factice (écrit par `addendum_factice.py`) + registre des GO de `main` ;
- ordres poussés au dépôt nu ;
- faux `curl` journalisé.

Étapes :
1. création (fabrication jouet) ;
2. ordre 1 « copie » ;
3. ordre 2 « causal » ;
4. **relance sans ordre neuf**, c'est-à-dire une boucle. Elle remplace les étapes « rejoue » et « fin » de la v8 : en v9, la
   relance d'un ordre déjà fait est une boucle, qui détruit.

Attendus neufs :
- « démarrage n° N » à chaque redémarrage ;
- « fin de la phase causale, code [1-9], poussée vérifiée » (point 5) ;
- à l'étape 4, « ordre refusé (aucun ordre neuf) : boucle de redémarrage présumée, destruction immédiate » ;
- un seul DELETE.

Runs, tous comptés (R4) :
- **run 1** (`repetition-jouet-v9-locale-v1/`) : défaut du dispositif, pas du code. Le commit lancé ne portait pas le
  registre des GO de `main`, donc la ligne d'extension à 40 USD manquait.
  - Création : « GO non conforme : aucun calcul ».
  - Les relances suivantes ont toutes été lues comme des boucles (« GO-2026-11-04-04 non conforme à la date : boucle de
    redémarrage présumée, destruction immédiate ») : 3 DELETE, un par relance. Le faux `curl` laisse la machine en vie, ce
    qu'une vraie destruction ne ferait pas.
  - Fait utile : la détection marche aussi sur un refus qui précède l'ordre.
- **run 2** (`repetition-jouet-v9-locale-v2/`) : autre défaut du dispositif. L'addendum factice était écrit sous un autre
  nom, et son compagnon nommait `addendum.md`.
  - La garde du manifeste l'a refusé à juste titre : « MANIFESTE REFUSÉ : … nom 'addendum.md' au lieu de
    'SPARKS-EXP7-NUL-addendum-1.md' », puis arrêt avant tout calcul.
  - Run arrêté par moi après l'étape 1, par numéros de processus (R10).
- **run 3** : RUN3_V9

**Commande de la répétition sur le dépôt de travail** (pour la mère, avec réseau). C'est celle de la v8 (rapport v8,
section 5), avec ces changements :
- `CODE=a655bbfad4d14b57d259638b814e236e8f228af7` ;
- amorce v9 ;
- branche `essai/sparks-v9-repetition` ;
- étapes 4 et 5 de la v8 remplacées par l'étape 4 ci-dessous ;
- attendus de la section précédente.

Il faut d'abord pousser la branche `prep/sparks-exp7-nul-v9` : `worktree add … "$CODE"` exige que le commit soit connu du
dépôt où l'on joue.

```bash
#!/usr/bin/env bash
set -uo pipefail
CODE=a655bbfad4d14b57d259638b814e236e8f228af7
DEPOT=/home/user/controle-ia-travail
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v9-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v9-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v9-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
T 60 git -C "$DEPOT" show "$CODE:src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py" > "$J/addendum_factice.py"
T 60 python3 -I -B "$J/addendum_factice.py" "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md" "$CODE" || { echo "addendum factice non écrit : arrêt"; exit 2; }
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v9 (addendum factice marqué)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v9-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 10800 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/amorce-v9.sh"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v9.sh" > "$A"
etape() { T 5400 unshare -pf --mount-proc "${ENV[@]}" bash "$A" > "$J/$1.txt" 2>&1; echo "== $1 : code $?"; }
attendu() { if grep -qE -- "$3" "$2"; then echo "   OK   $1 : « $3 »"; else echo "   ÉCART $1 : « $3 » absent de $2"; fi; }
absent() { if grep -qE -- "$3" "$2" 2>/dev/null; then echo "   ÉCART $1 : « $3 » présent dans $2"; else echo "   OK   $1 : pas de « $3 »"; fi; }
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"; }
etape 1-creation
attendu 1 "$J/1-creation.txt" "mode jouet : addendum non exigé"
attendu 1 "$J/1-creation.txt" "fabrication, durée plafonnée"
attendu 1 "$J/racine/sparks/journal.txt" "essais : [0-9]+ passed"
attendu 1 "$J/racine/sparks/journal.txt" "essai d'égalité des lots : oui"
attendu 1 "$J/racine/sparks/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
attendu 1 "$J/racine/sparks/journal.txt" "ADDENDUM FACTICE \(jouet\)"
absent  1 "$J/racine/sparks/run.err" "No module named"
attendu 1 "$J/racine/sparks/run.err" "ARRET 0/28 modèles dans les bornes"
attendu 1 "$J/racine/sparks-v5-demarrages.txt" "^d [0-9]+ [0-9]+$"
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2 "$J/2-copie.txt" "redémarrage consigné au registre des démarrages : démarrage n° 2"
attendu 2 "$J/2-copie.txt" "ordre 1 \(copie\)"
attendu 2 "$J/2-copie.txt" "lot impossible"
absent  2 "$J/2-copie.txt" "boucle de redémarrage présumée"
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3 "$J/3-causal.txt" "ordre 2 \(causal\)"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
absent  3 "$J/racine/sparks-causal-002/run.err" "No module named"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "fin de la phase causale, code [1-9], poussée vérifiée"
absent  3 "$J/3-causal.txt" "boucle de redémarrage présumée"
etape 4-relance-sans-ordre-neuf
attendu 4 "$J/4-relance-sans-ordre-neuf.txt" "démarrage n° 6"
attendu 4 "$J/4-relance-sans-ordre-neuf.txt" "ordre refusé \(aucun ordre neuf\) : boucle de redémarrage présumée, destruction immédiate"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)"
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi
echo "   branches à supprimer par Lazar : essai/sparks-v9-repetition essai/sparks-exp7-nul-v5-$COURT essai/sparks-exp7-nul-causal-v5-$COURT-002 ordres/sparks-exp7-nul-v5-$COURT"
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v9-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v5-minuterie.log"
```

## 5. Commande exacte du tir, pour la fille

À ne lancer qu'après :
1. la réponse de Lazar au nœud R-1527 (clé d'instance) ;
2. une ligne de GO du tir dans `registres/go.md` : type « calcul », Lazar, au plus 5 USD, valide le jour du tir, périmètre
   qui nomme « SPARKS » et « tir », par exemple « SPARKS-EXP7-NUL tir réel » ;
3. **la poussée de la branche `prep/sparks-exp7-nul-v9`** (commit `a655bbfa…`) vers le dépôt de travail, par la mère :
   l'instance clone le dépôt et extrait le commit de tir, enfant du commit du code.

Il faut aussi `vastai` 1.8.3 dans le chemin de la session qui tire (point 22), ainsi que `VAST_API_KEY` et
`CONTROLE_IA_GITHUB_TOKEN` dans son environnement, jamais affichés. Toutes les commandes ci-dessous se jouent depuis un
clone du dépôt de travail extrait sur `prep/sparks-exp7-nul-v9`.

```bash
cd <clone du dépôt de travail> && git fetch -q origin prep/sparks-exp7-nul-v9 && git checkout -q a655bbfad4d14b57d259638b814e236e8f228af7
export SPARKS_REGISTRE_GO="$PWD/registres/go.md"        # registre de main, avec la ligne du tir
# 1. recherche d'offres : le lanceur imprime la commande ; la jouer telle quelle (sortie brute effacée par `offres`)
bash scripts/lancer_sparks_exp7_nul_v9.sh recherche
#    → timeout -k 10 120 env -i … vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw > … ; bash scripts/lancer_sparks_exp7_nul_v9.sh offres …
# 2. tir au rang 1 (25 minutes d'échéance) : contrôle de la liste fermée, du GO et du devis, puis le protocole pas à pas
bash scripts/lancer_sparks_exp7_nul_v9.sh tir a655bbfad4d14b57d259638b814e236e8f228af7 <GO_ID_DU_TIR> 25 1
```

Le mode tir imprime alors, avec les valeurs de l'offre et du GO, les étapes :
0. le commit de tir `essai/sparks-v9-tir-a655bbfad4d1` ;
1. la création, avec `GO_ID=<GO_ID_DU_TIR>`, `--disk 20`, l'étiquette, `GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN`, puis
   `apres-creation … $? <code> <GO> 25 1`. Sur « OFFRE RETIRÉE », il imprime la commande du rang suivant ;
2. les trois inventaires, le verdict `boucle $ID` et `journal-amorce` ;
3. la conduite selon le verdict ;
4. l'ordre « fin » ;
5. `start`, suivi de `apres-commande` ;
6. l'inventaire « absente » ;
7. le repli par `destruction $ID` ;
8. le devis.

Un exemple de cette sortie, joué hors réseau avec un registre de GO factice (GO-2026-11-05-09), est dans
`essais-et-banc-sparks-v9/exemple-sortie-tir.txt`.
