interdit() { case "$1" in *lecture-sondes-t06*|donnees/bras-attaque*|donnees/mode-tenu-a-l-ecart*|docs/notes/bras-attaque/*|donnees/lecture-b-7a-quarantaine-v1*|scripts/extraire_mesures_epreuve_t06_v1.py|registres/index-bras-attaque*) return 0;; esac; return 1; }
apporter() {  # $1 = révision, $2 = chemin : fichier et compagnon recopiés s'ils existent à cette révision ; un fichier suivi à S7 hors
    # de l'extraction partielle y est d'abord ajouté (sinon git le retirerait de l'arbre au changement de branche ; vu à la répétition)
    local q; interdit "$2" && arret "chemin interdit cité : $2" 2
    for q in "$2" "$2.sha256"; do git -C "$D" cat-file -e "$1:$q" 2>/dev/null || continue
        if git -C "$D" cat-file -e "HEAD:$q" 2>/dev/null && [ ! -e "$D/$q" ]; then
            git -C "$D" sparse-checkout add "/$q" 2>/dev/null || arret "extraction partielle de $q" 2; fi
        mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "$1:$q" > "$D/$q" || arret "copie de $q" 2; done; }
for f in $REGISTRES; do
    if git -C "$D" cat-file -e "$H:$f" 2>/dev/null; then apporter "$H" "$f"; j "registre $f recopié de main"; else j "registre $f : absent de main"; fi; done
[ -f "$D/registres/scellements-v1.md" ] || arret "registres/scellements-v1.md absent de main" 2
for p in $(awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); if ($4 ~ /^[A-Za-z0-9._\/-]+$/ && $4 !~ /\.\./) print $4 }' "$D/registres/scellements-v1.md" "$D/registres/prealables-p3bis-v1.md" 2>/dev/null | sort -u); do
    case "$p" in runs/"$RUN6"/*|diag/"$RUN6"/*|donnees/"$RUN6"/*) continue;; esac
    apporter "$H" "$p"; done
for k in JD JA JC CONCEPTS; do   # C-1 : la première ouverture ferme le périmètre des jeux ; ni plus ni moins que PERIMETRE
    case "$k" in CONCEPTS) cle=SCELLEMENT-CONCEPTS-T07;; *) cle=SCELLEMENT-JEUX-T07-$k;; esac
    n=$(grep -c "^| $cle |" "$D/registres/scellements-v1.md"); case "$PER" in *",$k,"*) e=1;; *) e=0;; esac
    [ "$n" -le 1 ] || arret "$cle : $n lignes au registre (au plus une)" 2
    [ "$n" = "$e" ] || arret "périmètre (C-1) : $cle $([ "$n" = 1 ] && echo présente || echo absente) à main, $([ "$e" = 1 ] && echo exigée || echo non exigée) par PERIMETRE=$PERIM : rien n'est ouvert" 2
    [ "$n" = 1 ] || { j "$cle : absente, hors du périmètre"; continue; }
    p=$(grep "^| $cle |" "$D/registres/scellements-v1.md" | awk -F'|' '{ gsub(/ /, "", $4); print $4 }')
    [ -f "$D/$p" ] && [ -f "$D/$p.sha256" ] || arret "$cle : $p ou son compagnon absent de main" 2
    [ "$k" = CONCEPTS ] && { j "$cle : $p présent"; continue; }
    for f in $(git -C "$D" ls-tree --name-only "$H" -- "$(dirname "$p")/" | grep -E '/journal-verification[^/]*\.txt$'); do apporter "$H" "$f"; done
    j "$cle : $p présent ; journaux du script : $(ls "$D/$(dirname "$p")" | grep -c '^journal-verification.*\.txt$')"
done
[ -z "$(git -C "$D" status --porcelain -- src tests)" ] || arret "src ou tests changés par la recopie des registres" 2
j "registres nommés de main recopiés ; registre $(sha256sum < "$D/registres/scellements-v1.md" | cut -c1-16) ; périmètre $PERIM"
