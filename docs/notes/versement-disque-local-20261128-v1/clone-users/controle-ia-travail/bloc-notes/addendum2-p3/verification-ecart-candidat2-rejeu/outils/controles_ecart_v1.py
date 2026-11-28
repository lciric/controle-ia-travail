"""Contrôles « rejeu et versement » de l'écart candidat 1 → candidat 2 (addendum 2 de P3), sur des copies.

Usage (depuis la racine du dépôt, pour le seul import de `controle_ia.prereg`) :
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -B -s controles_ecart_v1.py COPIES ARTEFACTS RAPPORT_VC1 DEPOT
  COPIES : dossier des copies (candidats 1 et 2, script, élément « Candidat 2 », plan v2, module v4).
  ARTEFACTS : dossier à moi ; y sont lus `entree7-fictive.md` et `entree7-chevrons.md`, y sont écrites les copies
    du candidat 2 avec l'entrée 7 (remplie par des empreintes fictives ; chevrons laissés).
  RAPPORT_VC1 : rapport de la contre-lecture 6 (mots des corrections VC1-01 à VC1-05).
  DEPOT : racine du dépôt ; seule l'existence de chemins exacts y est lue (aucune lecture de contenu).
Contrôles :
  A. empreintes des copies ;
  B. docstring du script : « mots exacts du rapport ; seuls les retours à la ligne sont choisis ici » ; corrections du
     rapport appliquées au candidat 1 (espaces normalisés), plus l'élément « Candidat 2 », égales au candidat 2 ;
  C. empreintes citées aux lignes changées (candidat 1 → candidat 2) égales aux sources du plan qui portent cette
     empreinte, recalculées ; chemin cité juste avant égal à la destination du plan ;
  D. `prereg.problemes`, garde 1 (expressions du module lues par `ast`, jamais importé), entrées « Contre-lecture » ;
     sur le candidat 2, puis sur le candidat 2 + entrée 7 fictive, puis + entrée 7 aux chevrons laissés ;
  E. plan de versement : empreinte de chaque source, destinations uniques, sous prereg/ ou docs/, absentes du dépôt ;
  F. chemins prereg/… et docs/… cités par le candidat 2 : pièce du plan de même empreinte, ou chemin existant au dépôt.
N'écrit que sous ARTEFACTS. N'importe du dépôt que `controle_ia.prereg`.
"""
import ast
import difflib
import hashlib
import json
import os
import re
import sys
from pathlib import Path

from controle_ia import prereg  # seul import du dépôt

ATTENDU = {
    "P3-addendum2-audit-verdict-v1-candidat1.md": "9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e",
    "P3-addendum2-audit-verdict-v1-candidat2.md": "5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247",
    "ecrire_candidat2_addendum2_v1.py": "51c7bd1b4886e43fd6a4bc80c8a11fbed3813c5307cd00b532c833d2295d5943",
    "ligne-candidat2-addendum2-v1.md": "7e106f17410587947775451f7ea58df978853b0e051338ba522c63d98b028568",
    "plan-versement-addendum2-v2.json": "6d312445bf7fa63bbea821c2a46c7d91f40918c1e5fe2df8190ae8594cdef39f",
    "audit_verdict_p3_v1.py": "967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d",
}
RAPPORT_VC1 = "3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f04"
MODULE, TESTS = ATTENDU["audit_verdict_p3_v1.py"], "f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07"
HEX = re.compile(r"\b[0-9a-f]{64}\b")
ANCRE = "- Date (UTC) : celle du commit de scellement, qui fait foi.\n"
ECHECS = []


