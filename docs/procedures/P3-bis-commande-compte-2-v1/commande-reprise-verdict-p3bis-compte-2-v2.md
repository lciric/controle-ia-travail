# Commande de reprise au compte 2 — verdict de P3-bis après perte de la session hôte — v2

- **Statut** : commande écrite de la session mère au compte 2, sur mot de Lazar du 2026-11-14 (R-2696, verbatim :
  « Recommandation : (1), confiance 0,7, comme le contre-lecte : go » ; nœud C4 (b) de R-2695). **Elle ne sert que dans un
  cas** : la session du compte 2 qui exécutait la commande d'ouverture (`commande-ouverture-verdict-p3bis-compte-2-v2.md`,
  `04ea3325…`) a été perdue **après** la poussée de la ligne `OUVERTURE-P3BIS` sur `verdict/p3bis-compte-2-v1` et **avant**
  la poussée du verdict. Le bloc 2 établit par programme que l'ouverture est poussée et qu'aucun verdict ni aucune
  passation ne l'est ; **il ne peut pas établir que la session d'origine est perdue** : une session vivante, dont le
  lecteur travaille encore, donne le même état. La perte se dit par Lazar, en conversation, en te remettant cette
  commande (session close ou conteneur détruit, et depuis quand) : sans ce mot, tu ne commences pas ; tu le recopies mot
  pour mot au bloc 8. Si ta conversation est celle qui a exécuté la commande d'ouverture, tu t'arrêtes : il faut une
  session neuve. Avant le bloc 1, vérifie que le texte collé est le fichier scellé dont Lazar te donne le chemin et
  l'empreinte. À coller par Lazar comme
  premier message d'une **session neuve** du compte 2, ouverte dans le dossier du dépôt. Aucune dépense ; aucun texte
  scellé changé ; aucun critère ajouté. Si elle contredit le module scellé, le module fait foi : tu t'arrêtes et tu le dis.
- **Version 2** : la version 1 (`commande-reprise-verdict-p3bis-compte-2-v1.md`, `fdc043c2…`, gardée, R12) corrigée selon
  sa contre-lecture (`contre-lecture-commande-reprise-compte-2-v1.md`, `9e6fe5ca…`, modèle B, « prête après corrections »,
  R-2701) : R1, R2 et R3 appliquées telles que données ; m4 (répétition) appliqué ; m3 noté pour la mère (annexe A) ;
  m5 et m6 dans R2 (a). La commande d'ouverture v2 n'est pas changée.
- **Ce qu'elle fait** : récupérer les **mêmes** paquets (`calcul/p3bis-reel-v2`, refspec explicite), vérifiés **à
  l'égalité** aux deux empreintes de la ligne d'ouverture du journal poussé ; les redéplier par les seules fonctions
  `lire_paquets` et `extraire` du module de S, **sans appeler `ouvrir` et sans écrire aucune ligne au journal** ; les remettre
  à un sous-agent lecteur **neuf** (jamais celui de la session perdue) ; déclarer l'écart en tête du verdict et le proposer
  au registre.
- **Rédacteur** : sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (modèle A, celui des auteurs de
  P3-bis), le 2026-11-14 de 10:00Z à 10:09Z pour la v1, de 10:12Z à 10:20Z pour la v2 (`date -u`) ; ni lecteur ni auteur du verdict ; aucun paquet ouvert ; de
  `calcul/p3bis-reel-v2`, la tête seule par `git ls-remote`.
- **Sigles** : UTC = temps universel coordonné ; « empreinte » = condensé sha256 ; « compagnon » = fichier `.sha256`
  voisin (R6) ; S = révision `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` ; « module, l. » = `ouverture_p3bis_v3.py` de S
  (`4a54a437…`) ; « texte, l. » = `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`).
- **Pièces** (même dossier, scellées) :

| pièce | empreinte | rôle |
|---|---|---|
| `controle_a_blanc_compte_2_v1.py` | `1a9dce715b5fde593119b32bd61c5ca3a9d8e476a02bbf72425fa54b967a5a62` | sa fonction `attester` seulement (bloc 2) |
| `repetition_reprise_jouet_v2.sh` | `56f9c40887afadfc4cac237212409a874b46e6d3a4db4cda329b27951ff164e7` | répétition sur jouet de **cette version 2** : ouverture simulée par la vraie garde (paquet daté avant les lignes d'écrit : trois réserves), perte simulée, arrêts du constat, reprise (annexe B) |
| `repetition-reprise-jouet-sortie-v2.txt` | `43d2f8de779f9f6f758fe6b20dad9037654076184353ba0881119a27aa4cff92` | sa sortie : « BILAN : 37 conformes sur 37 » |
| `repetition_reprise_jouet_v1.sh`, `repetition-reprise-jouet-sortie-v1.txt` | `f70bae22…`, `98f4f9cd…` | répétition de la v1 (gardée, R12) |
| `contre-lecture-commande-reprise-compte-2-v1.md` | `9e6fe5cacf2e9c987df73ba7aa893e999a552eb9c29b9b69fa2a83d05e3a0412` | contre-lecture de la v1 (modèle B, R-2701) |

## 0. D'abord, pour Lazar et la mère

1. **Fonctions de S, vérifiées dans le module** : `lire_paquets(racine_paquets, run)` (l. 1237-1259) ne lit que sous
   `racine_paquets` — paquet des lectures et son compagnon (`verifier`), relecture (taille, sel, longueur, flux), index du
   second paquet et son compagnon, morceaux par `relire_run` (l. 503-535) — et rend les fichiers des deux paquets en
   mémoire avec la cellule `"<empreinte du paquet des lectures> <empreinte du second paquet>"` ; sur un défaut, elle **lève**
   `RefusOuverture` (`paquet-faux`) sans rien écrire (la classe, l. 205-213, ne fait que porter le motif). `extraire(fichiers,
   sortie)` (l. 1262-1273) écrit les fichiers dans un dossier caché créé dans le parent de `sortie`, puis le renomme en
   `sortie` ; elle ne vérifie pas que `sortie` est absent (c'est `ouvrir` qui le fait, l. 1286-1287) : le bloc 4 l'exige donc
   lui-même, un renommage sur un dossier vide existant réussissant sous Linux. Le journal n'est écrit que par `inscrire`
   (l. 851-872), appelée **seulement** par `ouvrir` (l. 1304 et 1308) : ni `lire_paquets` ni `extraire` n'y touchent. Le
   bloc 4 le contrôle en plus par l'empreinte du journal avant et après.
2. **Écart** : un redépliage hors de la garde. Le texte, l. 1981-1983, recopié à l'octet : « **Toute ouverture hors de la
   garde** (fichier du paquet extrait ou lu, fichier de la classe 2 ouvert, fichier de lecture commité en clair, avant une
   ouverture autorisée) : consignée comme écart (date, qui, quoi) ; la réserve « résultat de P3-bis exposé avant les
   scores de T0.7 » est écrite au verdict et transmise à T0.7. » Ici le redépliage vient **après** l'ouverture autorisée
   (journalisée et poussée) et après les scores de T0.7 : lecture assumée par Lazar (R-2696) ; l'écart est consigné (date,
   qui, quoi) en tête du verdict et proposé au registre (bloc 8).
3. **Points que le mot de Lazar ne couvre pas explicitement** (annexe A) : la sortie d'origine de la garde (ses lignes
   « réserve : … ») est perdue avec la session ; la commande la **reconstitue par programme** (mêmes fonctions et même
   format que le module) dans un fichier au nom neuf, que la consigne du lecteur ne nomme pas ; et la liste « qui a lu
   quoi » ne doit porter aucune ligne au compte 2 (ou la mère adapte l'attestation).

## 1. Interdits

Mêmes interdits et même isolement que la commande d'ouverture version 2 (section 1), recopiés ici :

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`,
  `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur,
  `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ;
  fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit : `n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] && git commit …`
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner
  `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur :
  arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Exception de cette commande (R-2673, R-2696)** : `calcul/p3bis-reel-v2` est récupérée par le seul bloc 3 (refspec
explicite, sans contenu, puis liste positive) ; ses paquets ne sont lus que par `lire_paquets` (bloc 4), pour le seul
lecteur neuf du verdict, que tu héberges.

