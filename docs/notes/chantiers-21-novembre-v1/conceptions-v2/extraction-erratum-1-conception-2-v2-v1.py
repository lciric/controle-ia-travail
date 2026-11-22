#!/usr/bin/env python3
"""Extraction par programme, mot pour mot, des huit couples de la vérification de la
conception 2 (épreuves du devin), v2, et écriture de l'erratum 1 de cette v2
(classe C ; aucun appel réseau ; la v2 n'est pas réécrite).

La lecture des cellules est celle de `portage-conception-2-v2.py` (fonction
`lire_cellules`, importée sans modification) ; l'écriture et les épreuves reprennent
celles de `extraction-erratum-1-conceptions-v2-v1.py` (fonctions importées).
Ordre d'application : celui de la table de la vérification.
"""
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent


def charger(nom):
    spec = importlib.util.spec_from_file_location(nom.replace("-", "_"), ICI / nom)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


portage = charger("portage-conception-2-v2.py")
extraction = charger("extraction-erratum-1-conceptions-v2-v1.py")
Arret = portage.Arret
RACINE, BASE = portage.RACINE, portage.BASE
V2 = f"{BASE}/conceptions-v2/conception-2-epreuves-du-devin-v2.md"
VERIF = f"{BASE}/contre-lectures-v1/verification-conception-2-v2-opus-v1.md"
SORTIE = f"{BASE}/conceptions-v2/conception-2-epreuves-du-devin-v2-erratum-1.md"
ATTENDUS = ["6-b", "9-b", "13-b", "16-a", "17-a", "18-a", "2-b", "1-c"]


def appliquer_et_defaire(v2, couples):
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


def principal():
    v2p, verp, sortie = RACINE / V2, RACINE / VERIF, RACINE / SORTIE
    if sortie.exists():
        raise Arret(f"refus d'écraser : {sortie}")
    sha_v2, sha_ver = extraction.verifier_compagnon(v2p), extraction.verifier_compagnon(verp)
    v2 = v2p.read_text(encoding="utf-8")
    lues, non_portees = portage.lire_cellules(verp.read_text(encoding="utf-8"))
    if non_portees:
        raise Arret(f"éléments hors format dans la table : {[c['numero_table'] for c in non_portees]}")
    couples = [{"id": c["numero_table"], "lieu": c["lieu"], "gravite": c["gravite"], "mode": c["mode"],
                "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in lues]
    if [x["id"] for x in couples] != ATTENDUS:
        raise Arret(f"couples lus {[x['id'] for x in couples]} ≠ attendus {ATTENDUS}")
    fautes = [f"{x['id']} : ancien trouvé {v2.count(x['ancien'])} fois" for x in couples if v2.count(x["ancien"]) != 1]
    if fautes:
        raise Arret("aucun fichier écrit :\n  " + "\n  ".join(fautes))
    appliquer_et_defaire(v2, couples)
    sha_outil = extraction.sha256(Path(__file__).resolve())
    l = [
        "# Erratum 1 — Conception 2 — les épreuves du devin — v2",
        "",
        f"- **Cet erratum prime sur la v2** : `{V2}` — sha256 {sha_v2} (compagnon vérifié). La v2 n'est pas réécrite ; elle se lit avec cet erratum.",
        f"- Source des couples : `{VERIF}` — sha256 {sha_ver} (compagnon vérifié), table des constats.",
        f"- Couples extraits par programme, mot pour mot, par `{BASE}/conceptions-v2/{Path(__file__).name}` — sha256 {sha_outil} "
        f"(lecture des cellules : `portage-conception-2-v2.py`, sha256 {extraction.sha256(ICI / 'portage-conception-2-v2.py')}). "
        "Un nouveau donné « en deux lignes » est réuni par un saut de ligne.",
        "- Vérifications du programme : chaque ancien figure une seule fois dans la v2 ; appliqués dans l'ordre ci-dessous, chaque ancien est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne exactement la v2.",
        f"- Couples ({len(couples)}), à appliquer dans l'ordre de la table de la vérification : " + " ; ".join(x["id"] for x in couples) + ".",
        "",
    ]
    for x in couples:
        fa, fn = extraction.cloture(x["ancien"]), extraction.cloture(x["nouveau"])
        mode = "" if x["mode"] == "simple" else " — nouveau en deux lignes"
        l += [f"## {x['id']} — {x['gravite']} — {x['lieu']}{mode}", "",
              "Ancien :", f"{fa}text", x["ancien"], fa, "", "Nouveau :", f"{fn}text", x["nouveau"], fn, ""]
    with open(sortie, "x", encoding="utf-8") as f:
        f.write("\n".join(l))
    print(f"erratum écrit : {SORTIE} — sha256 {extraction.sha256(sortie)} ; couples : {len(couples)}")


if __name__ == "__main__":
    try:
        principal()
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
