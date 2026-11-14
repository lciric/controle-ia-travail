# Commande de la mère au compte 3 — phase A : lecteur du verdict de la table A de T0.6 sur 7b — v2

- **Statut** : commande écrite de la session mère au compte 3 (mot de Lazar R-2711 (2) : « hôte des lecteurs de 7b et de l'étape B :
  une session neuve du compte 3 »). À coller par Lazar comme **premier message d'une session neuve du compte 3, ouverte dans le
  dossier du dépôt**. Aucune dépense, aucun texte scellé changé, aucun critère ajouté ; si elle contredit T0.6 scellé, le texte fait
  foi : tu t'arrêtes et tu le dis. **Remettable seule** : la phase C fait l'objet d'une commande à part
  (`commande-compte-3-phase-c-v2.md`, même dossier), jouée plus tard dans **cette même session**.
- **Version 2** : la version 1 (`commande-compte-3-v1.md`, `21d891c5…`, gardée, R12) corrigée selon sa contre-lecture
  (`contre-lecture-commande-compte-3-v1.md`, `092acef6…`, modèle C, R-2735 : phase A « remettable après corrections ») ; constats
  appliqués à la phase A : CL3-01 (décision de la mère), CL3-02, CL3-03, CL3-07 (répétition), CL3-11, CL3-12, CL3-13, CL3-15,
  CL3-16, CL3-17, CL3-18, CL3-21 (traitement de chacun : `rapport-preparateur-v2.md`). **Décisions de Lazar portées** (R-2741) : N-A
  (a) pas d'extracteur, le lecteur lit lui-même les fichiers de service ; N-B (a) un seul agent lit et prononce ; N-D le lot NARCBench
  continue en parallèle sans rien ouvrir de T0.7, 7a ou 7b avant les verdicts ; N-E lecture sans attendre la grille de G0.
- **Rédacteur** : le préparateur de la v1 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, modèle A), le 2026-11-14
  à partir de 12:07:52Z (`date -u`) ; ni lecteur ni juge d'aucun verdict ; aucune sortie de 7a, 7b ou T0.7 ouverte.
