REGISTRES="registres/scellements-v1.md registres/scellements-v1.md.ouvertures.md registres/ouvertures-p3bis-v1.md registres/prealables-p3bis-v1.md registres/go.md"
MOTIFS='/*
!/*/
/.claude/
/src/
/tests/
/scripts/
!/scripts/extraire_mesures_epreuve_t06_v1.py
/brouillons/T0.7-*
/docs/*
!/docs/*/
/docs/decisions/
/docs/notes/g0-deux-semaines-v1/
/docs/sources/invites-2606.08892-v1/
/prereg/*
!/prereg/contre-lectures/
!/diag/*/lecture-sondes-t06.json*'
NOMMES=$(for f in $REGISTRES; do printf '/%s\n/%s.sha256\n' "$f" "$f"; done)
CITES=$(git -C "$D" show "$S7:$CONFIG" | python3 -I -c 'import json, sys
def f(x):
    if isinstance(x, dict):
        if isinstance(x.get("chemin"), str):
            yield x["chemin"]
        for v in x.values():
            yield from f(v)
    elif isinstance(x, list):
        for v in x:
            yield from f(v)
for p in sorted(set(f(json.load(sys.stdin)))):
    print("/" + p); print("/" + p + ".sha256")') || arret "configuration illisible dans S7" 2
git -C "$D" sparse-checkout init --no-cone && printf '%s\n%s\n%s\n' "$MOTIFS" "$NOMMES" "$CITES" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$S7" || arret "commit S7 introuvable" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$S7" ] || arret "tête ≠ S7" 2
git -C "$D" merge-base --is-ancestor "$C7" "$S7" || arret "C7 n'est pas ancêtre de S7" 2
git -C "$D" diff --quiet "$C7" "$S7" -- src tests || arret "arbre gelé changé entre C7 et S7" 2
H=$(git -C "$D" rev-parse origin/prep/t07-cache-motifs-v1); git -C "$D" merge-base --is-ancestor "$S7" "$H" || arret "S7 n'est pas ancêtre de main" 2
git -C "$D" cat-file -e "$S6^{commit}" 2>/dev/null && { git -C "$D" diff --quiet "$S6" "$S7" -- requirements-cpu.txt requirements-gpu.txt || j "exigences de paquets changées depuis la course 7b : installées telles que S7 les fixe (écrit)"; }
j "code conforme : S7 $S7, C7 $C7, main $H"
