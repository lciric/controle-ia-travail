#!/usr/bin/env bash
# Relecture « dépense et arrêts » de la chaîne de P4-instrument, v1 : banc des vérifications du GO, de l'accord, des
# révocations, du plafond par lancement, de la borne de l'étape et de la garde de calcul gelée, sur des registres
# artefacts fabriqués ici (R5). Relecteur neuf ; n'écrit que sous RACINE_NEUVE ; le dépôt de travail est lu, jamais
# écrit (copie de src/ sans __pycache__, copies des registres, de la garde et du module) ; aucun réseau ; aucun outil de
# location (ce banc n'en appelle aucun) ; aucun texte d'action de P3 lu.
# Attendu de chaque cas : ce que le texte (brouillon 4) exige ; « refus » = code 1 du module commun (aucune création).
# Verdict d'un cas : CONFORME (le code égale l'attendu) ou ÉCART (le code diffère : constat de la relecture).
# Usage : banc_depense_verifications_v1.sh RACINE_NEUVE
set -uo pipefail
[ $# -eq 1 ] || { echo "usage : banc_depense_verifications_v1.sh RACINE_NEUVE"; exit 2; }
E=$(realpath -m "$1")
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
DEP=/home/user/controle-ia-travail
P4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
CH=$P4/chaine; MOD=$P4/module; B4=$P4/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERIF=$CH/verifications_p4_v1.py
export PYTHONDONTWRITEBYTECODE=1
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }
echo "banc de relecture (dépense et arrêts) : vérifications, v1"
for f in "$VERIF" "$MOD/instrument_p4_v1.py" "$DEP/.claude/hooks/garde_calcul.py" "$B4" "$0"; do
    echo "fichier relu : $(basename "$f") $(sha256sum "$f" | cut -d' ' -f1)"