- **Pièces** (même dossier `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, chacune scellée) :

| pièce | empreinte | rôle |
|---|---|---|
| `attestation_qui_a_lu_quoi_compte_3_v2.py` | `be9dc21357eba7a736a0466adc5835e5ef68a48466b71f860fc3ff7cf6744047` | attestation par identifiant de session, préfixe compris (bloc 2) |
| `essai_attestation_compte_3_v2.sh`, sortie `essai-attestation-compte-3-v2-sortie-v1.txt` | `22b76f4f…`, `b2e14b4a…` | essai R5 : 12 conformes sur 12 |
| `repetition_phase_a_jouet_v2.sh`, sortie `repetition-phase-a-jouet-sortie-v2.txt` | voir le rapport v2 | répétition de bout en bout des blocs de cette commande sur dépôts jouets |

## 0. D'abord, pour Lazar et la mère

1. **Voie d'écriture** : une branche neuve `verdict/t06-table-a-7b-compte-3-v1`, créée sur `main`, poussée par refspec ; jamais `main`.
   Le verdict y reste : **il n'entre dans `main` qu'après l'inscription de la ligne `CODE-MOTS-ET-COUT-T06`** (décision de la mère sur
   CL3-01, R-2735 : T0.6 scellé, l. 765, veut le code de la pièce « mots et coût » écrit et contre-lu sans vue d'aucun résultat de 7b).
2. **Préalables de la remise** (mère) : liste « qui a lu quoi » **v2** scellée, qui donne l'identifiant de la session du lot du compte 3
   si elle existe ; consigne scellée du lecteur A (format fermé du rapport, noms permis des fichiers du verdict sans archive, aucun
   nombre ni issue hors des fichiers scellés du verdict, fichier du message reçu) ; **tout poussé sur `main` avant l'ouverture de la
   session** (CL3-17) ; lignes R de N-B (un seul agent) et de CL3-01 inscrites.
3. **Ce que la commande évite** : l'extracteur (N-A) ; `resume.json` de 7b (il porte `ligne_B`, `ligne_C`) ; toute ligne du registre des
   décisions dans les pièces du lecteur (CL3-03 : la ligne R-2704 portait des nombres de P3-bis et des mentions de T0.7) ; tout repli sur
   le modèle A pour le lecteur (CL3-11 : faute du modèle C, arrêt et nœud).
4. **Irréversible** : le nom de la branche (éprouvé par une poussée de la branche égale à `main` avant tout) ; la remise des pièces au
   lecteur (précédée du bordereau, d'un filtre de noms et d'un filtre de contenu).

## 1. Interdits permanents

Recopiés du brief du compte 3, section 6 (à recopier en tête de toute consigne de sous-agent) :

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`,
  `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a, l'étiqueteur,
  `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (variable `SECRETS` du bloc 1).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ;
  aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Exception unique, accordée par R-2711 (2)** : les fichiers de 7b nommés au bloc A2 (branche `calcul/t06-confirmation-7b-v1`) sont
récupérés dans un dépôt jetable sans contenu, puis extraits par liste positive (`git show <tête>:<chemin>`), pour le seul lecteur A.

**Interdits ajoutés** :
- **Tu n'ouvres aucun résultat** : tu copies, hashes et compares ; tu lis seulement les noms, les compagnons, les fichiers
  `empreintes.sha256` des traces (noms et empreintes) et le rapport final du lecteur.
- Jamais `resume.json`, `lecture-sondes-t06.json`, les activations ni les adaptateurs de 7b ; jamais une ligne de
  `registres/decisions.md` dans les pièces du lecteur.
- **Exclusions de cette session (CL3-02, Q11)** : elle est neuve et distincte de toute session du lot du brief du compte 3 ; elle
  n'exécute aucune tâche de ce lot ; elle est ensuite exclue de l'analyse du verdict A, de la conception et des verdicts de l'étape B
  bis, de T0.8 et de G0, **de la rédaction, de la contre-lecture et de la course du préenregistrement NARCBench (bras descriptif de
  T0.7), des brouillons des papiers B et C**, et de l'écriture comme de la contre-lecture du code de la pièce « mots et coût ».
- Aucune poussée hors de `verdict/t06-table-a-7b-compte-3-v1` ; jamais `main`, `lot/compte-3-v1` ni `lciric/controle-ia`.

## 2. Qui fait quoi

- **Toi, la session hôte** : blocs dans l'ordre ; extraction par liste positive ; remise ; copie, sceaux, commit, poussée ; rendu.
- **Le lecteur A** : **un seul** sous-agent neuf, qui lit la table A dans l'ordre du point 7 du plan de T0.6 et prononce le verdict
  (décision de Lazar R-2741, N-B (a) ; l'ordre de 7b, l. 374, nommait deux rôles : écart tranché). Il est du **modèle C**, nommé par Lazar
  en conversation ; si ton outil d'agent ne peut pas créer un sous-agent du modèle C : **arrêt, nœud de Lazar** (aucun repli). Sans
  contexte hérité ; il ne lit que sa consigne et les pièces de son espace ; il n'écrit que dans `verdict-ferme/`.
- **La mère** : marqueurs, liste v2, consigne A ; garde le verdict hors de `main` jusqu'à `CODE-MOTS-ET-COUT-T06` (section 15).

## 3. Marqueurs

| marqueur | qui, quand | où |
|---|---|---|
| chemin et empreinte de la version remise de cette commande | Lazar, en conversation ; le bloc 0b les imprime, tu compares | bloc 0b |
| `<<LISTE>>`, `<<EMPREINTE_LISTE>>` | la mère : liste « qui a lu quoi » v2 scellée (en-tête « session », « compte », « exclu de ») | bloc 1 |
| `<<CONSIGNE_LECTEUR_A>>`, `<<EMPREINTE_CONSIGNE_LECTEUR_A>>` | la mère : consigne scellée du lecteur A, chemin relatif à la racine | bloc 1 |
| `<<ESPACE>>`, `<<EMPREINTE_BORDEREAU>>`, `<<PY>>`, `<<NOTE_MODELE>>`, `<<CONSIGNE>>`, `<<EMPREINTE_CONSIGNE>>` | toi, par programme (bloc A4) ; arrêt s'il en reste un | bloc A4 |

## 4. Mode d'emploi

- **Avant l'ouverture de la session**, la mère a poussé sur `main` la liste v2, la consigne A et la version remise de cette commande.
- Chaque bloc se lance tel quel, dans un seul appel de ton outil de commande, dans l'ordre ; chaque bloc relit
  `$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh`. Une ligne « ARRÊT : » : tu t'arrêtes et tu suis la section 14.
- Bloc A2 au délai maximal de ton outil. Au-dessus de 80 % de quota, tu ne commences pas le bloc A4.
- Les commentaires « attendu : » disent la sortie conforme ; toute autre sortie est un arrêt.

## 5. Bloc 0 — aptitude (appels séparés) et bloc 0b — copie locale à jour

```bash
sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py
# attendu : appel BLOQUÉ par le crochet de garde. S'il passe : dis-le en tête de ton premier message à Lazar.
```

```bash
for k in GH_TOKEN GITHUB_TOKEN HCLOUD_TOKEN VAST_API_KEY ANTHROPIC_API_KEY OPENAI_API_KEY HF_TOKEN; do
    [ -n "${!k+x}" ] && echo "$k : présente" || echo "$k : absente"; done      # noms seulement, jamais une valeur
df -h "$HOME" . | sed -n '1,3p'; nproc; date -u +%Y-%m-%dT%H:%M:%SZ
# attendu : la liste des noms ; au moins 1 Gio libre. Dis aussi à Lazar le modèle de ta session, ton quota, et que ce message est le
# premier de cette session (session neuve, Q11).
```

```bash
cd "$(git rev-parse --show-toplevel)" || exit 1
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "ARRÊT : modifications suivies dans ton dépôt"; exit 1; }
git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || { echo "ARRÊT : récupération de main"; exit 1; }
[ "$(git rev-parse --abbrev-ref HEAD)" = main ] || git switch -q main || { echo "ARRÊT : passage sur main"; exit 1; }
git merge -q --ff-only refs/remotes/origin/main || { echo "ARRÊT : main local non avançable en avance rapide"; exit 1; }
echo "main local : $(git rev-parse HEAD)"
sha256sum docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-a-v2.md
# attendu : main local égal au distant ; l'empreinte imprimée est celle que Lazar t'a donnée en conversation (sinon arrêt)
```

## 6. Bloc 1 — variables (une seule fois)

```bash
export LC_ALL=C.UTF-8
arret() { echo "ARRÊT : $*"; exit 1; }
date -u +"début : %Y-%m-%dT%H:%M:%SZ"
DEPOT=$(git rev-parse --show-toplevel) || arret "lance ce bloc depuis le dossier du dépôt"
case "$(git -C "$DEPOT" remote get-url origin)" in
  *lciric/controle-ia-travail*) echo "dépôt : $DEPOT (lciric/controle-ia-travail)";;
  *) arret "le dépôt d'origine n'est pas lciric/controle-ia-travail";; esac
BAC="$HOME/bac-lecture-7b-compte-3-v2"                 # hors de tout arbre git ; neuf (R12)
[ ! -e "$BAC" ] || arret "$BAC existe déjà : rapport à la mère"
git -C "$HOME" rev-parse --show-toplevel >/dev/null 2>&1 && arret "$HOME est dans un arbre git"
SESSION_C3="session_${CLAUDE_CODE_REMOTE_SESSION_ID#cse_}"
[[ "$SESSION_C3" =~ ^session_[0-9A-Za-z]{10,}$ ]] || arret "identifiant de session introuvable (section 14)"
LISTE='<<LISTE>>'; EMPREINTE_LISTE='<<EMPREINTE_LISTE>>'
CONSIGNE_A='<<CONSIGNE_LECTEUR_A>>'; EMPREINTE_CONSIGNE_A='<<EMPREINTE_CONSIGNE_LECTEUR_A>>'
case "$LISTE $EMPREINTE_LISTE $CONSIGNE_A $EMPREINTE_CONSIGNE_A" in *'<<'*) arret "marqueur non rempli (la mère)";; esac
mkdir -p "$BAC" && date -u +%Y-%m-%dT%H:%M:%SZ > "$BAC/debut-v2.txt"
if "$DEPOT/.venv/bin/python" -c 'import numpy' 2>/dev/null; then PY="$DEPOT/.venv/bin/python"
else python3 -m venv "$BAC/venv-a-v2" && "$BAC/venv-a-v2/bin/pip" install -q --disable-pip-version-check numpy==2.4.6 \
     && PY="$BAC/venv-a-v2/bin/python" || arret "interpréteur"; fi
"$PY" -c 'import numpy, sys; print("interpréteur :", sys.executable, sys.version.split()[0], "numpy", numpy.__version__)' || arret "interpréteur sans numpy"
cat > "$BAC/variables-v2.sh" <<EOF
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
arret() { echo "ARRÊT : \$*"; exit 1; }
DEPOT='$DEPOT'; BAC='$BAC'; PY='$PY'; SESSION_C3='$SESSION_C3'
LISTE='$LISTE'; EMPREINTE_LISTE='$EMPREINTE_LISTE'; CONSIGNE_A='$CONSIGNE_A'; EMPREINTE_CONSIGNE_A='$EMPREINTE_CONSIGNE_A'
ICI="\$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1"
R6=20261111-151701-t06-reel; TR6=t06-20261112-051655-1Xzh; TRC6=consignation-20261112-051705-vUfJ
B7B=calcul/t06-confirmation-7b-v1; TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
BR_A=verdict/t06-table-a-7b-compte-3-v1; DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
H_MANIF_7B=7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6
LIGNE_RUN6='| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/20261111-151701-t06-reel/manifeste.json | 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 |'
LIGNE_VP3='| VERDICT-P3BIS | 2026-11-14T10:30:38Z | docs/verdicts/verdict-P3-bis-v1-issue.json | c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 |'
H_T06=ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169; H_CFG7B=b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527
H_ATTESTATION=be9dc21357eba7a736a0466adc5835e5ef68a48466b71f860fc3ff7cf6744047
ESPACE_A="\$BAC/espace-table-a-v2"; CLONE7B="\$BAC/clone-7b-v2"; NOTE_MODELE="modèle C"
SECRETS='(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'
INTERDITS_NOMS='lecture-sondes|resume\.json|activations|adaptateur|t07|t0\.7|bbis|b-bis|bras-attaque|mode-tenu|anteriorite-bras|etiqueteur|quarantaine|mesure-unanime'
INTERDITS_CONTENU='t07|t0\.7|scores|sondes|p3-?bis|bbis|b-bis|étape b bis|bras-attaque|mode-tenu'
EOF
echo "session : $SESSION_C3 ; variables : $BAC/variables-v2.sh"
# attendu : dépôt, interpréteur avec numpy, session « session_… » ; aucun « ARRÊT »
```

## 7. Bloc 2 — contrôles d'entrée, attestation, nouveauté de la session

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
date -u +%Y-%m-%dT%H:%M:%SZ
D=$(curl -sS --max-time 20 -D - -o /dev/null https://pypi.org/simple/numpy/ 2>/dev/null | tr -d '\r' | awk -F': ' 'tolower($1)=="date"{print $2}' | tail -1)
[ -n "$D" ] || arret "horloge de référence (en-tête Date de pypi.org) injoignable"
E=$(( $(date -u +%s) - $(date -u -d "$D" +%s) )); echo "écart de l'horloge à pypi.org : $E s"; [ "${E#-}" -le 120 ] || arret "horloge décalée de plus de 120 s"
(cd "$DEPOT/docs" && sha256sum -c --quiet sha256sums-lancement-v2.txt) && echo "empreintes de lancement conformes" || arret "empreintes de lancement"
[ "$(sha256sum "$ICI/attestation_qui_a_lu_quoi_compte_3_v2.py" | cut -d' ' -f1)" = "$H_ATTESTATION" ] && echo "attestation v2 : pièce conforme" || arret "pièce de l'attestation"
python3 -I -B "$ICI/attestation_qui_a_lu_quoi_compte_3_v2.py" "$DEPOT/$LISTE" "$EMPREINTE_LISTE" "$SESSION_C3" \
    || arret "attestation « qui a lu quoi » non conforme : rien n'est lancé ; la mère tranche"
cd "$DEPOT"
[ -z "$(git branch --list 'lot/compte-3-v1')" ] || arret "branche locale lot/compte-3-v1 : cette session n'est pas neuve ; la mère tranche"
[ "$(ls registres-provisoires/compte-3-* 2>/dev/null | wc -l)" = 0 ] || arret "journaux provisoires du lot du compte 3 dans ta copie ; la mère tranche"
[ -n "$(git config user.name)" ] && [ -n "$(git config user.email)" ] || arret "identité git (user.name, user.email) absente"
[ -z "$(git status --porcelain --untracked-files=no)" ] || arret "modifications suivies dans ton dépôt"
echo "session neuve : aucune trace locale du lot du compte 3"
# attendu : écart ≤ 120 s ; empreintes de lancement ; pièce conforme ; « ATTESTATION : CONFORME — … » ; « session neuve … » ; aucun « ARRÊT »
```

## 8. Phase A — table A de T0.6 sur 7b

### Bloc A1 — branche neuve, lignes de registre, pièces de main, poussée éprouvée

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
cd "$DEPOT"
[ -z "$(git ls-remote origin "refs/heads/$BR_A")" ] || arret "la branche $BR_A existe déjà au distant (R12)"
if [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_A" ] && [ -e "$BAC/c-main-a-v2.txt" ]; then echo "branche $BR_A déjà créée (bloc relancé)"
else git switch -q --no-track -c "$BR_A" refs/remotes/origin/main || arret "création de $BR_A"; git rev-parse HEAD > "$BAC/c-main-a-v2.txt"; fi
R=registres/scellements-v1.md
for L in "$LIGNE_RUN6" "$LIGNE_VP3"; do [ "$(grep -cxF -- "$L" "$R")" = 1 ] && echo "conforme :$(echo "$L" | cut -d'|' -f2)" \
    || arret "ligne absente, autre ou en double dans $R :$(echo "$L" | cut -d'|' -f2)"; done
sha256sum -c <<FIN || arret "pièces de main"
$H_T06  prereg/T0.6-organismes-v0-v1.md
$H_CFG7B  prereg/T0.6-organismes-config-7b-v1.json
$EMPREINTE_CONSIGNE_A  $CONSIGNE_A
FIN
for f in prereg/T0.6-organismes-v0-v1.md prereg/T0.6-organismes-config-7b-v1.json "$CONSIGNE_A"; do
    [ "$(cut -d' ' -f1 "$f.sha256")" = "$(sha256sum "$f" | cut -d' ' -f1)" ] || arret "compagnon de $f"; done
[ "$(ls docs/verdicts/verdict-T0.6-table-A-7b-v1* 2>/dev/null | wc -l)" = 0 ] || arret "fichiers du verdict de la table A déjà présents"
git push -q origin "refs/heads/$BR_A:refs/heads/$BR_A" && echo "branche poussée (égale à main) : $(git ls-remote origin "refs/heads/$BR_A" | cut -c1-12)" \
    || arret "poussée refusée : rapport à la mère"
# attendu : deux « conforme » ; trois « OK » ; compagnons égaux ; « branche poussée » ; aucun « ARRÊT »
```

### Bloc A2 — dépôt jetable de la branche de 7b, extraction par liste positive (délai maximal)

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$ESPACE_A" ] || arret "$ESPACE_A existe déjà"
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" | cut -f1)" = "$TETE_7B" ] || arret "tête de $B7B autre que $TETE_7B : rapport à la mère"
[ -e "$CLONE7B" ] || git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$B7B" "$DEPOT_URL" "$CLONE7B" || arret "dépôt jetable sans contenu"
[ "$(git -C "$CLONE7B" rev-parse HEAD)" = "$TETE_7B" ] || arret "tête du dépôt jetable"
P="$ESPACE_A/pieces"; mkdir -p "$P" "$ESPACE_A/verdict-ferme"
ext() { mkdir -p "$P/$(dirname "$1")"; git -C "$CLONE7B" show "$TETE_7B:$1" > "$P/$1" || arret "extraction de $1"; }
for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json diag/$R6/distillation-t06.json runs/$R6/manifeste.json \
         donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do
    ext "$f"; ext "$f.sha256"; (cd "$P/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
# traces : noms attendus exactement (relevés au distant, tête 55c3e3eb) ; « 11 traces » de R-2413 = 9 + 2 fichiers listés par les deux empreintes.sha256
T1="empreintes.sha256 journal.txt nvidia-smi.txt pip-freeze.txt progres-retenues.txt run.err run.json t06-minuterie.log tests.err tests.txt"
T2="empreintes.sha256 journal-consignation.txt t06-minuterie-fin.txt"
[ "$(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "traces/$TR6/" | sed 's#.*/##' | sort | tr '\n' ' ')" = "$(echo $T1 | tr ' ' '\n' | sort | tr '\n' ' ')" ] || arret "traces/$TR6 : noms autres qu'attendus"
[ "$(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "traces/$TRC6/" | sed 's#.*/##' | sort | tr '\n' ' ')" = "$(echo $T2 | tr ' ' '\n' | sort | tr '\n' ' ')" ] || arret "traces/$TRC6 : noms autres qu'attendus"
for g in $T1; do ext "traces/$TR6/$g"; done; for g in $T2; do ext "traces/$TRC6/$g"; done
n1=$(cd "$P/traces/$TR6" && sha256sum -c empreintes.sha256 2>&1 | grep -c ': OK$'); n2=$(cd "$P/traces/$TRC6" && sha256sum -c empreintes.sha256 2>&1 | grep -c ': OK$')
[ "$n1" = "$(wc -l < "$P/traces/$TR6/empreintes.sha256")" ] && [ "$n2" = "$(wc -l < "$P/traces/$TRC6/empreintes.sha256")" ] && [ $((n1 + n2)) = 11 ] \
    && echo "traces : $n1 + $n2 = 11 fichiers à leur empreinte (R-2413 : « 11 traces »)" || arret "traces : $n1 + $n2 fichiers conformes, 11 attendus"
[ "$(sha256sum "$P/runs/$R6/manifeste.json" | cut -d' ' -f1)" = "$H_MANIF_7B" ] && echo "manifeste de 7b égal à la ligne RUN-CONFIRMATION-T06" || arret "manifeste de 7b autre que la ligne"
{ echo "# Constat de l'hôte (compte 3), comptes de noms seulement, $(date -u +%Y-%m-%dT%H:%M:%SZ), tête $TETE_7B"
  echo "fichiers du dossier diag du run : $(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/" | grep -c .)"
  echo "résumé du run (resume.json) : $(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/resume.json" | grep -c .) (1 = présent ; non remis)"
  echo "arrêt du run (arret.json) : $(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/arret.json" | grep -c .) (0 = absent)"
} > "$P/constat-noms-7b-v2.txt"
n=$(cd "$P" && find . -type f | grep -c -i -E 'lecture-sondes|resume\.json|activations|adaptateur|bras-attaque|mode-tenu|etiqueteur|quarantaine|mesure-unanime')
[ "$n" = 0 ] && echo "aucun nom interdit parmi les fichiers extraits" || arret "$n nom(s) interdit(s) extraits : rien n'est remis ; rapport à la mère"
echo "extraits : $(cd "$P" && find . -type f | wc -l) fichiers, $(du -sb "$P" | cut -f1) octets"
# attendu : compagnons « OK » (silencieux) ; « traces : 9 + 2 = 11 … » ; « manifeste de 7b égal … » ; « aucun nom interdit » ;
# 26 fichiers, ≈ 19 000 000 octets ; aucun « ARRÊT »
```

### Bloc A3 — pièces du lecteur A, filtres de noms et de contenu, bordereau

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
P="$ESPACE_A/pieces"; cd "$DEPOT"
[ ! -e "$ESPACE_A/bordereau-remise-v2.txt" ] || arret "bordereau déjà écrit : bloc déjà joué"
for f in prereg/T0.6-organismes-v0-v1.md prereg/T0.6-organismes-config-7b-v1.json "$CONSIGNE_A"; do cp --parents "$f" "$f.sha256" "$P/" || arret "copie de $f"; done
C=$(cat "$BAC/c-main-a-v2.txt")
{ echo "# Extrait des registres pour le lecteur de la table A (v2)"; echo; echo "Commit de main : $C. Ligne recopiée telle quelle."; echo
  echo "## registres/scellements-v1.md"; git show "$C:registres/scellements-v1.md" | grep -n -F -- "$LIGNE_RUN6"; } > "$P/extrait-registres-table-a-v2.md"
[ "$(grep -c -E '^[0-9]+:\| RUN-CONFIRMATION-T06 \|' "$P/extrait-registres-table-a-v2.md")" = 1 ] || arret "extrait : une ligne attendue"
for f in "$P/extrait-registres-table-a-v2.md" "$P/constat-noms-7b-v2.txt"; do
    n=$(grep -c -i -E "$INTERDITS_CONTENU" "$f"); [ "$n" = 0 ] || arret "contenu interdit ($n ligne(s)) dans $(basename "$f") : rien n'est remis"; done
echo "conforme : aucun contenu interdit dans l'extrait et le constat"
(cd "$P" && find . -type f -print0 | sort -z | xargs -0 sha256sum) > "$ESPACE_A/bordereau-remise-v2.txt"
n=$(cut -c67- "$ESPACE_A/bordereau-remise-v2.txt" | grep -c -i -E "$INTERDITS_NOMS")
[ "$n" = 0 ] && echo "conforme : aucun nom interdit parmi les pièces" || arret "$n nom(s) interdit(s) parmi les pièces : rien n'est remis"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$ESPACE_A/bordereau-remise-v2.txt" || arret "sceau du bordereau"
echo "pièces : $(wc -l < "$ESPACE_A/bordereau-remise-v2.txt") fichiers ; bordereau $(cut -d' ' -f1 "$ESPACE_A/bordereau-remise-v2.txt.sha256")"
# attendu : une ligne recopiée ; « aucun contenu interdit … » ; « aucun nom interdit … » ; 33 fichiers ; l'empreinte du bordereau
```

