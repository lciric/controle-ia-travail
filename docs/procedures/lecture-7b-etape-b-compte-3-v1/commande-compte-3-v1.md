# Commande de la mère au compte 3 — hôte des lecteurs de 7b (table A de T0.6) et de l'étape B de T0.7 — v1

- **Statut** : commande écrite de la session mère au compte 3, sur le mot de Lazar du 2026-11-14 (R-2711 (2) : « hôte des
  lecteurs de 7b et de l'étape B : une session neuve du compte 3 »). À coller par Lazar comme **premier message d'une session
  neuve du compte 3, ouverte dans le dossier du dépôt**. Elle n'accorde aucune dépense (il n'y en a aucune), ne change aucun
  texte scellé, n'ajoute aucun critère. Si elle contredit un texte scellé (T0.6, T0.7, la base (A) de T0.8) ou le module
  `src/controle_ia/t07/` au commit C7, le texte ou le module fait foi : tu t'arrêtes et tu le dis.
- **Version 1, non contre-lue.** Rédacteur : préparateur neuf, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`
  (modèle A), le 2026-11-14 à partir de 11:02:05Z (`date -u`) ; ni lecteur ni juge d'aucun verdict ; il n'a ouvert aucune
  sortie de 7a, 7b ou T0.7 (noms, tailles et empreintes seulement). Contre-lecture à faire par un sous-agent neuf du modèle C
  (consigne : `consigne-contre-lecture-commande-compte-3-v1.md`, même dossier), puis version 2 si besoin.
- **Phases** : **A** (table A de 7b) est complète et remettable dès que ses trois marqueurs sont remplis. **B** (exécution de la
  pièce « mots et coût ») est un **gabarit** : ses marqueurs dépendent d'un code qui n'existe pas encore ; une version 2
  contre-lue les portera. **C** (étape B) est complète, mais ne se lance qu'après les préalables de `prealables-v1.md`
  (étapes 2 à 5), contrôlés par programme au bloc C3.
- **Sigles** : UTC = temps universel coordonné ; JSON = format de données texte ; « empreinte » = condensé sha256 d'un
  fichier ; « compagnon » = fichier `.sha256` voisin (règle R6) ; « 7b » = course de confirmation de T0.6, run
  `20261111-151701-t06-reel` ; « étape A » = notation de T0.7, run `20261114-001352-t07-lecture-reel` ; « C7 » = commit du
  code de T0.7 cité par `CODE-T07`, `c2fab6cc7267b76228a75dc3e2e08bc7aa038961`.
- **Pièces de cette commande** (même dossier `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, chacune scellée) :

| pièce | empreinte | rôle |
|---|---|---|
| `controle_a_blanc_etape_b_compte_3_v1.py` | `eb19ef6a56cd34913e644aa8aa4a76a65a9ddf96f22796b42f8f1c6198caa275` | contrôle à blanc de l'étape B (garde du registre de T0.7, sceaux, antériorités, garde adaptée, `CODE-T07`, fichiers, condition d'ordre B bis), lecture seule |
| `essai_controle_a_blanc_etape_b_compte_3_v1.sh`, sortie `essai-controle-a-blanc-etape-b-compte-3-sortie-v1.txt` | `c6fa5ac9…`, `8570610f…` | essai R5 : 28 conformes sur 28 |
| `attestation_qui_a_lu_quoi_compte_3_v1.py` | `639d85d6b3fb73008f64e40516455f13f1a04db13097fbbfee68f41e9ff575ca` | attestation « qui a lu quoi » (bloc 2) |
| `essai_attestation_compte_3_v1.sh`, sortie `essai-attestation-compte-3-sortie-v1.txt` | `a88ae9bb…`, `499b9fe4…` | essai R5 : 9 conformes sur 9 |
| `repetition_bloc_c2_jouet_v1.sh`, sortie `repetition-bloc-c2-jouet-sortie-v1.txt` | `235d5930…`, `ea097fa2…` | répétition du bloc C2 sur dépôts jouets : 7 conformes sur 7 (bloc `e58d180e…`) |
| `controle-a-blanc-etat-actuel-sortie-v1.txt` | `3ed16bc5…` | contrôle à blanc sur l'état de `main` du 2026-11-14 11:29Z : aucun refus, deux clés manquantes |
| `prealables-v1.md` | `0cd96b629cb181246a8c2b15ad235719d72eaea64650552e0d482b630506c129` | préalables, pour la mère (tu ne le lis pas) |
| `consigne-contre-lecture-commande-compte-3-v1.md` | `23f4767d…` | consigne du contre-lecteur de cette commande (pour la mère) |

## 0. D'abord, pour Lazar et la mère

1. **Voie d'écriture** : trois branches neuves, créées sur `main` au moment voulu, poussées par refspec, jamais `main` :
   `verdict/t06-table-a-7b-compte-3-v1` (phase A), `verdict/t06-mots-et-cout-compte-3-v1` (phase B),
   `verdict/t07-etape-b-compte-3-v1` (phase C). Rien n'est écrit dans `registres/` de `main` ; le seul fichier de `registres/`
   qui change, sur la branche de la phase C, est le journal `registres/scellements-v1.md.ouvertures.md`, écrit par le seul
   module de T0.7 ; tes faits vont dans `registres-provisoires/` (bloc F). La mère recopie ensuite (section 15).
2. **Ce que cette commande évite, et pourquoi** (détails : `prealables-v1.md`, § 1) : l'extracteur
   `scripts/extraire_mesures_epreuve_t06_v1.py` (il ouvre `lecture-sondes-t06.json`, que T0.6 scellé, l. 771, ferme jusqu'au
   contrôle d'ouverture v2 ; nœud N-A) ; `resume.json` de 7b (il porte `ligne_B` et `ligne_C`) ; `lecture_v3 etape-b` (refuse la
   configuration v8 : on joue `lecture_v4 etape-b`) ; l'étape B depuis `main` (on joue le code d'une arborescence détachée à
   C7, parce que `CODE-T07` refuse tout fichier de `src/controle_ia/` différent de C7).
3. **Irréversible** : (i) le nom de chaque branche (R12) ; (ii) la remise d'une pièce à un lecteur ; (iii) l'unique appel de
   l'étape B (lecture décisive unique, R12 ; ligne au journal). Chacun est précédé d'un contrôle à blanc dans le même bloc, et la
   poussée de la branche est éprouvée avant.
4. **Modèles** : chaque lecteur est un sous-agent neuf du **modèle C** que Lazar nomme en conversation ; à défaut, modèle A, et
   le verdict le dit (« modèle A, faute de C ») ; jamais le modèle B (indisponible jusqu'au 2026-11-20 15:00Z, R-2718) ; aucun
   identifiant de modèle n'est écrit dans un fichier.

## 1. Interdits permanents

Recopiés du brief du compte 3, section 6 (à recopier en tête de toute consigne de sous-agent) :

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`,
  `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a, l'étiqueteur,
  `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers
  nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit : `n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] && git commit …`
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner
  `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur :
  arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Exception unique de cette commande, accordée par le mot de Lazar R-2711 (2)** : les fichiers de 7b (branche
`calcul/t06-confirmation-7b-v1`) et de l'étape A (branche `donnees/t07-etape-a-v1`) nommés aux blocs A2 et C2 sont récupérés
par refspec, dans un dépôt jetable sans contenu, puis **extraits par liste positive** (`git show <tête>:<chemin>`), pour le
seul lecteur du verdict (phase A) et pour le seul module gelé de T0.7 (phase C). Rien d'autre de ces branches n'est extrait.

**Interdits ajoutés par cette commande** :

