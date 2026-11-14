# Préparation du lancement de l'audit des fuites de T0.7 — v1

- **Statut** : pièce de préparation, écrite à la demande de la session mère (préalable de l'étape B : clé `AUDIT-FUITES-T07`
  manquante, R-2734). Elle ne lance rien, ne tranche rien, ne change aucun texte scellé ; aucune dépense, aucune machine,
  aucun commit. Non contre-lue.
- **Rédacteur** : préparateur neuf, sous-agent de la session mère (modèle A), le 2026-11-14 de 11:53:13Z à la fin de ce texte
  (heures relevées par `date -u`). Il n'est **ni l'auditeur ni le contre-lecteur** de cet audit, et n'en sera pas.
- **Lu** : la consigne scellée de l'audit en entier (`prereg/T0.7-consigne-audit-fuites-v1.md`, `43102e80…3a5d`) ; dans
  `registres/decisions.md`, les lignes R-2355, R-2359, R-2413, R-2563, R-2564, R-2566, R-2598, R-2605, R-2692, R-2704 (résumé
  du verdict de P3-bis, chiffres compris), R-2711, R-2718, R-2720, R-2734, R-2735, R-2737, R-2741, et les en-têtes des
  lignes jusqu'à R-2745 ; dans `registres/scellements-v1.md`, les clés et horodatages des quinze lignes, les lignes entières
  des clés lues par l'auditeur, de `VERDICT-P3BIS`, `SCELLEMENT-P3BIS`, et la seule cellule « chemin » des lignes
  `SCORES-T07`, `SONDES-T07`, `GO-LECTURE-T07`, `SCELLEMENT-T07` ; l'en-tête de `registres/etat.md` ; les lignes de
  `registres/qui-a-lu-quoi-v1.md` qui nomment l'audit ; le travail du compte 4 sur la préparation de l'audit (§ 2.3) ; les
  préalables du compte 3 (`docs/procedures/lecture-7b-etape-b-compte-3-v1/prealables-v1.md`, `0cd96b62…`, constats 1 à 8 et
  étapes 1 à 5) et le bloc A2 de sa commande v1 ; `registres/code-t07/CODE-T07-v3.json` (champ `commit`, entrée de
  `criteres_v1.py`) ; dans la configuration scellée de 7b (`prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1ba…`), les seuls
  champs que l'auditeur lira au manifeste ; le code de `valider_audit_fuites`, de `manifeste.versions`, du crochet
  `.claude/hooks/garde_calcul.py` ; l'entrée `H1-classification` de `docs/sources/invites-2606.08892-v1/index.json`.