### Bloc A4 — message de remise et création du lecteur A

Avant : vérifie que ton outil d'agent peut créer un sous-agent du **modèle C** que Lazar t'a nommé ; sinon **arrêt, nœud de Lazar**.

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$BAC/message-remise-a-v2.txt" ] || arret "message déjà écrit : bloc déjà joué"
cat > "$BAC/message-remise-a-gabarit-v2.txt" <<'FIN'
Interdits permanents (brief du compte 3, section 6), en plus de ceux de ta consigne : aucune dépense ; aucune valeur de clé (jamais env, printenv, set sans argument, export -p, /proc/*/environ) ; jamais diag/*/lecture-sondes-t06.json, resume.json de 7b, les activations, les adaptateurs, la lecture B de 7a, donnees/lecture-b-7a-quarantaine-v1, donnees/mesure-unanime-v15-sortie-v1, essai/t06-explo-v3, aucun diag/ ni runs/ de 7a, l'étiqueteur, scripts/extraire_mesures_epreuve_t06_v1.py, la branche calcul/p3bis-reel-v2 ; jamais donnees/bras-attaque*, donnees/mode-tenu-a-l-ecart*, docs/notes/bras-attaque/, registres/index-bras-attaque*, anteriorite-bras-informe*, la branche claude/compassionate-meitner-d4ryyk ; aucune recherche récursive hors de l'espace donné ; jamais d'heure écrite à la main (date -u) ; aucun contact extérieur ; un refus de permission ou d'un classifieur : arrêt, tu le rapportes tel quel.
Tu es le lecteur neuf, unique, du verdict de la table A de T0.6 sur la course 7b (règle R13) : tu lis la table A dans l'ordre du point 7 du plan et tu prononces. Lis d'abord ta consigne, et elle seule fixe ce que tu lis et écris : <<ESPACE>>/pieces/<<CONSIGNE>> (empreinte <<EMPREINTE_CONSIGNE>>, égale à son compagnon : vérifie-la avant lecture).
- Run : 20261111-151701-t06-reel. Pièces : <<ESPACE>>/pieces (bordereau <<ESPACE>>/bordereau-remise-v2.txt, empreinte <<EMPREINTE_BORDEREAU>>, scellé). Tu n'écris que dans <<ESPACE>>/verdict-ferme.
- Constat de l'hôte (comptes de noms : résumé présent ou non, arrêt présent ou non) : <<ESPACE>>/pieces/constat-noms-7b-v2.txt.
- Interpréteur : <<PY>>.
- Avant tout, recopie le texte exact de ce message, tel que tu l'as reçu, dans <<ESPACE>>/verdict-ferme/verdict-T0.6-table-A-7b-v1-message-recu-v1.txt ; ton rapport final en donne l'empreinte sha256.
- Ton modèle s'écrit au verdict sans aucun identifiant : « <<NOTE_MODELE>> » (« modèle A » = celui des auteurs de T0.6).
- Aucun nombre ni aucune issue hors des fichiers scellés du verdict : ton rapport final suit la section « Ce que tu rends » de ta consigne, mot pour mot.
Tu ne lis rien d'autre (ni le dépôt, ni aucun fichier de T0.7, ni rien de l'étape B bis).
FIN
ESPACE="$ESPACE_A" BORDEREAU="$(cut -d' ' -f1 "$ESPACE_A/bordereau-remise-v2.txt.sha256")" PYV="$PY" NOTE="$NOTE_MODELE" \
  CONS="$CONSIGNE_A" ECONS="$EMPREINTE_CONSIGNE_A" \
  "$PY" -B - "$BAC/message-remise-a-gabarit-v2.txt" "$BAC/message-remise-a-v2.txt" <<'FIN' || arret "message de remise"
