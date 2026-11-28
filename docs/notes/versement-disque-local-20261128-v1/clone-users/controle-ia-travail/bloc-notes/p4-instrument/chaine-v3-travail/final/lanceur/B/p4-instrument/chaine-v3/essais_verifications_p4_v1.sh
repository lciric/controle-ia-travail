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
# Chaîne v2 : révocations sous des formes voisines (code 2, lignes affichées ; RC-depense-03), avec leurs témoins sains
# et les registres réels du dépôt de travail (copies, aucune fausse alerte) ; garde gelée d'une autre empreinte ou
# absente (code 2 ; RC-depense-04) ; accord à la forme de la dépense de la phase (somme, 150 USD, alerte à 120 USD ;
# RC-depense-05) et au GO cité à frontières de mot (RC-depense-09) ; rapports aux noms exacts (RC-fidelite-12) ;
# fenêtres glissantes, brutes et échappées, dans des fichiers, des chaînes JSON et des tableaux (RC-donnees-01) ;
# filtre de l'affichage (masquage puis fenêtres puis troncature ; RC-donnees-03, -04) ; recherche des jetons ; preuves
# à huit journaux ; journal de la répétition à cinq passages, sept récupérations conformes, vingt-sept artefacts avec
# l'état de l'instance gardée, deux refus, rien d'affiché (RC-fidelite-07, RC-depense-02).
# Chaîne v3 : formes voisines de révocation X01 à X05 de la vérification « dépense » (décision sans colonne de date,
# colonne vide en trop, identifiant de décision en gras, identifiant de GO en gras, GO de type « décision » qui révoque ;
# VC2-depense-01), avec les témoins V55 (mention libre, V10 du vérificateur) et V58 (GO de calcul qui cite la phase, V12) ;
# registres réels relus à la tête de main (git show, lecture seule) et dans l'arbre de travail s'il en diffère ; vingt-six
# rapports (RAPPORTS_NOMS) ; entrées non ordinaires (liens symboliques, tube nommé) refusées par fenetres et jetons
# (VC2-donnees-02) ; journal de la répétition : trois refus, état et heure limite dans les refus de la place et du
# clonage (VC2-depense-03), repli de l'affichage (VC2-donnees-01).
# Usage : essais_verifications_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || { echo "usage : essais_verifications_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; R=$(realpath -m "$3")
SOI=$(realpath "$0")
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v3
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
FORME="dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD"
{ cat registres/decisions.md; echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; $FORME. | essai |"; } > "$R/decisions-sain.md"
grep -q "^| $GO |" "$R/go-sain.md" || { echo "$GO absent du registre de C"; exit 2; }
NON_CONFORMES=0
racine() {   # $1 nom : racine d'un cas (liens vers le code, registres copiés)
    local r="$R/racine-$1"
    mkdir -p "$r/registres" "$r/.claude/hooks" && ln -s "$R/source/src" "$r/src" && ln -s "$R/source/docs" "$r/docs" \
        && cp "$R/source/.claude/hooks/garde_calcul.py" "$r/.claude/hooks/garde_calcul.py" \
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
# --- chaîne v2 : révocations sous des formes voisines (code 2, lignes affichées), témoins sains, registres réels
for x in GO-2026-10-04-08 GO-2026-10-20-06 GO-2026-10-20-07 R-262 R-269; do
    cas_go "V42-ligne-sans-espace-qui-revoque-$x" 2 "révocation possible sous une forme voisine" cat \
        "$(ajout_go "|GO-2026-10-21-01|$JOUR|révocation|révoque $x (essai)|—|$JOUR|Lazar|essai|")" cat
done
for ty in Révocation revocation RÉVOCATION; do
    cas_go "V43-type-$ty" 2 "révocation possible sous une forme voisine" cat \
        "$(ajout_go "| GO-2026-10-21-01 | $JOUR | $ty | révoque R-269 (essai) | — | $JOUR | Lazar | essai |")" cat
done
cas_go V43d-type-inconnu-qui-nomme-la-prolongation 2 "révocation possible sous une forme voisine" cat \
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | annulation | GO-2026-10-20-06 (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go V43e-ligne-precedee-de-blancs 2 "révocation possible sous une forme voisine" cat \
    "$(ajout_go "   | GO-2026-10-21-01 | $JOUR | révocation | révoque GO-2026-10-04-08 (essai) | — | $JOUR | Lazar | essai |")" cat
for x in R-262 R-269; do
    cas_go "V51-forme-exacte-sans-espace-$x" 2 "révocation possible sous une forme voisine" cat cat \
        "$(ajout_go "|R-998|$JOUR|**Révocation de $x** (essai).|essai|")"
done
cas_go V52-deux-identifiants-dans-une-cellule 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | $JOUR | **Révocation de R-262 et de R-269** (essai). | essai |")"
cas_go V53-point-dans-le-gras 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | $JOUR | **Révocation de R-269.** (essai) | essai |")"
cas_go V54-delegation-nommee 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | $JOUR | **Révocation de la délégation R-269** (essai). | essai |")"
cas_go V56-tiret-insecable-sans-gras 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | $JOUR | révoque R‑269 (tiret insécable, essai). | essai |")"
cas_go V57-sans-gras-ni-accent 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | $JOUR | Revocation de r-262 (essai). | essai |")"
grep -q "^    registres/decisions.md, ligne [0-9]* : | R-998 | $JOUR | Revocation de r-262" "$R/sortie-V57-sans-gras-ni-accent.txt" \
    && echo "    V57 : ligne de la forme voisine affichée : CONFORME" || { echo "    V57 : ligne de la forme voisine non affichée : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cas_go V55-forme-citee-sans-revoquer 0 "$GO conforme" cat cat "$(ajout_go "| R-998 | $JOUR | Note (essai) : la forme « **Révocation de R-269** » est décrite ici, sans révoquer. | essai |")"
cas_go V58-go-de-calcul-qui-nomme-la-phase 0 "$GO conforme" cat \
    "$(ajout_go "| GO-2026-10-21-03 | $JOUR | calcul | dans le plafond de GO-2026-10-04-08 (essai) | 1 USD | $JOUR | Lazar | essai |")" cat
cas_go V59-identifiants-voisins-sans-effet 0 "$GO conforme" cat cat "$(ajout_go "| R-998 | $JOUR | **Révocation de R-2690 et de R-2620** (essai). | essai |")"
cas_go V59b-revocation-d-un-go-voisin-de-type-inconnu 0 "$GO conforme" cat \
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | annulation | GO-2026-10-20-071 (essai) | — | $JOUR | Lazar | essai |")" cat
# chaîne v3 (VC2-depense-01) : formes voisines hors de la liste de la chaîne v2 (artefacts X01 à X05 de la vérification
# « dépense ») : code 2, lignes affichées ; témoins sains : V55 (mention libre) et V58 (GO de calcul qui cite la phase)
cas_go X01-decision-sans-colonne-de-date 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | **Révocation de R-269** : délégation retirée (essai) |")"
cas_go X02-decision-colonne-vide-en-trop 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| R-998 | $JOUR | | **Révocation de R-269** (essai) | essai |")"
cas_go X03-identifiant-de-decision-en-gras 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| **R-998** | $JOUR | **Révocation de R-269** (essai) | essai |")"
cas_go X04-identifiant-de-go-en-gras 2 "révocation possible sous une forme voisine" cat \
    "$(ajout_go "| **GO-2026-10-21-01** | $JOUR | révocation | GO-2026-10-20-07 (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go X05-go-de-type-decision-qui-revoque 2 "révocation possible sous une forme voisine" cat \
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | décision | Révocation de GO-2026-10-20-07 (délégation retirée, essai) | — | $JOUR | Lazar | essai |")" cat
grep -q "^    registres/go.md, ligne [0-9]* : | GO-2026-10-21-01 | $JOUR | décision | Révocation de GO-2026-10-20-07" "$R/sortie-X05-go-de-type-decision-qui-revoque.txt" \
    && echo "    X05 : ligne de la forme voisine affichée : CONFORME" || { echo "    X05 : ligne de la forme voisine non affichée : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cas_go X06-type-en-gras 2 "révocation possible sous une forme voisine" cat \
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | **révocation** | GO-2026-10-20-06 (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go X07-identifiant-de-decision-entre-guillemets-inverses 2 "révocation possible sous une forme voisine" cat cat "$(ajout_go "| \`R-998\` | $JOUR | « Annulation de GO-2026-10-04-08 » (essai) | essai |")"
cas_go X08-go-de-calcul-qui-mentionne-un-retrait-sans-identifiant 0 "$GO conforme" cat \
    "$(ajout_go "| GO-2026-10-21-03 | $JOUR | calcul | Retrait de l’instance 56799469 du registre (essai, apostrophe typographique : la commande du banc est entre guillemets simples) | 1 USD | $JOUR | Lazar | essai |")" cat
# registres réels du dépôt de travail, à la tête de main (git show, lecture seule ; chaîne v3 : relus après la correction
# de VC2-depense-01) : aucune fausse alerte, accord fabriqué ajouté ; puis l'arbre de travail, s'il en diffère
DT=/home/user/controle-ia-travail
GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks show main:registres/go.md > "$R/go-reel.md" \
    && GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks show main:registres/decisions.md > "$R/decisions-reel.md" || exit 2
echo "registres réels lus à la tête de main ($(GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks rev-parse main)) : go.md $(sha256sum "$R/go-reel.md" | cut -d' ' -f1) ; decisions.md $(sha256sum "$R/decisions-reel.md" | cut -d' ' -f1)"
r=$(racine R00); cp "$R/go-reel.md" "$r/registres/go.md"
{ cat "$R/decisions-reel.md"; echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; $FORME. | essai |"; } > "$r/registres/decisions.md"
"$PY" -B "$VERIF" go "$r" "$R/texte-sain.md" "$JOUR" 5.41 > "$R/sortie-R00.txt" 2>&1; verdict R00-registres-reels-go-sans-fausse-alerte "$?" 0 "$GO conforme" "$R/sortie-R00.txt"
"$PY" -B "$VERIF" accord "$r" "$R/texte-sain.md" R-999 "$JOUR" > "$R/sortie-R00b.txt" 2>&1; verdict R00b-registres-reels-accord "$?" 0 "(cite $GO) ; $FORME : conforme" "$R/sortie-R00b.txt"
if cmp -s "$DT/registres/go.md" "$R/go-reel.md" && cmp -s "$DT/registres/decisions.md" "$R/decisions-reel.md"; then
    echo "    R00c : registres de l'arbre de travail égaux à ceux de la tête de main : CONFORME"
else
    r=$(racine R00c); cp "$DT/registres/go.md" "$r/registres/go.md"
    { cat "$DT/registres/decisions.md"; echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; $FORME. | essai |"; } > "$r/registres/decisions.md"
    "$PY" -B "$VERIF" go "$r" "$R/texte-sain.md" "$JOUR" 5.41 > "$R/sortie-R00c.txt" 2>&1; verdict R00c-registres-de-l-arbre-de-travail-sans-fausse-alerte "$?" 0 "$GO conforme" "$R/sortie-R00c.txt"
fi
# garde de calcul gelée d'une autre empreinte, ou absente : code 2, aucun rejeu (RC-depense-04)
r=$(racine G15); echo "# modifiée (essai)" >> "$r/.claude/hooks/garde_calcul.py"
"$PY" -B "$VERIF" go "$r" "$R/texte-sain.md" "$JOUR" 5.41 > "$R/sortie-G15.txt" 2>&1; verdict G15-garde-gelee-modifiee "$?" 2 "garde de calcul gelée modifiée" "$R/sortie-G15.txt"
r=$(racine G15b); rm -f "$r/.claude/hooks/garde_calcul.py"
"$PY" -B "$VERIF" go "$r" "$R/texte-sain.md" "$JOUR" 5.41 > "$R/sortie-G15b.txt" 2>&1; verdict G15b-garde-gelee-absente "$?" 2 "garde de calcul gelée absente" "$R/sortie-G15b.txt"
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
cas_accord A00-accord-qui-cite-la-delegation 0 "(cite $GO) ; $FORME : conforme" R-999 cat
grep -q "ALERTE" "$R/sortie-A00-accord-qui-cite-la-delegation.txt" && { echo "    A00 : alerte écrite sous 120 USD : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    A00 : aucune alerte sous 120 USD : CONFORME"
cas_accord A00b-accord-qui-cite-un-message-du-jour 0 "(cite un message de Lazar du jour) ; $FORME : conforme" R-999 \
    "sed 's/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : message de Lazar dans la session ce jour-là ; $FORME. | essai |/'"
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
# chaîne v2 : forme de la dépense de la phase (RC-depense-05) ; GO cité à frontières de mot (RC-depense-09)
accord_avec() { printf "sed 's/^| R-999 | %s | .*/| R-999 | %s | **Accord de Lazar pour le lancement de P4-instrument** (essai) : %s | essai |/'" "$JOUR" "$JOUR" "$1"; }
cas_accord A08-forme-de-la-depense-absente 1 "forme « dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD » absente" R-999 "$(accord_avec "délégation $GO en cours ; dépense de la phase sous 150 USD.")"
cas_accord A08b-virgule-remplacee-par-un-point 1 "absente, mal formée ou en double" R-999 "$(accord_avec "délégation $GO ; dépense consignée 47.83 USD + borne 5,41 USD = 53.24 USD < 150 USD.")"
cas_accord A08c-forme-en-double 1 "absente, mal formée ou en double" R-999 "$(accord_avec "délégation $GO ; $FORME ; $FORME.")"
cas_accord A08d-somme-fausse 1 "somme fausse" R-999 "$(accord_avec "délégation $GO ; dépense consignée 47,83 USD + borne 5,41 USD = 53,25 USD < 150 USD.")"
cas_accord A08e-phase-a-150-usd 1 "150 USD ou plus" R-999 "$(accord_avec "délégation $GO ; dépense consignée 144,59 USD + borne 5,41 USD = 150,00 USD < 150 USD.")"
cas_accord A08f-juste-sous-150-usd-avec-alerte 0 "ALERTE : 120 USD atteints ou dépassés (GO-2026-10-04-08) : conforme" R-999 "$(accord_avec "délégation $GO ; dépense consignée 144,58 USD + borne 5,41 USD = 149,99 USD < 150 USD.")"
cas_accord A08g-borne-autre 1 "absente, mal formée ou en double" R-999 "$(accord_avec "délégation $GO ; dépense consignée 47,83 USD + borne 5,40 USD = 53,23 USD < 150 USD.")"
cas_accord A09-go-voisin-seul 1 "qu'au sein d'un identifiant voisin" R-999 "$(accord_avec "délégation GO-2026-10-20-071 ; $FORME.")"
cas_accord A09b-go-voisin-et-message-du-jour 0 "(cite un message de Lazar du jour)" R-999 "$(accord_avec "délégation GO-2026-10-20-071 ; message de Lazar dans la session ce jour-là ; $FORME.")"
# --- chaîne v2 : rapports attendus, noms exacts (RC-fidelite-12)
NOMS_R=$("$PY" -I -B -c 'import importlib.util, sys
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
print(" ".join(v.RAPPORTS_NOMS))' "$VERIF")
PAIRES_R=$(for n in $NOMS_R; do printf '%s=%s ' "$n" "$(printf 'a%.0s' {1..64})"; done)
cas_rapports() {   # $1 nom, $2 code attendu, $3 motif, puis les paires
    local n=$1 a=$2 m=$3 c; shift 3
    "$PY" -B "$VERIF" rapports "$@" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$a" "$m" "$R/sortie-$n.txt"
}
# shellcheck disable=SC2086
cas_rapports K00-noms-exacts 0 "rapport attendu : verification-module-v3-P4-instrument-v1.md" $PAIRES_R
[ "$(grep -c '^rapport attendu : ' "$R/sortie-K00-noms-exacts.txt")" = 26 ] && echo "    K00 : vingt-six rapports attendus (RAPPORTS_NOMS de la chaîne v3) : CONFORME" \
    || { echo "    K00 : nombre de rapports attendus : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# shellcheck disable=SC2086
cas_rapports K01-un-rapport-manquant 2 "manquants ['P4-instrument-v1-brouillon3.md']" $(printf '%s\n' $PAIRES_R | grep -v brouillon3)
# shellcheck disable=SC2086
cas_rapports K02-un-rapport-en-trop 2 "en trop ['P4-autre-v1.md']" $PAIRES_R "P4-autre-v1.md=$(printf 'b%.0s' {1..64})"
# shellcheck disable=SC2086
cas_rapports K03-un-rapport-en-double 2 "en double ['P4-instrument-v1-candidat1.md']" $PAIRES_R "P4-instrument-v1-candidat1.md=$(printf 'c%.0s' {1..64})"
# shellcheck disable=SC2086
cas_rapports K04-empreinte-courte 2 "mal formés" $(printf '%s\n' $PAIRES_R | sed '1s/=a*/=abc/')
cas_rapports K05-deux-rapports-de-la-forme-v1 2 "noms exacts" "P4-essai-contre-lecture-a-v1.md=$(printf 'a%.0s' {1..64})" "P4-essai-contre-lecture-b-v1.md=$(printf 'a%.0s' {1..64})"
# --- chaîne v2 : fenêtres glissantes (RC-donnees-01), dans des fichiers, des chaînes JSON et des tableaux
"$PY" -B "$H/outils_essais_p4_v1.py" fenetres "$R/textes/textes-fenetres.jsonl" > /dev/null 2>"$R/textes.err" || { echo "textes des fenêtres impossibles : $(tail -1 "$R/textes.err")"; exit 2; }
TX=$R/textes/textes-fenetres.jsonl
fabriquer() {   # $1 dossier neuf, $2 programme Python (texte k : textes honnêtes non dégénérés, k-ième), écrit dans le dossier
    mkdir -p "$1" && "$PY" -I -B - "$TX" "$1" "$2" <<'PYF' || { echo "fabrication impossible : $1"; exit 2; }
import json, sys
from pathlib import Path
import numpy as np
tx, d, prog = sys.argv[1:4]
T = [json.loads(l)["texte"] for l in open(tx, encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
D = Path(d)
(D / "journal.txt").write_text("2026-10-20T00:00:00Z début : essai sain\nPROGRES 2026-10-20T00:00:01Z etape=M5 conforme=True\n", encoding="utf-8")
(D / "resultat.json").write_text(json.dumps({"issue": "L3", "note": "essai sain"}), encoding="utf-8")
with open(D / "tableau.npz", "wb") as f:
    np.savez(f, noms=np.array(["sonde-a", "sonde-b"]), x=np.zeros(2))
exec(prog)
PYF
}
cas_fenetres() {   # $1 nom, $2 code attendu, $3 motif, puis les arguments de fenetres
    local n=$1 a=$2 m=$3 c; shift 3
    "$PY" -B "$VERIF" fenetres "$@" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$a" "$m" "$R/sortie-$n.txt"
}
fabriquer "$R/f/sain" "pass"
cas_fenetres F00-dossier-sain 0 "AUCUNE FENÊTRE D'UN TEXTE HONNÊTE" "$TX" "$R/f/sain"
fabriquer "$R/f/brut" "(D / 'run.err').write_text('erreur : ' + T[0] + '\n', encoding='utf-8')"
cas_fenetres F01-texte-brut 1 "FENÊTRES RETROUVÉES OU FICHIERS ILLISIBLES OU NON ORDINAIRES : 1" "$TX" "$R/f/brut"
fabriquer "$R/f/json" "(D / 'run.err').write_text('Traceback : ' + json.dumps(T[3], ensure_ascii=False) + '\n', encoding='utf-8')"
cas_fenetres F02-echappe-en-json 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/json"
fabriquer "$R/f/unicode" "(D / 'run.err').write_text(json.dumps(T[4]) + '\n', encoding='utf-8')"
cas_fenetres F03-echappe-en-uxxxx 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/unicode"
fabriquer "$R/f/repr" "(D / 'tests.err').write_text('valeur : ' + repr(T[1]) + '\n', encoding='utf-8')"
cas_fenetres F04-echappe-par-python 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/repr"
fabriquer "$R/f/milieu" "m = (len(T[0]) - 48) // 2; (D / 'run.err').write_text(T[0][:m] + '\n[...]\n' + T[0][m + 48:] + '\n', encoding='utf-8')"
cas_fenetres F05-texte-sans-sa-fenetre-du-milieu 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/milieu"
fabriquer "$R/f/npz" "np.savez(open(D / 'tableau.npz', 'wb'), noms=np.array(['sonde-a', T[2]]), x=np.zeros(2))"
cas_fenetres F06-chaine-d-un-tableau 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/npz"
fabriquer "$R/f/u0020" "Q = chr(34); B = chr(92); (D / 'resultat.json').write_text('{' + Q + 'note' + Q + ': ' + Q + ''.join(B + 'u0020' if ch == ' ' else (B + 'n' if ch == '\n' else ch) for ch in T[0]) + Q + '}', encoding='utf-8')"
cas_fenetres F07-chaine-json-aux-espaces-echappees 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/u0020"
fabriquer "$R/f/illisible" "(D / 'tableau.npz').write_bytes(b'pas un tableau')"
cas_fenetres F08-tableau-illisible 1 "FENÊTRES RETROUVÉES OU FICHIERS ILLISIBLES OU NON ORDINAIRES : 1" "$TX" "$R/f/illisible"
fabriquer "$R/f/degenere" "(D / 'tests.txt').write_text('.' * 200 + '\n' + '=' * 120 + '\n', encoding='utf-8')"
cas_fenetres F09-caractere-repete-seul 0 "AUCUNE FENÊTRE" "$TX" "$R/f/degenere"
fabriquer "$R/f/court" "(D / 'run.err').write_text(T[0][:40] + '\n', encoding='utf-8')"
cas_fenetres F10-fragment-de-40-caracteres 0 "AUCUNE FENÊTRE" "$TX" "$R/f/court"
fabriquer "$R/f/sous-dossier" "(D / 'a' / 'b').mkdir(parents=True); (D / 'a' / 'b' / 'trace.txt').write_text(T[1], encoding='utf-8')"
cas_fenetres F11-dans-un-sous-dossier 1 "FENÊTRES RETROUVÉES" "$TX" "$R/f/sous-dossier"
cas_fenetres F12-textes-absents 2 "textes honnêtes illisibles" "$R/textes/absent.jsonl" "$R/f/sain"
printf '{"condition": "saboteur", "texte": "ACTION: ADD autre condition, jamais lue pour les fenêtres de P4, essai long"}\n' > "$R/textes/sans-honnete.jsonl"
cas_fenetres F13-aucun-texte-honnete 2 "aucun texte honnête" "$R/textes/sans-honnete.jsonl" "$R/f/sain"
cas_fenetres F14-chemin-absent 2 "absent : recherche impossible" "$TX" "$R/f/absent"
# chaîne v3 (VC2-donnees-02) : entrées non ordinaires (lien symbolique vers un fichier qui porte un texte, vers un dossier,
# lien donné en argument, tube nommé) : jamais suivies ni lues, comptées et refusées (code 1, chemin écrit)
mkdir -p "$R/f-hors" && "$PY" -I -B -c 'import json, sys
T = [json.loads(l)["texte"] for l in open(sys.argv[1], encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
open(sys.argv[2], "w", encoding="utf-8").write("hors du dossier : " + T[0] + "\n")' "$TX" "$R/f-hors/texte.txt" || exit 2
fabriquer "$R/f/lien" "(D / 'lien.txt').symlink_to('$R/f-hors/texte.txt')"
cas_fenetres F15-lien-vers-un-texte-hors-du-dossier 1 "FENÊTRES RETROUVÉES OU FICHIERS ILLISIBLES OU NON ORDINAIRES : 1" "$TX" "$R/f/lien"
grep -qF "non ordinaire (lien symbolique ou autre, ni suivi ni lu) : $R/f/lien/lien.txt" "$R/sortie-F15-lien-vers-un-texte-hors-du-dossier.txt" \
    && ! grep -q "fenêtre(s) retrouvée(s)" "$R/sortie-F15-lien-vers-un-texte-hors-du-dossier.txt" && grep -q "fichiers parcourus : 3 ; entrées non ordinaires : 1" "$R/sortie-F15-lien-vers-un-texte-hors-du-dossier.txt" \
    && echo "    F15 : lien écrit par son chemin, ni suivi ni lu, compté : CONFORME" || { echo "    F15 : relevé du lien : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
fabriquer "$R/f/lien-dossier" "(D / 'lien-dossier').symlink_to('$R/f-hors', target_is_directory=True)"
cas_fenetres F16-lien-vers-un-dossier 1 "NON ORDINAIRES : 1" "$TX" "$R/f/lien-dossier"
cas_fenetres F17-lien-donne-en-argument 1 "NON ORDINAIRES : 1" "$TX" "$R/f/lien/lien.txt"
fabriquer "$R/f/tube" "import os; os.mkfifo(D / 'tube')"
cas_fenetres F18-tube-nomme 1 "NON ORDINAIRES : 1" "$TX" "$R/f/tube"
# aucune sortie de la recherche ne recopie un texte (fragments de 30 caractères des textes cherchés)
"$PY" -I -B - "$TX" "$R" <<'PYA' && echo "    sorties de la recherche des fenêtres : aucun fragment de texte : CONFORME" || { echo "    sorties de la recherche : fragment de texte : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import json, sys
from pathlib import Path
T = [json.loads(l)["texte"] for l in open(sys.argv[1], encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
s = "".join(p.read_text(encoding="utf-8", errors="replace") for p in Path(sys.argv[2]).glob("sortie-F*.txt"))
sys.exit(1 if any(t[i:i + 30] in s for t in T for i in range(0, len(t) - 30, 10)) else 0)
PYA
# --- chaîne v2 : filtre de l'affichage (RC-donnees-03, -04) : jetons masqués, puis fenêtres, puis troncature
JT=factice-hf-filtre-0001; JG=factice-gh-filtre-0001
montrer_cas() {   # $1 nom, $2 code attendu, $3 motif attendu (dernière ligne), $4 fichier d'entrée, puis variables
    local n=$1 a=$2 m=$3 e=$4 c; shift 4
    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 "$@" "$PY" -B "$VERIF" montrer "$TX" 300 < "$e" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$a" "$m" "$R/sortie-$n.txt"
}
"$PY" -I -B - "$TX" "$R" "$JT" <<'PYW' || { echo "entrées du filtre impossibles"; exit 2; }
import json, sys
from pathlib import Path
T = [json.loads(l)["texte"] for l in open(sys.argv[1], encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
R, jt = Path(sys.argv[2]), sys.argv[3]
(R / "w0.txt").write_text("OK  2a verifier-arbre : arbre intact\n", encoding="utf-8")
(R / "w1.txt").write_text("--  4a arrêt : " + json.dumps({"etape": "bras", "motif": "essai : " + T[0]}, ensure_ascii=False) + "\n", encoding="utf-8")
(R / "w2.txt").write_text("OK  6a dernière : fuite " + jt + "\n", encoding="utf-8")
(R / "w3.txt").write_text("x" * 290 + " " + jt + " fin\n", encoding="utf-8")
(R / "w4.txt").write_text("y" * 500 + "\n", encoding="utf-8")
PYW
montrer_cas W00-ligne-saine-inchangee 0 "OK  2a verifier-arbre : arbre intact" "$R/w0.txt" HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG
montrer_cas W01-motif-qui-recopie-un-texte 0 "--  4a (ligne retirée : " "$R/w1.txt" HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG
montrer_cas W02-jeton-masque 0 "OK  6a dernière : fuite ***" "$R/w2.txt" HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG
montrer_cas W03-jeton-a-cheval-sur-la-borne 0 "***" "$R/w3.txt" HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG
montrer_cas W04-ligne-tronquee 0 " […]" "$R/w4.txt" HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG
python3 -c 'import sys; l = open(sys.argv[1], encoding="utf-8").read().rstrip("\n").split("\n")[-1]; sys.exit(0 if l == "y" * 300 + " […]" else 1)' "$R/sortie-W04-ligne-tronquee.txt" && echo "    W04 : ligne tronquée à 300 caractères exactement, marque « […] » : CONFORME" || { echo "    W04 : ligne non tronquée : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
montrer_cas W05-jetons-absents-annonces 0 "OK  2a verifier-arbre : arbre intact" "$R/w0.txt"
head -1 "$R/sortie-W05-jetons-absents-annonces.txt" | grep -q "^--  masquage partiel : HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN" && echo "    W05 : masquage partiel annoncé : CONFORME" || { echo "    W05 : masquage partiel non annoncé : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -B "$VERIF" montrer "$R/textes/absent.jsonl" < "$R/w0.txt" > "$R/sortie-W06.txt" 2>&1; verdict W06-textes-absents "$?" 2 "textes honnêtes illisibles" "$R/sortie-W06.txt"
grep -qF -e "$JT" -e "factice-hf-filtre" -e "Synthetic probe zanzibar" "$R"/sortie-W0*.txt && { echo "    filtre : jeton ou texte affiché : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    filtre : aucun jeton ni texte affiché : CONFORME"
# --- chaîne v2 : recherche des jetons
mkdir -p "$R/j/sain" "$R/j/fuite"; echo "rien" > "$R/j/sain/a.txt"; echo "fuite $JG" > "$R/j/fuite/a.txt"
env -i PATH=/usr/bin:/bin HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG "$PY" -B "$VERIF" jetons "$R/j/sain" > "$R/sortie-T00.txt" 2>&1; verdict T00-jetons-sain "$?" 0 "AUCUN JETON" "$R/sortie-T00.txt"
env -i PATH=/usr/bin:/bin HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG "$PY" -B "$VERIF" jetons "$R/j/fuite" > "$R/sortie-T01.txt" 2>&1; verdict T01-jeton-dans-un-fichier "$?" 1 "JETONS RETROUVÉS" "$R/sortie-T01.txt"
env -i PATH=/usr/bin:/bin "$PY" -B "$VERIF" jetons "$R/j/sain" > "$R/sortie-T02.txt" 2>&1; verdict T02-jetons-absents-de-l-environnement "$?" 2 "recherche impossible" "$R/sortie-T02.txt"
# chaîne v3 (VC2-donnees-02) : lien symbolique vers un fichier qui porte un jeton : ni suivi ni lu, refusé (code 1)
mkdir -p "$R/j/lien" "$R/j-hors" && echo "fuite $JG" > "$R/j-hors/a.txt" && ln -s "$R/j-hors/a.txt" "$R/j/lien/a.txt"
env -i PATH=/usr/bin:/bin HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG "$PY" -B "$VERIF" jetons "$R/j/lien" > "$R/sortie-T03.txt" 2>&1; verdict T03-lien-symbolique-vers-un-jeton "$?" 1 "JETONS RETROUVÉS OU FICHIERS ILLISIBLES OU NON ORDINAIRES" "$R/sortie-T03.txt"
grep -qF "non ordinaire (lien symbolique ou autre, ni suivi ni lu) : $R/j/lien/a.txt" "$R/sortie-T03.txt" && ! grep -q "jeton retrouvé" "$R/sortie-T03.txt" \
    && echo "    T03 : lien écrit par son chemin, ni suivi ni lu : CONFORME" || { echo "    T03 : relevé du lien : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
grep -qF "$JG" "$R"/sortie-T0*.txt && { echo "    jetons affichés : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    recherche des jetons : aucun jeton affiché : CONFORME"
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
ecrire_preuves() {   # $1 dossier : les huit journaux sains, empreintes factices cohérentes
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
[ "$(grep -c . "$R/sortie-P00-preuves-saines.txt")" = 17 ] && echo "    dix-sept scripts éprouvés : CONFORME" || { echo "    nombre de scripts éprouvés : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
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
"$PY" -B "$H/outils_essais_p4_v1.py" journal-repetition "$VERIF" "$CODE_R" "$NOM_C" "$SHA_C" > "$R/journal-repetition-sain.txt" || exit 2
module_rep() {   # $1 nom, $2 code attendu, $3 motif, $4 commande sur le journal
    local n=$1 c j="$R/journal-$1.txt"
    eval "$4" < "$R/journal-repetition-sain.txt" > "$j"
    "$PY" -B "$VERIF" repetition "$CODE_R" "$j" "$NOM_C" "$SHA_C" > "$R/sortie-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$2" "$3" "$R/sortie-$n.txt"
}
module_rep J00-journal-sain 0 "verifications_p4_v1.py $(printf 'e%.0s' {1..64})" cat
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
module_rep J12-script-manquant 1 "les quatre attendus exactement" "sed '0,/^script répété : /{/^script répété : /d}'"
module_rep J13-fin-absente 1 "ligne absente ou en double : FIN DE LA RÉPÉTITION" "sed '/^FIN DE LA RÉPÉTITION$/d'"
module_rep J14-destruction-absente-d-un-cas-sain 1 "ligne absente ou en double : récupération (textes-degeneres)" "sed 's/^\\(récupération (textes-degeneres) : .*\\) ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)$/\\1/'"
module_rep J15-artefact-instance-detruite 1 "ligne absente ou en double : récupération (artefact-etiquette-autre)" "sed 's/^\\(récupération (artefact-etiquette-autre) : code 1 ; .*\\) ; INSTANCE 99999999 NON DÉTRUITE : NŒUD DE LAZAR$/\\1 ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)/'"
module_rep J16-tous-conformes-de-trop 1 "récupérations conformes, chacune suivie de la destruction" "sed '\$a récupération (autre) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)'"
module_rep J17-echec-sans-destruction-de-trop 1 "récupérations en échec, chacune sans destruction" "sed '\$a récupération (autre) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC ; INSTANCE 99999999 NON DÉTRUITE : NŒUD DE LAZAR'"
module_rep J18-lecture-jouet-absente 1 "lecture jouet : une ligne" "sed '/^lecture jouet (run-non-decisif) /d'"
module_rep J19-lecture-jouet-en-echec 1 "lecture jouet : une ligne" "sed 's/^lecture jouet (run-non-decisif) : code 0 ; issue L3$/lecture jouet (run-non-decisif) : code 1 ; issue illisible/'"
module_rep J21-utf8-invalide 1 "UTF-8 invalide" "python3 -I $R/octet.py"
module_rep J20-lecture-jouet-en-double 1 "lecture jouet : une ligne" "sed 's/^\\(lecture jouet (run-non-decisif) .*\\)$/\\1\\n\\1/'"
module_rep J20b-refus-de-la-lecture-du-run-decisif-absent 1 "ligne absente ou en double : lecture jouet sans --prereg du run décisif" "sed '/^lecture jouet sans --prereg /d'"
# chaîne v2 : état de l'instance gardée ; passage 5 et sa récupération ; refus ; rien d'affiché ; quatre scripts répétés
module_rep J22-etat-de-l-instance-gardee-absent 1 "état de l'instance gardée et heure limite de destruction absents" "awk '/^    --  8 instance 99999999 gardée/&&!v{v=1; next} {print}'"
module_rep J23-passage-5-sans-arret-du-module 1 "« ARRÊT pendant run » absent de son journal" "sed '/ARRÊT pendant run /d'"
module_rep J24-recuperation-5-sans-motif-d-arret 1 "« --  4a arrêt : » absent de son bloc" "sed '/^    --  4a arrêt : /d'"
module_rep J25-refus-de-la-place-disque-absent 1 "ligne absente ou en double : récupération (artefact-place-disque)" "sed '/^récupération (artefact-place-disque) : /d'"
module_rep J26-fenetre-affichee 1 "ligne absente ou en double : aucune fenêtre affichée par les récupérations" "sed '/^aucune fenêtre affichée par les récupérations$/d'"
module_rep J27-passage-5-absent 1 "passage : passage 5-arret-du-module : code 1" "sed '/^passage 5-arret-du-module : /d'"
module_rep J28-module-commun-non-repete 1 "les quatre attendus exactement" "sed '/^script répété : verifications_p4_v1.py /d'"
# chaîne v3 : refus du clonage (VC2-depense-03), état et heure limite dans les refus ; repli de l'affichage (VC2-donnees-01)
module_rep J29-refus-du-clonage-absent 1 "ligne absente ou en double : récupération (artefact-clonage-impossible)" "sed '/^récupération (artefact-clonage-impossible) : /d'"
module_rep J30-etat-absent-du-refus-de-la-place 1 "état de l'instance gardée et heure limite de destruction absents du refus" "awk '/^récupération \\(artefact-place-disque\\)/{print; getline; next} {print}'"
module_rep J31-etat-absent-du-refus-du-clonage 1 "état de l'instance gardée et heure limite de destruction absents du refus" "awk '/^récupération \\(artefact-clonage-impossible\\)/{print; getline; next} {print}'"
module_rep J32-repli-de-l-affichage-absent 1 "ligne absente ou en double : récupération en repli de l'affichage" "sed '/^récupération en repli de l.affichage /d'"
module_rep J33-refus-de-trop 1 "récupérations refusées en code 2 attendues" "sed '\$a récupération (autre) : code 2 ; essai'"
# --- usages faux : code 2
"$PY" -B "$VERIF" go "$R" > "$R/sortie-U1.txt" 2>&1; verdict U01-usage-faux-go "$?" 2 "usage" "$R/sortie-U1.txt"
"$PY" -B "$VERIF" repetition "$CODE_R" "$R/journal-repetition-sain.txt" > "$R/sortie-U2.txt" 2>&1; verdict U02-usage-faux-repetition "$?" 2 "usage" "$R/sortie-U2.txt"
"$PY" -B "$VERIF" rapports > "$R/sortie-U3.txt" 2>&1; verdict U03-usage-faux-rapports "$?" 2 "usage" "$R/sortie-U3.txt"
"$PY" -B "$VERIF" montrer "$TX" trois < "$R/w0.txt" > "$R/sortie-U4.txt" 2>&1; verdict U04-usage-faux-montrer "$?" 2 "LONGUEUR : entier attendu" "$R/sortie-U4.txt"
"$PY" -B "$VERIF" fenetres "$TX" > "$R/sortie-U5.txt" 2>&1; verdict U05-usage-faux-fenetres "$?" 2 "usage" "$R/sortie-U5.txt"
# aucun __pycache__ écrit dans le clone ni dans le bloc-notes
P_CACHE=$(find "$R/source/src" "$R/source/docs/procedures/P4-instrument-v1" "$H" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
rm -rf "$R/source" "$R"/racine-*
echo "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