def h(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def verifier(cond, msg):
    print(("  ok    " if cond else "  ÉCART ") + msg)
    if not cond:
        ECHECS.append(msg)


def guillemets(t, i):
    """Texte entre le « à l'indice i et son » apparié (imbrication comprise)."""
    assert t[i] == "«"
    n, j = 0, i
    while True:
        if t[j] == "«":
            n += 1
        elif t[j] == "»":
            n -= 1
            if n == 0:
                return t[i + 1:j].strip(), j
        j += 1


def corrections_vc1(rapport):
    """(constat, ancien, nouveau) pour chaque « remplacer « … » par « … » », et l'ajout de l'entrée 6 (VC1-03, point 2)."""
    out = []
    blocs = re.split(r"^### ", rapport, flags=re.M)
    for b in blocs:
        m = re.match(r"(VC1-0[1-5])", b)
        if not m:
            continue
        cid = m.group(1)
        cor = b[b.index("**Correction"):]
        for r in re.finditer(r"[Rr]emplacer «", cor):
            a, j = guillemets(cor, r.end() - 1)
            k = cor.index("«", j)
            assert re.fullmatch(r"\s*par\s*", cor[j + 1:k]), (cid, cor[j + 1:k])
            n, _ = guillemets(cor, k)
            out.append((cid, a, n))
        for r in re.finditer(r"ajouter après l'entrée 5 «", cor):
            n, _ = guillemets(cor, r.end() - 1)
            out.append((cid + " ajout", None, n))
    return out


def regex_garde1(module_src):
    arbre = ast.parse(module_src)
    motifs = {}
    for n in arbre.body:
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in (
                "EMPREINTE_MODULE_CITEE", "EMPREINTE_TESTS_CITEE"):
            v = n.value
            assert isinstance(v, ast.Call) and ast.unparse(v.func) == "re.compile" and len(v.args) == 1 and not v.keywords
            motifs[n.targets[0].id] = ast.literal_eval(v.args[0])
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in (
                "PREREG_ADDENDUM2", "CHEMIN_MODULE", "CHEMIN_TESTS"):
            motifs[n.targets[0].id] = ast.literal_eval(n.value)
    return motifs


def controles_texte(nom, chemin, motifs, entrees_attendues):
    print(f"[D] {nom} : {chemin.name} (sha256 {h(chemin)})")
    t = chemin.read_text(encoding="utf-8")
    p = prereg.problemes(chemin)
    verifier(p == [], f"prereg.problemes = {p!r}")
    for cle, attendu in (("EMPREINTE_MODULE_CITEE", MODULE), ("EMPREINTE_TESTS_CITEE", TESTS)):
        rx = re.compile(motifs[cle])
        trouves = rx.findall(t)
        verifier(trouves == [attendu], f"garde 1, {cle} : findall = {[x[:12] for x in trouves]} ; search = "
                 f"{rx.search(t).group(1)[:12] if rx.search(t) else None}")
    cl = prereg.sections(t)["Contre-lecture"]
    ent = list(prereg.ENTREE.finditer(cl))
    nums = [int(e.group(1)) for e in ent]
    verifier(nums == list(range(1, entrees_attendues + 1)), f"entrées « Contre-lecture » numérotées : {nums}")
    comptes = []
    for k, e in enumerate(ent):
        fin = ent[k + 1].start() if k + 1 < len(ent) else len(cl)
        comptes.append(len(set(HEX.findall(cl[e.start():fin]))))
    verifier(all(c >= 2 for c in comptes), f"empreintes distinctes par entrée : {comptes}")
    verifier(cl.lstrip().startswith("- **Contre-lecture 1**"), "aucun texte avant l'entrée 1 dans la section")
    restes = [m for m in ("<<", "À REMPLIR", "<verdict", "<empreinte", "<A>", "<B>") if m in t]
    print(f"  info  marqueurs restants (<<, À REMPLIR, <verdict, <empreinte, <A>, <B>) : {restes}")
    return p, restes


def main(argv):
    copies, artefacts, rapport_vc1, depot = map(Path, argv[1:5])
    print("[A] empreintes des copies")
    for nom, e in ATTENDU.items():
        verifier(h(copies / nom) == e, f"{nom} = {e[:12]}…")
    verifier(h(rapport_vc1) == RAPPORT_VC1, f"rapport VC1 = {RAPPORT_VC1[:12]}…")
    c1 = (copies / "P3-addendum2-audit-verdict-v1-candidat1.md").read_text(encoding="utf-8")
    c2 = (copies / "P3-addendum2-audit-verdict-v1-candidat2.md").read_text(encoding="utf-8")
    ligne = (copies / "ligne-candidat2-addendum2-v1.md").read_text(encoding="utf-8")
    plan = json.loads((copies / "plan-versement-addendum2-v2.json").read_text(encoding="utf-8"))

    print("[B] mots exacts du rapport (espaces normalisés) : corrections VC1-01 à VC1-05 appliquées au candidat 1")
    cors = corrections_vc1(rapport_vc1.read_text(encoding="utf-8"))
    for cid, a, n in cors:
        print(f"  info  {cid} : ancien {('« ' + norm(a)[:60] + '… »') if a else '(ajout)'} → nouveau « {norm(n)[:60]}… »")
    t = norm(c1)
    for cid, a, n in cors:
        if a is None:
            continue
        verifier(t.count(norm(a)) == 1, f"{cid} : ancien texte trouvé une fois dans le candidat 1 normalisé")
        t = t.replace(norm(a), norm(n))
    ajout = [n for cid, a, n in cors if a is None][0]
    verifier("<empreinte de ce rapport>" in ajout, "entrée 6 du rapport : marqueur « <empreinte de ce rapport> »")
    ajout = ajout.replace("<empreinte de ce rapport>", RAPPORT_VC1)
    t = t + " " + norm(ajout)
    t = t.replace(norm(ANCRE), norm(ligne) + " " + norm(ANCRE))
    verifier(t == norm(c2), "candidat 1 + corrections du rapport + élément « Candidat 2 » = candidat 2 (espaces normalisés)")
    fin_c1 = norm(c1)
    verifier(norm(c2).replace(norm(ligne) + " ", "", 1) != fin_c1, "témoin : le candidat 2 diffère bien du candidat 1")
    blocs = [(op, a1, a2, b1, b2) for op, a1, a2, b1, b2 in
             difflib.SequenceMatcher(None, c1.splitlines(True), c2.splitlines(True), autojunk=False).get_opcodes()
             if op != "equal"]
    print(f"  info  blocs changés (lignes, base 1) : {[(op, f'{a1+1}-{a2}', f'{b1+1}-{b2}') for op, a1, a2, b1, b2 in blocs]}")

    print("[C] empreintes citées aux lignes changées → sources du plan")
    par_sha = {}
    for p in plan:
        par_sha.setdefault(p["sha256"], []).append(p)
    l2 = c2.splitlines(True)
    for op, a1, a2, b1, b2 in blocs:
        bloc = "".join(l2[b1:b2])
        for m in HEX.finditer(bloc):
            e = m.group(0)
            avant = bloc[:m.start()]
            chemins = re.findall(r"`((?:prereg|docs)/[^`]+)`", avant)
            dernier_hex = avant.rfind(HEX.findall(avant)[-1]) if HEX.findall(avant) else -1
            chemin_cite = None
            for c in re.finditer(r"`((?:prereg|docs)/[^`]+)`", avant):
                if c.start() > dernier_hex:
                    chemin_cite = c.group(1)
            pieces = par_sha.get(e, [])
            if not pieces:
                verifier(False, f"l. {b1 + 1 + bloc[:m.start()].count(chr(10))} : {e[:12]}… sans pièce dans le plan")
                continue
            for p in pieces:
                reel = h(p["source"])
                ok_chemin = chemin_cite is None or chemin_cite == p["destination"]
                verifier(reel == e and ok_chemin,
                         f"l. {b1 + 1 + bloc[:m.start()].count(chr(10))} : {e[:12]}… = sha256({Path(p['source']).relative_to(Path(p['source']).parents[1]) if len(Path(p['source']).parents) > 1 else p['source']}) ; "
                         f"chemin cité {chemin_cite or '(aucun)'}{' = destination' if chemin_cite else ''}")

    print("[D] problemes, garde 1, entrées « Contre-lecture »")
    motifs = regex_garde1((copies / "audit_verdict_p3_v1.py").read_text(encoding="utf-8"))
    print(f"  info  motifs lus par ast : {motifs}")
    controles_texte("candidat 2", copies / "P3-addendum2-audit-verdict-v1-candidat2.md", motifs, 6)
    e7 = (artefacts / "entree7-fictive.md").read_text(encoding="utf-8")
    f7 = artefacts / "candidat2-plus-entree7-fictive.md"
    f7.write_text(c2 + e7, encoding="utf-8")
    controles_texte("candidat 2 + entrée 7 (empreintes fictives)", f7, motifs, 7)
    e7c = (artefacts / "entree7-chevrons.md").read_text(encoding="utf-8")
    f7c = artefacts / "candidat2-plus-entree7-chevrons-laisses.md"
    f7c.write_text(c2 + e7c, encoding="utf-8")
    print("  info  artefact : entrée 7 aux chevrons non remplis (le validateur doit-il l'arrêter ?)")
    p, restes = controles_texte("candidat 2 + entrée 7 (chevrons laissés)", f7c, motifs, 7)
    print(f"  info  => chevrons simples non vus par prereg.problemes : {p == [] and bool(restes)}")

    print("[E] plan de versement")
    dests = [p["destination"] for p in plan]
    verifier(len(dests) == len(set(dests)), f"{len(plan)} lignes ; destinations uniques")
    for p in plan:
        src, d, e = p["source"], p["destination"], p["sha256"]
        ok = Path(src).is_file() and h(src) == e
        sous = d.startswith(("prereg/", "docs/")) and ".." not in Path(d).parts and not d.startswith("/")
        absent = not os.path.lexists(depot / d)
        verifier(ok and sous and absent, f"{d} : source {'= ' + e[:12] if ok else 'ÉCART'} ; "
                 f"{'sous prereg/ ou docs/' if sous else 'HORS'} ; {'absente du dépôt' if absent else 'EXISTE DÉJÀ'}")
    shas = [p["sha256"] for p in plan]
    doublons = {s for s in shas if shas.count(s) > 1}
    print(f"  info  empreintes versées deux fois : {sorted(x[:12] for x in doublons)}")
    tdocs = [p for p in plan if p["destination"].startswith("docs/procedures/P3-addendum2-v1/")]
    for p in tdocs:
        print(f"  info  docs/procedures : {p['destination']} ← {p['sha256'][:12]}")
    verifier(any(p["destination"] == motifs["CHEMIN_TESTS"] and p["sha256"] == TESTS for p in tdocs),
             f"tests versés à CHEMIN_TESTS du module ({motifs['CHEMIN_TESTS']}) = tests v4 cités en tête ({TESTS[:12]})")
    verifier(any(p["destination"] == motifs["CHEMIN_MODULE"] and p["sha256"] == MODULE for p in tdocs),
             f"module versé à CHEMIN_MODULE ({motifs['CHEMIN_MODULE']}) = module cité en tête ({MODULE[:12]})")
    verifier(not os.path.lexists(depot / motifs["PREREG_ADDENDUM2"]),
             f"PREREG_ADDENDUM2 ({motifs['PREREG_ADDENDUM2']}) absent du dépôt (naîtra au scellement)")

    print("[F] chemins prereg/… et docs/… cités par le candidat 2")
    par_dest = {p["destination"]: p for p in plan}
    vus = {}
    for m in re.finditer(r"(?<![\w/.…-])((?:prereg|docs)/[A-Za-z0-9_./-]+)", c2):
        c = m.group(1).rstrip(".")
        suite = c2[m.end():m.end() + 260]
        prochain = re.search(r"(?<![\w/.…-])(?:prereg|docs|runs|diag|donnees|src|registres|tests)/", suite)
        fen = suite[:prochain.start()] if prochain else suite
        e = HEX.search(fen)
        ligne_no = c2[:m.start()].count("\n") + 1
        vus.setdefault(c, []).append((ligne_no, e.group(0) if e else None))
    for c, occ in sorted(vus.items()):
        lignes = [o[0] for o in occ]
        cites = sorted({o[1] for o in occ if o[1]})
        if c in par_dest:
            ok = all(x == par_dest[c]["sha256"] for x in cites)
            verifier(ok, f"{c} (l. {lignes}) : pièce du plan {par_dest[c]['sha256'][:12]}"
                     f"{'' if not cites else ' ; cité ' + ', '.join(x[:12] for x in cites)}")
        elif os.path.lexists(depot / c):
            print(f"  ok    {c} (l. {lignes}) : existe au dépôt{'' if not cites else ' ; empreinte citée ' + ', '.join(x[:12] for x in cites) + ' (contenu non lu)'}")
        else:
            print(f"  ABSENT {c} (l. {lignes}) : ni dans le plan, ni au dépôt"
                  f"{'' if not cites else ' ; empreinte citée ' + ', '.join(x[:12] for x in cites)}")
    print("[F] témoin : chemins cités par l'entrée 7 prévue")
    for m in re.finditer(r"`((?:prereg|docs)/[^`]+)`", e7):
        c = m.group(1)
        print(f"  info  {c} : plan {'oui' if c in par_dest else 'non'} ; dépôt {'existe' if os.path.lexists(depot / c) else 'absent'}")

    print(f"bilan : {len(ECHECS)} écart(s)")
    for x in ECHECS:
        print("  - " + x)
    return 1 if ECHECS else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