**Ajoutés** : rien de 7a, 7b, T0.6 ni T0.7 (cette commande ne touche aucun fichier de T0.7 : ni compagnon, ni texte, la
garde n'étant pas appelée) ; tu ne lis rien de ce qui est redéplié, ni le verdict, ni les fichiers de travail du lecteur
(seules lectures : taille et empreinte du second paquet dans son index, le chemin de `lecture-p3bis.json` pour
`exposer-issue`, les noms des fichiers de `verdict-ferme/`) ; **jamais `ouvrir`**, sous aucun mode ; aucune ligne écrite au
journal, par aucun moyen ; aucune analyse du verdict après l'avoir rendu, exclusion ensuite comme pour l'ouverture ; tu
n'écris pas dans `registres/` ; aucune poussée hors de `verdict/p3bis-compte-2-reprise-v1` ; tu ne touches pas
`verdict/p3bis-compte-2-v1` (lecture seule) ; jamais le premier lecteur ni aucun fichier de la session perdue ; les seuls
`find` portent sur des dossiers que cette commande crée.

## 2. Qui fait quoi, et mode d'emploi

- **Toi, session hôte neuve du compte 2** : blocs 1 à 8, dans l'ordre, chacun dans un seul appel de ton outil de commande,
  tel quel ; chaque bloc relit `$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh`. Une ligne « ARRÊT : » : tu t'arrêtes
  (section 4). Délai maximal de l'outil (dix minutes) pour les blocs 3 et 4, au premier plan. Quota au-dessus de 80 % : tu
  ne commences pas.
- **Le lecteur** : **un** sous-agent neuf de ta session, sans contexte hérité, du **modèle B** que Lazar te nomme en
  conversation (identités jamais écrites dans un fichier, R-2598) ; à défaut, modèle A, et le verdict le dit. Jamais le
  lecteur de la session perdue, jamais un agent qui a vu ses fichiers.
- **La mère** (après ta poussée) : recopie dans `main` le journal (commit de `verdict/p3bis-compte-2-v1`) s'il n'y est pas,
  puis le verdict de ta branche, rescelle, inscrit `VERDICT-P3BIS`, consigne l'écart, met à jour la liste « qui a lu quoi ».
- **Épreuve du crochet**, seule, dans un appel à part, avant le bloc 1 : `sha256sum
  scripts/lancer_course_ideation_bassins_etroits_v2.py` — attendue bloquée ; sinon, note-le (bloc 8) ; rien de payant ici.

## 3. Blocs

### Bloc 1 — variables

```bash
export LC_ALL=C.UTF-8
arret() { echo "ARRÊT : $*"; exit 1; }
date -u +"début : %Y-%m-%dT%H:%M:%SZ"
DEPOT=$(git rev-parse --show-toplevel) || arret "lance ce bloc depuis le dossier du dépôt"
case "$(git -C "$DEPOT" remote get-url origin)" in
  *lciric/controle-ia-travail*) echo "dépôt : $DEPOT";; *) arret "dépôt d'origine autre que lciric/controle-ia-travail";; esac
BAC="$HOME/bac-p3bis-reprise-compte-2-v1"
[ ! -e "$BAC" ] || arret "$BAC existe déjà : rapport à la mère"
git -C "$HOME" rev-parse --show-toplevel >/dev/null 2>&1 && arret "$HOME est dans un arbre git"
SESSION_C2="session_${CLAUDE_CODE_REMOTE_SESSION_ID#cse_}"
[[ "$SESSION_C2" =~ ^session_[0-9A-Za-z]{10,}$ ]] || arret "identifiant de session introuvable (section 4)"
mkdir -p "$BAC" && date -u +%Y-%m-%dT%H:%M:%SZ > "$BAC/debut-v1.txt"
if "$DEPOT/.venv/bin/python" -c 'import numpy' 2>/dev/null; then PY="$DEPOT/.venv/bin/python"
else python3 -m venv "$BAC/venv-v1" && "$BAC/venv-v1/bin/pip" install -q --disable-pip-version-check numpy==2.4.6 \
     && PY="$BAC/venv-v1/bin/python" || arret "interpréteur"; fi
"$PY" -c 'import numpy, sys; print("interpréteur :", sys.executable, sys.version.split()[0], "numpy", numpy.__version__)' || arret "numpy"
cat > "$BAC/variables-v1.sh" <<EOF
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
arret() { echo "ARRÊT : \$*"; exit 1; }
DEPOT='$DEPOT'; BAC='$BAC'; PY='$PY'; SESSION_C2='$SESSION_C2'
LISTE='registres/qui-a-lu-quoi-v1.md'; EMPREINTE_LISTE='9eb15acba4ef6e4f3ff1f6b30fbcef7557e58b5c8aafa9bc6bbe843c89c0d7ae'   # R-2692
ESPACE="\$BAC/p3bis-espace-ferme-reprise-v1"; CLONE="\$ESPACE/clone-calcul-p3bis-reel-v2"; SORTIE="\$ESPACE/paquets-ouverts"
PIECES="\$ESPACE/pieces"; VERDICT_FERME="\$ESPACE/verdict-ferme"; M="\$BAC/module-s-v1"
ICI="\$DEPOT/docs/procedures/P3-bis-commande-compte-2-v1"
RUN=20261113-121129-p3bis-reel; S=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0
TETE_CALCUL=2aaaaf872356e51272a36e670d348603a31f32f3
PAQUET_LECTURES=0fb83f67e92b8041294a47448990e828a9dcea87b97cab80bc79da3919bc12f1     # R-2684
BRANCHE_OUV=verdict/p3bis-compte-2-v1; BRANCHE=verdict/p3bis-compte-2-reprise-v1
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git; MODULE=controle_ia.premier_test_ia.ouverture_p3bis_v3
APPUI="SCORES-T07=13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d SONDES-T07=aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95"
EOF
echo "session : $SESSION_C2"
# attendu : dépôt, interpréteur avec numpy, session « session_… » ; aucun « ARRÊT »
```

### Bloc 2 — constat de perte, établi par programme ; attestation ; branche de reprise

Le cas est établi si et seulement si : la branche `verdict/p3bis-compte-2-v1` existe au distant ; elle porte le journal
au format attendu, dont la **seule** ligne `OUVERTURE-P3BIS` est la dernière, en mode `pleine`, à l'appui attendu, avec
le paquet des lectures `0fb83f67…12f1` ; **aucun** fichier `docs/verdicts/verdict-P3-bis-v1*` n'est sur cette branche ni
sur `main` ; aucune ligne `VERDICT-P3BIS` sur `main` ; le journal de `main`, s'il existe, est le même blob.

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
date -u +%Y-%m-%dT%H:%M:%SZ
D=$(curl -sS --max-time 20 -D - -o /dev/null https://pypi.org/simple/numpy/ 2>/dev/null | tr -d '\r' | awk -F': ' 'tolower($1)=="date"{print $2}' | tail -1)
[ -n "$D" ] || arret "horloge de référence injoignable"
E=$(( $(date -u +%s) - $(date -u -d "$D" +%s) )); echo "écart de l'horloge à pypi.org : $E s"; [ "${E#-}" -le 120 ] || arret "horloge décalée"
(cd "$DEPOT/docs" && sha256sum -c --quiet sha256sums-lancement-v2.txt) && echo "empreintes de lancement conformes" || arret "empreintes de lancement"
cd "$DEPOT"
[ -z "$(git status --porcelain --untracked-files=no)" ] || arret "modifications suivies dans ton dépôt"
[ -n "$(git config user.name)" ] && [ -n "$(git config user.email)" ] || arret "identité git absente"
git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || arret "récupération de main"
git fetch --no-tags -q origin "+refs/heads/$BRANCHE_OUV:refs/remotes/origin/$BRANCHE_OUV" \
    || arret "branche $BRANCHE_OUV absente : aucune ouverture poussée, cette commande ne s'applique pas"
O="refs/remotes/origin/$BRANCHE_OUV"; J=registres/ouvertures-p3bis-v1.md
git show "$O:$J" > "$BAC/journal-branche-v1.md" 2>/dev/null || arret "aucun journal sur $BRANCHE_OUV : cette commande ne s'applique pas"
[ "$(grep -c '^| OUVERTURE-P3BIS |' "$BAC/journal-branche-v1.md")" = 1 ] || arret "journal : une seule ligne OUVERTURE-P3BIS attendue"
L=$(tail -n 1 "$BAC/journal-branche-v1.md"); echo "$L" > "$BAC/ligne-ouverture-v1.txt"; echo "$L"
P2=$(echo "$L" | awk -F' [|] ' '{print $5}' | awk '{print $2}')
case "$L" in "| OUVERTURE-P3BIS | "*" | pleine | $APPUI | $PAQUET_LECTURES $P2 | - |") echo "conforme : dernière ligne = ouverture pleine, appui et paquet des lectures attendus";;
  *) arret "dernière ligne du journal autre que l'ouverture pleine attendue";; esac