import os, sys
t = open(sys.argv[1], encoding="utf-8").read()
for m, v in (("<<ESPACE>>", "ESPACE"), ("<<EMPREINTE_BORDEREAU>>", "BORDEREAU"), ("<<PY>>", "PYV"), ("<<NOTE_MODELE>>", "NOTE"),
             ("<<CONSIGNE>>", "CONS"), ("<<EMPREINTE_CONSIGNE>>", "ECONS")):
    t = t.replace(m, os.environ[v])
if "<<" in t or ">>" in t:
    sys.exit("marqueur resté dans le message")
with open(sys.argv[2], "x", encoding="utf-8") as f:
    f.write(t)
print("message écrit, aucun marqueur restant")
FIN
cd "$DEPOT" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$BAC/message-remise-a-v2.txt" || arret "sceau du message"
cat "$BAC/message-remise-a-v2.txt"
```

**Création du lecteur A** : **un** sous-agent neuf, agent généraliste sans contexte hérité, du modèle C, dont le **seul message** est le
texte exact affiché par le bloc A4, copié tel quel. Tu attends son rapport final sans rien lire de l'espace fermé ni lui envoyer d'autre
message. Pas de second lecteur.

### Bloc A5 — après le verdict A : message reçu attesté, copie, sceaux, commit, poussée (relançable)

Sur un rapport « arrêt » du lecteur : pas de bloc A5 ; bloc F-A seul ; nœud de Lazar.

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
V="$ESPACE_A/verdict-ferme"; cd "$V" || arret "verdict-ferme absent"
ls -1A
[ -z "$(find . -mindepth 1 -type d)" ] || arret "dossier inattendu dans verdict-ferme : rien n'est copié"
n=$(ls -1A | grep -v -E '^verdict-T0\.6-table-A-7b-v1(\.md|-issue\.json|-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md))(\.sha256)?$' | wc -l)
[ "$n" = 0 ] || arret "$n fichier(s) de nom inattendu (archives comprises) dans verdict-ferme : rien n'est copié"
[ -f verdict-T0.6-table-A-7b-v1.md ] || arret "verdict en prose absent"
M=verdict-T0.6-table-A-7b-v1-message-recu-v1.txt
[ -f "$M" ] || arret "message reçu non recopié par le lecteur : rien n'est commité ; nœud"
"$PY" -B -c 'import sys; a=open(sys.argv[1],encoding="utf-8").read().rstrip("\n"); b=open(sys.argv[2],encoding="utf-8").read().rstrip("\n"); sys.exit(0 if a == b else 1)' \
    "$M" "$BAC/message-remise-a-v2.txt" && echo "message reçu égal au message scellé" || arret "message reçu différent du message scellé : rien n'est commité ; nœud"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_A" ] || arret "tu n'es pas sur $BR_A"
if [ -e "$BAC/c-verdict-a-v2.txt" ]; then echo "verdict A déjà commité"; else
    mkdir -p docs/verdicts
    for f in $(ls -1A "$V" | grep -v '\.sha256$'); do
        [ -e "docs/verdicts/$f" ] && { cmp -s "$V/$f" "docs/verdicts/$f" || arret "docs/verdicts/$f existe et diffère"; } \
            || { cp "$V/$f" "docs/verdicts/$f" && cmp -s "$V/$f" "docs/verdicts/$f" || arret "copie de $f"; }
        PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "docs/verdicts/$f" || arret "sceau de $f"; done
    git add -- docs/verdicts/verdict-T0.6-table-A-7b-v1*
    git diff --cached --name-only | grep -v -E '^docs/verdicts/verdict-T0\.6-table-A-7b-v1[^/]*$' && arret "index : autre chose que les fichiers du verdict"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    git commit -q -m "T0.6, table A sur 7b : verdict du lecteur neuf, fichiers scellés (session hôte du compte 3 ; hors de main jusqu'à CODE-MOTS-ET-COUT-T06)" || arret "commit (relance ce bloc)"
    git rev-parse HEAD > "$BAC/c-verdict-a-v2.txt"; fi
git push -q origin "refs/heads/$BR_A:refs/heads/$BR_A" || arret "poussée du verdict A (relance ce bloc : il reprend à la poussée)"
echo "commit du verdict A : $(cat "$BAC/c-verdict-a-v2.txt")"; git ls-remote origin "refs/heads/$BR_A"
for f in docs/verdicts/verdict-T0.6-table-A-7b-v1*.sha256; do cat "$f"; done
# attendu : noms conformes ; « message reçu égal … » ; copies égales et scellées ; commit poussé (même commit au distant)
```

