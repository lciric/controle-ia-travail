#!/usr/bin/env bash
# Banc du module commun de la chaîne de P4-instrument, verifications_p4_v1.py (R5 : chaque garde, un cas sain et des
# artefacts), v1, neuf (la chaîne de P3 éprouvait ses sous-gardes dans le banc des contrôles ; celles de P4 sont plus
# nombreuses et se jouent ici, sans clone par cas). Sous-commandes go, accord, module (fonctions du module de P4, chargé
# à l'empreinte que cite le texte), preuves et repetition, sur des registres, des textes et des journaux altérés ou
# synthétiques. Racine d'essai : clone partagé de DEPOT_SOURCE au commit C (module de P4 versé), sans extraction des PDF
# de docs/sources ; une racine par cas, faite de liens vers src/, docs/ et .claude/ du clone (code et garde gelée) et de
# ses propres registres/ (copies changées). Texte d'essai : candidat tiré du brouillon 4 par outils_essais_p4_v1.py
# (lignes « Module de P4 » aux empreintes des fichiers de C). Registres d'essai : ceux de C (GO-2026-10-20-07, R-262,
# R-269 y sont consignés), plus une ligne d'accord du jour fabriquée. Aucun outil de location, aucun réseau. Verdict par
# cas : code attendu et motif attendu sur la dernière ligne ; sort en code 1 s'il reste un cas non conforme.
# Usage : essais_verifications_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || { echo "usage : essais_verifications_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; R=$(realpath -m "$3")
SOI=$(realpath "$0")
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERIF=$H/verifications_p4_v1.py
V=docs/procedures/P4-instrument-v1
GO=GO-2026-10-20-07
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --shared --no-checkout "$SRC" source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
CE=$(git rev-parse --verify -q "$C^{commit}") || { echo "commit $C introuvable"; exit 2; }
git sparse-checkout set --no-cone '/*' '!/docs/sources/pdf/' '!/docs/sources/lecture-pdf-niveau1/' '!/docs/sources/lecture-pdf-niveau2/' \
    && git checkout -q "$CE" || exit 2
echo "C = $CE"
for s in verifications_p4_v1.py outils_essais_p4_v1.py; do echo "script éprouvé : $s $(sha256sum "$H/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
for n in instrument_p4_v1.py lecture_p4_v1.py mesures_conception_p4_v1.py test_instrument_p4_v1.py test_lecture_p4_v1.py \
         test_gardes_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh; do
    [ -f "$V/$n" ] || { echo "$V/$n absent de C"; exit 2; }
done
JOUR=$(date -u +%F); HIER=$(date -u -d yesterday +%F)
"$PY" -B "$H/outils_essais_p4_v1.py" candidat "$B4" "$R/texte-sain.md" . 7a54d431d89745839220f882b41b13e8c62ecfdd \
    "$(printf 0%.0s {1..64})" 1102 > /dev/null 2>"$R/candidat.err" || { echo "candidat d'essai impossible : $(tail -1 "$R/candidat.err")"; exit 2; }
