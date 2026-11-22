# Plan de marche de la session de lecture du barreau 5 (« sabotage ou empreinte de l'adaptateur ») — v1

Écrit le 22 novembre 2026, entre 19:27Z et 19:50Z (`date -u`), par la session de lecture `session_013QMayiuN339pSspJBRTwYL` (Opus 5.5), fille du conducteur `session_013QMayjM1PQPWkLifMw9HDR`. Pièce de classe C (travail). Accords : `GO-2026-11-19-86` (accord de calcul, plafond commun de 200 USD), `GO-2026-11-21-64`, `GO-2026-11-22-117` (mot de Lazar ; cité en texte libre seulement, jamais comme `GO_ID` : la garde de calcul ne lit pas les accords de rang 100 et plus).

Mandat suivi, chaque pièce vérifiée par son compagnon avant lecture, dans l'ordre où le dernier erratum prime : erratum 3 (`1c9d9ce1…`), erratum 2 (`4d1678b5…`), erratum 1 (`cde0279c…`), mandat v2 (`b1eb2afc…`). Accusé du conducteur reçu à 19:26:52Z ; ma ligne d'inscription est dans la liste « qui a lu quoi » v21.

Rôle aveugle : je ne vois ni ne rends aucun score, aire, statistique ni grandeur d'adaptateur, ni la table, ni le sel, ni un coût d'un adaptateur tenu à l'écart. Je n'ai lu ni `registres/etat.md`, ni une passation, ni `registres/decisions.md` (mandat, § 9, point 10 ; écart à R14 déclaré). Je n'ai pas joué la suite d'essais entière (erratum 2, point 3).

---

## 1. Phase 1 : ce qui est fait (aucune instance créée, rien dépensé)

| geste | résultat |
|---|---|
| empreintes de lancement (`docs/sha256sums-lancement-v2.txt`) | code 0, trois « OK » |
| `verifier-arbre .` à la tête `fea9a345…` de `conducteur-b5f/lecture-v1` | **code 1** (seul le code est rendu, erratum 3, point 2) ; non expliqué par moi ; à la mère |
| références du clone dont le nom contient `barreau5-familles-jumelles-v1-formation` | **0** (avant et après les deux récupérations par nom entier) ; le clone de la session ne portait que deux références |
| branches récupérées, par leur nom entier, vers une référence distante | `conducteur-b5f/lecture-v1` (tête `fea9a345…`), `course/barreau5-commande-lecture-v2` (tête `5402367e…`) ; rien d'autre |
| texte scellé `bdff244f…`, devis `dc886195…`, additif 1 v2 `c3120d3a…`, sa pièce de scellement `02d1c52f…`, sa vérification `905f2015…` | égaux sur disque et au compagnon |
| au commit `c76e7916…` (`CODE-LECTURE-B5F`) : `lecture_v1.py` `ed0999df…`, `relecture_v1.py` `f6bd8c15…`, lanceur v1 `ae501c55…`, amorce `54a676f3…` | égaux (par `git show`) |
| au commit `5402367e…` : module v2 `c6c5d11c…`, lanceur v2 `c07fc124…`, essais v2 `82452204…` | égaux |
| `5402367e…` descend de `c76e7916…` ; différence entre eux | trois fichiers, tous ajoutés (`A`) : les trois de la liste fermée ; rien d'autre |
| registre propre, lignes à clé (filtre par programme, clés du § 4 point 4 et du § 5.2 seulement) | les huit clés attendues, dans l'ordre des dates (`SCELLEMENT` 19T23:47:32Z … `ENGAGEMENT` 21T16:02:55Z, `sha256 553cb395…`) ; `GO-LECTURE-B5F` à 2026-11-22T19:22:01Z, contenu `GO-2026-11-19-86` ; ni `SCORES-B5F`, ni `OUVERTURE-B5F`, ni `LECTURE-B5F`, ni `VERDICT-B5F` |
| colonne de référence de `GO-LECTURE-B5F` (registre au commit `e8ed1b11…`), par la fonction `commit_de_commande_cite` du module v2 | rend `5402367e5b62c8ac294c55d5cc0230ebdfbaa457` ; aucun accent combinant ; ligne égale à sa forme composée |
| essais, arbre de commande (`5402367e…`), `tests/test_commande_lecture_v2.py` | `113 passed, 1 skipped` ; arbre resté propre |
| essais, arbre au code figé (`c76e7916…`, en attendant le commit de la marche), les trois fichiers du § 5.1 | `90 passed` ; arbre resté propre ; **à rejouer au commit de la marche** |
| registre des accords de l'arbre de commande | la ligne `GO-2026-11-19-86` y est, identique à l'octet à celle de la tête ; `GO-2026-11-22-117` n'y est pas (sans effet : elle n'est jamais un `GO_ID`) |
| inventaire chez le loueur (identifiant, étiquette, état) | cinq instances, aucune à moi : 58936096, 58936099, 58936100, 60988826 (arrêtées), 61932710 (`neuron-lens-reajustement`, en marche). Aucune n'est touchée |
| clés, par leur nom | `VAST_API_KEY` présente (lue par l'outil du loueur dans l'environnement : aucune écriture sur disque) ; `HF_TOKEN` présente, de forme d'un jeton Hugging Face ; **`GH_TOKEN` présente mais de 14 signes, sans la forme d'un jeton GitHub** (question Q1) |
| outils | outil du loueur installé (`vastai` 1.11.2, sous `/root/.local/bin`) ; environnement Python à part, dans mon bloc-notes, aux exigences `requirements-cpu.txt` de `c76e7916…` (égales à celles de `5402367e…`) |
| recherche d'offres d'essai (lecture seule, aucune création), 19:38Z | requête du § 3.2, disque de 300 Go : neuf offres ; quatre passent toutes les bornes de la relecture décisive (1,1533 ; 1,2333 ; 1,2600 ; 1,2867 USD de l'heure ; stockage 0,0986 USD de l'heure au compte du code) ; **sur les neuf, `dph_total` = `dph_base` + `storage_cost` × 300 / 720 exactement** : le pas 4 « supposé » de l'additif tient sur cet instantané |