- **Non ouvert** : **aucune donnée ni sortie de 7a, 7b ou T0.7** ; aucun fichier sous `diag/`, `runs/`, `donnees/` de ces
  courses (les entrées de 7b sont d'ailleurs absentes du clone) ; de la branche de 7b, seuls ont été lus, dans un dépôt sans
  contenu de mon bac (effacé), la chaîne des commits (métadonnées), les tailles des huit chemins exacts et les quatre
  compagnons `.sha256` (empreintes) ; aucun dossier de 7b listé. Du texte scellé de T0.7, seules ses deux lignes de registre ont
  été hachées par programme (cellules), et le début des l. 2207 et 2208 affiché pour repérer leur forme. Aucun identifiant de
  modèle n'est écrit ici.

**Verdict.** Les conditions de lancement vérifiables sur les noms, empreintes et lignes de registre sont **tenues** (vérificateur :
48 contrôles conformes, 0 en défaut ; ses 9 essais R5 conformes). Le **découpeur est rapatrié** (commit `c7484c43…` présent,
trois empreintes égales). **Trois gestes restent avant le lancement**, à confier à un sous-agent puisque la mère ne lit rien de 7b
(R-2741) : rapatrier les quatre entrées de 7b (absentes du clone de la mère), jouer la comparaison des versions (condition 3 de
R-2359) et lire le commit du manifeste. **Lancement possible aujourd'hui** : environ 20 minutes de gestes, puis 3,5 à 4,5 heures
d'audit et 1 à 1,5 heure de contre-lecture (§ 13 de la consigne), sur processeur, 0 USD. **Consigne de lancement à donner : la
v2** (`consigne-lancement-auditeur-v2.md`), et la **v2** de celle du contre-lecteur (§ 5, D3).

## 1. Conditions de lancement (consigne, § 4 ; R-2355, R-2359, R-2605)

Relevé du vérificateur à 2026-11-14T12:26:38Z (`sorties-verifier-conditions-audit-fuites-t07-v1.txt`, contrôles C1 à C15 ;
`main` à `3663b1d8`, registre `6ea1e624…`).

| n° | condition | source | constat | état |
|---|---|---|---|---|
| 1 | Consigne scellée sous son nom, égale à son compagnon, sans marqueur | § 4, préalable 1 | `43102e80…3a5d` = compagnon = ligne ; 0 motif `<<NOM>>` (les trois marqueurs des brouillons sont remplis) | **tenue** |
| 2 | Ligne `CONSIGNE-AUDIT-FUITES-T07` une fois, quatre cellules, chemin et empreinte égaux | § 4, préalable 1 | l. 9, `2026-11-11T14:08:06Z` | **tenue** |
| 3 | Ligne `RUN-CONFIRMATION-T06` une fois ; forme `runs/<RUN_7B>/manifeste.json` ; `RUN_7B` ≠ 7a ; contrôle sur la ligne seule | § 4, préalable 2 | l. 11 ; `RUN_7B` = `20261111-151701-t06-reel` ; empreinte `7e1ac1f0…` = R-2413 | **tenue** |
| 4 | Manifeste égal à la ligne et à son compagnon ; `config.go_id` = `GO-2026-11-02-28` ; commit du manifeste présent sans `fetch` | § 4, préalable 2 | manifeste **absent du clone** ; à la tête `55c3e3eb` de `calcul/t06-confirmation-7b-v1`, son compagnon = `7e1ac1f0…` = la ligne ; `go_id` = `GO-2026-11-02-28` dans la configuration scellée de 7b (manifeste non ouvert) ; commit **probable** `935262b17ca95894a882b02f1526ee39d1738652` (base de la branche de 7b : commit de scellement de T0.6, voie B), **présent**, ancêtre de `main` | rapatriement (G1), commit à confirmer (G3) ; l'auditeur contrôle |
| 5 | Les deux entrées de 7b présentes, égales à leurs compagnons et au résultat `episodes-t06` | § 4, préalable 3 | **absentes du clone de la mère** ; présentes sur la branche de 7b (§ 3 ci-dessous) | **à rapatrier** (G1) |
| 6 | Aucune ligne `AUDIT-FUITES-T07` (R12) | § 4, préalable 4 | 0 ligne | **tenue** |
| 7 | Fenêtre : après la poussée vérifiée des sorties de 7b | § 4, « Fenêtre » | R-2413 (compagnons conformes, tête `55c3e3eb`) ; ligne `RUN-CONFIRMATION-T06` 2026-11-13T18:52:43Z ; tête distante inchangée (`git ls-remote`, 11:58:47Z et 12:26:38Z) | **tenue** |
| 8 | Fenêtre : avant l'exécution de l'étape B | § 4, « Fenêtre » | `AUDIT-FUITES-T07` et `ISSUE-MOTS-ET-COUT-T06` absentes : l'étape B, qui les exige, n'a pas pu être jouée ; R-2734 : pas avant mardi 17 | **tenue** |
| 9 | CLAF-18 contre P3-bis scellé (R-2359, condition 1) | § 4, « Ouverture des textes de 7b avant le verdict de P3-bis » | `VERDICT-P3BIS` inscrite le 2026-11-14 à 10:30:38Z : les textes de 7b seront ouverts **après** le verdict ; le remède que la consigne prévoit en cas de règle contraire (« attente du verdict de P3-bis ») est donc accompli, quoi que dise P3-bis. Règle résiduelle relevée par le compte 4 (P3-bis l. 1736-1740 et 2629 : « aucune version de T0.7 scellée après `VERDICT-P3BIS` ne lit 7b ») : sans effet, la consigne n'est pas une version de T0.7 et elle est scellée avant (2026-11-11T14:08:06Z). P3-bis non relu par ce préparateur | **tenue, sans objet** ; à consigner (G4) |
| 10 | Commit du découpeur `c7484c43` dans le clone de l'auditeur (R-2359, condition 2) | § 6.1 | absent à 12:02:44Z ; rapatrié par refspec explicite à 12:02:46Z ; commit orphelin (aucun parent), hors de `main` ; `tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`, `special_tokens_map.json` `6f38c737…` égaux à la consigne et aux compagnons du commit | **tenue** |
| 11 | Versions du manifeste de 7b comparées à `.venv` (R-2359, condition 3 ; R-2355, Q-B5-1 : chemin de décodage) | — | `.venv` : Python 3.13.18, numpy 2.4.6, transformers 5.18.0, tokenizers 0.23.2 (versions épinglées de R-2355 ; `requirements-cpu.txt`, que `requirements-gpu.txt` inclut, les épingle aussi au commit probable) ; manifeste non ouvert | **à faire** (G2) |
| 12 | Commits que le clone de l'auditeur doit contenir sans `fetch` (R-2605) | § 5.1, points 5 et 6 | `c7484c43` présent ; `7a54d431` présent ; `1609a4bf` présent ; `c2fab6cc` (commit de `CODE-T07-v3.json`) présent ; commit du manifeste : probable `935262b1`, présent | **tenue** (sous G3) |
| 13 | Modules importés égaux à leur version au commit cité | § 5.1, point 6 | `statistiques.py` `a8552575…` = `7a54d431` = arbre ; `sondes/evaluation.py` = `7a54d431` ; `criteres_v1.py` `12b999fe…` = `c2fab6cc` = entrée « fichiers » = `8ae9fc44` ; les quatre modules du commit du manifeste = commit probable ; `src/controle_ia/` de `main` = C7 (`c2fab6cc`), aucun fichier non suivi | **tenue** (l'auditeur refait contre le commit lu) |
| 14 | Sources de construction au commit du manifeste | § 5.1, point 5 | toutes présentes au commit probable, égales à `1609a4bf` et à l'arbre ; `prereg/P3-consignes-v1.md` = `a68468fe…` = `consignes_sha256` de la configuration scellée ; `H1-classification.txt` = `69d50fb9…` = son index | **tenue** (probable) |
| 15 | Cellules gelées du § 2 égales au texte scellé de T0.7 | § 2, § 10 | T0.7 `d7d180ec…` ; deuxièmes cellules `381a72d5…` (l. 2208) et `95c8b659…` (l. 2207), une ligne chacune ; ligne `AUDIT-FUITES-T07` `53eca69e…` | **tenue** |
| 16 | Interprète pour le découpeur | § 6.1 | `transformers` 5.18.0 dans `.venv` (chargement hors ligne déjà éprouvé par la contre-lecture 2, R-2355) | **tenue** |
| 17 | Dossier de sortie neuf ; bacs à sable libres | § 9 | aucune sortie de l'audit dans le dossier ; `/root/bac-audit-fuites-t07-v1/auditeur` et `…/contre-lecteur` absents | **tenue** |

## 2. Commandes jouées par ce préparateur, et sources

### 2.1 Commandes (toutes sur noms, empreintes, lignes ou métadonnées)

1. 11:53Z — lectures du registre par clé exacte (`grep -n '^| CLÉ | ' registres/scellements-v1.md`).
2. Branche du compte 4 : `git fetch origin +refs/heads/lot/compte-4-v1:refs/remotes/origin/lot/compte-4-v1` (tête
   `5a9e456ebb4fcc068edd651712078403a8b8f06c`, inchangée).
3. 11:58:47Z — `git ls-remote origin` sur les trois branches utiles : `calcul/t06-confirmation-7b-v1` = `55c3e3eb…`,
   `donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1` = `c7484c43…`, `donnees/t07-etape-a-v1` = `0c176db5…`.
4. 12:02:44Z → 12:02:46Z — **rapatriement du découpeur** :
   `git fetch --no-tags origin +refs/heads/donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1:refs/remotes/origin/donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1`
   (code 0 ; la référence = `c7484c43657a2ce22d76af33efd06aaa11a6aafa`) ; puis, pour chacun des trois fichiers,
   `git show c7484c43…:donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1/<fichier> | sha256sum` contre la consigne et contre
   `git show c7484c43…:<…>/<fichier>.sha256`.
5. 12:03:09Z — dépôt **sans contenu** de la branche de 7b dans mon bac
   (`git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch calcul/t06-confirmation-7b-v1`, puis
   approfondi à 15 commits) : chaîne des commits `55c3e3eb` ← `1ed396c2` ← `73b32881` ← `cdb070a3` ← `55519daa` (2026-11-12,
   05:09:39Z à 05:17:05Z, absents du clone de la mère) ← **`935262b1`** (2026-11-10T06:26:09Z, présent, ancêtre de `main`) ;
   `git ls-tree -l <tête> -- <chemin exact>` sur les huit chemins du § 3 ; `git show <tête>:<chemin>.sha256` sur les quatre
   compagnons ; **effacé** par son chemin exact à 12:16:06Z.
6. Essai jouet du comparateur des versions du compte 4 sur une racine hors du dépôt : sans lien `src`, code 2 (« interprète :
   échec ») ; avec un lien `src` vers celui du dépôt, il compare (une bibliothèque présente d'un seul côté donne le code 1).
   Jouet effacé.
7. 12:26:38Z → 12:26:46Z — vérificateur et ses essais (§ 2.2).

### 2.2 Vérificateur des conditions (rejouable par la mère, juste avant le lancement : G5)

- `verifier_conditions_audit_fuites_t07_v1.py` (`db7c6c80…`) : quinze familles de contrôles (C1 à C15) sur noms, empreintes et
  lignes ; il hache les entrées de 7b s'il les trouve, ne les ouvre pas, ne liste aucun dossier ; arguments
  `--commit <commit du manifeste>` et `--racine-7b <racine>` (défaut `/root/bac-audit-fuites-t07-v1/racine-7b`) ; code 0 si
  aucun défaut. Sa docstring dit le commit « lu par la mère » : selon D1 (§ 5), il est lu par le sous-agent de G3 et donné à la
  mère.
- `essais_verifier_conditions_audit_fuites_t07_v1.sh` (`ebfd3c3d…`) : un cas sain et huit artefacts sur des dépôts jouets
  (ligne `AUDIT-FUITES-T07` présente ; ligne de consigne en double ; ligne qui cite 7a ; marqueur restant ; `criteres_v1.py`
  modifié ; commit absent ; compagnon faux dans la racine ; entrée de 7b déposée dans l'arbre du dépôt) : **9 conformes sur 9**.
- Sorties brutes des deux : `sorties-verifier-conditions-audit-fuites-t07-v1.txt` (`415eed85…`) : **48 conformes, 0 en
  défaut, 4 « à faire »** (les quatre entrées de 7b, à rapatrier).

### 2.3 Travail du compte 4 sur la préparation de l'audit

Il n'est ni sous `registres-provisoires/` ni sous `docs/` de sa branche (76 fichiers changés sous `registres-provisoires/`,
tous des journaux et passations ; aucun sous `docs/`) mais sous
`brouillons/audit-fuites-t07-preparation-compte4-v1/` de `lot/compte-4-v1`, commit `c48ffff3` : note
`note-trois-conditions-r2359-v1.md` (`9b195262…`), comparateur `comparer-versions-7b-venv-v1.py` (`30e02120…`), essais
(`7718ba85…`) et leur sortie (`1c29c3e0…`), tous égaux à leurs compagnons. Constats repris ici : condition 1 tenable par
recherche ciblée dans P3-bis scellé (`76ab66ce…` = ligne `SCELLEMENT-P3BIS`) et ses trois addendums ; condition 2 tenable au
prix d'un rapatriement (fait, § 1, n° 10) ; condition 3 préparée et éprouvée, non jouée ; liste des commits nécessaires (§ 1,
n° 12). Le comparateur suppose le manifeste sous la racine du dépôt (il importe `controle_ia` depuis `RACINE/src`) : avec la
racine hors du dépôt retenue ici, un lien `src` temporaire suffit (essai jouet, § 2.1, point 6).

## 3. Entrées de 7b : absentes du clone de la mère, à rapatrier de `calcul/t06-confirmation-7b-v1`

Aucun des huit chemins n'existe dans l'arbre ni dans `HEAD` du clone de la mère (contrôle par chemin exact, sans listage). À la
tête `55c3e3eb89a4650419f35999aaa4c54288275b0d` :

| chemin | octets | compagnon (sha256 du fichier) |
|---|---|---|
| `runs/20261111-151701-t06-reel/manifeste.json` | 125 598 | `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` (= ligne `RUN-CONFIRMATION-T06`) |
| `diag/20261111-151701-t06-reel/episodes-t06.json` | 1 556 085 | `c7911933a6cc797db4be094bd252393bb4360cdc55a25867b624be721ccdb51c` |
| `donnees/20261111-151701-t06-reel/textes-actions-t06.jsonl` | 15 438 474 | `d196bb4fffd793dc52190aa2674aeff33619f17bd40d303f564515bde2ad783d` |
| `donnees/20261111-151701-t06-reel/mesures-t06.npz` | 1 830 726 | `aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049` (= sceau vérifié de R-2564) |

Total 18 950 883 octets, plus quatre compagnons de 81 à 91 octets. **Racine retenue : hors du dépôt**,
`/root/bac-audit-fuites-t07-v1/racine-7b/`, aux mêmes chemins relatifs (décision D4, § 5). La branche porte aussi les
activations (≈ 1,06 Go) et les adaptateurs : un `git fetch` ordinaire de la branche dans le clone de la mère les téléchargerait
tous ; d'où le dépôt jetable **sans contenu**, d'où ne sortent que les huit fichiers nommés (précédents : R-2564, bloc A2 de la
commande du compte 3).

**Commande de rapatriement (G1), non exécutée par ce préparateur** — elle extrait les contenus ; le préparateur n'a fait que
la vérifier en syntaxe :

```bash
bash <<'FIN'
set -u
arret() { echo "ARRÊT : $*"; exit 2; }
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
B7B=calcul/t06-confirmation-7b-v1
TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
R6=20261111-151701-t06-reel
BAC=/root/bac-audit-fuites-t07-v1
RACINE_7B=$BAC/racine-7b
JETABLE=$BAC/depot-7b-sans-contenu
[ ! -e "$RACINE_7B" ] || arret "$RACINE_7B existe déjà (R12)"
[ ! -e "$JETABLE" ] || arret "$JETABLE existe déjà"
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" < /dev/null | cut -f1)" = "$TETE_7B" ] || arret "tête de $B7B autre que $TETE_7B"
git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$B7B" "$DEPOT_URL" "$JETABLE" < /dev/null || arret "dépôt jetable"
[ "$(git -C "$JETABLE" rev-parse HEAD)" = "$TETE_7B" ] || arret "tête du dépôt jetable"
while read -r f sha taille; do
  for g in "$f" "$f.sha256"; do
    mkdir -p "$RACINE_7B/$(dirname "$g")"
    git -C "$JETABLE" show "$TETE_7B:$g" < /dev/null > "$RACINE_7B/$g" || arret "extraction de $g"
  done
  [ "$(cut -c1-64 "$RACINE_7B/$f.sha256")" = "$sha" ] || arret "compagnon de $f autre que ${sha:0:12}…"
  (cd "$RACINE_7B/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "empreinte de $f"
  [ "$(stat -c %s "$RACINE_7B/$f")" = "$taille" ] || arret "taille de $f"
  echo "conforme : $f ($taille octets, ${sha:0:12}…)"
done <<LISTE
runs/$R6/manifeste.json 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 125598
diag/$R6/episodes-t06.json c7911933a6cc797db4be094bd252393bb4360cdc55a25867b624be721ccdb51c 1556085
donnees/$R6/textes-actions-t06.jsonl d196bb4fffd793dc52190aa2674aeff33619f17bd40d303f564515bde2ad783d 15438474
donnees/$R6/mesures-t06.npz aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049 1830726
LISTE
rm -rf -- "$JETABLE" && echo "dépôt jetable effacé par son chemin exact"
FIN
# attendu : quatre « conforme », « dépôt jetable effacé », aucun « ARRÊT » ; rien n'est affiché des contenus,
# aucun dossier n'est listé ; le manifeste conforme est égal à la ligne RUN-CONFIRMATION-T06
```

## 4. Gestes, dans l'ordre

**Avant le lancement (G1 à G5).** La mère ne lit rien de 7b hors l'état BA-L2 (R-2741, N-C) : G1 à G3 vont à un **sous-agent
neuf « préparateur des entrées »** (D1), qui ne rend à la mère que des égalités et des empreintes.

- **G1 — rapatriement** : la commande du § 3 (≈ 5 min). Hacher et copier sans lire suffit ; c'est aussi ce que fait plus tard
  la mère avec le fichier d'audit (§ 3 de la consigne).
- **G2 — condition 3 de R-2359 (versions)**, après G1 :

```bash
bash <<'FIN'
set -u
arret() { echo "ARRÊT : $*"; exit 2; }
DEPOT=/home/user/controle-ia-travail; BAC=/root/bac-audit-fuites-t07-v1; P=$BAC/preparateur-entrees
C4=$P/comparer-versions-7b-venv-v1.py; J=$P/versions-7b-venv-v1.json
cd "$DEPOT" || arret "dépôt"; mkdir -p "$P"
git show refs/remotes/origin/lot/compte-4-v1:brouillons/audit-fuites-t07-preparation-compte4-v1/comparer-versions-7b-venv-v1.py < /dev/null > "$C4" || arret "comparateur"
[ "$(sha256sum "$C4" | cut -c1-64)" = 30e0212016ba694a6cbde1b6e77d7ee8ea95ff413379d90cd70ff6df6814a618 ] || arret "empreinte du comparateur"
[ ! -e "$BAC/racine-7b/src" ] || arret "$BAC/racine-7b/src existe déjà"
ln -s "$DEPOT/src" "$BAC/racine-7b/src"
python3 -I "$C4" "$BAC/racine-7b" registres/scellements-v1.md "$DEPOT/.venv/bin/python" < /dev/null > "$J"; code=$?
rm -- "$BAC/racine-7b/src"
echo "code du comparateur : $code (0 : toutes égales ; 1 : au moins une différence ; 2 : garde, rien comparé)"
[ "$code" != 2 ] || arret "garde du comparateur"
python3 -I - "$J" <<'PY'
import json, sys
d = {r["cle"]: r for r in json.load(open(sys.argv[1], encoding="utf-8"))["comparaison"]}
for k in ("transformers", "tokenizers", "python", "numpy"):
    print(f"{k} : {'égal' if d.get(k, {}).get('egal') else 'DIFFÉRENT ou absent'}")
autres = sorted(k for k, r in d.items() if k not in ("transformers", "tokenizers", "python", "numpy", "plateforme") and not r["egal"])
print("autres bibliothèques différentes (noms seuls) :", autres or "aucune")
PY
FIN
```

  Lecture : **décisives** au sens de R-2355 (chemin de décodage) : `transformers` et `tokenizers`, toutes deux « égal » ; sinon
  « arrêt prévu » (R-2355) : la mère ne lance pas et décide. `python`, `numpy` : rapportées. Le code 1 peut venir d'une
  bibliothèque présente sur l'instance de 7b et absente de `.venv` (`peft`, `vllm`, `transformer-lens` ne sont pas dans
  `.venv`) : sans effet sur l'audit, qui n'en importe aucune. Le tableau complet reste dans `$J`, que la mère n'ouvre pas.
- **G3 — commit du manifeste**, après G1 :

```bash
bash <<'FIN'
set -u
DEPOT=/home/user/controle-ia-travail
M=/root/bac-audit-fuites-t07-v1/racine-7b/runs/20261111-151701-t06-reel/manifeste.json
[ "$(sha256sum "$M" | cut -c1-64)" = 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 ] || { echo "ARRÊT : manifeste autre que la ligne"; exit 2; }
C7B=$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["commit"])' "$M" < /dev/null)
echo "commit du manifeste : $C7B ; égal au commit probable 935262b1… : $([ "$C7B" = 935262b17ca95894a882b02f1526ee39d1738652 ] && echo oui || echo NON)"
git -C "$DEPOT" cat-file -e "$C7B^{commit}" < /dev/null && echo "présent dans le clone de la mère" || echo "ABSENT : git -C $DEPOT fetch --no-tags --depth=1 origin $C7B:refs/remotes/origin/audit-fuites/${C7B:0:8}"
FIN
```

- **G4 — la mère consigne** (routine) : condition 1 de R-2359 sans objet (`VERDICT-P3BIS` avant tout lancement ; § 1, n° 9) ;
  conditions 2 et 3 tenues (n° 10 ; résultat de G2) ; racine hors du dépôt (D4) ; qui a joué G1 à G3 (D1).
- **G5 — la mère rejoue le vérificateur** avec le commit rendu par G3 :
  `python3 -I docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/verifier_conditions_audit_fuites_t07_v1.py /home/user/controle-ia-travail --commit <commit>`
  (depuis n'importe quel dossier) : **attendu 0 en défaut et 0 « à faire »** ; sinon, pas de lancement.

**Lancement et suite (G6 à G9).**

- **G6 — lancer l'auditeur** : sous-agent neuf du **modèle C** (jamais A, que le § 3 exclut ; jamais B avant le 20 novembre
  15:00 UTC), avec `consigne-lancement-auditeur-v2.md` **telle quelle**, après
  `(cd docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1 && sha256sum -c consigne-lancement-auditeur-v2.md.sha256)`.
- **G7 — au retour de l'auditeur** : sceaux de ses sorties (`sha256sum -c`), absence de `rapport-arret-v1.md` ; choix du modèle du
  contre-lecteur (D2) ; lancement d'un sous-agent neuf avec `consigne-contre-lecteur-audit-v2.md` telle quelle.
- **G8 — contre-lecture « conforme »** : copie octet pour octet de `audit-fuites-t07.json` et de son compagnon vers
  `diag/20261114-001352-t07-lecture-reel/` (réglage Q6 ; même sha256), ligne `AUDIT-FUITES-T07` (chemin de la copie, son
  sha256 ; strictement après la ligne 9), commit, poussée — au moment que fixe la réserve R6 (cloisonnement). « En échec » :
  aucune ligne ; la mère décide.
- **G9 — liste « qui a lu quoi »** : l'auditeur et le contre-lecteur (lectures : textes et mesures de 7b ; exclusions Q8 :
  lecteur de P3-bis, contre-lecteur de T0.7, verdict de G0 ; par prudence aussi développeur de la pièce « mots et coût » et
  rédacteur de l'étape B bis, R6) ; le sous-agent de G1 à G3 (manifeste : champs `versions` et `commit` ; aucun texte) ; ce
  préparateur (lectures du § « Lu » ci-dessus ; aucune donnée).

## 5. Décisions pour la mère (routine)

- **D1 — qui joue G1 à G3.** Enjeu : la mère ne lit rien de 7b hors BA-L2 (R-2741) ; G2 et G3 lisent deux champs du manifeste.
  (a) un sous-agent neuf « préparateur des entrées » (modèle A ou C), qui rend des égalités et le commit : rien de 7b sous les
  yeux de la mère ; un agent de plus à inscrire en G9. (b) la mère, sur un mot de Lazar étendant l'exception N-C aux champs
  `versions` et `commit` : plus court, mais un mot à obtenir. (c) lever la condition 3 de R-2359 et s'en remettre au contrôle de
  décodage de l'auditeur (§ 6.1 ; « autre version → arrêt prévu ») : un arrêt possible en cours d'audit. **Recommandation : (a)**,
  confiance 0,7.
- **D2 — modèle du contre-lecteur du fichier.** Enjeu : R2 veut un sous-agent neuf ; la consigne ne fixe pas son modèle ;
  l'auteur du fichier (l'auditeur) est en C ; B est indisponible jusqu'au 20 novembre 15:00 UTC. (a) **modèle A** : autre
  modèle que l'auteur du fichier, comme la ligne `CONSIGNE-AUDIT-FUITES-T07` l'exige pour la consigne (N-052) ; le § 3 n'exclut
  du rôle que des agents, pas le modèle A ; inconvénient : même modèle que les auteurs de la consigne. (b) **modèle C** : R-2718
  range les contre-lectures en C ; inconvénient : même modèle que l'auteur du fichier (réserve de lignée, précédent R-2441).
  (c) attendre B : ligne `AUDIT-FUITES-T07` au plus tôt le 20 novembre, après la date visée de l'étape B (mardi 17, R-2734).
  **Recommandation : (a)**, confiance 0,6. La consigne du contre-lecteur accepte A ou C (il note sa lettre).
