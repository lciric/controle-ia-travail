#!/usr/bin/env bash
# Correction sur place (2026-11-11, R-2367 ; consigne `consigne-correction-bancs-epingles-p3bis-v1.md`, `2748d944…`) : le
# banc joue aussi bien contre des contrôles épinglés que non épinglés : chaque épingle `^K=.*$` de la copie jouée est
# remplacée quelle qu'en soit la valeur (une occurrence exigée) ; K34 fabrique son artefact en remettant les treize
# épingles à A_EPINGLER dans une copie de la copie jouée (dépôt nu local) ; tout autre cas inchangé.
# Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`) : copie de `essais_controles_p3bis_v1.sh`, gardé
# tel quel (R12), noms de la chaîne en v2 ; configuration du banc à 800 directions ; essai de fermeture v3 (factice du banc).
# Brouillon 3 (2026-11-10, contre-lecture différentielle) : texte candidat = brouillon 10 (marqueurs remplis) ; clone de
# la copie en extraction partielle (CD-05), témoin fabriqué docs/notes/bras-attaque/ absent du clone (K00), refusé s'il
# est extrait (K36) ; borne de création du 18 novembre lue par le module commun.
# Brouillon 2 (2026-11-10, après la fusion du code corrigé) : vrais scripts de l'instance v2 (amorce, script, empreinte
# de la liste), vraie liste ciblée v2 (531 essais ; fichiers copiés, la suite remplacée par un troisième bouchon qui écrit
# « 531 passed », ou FAUX_SUITE), vraie sortie versée de l'essai de fermeture v2 ; l'essai rejoué au commit S reste
# factice ici (sept minutes par passage : joué par la répétition finale).
# Banc des contrôles avant dépense de P3-bis (R5), v1, décliné du banc des contrôles de P3 (docs/procedures/
# P3-premier-test-v2/essais_controles_p3_v1.sh) sous un nom neuf (R12) : un cas sain et un artefact par bloc, chacun joué
# contre le script entier, sur un dépôt synthétique et un dépôt nu local (aucun appel externe ; le vrai registres/go.md
# n'est jamais modifié ; aucun clone du dépôt de travail entier : place disque). Dépôt synthétique : src/ de HEAD (copie),
# configuration de P3, tâches de P3 et leur sceau, garde de calcul de HEAD, registre des GO fabriqué (ligne
# GO-2026-11-10-02 recopiée de main), dépendances épinglées aux versions de l'interpréteur PY du banc, liste ciblée v2
# d'un fichier d'essais trivial (deux essais), scripts de l'instance v2 factices (empreinte de la liste écrite, lanceur
# run_v2, dépôt de travail par défaut), essai de fermeture v2 factice (CONFORME, ou NON CONFORME sous
# FAUX_ESSAI_NON_CONFORME), chaîne versée (copies réelles), sortie versée de l'essai, longueurs attendues, rapport de la
# contre-lecture 4 factice ; texte candidat = le brouillon 9 dont les onze marqueurs sont remplis de valeurs du banc ;
# écarts au brouillon 9 déclarés appliqués (ligne « GO » et `GO_ID` : GO-2026-11-10-02 ; « création au plus tard le
# 23 novembre 2026 » : R-2077, message de la mère) ; configuration = brouillon 1 dont l'empreinte des consignes est remplie ; consignes = brouillon 2. Commits : C0 (base,
# tient lieu du commit du code de P3), C1 (commit du code : un module neuf seulement), C2 (pièces hors de l'arbre gelé),
# S (texte, configuration, consignes et sceaux).
# Copie jouée : celle de ce dossier, dont changent (lignes comptées et déclarées) : les épingles A_EPINGLER (valeurs du
# banc), CODE_P3 (C0), le clonage (dépôt nu local au lieu du dépôt de travail), et deux bouchons : le bloc du vrai
# tokeniseur (écrit la mesure FAUSSE_MESURE du banc ; il lit le tokeniseur de l'agent sur Hugging Face : joué par la
# répétition finale au candidat) et le bloc des gardes du lanceur run_v2 (texte, configuration et données génériques
# réels exigés : joué par la répétition finale). La comparaison des longueurs (module commun) est jouée ici.
# Verdict de chaque cas : code attendu et ligne KO attendue présente (aucun KO pour le cas sain).
# Usage : essais_controles_p3bis_v2.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
ICI=$(dirname "$(realpath "$0")")
SRC=$(realpath "$ICI/../../..")
PYB=/home/user/controle-ia-travail/.venv/bin/python
V=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md; CFG=prereg/P3-bis-temoin-positif-config-v1.json; CONSIGNES=prereg/P3-bis-consignes-v1.md
B10=brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md   # 9038a015…, recopié de main
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
for s in controles_avant_depense_p3bis_v2.sh verifications_p3bis_v2.py; do echo "script éprouvé : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
mkdir -p "$E" && cd "$E" || exit 2
NON_CONFORMES=0; NCAS=0
# --- dépôt synthétique -----------------------------------------------------------------------------------------------
git init -q -b main source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
cp -r "$SRC/src" . && find src -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null
cp "$SRC/pyproject.toml" .
mkdir -p prereg donnees/t05-pilote-v1 registres .claude/hooks scripts tests "$V" brouillons/P3-bis-temoin-positif-v1
cp "$SRC/prereg/P3-premier-test-config-v1.json" "$SRC/prereg/P3-premier-test-config-v1.json.sha256" prereg/
cp "$SRC/donnees/t05-pilote-v1/taches-pilote-60-v1.json" "$SRC/donnees/t05-pilote-v1/taches-pilote-60-v1.json.sha256" donnees/t05-pilote-v1/
git -C "$SRC" show HEAD:.claude/hooks/garde_calcul.py > .claude/hooks/garde_calcul.py
{ git -C "$SRC" show main:registres/go.md | sed -n '1,10p'; git -C "$SRC" show main:registres/go.md | grep '^| GO-2026-11-10-02 |'; } > registres/go.md
VNP=$("$PYB" -c "import numpy, pytest; print(f'numpy=={numpy.__version__}\npytest=={pytest.__version__}')")
printf '%s\n' "$VNP" > requirements-cpu.txt; echo "-r requirements-cpu.txt" > requirements-gpu.txt; echo "# aucune (banc)" > requirements-donnees.txt
# vrais scripts de l'instance v2, vraie liste ciblée v2 (et ses 30 fichiers d'essais, copiés pour la garde des chemins ;
# la liste n'est pas jouée ici : bouchon de la suite, la vraie liste est jouée par la répétition finale)
for f in scripts/essais-cibles-p3bis-v2.txt scripts/p3bis_instance_v2.sh scripts/amorce_instance_p3bis_v2.sh; do
    cp "$SRC/$f" "$SRC/$f.sha256" "$(dirname "$f")/" || { echo "$f absent de l'arbre fusionné"; exit 2; }