done
for f in go.md decisions.md; do echo "registre copié : $f $(sha256sum "$DEP/registres/$f" | cut -d' ' -f1)"; done
X=$E/racine; V=docs/procedures/P4-instrument-v1
mkdir -p "$X/.claude/hooks" "$X/registres" "$X/$V" || exit 2
(cd "$DEP" && tar --exclude=__pycache__ -cf - src) | (cd "$X" && tar -xf -) || exit 2
cp "$DEP/.claude/hooks/garde_calcul.py" "$X/.claude/hooks/" && cp "$DEP/registres/go.md" "$DEP/registres/decisions.md" "$X/registres/" || exit 2
cp "$MOD"/*.py "$X/$V/" && cp "$CH/amorce_instance_p4_v1.sh" "$CH/p4_instance_v1.sh" "$X/$V/" || exit 2
cp "$X/registres/go.md" "$E/go-sauve.md"; cp "$X/registres/decisions.md" "$E/decisions-sauve.md"
cp "$X/.claude/hooks/garde_calcul.py" "$E/garde-sauve.py"
"$PY" -B "$CH/outils_essais_p4_v1.py" candidat "$B4" "$E/prereg.md" "$X" 7a54d431d89745839220f882b41b13e8c62ecfdd \
    "$(printf 0%.0s {1..64})" 1102 > /dev/null || { echo "texte d'essai impossible"; exit 2; }
echo "texte d'essai (tiré du brouillon 4 par outils_essais_p4_v1.py candidat) : $(sha256sum "$E/prereg.md" | cut -d' ' -f1)"
JOUR=$(date -u +%F); DEMAIN=$(date -u -d tomorrow +%F); HIER=$(date -u -d yesterday +%F)
echo "jour du banc : $JOUR"
ECARTS=0; N=0
remettre() { cp "$E/go-sauve.md" "$X/registres/go.md"; cp "$E/decisions-sauve.md" "$X/registres/decisions.md"; cp "$E/garde-sauve.py" "$X/.claude/hooks/garde_calcul.py"; }
go_col() {   # $1 colonne (1 à 8), $2 valeur : ligne de GO-2026-10-20-07 changée
    python3 - "$X/registres/go.md" "$1" "$2" <<'PYG'
import sys
from pathlib import Path
g, k, val = Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
L = g.read_text(encoding="utf-8").split("\n")
n = sum(l.startswith("| GO-2026-10-20-07 |") for l in L)
assert n == 1, n
L = ["|".join(c if i != k else f" {val} " for i, c in enumerate(l.split("|"))) if l.startswith("| GO-2026-10-20-07 |") else l for l in L]
g.write_text("\n".join(L), encoding="utf-8")
PYG
}
ligne_go() { printf '%s\n' "$1" >> "$X/registres/go.md"; }
ligne_dec() { printf '%s\n' "$1" >> "$X/registres/decisions.md"; }
accord_du_jour() { ligne_dec "| R-990 | ${2:-$JOUR} | ${1:-**Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation GO-2026-10-20-07 en cours.} | essai |"; }
verdict() {   # $1 nom, $2 attendu, $3 code, $4 fichier de sortie, $5 constat si écart
    local v; N=$((N + 1))
    if [ "$2" = "$3" ]; then v="CONFORME"; else v="ÉCART (attendu $2) ${5:-}"; ECARTS=$((ECARTS + 1)); fi
    echo "$1 : code $3 ; $v"
    grep -v '^$' "$4" | tail -1 | sed 's/^/    | /' | couper 230
}
cas_go() {   # $1 nom, $2 attendu, $3 jour, $4 borne, $5 constat si écart
    (cd "$X" && PYTHONPATH=src "$PY" -B "$VERIF" go . "$E/prereg.md" "$3" "$4") > "$E/sortie.txt" 2>&1
    verdict "$1" "$2" "$?" "$E/sortie.txt" "${5:-}"
}
cas_accord() {   # $1 nom, $2 attendu, $3 identifiant, $4 jour, $5 constat si écart
    (cd "$X" && PYTHONPATH=src "$PY" -B "$VERIF" accord . "$E/prereg.md" "$3" "$4") > "$E/sortie.txt" 2>&1
    verdict "$1" "$2" "$?" "$E/sortie.txt" "${5:-}"
}
cas_cli() {   # $1 nom, $2 attendu, $3 jour, $4 constat si écart : ligne de commande du module, telle que le lanceur la joue
    (cd "$X" && PYTHONPATH=src "$PY" -B "$V/instrument_p4_v1.py" --controle go --go GO-2026-10-20-07 --accord R-990 --jour "$3" --borne 5.41) > "$E/sortie.txt" 2>&1
    verdict "$1" "$2" "$?" "$E/sortie.txt" "${4:-}"
}
cas_module_seul() {   # $1 nom, $2 jour : verdict de controler_go seul (sans la garde gelée), pour situer qui refuse
    (cd "$X" && PYTHONPATH=src "$PY" -B - "$V/instrument_p4_v1.py" "$2" > "$E/sortie-module.txt" 2>&1 <<'PYM'
import importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("ip", sys.argv[1]); ip = importlib.util.module_from_spec(spec); spec.loader.exec_module(ip)
try:
    ip.controler_go("GO-2026-10-20-07", Path("registres/go.md").read_text(encoding="utf-8"),
                    Path("registres/decisions.md").read_text(encoding="utf-8"), sys.argv[2], 5.41)
    print("module seul : accepte")
except ip.GardeArret as e:
    print("module seul : refuse :", str(e)[:150])
PYM
    )
    echo "    module seul ($1) : $(tail -1 "$E/sortie-module.txt" | couper 200)"
}
echo "== GO et dépense : cas sains"
remettre; cas_go V00-sain 0 "$JOUR" 5.41
remettre; go_col 6 "$JOUR"; cas_go V01-echeance-le-jour-meme 0 "$JOUR" 5.41
echo "== GO échu, registre mal formé, garde qui refuse"
remettre; cas_go V02-go-echu-lendemain-de-l-echeance 1 2026-12-01 5.41
remettre; go_col 6 "$HIER"; cas_go V02b-echeance-hier 1 "$JOUR" 5.41
remettre; go_col 6 2026-11-31; cas_go V03-echeance-impossible-2026-11-31 1 "$JOUR" 5.41; cas_module_seul V03 "$JOUR"
remettre; go_col 2 "$DEMAIN"; cas_go V04-go-accorde-demain 1 "$JOUR" 5.41; cas_module_seul V04 "$JOUR"
remettre; go_col 3 Calcul; cas_go V05-type-Calcul-majuscule 1 "$JOUR" 5.41
remettre; go_col 7 lazar; cas_go V06-accorde-par-lazar-minuscule 1 "$JOUR" 5.41
remettre; ligne_go "| GO-2026-10-21-02 | $JOUR | calcul | ligne à sept colonnes (essai) | — | $JOUR | Lazar |"; cas_go V07-autre-ligne-a-sept-colonnes 1 "$JOUR" 5.41; cas_module_seul V07 "$JOUR"
remettre; grep '^| GO-2026-10-20-07 |' "$X/registres/go.md" | sed 's/^| GO-2026-10-20-07 |/|  GO-2026-10-20-07 |/' >> "$X/registres/go.md"; cas_go V08-go-cite-en-double-espaces-differents 1 "$JOUR" 5.41; cas_module_seul V08 "$JOUR"
remettre; sed -i 's/^| GO-2026-10-20-07 |/|GO-2026-10-20-07|/' "$X/registres/go.md"; cas_go V09-go-cite-sans-espace 1 "$JOUR" 5.41
remettre; printf '\xff\xfe registre abîmé\n' >> "$X/registres/go.md"; cas_go V10-registre-utf8-invalide 1 "$JOUR" 5.41
remettre; rm -f "$X/registres/go.md"; cas_go V11-registre-absent 1 "$JOUR" 5.41
remettre; rm -f "$X/.claude/hooks/garde_calcul.py"; cas_go V12-garde-absente 1 "$JOUR" 5.41
echo "== plafond par lancement (colonne « plafond » de GO-2026-10-20-07)"
remettre; go_col 5 "10 USD"; cas_go V20-plafond-10-USD-sans-par-lancement 1 "$JOUR" 5.41
remettre; go_col 5 "10 USD par lancement"; cas_go V21-plafond-exact 0 "$JOUR" 5.41
remettre; go_col 5 "$(printf '10\xc2\xa0USD par lancement')"; cas_go V22-plafond-espace-insecable 1 "$JOUR" 5.41
remettre; go_col 5 "≤ 10 USD par lancement"; cas_go V23-plafond-precede 1 "$JOUR" 5.41
remettre; go_col 5 "100 USD par lancement"; cas_go V24-plafond-100-USD 1 "$JOUR" 5.41
echo "== borne de l'étape"
for b in 10 10.0 1e1 nan inf -1 0 5,41 abc; do remettre; cas_go "V30-borne-$b" 1 "$JOUR" "$b"; done
remettre; cas_go V31-borne-9.99 0 "$JOUR" 9.99
echo "== révocations au registre des GO (huit colonnes, type « révocation ») : chaque identifiant, périmètre et référence"
for x in GO-2026-10-04-08 GO-2026-10-20-06 GO-2026-10-20-07 R-262 R-269; do
    remettre; ligne_go "| GO-2026-10-21-01 | $JOUR | révocation | révoque $x (essai) | — | $JOUR | Lazar | essai |"; cas_go "V40-perimetre-$x" 1 "$JOUR" 5.41
    remettre; ligne_go "| GO-2026-10-21-01 | $JOUR | révocation | essai | — | $JOUR | Lazar | message de Lazar : révoque $x |"; cas_go "V41-reference-$x" 1 "$JOUR" 5.41
done
echo "== révocations au registre des GO : formes voisines (ligne sans espace après la barre, type écrit autrement)"
for x in GO-2026-10-04-08 GO-2026-10-20-06 GO-2026-10-20-07 R-262 R-269; do
    remettre; ligne_go "|GO-2026-10-21-01|$JOUR|révocation|révoque $x (essai)|—|$JOUR|Lazar|essai|"
    cas_go "V42-sans-espace-$x" 1 "$JOUR" 5.41 "RC-depense-03"; cas_module_seul "V42-$x" "$JOUR"
done
for t in Révocation revocation RÉVOCATION; do
    remettre; ligne_go "| GO-2026-10-21-01 | $JOUR | $t | révoque GO-2026-10-20-07 (essai) | — | $JOUR | Lazar | essai |"
    cas_go "V43-type-$t" 1 "$JOUR" 5.41 "RC-depense-03"
done
remettre; ligne_go "| GO-2026-10-21-01 | $JOUR | révocation | révoque GO-2026-10-20-07 (essai) | — | $JOUR | Lazar |"; cas_go V44-revocation-a-sept-colonnes 1 "$JOUR" 5.41
remettre; ligne_go "| GO-2026-10-21-01 | $JOUR | révocation | révoque GO-2026-10-20-071 (essai) | — | $JOUR | Lazar | essai |"; cas_go V45-voisin-GO-2026-10-20-071-garde-par-sous-chaine 1 "$JOUR" 5.41; cas_module_seul V45 "$JOUR"
remettre; ligne_go "| GO-2026-10-21-01 | $DEMAIN | révocation | révoque R-269 (essai, datée demain) | — | $DEMAIN | Lazar | essai |"; cas_go V46-revocation-datee-demain 1 "$JOUR" 5.41
remettre; ligne_go "| GO-2026-10-21-01 | $JOUR | décision | aucune révocation de GO-2026-10-20-07 ni de R-269 (essai) | — | $JOUR | Lazar | essai |"; cas_go V47-mention-sans-revocation 0 "$JOUR" 5.41
echo "== révocations au registre des décisions (« **Révocation de R-262** » ou « **Révocation de R-269** » en tête de la cellule de décision)"
for x in R-262 R-269; do
    remettre; ligne_dec "| R-998 | $JOUR | **Révocation de $x** (essai). | essai |"; cas_go "V50-forme-exacte-$x" 1 "$JOUR" 5.41
    remettre; ligne_dec "|R-998|$JOUR|**Révocation de $x** (essai).|essai|"; cas_go "V51-forme-exacte-ligne-sans-espace-$x" 1 "$JOUR" 5.41 "RC-depense-03"
done
remettre; ligne_dec "| R-998 | $JOUR | **Révocation de R-262 et de R-269** (essai). | essai |"; cas_go V52-revocation-des-deux-en-une-cellule 1 "$JOUR" 5.41 "RC-depense-03"
remettre; ligne_dec "| R-998 | $JOUR | **Révocation de R-269.** (essai) | essai |"; cas_go V53-point-dans-le-gras 1 "$JOUR" 5.41 "RC-depense-03"
remettre; ligne_dec "| R-998 | $JOUR | **Révocation de la délégation R-269** (essai). | essai |"; cas_go V54-delegation-nommee 1 "$JOUR" 5.41 "RC-depense-03"
remettre; ligne_dec "| R-998 | $JOUR | Note (essai) : la forme « **Révocation de R-269** » est décrite ici, sans révoquer. | essai |"; cas_go V55-forme-citee-sans-revoquer 0 "$JOUR" 5.41
echo "== accord du jour (ligne R-… du registre des décisions)"
remettre; accord_du_jour; cas_accord A00-accord-sain-delegation 0 R-990 "$JOUR"
remettre; accord_du_jour "**Accord de Lazar pour le lancement de P4-instrument** (essai) : message de Lazar dans la session ce jour-là."; cas_accord A01-accord-sain-message-du-jour 0 R-990 "$JOUR"
remettre; accord_du_jour "" "$HIER"; cas_accord A02-accord-d-hier 1 R-990 "$JOUR"
remettre; accord_du_jour "" "$DEMAIN"; cas_accord A03-accord-de-demain 1 R-990 "$JOUR"
remettre; accord_du_jour "Accord de Lazar pour le lancement de P4-instrument (essai, sans gras) : GO-2026-10-20-07."; cas_accord A04-sans-la-forme-exacte 1 R-990 "$JOUR"
remettre; accord_du_jour "**Accord de Lazar pour le lancement de P4-instrument** (essai)."; cas_accord A05-ne-cite-ni-go-ni-message 1 R-990 "$JOUR"
remettre; accord_du_jour; accord_du_jour; cas_accord A06-accord-en-double 1 R-990 "$JOUR"
remettre; accord_du_jour; cas_accord A07-identifiant-mal-forme 1 R-99999 "$JOUR"
remettre; accord_du_jour "" 2026-12-01; cas_accord A08-accord-du-jour-go-echu 1 R-990 2026-12-01
remettre; accord_du_jour "**Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation GO-2026-10-20-071."; cas_accord A09-cite-un-go-voisin 1 R-990 "$JOUR" "RC-depense-09"
remettre; accord_du_jour "**Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation GO-2026-10-20-07 ; dépense consignée 148,00 USD + borne 5,41 USD = 153,41 USD, au-dessus des 150 USD de la phase."
cas_accord A10-accord-qui-ecrit-le-plafond-de-phase-depasse 1 R-990 "$JOUR" "RC-depense-05"
echo "== ligne de commande du module (--controle go), telle que le lanceur la joue"
remettre; accord_du_jour; cas_cli C00-sain 0 "$JOUR"
remettre; accord_du_jour; ligne_go "|GO-2026-10-21-01|$JOUR|révocation|révoque GO-2026-10-04-08 (essai)|—|$JOUR|Lazar|essai|"; cas_cli C01-revocation-sans-espace-de-la-phase 1 "$JOUR" "RC-depense-03"
remettre; accord_du_jour; ligne_dec "| R-998 | $JOUR | **Révocation de R-262 et de R-269** (essai). | essai |"; cas_cli C02-revocation-des-deux-decisions 1 "$JOUR" "RC-depense-03"
echo "== garde gelée remplacée dans l'arbre de travail (aucune empreinte relue par la chaîne)"
remettre; python3 - "$X/.claude/hooks/garde_calcul.py" <<'PYG'
import sys
from pathlib import Path
p = Path(sys.argv[1]); t = p.read_text(encoding="utf-8")
t = t.replace("def decider(commande: str, aujourd_hui: date) -> None:\n", "def decider(commande: str, aujourd_hui: date) -> None:\n    return  # garde neutralisée (artefact du banc)\n", 1)
p.write_text(t, encoding="utf-8")
PYG
echo "    garde de l'arbre de travail : $(sha256sum "$X/.claude/hooks/garde_calcul.py" | cut -d' ' -f1) (gelée : $(sha256sum "$E/garde-sauve.py" | cut -d' ' -f1))"
go_col 2 "$DEMAIN"; ligne_go "| GO-2026-10-21-02 | $JOUR | calcul | ligne à sept colonnes (essai) | — | $JOUR | Lazar |"
cas_go V60-garde-neutralisee-go-accorde-demain-et-registre-mal-forme 1 "$JOUR" 5.41 "RC-depense-04"
remettre
P_CACHE=$(find "$X" "$CH" "$MOD" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit (copie, chaîne, module)" || echo "__pycache__ écrit : $P_CACHE"
echo "FIN DU BANC DE RELECTURE DES VÉRIFICATIONS : $N cas ; écarts au texte : $ECARTS"