- **D3 — ce que la mère reçoit des agents.** Enjeu : la règle 8 de l'annexe A demande « verdict en une ligne » ; R-2741 exclut la
  mère de toute lecture de 7b, et la phrase gelée du § 11 (jeu, trait, comptes, séparation) en est une par procuration ; la
  consigne de l'audit ne demande à la mère que de lancer, copier et inscrire. (a) **v2** des deux consignes : messages limités au
  déroulement (« terminé, validé, scellé » ou « arrêté » ; « conforme » ou « en échec » et sa catégorie), le détail restant dans
  les fichiers, que lisent le contre-lecteur puis l'étape B. (b) v1 : la mère reçoit la phrase du § 11 et le verdict détaillé du
  contre-lecteur. **Recommandation : (a)**, confiance 0,75. Les v1 restent scellées, inchangées (R12) ; elles diffèrent des v2 par
  ce seul point de fond (plus le titre, la puce de version, le nom du compagnon contrôlé et le renvoi entre elles).
- **D4 — où vivent les entrées de 7b.** (a) **racine hors du dépôt**, `/root/bac-audit-fuites-t07-v1/racine-7b/` : rien de 7b dans
  l'arbre de travail partagé par les autres sous-agents de la mère (dont le futur développeur de la pièce « mots et coût », qui
  ne doit rien voir de 7b, T0.6 l. 765, CL3-01) ; rien à committer par mégarde (`runs/` et `diag/` ne sont pas ignorés par git) ;
  le § 7 de la consigne passe tous les chemins en argument. (b) chemins du dépôt (`runs/…`, `diag/…`, `donnees/…`) : lecture la
  plus littérale du § 5.1 ; comparateur sans lien `src` ; mais 7b dans l'arbre partagé. **Recommandation : (a)**, confiance 0,7 ;
  les deux consignes v1 et v2 sont écrites pour (a).