done
while IFS= read -r f; do [ -n "$f" ] && cp "$SRC/$f" "$f"; done < scripts/essais-cibles-p3bis-v2.txt
ESSAI_V=brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v1.txt   # vraie sortie versée de l'essai v2
cat > scripts/essai_fermeture_p3bis_v3.py <<'EOF'
"""Essai différentiel de fermeture factice du banc des contrôles de P3-bis."""
import os, sys
lignes = ["CONFORME — taille fixe : 16 783 360 octets", "CONFORME — longueur comprimée : règle des 16 octets"]
if os.environ.get("FAUX_ESSAI_NON_CONFORME"):
    lignes.append("NON CONFORME — variante endormie non détectée")
lignes.append("ESSAI DIFFÉRENTIEL DE FERMETURE : " + ("NON CONFORME" if os.environ.get("FAUX_ESSAI_NON_CONFORME") else "CONFORME"))
os.makedirs(sys.argv[1])
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(lignes) + "\n")
print(lignes[-1])
sys.exit(1 if os.environ.get("FAUX_ESSAI_NON_CONFORME") else 0)
EOF
git add -A && git commit -qm "C0 : base du banc (tient lieu du commit du code de P3)" && C0=$(git rev-parse HEAD)
printf '"""Module neuf factice du commit du code (banc des contrôles de P3-bis)."""\n' > src/controle_ia/premier_test_ia/ouverture_p3bis_banc_v2.py
git add -A && git commit -qm "C1 : commit du code (un ajout)" && C1=$(git rev-parse HEAD)
# pièces hors de l'arbre gelé
for s in lancer_p3bis_v2.sh surveiller_p3bis_v2.sh controle_cinq_minutes_p3bis_v2.sh controles_avant_depense_p3bis_v2.sh recuperation_p3bis_v2.sh verifications_p3bis_v2.py; do
    if [ -f "$ICI/$s" ]; then cp "$ICI/$s" "$V/$s"; else printf 'DEPOT_URL=https://github.com/lciric/controle-ia-travail.git\n' > "$V/$s"; fi
