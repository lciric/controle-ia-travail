#!/usr/bin/env python3
"""Extraction par programme, mot pour mot, des couples (ancien, nouveau) de la relecture
du concepteur sur une conception v2 corrigée par son erratum 1 ; écriture de l'erratum 2
et du texte consolidé « v2 plus erratum 1 plus erratum 2 » (classe C ; aucun appel
réseau ; ni la v2 ni l'erratum 1 ne sont réécrits).

Usage : python extraction-erratum-2-conceptions-v2-v2.py 1

Version 2 : seule différence avec la v1, la lecture de forme des passages cités
sur plusieurs lignes dans le format « - Rn. » (dossier 1, couple R17), tranchée par
l'orchestrateur : les lignes de suite portent l'indentation de la liste de la
relecture, soit la colonne de contenu de la ligne « - Rn. » (son indentation plus
deux) ; cette indentation est retirée, et seulement elle.

- construit en mémoire « v2 plus erratum 1 » (couples de l'erratum 1 relus par programme) ;
- lit les couples de la relecture ; un passage cité qui court sur plusieurs lignes est
  déclaré ambigu (l'indentation de la suite ne se lit pas sans choix) ; ambigu ou
  introuvable ou en double : arrêt, rien n'est écrit ;
- vérifie : chaque ancien est unique dans « v2 plus erratum 1 » et dans son corps ;
  appliqués dans l'ordre, chacun est unique à son tour ; chaque nouveau est présent ;
  défaire dans l'ordre inverse redonne « v2 plus erratum 1 » ;
- refuse d'écraser un fichier existant.
"""
import importlib.util
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ext1", ICI / "extraction-erratum-1-conceptions-v2-v1.py")
ext1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ext1)
Arret, sha256, verifier_compagnon, cloture = ext1.Arret, ext1.sha256, ext1.verifier_compagnon, ext1.cloture
RACINE, BASE = ext1.RACINE, ext1.BASE
MARQUE = "<!-- fin de l'en-tête de la v2 ; le texte de la v1 corrigé suit -->\n\n"
ORDRE = {"ligne": "ordre numérique, que la relecture prescrit", "blocs": "ordre d'apparition dans la relecture, qui n'en prescrit pas",
         "k": "ordre de la relecture, K1 à K13"}
CAS = {
    "1": {"titre": "Conception 1 — le hasard du défenseur comme preuve",
          "stem": "conception-1-hasard-du-defenseur", "format": "ligne"},
    "2": {"titre": "Conception 2 — les épreuves du devin",
          "stem": "conception-2-epreuves-du-devin", "format": "k"},
    "3": {"titre": "Conception 3 — l'audit après coup",
          "stem": "conception-3-audit-apres-coup", "format": "blocs"},
}


def lire_erratum_1(texte: str):
    motif = re.compile(r"^## (\S+)[^\n]*\n\nAncien :\n(`{3,})text\n(.*?)\n\2\n\nNouveau :\n(`{3,})text\n(.*?)\n\4\n", re.S | re.M)
    couples = [{"id": m.group(1), "ancien": m.group(3), "nouveau": m.group(5)} for m in motif.finditer(texte)]
    if not couples or len(couples) != len(re.findall(r"^## ", texte, re.M)):
        raise Arret("erratum 1 : couples non tous lisibles")
    return couples


def cites(fragment: str):
    """Passages « … » de premier niveau (guillemets imbriqués gardés) ou `…`."""
    out, i = [], 0
    while i < len(fragment):
        ch = fragment[i]
        if ch == "`":
            j = fragment.index("`", i + 1)
            out.append(fragment[i + 1:j]); i = j + 1
        elif ch == "«":
            prof, j = 1, i + 1
            while prof:
                if fragment[j] == "«": prof += 1
                elif fragment[j] == "»": prof -= 1
                j += 1
            c = fragment[i + 1:j - 1]
            if not (c.startswith(" ") and c.endswith(" ")):
                raise Arret(f"passage cité sans espaces de bord : {c[:60]}")
            out.append(c[1:-1]); i = j
        else:
            i += 1
    return out


LECTURES = []
ATTENDU_R17 = ("- Elle ne dit rien d'une sensibilité sans dommage.\n"
               "- Elle ne protège pas l'oracle d'une paraphrase de l'étiquette par l'agent : G3 ne retire que les copies exactes.")