## 6. Réserves

- **R1 — commit du manifeste : probable, non lu.** `935262b1` est la base de la branche de 7b (métadonnées), donc le commit le
  plus probable du manifeste ; le champ `commit` fait foi (G3, puis préalable 2 de l'auditeur). S'il diffère et manque au clone,
  G3 donne la commande de rapatriement par empreinte ; s'il diffère, C10 et C11 sont rejoués par G5 contre lui.
- **R2 — § 5.1, point 6, « les cinq premiers ».** La liste nomme quatre modules pour le commit du manifeste puis `7a54d431` pour
  `statistiques.py` : la consigne de lancement fait appliquer la désignation nommée et noter au journal l'empreinte au commit du
  manifeste ; elle est égale partout (`a8552575…` à `7a54d431`, `1609a4bf`, au commit probable et dans l'arbre) : sans effet ici.
- **R3 — `CODE-T07-v3.json` et non v2.** Le § 5.1 cite la v2 « le 11 novembre » ; la règle est « le fichier que cite la ligne » :
  v3 (`d3eaebfe…`, commit `c2fab6cc`), où `criteres_v1.py` garde l'empreinte de la consigne (`12b999fe…`).
- **R4 — réglages d'exécution ajoutés** (consignes, § 2) : `PYTHONDONTWRITEBYTECODE=1` (le § 9 interdit d'écrire ailleurs que
  dans le dossier de sortie ; un import depuis `src/` y écrirait des `__pycache__`), `HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`,
  `HF_HOME` et `TMPDIR` dans le bac à sable (§ 5.2 : aucun téléchargement). Ils ne changent ni la commande du § 7 ni un calcul.
- **R5 — rejeu octet pour octet** (§ 3) : la consigne de lancement demande des sorties indépendantes du dossier, de l'heure et de
  l'ordre des parcours ; et, pour l'essai 17, un commit absent passé en argument plutôt qu'un dépôt jouet à commits (règle 4).
- **R6 — cloisonnement des sorties de l'audit.** La table des candidats, le fichier et le rapport portent des comptes d'actions de
  7b par condition pour des suites de mots : une vue des textes de 7b dans la dimension « mots ». Le code de la pièce « mots et
  coût » s'écrit sans vue des résultats de 7b (T0.6 l. 765 ; CL3-01 retenu, R-2735) et le plan de l'étape B bis sans résultat lu
  (R-2730). Recommandation : `/root/bac-audit-fuites-t07-v1/` et les sorties de l'auditeur dans ce dossier (hors les pièces de
  préparation) dans la liste des chemins interdits de ces agents ; sorties de l'audit non committées avant la ligne
  `CODE-MOTS-ET-COUT-T06` et le scellement du plan de B bis (l'étape B attend aussi `ISSUE-MOTS-ET-COUT-T06` : l'ordre tient).