[[ "$P2" =~ ^[0-9a-f]{64}$ ]] && echo "$P2" > "$BAC/paquet-run-journal-v1.txt" || arret "empreinte du second paquet illisible dans la ligne"
[ "$(git ls-tree -r --name-only "$O" -- docs/verdicts | grep -c '^docs/verdicts/verdict-P3-bis-v1')" = 0 ] || arret "un verdict est déjà sur $BRANCHE_OUV : pas de perte"
B0=$(git merge-base refs/remotes/origin/main "$O") || arret "base de $BRANCHE_OUV introuvable"
[ "$(git diff --name-only "$B0" "$O")" = "$J" ] && echo "conforme : $BRANCHE_OUV ne porte que le journal depuis sa base" \
    || arret "$BRANCHE_OUV porte autre chose que le journal : la session d'origine a rendu (arrêt du lecteur, passation) ; ce n'est pas une perte"
[ "$(git ls-tree -r --name-only refs/remotes/origin/main -- docs/verdicts | grep -c '^docs/verdicts/verdict-P3-bis-v1')" = 0 ] || arret "un verdict est déjà sur main"
[ "$(git show refs/remotes/origin/main:registres/scellements-v1.md | grep -c '^| VERDICT-P3BIS |')" = 0 ] || arret "VERDICT-P3BIS déjà inscrite"
JM=$(git rev-parse -q --verify "refs/remotes/origin/main:$J" || true)
[ -z "$JM" ] || [ "$JM" = "$(git rev-parse "$O:$J")" ] || arret "le journal de main diffère de celui de $BRANCHE_OUV"
echo "conforme : perte établie (ouverture poussée, aucun verdict) ; journal de main : ${JM:-absent}"
# pièce dont la fonction attester sert au bloc 3 (attestation « qui a lu quoi »)
(cd "$ICI" && sha256sum -c) <<'FIN' || arret "pièce de cette commande"
1a9dce715b5fde593119b32bd61c5ca3a9d8e476a02bbf72425fa54b967a5a62  controle_a_blanc_compte_2_v1.py
FIN
if [ "$(git rev-parse --abbrev-ref HEAD)" = "$BRANCHE" ] && [ -e "$BAC/c-base-v1.txt" ]; then echo "branche $BRANCHE déjà créée (bloc relancé)"
else [ -z "$(git ls-remote origin "refs/heads/$BRANCHE")" ] || arret "la branche $BRANCHE existe déjà au distant (R12)"
     git switch -q --no-track -c "$BRANCHE" "$O" || arret "création de $BRANCHE"; git rev-parse HEAD > "$BAC/c-base-v1.txt"; fi
echo "branche $BRANCHE créée sur $BRANCHE_OUV $(cat "$BAC/c-base-v1.txt")"
git push -q origin "refs/heads/$BRANCHE:refs/heads/$BRANCHE" || arret "poussée de $BRANCHE refusée : rien n'est récupéré ni redéplié"
echo "branche $BRANCHE poussée (marque de reprise en cours, encore égale à $BRANCHE_OUV)"
for f in prereg/P3-bis-temoin-positif-v1.md prereg/P3-bis-temoin-positif-config-v1.json prereg/P3-bis-consignes-v1.md \
         prereg/P3-bis-addendum-1-garde-credit-v1.md prereg/P3-bis-addendum-2-telechargement-controle-v1.md \
         prereg/P3-bis-addendum-3-relance-credit-v1.md docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md \
         docs/decisions/decision-N-066-v1.md diag/20261019-230011-p3-reel/sondes-figees.json diag/20261019-230011-p3-reel/episodes-p3.json; do
    [ "$(cut -d' ' -f1 "$f.sha256")" = "$(sha256sum "$f" | cut -d' ' -f1)" ] || arret "compagnon de $f"; done
