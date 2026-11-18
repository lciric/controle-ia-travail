"""Fabrique la conception finale du saboteur a budget (ii-b) -- v1 -- par programme.

Usage (depuis la racine du depot) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-conception-finale-ii-b-v1.py

1. verifie les empreintes du brouillon 2 et du rapport de verification ;
2. lit les couples F1 a F21 dans le § 4 du rapport (blocs « Ancien » / « Nouveau » entre clotures text,
   sans le saut de ligne final), sans rien recopier a la main ;
3. les applique dans l'ordre ; chaque « ancien » doit etre trouve exactement une fois, sinon arret sans rien ecrire ;
4. verifie l'empreinte du resultat, sinon arret sans rien ecrire ;
5. ecrit conception-ii-b-v1.md puis differences-conception-brouillon2-vers-v1-v1.md (chaque hunk de diff -u
   rattache a son couple, puis la sortie entiere de diff). Creation exclusive : jamais d'ecrasement (R12).
"""
from __future__ import annotations

import difflib
import hashlib
import re
import sys
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
SOURCE = DOSSIER / "conception-ii-b-v1-brouillon2.md"
EMPREINTE_SOURCE = "47b86258df937dc5ec8c3e6ff74cc708ea0487a018f54f3a91a721b76543209c"
RAPPORT = DOSSIER / "verification-conception-ii-b-brouillon2-v1.md"
EMPREINTE_RAPPORT = "9996b8ca675d3ec86e570c366ba643a7d1707791f4db4a57647f99b3d0731d90"
EMPREINTE_ATTENDUE = "77f1cc99a766190f31d0fa78226f8b74afda3345355701cfd222ee4fdc2aeb8c"
SORTIE = DOSSIER / "conception-ii-b-v1.md"
NOTE = DOSSIER / "differences-conception-brouillon2-vers-v1-v1.md"
NB = 21


def arret(msg: str) -> None:
    sys.exit(f"ARRET, rien ecrit : {msg}")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> None:
    for f in (SORTIE, NOTE):
        if f.exists():
            arret(f"{f.name} existe deja (R12)")
    src_b, rap_b = SOURCE.read_bytes(), RAPPORT.read_bytes()
    if sha(src_b) != EMPREINTE_SOURCE:
        arret("empreinte du brouillon 2 differente")
    if sha(rap_b) != EMPREINTE_RAPPORT:
        arret("empreinte du rapport differente")
    source, rapport = src_b.decode("utf-8"), rap_b.decode("utf-8")

    debut = rapport.index("\n## 4. Verdict et couples exacts")
    fin = rapport.index("\n## 5. Refus", debut)
    sect = rapport[debut:fin]
    motif = re.compile(
        r"^### F(\d+) — ([^\n]*)\n\nAncien :\n\n```text\n(.*?)\n```\n\nNouveau :\n\n```text\n(.*?)\n```\n",
        re.S | re.M,
    )
    couples = [(int(m[1]), m[2], m[3], m[4]) for m in motif.finditer(sect)]
    if [c[0] for c in couples] != list(range(1, NB + 1)):
        arret(f"couples lus : {[c[0] for c in couples]}, attendu F1 a F{NB}")
    if len(re.findall(r"^### F\d+ ", sect, re.M)) != NB:
        arret("nombre d'en-tetes de couples different de 21")

    texte = source
    for n, titre, avant, apres in couples:
        k = texte.count(avant)
        if k != 1:
            arret(f"F{n} : « ancien » trouve {k} fois, attendu 1")
        texte = texte.replace(avant, apres, 1)
    sortie_b = texte.encode("utf-8")
    if sha(sortie_b) != EMPREINTE_ATTENDUE:
        arret(f"empreinte du resultat {sha(sortie_b)} != attendue")

    # rattachement des hunks aux couples : un hunk est lie au couple dont l'« apres » (ou l'« avant »)
    # recoupe ses lignes
    a, b = source.splitlines(keepends=True), texte.splitlines(keepends=True)
    diff = list(difflib.unified_diff(a, b, "brouillon2", "v1", n=3))
    sortie_diff = "".join(diff)
    hunks, cur = [], None
    for l in diff[2:]:
        if l.startswith("@@"):
            cur = [l, []]
            hunks.append(cur)
        else:
            cur[1].append(l)
    lignes_notes = []
    for i, (ent, corps) in enumerate(hunks, 1):
        chg = "".join(l[1:] for l in corps if l[0] in "+-")
        liens = [f"F{n}" for n, _, av, ap in couples
                 if any(x and x in chg for x in (av.strip().splitlines()[0], ap.strip().splitlines()[0]))]
        if not liens:
            arret(f"hunk {i} rattache a aucun couple")
        lignes_notes.append(f"- Hunk {i} `{ent.strip()}` : couple(s) {', '.join(liens)}")

    note = (
        "# Differences : conception du saboteur a budget (ii-b), brouillon 2 vers version finale v1\n\n"
        f"Source `{SOURCE.name}` (`{EMPREINTE_SOURCE}`) ; resultat `{SORTIE.name}` (`{EMPREINTE_ATTENDUE}`) ; "
        f"couples F1 a F{NB} lus par programme au § 4 de `{RAPPORT.name}` (`{EMPREINTE_RAPPORT}`), "
        "appliques dans l'ordre, chacun exactement une fois.\n\n"
        "## Couples\n\n" + "\n".join(f"- F{n} — {t}" for n, t, _, _ in couples) +
        "\n\n## Hunks rattaches\n\n" + "\n".join(lignes_notes) +
        "\n\n## Sortie de `diff -u`\n\n```diff\n" + sortie_diff + ("" if sortie_diff.endswith("\n") else "\n") + "```\n"
    )
    with open(SORTIE, "xb") as f:
        f.write(sortie_b)
    with open(NOTE, "xb") as f:
        f.write(note.encode("utf-8"))
    print("ecrit", SORTIE.name, sha(sortie_b))
    print("ecrit", NOTE.name)


if __name__ == "__main__":
    main()