- **Tu n'ouvres aucun résultat** : ni les fichiers extraits (tu les copies, hashes, compares), ni la sortie de l'étape B (gardée
  dans l'espace fermé, jamais affichée, hors la seule ligne de refus du journal sur un code 2), ni le verdict en prose, ni les
  fichiers de travail des lecteurs. Tu lis seulement : les noms (`git ls-tree --name-only`), les compagnons, les empreintes,
  les champs `fichier`, `octets` et `sha256` du manifeste des morceaux de `scores-actions-t07.npz` (par programme), et le
  rapport final de chaque lecteur.
- Jamais `resume.json` de 7b, ni les activations (`activations-sous-ensemble-t06-*`), ni les adaptateurs, ni
  `sondes-neuves-t07.npz`, `planchers-figees-t07.npz`, `temoins-lexicaux-t07.json`, ni rien de l'étape B bis.
- Aucune analyse d'un verdict après l'avoir rendu ; cette session est ensuite exclue de l'analyse de ces verdicts, de la
  conception et des verdicts de l'étape B bis, de T0.8 et de G0.
- Aucune poussée hors des trois branches de la section 0 ; jamais `main`, jamais `lot/compte-3-v1`, jamais `lciric/controle-ia`.
- **Un seul appel de `lecture_v4 etape-b`** (bloc C4) ; jamais un second « pour voir ». Un refus (code 2) est une attente : la
  relance sur le même run demande un mot écrit de la mère ; un code 3 est un nœud : aucune relance.
- Les seuls `find` de cette commande portent sur des dossiers qu'elle crée (`$ESPACE_A`, `$ESPACE_B`, `verdict-ferme/`).

## 2. Qui fait quoi

- **Toi, la session hôte (compte 3)** : tu joues les blocs dans l'ordre ; tu récupères et extrais par liste positive ; tu
  remets les pièces aux lecteurs ; tu appelles, une fois, l'étape B ; tu copies, scelles, commites et pousses sur tes
  branches ; tu rends à Lazar. Tu n'écris aucun verdict.
- **Lecteur A** (verdict de la table A de T0.6 sur 7b, critère 2 partie (ii)) : **un** sous-agent neuf, créé pour ce seul
  verdict, sans contexte hérité (jamais une bifurcation de ta conversation), du modèle C (ou A, faute de C) ; il lit sa
  consigne scellée et les pièces de `$ESPACE_A/pieces`, n'écrit que dans `$ESPACE_A/verdict-ferme`.
- **Lecteur B** (verdict de l'étape B de T0.7, critère 3) : **un autre** sous-agent neuf, mêmes règles, espace `$ESPACE_B`.
  Aucun lecteur ne reçoit de pièce de l'étape B bis ; aucun n'est la session mère, le compte 2, le compte 4, un auteur ou
  contre-lecteur de T0.6, de T0.7, de la pièce « mots et coût », de l'audit des fuites ou de cette commande.
- **La mère** : remplit les marqueurs ; inscrit les lignes de registre ; recopie dans `main` ce que tu pousses (section 15) ;
  soumet les verdicts à Lazar.

## 3. Marqueurs

| marqueur | qui le remplit, quand | où |
|---|---|---|
| chemin et empreinte de la version remise de cette commande | Lazar, en conversation : tu vérifies que le texte collé est ce fichier (`sha256sum` et compagnon) avant le bloc 1 | section 4 |
| `<<MODELE_LECTEUR>>` | Lazar, **en conversation** : « modèle C » (ou « modèle A, faute de C ») ; jamais écrit dans un fichier | blocs A4, C6 |
| `<<LISTE>>`, `<<EMPREINTE_LISTE>>` | la mère : chemin et empreinte de la liste « qui a lu quoi » **v2** scellée (en-tête avec « session », « compte », « exclu de ») | bloc 1 |
| `<<CONSIGNE_LECTEUR_A>>`, `<<EMPREINTE_CONSIGNE_LECTEUR_A>>` | la mère : consigne scellée du lecteur de la table A (chemin relatif à la racine du dépôt) | bloc 1 |
| `<<CONSIGNE_LECTEUR_B>>`, `<<EMPREINTE_CONSIGNE_LECTEUR_B>>` | la mère : consigne scellée du lecteur de l'étape B | bloc 1 (vide permis jusqu'à la phase C ; le bloc C0 s'arrête s'il reste) |
| `<<REGISTRE_BBIS>>`, `<<CLE_PLAN_BBIS>>` | la mère : registre propre et clé de la ligne de scellement du plan de l'étape B bis (proposés : `registres/etape-b-bis-v1.md`, `SCELLEMENT-PLAN-BBIS`) | bloc 1 (idem) |
| `<<R_BA_L2>>` | la mère : numéro de la ligne du registre des décisions qui consigne l'état de la ligne BA-L2 (« ne s'applique pas ») ou le mot de Lazar | bloc 1 (idem) |
| `<<COMMIT_PIECE>>`, `<<COMMANDE_PIECE>>`, `<<MOTIF_RUN_PIECE>>`, `<<LIGNE_CODE_MOTS_ET_COUT>>` | la mère, dans la **version 2** de cette commande, après la ligne `CODE-MOTS-ET-COUT-T06` (le bloc C2 lit le chemin du fichier « mots et coût » dans la ligne `ISSUE-MOTS-ET-COUT-T06` : aucun marqueur) | phase B |
| `<<ESPACE>>`, `<<EMPREINTE_BORDEREAU>>`, `<<PY>>`, `<<NOTE_MODELE>>`, `<<CONSIGNE>>`, `<<EMPREINTE_CONSIGNE>>` | toi, à l'exécution : remplacés par programme dans les messages de remise ; le bloc s'arrête s'il en reste un | blocs A4, C6 |

## 4. Mode d'emploi

- Avant tout : vérifie que le texte collé est le fichier scellé dont Lazar t'a donné le chemin et l'empreinte. Écart : arrêt.
- **Routine de reprise réduite** (brief, section 2) : pas de `verifier-arbre`, pas de lecture de `registres/` hors des lignes
  nommées par les blocs, pas d'inventaire du loueur ; empreintes de lancement au bloc 2.
- **Chaque bloc se lance tel quel, dans un seul appel de ton outil de commande**, dans l'ordre. L'état du shell ne survit pas
  d'un appel à l'autre : chaque bloc relit `$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh`. Une ligne « ARRÊT : »
  dans la sortie : tu t'arrêtes et tu suis la section 14.
- **Délai de l'outil** : les blocs A2, C1, C2 et C4 se lancent au **délai maximal** de ton outil (dix minutes), au premier
  plan. Si l'outil rend la main sans la ligne finale attendue : tu ne relances rien ; tu rapportes à la mère.
- **Quota** : au-dessus de 80 % (brief, section 7), tu ne commences ni le bloc A4 ni le bloc C4.
- Les commentaires « attendu : » disent la sortie conforme ; toute autre sortie est un arrêt.

## 5. Bloc 0 — épreuve d'aptitude (appels séparés)

```bash
sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py
# attendu : appel BLOQUÉ par le crochet de garde. S'il passe : dis-le en tête de ton premier message à Lazar ; rien de
# payant n'est lancé par cette commande (il n'y a rien de payant), mais la mère doit le savoir.
```

```bash
for k in GH_TOKEN GITHUB_TOKEN HCLOUD_TOKEN VAST_API_KEY ANTHROPIC_API_KEY OPENAI_API_KEY HF_TOKEN; do
    [ -n "${!k+x}" ] && echo "$k : présente" || echo "$k : absente"; done      # noms seulement, jamais une valeur
df -h "$HOME" . | sed -n '1,3p'; nproc; date -u +%Y-%m-%dT%H:%M:%SZ
# attendu : la liste des noms ; la place libre (phase A : ≥ 1 Gio ; phase C : ≥ 9 Gio si aucun interpréteur avec torch
# n'est prêt). Dis aussi à Lazar le modèle de ta session et ton quota.
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
BAC="$HOME/bac-lecture-7b-etape-b-compte-3-v1"                 # hors de tout arbre git ; neuf (R12)
[ ! -e "$BAC" ] || arret "$BAC existe déjà : rapport à la mère"
git -C "$HOME" rev-parse --show-toplevel >/dev/null 2>&1 && arret "$HOME est dans un arbre git"
SESSION_C3="session_${CLAUDE_CODE_REMOTE_SESSION_ID#cse_}"
[[ "$SESSION_C3" =~ ^session_[0-9A-Za-z]{10,}$ ]] || arret "identifiant de session introuvable (section 14)"
LISTE='<<LISTE>>'; EMPREINTE_LISTE='<<EMPREINTE_LISTE>>'
CONSIGNE_A='<<CONSIGNE_LECTEUR_A>>'; EMPREINTE_CONSIGNE_A='<<EMPREINTE_CONSIGNE_LECTEUR_A>>'
CONSIGNE_B='<<CONSIGNE_LECTEUR_B>>'; EMPREINTE_CONSIGNE_B='<<EMPREINTE_CONSIGNE_LECTEUR_B>>'
REGISTRE_BBIS='<<REGISTRE_BBIS>>'; CLE_BBIS='<<CLE_PLAN_BBIS>>'; R_BA_L2='<<R_BA_L2>>'
case "$LISTE $EMPREINTE_LISTE $CONSIGNE_A $EMPREINTE_CONSIGNE_A" in
  *'<<'*) arret "marqueur non rempli : LISTE, EMPREINTE_LISTE, CONSIGNE_LECTEUR_A ou son empreinte (la mère)";; esac
mkdir -p "$BAC" && date -u +%Y-%m-%dT%H:%M:%SZ > "$BAC/debut-v1.txt"
if "$DEPOT/.venv/bin/python" -c 'import numpy' 2>/dev/null; then PY="$DEPOT/.venv/bin/python"
else python3 -m venv "$BAC/venv-a-v1" && "$BAC/venv-a-v1/bin/pip" install -q --disable-pip-version-check numpy==2.4.6 \
     && PY="$BAC/venv-a-v1/bin/python" || arret "interpréteur"; fi
"$PY" -c 'import numpy, sys; print("interpréteur :", sys.executable, sys.version.split()[0], "numpy", numpy.__version__)' \
    || arret "interpréteur sans numpy"
cat > "$BAC/variables-v1.sh" <<EOF
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
arret() { echo "ARRÊT : \$*"; exit 1; }
DEPOT='$DEPOT'; BAC='$BAC'; PY='$PY'; SESSION_C3='$SESSION_C3'
LISTE='$LISTE'; EMPREINTE_LISTE='$EMPREINTE_LISTE'
CONSIGNE_A='$CONSIGNE_A'; EMPREINTE_CONSIGNE_A='$EMPREINTE_CONSIGNE_A'
CONSIGNE_B='$CONSIGNE_B'; EMPREINTE_CONSIGNE_B='$EMPREINTE_CONSIGNE_B'
REGISTRE_BBIS='$REGISTRE_BBIS'; CLE_BBIS='$CLE_BBIS'; R_BA_L2='$R_BA_L2'
ICI="\$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1"
R6=20261111-151701-t06-reel; R7=20261114-001352-t07-lecture-reel; TR6=t06-20261112-051655-1Xzh
B7B=calcul/t06-confirmation-7b-v1; TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
BEA=donnees/t07-etape-a-v1; TETE_EA=0c176db582ec13705e8fb7cc2d281215e2766e42
C7=c2fab6cc7267b76228a75dc3e2e08bc7aa038961
BR_A=verdict/t06-table-a-7b-compte-3-v1; BR_P=verdict/t06-mots-et-cout-compte-3-v1; BR_B=verdict/t07-etape-b-compte-3-v1
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
CLONE7B="\$BAC/clone-7b-v1"; CLONEEA="\$BAC/clone-etape-a-v1"; WT_C7="\$BAC/code-c7-v1"; MORCEAUX="\$BAC/morceaux-scores-v1"
ESPACE_A="\$BAC/espace-table-a-v1"; ESPACE_B="\$BAC/espace-etape-b-v1"
CONFIG_T07="\$DEPOT/prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"
SECRETS='(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'
EOF
echo "session : $SESSION_C3 ; variables : $BAC/variables-v1.sh"
# attendu : dépôt, interpréteur avec numpy, session « session_… » (égale à la ligne « Claude-Session » de tes consignes
# d'attribution, s'il y en a une) ; aucun « ARRÊT »
```