Lectures faites, et rien d'autre : `CLAUDE.md` ; les quatre pièces du mandat ; du texte scellé, les seules plages du § 3 point 2 (l. 35, 151-179, 217-233, 257, 260, 261, 345-361, 363-367, 369-371, 373-430, 432-434, 436-448), chaque plage vérifiée par programme à sa première ligne avant affichage ; du devis, § 3 (table des pièces, ligne « Carte »), § 4 et § 5 ; l'additif 1 v2 en entier, sa pièce de scellement en entier, la seule remarque 2 de sa vérification (l. 25) ; le lanceur v1, l'amorce, `relecture_v1.py` (en-tête, gardes de configuration, de registre, d'entrées, et côté session, l. 1-300 et 800-1247), le module et le lanceur v2. Le rapport de vérification `fca7d949…` n'est pas encore entre mes mains ; je ne l'ouvrirai pas (erratum 2, point 1).

## 2. Valeurs et noms

- Bloc-notes : `W=/tmp/claude-0/-home-user-controle-ia-travail/bda5eb11-739e-5dcf-b0d4-c583e4a0d6a7/scratchpad` ; interpréteur `PYTHON_B5F=$W/venv/bin/python`.
- Dépôt : `DEPOT=https://github.com/lciric/controle-ia-travail.git`.
- `CODE_FIGE=c76e79169eee337ce66c7d88f62d039e853eebfc` ; `COMMANDE=5402367e5b62c8ac294c55d5cc0230ebdfbaa457` (branche `course/barreau5-commande-lecture-v2`).
- Du signal (je n'en choisis aucune) : `COMMIT_MARCHE`, `BRANCHE_MARCHE`, `ENTREES_COMMIT`, `DIVERGENCE`, `GARDE`, `EXISTANTS.json` (par pièce), cumul commun relevé, chemin du rapport `fca7d949…`, mot sur les nœuds encore ouverts.
- `GO_ID=GO-2026-11-19-86` pour « config », « commande », « detruire ».
- Coupures (erratum 2, point 7) : relecture décisive **9 USD**, répétition générale **8 USD**.
- Témoin de « verifier-destruction » : 58936096 (intouchable : lu dans la liste, jamais touché).

## 3. Phase 2, au signal

### 3.0 Réception
1. Écrire les valeurs du signal dans `$W/signal-v1.txt` (aucune clé).
2. Refus mécaniques, avant tout geste : `BRANCHE_MARCHE` sous `formation-b5f/`, `course/`, `traces/` ou `donnees/` ; commit de commande autre que `5402367e…` ; `GARDE` hors des trois valeurs ; `DIVERGENCE` hors de 0 et 1 → je ne récupère rien, je le dis au conducteur.
3. Rapport `fca7d949…` : `sha256sum <chemin donné>` contre `fca7d949f7f8b6865e7b8de048e2c8ace80dae90503299074c726f76ea302c04` ; jamais ouvert. Différent : arrêt (liste d'arrêt, point 1).

### 3.1 Clone neuf, branches, arbres (nœud 1, réponse retenue)
```
git clone -q --single-branch --branch "$BRANCHE_MARCHE" "$DEPOT" "$W/clone"
git -C "$W/clone" for-each-ref --format='%(refname)' | grep -c 'barreau5-familles-jumelles-v1-formation'   # 0 attendu, rendu
git -C "$W/clone" fetch -q origin refs/heads/course/barreau5-commande-lecture-v2:refs/remotes/origin/course/barreau5-commande-lecture-v2
git -C "$W/clone" fetch -q --filter=blob:none origin \
    refs/heads/donnees/barreau5-familles-jumelles-v1-entrees-de-lecture:refs/remotes/origin/donnees/barreau5-familles-jumelles-v1-entrees-de-lecture
git -C "$W/clone" for-each-ref --format='%(refname)' | grep -c 'barreau5-familles-jumelles-v1-formation'   # 0, rendu
```
La branche des entrées est récupérée sans le contenu des fichiers (`--filter=blob:none`) : je n'en ai besoin que pour les noms et pour « commande » (`git branch -r --contains`). Jamais de `checkout` ni d'arbre de travail sur elle (erratum 2, point 5).

Contrôles, sans rien afficher d'autre que le résultat :
- `git -C "$W/clone" merge-base --is-ancestor "$COMMIT_MARCHE" origin/"$BRANCHE_MARCHE"` et `… --is-ancestor $CODE_FIGE "$COMMIT_MARCHE"` ; `git -C "$W/clone" diff --quiet $CODE_FIGE "$COMMIT_MARCHE" -- <CHEMINS_GELES>` (la constante de `harnais/validation_reelle.py`) ; `merge-base --is-ancestor "$ENTREES_COMMIT" origin/donnees/barreau5-familles-jumelles-v1-entrees-de-lecture`.
- Entrées, **noms seuls**, par programme : `git -C "$W/clone" ls-tree -r --name-only "$ENTREES_COMMIT"` et `git -C "$W/clone" diff-tree --root --no-commit-id -r --name-status "$ENTREES_COMMIT" -- entrees-de-lecture-b5f`. Attendu : sous `entrees-de-lecture-b5f/` seulement, `X-01` à `X-30` sans trou (`.safetensors`), `A1` à `A3` × {jumeau, saboteur, sur_saboteur} (`.safetensors`), `A1` à `A3-saboteur-evaluation.jsonl`, et leurs compagnons `.sha256` ; tous ajoutés par ce seul commit. Je rends les comptes par motif (tenus, apprentissage, épisodes, compagnons) et tout nom hors liste. Un nom hors liste, un fichier hors du dossier, ou un ajout par plus d'un commit : arrêt (mandat, § 2 ; nœud).
- Registre propre au commit de la marche : même filtre qu'en phase 1 (lignes à clé seules) ; `GO-LECTURE-B5F` présente, contenu `GO-2026-11-19-86`, et `commit_de_commande_cite` rend `5402367e…` ; aucune des quatre clés de clôture.

Arbres de travail, d'un même clone :
```
git -C "$W/clone" worktree add --detach "$W/fige" "$COMMIT_MARCHE"
git -C "$W/clone" worktree add --detach "$W/commande" 5402367e5b62c8ac294c55d5cc0230ebdfbaa457
```
Dans l'arbre de commande, le registre des accords est celui du commit de commande (ligne `GO-2026-11-19-86` égale à l'octet) : je n'y touche pas, sauf mot contraire (Q4).

Essais (R5), ligne de compte seule (erratum 2, point 3 ; erratum 3, point 1) :
```
cd "$W/fige" && PYTHONPATH=src "$PYTHON_B5F" -m pytest tests/test_barreau5_familles_relecture_v1.py tests/test_lancer_b5f_lecture_v1.py \
    tests/test_barreau5_familles_engagement_v1.py --tb=no -rN -q -p no:cacheprovider --basetemp="$W/essais-fige-marche" | tail -n 1
cd "$W/commande" && PYTHONPATH=src "$PYTHON_B5F" -m pytest tests/test_commande_lecture_v2.py --tb=no -rN -q -p no:cacheprovider \
    --basetemp="$W/essais-commande-marche" | tail -n 1
git -C "$W/fige" status --porcelain --untracked-files=all ; git -C "$W/commande" status --porcelain --untracked-files=all   # vides
```
Un essai rouge : arrêt, son nom seul au conducteur.

### 3.2 Une pièce (répétition d'abord si le signal la donne, relecture décisive ensuite)
Dossier de la pièce : `P=$W/repetition` ou `P=$W/lecture`. Environnement : `GO_ID=GO-2026-11-19-86`, `PYTHON_B5F=$W/venv/bin/python`.

**Pas 1, ligne d'engagement** (rédigée par moi, inscrite par la mère avant la première minute) :
- relecture : « engagement : barreau 5, familles jumelles, pièce relecture (GO-2026-11-19-86, plafond 200 USD commun, coupure 9 USD, arrêt au cumul plus un quart d'heure) : texte prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md, sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935, commit c76e79169eee337ce66c7d88f62d039e853eebfc (CODE-LECTURE-B5F) ; A100 SXM4 80 Go ≤ 1,30 USD de l'heure, stockage ≤ 0,12 USD de l'heure (additif 1 v2), étiquette b5f-lecture-v1 ; attendu [selon la garde : 9,6 à 17,3, ou 10,1 à 18,3 avec les points d'ancrage, pour trois_couches ; 5,2 à 7,7 pour une_sur_dix] ; pire cas [26,1, ou 27,5 | 14,0] ; dépense antérieure sous cette ligne [cumul commun relevé] ; mot de Lazar GO-2026-11-22-117 » ;
- répétition : même forme, « pièce répétition », « coupure 8 USD », sans la mention de stockage à 0,12 (la répétition garde 0,08), étiquette b5f-repetition-v1, attendu 4,2 à 6,4, pire cas 11,5.
J'attends l'accusé de l'inscription avant le pas 2.

**Pas 2, offre** (nœud 6 : recherche toutes les quinze minutes jusqu'à une offre admise ; machine 144450 exclue) :
```
vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 gpu_ram>=80 cpu_cores_effective>=16 cpu_ram>=128 cuda_max_good>=13.0 \
    disk_space>=DISQUE dph_total<=1.30 machine_id!=144450 rentable=true' --storage DISQUE --raw > "$P/offres-<AAAAMMJJ-HHMMSS>.json"
```
`DISQUE` = 300 (relecture) ou 150 (répétition). Un programme range les entrées par `dph_total` croissant puis par `id` croissant, et écrit la première dans `$P/OFFRE.json` ; je ne choisis rien. Pour la relecture, je relève `dph_total`, `dph_base`, `storage_cost` et rends si `dph_total` = `dph_base` + `storage_cost` × 300 / 720. Seul un refus de « commande » dont le motif commence par « offre : » fait passer à l'entrée suivante ; tout autre refus est un arrêt. Aucune offre admise : aucune création, recherche suivante dans quinze minutes.

**Pas 3, « config »** (relecture seulement ; arbre figé) :
```
cd "$W/fige" && GO_ID=GO-2026-11-19-86 PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v1.sh \
    config "$W/fige" decisif ../entrees/entrees-de-lecture-b5f "$DIVERGENCE" "$GARDE" > "$P/CONFIG.json"
```
Pour la répétition, « config » du lanceur figé refuse (il ne reçoit pas les quatre adaptateurs) : ni « config » ni « verifier » ; « commande » seule, qui rejoue les mêmes gardes (nœud 4, réponse retenue). **Écart déclaré.**

**Pas 4, « verifier »** (relecture seulement ; arbre figé ; juste avant la création) :
```
cd "$W/fige" && PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v1.sh verifier "$W/fige" "$COMMIT_MARCHE" "$P/CONFIG.json"
```
`CONFIG.json` ne porte pas les points d'ancrage : seule « commande » les contrôle ; je n'ajoute rien à la main.

**Pas 5, « commande »**, `RUN_ID=$(date -u +%Y%m%d-%H%M%S)-b5f-lecture` (ou `-b5f-repetition`) :
```
# relecture décisive : arbre de commande, version 2
cd "$W/commande" && GO_ID=GO-2026-11-19-86 PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v2.sh commande decisif \
    "$W/commande" "$P/OFFRE.json" "$COMMIT_MARCHE" "$BRANCHE_MARCHE" "$RUN_ID" "$ENTREES_COMMIT" "$DIVERGENCE" "$GARDE" \
    "$P/EXISTANTS.json" > "$P/commande-$RUN_ID.txt"
# répétition générale : arbre figé, version 1
cd "$W/fige" && GO_ID=GO-2026-11-19-86 PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v1.sh commande repetition \
    "$W/fige" "$P/OFFRE.json" "$COMMIT_MARCHE" "$BRANCHE_MARCHE" "$RUN_ID" - "$DIVERGENCE" une_sur_dix \
    "$P/EXISTANTS.json" > "$P/commande-$RUN_ID.txt"
```
Code 0 : la commande est la seconde ligne du fichier ; code 2 : refus, motif à la lettre au conducteur (sauf « offre : », pas 2). Les adaptateurs existants doivent être au commit de la marche (`git cat-file -e`), à leur empreinte.

**Pas 6, création.** Avant de jouer, je lis dans la commande : l'identifiant de l'offre, `--disk 300|150`, `--label b5f-lecture-v1|b5f-repetition-v1`, `--cancel-unavail`, `COMMIT=$COMMIT_MARCHE`, `ENTREES_COMMIT=` (« - » pour la répétition), `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `$HF_TOKEN` et `$GH_TOKEN` écrits par leur nom. Puis, aussitôt, telle quelle :
```
bash -c "$(sed -n '2p' "$P/commande-$RUN_ID.txt")" > "$P/creation-$RUN_ID.json" 2> "$P/creation-$RUN_ID.err"
```
(les clés sont développées par ce shell, depuis l'environnement ; `vastai` lit `VAST_API_KEY` dans l'environnement). Je rends l'identifiant d'instance de la réponse (`new_contract`). Si la sortie ne porte pas d'identifiant : liste des instances (réduite) ; rien de créé → retour au pas 2 ; une instance a existé, même une minute → pièce tombée (nœud 5, réponse retenue : arrêt, versement de ce qui existe, rien de relancé sans un mot de Lazar).

**Pas 7, veille**, toutes les quinze minutes au plus :
- état, par l'identifiant : `vastai show instances --raw`, réduit par programme à `id`, `label`, `actual_status`, `cur_state`, `dph_total`, `start_date` (liste d'objets, clés d'origine, témoin compris), écrit dans `$P/liste-<heure>.json` ; jamais la forme brute à l'écran ;
- journal : `vastai logs ID --tail 200`, gardé dans `$P/journal-<heure>.txt` ; je n'y lis que les lignes d'étape (préfixe « B5F ») ; tout compte autre qu'un compte de fichiers ou d'étapes (par adaptateur, famille, membre, classe ou signe) ou toute grandeur d'adaptateur : « journal non conforme », arrêt (erratum 2, point 6 ; mandat, § 6) ;
- dépense : dès que le cumul relevé de l'instance plus un quart d'heure atteint **9 USD** (8 pour la répétition), ou que le cumul commun plus un quart d'heure atteint 200 USD : `vastai stop instance ID` (par l'identifiant, sans destruction), appel au conducteur. La méthode du relevé est la question Q2.

**Pas 8, versement des scores fermés.** J'attends au journal « versement des sorties prouvé … au commit C » et « versement final prouvé au commit C », même C. Puis :
```
git -C "$W/clone" fetch -q origin refs/heads/donnees/barreau5-familles-jumelles-v1-lecture:refs/remotes/origin/donnees/barreau5-familles-jumelles-v1-lecture
# (répétition : …-v1-repetition)
cd "$W/fige" && PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v1.sh scores "$W/fige" "$C" "$RUN_ID" > "$P/scores-ligne.txt"   # relecture seulement
```
« scores » lit les fichiers fermés pour leurs seules tailles et empreintes ; je n'en ouvre aucun. Sans la seconde ligne, ou avec un « SIGNAL POUR LA MÈRE » : aucune destruction, transmis à la lettre. Sous `trois_couches` ou `couche_15`, l'amorce écrit ce signal par construction (activations à verser sur un volume qu'elle ne connaît pas) : aucune destruction, nœud 8 (question Q3).

**Pas 9, inventaire puis destruction** (seulement si le pas 8 a vu « versement final prouvé ») :
```
git -C "$W/clone" show "$C":traces-b5f-lecture/inventaire-final.json > "$P/INVENTAIRE.json"
git -C "$W/clone" show "$C":traces-b5f-lecture/inventaire-final.json.sha256 > "$P/INVENTAIRE.json.sha256"
# contrôle : empreinte égale au compagnon ; l'inventaire liste donnees/$RUN_ID/inventaire-activations.json (noms, tailles, empreintes)
vastai show instances --raw | <réduction par programme> > "$P/LISTE.json"
cd "$W/fige" && GO_ID=GO-2026-11-19-86 PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v1.sh detruire \
    "$W/fige" ID decisif|repetition "$P/LISTE.json" "$P/INVENTAIRE.json" "$C" > "$P/destruction.txt"
bash -c "$(sed -n '1p' "$P/destruction.txt")"          # la commande imprimée, telle quelle
vastai show instances --raw | <réduction> > "$P/LISTE_NEUVE.json"
cd "$W/fige" && PYTHON_B5F="$W/venv/bin/python" bash scripts/lancer_b5f_lecture_v1.sh verifier-destruction "$P/LISTE_NEUVE.json" ID 58936096
```
Une destruction ne se juge que par « verifier-destruction ». Je rédige la ligne du registre des arrêts ; la mère la verse. Si la minuterie de l'instance l'a déjà détruite, je le constate par la même vérification.

**Pas 10, `SCORES-B5F`** (relecture seulement) : je rends au conducteur le contenu de `$P/scores-ligne.txt`, à l'octet. La relecture ne se refait pas.

Entre les deux pièces : je passe de la répétition à la relecture sur des étapes seulement (marche menée au bout, versement prouvé, instance détruite), jamais sur une sortie (liste d'arrêt, point 12).

### 3.3 Ce que je rends, ce que je ne rends jamais
Je rends : étapes et heures (UTC), identifiants et étiquettes d'instance, identifiant et prix de l'offre, dépenses, commits et empreintes, ligne des scores, refus et arrêts à la lettre, lignes de registre rédigées. Je ne rends jamais un score, une aire, un résumé, une statistique, un produit, une poussée, une divergence, une norme, un poids, ni le contenu d'un fichier fermé, ni un nom opaque rapproché de quoi que ce soit. À la fin : passation scellée dans ce dossier.

## 4. Écarts déclarés
1. Routine de reprise sans `registres/etat.md`, passations ni `registres/decisions.md` (nœud 10) ; suite d'essais entière non jouée (erratum 2, point 3).
2. Répétition commandée par « commande » seule, sans « config » ni « verifier » (nœud 4).
3. Essais des trois fichiers de l'arbre figé joués en phase 1 au commit `c76e7916…`, faute de commit de la marche ; ils seront rejoués au commit de la marche.
4. La coupure de 9 USD de la relecture est plus stricte que celle du code (21 USD) : l'échéance que la commande imprime et que porte l'instance est calculée sur 21 USD ; c'est ma veille qui tient les 9 USD (pas 7).

## 5. Questions au conducteur
- **Q1 — `GH_TOKEN`.** Dans ma session, la variable existe mais a 14 signes et n'a pas la forme d'un jeton GitHub : elle semble être un tenant-lieu que remplace le relais réseau de ma session. Hors de ce relais, l'instance ne pourrait ni cloner le dépôt privé ni pousser ses sorties : la marche s'arrêterait au clonage, après la création (pièce tombée). Comment la session de formation a-t-elle passé un vrai jeton à ses instances ? Sans réponse, je ne crée rien.
- **Q2 — cumul.** Le cumul commun relevé au départ, et la méthode pour relever le cumul d'une instance. Proposition : heures depuis `start_date` × `dph_total`, plus la sortie de données facturée si le loueur la donne, recoupé par la facturation du compte ; la même méthode que pour la formation.
- **Q3 — `GARDE` et coupure.** Sous `trois_couches`, l'attendu de la relecture (9,6 à 17,3 USD, dont 3,9 à 7,6 de sortie de données) dépasse la coupure de 9 USD : un arrêt à la coupure en pleine marche ferait tomber la pièce. Sous `une_sur_dix`, l'attendu est de 5,2 à 7,7 USD. Si `trois_couches` est retenue, il faut aussi la procédure de transfert vers le volume, et la règle de destruction (l'amorce n'écrit jamais le témoin sous cette garde : aucune destruction par la minuterie).
- **Q4 — registre des accords de l'arbre de commande.** Je le laisse au commit de commande (la ligne `GO-2026-11-19-86` y est égale à l'octet) ; confirmes-tu, ou veux-tu que je le mette à jour depuis `main` (permis : hors des chemins gelés) ?
- **Q5 — répétition.** Quatre adaptateurs existants (`R<k>-saboteur`, `R<k>-temoin`), chacun au commit de la marche, chemin hors de `docs/`, `diag/`, `runs/`, à son empreinte : c'est encore ouvert.
- **Q6 — `verifier-arbre .`** rend le code 1 à la tête de `conducteur-b5f/lecture-v1` ; je n'en ai rien lu d'autre. Est-ce connu ?
- **Q7 — journal.** Sur la branche de sortie, `traces-b5f-lecture/journal/` porte aussi `marche.err`, `essais.txt`, `pip.txt` et d'autres fichiers d'outil. Je propose de n'ouvrir que `journal-b5f-lecture.txt` (lignes d'étape), et des autres les noms et tailles seulement. D'accord ?
- **Q8 — heures.** Les errata 2 et 3 disent « vers 19:40Z » et « vers 19:50Z » ; mon horloge lisait 19:27Z à l'accusé et 19:38Z pendant la recherche d'essai. Sans effet sur la marche ; signalé seulement.