### Bloc F-A — journal provisoire et passation (sans issue ni nombre du verdict)

Remplis d'abord les trois variables de tête (texte que tu as vu ; les heures viennent de `date -u`).

```bash
. "$HOME/bac-lecture-7b-compte-3-v2/variables-v2.sh" || exit 1
RAPPORT=$(cat <<'FIN'
<rapport final du lecteur A, tel quel, à la place de cette ligne>
FIN
)
CROCHET='<bloquée | passée>'; MODELES='lecteur : modèle C ; session hôte : <modèle A | modèle C> ; identités dites en conversation seulement'
case "$RAPPORT$CROCHET$MODELES" in *'<rapport final'*|*'<bloquée | passée>'*|*'<modèle A | modèle C>'*) arret "variables de tête non remplies";; esac
lire() { cat "$1" 2>/dev/null || echo "sans objet"; }
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_A" ] || arret "tu n'es pas sur $BR_A"
printf '%s\n' "$RAPPORT" > "$BAC/rapport-lecteur-a-v2.txt"          # en entier, hors du dépôt ; transmis à Lazar en conversation
mkdir -p registres-provisoires; N="registres-provisoires/compte-3-phase-a-$(date -u +%Y-%m-%d-%H%M)-v2.md"
{ echo "# Compte 3 — session hôte du lecteur de la table A — journal provisoire (v2)"; echo
  echo "Écrit le $(date -u +%Y-%m-%dT%H:%M:%SZ) (\`date -u\`) par la session \`$SESSION_C3\`, branche \`$BR_A\` ; identifiants provisoires P3A-…, à numéroter par la mère."; echo
  echo "- P3A-001 : commande phase A v2 exécutée depuis $(lire "$BAC/debut-v2.txt") ; épreuve du crochet : $CROCHET ; $MODELES ; liste \`$LISTE\` (\`$EMPREINTE_LISTE\`) : attestation conforme ; session neuve."
  echo "- P3A-002 : base main \`$(lire "$BAC/c-main-a-v2.txt")\` ; bordereau \`$(cut -d' ' -f1 "$ESPACE_A/bordereau-remise-v2.txt.sha256" 2>/dev/null)\` ; message \`$(cut -d' ' -f1 "$BAC/message-remise-a-v2.txt.sha256" 2>/dev/null)\` (reçu égal) ; verdict commité \`$(lire "$BAC/c-verdict-a-v2.txt")\`."
  echo "- P3A-003 : rapport final du lecteur, seules les lignes STATUT, FICHIERS, DÉCLARATIONS et MESSAGE (le rapport entier est transmis à Lazar en conversation) :"
  grep -E '^(STATUT|FICHIERS|DÉCLARATIONS|MESSAGE)' "$BAC/rapport-lecteur-a-v2.txt" | sed 's/^/    /'
  echo "- P3A-004 : cette session n'a ouvert aucun résultat ; elle est exclue de l'analyse du verdict A, de l'étape B bis (conception et verdicts), de T0.8, de G0, du préenregistrement NARCBench (rédaction, contre-lecture, course), des brouillons des papiers B et C et du code de la pièce « mots et coût »."
  echo "- P3A-005 : verdict hors de \`main\` jusqu'à la ligne \`CODE-MOTS-ET-COUT-T06\` (décision de la mère, R-2735)."
} > "$N"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$N" || arret "sceau"
git add -- "$N" "$N.sha256"
[ "$(git diff --cached --name-only | grep -vc '^registres-provisoires/')" = 0 ] || arret "index : autre chose que registres-provisoires/"
n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
git commit -q -m "Compte 3 : journal provisoire de la session hôte du lecteur de la table A" || arret "commit"
git push -q origin "refs/heads/$BR_A:refs/heads/$BR_A" || arret "poussée (relance : git push -q origin refs/heads/$BR_A:refs/heads/$BR_A)"
echo "RENDU — branche $BR_A ; tête $(git rev-parse HEAD)"; sha256sum "$N"
```