done
(cd "$V" && for s in *.sh *.py; do sha256sum "$s" > "$s.sha256"; done)    # docs/ est scellé (verifier-arbre)
cp "$SRC/$ESSAI_V" "$SRC/$ESSAI_V.sha256" brouillons/P3-bis-temoin-positif-v1/
"$PYB" -I -B - "$ICI/verifications_p3bis_v2.py" "$E/mesure-saine.json" "$E/mesure-a-differe.json" "$E/mesure-autre.json" "$V/longueurs-attendues-p3bis-banc-v1.json" <<'EOF' || exit 2
import importlib.util, json, sys, copy
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
pt = [{"tache": f"t{i}", **{m: {"saboteur": 90 + i % 3, "temoin": 90 + i % 3, "mention": 92} for m in v.MESURES}} for i in range(60)]
json.dump({"format": "llama3", "par_tache": pt}, open(sys.argv[2], "w"))
a = copy.deepcopy(pt); a[7]["indication_gabarit"]["temoin"] += 1
json.dump({"format": "llama3", "par_tache": a}, open(sys.argv[3], "w"))
b = copy.deepcopy(pt); b[0]["consigne_seule"]["mention"] = 93
json.dump({"format": "llama3", "par_tache": b}, open(sys.argv[4], "w"))
json.dump(v.resume_longueurs(pt), open(sys.argv[5], "w"), indent=1, sort_keys=True)
EOF
RAPPORT=brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-banc-v1.md
printf '# Contre-lecture 4 factice du banc des contrôles de P3-bis\n\nRelecture courte : rien à signaler (essai).\n' > "$RAPPORT"
cp "$SRC/brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-brouillon2.md" brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-banc.md
CONS_SHA=$(sha256sum brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-banc.md | cut -d' ' -f1)
"$PYB" -I - "$SRC/brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-brouillon1.json" "$CONS_SHA" brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-banc.json <<'EOF' || exit 2
import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8")); c["consignes_sha256"] = sys.argv[2]; c["n_plancher"] = 800   # v2 : R-2320
open(sys.argv[3], "w", encoding="utf-8").write(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
EOF
E_ESSAI=$(sha256sum "$ESSAI_V" | cut -d' ' -f1)
E_LONG=$(sha256sum "$V/longueurs-attendues-p3bis-banc-v1.json" | cut -d' ' -f1)
E_RAPPORT=$(sha256sum "$RAPPORT" | cut -d' ' -f1)
E_AMORCE=$(sha256sum scripts/amorce_instance_p3bis_v2.sh | cut -d' ' -f1); E_INST=$(sha256sum scripts/p3bis_instance_v2.sh | cut -d' ' -f1)
# texte candidat : brouillon 10, ses dix marqueurs remplis (l'essai de fermeture y est déjà cité : sortie v1, 06e84ff7…)
"$PYB" -I - "$SRC/$B10" brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat-banc.md "$C1" "$E_AMORCE" "$E_INST" \
    "$ESSAI_V" "$E_ESSAI" "$V/longueurs-attendues-p3bis-banc-v1.json" "$E_LONG" "$CONS_SHA" "$RAPPORT" "$E_RAPPORT" <<'EOF' || exit 2
import sys
t = open(sys.argv[1], encoding="utf-8").read()
c1, ea, ei, essai, ee, lg, el, cs, rap, er = sys.argv[3:13]
r = {"<<COMMIT_CODE_P3BIS>>": c1,
     "<<EMPREINTES_CODE_P3BIS>>": f"`scripts/amorce_instance_p3bis_v2.sh` (`{ea}`, sha256) ; `scripts/p3bis_instance_v2.sh` (`{ei}`, sha256)",
     "<<IDENTITE_CODE_P3BIS>>": "sortie versée (banc)", "<<TESTS_ATTENDUS_P3BIS>>": "531",
     "<<ESSAI_FERMETURE_P3BIS>>": f"`{essai}` (`{ee}`)", "<<LONGUEURS_P3BIS>>": f"`{lg}` (`{el}`)",
     "<<EMPREINTE_CONFIG_P3BIS>>": "0" * 64, "<<EMPREINTE_CONSIGNES_P3BIS>>": cs,
     "<<PIECES_SUR_MAIN_P3BIS>>": "commit du banc", "<<CHAINE_P3BIS>>": "chaîne du banc",
     "<<CONTRE_LECTURE_4_P3BIS>>": f"rapport `{rap}` (`{er}`), texte relu `{'1' * 64}`"}
for k, x in r.items():
    t = t.replace(k, x)
import re
assert not re.search(r"<<[A-Z0-9_]+>>", t), re.findall(r"<<[A-Z0-9_]+>>", t)
assert f"`{essai}`" in t and ee in t, "essai de fermeture non cité par le brouillon 10 sous ce chemin"
open(sys.argv[2], "w", encoding="utf-8").write(t)
EOF
mkdir -p docs/notes/bras-attaque
echo "témoin fabriqué par le banc (aucun contenu réel) : jamais extrait dans un clone de la chaîne (CD-05)" > docs/notes/bras-attaque/temoin-banc.txt
for f in "$ESSAI_V" "$V/longueurs-attendues-p3bis-banc-v1.json" "$RAPPORT" docs/notes/bras-attaque/temoin-banc.txt brouillons/P3-bis-temoin-positif-v1/*-banc.*; do
    (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256")
done
git add -A && git commit -qm "C2 : pièces hors de l'arbre gelé" && C2=$(git rev-parse HEAD)
REL_P=brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat-banc.md
REL_C=brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-banc.json
REL_K=brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-banc.md
sceller_s() { for f in "$P" "$CFG" "$CONSIGNES"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
cp "$REL_P" "$P"; cp "$REL_C" "$CFG"; cp "$REL_K" "$CONSIGNES"; sceller_s
git add -A && git commit -qm "S : scellement (banc)" && S0=$(git rev-parse HEAD)
git clone -q --bare . "$E/distant.git" || exit 2
cd "$E" || exit 2
# --- copie jouée --------------------------------------------------------------------------------------------------
"$PYB" -I - "$ICI/controles_avant_depense_p3bis_v2.sh" "$E/controles-banc.sh" "$E/distant.git" "$REL_P" "$(sha256sum "source/$REL_P" | cut -d' ' -f1)" \
    "$REL_C" "$(sha256sum "source/$REL_C" | cut -d' ' -f1)" "$REL_K" "$CONS_SHA" "$C1" "$ESSAI_V" "$E_ESSAI" \
    "$V/longueurs-attendues-p3bis-banc-v1.json" "$E_LONG" "$RAPPORT=$E_RAPPORT" "$PYB" "$C0" <<'EOF' || exit 2
import re, sys
src, dst, distant = sys.argv[1:4]
v = dict(zip(("CANDIDAT_RELU_CHEMIN", "CANDIDAT_RELU", "CONFIG_RELUE_CHEMIN", "CONFIG_RELUE", "CONSIGNES_RELUES_CHEMIN",
              "CONSIGNES_RELUES", "CODE_RELU", "ESSAI_FERMETURE_CHEMIN", "ESSAI_FERMETURE", "LONGUEURS_ATTENDUES_CHEMIN",
              "LONGUEURS_ATTENDUES", "RAPPORTS_ATTENDUS", "PY"), sys.argv[4:17]))
t = open(src, encoding="utf-8").read()
n = 0
def rep(a, b):
    global t, n
    assert t.count(a) == 1, a
    t = t.replace(a, b); n += 1
for k, x in v.items():
    lignes = re.findall(rf"^{k}=.*$", t, re.M)          # épinglée ou non (R-2367)
    assert len(lignes) == 1, k
    rep(lignes[0], f'{k}="{x}"')
rep(re.findall(r"^CODE_P3=.*$", t, re.M)[0], f"CODE_P3={sys.argv[17]}")
rep('git clone -q --no-checkout "$DEPOT_URL" "$D"', f'git clone -q --no-checkout "file://{distant}" "$D"')
rep('''HF_HOME="$W/cache-hf" PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" > "$W/longueurs-mesurees.json" 2> "$W/bloc-tokeniseur.txt" <<'EOF_TOK\'''',
    '''cat "${FAUSSE_MESURE:?}" > "$W/longueurs-mesurees.json"; cat > "$W/bloc-tokeniseur.txt" <<'EOF_TOK'   # bouchon du banc''')
rep('''PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" > "$W/bloc-gardes.txt" 2>&1 <<'EOF_GARDES\'''',
    '''cat > "$W/bloc-gardes.txt" <<'EOF_GARDES'   # bouchon du banc''')
rep('''PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no $FICHIERS > "$W/liste.txt" 2>&1; cs=$?''',
    '''printf '%s\\n' "${FAUX_SUITE:-531 passed in 1.00s}" > "$W/liste.txt"; cs=${FAUX_CODE_SUITE:-0}   # bouchon du banc''')
assert "A_EPINGLER" not in "\n".join(l for l in t.splitlines() if re.match(r"^[A-Z_]+=", l))
open(dst, "w", encoding="utf-8").write(t)
print(f"lignes changées dans la copie des contrôles : {n} (13 épingles, CODE_P3, clonage, trois bouchons)")
EOF
cp "$ICI/verifications_p3bis_v2.py" "$E/"          # module commun à côté de la copie jouée (H = dossier de la copie)
# --- cas -----------------------------------------------------------------------------------------------------------
variante() {   # $1 nom ; $2 commandes sur l'arbre de C2 (commit « base ») ; $3 commandes sur S (après la copie des relus) ; rend S'
    local b=$1
    git -C "$E/source" checkout -q -b "v/$b" "$C2"
    if [ "$2" != ":" ]; then (cd "$E/source" && eval "$2") && git -C "$E/source" add -A && git -C "$E/source" commit -qm "base $b"; fi
    (cd "$E/source" && cp "$REL_P" "$P" && cp "$REL_C" "$CFG" && cp "$REL_K" "$CONSIGNES" && eval "$3" && sceller_s)
    git -C "$E/source" add -A && git -C "$E/source" commit -qm "S $b" && git -C "$E/source" push -q "$E/distant.git" "v/$b"
    git -C "$E/source" rev-parse HEAD
    git -C "$E/source" checkout -q main
}
jouer() {   # $1 nom, $2 code attendu, $3 KO attendu (ou « - »), $4 S ; puis variables d'environnement
    local nom=$1 attendu=$2 koa=$3 s=$4 c v; shift 4
    NCAS=$((NCAS + 1))
    env -i PATH=/usr/bin:/bin HOME="$E" LANG=C.UTF-8 FAUSSE_MESURE="$E/mesure-saine.json" "$@" \
        bash "$E/controles-banc.sh" "$s" "$E/clone-$nom" calcul/p3bis-reel-v1 > "$E/console-$nom.txt" 2>&1; c=$?
    v=CONFORME
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    if [ "$koa" = - ]; then grep -q '^KO' "$E/console-$nom.txt" && v="NON CONFORME (KO inattendu : $(grep '^KO' "$E/console-$nom.txt" | head -2 | tr '\n' ' ' | cut -c1-200))"
    else grep -q "^KO  .*$koa" "$E/console-$nom.txt" || v="NON CONFORME (KO « $koa » absent)"; fi
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(grep -c '^KO' "$E/console-$nom.txt") KO ; $v"
    { grep '^KO' "$E/console-$nom.txt" | head -3; grep -v '^$' "$E/console-$nom.txt" | tail -1; } | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
    rm -rf "$E/clone-$nom" "$E/clone-$nom.travail" "$E/clone-$nom.liste.txt"
}
jouer K00-sain 0 - "$S0"
apres_k00() { local n; n=$(grep -c '^OK' "$E/console-K00-sain.txt"); NCAS=$((NCAS + 1))
    if [ "$n" -ge 30 ] && tail -1 "$E/console-K00-sain.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"; then echo "    cas sain : $n lignes OK, dernière ligne conforme : CONFORME"
    else echo "    cas sain : $n lignes OK : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi; }
apres_k00
NCAS=$((NCAS + 1)); if grep -q '^OK  0 clone en extraction partielle' "$E/console-K00-sain.txt"; then echo "    cas sain : clone en extraction partielle, témoin docs/notes/bras-attaque/ absent du disque : CONFORME"
else echo "    cas sain : extraction partielle non vue : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
jouer K01-s-ajoute-un-fichier 1 "1 contenu de S inattendu" "$(variante k01 : "echo x > autre.txt")"
jouer K02-commit-cite-deux-fois 1 "2 commit du code cité illisible, cité 2 fois" "$(variante k02 : "sed -i 's/^- Commit du code d.analyse : \(.*\)$/&\n- Commit du code d'\''analyse : \1/' $P")"
jouer K03-commit-cite-autre 1 "2 commit du code $C0 ≠ code relu épinglé" "$(variante k03 : "sed -i 's/$C1/$C0/' $P")"
jouer K04-arbre-gele-modifie 1 "2 arbre gelé de S modifié depuis le commit du code" "$(variante k04 "echo '# ajout' >> src/controle_ia/gardes.py" :)"
git -C "$E/source" checkout -q -b v/k05base "$C0" && echo "# modifié" >> "$E/source/src/controle_ia/gardes.py" && git -C "$E/source" commit -qam "C0 modifié" && C0M=$(git -C "$E/source" rev-parse HEAD) && git -C "$E/source" push -q "$E/distant.git" v/k05base && git -C "$E/source" checkout -q main
sed "s/^CODE_P3=.*/CODE_P3=$C0M/" "$E/controles-banc.sh" > "$E/controles-banc-k05.sh"; cp "$E/controles-banc.sh" "$E/controles-banc-sain.sh"; cp "$E/controles-banc-k05.sh" "$E/controles-banc.sh"
jouer K05-identite-fichier-de-p3-modifie 1 "3 identité avec P3" "$S0"
cp "$E/controles-banc-sain.sh" "$E/controles-banc.sh"
jouer K06-marqueur-restant 1 "4 marqueurs restants dans le texte : <<CHAINE_P3BIS>>" "$(variante k06 : "sed -i '0,/chaîne du banc/s//<<CHAINE_P3BIS>>/' $P")"
jouer K07-problemes-non-vide 1 "4 problemes() non vide" "$(variante k07 : "sed -i 's/^## Contre-lecture\$/## Contre-lecture retirée/' $P")"
jouer K08-texte-autre-que-le-relu 1 "4 $P de S ≠ candidat relu" "$(variante k08 : "sed -i 's/^## Seuil\$/## Seuil /' $P")"
jouer K09-config-autre-que-la-relue 1 "4 $CFG de S ≠ configuration relue" "$(variante k09 : "sed -i 's/\"lot\": 8/\"lot\": 8 /' $CFG")"
jouer K10-taches-non-citees 1 "4 tâches non citées par leur empreinte" "$(variante k10 : "sed -i 's/287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa/287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5ab/' $P")"
jouer K11-go-autre 1 "5 GO : GO-2026-11-08-13 : seul GO-2026-11-10-02" "$(variante k11 : "sed -i 's/^- GO : \*\*GO-2026-11-10-02\*\*/- GO : **GO-2026-11-08-13**/' $P")"
jouer K12-go-revoque 1 "5 GO : GO-2026-11-10-02 (ou GO-2026-11-02-29, qu'il prolonge) révoqué" "$(variante k12 "echo '| GO-2026-11-10-99 | 2026-11-10 | révocation | GO-2026-11-10-02 | — | 2026-11-10 | Lazar | essai |' >> registres/go.md" :)"
jouer K13-garde-de-calcul 1 "5 garde de calcul sur le registre de S" "$(variante k13 "echo '| GO-2026-11-09-98 | 2026-13-45 | calcul | dates illisibles | 1 USD | 2026-11-30 | Lazar | essai |' >> registres/go.md" :)"
jouer K14-essai-verse-non-conforme 1 "6 essai de fermeture : sortie" "$(variante k14 "echo 'NON CONFORME — variante' >> $ESSAI_V; echo 'ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME' >> $ESSAI_V; (cd brouillons/P3-bis-temoin-positif-v1 && sha256sum essai-fermeture-p3bis-v2-sortie-v1.txt > essai-fermeture-p3bis-v2-sortie-v1.txt.sha256)" :)"
jouer K15-essai-non-cite 1 "6 essai de fermeture : sortie" "$(variante k15 : "sed -i 's/$E_ESSAI/$(printf 'e%.0s' {1..64})/g' $P")"
jouer K16-essai-rejoue-non-conforme 1 "6 essai de fermeture rejoué au commit S" "$S0" FAUX_ESSAI_NON_CONFORME=1
jouer K17-longueurs-a-differe-de-t 1 "7 longueurs : t7 : indication_gabarit A 91 ≠ T 92" "$S0" FAUSSE_MESURE="$E/mesure-a-differe.json"
jouer K18-longueurs-resume-autre 1 "7 longueurs : résumé des longueurs" "$S0" FAUSSE_MESURE="$E/mesure-autre.json"
jouer K19-longueurs-non-citees 1 "7 longueurs attendues non citées" "$(variante k19 : "sed -i 's|\`$V/longueurs-attendues-p3bis-banc-v1.json\` (\`$E_LONG\`)|non citées|g' $P")"
jouer K20-n-cite-autre 1 "8 liste ciblée : « 531 passed" "$(variante k20 : "sed -i 's/^- Tests attendus : \`531\`/- Tests attendus : \`530\`/' $P")"
jouer K21-essai-en-echec 1 "8 liste ciblée : « 1 failed, 530 passed" "$S0" FAUX_SUITE="1 failed, 530 passed in 1.00s" FAUX_CODE_SUITE=1
jouer K22-liste-autre-empreinte 1 "8 liste ciblée absente ou d'empreinte autre" "$(variante k22 "echo '' >> scripts/essais-cibles-p3bis-v2.txt" :)"
jouer K23-versions-autres 1 "8 environnement PY" "$(variante k23 "sed -i 's/^numpy==.*/numpy==0.0.1/' requirements-cpu.txt" :)"
jouer K24-config-hors-ecarts 1 "9 configuration : écarts à celle de P3 hors des écarts du texte : \['lot'\]" "$(variante k24 "sed -i 's/\"lot\": 8/\"lot\": 4/' $REL_C; (cd brouillons/P3-bis-temoin-positif-v1 && sha256sum $(basename "$REL_C") > $(basename "$REL_C").sha256)" :)"
jouer K25-valeur-non-citee 1 "10 valeur(s) non citée(s) par le texte" "$(variante k25 : "sed -i 's/au plus \*\*2,10 USD de l.heure\*\*/au plus **2,50 USD de l'\''heure**/' $P")"
jouer K26-constante-autre 1 "10 constantes de la chaîne différentes" "$(variante k26 "sed -i 's/^GO_CALCUL=GO-2026-11-10-02/GO_CALCUL=GO-2026-11-08-13/' $V/lancer_p3bis_v2.sh" :)"
jouer K27-instance-avec-timeout 1 "11 scripts/p3bis_instance_v2.sh : commande « timeout »" "$(variante k27 "echo 'timeout 300m bash run.sh' >> scripts/p3bis_instance_v2.sh" :)"
jouer K28-instance-non-citee 1 "11 empreinte de scripts/p3bis_instance_v2.sh" "$(variante k28 : "sed -i 's/$E_INST/$(printf 'f%.0s' {1..64})/' $P")"
jouer K29-citation-en-double 1 "12 lecture précoce" "$(variante k29 : "sed -i 's/^- Chemin des consignes de P3 : \(.*\)$/&\n- Chemin des consignes de P3 : \1/' $P")"
jouer K30-lancement-autre-branche 1 "12 ligne « Lancement »" "$(variante k30 : "sed -i 's/\`BRANCHE=calcul\/p3bis-reel-v1\`/\`BRANCHE=calcul\/p3bis-reel-v9\`/' $P")"
git -C "$E/source" push -q "$E/distant.git" "$S0:refs/heads/calcul/p3bis-reel-v1"
jouer K31-branche-presente 1 "13 branche calcul/p3bis-reel-v1 : code 0" "$S0"
git -C "$E/source" push -q "$E/distant.git" --delete calcul/p3bis-reel-v1
jouer K32-rapport-absent 1 "14 rapport $RAPPORT absent" "$(variante k32 "git rm -q $RAPPORT $RAPPORT.sha256" :)"
jouer K33-sceau-faux-sous-docs 1 "14 verifier-arbre" "$(variante k33 "echo '0000000000000000000000000000000000000000000000000000000000000000  surveiller_p3bis_v2.sh' > $V/surveiller_p3bis_v2.sh.sha256" :)"
jouer K33b-sceau-faux-des-taches 1 "4 sceaux" "$(variante k33b "echo '0000000000000000000000000000000000000000000000000000000000000000  taches-pilote-60-v1.json' > donnees/t05-pilote-v1/taches-pilote-60-v1.json.sha256" :)"
# K36 : clone sans l'extraction partielle (ligne de la copie changée en « true ») : le témoin docs/notes/bras-attaque/ est
# extrait sur disque, refus avant tout contrôle (code 2)
sed 's|^git -C "$D" sparse-checkout set --no-cone .*$|true   # artefact du banc : extraction partielle retirée|' "$E/controles-banc.sh" > "$E/controles-banc-k36.sh"
[ "$(diff "$E/controles-banc.sh" "$E/controles-banc-k36.sh" | grep -c '^>')" = 1 ] || { echo "copie K36 non sûre"; exit 2; }
cp "$E/controles-banc.sh" "$E/controles-banc-sain.sh"; cp "$E/controles-banc-k36.sh" "$E/controles-banc.sh"
NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" LANG=C.UTF-8 FAUSSE_MESURE="$E/mesure-saine.json" bash "$E/controles-banc.sh" "$S0" "$E/clone-k36" calcul/p3bis-reel-v1 > "$E/console-K36.txt" 2>&1; c=$?
if [ "$c" = 2 ] && grep -q "REFUS : docs/notes/bras-attaque extrait sur disque" "$E/console-K36.txt" && ! grep -q '^OK  ' "$E/console-K36.txt"; then echo "K36-extraction-entiere-refusee : code 2 ; CONFORME"
else echo "K36-extraction-entiere-refusee : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
tail -1 "$E/console-K36.txt" | cut -c1-170 | sed 's/^/    | /'
cp "$E/controles-banc-sain.sh" "$E/controles-banc.sh"
# refus de départ (code 2)
k2() { local nom=$1; shift; NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" LANG=C.UTF-8 "$@" > "$E/console-$nom.txt" 2>&1
    local c=$?; if [ "$c" = 2 ]; then echo "$nom : code 2 ; CONFORME"; else echo "$nom : code $c ; NON CONFORME (2 attendu)"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
    grep -v '^$' "$E/console-$nom.txt" | tail -1 | cut -c1-170 | sed 's/^/    | /'; }
# K34 : artefact « épingles non remplies » fabriqué sur la copie jouée, les treize épingles remises à A_EPINGLER (R-2367)
sed -E 's/^(CANDIDAT_RELU|CANDIDAT_RELU_CHEMIN|CONFIG_RELUE|CONFIG_RELUE_CHEMIN|CONSIGNES_RELUES|CONSIGNES_RELUES_CHEMIN|CODE_RELU|ESSAI_FERMETURE|ESSAI_FERMETURE_CHEMIN|LONGUEURS_ATTENDUES|LONGUEURS_ATTENDUES_CHEMIN|RAPPORTS_ATTENDUS|PY)=.*$/\1=A_EPINGLER/' "$E/controles-banc.sh" > "$E/controles-banc-k34.sh"
[ "$(diff "$E/controles-banc.sh" "$E/controles-banc-k34.sh" | grep -c '^>')" = 13 ] && [ "$(grep -cE '^[A-Z_]+=A_EPINGLER$' "$E/controles-banc-k34.sh")" = 13 ] || { echo "copie K34 non sûre"; exit 2; }
k2 K34-epingles-non-remplies bash "$E/controles-banc-k34.sh" "$S0" "$E/clone-k34" calcul/p3bis-reel-v1
grep -q "A_EPINGLER" "$E/console-K34-epingles-non-remplies.txt" || { echo "    motif « A_EPINGLER » absent : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
k2 K35-usage bash "$E/controles-banc.sh" "$S0" "$E/clone-k35"
k2 K35b-branche-invalide bash "$E/controles-banc.sh" "$S0" "$E/clone-k35b" main
mkdir -p "$E/clone-k35c"; k2 K35c-dossier-existant bash "$E/controles-banc.sh" "$S0" "$E/clone-k35c" calcul/p3bis-reel-v1
echo "cas joués : $NCAS"
echo "FIN DU BANC DES CONTRÔLES DE P3-BIS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ]