def lire_ligne(texte: str):
    """Couples « - Rn. Ancien : X → Nouveau : Y », X et Y en `…` ou « … »."""
    couples, ambigus = [], []
    debuts = list(re.finditer(r"^\s*- (R\d+)\. Ancien : ", texte, re.M))
    for k, m in enumerate(debuts):
        fin = debuts[k + 1].start() if k + 1 < len(debuts) else len(texte)
        bloc = texte[m.end() - len("Ancien : "):fin]
        # le couple s'arrête à la fin du dernier passage cité de « Nouveau »
        a_txt, sep, n_txt = bloc.partition(" → Nouveau : ")
        if not sep:
            raise Arret(f"{m.group(1)} : « → Nouveau : » absent")
        anc = cites(a_txt)
        if n_txt[:1] not in ("«", "`"):
            raise Arret(f"{m.group(1)} : le nouveau ne commence pas par un passage cité")
        nv = cites(n_txt[: fin_cite(n_txt)] if n_txt.startswith("«") else n_txt[: n_txt.index("`", 1) + 1])
        if len(anc) != 1 or len(nv) != 1:
            raise Arret(f"{m.group(1)} : {len(anc)} ancien(s), {len(nv)} nouveau(x) cités")
        c = {"id": m.group(1), "ancien": anc[0], "nouveau": nv[0], "lieu": lieu_de(texte, m.start())}
        colonne = len(m.group(0)) - len(m.group(0).lstrip(" ")) + 2
        if "\n" in c["nouveau"] and "\n" not in c["ancien"]:
            tete, *suite = c["nouveau"].split("\n")
            retrait = " " * colonne
            if all(x.startswith(retrait) for x in suite):
                c["nouveau"] = "\n".join([tete] + [x[colonne:] for x in suite])
                c["note"] = (f"passage cité sur {len(suite) + 1} lignes : l'indentation de {colonne} espaces des lignes de suite, "
                             "colonne de contenu de la ligne de la relecture, est retirée (lecture de forme tranchée par l'orchestrateur)")
                LECTURES.append((c["id"], colonne))
        if "\n" in c["ancien"] or "\n" in c["nouveau"] and not c.get("note"):
            ambigus.append(f"{c['id']} : passage cité sur plusieurs lignes ; l'indentation de la suite "
                           f"(« {c['nouveau'].splitlines()[1][:40]}… ») est celle de la liste de la relecture "
                           "ou celle du texte à porter : non décidable sans choix")
        couples.append(c)
    # la relecture dit : « dans l'ordre R1 à R17 » ; ordre numérique
    couples.sort(key=lambda c: int(c["id"][1:]))
    if [int(c["id"][1:]) for c in couples] != list(range(1, len(couples) + 1)):
        raise Arret(f"numérotation lacunaire ou en double : {[c['id'] for c in couples]}")
    return couples, ambigus


def lire_k(texte: str):
    """Sections « **Kn** (lieu) » ; « - Ancien : « … » » puis « - Nouveau : « … » »,
    ou « - Nouveau, en N lignes : » suivi de N sous-puces citées, réunies par un saut de ligne."""
    couples, ambigus = [], []
    tetes = list(re.finditer(r"^\*\*(K\d+)\*\* \(([^\n]*)\)$", texte, re.M))
    nombres = {"deux": 2, "trois": 3, "quatre": 4}
    for k, t in enumerate(tetes):
        fin = tetes[k + 1].start() if k + 1 < len(tetes) else texte.index("\n## ", t.end())
        sec = texte[t.end():fin]
        ma = re.search(r"^- Ancien : ", sec, re.M)
        mn = re.search(r"^- Nouveau(?:, en (\w+) lignes)? : ?", sec, re.M)
        if not ma or not mn or mn.start() < ma.start():
            raise Arret(f"{t.group(1)} : lignes Ancien et Nouveau non lisibles")
        anc = cites(sec[ma.end():mn.start()])
        nv = cites(sec[mn.end():])
        attendu = nombres[mn.group(1)] if mn.group(1) else 1
        if len(anc) != 1 or len(nv) != attendu:
            raise Arret(f"{t.group(1)} : {len(anc)} ancien(s), {len(nv)} nouveau(x) pour {attendu} attendu(s)")
        c = {"id": t.group(1), "lieu": t.group(2), "ancien": anc[0], "nouveau": "\n".join(nv)}
        if attendu > 1:
            c["note"] = f"nouveau en {mn.group(1)} lignes, réunies par un saut de ligne"
        if "\n" in anc[0] or any("\n" in x for x in nv):
            ambigus.append(f"{c['id']} : passage cité sur plusieurs lignes")
        couples.append(c)
    if [c["id"] for c in couples] != [f"K{i}" for i in range(1, len(couples) + 1)]:
        raise Arret(f"numérotation inattendue : {[c['id'] for c in couples]}")
    return couples, ambigus


def fin_cite(s: str) -> int:
    prof, j = 0, 0
    while True:
        if s[j] == "«": prof += 1
        elif s[j] == "»":
            prof -= 1
            if prof == 0:
                return j + 1
        j += 1