- **R7 — rien ne bouge pendant l'audit.** Entre G6 et la fin de la contre-lecture : ni les sept modules importés, ni la ligne
  `CODE-T07`, ni les lignes lues du registre, ni la racine de 7b ; sinon le rejeu peut différer ou `prealables` s'arrêter.
- **R8 — clone éphémère.** Le clone de la mère est superficiel ; si son conteneur est remplacé, le commit du découpeur manque de
  nouveau : refaire le `fetch` du § 2.1, point 4, avant G6 (le vérificateur le dit : C8).
- **R9 — consigne de lancement et P3-bis.** Ce préparateur n'a pas relu P3-bis (le constat n° 9 repose sur `VERDICT-P3BIS` et sur
  la recherche du compte 4) ; la consigne attribue cette vérification à la mère.
- **R10 — fichiers de ce dossier.** Les pièces de préparation (ce texte, les quatre consignes, le vérificateur, ses essais et leur
  sortie) partagent le dossier de sortie de l'auditeur ; elles ne portent aucune donnée de 7b (noms, tailles, empreintes) ; les
  consignes disent à l'auditeur et au contre-lecteur de ne lire que leurs propres pièces.
- **R11 — chemins nommés dans la demande.** La demande situait le travail du compte 4 sous `registres-provisoires/` et `docs/` :
  il est sous `brouillons/` (§ 2.3) ; ses journaux n'ont pas été lus.

