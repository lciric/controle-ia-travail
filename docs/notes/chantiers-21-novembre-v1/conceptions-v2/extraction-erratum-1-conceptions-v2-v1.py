#!/usr/bin/env python3
"""Extraction par programme, mot pour mot, des couples (ancien, nouveau) restants
d'une vérification de conception v2, et écriture de l'erratum 1 de cette v2
(classe C, outil de correction ; aucun appel réseau ; la v2 n'est pas réécrite).

Usage : python extraction-erratum-1-conceptions-v2-v1.py 1|3

- lit les couples dans la vérification, par programme ;
- exige que chaque ancien figure une seule fois dans la v2 ; sinon, arrêt, rien n'est écrit ;
- éprouve en mémoire : appliqués dans l'ordre, chaque ancien est unique à son tour,
  chaque nouveau est présent, et défaire dans l'ordre inverse redonne la v2 ;
- refuse d'écraser un fichier existant.
"""
import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
BASE = "docs/notes/chantiers-21-novembre-v1"
CAS = {
    "1": {
        "titre": "Conception 1 — le hasard du défenseur comme preuve — v2",
        "v2": f"{BASE}/conceptions-v2/conception-1-hasard-du-defenseur-v2.md",
        "verification": f"{BASE}/contre-lectures-v1/verification-conception-1-v2-opus-v1.md",
        "sortie": f"{BASE}/conceptions-v2/conception-1-hasard-du-defenseur-v2-erratum-1.md",
        "format": "sections",
    },
    "3": {
        "titre": "Conception 3 — l'audit après coup — v2",
        "v2": f"{BASE}/conceptions-v2/conception-3-audit-apres-coup-v2.md",
        "verification": f"{BASE}/contre-lectures-v1/verification-conception-3-v2-opus-v1.md",
        "sortie": f"{BASE}/conceptions-v2/conception-3-audit-apres-coup-v2-erratum-1.md",
        "format": "blocs",
    },
}


class Arret(Exception):
    pass


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verifier_compagnon(p: Path) -> str:
    comp = p.with_name(p.name + ".sha256")
    if not comp.exists():
        raise Arret(f"compagnon absent : {comp}")
    attendu, vu = comp.read_text(encoding="utf-8").split()[0], sha256(p)
    if attendu != vu:
        raise Arret(f"empreinte non conforme : {p}")
    return vu


def section_couples(texte: str) -> str:
    debut = texte.index("## Couples restants")
    fin = texte.find("\n## ", debut + 3)
    return texte[debut: fin if fin >= 0 else len(texte)]


# un élément : « Ancien : » ou « Nouveau : » (ou « → nouveau : ») suivi d'un code en ligne
# `…` ou d'un bloc clôturé ```[langue]\n…\n```
ELEMENT = re.compile(
    r"(Ancien|[Nn]ouveau)\s*:\s*(?:`([^`\n]+)`|\n```[a-z]*\n(.*?)\n```)", re.S)


def lire_sections(sec: str):
    """Sections « ### Xn — titre » ; dans chacune, couples ancien puis nouveau."""
    couples = []
    titres = list(re.finditer(r"^### (\S+) — (.*)$", sec, re.M))
    if not titres:
        raise Arret("aucune section ### dans « Couples restants »")
    for i, t in enumerate(titres):
        corps = sec[t.end(): titres[i + 1].start() if i + 1 < len(titres) else len(sec)]
        elems = list(ELEMENT.finditer(corps))
        if not elems or len(elems) % 2:
            raise Arret(f"{t.group(1)} : éléments ancien, nouveau non appariés ({len(elems)})")
        nb_ancien = len(re.findall(r"\bAncien\s*:", corps))
        nb_nouveau = len(re.findall(r"\b[Nn]ouveau\s*:", corps))
        if nb_ancien != len(elems) // 2 or nb_nouveau != len(elems) // 2:
            raise Arret(f"{t.group(1)} : marques Ancien/Nouveau non toutes lisibles")
        for k in range(0, len(elems), 2):
            a, n = elems[k], elems[k + 1]
            if a.group(1) != "Ancien" or n.group(1).lower() != "nouveau":
                raise Arret(f"{t.group(1)} : ordre ancien, nouveau rompu")
            couples.append({
                "id": f"{t.group(1)}.{k // 2 + 1}" if len(elems) > 2 else t.group(1),
                "section": t.group(1), "lieu": t.group(2),
                "ancien": a.group(2) if a.group(2) is not None else a.group(3),
                "nouveau": n.group(2) if n.group(2) is not None else n.group(3),
            })
    return couples


