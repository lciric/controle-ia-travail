"""Dérivation de la répétition v3 de la phase B du compte 3 à partir de celle du brouillon v2 — v1.

Écrit le 2026-11-16 par le préparateur de la version 3 (modèle A ; aucun identifiant de modèle écrit). Le script v2
(`repetition-phase-b-v2/repetition_phase_b_jouet_v2.sh`, empreinte ci-dessous) n'est pas touché (R12) : ce programme écrit un fichier
neuf, et refuse s'il existe. Chaque couple doit trouver son ancien texte le nombre de fois dit ; sinon rien n'est écrit.

    python3 -I -B deriver_repetition_phase_b_v3_v1.py <répétition v2> <répétition v3, fichier neuf>
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

H_V2 = "cfaad459416c4e114cc0c14f589d34fb8e9da15eb883adf633e7c0d7d2b4083e"

BLOC_M_V4 = '''python3 -I - "$CMD_C4" "$T/blocs" c <<'FIN' > /dev/null
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"); b = re.findall(r"```bash\\n(.*?)```", t, re.S)
pathlib.Path(sys.argv[2], "bloc-m-phase-c-v4-brouillon1.sh").write_text(b[-1], encoding="utf-8")
FIN
'''

COUPLES: list[tuple[str, str, int]] = [
    ("# Répétition de bout en bout, sur dépôts jouets, de tous les blocs de commande-compte-3-phase-b-v2.md (règle R5 : chaque bloc sur un cas",
     "# Répétition de bout en bout, sur dépôts jouets, de tous les blocs de commande-compte-3-phase-b-v3.md (règle R5 : chaque bloc sur un cas",
     1),
    ("# Écrite le 2026-11-16 par le préparateur de la commande (sous-agent de la session mère, même modèle qu'elle). Aucune donnée réelle :",
     "# Écrite le 2026-11-16 par le préparateur du brouillon v2 (modèle B) ; version 3 par le préparateur de la v3 (modèle A), dérivée par\n"
     "# deriver_repetition_phase_b_v3_v1.py : noms v3, et contrôles ajoutés (bloc M de la phase C v3 égal à celui du brouillon 1 de sa v4,\n"
     "# forme du bloc C2 des deux versions ; somme des tailles du bloc B3 ; nom « bbis » parmi les entrées ; pip sans cache au bloc B2 ;\n"
     "# nom, titre et premier fait du journal provisoire v3). Aucune donnée réelle :",
     1),
    ("fabrique_depots_jouets_phase_b_v2.py", "fabrique_depots_jouets_phase_b_v3.py", 2),
    ("#     bash repetition_phase_b_jouet_v2.sh", "#     bash repetition_phase_b_jouet_v3.sh", 1),
    ("commande-compte-3-phase-b-v2.md", "commande-compte-3-phase-b-v3.md", 4),
    ('CMD_C="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-v3.md"',
     'CMD_C="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-v3.md"; CMD_C4="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-v4-brouillon1.md"',
     1),
    ('pathlib.Path(sys.argv[2], "bloc-m-phase-c-v3.sh").write_text(b[-1], encoding="utf-8")\nFIN\n',
     'pathlib.Path(sys.argv[2], "bloc-m-phase-c-v3.sh").write_text(b[-1], encoding="utf-8")\nFIN\n' + BLOC_M_V4,
     1),
    ('''grep -q 'lecture_etat_ba_l2_mere_v1.py' "$B/bloc-m-phase-c-v3.sh" && bon "bloc M extrait de la commande de la phase C v3 (son dernier bloc)" || mauvais "bloc M introuvable dans la phase C v3"\n''',
     '''grep -q 'lecture_etat_ba_l2_mere_v1.py' "$B/bloc-m-phase-c-v3.sh" && bon "bloc M extrait de la commande de la phase C v3 (son dernier bloc)" || mauvais "bloc M introuvable dans la phase C v3"
cmp -s "$B/bloc-m-phase-c-v3.sh" "$B/bloc-m-phase-c-v4-brouillon1.sh" && bon "bloc M du brouillon 1 de la phase C v4 égal à l'octet à celui de la v3 ($(sha256sum "$B/bloc-m-phase-c-v3.sh" | cut -c1-12)…)" || mauvais "bloc M : la v4 diffère de la v3"
LIGNE_IS='IS=$(grep '"'"'^| ISSUE-MOTS-ET-COUT-T06 |'"'"' registres/scellements-v1.md | cut -d'"'"'|'"'"' -f4 | tr -d '"'"' '"'"')'
for v in v3 v4-brouillon1; do f="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-$v.md"
    [ "$(grep -c -x -F "$LIGNE_IS" "$f")" = 3 ] && grep -q -F 'place . "refs/remotes/origin/$BR_P" "$IS"; place . "refs/remotes/origin/$BR_P" "$IS.sha256"; fi' "$f" \\
        && grep -q -F "BR_P='<<BRANCHE_PIECE>>'" "$f" \\
        && bon "phase C $v : fichier d'issue lu par la ligne ISSUE-MOTS-ET-COUT-T06 (C2, C5, F-C), repris sur <<BRANCHE_PIECE>> au bloc C2, comme la répétition le joue" \\
        || mauvais "phase C $v : forme du bloc C2 autre que celle que la répétition joue"; done
''',
     1),
    ('''printf '%s' "$DERNIERE" | grep -q "manifeste de 7b égal à la ligne RUN-CONFIRMATION-T06" && [ "$(printf '%s\\n' "$DERNIERE" | grep -c 'déjà là, égal')" = 10 ] && bon "[p1] B3 : dix fichiers déjà là, égaux ; manifeste égal à la ligne" || mauvais "[p1] B3 reprise"\n''',
     '''printf '%s' "$DERNIERE" | grep -q "manifeste de 7b égal à la ligne RUN-CONFIRMATION-T06" && [ "$(printf '%s\\n' "$DERNIERE" | grep -c 'déjà là, égal')" = 10 ] && bon "[p1] B3 : dix fichiers déjà là, égaux ; manifeste égal à la ligne" || mauvais "[p1] B3 reprise"
o=0; for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do o=$(( o + $(stat -c %s "$T/entrees/saines/$f") )); done
printf '%s' "$DERNIERE" | grep -q -F "10 fichiers ; cinq entrées : $o octets ; aucun nom interdit" && bon "[p1] B3 : somme des tailles des cinq entrées égale à celle des entrées fabriquées ($o octets, compagnons non comptés)" || mauvais "[p1] B3 : somme des tailles"
''',
     1),
    ('mv "$E/diag/$R6/resume.json" "$E/diag/$R6/de-trop.json"\n',
     'mv "$E/diag/$R6/resume.json" "$E/diag/$R6/note-bbis.json"\n'
     'joue "[p1] artefact : nom de l\'étape B bis parmi les entrées → B3 arrête" "$B/b07.sh" 1 "1 nom(s) interdit(s) parmi les entrées"\n'
     'mv "$E/diag/$R6/note-bbis.json" "$E/diag/$R6/de-trop.json"\n',
     1),
    ('''joue "[p1] artefact (exigences jouets introuvables) : B2 lance l'installation, détachée" "$B/b06.sh" 0 "installation lancée, détachée"\n''',
     '''grep -q -F '"$1/bin/pip" install -q --disable-pip-version-check --no-cache-dir -r "$2"' "$B/b06.sh" && bon "[p1] B2 : l'installation détachée est sans cache de pip (--no-cache-dir)" || mauvais "[p1] B2 : pip avec cache"
joue "[p1] artefact (exigences jouets introuvables) : B2 lance l'installation, détachée" "$B/b06.sh" 0 "installation lancée, détachée"
''',
     1),
    ('''    && bon "[p1] journal provisoire : cinq faits P3B, huit lignes de fichiers (chemin, empreinte, objet), rien d'autre (17 lignes)" || mauvais "[p1] journal provisoire"\n''',
     '''    && bon "[p1] journal provisoire : cinq faits P3B, huit lignes de fichiers (chemin, empreinte, objet), rien d'autre (17 lignes)" || mauvais "[p1] journal provisoire"
printf '%s\\n' "$J" | grep -q -E '^registres-provisoires/compte-3-phase-b-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{4}-v3\\.md$' && head -1 "$T/journal-p1.md" | grep -q 'journal provisoire (v3)$' \\
    && grep -q '^- P3B-001 : commande phase B v3 exécutée depuis 20' "$T/journal-p1.md" && bon "[p1] journal provisoire : nom en -v3.md, titre (v3), « commande phase B v3 exécutée »" || mauvais "[p1] journal provisoire : nom ou version"
''',
     1),
]


def main(argv: list[str]) -> int:
    src, dst = Path(argv[0]), Path(argv[1])
    if dst.exists():
        print(f"ARRÊT : {dst} existe déjà (R12)")
        return 1
    b = src.read_bytes()
    if hashlib.sha256(b).hexdigest() != H_V2:
        print("ARRÊT : répétition v2 d'une autre empreinte")
        return 1
    t = b.decode("utf-8")
    for ancien, nouveau, n in COUPLES:
        if t.count(ancien) != n:
            print(f"ARRÊT : « {ancien[:70]}… » trouvé {t.count(ancien)} fois ({n} exigée(s)) ; rien n'est écrit")
            return 1
        t = t.replace(ancien, nouveau)
    dst.write_text(t, encoding="utf-8")
    print(f"{len(COUPLES)} couples ; {dst} : {hashlib.sha256(t.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