## 7. Ce qui empêcherait de lancer l'audit aujourd'hui

- **Rien côté registre, consigne, T0.7, commits, découpeur ni interprète** : tout est conforme (§ 1).
- **Bloque tant que ce n'est pas fait** : G1 (entrées de 7b absentes du clone), G2 (condition 3 de R-2359), G3 et G5 ; avec D1,
  un sous-agent de plus à lancer ; ≈ 20 minutes au total.
- **Bloquerait** : `transformers` ou `tokenizers` du manifeste ≠ 5.18.0 ou 0.23.2 (R-2355 : arrêt prévu ; nœud avant tout
  lancement) ; commit du manifeste absent et non rapatriable ; modèle C indisponible ; refus d'un classifieur à la lecture des
  textes de 7b (l'auditeur s'arrête et le rapporte) ; conteneur remplacé sans nouveau `fetch` du découpeur (R8).
- **Délai** : lancé avant 14:00 UTC, audit et contre-lecture tiennent dans la journée ; l'audit n'est pas sur le chemin critique de
  l'étape B (mardi 17 au plus tôt, R-2734), mais doit précéder son exécution.

## 8. Pièces de ce dossier et empreintes

Dossier : `docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/` (celui que nomme le § 9 de la consigne). Toutes scellées
(compagnon `.sha256`), aucune committée.