def lire_blocs(sec: str):
    motif = re.compile(r"^\*\*(R-\d+)\*\*\nAncien :\n```text\n(.*?)\n```\nNouveau :\n```text\n(.*?)\n```", re.S | re.M)
    couples = [{"id": m.group(1), "section": m.group(1), "lieu": "voir la vérification",
                "ancien": m.group(2), "nouveau": m.group(3)} for m in motif.finditer(sec)]
    if len(couples) != len(re.findall(r"^\*\*R-\d+\*\*", sec, re.M)) or not couples:
        raise Arret("blocs R-n non tous lisibles")
    return couples


def cloture(t: str) -> str:
    n = 3
    while "`" * n in t:
        n += 1
    return "`" * n


def principal(cle: str):
    c = CAS[cle]
    v2p, verp, sortie = RACINE / c["v2"], RACINE / c["verification"], RACINE / c["sortie"]
    if sortie.exists():
        raise Arret(f"refus d'écraser : {sortie}")
    sha_v2, sha_ver = verifier_compagnon(v2p), verifier_compagnon(verp)
    v2 = v2p.read_text(encoding="utf-8")
    sec = section_couples(verp.read_text(encoding="utf-8"))
    couples = lire_sections(sec) if c["format"] == "sections" else lire_blocs(sec)
    fautes = [f"{x['id']} : ancien trouvé {v2.count(x['ancien'])} fois" for x in couples if v2.count(x["ancien"]) != 1]
    if fautes:
        raise Arret("aucun fichier écrit :\n  " + "\n  ".join(fautes))
    # épreuve en mémoire (rien n'est écrit dans la v2)
    t = v2
    for x in couples:
        if t.count(x["ancien"]) != 1:
            raise Arret(f"{x['id']} : ancien non unique à son tour")
        t = t.replace(x["ancien"], x["nouveau"], 1)
    for x in couples:
        if x["nouveau"] not in t:
            raise Arret(f"{x['id']} : nouveau absent après application")
    u = t
    for x in reversed(couples):
        if u.count(x["nouveau"]) != 1:
            raise Arret(f"{x['id']} : nouveau non unique en défaisant")
        u = u.replace(x["nouveau"], x["ancien"], 1)
    if u != v2:
        raise Arret("défaire ne redonne pas la v2")
    sha_outil = sha256(Path(__file__).resolve())
    l = [
        f"# Erratum 1 — {c['titre']}",
        "",
        f"- **Cet erratum prime sur la v2** : `{c['v2']}` — sha256 {sha_v2} (compagnon vérifié). La v2 n'est pas réécrite ; elle se lit avec cet erratum.",
        f"- Source des couples : `{c['verification']}` — sha256 {sha_ver} (compagnon vérifié), section « Couples restants ».",
        f"- Couples extraits par programme, mot pour mot, par `{BASE}/conceptions-v2/{Path(__file__).name}` — sha256 {sha_outil}.",
        "- Vérifications du programme : chaque ancien figure une seule fois dans la v2 ; appliqués dans l'ordre ci-dessous, chaque ancien est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne exactement la v2.",
        f"- Couples ({len(couples)}), à appliquer dans l'ordre : " + " ; ".join(x["id"] for x in couples) + ".",
        "",
    ]
    for x in couples:
        fa, fn = cloture(x["ancien"]), cloture(x["nouveau"])
        l += [f"## {x['id']}" + ("" if x["lieu"] == "voir la vérification" else f" — {x['lieu']}"), "",
              "Ancien :", f"{fa}text", x["ancien"], fa, "", "Nouveau :", f"{fn}text", x["nouveau"], fn, ""]
    with open(sortie, "x", encoding="utf-8") as f:
        f.write("\n".join(l))
    print(f"erratum écrit : {c['sortie']} — sha256 {sha256(sortie)} ; couples : {len(couples)}")


if __name__ == "__main__":
    try:
        principal(sys.argv[1])
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