cp registres/go.md "$R/go-sain.md"
{ cat registres/decisions.md; echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; dépense consignée et borne de l'étape sous 150 USD. | essai |"; } > "$R/decisions-sain.md"
grep -q "^| $GO |" "$R/go-sain.md" || { echo "$GO absent du registre de C"; exit 2; }
NON_CONFORMES=0
racine() {   # $1 nom : racine d'un cas (liens vers le code, registres copiés)
    local r="$R/racine-$1"
    mkdir -p "$r/registres" && ln -s "$R/source/src" "$r/src" && ln -s "$R/source/docs" "$r/docs" && ln -s "$R/source/.claude" "$r/.claude" \
        && cp "$R/go-sain.md" "$r/registres/go.md" && cp "$R/decisions-sain.md" "$r/registres/decisions.md" || { echo "racine $1 impossible"; exit 2; }
    printf '%s' "$r"
}
verdict() {   # $1 nom, $2 code obtenu, $3 code attendu, $4 motif attendu (dernière ligne), $5 sortie
    local v="CONFORME"
    [ "$2" = "$3" ] || v="NON CONFORME (code $2, attendu $3)"
    tail -1 "$5" | grep -qF -- "$4" || v="NON CONFORME (motif « $4 » absent de la dernière ligne)"
    grep -q "^Traceback" "$5" && v="NON CONFORME (trace d'exception)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$1 : code $2 ; $v"
    # la ligne affichée est une citation : « NON CONFORME » y est masqué, pour que le journal du banc ne porte aucune
    # ligne d'échec (verifications_p4_v1.py preuves refuse tout journal qui en contient une)
    tail -1 "$5" | couper 180 | sed -e 's/^/    | /' -e 's/NON CONFORME/NON-CONFORME (cité)/g'
}
cas_go() {   # $1 nom, $2 code attendu, $3 motif, $4 commande sur le texte, $5 sur go.md, $6 sur decisions.md, $7 jour, $8 borne
    local n=$1 r t c; r=$(racine "$n"); t="$R/texte-$n.md"
    eval "$4" < "$R/texte-sain.md" > "$t"
    eval "$5" < "$R/go-sain.md" > "$r/registres/go.md"; eval "$6" < "$R/decisions-sain.md" > "$r/registres/decisions.md"
    "$PY" -B "$VERIF" go "$r" "$t" "${7:-$JOUR}" "${8:-5.41}" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$2" "$3" "$R/sortie-$n.txt"
}
ajout_go() { printf "cat; echo '%s'" "$1"; }          # commande qui ajoute une ligne au registre lu sur l'entrée
cat > "$R/colonne.py" <<'PYC'
import sys
ident, k, valeur = sys.argv[1], int(sys.argv[2]), sys.argv[3]
L = sys.stdin.read().split("\n")
print("\n".join(("|".join(c if i != k else f" {valeur} " for i, c in enumerate(l.split("|"))) if l.startswith(f"| {ident} |") else l)
                for l in L), end="")
PYC
colonne_go() {   # $1 numéro de colonne (1 à 8), $2 valeur : commande qui change cette colonne de la ligne de GO-2026-10-20-07
    printf "python3 %q %q %q %q" "$R/colonne.py" "$GO" "$1" "$2"
}
# --- GO et dépense (texte, registre des GO, registre des décisions, jour, borne)
cas_go G00-sain 0 "$GO conforme" cat cat cat
cas_go G01-texte-sans-ligne-go 1 "absente, en double ou mal formée" "sed '/GO cité par la commande de création/d'" cat cat
cas_go G02-ligne-go-en-double 1 "absente, en double ou mal formée" "sed 's/^\\(  - \\*\\*GO cité par la commande de création\\*\\* : .*\\)\$/\\1\\n\\1/'" cat cat
cas_go G03-texte-cite-le-go-de-la-phase 1 "seul $GO est accepté" "sed 's/\`GO_ID=$GO\`/\`GO_ID=GO-2026-10-04-08\`/'" cat cat
cas_go G03b-ligne-go-mal-formee 1 "absente, en double ou mal formée" "sed 's/\`GO_ID=$GO\`/\`$GO\`/'" cat cat
cas_go G04-go-absent-du-registre 1 "$GO absent ou en double au registre des GO" cat "sed '/^| $GO |/d'" cat
cas_go G04b-go-en-double-au-registre 1 "absent ou en double" cat "sed 's/^| $GO |.*/&\\n&/'" cat
cas_go G05-go-d-un-autre-type 1 "de type « calcul », accordée par Lazar" cat "$(colonne_go 3 revendication)" cat
cas_go G06-go-accorde-par-la-session 1 "de type « calcul », accordée par Lazar" cat "$(colonne_go 7 session)" cat
cas_go G07-plafond-sans-le-prefixe 1 "ne commence pas par « 10 USD par lancement »" cat "$(colonne_go 5 '12 USD par lancement (essai)')" cat
cas_go G07b-plafond-au-prefixe-voisin 1 "ne commence pas par « 10 USD par lancement »" cat "$(colonne_go 5 '10 USD au plus par lancement (essai)')" cat
cas_go G07c-plafond-au-prefixe-exact 0 "$GO conforme" cat "$(colonne_go 5 '10 USD par lancement (essai)')" cat
cas_go G08-go-echu 1 "échu" cat "$(colonne_go 6 "$HIER")" cat
cas_go G08b-jour-de-l-echeance 0 "$GO conforme" cat cat cat 2026-11-30
cas_go G08c-lendemain-de-l-echeance 1 "échu" cat cat cat 2026-12-01
cas_go G08d-jour-mal-forme 1 "jour mal formé" cat cat cat 20-10-2026
cas_go G09-borne-de-10-usd 1 "inférieure à 10 USD" cat cat cat "$JOUR" 10
cas_go G09b-borne-juste-sous-10-usd 0 "borne de l'étape 9.99 USD" cat cat cat "$JOUR" 9.99
cas_go G09c-borne-nulle 1 "inférieure à 10 USD" cat cat cat "$JOUR" 0
cas_go G09d-borne-illisible 1 "illisible" cat cat cat "$JOUR" abc
for x in GO-2026-10-04-08 GO-2026-10-20-06 GO-2026-10-20-07 R-262 R-269; do
    cas_go "G10-revocation-au-registre-des-go-qui-nomme-$x" 1 "révocation au registre des GO (GO-2026-10-20-98)" cat \
        "$(ajout_go "| GO-2026-10-20-98 | $JOUR | révocation | révoque $x (essai) | — | $JOUR | Lazar | essai |")" cat
done
cas_go G10b-revocation-nommee-dans-la-reference 1 "révocation au registre des GO (GO-2026-10-20-98)" cat \
    "$(ajout_go "| GO-2026-10-20-98 | $JOUR | révocation | délégation de P4 (essai) | — | $JOUR | Lazar | R-269 (essai) |")" cat
# identifiant voisin d'un GO : le module ne le lit pas comme une révocation (identifiants entiers), mais la garde gelée
# compare par sous-chaîne et refuse ; la garde n'est jamais contournée : refus attendu, motif de la garde
cas_go G10c-revocation-d-un-go-voisin-refusee-par-la-garde 1 "garde de calcul gelée : GARDE (registres/go, R10) — commande bloquée : $GO révoqué par GO-2026-10-20-98" cat \
    "$(ajout_go "| GO-2026-10-20-98 | $JOUR | révocation | révoque GO-2026-10-20-071 (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go G10c2-revocation-d-une-decision-voisine 0 "$GO conforme" cat \
    "$(ajout_go "| GO-2026-10-20-98 | $JOUR | révocation | révoque R-2620 et R-2690 (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go G10d-revocation-a-sept-colonnes 1 "huit colonnes attendues" cat \
    "$(ajout_go "| GO-2026-10-20-98 | $JOUR | révocation | révoque $GO (essai) | — | $JOUR | Lazar |")" cat
cas_go G10e-ligne-qui-mentionne-une-revocation 0 "$GO conforme" cat \
    "$(ajout_go "| GO-2026-10-20-97 | $JOUR | décision | essai : aucune révocation de $GO ni de R-269 | — | $JOUR | Lazar | essai |")" cat
for x in R-262 R-269; do
    cas_go "G11-revocation-au-registre-des-decisions-$x" 1 "révocation au registre des décisions (R-998)" cat cat \
        "$(ajout_go "| R-998 | $JOUR | **Révocation de $x** (essai). | essai |")"
done
cas_go G11b-forme-de-revocation-ailleurs-qu-en-tete 0 "$GO conforme" cat cat "$(ajout_go "| R-998 | $JOUR | Note (essai) : la forme « **Révocation de R-262** » est décrite ici, sans révoquer. | essai |")"
cas_go G11c-revocation-d-une-autre-decision 0 "$GO conforme" cat cat "$(ajout_go "| R-998 | $JOUR | **Révocation de R-192** (essai). | essai |")"
cas_go G12-garde-gelee-qui-refuse-un-registre-mal-forme 1 "garde de calcul gelée" cat \
    "$(ajout_go "| GO-2026-10-20-96 | $JOUR | calcul | essai à sept colonnes | — | $JOUR | Lazar |")" cat
cas_go G12b-garde-gelee-qui-refuse-une-date-illisible 1 "garde de calcul gelée" cat \
    "$(ajout_go "| GO-2026-10-20-96 | hier | calcul | essai | — | $JOUR | Lazar | essai |")" cat
cas_go G13-module-non-cite-a-son-empreinte 1 "aucun code non cité n'est exécuté" \
    "sed 's|\\(Module de P4 : \`$V/instrument_p4_v1.py\` : \`\\)[0-9a-f]\\{64\\}|\\1$(printf 'a%.0s' {1..64})|'" cat cat
cas_go G13b-ligne-du-module-absente 1 "absente, en double ou mal formée" "sed '\\|Module de P4 : \`$V/instrument_p4_v1.py\`|d'" cat cat
r=$(racine G14); rm -f "$r/registres/decisions.md"
"$PY" -B "$VERIF" go "$r" "$R/texte-sain.md" "$JOUR" 5.41 > "$R/sortie-G14.txt" 2>&1; verdict G14-registre-des-decisions-absent "$?" 1 "absent ou illisible" "$R/sortie-G14.txt"
# --- accord du jour
cas_accord() {   # $1 nom, $2 code attendu, $3 motif, $4 identifiant, $5 commande sur decisions.md, $6 jour, $7 commande sur go.md
    local n=$1 r c; r=$(racine "$n")
    eval "$5" < "$R/decisions-sain.md" > "$r/registres/decisions.md"; eval "${7:-cat}" < "$R/go-sain.md" > "$r/registres/go.md"
    "$PY" -B "$VERIF" accord "$r" "$R/texte-sain.md" "$4" "${6:-$JOUR}" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$2" "$3" "$R/sortie-$n.txt"
}
cas_accord A00-accord-qui-cite-la-delegation 0 "(cite $GO) : conforme" R-999 cat
cas_accord A00b-accord-qui-cite-un-message-du-jour 0 "(cite un message de Lazar du jour) : conforme" R-999 \
    "sed 's/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : message de Lazar dans la session ce jour-là. | essai |/'"
cas_accord A01-accord-absent 1 "R-999 absent ou en double" R-999 "sed '/^| R-999 |/d'"
cas_accord A02-accord-en-double 1 "R-999 absent ou en double" R-999 "sed 's/^| R-999 |.*/&\\n&/'"
cas_accord A03-accord-d-un-autre-jour 1 "ligne du jour ($JOUR) attendue" R-999 "sed 's/^| R-999 | $JOUR |/| R-999 | $HIER |/'"
cas_accord A04-sans-la-forme-exacte 1 "ne commence pas par « **Accord de Lazar pour le lancement de P4-instrument** »" R-999 \
    "sed 's/^| R-999 | $JOUR | .*/| R-999 | $JOUR | Accord de Lazar pour le lancement de P4-instrument (essai), $GO. | essai |/'"
cas_accord A04b-forme-ailleurs-qu-en-tete 1 "ne commence pas par" R-999 \
    "sed 's/^| R-999 | $JOUR | .*/| R-999 | $JOUR | Note (essai) : **Accord de Lazar pour le lancement de P4-instrument** attendu, $GO. | essai |/'"
cas_accord A04c-forme-de-p3 1 "ne commence pas par" R-999 \
    "sed 's/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P3** (essai), $GO. | essai |/'"
cas_accord A05-ne-cite-ni-go-ni-message 1 "ne cite ni $GO ni un message de Lazar" R-999 \
    "sed 's/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai). | essai |/'"
cas_accord A06-go-echu-le-jour-de-l-accord 1 "échu ou illisible" R-999 cat "$JOUR" "$(colonne_go 6 "$HIER")"
cas_accord A07-identifiant-mal-forme 1 "mal formé" 999 cat
# --- module cité
cas_module() {   # $1 nom, $2 code attendu, $3 motif, $4 commande sur le texte
    local n=$1 r c t="$R/texte-$1.md"; r=$(racine "$n")
    eval "$4" < "$R/texte-sain.md" > "$t"
    "$PY" -B "$VERIF" module "$r" "$t" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$2" "$3" "$R/sortie-$n.txt"
}
cas_module M00-module-sain 0 "$V/test_lecture_p4_v1.py " cat
[ "$(grep -c . "$R/sortie-M00-module-sain.txt")" = 6 ] && echo "    six fichiers à l'empreinte citée : CONFORME" || { echo "    nombre de fichiers : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cas_module M01-ligne-d-un-test-absente 1 "sans ligne « Module de P4 »" "sed '\\|Module de P4 : \`$V/test_gardes_p4_v1.py\`|d'"
cas_module M02-empreinte-d-un-test-fausse 1 "empreinte" "sed 's|\\(Module de P4 : \`$V/test_lecture_p4_v1.py\` : \`\\)[0-9a-f]\\{64\\}|\\1$(printf 'b%.0s' {1..64})|'"
cas_module M03-ligne-hors-du-module 1 "hors du module" "sed 's|^\\(  - Module de P4 : \`$V/test_gardes_p4_v1.py\` : .*\\)\$|\\1\\n  - Module de P4 : \`$V/autre_p4_v1.py\` : \`$(printf 'c%.0s' {1..64})\`|'"
cas_module M04-ligne-mal-formee 1 "mal formée" "sed 's|^\\(  - Module de P4 : \`$V/lecture_p4_v1.py\` : \`[0-9a-f]*\\)\`|\\1|'"
# --- preuves des essais (journaux synthétiques)
PRV=$R/preuves; mkdir -p "$PRV/sain"
ecrire_preuves() {   # $1 dossier : les six journaux sains, empreintes factices cohérentes
    "$PY" -I -B - "$1" "$VERIF" <<'PYP'
import importlib.util, sys
d, verif = sys.argv[1:3]
spec = importlib.util.spec_from_file_location("v", verif); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
for n, (verdict, scripts) in v.JOURNAUX.items():
    open(f"{d}/{n}", "w", encoding="utf-8").write("".join(f"script éprouvé : {x} {'a' * 64}\n" for x in sorted(scripts)) + verdict + "\n")
PYP
}
preuve() {   # $1 nom, $2 code attendu, $3 motif, $4 dossier, puis les journaux nommés
    local n=$1 a=$2 m=$3 d=$4 c; shift 4
    "$PY" -B "$VERIF" preuves "$d" "$@" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$a" "$m" "$R/sortie-$n.txt"
}
ecrire_preuves "$PRV/sain"
preuve P00-preuves-saines 0 "verifications_p4_v1.py $(printf 'a%.0s' {1..64})" "$PRV/sain"
[ "$(grep -c . "$R/sortie-P00-preuves-saines.txt")" = 13 ] && echo "    treize scripts éprouvés : CONFORME" || { echo "    nombre de scripts éprouvés : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
preuve P00b-preuves-quatre-journaux 0 "verifications_p4_v1.py" "$PRV/sain" banc-lanceur-p4-v1.log banc-surveillance-p4-v1.log banc-verifications-p4-v1.log banc-controles-p4-v1.log
for k in 1 2 3; do
    mkdir -p "$PRV/faute-$k"; ecrire_preuves "$PRV/faute-$k"
    case $k in 1) l="cas X : code 1 ; NON CONF""ORME (essai)" ;; 2) l="Traceback (most recent call last): essai" ;; 3) l="JETON AFFI""CHÉ : sortie-essai.txt" ;; esac
    sed -i "1a $l" "$PRV/faute-$k/banc-scellement-p4-v1.log"
    preuve "P0$k-preuves-ligne-d-echec" 1 "ligne d'échec avant le verdict" "$PRV/faute-$k"
done
mkdir -p "$PRV/deux"; ecrire_preuves "$PRV/deux"
sed -i "s/^script éprouvé : verifications_p4_v1.py a*$/script éprouvé : verifications_p4_v1.py $(printf 'b%.0s' {1..64})/" "$PRV/deux/banc-lanceur-p4-v1.log"
preuve P04-preuves-deux-empreintes 1 "éprouvé sous deux empreintes" "$PRV/deux"
mkdir -p "$PRV/manque"; ecrire_preuves "$PRV/manque"; sed -i '/^script éprouvé : essais_controles_p4_v1.sh /d' "$PRV/manque/banc-controles-p4-v1.log"
preuve P05-preuves-script-non-eprouve 1 "manquants ['essais_controles_p4_v1.sh']" "$PRV/manque"
mkdir -p "$PRV/verdict"; ecrire_preuves "$PRV/verdict"; sed -i 's/cas non conformes : 0$/cas non conformes : 2/' "$PRV/verdict/banc-verifications-p4-v1.log"
preuve P06-preuves-verdict-non-conforme 1 "dernière ligne" "$PRV/verdict"
mkdir -p "$PRV/absent"; ecrire_preuves "$PRV/absent"; rm -f "$PRV/absent/repetition-finale-p4-v1.log"
preuve P07-preuves-journal-absent 1 "journal repetition-finale-p4-v1.log absent" "$PRV/absent"
preuve P08-preuves-journal-inconnu 1 "inconnus ou en double" "$PRV/sain" banc-autre-p4-v1.log
mkdir -p "$PRV/forme"; ecrire_preuves "$PRV/forme"; sed -i '1a script éprouvé : Autre.sh abc' "$PRV/forme/banc-lanceur-p4-v1.log"
preuve P09-preuves-ligne-mal-formee 1 "mal formée" "$PRV/forme"
# octet invalide (ligne coupée par octets au milieu d'un caractère) : refus net, sans trace d'exception
cat > "$R/octet.py" <<'PYO'
import sys
b = sys.stdin.buffer.read().split(b"\n")
b.insert(1, b"    | ligne coup\xc3")
sys.stdout.buffer.write(b"\n".join(b))
PYO
mkdir -p "$PRV/octets"; ecrire_preuves "$PRV/octets"
python3 -I "$R/octet.py" < "$PRV/sain/banc-surveillance-p4-v1.log" > "$PRV/octets/banc-surveillance-p4-v1.log"
preuve P10-preuves-utf8-invalide 1 "UTF-8 invalide" "$PRV/octets"
# --- journal de la répétition jouet (synthétique, conforme au module commun, puis altéré)
CODE_R=$(printf '1%.0s' {1..40}); NOM_C=P4-instrument-v1-candidat-essai.md; SHA_C=$(printf 'd%.0s' {1..64})
"$PY" -I -B - "$VERIF" "$CODE_R" "$NOM_C" "$SHA_C" > "$R/journal-repetition-sain.txt" <<'PYJ'
import importlib.util, sys
verif, code, nom, sha = sys.argv[1:5]
spec = importlib.util.spec_from_file_location("v", verif); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
print(f"commit du code répété : {code}\ncandidat répété : {nom} {sha}")
for s in sorted(v.SCRIPTS):
    print(f"script répété : {s} {'e' * 64}")
for p in v.PASSAGES:
    print(p + "; durée totale 1 s")
for x in v.CONFORMES:
    print(x); print("    --  3f versions non comparées (essai)")
print("lecture jouet (passage-1-sain) : code 0 ; issue L3")
for x, ko in v.ARTEFACTS.items():
    print(x); print(ko + "essai")
print("FIN DE LA RÉPÉTITION")
PYJ
module_rep() {   # $1 nom, $2 code attendu, $3 motif, $4 commande sur le journal
    local n=$1 c j="$R/journal-$1.txt"
    eval "$4" < "$R/journal-repetition-sain.txt" > "$j"
    "$PY" -B "$VERIF" repetition "$CODE_R" "$j" "$NOM_C" "$SHA_C" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$2" "$3" "$R/sortie-$n.txt"
}
module_rep J00-journal-sain 0 "repetition_jouet_p4_v1.sh $(printf 'e%.0s' {1..64})" cat
module_rep J01-candidat-autre 1 "ligne absente ou en double : candidat répété" "sed 's/^candidat répété : .*/candidat répété : autre.md 0000/'"
module_rep J02-commit-autre 1 "ligne absente ou en double : commit du code répété" "sed 's/^commit du code répété : .*/commit du code répété : $(printf '2%.0s' {1..40})/'"
module_rep J03-passage-manquant 1 "passage : passage 4-plafond-de-l-amorce : code 124" "sed '/^passage 4-plafond-de-l-amorce : /d'"
module_rep J04-passage-autre-code 1 "passage : passage 1-sain : code 0" "sed 's/^passage 1-sain : code 0 /passage 1-sain : code 1 /'"
module_rep J05-recuperation-conforme-absente 1 "ligne absente ou en double : récupération (arret-synthetique)" "sed '/^récupération (arret-synthetique) : /d'"
module_rep J06-ko-dans-un-cas-sain 1 "récupération (gardes-reelles)" "sed '/^récupération (gardes-reelles) : /a\\    KO  6b essai'"
module_rep J07-artefact-a-deux-ko 1 "récupération (artefact-scores-alteres)" "sed '/^récupération (artefact-scores-alteres) : /a\\    KO  4d essai'"
module_rep J08-artefact-autre-ko 1 "récupération (artefact-ajout-hors-perimetre)" "sed 's/^    KO  1c /    KO  1d /'"
module_rep J09-ko-hors-du-bloc 1 "récupération (artefact-texte-dans-le-journal)" "awk '/^    KO  4f /&&!v{v=1; next} {print}'"
module_rep J10-script-mal-forme 1 "ligne « script répété » mal formée" "sed '0,/^script répété : /s/^script répété : \\([a-z0-9_]*\\)_v1\\.\\([a-z]*\\) /script répété : \\1.\\2 /'"
module_rep J11-script-en-double 1 "script répété en double" "awk '/^script répété : /&&!d{print; d=1} {print}'"
module_rep J12-script-manquant 1 "les trois attendus exactement" "sed '0,/^script répété : /{/^script répété : /d}'"
module_rep J13-fin-absente 1 "ligne absente ou en double : FIN DE LA RÉPÉTITION" "sed '/^FIN DE LA RÉPÉTITION$/d'"
module_rep J14-destruction-absente-d-un-cas-sain 1 "ligne absente ou en double : récupération (textes-degeneres)" "sed 's/^\\(récupération (textes-degeneres) : .*\\) ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)$/\\1/'"
module_rep J15-artefact-instance-detruite 1 "ligne absente ou en double : récupération (artefact-etiquette-autre)" "sed 's/^\\(récupération (artefact-etiquette-autre) : code 1 ; .*\\) ; INSTANCE 99999999 NON DÉTRUITE : NŒUD DE LAZAR$/\\1 ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)/'"
module_rep J16-tous-conformes-de-trop 1 "récupérations conformes, chacune suivie de la destruction" "sed '\$a récupération (autre) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)'"
module_rep J17-echec-sans-destruction-de-trop 1 "récupérations en échec, chacune sans destruction" "sed '\$a récupération (autre) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC ; INSTANCE 99999999 NON DÉTRUITE : NŒUD DE LAZAR'"
module_rep J18-lecture-jouet-absente 1 "lecture jouet : une ligne" "sed '/^lecture jouet /d'"
module_rep J19-lecture-jouet-en-echec 1 "lecture jouet : une ligne" "sed 's/^lecture jouet (passage-1-sain) : code 0 ; issue L3$/lecture jouet (passage-1-sain) : code 1 ; issue illisible/'"
module_rep J21-utf8-invalide 1 "UTF-8 invalide" "python3 -I $R/octet.py"
module_rep J20-lecture-jouet-en-double 1 "lecture jouet : une ligne" "sed 's/^\\(lecture jouet .*\\)$/\\1\\n\\1/'"
# --- usages faux : code 2
"$PY" -B "$VERIF" go "$R" > "$R/sortie-U1.txt" 2>&1; verdict U01-usage-faux-go "$?" 2 "usage" "$R/sortie-U1.txt"
"$PY" -B "$VERIF" repetition "$CODE_R" "$R/journal-repetition-sain.txt" > "$R/sortie-U2.txt" 2>&1; verdict U02-usage-faux-repetition "$?" 2 "usage" "$R/sortie-U2.txt"
# aucun __pycache__ écrit dans le clone ni dans le bloc-notes
P_CACHE=$(find "$R/source/src" "$R/source/docs/procedures/P4-instrument-v1" "$H" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
rm -rf "$R/source" "$R"/racine-*
echo "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