## 7. Bloc 2 — contrôles d'entrée et attestation « qui a lu quoi »

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
date -u +%Y-%m-%dT%H:%M:%SZ
# (a) horloge : les lignes de journal et l'antériorité stricte se jugent à l'horloge de ce conteneur
D=$(curl -sS --max-time 20 -D - -o /dev/null https://pypi.org/simple/numpy/ 2>/dev/null | tr -d '\r' \
    | awk -F': ' 'tolower($1)=="date"{print $2}' | tail -1)
[ -n "$D" ] || arret "horloge de référence (en-tête Date de pypi.org) injoignable"
E=$(( $(date -u +%s) - $(date -u -d "$D" +%s) )); echo "écart de l'horloge à pypi.org : $E s"
[ "${E#-}" -le 120 ] || arret "horloge décalée de plus de 120 s"
# (b) empreintes de lancement
(cd "$DEPOT/docs" && sha256sum -c --quiet sha256sums-lancement-v2.txt) && echo "empreintes de lancement conformes" \
    || arret "empreintes de lancement"
# (c) pièces de cette commande
(cd "$ICI" && sha256sum -c) <<'FIN' || arret "pièces de cette commande"
eb19ef6a56cd34913e644aa8aa4a76a65a9ddf96f22796b42f8f1c6198caa275  controle_a_blanc_etape_b_compte_3_v1.py
639d85d6b3fb73008f64e40516455f13f1a04db13097fbbfee68f41e9ff575ca  attestation_qui_a_lu_quoi_compte_3_v1.py
FIN
# (d) attestation : ni ta session dans la liste, ni le compte 3 avec une exclusion
python3 -I -B "$ICI/attestation_qui_a_lu_quoi_compte_3_v1.py" "$DEPOT/$LISTE" "$EMPREINTE_LISTE" "$SESSION_C3" \
    || arret "attestation « qui a lu quoi » non conforme : rien n'est lancé ; la mère tranche"
# (e) identité git, état du dépôt
cd "$DEPOT"
[ -n "$(git config user.name)" ] && [ -n "$(git config user.email)" ] || arret "identité git (user.name, user.email) absente"
[ -z "$(git status --porcelain --untracked-files=no)" ] || arret "modifications suivies dans ton dépôt"
# attendu : écart au plus 120 s ; « empreintes de lancement conformes » ; deux « OK » ; « ATTESTATION : CONFORME — … » ;
# aucun « ARRÊT »
```

## 8. Phase A — table A de T0.6 sur 7b (peut commencer tout de suite)

### Bloc A1 — branche neuve, lignes de registre, pièces de main

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
cd "$DEPOT"
git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || arret "récupération de main"
[ -z "$(git ls-remote origin "refs/heads/$BR_A")" ] || arret "la branche $BR_A existe déjà au distant (R12)"
if [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_A" ] && [ -e "$BAC/c-main-a-v1.txt" ]; then echo "branche $BR_A déjà créée (bloc relancé)"
else git switch -q --no-track -c "$BR_A" refs/remotes/origin/main || arret "création de $BR_A"; git rev-parse HEAD > "$BAC/c-main-a-v1.txt"; fi
attendu() { [ "$(grep -cxF -- "$2" "$1")" = 1 ] && echo "conforme :$(echo "$2" | cut -d'|' -f2)" \
    || arret "ligne absente, autre ou en double dans $1 :$(echo "$2" | cut -d'|' -f2)"; }
R=registres/scellements-v1.md
attendu $R "| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/20261111-151701-t06-reel/manifeste.json | 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 |"
attendu $R "| VERDICT-P3BIS | 2026-11-14T10:30:38Z | docs/verdicts/verdict-P3-bis-v1-issue.json | c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 |"
sha256sum -c <<FIN || arret "pièces de main"
ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169  prereg/T0.6-organismes-v0-v1.md
b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527  prereg/T0.6-organismes-config-7b-v1.json
$EMPREINTE_CONSIGNE_A  $CONSIGNE_A
FIN
for f in prereg/T0.6-organismes-v0-v1.md prereg/T0.6-organismes-config-7b-v1.json "$CONSIGNE_A"; do
    [ "$(cut -d' ' -f1 "$f.sha256")" = "$(sha256sum "$f" | cut -d' ' -f1)" ] || arret "compagnon de $f"; done
[ "$(ls docs/verdicts/verdict-T0.6-table-A-7b-v1* 2>/dev/null | wc -l)" = 0 ] || arret "fichiers du verdict de la table A déjà présents"
# la poussée est éprouvée avant toute remise : la branche neuve, égale à main, est poussée
git push -q origin "refs/heads/$BR_A:refs/heads/$BR_A" && echo "branche poussée (égale à main) : $(git ls-remote origin "refs/heads/$BR_A" | cut -c1-12)" \
    || arret "poussée refusée : rapport à la mère"
# attendu : deux « conforme » ; trois « OK » ; compagnons égaux ; « branche poussée » ; aucun « ARRÊT »
```

### Bloc A2 — dépôt jetable de la branche de 7b, extraction par liste positive (délai maximal)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
[ ! -e "$ESPACE_A" ] || arret "$ESPACE_A existe déjà"
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" | cut -f1)" = "$TETE_7B" ] || arret "tête de $B7B autre que $TETE_7B : rapport à la mère"
if [ ! -e "$CLONE7B" ]; then
    git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$B7B" "$DEPOT_URL" "$CLONE7B" \
        || arret "dépôt jetable sans contenu"