sha256sum -c --quiet <<'FIN' && echo "pièces du lecteur conformes" || arret "pièces"
76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb  prereg/P3-bis-temoin-positif-v1.md
b3fdd021223abb2c8a9ae9898cd3f2105a8b40ee0212c370f0910fd989324499  docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md
21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351  docs/decisions/decision-N-066-v1.md
FIN
# attendu : horloge, branche de l'ouverture récupérée, la ligne d'ouverture, « perte établie », branche de reprise créée,
# pièces conformes ; aucun « ARRÊT »
```

### Bloc 3 — mêmes paquets : dépôt jetable, module de S, extraction par liste positive, vérifications à l'égalité

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
[ ! -e "$ESPACE" ] || arret "$ESPACE existe déjà (R12)"
mkdir -p "$ESPACE"; git init -q "$CLONE"
git -C "$CLONE" remote add origin "$DEPOT_URL"
git -C "$CLONE" config remote.origin.promisor true; git -C "$CLONE" config remote.origin.partialclonefilter blob:none
git -C "$CLONE" fetch --no-tags --filter=blob:none -q origin +refs/heads/calcul/p3bis-reel-v2:refs/remotes/origin/calcul/p3bis-reel-v2 \
    || arret "récupération de calcul/p3bis-reel-v2"
[ "$(git -C "$CLONE" rev-parse refs/remotes/origin/calcul/p3bis-reel-v2)" = "$TETE_CALCUL" ] && echo "conforme : tête $TETE_CALCUL" || arret "tête"
git -C "$CLONE" merge-base --is-ancestor "$S" refs/remotes/origin/calcul/p3bis-reel-v2 || arret "S non ancêtre"
mkdir -p "$M/controle_ia/premier_test_ia"
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
    git -C "$CLONE" show "$S:src/controle_ia/$f" > "$M/controle_ia/$f" || arret "git show de $f"; done
(cd "$M/controle_ia" && sha256sum -c --quiet) <<'FIN' && echo "conforme : module de S" || arret "module de S"
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  __init__.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439  gardes.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2  scellement.py
c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92  premier_test_ia/__init__.py
4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9  premier_test_ia/ouverture_p3bis_v3.py
FIN
PYTHONPATH="$M:$ICI" "$PY" -B - "$DEPOT/$LISTE" "$EMPREINTE_LISTE" "$SESSION_C2" <<'FIN' || arret "attestation « qui a lu quoi »"
import sys
from pathlib import Path
import controle_a_blanc_compte_2_v1 as c
ok, texte = c.attester(Path(sys.argv[1]), sys.argv[2], sys.argv[3], "compte 2")
print(("ATTESTATION : CONFORME — " if ok else "ATTESTATION : REFUS — ") + texte); sys.exit(0 if ok else 1)
FIN
PYTHONPATH="$M" "$PY" -B -c 'import sys, pathlib
from controle_ia.premier_test_ia import ouverture_p3bis_v3 as o
l = o.exiger_format_journal(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
print(len(l), "ligne(s) au format exact")' "$BAC/journal-branche-v1.md" || arret "journal hors format"
git -C "$CLONE" sparse-checkout set --no-cone /src/controle_ia/__init__.py /src/controle_ia/gardes.py /src/controle_ia/scellement.py \
    /src/controle_ia/premier_test_ia/__init__.py '/src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py*' \
    '/src/controle_ia/premier_test_ia/lecture_p3bis_v1.py*' '/src/controle_ia/premier_test_ia/lecture_p3bis_v2.py*' \
    "/diag/p3bis-ferme-$RUN/" "/diag/$RUN/" "/runs/$RUN/" '/traces/p3bis-*/' || arret "liste positive"
T=$(git -C "$CLONE" show "refs/remotes/origin/calcul/p3bis-reel-v2:diag/$RUN/paquet-run-ferme-v1.json" \
    | "$PY" -c 'import json, sys; print(int(json.load(sys.stdin)["taille"]))') || arret "taille du second paquet illisible"
LIBRE=$(df -B1 --output=avail "$ESPACE" | tail -1); MEM=$(free -b | awk '/^Mem:/{print $7}'); BESOIN=$((3 * T + 1073741824))
echo "second paquet : $T octets ; exigé : $BESOIN ; disque libre : $LIBRE ; mémoire disponible : $MEM"
[ "$LIBRE" -ge "$BESOIN" ] && [ "$MEM" -ge "$BESOIN" ] || arret "place ou mémoire insuffisante ; rien n'est extrait"
git -C "$CLONE" checkout -q --detach refs/remotes/origin/calcul/p3bis-reel-v2 || arret "extraction (relance ce bloc une fois après une coupure)"
cd "$CLONE"
n=$(git diff --name-status --no-renames "$S" HEAD | grep -vc '^A'); [ "$n" = 0 ] || arret "changements autres que des ajouts depuis S"
n=$(find . -path ./.git -prune -o -type f -print | sed 's#^\./##' | grep -v -E "^(src/controle_ia/|diag/p3bis-ferme-$RUN/|diag/$RUN/|runs/$RUN/|traces/p3bis-)" | wc -l)
[ "$n" = 0 ] && echo "conforme : aucun fichier hors de la liste positive" || arret "fichiers hors de la liste positive"
P="diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar"; H=$(sha256sum "$P" | cut -d' ' -f1)
[ "$H" = "$PAQUET_LECTURES" ] && [ "$H" = "$(cut -d' ' -f1 "$P.sha256")" ] && [ "$(stat -c %s "$P")" = 16783360 ] \
    && echo "conforme : paquet des lectures égal à la ligne du journal et à R-2684" || arret "paquet des lectures autre que celui de la ligne du journal"
R2=$("$PY" -c 'import json, sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["sha256"])' "diag/$RUN/paquet-run-ferme-v1.json")
[ "$R2" = "$(cat "$BAC/paquet-run-journal-v1.txt")" ] && echo "conforme : second paquet (index) égal à la ligne du journal" || arret "second paquet autre que celui de la ligne du journal"
[ -e "diag/$RUN/resume.json" ] && [ ! -e "diag/$RUN/arret.json" ] || arret "run sans résumé ou avec arrêt"
# attendu : tête, module, attestation conforme, journal au format exact, place suffisante, quatre « conforme » ; aucun « ARRÊT »
```

### Bloc 4 — redépliage par `lire_paquets` et `extraire` de S, sans `ouvrir`, sans ligne au journal

Le module importé est celui de S (empreinte vérifiée par le programme) ; l'empreinte du journal de ta racine est prise
avant et après ; le dossier de sortie doit être absent ; la cellule rendue par `lire_paquets` doit égaler celle de la
ligne d'ouverture. Puis la sortie de la garde est **reconstituée** : mêmes lignes « réserve : … » que le module les
imprime (l. 1306-1307, 1319-1320), calculées par ses fonctions (`lire_prealables`, `date_de_la_mise_en_paquet`).

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
date -u +%Y-%m-%dT%H:%M:%SZ > "$BAC/date-redepliage-v1.txt"; cat "$BAC/date-redepliage-v1.txt"
PYTHONPATH="$M" "$PY" -B - "$CLONE" "$RUN" "$SORTIE" "$DEPOT" "$(cat "$BAC/ligne-ouverture-v1.txt")" \
    "$ESPACE/sortie-de-la-garde-reconstituee-v1.txt" "$(cat "$BAC/date-redepliage-v1.txt")" <<'FIN' || arret "redépliage"
import hashlib, sys
from pathlib import Path
from controle_ia.premier_test_ia import ouverture_p3bis_v3 as o
clone, run, sortie, depot, ligne, reconst, quand = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), sys.argv[5], Path(sys.argv[6]), sys.argv[7]
assert hashlib.sha256(Path(o.__file__).read_bytes()).hexdigest() == "4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9", "module autre que S"
journal = depot / o.JOURNAL_OUVERTURES
avant = hashlib.sha256(journal.read_bytes()).hexdigest()
assert not sortie.exists() and sortie.parent.is_dir() and not reconst.exists(), "sortie déjà présente ou parent absent"
assert not list(sortie.parent.glob(".ouverture-*")), "dossier caché d'un redépliage interrompu : rapport à la mère"
cellule = [c.strip() for c in ligne.strip().strip("|").split("|")][4]
p = o.lire_paquets(clone, run)                      # lit seulement ; lève RefusOuverture sur un défaut, sans rien écrire
assert p["cellule"] == cellule, "paquets autres que ceux de la ligne d'ouverture"
pre = o.lire_prealables(depot / o.REGISTRE_PREALABLES)
date_paquet = o.date_de_la_mise_en_paquet(clone, run, None)
reserves = [f"{k} : écrit après la lecture fermée : sa cécité repose sur la fermeture" for k, l in pre["ecrits"].items() if l["instant"] > date_paquet]
o.extraire({**p["lectures"], **p["run"]}, sortie)   # dossier caché du même parent, renommé en sortie
assert hashlib.sha256(journal.read_bytes()).hexdigest() == avant, "le journal a changé"
reconst.write_text("# Sortie de la garde, reconstituée par programme (reprise, R-2696) : la sortie d'origine est perdue avec la session hôte\n"
                   f"ligne d'ouverture du journal : {ligne}\n"
                   f"redépliage hors de la garde : {quand}, par lire_paquets et extraire du module de S, sans ligne neuve au journal\n"
                   + "".join(f"réserve : {r}\n" for r in reserves), encoding="utf-8")