## 12. Ce que tu ne fais jamais ici

Lire une sortie ; lancer l'extracteur ; rapatrier `lecture-sondes-t06.json`, `resume.json`, des activations ou des adaptateurs ; mettre une
ligne de `registres/decisions.md` dans les pièces ; pousser sur `main` ; écrire un identifiant de modèle dans un fichier ; prendre un lecteur
d'un autre modèle que le modèle C.

## 13. Rendu à Lazar (il transmet à la mère)

1. Une à trois lignes : « Phase A : verdict du lecteur neuf (modèle C) scellé et poussé sur `verdict/t06-table-a-7b-compte-3-v1` ; hors de
   `main` jusqu'à `CODE-MOTS-ET-COUT-T06` ; rien d'autre lu. » — ou le bloc et le motif d'un arrêt.
2. Le rapport final du lecteur, en entier (`$BAC/rapport-lecteur-a-v2.txt`), **pour Lazar** ; la mère ne le recopie dans aucun fichier lu par
   le développeur ou le contre-lecteur de la pièce « mots et coût » ni dans le registre des décisions avant la ligne `CODE-MOTS-ET-COUT-T06`.
3. Pour la mère : sortie « RENDU » du bloc F-A, commits, empreintes du verdict, du bordereau, du message ; épreuve du crochet.