fi
[ "$(git -C "$CLONE7B" rev-parse HEAD)" = "$TETE_7B" ] || arret "tête du dépôt jetable"
P="$ESPACE_A/pieces"; mkdir -p "$P" "$ESPACE_A/verdict-ferme"
LISTE_A="diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json diag/$R6/distillation-t06.json runs/$R6/manifeste.json
donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl"
for f in $LISTE_A; do for g in "$f" "$f.sha256"; do
    mkdir -p "$P/$(dirname "$g")"; git -C "$CLONE7B" show "$TETE_7B:$g" > "$P/$g" || arret "extraction de $g"; done
    (cd "$P/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
T=$(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "traces/$TR6/")
[ "$(printf '%s\n' "$T" | grep -c .)" = 10 ] || arret "traces/$TR6 : 10 fichiers attendus"
for g in $T; do mkdir -p "$P/$(dirname "$g")"; git -C "$CLONE7B" show "$TETE_7B:$g" > "$P/$g" || arret "extraction de $g"; done
[ "$(sha256sum "$P/runs/$R6/manifeste.json" | cut -d' ' -f1)" = 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 ] \
    && echo "manifeste de 7b égal à la ligne RUN-CONFIRMATION-T06" || arret "manifeste de 7b autre que la ligne"
# constat de noms (aucun contenu) pour la ligne A1 de la table A
{ echo "# Constat de l'hôte (compte 3), noms seuls, $(date -u +%Y-%m-%dT%H:%M:%SZ), tête $TETE_7B"
  echo "diag/$R6/ : $(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/" | sed 's#.*/##' | tr '\n' ' ')"
  echo "resume.json : $(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/resume.json" | grep -c .) (présent si 1 ; non remis : il porte ligne_B et ligne_C)"
  echo "arret.json : $(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/arret.json" | grep -c .) (absent si 0)"
} > "$P/constat-noms-7b-v1.txt"
n=$(cd "$P" && find . -type f | grep -c -E 'lecture-sondes|resume\.json|activations|adaptateur|bras-attaque|mode-tenu|etiqueteur|quarantaine|mesure-unanime')
[ "$n" = 0 ] && echo "aucun nom interdit parmi les fichiers extraits" || arret "$n nom(s) interdit(s) extraits : rien n'est remis ; rapport à la mère"
echo "extraits : $(cd "$P" && find . -type f | wc -l) fichiers, $(du -sb "$P" | cut -f1) octets"
# attendu : six fichiers et leurs compagnons « OK » (silencieux) ; dix fichiers de traces ; « manifeste de 7b égal … » ;
# « aucun nom interdit » ; ≈ 19 000 000 octets ; aucun « ARRÊT »
```

### Bloc A3 — pièces du lecteur A et bordereau

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
P="$ESPACE_A/pieces"; cd "$DEPOT"
for f in prereg/T0.6-organismes-v0-v1.md prereg/T0.6-organismes-config-7b-v1.json "$CONSIGNE_A"; do
    cp --parents "$f" "$f.sha256" "$P/" || arret "copie de $f"; done
C=$(cat "$BAC/c-main-a-v1.txt")
{ echo "# Extrait des registres pour le lecteur de la table A (v1)"; echo; echo "Commit de main : $C. Lignes recopiées telles quelles."
  echo; echo "## registres/scellements-v1.md"; git show "$C:registres/scellements-v1.md" | grep -n -E '^\| (RUN-CONFIRMATION-T06|VERDICT-P3BIS) \|'
  echo; echo "## registres/decisions.md"; for r in R-2077 R-2082 R-2413 R-2704; do git show "$C:registres/decisions.md" | grep -n "^| $r |"; done
} > "$P/extrait-registres-table-a-v1.md"
[ "$(grep -c -E '^[0-9]+:\| ' "$P/extrait-registres-table-a-v1.md")" = 6 ] || arret "extrait des registres : six lignes attendues"
(cd "$P" && find . -type f -print0 | sort -z | xargs -0 sha256sum) > "$ESPACE_A/bordereau-remise-v1.txt"
n=$(cut -c67- "$ESPACE_A/bordereau-remise-v1.txt" | grep -c -i -E 't07|t0\.7|lecture-sondes|resume\.json|activations|adaptateur|bbis|b-bis|bras-attaque|mode-tenu|anteriorite-bras|etiqueteur|quarantaine|mesure-unanime')
[ "$n" = 0 ] && echo "conforme : aucun nom interdit parmi les pièces" || arret "$n nom(s) interdit(s) parmi les pièces : rien n'est remis"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$ESPACE_A/bordereau-remise-v1.txt" || arret "sceau du bordereau"
echo "pièces : $(wc -l < "$ESPACE_A/bordereau-remise-v1.txt") fichiers ; bordereau $(cut -d' ' -f1 "$ESPACE_A/bordereau-remise-v1.txt.sha256")"
# attendu : six lignes recopiées (non affichées) ; « aucun nom interdit » ; l'empreinte du bordereau ; aucun « ARRÊT »
```

### Bloc A4 — message de remise et création du lecteur A

Avant : vérifie que ton outil d'agent peut créer un sous-agent du modèle que Lazar t'a nommé ; fixe `NOTE_MODELE`.

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
NOTE_MODELE="modèle C"      # « modèle A, faute de C » si ton outil d'agent ne peut pas créer un sous-agent du modèle C
cat > "$BAC/message-remise-a-gabarit-v1.txt" <<'FIN'
Interdits permanents (brief du compte 3, section 6), en plus de ceux de ta consigne : aucune dépense ; aucune valeur de clé (jamais env, printenv, set sans argument, export -p, /proc/*/environ) ; jamais diag/*/lecture-sondes-t06.json, resume.json de 7b, les activations, les adaptateurs, la lecture B de 7a, donnees/lecture-b-7a-quarantaine-v1, donnees/mesure-unanime-v15-sortie-v1, essai/t06-explo-v3, aucun diag/ ni runs/ de 7a, l'étiqueteur, scripts/extraire_mesures_epreuve_t06_v1.py, la branche calcul/p3bis-reel-v2 ; jamais donnees/bras-attaque*, donnees/mode-tenu-a-l-ecart*, docs/notes/bras-attaque/, registres/index-bras-attaque*, anteriorite-bras-informe*, la branche claude/compassionate-meitner-d4ryyk ; aucune recherche récursive hors de l'espace donné ; jamais d'heure écrite à la main (date -u) ; aucun contact extérieur ; un refus de permission ou d'un classifieur : arrêt, tu le rapportes tel quel.
Tu es le lecteur neuf du verdict de la table A de T0.6 sur la course 7b (règle R13). Lis d'abord ta consigne, et elle seule fixe ce que tu lis et écris : <<ESPACE>>/pieces/<<CONSIGNE>> (empreinte <<EMPREINTE_CONSIGNE>>, égale à son compagnon : vérifie-la avant lecture).
- Run : 20261111-151701-t06-reel. Pièces : <<ESPACE>>/pieces (bordereau <<ESPACE>>/bordereau-remise-v1.txt, empreinte <<EMPREINTE_BORDEREAU>>, scellé). Tu n'écris que dans <<ESPACE>>/verdict-ferme.
- Constat de l'hôte sur les noms (résumé présent ou non, arrêt présent ou non) : <<ESPACE>>/pieces/constat-noms-7b-v1.txt.
- Interpréteur : <<PY>>.
- Ton modèle s'écrit au verdict sans aucun identifiant : « <<NOTE_MODELE>> » (« modèle A » = celui des auteurs de T0.6 et de T0.7).
Tu ne lis rien d'autre (ni le dépôt, ni aucun fichier de T0.7, ni rien de l'étape B bis). Ton rapport final suit la section « Ce que tu rends » de ta consigne, mot pour mot.
FIN
ESPACE="$ESPACE_A" BORDEREAU="$(cut -d' ' -f1 "$ESPACE_A/bordereau-remise-v1.txt.sha256")" PYV="$PY" NOTE="$NOTE_MODELE" \
  CONS="$CONSIGNE_A" ECONS="$EMPREINTE_CONSIGNE_A" \
  "$PY" -B - "$BAC/message-remise-a-gabarit-v1.txt" "$BAC/message-remise-a-v1.txt" <<'FIN' || arret "message de remise"
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
cd "$DEPOT" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$BAC/message-remise-a-v1.txt" || arret "sceau du message"
cat "$BAC/message-remise-a-v1.txt"
```

**Création du lecteur A** : **un** sous-agent neuf, par l'outil d'agent de ta session — agent généraliste, sans contexte
hérité, du modèle fixé ci-dessus —, dont le **seul message** est le texte exact affiché par le bloc A4, copié tel quel. Tu
attends son rapport final sans rien lire de l'espace fermé et sans lui envoyer d'autre message. Pas de second lecteur.

### Bloc A5 — après le verdict A : copie, sceaux, commit, poussée

Sur un rapport « arrêt » du lecteur : pas de bloc A5 ; bloc F seul ; nœud de Lazar.

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
V="$ESPACE_A/verdict-ferme"; cd "$V" || arret "verdict-ferme absent"
ls -1A
[ -z "$(find . -mindepth 1 -type d)" ] || arret "dossier inattendu dans verdict-ferme : rien n'est copié"
n=$(ls -1A | grep -v -E '^verdict-T0\.6-table-A-7b-v1(\.md|-issue\.json|-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md))(\.sha256)?$' | wc -l)
[ "$n" = 0 ] || arret "$n fichier(s) de nom inattendu dans verdict-ferme : rien n'est copié"
[ -f verdict-T0.6-table-A-7b-v1.md ] || arret "verdict en prose absent"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_A" ] || arret "tu n'es pas sur $BR_A"
if [ -e "$BAC/c-verdict-a-v1.txt" ]; then echo "verdict A déjà commité"; else
    for f in $(ls -1A "$V" | grep -v '\.sha256$'); do
        [ -e "docs/verdicts/$f" ] && { cmp -s "$V/$f" "docs/verdicts/$f" || arret "docs/verdicts/$f existe et diffère"; } \
            || { cp "$V/$f" "docs/verdicts/$f" && cmp -s "$V/$f" "docs/verdicts/$f" || arret "copie de $f"; }
        PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "docs/verdicts/$f" || arret "sceau de $f"; done
    git add -- docs/verdicts/verdict-T0.6-table-A-7b-v1*
    git diff --cached --name-only | grep -v -E '^docs/verdicts/verdict-T0\.6-table-A-7b-v1[^/]*$' && arret "index : autre chose que les fichiers du verdict"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    git commit -q -m "T0.6, table A sur 7b : verdict du lecteur neuf, fichiers scellés (session hôte du compte 3)" || arret "commit (relance ce bloc)"
    git rev-parse HEAD > "$BAC/c-verdict-a-v1.txt"; fi
git push -q origin "refs/heads/$BR_A:refs/heads/$BR_A" || arret "poussée du verdict A (relance ce bloc : il reprend à la poussée)"
echo "commit du verdict A : $(cat "$BAC/c-verdict-a-v1.txt")"; git ls-remote origin "refs/heads/$BR_A"
for f in docs/verdicts/verdict-T0.6-table-A-7b-v1*.sha256; do cat "$f"; done
# attendu : noms conformes ; copies égales et scellées ; commit poussé (même commit au distant) ; les compagnons
```

Puis bloc F (journal provisoire) et **rendu à Lazar de la phase A** (section 13). La phase A est close ; la suite attend la
mère.