def lieu_de(texte: str, pos: int) -> str:
    t = [m.group(1) for m in re.finditer(r"^\*\*(Constat [^*]+|[^*]+)\*\*", texte[:pos], re.M)]
    return t[-1] if t else "?"


def lire_blocs(texte: str):
    paire = re.compile(r"^Ancien :\n```text\n(.*?)\n```\nNouveau :\n```text\n(.*?)\n```", re.S | re.M)
    paires = list(paire.finditer(texte))
    if len(paires) != len(re.findall(r"^Ancien :", texte, re.M)):
        raise Arret("blocs « Ancien : » non tous lisibles")
    couples, par_entete = [], {}
    for p in paires:
        ent = list(re.finditer(r"^\*\*(F-\d+)(?: et (F-\d+))?\b[^\n]*", texte[:p.start()], re.M))[-1]
        ids = [x for x in ent.groups() if x]
        rang = par_entete.get(ent.start(), 0)
        if rang >= len(ids):
            raise Arret(f"plus de couples que d'identifiants sous « {ent.group(0)[:40]} »")
        par_entete[ent.start()] = rang + 1
        couples.append({"id": ids[rang], "ancien": p.group(1), "nouveau": p.group(2),
                        "lieu": ent.group(0).strip("*").strip(),
                        **({"note": "identifiant attribué par l'ordre des couples sous l'intitulé commun"} if len(ids) > 1 else {})})
    return couples, []


def appliquer(t, couples, quoi):
    for x in couples:
        if t.count(x["ancien"]) != 1:
            raise Arret(f"{quoi} {x['id']} : ancien trouvé {t.count(x['ancien'])} fois à son tour")
        t = t.replace(x["ancien"], x["nouveau"], 1)
    for x in couples:
        if x["nouveau"] not in t:
            raise Arret(f"{quoi} {x['id']} : nouveau absent")
    return t


def defaire(t, couples, quoi):
    for x in reversed(couples):
        if t.count(x["nouveau"]) != 1:
            raise Arret(f"{quoi} {x['id']} : nouveau trouvé {t.count(x['nouveau'])} fois en défaisant")
        t = t.replace(x["nouveau"], x["ancien"], 1)
    return t


def bloc_couple(x):
    fa, fn = cloture(x["ancien"]), cloture(x["nouveau"])
    note = f" ({x['note']})" if x.get("note") else ""
    return [f"## {x['id']} — {x['lieu']}{note}", "", "Ancien :", f"{fa}text", x["ancien"], fa, "",
            "Nouveau :", f"{fn}text", x["nouveau"], fn, ""]