print(f"redéplié : {len(p['lectures']) + len(p['run'])} fichiers ; cellule égale à la ligne d'ouverture ; journal inchangé ({avant[:12]}…) ; {len(reserves)} réserve(s) reconstituée(s)")
FIN
cat "$ESPACE/sortie-de-la-garde-reconstituee-v1.txt"
# attendu : « redéplié : … fichiers ; cellule égale … ; journal inchangé … ; 3 réserve(s) reconstituée(s) » ; aucun « ARRÊT »
```

### Bloc 5 — pièces et bordereau

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
[ ! -e "$PIECES" ] && [ ! -e "$VERDICT_FERME" ] || arret "pièces ou verdict-ferme déjà présents"
mkdir -p "$PIECES" "$VERDICT_FERME"; cd "$DEPOT"
for f in prereg/P3-bis-temoin-positif-v1.md prereg/P3-bis-temoin-positif-config-v1.json prereg/P3-bis-consignes-v1.md \
         prereg/P3-bis-addendum-1-garde-credit-v1.md prereg/P3-bis-addendum-2-telechargement-controle-v1.md \
         prereg/P3-bis-addendum-3-relance-credit-v1.md docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md \
         docs/decisions/decision-N-066-v1.md diag/20261019-230011-p3-reel/sondes-figees.json diag/20261019-230011-p3-reel/episodes-p3.json; do
    cp --parents "$f" "$f.sha256" "$PIECES/" || arret "copie de $f"; done
for f in docs/decisions/rendez-vous-P3-bis-v*.md; do [ -e "$f" ] && { cp --parents "$f" "$f.sha256" "$PIECES/" || arret "copie de $f"; }; done
cp --parents registres/ouvertures-p3bis-v1.md "$PIECES/" && cp "$ESPACE/sortie-de-la-garde-reconstituee-v1.txt" "$PIECES/" || arret "copie du journal"
C=$(git rev-parse refs/remotes/origin/main)
for r in R-2386 R-2399 R-2407 R-2450 R-2457 R-2492 R-2493 R-2495 R-2496 R-2497 R-2498 R-2499 R-2512 R-2516 R-2517 \
         R-2518 R-2519 R-2520 R-2521 R-2546 R-2547; do
    [ "$(git show "$C:registres/decisions.md" | grep -c "^| $r |")" = 1 ] || arret "$r : une ligne exactement attendue"; done
{ echo "# Extrait des registres pour le lecteur du verdict de P3-bis (v1)"; echo
  echo "Commit de main : $C. Lignes recopiées telles quelles, précédées de leur numéro."
  for f in registres/decisions.md registres/depenses.md registres/arrets.md; do echo "- $f : $(git show "$C:$f" | sha256sum | cut -d' ' -f1)"; done
  echo; echo "## registres/decisions.md"; echo
  for r in R-2386 R-2399 R-2407 R-2450 R-2457 R-2492 R-2493 R-2495 R-2496 R-2497 R-2498 R-2499 R-2512 R-2516 R-2517 \
           R-2518 R-2519 R-2520 R-2521 R-2546 R-2547; do git show "$C:registres/decisions.md" | grep -n "^| $r |"; done
  echo; echo "## registres/depenses.md"; echo; git show "$C:registres/depenses.md" | grep -n -E '60286945|60370121|60432755|60492378'
  echo; echo "## registres/arrets.md"; echo; git show "$C:registres/arrets.md" | grep -n -E '60286945|60370121|60432755|60492378'
} > "$PIECES/extrait-registres-p3bis-v1.md"
echo "extrait des registres : $(grep -c -E '^[0-9]+:\| ' "$PIECES/extrait-registres-p3bis-v1.md") lignes recopiées (non affichées)"
cd "$CLONE"
cp --parents "runs/$RUN/manifeste.json" "runs/$RUN/manifeste.json.sha256" "diag/$RUN/resume.json" "diag/$RUN/resume.json.sha256" \
    "diag/$RUN/sondes-figees.json" "diag/$RUN/sondes-figees.json.sha256" "diag/$RUN/paquet-run-ferme-v1.json" \
    "diag/$RUN/paquet-run-ferme-v1.json.sha256" src/controle_ia/premier_test_ia/lecture_p3bis_v1.py \
    src/controle_ia/premier_test_ia/lecture_p3bis_v1.py.sha256 src/controle_ia/premier_test_ia/lecture_p3bis_v2.py \
    src/controle_ia/premier_test_ia/lecture_p3bis_v2.py.sha256 "$PIECES/" || arret "copie de la classe 1"
cp -r --parents traces/p3bis-* "$PIECES/" || arret "copie des traces"
(cd "$PIECES" && find . -type f -print0 | sort -z | xargs -0 sha256sum) > "$ESPACE/bordereau-remise-v1.txt"
n=$(cut -c67- "$ESPACE/bordereau-remise-v1.txt" | grep -c -i -E 't07|t0\.7|t06|lecture-sondes|bras-attaque|mode-tenu|anteriorite-bras|etiqueteur|quarantaine|mesure-unanime')
[ "$n" = 0 ] && echo "conforme : aucun nom interdit parmi les pièces" || arret "nom interdit parmi les pièces"
cd "$DEPOT" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$ESPACE/bordereau-remise-v1.txt" || arret "sceau du bordereau"
# attendu : au moins 40 lignes recopiées ; « aucun nom interdit » ; l'empreinte du bordereau ; aucun « ARRÊT »
```

### Bloc 6 — message de remise au lecteur neuf