## 9. Phase B — exécution de la pièce « mots et coût » (gabarit ; version 2 requise)

**Ne joue aucun bloc de cette phase avec cette version.** La pièce n'existe pas au 2026-11-14 (aucun module, aucune ligne
`CODE-MOTS-ET-COUT-T06`). La version 2 de cette commande, contre-lue, remplira : `<<COMMIT_PIECE>>` (commit de `main` qui
porte le code), `<<LIGNE_CODE_MOTS_ET_COUT>>` (la ligne exacte du registre), `<<COMMANDE_PIECE>>` (l'appel exact, une ligne,
racine = ton dépôt, entrées de 7b déjà placées), `<<MOTIF_RUN_PIECE>>` (motif du nom de run qu'elle crée). Forme prévue, à
garder en v2 : branche `verdict/t06-mots-et-cout-compte-3-v1` créée sur `main` ; ligne `CODE-MOTS-ET-COUT-T06` comparée à
l'octet ; entrées de 7b placées depuis `$CLONE7B` (les cinq fichiers de P5.2 des préalables, avec compagnons, jamais
commités) ; sorties `diag/<run-mc>/` et `runs/<run-mc>/` absentes avant ; **un seul appel**, sortie dans `$BAC`, jamais
affichée ; à la fin, les seuls fichiers neufs sont sous `diag/<run-mc>/` et `runs/<run-mc>/`, scellés, commités seuls (aucun
fichier de 7b), poussés ; aucun ouvert. La mère vérifie les blobs, lit l'état de BA-L2 selon le nœud N-C, inscrit
`LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06`.

## 10. Phase C — étape B de T0.7 (après les préalables, jamais avant)

### Bloc C0 — conditions écrites par la mère (lecture seule)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
case "$CONSIGNE_B $EMPREINTE_CONSIGNE_B $REGISTRE_BBIS $CLE_BBIS $R_BA_L2" in
  *'<<'*) arret "marqueur de la phase C non rempli (la mère) : la phase C ne commence pas";; esac
cd "$DEPOT"; git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || arret "récupération de main"
M=refs/remotes/origin/main
for k in AUDIT-FUITES-T07 ISSUE-MOTS-ET-COUT-T06 LECTURE-T08-BASE-A CODE-MOTS-ET-COUT-T06; do
    [ "$(git show "$M:registres/scellements-v1.md" | grep -c "^| $k |")" = 1 ] && echo "ligne $k : une" || arret "ligne $k absente ou en double sur main"; done
[ "$(git show "$M:registres/decisions.md" | grep -c "^| $R_BA_L2 |")" = 1 ] && echo "décision $R_BA_L2 (état de BA-L2) présente" \
    || arret "ligne $R_BA_L2 absente du registre des décisions : l'étape B attend (T0.7, l. 2183)"
[ "$(git show "$M:$REGISTRE_BBIS" 2>/dev/null | grep -c "^| $CLE_BBIS |")" = 1 ] && echo "ligne $CLE_BBIS présente dans $REGISTRE_BBIS" \
    || arret "plan de l'étape B bis non scellé (ligne $CLE_BBIS absente de $REGISTRE_BBIS) : aucune étape B"
[ "$(git show "$M:registres/scellements-v1.md" | grep -c "^| $CLE_BBIS |")" = 0 ] || arret "$CLE_BBIS écrite au registre de T0.7 : nœud"
# attendu : quatre « ligne … : une » ; la décision ; la ligne de B bis ; aucun « ARRÊT » (la décision $R_BA_L2 n'est pas lue
# ici : la mère y a écrit l'état de BA-L2 ou le mot de Lazar)
```

### Bloc C1 — branche neuve, code détaché à C7, interpréteur avec torch (délai maximal)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
cd "$DEPOT"
[ -z "$(git status --porcelain --untracked-files=no)" ] || arret "modifications suivies dans ton dépôt"
[ -z "$(git ls-remote origin "refs/heads/$BR_B")" ] || arret "la branche $BR_B existe déjà au distant (R12)"
if [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] && [ -e "$BAC/c-main-b-v1.txt" ]; then echo "branche $BR_B déjà créée (bloc relancé)"
else git switch -q --no-track -c "$BR_B" refs/remotes/origin/main || arret "création de $BR_B"; git rev-parse HEAD > "$BAC/c-main-b-v1.txt"; fi
git cat-file -e "$C7^{commit}" || arret "commit C7 absent de ton dépôt : rapport à la mère"
git merge-base --is-ancestor "$C7" HEAD || arret "C7 n'est pas un ancêtre de la base de $BR_B"
[ -e "$WT_C7" ] || git worktree add -q --detach "$WT_C7" "$C7" || arret "arborescence détachée à C7"
[ "$(git -C "$WT_C7" rev-parse HEAD)" = "$C7" ] || arret "arborescence C7 : tête autre"
[ -z "$(git -C "$WT_C7" status --porcelain --untracked-files=all -- src/controle_ia)" ] || arret "arborescence C7 : src/controle_ia/ modifié"
echo "code de l'étape B : $WT_C7 (C7, propre)"
if "$PY" -c 'import torch, scipy, numpy' 2>/dev/null; then PYC="$PY"
else L=$(df -Pk "$HOME" | awk 'NR==2{print $4}'); [ "$L" -ge 9437184 ] || arret "place libre $L Kio < 9 Gio : rapport à la mère"
     python3 -m venv "$BAC/venv-c-v1" && "$BAC/venv-c-v1/bin/pip" install -q --disable-pip-version-check -r "$WT_C7/requirements-cpu.txt" \
         && PYC="$BAC/venv-c-v1/bin/python" || arret "interpréteur avec torch"; fi
"$PYC" -c 'import torch, scipy, numpy, sys; print("interpréteur de la phase C :", sys.executable, "torch", torch.__version__, "numpy", numpy.__version__)' \
    || arret "interpréteur de la phase C"
grep -q '^PYC=' "$BAC/variables-v1.sh" || echo "PYC='$PYC'" >> "$BAC/variables-v1.sh"
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" && echo "branche $BR_B poussée (égale à main)" || arret "poussée refusée : rapport à la mère"
# attendu : branche créée ; C7 ancêtre ; « code de l'étape B : … (C7, propre) » ; interpréteur avec torch 2.14.1 ;
# « branche … poussée » ; aucun « ARRÊT »
```

### Bloc C2 — données de l'étape B placées dans la racine (jamais commitées ; délai maximal)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
place() {   # $1 dépôt jetable, $2 tête, $3 chemin : copie à l'octet dans la racine ; jamais sur un fichier suivi
    git -C "$DEPOT" ls-files --error-unmatch -- "$3" >/dev/null 2>&1 && arret "$3 est un fichier suivi de la branche"
    if [ -e "$DEPOT/$3" ]; then           # déjà placé (phase B, ou bloc relancé) : accepté seulement s'il est égal au blob
        git -C "$1" show "$2:$3" | cmp -s - "$DEPOT/$3" && { echo "déjà placé, égal : $3"; return 0; } || arret "$3 existe et diffère du blob"
    fi
    mkdir -p "$DEPOT/$(dirname "$3")"; git -C "$1" show "$2:$3" > "$DEPOT/$3" || arret "extraction de $3"; }
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" | cut -f1)" = "$TETE_7B" ] || arret "tête de $B7B"
[ -e "$CLONE7B" ] || git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$B7B" "$DEPOT_URL" "$CLONE7B" || arret "dépôt jetable de 7b"
for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json runs/$R6/manifeste.json donnees/$R6/mesures-t06.npz \
         donnees/$R6/textes-actions-t06.jsonl; do
    place "$CLONE7B" "$TETE_7B" "$f"; place "$CLONE7B" "$TETE_7B" "$f.sha256"
    (cd "$DEPOT/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$BEA" | cut -f1)" = "$TETE_EA" ] || arret "tête de $BEA"