## 14. Ce qui arrête tout

- Tout « ARRÊT » d'un bloc. Avant le bloc A4, rien d'irréversible (hors le nom de la branche poussée) : tu le dis à Lazar (bloc et motif).
  Un arrêt au bloc 1 : tu peux effacer `$BAC` et relancer le bloc 1 une fois.
- Identifiant de session introuvable : remplace `SESSION_C3=…` par celui que donne l'outil qui décrit ta session (ou la ligne
  « Claude-Session » de tes consignes d'attribution), puis relance le bloc 1 ; sinon, arrêt.
- Attestation ou nouveauté non conformes ; tête autre ; compagnon faux ; nom ou contenu interdit : rien n'est remis ; la mère tranche.
- Pas de sous-agent du modèle C : arrêt, nœud. Rapport « arrêt » du lecteur, message reçu absent ou différent : rien n'est commité ; nœud.
- Refus de permission, du crochet ou d'un classifieur, poussée refusée : arrêt, rapport à la mère, aucun contournement.

## 15. Ce que fait la mère ensuite (pour mémoire)

1. Vérifie la branche (parents, fichiers : `docs/verdicts/verdict-T0.6-table-A-7b-v1*` puis `registres-provisoires/…`), sans recopier dans
   `main` ; consigne au registre des décisions le seul fait (branche, commits, empreintes), **sans l'issue ni aucun nombre**.