Avant ce bloc : vérifie que ton outil d'agent peut créer un sous-agent du modèle B ; fixe `NOTE_MODELE`.

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
NOTE_MODELE="modèle B"      # « modèle A, faute de B » sinon
cat > "$BAC/message-remise-gabarit-v1.txt" <<'FIN'
Interdits permanents (brief du compte 2, section 6), en plus de ceux de ta consigne : aucune dépense ; aucune valeur de clé (jamais env, printenv, set sans argument, export -p, /proc/*/environ) ; jamais diag/*/lecture-sondes-t06.json, la lecture B de 7a, donnees/lecture-b-7a-quarantaine-v1, donnees/mesure-unanime-v15-sortie-v1, essai/t06-explo-v3, aucun diag/ ni runs/ de 7a ou 7b, l'étiqueteur, scripts/extraire_mesures_epreuve_t06_v1.py, la branche calcul/p3bis-reel-v2 (tu ne lis que ce qui en a été redéplié pour toi, dans paquets-ouverts/, selon ta consigne) ; jamais donnees/bras-attaque*, donnees/mode-tenu-a-l-ecart*, docs/notes/bras-attaque/, registres/index-bras-attaque*, anteriorite-bras-informe*, ni la branche claude/compassionate-meitner-d4ryyk ; aucune recherche récursive hors de l'espace fermé ; aucune heure écrite à la main (date -u) ; aucune commande git, aucun appel au loueur ; un refus de permission, du crochet ou d'un classifieur : arrêt, sans contournement ; rien de publié, aucun contact extérieur.
Tu es le lecteur neuf du verdict de P3-bis (règle R13), après la perte de la session qui hébergeait un premier lecteur : tu ne lis rien de ce premier lecteur. Lis d'abord ta consigne, et elle seule fixe ce que tu lis et écris :
<<ESPACE>>/pieces/docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md (empreinte b3fdd021223abb2c8a9ae9898cd3f2105a8b40ee0212c370f0910fd989324499, égale à son compagnon : vérifie-la avant lecture).
- Mode de l'ouverture : pleine (voie normale). Ligne du journal : <<LIGNE_OUVERTURE>>
- Écart à déclarer en tête de ton verdict, mot pour mot, avant le verdict : « Écart (reprise, R-2696) : les paquets ont été redépliés hors de la garde le <<DATE_REDEPLIAGE>>, après l'ouverture pleine journalisée par la garde (ligne ci-dessus), par les fonctions lire_paquets et extraire du module de S, sans appel de ouvrir et sans ligne neuve au journal ; paquets vérifiés à l'égalité aux deux empreintes de la ligne d'ouverture ; la session qui hébergeait le premier lecteur a été perdue avant la poussée du verdict ; sortie de la garde reconstituée par programme. Lecture du texte scellé de P3-bis, l. 1981-1983 (« Toute ouverture hors de la garde […] avant une ouverture autorisée »), assumée par Lazar : le redépliage suit l'ouverture autorisée. » Tu écris aussi la réserve gelée « résultat de P3-bis exposé avant les scores de T0.7 » si et seulement si ta consigne l'exige au vu de ce qui précède ; sinon tu écris pourquoi tu ne l'écris pas, comme une question pour Lazar.
- Espace fermé : <<ESPACE>>. Pièces : <<ESPACE>>/pieces (bordereau <<ESPACE>>/bordereau-remise-v1.txt, empreinte <<EMPREINTE_BORDEREAU>>, scellé). Paquets redépliés : <<ESPACE>>/paquets-ouverts. Tu n'écris que dans <<ESPACE>>/verdict-ferme.
- Run : 20261113-121129-p3bis-reel. Interpréteur : <<PY>>.
- Réserves imprimées par la garde : reconstituées par programme dans <<ESPACE>>/pieces/sortie-de-la-garde-reconstituee-v1.txt (le fichier sortie-de-la-garde-v1.txt que nomme ta consigne est perdu avec la session).
- Ton modèle s'écrit au verdict sans aucun identifiant : « <<NOTE_MODELE>> » (« modèle A » = celui des auteurs du texte de P3-bis et de son code de lecture ; A ≠ B).
Tu ne lis rien d'autre (ni le dépôt, ni le clone de calcul, ni aucun fichier de T0.7, ni lecture-sondes-t06.json). Ton rapport final suit la section « Ce que tu rends » de ta consigne, mot pour mot ; sous l'ouverture pleine, la ligne « ISSUE : … » y est permise.
FIN
ESPACE="$ESPACE" LIGNE="$(cat "$BAC/ligne-ouverture-v1.txt")" BORDEREAU="$(cut -d' ' -f1 "$ESPACE/bordereau-remise-v1.txt.sha256")" \
  PY="$PY" NOTE_MODELE="$NOTE_MODELE" QUAND="$(cat "$BAC/date-redepliage-v1.txt")" \
  "$PY" -B - "$BAC/message-remise-gabarit-v1.txt" "$BAC/message-remise-v1.txt" <<'FIN' || arret "message de remise"
import os, sys
t = open(sys.argv[1], encoding="utf-8").read()
for m, v in (("<<ESPACE>>", "ESPACE"), ("<<LIGNE_OUVERTURE>>", "LIGNE"), ("<<EMPREINTE_BORDEREAU>>", "BORDEREAU"),
             ("<<PY>>", "PY"), ("<<NOTE_MODELE>>", "NOTE_MODELE"), ("<<DATE_REDEPLIAGE>>", "QUAND")):
    t = t.replace(m, os.environ[v])
if "<<" in t or ">>" in t:
    sys.exit("marqueur resté dans le message")
with open(sys.argv[2], "x", encoding="utf-8") as f:
    f.write(t)
print("message écrit, aucun marqueur restant")
FIN
cd "$DEPOT" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$BAC/message-remise-v1.txt" || arret "sceau du message"
cat "$BAC/message-remise-v1.txt"
```

**Création du lecteur** : **un** sous-agent neuf (outil d'agent de ta session, agent généraliste, sans contexte hérité),
du modèle B, dont le seul message est le texte exact affiché par le bloc 6. Tu attends son rapport final sans rien lire de
l'espace fermé. Sur « STATUT : arret … » : pas de bloc 7 ; bloc 8 seul ; nœud.

### Bloc 7 — après le verdict : copie, sceaux, contrôles, poussée de la branche de reprise

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
cd "$VERDICT_FERME" || arret "verdict-ferme absent"; ls -1A
[ -z "$(find . -mindepth 1 -type d)" ] || arret "dossier inattendu dans verdict-ferme"
n=$(ls -1A | grep -v -E '^verdict-P3-bis-v1(\.md|-issue\.json|-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md))(\.sha256)?$' | wc -l)
[ "$n" = 0 ] || arret "fichier de nom inattendu dans verdict-ferme"
[ -f verdict-P3-bis-v1.md ] && [ -f verdict-P3-bis-v1-issue.json ] || arret "verdict ou fichier d'issue absent"
grep -q "Écart (reprise, R-2696)" verdict-P3-bis-v1.md && echo "conforme : écart déclaré dans le verdict (seule recherche faite dans le verdict)" \
    || arret "écart de reprise non déclaré dans le verdict : rien n'est commité"
cd "$DEPOT"
git fetch --no-tags -q origin "+refs/heads/$BRANCHE_OUV:refs/remotes/origin/$BRANCHE_OUV" || arret "récupération de $BRANCHE_OUV"
[ "$(git rev-parse "refs/remotes/origin/$BRANCHE_OUV")" = "$(cat "$BAC/c-base-v1.txt")" ] \
    || arret "$BRANCHE_OUV a bougé depuis le constat : la session d'origine n'était pas perdue ; rien n'est commité ; nœud de Lazar"
if [ -e "$BAC/c-verdict-v1.txt" ]; then [ "$(git rev-parse HEAD)" = "$(cat "$BAC/c-verdict-v1.txt")" ] || arret "tête"; echo "verdict déjà commité"
else
    for f in $(ls -1A "$VERDICT_FERME" | grep -v '\.sha256$'); do
        if [ -e "docs/verdicts/$f" ]; then cmp -s "$VERDICT_FERME/$f" "docs/verdicts/$f" || arret "docs/verdicts/$f existe et diffère"
        else cp "$VERDICT_FERME/$f" "docs/verdicts/$f" && cmp -s "$VERDICT_FERME/$f" "docs/verdicts/$f" || arret "copie de $f"; fi
        PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "docs/verdicts/$f" || arret "sceau de $f"
    done
    "$PY" -B -c 'import hashlib, json, sys
d = json.load(open(sys.argv[1], encoding="utf-8")); h = hashlib.sha256(open(sys.argv[2], "rb").read()).hexdigest()
print("empreinte du verdict en prose : " + ("égale à verdict_sha256" if d.get("verdict_sha256") == h else "AUTRE")); sys.exit(0 if d.get("verdict_sha256") == h else 1)' \
        docs/verdicts/verdict-P3-bis-v1-issue.json docs/verdicts/verdict-P3-bis-v1.md || arret "verdict_sha256 autre : nœud"
    LP=$(ls -d "$SORTIE"/diag/*-p3bis-lecture-complementaire/lecture-p3bis.json 2>/dev/null)
    [ "$(printf '%s\n' "$LP" | grep -c .)" = 1 ] || arret "lecture-p3bis.json introuvable ou multiple"
    (cd "$CLONE" && PYTHONPATH="$M" "$PY" -B -m "$MODULE" exposer-issue "$DEPOT/docs/verdicts/verdict-P3-bis-v1-issue.json" --lecture-p3bis "$LP") \
        > "$BAC/exposer-issue-v1.txt" 2>&1 || { cat "$BAC/exposer-issue-v1.txt"; arret "exposer-issue : rien n'est commité ; nœud"; }
    git add -- docs/verdicts/verdict-P3-bis-v1*
    git diff --cached --name-only | grep -v -E '^docs/verdicts/verdict-P3-bis-v1[^/]*$' && arret "index : autre chose que le verdict"
    n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] || arret "garde des secrets"
    git commit -q -m "P3-bis : verdict du lecteur neuf après reprise (paquets redépliés hors de la garde, R-2696), session du compte 2" || arret "commit"
    git rev-parse HEAD > "$BAC/c-verdict-v1.txt"
fi
cat "$BAC/exposer-issue-v1.txt"
git push -q origin "refs/heads/$BRANCHE:refs/heads/$BRANCHE" || arret "poussée (relance ce bloc : il reprend à la poussée)"
echo "commit du verdict : $(cat "$BAC/c-verdict-v1.txt")"; git ls-remote origin "refs/heads/$BRANCHE"
for f in docs/verdicts/verdict-P3-bis-v1*.sha256; do cat "$f"; done
```

### Bloc 8 — journal provisoire, écart proposé au registre, passation, rendu

```bash
. "$HOME/bac-p3bis-reprise-compte-2-v1/variables-v1.sh" || exit 1
RAPPORT_LECTEUR=$(cat <<'FIN'
<lignes du rapport final du lecteur, telles quelles, à la place de cette ligne>
FIN
)
CROCHET='<bloquée | passée>'
PERTE='<mots de Lazar qui disent la session d origine perdue, recopiés tels quels, sans apostrophe droite>'
MODELES='lecteur : <modèle B | modèle A, faute de B> ; session hôte : <modèle A | modèle B> ; identités dites en conversation seulement (R-2598)'
case "$RAPPORT_LECTEUR$CROCHET$MODELES$PERTE" in *'<'*'>'*) arret "variables de tête non remplies";; esac
lire() { cat "$1" 2>/dev/null || echo "sans objet"; }
cd "$DEPOT"; mkdir -p registres-provisoires
[ -e "$BAC/noms-v1.txt" ] || printf '%s\n%s\n' "registres-provisoires/compte-2-reprise-verdict-p3bis-$(date -u +%Y-%m-%d)-v1.md" \
    "registres-provisoires/passation-compte-2-reprise-verdict-p3bis-$(date -u +%Y-%m-%d-%H%M).md" > "$BAC/noms-v1.txt"
J=$(sed -n 1p "$BAC/noms-v1.txt"); P=$(sed -n 2p "$BAC/noms-v1.txt")
if [ -e "$BAC/c-fin-v1.txt" ]; then echo "déjà commités"; else
[ -e "$J" ] || { echo "# Compte 2 — reprise du verdict de P3-bis — journal provisoire (v1)"; echo
  echo "Écrit le $(date -u +%Y-%m-%dT%H:%M:%SZ) par la session \`$SESSION_C2\`, branche \`$BRANCHE\` ; identifiants provisoires P2R-…, à numéroter par la mère."; echo
  echo "- P2R-001 : reprise commencée $(lire "$BAC/debut-v1.txt") ; base \`$(lire "$BAC/c-base-v1.txt")\` (tête de $BRANCHE_OUV) ; épreuve du crochet : $CROCHET ; $MODELES."
  echo "- P2R-002 : perte dite par Lazar, verbatim : « $PERTE » ; établi par programme : ligne d'ouverture poussée, branche de l'ouverture réduite au journal, aucun verdict ; ligne : \`$(lire "$BAC/ligne-ouverture-v1.txt")\`."
  echo "- P2R-003 : **écart proposé au registre** — paquets redépliés hors de la garde le $(lire "$BAC/date-redepliage-v1.txt"), par la session \`$SESSION_C2\` du compte 2, par lire_paquets et extraire du module de S (\`4a54a437…\`), sans appel de ouvrir ni ligne neuve au journal (empreinte du journal inchangée), paquets égaux aux deux empreintes de la ligne d'ouverture ; lecture assumée du texte scellé de P3-bis, l. 1981-1983 (R-2696) ; sortie de la garde reconstituée par programme (\`sortie-de-la-garde-reconstituee-v1.txt\`)."
  echo "- P2R-004 : bordereau \`$(cut -d' ' -f1 "$ESPACE/bordereau-remise-v1.txt.sha256" 2>/dev/null)\` ; message \`$(cut -d' ' -f1 "$BAC/message-remise-v1.txt.sha256" 2>/dev/null)\`."
  echo "- P2R-005 : rapport final du lecteur :"; printf '%s\n' "$RAPPORT_LECTEUR" | sed 's/^/    /'
  echo "- P2R-006 : verdict commité \`$(lire "$BAC/c-verdict-v1.txt")\` ; exposer-issue : \`$(lire "$BAC/exposer-issue-v1.txt")\`."
  echo "- P2R-007 : cette session est désormais exclue de l'analyse du verdict de P3-bis et, par prudence, des verdicts de 7b et de l'étape B."
} > "$J"
[ -e "$P" ] || { echo "# Passation — compte 2, reprise du verdict de P3-bis — $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo
  echo "- **Fait** : voir \`$J\`."
  echo "- **Reste** (mère) : journal dans main s'il n'y est pas (commit de $BRANCHE_OUV), puis le verdict (commit \`$(lire "$BAC/c-verdict-v1.txt")\`), rescellé ; VERDICT-P3BIS ; écart P2R-003 au registre ; liste « qui a lu quoi »."
  echo "- **Prochaine action** : aucune pour ce compte sur P3-bis."; echo "- **Instances actives** : aucune."
} > "$P"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$J" "$P" || arret "sceau"
git add -- "$J" "$J.sha256" "$P" "$P.sha256"
[ "$(git diff --cached --name-only | grep -vc '^registres-provisoires/')" = 0 ] || arret "index"
n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] || arret "garde des secrets"
git commit -q -m "Compte 2 : journal provisoire et passation de la reprise du verdict de P3-bis" || arret "commit"
git rev-parse HEAD > "$BAC/c-fin-v1.txt"
fi
git push -q origin "refs/heads/$BRANCHE:refs/heads/$BRANCHE" || arret "poussée (relance ce bloc)"
echo "RENDU — branche $BRANCHE ; base $(lire "$BAC/c-base-v1.txt") ; verdict $(lire "$BAC/c-verdict-v1.txt") ; fin $(lire "$BAC/c-fin-v1.txt")"
for f in docs/verdicts/verdict-P3-bis-v1* "$J" "$P"; do case "$f" in *.sha256) ;; *) [ -e "$f" ] && sha256sum "$f";; esac; done
```

**Rendu à Lazar** (verdict d'abord ; il transmet à la mère) : une à trois lignes (reprise faite, verdict du lecteur neuf
poussé sur `verdict/p3bis-compte-2-reprise-v1`, rien d'autre lu ; ou le code d'arrêt et le bloc) ; la ligne d'`exposer-issue`
telle quelle ; la sortie « RENDU » ; l'écart P2R-003 ; erreurs, une ligne chacune ; aucune analyse.

## 4. Ce qui arrête tout

- Sans mot de Lazar disant la session d'origine perdue, ou dans la conversation même qui a exécuté l'ouverture : tu ne
  commences pas.
- La branche de l'ouverture a bougé entre le constat et le commit du verdict (bloc 7) : la session d'origine vivait ;
  rien n'est commité ; nœud de Lazar. Si, malgré tout, deux verdicts existent, aucun n'est inscrit sans un mot de Lazar.
- Tout « ARRÊT » d'un bloc. En particulier, **le cas n'est pas établi** (pas de branche ou de journal d'ouverture ; plus
  d'une ligne d'ouverture ; dernière ligne autre ; branche de l'ouverture qui porte autre chose que le journal, par
  exemple l'arrêt du lecteur ou une passation rendus par la session d'origine ; un verdict déjà présent ; `VERDICT-P3BIS` inscrite ; journal de `main`
  différent) : cette commande ne s'applique pas, rapport à la mère.
- Paquets autres que ceux de la ligne d'ouverture (empreinte du paquet des lectures, du second paquet, cellule rendue par
  `lire_paquets`), morceau défectueux (`lire_paquets` lève) : rien n'est redéplié ; nœud de Lazar.