[ -e "$CLONEEA" ] || git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$BEA" "$DEPOT_URL" "$CLONEEA" || arret "dépôt jetable de l'étape A"
for f in runs/$R7/manifeste.json diag/$R7/sondes-t07.json; do
    place "$CLONEEA" "$TETE_EA" "$f"; place "$CLONEEA" "$TETE_EA" "$f.sha256"
    (cd "$DEPOT/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
S=donnees/$R7/scores-actions-t07.npz; mkdir -p "$MORCEAUX"
for g in $(git -C "$CLONEEA" ls-tree --name-only "$TETE_EA" "donnees/$R7/" | grep -E '/scores-actions-t07\.npz\.morceau(x\.json|-[0-9]{3})(\.sha256)?$'); do
    git -C "$CLONEEA" show "$TETE_EA:$g" > "$MORCEAUX/$(basename "$g")" || arret "extraction de $g"; done
place "$CLONEEA" "$TETE_EA" "$S.sha256"
"$PY" -B - "$MORCEAUX" <<'FIN' || arret "morceaux de scores-actions-t07.npz"
import hashlib, json, pathlib, sys
d = pathlib.Path(sys.argv[1]); m = json.loads((d / "scores-actions-t07.npz.morceaux.json").read_text(encoding="utf-8"))
noms = sorted(p.name for p in d.glob("scores-actions-t07.npz.morceau-[0-9][0-9][0-9]"))
assert [pathlib.Path(x["fichier"]).name for x in m["morceaux"]] == noms, "morceaux nommés ≠ morceaux présents"
for x in m["morceaux"]:
    p = d / pathlib.Path(x["fichier"]).name; h = hashlib.sha256(p.read_bytes()).hexdigest()
    assert h == x["sha256"] == (d / (p.name + ".sha256")).read_text(encoding="utf-8").split()[0], f"empreinte de {p.name}"
    assert p.stat().st_size == x["octets"], f"taille de {p.name}"
assert sum(x["octets"] for x in m["morceaux"]) == m["octets"], "somme des tailles"
print(f"{len(noms)} morceaux conformes, {m['octets']} octets")
FIN
[ ! -e "$DEPOT/$S" ] || arret "$S existe déjà"
cat "$MORCEAUX"/scores-actions-t07.npz.morceau-[0-9][0-9][0-9] > "$DEPOT/$S" || arret "recomposition"
(cd "$DEPOT/donnees/$R7" && sha256sum -c --quiet scores-actions-t07.npz.sha256) || arret "recomposition : empreinte autre que le compagnon"
[ "$(sha256sum "$DEPOT/$S" | cut -d' ' -f1)" = 13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d ] \
    && echo "scores recomposés égaux à la ligne SCORES-T07" || arret "scores recomposés autres que la ligne SCORES-T07"
[ "$(sha256sum "$DEPOT/diag/$R7/sondes-t07.json" | cut -d' ' -f1)" = aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95 ] \
    && echo "sondes-t07.json égal à la ligne SONDES-T07" || arret "sondes-t07.json autre que la ligne SONDES-T07"
# fichier « mots et coût » cité par ISSUE-MOTS-ET-COUT-T06 : placé depuis la branche de la phase B s'il n'est pas sur main
IS=$(git show refs/remotes/origin/main:registres/scellements-v1.md | grep '^| ISSUE-MOTS-ET-COUT-T06 |' | cut -d'|' -f4 | tr -d ' ')
if [ ! -e "$DEPOT/$IS" ]; then
    git fetch --no-tags -q origin "+refs/heads/$BR_P:refs/remotes/origin/$BR_P" || arret "récupération de $BR_P"
    place . "refs/remotes/origin/$BR_P" "$IS"; place . "refs/remotes/origin/$BR_P" "$IS.sha256"; fi
(cd "$DEPOT/$(dirname "$IS")" && sha256sum -c --quiet "$(basename "$IS").sha256") && echo "fichier « mots et coût » présent, compagnon égal" \
    || arret "fichier « mots et coût » : compagnon"
git status --porcelain --untracked-files=no | grep -q . && arret "un fichier suivi a changé"
du -sb "$DEPOT/diag/$R6" "$DEPOT/runs/$R6" "$DEPOT/donnees/$R6" "$DEPOT/runs/$R7" "$DEPOT/donnees/$R7" | awk '{s+=$1} END {print "données placées :", s, "octets"}'
# attendu : compagnons « OK » (silencieux) ; « 3 morceaux conformes, 132091350 octets » ; « scores recomposés égaux … » ;
# « sondes-t07.json égal … » ; « fichier « mots et coût » présent … » ; ≈ 151 000 000 octets ; aucun « ARRÊT »
```

### Bloc C3 — contrôle à blanc complet (lecture seule)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
cd "$BAC"
[ "$(PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.t07.lecture_v4 empreinte-config "$CONFIG_T07")" = 0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12 ] \
    && echo "configuration v8 : empreinte canonique conforme (lecture_v4)" || arret "empreinte canonique de la configuration"
PYTHONPATH="$WT_C7/src" "$PYC" -B "$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/controle_a_blanc_etape_b_compte_3_v1.py" \
    --racine "$DEPOT" --registre "$DEPOT/registres/scellements-v1.md" --config "$CONFIG_T07" \
    --registre-bbis "$DEPOT/$REGISTRE_BBIS" --cle-bbis "$CLE_BBIS" --mode avant-etape-b; K=$?; echo "code $K"
[ "$K" = 0 ] || arret "contrôle à blanc non conforme : aucune étape B ; la mère lève la cause"
# attendu : « 2. … manquantes aucune » ; « refus du registre … : aucun » ; « 3. lignes vérifiées … : n sur n » ;
# « 5. garde adaptée : ouvertures de P3-bis ['pleine'] ; codes aucun » ; « 6. CODE-T07 : commit c2fab6cc7267… ; … 26 fichiers
# conformes » ; fichiers de données « conforme » ; lecture-t07.json et arret-etape-b.json « absent » ; « 8. condition
# d'ordre B bis (…) : REMPLIE » ; « CONTRÔLE À BLANC DE L'ÉTAPE B : TOUT CONFORME » ; « code 0 ». Tout autre : ARRÊT.
```

### Bloc C4 — l'unique appel de l'étape B, puis journal et sortie commités et poussés (un seul appel de l'outil, délai maximal)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
[ ! -e "$BAC/code-etape-b-v1.txt" ] || arret "l'étape B a déjà été appelée : aucun second appel"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
mkdir -p "$ESPACE_B/pieces" "$ESPACE_B/verdict-ferme"
J=registres/scellements-v1.md.ouvertures.md; NJ=$(wc -l < "$J")
cd "$BAC"
PYTHONPATH="$WT_C7/src" "$PYC" -B "$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/controle_a_blanc_etape_b_compte_3_v1.py" \
    --racine "$DEPOT" --registre "$DEPOT/registres/scellements-v1.md" --config "$CONFIG_T07" \
    --registre-bbis "$DEPOT/$REGISTRE_BBIS" --cle-bbis "$CLE_BBIS" --mode avant-etape-b > "$BAC/blanc-avant-appel-v1.txt" 2>&1 \
    || { tail -n 20 "$BAC/blanc-avant-appel-v1.txt"; arret "contrôle à blanc juste avant l'appel : aucune étape B"; }
grep -q "TOUT CONFORME" "$BAC/blanc-avant-appel-v1.txt" && echo "contrôle à blanc juste avant l'appel : tout conforme" || arret "contrôle à blanc"
date -u +"appel de l'étape B : %Y-%m-%dT%H:%M:%SZ"
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.t07.lecture_v4 etape-b "$DEPOT" "$R6" "$R7" "$CONFIG_T07" \
    --registre "$DEPOT/registres/scellements-v1.md" > "$ESPACE_B/sortie-etape-b-v1.txt" 2>&1
CODE=$?; echo "$CODE" > "$BAC/code-etape-b-v1.txt"; echo "code de l'étape B : $CODE (sortie gardée dans l'espace fermé, non affichée)"
cd "$DEPOT"
echo "lignes ajoutées au journal : $(( $(wc -l < "$J") - NJ ))"
[ "$CODE" = 2 ] && { echo "ligne de refus :"; tail -n 1 "$J"; }
# commit 1 : le journal seul (la mère le recopie dans main)
git add -- "$J"
git diff --cached --name-only | grep -v -x -F "$J" && arret "index : autre chose que le journal"
n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
git diff --cached --quiet || { git commit -q -m "T0.7, étape B : journal des ouvertures (code $CODE ; session hôte du compte 3)" && git rev-parse HEAD > "$BAC/c-journal-b-v1.txt"; }
# commit 2 : la sortie du module (lecture unique ou arrêt), sans les données placées
for f in "diag/$R7/lecture-t07.json" "diag/$R7/arret-etape-b.json"; do [ -e "$f" ] && git add -- "$f" "$f.sha256"; done
git diff --cached --name-only | grep -v -E "^diag/$R7/(lecture-t07|arret-etape-b)\.json(\.sha256)?$" && arret "index : autre chose que la sortie du module"
n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
git diff --cached --quiet || { git commit -q -m "T0.7, étape B : sortie scellée du module (code $CODE)" && git rev-parse HEAD > "$BAC/c-sortie-b-v1.txt"; }
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" || arret "poussée (relance un bloc qui ne fait que : git push -q origin refs/heads/$BR_B:refs/heads/$BR_B)"
git ls-remote origin "refs/heads/$BR_B"
for f in "diag/$R7/lecture-t07.json" "diag/$R7/arret-etape-b.json"; do [ -e "$f" ] && echo "$f : $(cut -d' ' -f1 "$f.sha256")"; done
# attendu (code 0) : « contrôle à blanc … tout conforme » ; « code de l'étape B : 0 » ; deux lignes ajoutées au journal
# (OUVERTURE-T07 de l'étape B, puis l'ouverture des scores) ; deux commits poussés ; l'empreinte de lecture-t07.json.
# Code 2 : refus, ligne REFUS-T07 affichée, commitée, poussée ; arrêt ; la mère lève la cause et donne, par écrit, le mot de
# relance (aucune relance sans lui). Code 3 : arret-etape-b.json commité, poussé ; nœud de Lazar ; aucune relance.
```

### Bloc C5 — pièces du lecteur B et bordereau (code 0 seulement)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
[ "$(cat "$BAC/code-etape-b-v1.txt")" = 0 ] || arret "étape B sans lecture (code $(cat "$BAC/code-etape-b-v1.txt")) : aucun lecteur"
P="$ESPACE_B/pieces"; cd "$DEPOT"
IS=$(grep '^| ISSUE-MOTS-ET-COUT-T06 |' registres/scellements-v1.md | cut -d'|' -f4 | tr -d ' ')
for f in prereg/T0.7-sondes-v0-v1.md prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json \
         prereg/T0.6-organismes-v0-v1.md prereg/T0.8-base-A-mots-et-cout-v1.md prereg/T0.7-consigne-audit-fuites-v1.md \
         docs/decisions/decision-N-063-v2.md docs/verdicts/verdict-P3-bis-v1-issue.json "$CONSIGNE_B" \
         "diag/$R7/lecture-t07.json" "diag/$R7/audit-fuites-t07.json" "$IS"; do
    cp --parents "$f" "$f.sha256" "$P/" || arret "copie de $f"
    [ "$(cut -d' ' -f1 "$P/$f.sha256")" = "$(sha256sum "$P/$f" | cut -d' ' -f1)" ] || arret "compagnon de $f"; done
[ "$(sha256sum "$P/$CONSIGNE_B" | cut -d' ' -f1)" = "$EMPREINTE_CONSIGNE_B" ] || arret "consigne du lecteur B autre que l'empreinte"
C=$(cat "$BAC/c-main-b-v1.txt")
{ echo "# Extrait des registres pour le lecteur de l'étape B (v1)"; echo; echo "Commit de main : $C ; journal de la branche : $(cat "$BAC/c-journal-b-v1.txt")."
  echo; echo "## registres/scellements-v1.md"; grep -n '^| ' registres/scellements-v1.md
  echo; echo "## registres/scellements-v1.md.ouvertures.md (lignes de l'étape B)"; grep -n 'etape-B\|scores-t07' registres/scellements-v1.md.ouvertures.md
  echo; echo "## registres/decisions.md (état de BA-L2)"; git show "$C:registres/decisions.md" | grep -n "^| $R_BA_L2 |"
} > "$P/extrait-registres-etape-b-v1.md"
(cd "$P" && find . -type f -print0 | sort -z | xargs -0 sha256sum) > "$ESPACE_B/bordereau-remise-v1.txt"
n=$(cut -c67- "$ESPACE_B/bordereau-remise-v1.txt" | grep -c -i -E 'bbis|b-bis|etape-b-bis|lecture-sondes|resume\.json|scores-actions|activations|adaptateur|sondes-neuves|bras-attaque|mode-tenu|anteriorite-bras|etiqueteur|quarantaine|mesure-unanime')
[ "$n" = 0 ] && echo "conforme : aucun nom interdit parmi les pièces (rien de l'étape B bis)" || arret "$n nom(s) interdit(s) parmi les pièces : rien n'est remis"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$ESPACE_B/bordereau-remise-v1.txt" || arret "sceau du bordereau"
echo "pièces : $(wc -l < "$ESPACE_B/bordereau-remise-v1.txt") fichiers ; bordereau $(cut -d' ' -f1 "$ESPACE_B/bordereau-remise-v1.txt.sha256")"
# attendu : douze fichiers et leurs compagnons conformes ; « aucun nom interdit … » ; l'empreinte du bordereau
```

### Bloc C6 — message de remise et création du lecteur B

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
NOTE_MODELE="modèle C"      # « modèle A, faute de C » si ton outil d'agent ne peut pas créer un sous-agent du modèle C
sed -e 's/de la table A de T0.6 sur la course 7b/de l'"'"'étape B de T0.7 (critère 3 de G0)/' \
    -e 's#- Run : 20261111-151701-t06-reel\.#- Runs : 20261111-151701-t06-reel (7b) et 20261114-001352-t07-lecture-reel (T0.7).#' \
    -e '/^- Constat de l.hôte sur les noms/d' -e 's/(ni le dépôt, ni aucun fichier de T0.7, ni rien de l.étape B bis)/(ni le dépôt, ni les scores, ni rien de l'"'"'étape B bis)/' \
    "$BAC/message-remise-a-gabarit-v1.txt" > "$BAC/message-remise-b-gabarit-v1.txt"
grep -q "étape B de T0.7 (critère 3 de G0)" "$BAC/message-remise-b-gabarit-v1.txt" && ! grep -q "Constat de l" "$BAC/message-remise-b-gabarit-v1.txt" \
    && grep -q "ni les scores" "$BAC/message-remise-b-gabarit-v1.txt" || arret "gabarit du message B"
ESPACE="$ESPACE_B" BORDEREAU="$(cut -d' ' -f1 "$ESPACE_B/bordereau-remise-v1.txt.sha256")" PYV="$PY" NOTE="$NOTE_MODELE" \
  CONS="$CONSIGNE_B" ECONS="$EMPREINTE_CONSIGNE_B" \
  "$PY" -B - "$BAC/message-remise-b-gabarit-v1.txt" "$BAC/message-remise-b-v1.txt" <<'FIN' || arret "message de remise B"
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
cd "$DEPOT" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$BAC/message-remise-b-v1.txt" || arret "sceau du message B"
cat "$BAC/message-remise-b-v1.txt"
```

**Création du lecteur B** : comme le lecteur A (agent neuf, sans contexte hérité, seul message = le texte affiché), **jamais
le même agent que le lecteur A**.

### Bloc C7 — après le verdict B : copie, sceaux, commit, poussée

Sur un rapport « arrêt » du lecteur B : pas de bloc C7 ; bloc F seul ; nœud de Lazar.

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
V="$ESPACE_B/verdict-ferme"; cd "$V" || arret "verdict-ferme absent"
ls -1A
[ -z "$(find . -mindepth 1 -type d)" ] || arret "dossier inattendu dans verdict-ferme : rien n'est copié"
n=$(ls -1A | grep -v -E '^verdict-T0\.7-etape-B-v1(\.md|-issue\.json|-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md))(\.sha256)?$' | wc -l)
[ "$n" = 0 ] || arret "$n fichier(s) de nom inattendu dans verdict-ferme : rien n'est copié"
[ -f verdict-T0.7-etape-B-v1.md ] || arret "verdict en prose absent"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
if [ -e "$BAC/c-verdict-b-v1.txt" ]; then echo "verdict B déjà commité"; else
    for f in $(ls -1A "$V" | grep -v '\.sha256$'); do
        [ -e "docs/verdicts/$f" ] && { cmp -s "$V/$f" "docs/verdicts/$f" || arret "docs/verdicts/$f existe et diffère"; } \
            || { cp "$V/$f" "docs/verdicts/$f" && cmp -s "$V/$f" "docs/verdicts/$f" || arret "copie de $f"; }
        PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "docs/verdicts/$f" || arret "sceau de $f"; done
    git add -- docs/verdicts/verdict-T0.7-etape-B-v1*
    git diff --cached --name-only | grep -v -E '^docs/verdicts/verdict-T0\.7-etape-B-v1[^/]*$' && arret "index : autre chose que les fichiers du verdict"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    git commit -q -m "T0.7, étape B : verdict du lecteur neuf, fichiers scellés (session hôte du compte 3)" || arret "commit (relance ce bloc)"
    git rev-parse HEAD > "$BAC/c-verdict-b-v1.txt"; fi
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" || arret "poussée du verdict B (relance ce bloc : il reprend à la poussée)"
echo "commit du verdict B : $(cat "$BAC/c-verdict-b-v1.txt")"; git ls-remote origin "refs/heads/$BR_B"
for f in docs/verdicts/verdict-T0.7-etape-B-v1*.sha256; do cat "$f"; done
# attendu : noms conformes ; copies égales et scellées ; commit poussé (même commit au distant) ; les compagnons
```

## 11. Bloc F — journal provisoire, passation, nettoyage (à la fin de chaque phase jouée)

```bash
. "$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh" || exit 1
RAPPORTS=$(cat <<'FIN'
<rapports finaux des lecteurs, tels quels, à la place de cette ligne>
FIN
)
CROCHET='<bloquée | passée>'; MODELES='lecteurs : <modèle C | modèle A, faute de C> ; session hôte : <modèle A | modèle C> ; identités dites en conversation seulement'
case "$RAPPORTS$CROCHET$MODELES" in *'<rapports finaux'*|*'<bloquée | passée>'*|*'<modèle C | modèle A'*|*'<modèle A | modèle C>'*)
    arret "variables de tête non remplies";; esac          # les seuls gabarits ; un « < » d'un rapport ne compte pas
lire() { cat "$1" 2>/dev/null || echo "sans objet"; }
cd "$DEPOT"; B=$(git rev-parse --abbrev-ref HEAD)
case "$B" in "$BR_A"|"$BR_B") ;; *) arret "branche courante $B : ni $BR_A ni $BR_B";; esac
mkdir -p registres-provisoires; N="registres-provisoires/compte-3-lecteurs-$(date -u +%Y-%m-%d-%H%M)-v1.md"
{ echo "# Compte 3 — session hôte des lecteurs de 7b et de l'étape B — journal provisoire (v1)"; echo
  echo "Écrit le $(date -u +%Y-%m-%dT%H:%M:%SZ) (\`date -u\`) par la session \`$SESSION_C3\`, branche \`$B\` ; identifiants provisoires P3L-…, à numéroter par la mère."; echo
  echo "- P3L-001 : commande exécutée depuis $(lire "$BAC/debut-v1.txt") ; épreuve du crochet : $CROCHET ; $MODELES ; liste \`$LISTE\` (\`$EMPREINTE_LISTE\`) : attestation conforme."
  echo "- P3L-002 : phase A — base main \`$(lire "$BAC/c-main-a-v1.txt")\` ; bordereau \`$(cut -d' ' -f1 "$ESPACE_A/bordereau-remise-v1.txt.sha256" 2>/dev/null)\` ; message \`$(cut -d' ' -f1 "$BAC/message-remise-a-v1.txt.sha256" 2>/dev/null)\` ; verdict commité \`$(lire "$BAC/c-verdict-a-v1.txt")\`."
  echo "- P3L-003 : phase C — base main \`$(lire "$BAC/c-main-b-v1.txt")\` ; code de l'étape B : $(lire "$BAC/code-etape-b-v1.txt") ; journal \`$(lire "$BAC/c-journal-b-v1.txt")\` ; sortie \`$(lire "$BAC/c-sortie-b-v1.txt")\` ; bordereau \`$(cut -d' ' -f1 "$ESPACE_B/bordereau-remise-v1.txt.sha256" 2>/dev/null)\` ; verdict commité \`$(lire "$BAC/c-verdict-b-v1.txt")\`."
  echo "- P3L-004 : rapports finaux des lecteurs :"; printf '%s\n' "$RAPPORTS" | sed 's/^/    /'
  echo "- P3L-005 : cette session n'a ouvert aucun résultat ; elle est exclue de l'analyse de ces verdicts, de l'étape B bis, de T0.8 et de G0."
} > "$N"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$N" || arret "sceau"
git add -- "$N" "$N.sha256"
[ "$(git diff --cached --name-only | grep -vc '^registres-provisoires/')" = 0 ] || arret "index : autre chose que registres-provisoires/"
n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
git commit -q -m "Compte 3 : journal provisoire de la session hôte des lecteurs" || arret "commit"
git push -q origin "refs/heads/$B:refs/heads/$B" || arret "poussée"
echo "RENDU — branche $B ; tête $(git rev-parse HEAD)"; sha256sum "$N"
# nettoyage, seulement après la phase C poussée : données placées retirées par chemins exacts, arborescence C7 retirée
if [ "$B" = "$BR_B" ] && [ -e "$BAC/c-verdict-b-v1.txt" ]; then
    IS=$(grep '^| ISSUE-MOTS-ET-COUT-T06 |' registres/scellements-v1.md | cut -d'|' -f4 | tr -d ' ')
    for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json runs/$R6/manifeste.json donnees/$R6/mesures-t06.npz \
             donnees/$R6/textes-actions-t06.jsonl runs/$R7/manifeste.json diag/$R7/sondes-t07.json donnees/$R7/scores-actions-t07.npz $IS; do
        git ls-files --error-unmatch -- "$f" >/dev/null 2>&1 || rm -f -- "$f" "$f.sha256"; done
    git worktree remove "$WT_C7" && echo "données placées retirées ; arborescence C7 retirée"; fi
```

## 12. Ce que tu ne fais jamais ici

Lire une sortie ; lancer l'extracteur ; rapatrier `lecture-sondes-t06.json`, `resume.json`, des activations ou des
adaptateurs ; appeler `lecture_v3` ; appeler l'étape B depuis `main` ou deux fois ; écrire dans `registres/` hors du journal
écrit par le module ; remettre à un lecteur une pièce de l'étape B bis ; écrire un identifiant de modèle dans un fichier.

## 13. Rendu à Lazar (après chaque phase ; il le transmet à la mère)

1. Une à trois lignes : « Phase A : verdict du lecteur neuf (<modèle C | modèle A, faute de C>) scellé et poussé sur
   `verdict/t06-table-a-7b-compte-3-v1` ; rien d'autre lu. » — ou « Phase C : étape B appelée une fois, code <n> ; … » — ou, sur
   un arrêt, le bloc et le motif seuls.
2. **À transmettre à la mère** : la sortie « RENDU » du bloc F (branche, tête, empreinte du journal provisoire), les commits
   (`c-*-v1.txt`), les empreintes des fichiers du verdict, du bordereau et du message ; pour la phase C, le code de l'étape B et
   le nombre de lignes ajoutées au journal ; le résultat de l'épreuve du crochet.
3. Erreurs, écarts : une ligne chacun. Aucune analyse des verdicts.

## 14. Ce qui arrête tout

- Tout « ARRÊT » d'un bloc. **Avant le bloc A4, rien d'irréversible n'a eu lieu** (hors le nom de la branche poussée) : tu le
  dis à Lazar (bloc et motif) et rien d'autre ; un arrêt au bloc 1 : tu peux effacer `$BAC` et relancer le bloc 1 une fois.
- Identifiant de session introuvable au bloc 1 : remplace `SESSION_C3=…` par celui que donne l'outil qui décrit ta session (ou
  la ligne « Claude-Session » de tes consignes d'attribution), puis relance le bloc 1 ; sinon, arrêt.
- Attestation non conforme, tête de branche autre, compagnon faux, nom interdit extrait ou parmi les pièces : rien n'est remis ;
  la mère tranche.
- Bloc C0 ou C3 non conforme : **aucune étape B** ; la mère lève la cause.
- Étape B : code 2 (refus, attente : relance sur le même run seulement sur un mot écrit de la mère) ; code 3 (nœud de Lazar,
  aucune relance) ; outil qui rend la main sans « code de l'étape B : … » : tu ne relances rien ; un seul appel pour relever
  `ls diag/$R7/` (noms) et `tail -n 3` du journal, puis rapport (nœud).
- Rapport d'un lecteur « arrêt » : rien n'est commité ; nœud de Lazar.
- Ouverture fautive d'un fichier interdit par ta session : déclarée aussitôt à la mère ; le verdict concerné n'est pas inscrit.
- Refus de permission, du crochet ou d'un classifieur, poussée refusée : arrêt, rapport à la mère, aucun contournement.

## 15. Ce que fait la mère ensuite (pour mémoire ; tu ne le fais pas)

1. **Phase A** : récupère `verdict/t06-table-a-7b-compte-3-v1` par refspec ; vérifie que le commit du verdict a pour parent la
   base rendue et n'ajoute que `docs/verdicts/verdict-T0.6-table-A-7b-v1*` (et, dans un commit à part, le journal provisoire) ;
   recopie à l'octet dans `main` (même blob), rescelle, consigne au registre des décisions, met à jour la liste « qui a lu
   quoi » (hôte : rien ouvert ; lecteur A : pièces du bordereau), soumet le verdict à Lazar. Aucune ligne de verdict dans
   `registres/scellements-v1.md` (une clé sans marque déclarée y ferait refuser l'étape B).
2. **Phase B** (version 2) : vérifie les blobs des sorties de la pièce par empreinte, sans les ouvrir ; lit l'état de BA-L2
   selon le nœud N-C ; inscrit `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` ; consigne la ligne `<<R_BA_L2>>`.
3. **Phase C** : recopie dans `main` le seul commit du journal (`registres/scellements-v1.md.ouvertures.md`, même blob) **avant
   toute autre écriture dans ce journal** ; la sortie `lecture-t07.json` reste sur la branche, comme les sorties de l'étape A
   restent sur `donnees/t07-etape-a-v1` (ou la mère décide de la recopier) ; recopie les fichiers du verdict B ; liste « qui a
   lu quoi » ; soumet le verdict à Lazar ; transmet à l'étape B bis **rien** de cette branche avant le verdict scellé de B bis.

## Annexe — essais et limites (règle R5)

- **Contrôle à blanc** : `essai_controle_a_blanc_etape_b_compte_3_v1.sh` (28 conformes sur 28, racine jouet et registres
  réels en copie) ; sur l'état actuel de `main` : aucun refus, deux clés manquantes (`prealables-v1.md`, § 4).
- **Attestation** : `essai_attestation_compte_3_v1.sh` (9 conformes sur 9 ; liste réelle v1 : conforme, une ligne du compte 3
  sans exclusion).
- **Répétitions partielles** : bloc C2 sur dépôts jouets (`repetition_bloc_c2_jouet_v1.sh`, 7 conformes sur 7 : placement par
  liste positive, trois morceaux vérifiés et recomposés, fichier « mots et coût » pris sur la branche de la phase B, fichier
  fermé jamais placé, aucun fichier suivi touché, reprise sur fichiers déjà placés, arrêt sur fichier altéré et sur tête autre ;
  limite : transport local) ; blocs 1, 2, A4 et C6 joués sur un dossier jouet (bloc 2 : la session mère, présente dans la
  liste v1, est arrêtée par l'attestation ; A4 et C6 : messages sans marqueur restant ; C6 s'arrête si les marqueurs de la
  phase C ne sont pas remplis).
- **Limite** : les autres blocs (A1, A2, A3, A5, C0, C1, C3, C4, C5, C7, F) **n'ont pas été répétés** (le rédacteur n'a rapatrié
  aucune sortie) ; syntaxe vérifiée par `bash -n` pour les 18 blocs. Une répétition de bout en bout sur une copie du dépôt et
  des branches jouets, comme celle de la commande de P3-bis (32 sur 32), est recommandée avant la remise de la phase C
  (rapport, D-3).