| pièce | sha256 |
|---|---|
| `consigne-lancement-auditeur-v2.md` — **à donner** (G6) | `2d58bd8bb9e2186113b343c0326d02cf14ba709676c437ea6d2af43abb1ef7b0` |
| `consigne-contre-lecteur-audit-v2.md` — **à donner** (G7) | `590716ab1b35451e2b9a834e5166bcaff7f4bb16b0bfb617e06150daabb6f5f4` |
| `consigne-lancement-auditeur-v1.md` — gardée (R12 ; option D3 (b)) | `11872d57af26de80236ab3c9c0a43af364a3c773b5e5f9cf6db2b8116df07e88` |
| `consigne-contre-lecteur-audit-v1.md` — gardée (R12 ; option D3 (b)) | `9094a48a50987b01a6bfe36659758bc64ad852088a380ab5317d2a7a47653791` |
| `verifier_conditions_audit_fuites_t07_v1.py` | `db7c6c8060376cde1962908a4a5df78ca2c7bb9df7c6a0ead6a83bc0b84d9599` |
| `essais_verifier_conditions_audit_fuites_t07_v1.sh` | `ebfd3c3d3950829aad0d86330a4c707e78a52f8134297b4f7f855f38716a2d1e` |
| `sorties-verifier-conditions-audit-fuites-t07-v1.txt` | `415eed8581e6d716da1bc06a5f885b6555af38d438950b7148a62a0fe22dea4a` |
| `preparation-lancement-v1.md` — ce texte | son compagnon |

Hors du dépôt : rien de durable (le dépôt sans contenu, les jouets et le vérificateur de travail de mon bac sont effacés ou
sans usage). Dans le clone de la mère : deux références ajoutées par `fetch` à refspec explicite,
`refs/remotes/origin/donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1` (nouvelle) et
`refs/remotes/origin/lot/compte-4-v1` (déjà présente, inchangée).