2. **Tant que la ligne `CODE-MOTS-ET-COUT-T06` n'est pas inscrite**, le verdict A, son fichier d'issue et le journal provisoire restent hors
   des fichiers lus par l'auteur et le contre-lecteur de la pièce « mots et coût » (liste positive dans leurs consignes ; jamais la branche
   `verdict/t06-table-a-7b-compte-3-v1`) ; si l'ordre ne peut pas être tenu : nœud de Lazar (CL3-01, R-2735).
3. Après la ligne `CODE-MOTS-ET-COUT-T06` : recopie à l'octet dans `main` (même blob), rescelle, consigne le verdict, met à jour la liste
   « qui a lu quoi » (hôte : rien ouvert ; lecteur A : pièces du bordereau ; exclusions de la section 1), soumet le verdict à Lazar pour GO.
   Aucune ligne de verdict dans `registres/scellements-v1.md`.

## Annexe — essais (règle R5)

- Attestation v2 : `essai_attestation_compte_3_v2.sh`, 12 conformes sur 12 (liste réelle v1 : conforme ; identifiant entier ou tronqué :
  arrêt ; autre session identifiée du compte 3 : admise ; ligne du compte 3 sans identifiant avec une exclusion : arrêt).
- **Répétition de bout en bout** de cette commande (blocs 0b, 1, 2, A1 à A5, F-A) sur dépôts jouets : `repetition_phase_a_jouet_v2.sh`,
  sortie versée `repetition-phase-a-jouet-sortie-v2.txt` (résultat au rapport v2), avec artefacts.