def principal(cle):
    c = CAS[cle]
    d = f"{BASE}/conceptions-v2"
    v2c, e1c = f"{d}/{c['stem']}-v2.md", f"{d}/{c['stem']}-v2-erratum-1.md"
    relc = f"{BASE}/relectures-fable-v2/conception-{cle}/relecture-fable-api.md"
    e2c, v3c = f"{d}/{c['stem']}-v2-erratum-2.md", f"{d}/{c['stem']}-v3-consolidee.md"
    for p in (e2c, v3c):
        if (RACINE / p).exists():
            raise Arret(f"refus d'écraser : {p}")
    sha = {p: verifier_compagnon(RACINE / p) for p in (v2c, e1c, relc)}
    v2 = (RACINE / v2c).read_text(encoding="utf-8")
    e1 = lire_erratum_1((RACINE / e1c).read_text(encoding="utf-8"))
    v2e1 = appliquer(v2, e1, "erratum 1")
    if defaire(v2e1, e1, "erratum 1") != v2:
        raise Arret("erratum 1 : défaire ne redonne pas la v2")
    rel = (RACINE / relc).read_text(encoding="utf-8")
    rel = rel[rel.index("\n---\n"):]
    if cle != "1":
        raise Arret("la v2 du programme ne traite que le dossier 1")
    couples, ambigus = {"ligne": lire_ligne, "blocs": lire_blocs, "k": lire_k}[c["format"]](rel)
    if [x[0] for x in LECTURES] != ["R17"]:
        raise Arret(f"lecture de forme appliquée à {LECTURES}, attendu R17 seul")
    if next(x for x in couples if x["id"] == "R17")["nouveau"] != ATTENDU_R17:
        raise Arret("R17 : le nouveau texte lu ne redonne pas le texte donné par l'orchestrateur")
    corps = v2e1.split(MARQUE, 1)[1]
    corps_v2 = v2.split(MARQUE, 1)[1]
    fautes = list(ambigus)
    for x in couples:
        n, nc = v2e1.count(x["ancien"]), corps.count(x["ancien"])
        if n != 1 or nc != 1:
            fautes.append(f"{x['id']} : ancien trouvé {n} fois dans « v2 plus erratum 1 » ({nc} dans le corps)")
    if fautes:
        raise Arret(f"{len(couples)} couples lus ; dossier arrêté, aucun fichier écrit :\n  " + "\n  ".join(fautes))
    v2e1e2 = appliquer(v2e1, couples, "erratum 2")
    if defaire(v2e1e2, couples, "erratum 2") != v2e1:
        raise Arret("erratum 2 : défaire ne redonne pas « v2 plus erratum 1 »")
    corps3 = appliquer(corps_v2, e1, "erratum 1 (corps)")
    corps3 = appliquer(corps3, couples, "erratum 2 (corps)")
    if corps3 != v2e1e2.split(MARQUE, 1)[1]:
        raise Arret("corps consolidé non conforme")
    if defaire(defaire(corps3, couples, "erratum 2"), e1, "erratum 1") != corps_v2:
        raise Arret("défaire les deux errata ne redonne pas le corps de la v2")
    outil = f"{d}/{Path(__file__).name}"
    sha_outil = sha256(Path(__file__).resolve())
    ids = " ; ".join(x["id"] for x in couples)
    l = [f"# Erratum 2 — {c['titre']} — v2", "",
         f"- **Cet erratum prime sur la v2 et sur l'erratum 1** : v2 `{v2c}` — sha256 {sha[v2c]} ; erratum 1 `{e1c}` — sha256 {sha[e1c]} (compagnons vérifiés). Ni la v2 ni l'erratum 1 ne sont réécrits.",
         f"- Ses couples s'appliquent à la v2 corrigée par l'erratum 1, dans l'ordre ci-dessous.",
         f"- Source des couples : relecture du concepteur `{relc}` — sha256 {sha[relc]} (compagnon vérifié).",
         f"- Couples extraits par programme, mot pour mot, par `{outil}` — sha256 {sha_outil}.",
         f"- **Lecture de R17, tranchée par l'orchestrateur, pas par le concepteur** (lecture de forme). Dans la relecture, la ligne « - R17. » est indentée de deux espaces ; sa colonne de contenu est donc {LECTURES[0][1]}, et les {LECTURES[0][1]} espaces de la seconde ligne du nouveau texte sont l'indentation de la liste de la relecture. L'ancien texte est en colonne 0 dans la v2. Le nouveau texte est donc « - Elle ne dit rien d'une sensibilité sans dommage. », un saut de ligne, puis « - Elle ne protège pas l'oracle d'une paraphrase de l'étiquette par l'agent : G3 ne retire que les copies exactes. », en colonne 0 (puce sœur). Le programme retire ces {LECTURES[0][1]} espaces et rien d'autre, et vérifie que le résultat est ce texte.",
         "- Vérifications du programme : « v2 plus erratum 1 » construit en mémoire ; chaque ancien y figure une seule fois ; appliqués dans l'ordre, chacun est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne « v2 plus erratum 1 ».",
         f"- Texte consolidé : `{v3c}`.",
         f"- Couples ({len(couples)}), dans l'ordre d'application ({ORDRE[c['format']]}) : {ids}.", ""]
    for x in couples:
        l += bloc_couple(x)
    with open(RACINE / e2c, "x", encoding="utf-8") as f:
        f.write("\n".join(l))
    sha_e2 = sha256(RACINE / e2c)
    h = [f"# {c['titre']} — v3 consolidée", "",
         "- **Consolidation mécanique seulement, sans aucun mot nouveau** : le texte qui suit l'en-tête est le corps de la v2, auquel sont appliqués par programme, mot pour mot, les couples de l'erratum 1 puis ceux de l'erratum 2. Elle ne remplace aucune de ces pièces, qui font foi.",
         f"- v2 : `{v2c}` — sha256 {sha[v2c]}.",
         f"- Erratum 1 : `{e1c}` — sha256 {sha[e1c]} ({len(e1)} couples).",
         f"- Erratum 2 : `{e2c}` — sha256 {sha_e2} ({len(couples)} couples).",
         f"- Lecture de forme de R17 tranchée par l'orchestrateur : voir l'en-tête de l'erratum 2.",
         f"- Programme : `{outil}` — sha256 {sha_outil}. Défaire l'erratum 2 puis l'erratum 1 redonne exactement le corps de la v2.",
         "", "<!-- fin de l'en-tête de la consolidation ; le texte consolidé suit -->", "", ""]
    with open(RACINE / v3c, "x", encoding="utf-8") as f:
        f.write("\n".join(h) + corps3)
    print(f"erratum 2 : {e2c} — sha256 {sha_e2} ; couples {len(couples)}")
    print(f"consolidée : {v3c} — sha256 {sha256(RACINE / v3c)}")


if __name__ == "__main__":
    try:
        principal(sys.argv[1])
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
