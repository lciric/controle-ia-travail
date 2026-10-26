"""Dérive le script de scellement v4 du pilote 4 et ses essais v4 de la v3 (`sceller_pilote4_v3.py`, aee63b20… ;
`essais_scellement_pilote4_v3.sh`, 68af2141…), par remplacements exacts au nombre attendu.

Pourquoi : le texte v3 du pilote 4 a été scellé (25 octobre 2026, 22:27 UTC) et son fichier d'empreintes
`EMPREINTES-pilote4-gemini-v1.txt` est dans le dossier des pièces ; le texte v4 (objet v6.2, décision de Lazar du
25 octobre, 23:54 Paris) se scelle dans le même dossier, et le script v3 refuserait (R12 : il n'écrase jamais) ;
la v4 écrit `EMPREINTES-pilote4-gemini-v2.txt`. Rien d'autre ne change dans le script. Les essais v4 sont ceux de la v3
pour ce nom, la clé de course `v6-2` (l'« autre course » de l'artefact `graine-autre-course` devient `v6-3`), plus un cas
sain où le fichier d'empreintes v1 existe déjà (il ne doit pas bloquer le scellement de la v4).

Usage : python3 -I deriver_scellement_pilote4_v4.py SCELLER_V3 ESSAIS_V3 SORTIE_SCELLER SORTIE_ESSAIS
Refuse si une source n'a pas l'empreinte attendue, si une occurrence n'est pas au nombre attendu, ou si une sortie
existe (R12).
"""
import hashlib, pathlib, sys

SHA_S3 = "aee63b20b45e1bd1e5c109699b2e3ba36a1ef216d7f051d54c2fcd0340033de9"
SHA_E3 = "68af2141eeef563640e5166e8c4fb72eab6bea5f6d855b9c07734accbadbc9af"
s3, e3, s4, e4 = (pathlib.Path(a) for a in sys.argv[1:5])
for p in (s4, e4):
    if p.exists():
        sys.exit(f"refus : {p} existe déjà (R12)")
for p, h in ((s3, SHA_S3), (e3, SHA_E3)):
    if hashlib.sha256(p.read_bytes()).hexdigest() != h:
        sys.exit(f"refus : {p.name} n'a pas l'empreinte attendue {h[:8]}…")


def deriver(t, remplacements):
    for ancien, nouveau, n in remplacements:
        k = t.count(ancien)
        if k != n:
            sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
        t = t.replace(ancien, nouveau)
    return t


ts = deriver(s3.read_text(encoding="utf-8"), [
    ("contre-lectures, remplit les champs du scellement et eux seuls, écrit le compagnon `.sha256` — v3.\n",
     "contre-lectures, remplit les champs du scellement et eux seuls, écrit le compagnon `.sha256` — v4.\n", 1),
    ("Usage : python -I sceller_pilote4_v3.py PREREG", "Usage : python -I sceller_pilote4_v4.py PREREG", 1),
    ("v3 (contre-lecture 2, P4C2-08) : refuse aussi",
     "v4 (texte v4 du pilote 4, objet v6.2) : écrit `EMPREINTES-pilote4-gemini-v2.txt` (le fichier v1 est celui du texte v3,\n"
     "scellé le 25 octobre 2026 et jamais lancé : il n'est jamais réécrit) ; rien d'autre ne change.\n"
     "v3 (contre-lecture 2, P4C2-08) : refuse aussi", 1),
    ("`EMPREINTES-pilote4-gemini-v1.txt` (toutes les pièces", "`EMPREINTES-pilote4-gemini-v2.txt` (toutes les pièces", 1),
    ('sortie = pieces / "EMPREINTES-pilote4-gemini-v1.txt"', 'sortie = pieces / "EMPREINTES-pilote4-gemini-v2.txt"', 1),
])
if ts.count("EMPREINTES-pilote4-gemini-v1.txt") != 0:
    sys.exit("refus : le nom du fichier d'empreintes v1 reste dans le script")

te = deriver(e3.read_text(encoding="utf-8"), [
    ("# Essais (R5) du script de scellement du pilote 4, v3 (`sceller_pilote4_v3.py`) : ceux de la v2",
     "# Essais (R5) du script de scellement du pilote 4, v4 (`sceller_pilote4_v4.py`) : ceux de la v3 (`essais_scellement_pilote4_v3.sh`)\n"
     "# pour le fichier d'empreintes `EMPREINTES-pilote4-gemini-v2.txt` et la clé de course `v6-2`, plus un cas sain où le fichier\n"
     "# d'empreintes v1 (celui du texte v3 scellé) existe déjà ; la v3 reprenait ceux de la v2", 1),
    ("# Usage : bash essais_scellement_pilote4_v3.sh SCRIPT", "# Usage : bash essais_scellement_pilote4_v4.sh SCRIPT", 1),
    ("   graine de la course v6-2 = 7\\n", "   graine de la course v6-3 = 7\\n", 1),
    ("v6-1", "v6-2", 14),
    ("EMPREINTES-pilote4-gemini-v1.txt", "EMPREINTES-pilote4-gemini-v2.txt", 2),
    ('echo "== bilan : $ok sur $n cas conformes =="\n',
     'cas sain-avec-empreintes-v1 "scellé : pilote4-gemini-organisme-v9.md" v6-2 "printf \'empreintes du texte v3\\n\' > pieces/EMPREINTES-pilote4-gemini-v1.txt; (cd pieces && sha256sum EMPREINTES-pilote4-gemini-v1.txt > EMPREINTES-pilote4-gemini-v1.txt.sha256)"\n'
     'n=$((n + 1)); if [ "$(cat "$E/sain-avec-empreintes-v1/prereg/pieces/EMPREINTES-pilote4-gemini-v1.txt")" = "empreintes du texte v3" ] && grep -q "pieces/EMPREINTES-pilote4-gemini-v1.txt" "$E/sain-avec-empreintes-v1/prereg/pieces/EMPREINTES-pilote4-gemini-v2.txt"; then ok=$((ok + 1)); echo "OK     sain-avec-empreintes-v1-intact : le fichier v1 n\'est pas réécrit et figure au fichier v2"; else echo "ÉCHEC  sain-avec-empreintes-v1-intact"; fi\n'
     'echo "== bilan : $ok sur $n cas conformes =="\n', 1),
])
if "v6-1" in te:
    sys.exit("refus : v6-1 reste dans les essais")
s4.write_text(ts, encoding="utf-8")
e4.write_text(te, encoding="utf-8")
for p in (s4, e4):
    print(f"écrit : {p.name} {hashlib.sha256(p.read_bytes()).hexdigest()}")