- Journal changé après le redépliage (contrôle du bloc 4) : arrêt, nœud (impossible par le code, contrôlé quand même).
- **Jamais `ouvrir`** pour contourner un arrêt : une ligne neuve au journal serait un écart non couvert par R-2696.
- Écart non déclaré dans le verdict, `verdict_sha256` autre, `exposer-issue` en arrêt, rapport « STATUT : arret … » :
  rien n'est commité ; nœud.
- Perte de **cette** session avant la poussée du verdict : nœud de Lazar (une seconde reprise demande une version neuve de
  cette commande).
- Identifiant de session introuvable : le relever (outil qui décrit ta session, ou ligne « Claude-Session ») et le poser à
  la main au bloc 1 ; sinon, arrêt. Refus de permission, du crochet ou d'un classifieur, poussée refusée : arrêt, rapport.

## Annexe A — ce que le mot de Lazar couvre, et ce qu'il ne couvre pas explicitement

Couvert (R-2696) : session neuve du compte 2 ; mêmes paquets, vérifiés aux empreintes de la ligne du journal ;
`lire_paquets` et `extraire` de S ; ni `ouvrir` ni ligne neuve ; lecteur neuf ; écart au verdict et au registre ; lecture
assumée du texte, l. 1981-1983.

Non couvert explicitement, à confirmer par la mère (ou par Lazar s'il le juge) :
1. **Sortie de la garde reconstituée** : la consigne du lecteur nomme `sortie-de-la-garde-v1.txt` (lignes « réserve : … »),
   perdue avec la session. La commande la recalcule par les fonctions du module (même format, l. 1306-1307) dans
   `sortie-de-la-garde-reconstituee-v1.txt`, nom neuf, déclaré au lecteur. Le texte gelé de la réserve est identique ; la
   source change. Parade pour l'avenir (hors de cette commande) : une version neuve de la commande d'ouverture pourrait
   commiter `sortie-de-la-garde-v1.txt` (classe 1 : chemin de sortie et réserves) avec le journal au bloc 9.
2. **Réserve « exposé avant les scores de T0.7 »** : le texte la lie à une ouverture hors de la garde « avant une ouverture
   autorisée ». La commande ne tranche pas à la place du lecteur : elle lui donne l'écart et la lecture de Lazar, et lui
   demande d'écrire la réserve si sa consigne l'exige, sinon de dire pourquoi, en question pour Lazar.
3. **Liste « qui a lu quoi »** : l'attestation arrête dès qu'une ligne porte le compte 2. Si la mère inscrit la session
   perdue (hôte, ou son lecteur) au compte 2, la reprise s'arrêtera : soit la mère l'inscrit hors du périmètre de la liste
   (qui ne porte que les lectures qui excluent du verdict), soit elle adapte l'attestation dans une version neuve.
4. **Réserve « exposé avant les scores de T0.7 »** (constat m3 de la contre-lecture) : la consigne du lecteur, section 7,
   ne reprend pas le « avant une ouverture autorisée » du texte ; un lecteur qui la suit à la lettre l'écrira sans doute,
   alors que son énoncé serait ici inexact (les scores de T0.7 sont l'appui même de l'ouverture). Le verdict de reprise
   est à relire sur ce point par la mère avant toute transmission à T0.7.
5. **Fichiers de la session perdue** : si son conteneur revenait, son espace fermé (paquets extraits, verdict partiel) ne
   doit être ni lu ni repris ; seule cette reprise vaut.

## Annexe B — répétition sur jouet (version 2)

`bash docs/procedures/P3-bis-commande-compte-2-v1/repetition_reprise_jouet_v2.sh <dépôt> <bac neuf> [<python avec numpy>]`.
Elle fabrique un dépôt de calcul jouet (paquets factices par les fonctions de S) dont le commit du paquet est **daté avant
les lignes d'écrit** ; simule l'ouverture par la **vraie garde** de S (`ouvrir`, mode `pleine`, trois lignes « réserve »)
sur une copie du dépôt et pousse le journal sur `verdict/p3bis-compte-2-v1` d'un faux dépôt distant ; simule la perte ;
puis joue les huit blocs de ce texte, extraits tels quels, avec un lecteur simulé. Éprouvés en plus : cinq arrêts du
constat (branche absente ; deux lignes d'ouverture ; dernière ligne un refus ; verdict déjà présent ; **arrêt du lecteur
rendu par la session d'origine**, cas M1) ; redépliage refusé sur un morceau altéré et sur un dossier caché laissé ;
reconstitution à trois réserves, égales aux lignes imprimées par la garde ; branche d'origine qui bouge avant le commit du
verdict (arrêt, rien commité) ; journal inchangé. Sortie : `repetition-reprise-jouet-sortie-v2.txt` (`43d2f8de…`, 2026-11-14T10:19:28Z → 10:20:29Z, « BILAN : 37 conformes sur 37 » ;
empreinte des blocs : `c5b8f89a0117e8d04d6130f57ae549ce6321c51c040c7d7e153d3ed666edfd77`). Limite : les vrais paquets, leur taille et la poussée réelle ne sont éprouvés que
le jour même ; la perte elle-même ne s'éprouve pas, elle se dit par Lazar.
